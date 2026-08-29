#!/usr/bin/env python3
"""Positive and negative controls for the equal-arrival semilinear quotient.

C1  td=6 / D9 promoted residue cell (r,nu,l) = (2,3,1), (dp,dq) = (6,10):
    the T1 solve must reproduce Obstruction O's rigid coefficient ratio
    A_1/A_2 = 2 +- sqrt(3)  (SHEET6-MULTIPOLE.md OBSTRUCTION O, SHEET6-L1 §5).
C2  D9 nu = 1 log obstruction: the reduced equation must be  2 p s' - l p' s = c'
    and the partial-fraction residue must be  (-1)^{n-1} C(2n-2, n-1) != 0.
C3  class-B/C recurrence: reproduce xmodel/sol-td7-law.md eq. (4) exactly.
C4  D9 duplicate-normalization: exhibit a single-member cell collision between
    two DIFFERENT equal-join records, and prove no whole-family collision.
C5  unequal-mu false family: the affine consistency residual is nonzero, so
    nu_G is pinned; no unbounded family exists there.
C6  case-III incoming/merge-local index separation.
"""
from fractions import Fraction as Fr
from math import gcd

from polyexact import Poly
from t1_merge_reduction import (_t_poly, rad_and_S_equalmu, build_equalmu_symbols)
from eqjoin_semilinear import EqJoinFamily, merge_local, classify_unbounded


# ---------------------------------------------------------------- C1 -------
def solve_equalmu_cell(r, mu, eps, lex, nu, sigma_fix=None):
    """Solve the reduced (T1-EQ) equation exactly for the monic Rad and S.

    Normalization: the substitution t -> c*t rescales every root, so one root
    scale may be fixed.  For lex >= 1 we fix S = t^lex + ... with sigma_0
    given by `sigma_fix` (default -1); for lex = 0 nothing is fixed.
    Returns (solution dict or None, reduced coefficient list)."""
    n, names = build_equalmu_symbols(r, lex)
    t = _t_poly(n, nu)
    Rad, Rad_t, S, S_t = rad_and_S_equalmu(n, r, lex, nu)
    dp = eps + nu * r * mu
    dq = 1 + nu * (r + lex)
    rho = Fr(dp, dq)
    reduced = (Poly.const(n, rho - eps) * Rad * S
               + Poly.const(n, nu) * Poly.const(n, rho - mu) * t * Rad_t * S
               + Poly.const(n, rho * nu) * t * Rad * S_t)
    # extract the coefficient of t^j = eta^(nu*j)
    coeffs = {}
    for j in range(r + lex + 1):
        coeffs[j] = reduced.coeff_in(0, nu * j)
    # substitute the normalization and solve the (triangular) system
    subs = {}
    if lex >= 1:
        subs[1 + r] = Fr(-1 if sigma_fix is None else sigma_fix)
    # unknowns: pi_0..pi_{r-1}, sigma_0..sigma_{lex-1} minus fixed ones
    unknown = [i for i in range(1, n) if i not in subs]
    # solve top-down: coefficient of t^{r+lex-1}, ..., t^1 must vanish
    sol = dict(subs)
    for j in range(r + lex - 1, 0, -1):
        c = coeffs[j]
        # substitute known values
        cc = _subst(c, sol, n)
        lin = _as_linear(cc, unknown, n)
        if lin is None:
            return None, coeffs
        const, lincoef = lin
        live = [i for i in unknown if i not in sol and lincoef.get(i, Fr(0)) != 0]
        if len(live) != 1:
            if all(lincoef.get(i, Fr(0)) == 0 for i in unknown if i not in sol):
                if const != 0:
                    return None, coeffs
                continue
            return None, coeffs
        i = live[0]
        sol[i] = -const / lincoef[i]
    C = _subst(coeffs[0], sol, n)
    Cval = C.d.get((0,) * n, Fr(0))
    if len(C.d) > 1:
        return None, coeffs
    return {"sol": sol, "C": Cval, "names": names, "dp": dp, "dq": dq}, coeffs


def _subst(poly, sol, n):
    out = Poly(n)
    for k, v in poly.d.items():
        c = v
        e = list(k)
        ok = True
        for i, p in enumerate(e):
            if p and i in sol:
                c = c * (sol[i] ** p)
                e[i] = 0
        if ok:
            out = out + Poly(n, {tuple(e): c})
    return out


def _as_linear(poly, unknown, n):
    """Write poly = const + sum_i lincoef[i]*var_i, or return None."""
    const = Fr(0)
    lincoef = {}
    for k, v in poly.d.items():
        deg = sum(k)
        if deg == 0:
            const += v
        elif deg == 1:
            i = k.index(1)
            lincoef[i] = lincoef.get(i, Fr(0)) + v
        else:
            return None
    return const, lincoef


