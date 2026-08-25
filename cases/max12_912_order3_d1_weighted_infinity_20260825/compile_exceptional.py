#!/usr/bin/env python3
"""Compile the exact D1 weighted-infinity exceptional divisor.

The script is source orchestration, but it is deliberately AWS-only because
it reconstructs the full sparse Faber rows.  Singular performs every ideal
operation; this compiler makes no component claim.
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
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = (ROOT / "cases" /
      "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
      "compile_gate_v2.py")
WEIGHTS = tuple(9 - index for index in range(8))
LOAD_WEIGHTS = (0, 6, 15, 18)  # s,k,mu,nu
CUBE = {
    7: "3*p",
    6: "3*q",
    5: "3*p^2",
    4: "6*p*q",
    3: "p^3+3*q^2",
    2: "3*p^2*q",
    1: "3*p*q^2",
    0: "q^3",
}


class ExceptionalFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_infty_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_v2():
    spec = importlib.util.spec_from_file_location("d1_infty_v2", V2)
    if spec is None or spec.loader is None:
        raise ExceptionalFailure(str(V2))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def check_weights(rows) -> dict[str, object]:
    report = {}
    for ell in range(1, 9):
        expected = 12 + ell
        counts = {}
        for monomial, coefficient in rows[ell].items():
            if not coefficient:
                continue
            if ell == 8 and not any(monomial):
                if coefficient != -1:
                    raise ExceptionalFailure(("unexpected R8 target", coefficient))
                weight = 20  # conceptual homogenizing coordinate -R
            else:
                weight = sum(monomial[index] * WEIGHTS[index]
                             for index in range(8))
                weight += sum(monomial[8 + index] * LOAD_WEIGHTS[index]
                              for index in range(4))
            counts[str(weight)] = counts.get(str(weight), 0) + 1
            if weight != expected:
                raise ExceptionalFailure(("row is not weighted homogeneous",
                                          ell, monomial, weight, expected))
        report[f"R{ell}"] = {
            "expected_weight": expected,
            "weight_histogram": counts,
        }
    return report


def exceptional_rows(rows) -> dict[int, dict[tuple[int, ...], Fraction]]:
    """Set s=1 and finite-load Rees coordinates K=M=N=R=0."""
    out = {}
    for ell in range(1, 9):
        specialized = {}
        for monomial, coefficient in rows[ell].items():
            if ell == 8 and not any(monomial):
                continue  # affine -1 becomes -R, then R=0
            if any(monomial[index] for index in (9, 10, 11)):
                continue  # K=M=N=0
            bmonomial = tuple(monomial[:8])
            specialized[bmonomial] = (
                specialized.get(bmonomial, Fraction(0)) + coefficient
            )
        out[ell] = {monomial: coefficient
                    for monomial, coefficient in specialized.items()
                    if coefficient}
    return out


def coefficient_string(value) -> str:
    terms = []
    for monomial, scalar in sorted(value.items(), reverse=True):
        factors = []
        for index, exponent in enumerate(monomial):
            if exponent == 1:
                factors.append(f"B{index}")
            elif exponent:
                factors.append(f"B{index}^{exponent}")
        if scalar.denominator == 1:
            coefficient = str(scalar.numerator)
        else:
            coefficient = f"({scalar.numerator}/{scalar.denominator})"
        body = "*".join(factors)
        terms.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(terms).replace("+-", "-") or "0"


def row_digest(value) -> str:
    canonical = [
        [list(monomial), scalar.numerator, scalar.denominator]
        for monomial, scalar in sorted(value.items())
    ]
    return sha256(json.dumps(canonical, separators=(",", ":")).encode()).hexdigest()


def singular_source(exceptional, characteristic: int, tag: str,
                    chart: str) -> str:
    coefficient = "0" if characteristic == 0 else str(characteristic)
    variables = "p,q," + ",".join(f"B{i}" for i in range(8)) + ",v"
    lines = [
        'LIB "primdec.lib";',
        'LIB "elim.lib";',
        f"ring R={coefficient},({variables}),(dp(2),dp(8),dp(1));",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly E{ell}={coefficient_string(exceptional[ell])};")
    lines.append("ideal I=E1,E2,E3,E4,E5,E6,E7,E8;")
    for index in range(8):
        lines.append(f"poly C{index}=B{index}-({CUBE[index]});")
    lines.extend([
        "ideal graph=C0,C1,C2,C3,C4,C5,C6,C7;",
        "ideal J=eliminate(graph,p*q);",
        "ideal irrelevant=B0,B1,B2,B3,B4,B5,B6,B7;",
        "list SAT=sat(I,irrelevant);",
        "ideal IS=SAT[1];",
        "ideal WRONG=E1,E2,E3,E4,E5,E6,E7,E8-1;",
        "ideal GI=std(IS);",
        "ideal GJ=std(J);",
        "ideal I_mod_J=reduce(IS,GJ);",
        "ideal WRONG_mod_J=reduce(WRONG,GJ);",
        f'print("AWS_TAG={tag}");',
        f'print("CHARACTERISTIC={characteristic}");',
        f'print("CHART={chart}");',
        'print("SCOPE=FINITE_LOAD_EXCEPTIONAL_DIVISOR_S1_KMNR_ZERO");',
        'print("SATURATED_I_DIM_WITH_FREE_PQ="+string(dim(GI)));',
        'print("CUBE_KERNEL_DIM_WITH_FREE_PQ="+string(dim(GJ)));',
        'print("I_IN_CUBE_REMAINDER_SIZE="+string(size(I_mod_J)));',
        'print("WRONG_SHIFT_REMAINDER_SIZE="+string(size(WRONG_mod_J)));',
        'print("START_MINASS_GTZ");',
    ]
    if chart == "global":
        lines.append("ideal WORK=IS;")
    else:
        lines.append(f"ideal WORK=IS,v*B{int(chart)}-1;")
        lines.append(f"J=J,v*B{int(chart)}-1;")
        lines.append("GJ=std(J);")
    lines.extend([
        "list MA=minAssGTZ(WORK);",
        'print("MINASS_COUNT="+string(size(MA)));',
        'if (size(MA)==0) { print("FAIL_EMPTY_MINASS"); quit; }',
        "ideal RI=MA[1];",
        "for (int component=1; component<=size(MA); component++)",
        "{",
        "  ideal PC=std(MA[component]);",
        '  print("COMPONENT="+string(component)+" DIM="+string(dim(PC))'
        '+" MULT="+string(mult(PC)));',
        "  PC;",
        "  if (component>1) { RI=intersect(RI,MA[component]); }",
        "}",
        "ideal GRI=std(RI);",
        "ideal RAD_I_mod_J=reduce(GRI,GJ);",
        "ideal J_mod_RAD_I=reduce(GJ,GRI);",
        'print("RAD_I_IN_CUBE_REMAINDER_SIZE="+string(size(RAD_I_mod_J)));',
        'print("CUBE_IN_RAD_I_REMAINDER_SIZE="+string(size(J_mod_RAD_I)));',
        'print("CUBE_KERNEL_GENERATORS_BEGIN");',
        "GJ;",
        'print("CUBE_KERNEL_GENERATORS_END");',
        'print("PASS_D1_WEIGHTED_INFINITY_EXCEPTIONAL_SOURCE");',
        'print("FIREWALL=NO_DEFORMATION_OR_WHOLE_BOUNDARY_INFERENCE");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", action="store_true")
    parser.add_argument("--characteristic", type=int, default=0)
    parser.add_argument("--chart", default="global",
                        choices=("global", "0", "1", "2", "3", "4",
                                 "5", "6", "7"))
    args = parser.parse_args()
    if args.characteristic < 0 or args.characteristic == 1:
        raise ExceptionalFailure("invalid characteristic")
    tag = require_aws()
    v2 = load_v2()
    _, _, _, rows, parent_payload = v2.compile_all()
    weight_report = check_weights(rows)
    exceptional = exceptional_rows(rows)
    if args.singular:
        print(singular_source(exceptional, args.characteristic, tag,
                              args.chart), end="")
        return
    payload = {
        "aws_tag": tag,
        "parent_row_sha256": parent_payload["row_sha256"],
        "weights": {
            "A": list(WEIGHTS), "k": 6, "mu": 15, "nu": 18,
            "rho": 20,
        },
        "weight_checks": weight_report,
        "exceptional_specialization": "s=1,K=M=N=R=0",
        "projective_chart": args.chart,
        "exceptional_row_sha256": {
            f"E{ell}": row_digest(exceptional[ell]) for ell in range(1, 9)
        },
        "exceptional_row_supports": {
            f"E{ell}": len(exceptional[ell]) for ell in range(1, 9)
        },
        "cube_parameterization": {f"B{index}": CUBE[index]
                                  for index in range(8)},
        "scope": (
            "source and saturated exceptional-divisor compiler only; no component, "
            "deformation, D1, counterexample, or JC2 verdict"
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-WEIGHTED-INFINITY-EXCEPTIONAL-COMPILER")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
