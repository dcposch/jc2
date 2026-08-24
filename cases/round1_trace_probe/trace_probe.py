#!/usr/bin/env python3
"""Narrow TRACE-REG principal-part and data-sufficiency audit.

Requires SymPy 1.14.0.  This is not a trace engine for the residue-A family.
It checks the local trace formula, two exact controls, and one collision
showing that valuation/contact decorations without completed coefficients do
not determine a Newton-sum residue.

Replay:

  uv run --no-project --with sympy==1.14.0 \
    python3 cases/round1_trace_probe/trace_probe.py \
    --out cases/round1_trace_probe/results.json
"""

import argparse
import hashlib
import json
import os

import sympy as sp


HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.dirname(HERE)
ROOT = os.path.dirname(CASES)
TOOL = "cases/round1_trace_probe/trace_probe.py"

INPUTS = [
    "AUDIT.md",
    "PROGRESS.md",
    "ladder/TRANSPORT.md",
    "ladder/SHEET6-CLASSICAL.md",
    "ladder/GROK-MONODROMY.md",
    "xmodel/round1-boundary-passport-20260824.md",
    "cases/round1_boundary_probe/results.json",
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def json_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        .encode()).hexdigest()


def expr_string(expr):
    return sp.sstr(sp.collect(sp.expand(expr), sorted(expr.free_symbols,
                                                       key=str)))


def laurent_terms(expr, variable):
    """Exact finite Laurent polynomial as exponent -> coefficient."""
    out = {}
    for term in sp.Add.make_args(sp.expand(expr)):
        exponent = term.as_powers_dict().get(variable, sp.Integer(0))
        assert exponent.is_Integer, (term, exponent)
        exponent = int(exponent)
        coefficient = sp.simplify(term / variable ** exponent)
        assert not coefficient.has(variable), (term, variable)
        out[exponent] = sp.simplify(out.get(exponent, 0) + coefficient)
    return {n: c for n, c in out.items() if c != 0}


def principal_part(expr, variable):
    return sp.expand(sum(c * variable ** n
                         for n, c in laurent_terms(expr, variable).items()
                         if n < 0))


def residue(expr, variable):
    """Coefficient residue Res(expr dvariable)."""
    return sp.simplify(laurent_terms(expr, variable).get(-1, 0))


