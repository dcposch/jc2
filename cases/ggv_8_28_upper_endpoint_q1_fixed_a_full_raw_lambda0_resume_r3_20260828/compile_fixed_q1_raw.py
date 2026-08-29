#!/usr/bin/env python3
"""Compile two literal fixed-A, deep-q1 endpoint coefficient systems.

This is a source compiler, not a solver.  It keeps X external and expands
the authoritative raw recurrence over Q through the complete supported tail
D35.  The only restrictions beyond the raw windows are the preregistered fixed slices

    A=X^4-1, R0=lambda*A, S=3*lambda*A', V0=A*S, T=A*U,

for lambda=0 and lambda=1.  Rows D23,...,D35 are imposed, so the q1 through
q13 exactness gates are licensed by the reviewed characteristic/de Rham
connection.  The q1 restriction is not claimed from D0,...,D22 alone.
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
BASE_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
Q1_CASE = ROOT / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828"
Q1_CHECKER = Q1_CASE / "verify_q1_prefix_target.py"
Q1_README = Q1_CASE / "README.md"
Q1_RESULT = Q1_CASE / "RESULT.json"
Q1_TARGET = Q1_CASE / "TARGET.json"
R7R1 = ROOT / "cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py"
DEEP_Q1_R1 = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py"


PINS = {
    BASE_COMPILER: "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    RAW_INPUT: "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    Q1_CHECKER: "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119",
    Q1_README: "ef2adf41201e201a907e4a0b2e1316c0e1ca08775b3f434310dba9a0b5a3de76",
    Q1_RESULT: "ba900c6eacc7302491105bec49516d2e95dff982959a3904370b7e540216260b",
    Q1_TARGET: "c41f04a93f509adb1f430e808c69cd2171439c9e19fb001c6ea2bf0f29633a46",
    R7R1: "1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa",
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


ce = load_module("ggv_fixed_q1_raw_base", BASE_COMPILER)
MV = ce.MV
M0 = MV.zero()


def xsum(*items):
    out = ()
    for item in items:
        out = ce.xadd(out, item)
    return out


def xscalar(poly, scalar: MV):
    return tuple(coefficient * scalar for coefficient in poly)


def fixed_polynomials(lam: int):
    assert lam in (0, 1)
    A = (MV.const(-1), M0, M0, M0, MV.const(1))
    Aprime = ce.xder(A)
    S = ce.xscale(Aprime, 3 * lam)
    V0 = ce.xmul(A, S)
    U = tuple(MV.var(f"u_{degree}") for degree in range(6))
    T = ce.xmul(A, U)
    Z = tuple(MV.var(f"z_{degree}") for degree in range(7))
    c2 = MV.var("c2")

    F = {
        0: ce.xpow(A, 4),
        1: ce.xmul(ce.xpow(A, 2), V0),
        2: ce.xscale(xsum(ce.xmul(V0, V0), ce.xmul(ce.xpow(A, 2), Z)), Q(1, 4)),
        3: ce.xscale(xsum(ce.xmul(V0, Z), ce.xmul(A, T)), Q(1, 8)),
    }

    # These are independently rederived by desk_check() from F*y'=e*F'*y.
    G = {
        0: ce.xpow(A, 6),
        1: ce.xscale(ce.xmul(ce.xpow(A, 5), S), Q(3, 2)),
        2: xsum(
            ce.xscale(ce.xmul(ce.xpow(A, 4), ce.xmul(S, S)), Q(3, 4)),
            ce.xscale(ce.xmul(ce.xpow(A, 4), Z), Q(3, 8)),
            xscalar(ce.xpow(A, 5), c2),
        ),
        3: xsum(
            ce.xscale(ce.xmul(ce.xpow(A, 3), ce.xmul(ce.xmul(S, S), S)), Q(1, 8)),
            ce.xscale(ce.xmul(ce.xpow(A, 3), ce.xmul(S, Z)), Q(3, 8)),
            ce.xscale(ce.xmul(ce.xpow(A, 4), U), Q(3, 16)),
            ce.xscale(xscalar(ce.xmul(ce.xpow(A, 4), S), c2), Q(5, 4)),
        ),
    }
    return A, S, V0, U, T, Z, F, G


def recurrence_rows(F, G, maximum=35):
    rows = {}
    for n in range(maximum + 1):
        value = ()
        for i in range(n + 1):
            j = n - i
            if i not in F or j not in G:
                continue
            value = ce.xadd(value, ce.xscale(ce.xmul(ce.xder(F[i]), G[j]), 12 - j))
            value = ce.xadd(value, ce.xscale(ce.xmul(F[i], ce.xder(G[j])), i - 8))
        rows[n] = value
    return rows


def build_system(source, lam: int):
    windows = ce.raw_windows(source)
    census = ce.verify_windows(windows)
    A, S, V0, U, T, Z, F, G = fixed_polynomials(lam)

    for weight in range(4, 15):
        F[weight] = ce.xvar_poly(windows["F"][weight])
    for weight in range(4, 22):
        G[weight] = ce.xvar_poly(windows["G"][weight])

    rows = recurrence_rows(F, G, 35)
    for n in range(4):
        assert not rows[n], f"fixed/cascade row D{n} did not vanish for lambda={lam}"

    generators = []
    per_row = {}
    for n in range(4, 36):
        target = 1 if n == 22 else 0
        count = 0
        max_degree = max(len(rows[n]), 1 if target else 0)
        for degree in range(max_degree):
            coefficient = rows[n][degree] if degree < len(rows[n]) else M0
            if degree == 0 and target:
                coefficient = coefficient - MV.const(1)
            if coefficient.terms:
                encoded = coefficient.encode()
                generators.append({
                    "row": n,
                    "x_degree": degree,
                    "terms": encoded,
                    "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
                })
                count += 1
        row_records = [item for item in generators if item["row"] == n]
        per_row[str(n)] = {
            "target": target,
            "generator_count": count,
            "raw_polynomial_degree": len(rows[n]) - 1,
            "row_sha256": hashlib.sha256(ce.compact(row_records)).hexdigest(),
        }

    variables = []
    for weight in range(21, 3, -1):
        if weight in windows["G"]:
            variables.extend(windows["G"][weight][degree]
                             for degree in sorted(windows["G"][weight], reverse=True))
        if weight in windows["F"]:
            variables.extend(windows["F"][weight][degree]
                             for degree in sorted(windows["F"][weight], reverse=True))
    variables.append("c2")
    variables.extend(f"u_{degree}" for degree in range(5, -1, -1))
    variables.extend(f"z_{degree}" for degree in range(6, -1, -1))
    assert len(variables) == len(set(variables)) == 300

    used = sorted({name for item in generators for mon, _ in item["terms"] for name in mon})
    assert set(used) <= set(variables)
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-Q1-FIXED-A-FULL-RAW-v1",
        "field": "Q",
        "slice": {
            "lambda": lam,
            "A": "X^4-1",
            "R0": f"{lam}*A",
            "S": f"{3 * lam}*A'",
            "V0": "A*S",
            "T": "A*U",
            "degree_U_at_most": 5,
            "degree_Z_at_most": 6,
        },
        "recurrence": "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')",
        "charged_rows": {
            "zero": list(range(22)) + list(range(23, 36)),
            "affine_target": {"row": 22, "value": 1},
            "D0_D3_verified_identically": True,
            "D23_through_D35_imposed": True,
        },
        "q1_firewall": {
            "status": "full tail D23..D35 imposed; q1..q13 exactness licensed by reviewed tower theorem",
            "not_claimed_from_D0_through_D22": True,
            "D23_equation_in_this_ideal": True,
            "D35_note": "included literally; any structural cancellation must be replayed from the compiled row",
        },
        "lambda_firewall": {
            "lambda_0_and_1_are_separate_literal_slices": True,
            "lambda_nonzero_normalization_claimed": False,
            "lambda_1_is_diagnostic_unless_a_separate_normalization_theorem_is_supplied": True,
        },
        "low_prefix": {
            "F0": "A^4",
            "F1": "A^3*S",
            "F2": "A^2*(S^2+Z)/4",
            "F3": "A*(S*Z+A*U)/8",
            "G0": "A^6",
            "G1": "3*A^5*S/2",
            "G2": "3*A^4*S^2/4+3*A^4*Z/8+c2*A^5",
            "G3": "A^3*S^3/8+3*A^3*S*Z/8+3*A^4*U/16+5*c2*A^4*S/4",
        },
        "slotless": {"F_max_weight": 14, "G_max_weight": 21, "G22_present": False},
        "variables": variables,
        "variable_count": len(variables),
        "windows": census,
        "generators": generators,
        "generator_count": len(generators),
        "per_row": per_row,
        "pins": {str(path.relative_to(ROOT)): digest for path, digest in PINS.items()},
    }


def mode_audit(system):
    windows = system["windows"]["G"]
    modes = {
        2: "5/4", 4: "1", 6: "3/4", 8: "1/2", 10: "1/4",
        12: "0", 14: "-1/4", 16: "-1/2", 18: "-3/4", 20: "-1",
    }
    records = []
    for birth, exponent in modes.items():
        if birth == 2:
            representation = "explicit c2 in G2 and its linked G3 contribution"
        else:
            assert str(birth) in windows
            representation = (
                "retained inside the complete free raw G%d window; no mode value is fixed or omitted" % birth
            )
        records.append({
            "birth": birth,
            "exponent": exponent,
            "representation": representation,
            "raw_G_window": None if birth == 2 else [windows[str(birth)]["lower"], windows[str(birth)]["upper"]],
        })
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-Q1-FULL-MODE-AUDIT-v1",
        "modes": records,
        "raw_coordinate_firewall": (
            "c4,...,c20 are not adjoined a second time: complete raw G4,...,G21 "
            "coefficients are the primitive coordinates and include every polynomial trajectory, "
            "including trajectories whose reconstructed negative-power modes c14,...,c20 are forced nonzero"
        ),
        "no_mode_zero_assumption_except_none": True,
    }


def decode(encoded):
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def singular_script(system, modulus: int, order: str, algorithm: str):
    assert order in ("lp", "dp")
    assert algorithm in ("std", "slimgb")
    variables = system["variables"]
    expressions = [decode(item["terms"]).expression(modulus) for item in system["generators"]]
    lines = [
        "// Literal fixed-A deep-q1 raw endpoint system.",
        f"ring fixed_q1={modulus},({','.join(variables)}),{order};",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        'print("RAW variables="+string(nvars(basering))+" generators="+string(size(I)));',
        "int start_time=timer;",
        'print("START_GROEBNER");',
        f"ideal J={algorithm}(I);",
        "int elapsed=timer-start_time;",
        'print("END_GROEBNER seconds="+string(elapsed));',
        'print("BASIS_SIZE="+string(size(J)));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
        "quit;",
        "",
    ]
    return "\n".join(lines)


def parse_script(system):
    text = singular_script(system, 0, "lp", "std")
    return text.split("int start_time=timer;", 1)[0] + 'print("PARSE_PASS");\nquit;\n'


def desk_check():
    for path, expected in PINS.items():
        actual = sha256(path)
        assert expected != "TO_BE_FROZEN", f"unfrozen pin: {path} actual={actual}"
        assert actual == expected, (path, actual, expected)

    q1 = load_module("ggv_fixed_q1_formula_source", Q1_CHECKER)
    formal_F = q1.general_prefix(3)
    _, formal_G = q1.continuation(formal_F, 3)
    substitutions = {"v0": q1.la_term(1, 1, "s"), "t": q1.la_term(1, 1, "u")}
    actual = {weight: q1.la_substitute(formal_G[weight], substitutions) for weight in range(4)}
    expected = {
        0: q1.la_term(1, 6),
        1: q1.la_term(Q(3, 2), 5, "s"),
        2: q1.la_add(q1.la_term(Q(3, 4), 4, "s", "s"),
                     q1.la_term(Q(3, 8), 4, "z"), q1.la_term(1, 5, "c2")),
        3: q1.la_add(q1.la_term(Q(1, 8), 3, "s", "s", "s"),
                     q1.la_term(Q(3, 8), 3, "s", "z"),
                     q1.la_term(Q(3, 16), 4, "u"),
                     q1.la_term(Q(5, 4), 4, "c2", "s")),
    }
    assert actual == expected

    source = json.loads(RAW_INPUT.read_text())
    windows = ce.raw_windows(source)
    census = ce.verify_windows(windows)
    for lam in (0, 1):
        *_, F, G = fixed_polynomials(lam)
        rows = recurrence_rows(F, G, 3)
        assert all(not rows[n] for n in range(4))
    return {
        "status": "DESK_CHECK_PASS",
        "low_G": {f"G{weight}": q1.la_encode(actual[weight]) for weight in range(4)},
        "window_dimensions": {
            kind: {weight: item["dimension"] for weight, item in census[kind].items()}
            for kind in ("F", "G")
        },
        "pins": {str(path.relative_to(ROOT)): sha256(path) for path in PINS},
    }


def write_outputs(output_dir: Path):
    audit = desk_check()
    source = json.loads(RAW_INPUT.read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "DESK_CHECK.json").write_bytes(ce.pretty(audit))
    manifest = {}
    for lam in (0, 1):
        system = build_system(source, lam)
        slice_dir = output_dir / f"lambda_{lam}"
        slice_dir.mkdir(parents=True, exist_ok=True)
        payloads = {
            "RAW_DIRECT_SYSTEM.json": ce.pretty(system),
            "MODE_AUDIT.json": ce.pretty(mode_audit(system)),
            "raw_parse.sing": parse_script(system).encode(),
            "raw_p65521_lp_std.sing": singular_script(system, 65521, "lp", "std").encode(),
            "raw_p65521_dp_slimgb.sing": singular_script(system, 65521, "dp", "slimgb").encode(),
            "raw_q_lp_std.sing": singular_script(system, 0, "lp", "std").encode(),
            "raw_q_dp_slimgb.sing": singular_script(system, 0, "dp", "slimgb").encode(),
        }
        for name, payload in payloads.items():
            (slice_dir / name).write_bytes(payload)
            manifest[f"lambda_{lam}/{name}"] = hashlib.sha256(payload).hexdigest()
        print(json.dumps({
            "event": "SLICE_COMPILED", "lambda": lam,
            "variables": system["variable_count"], "generators": system["generator_count"],
            "system_sha256": manifest[f"lambda_{lam}/RAW_DIRECT_SYSTEM.json"],
        }, sort_keys=True), flush=True)
    manifest["DESK_CHECK.json"] = sha256(output_dir / "DESK_CHECK.json")
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
        print(json.dumps({"status": "COMPILE_PASS", "artifact_count": len(manifest)}, sort_keys=True))


if __name__ == "__main__":
    main()
