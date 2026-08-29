#!/usr/bin/env python3
"""Compile the high-contact translated C2 target-shadow client; AWS only."""

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
V3_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_v3_parenthesized_loads_20260826"
V3 = V3_DIR / "compile_v3_parenthesized_loads.py"
PINS = {
    V3: "0f7b9482f214347858f61181119f52fc434de8223ae7a3c4099049bd737897ef",
    V3_DIR / "FREEZE.sha256": "7016cdba48152e5e44b285a56812f2b2e077f110cc6e5baa5adbbe9d184d2432",
    V3_DIR / "RESULT.md": "88609fdfc50b89625f79e7dcee3b8ceb47d61c3b6668e86ee80da67ad4129e24",
    V3_DIR / "EVIDENCE.sha256": "d2e5d59f94d3489fd8bd3509fd0ece0dc2456c234173f5023ebad2f201bb3c06",
}
CONTACTS = tuple(range(10, 16))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only high-contact C2-shadow compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only high-contact C2-shadow compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import frozen module", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_mapping(mapping) -> None:
    for source, expected in mapping.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen ancestry mismatch", str(source), actual, expected))


def jet_names(stem: str, maximum_index: int) -> list[str]:
    return [stem] + [f"{stem}_{index}" for index in range(1, maximum_index + 1)]


def series(stem: str, maximum_index: int) -> str:
    return "+".join(
        stem if index == 0 else f"sigma^{index}*{stem}_{index}"
        for index in range(maximum_index + 1)
    )


def fresh(stem: str, index: int) -> str:
    return stem if index == 0 else f"{stem}_{index}"


