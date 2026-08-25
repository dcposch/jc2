#!/usr/bin/env python3
"""Hash-anchored nonmutating syntax successor for V1 exceptional compiler."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
V1 = HERE / "compile_exceptional.py"
EXPECTED_V1 = "8f0d991e569df93f3c94d4b5a1e51a85e436b170792245a99ea98b6877277499"
OLD = b"        'print(\"START_MINASS_GTZ\");',\n    ]\n    if chart == \"global\":"
NEW = b"        'print(\"START_MINASS_GTZ\");',\n    ])\n    if chart == \"global\":"


def main() -> None:
    source = V1.read_bytes()
    got = sha256(source).hexdigest()
    if got != EXPECTED_V1:
        raise SystemExit(f"REFUSE_V1_HASH_MISMATCH:{got}")
    if source.count(OLD) != 1:
        raise SystemExit("REFUSE_PATCH_ANCHOR_COUNT")
    repaired = source.replace(OLD, NEW)
    namespace = {
        "__name__": "d1_weighted_infinity_exceptional_v2_body",
        "__file__": str(V1),
        "__package__": None,
    }
    exec(compile(repaired, str(V1) + "[V2_ONE_TOKEN_PATCH]", "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()

