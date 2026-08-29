#!/usr/bin/env python3
"""Compile the complete low-a D1 d=2,3 local-row producer; AWS only."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py"
BASE_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/FREEZE.sha256"
MINER_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826"
MINER = MINER_DIR / "mine_support.py"
PINS = {
    BASE: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    BASE_FREEZE: "34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6",
    MINER: "0e94e5408b8a3b5db06c8eff5c759df1c75a2e8bb4563aa4964f42c39952fe9a",
    MINER_DIR / "RESULT.md": "613a8fe989b8c1c34c5c6d3846054df52414bfebd172a56567bacb74e503455f",
    MINER_DIR / "PRODUCER_FREEZE.sha256": "97f66090720b6c26728af1b9d3a3ba6516f934507aa0f3209cda830e10dd4d4f",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 d23 low-a compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 d23 low-a compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


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


def frac(value: Fraction | str | int) -> str:
    q = value if isinstance(value, Fraction) else Fraction(value)
    return str(q.numerator) if q.denominator == 1 else f"({q.numerator}/{q.denominator})"


def jets(stem: str, maximum: int) -> list[str]:
    return [stem] + [f"{stem}_{j}" for j in range(1, maximum + 1)]


def series(stem: str, maximum: int) -> str:
    return "+".join(stem if j == 0 else f"sigma^{j}*{stem}_{j}" for j in range(maximum + 1))


def inv_series(q: int, pseries: str) -> str:
    # Enough t-depth for all seven literal rows.  Extra terms are harmless.
    terms = []
    for j in range(5):
        coefficient = Fraction((-1) ** j * math.comb(q + j - 1, j), 1)
        term = frac(coefficient)
        if j:
            term += f"*(({pseries})/2)^{j}*t^{2*j}"
        terms.append(term)
    return "(" + "+".join(terms).replace("+-", "-") + ")"


def t_coefficient(lines: list[str], source: str, name: str, degree: int) -> None:
    previous = source
    for j in range(1, degree + 1):
        current = f"{name}_D{j}"
        lines.append(f"poly {current}=diff({previous},t);")
        previous = current
    lines.append(f"poly {name}=subst({previous},t,0)/{math.factorial(degree)};")


def sigma_extract(lines: list[str], source: str, prefix: str, minimum: int, maximum: int) -> dict[int, str]:
    result: dict[int, str] = {}
    lines += [f"poly {prefix}Q{minimum}={source}/sigma^{minimum};",
              f"int {prefix}exact=(sigma^{minimum}*{prefix}Q{minimum}-{source}==0);"]
    for grade in range(minimum, maximum + 1):
        qname = f"{prefix}Q{grade}"
        gname = f"{prefix}g{grade}"
        result[grade] = gname
        lines.append(f"poly {gname}=subst({qname},sigma,0);")
        if grade < maximum:
            rem = f"{prefix}Rem{grade+1}"
            lines += [f"poly {rem}={qname}-{gname};",
                      f"if (reduce({rem},ideal(sigma))!=0) {{ {prefix}exact=0; }}",
                      f"poly {prefix}Q{grade+1}={rem}/sigma;"]
    return result


def source_row(tail_base, tails, row: int, coeffs, loads) -> str:
    return tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")


def block(characteristic: int, base, v1, tail_base, tails, miner, a: int, d: int) -> tuple[list[str], dict]:
    smin = 1 if a <= d else 0
    r = a + smin
    G = 10 + 2 * a + d
    T = G + d
    row = {"a": a, "d": d, "c": a + d, "s_min": smin, "r": r,
           "first_ac_grade": G, "target_grade": T}
    primitive = miner.enumerate_primitives(row)
    padded = miner.enumerate_primitives(row, pad=1)
    sig = miner.signature
    if {sig(x) for x in primitive} != {sig(x) for x in padded}:
        fail(("padded inventory mismatch", row))
    first = [x for x in primitive if int(x["first_grade"]) == G]
    ac_signature = ("unloaded", None, 10, 0, 1, 1, 1, "3/4")
    if len(first) != 1 or tuple(first[0][key] for key in (
        "summand", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient"
    )) != ac_signature:
        fail(("AC is not unique first primitive", row, first))
    negative = a == 1 and d == 3
    maxpole = max(int(x["pole"]) for x in primitive)
    if maxpole != (3 if negative else 2):
        fail(("unexpected pole ceiling", row, maxpole))
    dangerous = [x for x in primitive if int(x["local_pole_upper_at_A_root"]) >= 2]
    if len(dangerous) != (2 if negative else 1):
        fail(("dangerous family count", row, dangerous))

    def depth_with(stem: str) -> int:
        if stem in ("A", "C", "R"):
            candidates = [T - int(x["first_grade"]) for x in primitive if int(x[stem]) > 0]
        else:
            candidates = [T - int(x["first_grade"]) for x in primitive if x["load"] == stem]
        return max(candidates, default=0)

    amax, cmax, rmax = depth_with("A"), depth_with("C"), depth_with("R")
    k0max, k6max, k2max = depth_with("k10"), depth_with("k6"), depth_with("k2")
    pmax = T - min(int(x["first_grade"]) for x in primitive)
    rootmax = pmax
    mu2max, mu4max = max(T - 28, 0), max(T - 32, 0)

    variables = ["z", "t", "sigma", "p"]
    variables += [f"ell{j}" for j in range(1, pmax + 1)]
    for stem, maximum in (("a1", amax), ("a0", amax), ("c1", cmax), ("c0", cmax),
                          ("b1", rmax), ("b0", rmax), ("k0", k0max),
                          ("k60", k6max), ("k20", k2max), ("mu20", mu2max),
                          ("mu4", mu4max)):
        variables += jets(stem, maximum)
    variables += ["mu6", "J", "lam"] + [f"rho{j}" for j in range(1, rootmax + 1)]
    variables += ["au", "cv", "ilam", "icv", "ik0"]
    # Stable de-duplication is important where a zero ceiling still introduces a stem.
    variables = list(dict.fromkeys(variables))
    prefix = f"B{a}{d}_"
    lines = [f"ring {prefix}R={characteristic},({','.join(variables)}),dp;",
             f'print("{prefix}BASELINE=A{a}_D{d}_S{smin}_G{G}_T{T}");',
             f'print("{prefix}PRIMITIVE_COUNT={len(primitive)}");',
             f'print("{prefix}GLOBAL_POLE_CEILING={maxpole}");']
    pseries = "p" + "".join(f"+2*sigma^{j}*ell{j}" for j in range(1, pmax + 1))
    pname = f"{prefix}P"
    lines.append(f"poly {pname}={pseries};")
    A = f"sigma^{a}*(({series('a1', amax)})+t*({series('a0', amax)}))"
    C = f"sigma^{a+d}*(({series('c1', cmax)})+t*({series('c0', cmax)}))"
    R = f"sigma^{r}*(({series('b1', rmax)})+t*({series('b0', rmax)}))"
    load_series = {"k10": series("k0", k0max), "k6": series("k60", k6max),
                   "k2": series("k20", k2max)}
    inv = {q: inv_series(q, pname) for q in range(1, maxpole + 1)}
    hterms = []
    ra2_hterm = None
    for item in primitive:
        q = int(item["pole"])
        eR, eA, eC = (int(item[x]) for x in ("R", "A", "C"))
        tpower = 1 + 2 * q - eR - eA - eC
        if tpower < 0:
            fail(("improper primitive", row, item))
        factors = [frac(str(item["coefficient"])), f"sigma^{int(item['fixed_sigma'])}"]
        if item["load"] is not None:
            factors.append(f"({load_series[str(item['load'])]})")
        if tpower:
            factors.append(f"t^{tpower}")
        for expression, exponent in ((R, eR), (A, eA), (C, eC)):
            if exponent:
                factors.append(f"({expression})^{exponent}")
        factors.append(inv[q])
        hterm = "*".join(factors)
        hterms.append(hterm)
        if (eR, eA, eC, q, str(item["coefficient"])) == (1, 2, 0, 2, "-3/8"):
            ra2_hterm = hterm
    lines.append(f"poly {prefix}H=" + "+".join(hterms).replace("+-", "-") + ";")
    for j in range(1, 8):
        t_coefficient(lines, f"{prefix}H", f"{prefix}h{j}", j + 1)

    pp = f"({pname})"
    coeffs = base.source_coefficients(
        pp, f"sigma^{a}*({series('a1', amax)})", f"sigma^{a}*({series('a0', amax)})",
        f"sigma^{a+d}*({series('c1', cmax)})", f"sigma^{a+d}*({series('c0', cmax)})",
        f"sigma^{r}*({series('b1', rmax)})", f"sigma^{r}*({series('b0', rmax)})",
    )
    loads = {"k10": f"({load_series['k10']})", "k6": f"({load_series['k6']})",
             "k2": f"({load_series['k2']})"}
    targets = {1: "0", 2: series("mu20", mu2max), 3: "0", 4: series("mu4", mu4max),
               5: "0", 6: "mu6", 7: "J/4"}
    source_names, full_names = [], []
    for j in range(1, 8):
        source = source_row(tail_base, tails, j, coeffs, loads)
        target = "0" if targets[j] == "0" else f"sigma^{2*(12+j)}*({targets[j]})"
        lines += [f"poly {prefix}SourcePhi{j}={source};",
                  f"poly {prefix}FullPhi{j}={prefix}SourcePhi{j}-({target});"]
        source_names.append(f"{prefix}SourcePhi{j}")
        full_names.append(f"{prefix}FullPhi{j}")
    predicted = {
        1: f"{prefix}h1",
        2: f"{prefix}h2",
        3: f"{prefix}h3+({pname}/4)*{prefix}h1",
        4: f"{prefix}h4+({pname}/2)*{prefix}h2",
        # Singular parses ``P^2/32`` as ``P^(2/32)``.  Parenthesize every
        # powered numerator before rational division.
        5: f"{prefix}h5+(3*{pname}/4)*{prefix}h3+(3*({pname}^2)/32)*{prefix}h1",
        6: f"{prefix}h6+{pname}*{prefix}h4+(({pname}^2)/4)*{prefix}h2",
        7: f"{prefix}h7+(5*{pname}/4)*{prefix}h5+(15*({pname}^2)/32)*{prefix}h3+(5*({pname}^3)/128)*{prefix}h1",
    }
    lines += [f"ideal {prefix}ST=std(ideal(sigma^{T+1}));", f"int {prefix}bridge=1;"]
    for j in range(1, 8):
        lines += [f"poly {prefix}PredPhi{j}={predicted[j]};",
                  f"if (reduce({prefix}SourcePhi{j}-{prefix}PredPhi{j},{prefix}ST)!=0) {{ {prefix}bridge=0; }}"]
    # Extract every full row and certify all recursive quotient identities.
    extracted = []
    for j in range(1, 8):
        extracted.append(sigma_extract(lines, f"{prefix}FullPhi{j}", f"{prefix}F{j}_", G, T))
    lines.append(f"int {prefix}quotients=" + "*".join(f"{prefix}F{j}_exact" for j in range(1, 8)) + ";")

    root = "lam" + "".join(f"+sigma^{j}*rho{j}" for j in range(1, rootmax + 1))
    rootpoly = f"({root})^2+({pname}/2)"
    root_coeff_names = []
    root_extract = sigma_extract(lines, rootpoly, f"{prefix}Root_", 0, rootmax)
    lines.append(f"int {prefix}root_constant=({root_extract[0]}==p/2+lam^2);")
    for grade in range(1, rootmax + 1):
        root_coeff_names.append(root_extract[grade])
    root_ideal_generators = root_coeff_names + ["ilam*lam-1"]
    lines.append(f"ideal {prefix}RootIdeal=std(ideal({','.join(root_ideal_generators)}));")

    # Unique first AC numerator and the two etale orientations.
    first_h = {}
    for j in range(1, 5):
        first_h[j] = sigma_extract(lines, f"{prefix}h{j}", f"{prefix}H{j}_", G, G)[G]
    lines += [f"poly {prefix}Nfirst={first_h[1]}*z+{first_h[2]};",
              f"poly {prefix}NfirstExpected=(3/4)*((a1*c0+a0*c1)*z+a0*c0-(p/2)*a1*c1);",
              f"int {prefix}firstAC=({prefix}Nfirst-{prefix}NfirstExpected==0);"]

    if not negative:
        lines += [
            f"poly {prefix}N2={prefix}h1*z^3+{prefix}h2*z^2+({prefix}h3+{pname}*{prefix}h1)*z+({prefix}h4+{pname}*{prefix}h2);",
            f"poly {prefix}Rec5={prefix}h5+{pname}*{prefix}h3+(({pname}^2)/4)*{prefix}h1;",
            f"poly {prefix}Rec6={prefix}h6+{pname}*{prefix}h4+(({pname}^2)/4)*{prefix}h2;",
            f"poly {prefix}Rec7={prefix}h7+{pname}*{prefix}h5+(({pname}^2)/4)*{prefix}h3;",
            f"int {prefix}recurrence=(reduce({prefix}Rec5,{prefix}ST)==0 && reduce({prefix}Rec6,{prefix}ST)==0 && reduce({prefix}Rec7,{prefix}ST)==0);",
        ]
        orientation_results = []
        for sign, label in ((1, "plus"), (-1, "minus")):
            root_signed = root if sign == 1 else f"-({root})"
            a0image = "-au*lam" if sign == 1 else "au*lam"
            c0image = "cv*lam" if sign == 1 else "-cv*lam"
            psi = f"{prefix}SourcePhi4+({root_signed})*({prefix}SourcePhi3+({pname}/4)*{prefix}SourcePhi1)"
            evalname = f"{prefix}Psi_{label}"
            lines += [f"poly {evalname}={psi};",
                      f"{evalname}=subst({evalname},p,-2*lam^2);",
                      f"{evalname}=subst({evalname},a1,au); {evalname}=subst({evalname},a0,{a0image});",
                      f"{evalname}=subst({evalname},c1,cv); {evalname}=subst({evalname},c0,{c0image});",
                      f"poly {evalname}Red=reduce({evalname},{prefix}RootIdeal);"]
            coeffs_eval = sigma_extract(lines, f"{evalname}Red", f"{evalname}_", G, T)
            lower_zero = " && ".join(f"{coeffs_eval[g]}==0" for g in range(G, T)) or "1"
            result = f"{prefix}orient_{label}"
            lines.append(f"int {result}=(({lower_zero}) && {coeffs_eval[T]}-(3/2)*lam^2*cv^2==0);")
            orientation_results.append(result)
        # The same functional made from full rows differs only by the row-4 target,
        # which starts after every positive ceiling here.
        lines += [f"poly {prefix}TargetFirewall={prefix}SourcePhi4-{prefix}FullPhi4;",
                  f"int {prefix}targetfree=(reduce({prefix}TargetFirewall,{prefix}ST)==0);",
                  f"ideal {prefix}Unit=std(ideal((3/2)*lam^2*cv^2,ilam*lam-1,icv*cv-1,ik0*k0-1));",
                  f"int {prefix}unit=(reduce(1,{prefix}Unit)==0);",
                  f"int {prefix}endpoint={prefix}bridge*{prefix}quotients*{prefix}root_constant*{prefix}firstAC*{prefix}recurrence*{prefix}targetfree*{orientation_results[0]}*{orientation_results[1]}*{prefix}unit;",
                  f'print("{prefix}MOVING_L2_RECURRENCE="+string({prefix}recurrence));',
                  f'print("{prefix}TARGET_FREE_LOCAL_ROWS="+string({prefix}targetfree));',
                  f'print("{prefix}BOTH_ORIENTATIONS="+string({orientation_results[0]}*{orientation_results[1]}));',
                  f'print("{prefix}LOCAL_COEFFICIENT=3/2*lam^2*cv^2");',
                  f'if ({prefix}endpoint!=1) {{ print("{prefix}FAIL=BRIDGE_ROOT_OR_LOCAL_ROW"); quit; }}',
                  f'print("{prefix}ENDPOINT=PASS_EMPTY_CLOSED_R_TAIL");']
    else:
        # E must retain both local double-pole families and refuse the L2 endpoint.
        dangerous_signatures = {(x["R"], x["A"], x["C"], x["coefficient"]) for x in dangerous}
        if dangerous_signatures != {(0, 0, 2, "3/8"), (1, 2, 0, "-3/8")}:
            fail(("E dangerous signatures", dangerous_signatures))
        if ra2_hterm is None:
            fail("E is missing the RA2 analytic primitive")
        # This is a genuine local coefficient check, not only an inventory
        # sentinel.  For E the RA2 primitive starts in grade 16.  At the
        # A-allocated moving root its first two numerator coefficients vanish,
        # while the grade-18 coefficient is the square of the first corrected
        # value of A at that root, multiplied by the leading value of R.
        lines += [f"poly {prefix}HRA2={ra2_hterm};"]
        for j in range(1, 5):
            t_coefficient(lines, f"{prefix}HRA2", f"{prefix}RA2h{j}", j + 1)
        lines += [
            f"poly {prefix}RA2N2={prefix}RA2h1*z^3+{prefix}RA2h2*z^2+({prefix}RA2h3+{pname}*{prefix}RA2h1)*z+({prefix}RA2h4+{pname}*{prefix}RA2h2);",
            f"poly {prefix}RA2AtRoot=subst({prefix}RA2N2,z,{root});",
            f"{prefix}RA2AtRoot=subst({prefix}RA2AtRoot,p,-2*lam^2);",
            f"{prefix}RA2AtRoot=subst({prefix}RA2AtRoot,a1,au); {prefix}RA2AtRoot=subst({prefix}RA2AtRoot,a0,-au*lam);",
            f"poly {prefix}RA2AtRootRed=reduce({prefix}RA2AtRoot,{prefix}RootIdeal);",
        ]
        ra2_coeffs = sigma_extract(lines, f"{prefix}RA2AtRootRed", f"{prefix}RA2Local_", 16, 18)
        ra2_expected = f"(-3/8)*(b1*lam+b0)*(lam*a1_1+a0_1+au*rho1)^2"
        lines += [
            f"poly {prefix}RA2ExpectedRed=reduce(({ra2_expected}),{prefix}RootIdeal);",
            f"int {prefix}ra2_second_correction=({ra2_coeffs[16]}==0 && {ra2_coeffs[17]}==0 && {ra2_coeffs[18]}-{prefix}RA2ExpectedRed==0);",
            f"int {prefix}negative_inventory={prefix}ra2_second_correction;",
                  f"int {prefix}endpoint={prefix}bridge*{prefix}quotients*{prefix}root_constant*{prefix}firstAC*{prefix}negative_inventory;",
                  f'print("{prefix}NEGCTRL_C2_AND_RA2_LOCAL_DOUBLE=1");',
                  f'print("{prefix}NEGCTRL_RA2_SECOND_CORRECTION="+string({prefix}ra2_second_correction));',
                  f'print("{prefix}NEGCTRL_GLOBAL_POLE3=1");',
                  f'if ({prefix}endpoint!=1) {{ print("{prefix}FAIL=NEGATIVE_CONTROL_BRIDGE"); quit; }}',
                  f'print("{prefix}ENDPOINT=PASS_ROUTE_DEDICATED_E_SUCCESSOR_NO_EMPTY_VERDICT");']

    metadata = {"a": a, "d": d, "s_min": smin, "r_floor": r, "G": G, "T": T,
                "negative": negative, "primitive_count": len(primitive), "maxpole": maxpole,
                "jet_maxima": {"p": pmax, "A": amax, "C": cmax, "R": rmax,
                               "k10": k0max, "k6": k6max, "k2": k2max,
                               "mu2": mu2max, "mu4": mu4max}}
    return lines, metadata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    check(PINS)
    base = load(BASE, "d1_low_local_base")
    check(base.PINS)
    v1 = base.load_v1()
    check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()
    miner = load(MINER, "d1_d23_support_miner")
    output = args.output.resolve()
    if output.exists():
        fail("D1 d23 low-a output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_unique_ac_d23_lowa6_local_row_{label}.sing"
    lines: list[str] = []
    blocks = []
    for a in range(1, 7):
        for d in (2, 3):
            section, metadata = block(args.characteristic, base, v1, tail_base, tails, miner, a, d)
            lines += section
            blocks.append(metadata)
    if sum(not x["negative"] for x in blocks) != 11 or sum(x["negative"] for x in blocks) != 1:
        fail("block partition mismatch")
    lines += ['print("D1D23_LOWA6_POSITIVE_BLOCKS=11");',
              'print("D1D23_LOWA6_NEGATIVE_BLOCKS=1");',
              'print("D1D23_LOWA6_E_CONTROL=A1_D3_S1");',
              'print("D1D23_LOWA6_HIGH_ROUTING=A7_TIE_A8_A9_LOAD_FIRST_EXCLUDED");',
              'print("D1D23_LOWA6_ENDPOINT=PASS_ELEVEN_EMPTY_ONE_ROUTED");', "quit;"]
    target.write_text("\n".join(lines) + "\n")
    inventory = {"status": "PASS-D1-D23-LOWA6-LOCAL-ROW-COMPILER",
                 "scope": "ELEVEN_LOW_A_CLOSED_R_TAILS_PLUS_E_NEGATIVE_NO_HIGH_A_OR_GLOBAL_VERDICT",
                 "registered_aws_lane": tag, "characteristic": args.characteristic,
                 "blocks": blocks, "input_sha256": digest(target)}
    inventory_path = output / "source_inventory.json"
    inventory_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    print(json.dumps(inventory, sort_keys=True))


if __name__ == "__main__":
    main()
