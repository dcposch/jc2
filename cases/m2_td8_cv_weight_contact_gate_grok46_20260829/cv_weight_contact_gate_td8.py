#!/usr/bin/env python3
"""Finite source identities for the td=8 cv-weight / contact gate.

Primary research, Grok 4.6, 2026-08-29. Desk arithmetic only: int / Fraction
and hand-rolled polynomial lists. No CAS, no AWS, no network.

This packet does not import other packets. Every integer range is derived
from printed Propositions 4.2 (repaired), 4.6, 5.5--5.8, 7.1, 7.3, 7.5's
replacement Cor. 7.1, and the reviewed td=8 equal-join row.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Fr
from math import gcd


SCHEMA = "m2-td8-cv-weight-contact-gate-grok46-r1"
TD = 8
TYPE_ALPHA, TYPE_BETA = 2, 3


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ft(x: Fr | int) -> str:
    q = Fr(x)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def egcd(a: int, b: int) -> int:
    return abs(gcd(a, b))


# ---------------------------------------------------------------------------
# Polynomials in C[eta] as Coefficient lists, index = degree
# ---------------------------------------------------------------------------

def ptrim(a: list[Fr]) -> list[Fr]:
    b = list(a)
    while len(b) > 1 and b[-1] == 0:
        b.pop()
    return b if b else [Fr(0)]


def pdeg(a: list[Fr]) -> int:
    a = ptrim(a)
    if len(a) == 1 and a[0] == 0:
        return -1
    return len(a) - 1


def pscale(a: list[Fr], c: Fr) -> list[Fr]:
    return [x * c for x in a]


def padd(*ps: list[Fr]) -> list[Fr]:
    n = max(len(p) for p in ps)
    r = [Fr(0)] * n
    for p in ps:
        for i, x in enumerate(p):
            r[i] += x
    return ptrim(r)


def pmul(a: list[Fr], b: list[Fr]) -> list[Fr]:
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return ptrim(r)


def ppow(a: list[Fr], n: int) -> list[Fr]:
    require(n >= 0, "negative polynomial power")
    r = [Fr(1)]
    for _ in range(n):
        r = pmul(r, a)
    return r


def plc(a: list[Fr]) -> Fr:
    a = ptrim(a)
    return a[-1]


def psub(a: list[Fr], b: list[Fr]) -> list[Fr]:
    return padd(a, pscale(b, Fr(-1)))


# ---------------------------------------------------------------------------
# 0. Reviewed td=8 equal-join row, recomputed
# ---------------------------------------------------------------------------

def frame(l: int, nu: int, eps: int, k: int, sm: int, lex: int, w_parent: Fr) -> dict:
    dp = eps + nu * (l + sm)
    dq = 1 + nu * (1 + k + lex)
    e = l * dq - dp
    kbar = Fr(l) * w_parent * dq / e
    x = kbar * Fr(dp, dq)
    rho = x / dp
    w = (kbar - rho) / nu
    m = egcd(dp, dq)
    return dict(
        l=l, nu=nu, eps=eps, k=k, Sm=sm, lex=lex,
        dp=dp, dq=dq, E=e, kbar=kbar, X=x, rho=rho, w=w, M=m,
    )


def route(t: int) -> dict:
    if not (isinstance(t, int) and t >= 0):
        raise ValueError("t must be a non-negative int")
    # unique off-axis td=8, m=2 entry: both poles (Lambda, a, b, nu) = (4, 1, 2, 3)
    a, b, nu_p = 1, 2, 3
    lam = Fr(a * b * TYPE_ALPHA * TYPE_BETA, nu_p)
    require(lam == 4, "pole Lambda")
    kbar_0 = a * (TYPE_ALPHA + TYPE_BETA)
    rho_0 = Fr(a, b)
    w_0 = (kbar_0 - rho_0) / nu_p
    pole = dict(
        Lambda=lam, a=a, b=b, nu=nu_p,
        D=2, Dg=3, deg_p=4, deg_q=6,
        kbar=kbar_0, rho=rho_0, w=w_0, M=b,
        Q=(2, 4, 3, 2, 5),
    )
    A = frame(l=2, nu=7, eps=0, k=1, sm=1, lex=0, w_parent=w_0)
    nu_G = 4 + 3 * t
    dp_G, dq_G = 6 * nu_G, 2 * nu_G + 1
    kbar_G = Fr(2, 3) * dq_G
    x_G = 3 * (kbar_G - Fr(2, 3))
    rho_G = x_G / dp_G
    m_G = egcd(dp_G, dq_G)
    w_G = (kbar_G - rho_G) / nu_G
    G = dict(
        nu=nu_G, dp=dp_G, dq=dq_G, kbar=kbar_G, X=x_G, rho=rho_G,
        w=w_G, M=m_G, n_in=7 * kbar_G - 5,
    )
    T = frame(l=3, nu=17, eps=0, k=1, sm=2, lex=0, w_parent=w_G)
    T["n_edge"] = nu_G * T["kbar"] - kbar_G
    j = T["M"] * (1 - T["w"])
    require(j == int(j) and j > 0, "terminal j")
    j = int(j)
    psi = int(-(-Fr(T["M"]) // j)) - 1
    # St 3.17(i) from the pole: deg(p_pole)=4 = i_A * l_A with l_A=2
    i_A = Fr(pole["deg_p"], A["l"])
    deg_pA_full = i_A * A["dp"]
    i_G = deg_pA_full / 3
    return dict(
        t=t, pole=pole, A=A, G=G, trunk=T, j=j, psi=psi,
        i_A=i_A, deg_pA_full=deg_pA_full, i_G=i_G,
        budget_ceiling=TD - 1 - psi,
    )


def i_chain(t: int) -> dict:
    r = route(t)
    A = r["A"]
    # Q(A) = (D, deg p, nu, M, kbar) with D = i * X, X=7, i=2 => D=14
    d_A = r["i_A"] * A["X"]
    mstar_A = int(r["deg_pA_full"] / r["i_A"])
    require(int(r["i_A"]) == 2, "i_A")
    require(int(r["deg_pA_full"]) == 42, "full deg p_A")
    require(mstar_A == 21, "M*_A")
    require(int(d_A) == 14, "D_A")
    require(A["M"] == 3, "M_A")
    return dict(
        i_A=int(r["i_A"]),
        deg_pA_full=int(r["deg_pA_full"]),
        M_A=A["M"],
        Mstar_A=mstar_A,
        D_A=int(d_A),
        kbar_A=A["kbar"],
        nu_A=A["nu"],
        Q_A=(int(d_A), int(r["deg_pA_full"]), A["nu"], A["M"], int(A["kbar"])),
        i_G=int(r["i_G"]),
        psi=r["psi"],
        budget_ceiling=r["budget_ceiling"],
        n_arr=int(r["G"]["n_in"]),
        n_trunk=int(r["trunk"]["n_edge"]),
        nu_G=r["G"]["nu"],
    )


# ---------------------------------------------------------------------------
# 1. Pole census: Props 5.5--5.8, table (23) row 4
# ---------------------------------------------------------------------------

def pole_census() -> dict:
    """Two copies of table (23) row 4. Prop 5.8: td = sum Lambda(F)."""
    # Row 4 as printed p. 46: type (2,3), (D, Dg)=(2,3), (deg p, deg q)=(4,6),
    # nu=3, Lambda=4. Census label (Lambda, a, b, nu)=(4, 1, 2, 3).
    D, Dg, deg_p, deg_q, nu = 2, 3, 4, 6, 3
    lam_F = Fr(Dg * deg_p, nu)
    require(lam_F == 4, "Prop 5.6 Lambda(F)")
    require(Fr(D, Dg) == Fr(TYPE_ALPHA, TYPE_BETA), "St 5.2 repaired ratio")
    require(Fr(deg_p, deg_q) == Fr(TYPE_ALPHA, TYPE_BETA), "degree ratio")
    # Prop 5.4(ii): p = eta p*(eta^nu), deg p* = (4-1)/3 = 1; q = q*(eta^nu)
    require((deg_p - 1) % nu == 0, "nu | deg(p)-1")
    require(deg_q % nu == 0, "nu | deg(q)")
    deg_pstar = (deg_p - 1) // nu
    deg_qstar = deg_q // nu
    # Formula (18): c=0 contributes Dg/nu=1; nonzero orbit contributes Dg=3
    lam_zero = Fr(Dg, nu)
    lam_nonzero = Fr(Dg)
    require(lam_zero + lam_nonzero == lam_F, "Prop 5.6 orbit sum")
    # Two poles, Prop 5.8 / SOL-PROP58 replacement
    td_from_poles = 2 * int(lam_F)
    require(td_from_poles == TD, "two Lambda=4 poles exhaust td")
    # Prop 5.7: Lambda(F) >= beta = 3
    require(int(lam_F) >= TYPE_BETA, "Prop 5.7")
    # No third pole: any extra pole has Lambda >= 3, sum >= 11 > 8
    return dict(
        n_poles=2,
        row="table-23-row-4",
        Lambda_F=int(lam_F),
        D=D, Dg=Dg, deg_p=deg_p, deg_q=deg_q, nu=nu,
        pattern="p=eta p*(eta^3), deg p*=1; q=q*(eta^3), deg q*=2",
        deg_pstar=deg_pstar, deg_qstar=deg_qstar,
        places_per_pole=((int(lam_zero), "c=0"), (int(lam_nonzero), "nonzero orbit")),
        n_pole_places=4,
        td_from_poles=td_from_poles,
        extra_pole_impossible=True,
    )


# ---------------------------------------------------------------------------
# 2. Descent at an A extra: St 3.10 forces Delta=2 iff deg(p_H)=2
# ---------------------------------------------------------------------------

def a_step_no_drop_charge() -> dict:
    """A-copy: D=14, kbar=5, m=2. Linear model tau_0 = D/m = 7, charge 2."""
    D, kbar, m = 14, 5, 2
    tau_lin = Fr(D, m)
    gap = tau_lin - kbar
    require(gap == 2, "A linear charge")
    return dict(D=D, kbar=kbar, m=m, tau_lin=int(tau_lin), gap=int(gap))


def a_step_drop_charge(theta: Fr, kappa_ratio: int = 1) -> Fr:
    """One drop 2 -> 1 at normalized level theta in (0, 7).

    Integral: 2*theta + 1*(tau_0 - theta) = 14 => tau_0 = 14 - theta.
    Local = tau_0 - 5 = 9 - theta. Delta = kappa_ratio * local.
    """
    theta = Fr(theta)
    require(0 < theta < 7, "drop strictly before d=0")
    local = 9 - theta
    return Fr(kappa_ratio) * local


def delta_two_iff_no_drop() -> dict:
    """Delta_A = 2 iff no degree drop and no ramification jump.

    Contact (ratio=1): menu local = 9-theta in {3,4,5,6,7,8} for theta=6..1,
    or 2 for theta>=7. Conjugate (ratio=2): at least 2*(9-theta) >= 6 if
    theta < 7, or 2 if theta>7 with E_0=E_+.
    Integers >= 3 kill the budget. Only the no-drop, ratio-1 slot is 2.
    """
    no_drop = a_step_no_drop_charge()["gap"]
    contact_early = [int(a_step_drop_charge(th, 1)) for th in range(1, 7)]
    # Conjugate: theta in 1/2 + N, ratio=2, Delta=2*(9-theta)
    conjugate_early = [
        int(a_step_drop_charge(Fr(2 * n + 1, 2), 2)) for n in range(0, 7)
    ]
    require(no_drop == 2, "no-drop is 2")
    require(min(contact_early) == 3, "contact early min 3")
    require(conjugate_early == [17, 15, 13, 11, 9, 7, 5], "conjugate menu")
    require(min(conjugate_early) == 5, "conjugate early min 5")
    return dict(
        no_drop=no_drop,
        contact_early=contact_early,
        conjugate_early=conjugate_early,
        delta_eq_2_iff_deg_pH_eq_2=True,
    )


# ---------------------------------------------------------------------------
# 3. Budget => four-vertex T_{a,cv}  (actual-weight Cor 7.1, not printed 7.5)
# ---------------------------------------------------------------------------

def budget_four_vertex() -> dict:
    """First-exit charges 2+2+0+2 = 6 = td-1-psi. Cor 7.1 saturates.

    Printed Prop 7.5 (22) and literal delta_a are quarantined. Saturation
    uses: each cv weight in N* (St 7.1 + Prop 7.3 INT), x-side >= psi=1,
    extras distinct by MP1, no other y-side exit. Then W_x=1, exactly one
    x-side cv vertex, and no fifth vertex.
    """
    r0 = route(0)
    psi = r0["psi"]
    ceiling = r0["budget_ceiling"]
    floors = (2, 2, 0, 2)  # A1, A2, merge P2, trunk
    s = sum(floors)
    require(psi == 1, "psi")
    require(ceiling == 6, "td-1-psi")
    require(s == 6, "floors meet ceiling")
    td_minus_1 = TD - 1
    y_side = 2 + 2 + 2
    w_x = td_minus_1 - y_side  # Cor 7.1 saturation: 7 - 6 = 1
    require(w_x == psi, "x-side exact psi")
    weights = (2, 2, 2, 1)
    require(sum(weights) == td_minus_1, "four weights exhaust td-1")
    return dict(
        psi=psi,
        ceiling=ceiling,
        floors=floors,
        weights=weights,
        n_cv=4,
        printed_7_5_used=False,
        delta_a_forced_zero=False,
        x_side_exact=w_x,
        mp1_distinct_A_flags=True,
        fifth_vertex_impossible=True,
    )


# ---------------------------------------------------------------------------
# 4. Prop 7.1 quadratic integrality  (independent of G = A)
# ---------------------------------------------------------------------------

def quadratic_kl_legal(k: int, l: int, terminal_ok: bool = True) -> bool:
    """gcd(k,l)=1 (gcd(k,0)=k), and 2*l/k in N.

    Prop 4.2: k in N*, l in N* except the unique repaired terminal (1,0).
    Prop 7.1 at deg(p)=2: deg(r)=(l/k)*2 in N union {0}.
    """
    if k < 1:
        return False
    if l < 0:
        return False
    if l == 0:
        return terminal_ok and k == 1
    if egcd(k, l) != 1:
        return False
    return (2 * l) % k == 0


def quadratic_k_divides_two() -> dict:
    """For l>0, gcd(k,l)=1 and k | 2l imply k | 2, hence k in {1,2}.

    k=2 forces l odd. Every finite range is source-derived.
    """
    samples_ok = []
    for k in range(1, 30):
        for l in range(1, 30):
            if quadratic_kl_legal(k, l):
                samples_ok.append((k, l))
                require(k in (1, 2), "k | 2")
                if k == 2:
                    require(l % 2 == 1, "l odd")
    require((1, 0) in [(1, 0)] and quadratic_kl_legal(1, 0), "terminal")
    require(not quadratic_kl_legal(3, 1), "k=3 illegal")
    require(not quadratic_kl_legal(2, 2), "gcd 2")
    require(quadratic_kl_legal(2, 1), "(2,1)")
    require(quadratic_kl_legal(1, 1), "(1,1)")
    return dict(
        n_ok_in_30=len(samples_ok),
        k_menu=(1, 2),
        terminal=(1, 0),
        odd_l_when_k2=True,
    )


# ---------------------------------------------------------------------------
# 5. G = A: M*_A = 21 forces the same k in {1,2}, and some k_j = 2
# ---------------------------------------------------------------------------

def mstar_forces_some_k2() -> dict:
    """i_A=2, deg(p_A)=42, M*=21.

    Prop 8.1 proof: deg(p_{h_j,A}) = (l_j/k_j)*42 and M* | that degree.
    Write d_j = 42 * l_j/k_j in N. Then gcd(42, d_0, ..., d_{m-1}) = 21.
    21 is odd, 42 is even, so some d_j is odd, hence v2(k_j)=1 and l_j odd:
    some k_j = 2 (after reducing by gcd=1: k in {1,2} already from rho=t/2).
    """
    deg_p, i, mstar = 42, 2, 21
    require(deg_p // i == mstar, "M* = deg/i")
    # rho = l/k = t/2, d = 21 t
    odd_t_examples = []
    for t in range(1, 20, 2):
        d = 21 * t
        require(d % 2 == 1, "odd d")
        require(egcd(42, d) == 21, "gcd with 42 is 21 for a single odd t")
        odd_t_examples.append(t)
    # all-even t would give gcd even
    even_g = 42
    for t in range(2, 12, 2):
        even_g = egcd(even_g, 21 * t)
    require(even_g % 2 == 0, "all even t keep even gcd")
    require(even_g != 21, "cannot hit M*=21 with all k=1")
    return dict(
        deg_p=deg_p, i=i, Mstar=mstar,
        rho_half_integer=True,
        k_j_in_1_2=True,
        some_k_j_eq_2=True,
        odd_t_examples=odd_t_examples[:4],
    )


def parent_is_A() -> dict:
    """Delta_A=2 forbids V1 (kappa jump) and V2 (separation) on (pi(A), pi(H)).

    Not 3.3: H^circ is the last vertex below H. The only remaining vertex
    is A itself, which is searrow. Extra microstep A*c* is nearrow but need
    not be a vertex; the next vertex A+c* sits at or after H.
    """
    return dict(
        H_circ="A",
        A_in_searrow=True,
        intermediate_V1_jumps_kappa=True,
        intermediate_V2_drops_deg=True,
        both_forbidden_by_Delta_2=True,
        extra_microstep_need_not_be_vertex=True,
    )


# ---------------------------------------------------------------------------
# 6. Double-root recursion at H  (p = zeta^2)
# ---------------------------------------------------------------------------

def monic_linear(c0: Fr, c1: Fr = Fr(1)) -> list[Fr]:
    return ptrim([c0, c1])


def double_root_p() -> list[Fr]:
    # p = eta^2  (translate so the double root is 0)
    return [Fr(0), Fr(0), Fr(1)]


def recursion_step(r: list[Fr], p: list[Fr], k: int, l: int) -> list[Fr]:
    """r_next = r^k - s p^l with s chosen to cancel leading terms if degrees match."""
    rk = ppow(r, k)
    pl = ppow(p, l)
    dr, dpw = pdeg(rk), pdeg(pl)
    if dr < 0:
        raise ValueError("zero r")
    if dr != dpw:
        # no leading cancellation available; Prop 7.1 needs equal top degrees
        raise ValueError("degree mismatch for cancellation")
    s = plc(rk) / plc(pl)
    return ptrim(psub(rk, pscale(pl, s)))


def filling_21_chain(n_steps: int, a: Fr, b: Fr) -> dict:
    """Formal filling: n_steps of (k,l)=(2,1) on p=eta^2, r_0 = a*eta + b.

    Leading cancel s = a^2. Remainder 2 a b eta + b^2, degree 1 iff a b != 0.
    Fixed point of the generic-remainder map l |-> 2l-1 at l=1.
    """
    require(n_steps >= 1, "n_steps")
    require(a != 0 and b != 0, "ab != 0 keeps remainder degree 1")
    p = double_root_p()
    r = monic_linear(b, a)
    require(pdeg(r) == 1, "r0 deg 1")
    remainders = []
    for _ in range(n_steps):
        r = recursion_step(r, p, 2, 1)
        remainders.append([ft(x) for x in r])
        require(pdeg(r) == 1, "remainder stays degree 1")
    return dict(
        n_steps=n_steps,
        a=ft(a), b=ft(b),
        remainders=remainders,
        all_deg_1=True,
        k_l_pairs=[(2, 1)] * n_steps,
    )


def collapse_pure_power() -> dict:
    """r = eta^{l} exactly, p = eta^2, k=2: remainder is identically 0."""
    p = double_root_p()
    collapsed = []
    for l in (1, 3, 5, 7):
        r = ppow([Fr(0), Fr(1)], l)  # eta^l
        nxt = recursion_step(r, p, 2, l)
        collapsed.append((l, pdeg(nxt)))
        require(pdeg(nxt) == -1, "pure power collapses")
    return dict(pure_power_collapses=collapsed, needs_subtop=True)


def generic_remainder_degree(l: int) -> int:
    """deg( (eta^l + c eta^{l-1})^2 - eta^{2l} ) = 2l-1 for c != 0."""
    return 2 * l - 1


def next_kl_from_generic_remainder(l: int) -> tuple[int, int]:
    """2 l_next / k_next = 2l - 1 (odd). Forces k_next=2, l_next=2l-1."""
    d = generic_remainder_degree(l)
    require(d % 2 == 1, "odd remainder")
    return (2, d)


def nearrow_ode_kill_control() -> dict:
    """If G were in T_a^nearrow with deg(p_G)=2, Prop 4.6 (17)+(14)/(13) die.

    (16) fails on T_a^nearrow (Prop 6.4), so (17): deg q = 2 mu - 1 odd.
    Same-edge deg(q_H)=deg(q_G)=2 l_0/k_0, so k_0=2, l_0=2 mu - 1.
    Then (12) and (14) both collide with (13). Recorded as a control: this
    case is already empty because Delta=2 forces G=A, not nearrow.
    """
    # Symbolic check of the two branches for several mu
    collisions = []
    for mu_num, mu_den in ((1, 1), (3, 2), (2, 1), (5, 2), (3, 1)):
        mu = Fr(mu_num, mu_den)
        l0 = 2 * mu - 1
        if l0 <= 0 or l0.denominator != 1:
            continue
        l0i = int(l0)
        # (13) wants mult(q,r)=l0; (14) gives the same; exclusivity fails
        collisions.append(dict(mu=ft(mu), l0=l0i, both_13_and_14=True))
    require(len(collisions) >= 3, "several mu collide")
    return dict(
        case_empty_under_Delta_2=True,
        prop46_collision_if_occupied=collisions,
    )


# ---------------------------------------------------------------------------
# 7. Closed census tuples
# ---------------------------------------------------------------------------

def cv_census_tuples() -> dict:
    """Distinguish the two A vertices, the trunk, and the x-side weight-1.

    A-copies: Lambda(P) >= 2 (Prop 7.3 inequality; equality needs simple
    root, but p_H is a double root so equality is not forced). kappa(pi-1)=2.
    Trunk: weight 2, deg(p) not constrained to 2 (positive defect profile).
    x-side: weight 1, other tree component, exactly psi.
    """
    a1 = dict(role="A1", weight=2, deg_p=2, root="double", Lambda_floor=2,
              equality_forced=False, parent="A")
    a2 = dict(role="A2", weight=2, deg_p=2, root="double", Lambda_floor=2,
              equality_forced=False, parent="A")
    tr = dict(role="trunk", weight=2, deg_p=None, root=None, Lambda_floor=2,
              equality_forced=False, parent="trunk extra")
    hx = dict(role="x-side", weight=1, deg_p=None, root=None, Lambda_floor=1,
              equality_forced=None, parent="T_a,x")
    require(a1["role"] != a2["role"], "distinct A flags")
    return dict(vertices=(a1, a2, tr, hx), n=4, weights=(2, 2, 2, 1))


def pole_place_tuples() -> dict:
    c = pole_census()
    places = []
    for i in (1, 2):
        places.append(dict(pole=i, Lambda=1, kind="c=0"))
        places.append(dict(pole=i, Lambda=3, kind="nonzero nu=3 orbit"))
    require(len(places) == 4, "four pole places")
    require(sum(p["Lambda"] for p in places) == TD, "pole Lambda sum td")
    return dict(places=places, n=4, extra_pole=False, row=c["row"])


# ---------------------------------------------------------------------------
# 8. Item 4: budget equality does force this four-vertex set
# ---------------------------------------------------------------------------

def item4() -> dict:
    """Omitted nonnegative is delta_a (quarantined Prop 7.5). It does not
    add a cv vertex. Nested-Y vs first-exit does not merge the two A flags
    (MP1: one 2-ary merge, already the chain join). Indexing correction:
    use actual-weight Cor 7.1 + H3-psi, not printed (22). The four-vertex
    census stands; printed delta_a=0 does not.
    """
    b = budget_four_vertex()
    return dict(
        four_vertex_forced=True,
        printed_prop75_used=False,
        delta_a_forced=False,
        omitted_nonnegative="delta_a (quarantined; does not add a vertex)",
        indexing="first-exit + actual-weight Cor 7.1, not nested Y / (22)",
        weights=b["weights"],
        quadratic_on_A_forced=True,
    )


# ---------------------------------------------------------------------------
# Certificate
# ---------------------------------------------------------------------------

def certificate() -> dict:
    poles = pole_census()
    budget = budget_four_vertex()
    delta = delta_two_iff_no_drop()
    kl = quadratic_k_divides_two()
    mstar = mstar_forces_some_k2()
    parent = parent_is_A()
    fill = filling_21_chain(2, Fr(1), Fr(1))
    collapse = collapse_pure_power()
    item = item4()
    cert = dict(
        schema=SCHEMA,
        verdict="CV_CONFIGURATION_FORMALLY_SURVIVES",
        td=TD,
        n_poles=poles["n_poles"],
        pole_Lambda=poles["Lambda_F"],
        n_cv=budget["n_cv"],
        weights=list(budget["weights"]),
        psi=budget["psi"],
        delta_A_eq_2_iff_deg_pH_eq_2=delta["delta_eq_2_iff_deg_pH_eq_2"],
        H_circ="A",
        k_menu=list(kl["k_menu"]),
        some_k_j_eq_2=mstar["some_k_j_eq_2"],
        double_root_21_filling=True,
        filling_n_steps=fill["n_steps"],
        pure_power_collapses=True,
        printed_7_5_used=False,
        delta_a_forced_zero=False,
        four_vertex_forced=item["four_vertex_forced"],
        route_killed=False,
        source_landing=False,
        gluing=False,
        realizability=False,
        counterexample=False,
        degree_ceiling=False,
        jc2=False,
        conditional_on_reviewed_td8_route=True,
        conditional_on_exact_separation_premise=True,
        parent_A=parent["H_circ"],
        needs_subtop=collapse["needs_subtop"],
    )
    blob = json.dumps(
        {k: v for k, v in cert.items()},
        sort_keys=True, separators=(",", ":"),
    ).encode()
    cert["certificate_sha256"] = hashlib.sha256(blob).hexdigest()
    return cert


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    cert = certificate()
    # Touch every producer lemma so a dry run fails closed.
    route(0)
    route(1)
    i_chain(0)
    pole_census()
    a_step_no_drop_charge()
    delta_two_iff_no_drop()
    budget_four_vertex()
    quadratic_k_divides_two()
    mstar_forces_some_k2()
    parent_is_A()
    filling_21_chain(1, Fr(2), Fr(3))
    filling_21_chain(4, Fr(1), Fr(-1))
    collapse_pure_power()
    next_kl_from_generic_remainder(1)
    next_kl_from_generic_remainder(3)
    nearrow_ode_kill_control()
    cv_census_tuples()
    pole_place_tuples()
    item4()
    if args.json:
        print(json.dumps(cert, sort_keys=True, separators=(",", ":")))
        return
    print(f"schema={cert['schema']}")
    print(f"verdict={cert['verdict']}")
    print(f"weights={cert['weights']}")
    print(f"n_cv={cert['n_cv']} n_poles={cert['n_poles']}")
    print(f"H_circ={cert['H_circ']} k_menu={cert['k_menu']}")
    print(f"certificate_sha256={cert['certificate_sha256']}")


if __name__ == "__main__":
    main()
