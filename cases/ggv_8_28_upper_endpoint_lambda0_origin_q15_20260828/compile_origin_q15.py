#!/usr/bin/env python3
"""Compile the lambda=0 exact-D0 q5..q15 plus origin endpoint system.

The endpoint equation is reconstructed from the full ten-mode
characteristic; G11 and G15 are never introduced as independent raw slots.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
QG_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_20260828/compile_q_gates.py"
RAW_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_20260828/compile_fixed_q1_raw.py"
BASE_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
TAIL = ROOT / "cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/probe_literal_tail.py"
ACTIVE_D0 = ROOT / "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py"
DEEP_Q1_R1 = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py"

PINS = {
    QG_COMPILER: "b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201",
    RAW_COMPILER: "82284effbd507693cb8deb00e33b108d0f62d3d3861ce487e75d2e3f98b8fbea",
    BASE_COMPILER: "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    RAW_INPUT: "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    TAIL: "f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45",
    ACTIVE_D0: "112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26",
    DEEP_Q1_R1: "a5e6479f20cd7fcd50b317e174fd192512e5295de9c2126e717c005cb22acf69",
}

MODE_EXPONENTS = {
    2: Q(5, 4), 4: Q(1), 6: Q(3, 4), 8: Q(1, 2),
    10: Q(1, 4), 12: Q(0), 14: Q(-1, 4), 16: Q(-1, 2),
    18: Q(-3, 4), 20: Q(-1),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


qg = load_module("ggv_origin_q15_qg", QG_COMPILER)
ce = qg.ce
MV = ce.MV
M0 = MV.zero()
A = qg.A


def l_mul(left, right):
    out = {}
    for left_exponent, left_poly in left.items():
        for right_exponent, right_poly in right.items():
            exponent = left_exponent + right_exponent
            out[exponent] = ce.xadd(
                out.get(exponent, ()), ce.xmul(left_poly, right_poly)
            )
            if not out[exponent]:
                del out[exponent]
    return out


def l_scalar(item, scalar):
    return {
        exponent: qg.xscalar(poly, scalar)
        for exponent, poly in item.items()
        if qg.xscalar(poly, scalar)
    }


def fractional_power(F, exponent, maximum):
    """Solve F*y'=exponent*F'*y in Laurent powers of A."""
    out = {0: {int(4 * exponent): (MV.const(1),)}}
    for n in range(1, maximum + 1):
        numerator = {}
        for i in range(1, n + 1):
            if not F.get(i):
                continue
            numerator = qg.l_add(
                numerator,
                qg.l_scale(
                    l_mul({0: F[i]}, out[n - i]),
                    (exponent + 1) * i - n,
                ),
            )
        out[n] = qg.l_scale(qg.l_shift(numerator, -4), Q(1, n))
    return out


def characteristic(F, modes, maximum):
    exponents = set(MODE_EXPONENTS.values()) | {Q(3, 2)}
    powers = {exponent: fractional_power(F, exponent, maximum)
              for exponent in exponents}
    G = {}
    for n in range(maximum + 1):
        row = powers[Q(3, 2)][n]
        for birth, exponent in MODE_EXPONENTS.items():
            if birth <= n:
                row = qg.l_add(
                    row, l_scalar(powers[exponent][n - birth], modes[birth])
                )
        G[n] = row
    return G


def origin_coefficient(item, degree):
    """Coefficient X^0 or X^1; A'(0)=0 and A(0)=-1."""
    assert degree in (0, 1)
    out = M0
    for exponent, poly in item.items():
        if degree < len(poly):
            out = out + poly[degree].scale(-1 if exponent % 2 else 1)
    return out


def mv_substitute(poly, replacements):
    out = M0
    for monomial, coefficient in poly.terms.items():
        term = MV.const(coefficient)
        for name in monomial:
            term = term * replacements.get(name, MV.var(name))
        out = out + term
    return out


