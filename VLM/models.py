from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelPreset:
    name: str
    slug: str
    provider: str
    family: str
    open_source: bool
    notes: str = ""


# Presets are convenience aliases. If a model is not listed, users can still pass
# a raw OpenRouter slug directly to the CLI.
MODEL_PRESETS: dict[str, ModelPreset] = {
    "llama-3.2-vision": ModelPreset(
        name="llama-3.2-vision",
        slug="meta-llama/llama-3.2-90b-vision-instruct",
        provider="Meta",
        family="Llama 3.2 Vision",
        open_source=True,
        notes="Alias to the 90B Vision Instruct variant.",
    ),
    "gpt-4o": ModelPreset(
        name="gpt-4o",
        slug="openai/gpt-4o",
        provider="OpenAI",
        family="GPT-4o",
        open_source=False,
        notes="Strong general multimodal baseline.",
    ),
    "qwen2.5-vl-72b": ModelPreset(
        name="qwen2.5-vl-72b",
        slug="qwen/qwen2.5-vl-72b-instruct",
        provider="Qwen",
        family="Qwen2.5-VL",
        open_source=True,
        notes="Open-source VLM option.",
    ),
    "gemma-3": ModelPreset(
        name="gemma-3",
        slug="google/gemma-3-27b-it",
        provider="Google",
        family="Gemma 3",
        open_source=True,
        notes="Alias to Gemma 3 27B IT.",
    ),

    "claude-3.5-sonnet": ModelPreset(
        name="claude-3.5-sonnet",
        slug="anthropic/claude-3.5-sonnet",
        provider="Anthropic",
        family="Claude 3.5",
        open_source=False,
        notes="Closed-source multimodal option.",
    ),
}


def resolve_model_slug(model_or_preset: str) -> str:
    key = model_or_preset.strip()
    preset = MODEL_PRESETS.get(key)
    return preset.slug if preset else key


def list_model_presets() -> list[ModelPreset]:
    return [MODEL_PRESETS[k] for k in sorted(MODEL_PRESETS)]
