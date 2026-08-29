#!/usr/bin/env python3
"""Compile the direct seven-row K2 source/analytic equality certificate.

This compiler is AWS-only.  It reuses the frozen complete-source V1
emitter, deletes the expensive Groebner comparison, and checks the exact
unitriangular Laurent-to-Faber row identities coefficient by coefficient.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_disc_halfweight_kuranishi_20260826/compile_disc_halfweight.py"
V1_SHA = "4114c4aec72f710c138d49eb7b2d51cbbce14377b7e228526911219902ad3f9d"

Poly = dict[tuple[int, int], Fraction]  # exponents of (b,e)
Series = list[Poly]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only K2 row compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only K2 row compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    if digest(V1) != V1_SHA:
        fail(("V1 compiler hash mismatch", digest(V1), V1_SHA))
    spec = importlib.util.spec_from_file_location("disc_halfweight_v1_rows", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pclean(value: Poly) -> Poly:
    return {key: coefficient for key, coefficient in value.items() if coefficient}


def padd(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for key, coefficient in right.items():
        out[key] = out.get(key, Fraction(0)) + coefficient
    return pclean(out)


def pscale(value: Poly, scalar: Fraction) -> Poly:
    return pclean({key: scalar * coefficient for key, coefficient in value.items()})


def pmul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (bi, ei), left_coefficient in left.items():
        for (bj, ej), right_coefficient in right.items():
            key = (bi + bj, ei + ej)
            out[key] = out.get(key, Fraction(0)) + left_coefficient * right_coefficient
    return pclean(out)


ONE: Poly = {(0, 0): Fraction(1)}
BVAR: Poly = {(1, 0): Fraction(1)}
EVAR: Poly = {(0, 1): Fraction(1)}


def smul(left: Series, right: Series, cap: int) -> Series:
    out: Series = [{} for _ in range(cap + 1)]
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            if i + j <= cap:
                out[i + j] = padd(out[i + j], pmul(left_coefficient, right_coefficient))
    return out


def spow(base: Series, exponent: int, cap: int) -> Series:
    out: Series = [ONE] + [{} for _ in range(cap)]
    for _ in range(exponent):
        out = smul(out, base, cap)
    return out


def row_transform(cap: int = 7) -> dict[tuple[int, int], Poly]:
    """Return T from q^4+b*v*q^3+e*v^2*q^2=1.

    With q=A/w and v=1/w, A^-j=v^j*q^-j.  Therefore T_(ell,j)
    is the coefficient of v^(ell-j) in q^-j.
    """

    q: Series = [ONE] + [{} for _ in range(cap)]
    for n in range(1, cap + 1):
        q[n] = {}
        q4 = spow(q, 4, cap)
        q3 = spow(q, 3, cap)
        q2 = spow(q, 2, cap)
        known = q4[n]
        if n >= 1:
            known = padd(known, pmul(BVAR, q3[n - 1]))
        if n >= 2:
            known = padd(known, pmul(EVAR, q2[n - 2]))
        q[n] = pscale(known, Fraction(-1, 4))

    inv: Series = [ONE] + [{} for _ in range(cap)]
    for n in range(1, cap + 1):
        total: Poly = {}
        for j in range(1, n + 1):
            total = padd(total, pmul(q[j], inv[n - j]))
        inv[n] = pscale(total, Fraction(-1))

    transform: dict[tuple[int, int], Poly] = {}
    for j in range(1, cap + 1):
        invj = spow(inv, j, cap)
        for ell in range(j, cap + 1):
            transform[(ell, j)] = invj[ell - j]
    if any(transform[(ell, ell)] != ONE for ell in range(1, cap + 1)):
        fail("row transform is not unitriangular")
    return transform


def qtext(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def poly_text(value: Poly) -> str:
    if not value:
        return "0"
    terms: list[str] = []
    for (b_exponent, e_exponent), coefficient in sorted(
        value.items(), key=lambda item: (sum(item[0]), item[0]), reverse=True
    ):
        factors: list[str] = []
        if b_exponent == 1:
            factors.append("b")
        elif b_exponent:
            factors.append(f"b^{b_exponent}")
        if e_exponent == 1:
            factors.append("ee")
        elif e_exponent:
            factors.append(f"ee^{e_exponent}")
        body = "*".join(factors)
        if not body:
            term = qtext(coefficient)
        elif coefficient == 1:
            term = body
        elif coefficient == -1:
            term = "-" + body
        else:
            term = qtext(coefficient) + "*" + body
        terms.append(term)
    return "+".join(terms).replace("+-", "-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v1 = load_v1()
    for source, expected in v1.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen dependency mismatch", str(source), actual, expected))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_halfweight_v3_rows_p{args.characteristic}.sing"
    v1.emit(target, args.characteristic, tails)
    text = target.read_text()
    start = text.find("ideal IE=e1,e2,e3,e4,e5,e6,e7;\n")
    if start < 0:
        fail("V1 comparison start anchor missing")
    if text.count('print("DISC_HALF_ENDPOINT=PASS_SOURCE_ANALYTIC_IDEAL_EQUALITY");') != 1:
        fail("V1 endpoint anchor missing or nonunique")

    transform = row_transform()
    replacement = [
        'print("DISC_HALF_ROW_TRANSFORM_RELATION=q^4+b*v*q^3+ee*v^2*q^2-1");',
        'print("DISC_HALF_ROW_TRANSFORM_UNIT_DIAGONAL=1");',
        "int row_identity=1;",
    ]
    for ell in range(1, 8):
        summands: list[str] = []
        for j in range(1, ell + 1):
            coefficient = poly_text(transform[(ell, j)])
            if coefficient != "0":
                summands.append(f"({coefficient})*h{j}")
        predicted = "+".join(summands).replace("+-", "-") or "0"
        replacement.extend(
            [
                f"poly TP{ell}={predicted};",
                f"poly TD{ell}=16*e{ell}-TP{ell};",
                f"int TC{ell}=(TD{ell}==0);",
                f'print("DISC_HALF_ROW_IDENTITY_{ell}="+string(TC{ell}));',
                f"if (TC{ell}!=1) {{ row_identity=0; print(\"DISC_HALF_ROW_REMAINDER_{ell}\"); print(TD{ell}); }}",
            ]
        )
    replacement.extend(
        [
            'if (row_identity!=1) { print("DISC_HALF_FAIL=ROW_IDENTITY"); quit; }',
            'print("DISC_HALF_SOURCE_ANALYTIC_IDEAL_EQUALITY_BY_UNITRIANGULAR_ROWS=1");',
            'print("DISC_HALF_V3_DIRECT_ROW_CERTIFICATE=1");',
            'print("DISC_HALF_ENDPOINT=PASS_EXACT_SOURCE_ANALYTIC_ROW_EQUALITY");',
            "quit;",
            "",
        ]
    )
    text = text[:start] + "\n".join(replacement)
    target.write_text(text)

    payload = {
        "status": "PASS-DISC-HALFWEIGHT-V3-DIRECT-ROW-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "tails_sha256": digest(v1.TAILS),
        "all_tails_sha256": v1.EXPECTED_ALL_TAILS,
        "input_sha256": digest(target),
        "transform_relation": "q^4+b*v*q^3+e*v^2*q^2=1",
        "scope": "EXACT_K2_SOURCE_ANALYTIC_ROW_EQUALITY_ONLY_NO_ARC_TAYLOR_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
