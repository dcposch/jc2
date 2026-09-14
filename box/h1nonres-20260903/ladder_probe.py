#!/usr/bin/env python3
"""One-core exact probes for the proposed NONRES Jacobian ladder.

This intentionally builds only the top-form B1 Jacobian contribution and the
D=108 common-h3 incidence rows.  It does not compile a full joint chart and it
does not promote a nonzero linear coefficient to a unit-ideal certificate.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import argparse
import hashlib
import importlib.util
import json
from math import ceil, comb, factorial, gcd
from pathlib import Path
import re
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
FROZEN = Path("/tmp/jc2-lane.7wKvYN/inputs/moh_skeleton_full.py")


def load_frozen_moh():
    spec = importlib.util.spec_from_file_location("h1nonres_frozen_moh", FROZEN)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


MOH = load_frozen_moh()


@dataclass(frozen=True)
class Wanted:
    label: str
    n: int
    m: int
    middle: tuple[int, ...]
    values: tuple[tuple[int, int], ...]


WANTED = (
    Wanted("(99,66)", 99, 66, (77, 97), ((2, 8), (3, 8))),
    Wanted("D=108", 108, 72, (81, 106), ((2, 7), (3, 7))),
    Wanted("D=126", 126, 84, (-14, 63, 124), ((2, 1), (3, 10), (4, 5))),
)


def census_skeleton(wanted: Wanted):
    matches = []
    target_values = dict(wanted.values)
    for m, middle, values in MOH.census(wanted.n, Kmin=16, full=True):
        if m == wanted.m and tuple(middle) == wanted.middle and values == target_values:
            matches.append(MOH.Skel(wanted.n, m, list(middle), values))
    assert len(matches) == 1, (wanted, len(matches))
    skeleton = matches[0]
    assert skeleton.full_ok() and skeleton.windows_ok()
    return skeleton


def b1_band_polynomial(n: int, m: int, K: int, A: int, B: int, p: int, q: int) -> sp.Expr:
    """Coefficient of t^p in the homogenised Jacobian, B1 block only.

    KF=A0^e and KG=A0^f+t^p*(w-1)^q*A0^(f-1).  Expanding the
    transported Jacobian gives the expression below exactly.
    """
    w = sp.Symbol("w")
    e, f = n // K, m // K
    assert e * K == n and f * K == m
    # Factoring before expansion avoids repeatedly expanding huge powers of
    # A0.  This is identically the derivative expression in the docstring.
    exponent_w = A * (e + f - 1) - 1
    exponent_w_minus_1 = B * (e + f - 1) + q - 1
    linear = K * (q - K + p) * w + A * (K - p)
    factored = e * w**exponent_w * (w - 1) ** exponent_w_minus_1 * linear

    # Derive, rather than merely assume, the displayed linear factor from the
    # transported Jacobian operator.  Factoring only this small bracket keeps
    # the check cheap even when the full row has degree in the hundreds.
    A0 = w**A * (w - 1) ** B
    Q = (w - 1) ** q
    derivative_bracket = n * A0 * sp.diff(Q, w) - e * (K - p) * Q * sp.diff(A0, w)
    factored_bracket = e * w ** (A - 1) * (w - 1) ** (B + q - 1) * linear
    assert sp.factor(derivative_bracket - factored_bracket) == 0

    return factored


def ladder_case(wanted: Wanted) -> dict:
    S = census_skeleton(wanted)
    n, m, K, e, f = S.n, S.m, S.d[2], S.e, S.dd
    ds, vs = S.d[S.s], S.V[S.s]
    us = ds - vs
    assert K % ds == 0
    A, B = us * K // ds, vs * K // ds
    assert A + B == K
    k0 = A * (e + f - 1) - 1
    raw = []
    for p in range(1, vs + 1):
        # Check every ambient B1 coordinate at t-index r=p-1.  Later support
        # cuts may remove some of these coordinates; this is a raw-row check.
        qmax = K - p
        coefficients = []
        for q in range(qmax + 1):
            row = b1_band_polynomial(n, m, K, A, B, p, q)
            # The constructed row is already factored by w^k0.  Read the
            # coefficient without asking Sympy to expand the leading monomial.
            exponent_w_minus_1 = B * (e + f - 1) + q - 1
            linear = K * (q - K + p) * sp.Symbol("w") + A * (K - p)
            shifted = e * (sp.Symbol("w") - 1) ** exponent_w_minus_1 * linear
            assert row == sp.Symbol("w") ** k0 * shifted
            coefficient = int(shifted.subs(sp.Symbol("w"), 0))
            coefficients.append(coefficient)
            assert abs(coefficient) == e * A * (K - p)
        actual = e * A * (K - p)
        corrected = Fraction(n, ds) * (us * (K - p))
        proposed = Fraction(n, ds) * (n - us * p)
        assert corrected.denominator == proposed.denominator == 1
        assert actual == corrected
        raw.append(
            {
                "p": p,
                "q_range_checked": [0, qmax],
                "number_of_coordinates_checked": len(coefficients),
                "signed_coefficients": sorted(set(coefficients)),
                "actual_abs_k0_coefficient": actual,
                "corrected_formula_i0": int(corrected),
                "prompt_formula_i0": int(proposed),
                "prompt_matches": actual == proposed,
            }
        )

    # A nonzero coefficient times a linear functional is not a constant.  The
    # ladder-only ideal has the all-zero common point and hence is proper.
    functionals = sp.symbols(f"L1:{vs + 1}")
    ladder_rows = [raw[index]["actual_abs_k0_coefficient"] * functionals[index] for index in range(vs)]
    basis = sp.groebner(ladder_rows, *functionals, domain=sp.QQ)
    nf_one = basis.reduce(sp.Integer(1))[1]
    assert nf_one == 1

    return {
        "label": wanted.label,
        "census_key": {
            "n": n,
            "m": m,
            "M_2_to_M_s": [S.M[index] for index in range(2, S.s + 1)],
            "V_2_to_V_s": [S.V[index] for index in range(2, S.s + 1)],
        },
        "d_1_to_d_splus1": [S.d[index] for index in range(1, S.s + 2)],
        "K=d2": K,
        "e=n/K": e,
        "f=m/K": f,
        "d_s": ds,
        "u_s": us,
        "v_s": vs,
        "gcd(u_s,v_s)": gcd(us, vs),
        "NONRES": all((us * p) % ds for p in range(1, vs + 1)),
        "top_K2": f"w^{A}(w-1)^{B}",
        "A": A,
        "B": B,
        "k0": k0,
        "identity_needed_by_prompt": {"n_equals_u_s_times_d2": n == us * K},
        "raw_B1_k0_rows": raw,
        "ladder_only_ideal": {
            "ring": "Q[L1,...,L_v_s]",
            "rows": [str(row) for row in ladder_rows],
            "normal_form_of_1": str(nf_one),
            "all_zero_common_point": True,
            "unit_ideal": False,
        },
    }


def banked_9966_pivots() -> dict:
    paths = {
        "delta=5/2": ROOT / "box/g9966s8-20260903/runs/delta52/stage8.json",
        "delta=2": ROOT / "box/g9966band-20260903/runs/delta2/stage4.json",
    }
    result = {}
    pattern = re.compile(r"stage(?P<p>[0-9]+)_J_d[0-9]+_k(?P<k>[0-9]+)$")
    for branch, path in paths.items():
        ledger = json.loads(path.read_text(encoding="utf-8"))["joint_elimination"]["pivot_ledger"]
        checked = []
        non_jacobian = []
        for entry in ledger:
            match = pattern.match(entry["row"])
            if match is None:
                non_jacobian.append(entry)
                continue
            p, k = int(match.group("p")), int(match.group("k"))
            i = k - 35
            coefficient = Fraction(entry["coefficient"])
            expected = 9 * (99 - 3 * p - 11 * i)
            assert abs(coefficient) == expected
            assert expected == Fraction(99, 11) * (99 - 3 * p - 11 * i)
            checked.append({"p": p, "i": i, "coefficient": str(coefficient), "abs": expected})
        result[branch] = {
            "ledger_pivots": len(ledger),
            "Jacobian_pivots_checked": len(checked),
            "non_Jacobian_pivots": [
                {"row": item["row"], "coefficient": item["coefficient"]} for item in non_jacobian
            ],
            "all_match_9(99-3p-11i)": True,
            "minimum_abs_Jacobian_pivot": min(item["abs"] for item in checked),
        }
    assert result["delta=5/2"]["Jacobian_pivots_checked"] == 66
    assert result["delta=2"]["Jacobian_pivots_checked"] == 31
    assert result["delta=2"]["ledger_pivots"] == 35
    return result


TZ = dict[tuple[int, int], sp.Expr]


def d108_h3_template() -> tuple[TZ, list[sp.Symbol]]:
    result: TZ = {(0, 7): sp.Integer(1), (0, 8): sp.Integer(2), (0, 9): sp.Integer(1)}
    variables = []
    for r in range(1, 10):
        vmin = max(0, ceil((43 - 4 * r) / 6))
        cap = 9 - r
        for degree in range(vmin, cap + 1):
            variable = sp.Symbol(f"Hc_{r}_{degree}")
            variables.append(variable)
            for q in range(vmin, degree + 1):
                result[(r, q)] = result.get((r, q), sp.Integer(0)) + variable * comb(
                    degree - vmin, q - vmin
                )
    assert [str(item) for item in variables] == [
        "Hc_1_7", "Hc_1_8", "Hc_2_6", "Hc_2_7", "Hc_3_6", "Hc_4_5", "Hc_5_4"
    ]
    return result, variables


def d108_incidence_rows() -> tuple[list[tuple[str, sp.Expr]], list[sp.Symbol]]:
    h3, variables = d108_h3_template()
    wbasis: TZ = defaultdict(lambda: sp.Integer(0))
    for (r, q), coefficient in h3.items():
        for j in range(q + 1):
            wbasis[(r, j)] += coefficient * comb(q, j) * (-1) ** (q - j)
    wbasis = {key: sp.expand(value) for key, value in wbasis.items() if sp.expand(value) != 0}
    jet1, jet2, c = sp.symbols("jet1 jet2 c")
    collected: TZ = defaultdict(lambda: sp.Integer(0))
    for (r, j), coefficient in wbasis.items():
        for a in range(j + 1):
            for b in range(j - a + 1):
                k = j - a - b
                local_power = r + 2 * a + 3 * b + 4 * k
                if local_power > 8:
                    continue
                multinomial = factorial(j) // (factorial(a) * factorial(b) * factorial(k))
                collected[(local_power, k)] += coefficient * multinomial * jet1**a * jet2**b
    collected[(8, 0)] -= c
    collected[(8, 2)] += 1
    rows = [
        (f"minor_n{power}_pi{k}", sp.expand(value))
        for (power, k), value in sorted(collected.items())
        if sp.expand(value) != 0 or (power, k) == (8, 2)
    ]
    assert len(rows) == 13
    return rows, variables


def qstar_reduce(rows: list[tuple[str, sp.Expr]], eligible: list[sp.Symbol]):
    work = [(label, sp.expand(row)) for label, row in rows if row != 0]
    available = set(eligible)
    pivots = []
    while True:
        selected = None
        for index, (label, row) in enumerate(work):
            for variable in sorted(row.free_symbols & available, key=str):
                coefficient = sp.diff(row, variable)
                remainder = sp.expand(row - coefficient * variable)
                if coefficient.is_Rational and coefficient != 0 and variable not in remainder.free_symbols:
                    selected = index, label, variable, sp.Rational(coefficient), remainder
                    break
            if selected is not None:
                break
        if selected is None:
            break
        index, label, variable, coefficient, remainder = selected
        rhs = sp.cancel(-remainder / coefficient)
        pivots.append((label, variable, coefficient, rhs))
        available.remove(variable)
        del work[index]
        work = [(old_label, sp.expand(old_row.subs(variable, rhs))) for old_label, old_row in work]
    return [(label, sp.expand(row)) for label, row in work if row != 0], pivots


def d108_incidence_probe() -> dict:
    rows, variables = d108_incidence_rows()
    residual, pivots = qstar_reduce(rows, variables)
    expected = {
        "minor_n6_pi0": "-jet2**2",
        "minor_n7_pi0": "2*jet1**2*jet2",
        "minor_n7_pi1": "-2*jet2",
        "minor_n8_pi0": "-c - jet1**4 + 9*jet1*jet2**2",
        "minor_n8_pi1": "2*jet1**2",
    }
    assert {label: str(value) for label, value in residual} == expected
    assert len(pivots) == 7
    assert [str(item[2]) for item in pivots] == ["-1", "1", "1", "-1", "1", "-1", "1"]
    prompt_i0 = [12 * (108 - 2 * p) for p in range(1, 8)]
    actual_jacobian_i0 = [24 * (36 - p) for p in range(1, 8)]
    return {
        "raw_labels": len(rows),
        "Qstar_pivots": [
            {"row": label, "variable": str(variable), "coefficient": str(coefficient)}
            for label, variable, coefficient, _rhs in pivots
        ],
        "residual": expected,
        "prompt_Jacobian_formula_i0": prompt_i0,
        "actual_raw_B1_Jacobian_i0": actual_jacobian_i0,
        "same_family": False,
        "closed_form_reproduces_incidence_residues": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    cases = [ladder_case(item) for item in WANTED]
    payload = {
        "type": "H1-NONRES / EXACT RAW-LADDER AND D108-INCIDENCE PROBE",
        "frozen_census": str(FROZEN),
        "banked_9966": banked_9966_pivots(),
        "cases": cases,
        "D108_incidence": d108_incidence_probe(),
        "conclusion": {
            "prompt_numeric_generalization": "false outside n=u_s*d2",
            "correct_raw_k0_formula": "+/- (n/d_s)*u_s*(d2-p)",
            "corrected_9966_fitted_extension": "+/- (n/d_s)*(u_s*(d2-p)-d_s*i)",
            "NONRES_congruence_survives_correction": True,
            "reason": "d_s divides d2, so both candidate zero conditions imply d_s divides u_s*p",
            "nonzero_ladder_row_implies_unit_ideal": False,
        },
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output_dir is not None:
        output_dir = args.output_dir.resolve()
        assert output_dir == Path(__file__).resolve().parent
        output_dir.mkdir(parents=True, exist_ok=True)
        output = output_dir / "ladder_probe.stdout.json"
        output.write_text(rendered, encoding="utf-8")

        def sha256(path: Path) -> str:
            digest = hashlib.sha256()
            digest.update(path.read_bytes())
            return digest.hexdigest()

        artifacts = (Path(__file__).resolve(), output)
        manifest = output_dir / "ladder-artifacts.sha256"
        manifest.write_text(
            "".join(f"{sha256(path)}  {path.relative_to(ROOT)}\n" for path in artifacts),
            encoding="utf-8",
        )
        check = subprocess.run(
            ["sha256sum", "-c", str(manifest.relative_to(ROOT))],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        (output_dir / "ladder-artifacts.sha256.check.log").write_text(
            check.stdout, encoding="utf-8"
        )
    print(rendered, end="")


if __name__ == "__main__":
    main()
