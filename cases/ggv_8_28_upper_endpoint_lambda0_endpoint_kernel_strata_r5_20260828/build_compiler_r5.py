#!/usr/bin/env python3
"""Apply the exact post-qring symbol repair to the frozen r2 compiler."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


R2_COMPILER_SHA256 = "53ad2aa298b499d83c593171fb3da9c1dce39bfe7f924bf461db4887a8a6f578"
EXPECTED_R5_COMPILER_SHA256 = "575f0f34065bf06b76311a51fa71622d42d2e9a75fbb85979f79d9da97f3c06e"
OLD = '''        "qring r=std(BRANCH_IDEAL);",
        'print("BRANCH_RELATION_ZERO="+string(BRANCH_FACTOR==0));',
        'if(BRANCH_FACTOR!=0){ print("FATAL_QUOTIENT_RELATION"); quit; }',
'''
NEW = '''        "qring r=std(BRANCH_IDEAL);",
        f"poly BRANCH_FACTOR_Q={factor};",
        'print("BRANCH_RELATION_ZERO="+string(BRANCH_FACTOR_Q==0));',
        'if(BRANCH_FACTOR_Q!=0){ print("FATAL_QUOTIENT_RELATION"); quit; }',
'''


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r2-compiler", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.r2_compiler.read_text()
    if sha_text(source) != R2_COMPILER_SHA256:
        raise SystemExit("R2_COMPILER_SOURCE_DRIFT")
    if source.count(OLD) != 1:
        raise SystemExit("R2_QRING_BLOCK_DRIFT")
    result = source.replace(OLD, NEW)
    actual = sha_text(result)
    if EXPECTED_R5_COMPILER_SHA256 != "TO_BE_FROZEN" and actual != EXPECTED_R5_COMPILER_SHA256:
        raise SystemExit(f"R5_COMPILER_HASH_DISAGREEMENT:{actual}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result)
    print(f"R2_COMPILER_SHA256={R2_COMPILER_SHA256}")
    print(f"R5_COMPILER_SHA256={actual}")
    print("R5_COMPILER_QRING_SYMBOL_FIX_PASS")


if __name__ == "__main__":
    main()
