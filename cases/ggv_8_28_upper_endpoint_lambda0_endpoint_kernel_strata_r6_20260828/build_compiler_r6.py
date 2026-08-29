#!/usr/bin/env python3
"""Apply exact ambient-reducer/qideal guards to the frozen r2 compiler."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


R2_COMPILER_SHA256 = "53ad2aa298b499d83c593171fb3da9c1dce39bfe7f924bf461db4887a8a6f578"
EXPECTED_R6_COMPILER_SHA256 = "a5587996f3d9de7049fe5de790d9bd16a53fa389732016bc4642e2c02a7d0d11"
OLD = '''        "ideal BRANCH_IDEAL=BRANCH_FACTOR;",
        "qring r=std(BRANCH_IDEAL);",
        'print("BRANCH_RELATION_ZERO="+string(BRANCH_FACTOR==0));',
        'if(BRANCH_FACTOR!=0){ print("FATAL_QUOTIENT_RELATION"); quit; }',
'''
NEW = '''        "ideal BRANCH_IDEAL=BRANCH_FACTOR;",
        "ideal BRANCH_SB=std(BRANCH_IDEAL);",
        "poly BRANCH_REMAINDER=reduce(BRANCH_FACTOR,BRANCH_SB);",
        'print("AMBIENT_BRANCH_REDUCER_ZERO="+string(BRANCH_REMAINDER==0));',
        'if(BRANCH_REMAINDER!=0){ print("FATAL_AMBIENT_BRANCH_REDUCER"); quit; }',
        "qring r=BRANCH_SB;",
        "ideal QUOTIENT_DEFINING_IDEAL=ideal(basering);",
        'write("'+label+'_QUOTIENT_DEFINING_IDEAL.txt",string(QUOTIENT_DEFINING_IDEAL));',
        'print("QUOTIENT_DEFINING_IDEAL_NONEMPTY="+string(size(QUOTIENT_DEFINING_IDEAL)>0));',
        'if(size(QUOTIENT_DEFINING_IDEAL)==0){ print("FATAL_QUOTIENT_IDEAL_EMPTY"); quit; }',
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
    if EXPECTED_R6_COMPILER_SHA256 != "TO_BE_FROZEN" and actual != EXPECTED_R6_COMPILER_SHA256:
        raise SystemExit(f"R6_COMPILER_HASH_DISAGREEMENT:{actual}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result)
    print(f"R2_COMPILER_SHA256={R2_COMPILER_SHA256}")
    print(f"R6_COMPILER_SHA256={actual}")
    print("R6_COMPILER_AMBIENT_QIDEAL_GUARD_PASS")


if __name__ == "__main__":
    main()
