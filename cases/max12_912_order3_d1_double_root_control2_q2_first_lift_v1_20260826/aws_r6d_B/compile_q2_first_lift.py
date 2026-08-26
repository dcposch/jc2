#!/usr/bin/env python3
"""AWS-only exact compiler for the first omitted q2 witness layer."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHARGED = (
    ROOT / "cases" /
    "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
    "independent_reconstruct.py"
)
CHARGED_SHA = "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"
PINNED_B = (
    ROOT / "cases" /
    "max12_912_order3_d1_double_root_control2_la20_syzygy_20260826" /
    "base_B.sing"
)
PINNED_B_SHA = "c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b"

NAMES = ("la", "tau", "rho", "q2", "q1", "q0", "r2", "r1", "r0")
INDEX = {name: i for i, name in enumerate(NAMES)}
ZERO = (0,) * len(NAMES)


class CompileFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_q2_first_lift_v1_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_charged():
    if sha256(CHARGED.read_bytes()).hexdigest() != CHARGED_SHA:
        raise CompileFailure("charged source hash")
    spec = importlib.util.spec_from_file_location("q2_lift_charged", CHARGED)
    if spec is None or spec.loader is None:
        raise CompileFailure("charged import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(p):
    return {m: c for m, c in p.items() if c}


def add(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Fraction(0)) + c
    return clean(out)


def scale(c, p):
    c = Fraction(c)
    return clean({m: c * v for m, v in p.items()})


def mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, Fraction(0)) + ca * cb
    return clean(out)


def const(c):
    c = Fraction(c)
    return {} if not c else {ZERO: c}


def mon(c=1, **powers):
    e = [0] * len(NAMES)
    for name, power in powers.items():
        if name not in INDEX or not isinstance(power, int) or power < 0:
            raise CompileFailure(("bad monomial", name, power))
        e[INDEX[name]] = power
    c = Fraction(c)
    return {} if not c else {tuple(e): c}


def powers(image, maximum):
    out = [const(1)]
    for _ in range(maximum):
        out.append(mul(out[-1], image))
    return out


def coefficient_images():
    q2, q1, q0 = mon(q2=1), mon(q1=1), mon(q0=1)
    r2, r1, r0 = mon(r2=1), mon(r1=1), mon(r0=1)
    return (
        add(add(const(8), scale(2, q0)), r0),
        add(add(const(-36), add(scale(-3, q0), scale(2, q1))), r1),
        add(add(add(const(54), scale(-3, q1)), scale(2, q2)), r2),
        add(add(const(-15), q0), scale(-3, q2)),
        add(const(-36), q1),
        add(const(27), q2),
        const(6),
        const(-9),
        {},
    )


def substitute(source, images):
    maxima = [0] * len(images)
    for m in source:
        for i, e in enumerate(m):
            maxima[i] = max(maxima[i], e)
    table = [powers(image, maximum) for image, maximum in zip(images, maxima)]
    out = {}
    for source_m, coefficient in source.items():
        term = const(coefficient)
        for i, e in enumerate(source_m):
            term = mul(term, table[i][e])
            if not term:
                break
        out = add(out, term)
    return clean(out)


def target(ell):
    if ell == 3:
        return mon(Fraction(2, 3), la=15)
    if ell == 8:
        return add(mon(la=20), mon(la=20, tau=1))
    return {}


def multipliers():
    return {
        1: add(add(add(add(add(mon(Fraction(1, 108), q1=2),
                              mon(Fraction(-7, 72), r2=1)),
                          mon(Fraction(1, 8), r1=1)),
                      mon(Fraction(-5, 18), q1=1)),
                  mon(Fraction(1, 8), q0=1)), const(Fraction(115, 24))),
        2: add(add(mon(Fraction(1, 12), q1=1),
                   mon(Fraction(-5, 36), q0=1)), const(Fraction(-29, 9))),
        3: {},
        4: add(mon(Fraction(-1, 24), q1=1), const(Fraction(3, 2))),
        5: add(mon(Fraction(-1, 24), q0=1), const(Fraction(-25, 24))),
        6: mon(Fraction(1, 24), q1=1),
        7: const(Fraction(3, 8)),
        8: const(-1),
    }


def old_witness():
    out = add(mon(la=20, tau=1), mon(la=20))
    for p in (
        mon(Fraction(1, 243), q1=1, q0=3),
        mon(Fraction(1, 54), q1=1, r2=1, r1=1),
        mon(Fraction(7, 108), q1=1, r1=2),
        mon(Fraction(1, 54), q1=1, r2=1, r0=1),
        mon(Fraction(-1, 54), q0=1, r1=1, r0=1),
        mon(Fraction(1, 108), q1=1, r0=2),
    ):
        out = add(out, p)
    return out


def specialize_q2_zero(p):
    q2_pos = INDEX["q2"]
    return clean({m: c for m, c in p.items() if m[q2_pos] == 0})


def divide_q2(p):
    q2_pos = INDEX["q2"]
    out = {}
    for m, c in p.items():
        if m[q2_pos] < 1:
            raise CompileFailure(("not q2 divisible", m, c))
        e = list(m)
        e[q2_pos] -= 1
        out[tuple(e)] = c
    return clean(out)


def frac(c):
    c = Fraction(c)
    return str(c.numerator) if c.denominator == 1 else f"({c.numerator}/{c.denominator})"


def render(p):
    chunks = []
    for m, c in sorted(p.items(), reverse=True):
        factors = []
        for name, e in zip(NAMES, m):
            if e == 1:
                factors.append(name)
            elif e:
                factors.append(f"{name}^{e}")
        body = "*".join(factors)
        chunks.append(f"{frac(c)}*{body}" if body else frac(c))
    return "+".join(chunks).replace("+-", "-") or "0"


def canonical(p):
    return [
        {"exponents": dict(zip(NAMES, m)),
         "numerator": c.numerator, "denominator": c.denominator}
        for m, c in sorted(p.items())
    ]


def digest(p):
    blob = json.dumps(canonical(p), sort_keys=True, separators=(",", ":"))
    return sha256(blob.encode()).hexdigest()


def weight_record(m, coefficient):
    e = dict(zip(NAMES, m))
    rsum = e["r2"] + e["r1"] + e["r0"]
    qsum = e["q1"] + e["q0"]
    # Twice the L-constant avoids fractions: 2*la + 15*R-degree.
    constant_l_twice = 2 * e["la"] + 15 * rsum
    sample = (
        4 * e["la"] + e["tau"] + e["rho"] + 23 * e["q2"]
        + 22 * qsum + 30 * rsum
    )
    return {
        "coefficient": str(coefficient),
        "exponents": e,
        "weight_form": {
            "D_coefficient": e["q2"],
            "betaL_coefficient": qsum,
            "constant_L_twice": constant_l_twice,
            "T_coefficient": e["tau"],
            "H_coefficient": e["rho"],
        },
        "sample_weight": sample,
    }


def extract_base_b():
    if sha256(PINNED_B.read_bytes()).hexdigest() != PINNED_B_SHA:
        raise CompileFailure("pinned B hash")
    text = PINNED_B.read_text()
    out = {}
    for ell in range(1, 9):
        hits = re.findall(rf"^poly E{ell}=(.*);$", text, flags=re.MULTILINE)
        if len(hits) != 1:
            raise CompileFailure(("base B anchor", ell, len(hits)))
        out[ell] = hits[0]
    return out


def singular_source(tag, order, base_b, rows, fs, witness, correction):
    if order == "A":
        ring = "ring R=0,(s,la,tau,rho,q2,q1,q0,r2,r1,r0),dp;"
        marker = "PASS_Q2_FIRST_LIFT_A_DP"
    else:
        ring = "ring R=0,(s,q2,la,tau,rho,q1,q0,r2,r1,r0),(lp(2),dp(8));"
        marker = "PASS_Q2_FIRST_LIFT_B_LPDP"
    lines = [
        "// Exact transported q2 lift; expanded source only.",
        ring,
        "option(redSB);",
        f'print("AWS_TAG={tag}");',
        f'print("ENCODING={order}_EXPANDED_Q2_TRANSPORT");',
    ]
    for ell in range(1, 9):
        lines.append(f"poly BASE{ell}={base_b[ell]};")
        lines.append(f"poly E{ell}={render(rows[ell])};")
        lines.append(f"poly DIFFROW{ell}=subst(E{ell},q2,0)-subst(BASE{ell},s,1);")
        lines.append(
            f'if (DIFFROW{ell}!=0) {{ print("FAIL_BASE_ROW_{ell}"); quit; }}'
        )
    for ell in range(1, 9):
        lines.append(f"poly F{ell}={render(fs[ell])};")
    lines.extend([
        f"poly W={render(witness)};",
        f"poly CORR={render(correction)};",
        "poly WQ2=F1*E1+F2*E2+F3*E3+F4*E4+F5*E5+F6*E6+F7*E7+F8*E8;",
        'if (subst(WQ2,q2,0)-W!=0) { print("FAIL_Q2_ZERO_WITNESS"); quit; }',
        'if (WQ2-W-q2*CORR!=0) { print("FAIL_Q2_CORRECTION_IDENTITY"); quit; }',
        'print("PASS_ALL_EIGHT_BASE_ROWS");',
        'print("PASS_Q2_TRANSPORT_IDENTITY");',
        'print("CORRECTION_BEGIN");',
        "print(CORR);",
        'print("CORRECTION_END");',
        'print("FIREWALL=TRANSPORTED_MULTIPLIERS_FULL_Q2_FIXED_AXIS_LOAD_ONLY_NOT_OPTIMAL_SYZYGY");',
        f'print("{marker}");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=".")
    args = parser.parse_args()
    tag = require_aws()
    charged = load_charged()
    built = charged.build()
    if tuple(built["names"]) != tuple([f"a{i}" for i in range(8)] + ["k"]):
        raise CompileFailure("charged names")
    tails = built["tails"]
    images = coefficient_images()
    rows = {
        ell: add(substitute(tails[ell], images), scale(-1, target(ell)))
        for ell in range(1, 9)
    }
    fs = multipliers()
    wq2 = {}
    for ell in range(1, 9):
        wq2 = add(wq2, mul(fs[ell], rows[ell]))
    witness = old_witness()
    if specialize_q2_zero(wq2) != witness:
        raise CompileFailure("q2-zero witness mismatch")
    correction = divide_q2(add(wq2, scale(-1, witness)))
    if not correction:
        raise CompileFailure("unexpected zero q2 correction")
    base_b = extract_base_b()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    source_a = singular_source(tag, "A", base_b, rows, fs, witness, correction)
    source_b = singular_source(tag, "B", base_b, rows, fs, witness, correction)
    path_a = output / "q2_first_lift_A_dp.sing"
    path_b = output / "q2_first_lift_B_lpdp.sing"
    path_a.write_text(source_a)
    path_b.write_text(source_b)
    records = [weight_record(m, c) for m, c in sorted(wq2.items())]
    correction_records = [weight_record(m, c) for m, c in sorted(correction.items())]
    payload = {
        "tag": tag,
        "charged_source_sha256": CHARGED_SHA,
        "pinned_B_sha256": PINNED_B_SHA,
        "rows_sha256": {str(ell): digest(rows[ell]) for ell in range(1, 9)},
        "witness_sha256": digest(witness),
        "q2_lift_sha256": digest(wq2),
        "correction_sha256": digest(correction),
        "q2_lift_terms": len(wq2),
        "correction_terms_after_factoring_one_q2": len(correction),
        "sample_min_weight": min(r["sample_weight"] for r in records),
        "sample_min_terms": [r for r in records if r["sample_weight"] == min(x["sample_weight"] for x in records)],
        "correction_weight_records": correction_records,
        "outputs": {
            path_a.name: sha256(path_a.read_bytes()).hexdigest(),
            path_b.name: sha256(path_b.read_bytes()).hexdigest(),
        },
        "firewall": "transported multipliers only; low correction does not rule out corrected syzygies",
    }
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS_Q2_FIRST_LIFT_COMPILER")


if __name__ == "__main__":
    main()
