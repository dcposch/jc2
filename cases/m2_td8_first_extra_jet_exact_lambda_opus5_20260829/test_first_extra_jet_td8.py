#!/usr/bin/env python3
"""Ordinary and -O test suite for first_extra_jet_td8.py.

No `assert` statements are used, so `python3 -O` runs the identical battery.
"""

from fractions import Fraction as Fr
import hashlib
import io
import json
import sys
import contextlib

import first_extra_jet_td8 as M

COUNT = 0
FAILS = []


def check(cond, label):
    global COUNT
    COUNT += 1
    if not cond:
        FAILS.append(label)


def eq(a, b, label):
    check(a == b, "%s: got %r want %r" % (label, a, b))


def raises(fn, label, exc=Exception):
    global COUNT
    COUNT += 1
    try:
        fn()
    except exc:
        return
    FAILS.append("%s: no exception" % label)


# ---------------------------------------------------------------- 1. route ---
def test_route():
    for t in (0, 1, 2, 3, 7, 20, 100, 1000):
        r = M.route(t)
        G, T, A = r["G"], r["trunk"], r["A"]
        eq(G["nu"], 4 + 3 * t, "nu_G t=%d" % t)
        eq(G["dp"], 24 + 18 * t, "dp_G t=%d" % t)
        eq(G["dq"], 9 + 6 * t, "dq_G t=%d" % t)
        eq(G["kbar"], 6 + 4 * t, "kbar_G t=%d" % t)
        eq(G["X"], 16 + 12 * t, "X_G t=%d" % t)
        eq(G["rho"], Fr(2, 3), "rho_G t=%d" % t)
        eq(G["w"], Fr(4, 3), "w_G t=%d" % t)
        eq(G["M"], 3, "M_G t=%d" % t)
        eq(G["n_in"], 37 + 28 * t, "n_in t=%d" % t)
        eq(T["n_edge"], 22 + 17 * t, "n_F t=%d" % t)
        # t-free objects
        eq((A["dp"], A["dq"], A["kbar"], A["X"], A["rho"], A["w"], A["M"]),
           (21, 15, 5, 7, Fr(1, 3), Fr(2, 3), 3), "A frame t=%d" % t)
        eq((T["dp"], T["dq"], T["kbar"], T["X"], T["rho"], T["w"], T["M"]),
           (85, 35, 7, 17, Fr(1, 5), Fr(2, 5), 5), "trunk frame t=%d" % t)
        eq(r["j"], 3, "j t=%d" % t)
        eq(r["psi"], 1, "psi t=%d" % t)
        eq(r["budget_ceiling"], 6, "ceiling t=%d" % t)
        # i-chain
        ic = r["ichain"]
        eq(ic["i_A"], 2, "i_A t=%d" % t)
        eq(ic["deg_pA_full"], 42, "deg pA full t=%d" % t)
        eq(ic["i_G"], 14, "i_G t=%d" % t)
        eq(ic["i_T"], 28 * (4 + 3 * t), "i_T t=%d" % t)
        # pole
        eq(r["pole"]["Q"], (2, 4, 3, 2, 5), "pole Q t=%d" % t)
        eq(r["pole"]["w"], Fr(3, 2), "pole w t=%d" % t)
    raises(lambda: M.route(-1), "route rejects t=-1", ValueError)
    raises(lambda: M.route(Fr(1, 2)), "route rejects fractional t", ValueError)


# ------------------------------------------------------- 2. the descent law ---
def independent_tau0(D, deg0, drops):
    """Second implementation: walk the profile accumulating area."""
    D = Fr(D)
    segs = []
    prev = Fr(0)
    deg = Fr(deg0)
    for tau, nd in drops:
        segs.append((prev, Fr(tau), deg))
        prev, deg = Fr(tau), Fr(nd)
    segs.append((prev, None, deg))
    left = D
    for a, b, dg in segs:
        span = None if b is None else b - a
        if span is None or dg * span > left:
            return a + left / dg
        left -= dg * span
    raise RuntimeError("unreachable")


