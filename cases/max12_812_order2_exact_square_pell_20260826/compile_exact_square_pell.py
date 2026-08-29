#!/usr/bin/env python3
"""Compile the exact-square seven-tail Pell/Chebyshev classification probe.

The computational payload is deliberately AWS-only.  It constructs the first
seven negative Laurent coefficients of

    sqrt(Q) * (Q^2 + beta*Q + gamma),
    Q=z^4+p*z^2+c*z+r,

by an exact rational recurrence and asks Singular to compare their radical
with the square and Chebyshev loci predicted by hand.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PADE_PROMOTION = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md"
PADE_THEOREM = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md"
PADE_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md"
ONEPARAM_PROMOTION = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md"

EXPECTED = {
    PADE_PROMOTION: "40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94",
    PADE_THEOREM: "2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5",
    PADE_REVIEW: "73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6",
    ONEPARAM_PROMOTION: "82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f",
}

VARS = ("p", "c", "r", "beta", "gamma")
Exponent = tuple[int, int, int, int, int]
Poly = dict[Exponent, Fraction]
ZERO: Poly = {}
ONE: Poly = {(0, 0, 0, 0, 0): Fraction(1)}
PVAR: Poly = {(1, 0, 0, 0, 0): Fraction(1)}
CVAR: Poly = {(0, 1, 0, 0, 0): Fraction(1)}
RVAR: Poly = {(0, 0, 1, 0, 0): Fraction(1)}
BETA: Poly = {(0, 0, 0, 1, 0): Fraction(1)}
GAMMA: Poly = {(0, 0, 0, 0, 1): Fraction(1)}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only exact-square Pell compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only exact-square Pell compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def clean(poly: Poly) -> Poly:
    return {m: q for m, q in poly.items() if q}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return clean(out)


def scale(value: Fraction | int, poly: Poly) -> Poly:
    coefficient = Fraction(value)
    return clean({m: coefficient * q for m, q in poly.items()})


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, Fraction(0)) + lc * rc
    return clean(out)


def series_power(alpha: Fraction, maximum: int) -> list[Poly]:
    """Coefficients of (1+p*t^2+c*t^3+r*t^4)^alpha through maximum."""
    coefficients = [ZERO for _ in range(maximum + 1)]
    coefficients[0] = ONE
    terms = ((2, PVAR), (3, CVAR), (4, RVAR))
    for n in range(1, maximum + 1):
        numerator = ZERO
        for degree, variable in terms:
            if n >= degree:
                factor = (alpha + 1) * degree - n
                numerator = add(numerator, scale(factor, multiply(variable, coefficients[n - degree])))
        coefficients[n] = scale(Fraction(1, n), numerator)
    return coefficients


def integerized(poly: Poly) -> tuple[int, Poly]:
    denominator = 1
    for coefficient in poly.values():
        denominator = math.lcm(denominator, coefficient.denominator)
    return denominator, scale(denominator, poly)


def singular_text(poly: Poly) -> str:
    if not poly:
        return "0"
    ordered = sorted(poly.items(), key=lambda item: item[0], reverse=True)
    pieces: list[str] = []
    for monomial, coefficient in ordered:
        if coefficient.denominator != 1:
            fail(("nonintegral polynomial passed to Singular formatter", coefficient))
        integer = coefficient.numerator
        factors = []
        for variable, exponent in zip(VARS, monomial):
            if exponent == 1:
                factors.append(variable)
            elif exponent > 1:
                factors.append(f"{variable}^{exponent}")
        body = "*".join(factors) if factors else "1"
        magnitude = abs(integer)
        term = body if magnitude == 1 else f"{magnitude}*{body}"
        if not pieces:
            pieces.append(term if integer > 0 else f"-{term}")
        else:
            pieces.append(("+" if integer > 0 else "-") + term)
    return "".join(pieces)


def tail_equations() -> list[tuple[int, Poly]]:
    five = series_power(Fraction(5, 2), 17)
    three = series_power(Fraction(3, 2), 13)
    one = series_power(Fraction(1, 2), 9)
    equations: list[tuple[int, Poly]] = []
    for ell in range(1, 8):
        equation = add(
            five[10 + ell],
            multiply(BETA, three[6 + ell]),
            multiply(GAMMA, one[2 + ell]),
        )
        equations.append(integerized(equation))
    return equations


def emit(path: Path, characteristic: int, equations: list[tuple[int, Poly]]) -> None:
    equation_text = [singular_text(poly) for _, poly in equations]
    lines = [
        'LIB "elim.lib";',
        f"ring C={characteristic},(z,p,c,r,beta,gamma),dp;",
        "poly Q0=z^4+p*z^2+r;",
        "poly Delta=p^2-4*r;",
        "poly Delta2=Delta*Delta;",
        "poly Delta4=Delta2*Delta2;",
        "poly Delta5=Delta4*Delta;",
        "poly T=z^2+p/2;",
        "poly T2=T*T; poly T3=T2*T; poly T5=T3*T2;",
        "poly PCheb=Q0*Q0+(5/16)*Delta*Q0+(5/256)*Delta2;",
        "poly ACheb=T5-(5/16)*Delta*T3+(5/256)*Delta2*T;",
        "poly PellCheck=ACheb*ACheb-Q0*PCheb*PCheb-(1/262144)*Delta5;",
        "int pellIdentity=(PellCheck==0);",
        'print("EXACT_SQUARE_PELL_CHEBYSHEV_IDENTITY="+string(pellIdentity));',
        'if (pellIdentity!=1) { print("EXACT_SQUARE_PELL_FAIL=CHEBYSHEV_IDENTITY"); quit(81); }',
        f"ring R={characteristic},(gamma,beta,r,c,p),dp;",
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
    ]
    for ell, ((denominator, _), text) in enumerate(zip(equations, equation_text), start=1):
        lines.append(f"poly E{ell}={text};")
        lines.append(f'print("EXACT_SQUARE_PELL_E{ell}_DENOMINATOR={denominator}");')
    lines.extend(
        [
            "ideal I=E1,E2,E3,E4,E5,E6,E7;",
            "ideal Raw=std(I);",
            "poly Delta=p^2-4*r;",
            "ideal Square=std(ideal(c,Delta));",
            "ideal Chebyshev=std(ideal(c,16*beta-5*Delta,256*gamma-5*Delta^2));",
            "ideal Expected=std(intersect(Square,Chebyshev));",
            "int predictedSolutions=idealZero(I,Expected);",
            "ideal OffC=std(sat(Raw,ideal(c)));",
            "int offCUnit=(reduce(1,OffC)==0);",
            "ideal RadRaw=radical(Raw);",
            "ideal Rad=std(RadRaw);",
            "int radInExpected=idealZero(Rad,Expected);",
            "int expectedInRad=idealZero(Expected,Rad);",
            'print("EXACT_SQUARE_PELL_RAW_BEGIN"); print(Raw); print("EXACT_SQUARE_PELL_RAW_END");',
            'print("EXACT_SQUARE_PELL_RADICAL_BEGIN"); print(Rad); print("EXACT_SQUARE_PELL_RADICAL_END");',
            'print("EXACT_SQUARE_PELL_EXPECTED_BEGIN"); print(Expected); print("EXACT_SQUARE_PELL_EXPECTED_END");',
            'print("EXACT_SQUARE_PELL_RAW_DIM="+string(dim(Raw)));',
            'print("EXACT_SQUARE_PELL_RADICAL_SIZE="+string(size(Rad)));',
            'print("EXACT_SQUARE_PELL_PREDICTED_SOLUTIONS="+string(predictedSolutions));',
            'print("EXACT_SQUARE_PELL_OFF_C_UNIT="+string(offCUnit));',
            'print("EXACT_SQUARE_PELL_RAD_IN_EXPECTED="+string(radInExpected));',
            'print("EXACT_SQUARE_PELL_EXPECTED_IN_RAD="+string(expectedInRad));',
            "if (predictedSolutions*offCUnit*radInExpected*expectedInRad!=1) {",
            '  print("EXACT_SQUARE_PELL_ENDPOINT=REPAIR_OR_EXTRA_COMPONENT"); quit(82);',
            "}",
            'print("EXACT_SQUARE_PELL_ENDPOINT=PASS_SQUARE_UNION_CHEBYSHEV_REDUCED_SUPPORT");',
            'print("EXACT_SQUARE_PELL_SCOPE=SEVEN_LAURENT_TAILS_ONLY_NO_REES_TAYLOR_ORDER2_OR_JC2_VERDICT");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    equations = tail_equations()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"exact_square_pell_{label}.sing"
    emit(singular, args.characteristic, equations)
    result = {
        "status": "PASS-EXACT-SQUARE-PELL-COMPILER",
        "scope": "SEVEN_LAURENT_TAIL_CLASSIFICATION_PROBE_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "equation_denominators": [denominator for denominator, _ in equations],
        "charged_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
