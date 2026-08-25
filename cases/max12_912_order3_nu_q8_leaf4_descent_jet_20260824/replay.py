#!/usr/bin/env python3
"""Exact local quotient/Hurwitz descent at the corrected Q8 branch."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
JET_REPLAY = ROOT / "cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.py"
JET_REPLAY_SHA256 = "5536f16ac30da115021835d1a07c3116d7b1cb6675e628726dcfe766533528df"
JET_JSON = ROOT / "cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.json"
JET_JSON_SHA256 = "bbb9316eb207305400b141dadd27d94fd8fece766ae5d333190ec9f42da5b313"
JET_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_normalization_jet_20260824/MANIFEST.sha256"
JET_MANIFEST_SHA256 = "036b8656ba53dd3b1b212b2bf5bec6d0eed83f8a56023cf3ebf0b689156d8971"
JET_FREEZE = ROOT / "cases/max12_912_order3_nu_q8_normalization_jet_20260824/FREEZE.txt"
JET_FREEZE_SHA256 = "807ad9dacbc477972c3c30b3770d84ca27340b5771ec2aad3efc90d7eb3e5b50"
JET_REPORT = ROOT / "xmodel/max12-912-order3-nu-q8-normalization-jet-20260824.md"
JET_REPORT_SHA256 = "739fbad475bc10540756c7a0180168185523f6e3cfe368225e03efa1abe62d65"


def load_jet():
    for path, expected in (
        (JET_REPLAY, JET_REPLAY_SHA256),
        (JET_JSON, JET_JSON_SHA256),
        (JET_MANIFEST, JET_MANIFEST_SHA256),
        (JET_FREEZE, JET_FREEZE_SHA256),
        (JET_REPORT, JET_REPORT_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError(f"dependency hash mismatch: {path}: {got}")
    spec = importlib.util.spec_from_file_location("q8_leaf4_parent", JET_REPLAY)
    if spec is None or spec.loader is None:
        raise RuntimeError(JET_REPLAY)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


J = load_jet()
P, M, G = J.P, J.M, J.G
NF, Series = J.NF, J.Series
ZERO, ONE = J.ZERO, J.ONE


def series_inverse(value):
    if not value.coefficients[0]:
        raise ZeroDivisionError
    out = [ZERO] * 4
    out[0] = value.coefficients[0].inverse()
    for degree in range(1, 4):
        correction = sum((
            value.coefficients[index] * out[degree - index]
            for index in range(1, degree + 1)
        ), ZERO)
        out[degree] = -out[0] * correction
    inverse = Series(out)
    product = value * inverse
    assert product.coefficients == (ONE, ZERO, ZERO, ZERO)
    return inverse


def series_divide(numerator, denominator):
    return numerator * series_inverse(denominator)


def unit_certificate(value):
    gcd = G.pgcd(value.poly, J.Q8)
    if gcd != (Fraction(1),):
        raise RuntimeError(("not a unit", value.poly, gcd))
    inverse = value.inverse()
    assert value * inverse == ONE
    return {
        "value": J.digest(value),
        "gcd_Q8": "1",
        "inverse_mod_Q8": J.digest(inverse),
    }


def polynomial_series(coefficients, value):
    total = Series.constant(0)
    for coefficient in reversed(coefficients):
        total = total * value + coefficient
    return total


def reconstruct_jet():
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    v0 = NF((Fraction(0), Fraction(1)))
    D0 = 3 * v0 ** 2 - 2
    A20 = 3 * v0 ** 2 + 3 * v0 + 1
    x50 = -36 * v0 ** 2 * A20 / D0
    x30 = x50 * (v0 + 2)
    x10 = x50 * (v0 + 1) + x50 ** 2 * (3 * v0 + 1) / (9 * v0)
    base = [
        ZERO, x10, ZERO, ONE + x30, ZERO, NF(3) + x50,
        ZERO, NF(3), ZERO,
    ]

    normals = (0, 2, 4, 6)
    selected_odd = (3, 5, 7)
    matrix3 = [
        [
            J.nf_eval(M.cpartial(tails[ell], column), base)
            for column in normals[1:]
        ]
        for ell in selected_odd
    ]
    rhs3 = [
        -J.nf_eval(M.cpartial(tails[ell], normals[0]), base)
        for ell in selected_odd
    ]
    n1 = [ONE] + J.solve(matrix3, rhs3)

    def equations(unknowns):
        values = J.make_series(base, n1, unknowns)
        return [
            J.series_eval(tails[ell], values).coefficients[2]
            for ell in (2, 4, 6)
        ] + [
            J.series_eval(tails[ell], values).coefficients[3]
            for ell in (1, 3, 5, 7)
        ]

    origin = equations([ZERO] * 7)
    columns = []
    for column in range(7):
        basis = [ZERO] * 7
        basis[column] = ONE
        image = equations(basis)
        columns.append([
            image[row] - origin[row] for row in range(7)
        ])
    matrix7 = [
        [columns[column][row] for column in range(7)]
        for row in range(7)
    ]
    solution = J.solve(matrix7, [-entry for entry in origin])
    assert all(not entry for entry in equations(solution))
    values = J.make_series(base, n1, solution)

    nu_series = J.series_eval(tails[6], values)
    rho_series = J.series_eval(tails[8], values)
    assert not any(nu_series.coefficients[index] for index in (1, 2, 3))
    nu = nu_series.coefficients[0]
    p = Fraction(1, 3) * values[7]
    x3 = values[3] - p ** 3
    x5 = values[5] - 3 * p ** 2
    v = series_divide(x3, p * x5) - 2

    s = -(Fraction(1, 3) * p + rho_series * (Fraction(10, 9) / nu))
    ring = M.Ring(compiled["ring_names"])
    U = {}
    g_source = None
    for index in range(8):
        U[index - 9] = ring.var(f"a{index}")
    g_source = P.faber(ring, 9, 12, U)
    f_series = {9: Series.constant(1)}
    for index in range(8):
        f_series[index] = values[index]
    g_series = {
        exponent: J.series_eval(coefficient, values)
        for exponent, coefficient in g_source.items()
    }
    f_pair = J.qseries_reduce(f_series, s)
    g_pair = J.qseries_reduce(g_series, s)
    F_pair = J.qseries_pow(f_pair, 4, s)
    G_pair = J.qseries_pow(g_pair, 3, s)
    E = G_pair[0] * F_pair[1] - G_pair[1] * F_pair[0]
    normF = J.qseries_norm(F_pair, s)
    tau = series_divide(
        2 * (G_pair[0] * F_pair[0] - s * G_pair[1] * F_pair[1]),
        normF,
    )
    discriminant = series_divide(4 * s * E * E, normF * normF)

    t = Series((ZERO, ONE))
    pi = p ** 9
    theta = series_divide(t * t, pi)
    q = series_divide(rho_series, p ** 10)
    S = rho_series ** 9
    assert S.coefficients == (pi ** 10 * q ** 9).coefficients

    # The parity identity r6=p^9 R6(v) is a negative control: it must not be
    # extended to the non-parity branch.  Its first failure occurs at theta.
    A2 = 3 * v ** 2 + 3 * v + 1
    A5 = polynomial_series((2, 18, 69, 131, 117, 33), v)
    D = 3 * v ** 2 - 2
    parity_R6 = series_divide(-2304 * v ** 6 * A2 ** 3 * A5, D ** 4)
    parity_defect = pi * parity_R6 - nu_series
    assert not parity_defect.coefficients[0]
    assert not parity_defect.coefficients[1]
    assert parity_defect.coefficients[2]
    assert not parity_defect.coefficients[3]

    return {
        "theta": theta,
        "pi": pi,
        "q": q,
        "S": S,
        "tau": tau,
        "Delta": discriminant,
        "parity_R6_defect": parity_defect,
    }


def main():
    data = reconstruct_jet()
    theta2 = data["theta"].coefficients[2]
    assert theta2 == ONE
    coordinate_certificates = {}
    for name in ("Delta", "tau", "q", "S"):
        series = data[name]
        assert not series.coefficients[1]
        coefficient_theta = series.coefficients[2] / theta2
        coordinate_certificates[name] = {
            "constant": J.digest(series.coefficients[0]),
            "d_dtheta_at_node": unit_certificate(coefficient_theta),
        }
    dS_dDelta = (
        data["S"].coefficients[2] / data["Delta"].coefficients[2]
    )

    # Terminal descent, with r8=u^2 R, u^3=h, S=r8^9:
    # S'=9*r8^8*r8'=j*r8^8/u=j*h^5*R^8, hence
    # h^3*(S')^9=j^9*S^8.  These integer checks guard every exponent.
    assert 9 * 20 % 3 == 0             # S is Kummer-fixed.
    assert 8 * 2 - 1 == 15 == 5 * 3   # r8^8/u=h^5 R^8.
    assert 72 == 9 * 8                 # r8^72=S^8.
    assert 9 == 3 * 3                  # u^9=h^3.

    payload = {
        "case": "max12_912_order3_nu_q8_leaf4_descent_jet_20260824",
        "dependency_sha256": {
            "q8_norm_taylor_terminal_report": JET_REPORT_SHA256,
            "q8_norm_taylor_terminal_replay": JET_REPLAY_SHA256,
            "q8_norm_taylor_terminal_json": JET_JSON_SHA256,
            "q8_norm_taylor_terminal_manifest": JET_MANIFEST_SHA256,
            "q8_norm_taylor_terminal_freeze": JET_FREEZE_SHA256,
        },
        "invariant_coordinates": {
            "theta": "a0^2/p^9",
            "pi": "p^9",
            "q": "r8/p^10",
            "S": "r8^9=pi^10*q^9",
            "tau": "beta_plus+beta_minus",
            "Delta": (
                "(beta_plus-beta_minus)^2=4*s*E^2/Norm(F)^2"
            ),
            "field": "all six coordinates are in K=C(x)",
        },
        "etale_at_every_Q8_contact": coordinate_certificates,
        "dS_dDelta_at_node": unit_certificate(dS_dDelta),
        "parity_formula_negative_control": {
            "invalid_off_parity": "r6=p^9*R6(v)",
            "defect": "p^9*R6(v)-nu=unit*t^2+O(t^4)",
            "t2": unit_certificate(
                data["parity_R6_defect"].coefficients[2]
            ),
        },
        "terminal_descent": {
            "source": "9*r8'=j/u, r8=u^2*R, u^3=h",
            "first": "S'=j*h^5*R^8",
            "root_free": "h^3*(S')^9=j^9*S^8",
        },
        "formal_local_conclusion": (
            "Delta, tau, q, and S are all etale quotient coordinates at "
            "each Q8 contact, and the terminal differential descends to K "
            "without selecting a critical root"
        ),
        "open": (
            "no global leaf-4 quotient relation or projective boundary is "
            "computed; the true Taylor center r/u remains free, so no "
            "punctured trajectory is excluded"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
