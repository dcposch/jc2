#!/usr/bin/env python3
"""AWS-only compiler for a corrected-V2 mod-32003 toric plane witness."""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import platform


EXPECTED = "5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47"


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"non-unique source marker: {old!r}")
    return text.replace(old, new, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()

    vendor = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor_text = vendor.read_text(encoding="utf-8").strip() if vendor.exists() else ""
    if platform.system() != "Linux" or vendor_text != "Amazon EC2":
        raise RuntimeError("AWS EC2 only")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing registered lane tag")

    raw = args.source.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED:
        raise RuntimeError(f"source hash mismatch: {actual}")
    text = raw.decode("utf-8")
    text = replace_once(
        text,
        "ring R=0,(a0,a1,a2,a3,a4,a5,a6),dp;",
        "ring R=32003,(a0,a1,a2,a3,a4,a5,a6),(dp(5),dp(2));",
    )
    marker = "list SS=sat(Itail,ideal(r7));"
    if text.count(marker) != 1:
        raise RuntimeError("missing unique saturation marker")
    text = text.split(marker, 1)[0]
    text += r'''
list SS=sat(Itail,ideal(r7));
ideal J=std(SS[1]);
print("MOD32003_SAT_UNIT="+string(reduce(1,J)==0));
print("MOD32003_SAT_DIM="+string(dim(J)));
ideal EP=eliminate(J,a0*a1*a2*a3*a4);
EP=std(EP);
print("MOD32003_PLANE_SIZE="+string(size(EP)));
print("MOD32003_PLANE_BEGIN");
print(EP);
print("MOD32003_PLANE_END");
if (size(EP)!=1)
{
  print("MOD32003_PLANE=FAIL_NONPRINCIPAL");
  quit;
}
list FF=factorize(EP[1],1);
print("MOD32003_FACTOR_COUNT="+string(size(FF[1])));
print("MOD32003_FACTORIZATION_BEGIN");
print(FF);
print("MOD32003_FACTORIZATION_END");

poly F=EP[1];
ideal NT=F,diff(F,a5),diff(F,a6);
list NST=sat(NT,ideal(a5*a6));
ideal N=std(NST[1]);
int torus_nonsingular=(reduce(1,N)==0);
print("MOD32003_TORUS_NONSINGULAR="+string(torus_nonsingular));
if (torus_nonsingular==0)
{
  print("MOD32003_NONDEGENERACY=FAIL_INTERIOR");
  quit;
}
print("MOD32003_PLANE_AND_TORUS=PASS");
quit;
'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"source_sha256={actual}")
    print(f"output_sha256={hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
