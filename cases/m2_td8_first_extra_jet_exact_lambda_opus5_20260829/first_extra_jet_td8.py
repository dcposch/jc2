#!/usr/bin/env python3
"""Exact first-separation charge Delta(F) = kappa_H(pi(H)-1) on the td=8 equal-join
affine route, and the freedom of the first extra-branch jet (r_*, p_*).

Primary research, Opus 5, 2026-08-29.  Desk arithmetic only: int / Fraction and
hand-rolled polynomial lists.  No CAS, no AWS, no network.

Contents
--------
0. Route recomputation (pole -> A-step -> equal merge -> trunk -> terminal), the
   St 3.17(i) i-chain, and the recorded AF2 floors.
1. The DESCENT LAW.  Normalize u by tau := kappa_F * (u - pi(F)).  Then
        d_{I(u)} in units of 1/kappa_F  has  D_F = int_0^{tau_0} deg(p_{I(tau)}) dtau
   (St 3.10(iii) + St 3.9(iii): omega is convex, piecewise linear, slope -deg p),
   and the exact charge is
        kappa_F (pi(H) - 1) = tau_0 - kbar_F ,     Delta(F) = (kappa_H/kappa_F)(tau_0 - kbar_F).
   With no drop this is exactly the corrected St 9.3(24) gap D_F/m - kbar_F.
2. A-step (m = mult(p_F,c*) = i_A * 1 = 2): only one drop 2 -> 1 is possible, so
   the whole charge is a one-parameter law in theta := kappa_F*(O(S1,S2) - pi(F)).
   Integrality of kappa_H(pi(H)-1) (Prop 7.3 generic-perturbation line) forces
   theta in Z (contact separation) or theta in Z + 1/2 (conjugate separation),
   giving a finite menu.
3. Trunk (m = 2*i_F): Delta = 2 iff kappa_H = kappa_F and the branch-area deficit
   over the 9 normalized steps is exactly i_F.
4. Budget: sum of the exit charges <= td-1-psi = 6 and each >= 2 forces all three
   to be exactly 2.  Any single early separation kills every member of the family.
5. The JET LAYER.  Existence of F*c* forces  ord_{c*}(p_{n-k}) >= m-k  (k<m), and
        p_{F*c*}(eta) = sum_{k=0}^{m} c_k eta^{m-k},   c_k := [(eta-c*)^{m-k}] p_{n-k},
   with c_0 pinned by St 3.9(ii) and c_1..c_m NOT pinned by anything printed.
   A derived nu_F-semi-invariance of the subtop pieces is proved and imposed; the
   discriminant of p_{F*c*} is still a free affine function of c_2, so theta=1
   (Delta=8) and theta>=7 (Delta=2) are both unrefuted.

Reproduce:  python3 first_extra_jet_td8.py [--json]
"""

from fractions import Fraction as Fr
import hashlib
import json
import sys

# ---------------------------------------------------------------------------
# 0.  Route data (recomputed, not imported)
# ---------------------------------------------------------------------------

TD = 8


