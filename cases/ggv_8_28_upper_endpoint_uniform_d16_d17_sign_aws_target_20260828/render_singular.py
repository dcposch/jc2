#!/usr/bin/env python3
"""Render one frozen sign-lower-system job for Singular."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_TARGET = HERE / "sign_branch_elimination_target.json"
EXPECTED_SCHEMA = "jc2.ggv.uniform_d16_d17.sign_lower_aws_target.v1"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1 if divisor == 2 else 2
    return True


def scalar_text(value, field, prime):
    value = Q(value)
    if field == "q":
        if value.denominator == 1:
            return str(value.numerator)
        return f"({value.numerator}/{value.denominator})"
    denominator = value.denominator % prime
    assert denominator
    return str((value.numerator % prime) * pow(denominator, -1, prime) % prime)


def gaussian_text(coefficient, field, prime):
    real, imaginary = (Q(value) for value in coefficient)
    pieces = []
    if real:
        pieces.append(scalar_text(real, field, prime))
    if imaginary:
        imag = scalar_text(imaginary, field, prime)
        pieces.append(f"({imag})*i")
    return "+".join(pieces) if pieces else "0"


def polynomial_text(equation, field, prime):
    pieces = []
    for term in equation:
        coefficient = gaussian_text(term["coefficient"], field, prime)
        monomial = "*".join(term["monomial"])
        pieces.append(coefficient if not monomial else f"({coefficient})*{monomial}")
    return "+".join(pieces) if pieces else "0"


def render(arguments):
    target = json.loads(arguments.target.read_text())
    assert target["schema"] == EXPECTED_SCHEMA
    assert target["status"] == "FROZEN_DESIGN_NOT_LAUNCHED"
    for field in ("classifier_checker_sha256", "classifier_result_sha256",
                  "producer_result_sha256", "authoritative_raw_system_sha256"):
        assert len(target["source"][field]) == 64
    assert arguments.branch in target["branch_order"]
    branch = target["branches"][arguments.branch]
    if arguments.certify and arguments.field != "q":
        raise SystemExit("--certify is exact-Q(i) only")
    if arguments.field == "mod":
        assert is_prime(arguments.prime)
        assert arguments.prime % 4 == 3, "i^2+1 must be irreducible for GF(p^2)"
    characteristic = "0" if arguments.field == "q" else str(arguments.prime)
    variables = branch["variables"]
    equations = [branch["equations"][label] for label in branch["equation_order"]]
    generators = [polynomial_text(equation, arguments.field, arguments.prime)
                  for equation in equations]
    lines = [
        f"// target_sha256={digest(arguments.target)}",
        f"// branch={arguments.branch}",
        f"// field={arguments.field}",
        f"ring R=({characteristic},i),({','.join(variables)}),{arguments.order};",
        "minpoly=i2+1;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(generators) + ";",
        f'print("TARGET_SHA256={digest(arguments.target)}");',
        f'print("BRANCH={arguments.branch}");',
        f'print("FIELD={arguments.field}");',
        f'print("PRIME={arguments.prime if arguments.field == "mod" else 0}");',
        f'print("VARIABLE_COUNT={len(variables)}");',
        f'print("GENERATOR_COUNT={len(generators)}");',
        "int started=timer;",
    ]
    if arguments.certify:
        lines.extend(["matrix TRANS;", "ideal G=liftstd(I,TRANS);"])
    else:
        lines.append("ideal G=std(I);")
    lines.extend([
        'print("STD_SECONDS="+string(timer-started));',
        'print("STD_SIZE="+string(size(G)));',
        'print("DIMENSION="+string(dim(G)));',
        "int unit_index=0;",
        "for (int gi=1; gi<=size(G); gi++)",
        "{",
        "  if ((G[gi]<>0) && (deg(G[gi])==0)) { unit_index=gi; break; }",
        "}",
        "if (unit_index==0)",
        "{",
        '  print("UNIT=0");',
        '  print("NONUNIT_OR_INCONCLUSIVE=1");',
        "}",
        "else",
        "{",
        '  print("UNIT=1");',
    ])
    if arguments.certify:
        lines.extend([
            "  poly constant=G[unit_index];",
            "  poly check=0;",
            "  for (int jj=1; jj<=size(I); jj++)",
            "  {",
            "    check=check+I[jj]*TRANS[jj,unit_index]/constant;",
            "  }",
            '  if (check==1) { print("CERTIFICATE_CHECK=PASS"); }',
            '  else { print("CERTIFICATE_CHECK=FAIL"); exit(7); }',
            '  print("CERTIFICATE_BEGIN");',
            "  for (jj=1; jj<=size(I); jj++)",
            "  {",
            "    if (TRANS[jj,unit_index]<>0)",
            "    {",
            '      print("C["+string(jj)+"]="+string(TRANS[jj,unit_index]/constant));',
            "    }",
            "  }",
            '  print("CERTIFICATE_END");',
        ])
    lines.extend(["}", "exit(0);", ""])
    arguments.output.write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--field", choices=("mod", "q"), required=True)
    parser.add_argument("--prime", type=int, default=32003)
    parser.add_argument("--order", choices=("dp", "lp"), default="dp")
    parser.add_argument("--certify", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    render(arguments)


if __name__ == "__main__":
    main()
