#!/usr/bin/env python3
"""Pinned adapter licensing order 16384 in the frozen contact generator."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_912_order3_nu_q8_contact_hensel_aws_20260825/generate.py"
BASE_SHA256 = "77ab6350846c86f969033e8cd16dc180c500d6100d810fe2e7b8ddc8b38cd84c"
OLD = "choices=(64, 256, 1024, 2048, 4096, 8192)"
NEW = "choices=(64, 256, 1024, 2048, 4096, 8192, 16384)"


def main() -> None:
    source = BASE.read_bytes()
    if sha256(source).hexdigest() != BASE_SHA256:
        raise RuntimeError("base generator hash")
    text = source.decode("utf-8")
    if text.count(OLD) != 1 or NEW in text:
        raise RuntimeError("order-choice patch anchor")
    text = text.replace(OLD, NEW)
    namespace = {
        "__name__": "__main__",
        "__file__": str(BASE),
        "__package__": None,
    }
    exec(compile(text, str(BASE), "exec"), namespace)


if __name__ == "__main__":
    main()