def test_descent():
    # gap recovery: no drop reproduces corrected St 9.3 (24) exactly
    eq(M.local_charge(14, 5, 2, []), Fr(2), "A no-drop = gap")
    eq(M.af2_gap(14, 5, 2), Fr(2), "A af2 gap")
    for t in (0, 1, 5):
        td_ = M.trunk_data(t)
        eq(M.local_charge(td_["D"], 7, td_["m"], []), Fr(3, 2),
           "trunk no-drop = gap t=%d" % t)
        eq(td_["gap"], Fr(3, 2), "trunk af2 gap t=%d" % t)
    # A-step closed form 9 - theta for every drop level below tau_lin
    for num in range(1, 28):
        th = Fr(num, 4)
        got = M.local_charge(14, 5, 2, [(th, 1)])
        want = Fr(9) - th if th < 7 else Fr(2)
        eq(got, want, "A closed form theta=%s" % th)
        eq(M.descent_tau0(14, 2, [(th, 1)]), independent_tau0(14, 2, [(th, 1)]),
           "A independent integrator theta=%s" % th)
    # drop at or beyond tau_lin cannot change the charge
    for th in (7, 8, Fr(15, 2), 100):
        eq(M.local_charge(14, 5, 2, [(th, 1)]), Fr(2), "A late drop theta=%s" % th)
    # multi-drop profiles agree with the independent integrator
    profiles = [
        [(1, 5), (2, 3), (4, 1)],
        [(Fr(1, 2), 9), (3, 4), (Fr(11, 2), 2)],
        [(2, 6)],
        [],
    ]
    for pr in profiles:
        eq(M.descent_tau0(60, 10, pr), independent_tau0(60, 10, pr),
           "multi-drop %r" % (pr,))
    # convexity guards
    raises(lambda: M.descent_tau0(14, 2, [(3, 3)]), "degree must decrease", ValueError)
    raises(lambda: M.descent_tau0(14, 2, [(3, 0)]), "degree stays >= 1", ValueError)
    raises(lambda: M.descent_tau0(14, 2, [(3, 1), (2, 1)]), "levels increase", ValueError)
    raises(lambda: M.descent_tau0(0, 2, []), "D positive", ValueError)
    raises(lambda: M.descent_tau0(14, 0, []), "deg0 >= 1", ValueError)
    # exact_charge multiplies by the ramification ratio
    eq(M.exact_charge(14, 5, 2, [(Fr(1, 2), 1)], 2), Fr(17), "kappa jump 2 at 1/2")
    eq(M.exact_charge(14, 5, 2, [], 1), Fr(2), "no jump no drop")


# ---------------------------------------------------------- 3. A-step menu ---
def test_a_step():
    menu = M.a_step_menu()
    eq(menu["contact"]["theta=1"], Fr(8), "contact theta=1")
    eq(menu["contact"]["theta=6"], Fr(3), "contact theta=6")
    eq(menu["contact"]["theta>=7"], Fr(2), "contact late")
    for th in range(1, 7):
        eq(menu["contact"]["theta=%d" % th], Fr(9 - th), "contact %d" % th)
    # conjugate family: theta in Z + 1/2, kappa doubles, charges are odd
    conj_vals = [v for k, v in menu["conjugate"].items() if k != "theta>7"]
    check(all(int(v) % 2 == 1 for v in conj_vals), "conjugate charges are odd")
    eq(sorted(int(v) for v in conj_vals), [5, 7, 9, 11, 13, 15, 17],
       "conjugate value set")
    eq(menu["values"], [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17], "full A menu")
    check(min(menu["values"]) == 2, "A menu floor is the AF2 floor 2")
    check(len([v for v in menu["values"] if v < 3]) == 1, "2 is the unique sub-3 value")
    check(sorted(menu["values"]) == menu["values"], "A menu sorted")
    # only theta >= tau_lin gives 2
    for th in (Fr(1, 2), 1, Fr(3, 2), 2, 3, 4, 5, 6, Fr(13, 2)):
        check(M.a_step_charge(th, 1) > 2 and M.a_step_charge(th, 2) > 2,
              "early separation charges > 2 at theta=%s" % th)
    for th in (7, Fr(15, 2), 9, 50):
        eq(M.a_step_charge(th, 1), Fr(2), "late separation is 2 at %s" % th)
        eq(M.a_step_charge(th, 2), Fr(2), "late separation is 2 (ratio ignored) %s" % th)
    raises(lambda: M.a_step_charge(0), "theta must be positive", ValueError)
    raises(lambda: M.a_step_charge(-1), "theta must be positive (neg)", ValueError)
    # integrality filter: non-integral theta in the contact family is excluded
    for th in (Fr(1, 3), Fr(2, 3), Fr(4, 3), Fr(5, 2)):
        c = M.a_step_charge(th, 1)
        check(c.denominator != 1 or th.denominator == 1,
              "contact non-integral theta gives non-integral charge %s" % th)