def reduced_F15(windows):
    F, _, _ = qg.reduced_lambda0_F(windows)
    F[14] = ce.xvar_poly(windows["F"][14])
    F[15] = ()  # There is no weight-15 raw F window.
    blocks = {n: [] for n in range(5, 16)}
    blocks[5] = [f"r_{degree}" for degree in range(3, -1, -1)]
    blocks[6] = [f"e_{degree}" for degree in range(6, -1, -1)]
    blocks[7] = [f"f_{degree}" for degree in range(5, -1, -1)]
    for n in range(8, 15):
        blocks[n] = [windows["F"][n][degree]
                     for degree in sorted(windows["F"][n], reverse=True)]
    source_variables = []
    for n in range(14, 7, -1):
        source_variables.extend(blocks[n])
    source_variables.extend(blocks[7])
    source_variables.extend(blocks[6])
    source_variables.extend(blocks[5])
    source_variables.extend(f"Q_{degree}" for degree in range(2, -1, -1))
    return F, source_variables, blocks


def raw_origin_census(source):
    slots = source["raw_slots_through_weight_22"]
    supports = {"F": {0: {0, 4, 8, 12, 16}},
                "G": {0: {0, 4, 8, 12, 16, 20, 24}}}
    parity_rows = []
    constants = {"F": 8, "G": 12}
    for side in ("F", "G"):
        for slot in slots[side]:
            weight = int(slot["weight"])
            x = int(slot["raw_exponents"]["x"])
            y = int(slot["raw_exponents"]["y"])
            assert weight == constants[side] + 3 * x - y
            assert weight % 2 == (x + y) % 2
            supports[side].setdefault(weight, set()).add(x)
            parity_rows.append((side, slot["slot"], weight, x + y))
    contributions = []
    for i in range(23):
        j = 22 - i
        if 1 in supports["F"].get(i, set()) and 0 in supports["G"].get(j, set()):
            coefficient = 12 - j
            if coefficient:
                contributions.append((i, j, "Fprime_G", coefficient, "F11[X1]*G11[X0]"))
        if 0 in supports["F"].get(i, set()) and 1 in supports["G"].get(j, set()):
            coefficient = i - 8
            if coefficient:
                contributions.append((i, j, "F_Gprime", coefficient, "F7[X0]*G15[X1]"))
    assert contributions == [
        (7, 15, "F_Gprime", -1, "F7[X0]*G15[X1]"),
        (11, 11, "Fprime_G", 1, "F11[X1]*G11[X0]"),
    ]
    return {
        "slot_count": len(parity_rows),
        "weight_parity_equals_raw_total_degree_parity": True,
        "origin_contributions": [list(item) for item in contributions],
        "identity": "D22[X0]=F11[X1]*G11[X0]-F7[X0]*G15[X1]",
    }


def encode_laurent(item):
    return {str(exponent): [coefficient.encode() for coefficient in poly]
            for exponent, poly in sorted(item.items())}


def polynomial_window_constraints(item, lower, upper, row_label):
    """Compile Laurent polynomiality and the authoritative raw X window."""
    minimum = min(item) if item else 0
    denominator_power = max(0, -minimum)
    numerator = ()
    for exponent, poly in item.items():
        numerator = ce.xadd(
            numerator, ce.xmul(ce.xpow(A, exponent + denominator_power), poly)
        )
    denominator = ce.xpow(A, denominator_power)
    quotient, remainder = qg.x_divmod_monic(numerator, denominator)
    equations = []
    for degree, coefficient in enumerate(remainder):
        if coefficient.terms:
            encoded = coefficient.encode()
            equations.append({
                "kind": "polynomiality_remainder", "row": row_label,
                "x_degree": degree, "terms": encoded,
                "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
            })
    for degree, coefficient in enumerate(quotient):
        if coefficient.terms and not lower <= degree <= upper:
            encoded = coefficient.encode()
            equations.append({
                "kind": "raw_window", "row": row_label,
                "x_degree": degree, "window": [lower, upper],
                "terms": encoded,
                "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
            })
    return {
        "row": row_label,
        "denominator_A_power": denominator_power,
        "numerator": [coefficient.encode() for coefficient in numerator],
        "quotient": [coefficient.encode() for coefficient in quotient],
        "remainder": [coefficient.encode() for coefficient in remainder],
        "window": [lower, upper],
        "equations": equations,
    }, quotient


