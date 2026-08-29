#!/usr/bin/env python3
"""Ordinary and optimized tests for the td=8 Prop. 8.1(iv) affine solver."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "prop81iv_td8_affine.py"
Fr = Fraction


def load_module():
    spec = importlib.util.spec_from_file_location("prop81iv_td8_affine", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("module spec unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


M = load_module()
CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(f"CHECK_FAILED:{label}")


def test_i_chain() -> None:
    c = M.i_chain()
    check(c == {
        "deg_p_pole_full": 4, "l_A": 2, "i_A": 2,
        "dp_A_red": 21, "deg_p_A_full": 42, "mu_G": 3, "i_G": 14,
    }, "i-chain")


def test_pin_and_closed_forms() -> None:
    for t in range(0, 81):
        cell = M.pin_cell(t)
        nu = 4 + 3 * t
        check(cell["nu"] == nu, f"nu-{t}")
        check(cell["dp_red"] == 24 + 18 * t, f"dp-{t}")
        check(cell["dq_red"] == 9 + 6 * t, f"dq-{t}")
        check(cell["M"] == 3, f"M-{t}")
        check(cell["kbar"] == 6 + 4 * t, f"kbar-{t}")
        check(cell["X"] == 16 + 12 * t, f"X-{t}")
        check(cell["i_prop81"] == 14, f"i-{t}")
        check(cell["rho_frame"] == Fr(2, 3), f"frame-rho-{t}")
        check(cell["rho_ode"] == Fr(6 * nu, 2 * nu + 1), f"ode-rho-{t}")
        check(cell["w"] == Fr(4, 3), f"w-{t}")
        ids = M.t_coeff_identities(nu)
        check(ids["t2"] == 0, f"t2-{t}")
        check(ids["t1_factor"] == Fr(3 * nu, 2 * nu + 1), f"t1-{t}")
        check(ids["t1_factor"] != 0, f"t1-nonzero-{t}")
        sides = M.side_conditions(t)
        check(all(sides.values()), f"sides-{t}:{[k for k,v in sides.items() if not v]}")
        sol = M.solve_reduced(t)
        check(sol["sigma"] == "0", f"sigma-{t}")
        check(sol["ctilde"] == M.ft(-cell["rho_ode"]), f"ctilde-{t}")


def test_eta_identity_box() -> None:
    for t in range(0, 12):
        out = M.verify_eta_identity(t)
        check(out["eta_identity"] is True, f"eta-{t}")
        check(out["deg_p"] == 24 + 18 * t, f"eta-dp-{t}")
        check(out["deg_q"] == 9 + 6 * t, f"eta-dq-{t}")
    # Independent gauge a = 2, and the opposite-imaginary gauge via a = 1
    # already covered; a = 3 is a second rational scale.
    for a in (Fr(1), Fr(2), Fr(3)):
        out = M.verify_eta_identity(0, a)
        check(out["eta_identity"] is True, f"eta-a-{a}")


def test_uniqueness() -> None:
    for t in (0, 1, 4, 11):
        u = M.uniqueness_scan(t)
        check(u["good"] > 0 and u["rejected"] > 0, f"uniqueness-counts-{t}")


def test_mutations() -> None:
    """Adversarial mutations of the reduced / eta data must fail."""
    t = 0
    cell = M.pin_cell(t)
    nu = int(cell["nu"])
    rho = cell["rho_ode"]

    # Nonzero sigma leaves a t^1 residue.
    E = M.reduced_E(nu, rho, Fr(1), Fr(-1))
    E = E + [Fr(0)] * (3 - len(E))
    check(E[2] == 0 and E[1] != 0, "mutation-sigma")

    # pi = 0 makes the constant vanish (and collapses the orbits at 0).
    E0 = M.reduced_E(nu, rho, Fr(0), Fr(0))
    check(E0 == [Fr(0)], "mutation-pi-zero")

    # Wrong ODE rho leaves a t^2 residue.
    Ewrong = M.reduced_E(nu, rho + 1, Fr(0), Fr(-1))
    Ewrong = Ewrong + [Fr(0)] * (3 - len(Ewrong))
    check(Ewrong[2] != 0, "mutation-rho")

    # Drop the eta factor: q = S instead of eta*S.  Constant term of the
    # eta-ODE must fail R1.0 (e0 = 0).
    S = M.padd(M.monomial(2 * nu, Fr(1)), [Fr(-1)])
    p = M.ppow(S, 3)
    q_no_eta = S
    lhs = M.ode_left(p, q_no_eta, rho)
    # Residual against any multiple of p: lhs should not be a multiple of p
    # of degree 0, because the order-0 term at eta=0 vanishes on the LHS
    # while p(0) != 0 would be required of a nonzero multiple.
    check(lhs[0] == 0 and pe_nonzero_const(p), "mutation-drop-eta")

    # Extra simple q-orbit: q = eta * S * (eta^nu - 2).
    extra = M.padd(M.monomial(nu, Fr(1)), [Fr(-2)])
    q_ex = M.pmul(M.monomial(1, Fr(1)), M.pmul(S, extra))
    lhs_ex = M.ode_left(p, q_ex, Fr(len(p) - 1, len(q_ex) - 1))
    # Top cancellation uses the new degrees, but extras make the residual
    # a non-constant / non-multiple of p.
    check(not is_multiple(lhs_ex, p), "mutation-extra-orbit")

    # Proportional pattern q = eta * p (R2.3(i)): collapses to a nonconstant
    # times p' on the left, never a multiple of p of degree 0.
    q_prop = M.pmul(M.monomial(1, Fr(1)), p)
    lhs_prop = M.ode_left(p, q_prop, Fr(len(p) - 1, len(q_prop) - 1))
    check(not is_multiple(lhs_prop, p), "mutation-proportional")

    # Wrong multiplicity: mu = 2, p = S^2, q = eta S, rho = 4 nu / (2 nu + 1).
    p2 = M.ppow(S, 2)
    q2 = M.pmul(M.monomial(1, Fr(1)), S)
    rho2 = Fr(4 * nu, 2 * nu + 1)
    lhs2 = M.ode_left(p2, q2, rho2)
    # Opposite orbits still solve the equal-mu two-orbit problem for any mu,
    # so mu=2 is a POSITIVE control that the same sigma=0 law is mu-uniform
    # at pattern level.  Record that it does solve, and that mu=3 is the
    # cell's actual multiplicity.
    ct2 = rho2 * Fr(-1)
    res2 = M.padd(lhs2, M.pscale(p2, -ct2))
    check(res2 == [Fr(0)], "mu2-same-sigma-law")
    check(cell["mu"] == 3, "cell-mu-is-3")

    # Neighboring nu not in the affine family still solves the same pattern
    # ODE; the family constraint is kbar integrality, not (iv).
    ids5 = M.t_coeff_identities(5)
    check(ids5["t2"] == 0 and ids5["t1_factor"] != 0, "nu5-ode-shape")
    check(5 % 3 != 1, "nu5-not-family")


def pe_nonzero_const(p) -> bool:
    return p[0] != 0


def is_multiple(lhs, p) -> bool:
    """True iff lhs = c * p for some constant c (possibly 0)."""
    if lhs == [Fr(0)]:
        return True
    if len(lhs) != len(p):
        return False
    # p monic of known leading 1 in our gauges; compare ratios at the top.
    if p[-1] == 0:
        return False
    c = lhs[-1] / p[-1]
    return M.padd(lhs, M.pscale(p, -c)) == [Fr(0)]


def test_certificate_and_dash_O_identity() -> None:
    cert = M.family_certificate()
    check(cert["verdict_local_prop81iv"] == "PROVED_ADMISSIBLE_FOR_ALL_T_GE_0",
          "verdict")
    fw = cert["firewall"]
    check(fw["local_formal_cell_survival"] is True, "fw-local")
    check(fw["exact_lambda_cost"] is False, "fw-lambda")
    check(fw["source_landing"] is False, "fw-landing")
    check(fw["geometric_realizability"] is False, "fw-real")
    check(fw["degree_bound"] is False, "fw-degree")
    check(fw["jc2"] is False, "fw-jc2")
    check(cert["solution"]["exceptional_t"] == [], "no-exceptions")
    body = json.dumps({k: v for k, v in cert.items()
                       if k != "certificate_sha256"},
                      sort_keys=True, separators=(",", ":")).encode()
    # Recreate the hashed payload the same way the producer does.
    payload = {k: v for k, v in cert.items() if k != "certificate_sha256"}
    body2 = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    import hashlib
    check(hashlib.sha256(body2).hexdigest() == cert["certificate_sha256"],
          "cert-hash")
    # Producer stdout is deterministic.
    r1 = subprocess.run([sys.executable, str(SOURCE)],
                        check=True, capture_output=True, text=True)
    r2 = subprocess.run([sys.executable, str(SOURCE)],
                        check=True, capture_output=True, text=True)
    check(r1.stdout == r2.stdout, "stdout-stable")
    blob = json.loads(r1.stdout)
    check(blob["certificate_sha256"] == cert["certificate_sha256"],
          "stdout-cert")


def test_invalid_t() -> None:
    failed = False
    try:
        M.pin_cell(-1)
    except ValueError:
        failed = True
    check(failed, "invalid-t")


def main() -> int:
    test_i_chain()
    test_pin_and_closed_forms()
    test_eta_identity_box()
    test_uniqueness()
    test_mutations()
    test_certificate_and_dash_O_identity()
    test_invalid_t()
    print(f"TD8_PROP81IV_PARAMETRIC_GROK46_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
