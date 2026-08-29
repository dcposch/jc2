#!/usr/bin/env python3
"""Compile exact q1,...,q13 de Rham gates for the fixed deep-q1 slices.

The coefficient formula is independently implemented as

    q_n = 2/(n+2) [t^n] F^((n+2)/8).

On a quadratic component p^2=+/-A, each q_n is represented as
p^r*N/A^k.  Exactness is compiled by a complete rational primitive ansatz
for the first-order operator

    d(p^r P/A^d)/p^r
      = (A P' + (r/2-d) A'P)/A^(d+1).

The sign of the quadratic twist changes a whole character row only by a
nonzero scalar, so the coefficient ideal is the same.  The full lambda
slices are necessary de Rham screens for the raw endpoint system.  A third,
strictly labelled system consumes the reviewed c2!=0, exact-D=0 successor
on lambda=0 and the reviewed D12 lift before setting U=0 by the q3 gate.
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
RAW_COMPILER = HERE / "compile_fixed_q1_raw.py"
BASE_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
R7 = ROOT / "cases/ggv_quarter_root_characteristic_r7_20260827/verify_r7.py"
R7R1 = ROOT / "cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py"
Q1_PREFIX = ROOT / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py"
ACTIVE_D0 = ROOT / "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py"
ACTIVE_D0_RESULT = ACTIVE_D0.with_name("RESULT.json")
DEEP_Q1_R1 = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py"


PINS = {
    RAW_COMPILER: "82284effbd507693cb8deb00e33b108d0f62d3d3861ce487e75d2e3f98b8fbea",
    BASE_COMPILER: "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    RAW_INPUT: "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    R7: "c40820e300f39d92d757de698ecf6c8a5ad0b79711e369275b2de93dd6488244",
    R7R1: "1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa",
    Q1_PREFIX: "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119",
    ACTIVE_D0: "112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26",
    ACTIVE_D0_RESULT: "568934cecfd224cfdff6f8af0791f71f54426ccc0fc5384fc4d0d90a2712c02e",
    DEEP_Q1_R1: "a5e6479f20cd7fcd50b317e174fd192512e5295de9c2126e717c005cb22acf69",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


rawc = load_module("ggv_q_gate_raw_compiler", RAW_COMPILER)
ce = rawc.ce
MV = ce.MV
M0 = MV.zero()
A = (MV.const(-1), M0, M0, M0, MV.const(1))
APRIME = ce.xder(A)


def xsum(*items):
    out = ()
    for item in items:
        out = ce.xadd(out, item)
    return out


def xscalar(poly, scalar: MV):
    return ce.xtrim(coefficient * scalar for coefficient in poly)


def xshift(poly, amount: int):
    return (M0,) * amount + tuple(poly) if poly else ()


def x_divmod_monic(dividend, divisor):
    divisor = ce.xtrim(divisor)
    assert divisor and divisor[-1] == MV.const(1)
    remainder = list(ce.xtrim(dividend))
    quotient = [M0] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[degree] = quotient[degree] + coefficient
        subtract = [M0] * degree + [coefficient * item for item in divisor]
        remainder = list(ce.xadd(remainder, tuple(-item for item in subtract)))
    return ce.xtrim(quotient), ce.xtrim(remainder)


def divide_A_once(poly):
    quotient, remainder = x_divmod_monic(poly, A)
    return quotient if not remainder else None


def l_add(*items):
    out = {}
    for item in items:
        for exponent, poly in item.items():
            out[exponent] = ce.xadd(out.get(exponent, ()), poly)
            if not out[exponent]:
                del out[exponent]
    return out


def l_scale(item, scalar):
    return {exponent: ce.xscale(poly, scalar)
            for exponent, poly in item.items() if ce.xscale(poly, scalar)}


def l_mul_x(item, poly):
    return {exponent: ce.xmul(value, poly)
            for exponent, value in item.items() if ce.xmul(value, poly)}


def l_shift(item, amount):
    return {exponent + amount: poly for exponent, poly in item.items()}


def q_laurent(F, n: int):
    """Return (initial p-character, Laurent-in-A rational coefficient)."""
    exponent = Q(n + 2, 8)
    character = (n + 2) % 4
    base_a_exponent = (n + 2 - character) // 2
    out = {0: {base_a_exponent: (MV.const(1),)}}
    for weight in range(1, n + 1):
        numerator = {}
        for index in range(1, weight + 1):
            if index not in F:
                continue
            factor = (exponent + 1) * index - weight
            numerator = l_add(
                numerator,
                l_scale(l_mul_x(out[weight - index], F[index]), factor),
            )
        out[weight] = l_scale(l_shift(numerator, -4), Q(1, weight))
    return character, l_scale(out[n], Q(2, n + 2))


def common_fraction(character, item):
    minimum = min(item) if item else 0
    denominator_power = max(0, -minimum)
    numerator = ()
    for exponent, poly in item.items():
        numerator = ce.xadd(
            numerator,
            ce.xmul(ce.xpow(A, exponent + denominator_power), poly),
        )

    # Cancel literal common A factors first.
    while denominator_power:
        quotient = divide_A_once(numerator)
        if quotient is None:
            break
        numerator = quotient
        denominator_power -= 1

    # On either quadratic component p^2=+/-A.  Moving by p^2 changes the
    # whole row by a nonzero twist scalar only; choose the least-pole form.
    if character == 2:
        numerator = ce.xmul(A, numerator)
        character = 0
        while denominator_power:
            quotient = divide_A_once(numerator)
            if quotient is None:
                break
            numerator = quotient
            denominator_power -= 1
    changed = True
    while changed:
        changed = False
        if character == 3 and denominator_power:
            character = 1
            denominator_power -= 1
            changed = True
        elif character == 1:
            quotient = divide_A_once(numerator)
            if quotient is not None:
                numerator = quotient
                character = 3
                changed = True
    return character, denominator_power, numerator


def q_fraction(F, n: int):
    return common_fraction(*q_laurent(F, n))


def poly_degree(poly):
    return len(ce.xtrim(poly)) - 1


def primitive_bound(rhs, alpha):
    degree = poly_degree(rhs)
    if degree < 0:
        return 0
    ordinary = max(0, degree - 3)
    resonance = -4 * alpha
    if resonance.denominator == 1 and resonance >= 0 and resonance - 1 <= degree:
        ordinary = max(ordinary, int(resonance))
    return ordinary


def exactness_gate(F, n: int):
    character, denominator_power, numerator = q_fraction(F, n)
    primitive_denominator = max(0, denominator_power - 1)
    alpha = Q(character, 2) - primitive_denominator
    rhs = numerator if denominator_power else ce.xmul(A, numerator)
    degree_bound = primitive_bound(rhs, alpha)
    primitive_names = [f"h{n}_{degree}" for degree in range(degree_bound + 1)]
    primitive = tuple(MV.var(name) for name in primitive_names)
    operator = xsum(
        ce.xmul(A, ce.xder(primitive)),
        ce.xscale(ce.xmul(APRIME, primitive), alpha),
    )
    residual = ce.xadd(operator, ce.xscale(rhs, -1))
    equations = []
    for degree, coefficient in enumerate(residual):
        if coefficient.terms:
            encoded = coefficient.encode()
            equations.append({
                "q": n,
                "x_degree": degree,
                "terms": encoded,
                "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
            })
    return {
        "q": n,
        "character_p_power": character,
        "coefficient_denominator_A_power": denominator_power,
        "coefficient_numerator": [item.encode() for item in numerator],
        "primitive_denominator_A_power": primitive_denominator,
        "operator_alpha": str(alpha),
        "primitive_degree_bound": degree_bound,
        "primitive_variables": primitive_names,
        "equations": equations,
    }


def full_slice_F(lam: int, windows):
    *_, F, _ = rawc.fixed_polynomials(lam)
    for weight in range(4, 14):
        F[weight] = ce.xvar_poly(windows["F"][weight])
    source_variables = []
    for weight in range(13, 3, -1):
        source_variables.extend(windows["F"][weight][degree]
                                for degree in sorted(windows["F"][weight], reverse=True))
    source_variables.extend(f"u_{degree}" for degree in range(5, -1, -1))
    source_variables.extend(f"z_{degree}" for degree in range(6, -1, -1))
    blocks = {
        n: ([windows["F"][n][degree] for degree in sorted(windows["F"][n], reverse=True)]
            if n >= 4 else
            ([f"u_{degree}" for degree in range(5, -1, -1)] if n == 3 else []))
        for n in range(1, 14)
    }
    return F, source_variables, blocks


def reduced_lambda0_F(windows):
    Qpoly = tuple(MV.var(f"Q_{degree}") for degree in range(3))
    Rpoly = tuple(MV.var(f"r_{degree}") for degree in range(4))
    Epoly = tuple(MV.var(f"e_{degree}") for degree in range(7))
    fpoly = tuple(MV.var(f"f_{degree}") for degree in range(6))
    F = {
        0: ce.xpow(A, 4),
        1: (),
        2: ce.xscale(ce.xmul(ce.xpow(A, 3), Qpoly), Q(-1, 8)),
        3: (),
        4: ce.xscale(ce.xmul(ce.xpow(A, 2), ce.xmul(Qpoly, Qpoly)), Q(1, 256)),
        5: ce.xscale(ce.xmul(ce.xpow(A, 2), Rpoly), Q(1, 256)),
        6: ce.xscale(ce.xmul(A, Epoly), Q(1, 2048)),
        7: ce.xmul(A, fpoly),
    }
    for weight in range(8, 14):
        F[weight] = ce.xvar_poly(windows["F"][weight])
    source_variables = []
    for weight in range(13, 7, -1):
        source_variables.extend(windows["F"][weight][degree]
                                for degree in sorted(windows["F"][weight], reverse=True))
    source_variables.extend(f"f_{degree}" for degree in range(5, -1, -1))
    source_variables.extend(f"e_{degree}" for degree in range(6, -1, -1))
    source_variables.extend(f"r_{degree}" for degree in range(3, -1, -1))
    source_variables.extend(f"Q_{degree}" for degree in range(2, -1, -1))
    blocks = {n: [] for n in range(1, 14)}
    blocks[2] = [f"Q_{degree}" for degree in range(2, -1, -1)]
    blocks[5] = [f"r_{degree}" for degree in range(3, -1, -1)]
    blocks[6] = [f"e_{degree}" for degree in range(6, -1, -1)]
    blocks[7] = [f"f_{degree}" for degree in range(5, -1, -1)]
    for n in range(8, 14):
        blocks[n] = [windows["F"][n][degree]
                     for degree in sorted(windows["F"][n], reverse=True)]
    return F, source_variables, blocks


def compile_gate_system(system_id, F, source_variables, blocks, scope):
    gates = []
    equations = []
    primitive_variables = []
    for n in range(1, 14):
        gate = exactness_gate(F, n)
        gate["new_source_variables"] = blocks[n]
        gate["new_variables"] = blocks[n] + gate["primitive_variables"]
        gates.append(gate)
        equations.extend(gate["equations"])
        primitive_variables.extend(gate["primitive_variables"])
    variables = source_variables + primitive_variables
    assert len(variables) == len(set(variables))
    used = {name for equation in equations for mon, _ in equation["terms"] for name in mon}
    assert used <= set(variables), sorted(used - set(variables))
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-Q1-Q13-DE-RHAM-GATES-v1",
        "system_id": system_id,
        "field": "Q",
        "formula": "q_n=2/(n+2)*[t^n]F^((n+2)/8)",
        "component_model": "p^2=+/-A; twist changes each character equation by a nonzero scalar",
        "tail_license": "D22=1 and D23=...=D35=0; q13 uses the structural terminal-row cancellation/license",
        "scope": scope,
        "source_variables": source_variables,
        "source_variable_count": len(source_variables),
        "primitive_variables": primitive_variables,
        "primitive_variable_count": len(primitive_variables),
        "variables": variables,
        "variable_count": len(variables),
        "gates": gates,
        "equations": equations,
        "equation_count": len(equations),
        "pins": {str(path.relative_to(ROOT)): digest for path, digest in PINS.items()},
    }


def decode(encoded):
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def singular_script(system, modulus: int, order: str, algorithm: str, tracked=False):
    assert order in ("lp", "dp") and algorithm in ("std", "slimgb")
    variables = system["variables"]
    expressions = [decode(item["terms"]).expression(modulus) for item in system["equations"]]
    lines = [
        "// Exact q1..q13 de Rham gate ideal.",
        f"ring qgates={modulus},({','.join(variables)}),{order};",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("QGATES variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        'print("START_GROEBNER");',
    ]
    if tracked:
        lines.extend([
            "matrix T; ideal J=liftstd(I,T);",
            "matrix basis_replay=matrix(I)*T-matrix(J);",
            'print("BASIS_REPLAY_ZERO="+string(size(module(basis_replay))==0));',
        ])
    else:
        lines.append(f"ideal J={algorithm}(I);")
    lines.extend([
        "int elapsed=timer-start_time;",
        'print("END_GROEBNER seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
    ])
    if tracked:
        lines.extend([
            "if(is_unit){",
            "  matrix H=lift(J,ideal(1));",
            "  matrix C=T*H;",
            "  matrix replay=matrix(I)*C-matrix(ideal(1));",
            '  print("UNIT_REPLAY_ZERO="+string(size(module(replay))==0));',
            '  write("unit_cofactors.txt",C);',
            "}",
        ])
    lines.extend(["quit;", ""])
    return "\n".join(lines)


def encode_poly(poly):
    return [item.encode() for item in poly]


def assert_poly_equal(left, right, label):
    assert ce.xtrim(left) == ce.xtrim(right), label


def desk_check():
    for path, expected in PINS.items():
        actual = sha256(path)
        assert expected != "TO_BE_FROZEN", f"unfrozen pin: {path} actual={actual}"
        assert actual == expected, (path, actual, expected)
    source = json.loads(RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    ce.verify_windows(windows)

    # q1, q2, q3 fixed-slice identities from the all-row formula.
    low = {}
    for lam in (0, 1):
        F, _, _ = full_slice_F(lam, windows)
        q1 = q_fraction(F, 1)
        q2 = q_fraction(F, 2)
        q3 = q_fraction(F, 3)
        _, S, _, U, _, Z, _, _ = rawc.fixed_polynomials(lam)
        if lam == 0:
            assert not q1[2]
        else:
            assert q1[:2] == (1, 0)
            assert_poly_equal(q1[2], ce.xscale(S, Q(1, 4)), f"lambda{lam} q1")
        assert q2[:2] == (0, 0)
        assert_poly_equal(q2[2], ce.xscale(Z, Q(1, 16)), f"lambda{lam} q2")
        if lam == 0:
            assert q3[:2] == (1, 0)
            assert_poly_equal(q3[2], ce.xscale(U, Q(1, 32)), "lambda0 q3")
        else:
            expected_numerator = ce.xscale(xsum(
                ce.xscale(ce.xmul(A, U), 16),
                ce.xscale(ce.xmul(S, Z), 4),
                ce.xscale(ce.xmul(ce.xmul(S, S), S), -1),
            ), Q(1, 512))
            assert q3[:2] == (1, 1)
            assert_poly_equal(q3[2], expected_numerator, "lambda1 q3")
        low[f"lambda_{lam}"] = {
            "q1": {"character": q1[0], "A_denominator": q1[1], "numerator": encode_poly(q1[2])},
            "q2": {"character": q2[0], "A_denominator": q2[1], "numerator": encode_poly(q2[2])},
            "q3": {"character": q3[0], "A_denominator": q3[1], "numerator": encode_poly(q3[2])},
        }

    # Parent-provided q5/q7/q9 hand expressions are checksums only: derive
    # them again from the Lagrange recurrence before comparison.
    reduced_F, _, _ = reduced_lambda0_F(windows)
    checks = {}
    Qpoly = tuple(MV.var(f"Q_{degree}") for degree in range(3))
    Rpoly = tuple(MV.var(f"r_{degree}") for degree in range(4))
    fpoly = tuple(MV.var(f"f_{degree}") for degree in range(6))
    F9 = reduced_F[9]
    expected = {
        5: ce.xscale(Rpoly, Q(1, 1024)),
        7: xsum(ce.xscale(fpoly, Q(1, 4)),
                ce.xscale(ce.xmul(Qpoly, Rpoly), Q(-1, 65536))),
        9: xsum(ce.xscale(F9, Q(1, 4)),
                ce.xscale(ce.xmul(Qpoly, fpoly), Q(-3, 256)),
                ce.xscale(ce.xmul(ce.xmul(Qpoly, Qpoly), Rpoly), Q(-3, 8388608))),
    }
    for n in (5, 7, 9):
        actual = q_fraction(reduced_F, n)
        assert actual[:2] == (3, 0), (n, actual[:2])
        assert_poly_equal(actual[2], expected[n], f"reduced q{n}")
        checks[f"q{n}"] = {"character": 3, "A_denominator": 0,
                            "numerator": encode_poly(actual[2])}
    q8 = q_fraction(reduced_F, 8)
    F8 = reduced_F[8]
    Epoly = tuple(MV.var(f"e_{degree}") for degree in range(7))
    expected_q8 = ce.xmul(A, xsum(
        ce.xscale(F8, Q(1, 4)),
        ce.xscale(ce.xmul(Qpoly, Epoly), Q(-1, 2 ** 18)),
        ce.xscale(ce.xpow(Qpoly, 4), Q(-1, 2 ** 23)),
    ))
    assert q8[:2] == (0, 0)
    assert_poly_equal(q8[2], expected_q8, "reduced q8 even guard")
    checks["q8_even_guard"] = {"character": 0, "A_denominator": 0,
                                "numerator": encode_poly(q8[2])}
    return {
        "status": "DESK_CHECK_PASS",
        "q1_q2_q3": low,
        "reduced_lambda0_anchor_rederivation": checks,
        "pins": {str(path.relative_to(ROOT)): sha256(path) for path in PINS},
    }


def write_outputs(output_dir: Path):
    audit = desk_check()
    source = json.loads(RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "DESK_CHECK.json").write_bytes(ce.pretty(audit))
    manifest = {"DESK_CHECK.json": sha256(output_dir / "DESK_CHECK.json")}
    specs = []
    for lam in (0, 1):
        F, variables, blocks = full_slice_F(lam, windows)
        specs.append((
            f"lambda_{lam}_full_qgates", F, variables, blocks,
            {
                "lambda": lam,
                "kind": "necessary full-tail de Rham screen for the literal fixed slice",
                "raw_D0_D22_endpoint_equations_in_this_file": False,
                "must_intersect_with_raw_endpoint_system_for_survival": True,
                "lambda_nonzero_normalization_claimed": False,
            },
        ))
    F, variables, blocks = reduced_lambda0_F(windows)
    specs.append((
        "lambda_0_c2_nonzero_exact_D0_reduced_qgates", F, variables, blocks,
        {
            "lambda": 0,
            "kind": "reviewed proper subbranch only",
            "conditions": ["c2!=0", "exact defect D=0", "reviewed D11/D12 lifts", "q3 plus A|U gives U=0"],
            "forms": ["F2=-A^3*Q/8", "F4=A^2*Q^2/256", "F5=A^2*r/256", "A|F6", "F7=A*f"],
            "not_the_full_lambda0_slice": True,
            "raw_D0_D22_endpoint_equations_in_this_file": False,
        },
    ))
    for system_id, F, variables, blocks, scope in specs:
        system = compile_gate_system(system_id, F, variables, blocks, scope)
        system_dir = output_dir / system_id
        system_dir.mkdir(parents=True, exist_ok=True)
        payloads = {
            "Q_GATE_SYSTEM.json": ce.pretty(system),
            "qgates_p65521_lp_std.sing": singular_script(system, 65521, "lp", "std").encode(),
            "qgates_p65519_dp_slimgb.sing": singular_script(system, 65519, "dp", "slimgb").encode(),
            "qgates_p65497_dp_slimgb.sing": singular_script(system, 65497, "dp", "slimgb").encode(),
            "qgates_q_lp_std.sing": singular_script(system, 0, "lp", "std").encode(),
            "qgates_q_lp_tracked.sing": singular_script(system, 0, "lp", "std", tracked=True).encode(),
        }
        for name, payload in payloads.items():
            (system_dir / name).write_bytes(payload)
            manifest[f"{system_id}/{name}"] = hashlib.sha256(payload).hexdigest()
        print(json.dumps({
            "event": "Q_GATE_SYSTEM_COMPILED", "system_id": system_id,
            "variables": system["variable_count"], "equations": system["equation_count"],
            "sha256": manifest[f"{system_id}/Q_GATE_SYSTEM.json"],
        }, sort_keys=True), flush=True)
    (output_dir / "GENERATED.sha256.json").write_bytes(ce.pretty(manifest))
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desk-check", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.desk_check == (args.output_dir is not None):
        parser.error("choose exactly one of --desk-check or --output-dir")
    if args.desk_check:
        print(json.dumps(desk_check(), indent=2, sort_keys=True))
    else:
        manifest = write_outputs(args.output_dir)
        print(json.dumps({"status": "Q_GATE_COMPILE_PASS", "artifact_count": len(manifest)}, sort_keys=True))


if __name__ == "__main__":
    main()
