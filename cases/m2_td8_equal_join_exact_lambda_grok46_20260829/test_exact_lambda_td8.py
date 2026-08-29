#!/usr/bin/env python3
"""Tests for the td=8 equal-join exact-lambda packet."""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
import sys
from fractions import Fraction

import exact_lambda_td8 as E


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def test_floors() -> None:
    f = E.recorded_floors()
    check(f["A_step"]["gap_linear"] == "2", "A gap")
    check(f["A_step"]["af2_floor"] == 2, "A floor")
    check(f["A_step"]["linear_in_N"] is True, "A linear in N")
    check(f["trunk"]["gap_linear"] == "3/2", "trunk gap")
    check(f["trunk"]["af2_floor"] == 2, "trunk floor")
    check(f["trunk"]["simple_orbit_ceiling"] == 10, "wrong simple-orbit price")
    check(f["trunk"]["linear_in_N"] is False, "trunk linear not in N")
    check(f["merge_p2_exact"] == 0, "merge P2")
    check(f["recorded_sum"] == 6, "sum")
    check(f["td_minus_1_minus_psi"] == 6, "budget")


def test_closed_forms() -> None:
    a = E.a_step_closed_form(Fraction(1))
    check(a["B"] == "3/2", "B at gauge 1")
    check(a["ctilde"] == "21/10", "A ctilde")
    a2 = E.a_step_closed_form(Fraction(2))
    check(a2["B"] == "3", "B scales")
    check(a2["ctilde"] == "42/5", "A ctilde scales as A^2")
    tr = E.trunk_closed_form(Fraction(1))
    check(tr["D"] == "4/3", "D at gauge 1")
    check(tr["ctilde"] == "68/21", "trunk ctilde")
    tr2 = E.trunk_closed_form(Fraction(3))
    check(tr2["D"] == "4", "D scales")
    check(tr2["ctilde"] == "204/7", "trunk ctilde scales as C^2")


def test_mutations() -> None:
    pt = E.poly_from_roots([(Fraction(1), 2), (Fraction(1), 1)])
    w = E.poly_from_roots([(Fraction(1), 1), (Fraction(1), 1)])
    check(E.ode_holds(pt, w, 7, Fraction(21, 15)) is None, "A coincident roots")
    pt = E.poly_from_roots([(Fraction(1), 2), (Fraction(2), 1)])
    w = E.poly_from_roots([(Fraction(1), 1), (Fraction(2), 1)])
    check(E.ode_holds(pt, w, 7, Fraction(21, 15)) is None, "A B=2 rejected")
    pt = E.poly_from_roots([(Fraction(1), 3), (Fraction(1), 2)])
    w = E.poly_from_roots([(Fraction(1), 1), (Fraction(1), 1)])
    check(E.ode_holds(pt, w, 17, Fraction(85, 35)) is None, "trunk coincident")
    pt = E.poly_from_roots([(Fraction(1), 3), (Fraction(2), 2)])
    w = E.poly_from_roots([(Fraction(1), 1), (Fraction(2), 1)])
    check(E.ode_holds(pt, w, 17, Fraction(85, 35)) is None, "trunk D=2 rejected")
    wrong_rho = E.ode_holds(
        E.poly_from_roots([(Fraction(1), 2), (Fraction(3, 2), 1)]),
        E.poly_from_roots([(Fraction(1), 1), (Fraction(3, 2), 1)]),
        7,
        Fraction(2, 3),
    )
    check(wrong_rho is None, "frame rho 2/3 is not the A-step ODE ratio")


def test_i_chain() -> None:
    for t in (0, 1, 2, 3, 10, 15, 100, 1000):
        d = E.i_chain(t)
        check(d["i_A"] == 2, "i_A")
        check(d["i_G"] == 14, "i_G")
        check(d["i_F"] == 28 * (4 + 3 * t), "i_F")
        check(d["D_over_im_A"] == 7, "A D/im")
        check(d["D_over_im_trunk"] == "17/2", "trunk D/im t-free")
        check(d["n_arr"] == 37 + 28 * t, "n_arr")
        check(d["n_trunk"] == 22 + 17 * t, "n_trunk")
        check(d["nu_G"] == 4 + 3 * t, "nu_G")
    try:
        E.i_chain(-1)
        check(False, "negative t must fail")
    except ValueError:
        check(True, "negative t rejected")


def test_mp1() -> None:
    d = E.mp1_two_extras_independent()
    check(d["sum_r_minus_1"] == 1, "one merge")
    check(d["shared_first_separation_forbidden_by_MP1"] is True, "no shared cv")
    check(d["A_extra_ratio"] != d["merge_orbit_ratio"], "extra is not merge arrival")


def test_uniqueness() -> None:
    nA = E.uniqueness_scan_A(bound=8)
    nT = E.uniqueness_scan_trunk(bound=8)
    check(nA > 0, "A hits")
    check(nT > 0, "trunk hits")


def test_certificate_firewall() -> None:
    cert = E.certificate()
    check(cert["verdict"] == "PARTIAL", "verdict")
    check(cert["exact_lambda_two_proved"] is False, "not exact")
    check(cert["route_killed_by_strict_lambda"] is False, "not killed")
    check(cert["configuration_realizable"] is False, "not realizable")
    check(cert["source_landing"] is False, "no landing")
    check(cert["jc2"] is False, "no jc2")
    copy = dict(cert)
    digest = copy.pop("certificate_sha256")
    blob = json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()
    check(hashlib.sha256(blob).hexdigest() == digest, "certificate hash")


def test_stdout_identity() -> None:
    here = pathlib.Path(__file__).resolve().parent
    ordinary = subprocess.check_output(
        [sys.executable, str(here / "exact_lambda_td8.py")],
        cwd=str(here),
    )
    optimized = subprocess.check_output(
        [sys.executable, "-O", str(here / "exact_lambda_td8.py")],
        cwd=str(here),
    )
    check(ordinary == optimized, "stdout identity")
    text = ordinary.decode()
    check("PARTIAL" in text, "stdout verdict")
    check("certificate_sha256" in text, "stdout hash line")


def main() -> None:
    test_floors()
    test_closed_forms()
    test_mutations()
    test_i_chain()
    test_mp1()
    test_uniqueness()
    test_certificate_firewall()
    test_stdout_identity()
    print(f"TD8_EXACT_LAMBDA_GROK46_TEST_PASS checks={CHECKS}")


if __name__ == "__main__":
    main()