def ancestry():
    check_mapping(PINS)
    v3 = load_module(V3, "d1_highcontact_v3")
    check_mapping(v3.PINS)
    v2 = v3.load_v2()
    check_mapping(v2.PINS)
    v1 = v2.load_v1()
    check_mapping(v1.PINS)
    a8 = v1.load_a8()
    check_mapping(a8.PINS)
    source_base = a8.load_base()
    check_mapping(source_base.PINS)
    frozen_cge3 = source_base.load_v1()
    check_mapping(frozen_cge3.EXPECTED)
    tails = json.loads(frozen_cge3.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != frozen_cge3.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = frozen_cge3.load_base()
    return source_base, tail_base, tails


def source_row(tail_base, tails, row: int, coeffs, loads, targets) -> str:
    expression = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace(
        "Lambda", "(sigma^2)"
    )
    if targets[row] != "0":
        expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
    return expression


def section(a: int, characteristic: int, source_base, tail_base, tails) -> list[str]:
    grade = 12 + 2 * a
    mu2_index = grade - 28
    mu4_index = grade - 32
    mu6_index = max(grade - 36, 0)
    correction = grade - (18 + a)
    p_index = max(mu2_index, correction, 2)
    ac_index = max(correction + 1, 2)
    r_index = max(a - 9, 2)
    k2_index = max(a - 9, 2)
    k0_index = 2

    variables = ["z", "sigma", "p"]
    variables += [f"ell{index}" for index in range(1, p_index + 1)]
    for stem in ("a1", "a0", "c1", "c0"):
        variables += jet_names(stem, ac_index)
    for stem in ("b1", "b0"):
        variables += jet_names(stem, r_index)
    variables += jet_names("k0", k0_index)
    variables += jet_names("k60", correction)
    variables += jet_names("k20", k2_index)
    variables += jet_names("mu20", mu2_index)
    variables += jet_names("mu4", mu4_index)
    variables += jet_names("mu6", mu6_index)
    variables += ["J", "u1", "u0"]

    prefix = f"HC{a}_"
    lines = [
        f"ring {prefix}R={characteristic},({','.join(variables)}),dp;",
        f'print("{prefix}SOURCE_HASHES=PASS");',
        f"ideal {prefix}Sigma28=std(ideal(sigma^28));",
        f"ideal {prefix}Sigma1=std(ideal(sigma));",
        f"int {prefix}divisible=1; int {prefix}identities=1;",
    ]
    pp = "p" + "".join(f"+2*sigma^{index}*ell{index}" for index in range(1, p_index + 1))
    az = f"sigma^{a}*({series('a1', ac_index)})"
    ac = f"sigma^{a}*({series('a0', ac_index)})"
    cz = f"sigma^{a + 1}*({series('c1', ac_index)})"
    cc = f"sigma^{a + 1}*({series('c0', ac_index)})"
    rz = f"sigma^{a}*({series('b1', r_index)})"
    rc = f"sigma^{a}*({series('b0', r_index)})"
    coeffs = source_base.source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {
        "k10": f"({series('k0', k0_index)})",
        "k6": f"({series('k60', correction)})",
        "k2": f"({series('k20', k2_index)})",
    }
    targets = {
        1: "0",
        2: series("mu20", mu2_index),
        3: "0",
        4: series("mu4", mu4_index),
        5: "0",
        6: series("mu6", mu6_index),
        7: "J/4",
    }
    row_names: dict[tuple[int, int], str] = {}
    for row in range(1, 8):
        expression = source_row(tail_base, tails, row, coeffs, loads, targets)
        lines += [
            f"poly {prefix}Phi{row}={expression};",
            f"if (reduce({prefix}Phi{row},{prefix}Sigma28)!=0) {{ {prefix}divisible=0; }}",
            f"poly {prefix}Q28_{row}={prefix}Phi{row}/sigma^28;",
            f"if (sigma^28*{prefix}Q28_{row}-{prefix}Phi{row}!=0) {{ {prefix}identities=0; }}",
        ]
        for current in range(28, grade + 1):
            qname = f"{prefix}Q{current}_{row}"
            gname = f"{prefix}g{current}_{row}"
            row_names[(current, row)] = gname
            lines.append(f"poly {gname}=subst({qname},sigma,0);")
            if current < grade:
                rem = f"{prefix}Rem{current + 1}_{row}"
                nxt = f"{prefix}Q{current + 1}_{row}"
                lines += [
                    f"poly {rem}={qname}-{gname};",
                    f"if (reduce({rem},{prefix}Sigma1)!=0) {{ {prefix}identities=0; }}",
                    f"poly {nxt}={rem}/sigma;",
                    f"if (sigma*{nxt}-{rem}!=0) {{ {prefix}identities=0; }}",
                ]

    fresh2 = fresh("mu20", mu2_index)
    fresh4 = fresh("mu4", mu4_index)
    lines += [
        f"int {prefix}fresh_earlier=1;",
    ]
    for current in range(28, grade):
        for row in range(1, 8):
            lines.append(
                f"if (diff({row_names[(current, row)]},{fresh2})!=0 || "
                f"diff({row_names[(current, row)]},{fresh4})!=0) {{ {prefix}fresh_earlier=0; }}"
            )
    lines += [
        f"int {prefix}fresh_rows=1;",
        f"if (diff({row_names[(grade, 2)]},{fresh2})!=-1) {{ {prefix}fresh_rows=0; }}",
        f"if (diff({row_names[(grade, 4)]},{fresh4})!=-1) {{ {prefix}fresh_rows=0; }}",
    ]
    for row in range(1, 8):
        if row != 2:
            lines.append(
                f"if (diff({row_names[(grade, row)]},{fresh2})!=0) {{ {prefix}fresh_rows=0; }}"
            )
        if row != 4:
            lines.append(
                f"if (diff({row_names[(grade, row)]},{fresh4})!=0) {{ {prefix}fresh_rows=0; }}"
            )
    lines += [
        f"poly {prefix}base2=subst({row_names[(grade, 2)]},{fresh2},0);",
        f"poly {prefix}base4=subst({row_names[(grade, 4)]},{fresh4},0);",
        f"int {prefix}sections=(subst({row_names[(grade, 2)]},{fresh2},{prefix}base2)==0 && "
        f"subst({row_names[(grade, 4)]},{fresh4},{prefix}base4)==0);",
        f"int {prefix}row3_target_free=1;",
    ]
    for target_stem, target_index in (("mu20", mu2_index), ("mu4", mu4_index), ("mu6", mu6_index)):
        for index in range(target_index + 1):
            lines.append(
                f"if (diff({row_names[(grade, 3)]},{fresh(target_stem, index)})!=0) "
                f"{{ {prefix}row3_target_free=0; }}"
            )
    lines.append(
        f"if (diff({row_names[(grade, 3)]},J)!=0) {{ {prefix}row3_target_free=0; }}"
    )

    c2_coeffs = source_base.source_coefficients(
        "p", "0", "0", f"sigma^{a + 1}*c1", f"sigma^{a + 1}*c0", "0", "0"
    )
    zero_loads = {"k10": "0", "k6": "0", "k2": "0"}
    zero_targets = {row: "0" for row in range(1, 8)}
    for row in range(1, 8):
        expression = source_row(tail_base, tails, row, c2_coeffs, zero_loads, zero_targets)
        lines += [
            f"poly {prefix}C2Phi{row}={expression};",
            f"poly {prefix}C2Q{row}={prefix}C2Phi{row}/sigma^{grade};",
            f"int {prefix}C2div{row}=(sigma^{grade}*{prefix}C2Q{row}-{prefix}C2Phi{row}==0);",
            f"poly {prefix}C2g{row}=subst({prefix}C2Q{row},sigma,0);",
        ]
    expected = {
        1: "0",
        2: "(3/8)*c1^2",
        3: "(3/4)*c1*c0",
        4: "(3/16)*(2*c0^2-p*c1^2)",
        5: "-(3/16)*p*c1*c0",
        6: "0",
        7: "-(3/128)*p^2*c1*c0",
    }
    equality = " && ".join(
        f"{prefix}C2g{row}-({expected[row]})==0" for row in range(1, 8)
    )
    divisibility = "*".join(f"{prefix}C2div{row}" for row in range(1, 8))
    lines += [
        f"int {prefix}C2rows=({equality});",
        f"int {prefix}C2divisible={divisibility};",
        f"poly {prefix}T2=(3/8)*c1^2-mu20;",
        f"poly {prefix}T3=(3/4)*c1*c0;",
        f"poly {prefix}T4=(3/16)*(2*c0^2-p*c1^2)-mu4;",
        f"poly {prefix}T5=-(3/16)*p*c1*c0;",
        f"poly {prefix}T7=-(3/128)*p^2*c1*c0;",
        f"ideal {prefix}witness=std(ideal(p-1,c1,c0-1,mu20,mu4-3/8,u1,u0-1));",
        f"int {prefix}witness_ok=(reduce(1,{prefix}witness)!=0 && "
        f"reduce({prefix}T2,{prefix}witness)==0 && reduce({prefix}T3,{prefix}witness)==0 && "
        f"reduce({prefix}T4,{prefix}witness)==0 && reduce({prefix}T5,{prefix}witness)==0 && "
        f"reduce({prefix}T7,{prefix}witness)==0 && "
        f"reduce(u1*c1+u0*c0-1,{prefix}witness)==0);",
        f'print("{prefix}RECURSIVE_QUOTIENT_IDENTITIES="+string({prefix}identities));',
        f'print("{prefix}DIVISIBLE_FROM_GRADE28="+string({prefix}divisible));',
        f'print("{prefix}TAGGED_C2_TRANSLATION="+string({prefix}C2rows));',
        f'print("{prefix}TAGGED_C2_DIVISIBLE="+string({prefix}C2divisible));',
        f'print("{prefix}FRESH_TARGETS_ABSENT_EARLIER="+string({prefix}fresh_earlier));',
        f'print("{prefix}FRESH_TARGET_ROW_COEFFICIENTS="+string({prefix}fresh_rows));',
        f'print("{prefix}FRESH_TARGET_EXACT_SECTIONS="+string({prefix}sections));',
        f'print("{prefix}ROW3_TARGET_FREE="+string({prefix}row3_target_free));',
        f'print("{prefix}TARGET_SHADOW_CONTACT_WITNESS="+string({prefix}witness_ok));',
        f"if ({prefix}identities*{prefix}divisible*{prefix}C2rows*{prefix}C2divisible*"
        f"{prefix}fresh_earlier*{prefix}fresh_rows*{prefix}sections*"
        f"{prefix}row3_target_free*{prefix}witness_ok!=1) {{ "
        f'print("{prefix}FAIL=SOURCE_TRANSLATION_OR_TARGET_SHADOW"); quit; }}',
        f'print("{prefix}ENDPOINT=PASS_C2_PAIR_SHADOWED_AT_A{a}");',
    ]
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    source_base, tail_base, tails = ancestry()
    output = args.output.resolve()
    if output.exists():
        fail("high-contact C2-shadow output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_highcontact_c2_target_shadow_{label}.sing"
    lines: list[str] = []
    for a in CONTACTS:
        lines.extend(section(a, args.characteristic, source_base, tail_base, tails))
    lines += [
        'print("HC_UNIFORM_SHIFT_IDENTITY=SIGMA_2S_AND_TARGET_INDEX_2S");',
        'print("HC_C2_PAIR_TRANSLATES_AS_TAGGED_BLOCK=1");',
        'print("HC_C2_PAIR_SURVIVES_COMPLETE_TARGETS=0");',
        'print("HC_ENDPOINT=PASS_UNCHANGED_C2_INDUCTION_FALSIFIED");',
        "quit;",
    ]
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-HIGHCONTACT-C2-TARGET-SHADOW-COMPILER",
        "scope": "SOURCE_NAVIGATION_A10_A15_PLUS_SYMBOLIC_SHIFT_NO_EMPTY_OR_SURVIVAL_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "contacts": list(CONTACTS),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

