import json
import os
from typing import Dict, Any

_ABI_DIR = os.path.join(os.path.dirname(__file__), "abis")

_FILEMAP = {
    "router":      "Router.json",
    "wrapper":  "wrapperContract.json", 
    "erc20Permit":           "erc20Permit.json",
    "curve":           "curve.json",
}

def _load_json(path: str) -> Any:
    if not os.path.exists(path):
        raise FileNotFoundError(f"ABI file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_default_abis() -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for key, fname in _FILEMAP.items():
        out[key] = _load_json(os.path.join(_ABI_DIR, fname))
    return out
