#!/usr/bin/env python3
"""AWS-only compiler for corrected-V2 plane elimination at frozen primes."""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import platform


EXPECTED_SOURCE = "5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47"
PRIMES = (
    32003, 32009, 32027, 32029, 32051, 32057, 32059, 32063,
    32069, 32077, 32083, 32089, 32099, 32117, 32119, 32141,
    32143, 32159, 32173, 32183, 32189, 32191, 32203, 32213,
    32233, 32237, 32251, 32257, 32261, 32297, 32303, 32309,
)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one source marker, found {count}: {old!r}")
    return text.replace(old, new, 1)


def require_aws() -> None:
    vendor_path = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    if platform.system() != "Linux" or vendor != "Amazon EC2":
        raise RuntimeError("AWS EC2 only")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing registered AWS lane tag")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("prime", type=int)
    args = parser.parse_args()

    require_aws()
    if args.prime not in PRIMES:
        raise RuntimeError(f"prime {args.prime} is not frozen")
    raw = args.source.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SOURCE:
        raise RuntimeError(f"source hash mismatch: {actual}")

    text = raw.decode("utf-8")
    text = replace_once(
        text,
        "ring R=0,(a0,a1,a2,a3,a4,a5,a6),dp;",
        f"ring R={args.prime},(a0,a1,a2,a3,a4,a5,a6),(dp(5),dp(2));",
    )
    marker = "list SS=sat(Itail,ideal(r7));"
    if text.count(marker) != 1:
        raise RuntimeError("missing unique saturation marker")
    text = text.split(marker, 1)[0]
    text += f'''\nlist SS=sat(Itail,ideal(r7));
ideal J=std(SS[1]);
print("PRIME={args.prime}");
print("SAT_UNIT="+string(reduce(1,J)==0));
print("SAT_DIM="+string(dim(J)));
ideal EP=std(eliminate(J,a0*a1*a2*a3*a4));
print("PLANE_SIZE="+string(size(EP)));
print("PLANE_BEGIN");
print(EP);
print("PLANE_END");
if (size(EP)!=1)
{{
  print("PRIME_COMPLETE=FAIL_NONPRINCIPAL");
  quit;
}}
list FF=factorize(EP[1],1);
print("FACTOR_COUNT="+string(size(FF[1])));
print("PRIME_COMPLETE=PASS");
quit;
'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"prime={args.prime}")
    print(f"source_sha256={actual}")
    print(f"output_sha256={hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