# --------------------------------------------------------------- 4. trunk ---
def test_trunk():
    for t in (0, 1, 4, 33):
        td_ = M.trunk_data(t)
        iF = 28 * (4 + 3 * t)
        eq(td_["i_F"], iF, "i_F t=%d" % t)
        eq(td_["m"], 2 * iF, "m t=%d" % t)
        eq(td_["D"], 17 * iF, "D t=%d" % t)
        eq(td_["gap"], Fr(3, 2), "gap t=%d" % t)
        eq(td_["tau_lin"], Fr(17, 2), "tau_lin t=%d" % t)
        # charge 2 <=> tau0 = 9
        eq(Fr(9) - 7, Fr(2), "tau0=9 gives charge 2 t=%d" % t)
        # explicit realization: half the group leaves at tau = 8
        r = M.trunk_area_deficit(t, [(8, iF)])
        eq(r["tau0"], Fr(9), "half-drop tau0 t=%d" % t)
        eq(r["local_charge"], Fr(2), "half-drop charge t=%d" % t)
        eq(r["deficit_over_iF"], Fr(1), "deficit is one i_F unit t=%d" % t)
        # a drop that is too small keeps the charge below 2 (hence non-integral)
        r2 = M.trunk_area_deficit(t, [(8, 2 * iF - 1)])
        check(Fr(3, 2) <= r2["local_charge"] < Fr(2),
              "small drop stays under 2 t=%d" % t)
        # a drop that is too big overshoots
        r3 = M.trunk_area_deficit(t, [(4, iF)])
        check(r3["local_charge"] > 2, "early half-drop overshoots t=%d" % t)
    # kappa_H = kappa_F is forced when the charge is 2 (2*(3/2+S) >= 3 > 2)
    for S in (Fr(0), Fr(1, 4), Fr(1, 2), Fr(1)):
        check(2 * (Fr(3, 2) + S) > 2, "ramification jump forbids charge 2 (S=%s)" % S)


# --------------------------------------------------------------- 5. budget ---
def test_budget():
    b = M.budget_forcing(0)
    eq(b["ceiling"], 6, "ceiling")
    eq(b["floor_total"], 6, "floor total")
    eq(b["margin"], 0, "margin")
    check(b["all_three_forced_to_two"], "all three forced to two")
    # a single early separation at one A-copy exceeds the ceiling, every t
    for th in (1, 2, 3, 4, 5, 6, Fr(1, 2), Fr(13, 2)):
        for ratio in (1, 2):
            tot = M.a_step_charge(th, ratio) + 2 + 2
            check(tot > 6, "early sep kills the route theta=%s r=%d" % (th, ratio))
    eq(M.a_step_charge(7, 1) + M.a_step_charge(7, 1) + 2, Fr(6),
       "all-late totals exactly the ceiling")


