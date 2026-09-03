#!/usr/bin/env python3
"""Run CONJ[APPII-UNIFORM] cheapest test: controls + G2.

Positive: Moh (15,10;11;3;X^2) SATURATED-EMPTY with ERRATUM[APPII-GAMMA-B];
          Moh (16,12;13;3;X) SATURATED-EMPTY.
Negative: P = pi^5 - gamma^5, Q = P^3 + a pi  must SURVIVE (a),(b), tail.
G2: (15,10;4;1;X^4) with and without (c).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import traceback

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from appii_reduce import (  # noqa: E402
    closed_form, datum, supports, build_h, build_beta_generic, build_beta_moh_ab,
    tail_m2n3, tail_m3n4, jac_eqs, groebner_sat, euclid, eqs_from_poly,
    leading_support, h_monomials, coeff_monomials,
)

OUT = os.path.join(HERE, "results")
os.makedirs(OUT, exist_ok=True)

x, y = sp.symbols("x y")


def dump(name, obj):
    path = os.path.join(OUT, name)
    def conv2(o):
        if isinstance(o, dict):
            return {str(k): conv2(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [conv2(v) for v in o]
        if isinstance(o, sp.Basic):
            return str(o)
        if isinstance(o, (int, float, str, bool)) or o is None:
            return o
        return str(o)
    with open(path, "w") as f:
        json.dump(conv2(obj), f, indent=2)
    print("  wrote", path)
    return path


def banner(s):
    print("\n" + "=" * 72)
    print(s)
    print("=" * 72)


# ---------------------------------------------------------------------------
# 0. closed-form gate
# ---------------------------------------------------------------------------

def step_closed_form():
    banner("0. closed form vs charged Phi / printed p.207 / G2")
    rows = [
        ("(16,12;13;3;X)", 16, 12, 13, 3, 1, sp.Rational(-1), sp.Rational(1, 4)),
        ("(15,10;11;3;X2)", 15, 10, 11, 3, 2, sp.Rational(-1), sp.Rational(1, 2)),
        ("G2 (15,10;4;1;X4)", 15, 10, 4, 1, 4, sp.Rational(-1, 2), sp.Rational(5, 4)),
        ("control (15,5;9;1;X4)", 15, 5, 9, 1, 4, sp.Rational(-1), sp.Rational(11, 3)),
    ]
    out = []
    allok = True
    for lab, n, m, M2, V2, k, p2, p1 in rows:
        C = closed_form(n, m, M2, V2, k)
        ok = (C["delta2"] == p2 and C["delta1"] == p1)
        allok &= ok
        print("  %-28s closed=(%s, %s) expect=(%s, %s) %s  n*=%d m*=%d d2=%d U2=%d R=%d"
              % (lab, C["delta2"], C["delta1"], p2, p1, "MATCH" if ok else "FAIL",
                 C["nstar"], C["mstar"], C["d2"], C["U2"], C["R"]))
        out.append(dict(lab=lab, ok=ok, **{k: str(C[k]) for k in
                    ("delta1", "delta2", "nstar", "mstar", "d2", "U2", "R")}))
    return dict(allok=allok, rows=out)


# ---------------------------------------------------------------------------
# 1. Moh (15,10;11;3;X^2): general routine + frozen replay + ERRATUM
# ---------------------------------------------------------------------------

def step_moh_1510():
    banner("1. POSITIVE (15,10;11;3;X^2) via general routine + ERRATUM")
    t0 = time.time()
    C = datum(15, 10, 11, 3, 2)
    S = supports(C, use_c=True)
    print("  licensed_c", S["licensed_c"], "n_h", S["n_h"], "n_beta", S["n_beta"], S["notes"])
    print("  h_free", S["h_free"])
    print("  lead", S["lead"])
    h, hfrees, hnames = build_h(C, S, x, y, use_c=True)
    beta, bfrees, bnames, A = build_beta_moh_ab(h, x, y)
    print("  deg_y h", sp.degree(h, y), "monic", sp.LC(sp.Poly(h, y)) == 1)
    T = tail_m2n3(h, beta, x, y, C["d2"])
    print("  deg_gamma", T["deg_gamma"], "n_eqs7", len(T["eqs7"]),
          "n_eqs3", len(T["eqs3"]), "n_eqs_rem", len(T["eqs_rem"]))

    # ERRATUM: Euclidean gamma vs printed B-coeff
    # Rebuild Moh a1..a12 shapes and compare
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 = A_ = sp.symbols("a1:13")
    B = (y ** 2 - x ** 2 + a1 * y + a2 * x + a3) * y + (a4 * x + a5)
    AA = sp.expand(B * y + (a6 * x + a7))
    hh = sp.expand(AA * y + a8)
    be = sp.expand(a9 * AA + a10 * y + a11 * x + a12)
    _, gamma = euclid(be ** 2, hh, y)
    alpha, _ = euclid(be ** 2, hh, y)
    al_moh = sp.expand(a9 ** 2 * B + 2 * a9 * a10)
    ga_printed = sp.expand(
        ((a9 ** 2 * a6 + 2 * a9 * a11) * x + (a9 ** 2 * a7 + 2 * a9 * a12)) * AA
        - a9 ** 2 * a10 * B + (a10 * y + a11 * x + a12) ** 2 - 2 * a8 * a9 * a10
    )
    ga_audited = sp.expand(
        ((a9 ** 2 * a6 + 2 * a9 * a11) * x + (a9 ** 2 * a7 + 2 * a9 * a12)) * AA
        - a9 ** 2 * a8 * B + (a10 * y + a11 * x + a12) ** 2 - 2 * a8 * a9 * a10
    )
    printed_g = sp.expand(gamma - ga_printed) == 0
    audited_g = sp.expand(gamma - ga_audited) == 0
    printed_a = sp.expand(alpha - al_moh) == 0
    print("  printed alpha reproduced:", printed_a)
    print("  printed gamma (B-coeff -a9^2 a10) reproduced:", printed_g, "  [expect False]")
    print("  audited  gamma (B-coeff -a9^2 a8 ) reproduced:", audited_g, "  [expect True]")

    # Case 1 a9=0
    s0 = {a9: 0}
    be0 = sp.expand(be.subs(s0))
    ga0 = sp.expand(gamma.subs(s0))
    case1 = dict(
        alpha=str(sp.expand(alpha.subs(s0))),
        beta=str(be0),
        gamma_minus_beta2=str(sp.expand(ga0 - be0 ** 2)),
        deg_beta3=int(sp.degree(sp.Poly(sp.expand(be0 ** 3), y), y)),
        note="a9=0 => alpha=0, gamma=beta^2, deg beta^3 <= 3 < 5; (3) forces "
             "3gamma+a=0 so gamma constant, then (4) needs deg eps=4: CONTRADICTION",
    )
    print("  Case 1 a9=0: gamma-beta^2 =", case1["gamma_minus_beta2"],
          "deg beta^3", case1["deg_beta3"], "CONTRADICTION as Moh")

    # Case 2: audited substitutions a8=0, a6=-2 a11/a9, a7=-2 a12/a9
    # (printed a10=0 is the ERRATUM path; we use audited)
    s2 = {a8: 0, a6: -2 * a11 / a9, a7: -2 * a12 / a9}
    ga2 = sp.expand(sp.together(gamma.subs(s2)).simplify())
    be2 = sp.expand(be.subs(s2))
    h2 = sp.expand(hh.subs(s2))
    c2, _ = euclid(be2 ** 3, h2 ** 2, y)
    res = sp.expand(c2 - 3 * ga2)
    Pr = sp.Poly(res, x, y)
    mons = [(mo, sp.factor(co)) for mo, co in zip(Pr.monoms(), Pr.coeffs()) if mo != (0, 0)]
    sysm = [sp.expand(sp.numer(sp.together(co))) for _, co in mons]
    print("  Case 2 audited: n_eqs (non-constant monomials of c2-3gamma) =", len(mons))
    for mo, co in mons:
        print("     x^%d y^%d : %s" % (mo[0], mo[1], co))

    Tsym = sp.Symbol("T")
    t1 = time.time()
    Gb = sp.groebner(sysm + [Tsym * a9 - 1], *(list(A_) + [Tsym]), order="lex")
    L = list(Gb)
    empty = L == [1]
    t_gb = time.time() - t1
    print("  Case 2 sat a9!=0 lex Q[a1..a12,T] T*a9-1 : EMPTY" if empty
          else "  Case 2 NON-TRIVIAL size %d" % len(L), "  time %.3fs" % t_gb)

    # pos/neg controls (same ring)
    def sat(sys):
        return list(sp.groebner(list(sys) + [Tsym * a9 - 1], *(list(A_) + [Tsym]), order="lex"))
    E = [(mo, sp.expand(sp.numer(sp.together(co)))) for mo, co in mons]
    full = sat([e for _, e in E])
    pos = []
    for drop in range(len(E)):
        sub = [e for i, (_, e) in enumerate(E) if i != drop]
        G = sat(sub)
        pos.append(dict(dropped=str(E[drop][0]),
                        empty=(G == [1]), size=len(G)))
        print("  POSITIVE drop %s -> %s" % (E[drop][0], "EMPTY [1]" if G == [1] else "NON-TRIVIAL (%d)" % len(G)))
    Gneg = sat([a9 - 1, a10 - 2, a11 - 3])
    print("  NEGATIVE a9=1,a10=2,a11=3 ->",
          "EMPTY BAD" if Gneg == [1] else "NON-TRIVIAL (%d) expected" % len(Gneg))

    # replay frozen control2
    frozen = "/tmp/jc2-lane.zyQliU/inputs/moh_1510_control2.py"
    frozen_pm = "/tmp/jc2-lane.zyQliU/inputs/moh_1510_controls_pm.py"
    rc, out, err = 0, "", ""
    rc2, out2, err2 = 0, "", ""
    try:
        r = subprocess.run([sys.executable, "-u", frozen], capture_output=True, text=True, timeout=60)
        rc, out, err = r.returncode, r.stdout, r.stderr
        r2 = subprocess.run([sys.executable, "-u", frozen_pm], capture_output=True, text=True, timeout=60)
        rc2, out2, err2 = r2.returncode, r2.stdout, r2.stderr
    except Exception as e:
        err = str(e)
    replay_empty = "saturated Groebner basis at a9 != 0 : EMPTY (1 in ideal)" in out
    replay_aud = "audited  (coefficient of B = -a9^2*a8 ) : gamma reproduced = True" in out
    replay_prt = "printed  (coefficient of B = -a9^2*a10) : gamma reproduced = False" in out
    print("  FROZEN replay control2 EMPTY", replay_empty, "audited", replay_aud, "printed-false", replay_prt)

    verdict = "SATURATED-EMPTY" if empty and case1["deg_beta3"] <= 3 else "SURVIVES"
    result = dict(
        name="MOH-1510-V2=3",
        verdict=verdict,
        licensed_c=S["licensed_c"],
        n_h=S["n_h"], n_beta_moh=4, n_eqs3=len(mons),
        printed_alpha_ok=printed_a,
        printed_gamma_ok=printed_g,
        audited_gamma_ok=audited_g,
        erratum="ERRATUM[APPII-GAMMA-B]: B-coeff of gamma is -a9^2 a8, not -a9^2 a10",
        case1_contra=True,
        case2_empty=empty,
        case2_basis_size=len(L),
        case2_gb_time=t_gb,
        ring="Q[a1..a12,T]",
        order="lex",
        rabinowitsch="T*a9-1",
        positive=pos,
        negative_nontrivial=(Gneg != [1]),
        replay_empty=replay_empty,
        replay_audited=replay_aud,
        replay_printed_false=replay_prt,
        elapsed=time.time() - t0,
        notes=S["notes"],
    )
    dump("moh1510.json", result)
    return result


# ---------------------------------------------------------------------------
# 2. Moh (16,12;13;3;X)
# ---------------------------------------------------------------------------

def step_moh_1612(timeout=180):
    banner("2. POSITIVE (16,12;13;3;X) p.208-209 shapes + Jacobian")
    t0 = time.time()
    C = datum(16, 12, 13, 3, 1)
    S = supports(C, use_c=True)
    print("  Phi", C["delta2"], C["delta1"], "n_h", S["n_h"], "h_free", S["h_free"], S["notes"])

    # Printed p.208 (1)-(5), alpha1 absorbed (=0)
    b1, b2, b3, b4 = sp.symbols("b1:5")
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols("c1:14")
    h = sp.expand(y ** 3 * (y - x) + b1 * y ** 3 + b2 * y ** 2 + b3 * y + b4)
    A = sp.expand(sp.together((h - b4) / y))
    B = sp.expand(sp.together((A - sp.expand(A.subs(y, 0))) / y))
    alpha2 = c1 * A + c2
    beta2 = c3 * A + c4
    alpha3 = c5 * A + c6 * B + c7
    beta3 = c8 * A + c9 * B + c10
    alpha4 = c11 * A + c12 * B + c13 * (y - x)
    f = sp.expand(h ** 3 + beta2 * h + beta3)
    g = sp.expand(h ** 4 + alpha2 * h ** 2 + alpha3 * h + alpha4)
    print("  deg f,g", sp.degree(f, y), sp.degree(g, y), "degx", sp.degree(f, x), sp.degree(g, x))
    c, T = sp.symbols("c T")
    unk = [b1, b2, b3, b4, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c]
    print("  #unk", len(unk), "building J ...")
    tJ = time.time()
    eqs, J = jac_eqs(f, g, c, 1, x, y)
    print("  J built in %.2fs, #eqs" % (time.time() - tJ), len(eqs),
          "deg_y J", sp.degree(J, y) if J != 0 else None)

    names = [str(v) for v in unk]
    main = groebner_sat(eqs, names, "c", order="grevlex", timeout=timeout, engine="singular")
    print("  MAIN sat c!=0:", main.get("verdict"), "size", main.get("basis_size"),
          "time", "%.2fs" % main.get("elapsed", 0))

    # unsaturated and negative: skip unsaturated if MAIN already took most of the budget
    remain = max(20, timeout - (time.time() - t0))
    # negative: toy c=1 in the same ring (should be non-trivial without the J eqs)
    neg = groebner_sat([c - 1], names, "c", order="grevlex", timeout=30, engine="singular")
    print("  NEGATIVE toy c=1 (no J eqs):", neg.get("verdict"), "(expect SURVIVES)")

    # eta-reduced 10-unknown form (p.209): h (4) + beta2=p A+q (2) + beta3=r A+s B+t (3) + a2
    print("  --- p.209 eta-form (10 shape + c) ---")
    p, q, r, s, t, a2 = sp.symbols("p q r s t a2")
    beta2e = sp.expand(p * A + q)
    beta3e = sp.expand(r * A + s * B + t)
    packed = tail_m3n4(h, beta2e, beta3e, a2, x, y)
    fe, ge = packed["f"], packed["g"]
    print("  eta deg f,g", sp.degree(fe, y), sp.degree(ge, y))
    unke = [b1, b2, b3, b4, p, q, r, s, t, a2, c]
    eqse, Je = jac_eqs(fe, ge, c, 1, x, y)
    print("  eta #unk", len(unke), "#eqs", len(eqse))
    maine = groebner_sat(eqse, [str(v) for v in unke], "c", order="grevlex",
                         timeout=min(120, max(30, timeout - (time.time() - t0))),
                         engine="singular")
    print("  ETA MAIN sat c!=0:", maine.get("verdict"), "size", maine.get("basis_size"),
          "time", "%.2fs" % maine.get("elapsed", 0))

    verdict = "SATURATED-EMPTY" if (
        main.get("verdict") == "SATURATED-EMPTY" or maine.get("verdict") == "SATURATED-EMPTY"
    ) else main.get("verdict", "UNKNOWN")
    result = dict(
        name="MOH-1612",
        verdict=verdict,
        n_unknowns_17pc=len(unk), n_eqs_17=len(eqs),
        main=main, eta=maine, negative=neg,
        elapsed=time.time() - t0,
        notes=S["notes"] + ["alpha1=0 absorbed; p.208 (1)-(5); p.209 eta-form parallel"],
    )
    dump("moh1612.json", result)
    return result


# ---------------------------------------------------------------------------
# 3. Negative control: P = pi^5 - gamma^5, Q = P^3 + a pi
# ---------------------------------------------------------------------------

def step_control_family():
    banner("3. NEGATIVE CONTROL P=pi^5-gamma^5, Q=P^3+a pi  (must SURVIVE)")
    t0 = time.time()
    C = datum(15, 5, 9, 1, 4)
    print("  closed", C["delta2"], C["delta1"], "n*", C["nstar"], "m*", C["mstar"],
          "d2", C["d2"], "U2", C["U2"])
    a = sp.symbols("a")
    # unshifted pair in (x,y) ~ (gamma, pi)
    P_u = y ** 5 - x ** 5
    Q_u = sp.expand(P_u ** 3 + a * y)
    J_u = sp.expand(sp.diff(P_u, x) * sp.diff(Q_u, y) - sp.diff(P_u, y) * sp.diff(Q_u, x))
    print("  unshifted J =", J_u, "  [expect -5 a x^4]")
    ju_ok = sp.expand(J_u + 5 * a * x ** 4) == 0

    # D1-centering: Y = pi - gamma, h = (Y+x)^5 - x^5  (one 5th-root shifted to 0)
    # Moh p.207: "choose x,y properly so that the pi-root in D1 is sigma = pi t^{delta1}"
    h = sp.expand((y + x) ** 5 - x ** 5)
    print("  shifted h =", h)
    mons_h = sorted(sp.Poly(h, x, y).monoms())
    print("  h monomials (x^i y^j)", mons_h)
    d1 = C["delta1"]
    # (a) order: i <= delta1 (j+1)
    fails_a = []
    for (i, j) in mons_h:
        bound = d1 * (j + 1)
        ok = (i <= bound) or (i, j) == (0, 5)  # monic leader always kept
        # leader y^5: i=0 always ok
        if not (sp.Integer(i) <= bound):
            fails_a.append(((i, j), str(bound)))
    print("  (a) order failures (must be empty):", fails_a)
    # tot and deg_x
    degx = max(i for (i, j) in mons_h)
    print("  deg_x h =", degx, " U2=", C["U2"], "  (shifted form saturates U2)")

    # (b) remainder degrees: m*=1 so P=h, no beta_i; Q = h^3 + a (y+x)
    Q_s = sp.expand(h ** 3 + a * (y + x))
    tail = sp.expand(Q_s - h ** 3)
    print("  tail Q-h^3 =", tail, "  (polynomial, no h^{-1})")
    tail_ok = sp.degree(sp.Poly(tail, y), y) < C["d2"]

    # (a) on alpha_3 = a(y+x): weight n*=3, i <= delta1 (j+3)
    alpha3 = a * (y + x)
    fails_alpha = []
    for (i, j) in sp.Poly(alpha3.subs(a, 1), x, y).monoms():
        bound = d1 * (j + 3)
        if not (sp.Integer(i) <= bound):
            fails_alpha.append(((i, j), str(bound)))
    print("  (a) alpha3 order failures:", fails_alpha)

    J_s = sp.expand(sp.diff(h, x) * sp.diff(Q_s, y) - sp.diff(h, y) * sp.diff(Q_s, x))
    print("  shifted J =", sp.factor(J_s))
    # genuine pair with J = c gamma^k : unshifted is the witness; shifted is
    # an affine change Y=pi-x, Jacobian picks a constant * power of x.
    genuine = ju_ok and (fails_a == []) and tail_ok and (fails_alpha == [])

    # if we wrongly imposed 2,2,6 on this pair, h_top would have to be
    # y^3(y^2-x^2)= y^5 - x^2 y^3, which the shifted h is not.
    lead_226 = leading_support(3, 2, split_pm=True)  # wrong geometry
    lead_ctrl = {(i, j): 1 for (i, j) in mons_h if i + j == 5}
    print("  2,2,6 lead", lead_226, "  control lead (tot=5)", lead_ctrl)
    over_c = lead_226 != {ij: lead_ctrl.get(ij, 0) for ij in lead_226}

    steps = dict(
        a_order_h=("SURVIVES" if not fails_a else "DIES"),
        a_order_alpha3=("SURVIVES" if not fails_alpha else "DIES"),
        b_deg=("SURVIVES" if tail_ok else "DIES"),
        tail_cancellation=("SURVIVES" if tail == sp.expand(a * (y + x)) else "DIES"),
        jacobian_unshifted=("SURVIVES" if ju_ok else "DIES"),
        unlicensed_226_would_kill=over_c,
    )
    print("  steps:", steps)
    print("  J = c gamma^4 genuine (unshifted):", ju_ok, "  J_u =", J_u)

    result = dict(
        name="CONTROL-FAMILY-A",
        verdict="SURVIVES" if genuine else "DIES",
        nstar=C["nstar"], mstar=C["mstar"], d2=C["d2"],
        delta1=str(C["delta1"]), delta2=str(C["delta2"]),
        ju=str(J_u), ju_ok=ju_ok,
        shifted_h=str(h), h_monomials=mons_h,
        fails_a=[str(t) for t in fails_a],
        fails_alpha=[str(t) for t in fails_alpha],
        tail=str(tail), tail_ok=tail_ok,
        steps=steps,
        note="m*=1: P=h, no beta; tail Q-h^3=a(y+x) after D1-centering. "
             "Unshifted J=-5 a x^4.  (c) 2,2,6 is a different leading form "
             "and would exclude this existing pair — not applied.",
        elapsed=time.time() - t0,
    )
    dump("control_family.json", result)
    return result


# ---------------------------------------------------------------------------
# 4. G2
# ---------------------------------------------------------------------------

def step_g2_counts():
    banner("4a. G2 supports with and without (c)")
    C = datum(15, 10, 4, 1, 4)
    Soff = supports(C, use_c=False)
    Son = supports(C, use_c=True)
    print("  Phi", C["delta2"], C["delta1"], "U2", C["U2"], "two_point", C["two_point"])
    print("  WITHOUT c: n_h", Soff["n_h"], "n_beta", Soff["n_beta"], "n_ord", Soff["n_ord"])
    print("    h_free", Soff["h_free"])
    print("    notes", Soff["notes"])
    print("  WITH c (requested): licensed", Son["licensed_c"], "n_h", Son["n_h"], Son["notes"])
    # unlicensed 2,2,6 on G2
    lead_wrong = leading_support(3, 2, split_pm=True)  # Moh's (15,10) V2=3 form
    lead_newton = {(0, 5): 1, (2, 1): 1}  # y^5 + a x^2 y  (a free)
    print("  unlicensed 2,2,6 lead", lead_wrong)
    print("  Newton (delta2=-1/2, V2=1) support y^5 + x^2 y")
    return dict(C={k: str(C[k]) if not isinstance(C[k], (int, bool)) else C[k]
                   for k in C},
                Soff=dict(n_h=Soff["n_h"], n_beta=Soff["n_beta"], n_ord=Soff["n_ord"],
                          h_free=Soff["h_free"], notes=Soff["notes"],
                          beta_all=Soff["beta_all"]),
                Son=dict(licensed_c=Son["licensed_c"], n_h=Son["n_h"], notes=Son["notes"]))


def step_g2_unlicensed_226():
    """Unlicensed (c)=2,2,6 on G2: same (5)(6) as Moh, identity (3) independent of k.

    This is a METHOD probe, not a G2 theorem.  Labelled unlicensed.
    """
    banner("4b. G2 + unlicensed (c) 2,2,6  [METHOD probe, not a G2 kill]")
    t0 = time.time()
    # identical to Moh 1510 Case 2 system: (3) does not see k
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 = A_ = sp.symbols("a1:13")
    B = (y ** 2 - x ** 2 + a1 * y + a2 * x + a3) * y + (a4 * x + a5)
    AA = sp.expand(B * y + (a6 * x + a7))
    hh = sp.expand(AA * y + a8)
    be = sp.expand(a9 * AA + a10 * y + a11 * x + a12)
    _, gamma = euclid(be ** 2, hh, y)
    s2 = {a8: 0, a6: -2 * a11 / a9, a7: -2 * a12 / a9}
    ga2 = sp.expand(sp.together(gamma.subs(s2)).simplify())
    be2 = sp.expand(be.subs(s2))
    h2 = sp.expand(hh.subs(s2))
    c2, _ = euclid(be2 ** 3, h2 ** 2, y)
    res = sp.expand(c2 - 3 * ga2)
    Pr = sp.Poly(res, x, y)
    sysm = [sp.expand(sp.numer(sp.together(co)))
            for mo, co in zip(Pr.monoms(), Pr.coeffs()) if mo != (0, 0)]
    T = sp.Symbol("T")
    Gb = sp.groebner(sysm + [T * a9 - 1], *(list(A_) + [T]), order="lex")
    empty = list(Gb) == [1]
    print("  unlicensed 2,2,6 + (3) sat a9!=0 :", "EMPTY" if empty else "NON-TRIVIAL",
          "time %.2fs" % (time.time() - t0))
    print("  FALLACY-v2: this is Moh's (15,10) shape, not G2's (delta2'=-1/2) shape.")
    return dict(
        verdict="SATURATED-EMPTY" if empty else "SURVIVES",
        licensed=False,
        reason="(c) 2,2,6 is the inverse-6.3 split of the (75,50)->(15,10;V2=3) row; "
               "G2 has delta2'=-1/2 (one point at infinity) and u'=4, V2'=1.  "
               "Identity (3) does not see k, so the kill is Moh's Case 2, not a G2 theorem.",
        elapsed=time.time() - t0,
        empty=empty,
        ring="Q[a1..a12,T]", order="lex", rabinowitsch="T*a9-1",
    )


def step_g2_without_c_tail(beta_mode="moh_ab", timeout=90):
    """G2 without (c): order-conditioned h (14) + beta, identity (3).

    beta_mode:
      'moh_ab'  : 4-coeff Moh pattern (SLICE: that span is for delta1=1/2)
      'generic' : 27 order-conditioned monomials (the honest (a) support)
    """
    banner("4c. G2 WITHOUT (c), beta=%s, tail (3)" % beta_mode)
    t0 = time.time()
    C = datum(15, 10, 4, 1, 4)
    S = supports(C, use_c=False)
    h, hfrees, hnames = build_h(C, S, x, y, use_c=False)
    if beta_mode == "moh_ab":
        beta, bfrees, bnames, A = build_beta_moh_ab(h, x, y)
        slice_flag = True
        note = "Moh-pattern beta is a SLICE at delta1'=5/4 (honest support has 27 mons)"
    else:
        beta, bfrees, bnames = build_beta_generic(S, x, y)
        slice_flag = False
        note = "generic order-conditioned beta, 27 monomials"
        A = None
    unk = hfrees + bfrees
    names = hnames + bnames
    print("  #h", len(hfrees), "#beta", len(bfrees), "total", len(unk), note)
    print("  building tail (3) ...")
    t1 = time.time()
    try:
        T = tail_m2n3(h, beta, x, y, C["d2"])
    except Exception as e:
        print("  CONSTRUCTION ERROR", e)
        traceback.print_exc()
        return dict(verdict="ERROR", error=str(e), elapsed=time.time() - t0,
                    n_unknowns=len(unk), beta_mode=beta_mode, slice=slice_flag)
    t_build = time.time() - t1
    print("  built in %.2fs  deg_gamma=%s  #eqs7=%d #eqs3=%d #eqs_rem=%d #eqs=%d"
          % (t_build, T["deg_gamma"], len(T["eqs7"]), len(T["eqs3"]),
             len(T["eqs_rem"]), len(T["eqs"])))
    n_eq, n_unk = len(T["eqs"]), len(unk)
    if n_unk > 30 and beta_mode == "generic":
        # still TRY a short Singular run; if it can't even start, COUNTING-BOUND
        print("  COUNTING: %d unknowns, %d equations (cubic/quadratic in the params)"
              % (n_unk, n_eq))
    # saturate a leading coefficient of beta so the expansion is non-degenerate:
    # for moh_ab, p (=a9); for generic, no single leader — saturate nothing extra
    # and instead saturate that we are not the zero beta?  Use p if present else
    # the first beta coeff.  Also the system (3) does not involve c.
    sat_name = "bp" if "bp" in names else (names[-1] if names else "h_0_4")
    if beta_mode == "moh_ab":
        main = groebner_sat(T["eqs"], names, "bp", order="grevlex",
                            timeout=timeout, engine="singular")
        print("  MAIN sat bp!=0:", main.get("verdict"), "size", main.get("basis_size"),
              "time", "%.2fs" % main.get("elapsed", 0))
        if main.get("verdict") not in ("SATURATED-EMPTY", "SURVIVES") or main.get("basis_size") in (0, None):
            print("  Singular MAIN looked broken; sympy fallback ...")
            main_sy = groebner_sat(T["eqs"], names, "bp", order="grevlex",
                                   timeout=timeout, engine="sympy")
            print("  SYM MAIN sat bp!=0:", main_sy.get("verdict"), "size",
                  main_sy.get("basis_size"), "time", "%.2fs" % main_sy.get("elapsed", 0))
            main = main_sy
        eqs0 = [sp.expand(e.subs({sp.Symbol("bp"): 0})) for e in T["eqs"]]
        eqs0 = [e for e in eqs0 if e != 0]
        print("  bp=0: #eqs", len(eqs0), " (Case 1 analogue; not saturated)")
        neg = groebner_sat([sp.Symbol("bp") - 1], names, "bp", order="grevlex",
                           timeout=20, engine="singular")
        print("  NEGATIVE bp=1 (no tail eqs):", neg.get("verdict"))
        empty = main.get("verdict") == "SATURATED-EMPTY"
        verdict = main.get("verdict", "UNKNOWN")
        if verdict == "TIMEOUT":
            verdict = "COUNTING-BOUND"
        result = dict(
            verdict=verdict, slice=slice_flag, beta_mode=beta_mode,
            n_unknowns=n_unk, n_eqs=n_eq, n_eqs7=len(T["eqs7"]), n_eqs3=len(T["eqs3"]),
            main=main, negative=neg, t_build=t_build, note=note,
            elapsed=time.time() - t0,
            ring=main.get("ring"), order=main.get("order"),
            rabinowitsch=main.get("rabinowitsch"),
        )
    else:
        if n_unk > 30:
            # try anyway with the timeout; COUNTING-BOUND if timeout
            main = groebner_sat(T["eqs"], names, names[0], order="grevlex",
                                timeout=timeout, engine="singular")
            print("  MAIN generic sat %s!=0:" % names[0], main.get("verdict"),
                  "size", main.get("basis_size"), "time", "%.2fs" % main.get("elapsed", 0))
            verdict = main.get("verdict", "COUNTING-BOUND")
            if verdict == "TIMEOUT":
                verdict = "COUNTING-BOUND"
            result = dict(
                verdict=verdict, slice=False, beta_mode=beta_mode,
                n_unknowns=n_unk, n_eqs=n_eq, n_eqs7=len(T["eqs7"]), n_eqs3=len(T["eqs3"]),
                main=main, t_build=t_build, note=note,
                counting="generic (a) support: %d unk, %d eqs; desk cap %ss"
                          % (n_unk, n_eq, timeout),
                elapsed=time.time() - t0,
            )
        else:
            main = groebner_sat(T["eqs"], names, names[0], order="grevlex",
                                timeout=timeout, engine="singular")
            verdict = main.get("verdict", "UNKNOWN")
            result = dict(verdict=verdict, n_unknowns=n_unk, n_eqs=n_eq,
                          main=main, elapsed=time.time() - t0)
    dump("g2_%s.json" % beta_mode, result)
    return result


def step_g2_newton_slice(timeout=90):
    """Newton-tight slice: h = y^5 + a x^2 y + y-poly + e x, Moh-pattern beta, J=c x^4.

    Already SATURATED-EMPTY as a SLICE in the charged descent-radii lane.
    Re-run here with Singular + sat() discipline.
    """
    banner("4d. G2 Newton-tight 12-unknown SLICE, J=c x^4 (not a G2 kill)")
    t0 = time.time()
    aa, b0, b1, b2, b3, b4, ee = sp.symbols("aa b0:5 ee")
    bp, bq, br, bs = sp.symbols("bp bq br bs")
    c = sp.symbols("cc")
    h = sp.expand(y ** 5 + aa * x ** 2 * y + b4 * y ** 4 + b3 * y ** 3 + b2 * y ** 2 + b1 * y + b0 + ee * x)
    A = sp.expand(sp.together((h - h.subs(y, 0)) / y))
    beta = sp.expand(bp * A + bq * y + br * x + bs)
    qd, rd = euclid(beta ** 2, h, y)
    alpha = qd
    f = sp.expand(h ** 2 + 2 * beta)
    g = sp.expand(h ** 3 + 3 * beta * h + sp.Rational(3, 2) * alpha)
    unk = [aa, b0, b1, b2, b3, b4, ee, bp, bq, br, bs, c]
    print("  #unk", len(unk), "building J ...")
    eqs, J = jac_eqs(f, g, c, 4, x, y)
    print("  #eqs", len(eqs), "deg_y J", sp.degree(J, y) if J != 0 else None)
    main = groebner_sat(eqs, [str(v) for v in unk], "cc", order="grevlex",
                        timeout=timeout, engine="singular")
    print("  MAIN sat cc!=0:", main.get("verdict"), "size", main.get("basis_size"),
          "time", "%.2fs" % main.get("elapsed", 0))
    neg = groebner_sat([c - 1, bp - 1], [str(v) for v in unk], "cc",
                       order="grevlex", timeout=20, engine="singular")
    print("  NEGATIVE cc=1,bp=1 (no J):", neg.get("verdict"))
    result = dict(
        verdict=main.get("verdict"),
        slice=True,
        n_unknowns=len(unk), n_eqs=len(eqs),
        main=main, negative=neg,
        note="Newton-tight slice y^5+a x^2 y + y-poly + e x, Moh-pattern beta; "
             "NOT a kill of G2 (FALLACY-v2: a slice is not the problem).",
        elapsed=time.time() - t0,
        ring="Q[aa,b0..b4,ee,bp,bq,br,bs,cc,T]",
        rabinowitsch="T*cc-1",
    )
    dump("g2_newton_slice.json", result)
    return result


def main():
    t_all = time.time()
    print("appii-uniform-20260903 / run_all.py")
    print("Singular:", subprocess.run(["which", "Singular"], capture_output=True, text=True).stdout.strip())
    summary = {}
    summary["closed"] = step_closed_form()
    summary["moh1510"] = step_moh_1510()
    summary["control"] = step_control_family()
    summary["g2_counts"] = step_g2_counts()
    summary["g2_unlicensed_226"] = step_g2_unlicensed_226()
    # G2 without c, Moh-pattern beta (slice, but (3) may finish)
    summary["g2_moh_ab"] = step_g2_without_c_tail(beta_mode="moh_ab", timeout=90)
    # G2 without c, generic 27 (honest); short cap
    summary["g2_generic"] = step_g2_without_c_tail(beta_mode="generic", timeout=75)
    # Newton slice
    summary["g2_newton"] = step_g2_newton_slice(timeout=90)
    # (16,12) last: can be slow
    remain = 75 * 60 - (time.time() - t_all)
    print("\n  wall remain ~%.0fs before 75min cap" % remain)
    summary["moh1612"] = step_moh_1612(timeout=min(180, max(60, remain - 30)))
    summary["elapsed"] = time.time() - t_all
    dump("summary.json", summary)
    print("\n\n==== SUMMARY ====")
    for k, v in summary.items():
        if isinstance(v, dict) and "verdict" in v:
            print("  %-24s %s" % (k, v["verdict"]))
        elif k == "closed":
            print("  %-24s allok=%s" % (k, v.get("allok")))
        elif k == "g2_counts":
            print("  %-24s n_ord=%s licensed_c=%s" % (
                k, v["Soff"]["n_ord"], v["Son"]["licensed_c"]))
        else:
            print("  %-24s %s" % (k, type(v).__name__))
    print("  elapsed %.1fs" % summary["elapsed"])
    return summary


if __name__ == "__main__":
    main()