def cyclic_trace_power(series, source_parameter, target_parameter,
                       ramification_index, power):
    """Trace under t=u^e by the exact roots-of-unity filter.

    If series^power = sum c_n u^n, summing over u -> zeta*u retains
    exactly e|n and produces e*c_n*t^(n/e).  Characteristic zero and a
    tame cyclic splitting field are understood; the result descends.
    """
    terms = laurent_terms(sp.expand(series ** power), source_parameter)
    answer = 0
    for exponent, coefficient in terms.items():
        if exponent % ramification_index == 0:
            answer += (ramification_index * coefficient *
                       target_parameter ** (exponent // ramification_index))
    return sp.expand(answer)


def power_record(expressions, parameter):
    return {
        name: {
            "expression": expr_string(expr),
            "principal_part": expr_string(principal_part(expr, parameter)),
            "residue_of_expression_dt": expr_string(residue(expr, parameter)),
        }
        for name, expr in expressions.items()
    }


def newton_identity_gate():
    """Symbolic degree-four check of the exact Newton recursion used."""
    roots = sp.symbols("lambda1:5")
    power_sums = [None] + [sum(r ** m for r in roots) for m in range(1, 5)]
    elementary = [sp.Integer(1)]
    for m in range(1, 5):
        value = sum((-1) ** (i - 1) * elementary[m - i] * power_sums[i]
                    for i in range(1, m + 1)) / m
        elementary.append(sp.expand(value))
    T = sp.symbols("T")
    reconstructed = sum((-1) ** m * elementary[m] * T ** (4 - m)
                        for m in range(5))
    expected = sp.prod(T - r for r in roots)
    assert sp.expand(reconstructed - expected) == 0
    return {
        "degree": 4,
        "recursion": ("m*e_m = sum_{i=1}^m (-1)^(i-1) "
                      "e_(m-i)*Tr(z^i)"),
        "characteristic_polynomial_reconstructed": True,
    }


def tame_control(t, q):
    """Nontrivial tame automorphism (P,Q)=(x,y+x^2), degree one."""
    affine = {
        "Tr(x)": t,
        "Tr(x^2)": t ** 2,
        "Tr(y)": q - t ** 2,
        "Tr(y^2)": (q - t ** 2) ** 2,
    }
    infinity = {
        "Tr(x)": t ** -1,
        "Tr(x^2)": t ** -2,
        "Tr(y)": q - t ** -2,
        "Tr(y^2)": (q - t ** -2) ** 2,
    }
    assert all(principal_part(v, t) == 0 for v in affine.values())
    return {
        "map": "P=x, Q=y+x^2",
        "jacobian": "1",
        "field_degree": 1,
        "inverse": "x=P, y=Q-P^2",
        "affine_target_DVR": {
            "substitution": "P=t, Q=q (generic q)",
            "power_sums": power_record(affine, t),
        },
        "target_infinity_chart": {
            "substitution": "P=t^-1, Q=q",
            "power_sums": power_record(infinity, t),
            "note": ("poles here are ordinary polynomial growth at target "
                     "infinity, not failure of A-regularity"),
        },
    }


def nonproper_control(t, u, q):
    """Degree-two nonproper map (P,Q)=(x^2,xy)."""
    x = u
    y = q / u
    values = {
        "Tr(x)": cyclic_trace_power(x, u, t, 2, 1),
        "Tr(x^2)": cyclic_trace_power(x, u, t, 2, 2),
        "Tr(y)": cyclic_trace_power(y, u, t, 2, 1),
        "Tr(y^2)": cyclic_trace_power(y, u, t, 2, 2),
    }
    expected = {"Tr(x)": 0, "Tr(x^2)": 2 * t,
                "Tr(y)": 0, "Tr(y^2)": 2 * q ** 2 / t}
    assert all(sp.expand(values[k] - expected[k]) == 0 for k in values)
    return {
        "map": "P=x^2, Q=x*y",
        "jacobian": "2*x^2",
        "field_degree": 2,
        "nonproper_witness": (
            "x=u -> 0, y=q/u -> infinity maps to (P,Q)=(u^2,q); "
            "(0,q), q!=0, has no affine preimage"),
        "target_DVR": {
            "relation": "t=P=u^2, Q=q (generic nonzero q)",
            "branches": ["x=u,y=q/u", "x=-u,y=-q/u"],
            "power_sums": power_record(values, t),
        },
        "diagnostic": (
            "m=1 cancels on both coordinates, while Tr(y^2)=2*q^2/t "
            "has residue 2*q^2 and detects nonregularity"),
    }


def completion_collision(t, u, a, b):
    """Two denominator-42 completions with identical contact decoration."""
    e = 42
    # Relative to the invariant leading exponent -84, the three
    # non-invariant exponents occur at offsets 54, 74, 79.  Their gcd
    # sequence with 42 is 42 -> 6 -> 2 -> 1, the recorded (7,3,2)
    # characteristic-index pattern.  The a- and b-slots are invariant
    # under u -> zeta*u, so changing b changes no conjugate contact.
    series = (u ** -84 + u ** -30 + u ** -10 + u ** -5 +
              a * u ** -42 + b * u ** 42)
    trace1 = cyclic_trace_power(series, u, t, e, 1)
    trace2 = cyclic_trace_power(series, u, t, e, 2)
    expected1 = 42 * (t ** -2 + a * t ** -1 + b * t)
    expected2 = 42 * (t ** -4 + 2 * a * t ** -3 +
                      a ** 2 * t ** -2 + 2 * b * t ** -1 +
                      2 * a * b + b ** 2 * t ** 2)
    assert sp.expand(trace1 - expected1) == 0
    assert sp.expand(trace2 - expected2) == 0
    shared_decoration = {
        "ramification_denominator": 42,
        "conjugate_orbit_size": 42,
        "invariant_leading_exponent": -84,
        "leading_coefficient": 1,
        "characteristic_offsets_from_leading": [54, 74, 79],
        "characteristic_gcd_sequence": [42, 6, 2, 1],
        "characteristic_index_sequence": [7, 3, 2],
        "varying_slot_offset_from_leading": 126,
        "occupied_exponents": [-84, -42, -30, -10, -5, 42],
        "all_displayed_coefficients_nonzero": True,
        "contact_invariance": (
            "the varying b*u^42 term is fixed by u -> zeta*u, so it "
            "cancels in every conjugate difference and changes no contact"),
    }
    completions = []
    for bv in (1, 2):
        s1 = sp.expand(trace1.subs({a: 1, b: bv}))
        s2 = sp.expand(trace2.subs({a: 1, b: bv}))
        completions.append({
            "a": 1,
            "b": bv,
            "decoration": shared_decoration,
            "Tr(z)": expr_string(s1),
            "Tr(z^2)": expr_string(s2),
            "principal_part_Tr(z)": expr_string(principal_part(s1, t)),
            "principal_part_Tr(z^2)": expr_string(principal_part(s2, t)),
            "residue_Tr(z)_dt": expr_string(residue(s1, t)),
            "residue_Tr(z^2)_dt": expr_string(residue(s2, t)),
        })
    assert completions[0]["decoration"] == completions[1]["decoration"]
    assert completions[0]["residue_Tr(z^2)_dt"] == "84"
    assert completions[1]["residue_Tr(z^2)_dt"] == "168"
    return {
        "local_relation": "t=u^42",
        "family": ("z_b=u^-84+u^-30+u^-10+u^-5+"
                   "a*u^-42+b*u^42"),
        "generic_formulas": {
            "Tr(z)": expr_string(trace1),
            "Tr(z^2)": expr_string(trace2),
            "Res(Tr(z)dt)": expr_string(residue(trace1, t)),
            "Res(Tr(z^2)dt)": expr_string(residue(trace2, t)),
        },
        "completions": completions,
        "decisive_collision": True,
        "meaning": (
            "denominator, full exponent support, leading coefficient, all "
            "characteristic gcd drops and every conjugate contact agree, "
            "but the second Newton-sum residue changes with an invariant "
            "completed coefficient"),
        "not_a_formal_Keller_countermodel": (
            "this is a local data-sufficiency witness; no polynomial pair or "
            "constant-Jacobian completion is asserted"),
    }


def local_trace_formula():
    return {
        "setup": (
            "At a target DVR K_v=kappa_v((t)), put each tame completed "
            "factor in split form t=u_w^e_w and write "
            "z_w(u_w)^m=sum_n c_(w,m,n)u_w^n, with coefficients in the "
            "residue field kappa_w."),
        "formula": (
            "Tr(z^m)=sum_w e_w*sum_{e_w|n} "
            "Tr_(kappa_w/kappa_v)(c_(w,m,n))*t^(n/e_w)"),
        "base_coefficient_specialization": (
            "if every c_(w,m,n) lies in kappa_v, the coefficient factor is "
            "e_w*f_w*c_(w,m,n)"),
        "principal_part": "retain the terms n<0 with e_w|n",
        "residue": (
            "Res_t(Tr(z^m)dt)=sum_w e_w*"
            "Tr_(kappa_w/kappa_v)(c_(w,m,-e_w))"),
        "required_data": [
            "all places w above the same target valuation v",
            "ramification and residue degrees e_w,f_w",
            "a common target uniformizer and branch embeddings",
            "the completed coefficients contributing to c_(w,m,n)",
        ],
    }


def input_manifest():
    manifest = {}
    for rel in INPUTS:
        path = os.path.join(ROOT, rel)
        assert os.path.isfile(path), rel
        manifest[rel] = {"bytes": os.path.getsize(path),
                         "sha256": sha256_file(path)}
    p1 = json.load(open(os.path.join(
        ROOT, "cases/round1_boundary_probe/results.json")))
    assert p1["verdict"] == "COSTUME"
    return manifest


def run(out_path):
    t, u, q, a, b = sp.symbols("t u q a b", nonzero=True)
    manifest = input_manifest()
    newton = newton_identity_gate()
    tame = tame_control(t, q)
    nonproper = nonproper_control(t, u, q)
    collision = completion_collision(t, u, a, b)
    assert collision["decisive_collision"]
    verdict = "INSUFFICIENT-DATA"
    out = {
        "tool": TOOL,
        "tool_sha256": sha256_file(os.path.join(ROOT, TOOL)),
        "engine": {"sympy": sp.__version__, "arithmetic": "exact QQ[symbols]"},
        "status": "INTERNAL / PRODUCER-CHECKED",
        "verdict": verdict,
        "verdict_reason": (
            "The current valuation/contact packet does not supply a complete "
            "target-local branch decomposition or the coefficients selected "
            "by the trace residue formula.  Two exact completions with the "
            "same retained coarse decorations have different m=2 residues."),
        "conditional_algebra_gate": newton,
        "local_trace_formula": local_trace_formula(),
        "controls": {"tame_automorphism": tame,
                     "generically_finite_nonproper": nonproper},
        "underdetermination_collision": collision,
        "campaign_data_audit": {
            "retained": [
                "pole/place counts, ramification indices and cycle types",
                "Newton pairs, characteristic denominators and contacts",
                "the pure-boundary determinant identity",
                "finite modular D25 source jets in their own chart",
            ],
            "missing_for_trace": [
                "a proved GGV/source-to-paired-boundary dictionary",
                "all branches grouped above one target DVR",
                "a common target uniformizer with conjugation twists fixed",
                "the completed coefficient slots entering c_(w,m,-e_w)",
                "a construction of the field trace from D25 tail labels",
            ],
            "p1_usage": (
                "P1 is used only as a COSTUME perimeter/tooling result; no "
                "P1 invariant is assumed as a proposition"),
        },
        "perimeter": [
            "the collision is not a Keller map or formal Keller countermodel",
            "m=1,2 do not establish the trace criterion when field degree >2",
            "no claim is made about all residue-A coefficient completions",
            "no trace regularity, finiteness, or automorphism is proved",
        ],
        "input_manifest": manifest,
        "input_manifest_sha256": json_hash(manifest),
    }
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)
        f.write("\n")
    print("VERDICT:", verdict)
    print("COLLISION RESIDUES:",
          [c["residue_Tr(z^2)_dt"] for c in collision["completions"]])
    print("WROTE:", out_path)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "results.json"))
    args = ap.parse_args()
    run(args.out)


if __name__ == "__main__":
    main()