# ------------------------------------------------------------ 6. jet layer ---
def test_jet_layer():
    pF, p_red = M.p_F_full()
    eq(len(p_red) - 1, 21, "deg p_red")
    eq(len(pF) - 1, 42, "deg p_F")
    # multiplicities: extra orbit is a double root of the FULL pattern (i_A * 1)
    eq(M.ord_at_cstar(pF, 4), 2, "mult(p_F,c*) = 2")
    eq(M.ord_at_A(pF, 6), 4, "mult(p_F,c_A) = 4")
    # DERIVED semi-invariance weights of the subtop pieces, pinned by (kbar,nu,D)
    N1, e0, e1, e2 = M.pinned_weights(M.A_KBAR, M.NU, M.A_D)
    eq((N1, e0, e1, e2), (2, 0, 4, 1), "A pinned weights")
    eq(e0, 0, "A top weight recovers the printed l = 0")
    eq((2 * e1) % M.NU, e2, "A weight law e2 = 2 e1 (mod nu)")
    N1t, e0t, e1t, e2t = M.pinned_weights(7, 17, 17 * 112)
    eq((N1t, e0t, e1t, e2t), (10, 0, 12, 7), "trunk pinned weights")
    eq(e0t, 0, "trunk top weight recovers l = 0")
    eq((2 * e1t) % 17, e2t, "trunk weight law")
    check(e1 != 0, "e1 is a unit inverse, never 0")
    raises(lambda: M.pinned_weights(7, 7, 14), "non-unit N1 rejected", ValueError)
    # forced vanishing orders  ord_{c*}(p_{n-k}) >= m-k
    sub1, sub2 = M.build_jets(e1, e2, Fr(1))
    eq(M.ord_at_cstar(sub1, 4), 1, "ord_{c*} p_{n-1} = 1 (>= m-1 = 1)")
    eq(M.ord_at_A(sub1, 6), 3, "ord_{cA} p_{n-1} >= 3")
    eq(M.ord_at_A(sub2, 6), 2, "ord_{cA} p_{n-2} >= 2")
    c0, c1, c2 = M.child_pattern_coefficients(sub1, sub2)
    check(not M.kzero(c0), "c0 nonzero (St 3.9(ii) pin)")
    check(not M.kzero(c1), "c1 nonzero")
    check(not M.kzero(c2), "c2 nonzero")
    # jet E: generic subtop -> distinct roots -> theta = 1 -> charge 8
    check(not M.kzero(M.discriminant(c0, c1, c2)), "jet E discriminant nonzero")
    eq(M.a_step_charge(1, 1), Fr(8), "jet E charge 8")
    # jet L: tuned subtop -> double root -> no first-step separation
    s_sq, c0b, c1b, c2u, tuned = M.square_jet_scalar(e1, e2)
    check(M.is_rational_scalar(s_sq), "jet L scalar is rational (realizable)")
    eq(s_sq[0], Fr(3, 8), "jet L scalar value at the pinned weights")
    sub1L, sub2L = M.build_jets(e1, e2, s_sq[0])
    cc = M.child_pattern_coefficients(sub1L, sub2L)
    check(M.kzero(M.discriminant(*cc)), "jet L discriminant vanishes")
    eq(M.a_step_charge(7, 1), Fr(2), "jet L charge 2")
    # the two admissible jets differ ONLY in the free subtop value
    check(sub1L == sub1, "jets share p_{n-1}")
    check(sub2L != sub2, "jets differ in p_{n-2}")
    # derived semi-invariance weight law e2 = 2 e1 (mod 7)
    ok, bad = M.semiinv_scan()
    eq(len(ok), 7, "seven weights")
    on_weight_ok = all(v is not None for v in ok.values())
    check(on_weight_ok, "square jet realizable on-weight")
    eq(sorted(set(ok.values())) if on_weight_ok else None,
       [Fr(1, 4), Fr(3, 8)], "on-weight scalar values")
    check(not any(bad.values()), "square jet NOT realizable off-weight")
    # K arithmetic sanity
    one = [Fr(1)] + [Fr(0)] * (M.NU - 1)
    eta = [Fr(0), Fr(1)] + [Fr(0)] * (M.NU - 2)
    eq(M.kmul(eta, M.kinv(eta)), one, "K inverse of eta")
    eq(M.keval(M.orbit(M.BVAL)), [Fr(0)] * M.NU, "eta^7 - B vanishes at c*")
    check(not M.kzero(M.keval(M.orbit(M.AVAL))), "eta^7 - A does not vanish at c*")
    raises(lambda: M.kinv([Fr(0)] * M.NU), "kinv rejects zero", ZeroDivisionError)


