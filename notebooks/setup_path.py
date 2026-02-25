"""
Import this module as the first cell of any notebook in notebooks/.
It adds the project root to sys.path so that utils, metrics, and VLM
are importable regardless of where Jupyter was launched from.
"""
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent   # .../ML/CAD
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))
