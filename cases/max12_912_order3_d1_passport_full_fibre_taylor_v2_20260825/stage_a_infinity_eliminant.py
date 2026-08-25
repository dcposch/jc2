#!/usr/bin/env python3
"""Emit a bounded exact infinity-eliminant lane for one D1 load.

The emitted Singular job keeps ``q=1/s`` in the coefficient field, fixes
``k=mu=nu=1``, and computes a lexicographic eliminant for a registered
separating linear form.  Its Newton polygon can exclude rational sections on
this one load if every root valuation is nonintegral.  It says nothing about
generic loads or any exceptional load divisor.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "compile_gate_v2.py"
LINEAR_FORM = (2, 3, 5, 7, 11, 13, 17, 19)


class InfinityEliminantFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_compiler():
    spec = importlib.util.spec_from_file_location(
        "d1_v2_infinity_compiler", COMPILER
    )
    if spec is None or spec.loader is None:
        raise InfinityEliminantFailure(str(COMPILER))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rational_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def fixed_load_row(value) -> str:
    terms = []
    for monomial, scalar in sorted(value.items(), reverse=True):
        scalar = Fraction(scalar)
        factors = []
        for index in range(8):
            exponent = monomial[index]
            if exponent == 1:
                factors.append(f"A{index}")
            elif exponent:
                factors.append(f"A{index}^{exponent}")
        s_exponent = monomial[8]
        if s_exponent:
            factors.append("(1/q)" if s_exponent == 1
                           else f"(1/q^{s_exponent})")
        # monomial[9:12] are k,mu,nu, all fixed to one in this lane.
        body = "*".join(factors)
        coefficient = rational_string(scalar)
        terms.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(terms).replace("+-", "-") or "0"


def singular_source(characteristic: int, tag: str) -> str:
    compiler = load_compiler()
    _, _, _, rows, _ = compiler.compile_all()
    coefficient_field = f"({characteristic},q)"
    variables = ",".join([f"A{i}" for i in range(8)] + ["L"])
    lines = [
        'LIB "standard.lib";',
        f"ring R={coefficient_field},({variables}),lp;",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly R{ell}={fixed_load_row(rows[ell])};")
    linear_body = "+".join(
        f"{coefficient}*A{index}"
        for index, coefficient in enumerate(LINEAR_FORM)
    )
    lines.extend([
        f"poly separating=L-({linear_body});",
        "ideal I=R1,R2,R3,R4,R5,R6,R7,R8,separating;",
        f'print("AWS_TAG={tag}");',
        f'print("CHARACTERISTIC={characteristic}");',
        'print("LOAD=k=1,mu=1,nu=1");',
        'print("BASE_PARAMETER=q=1/s;PLACE=q=0");',
        f'print("LINEAR_FORM={linear_body}");',
        'print("START_FGLM");',
        'ideal G=stdfglm(I,"slimgb");',
        'print("PASS_D1_FIXED_LOAD_FGLM");',
        'print("quotient_dimension="+string(vdim(G)));',
        "ideal E=eliminate(G,A0*A1*A2*A3*A4*A5*A6*A7);",
        "E=std(E);",
        'print("eliminant_count="+string(size(E)));',
        "if (size(E)!=1) { print(\"REFUSE_NONPRINCIPAL_ELIMINANT\"); quit; }",
        "poly e=E[1];",
        'print("eliminant_degree="+string(deg(e)));',
        'print("eliminant_leadcoef="+string(leadcoef(e)));',
        "poly derivative=diff(e,L);",
        "poly repeated=gcd(e,derivative);",
        'print("eliminant_gcd_derivative_degree="+string(deg(repeated)));',
        "matrix coefficients=coeffs(e,L);",
        "for (int row=1; row<=nrows(coefficients); row++)",
        "{",
        "  number coefficient=number(coefficients[row,1]);",
        "  if (coefficient==0)",
        "  {",
        '    print("COEFF_VAL degree="+string(row-1)+" value=INF");',
        "  }",
        "  else",
        "  {",
        "    number num=numerator(coefficient);",
        "    number den=denominator(coefficient);",
        "    int numerator_order=0;",
        "    int denominator_order=0;",
        "    while (subst(num,q,0)==0) { num=num/q; numerator_order++; }",
        "    while (subst(den,q,0)==0) { den=den/q; denominator_order++; }",
        '    print("COEFF_VAL degree="+string(row-1)+" value="'
        '+string(numerator_order-denominator_order));',
        "  }",
        "}",
        'print("ELIMINANT_BEGIN");',
        "e;",
        'print("ELIMINANT_END");',
        'print("STATUS=FIXED_LOAD_INFINITY_CERTIFICATE_CANDIDATE");',
        'print("FIREWALL=NO_GENERIC_LOAD_OR_TAYLOR_INFERENCE");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=0)
    args = parser.parse_args()
    if args.characteristic < 0 or args.characteristic == 1:
        raise InfinityEliminantFailure("invalid characteristic")
    tag = require_aws()
    print(singular_source(args.characteristic, tag), end="")


if __name__ == "__main__":
    main()
