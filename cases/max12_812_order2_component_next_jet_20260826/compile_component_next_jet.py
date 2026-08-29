#!/usr/bin/env python3
"""AWS-only compiler for matched componentwise next divided jets."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
DESIGN = ROOT / "xmodel/max12-812-order2-square-discriminant-next-jet-design-20260826.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
FIRST_NORMAL = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md"
UFD_V2 = ROOT / "xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md"
UFD_V2_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md"
EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    DESIGN: "8d44393d23e5af2a59cd90713cba71daf1d07185be5a4ca905c1b56559af1c9e",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    FIRST_NORMAL: "827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc",
    UFD_V2: "4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d",
    UFD_V2_REVIEW: "08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOAD_LAMBDA_WEIGHTS = [2, 6, 10]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only component compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only component compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def component_data(config: str) -> tuple[str, dict[int, str], dict[str, str], str, list[str], list[str]]:
    if config == "square":
        p = "p"
        c = "(Lambda*cs)"
        r = "((p^2+Lambda*rs)/4)"
        n3, n2 = "u3", "u2"
        n1 = "((p*u3+Lambda*v1)/2)"
        n0 = "((p*u2+Lambda*v0)/2)"
        variables = "Lambda,p,u2,u3,k10,cs,rs,v0,v1,k6,k2,mu2,mu4,mu6,J"
        small = ["p", "u2", "u3", "k10", "cs", "rs", "v0", "v1"]
        saturations = ["ideal(p)", "ideal(u2,u3,k10)"]
        load_expr = {"k10": "k10", "k6": "k6", "k2": "k2"}
    elif config == "disc":
        p = "(d-3*a^2)"
        c = "(2*a*(a^2-d)+Lambda*cs)"
        r = "(a^2*d+Lambda*rs)"
        n3, n2 = "lam", "(a*lam)"
        n1 = "((d-2*a^2)*lam+Lambda*v1)"
        n0 = "(-a*d*lam+Lambda*v0)"
        variables = "Lambda,a,d,lam,kappa,cs,rs,v0,v1,k6,k2,mu2,mu4,mu6,J"
        small = ["a", "d", "lam", "kappa", "cs", "rs", "v0", "v1"]
        saturations = ["ideal(lam)", "ideal(a,d)", "ideal(d-a^2)"]
        load_expr = {"k10": "(Lambda*kappa)", "k6": "k6", "k2": "k2"}
    else:
        fail(("unknown config", config))
    coeffs = {
        6: f"(2*({p}))",
        5: f"(2*({c}))",
        4: f"(({p})^2+2*({r}))",
        3: f"(2*({p})*({c})+Lambda*({n3}))",
        2: f"(({c})^2+2*({p})*({r})+Lambda*({n2}))",
        1: f"(2*({c})*({r})+Lambda*({n1}))",
        0: f"(({r})^2+Lambda*({n0}))",
    }
    return variables, coeffs, load_expr, ",".join(small), small, saturations


def term_text(monomial: list[int], coefficient: Fraction, coeffs: dict[int, str], loads: dict[str, str]) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent == 1:
            factors.append(coeffs[i])
        elif exponent:
            factors.append(f"({coeffs[i]})^{exponent}")
    lambda_power = 0
    for offset, exponent in enumerate(monomial[7:]):
        if exponent:
            name = NAMES[7 + offset]
            factors.append(loads[name] if exponent == 1 else f"({loads[name]})^{exponent}")
            lambda_power += LOAD_LAMBDA_WEIGHTS[offset] * exponent
    if lambda_power:
        factors.append(f"Lambda^{lambda_power}")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)


def tail_text(entries: list[list[object]], ell: int, coeffs: dict[int, str], loads: dict[str, str]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail load nonlinearity", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        terms.append(term_text(monomial, Fraction(str(raw_coefficient)), coeffs, loads))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, config: str, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    variables, coeffs, loads, small_variables, small_list, saturations = component_data(config)
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring Rfull={characteristic},({variables}),dp;",
        'print("COMPONENT_NEXT_SOURCE_HASHES=PASS");',
        f'print("COMPONENT_NEXT_CONFIG={config}");',
        "ideal Lambda3=std(ideal(Lambda^3));",
        "int divisible=1;",
        "int identity=1;",
        "int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell, coeffs, loads)
        if targets[ell] != "0":
            expression += f"-Lambda^{12 + ell}*({targets[ell]})"
        lines.extend([
            f"poly Phi{ell}={expression};",
            f"if (reduce(Phi{ell},Lambda3)!=0) {{ divisible=0; }}",
            f"poly Xi{ell}=Phi{ell}/Lambda^3;",
            f"if (Lambda^3*Xi{ell}-Phi{ell}!=0) {{ identity=0; }}",
            f"poly e{ell}=subst(Xi{ell},Lambda,0);",
            f"if (diff(e{ell},k6)!=0 || diff(e{ell},k2)!=0 || diff(e{ell},mu2)!=0 || diff(e{ell},mu4)!=0 || diff(e{ell},mu6)!=0 || diff(e{ell},J)!=0) {{ forbidden=0; }}",
        ])
    lines.extend([
        'print("COMPONENT_NEXT_LAMBDA3_DIVISIBLE="+string(divisible));',
        'print("COMPONENT_NEXT_DIVISION_IDENTITY="+string(identity));',
        'print("COMPONENT_NEXT_FORBIDDEN_INDEPENDENCE="+string(forbidden));',
        'if (divisible!=1) { print("COMPONENT_NEXT_FAIL=DIVISIBILITY"); quit(81); }',
        'if (identity!=1) { print("COMPONENT_NEXT_FAIL=IDENTITY"); quit(82); }',
        'if (forbidden!=1) { print("COMPONENT_NEXT_FAIL=FORBIDDEN"); quit(83); }',
        'print("COMPONENT_NEXT_ROWS_BEGIN");',
        'print(e1); print(e2); print(e3); print(e4); print(e5); print(e6); print(e7);',
        'print("COMPONENT_NEXT_ROWS_END");',
        "ideal Eraw=e1,e2,e3,e4,e5,e6,e7;",
        f"ring Rsmall={characteristic},({small_variables}),dp;",
        "ideal E=imap(Rfull,Eraw);",
        "E=std(E);",
        'print("COMPONENT_NEXT_STD_DONE");',
        'print("COMPONENT_NEXT_RAW_SIZE="+string(size(E)));',
        'print("COMPONENT_NEXT_RAW_DIM="+string(dim(E)));',
    ])
    current = "E"
    for index, saturation in enumerate(saturations, start=1):
        nxt = f"ES{index}"
        lines.extend([
            f'print("COMPONENT_NEXT_SAT_{index}_START");',
            f"ideal {nxt}=sat({current},{saturation});",
            f"{nxt}=std({nxt});",
            f'print("COMPONENT_NEXT_SAT_{index}_DONE");',
            f'print("COMPONENT_NEXT_SAT_{index}_SIZE="+string(size({nxt})));',
            f'print("COMPONENT_NEXT_SAT_{index}_DIM="+string(dim({nxt})));',
        ])
        current = nxt
    lines.extend([
        f'int endpoint_unit=(reduce(1,{current})==0);',
        'print("COMPONENT_NEXT_ENDPOINT_UNIT="+string(endpoint_unit));',
        f'print("COMPONENT_NEXT_ENDPOINT_BASIS_BEGIN"); print({current}); print("COMPONENT_NEXT_ENDPOINT_BASIS_END");',
        'print("COMPONENT_NEXT_TRANSVERSE_SECTION=RETAINED");',
        'print("COMPONENT_NEXT_ENDPOINT=PASS_MATCHED_VALUATION_ONLY");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", choices=("square", "disc"), required=True)
    parser.add_argument("--characteristic", type=int, choices=(32003, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED_STATIC.items():
        if digest(source) != expected:
            fail(("frozen source mismatch", source, digest(source), expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"component_next_{args.config}_p{args.characteristic}.sing"
    emit(singular, args.config, args.characteristic, tails)
    payload = {
        "status": "PASS-COMPONENT-NEXT-JET-COMPILER",
        "registered_aws_lane": tag,
        "config": args.config,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
        "scope": "MATCHED_VALUATION_NEXT_JET_ONLY_NO_COMPONENT_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
