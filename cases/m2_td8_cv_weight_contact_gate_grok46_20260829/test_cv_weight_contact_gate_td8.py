#!/usr/bin/env python3
"""Tests for the td=8 cv-weight / contact-gate packet.

Raises ValueError / AssertionError (the latter is not stripped by -O when
raised via check(), only bare `assert` statements are). No `assert` in this
file or in the producer.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
import sys
from fractions import Fraction as Fr

import cv_weight_contact_gate_td8 as C


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def test_route_and_i_chain() -> None:
    for t in (0, 1, 2, 3, 7, 20, 100, 1000):
        r = C.route(t)
        ic = C.i_chain(t)
        check(r["pole"]["Lambda"] == 4, "pole Lambda")
        check(r["A"]["dp"] == 21, "A dp")
        check(r["A"]["dq"] == 15, "A dq")
        check(r["A"]["kbar"] == 5, "A kbar")
        check(r["A"]["nu"] == 7, "A nu")
        check(r["A"]["M"] == 3, "A M")
        check(ic["i_A"] == 2, "i_A")
        check(ic["deg_pA_full"] == 42, "full deg p_A")
        check(ic["Mstar_A"] == 21, "M*")
        check(ic["D_A"] == 14, "D_A")
        check(ic["Q_A"] == (14, 42, 7, 3, 5), "Q(A)")
        check(ic["i_G"] == 14, "i_G")
        check(ic["psi"] == 1, "psi")
        check(ic["budget_ceiling"] == 6, "ceiling")
        check(ic["n_arr"] == 37 + 28 * t, "n_arr")
        check(ic["n_trunk"] == 22 + 17 * t, "n_trunk")
        check(r["G"]["M"] == 3, "M_G")
        check(r["G"]["w"] == Fr(4, 3), "w_G")
        check(r["trunk"]["dp"] == 85, "trunk dp")
        check(r["trunk"]["dq"] == 35, "trunk dq")
        check(r["trunk"]["kbar"] == 7, "trunk kbar")
        check(r["j"] == 3, "j")
    try:
        C.route(-1)
        check(False, "negative t must fail")
    except ValueError:
        check(True, "negative t rejected")
    try:
        C.i_chain(-3)
        check(False, "negative t i_chain must fail")
    except ValueError:
        check(True, "negative t i_chain rejected")


def test_pole_census() -> None:
    p = C.pole_census()
    check(p["n_poles"] == 2, "two poles")
    check(p["Lambda_F"] == 4, "Lambda 4")
    check(p["D"] == 2 and p["Dg"] == 3, "D,Dg")
    check(p["deg_p"] == 4 and p["deg_q"] == 6, "degrees")
    check(p["nu"] == 3, "nu")
    check(p["deg_pstar"] == 1, "p*")
    check(p["deg_qstar"] == 2, "q*")
    check(p["n_pole_places"] == 4, "four places")
    check(p["td_from_poles"] == 8, "td")
    check(p["extra_pole_impossible"] is True, "no third pole")
    pl = C.pole_place_tuples()["places"]
    check(len(pl) == 4, "place tuples")
    check(sum(x["Lambda"] for x in pl) == 8, "place Lambda sum")
    check({x["Lambda"] for x in pl} == {1, 3}, "1 and 3")


def test_descent() -> None:
    g = C.a_step_no_drop_charge()
    check(g["gap"] == 2, "no-drop 2")
    check(g["tau_lin"] == 7, "tau_lin")
    d = C.delta_two_iff_no_drop()
    check(d["delta_eq_2_iff_deg_pH_eq_2"] is True, "iff")
    check(d["contact_early"] == [8, 7, 6, 5, 4, 3], "contact menu")
    check(d["conjugate_early"] == [17, 15, 13, 11, 9, 7, 5], "conjugate menu")
    check(C.a_step_drop_charge(Fr(1), 1) == 8, "theta=1")
    check(C.a_step_drop_charge(Fr(6), 1) == 3, "theta=6")
    check(C.a_step_drop_charge(Fr(1, 2), 2) == 17, "conj theta=1/2")
    check(C.a_step_drop_charge(Fr(13, 2), 2) == 5, "conj theta=13/2")
    try:
        C.a_step_drop_charge(7, 1)
        check(False, "theta=7 is not a drop")
    except ValueError:
        check(True, "theta=7 rejected")
    try:
        C.a_step_drop_charge(0, 1)
        check(False, "theta=0 rejected")
    except ValueError:
        check(True, "theta=0 rejected")


def test_budget() -> None:
    b = C.budget_four_vertex()
    check(b["psi"] == 1, "psi")
    check(b["ceiling"] == 6, "ceiling")
    check(b["floors"] == (2, 2, 0, 2), "floors")
    check(b["weights"] == (2, 2, 2, 1), "weights")
    check(b["n_cv"] == 4, "n_cv")
    check(b["printed_7_5_used"] is False, "no printed 7.5")
    check(b["delta_a_forced_zero"] is False, "delta not forced")
    check(b["x_side_exact"] == 1, "x-side")
    check(b["fifth_vertex_impossible"] is True, "no fifth")
    it = C.item4()
    check(it["four_vertex_forced"] is True, "item4 forced")
    check(it["printed_prop75_used"] is False, "item4 no 7.5")
    check(it["quadratic_on_A_forced"] is True, "quadratic forced")


def test_quadratic_kl() -> None:
    kl = C.quadratic_k_divides_two()
    check(kl["k_menu"] == (1, 2), "k menu")
    check(kl["terminal"] == (1, 0), "terminal")
    check(C.quadratic_kl_legal(1, 0) is True, "(1,0)")
    check(C.quadratic_kl_legal(1, 5) is True, "(1,5)")
    check(C.quadratic_kl_legal(2, 1) is True, "(2,1)")
    check(C.quadratic_kl_legal(2, 3) is True, "(2,3)")
    check(C.quadratic_kl_legal(2, 9) is True, "(2,9)")
    check(C.quadratic_kl_legal(2, 2) is False, "gcd")
    check(C.quadratic_kl_legal(3, 1) is False, "k=3")
    check(C.quadratic_kl_legal(4, 1) is False, "k=4")
    check(C.quadratic_kl_legal(7, 5) is False, "(7,5) 10/7")
    check(C.quadratic_kl_legal(14, 5) is False, "(14,5)")
    check(C.quadratic_kl_legal(0, 1) is False, "k=0")
    check(C.quadratic_kl_legal(2, 0) is False, "(2,0) not the unique terminal")
    # all legal pairs in a window have k | 2
    n = 0
    for k in range(1, 40):
        for l in range(0, 40):
            if C.quadratic_kl_legal(k, l):
                n += 1
                if l > 0:
                    check(k in (1, 2), f"k|2 at ({k},{l})")
    check(n > 20, "many legal pairs")
    check(kl["n_ok_in_30"] > 10, "samples")


def test_mstar_and_parent() -> None:
    m = C.mstar_forces_some_k2()
    check(m["Mstar"] == 21, "M*")
    check(m["some_k_j_eq_2"] is True, "some k=2")
    check(m["k_j_in_1_2"] is True, "k in 1,2")
    p = C.parent_is_A()
    check(p["H_circ"] == "A", "parent A")
    check(p["both_forbidden_by_Delta_2"] is True, "no intermediate")


def test_double_root_filling() -> None:
    p = C.double_root_p()
    check(C.pdeg(p) == 2, "p deg 2")
    f1 = C.filling_21_chain(1, Fr(1), Fr(1))
    check(f1["all_deg_1"] is True, "one step")
    f2 = C.filling_21_chain(2, Fr(1), Fr(1))
    check(len(f2["remainders"]) == 2, "two remainders")
    f4 = C.filling_21_chain(4, Fr(2), Fr(3))
    check(f4["n_steps"] == 4, "four steps")
    fneg = C.filling_21_chain(3, Fr(1), Fr(-2))
    check(fneg["all_deg_1"] is True, "negative b")
    # remainder of (eta+1)^2 - eta^2 is 2 eta + 1, degree 1
    r = C.monic_linear(Fr(1), Fr(1))
    nxt = C.recursion_step(r, p, 2, 1)
    check(C.pdeg(nxt) == 1, "explicit remainder deg")
    check(nxt[0] == 1, "const term")
    check(nxt[1] == 2, "linear term")
    col = C.collapse_pure_power()
    check(col["needs_subtop"] is True, "subtop")
    check(all(d == -1 for _, d in col["pure_power_collapses"]), "collapse")
    check(C.next_kl_from_generic_remainder(1) == (2, 1), "fixed point l=1")
    check(C.next_kl_from_generic_remainder(3) == (2, 5), "l=3 -> 5")
    check(C.generic_remainder_degree(1) == 1, "gen 1")
    check(C.generic_remainder_degree(5) == 9, "gen 5")
    try:
        C.filling_21_chain(1, Fr(1), Fr(0))
        check(False, "b=0 must fail")
    except ValueError:
        check(True, "b=0 rejected")
    try:
        C.filling_21_chain(1, Fr(0), Fr(1))
        check(False, "a=0 must fail")
    except ValueError:
        check(True, "a=0 rejected")


def test_nearow_control() -> None:
    n = C.nearrow_ode_kill_control()
    check(n["case_empty_under_Delta_2"] is True, "empty")
    check(len(n["prop46_collision_if_occupied"]) >= 3, "collisions")


def test_census_tuples() -> None:
    c = C.cv_census_tuples()
    check(c["n"] == 4, "four")
    check(c["weights"] == (2, 2, 2, 1), "weights")
    roles = [v["role"] for v in c["vertices"]]
    check(roles == ["A1", "A2", "trunk", "x-side"], "roles")
    check(c["vertices"][0]["deg_p"] == 2, "A1 deg")
    check(c["vertices"][1]["deg_p"] == 2, "A2 deg")
    check(c["vertices"][0]["root"] == "double", "double")
    check(c["vertices"][0]["equality_forced"] is False, "Prop 7.3 inequality")
    check(c["vertices"][2]["deg_p"] is None, "trunk not quadratic-forced")
    check(c["vertices"][3]["weight"] == 1, "x-side")


def test_mutations() -> None:
    # third pole of Lambda >= 3 would overshoot td
    check(2 * 4 + 3 > 8, "third pole overshoots")
    # early A-separation overshoots the exit ceiling
    check(C.a_step_drop_charge(1, 1) + 2 + 2 > 6, "early A kills budget")
    check(3 + 2 + 2 > 6, "any Delta_A>=3 kills")
    # all-k=1 cannot hit M*=21
    g = 42
    for t in (2, 4, 6, 8, 10):
        g = C.egcd(g, 21 * t)
    check(g != 21, "all even t")
    check(g % 2 == 0, "stays even")
    # k=7 is illegal at a quadratic cv (independent of M*)
    check(C.quadratic_kl_legal(7, 5) is False, "7 does not divide 2")
    # printed unrepaired (24) would flip the A gap sign: 14/2 + 5 = 12, not 2
    check(Fr(14, 2) + 5 == 12, "printed sign slip")
    check(Fr(14, 2) - 5 == 2, "repaired gap")


def test_certificate_firewall() -> None:
    cert = C.certificate()
    check(cert["verdict"] == "CV_CONFIGURATION_FORMALLY_SURVIVES", "verdict")
    check(cert["route_killed"] is False, "not killed")
    check(cert["source_landing"] is False, "no landing")
    check(cert["gluing"] is False, "no gluing")
    check(cert["realizability"] is False, "no realizability")
    check(cert["counterexample"] is False, "no counterexample")
    check(cert["degree_ceiling"] is False, "no ceiling")
    check(cert["jc2"] is False, "no jc2")
    check(cert["printed_7_5_used"] is False, "no 7.5")
    check(cert["delta_a_forced_zero"] is False, "no delta_a")
    check(cert["conditional_on_reviewed_td8_route"] is True, "cond route")
    check(cert["conditional_on_exact_separation_premise"] is True, "cond sep")
    check("cap" not in json.dumps(cert).lower(), "no cap token")
    copy = dict(cert)
    digest = copy.pop("certificate_sha256")
    blob = json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()
    check(hashlib.sha256(blob).hexdigest() == digest, "certificate hash")


def test_stdout_identity() -> None:
    here = pathlib.Path(__file__).resolve().parent
    ordinary = subprocess.check_output(
        [sys.executable, str(here / "cv_weight_contact_gate_td8.py")],
        cwd=str(here),
    )
    optimized = subprocess.check_output(
        [sys.executable, "-O", str(here / "cv_weight_contact_gate_td8.py")],
        cwd=str(here),
    )
    check(ordinary == optimized, "stdout identity")
    text = ordinary.decode()
    check("CV_CONFIGURATION_FORMALLY_SURVIVES" in text, "stdout verdict")
    check("certificate_sha256" in text, "stdout hash line")
    check("cap" not in text.lower(), "no cap in stdout")
    js = subprocess.check_output(
        [sys.executable, str(here / "cv_weight_contact_gate_td8.py"), "--json"],
        cwd=str(here),
    )
    js_o = subprocess.check_output(
        [sys.executable, "-O", str(here / "cv_weight_contact_gate_td8.py"), "--json"],
        cwd=str(here),
    )
    check(js == js_o, "json identity")
    cert = json.loads(js.decode())
    check(cert["verdict"] == "CV_CONFIGURATION_FORMALLY_SURVIVES", "json verdict")


def test_no_assert_tokens() -> None:
    here = pathlib.Path(__file__).resolve().parent
    for name in ("cv_weight_contact_gate_td8.py", "test_cv_weight_contact_gate_td8.py"):
        src = (here / name).read_text()
        # reject the statement `assert `; allow the word in comments/strings only
        # if it is this helper. Count real assert statements.
        n_assert = 0
        for line in src.splitlines():
            s = line.strip()
            if s.startswith("assert ") or s.startswith("assert("):
                n_assert += 1
        check(n_assert == 0, f"no assert in {name}")


def main() -> None:
    test_route_and_i_chain()
    test_pole_census()
    test_descent()
    test_budget()
    test_quadratic_kl()
    test_mstar_and_parent()
    test_double_root_filling()
    test_nearow_control()
    test_census_tuples()
    test_mutations()
    test_certificate_firewall()
    test_stdout_identity()
    test_no_assert_tokens()
    print(f"TD8_CV_WEIGHT_CONTACT_GATE_GROK46_TEST_PASS checks={CHECKS}")


if __name__ == "__main__":
    main()
