#!/usr/bin/env python3
"""Compile the full D1 a=8,d=2 load-first split; AWS only."""

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
        fail("AWS-only a8 d2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a8 d2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def signature(item) -> tuple:
    return tuple(item[key] for key in (
        "summand", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient"
    ))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    check(PINS)

    low = load(LOW, "d1_a8d2_lowa6_frozen")
    low.check(low.PINS)
    base = low.load(low.BASE, "d1_a8d2_source_base")
    low.check(base.PINS)
    v1 = base.load_v1()
    low.check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()
    miner = low.load(low.MINER, "d1_a8d2_support_miner")

    a, d, c, r = 8, 2, 10, 8
    load_grade, G, T = 27, 28, 30
    row = {"a": a, "d": d, "c": c, "s_min": 0, "r": r,
           "first_ac_grade": G, "target_grade": T}
    primitive = miner.enumerate_primitives(row)
    padded = miner.enumerate_primitives(row, pad=1)
    if {miner.signature(x) for x in primitive} != {miner.signature(x) for x in padded}:
        fail("padded primitive mismatch")
    if len(primitive) != 6:
        fail(("primitive count", primitive))
    expected_first = {
        ("k6", "k6", 17, 0, 0, 1, 1, "3/4"),
    }
    if {signature(x) for x in primitive if int(x["first_grade"]) == load_grade} != expected_first:
        fail(("load-first inventory", primitive))
    pole_two = [x for x in primitive if int(x["pole"]) == 2]
    if len(pole_two) != 1 or signature(pole_two[0]) != (
        "unloaded", None, 10, 0, 0, 2, 2, "3/8"
    ) or int(pole_two[0]["first_grade"]) != T:
        fail(("sole pole-two target", pole_two))

    def depth(stem: str) -> int:
        if stem in ("A", "C", "R"):
            values = [T - int(x["first_grade"]) for x in primitive if int(x[stem]) > 0]
        else:
            values = [T - int(x["first_grade"]) for x in primitive if x["load"] == stem]
        return max(values, default=0)

    amax, cmax, rmax = depth("A"), depth("C"), depth("R")
    k0max, k6max, k2max = depth("k10"), depth("k6"), depth("k2")
    pmax = T - min(int(x["first_grade"]) for x in primitive)
    mu2max, mu4max = T - 28, 0

    variables = ["z", "t", "sigma", "p"]
    variables += [f"ell{j}" for j in range(1, pmax + 1)]
    for stem, maximum in (
        ("a1", amax), ("a0", amax), ("c1", cmax), ("c0", cmax),
        ("b1", rmax), ("b0", rmax), ("k0", k0max), ("k60", k6max),
        ("k20", k2max), ("mu20", mu2max), ("mu4", mu4max),
    ):
        variables += low.jets(stem, maximum)
    variables += ["mu6", "J", "lam"] + [f"rho{j}" for j in range(1, pmax + 1)]
    variables += ["ilam", "ic1", "ic0", "ik0", "ik60", "idelta"]
    variables = list(dict.fromkeys(variables))
    prefix = "A8D2_"
    lines = [
        f"ring {prefix}R={args.characteristic},({','.join(variables)}),dp;",
        'print("A8D2_BASELINE=A8_D2_RGE8_LOAD27_T30");',
        'print("A8D2_PRIMITIVE_COLUMNS=6");',
        'print("A8D2_GLOBAL_POLE_CEILING=2");',
    ]
    pseries = "p" + "".join(f"+2*sigma^{j}*ell{j}" for j in range(1, pmax + 1))
    P = f"{prefix}P"
    lines.append(f"poly {P}={pseries};")
    A = f"sigma^8*(({low.series('a1', amax)})+t*({low.series('a0', amax)}))"
    C = f"sigma^10*(({low.series('c1', cmax)})+t*({low.series('c0', cmax)}))"
    R = f"sigma^8*(({low.series('b1', rmax)})+t*({low.series('b0', rmax)}))"
    loads = {
        "k10": low.series("k0", k0max),
        "k6": low.series("k60", k6max),
        "k2": low.series("k20", k2max),
    }
    inv = {q: low.inv_series(q, P) for q in (1, 2)}
    hterms = []
    for item in primitive:
        q = int(item["pole"])
        eR, eA, eC = (int(item[x]) for x in ("R", "A", "C"))
        tpower = 1 + 2 * q - eR - eA - eC
        if tpower < 0:
            fail(("improper primitive", item))
        factors = [low.frac(str(item["coefficient"])), f"sigma^{int(item['fixed_sigma'])}"]
        if item["load"] is not None:
            factors.append(f"({loads[str(item['load'])]})")
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

    pp = f"({P})"
    coeffs = base.source_coefficients(
        pp, f"sigma^8*({low.series('a1', amax)})", f"sigma^8*({low.series('a0', amax)})",
        f"sigma^10*({low.series('c1', cmax)})", f"sigma^10*({low.series('c0', cmax)})",
        f"sigma^8*({low.series('b1', rmax)})", f"sigma^8*({low.series('b0', rmax)})",
    )
    literal_loads = {key: f"({value})" for key, value in loads.items()}
    targets = {1: "0", 2: low.series("mu20", mu2max), 3: "0",
               4: low.series("mu4", mu4max), 5: "0", 6: "mu6", 7: "J/4"}
    for j in range(1, 8):
        source = low.source_row(tail_base, tails, j, coeffs, literal_loads)
        target = "0" if targets[j] == "0" else f"sigma^{2*(12+j)}*({targets[j]})"
        lines += [f"poly {prefix}SourcePhi{j}={source};",
                  f"poly {prefix}FullPhi{j}={prefix}SourcePhi{j}-({target});"]
    predicted = {
        1: f"{prefix}h1", 2: f"{prefix}h2",
        3: f"{prefix}h3+({P}/4)*{prefix}h1",
        4: f"{prefix}h4+({P}/2)*{prefix}h2",
        5: f"{prefix}h5+(3*{P}/4)*{prefix}h3+(3*({P}^2)/32)*{prefix}h1",
        6: f"{prefix}h6+{P}*{prefix}h4+(({P}^2)/4)*{prefix}h2",
        7: f"{prefix}h7+(5*{P}/4)*{prefix}h5+(15*({P}^2)/32)*{prefix}h3+(5*({P}^3)/128)*{prefix}h1",
    }
    lines += [f"ideal {prefix}ST=std(ideal(sigma^{T+1}));", f"int {prefix}bridge=1;"]
    for j in range(1, 8):
        lines += [f"poly {prefix}PredPhi{j}={predicted[j]};",
                  f"if (reduce({prefix}SourcePhi{j}-{prefix}PredPhi{j},{prefix}ST)!=0) {{ {prefix}bridge=0; }}"]
    for j in range(1, 8):
        low.sigma_extract(lines, f"{prefix}FullPhi{j}", f"{prefix}F{j}_", load_grade, T)
    lines.append(f"int {prefix}quotients=" + "*".join(f"{prefix}F{j}_exact" for j in range(1, 8)) + ";")

    load_h1 = low.sigma_extract(lines, f"{prefix}h1", f"{prefix}LH1_", load_grade, load_grade)[load_grade]
    load_h2 = low.sigma_extract(lines, f"{prefix}h2", f"{prefix}LH2_", load_grade, load_grade)[load_grade]
    lines += [
        f"int {prefix}load_first=({load_h1}-(3/4)*k60*c1==0 && {load_h2}-(3/4)*k60*c0==0);",
        f"ideal {prefix}Dk60C1=std(ideal({load_h1},{load_h2},ik60*k60-1,ic1*c1-1));",
        f"ideal {prefix}Dk60C0=std(ideal({load_h1},{load_h2},ik60*k60-1,ic0*c0-1));",
        f"int {prefix}dk60_units=(reduce(1,{prefix}Dk60C1)==0 && reduce(1,{prefix}Dk60C0)==0);",
    ]

    root = "lam" + "".join(f"+sigma^{j}*rho{j}" for j in range(1, pmax + 1))
    root_coeffs = low.sigma_extract(lines, f"(({root})^2+({P}/2))", f"{prefix}Root_", 0, pmax)
    lines += [
        f"int {prefix}root_constant=({root_coeffs[0]}==p/2+lam^2);",
        f"ideal {prefix}RootK0=std(ideal(" + ",".join(root_coeffs[g] for g in range(1, pmax + 1)) + ",k60,ilam*lam-1));",
    ]
    first_h1 = low.sigma_extract(lines, f"{prefix}h1", f"{prefix}GH1_", G, G)[G]
    first_h2 = low.sigma_extract(lines, f"{prefix}h2", f"{prefix}GH2_", G, G)[G]
    lines += [
        f"poly {prefix}FirstRz=a1*c0+(a0+k60_1)*c1;",
        f"poly {prefix}FirstR0=(a0+k60_1)*c0-(p/2)*a1*c1;",
        f"int {prefix}first_tie=(reduce({first_h1}-(3/4)*{prefix}FirstRz,{prefix}RootK0)==0 && reduce({first_h2}-(3/4)*{prefix}FirstR0,{prefix}RootK0)==0);",
        f"poly {prefix}DeltaC=c0^2+(p/2)*c1^2;",
        f"ideal {prefix}Rank2=std(ideal({prefix}FirstRz,{prefix}FirstR0,k60,idelta*{prefix}DeltaC-1));",
        f"int {prefix}rank2_off_delta=(reduce(a1,{prefix}Rank2)==0 && reduce(a0+k60_1,{prefix}Rank2)==0);",
        f"poly {prefix}Rec5={prefix}h5+{P}*{prefix}h3+(({P}^2)/4)*{prefix}h1;",
        f"poly {prefix}Rec6={prefix}h6+{P}*{prefix}h4+(({P}^2)/4)*{prefix}h2;",
        f"poly {prefix}Rec7={prefix}h7+{P}*{prefix}h5+(({P}^2)/4)*{prefix}h3;",
        f"int {prefix}recurrence=(reduce({prefix}Rec5,{prefix}ST)==0 && reduce({prefix}Rec6,{prefix}ST)==0 && reduce({prefix}Rec7,{prefix}ST)==0);",
    ]
    functional = f"({prefix}SourcePhi3+({P}/4)*{prefix}SourcePhi1)"
    orientations = {}
    for sign, label_name in ((1, "plus"), (-1, "minus")):
        signed_root = root if sign == 1 else f"-({root})"
        name = f"{prefix}Psi_{label_name}"
        lines += [f"poly {name}={prefix}SourcePhi4+({signed_root})*{functional};",
                  f"{name}=subst({name},p,-2*lam^2);",
                  f"poly {name}Red=reduce({name},{prefix}RootK0);"]
        orientations[label_name] = low.sigma_extract(lines, f"{name}Red", f"{name}_", G, T)
    qplus = "(3/8)*(c1*lam+c0)^2"
    qminus = "(3/8)*(-c1*lam+c0)^2"
    lower_plus = " && ".join(f"{orientations['plus'][g]}==0" for g in range(G, T))
    lower_minus = " && ".join(f"{orientations['minus'][g]}==0" for g in range(G, T))
    lines += [
        f"poly {prefix}Qplus=reduce(({qplus}),{prefix}RootK0);",
        f"poly {prefix}Qminus=reduce(({qminus}),{prefix}RootK0);",
        f"int {prefix}dual_pair=({lower_plus} && {lower_minus} && {orientations['plus'][T]}-{prefix}Qplus==0 && {orientations['minus'][T]}-{prefix}Qminus==0);",
        f"ideal {prefix}UnitC1=std(ideal({prefix}Qplus,{prefix}Qminus,k60,ilam*lam-1,ic1*c1-1,ik0*k0-1));",
        f"ideal {prefix}UnitC0=std(ideal({prefix}Qplus,{prefix}Qminus,k60,ilam*lam-1,ic0*c0-1,ik0*k0-1));",
        f"int {prefix}vk60_units=(reduce(1,{prefix}UnitC1)==0 && reduce(1,{prefix}UnitC0)==0);",
        f"poly {prefix}Target134=({prefix}SourcePhi1-{prefix}FullPhi1)+({prefix}SourcePhi3-{prefix}FullPhi3)+({prefix}SourcePhi4-{prefix}FullPhi4);",
        f"int {prefix}targetfree134=(reduce({prefix}Target134,{prefix}ST)==0);",
        f"poly {prefix}Row2Target={prefix}FullPhi2-{prefix}SourcePhi2;",
        f"poly {prefix}Row2Expected=-(sigma^28*({low.series('mu20', mu2max)}));",
        f"int {prefix}row2_target=({prefix}Row2Target-{prefix}Row2Expected==0);",
        f"int {prefix}endpoint={prefix}bridge*{prefix}quotients*{prefix}load_first*{prefix}dk60_units*{prefix}Root_exact*{prefix}root_constant*{prefix}first_tie*{prefix}rank2_off_delta*{prefix}recurrence*{prefix}dual_pair*{prefix}vk60_units*{prefix}targetfree134*{prefix}row2_target;",
        f'print("A8D2_LITERAL_ANALYTIC_BRIDGE="+string({prefix}bridge));',
        f'print("A8D2_ALL_SEVEN_QUOTIENTS="+string({prefix}quotients));',
        f'print("A8D2_DK60_LOAD_FIRST="+string({prefix}load_first));',
        f'print("A8D2_DK60_EXACT_C_CHART_UNITS="+string({prefix}dk60_units));',
        f'print("A8D2_VK60_MOVING_ROOT="+string({prefix}Root_exact*{prefix}root_constant));',
        f'print("A8D2_VK60_FIRST_TIE="+string({prefix}first_tie));',
        f'print("A8D2_VK60_RANK2_OFF_DELTA="+string({prefix}rank2_off_delta));',
        f'print("A8D2_POLE2_RECURRENCE="+string({prefix}recurrence));',
        f'print("A8D2_VK60_DUAL_TARGET_PAIR="+string({prefix}dual_pair));',
        f'print("A8D2_VK60_EXACT_C_CHART_UNITS="+string({prefix}vk60_units));',
        f'print("A8D2_TARGET_FREE_ROWS134="+string({prefix}targetfree134));',
        f'print("A8D2_ROW2_TARGET_RETAINED="+string({prefix}row2_target));',
        f'if ({prefix}endpoint!=1) {{ print("A8D2_FAIL=SOURCE_SPLIT_OR_DUAL_PAIR"); quit; }}',
        'print("A8D2_ENDPOINT=PASS_EMPTY_A8_D2_CLOSED_R_TAIL");',
        "quit;",
    ]

    output = args.output.resolve()
    if output.exists():
        fail("a8 d2 output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    script = output / f"square_d1_a8_d2_loadfirst_dual_{label}.sing"
    script.write_text("\n".join(lines) + "\n")
    inventory = {
        "status": "PASS-D1-A8-D2-LOADFIRST-DUAL-COMPILER",
        "scope": "A8_D2_ONLY_NO_A8D3_A9_OR_GLOBAL_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "block": {**row, "load_grade": load_grade, "primitive_count": len(primitive),
                  "primitive_columns": primitive,
                  "jet_maxima": {"p": pmax, "A": amax, "C": cmax, "R": rmax,
                                  "k10": k0max, "k6": k6max, "k2": k2max,
                                  "mu2": mu2max, "mu4": mu4max}},
        "input_sha256": digest(script),
    }
    (output / "source_inventory.json").write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    print(json.dumps(inventory, sort_keys=True))


if __name__ == "__main__":
    main()
