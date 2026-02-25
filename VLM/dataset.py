from __future__ import annotations

import base64
import hashlib
import json
import mimetypes
import struct
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator, Literal


ImageEncoding = Literal["path", "bytes", "base64", "data_url"]


@dataclass(frozen=True)
class DrawingSample:
    sample_id: str
    drawing_path: str
    model_path: str | None
    file_name: str
    stem: str
    extension: str
    mime_type: str
    size_bytes: int
    width: int | None
    height: int | None
    sha256: str


@dataclass(frozen=True)
class ImagePayload:
    encoding: ImageEncoding
    mime_type: str
    data: str | bytes


class CADDrawingDataset:
    """
    Loader for `data/drawings` PNG/JPEG files with paired `data/models/*.py` lookup.

    The loader returns metadata-only `DrawingSample` records first, then exposes
    explicit methods to materialize image payloads in portable encodings that work
    across most VLM APIs (raw bytes, base64, or data URL).
    """

    def __init__(
        self,
        repo_root: str | Path = ".",
        drawings_dir: str | Path = "data/drawings",
        models_dir: str | Path = "data/models",
    ) -> None:
        self.repo_root = Path(repo_root).resolve()
        self.drawings_dir = (self.repo_root / drawings_dir).resolve()
        self.models_dir = (self.repo_root / models_dir).resolve()

        if not self.drawings_dir.exists():
            raise FileNotFoundError(f"Drawings directory not found: {self.drawings_dir}")

    def iter_samples(self) -> Iterator[DrawingSample]:
        for image_path in sorted(self.drawings_dir.iterdir()):
            if not image_path.is_file():
                continue
            mime_type = mimetypes.guess_type(image_path.name)[0] or "application/octet-stream"
            if not mime_type.startswith("image/"):
                continue
            yield self._build_sample(image_path)

    def list_samples(self) -> list[DrawingSample]:
        return list(self.iter_samples())

    def get_sample(self, sample_id: str) -> DrawingSample:
        sample_map = {sample.sample_id: sample for sample in self.iter_samples()}
        try:
            return sample_map[sample_id]
        except KeyError as exc:
            raise KeyError(f"Sample not found: {sample_id}") from exc

    def get_image_payload(
        self,
        sample: DrawingSample,
        encoding: ImageEncoding = "data_url",
    ) -> ImagePayload:
        path = Path(sample.drawing_path)
        if encoding == "path":
            return ImagePayload(encoding=encoding, mime_type=sample.mime_type, data=str(path))

        raw = path.read_bytes()
        if encoding == "bytes":
            return ImagePayload(encoding=encoding, mime_type=sample.mime_type, data=raw)

        b64 = base64.b64encode(raw).decode("ascii")
        if encoding == "base64":
            return ImagePayload(encoding=encoding, mime_type=sample.mime_type, data=b64)

        if encoding == "data_url":
            return ImagePayload(
                encoding=encoding,
                mime_type=sample.mime_type,
                data=f"data:{sample.mime_type};base64,{b64}",
            )

        raise ValueError(f"Unsupported encoding: {encoding}")

    def build_openai_vision_content(
        self,
        sample: DrawingSample,
        prompt: str,
        image_encoding: Literal["data_url", "path"] = "data_url",
        image_detail: str = "high",
    ) -> list[dict]:
        """
        Returns content array for OpenAI-compatible chat APIs (including OpenRouter).

        Default `data_url` is the most portable because it avoids local file path access
        assumptions on the API side. `path` is provided for local engines/tools.
        """

        if image_encoding not in {"data_url", "path"}:
            raise ValueError("OpenAI/OpenRouter content only supports 'data_url' or 'path' here.")

        payload = self.get_image_payload(sample, encoding=image_encoding)
        image_url = str(payload.data)

        return [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": image_detail,
                },
            },
        ]

    def export_manifest_jsonl(self, output_path: str | Path) -> int:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        count = 0
        with output_path.open("w", encoding="utf-8") as f:
            for sample in self.iter_samples():
                f.write(json.dumps(asdict(sample), ensure_ascii=True) + "\n")
                count += 1
        return count

    def _build_sample(self, image_path: Path) -> DrawingSample:
        data = image_path.read_bytes()
        width, height = _image_size_from_bytes(data, image_path.suffix.lower())
        stem = image_path.stem
        model_path = self.models_dir / f"{stem}.py"
        return DrawingSample(
            sample_id=stem,
            drawing_path=str(image_path),
            model_path=str(model_path) if model_path.exists() else None,
            file_name=image_path.name,
            stem=stem,
            extension=image_path.suffix.lower(),
            mime_type=mimetypes.guess_type(image_path.name)[0] or "application/octet-stream",
            size_bytes=len(data),
            width=width,
            height=height,
            sha256=hashlib.sha256(data).hexdigest(),
        )


def _image_size_from_bytes(data: bytes, extension: str) -> tuple[int | None, int | None]:
    if extension == ".png":
        return _png_size(data)
    if extension in {".jpg", ".jpeg"}:
        return _jpeg_size(data)
    return (None, None)


def _png_size(data: bytes) -> tuple[int | None, int | None]:
    # PNG header is fixed; width/height are the first 8 bytes of IHDR payload.
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return (None, None)
    if data[12:16] != b"IHDR":
        return (None, None)
    width, height = struct.unpack(">II", data[16:24])
    return (int(width), int(height))


def _jpeg_size(data: bytes) -> tuple[int | None, int | None]:
    # Minimal JPEG SOF parser for dimensions; enough for dataset metadata.
    if len(data) < 4 or data[0:2] != b"\xff\xd8":
        return (None, None)
    i = 2
    sof_markers = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        i += 2
        if marker in {0xD8, 0xD9}:
            continue
        if marker == 0xDA:
            break
        if i + 2 > len(data):
            break
        seg_len = struct.unpack(">H", data[i : i + 2])[0]
        if seg_len < 2 or i + seg_len > len(data):
            break
        if marker in sof_markers and seg_len >= 7:
            # precision(1), height(2), width(2), components(1)
            height, width = struct.unpack(">HH", data[i + 3 : i + 7])
            return (int(width), int(height))
        i += seg_len
    return (None, None)


def samples_to_dicts(samples: Iterable[DrawingSample]) -> list[dict]:
    return [asdict(sample) for sample in samples]
