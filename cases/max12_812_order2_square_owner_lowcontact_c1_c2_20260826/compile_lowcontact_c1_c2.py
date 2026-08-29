#!/usr/bin/env python3
"""Compile exact low-contact square fan clients c=1 and c=2 (AWS only)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
BASE = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
HALF_RESULTS = ROOT / "cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md"
HALF_REVIEW = ROOT / "xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md"
PTANGENT_RESULT = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULT.md"
PTANGENT_RESULTS = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULTS.sha256"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    HALF_RESULTS: "eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af",
    HALF_REVIEW: "49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214",
    PTANGENT_RESULT: "74551fe8b2ed1e4b9b1fd1594cee54e3bd3d87e6acee8b8c29d9384f5317d5ea",
    PTANGENT_RESULTS: "380245162296ae04a2cdcc677b04d4617bd415e09665c999090bfab1741839a6",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only low-contact compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only low-contact compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("square_tail_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot load frozen base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_coefficients(scenario: str) -> dict[int, str]:
    if scenario == "c1":
        pp = "(p+2*sigma*ell1)"
        avec1 = "(a1+sigma*aa1)"
        avec0 = "(a0+sigma*aa0)"
        cz = "(sigma*e11+sigma^2*e21)"
        c0 = "(sigma*e10+sigma^2*e20)"
        kc = "(sigma^3*bs1)"
        kr = f"((({pp})^2+sigma^3*br1)/4)"
    elif scenario == "c2":
        pp = "(p+2*sigma*ell1+2*sigma^2*ell2)"
        avec1 = "(a1+sigma*aa1+sigma^2*aaa1)"
        avec0 = "(a0+sigma*aa0+sigma^2*aaa0)"
        cz = "(sigma^2*e21+sigma^3*e31+sigma^4*e41)"
        c0 = "(sigma^2*e20+sigma^3*e30+sigma^4*e40)"
        kc = "(sigma^3*bs1+sigma^4*bs2)"
        kr = f"((({pp})^2+sigma^3*br1+sigma^4*br2)/4)"
    else:
        fail(("unknown scenario", scenario))
    n3 = f"(sigma^3*{avec1})"
    n2 = f"(sigma^3*{avec0})"
    n1 = f"(sigma^3*(({pp})*{avec1}+({cz}))/2)"
    n0 = f"(sigma^3*(({pp})*{avec0}+({c0}))/2)"
    return {
        6: f"(2*({pp}))",
        5: f"(2*({kc}))",
        4: f"(({pp})^2+2*({kr}))",
        3: f"(2*({pp})*({kc})+sigma^2*({n3}))",
        2: f"(({kc})^2+2*({pp})*({kr})+sigma^2*({n2}))",
        1: f"(2*({kc})*({kr})+sigma^2*({n1}))",
        0: f"(({kr})^2+sigma^2*({n0}))",
    }


def emit_scenario(lines: list[str], base, tails, characteristic: int, scenario: str) -> None:
    if scenario == "c1":
        variables = "sigma,p,ell1,a0,a1,aa0,aa1,e10,e11,e20,e21,bs1,br1,k0,k1,k6,k2,mu2,mu4,mu6,J"
        start, stop = 11, 12
        leading = ("e10", "e11")
        localizers = ("p",)
        forbidden = ("k0", "k1", "k6", "k2", "mu2", "mu4", "mu6", "J", "bs1", "br1")
        small = "p,ell1,a0,a1,aa0,aa1,e10,e11,e20,e21"
    else:
        variables = "sigma,p,ell1,ell2,a0,a1,aa0,aa1,aaa0,aaa1,e20,e21,e30,e31,e40,e41,bs1,br1,bs2,br2,k0,k1,k6,k2,mu2,mu4,mu6,J"
        start, stop = 12, 14
        leading = ("e20", "e21")
        localizers = ("p", "k0")
        forbidden = ("k6", "k2", "mu2", "mu4", "mu6", "J")
        small = "p,k0,ell1,ell2,a0,a1,aa0,aa1,aaa0,aaa1,e20,e21,e30,e31,e40,e41,bs1,br1,bs2,br2,k1"
    coeffs = source_coefficients(scenario)
    loads = {"k10": "(k0+sigma*k1)", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    prefix = scenario.upper()
    lines.extend(
        [
            f"ring R{scenario}full={characteristic},({variables}),dp;",
            f"ideal Sigma{start}=std(ideal(sigma^{start}));",
            f"int {scenario}div=1; int {scenario}identity=1; int {scenario}forbidden=1;",
        ]
    )
    grade_rows: dict[int, list[str]] = {grade: [] for grade in range(start, stop + 1)}
    for row in range(1, 8):
        expression = base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        if targets[row] != "0":
            expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
        lines.extend(
            [
                f"poly {scenario}Phi{row}={expression};",
                f"if (reduce({scenario}Phi{row},Sigma{start})!=0) {{ {scenario}div=0; }}",
                f"poly {scenario}Q{row}_{start}={scenario}Phi{row}/sigma^{start};",
                f"if (sigma^{start}*{scenario}Q{row}_{start}-{scenario}Phi{row}!=0) {{ {scenario}identity=0; }}",
            ]
        )
        previous = f"{scenario}Q{row}_{start}"
        for grade in range(start, stop + 1):
            current = f"{scenario}g{grade}_{row}"
            lines.append(f"poly {current}=subst({previous},sigma,0);")
            grade_rows[grade].append(current)
            if grade < stop:
                remainder = f"{scenario}rem{grade + 1}_{row}"
                quotient = f"{scenario}Q{row}_{grade + 1}"
                lines.extend(
                    [
                        f"poly {remainder}={previous}-{current};",
                        f"if (reduce({remainder},std(ideal(sigma)))!=0) {{ {scenario}identity=0; }}",
                        f"poly {quotient}={remainder}/sigma;",
                        f"if (sigma*{quotient}-{remainder}!=0) {{ {scenario}identity=0; }}",
                    ]
                )
                previous = quotient
            for variable in forbidden:
                lines.append(f"if (diff({current},{variable})!=0) {{ {scenario}forbidden=0; }}")
    lines.extend(
        [
            f'print("SQUARE_LOW_{prefix}_DIVISIBLE="+string({scenario}div));',
            f'print("SQUARE_LOW_{prefix}_IDENTITIES="+string({scenario}identity));',
            f'print("SQUARE_LOW_{prefix}_FORBIDDEN="+string({scenario}forbidden));',
            f'if ({scenario}div*{scenario}identity*{scenario}forbidden!=1) {{ print("SQUARE_LOW_{prefix}_FAIL=SOURCE_EXTRACTION"); quit; }}',
        ]
    )
    all_rows = [name for grade in range(start, stop + 1) for name in grade_rows[grade]]
    lines.append(f"ideal {scenario}Efull=" + ",".join(all_rows) + ";")
    lines.extend(
        [
            f"ring R{scenario}small={characteristic},({small}),dp;",
            f"ideal {scenario}E=std(imap(R{scenario}full,{scenario}Efull));",
        ]
    )
    localized = f"{scenario}E"
    for index, variable in enumerate(localizers, start=1):
        next_name = f"{scenario}Loc{index}"
        lines.append(f"ideal {next_name}=std(sat({localized},ideal({variable}))); ")
        localized = next_name
    lines.extend(
        [
            f"ideal {scenario}Rad=std(radical({localized}));",
            f"int {scenario}lead0=(reduce({leading[0]},{scenario}Rad)==0);",
            f"int {scenario}lead1=(reduce({leading[1]},{scenario}Rad)==0);",
            f"ideal {scenario}LeadSat=std(sat({localized},ideal({leading[0]},{leading[1]})));",
            f"int {scenario}unit=(reduce(1,{scenario}LeadSat)==0);",
            f'print("SQUARE_LOW_{prefix}_RADICAL_BEGIN"); print({scenario}Rad); print("SQUARE_LOW_{prefix}_RADICAL_END");',
            f'print("SQUARE_LOW_{prefix}_LEAD0_IN_RADICAL="+string({scenario}lead0));',
            f'print("SQUARE_LOW_{prefix}_LEAD1_IN_RADICAL="+string({scenario}lead1));',
            f'print("SQUARE_LOW_{prefix}_LEADING_SAT_UNIT="+string({scenario}unit));',
            f'if ({scenario}lead0*{scenario}lead1*{scenario}unit!=1) {{ print("SQUARE_LOW_{prefix}_ENDPOINT=NONUNIT_NEEDS_SPLIT"); }} else {{ print("SQUARE_LOW_{prefix}_ENDPOINT=PASS_LEADING_C_KILLED"); }}',
        ]
    )


def emit(path: Path, characteristic: int, tails) -> None:
    base = load_base()
    lines = ['LIB "elim.lib";', 'LIB "primdec.lib";', 'print("SQUARE_LOWCONTACT_SOURCE_HASHES=PASS");']
    emit_scenario(lines, base, tails, characteristic, "c1")
    emit_scenario(lines, base, tails, characteristic, "c2")
    lines.extend(['print("SQUARE_LOWCONTACT_ENDPOINT=COMPLETE");', "quit;"])
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
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_lowcontact_c1_c2_{label}.sing"
    emit(target, args.characteristic, tails)
    payload = {
        "status": "PASS-SQUARE-LOWCONTACT-C1-C2-COMPILER",
        "scope": "C1_C2_SOURCE_FAN_CLIENTS_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
