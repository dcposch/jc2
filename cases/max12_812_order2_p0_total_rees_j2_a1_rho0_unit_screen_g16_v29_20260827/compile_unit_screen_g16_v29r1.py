#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
V1 = HERE / "compile_unit_screen_g16_v29.py"
V1_SHA = "bdce64b98449195ad1fe16a09ce0f23b36560d03a6a4559c5e36ab27cd538f29"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if digest(V1) != V1_SHA:
        raise RuntimeError("frozen V29 V1 compiler hash")
    spec = importlib.util.spec_from_file_location("v29_v1_frozen_for_r1", V1)
    if spec is None or spec.loader is None:
        raise RuntimeError("V29 V1 import")
    v1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v1)
    manifest = json.loads(v1.V28_RESULT.read_text())
    names = {f"Tg16_{row}_q.poly" for row in range(1, 8)}
    if {Path(value).name for value in manifest.get("coefficient_paths", {}).values()} != names:
        raise RuntimeError("V28 path-name census")

    original_path = v1.Path
    remapped = []

    def bundled_path(value):
        path = original_path(value)
        if path.name in names and path.is_absolute() and path.parent.name == "compiled":
            candidate = v1.V28 / path.name
            if not candidate.is_file():
                raise RuntimeError(("missing bundled V28 coefficient", candidate))
            remapped.append(path.name)
            return candidate
        return path

    v1.Path = bundled_path
    v1.main()
    if sorted(remapped) != sorted(names):
        raise RuntimeError(("R1 remap census", remapped))
    print("V29_R1_BUNDLED_REMAPS=7")


if __name__ == "__main__":
    main()

