#!/usr/bin/env python3
"""AWS-only exact-Q verifier compiler for a reconstructed plane candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import platform
from fractions import Fraction


EXPECTED_SOURCE = "5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47"


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
    parser.add_argument("candidate_json", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()
    require_aws()

    raw = args.source.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SOURCE:
        raise RuntimeError(f"source hash mismatch: {actual}")
    payload = json.loads(args.candidate_json.read_text(encoding="utf-8"))
    if payload.get("schema") != 1:
        raise RuntimeError("unknown candidate schema")
    plane = payload["plane_polynomial"]
    residual = payload["residual_polynomial"]
    if not isinstance(plane, str) or not isinstance(residual, str):
        raise RuntimeError("candidate polynomials are not strings")

    source_coefficients = {
        tuple(int(value) for value in key.split(",")): Fraction(text)
        for key, text in payload["coefficients"].items()
    }
    residual_coefficients: dict[tuple[int, int], Fraction] = {}
    for (s_power, t_power), coefficient in source_coefficients.items():
        if s_power % 2 or (t_power + 3 * (s_power // 2)) % 8:
            raise RuntimeError("candidate contains a non-invariant monomial")
        q_power = s_power // 2
        v_power = (t_power + 3 * q_power) // 8
        residual_coefficients[(q_power, v_power)] = coefficient

    def fraction_text(value: Fraction) -> str:
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"

    def one_variable_polynomial(entries: list[tuple[int, Fraction]], variable: str) -> str:
        pieces: list[str] = []
        for power, coefficient in sorted(entries, reverse=True):
            numerator = coefficient.numerator
            absolute = Fraction(abs(numerator), coefficient.denominator)
            coefficient_part = fraction_text(absolute)
            if power == 0:
                term = coefficient_part
            else:
                variable_part = variable if power == 1 else f"{variable}^{power}"
                term = variable_part if absolute == 1 else f"{coefficient_part}*{variable_part}"
            prefix = "-" if numerator < 0 else ("+" if pieces else "")
            pieces.append(prefix + term)
        return "".join(pieces)

    left = one_variable_polynomial(
        [(v_power, coefficient) for (q_power, v_power), coefficient in residual_coefficients.items() if q_power == 0],
        "v",
    )
    top_h = one_variable_polynomial(
        [(q_power - 1, coefficient) for (q_power, v_power), coefficient in residual_coefficients.items() if v_power == 3],
        "q",
    )

    text = raw.decode("utf-8")
    text = replace_once(
        text,
        'LIB "elim.lib";\n',
        'LIB "elim.lib";\nLIB "modstd.lib";\nLIB "moddiq.lib";\n',
    )
    text = replace_once(text, "ideal Gtail=std(Itail);", "ideal Gtail=modStd(Itail);")
    text = replace_once(text, "ideal Gcoef=std(Icoef);", "ideal Gcoef=modStd(Icoef);")
    marker = "list SS=sat(Itail,ideal(r7));"
    if text.count(marker) != 1:
        raise RuntimeError("missing unique saturation marker")
    text = text.split(marker, 1)[0]
    text += f'''\nlist SS=modSat(Itail,ideal(r7));
ideal J=modStd(SS[1]);
print("EXACT_SOURCE_SAT_UNIT="+string(reduce(1,J)==0));
print("EXACT_SOURCE_SAT_DIM="+string(dim(J)));
poly FCAND={plane};
int member=(reduce(FCAND,J)==0);
print("EXACT_CANDIDATE_MEMBER="+string(member));
list FFC=factorize(FCAND,1);
print("EXACT_PLANE_FACTOR_COUNT="+string(size(FFC[1])));
if ((reduce(1,J)==0) || (dim(J)!=1) || (member!=1) || (size(FFC[1])!=1))
{{
  print("EXACT_CANDIDATE=FAIL");
  quit;
}}

ring Q=0,(q,v),dp;
poly P={residual};
list FFP=factorize(P,1);
print("EXACT_RESIDUAL_FACTOR_COUNT="+string(size(FFP[1])));
ideal ST=P,diff(P,q),diff(P,v);
list SST=sat(ST,ideal(q*v));
ideal N=std(SST[1]);
print("EXACT_TORUS_SING_DIM="+string(dim(N)));
if (dim(N)==0)
{{
  print("EXACT_TORUS_SING_VDIM="+string(vdim(N)));
}}
poly Pqq=diff(diff(P,q),q);
poly Pqv=diff(diff(P,q),v);
poly Pvv=diff(diff(P,v),v);
poly Hess=Pqq*Pvv-Pqv^2;
ideal NH=std(N,ideal(Hess));
print("EXACT_HESSIAN_UNIT="+string(reduce(1,NH)==0));

poly Left={left};
poly LeftGCD=gcd(Left,diff(Left,v));
print("EXACT_LEFT_FACE_SQUAREFREE="+string(deg(LeftGCD)==0));
poly Htop={top_h};
poly TopGCD=gcd(Htop,diff(Htop,q));
print("EXACT_TOP_FACE_SQUAREFREE="+string(deg(TopGCD)==0));
print("EXACT_LEFT_FACE_BEGIN"); print(Left); print("EXACT_LEFT_FACE_END");
print("EXACT_TOP_H_BEGIN"); print(Htop); print("EXACT_TOP_H_END");
if ((size(FFP[1])==1) && (dim(N)==0) && (vdim(N)==3)
    && (reduce(1,NH)==0) && (deg(LeftGCD)==0) && (deg(TopGCD)==0))
{{
  print("EXACT_NODE_BOUNDARY_CERTIFICATE=PASS");
}}
else
{{
  print("EXACT_NODE_BOUNDARY_CERTIFICATE=FAIL");
}}
print("EXACT_CANDIDATE=PASS_RELATION_AND_GEOMETRY");
quit;
'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"source_sha256={actual}")
    print(f"candidate_sha256={hashlib.sha256(args.candidate_json.read_bytes()).hexdigest()}")
    print(f"output_sha256={hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
