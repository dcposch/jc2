#!/usr/bin/env python3
"""Hostile gate replay for the three DERIVED-SOURCE facts of
xmodel/g9966-source-review-opus5-20260903.md.

All asserted values are Fraction / sympy exact. No floats.
p' and q' mean d/d(pi) (Moh Prop A.1 / Xu (7.1)), never a label.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd
import itertools
import json
import sympy as sp

R = {}

# ---------------------------------------------------------------------------
# Skeleton: Moh p.202 row + p.194 (u_s = d_s - v_s)
# ---------------------------------------------------------------------------
n, m = 99, 66
M = {1: -66, 2: 77, 3: 97}
d = {1: 99, 2: 33, 3: 11, 4: 1}
v_s, u_s, d_s = 8, 3, 11
mu = {0: -99, 1: -66, 2: -55, 3: -145}  # deg T_i = -mu_i; T_0=g, T_1=f
delta_maj = {3: F(-1), 2: F(1, 3), 1: F(4, 9)}

R["skeleton"] = dict(
    n=n, m=m, M=M, d=d, v_s=v_s, u_s=u_s, d_s=d_s,
    minus_mu={i: -mu[i] for i in mu},
    delta_major={k: str(v) for k, v in delta_maj.items()},
)

# p.190 minor test: D^* iff V_r <= d_r/(n-M_r)
thr = F(d[3], n - M[3])
R["p190_dichotomy"] = dict(
    threshold=str(thr),  # 11/2
    V3_table_is_major=(v_s > thr),  # 8 > 11/2
    u_s_is_minor=(u_s <= thr and u_s >= 1),  # 3 <= 11/2
)

# p.194 major-radius formula (NOT the minor delta*)
d2 = F(u_s * (n - M[2]) - d_s, v_s * (n - M[2]) - d_s)
R["p194_delta2_major"] = dict(value=str(d2), matches_p202=(d2 == delta_maj[2]))


# ---------------------------------------------------------------------------
# Fact 1. Prop 6.1 order identity with MINOR V_r = u_s
# Printed p.191 (r=s empties the sum) and p.193 eq (3):
#   ord g(sigma) = n*delta_s + V_r*(n/d_r)*(delta - delta_r)
#                = n[ 1/(n-M_r)(-1+delta_r) + (V_r/d_r)(delta-delta_r) ]
# ---------------------------------------------------------------------------
def ord_g_p191(dl, V_r):
    """p.191 first display, r=s so the sum i=r+1..s is empty."""
    return n * delta_maj[3] + V_r * F(n, d_s) * (dl - delta_maj[3])


def ord_g_p193(dl, V_r):
    """p.193 eq (3) / p.192 eq (1)."""
    return n * (
        F(1, n - M[3]) * (-1 + delta_maj[3]) + F(V_r, d_s) * (dl - delta_maj[3])
    )


def ord_g_contact(dl):
    """Direct: 72 major g-roots at contact -1, 27 principal at contact delta."""
    return (v_s * n // d_s) * F(-1) + (u_s * n // d_s) * dl


def ord_g_closed(dl):
    return F(n, d_s) * (u_s * dl - v_s)  # 9(3*delta-8)


samples = [F(k, 12) for k in range(12, 40)]  # (1, 10/3)
agree = all(
    ord_g_p191(dl, u_s)
    == ord_g_p193(dl, u_s)
    == ord_g_contact(dl)
    == ord_g_closed(dl)
    for dl in samples
)
# Prop 6.2 p.195 at the order-1 probe: (u_s - v_s)*n/d_s
ord_at_1 = ord_g_closed(F(1))
R["fact1_order_identity"] = dict(
    four_forms_agree=agree,
    closed_form="(n/d_s)(u_s*delta - v_s) = 9(3*delta-8)",
    V_r_used="u_s=3 (minor factor), NOT table V_3=8",
    ord_g_delta_1=str(ord_at_1),  # -45, matches Prop 6.2 p.195
    matches_prop62_p195=(ord_at_1 == F(u_s - v_s) * n / d_s),
    ord_g_delta_2=str(ord_g_closed(F(2))),  # -18, Moh p.209
    ord_g_delta_52=str(ord_g_closed(F(5, 2))),
    ceiling="ord g < 0  <=>  delta < v_s/u_s = 8/3",
    major_V3_would_give=str(ord_g_p191(F(2), v_s)),  # not -18
    hypotheses=[
        "g monic in y, deg_y = n > 1",
        "r=s=3, tower is the single major disc D_s of radius delta_s=-1",
        "pi-c_s factor of p(pi) (Prop 4.6) with multiplicity V_r=u_s=3",
        "minor test d_s/(n-M_s)=11/2 >= V_r=3 >= 1  (p.190 / Prop 6.1 hyp)",
        "sigma a pi-root of g * prod_{i<s} T_i^psi with ord(sigma-tau)>delta_s",
        "highest form [(y-ax)^{v_s}(y-bx)^{u_s}]^{n/d_s}, a!=b  (p.194)",
    ],
)

# Xu §8 five displayed orders, from the skeleton (Cor 7.5 exponents)
def xu8_orders(dl):
    base = ord_g_closed(dl)  # 9(-8+3 delta)
    # T3 multiplicity index 13 = (-mu_s - 2)/d_s = (145-2)/11
    # (T3)_f index 22 = (-mu_s + n - 2)/d_s = (145+99-2)/11
    t3_idx = F(-mu[3] - 2, d_s)
    t3f_idx = F(-mu[3] + n - 2, d_s)
    return dict(
        f=base * F(m, n),
        g=base,
        T2=base * F(-mu[2], n),
        T3f=base * t3f_idx / 9,  # 22(-8+3delta)
        T3=base * t3_idx / 9 - 1 + dl,  # 13(-8+3delta)-1+delta
    )


want = {
    F(2): dict(f=-12, g=-18, T2=-10, T3f=-44, T3=-25),
    F(5, 2): dict(f=-3, g=F(-9, 2), T2=F(-5, 2), T3f=-11, T3=-5),
}
xu_chk = {}
for dl, w in want.items():
    got = xu8_orders(dl)
    xu_chk[str(dl)] = {
        k: str(got[k]) for k in got
    }
    xu_chk[str(dl)]["matches_xu_printed"] = all(got[k] == w[k] for k in w)
    xu_chk[str(dl)]["T3f_is_22_times"] = got["T3f"] == 22 * (-8 + 3 * dl)
    xu_chk[str(dl)]["T3_is_13_times_shift"] = got["T3"] == 13 * (-8 + 3 * dl) - 1 + dl
R["xu_section8_orders"] = xu_chk
R["xu_index_identities"] = dict(
    T3_index=str(F(-mu[3] - 2, d_s)),  # 13
    T3f_index=str(F(-mu[3] + n - 2, d_s)),  # 22
    deg_q=int(u_s * (-mu[3] - 2) / d_s + 1),  # 40
    deg_p=u_s,
)

# Prop 6.2 bidegrees (p.195)
R["prop62"] = dict(
    deg_y_g=int(v_s * n / d_s),
    deg_z_g=int(u_s * n / d_s),
    deg_y_f=int(v_s * (-mu[1]) / d_s),
    deg_z_f=int(u_s * (-mu[1]) / d_s),
    deg_y_T2=int(v_s * (-mu[2]) / d_s),
    deg_z_T2=int(u_s * (-mu[2]) / d_s),
)


# ---------------------------------------------------------------------------
# Fact 2. Face ODE, resonance budget, Galois
# ---------------------------------------------------------------------------
def a_of(dl):  # ord T3
    return 13 * (-8 + 3 * dl) - 1 + dl  # = 40*dl - 105


def b_of(dl):  # ord g
    return 9 * (-8 + 3 * dl)  # = 27*dl - 72


lead_c = 27 * a_of(F(2)) - 40 * b_of(F(2))
R["face_ode"] = dict(
    equation="9*a*q*p' - b*q'*p = c*p^14   (p'=d/dpi, q'=d/dpi)",
    a="40*delta-105",
    b="27*delta-72",
    leading_c_monic=str(lead_c),
    c_delta_independent=all(
        27 * a_of(F(k, 6)) - 40 * b_of(F(k, 6)) == 45 for k in range(7, 16)
    ),
    # exponent match in Xu (7.1), all delta
    jacobian_exponents_match=all(
        (a_of(F(k, 6)) + b_of(F(k, 6)) - 1)
        == (22 * (-8 + 3 * F(k, 6)) - 2 + F(k, 6))
        for k in range(7, 16)
    ),
)


def rho_of(dl):
    """Resonant r/mm = 9a/b = 5(8delta-21)/(3delta-8)."""
    return F(9 * a_of(dl), 1) / b_of(dl) if b_of(dl) != 0 else None


NONRES = lambda mm: 13 * mm + 1


def screen_delta(dl):
    """Return partition -> feasible multiplicity vectors (sum r <= 40)."""
    if b_of(dl) == 0:
        return dict(note="ord g = 0; detector fails; ODE degenerates")
    rho = rho_of(dl)
    out = {}
    for part in ((1, 1, 1), (2, 1), (3,)):
        opts = []
        for mm in part:
            choices = [NONRES(mm)]
            rres = rho * mm
            if rres.denominator == 1 and rres >= 0:
                choices.append(int(rres))
            opts.append(sorted(set(choices)))
        feasible = [combo for combo in itertools.product(*opts) if sum(combo) <= 40]
        out[str(part)] = dict(
            rho=str(rho),
            nonresonant_total=sum(NONRES(mm) for mm in part),
            feasible=[list(x) for x in feasible],
        )
    return out


# Candidate list charged by the task, plus den>3 probe
task_deltas = [
    F(4, 3), F(5, 3), F(2), F(7, 3), F(8, 3), F(5, 2),
    F(1), F(3), F(3, 2),
]
enum = {}
for dl in task_deltas:
    row = dict(delta=str(dl))
    if dl <= 1:
        row["status"] = "excluded_by_Xu_Prop_7.3_delta>1" if dl == 1 else "not_in_open_interval"
        if dl == 1:
            row["note"] = "Prop 7.3: leaders at order 1 are powers of one linear poly (no split)"
    elif dl >= F(8, 3):
        row["status"] = "excluded_by_ceiling_ord_g>=0"
        row["ord_g"] = str(ord_g_closed(dl))
        if dl == F(8, 3):
            row["screen"] = screen_delta(dl)
    else:
        row["status"] = "in_window"
        row["ord_g"] = str(ord_g_closed(dl))
        row["screen"] = screen_delta(dl)
        row["alive_ode"] = any(
            v.get("feasible") for v in row["screen"].values() if isinstance(v, dict)
        )
    enum[str(dl)] = row

R["task_delta_screen"] = enum
R["ode_survivors_in_task_list"] = [
    k for k, v in enum.items() if v.get("alive_ode")
]


# Galois: den=e of delta, action pi |-> zeta_e^p pi with gcd(p,e)=1
# => nonzero orbits have size e. A cubic split requires e | 3 or e with 0+orbit.
def galois_cubic(e, part):
    if e == 1:
        return True, "unramified; translation+scale gauge"
    if part == (3,):
        return True, "all mass at the unique fixed point 0: not a split"
    if e > 3:
        return False, (
            "nonzero mu_e-orbit has size e>3; cannot fit in deg p=3 "
            "except all-at-0 (no split). This is the missing proof that "
            "den(delta)<=u_s=3 for a cubic split."
        )
    if e == 2:
        if part == (1, 1, 1):
            return True, "orbit {0, gamma, -gamma}: p=pi(pi^2-c), c!=0"
        if part == (2, 1):
            return False, (
                "mu_2: pi|->-pi. A 2+1 multiset of distinct roots needs "
                "the double and the simple both fixed (=0): impossible"
            )
    if e == 3:
        if part == (1, 1, 1):
            return True, "orbit {gamma, w*gamma, w^2*gamma}: p=pi^3-c, c!=0"
        if part == (2, 1):
            return False, "mu_3: 2+1 cannot be a union of size-3 orbits and {0}"
    return False, "no stable cubic multiset"


# den>3 probe: all reduced fractions in (1, 8/3) with den<=30
wide = []
for den in range(1, 31):
    for num in range(den + 1, int(F(8, 3) * den) + 1):
        dl = F(num, den)
        if dl <= 1 or dl >= F(8, 3):
            continue
        if gcd(num, den) != 1:
            continue
        scr = screen_delta(dl)
        alive = [
            p for p, v in scr.items()
            if isinstance(v, dict) and v.get("feasible") and p != "(3,)"
        ]
        gal = {p: galois_cubic(dl.denominator, eval(p)) for p in ("(1, 1, 1)", "(2, 1)")}
        gal_alive = [p for p in alive if gal[p][0]]
        wide.append(dict(
            delta=str(dl), den=dl.denominator,
            ode_alive=alive,
            galois_alive=gal_alive,
        ))

R["wide_screen_den_le_30"] = dict(
    n_candidates=len(wide),
    ode_alive=[w["delta"] for w in wide if w["ode_alive"]],
    galois_and_ode_alive=[w["delta"] for w in wide if w["galois_alive"]],
    note=(
        "Without Xu's den<=3 assertion, ODE+Galois still leaves only "
        "delta=2 and delta=5/2 as split survivors inside (1,8/3)."
    ),
)

R["xu_den_bound"] = dict(
    printed="Xu p.13: 'the denominator of order delta <= u_s = 3'",
    proof_exhibited_in_pp10_13=False,
    type="SOURCE-ASSERTED",
    classification_survives_without_it=True,
    reason="mu_e-orbits of size e>3 cannot embed in a cubic split",
)


# ---- explicit ODE solutions ----
pi_, A_, C_, W_, S_ = sp.symbols("pi a c w s")


def ode_residual(dl, p, q):
    a, b = sp.Rational(a_of(dl)), sp.Rational(b_of(dl))
    return sp.expand(9 * a * q * sp.diff(p, pi_) - b * sp.diff(q, pi_) * p - 45 * p ** 14)


# delta=2 charged family
p_B = pi_ ** 2 * (pi_ + 3 * A_)
q_B = pi_ ** 25 * (pi_ + 3 * A_) ** 14 * (pi_ - 2 * A_)
res_B = sp.simplify(ode_residual(F(2), p_B, q_B))

# extra-root uniqueness: p=pi^2 (pi-s), q=pi^25 (pi-s)^14 (pi-w)
p_gen = pi_ ** 2 * (pi_ - S_)
q_gen = pi_ ** 25 * (pi_ - S_) ** 14 * (pi_ - W_)
res_gen = sp.expand(ode_residual(F(2), p_gen, q_gen))
# residual is c(s,w) * pi^N * (pi-s)^M ; demand all coeffs 0
poly_gen = sp.Poly(sp.together(res_gen), pi_)
# factor out pi^{...}(pi-s)^{...} numerically by substituting and collecting
# Solve: content in (s,w) after expanding
coeffs = sp.Poly(res_gen, pi_).coeffs()
rel = [sp.numer(sp.together(c)) for c in coeffs]
ideal_gens = [sp.expand(g) for g in rel if g != 0]
# Groebner in Q[s,w] (a not present)
sols = sp.solve(ideal_gens, [W_], dict=True) if ideal_gens else []
# Filter s!=0 (genuine [2,1])
w_in_terms_of_s = []
for sol in sols:
    w = sp.simplify(sol[W_])
    w_in_terms_of_s.append(str(w))
R["delta2_face"] = dict(
    charged_residual_is_zero=bool(res_B == 0),
    deg_q=int(sp.degree(sp.expand(q_B), pi_)),
    extra_root_solutions_w_of_s=sorted(set(w_in_terms_of_s)),
    charged_is_w_eq_minus_two_thirds_s=(
        any(sp.simplify(sp.sympify(w) + sp.Rational(2, 3) * S_) == 0 for w in w_in_terms_of_s)
        or any(w == "-2*s/3" for w in w_in_terms_of_s)
    ),
    unique_vector="only (25,14) among [2,1]/[1,1,1] has sum r<=40",
    leftover_degree=1,
    forced_how=(
        "ODE local budget: [1,1,1] rho=25/2 not integral and nonres 42>40; "
        "[2,1] nonres 41>40; only resonant r(mm=2)=25 plus nonres r(mm=1)=14. "
        "Extra linear factor position then fixed by the ODE to w=-2s/3 "
        "(= 2a when s=-3a). Gauge pi|->lam*pi eats a. Face = a point."
    ),
)

# Xu (8.2) Jacobian identity (printed)
t = sp.symbols("t")
# (8.2): d(t,pi) of (pi(pi+3a)^2 (pi-2a) t^{-1} , pi^2 (pi+3a) t^{-2})
# Wait, looking at the page again:
# d/d(t,pi) ( pi(pi+3a)^2 (pi-2a) t^{-1} , pi^2 (pi+3a) t^{-2} ) = 5 pi^4 (pi+3a)^2 t^{-4}
U = pi_ * (pi_ + 3 * A_) ** 2 * (pi_ - 2 * A_) * t ** (-1)
V = pi_ ** 2 * (pi_ + 3 * A_) * t ** (-2)
# Jacobian U_t V_pi - U_pi V_t
jac = sp.diff(U, t) * sp.diff(V, pi_) - sp.diff(U, pi_) * sp.diff(V, t)
rhs82 = 5 * pi_ ** 4 * (pi_ + 3 * A_) ** 2 * t ** (-4)
R["xu_8_2"] = dict(
    identity_holds=bool(sp.simplify(jac - rhs82) == 0),
)

# delta=5/2
p_X = pi_ * (pi_ ** 2 - C_)
q1_int = sp.integrate(sp.expand(p_X ** 3), pi_)
e0, k_ = sp.symbols("e0 k")
q1g = k_ * q1_int + e0
q_X = sp.expand(p_X ** 10 * q1g)
res_X = sp.expand(ode_residual(F(5, 2), p_X, q_X))
polyX = sp.Poly(res_X, pi_)
eqs = [polyX.coeff_monomial(pi_ ** j) for j in range(int(polyX.degree()) + 1)]
sol_X = sp.solve(eqs, [k_], dict=True)
res_after = sp.simplify(res_X.subs(sol_X[0])) if sol_X else "NOSOL"

# zeros of Xu's q1 = -2 int p^3 (const 0) at {0, +/-sqrt(c)}
q1_xu = -2 * q1_int
sqrtc = sp.sqrt(C_)
R["delta52_face"] = dict(
    solved_k=[{str(a): str(b) for a, b in d0.items()} for d0 in sol_X],
    residual_after_k=str(res_after),
    e0_drops_out_of_q1_prime=True,
    q1_xu_at_0=str(sp.simplify(q1_xu.subs(pi_, 0))),
    q1_xu_at_sqrtc=str(sp.simplify(q1_xu.subs(pi_, sqrtc))),
    q1_xu_at_msqrtc=str(sp.simplify(q1_xu.subs(pi_, -sqrtc))),
    q1_with_e0_at_0=str(e0),
    vector_note=(
        "Xu q1=-2 int p^3 (e0=0) vanishes at pi=0 to order 4, and the "
        "evaluation at +/-sqrt(c) is computed below; e0!=0 makes q1(0)!=0. "
        "Both live inside q=p^10 q1, q1'=k p^3, not a new partition."
    ),
)

# [2,1] ODE-admissible vectors at 5/2, Galois-killed
R["delta52_21_ode_alive_galois_dead"] = enum["5/2"]["screen"]["(2, 1)"]["feasible"]

# q=p^{13}(pi-c) generic Xu reduction: never has sum r<=40 for squarefree p
R["generic_q_p13"] = dict(
    squarefree_r_per_root=13,
    total_if_3_simple=13 * 3 + 1,
    note="Xu's generic reduction is the all-simple iterate; it is the "
         "non-resonant-too-big / Cor 7.5 regime, not the delta=2 [2,1] case.",
)


# ---------------------------------------------------------------------------
# Fact 3. Trees, Im, IM, (4.3) vs Thm 3.4
# ---------------------------------------------------------------------------
def finals_from_packets(packets, delta1):
    """ord g(sigma')=0 => gk*delta' + delta1*(27-gk) - 72 = 0."""
    out = []
    for gk in packets:
        others = 27 - gk
        final = F(72 - delta1 * others, gk)
        fk = gk * m // n
        out.append(dict(g=gk, f=fk, final=final))
    return out


def pfr(stages, delta1):
    Q = v_s * m // d_s  # 48
    out = []
    for i, st in enumerate(stages):
        others = sum(s2["f"] for j, s2 in enumerate(stages) if j != i)
        out.append(F(Q - others * delta1, st["f"]))
    return out


def thm34_principal(k, dl):
    lam_f = F(m, d_s) * (u_s * dl - v_s)  # ord f at the split
    return -(k - 1) * lam_f


trees = {
    "B_delta2": dict(delta=F(2), packets=[18, 9]),
    "X_delta52": dict(delta=F(5, 2), packets=[9, 9, 9]),
    "C_delta2_dead": dict(delta=F(2), packets=[9, 9, 9]),
}
tree_out = {}
for name, tr in trees.items():
    st = finals_from_packets(tr["packets"], tr["delta"])
    pf = pfr(st, tr["delta"])
    k = len(tr["packets"])
    sD = sum(st[i]["f"] * (pf[i] - 1) for i in range(k))
    sD1 = sum((st[i]["f"] - 1) * (pf[i] - 1) for i in range(k))  # 4.7(i) extra
    t34 = thm34_principal(k, tr["delta"])
    Im = 1 + sum(x - 1 for x in pf)
    tree_out[name] = dict(
        packets=tr["packets"],
        delta=str(tr["delta"]),
        finals=[str(x) for x in pf],
        ord_g_finals=[str(s["final"]) for s in st],
        derivations_agree=all(a == b["final"] for a, b in zip(pf, st)),
        sum_D_delta_minus_1=str(sD),
        thm47i_extra_D_minus_1=str(sD1),
        thm34_principal=str(t34),
        diff_4_3_minus_thm34=str(sD - t34),
        diff_47i_minus_thm34=str(sD1 - t34),
        Im=str(Im),
        floor_ok=all(x >= F(v_s, u_s) for x in pf),
    )
R["trees"] = tree_out

# closed form
kk, dd = sp.symbols("k delta")
lhs43 = 48 * kk - 18 * dd * (kk - 1) - 18
rhs34 = (kk - 1) * 6 * (8 - 3 * dd)
R["identity_closed_form"] = dict(
    eq43_extra_minus_thm34=str(sp.simplify(lhs43 - rhs34)),
    is_30=bool(sp.simplify(lhs43 - rhs34) == 30),
    thm47i_extra="sum (|D|-1)(delta-1) is NOT this quantity and is not constant vs thm34",
)

# IM from printed major tower, single final major place at delta_1=4/9
# Xu Thm 5.1: IM = n/(m+n) * sum |D^f|(1-delta)
n_maj_f = v_s * m // d_s  # 48
IM_formula2 = F(n, m + n) * n_maj_f * (1 - delta_maj[1])
# contact formula for lambda^g at sigma_1 (r=2 step of p.191 with V=V_2=8)
lam_g = n * (
    F(1, n - M[2]) * (-1 + delta_maj[2])
    + F(8, d[2]) * (delta_maj[1] - delta_maj[2])
)
IM_formula1 = -(n_maj_f) * lam_g
R["IM"] = dict(
    n_major_f=n_maj_f,
    lambda_g_delta1=str(lam_g),
    IM_thm51_contact=str(IM_formula1),
    IM_thm51_second=str(IM_formula2),
    agrees=(IM_formula1 == IM_formula2 == 16),
    scope="single printed major place at delta_1=4/9 covering all 48 major f-roots",
)
R["cor53"] = {
    k: dict(Im=v["Im"], IM="16", passes=(F(v["Im"]) <= 16))
    for k, v in tree_out.items()
}

print(json.dumps(R, indent=1, default=str))