def control_td6_residue_cell():
    """C1: (r,mu,eps,lex,nu) = (2,1,0,1,3) -> (dp,dq) = (6,10), M = 2,
    Rad = t^2 + pi_1 t + pi_0 with root ratio 2 +- sqrt(3)."""
    res, coeffs = solve_equalmu_cell(2, 1, 0, 1, 3, sigma_fix=-1)
    assert res is not None, "td=6 residue cell must be T1-alive"
    sol = res["sol"]
    pi1 = sol[2]        # variable index 1+1 = pi_1
    pi0 = sol[1]        # pi_0
    # roots A_1, A_2 of t^2 + pi1 t + pi0; ratio z satisfies z + 1/z + 2 = pi1^2/pi0
    ratio_invariant = pi1 * pi1 / pi0
    # for ratio 2+sqrt(3): z + 1/z = (2+sqrt3) + (2-sqrt3) = 4, so invariant = 6
    return {
        "dp": res["dp"], "dq": res["dq"], "M": gcd(res["dp"], res["dq"]),
        "pi0": pi0, "pi1": pi1, "C": res["C"],
        "ratio_invariant_pi1sq_over_pi0": ratio_invariant,
        "expected_invariant_for_2pm_sqrt3": Fr(6),
        "matches_obstruction_O": ratio_invariant == Fr(6) and res["C"] != 0,
    }


# ---------------------------------------------------------------- C2 -------
def control_d9_nu1_log(l_even_max=12):
    """C2: nu = 1 (case I) reduction and the exact log residue.

    At nu = 1 the eta factor is absorbed (MP6(c)), q = p*s, and
        rho*p*q' - p'*q = C*p  with rho = 2/(2+l)
    reduces to  2 p s' - l p' s = c',  c' = (2+l)*C.
    For even l = 2n-2 the antiderivative test gives a nonzero residue
        C(-n, n-1) = (-1)^{n-1} * binom(2n-2, n-1) != 0,
    so no rational s exists: the whole even-l branch is log-dead."""
    from math import comb
    rows = []
    for l in range(2, l_even_max + 1, 2):
        n = (l + 2) // 2
        residue = (-1) ** (n - 1) * comb(2 * n - 2, n - 1)
        rows.append({"l": l, "n": n, "residue": residue, "nonzero": residue != 0})
    # symbolic check of the nu = 1 reduction, r = 2, eps = 0, q = p*s
    N = 1 + 2 + 1   # eta, pi0, pi1, sg0 ; deg s = 1 sample
    eta = Poly.var(N, 0)
    p = eta.pow(2) + Poly.var(N, 2) * eta + Poly.var(N, 1)
    s = eta + Poly.var(N, 3)
    q = p * s
    rho = Fr(2, 3)      # l = 1 sample: dp = 2, dq = 3
    lhs = Poly.const(N, rho) * p * q.diff(0) - p.diff(0) * q
    red = Poly.const(N, Fr(2, 3)) * p * s.diff(0) - Poly.const(N, Fr(1, 3)) * p.diff(0) * s
    ok = (lhs - p * red).is_zero()
    return {"rows": rows, "nu1_reduction_identity": ok,
            "reduction": "2*p*s' - l*p'*s = (2+l)*C   [rho = 2/(2+l)]"}


# ---------------------------------------------------------------- C3 -------
def control_classBC_recurrence(mu0, l, nu):
    """C3: reproduce xmodel/sol-td7-law.md eq (4) EXACTLY from (T1-GEN).

    Class B/C shape: p = eta^mu0 (t - A), q = eta (t - A) s(t), deg s = l.
    (T1-GEN) reduces to
        (rho-mu0)(t-A)s + (rho-1)*nu*t*s + rho*nu*t*(t-A)*s' = C.
    The coefficient of t^k is  alpha_k*s_{k-1} - beta_k*A*s_k  with
        alpha_k = rho*(1+nu*k) - d,      beta_k = rho*(1+nu*k) - mu0,
        d = mu0 + nu = dp,  D = 1 + (l+1)*nu = dq,  rho = d/D.
    Hence  s_{k-1} = A*(beta_k/alpha_k)*s_k  and
        beta_k/alpha_k = (1 + d*k - mu0*(l+1)) / (d*(k - l - 1)),
    which is eq. (4) verbatim; the law `dead iff dp | dq` follows from
        mu0*(l+1) - 1 + D = d*(l+1)."""
    d = mu0 + nu
    D = 1 + (l + 1) * nu
    rho = Fr(d, D)
    rows = []
    ok = True
    for k in range(1, l + 1):
        alpha = rho * (1 + nu * k) - d
        beta = rho * (1 + nu * k) - mu0
        predicted = Fr(1 + d * k - mu0 * (l + 1), d * (k - l - 1))
        got = beta / alpha
        rows.append({"k": k, "alpha": alpha, "beta": beta,
                     "ratio": got, "sol_td7_law_eq4": predicted,
                     "match": got == predicted})
        ok = ok and got == predicted
    identity = (mu0 * (l + 1) - 1 + D == d * (l + 1))
    dead = any(d * k == mu0 * (l + 1) - 1 for k in range(1, l + 1))
    return {"d": d, "D": D, "rows": rows,
            "recurrence_matches_sol_td7_law": ok,
            "eq8_identity": identity,
            "T1_dead": dead,
            "dp_divides_dq": (D % d == 0),
            "law_agrees": dead == (D % d == 0)}


