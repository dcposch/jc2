#!/usr/bin/env python3
"""Transcribe the pinned H table into a standalone Singular point-count job."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


P = 127
Q = P * P
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
CONTROL_EXPECTED = {
    0: (8, 7, 1),
    39: (4, 3, 1),
    71: (3, 3, 0),
    128: (2, 2, 0),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_candidate(path: Path) -> dict:
    digest = sha256(path)
    if digest != CANDIDATE_SHA256:
        raise SystemExit(f"candidate hash mismatch: {digest}")
    data = json.loads(path.read_text())
    if data.get("status") != "PASS" or data.get("prime") != P:
        raise SystemExit("candidate status/prime mismatch")
    if data.get("degree_v") != 190:
        raise SystemExit("candidate v-degree mismatch")
    if data["nonzero_support"].get("190") != [[0, 1]]:
        raise SystemExit("candidate is not monic in v")
    return data


def reference_counts(path: Path, start: int, stop: int) -> dict[int, tuple[int, int, int]]:
    data = json.loads(path.read_text())
    if data.get("candidate_sha256") != CANDIDATE_SHA256:
        raise SystemExit("reference candidate hash mismatch")
    table = {int(i): (int(t), int(s), int(g)) for i, t, s, g in data["per_w"]}
    missing = [i for i in range(start, stop) if i not in table]
    if missing:
        raise SystemExit(f"reference misses indices: {missing[:8]}")
    return {i: table[i] for i in range(start, stop)}


def emit_build_proc(name: str, support: dict, derivative_w: bool) -> None:
    print(f"proc {name}(number ww)")
    print("{")
    print("  poly out=0;")
    for vd in sorted(map(int, support)):
        for wd, coefficient in support[str(vd)]:
            wd = int(wd)
            coefficient = int(coefficient) % P
            if derivative_w:
                if wd == 0:
                    continue
                coefficient = coefficient * wd % P
                wd -= 1
            if coefficient == 0:
                continue
            wp = "1" if wd == 0 else ("ww" if wd == 1 else f"ww^{wd}")
            vp = "1" if vd == 0 else ("v" if vd == 1 else f"v^{vd}")
            print(f"  out=out+{coefficient}*({wp})*({vp});")
    print("  return(out);")
    print("}")


def w_expression(index: int) -> str:
    i = index % P
    j = index // P
    if j == 0:
        return str(i)
    if i == 0:
        return "a" if j == 1 else f"{j}*a"
    return f"{i}+a" if j == 1 else f"{i}+{j}*a"


def emit_record(index: int, expected: tuple[int, int, int]) -> None:
    total, smooth, singular = expected
    print(f"number w{index}={w_expression(index)};")
    print(f"list C{index}=countFiber(w{index});")
    print(
        f'print("RECORD|index={index}|total="+string(C{index}[1])'
        f'+"|smooth="+string(C{index}[2])+"|singular="+string(C{index}[3]));'
    )
    print(
        f"if(C{index}[1]!={total} || C{index}[2]!={smooth} || "
        f"C{index}[3]!={singular})"
    )
    print("{")
    print(f'  print("SINGULAR_COUNT_MISMATCH_INDEX_{index}");')
    print("  exit;")
    print("}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--mode", choices=("controls", "shard"), required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=0)
    parser.add_argument("--reference", type=Path)
    args = parser.parse_args()

    candidate = load_candidate(args.candidate)
    if args.mode == "controls":
        expected = CONTROL_EXPECTED
        marker = "SINGULAR_FQ2_CONTROLS_PASS"
    else:
        if not (0 <= args.start < args.stop <= Q):
            raise SystemExit("invalid shard interval")
        if args.reference is None:
            raise SystemExit("shard mode requires --reference")
        expected = reference_counts(args.reference, args.start, args.stop)
        marker = "SINGULAR_FQ2_SHARD_PASS"

    print("option(noredefine);")
    print("ring E=(127,a),(v),lp;")
    print("minpoly=a2-a+3;")
    emit_build_proc("buildH", candidate["nonzero_support"], False)
    emit_build_proc("buildHw", candidate["nonzero_support"], True)
    print("proc powMod(poly base,int exponent,ideal G)")
    print("{")
    print("  poly result=1;")
    print("  poly power=reduce(base,G);")
    print("  int e=exponent;")
    print("  int half;")
    print("  while(e>0)")
    print("  {")
    print("    half=e div 2;")
    print("    if(e-2*half==1){result=reduce(result*power,G);}")
    print("    e=half;")
    print("    if(e>0){power=reduce(power*power,G);}")
    print("  }")
    print("  return(result);")
    print("}")
    print("proc countFiber(number ww)")
    print("{")
    print("  poly h=buildH(ww);")
    print("  if(deg(h)!=190){print(\"FIBRE_DEGREE_FAILURE\");exit;}")
    print("  poly hv=diff(h,v);")
    print("  poly hw=buildHw(ww);")
    print("  ideal G=h;")
    print("  G=std(G);")
    print(f"  poly frob=powMod(v,{Q},G)-v;")
    print("  poly rationalRoots=gcd(h,frob);")
    print("  poly singularRoots=gcd(gcd(rationalRoots,hv),hw);")
    print("  int total=deg(rationalRoots);")
    print("  int singular=deg(singularRoots);")
    print("  int smooth=total-singular;")
    print("  if(total<0 || singular<0 || smooth<0){print(\"NEGATIVE_COUNT_FAILURE\");exit;}")
    print("  return(list(total,smooth,singular));")
    print("}")
    print('print("SINGULAR_FQ2_POINT_COUNT_BEGIN");')
    print(f'print("mode={args.mode}");')
    print(f'print("candidate_sha256={CANDIDATE_SHA256}");')
    print('print("field_modulus=a2-a+3");')
    for index, counts in expected.items():
        emit_record(index, counts)
    print(f'print("{marker}");')
    print("exit;")


if __name__ == "__main__":
    main()