def frame(l, nu, eps, k, Sm, lex, w_parent):
    """P0 transport at a chain step.  Returns the reduced-cell frame."""
    dp = eps + nu * (l + Sm)
    dq = 1 + nu * (1 + k + lex)
    E = l * dq - dp
    kbar = Fr(l) * w_parent * dq / E
    X = kbar * Fr(dp, dq)
    rho = X / dp
    w = (kbar - rho) / nu
    M = _gcd(dp, dq)
    return dict(l=l, nu=nu, eps=eps, k=k, Sm=Sm, lex=lex,
                dp=dp, dq=dq, E=E, kbar=kbar, X=X, rho=rho, w=w, M=M)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def route(t):
    """The full reviewed route at affine parameter t >= 0."""
    if not (isinstance(t, int) and t >= 0):
        raise ValueError("t must be a non-negative int")
    nu_G = 4 + 3 * t

    # entry: unique off-axis td=8, m=2 header, both poles (Lambda,a,b,nu)=(4,1,2,3)
    a, b, nu_p, alpha, beta = 1, 2, 3, 2, 3
    Lam = Fr(a * b * alpha * beta, nu_p)
    kbar_0 = a * (alpha + beta)
    rho_0 = Fr(a, b)
    w_0 = (kbar_0 - rho_0) / nu_p
    pole = dict(Lambda=Lam, kbar=kbar_0, rho=rho_0, w=w_0, M=b,
                Q=(2, 4, 3, 2, 5))

    A = frame(l=2, nu=7, eps=0, k=1, Sm=1, lex=0, w_parent=w_0)

    # equal-arrival merge, two nonzero mu=3 edges
    dp_G, dq_G = 6 * nu_G, 2 * nu_G + 1
    kbar_G = Fr(2, 3) * dq_G
    X_G = 3 * (kbar_G - Fr(2, 3))
    rho_G = X_G / dp_G
    M_G = _gcd(dp_G, dq_G)
    w_G = (kbar_G - rho_G) / nu_G
    G = dict(nu=nu_G, dp=dp_G, dq=dq_G, kbar=kbar_G, X=X_G, rho=rho_G,
             w=w_G, M=M_G, n_in=7 * kbar_G - 5)

    T = frame(l=3, nu=17, eps=0, k=1, Sm=2, lex=0, w_parent=w_G)
    T["n_edge"] = nu_G * T["kbar"] - kbar_G

    j = T["M"] * (1 - T["w"])
    psi = -(-T["M"] // j) - 1 if j == int(j) else None
    psi = int(-(-Fr(T["M"]) // j)) - 1

    # St 3.17(i) i-chain (Prop 8.1 exponents), full-pattern degrees
    i_A = Fr(4, 2)                       # deg(p_pole,full)=4 = i_A * l_A, l_A=2
    deg_pA_full = i_A * A["dp"]          # = 42
    i_G = deg_pA_full / 3                # = i_G * mu, mu = 3
    deg_pG_full = i_G * dp_G
    i_T = deg_pG_full / 3                # = i_trunk * l, l = 3
    ichain = dict(i_A=i_A, deg_pA_full=deg_pA_full, i_G=i_G,
                  deg_pG_full=deg_pG_full, i_T=i_T)

    return dict(t=t, pole=pole, A=A, G=G, trunk=T, j=j, psi=psi, ichain=ichain,
                budget_ceiling=TD - 1 - psi)


# ---------------------------------------------------------------------------
# 1.  The descent law
# ---------------------------------------------------------------------------

def descent_tau0(D, deg0, drops):
    """Normalized descent length tau_0 along the extra branch.

    D     : D_F = kappa_F * d_F  (integer or Fraction)
    deg0  : deg(p_{F*c*}) = mult(p_F, c*), the initial branch count
    drops : sorted list of (tau_r, new_deg) with 0 < tau_1 < tau_2 < ... and
            deg0 > new_deg_1 > new_deg_2 > ... >= 1.

    Returns tau_0 with  int_0^{tau_0} deg(tau) dtau = D.
    """
    D = Fr(D)
    if D <= 0:
        raise ValueError("D_F must be positive")
    if deg0 < 1:
        raise ValueError("initial degree must be >= 1")
    prev_tau, prev_deg, acc = Fr(0), Fr(deg0), Fr(0)
    for tau_r, new_deg in drops:
        tau_r = Fr(tau_r)
        if tau_r <= prev_tau:
            raise ValueError("drop levels must be strictly increasing")
        if not (1 <= new_deg < prev_deg):
            raise ValueError("degree must strictly decrease and stay >= 1")
        seg = prev_deg * (tau_r - prev_tau)
        if acc + seg >= D:
            return prev_tau + (D - acc) / prev_deg
        acc += seg
        prev_tau, prev_deg = tau_r, Fr(new_deg)
    return prev_tau + (D - acc) / prev_deg


def local_charge(D, kbar, deg0, drops):
    """kappa_F * (pi(H) - 1)  =  tau_0 - kbar_F."""
    return descent_tau0(D, deg0, drops) - Fr(kbar)


def exact_charge(D, kbar, deg0, drops, kappa_ratio=1):
    """Delta(F) = kappa_H(pi(H)-1) = (kappa_H/kappa_F) * (tau_0 - kbar_F)."""
    return Fr(kappa_ratio) * local_charge(D, kbar, deg0, drops)


def af2_gap(D, kbar, m):
    """The corrected St 9.3(24) reduced gap D_F/mult - kbar_F (the AF2 lower bound)."""
    return Fr(D, 1) / Fr(m) - Fr(kbar)


# ---------------------------------------------------------------------------
# 2.  A-step menu   (D_F = 14, kbar = 5, m = 2)
# ---------------------------------------------------------------------------

A_D, A_KBAR, A_M = 14, 5, 2
A_TAU_LIN = Fr(A_D, A_M)               # 7
A_NOSEP_CHARGE = A_TAU_LIN - A_KBAR    # 2


def a_step_charge(theta, kappa_ratio=1):
    """Charge at an A-copy given separation at normalized level theta > 0.

    theta >= tau_lin = 7 means d reaches 0 before the pair separates: the whole
    descent has degree 2, kappa_H = kappa_F, and the charge is exactly 2.
    """
    theta = Fr(theta)
    if theta <= 0:
        raise ValueError("theta must be positive")
    if theta >= A_TAU_LIN:
        return Fr(2)                      # no drop below u_0; kappa cannot jump
    return Fr(kappa_ratio) * (Fr(9) - theta)


def a_step_menu():
    """All integral charges available at an A-copy.

    contact separation  (S2 from another place):  kappa_H = kappa_F, theta in N*
    conjugate separation (S2 = a conjugate of S1): kappa_H = 2 kappa_F,
                                                   theta in 1/2 + N  (b odd)
    In both families theta >= tau_lin collapses to the charge 2.
    """
    contact = {}
    for th in range(1, int(A_TAU_LIN)):        # 1..6
        contact["theta=%d" % th] = a_step_charge(th, 1)
    contact["theta>=7"] = Fr(2)

    conj = {}
    th = Fr(1, 2)
    while th < A_TAU_LIN:
        conj["theta=%s" % th] = a_step_charge(th, 2)
        th += 1
    conj["theta>7"] = Fr(2)

    values = sorted({int(v) for v in contact.values()} |
                    {int(v) for v in conj.values()})
    return dict(contact=contact, conjugate=conj, values=values)


# ---------------------------------------------------------------------------
# 3.  Trunk   (D_F = 17 i_F, kbar = 7, m = 2 i_F)
# ---------------------------------------------------------------------------

def trunk_data(t):
    r = route(t)
    i_F = r["ichain"]["i_T"]
    return dict(i_F=i_F, D=17 * i_F, kbar=7, m=2 * i_F,
                gap=af2_gap(17 * i_F, 7, 2 * i_F),
                tau_lin=Fr(17, 2), tau0_for_charge_2=Fr(9))


def trunk_area_deficit(t, drops):
    """Branch-area shed relative to the constant-degree profile, in units of i_F.

    Delta_trunk = 2 (with kappa_H = kappa_F) iff tau_0 = 9, iff the deficit
    18 i_F - int_0^9 deg  equals exactly i_F.
    """
    td_ = trunk_data(t)
    tau0 = descent_tau0(td_["D"], td_["m"], drops)
    return dict(tau0=tau0, local_charge=tau0 - 7,
                deficit_over_iF=(td_["m"] * Fr(9) - td_["D"]) / td_["i_F"]
                if tau0 == 9 else None)


# ---------------------------------------------------------------------------
# 4.  Budget
# ---------------------------------------------------------------------------

def budget_forcing(t):
    r = route(t)
    ceiling = r["budget_ceiling"]                     # td - 1 - psi = 6
    floors = dict(A1=2, A2=2, merge=0, trunk=2, origin=0)
    total = sum(floors.values())
    # each priced charge is an integer >= 2 (integrality + positive gap)
    forced = (total == ceiling)
    return dict(ceiling=ceiling, floors=floors, floor_total=total,
                all_three_forced_to_two=forced,
                margin=ceiling - total)


# ---------------------------------------------------------------------------
# 5.  Jet layer:  Q[eta] and the field K = Q[eta]/(eta^NU - B)
# ---------------------------------------------------------------------------

NU = 7
AVAL = Fr(1)          # gauge A = 1  (L1 family C, chain orbit)
BVAL = Fr(3, 2)       # B = (3/2) A  (the unique extra orbit, Prop 8.1(iv))


def padd(u, v):
    n = max(len(u), len(v))
    return [(u[i] if i < len(u) else Fr(0)) + (v[i] if i < len(v) else Fr(0))
            for i in range(n)]


def pscale(u, c):
    return [c * x for x in u]


def pmul(u, v):
    if not u or not v:
        return []
    out = [Fr(0)] * (len(u) + len(v) - 1)
    for i, a in enumerate(u):
        if a:
            for j, b in enumerate(v):
                if b:
                    out[i + j] += a * b
    return out


def ppow(u, n):
    out = [Fr(1)]
    for _ in range(n):
        out = pmul(out, u)
    return out


def pderiv(u):
    return [Fr(i) * u[i] for i in range(1, len(u))]


def orbit(c):
    """eta^NU - c."""
    p = [Fr(0)] * (NU + 1)
    p[NU] = Fr(1)
    p[0] = -Fr(c)
    return p


def keval(u):
    """Value of a Q[eta] polynomial at the class of eta in K = Q[eta]/(eta^NU - B).

    Returned as a length-NU coefficient vector over Q in the basis 1,eta,..,eta^6.
    This *is* evaluation at a root c* of eta^NU = B.
    """
    out = [Fr(0)] * NU
    for i, a in enumerate(u):
        if a:
            out[i % NU] += a * BVAL ** (i // NU)
    return out


def kzero(v):
    return all(x == 0 for x in v)


def kmul(u, v):
    out = [Fr(0)] * NU
    for i, a in enumerate(u):
        if a:
            for j, b in enumerate(v):
                if b:
                    k = i + j
                    out[k % NU] += a * b * (BVAL if k >= NU else Fr(1))
    return out


def taylor_at_cstar(u, k):
    """[(eta-c*)^k] u  =  u^{(k)}(c*) / k!   as an element of K."""
    d = list(u)
    fact = 1
    for r in range(k):
        d = pderiv(d)
        fact *= (r + 1)
    return [x / fact for x in keval(d)]


def ord_at_cstar(u, cap=6):
    for k in range(cap + 1):
        if not kzero(taylor_at_cstar(u, k)):
            return k
    return cap + 1


def ord_at_A(u, cap=6):
    """Vanishing order of a Q[eta] polynomial at a root of eta^NU = A.

    Same construction with B replaced by A; done by a temporary swap so the
    single K-implementation is reused.
    """
    global BVAL
    keep = BVAL
    try:
        BVAL = AVAL
        return ord_at_cstar(u, cap)
    finally:
        BVAL = keep


def p_F_full():
    """Full f-pattern at the A-vertex: p_F = (p_red)^{i_A}, i_A = 2, degree 42.

    p_red = (eta^7 - A)^2 (eta^7 - B)  (St 9.6(iii)(A) shape, E7-corrected,
    L1 family C with B = (3/2)A).
    """
    p_red = pmul(ppow(orbit(AVAL), 2), orbit(BVAL))
    return pmul(p_red, p_red), p_red


def child_pattern_coefficients(sub1, sub2):
    """p_{G1}(eta) = c0 eta^2 + c1 eta + c2 for the A-step (m = 2).

    c0 = [(eta-c*)^2] p_F        (pinned by St 3.9(ii))
    c1 = [(eta-c*)^1] p_{n-1}    (subtop 1; only ord >= 1 is forced)
    c2 = [(eta-c*)^0] p_{n-2}    (subtop 2; nothing is forced)
    """
    pF, _ = p_F_full()
    c0 = taylor_at_cstar(pF, 2)
    c1 = taylor_at_cstar(sub1, 1)
    c2 = taylor_at_cstar(sub2, 0)
    return c0, c1, c2


def discriminant(c0, c1, c2):
    return [a - b for a, b in zip(kmul(c1, c1), pscale(kmul(c0, c2), Fr(4)))]


def semiinv_subtop(e, factors):
    """eta^e * prod(factors)(eta^7): the derived nu_F-semi-invariant shape.

    factors is a list of (value, multiplicity) meaning prod (eta^7 - value)^mult.
    """
    out = [Fr(0)] * (e + 1)
    out[e] = Fr(1)
    for val, mult in factors:
        out = pmul(out, ppow(orbit(val), mult))
    return out


def pinned_weights(kbar, nu, D):
    """DERIVED nu_F-semi-invariance weights of the subtop pieces of f^F.

    Acting by x^{1/kappa} -> zeta x^{1/kappa} on  f(x,y) = sum_j x^{j/kappa} p_j(eta_F)
    gives  p_j(omega eta) = zeta^{-j} p_j(eta)  with omega = zeta^{kappa pi(F)}.
    The kernel of zeta |-> omega kills every p_{n-k} with (kappa/kappa_F) nmid k, and
    on the surviving pieces (k = (kappa/kappa_F) k') one gets
        p_{n-k}  supported on eta-exponents  ==  (k' - D_F) * N1^{-1}   (mod nu_F),
        N1 := kappa_F pi(F) mod nu_F = (kappa_F - kbar_F) mod nu_F,  gcd(N1,nu_F)=1.
    Since nu_F | kappa_F this is N1 = (-kbar_F) mod nu_F, independent of kappa_F.

    Returns (N1, e0, e1, e2): the top weight e0 (= l of St 3.16) and the first two
    subtop weights.  e0 = 0 recovers the printed l = 0 of the (a)-patterns.
    """
    N1 = (-Fr(kbar).numerator) % nu
    if _gcd(N1, nu) != 1:
        raise ValueError("N1 must be a unit mod nu")
    inv = pow(N1, -1, nu)
    e0 = (-Fr(D).numerator % nu) * inv % nu
    return N1, e0, (1 - Fr(D).numerator) * inv % nu % nu, (2 - Fr(D).numerator) * inv % nu


def build_jets(e1, e2, s_free):
    """Two admissible subtop fillings differing only in the free constant s_free.

    p_{n-1} = eta^{e1} (eta^7-A)^3 (eta^7-B)          -> ord_{c*} = 1 (forced), ord_{cA} = 3
    p_{n-2} = eta^{e2} (eta^7-A)^2 * s_free           -> ord_{cA} = 2 (forced), value at c* free
    """
    sub1 = semiinv_subtop(e1, [(AVAL, 3), (BVAL, 1)])
    sub2 = pscale(semiinv_subtop(e2, [(AVAL, 2)]), s_free)
    return sub1, sub2


def is_rational_scalar(v):
    """True iff the K-element v lies in Q*1 (i.e. is a rational number)."""
    return all(x == 0 for x in v[1:])


def square_jet_scalar(e1, e2):
    """The scalar s_free that makes p_{G1} a perfect square, as an element of K.

    Realizability of the perfect-square (no-first-step-separation) jet inside the
    derived semi-invariant shape holds iff this scalar is a RATIONAL number, i.e.
    iff the free subtop value p_{n-2}(c*) can be tuned to c1^2/(4 c0).
    """
    sub1, sub2_unit = build_jets(e1, e2, Fr(1))
    c0, c1, c2u = child_pattern_coefficients(sub1, sub2_unit)
    tuned = kdiv(kmul(c1, c1), pscale(c0, Fr(4)))     # required value of c2
    return kdiv(tuned, c2u), c0, c1, c2u, tuned


def semiinv_scan():
    """e2 = 2 e1 (mod 7) is exactly the weight that makes the square jet realizable."""
    ok, bad = {}, {}
    for e1 in range(NU):
        e2 = (2 * e1) % NU
        s, _, _, _, _ = square_jet_scalar(e1, e2)
        ok["e1=%d,e2=%d" % (e1, e2)] = (s[0] if is_rational_scalar(s) else None)
        e2b = (e2 + 1) % NU
        sb, _, _, _, _ = square_jet_scalar(e1, e2b)
        bad["e1=%d,e2=%d" % (e1, e2b)] = is_rational_scalar(sb)
    return ok, bad


def kinv(v):
    """Inverse in K = Q[eta]/(eta^7 - B) by exact linear algebra over Q."""
    if kzero(v):
        raise ZeroDivisionError("zero element of K")
    # solve  M x = e_0  where M is multiplication by v
    M = []
    basis = []
    for j in range(NU):
        ej = [Fr(0)] * NU
        ej[j] = Fr(1)
        basis.append(kmul(v, ej))
    for i in range(NU):
        M.append([basis[j][i] for j in range(NU)] + [Fr(1) if i == 0 else Fr(0)])
    # Gaussian elimination
    for col in range(NU):
        piv = next(r for r in range(col, NU) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(NU):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [M[r][NU] for r in range(NU)]


def kdiv(u, v):
    return kmul(u, kinv(v))


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def _fr(x):
    if isinstance(x, Fr):
        return str(x) if x.denominator != 1 else int(x)
    if isinstance(x, dict):
        return {k: _fr(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_fr(v) for v in x]
    return x


def run():
    out = {}
    r0 = route(0)
    out["route_t0"] = _fr({k: r0[k] for k in
                           ("pole", "A", "G", "trunk", "j", "psi",
                            "ichain", "budget_ceiling")})
    out["route_family_checks"] = _fr(
        {f"t={t}": dict(nu_G=route(t)["G"]["nu"],
                        kbar_G=route(t)["G"]["kbar"],
                        n_in=route(t)["G"]["n_in"],
                        n_edge=route(t)["trunk"]["n_edge"],
                        i_T=route(t)["ichain"]["i_T"])
         for t in (0, 1, 2, 5, 37)})

    # descent law: gap recovery
    out["gap_recovery"] = _fr(dict(
        A_gap=af2_gap(A_D, A_KBAR, A_M),
        A_nodrop_charge=local_charge(A_D, A_KBAR, A_M, []),
        trunk_gap_t0=trunk_data(0)["gap"],
        trunk_nodrop_charge_t0=local_charge(trunk_data(0)["D"], 7,
                                            trunk_data(0)["m"], []),
    ))

    menu = a_step_menu()
    out["a_step"] = _fr(dict(
        D=A_D, kbar=A_KBAR, m=A_M, tau_lin=A_TAU_LIN,
        nosep_charge=A_NOSEP_CHARGE,
        contact=menu["contact"], conjugate=menu["conjugate"],
        integral_values=menu["values"],
    ))

    tr = trunk_data(0)
    half_drop = trunk_area_deficit(0, [(8, tr["i_F"])])
    out["trunk"] = _fr(dict(
        i_F_t0=tr["i_F"], D=tr["D"], m=tr["m"], gap=tr["gap"],
        tau_lin=tr["tau_lin"], tau0_needed_for_charge_2=Fr(9),
        example_half_drop_at_tau8=half_drop,
        deficit_units_of_iF=Fr(1),
    ))

    out["budget"] = _fr(budget_forcing(0))

    # jet layer
    pF, p_red = p_F_full()
    jet = dict(deg_p_red=len(p_red) - 1, deg_p_F=len(pF) - 1,
               ord_cstar_pF=ord_at_cstar(pF, 4),
               ord_cA_pF=ord_at_A(pF, 6))
    N1, e0, e1, e2 = pinned_weights(A_KBAR, NU, A_D)
    # the free datum is the K-value c2 = p_{n-2}(c*)
    s_sq, c0, c1, c2_unit, tuned = square_jet_scalar(e1, e2)
    sub1, sub2_unit = build_jets(e1, e2, Fr(1))
    disc_unit = discriminant(c0, c1, c2_unit)
    sq_realizable = is_rational_scalar(s_sq)
    sub1_sq, sub2_sq = build_jets(e1, e2, s_sq[0] if sq_realizable else Fr(1))
    c0b, c1b, c2b = child_pattern_coefficients(sub1_sq, sub2_sq)
    ok_scan, bad_scan = semiinv_scan()
    N1t, e0t, e1t, e2t = pinned_weights(7, 17, 17 * route(0)["ichain"]["i_T"])
    jet.update(dict(
        A_pinned_weights=dict(N1=N1, e0=e0, e1=e1, e2=e2),
        trunk_pinned_weights=dict(N1=N1t, e0=e0t, e1=e1t, e2=e2t),
        ord_cstar_sub1=ord_at_cstar(sub1, 4), ord_cA_sub1=ord_at_A(sub1, 6),
        ord_cA_sub2=ord_at_A(sub2_unit, 6),
        c0_nonzero=not kzero(c0), c1_nonzero=not kzero(c1),
        jet_E_disc_nonzero=not kzero(disc_unit),
        jet_E_s_free=1,
        jet_L_s_free=s_sq[0] if sq_realizable else None,
        jet_L_s_free_is_rational=sq_realizable,
        jet_L_disc_zero=kzero(discriminant(c0b, c1b, c2b)),
        semiinv_weight_law_ok=ok_scan,
        semiinv_offweight_realizable=bad_scan,
        jet_E_theta=1, jet_E_charge=int(a_step_charge(1, 1)),
        jet_L_theta=">=7", jet_L_charge=int(a_step_charge(7, 1)),
    ))
    out["jet_layer"] = _fr(jet)

    out["verdict"] = "NOT_DETERMINED_FROM_PRINTED_DATA_WITH_EXACT_SEPARATION_LAW"
    out["firewall"] = dict(
        route_killed=False, exact_lambda_two_proved=False,
        source_landing=False, keller_realizability=False,
        counterexample=False, jc2=False,
        aws_launched=False, canonical_edited=False,
    )
    return out


def certificate(payload):
    body = {k: v for k, v in payload.items() if k != "certificate_sha256"}
    blob = json.dumps(body, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode()).hexdigest()


def main(argv):
    out = run()
    out["certificate_sha256"] = certificate(out)
    text = json.dumps(out, indent=2, sort_keys=True)
    if "--json" in argv:
        print(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