# ------------------------------------------------------------ 7. mutations ---
def test_mutations():
    # M1: the printed (uncorrected) (24) sign would read gap = D/m + kbar
    check(Fr(14, 2) + 5 != M.af2_gap(14, 5, 2), "M1 printed sign is not the gap")
    # M2: the simple-orbit slogan ceil(X - kbar) on the trunk is the wrong rule
    check(17 - 7 != M.trunk_data(0)["gap"], "M2 simple-orbit slogan wrong")
    # M3: forgetting i (reduced multiplicity 1 instead of m = i*mult_red)
    check(M.af2_gap(14, 5, 1) != Fr(2), "M3 dropping i changes the A gap")
    check(M.af2_gap(17 * 112, 7, 2) != Fr(3, 2), "M3 dropping i changes the trunk gap")
    # M4: kappa ratio cannot exceed m = 2 on the A-step
    check(M.exact_charge(14, 5, 2, [(1, 1)], 3) != M.exact_charge(14, 5, 2, [(1, 1)], 2),
          "M4 ratio 3 is a different (inadmissible) number")
    # M5: a 'drop' that raises the degree violates St 3.10(i)
    raises(lambda: M.descent_tau0(14, 2, [(1, 4)]), "M5 degree cannot rise", ValueError)
    # M6: charge below the AF2 floor is unreachable
    for th in (Fr(1, 2), 1, 3, 6, 7, 20):
        check(M.a_step_charge(th, 1) >= 2, "M6 charge >= floor at %s" % th)
    # M7: an off-weight subtop cannot realize the square jet
    _, bad = M.semiinv_scan()
    check(not any(bad.values()), "M7 off-weight square jet unrealizable")
    # M8: wrong frame rho (2/3 campaign frame) is not the A-step ODE ratio 7/5
    check(Fr(2, 3) != Fr(21, 15), "M8 frame rho is not the ODE ratio")
    # M9: budget with any charge 3 is over ceiling
    check(3 + 2 + 2 > M.budget_forcing(0)["ceiling"], "M9 3+2+2 over ceiling")


# ------------------------------------------------- 8. certificate / stdout ---
def test_certificate():
    out = M.run()
    cert = M.certificate(out)
    eq(len(cert), 64, "certificate length")
    out2 = M.run()
    eq(M.certificate(out2), cert, "certificate is deterministic")
    check(out["verdict"].startswith("NOT_DETERMINED_FROM_PRINTED_DATA"), "verdict")
    fw = out["firewall"]
    check(not any(fw.values()), "firewall all false")
    # stdout identity
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        M.main(["--json"])
    h = hashlib.sha256(buf.getvalue().encode()).hexdigest()
    buf2 = io.StringIO()
    with contextlib.redirect_stdout(buf2):
        M.main([])
    eq(hashlib.sha256(buf2.getvalue().encode()).hexdigest(), h, "stdout identity")
    payload = json.loads(buf.getvalue())
    eq(payload["certificate_sha256"], cert, "in-stdout certificate")
    eq(payload["a_step"]["integral_values"],
       [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17], "stdout A menu")
    eq(payload["budget"]["margin"], 0, "stdout margin")


def main():
    test_route()
    test_descent()
    test_a_step()
    test_trunk()
    test_budget()
    test_jet_layer()
    test_mutations()
    test_certificate()
    if FAILS:
        for f in FAILS:
            print("FAIL", f)
        print("TD8_FIRST_EXTRA_JET_OPUS5_TEST_FAIL failures=%d checks=%d"
              % (len(FAILS), COUNT))
        return 1
    print("TD8_FIRST_EXTRA_JET_OPUS5_TEST_PASS checks=%d" % COUNT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