def control_classBC_symbolic(mu0, l, nu):
    """Symbolic cross-check of the same coefficient extraction."""
    N = 1 + 1 + (l + 1)
    t = Poly.var(N, 0)
    A = Poly.var(N, 1)
    s = Poly.const(N, 0)
    s_t = Poly.const(N, 0)
    for j in range(l + 1):
        s = s + Poly.var(N, 2 + j) * t.pow(j)
        if j >= 1:
            s_t = s_t + Poly.const(N, j) * Poly.var(N, 2 + j) * t.pow(j - 1)
    d = mu0 + nu
    D = 1 + (l + 1) * nu
    rho = Fr(d, D)
    red = (Poly.const(N, rho - mu0) * (t - A) * s
           + Poly.const(N, (rho - 1) * nu) * t * s
           + Poly.const(N, rho * nu) * t * (t - A) * s_t)
    out = []
    for k in range(1, l + 1):
        ck = red.coeff_in(0, k)
        a_coef = Fr(0)
        b_coef = Fr(0)
        other = 0
        for key, v in ck.d.items():
            if key[1] == 0 and key[2 + k - 1] == 1 and sum(key) == 1:
                a_coef += v
            elif key[1] == 1 and key[2 + k] == 1 and sum(key) == 2:
                b_coef += v
            else:
                other += 1
        out.append({"k": k, "alpha": a_coef, "A_beta": b_coef, "unexpected": other})
    return out


# ---------------------------------------------------------------- C4 -------
def control_duplicate_normalization():
    """C4: the D9-style duplicate hazard, exactly.

    (r,mu,eps,w) = (2,10,0,9) and (2,9,4,5) give IDENTICAL
    (dp,dq,nu,M,kbar,X,w_child) at nu = 2 but different lambda, and NO
    whole-family collision, because (slope, intercept) of dp in nu is
    (r*mu, eps)."""
    f1 = EqJoinFamily(2, 10, 0, Fr(9))
    f2 = EqJoinFamily(2, 9, 4, Fr(5))
    nu = 2
    same = {
        "dp": f1.dp(nu) == f2.dp(nu),
        "dq": f1.dq(nu) == f2.dq(nu),
        "M": f1.M(nu) == f2.M(nu),
        "kbar": f1.kbar(nu) == f2.kbar(nu),
        "X": f1.X(nu) == f2.X(nu),
        "w_child": f1.w_child == f2.w_child,
    }
    differ = {
        "lambda": (f1.lam, f2.lam),
        "family_hash": (f1.family_hash() != f2.family_hash()),
    }
    # no whole-family collision: dp slopes differ
    slopes = (f1.r * f1.mu, f2.r * f2.mu)
    return {
        "cell_tuple_collides_at_nu2": all(same.values()),
        "same": same, "differ": differ,
        "dp_slopes": slopes, "whole_family_collision": slopes[0] == slopes[1] and f1.eps == f2.eps,
        "f1": f1.record(), "f2": f2.record(),
    }


# ---------------------------------------------------------------- C5 -------
def control_unequal_mu_false_family(box=8):
    """C5: for UNEQUAL arrival multiplicities the pairwise consistency
    residual is affine in nu with a nonzero coefficient, so nu_G is pinned.
    Exhaustive over an exact algebraic box (the statement itself is proved
    in the report; this is the mechanical cross-check)."""
    bad = []
    checked = 0
    for mu_e in range(1, box + 1):
        for mu_f in range(1, box + 1):
            if mu_e == mu_f:
                continue
            for eps in range(0, min(mu_e, mu_f)):
                for s in range(2, box + 1):
                    for P in range(1, 3 * box + 1):
                        Ce = mu_e * s - P
                        Cf = mu_f * s - P
                        T = P - s * eps
                        if T == 0:
                            continue
                        for an, ad in ((1, 1), (2, 3), (3, 2), (5, 7)):
                            we = Fr(an, ad)
                            # solve the CONSTANT equation for w_f; if the slope
                            # then also vanishes we would have a false family
                            ke = Fr(mu_e) * we
                            if mu_e - eps == 0:
                                continue
                            kf = ke * Fr(mu_f - eps, mu_e - eps)
                            if kf <= 0:
                                continue
                            slope = ke * Cf - kf * Ce
                            checked += 1
                            if slope == 0:
                                bad.append((mu_e, mu_f, eps, s, P, str(we)))
    return {"checked": checked, "false_families": bad, "clean": not bad}


# ---------------------------------------------------------------- C6 -------
def caseIII_merge_local_bound(mu0, what0, C0):
    """C6: merge-local index bound at a case-III merge.

    E_0 = nu_G*C_0 and Theorem 4a (E_e <= M*mu_e*num(what_e)) with M | C_0 give
        nu_G <= mu0 * num(what0),   what0 = nu_H * w_H  (the EFFECTIVE invariant).
    This binds nu_G only.  The incoming index nu_H is bounded separately
    (sol56 two-pole theorem)."""
    what0 = Fr(what0)
    return {
        "nu_G_bound": mu0 * what0.numerator,
        "note": "what0 = nu_H * w_H; the bound therefore carries a nu_H factor",
    }