def system(slice_kind="general"):
    assert slice_kind in ("general", "control_q_e_F8_r_zero")
    source = json.loads(RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    ce.verify_windows(windows)
    F, source_variables, blocks = reduced_F15(windows)
    if slice_kind == "control_q_e_F8_r_zero":
        zero_names = (
            {f"Q_{degree}" for degree in range(3)}
            | {f"r_{degree}" for degree in range(4)}
            | {f"e_{degree}" for degree in range(7)}
            | set(blocks[8])
        )
        replacements = {name: M0 for name in zero_names}
        F = {
            n: ce.xtrim(mv_substitute(coefficient, replacements)
                        for coefficient in poly)
            for n, poly in F.items()
        }
        source_variables = [name for name in source_variables
                            if name not in zero_names]
        blocks = {n: [name for name in names if name not in zero_names]
                  for n, names in blocks.items()}
    modes = {birth: MV.var(f"c{birth}") for birth in MODE_EXPONENTS}
    G = characteristic(F, modes, 15)
    g_windows = {
        8: (0, 16), 9: (0, 15), 10: (0, 14), 11: (0, 13),
        12: (0, 12), 13: (1, 11), 14: (1, 10), 15: (1, 9),
    }
    g_constraints = {}
    g_polys = {}
    for weight, (lower, upper) in g_windows.items():
        compiled, polynomial = polynomial_window_constraints(
            G[weight], lower, upper, f"G{weight}"
        )
        g_constraints[weight] = compiled
        g_polys[weight] = polynomial
    g11_constraints, g11_poly = g_constraints[11], g_polys[11]
    g15_constraints, g15_poly = g_constraints[15], g_polys[15]
    g11_x0 = g11_poly[0] if g11_poly else M0
    g15_x1 = g15_poly[1] if len(g15_poly) > 1 else M0
    g11_origin_direct = origin_coefficient(G[11], 0)
    g15_x1_direct = origin_coefficient(G[15], 1)
    endpoint = F[11][1] * g11_x0 - F[7][0] * g15_x1 - MV.const(1)
    endpoint_value = endpoint + MV.const(1)

    g11_names = {name for monomial in g11_origin_direct.terms for name in monomial}
    g15_names = {name for monomial in g15_x1_direct.terms for name in monomial}
    assert not ({"c12", "c14", "c16", "c18", "c20"} & g11_names)
    assert not ({"c16", "c18", "c20"} & g15_names)

    odd_source = set(blocks[5] + blocks[7] + blocks[9]
                     + blocks[11] + blocks[13])
    zero_odd = {name: M0 for name in odd_source}
    assert not mv_substitute(g11_x0, zero_odd).terms
    assert not mv_substitute(g15_x1, zero_odd).terms
    odd_endpoint = mv_substitute(endpoint, zero_odd)
    assert odd_endpoint == MV.const(-1)

    gates = []
    equations = []
    primitive_variables = []
    for n in range(5, 16):
        gate = qg.exactness_gate(F, n)
        gate["new_source_variables"] = blocks[n]
        gate["new_variables"] = blocks[n] + gate["primitive_variables"]
        gates.append(gate)
        equations.extend(gate["equations"])
        primitive_variables.extend(gate["primitive_variables"])

    raw_constraints = [equation for weight in range(8, 16)
                       for equation in g_constraints[weight]["equations"]]
    equations.extend(raw_constraints)
    endpoint_encoded = endpoint.encode()
    endpoint_equation = {
        "kind": "origin_endpoint",
        "row": "D22[X0]",
        "target": "1",
        "terms": endpoint_encoded,
        "sha256": hashlib.sha256(ce.compact(endpoint_encoded)).hexdigest(),
    }
    open_poly = MV.var("invc2") * MV.var("c2") - MV.const(1)
    open_encoded = open_poly.encode()
    open_equation = {
        "kind": "open_condition", "condition": "c2!=0",
        "terms": open_encoded,
        "sha256": hashlib.sha256(ce.compact(open_encoded)).hexdigest(),
    }
    equations.extend([endpoint_equation, open_equation])
    mode_variables = [f"c{birth}" for birth in MODE_EXPONENTS]
    variables = source_variables + mode_variables + ["invc2"] + primitive_variables
    assert len(variables) == len(set(variables))
    used = {name for equation in equations
            for monomial, _ in equation["terms"] for name in monomial}
    assert used <= set(variables), sorted(used - set(variables))
    return {
        "schema": "GGV-8_28-UPPER-LAMBDA0-ORIGIN-Q5-Q15-v1",
        "system_id": (
            "lambda_0_c2_nonzero_exact_D0_q3_U0_origin_q5_q15"
            if slice_kind == "general" else
            "lambda_0_c2_nonzero_exact_D0_q3_U0_Q_e_F8_r_zero_control"
        ),
        "slice_kind": slice_kind,
        "field": "Q",
        "fixed_A": "X^4-1",
        "conditions": ["lambda=0", "c2!=0", "exact D=0", "reviewed D11/D12 lifts", "q3 plus A|U gives U=0"],
        "forms": ["F2=-A^3*Q/8", "F4=A^2*Q^2/256", "F5=A^2*r/256", "F6=A*e/2048", "F7=A*f", "F15=0"],
        "q_formula": "q_n=2/(n+2)*[t^n]F^((n+2)/8)",
        "q_range": [5, 15],
        "characteristic": "G=F^(3/2)+sum_{birth=2,4,...,20} c_birth*t^birth*F^((6-birth)/4)",
        "mode_exponents": {str(k): str(v) for k, v in MODE_EXPONENTS.items()},
        "G11_laurent": encode_laurent(G[11]),
        "G15_laurent": encode_laurent(G[15]),
        "G8_G15_polynomial_windows": {
            str(weight): g_constraints[weight] for weight in range(8, 16)
        },
        "G11_polynomial_window": g11_constraints,
        "G15_polynomial_window": g15_constraints,
        "G11_X0_direct_laurent": g11_origin_direct.encode(),
        "G15_X1_direct_laurent": g15_x1_direct.encode(),
        "G11_X0": g11_x0.encode(),
        "G15_X1": g15_x1.encode(),
        "endpoint_value": endpoint_value.encode(),
        "endpoint_equation": endpoint_equation,
        "open_equation": open_equation,
        "all_odd_source_zero_endpoint_residual": odd_endpoint.encode(),
        "raw_origin_census": raw_origin_census(source),
        "source_variables": source_variables,
        "mode_variables": mode_variables,
        "primitive_variables": primitive_variables,
        "variables": variables,
        "variable_count": len(variables),
        "gates": gates,
        "equations": equations,
        "equation_count": len(equations),
        "scope": "proper lambda=0,c2!=0,exact-D0,q3-U0 branch only; necessary q5..q15 and exact origin endpoint equation",
        "control_checksum_candidate": (
            None if slice_kind == "general" else {
                "parent_formula_endpoint": "-8*a1*(3*c6*b2+2*c8*a2)",
                "parent_formula_G15_remainder_X1": "40*(3*c6*b2+2*c8*a2)",
                "status_before_AWS_reduction": "checksum only; parameters must be derived and mapped independently",
            }
        ),
        "negative_control_firewall": "arbitrary Q is retained in the general system; G15 polynomiality alone is diagnostic and cannot classify the general branch",
        "pins": {str(path.relative_to(ROOT)): digest for path, digest in PINS.items()},
    }


def constant_poly(poly):
    out = []
    for coefficient in poly:
        assert set(coefficient.terms) <= {()}
        out.append(coefficient.terms.get((), Q(0)))
    while out and not out[-1]:
        out.pop()
    return out


def constant_laurent(item):
    return {exponent: constant_poly(poly) for exponent, poly in item.items()
            if constant_poly(poly)}


def desk_check():
    for path, expected in PINS.items():
        assert sha256(path) == expected, path
    source = json.loads(RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    ce.verify_windows(windows)
    census = raw_origin_census(source)

    # A parity-symmetric exact sample checks this characteristic recurrence
    # against the independently frozen literal-tail implementation.
    Qpoly = (MV.const(2), MV.const(-1))
    Epoly = (MV.const(3), MV.const(1))
    F = {
        1: (),
        2: ce.xscale(ce.xmul(ce.xpow(A, 3), Qpoly), Q(-1, 8)),
        3: (),
        4: ce.xscale(ce.xmul(ce.xpow(A, 2), ce.xmul(Qpoly, Qpoly)), Q(1, 256)),
        5: (),
        6: ce.xscale(ce.xmul(A, Epoly), Q(1, 2048)),
        7: (), 8: (MV.const(5),), 9: (), 10: (MV.const(-2),),
        11: (), 12: (MV.const(7),), 13: (), 14: (M0, M0, MV.const(1)),
        15: (),
    }
    modes_q = {birth: Q(index + 1) for index, birth in enumerate(MODE_EXPONENTS)}
    modes_mv = {birth: MV.const(value) for birth, value in modes_q.items()}
    ours = characteristic(F, modes_mv, 15)
    tail = load_module("ggv_origin_q15_tail", TAIL)
    up = tail.load_upstream()
    tail_F = {0: {4: [Q(1)]}}
    tail_F.update({n: ({0: constant_poly(F[n])} if F[n] else {})
                   for n in range(1, 16)})
    theirs = tail.characteristic_special(up, tail_F, modes_q, 15)
    for n in range(16):
        assert constant_laurent(ours[n]) == theirs[n], n
    assert not ours[11] and not ours[15]
    for n in (5, 7, 9, 11, 13, 15):
        assert not qg.q_fraction(F, n)[2], n

    return {
        "status": "DESK_CHECK_PASS",
        "raw_origin_census": census,
        "ten_mode_characteristic_matches_frozen_tail_through_weight": 15,
        "parity_sample_odd_G11_G15_and_q5_to_q15": "zero",
        "pins": {str(path.relative_to(ROOT)): sha256(path) for path in PINS},
    }


def write_outputs(output_dir: Path, slice_kind: str):
    audit = desk_check()
    data = system(slice_kind)
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        "DESK_CHECK.json": ce.pretty(audit),
        "ORIGIN_Q15_SYSTEM.json": ce.pretty(data),
    }
    manifest = {}
    for name, payload in payloads.items():
        (output_dir / name).write_bytes(payload)
        manifest[name] = hashlib.sha256(payload).hexdigest()
    (output_dir / "GENERATED.sha256.json").write_bytes(ce.pretty(manifest))
    print(json.dumps({
        "status": "COMPILE_PASS", "variables": data["variable_count"],
        "equations": data["equation_count"],
        "endpoint_terms": len(data["endpoint_equation"]["terms"]),
        "system_sha256": manifest["ORIGIN_Q15_SYSTEM.json"],
    }, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desk-check", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--system", choices=("general", "control_q_e_F8_r_zero"),
                        default="general")
    args = parser.parse_args()
    if args.desk_check == (args.output_dir is not None):
        parser.error("choose exactly one of --desk-check or --output-dir")
    if args.desk_check:
        print(json.dumps(desk_check(), indent=2, sort_keys=True))
    else:
        write_outputs(args.output_dir, args.system)


if __name__ == "__main__":
    main()
