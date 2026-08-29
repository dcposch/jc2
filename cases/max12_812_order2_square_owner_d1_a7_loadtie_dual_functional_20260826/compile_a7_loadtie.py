#!/usr/bin/env python3
"""Compile the full a=7 D1 load-tie dual-functional client; AWS only."""

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
LOW = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826/compile_local_row.py"
LOW_PRODUCER = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826/PRODUCER_FREEZE.sha256"
PINS = {
    LOW: "b2fe07fdd2f855598dde5c6ef9828909c94496eb5e196756eff504056cde2769",
    LOW_PRODUCER: "4d69b97d8c6e24baadc76aba69d3d37158a3aa466cf7e44bc3111008c5a07fd3",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(mapping) -> None:
    for path, expected in mapping.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a7 load-tie compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a7 load-tie compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def primitive_signature(item) -> tuple:
    return tuple(item[key] for key in (
        "summand", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient"
    ))


def compile_block(characteristic: int, low, base, tail_base, tails, miner, d: int):
    a, r = 7, 7
    G, T = 24 + d, 24 + 2 * d
    row = {"a": a, "d": d, "c": a + d, "s_min": 0, "r": r,
           "first_ac_grade": G, "target_grade": T}
    primitive = miner.enumerate_primitives(row)
    padded = miner.enumerate_primitives(row, pad=1)
    if {miner.signature(x) for x in primitive} != {miner.signature(x) for x in padded}:
        fail(("padded primitive mismatch", row))
    if len(primitive) != {2: 5, 3: 7}[d]:
        fail(("primitive count", row, primitive))
    first = {primitive_signature(x) for x in primitive if int(x["first_grade"]) == G}
    expected_first = {
        ("k6", "k6", 17, 0, 0, 1, 1, "3/4"),
        ("unloaded", None, 10, 0, 1, 1, 1, "3/4"),
    }
    if first != expected_first:
        fail(("first load tie", row, first))
    if max(int(x["pole"]) for x in primitive) != 2:
        fail(("pole ceiling", row, primitive))
    pole_two = [x for x in primitive if int(x["pole"]) == 2]
    if len(pole_two) != 1 or primitive_signature(pole_two[0]) != (
        "unloaded", None, 10, 0, 0, 2, 2, "3/8"
    ) or int(pole_two[0]["first_grade"]) != T:
        fail(("sole target pole-two column", row, pole_two))

    def depth_with(stem: str) -> int:
        if stem in ("A", "C", "R"):
            values = [T - int(x["first_grade"]) for x in primitive if int(x[stem]) > 0]
        else:
            values = [T - int(x["first_grade"]) for x in primitive if x["load"] == stem]
        return max(values, default=0)

    amax, cmax, rmax = depth_with("A"), depth_with("C"), depth_with("R")
    k0max, k6max, k2max = depth_with("k10"), depth_with("k6"), depth_with("k2")
    pmax = T - min(int(x["first_grade"]) for x in primitive)
    mu2max, mu4max = max(T - 28, 0), max(T - 32, 0)

    variables = ["z", "t", "sigma", "p"]
    variables += [f"ell{j}" for j in range(1, pmax + 1)]
    for stem, maximum in (
        ("a1", amax), ("a0", amax), ("c1", cmax), ("c0", cmax),
        ("b1", rmax), ("b0", rmax), ("k0", k0max), ("k60", k6max),
        ("k20", k2max), ("mu20", mu2max), ("mu4", mu4max),
    ):
        variables += low.jets(stem, maximum)
    variables += ["mu6", "J", "lam"] + [f"rho{j}" for j in range(1, pmax + 1)]
    variables += ["ilam", "ic1", "ic0", "ik0", "idelta"]
    variables = list(dict.fromkeys(variables))
    prefix = f"A7D{d}_"
    lines = [
        f"ring {prefix}R={characteristic},({','.join(variables)}),dp;",
        f'print("{prefix}BASELINE=A7_D{d}_RGE7_G{G}_T{T}");',
        f'print("{prefix}PRIMITIVE_COLUMNS={len(primitive)}");',
        f'print("{prefix}GLOBAL_POLE_CEILING=2");',
    ]
    pseries = "p" + "".join(f"+2*sigma^{j}*ell{j}" for j in range(1, pmax + 1))
    pname = f"{prefix}P"
    lines.append(f"poly {pname}={pseries};")
    A = f"sigma^7*(({low.series('a1', amax)})+t*({low.series('a0', amax)}))"
    C = f"sigma^{7+d}*(({low.series('c1', cmax)})+t*({low.series('c0', cmax)}))"
    R = f"sigma^7*(({low.series('b1', rmax)})+t*({low.series('b0', rmax)}))"
    load_series = {
        "k10": low.series("k0", k0max),
        "k6": low.series("k60", k6max),
        "k2": low.series("k20", k2max),
    }
    inv = {q: low.inv_series(q, pname) for q in (1, 2)}
    hterms = []
    for item in primitive:
        q = int(item["pole"])
        eR, eA, eC = (int(item[x]) for x in ("R", "A", "C"))
        tpower = 1 + 2 * q - eR - eA - eC
        if tpower < 0:
            fail(("improper primitive", row, item))
        factors = [low.frac(str(item["coefficient"])), f"sigma^{int(item['fixed_sigma'])}"]
        if item["load"] is not None:
            factors.append(f"({load_series[str(item['load'])]})")
        if tpower:
            factors.append(f"t^{tpower}")
        for expression, exponent in ((R, eR), (A, eA), (C, eC)):
            if exponent:
                factors.append(f"({expression})^{exponent}")
        factors.append(inv[q])
        hterms.append("*".join(factors))
    lines.append(f"poly {prefix}H=" + "+".join(hterms).replace("+-", "-") + ";")
    for j in range(1, 8):
        low.t_coefficient(lines, f"{prefix}H", f"{prefix}h{j}", j + 1)

    pp = f"({pname})"
    coeffs = base.source_coefficients(
        pp, f"sigma^7*({low.series('a1', amax)})", f"sigma^7*({low.series('a0', amax)})",
        f"sigma^{7+d}*({low.series('c1', cmax)})", f"sigma^{7+d}*({low.series('c0', cmax)})",
        f"sigma^7*({low.series('b1', rmax)})", f"sigma^7*({low.series('b0', rmax)})",
    )
    loads = {key: f"({value})" for key, value in load_series.items()}
    targets = {
        1: "0", 2: low.series("mu20", mu2max), 3: "0",
        4: low.series("mu4", mu4max), 5: "0", 6: "mu6", 7: "J/4",
    }
    for j in range(1, 8):
        source = low.source_row(tail_base, tails, j, coeffs, loads)
        target = "0" if targets[j] == "0" else f"sigma^{2*(12+j)}*({targets[j]})"
        lines += [
            f"poly {prefix}SourcePhi{j}={source};",
            f"poly {prefix}FullPhi{j}={prefix}SourcePhi{j}-({target});",
        ]
    predicted = {
        1: f"{prefix}h1",
        2: f"{prefix}h2",
        3: f"{prefix}h3+({pname}/4)*{prefix}h1",
        4: f"{prefix}h4+({pname}/2)*{prefix}h2",
        5: f"{prefix}h5+(3*{pname}/4)*{prefix}h3+(3*({pname}^2)/32)*{prefix}h1",
        6: f"{prefix}h6+{pname}*{prefix}h4+(({pname}^2)/4)*{prefix}h2",
        7: f"{prefix}h7+(5*{pname}/4)*{prefix}h5+(15*({pname}^2)/32)*{prefix}h3+(5*({pname}^3)/128)*{prefix}h1",
    }
    lines += [f"ideal {prefix}ST=std(ideal(sigma^{T+1}));", f"int {prefix}bridge=1;"]
    for j in range(1, 8):
        lines += [
            f"poly {prefix}PredPhi{j}={predicted[j]};",
            f"if (reduce({prefix}SourcePhi{j}-{prefix}PredPhi{j},{prefix}ST)!=0) {{ {prefix}bridge=0; }}",
        ]
    for j in range(1, 8):
        low.sigma_extract(lines, f"{prefix}FullPhi{j}", f"{prefix}F{j}_", G, T)
    lines.append(f"int {prefix}quotients=" + "*".join(f"{prefix}F{j}_exact" for j in range(1, 8)) + ";")

    root = "lam" + "".join(f"+sigma^{j}*rho{j}" for j in range(1, pmax + 1))
    # sigma_extract interpolates its source into products and differences;
    # protect the entire root polynomial, not only its second summand.
    root_coeffs = low.sigma_extract(lines, f"(({root})^2+({pname}/2))", f"{prefix}Root_", 0, pmax)
    lines += [
        f"int {prefix}root_constant=({root_coeffs[0]}==p/2+lam^2);",
        f"ideal {prefix}RootIdeal=std(ideal(" + ",".join(root_coeffs[g] for g in range(1, pmax + 1)) + ",ilam*lam-1));",
    ]

    first_h = {}
    for j in (1, 2):
        first_h[j] = low.sigma_extract(lines, f"{prefix}h{j}", f"{prefix}H{j}_", G, G)[G]
    lines += [
        f"poly {prefix}Nfirst={first_h[1]}*z+{first_h[2]};",
        f"poly {prefix}FirstRz=a1*c0+(a0+k60)*c1;",
        f"poly {prefix}FirstR0=(a0+k60)*c0-(p/2)*a1*c1;",
        f"poly {prefix}NfirstExpected=(3/4)*({prefix}FirstRz*z+{prefix}FirstR0);",
        f"int {prefix}first_tie=({prefix}Nfirst-{prefix}NfirstExpected==0);",
        f"poly {prefix}DeltaC=c0^2+(p/2)*c1^2;",
        f"ideal {prefix}Rank2Ideal=std(ideal({prefix}FirstRz,{prefix}FirstR0,idelta*{prefix}DeltaC-1));",
        f"int {prefix}rank2_off_delta=(reduce(a1,{prefix}Rank2Ideal)==0 && reduce(a0+k60,{prefix}Rank2Ideal)==0);",
    ]

    lines += [
        f"poly {prefix}N2={prefix}h1*z^3+{prefix}h2*z^2+({prefix}h3+{pname}*{prefix}h1)*z+({prefix}h4+{pname}*{prefix}h2);",
        f"poly {prefix}Rec5={prefix}h5+{pname}*{prefix}h3+(({pname}^2)/4)*{prefix}h1;",
        f"poly {prefix}Rec6={prefix}h6+{pname}*{prefix}h4+(({pname}^2)/4)*{prefix}h2;",
        f"poly {prefix}Rec7={prefix}h7+{pname}*{prefix}h5+(({pname}^2)/4)*{prefix}h3;",
        f"int {prefix}recurrence=(reduce({prefix}Rec5,{prefix}ST)==0 && reduce({prefix}Rec6,{prefix}ST)==0 && reduce({prefix}Rec7,{prefix}ST)==0);",
    ]

    functional = f"({prefix}SourcePhi3+({pname}/4)*{prefix}SourcePhi1)"
    orientation = {}
    for sign, label in ((1, "plus"), (-1, "minus")):
        signed_root = root if sign == 1 else f"-({root})"
        name = f"{prefix}Psi_{label}"
        lines += [
            f"poly {name}={prefix}SourcePhi4+({signed_root})*{functional};",
            f"{name}=subst({name},p,-2*lam^2);",
            f"poly {name}Red=reduce({name},{prefix}RootIdeal);",
        ]
        orientation[label] = low.sigma_extract(lines, f"{name}Red", f"{name}_", G, T)
    qplus = f"(3/8)*(c1*lam+c0)^2"
    qminus = f"(3/8)*(-c1*lam+c0)^2"
    lower_plus = " && ".join(f"{orientation['plus'][g]}==0" for g in range(G, T))
    lower_minus = " && ".join(f"{orientation['minus'][g]}==0" for g in range(G, T))
    lines += [
        f"poly {prefix}QplusRed=reduce(({qplus}),{prefix}RootIdeal);",
        f"poly {prefix}QminusRed=reduce(({qminus}),{prefix}RootIdeal);",
        f"int {prefix}dual_pair=({lower_plus} && {lower_minus} && {orientation['plus'][T]}-{prefix}QplusRed==0 && {orientation['minus'][T]}-{prefix}QminusRed==0);",
        f"poly {prefix}TargetFirewall=({prefix}SourcePhi1-{prefix}FullPhi1)+({prefix}SourcePhi3-{prefix}FullPhi3)+({prefix}SourcePhi4-{prefix}FullPhi4);",
        f"int {prefix}targetfree=(reduce({prefix}TargetFirewall,{prefix}ST)==0);",
        f"poly {prefix}Row2Target={prefix}FullPhi2-{prefix}SourcePhi2;",
        f"poly {prefix}Row2TargetExpected=-(sigma^28*({low.series('mu20', mu2max)}));",
        f"int {prefix}row2_target=({prefix}Row2Target-{prefix}Row2TargetExpected==0);",
        f"ideal {prefix}UnitC1=std(ideal({prefix}QplusRed,{prefix}QminusRed,ilam*lam-1,ic1*c1-1,ik0*k0-1));",
        f"ideal {prefix}UnitC0=std(ideal({prefix}QplusRed,{prefix}QminusRed,ilam*lam-1,ic0*c0-1,ik0*k0-1));",
        f"int {prefix}exact_contact_units=(reduce(1,{prefix}UnitC1)==0 && reduce(1,{prefix}UnitC0)==0);",
        f"int {prefix}endpoint={prefix}bridge*{prefix}quotients*{prefix}Root_exact*{prefix}root_constant*{prefix}first_tie*{prefix}rank2_off_delta*{prefix}recurrence*{prefix}dual_pair*{prefix}targetfree*{prefix}row2_target*{prefix}exact_contact_units;",
        f'print("{prefix}FIRST_WALL=C_TIMES_A_PLUS_K60_OVER_L");',
        f'print("{prefix}RANK_JUMP_DETERMINANT=c0^2+(p/2)*c1^2");',
        f'print("{prefix}LITERAL_ANALYTIC_BRIDGE="+string({prefix}bridge));',
        f'print("{prefix}ALL_SEVEN_QUOTIENTS="+string({prefix}quotients));',
        f'print("{prefix}MOVING_ROOT="+string({prefix}Root_exact*{prefix}root_constant));',
        f'print("{prefix}FIRST_TIED_COLUMN="+string({prefix}first_tie));',
        f'print("{prefix}RANK2_OFF_DELTA="+string({prefix}rank2_off_delta));',
        f'print("{prefix}POLE2_RECURRENCE="+string({prefix}recurrence));',
        f'print("{prefix}DUAL_LEFT_KERNEL_TARGET_PAIR="+string({prefix}dual_pair));',
        f'print("{prefix}TARGET_FREE_ROWS134="+string({prefix}targetfree));',
        f'print("{prefix}EXACT_CONTACT_CHART_UNITS="+string({prefix}exact_contact_units));',
        f'print("{prefix}ROW2_TARGET_RETAINED="+string({prefix}row2_target));',
        f'if ({prefix}endpoint!=1) {{ print("{prefix}FAIL=SOURCE_RANK_OR_DUAL_PAIR"); quit; }}',
        f'print("{prefix}ENDPOINT=PASS_EMPTY_A7_D{d}_CLOSED_R_TAIL");',
        "quit;",
    ]
    metadata = {
        "a": 7, "d": d, "c": 7 + d, "r_floor": 7, "G": G, "T": T,
        "primitive_count": len(primitive), "maxpole": 2,
        "jet_maxima": {"p": pmax, "A": amax, "C": cmax, "R": rmax,
                       "k10": k0max, "k6": k6max, "k2": k2max,
                       "mu2": mu2max, "mu4": mu4max},
        "primitive_columns": primitive,
    }
    return lines, metadata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    check(PINS)
    low = load(LOW, "d1_lowa6_frozen")
    low.check(low.PINS)
    base = low.load(low.BASE, "d1_a7_source_base")
    low.check(base.PINS)
    v1 = base.load_v1()
    low.check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()
    miner = low.load(low.MINER, "d1_a7_support_miner")
    output = args.output.resolve()
    if output.exists():
        fail("a7 load-tie output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    blocks = []
    input_shas = {}
    for d in (2, 3):
        lines, metadata = compile_block(args.characteristic, low, base, tail_base, tails, miner, d)
        target = output / f"square_d1_a7_loadtie_dual_functional_d{d}_{label}.sing"
        target.write_text("\n".join(lines) + "\n")
        input_shas[f"d{d}"] = digest(target)
        blocks.append(metadata)
    inventory = {
        "status": "PASS-D1-A7-LOADTIE-DUAL-FUNCTIONAL-COMPILER",
        "scope": "A7_D2_D3_ONLY_NO_A8_A9_OR_GLOBAL_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "blocks": blocks,
        "input_sha256": input_shas,
    }
    (output / "source_inventory.json").write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    print(json.dumps(inventory, sort_keys=True))


if __name__ == "__main__":
    main()
