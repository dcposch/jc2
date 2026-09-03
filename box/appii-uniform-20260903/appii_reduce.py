#!/usr/bin/env python3
"""Moh Appendix II reduction, uniform in the descended datum.

Inputs: n', m', M2', V2', k, and the closed-form radii delta1', delta2'.
Output: the polynomial system in the alpha_i, beta_i coefficients after
  (a) D1 order conditions,
  (b) remainder-degree bounds,
  tail cancellation (pi^{-1} / h^{-1} series),
  (c) inverse-Prop-6.3 root split, only when licensed.

SOURCE-READ (pdftoppm -r 200; journal page N = PDF page N-139):
  box/appii-uniform-20260903/moh-pages/j207_pdf68-68.png  Prop A.5, p.207 table
  box/appii-uniform-20260903/moh-pages/j208_pdf69-69.png  (16,12) shapes, ord >= i(-1/4)
  box/appii-uniform-20260903/moh-pages/j209_pdf70-70.png  eta-reduction, (16,12) identities
  box/appii-uniform-20260903/moh-pages/j210_pdf71-71.png  (15,10) (1)-(4), 2/2/6 split
  box/appii-uniform-20260903/moh-pages/j211_pdf72-72.png  shapes (5)-(6), Case 1/2

Prime marks n', m', M_i', V_i', d_i', delta_i', k are labels, never derivatives.
Order convention (Prop 5.1): t = x^{-1}; ord(x^i y^j at sigma=pi t^{delta1})
= -i + delta1 * j.  Moh p.208 "ord alpha_i(sigma) >= i(-1/4)" is
ord >= -i * delta1 (delta1 = 1/4 there).  The CONJ writeup's "i * delta1'"
names that same bound (Moh's signed quantity), not the positive number 5/4.

FALLACY-v2 sat(): declare ring, generator order, coefficient field Q,
Rabinowitsch generator, and both controls.  The returned object is the
Groebner basis of that component.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd, comb
import os
import subprocess
import tempfile
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# closed form (charged prop55k.py; PROVED in prop55k-opus5, delta 17(z))
# ---------------------------------------------------------------------------

def closed_form(n, m, M2, V2, k):
    d2 = gcd(n, m)
    Pi = (n + m) // d2
    U2 = d2 - V2
    R = n - M2 - 1
    dlt2 = F(-(k + 1), R)
    dlt1 = F((k + 1) * (Pi * U2 - R), R * (Pi * V2 - 1))
    return dict(d2=d2, nstar=n // d2, mstar=m // d2, Pi=Pi, U2=U2, R=R,
                delta2=dlt2, delta1=dlt1, k=k, n=n, m=m, M2=M2, V2=V2)


def datum(n, m, M2, V2, k, delta1=None, delta2=None):
    C = closed_form(n, m, M2, V2, k)
    if delta1 is None:
        delta1 = C["delta1"]
    if delta2 is None:
        delta2 = C["delta2"]
    C["delta1"] = F(delta1)
    C["delta2"] = F(delta2)
    d2, U2, V2 = C["d2"], C["U2"], C["V2"]
    C["degx_h"] = U2
    C["degx_f"] = (U2 * m // d2) if d2 else 0
    C["degx_g"] = (U2 * n // d2) if d2 else 0
    C["two_point"] = (C["delta2"] == -1)
    # (c) inverse-Prop-6.3 2,2,6 split: licensed only for the (15,10)
    # image of (75,50) with u_s=1, V2=3, delta2'=-1 (Moh p.210).
    C["split_226_licensed"] = (
        (n, m, M2, V2, k) == (15, 10, 11, 3, 2) and C["delta2"] == -1
    )
    return C


# ---------------------------------------------------------------------------
# (a) monomial supports
# ---------------------------------------------------------------------------

def h_monomials(delta1, deg_y, deg_x, tot):
    """ord h(sigma) >= -delta1  <=>  i <= delta1 * (j+1), drop monic y^{deg_y}."""
    out = []
    d1 = F(delta1)
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if i + j > tot:
                continue
            if F(i) <= d1 * F(j + 1):
                out.append((i, j))
    return out


def coeff_monomials(delta1, deg_y, deg_x, tot, weight):
    """ord poly(sigma) >= -weight * delta1  <=>  i <= delta1 * (j+weight)."""
    out = []
    d1 = F(delta1)
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if tot is not None and i + j > tot:
                continue
            if F(i) <= d1 * F(j + weight):
                out.append((i, j))
    return out


def leading_support(V2, u, split_pm):
    """Homogeneous leading form of h when delta2' = -1 (Lemma 5.3).

    u=1: y^{V2}(y-x);  u=2 and split_pm: y^{V2}(y^2-x^2)  (Moh p.210 2,2,6);
    otherwise y^{V2}(y-x)^u.
    """
    from collections import Counter
    if split_pm and u >= 2:
        a, b = u % 2, u // 2
    else:
        a, b = u, 0
    acc = Counter()
    ab = a + b
    for p in range(ab + 1):
        for q in range(b + 1):
            i = p + q
            j = (ab - p) + (b - q) + V2
            c = comb(ab, p) * ((-1) ** p) * comb(b, q)
            if c:
                acc[(i, j)] += c
    return {ij: c for ij, c in acc.items() if c}


def supports(C, use_c=False):
    """Return h_free, beta_free, lead dict, and licensing notes."""
    d1, d2, U2, V2 = C["delta1"], C["d2"], C["U2"], C["V2"]
    mstar, n = C["mstar"], C["n"]
    hm = h_monomials(d1, d2, C["degx_h"], d2)
    bm = coeff_monomials(d1, d2 - 1, C["degx_f"], C["m"], mstar)
    leader = [t for t in hm if t[0] + t[1] == d2]
    lower = [t for t in hm if t[0] + t[1] < d2]
    notes = []
    lead = {}
    licensed_c = False
    if use_c:
        if C["split_226_licensed"]:
            lead = leading_support(V2, U2, split_pm=True)
            h_free = list(lower)
            licensed_c = True
            notes.append("c: 2,2,6 licensed (15,10;11;3;X^2), h_top=y^3(y^2-x^2)")
        elif C["two_point"] and U2 >= 1:
            # two-point leading form from Lemma 5.3, NOT the inverse-6.3 2,2,6
            split_pm = (U2 == 2)
            lead = leading_support(V2, U2, split_pm=split_pm)
            h_free = list(lower)
            licensed_c = False
            notes.append(
                "c: two-point Lemma 5.3 leading form (NOT inverse-6.3 2,2,6); "
                "unlicensed as Prop 6.3 inverse split"
            )
        else:
            h_free = [t for t in hm if t != (0, d2)]
            notes.append("c requested but delta2'!=-1: no two-point leading form; order only")
    else:
        h_free = [t for t in hm if t != (0, d2)]
        notes.append("c off: order conditions only, monic y^{d2}")
    return dict(
        h_all=hm, h_free=h_free, h_leader=leader, beta_all=bm, lead=lead,
        licensed_c=licensed_c, notes=notes,
        n_h=len(h_free), n_beta=len(bm), n_ord=len(h_free) + len(bm) + 1,
    )


# ---------------------------------------------------------------------------
# polynomial builders
# ---------------------------------------------------------------------------

def poly_from_mons(mons, coeffs, x, y):
    acc = 0
    for (i, j), c in zip(mons, coeffs):
        acc += c * x ** i * y ** j
    return sp.expand(acc)


def build_h(C, S, x, y, use_c=False):
    d2 = C["d2"]
    h = y ** d2
    frees = []
    if use_c and S["lead"]:
        h = 0
        for (i, j), c in S["lead"].items():
            h += int(c) * x ** i * y ** j
    names = []
    for (i, j) in S["h_free"]:
        a = sp.symbols("h_%d_%d" % (i, j))
        frees.append(a)
        names.append("h_%d_%d" % (i, j))
        h += a * x ** i * y ** j
    return sp.expand(h), frees, names


def build_beta_generic(S, x, y):
    frees, names = [], []
    acc = 0
    for (i, j) in S["beta_all"]:
        a = sp.symbols("b_%d_%d" % (i, j))
        frees.append(a)
        names.append("b_%d_%d" % (i, j))
        acc += a * x ** i * y ** j
    return sp.expand(acc), frees, names


def build_beta_moh_ab(h, x, y):
    """Moh p.211 (6): beta = bp A + bq y + br x + bs, A = (h - h|_{y=0})/y.

    Names avoid Singular's reserved `p` (characteristic).  Licensed for
    (15,10; V2=3, delta1=1/2) where the 4-span equals the order support.
    Elsewhere this is a SLICE, labelled as such.
    """
    bp, bq, br, bs = sp.symbols("bp bq br bs")
    h0 = sp.expand(h.subs(y, 0))
    A = sp.expand(sp.together((h - h0) / y))
    beta = sp.expand(bp * A + bq * y + br * x + bs)
    return beta, [bp, bq, br, bs], ["bp", "bq", "br", "bs"], A


def euclid(num, den, y):
    q, r = sp.div(sp.Poly(sp.expand(num), y), sp.Poly(sp.expand(den), y), y)
    return sp.expand(q.as_expr()), sp.expand(r.as_expr())


def eqs_from_poly(poly, x, y, drop_constant=False):
    """Identities: every (x,y)-coefficient vanishes (optionally keep constant)."""
    p = sp.expand(poly)
    if p == 0:
        return []
    P = sp.Poly(p, x, y)
    eqs = []
    for mon, co in zip(P.monoms(), P.coeffs()):
        if drop_constant and mon == (0, 0):
            continue
        e = sp.expand(sp.numer(sp.together(co)))
        if e != 0:
            eqs.append(e)
    return eqs


# ---------------------------------------------------------------------------
# tail cancellation, (m*, n*) = (2, 3)  -- Moh p.210 (2)(3)(4)
# ---------------------------------------------------------------------------

def tail_m2n3(h, beta, x, y, d2):
    """beta^2 = alpha h + gamma, deg_y gamma < d2  (always, Euclidean).

    Polynomiality of g ~ f^{3/2} + a f^{-1/2} + ... forces
      (3)  beta^3 = (3 gamma + a) h^2 + eps h + delta
    with a in k and deg_y eps, delta < d2-1.

    Computational form (control2): the h^2-quotient of beta^3, minus 3*gamma,
    is a constant in (x,y).  (7) deg_y gamma <= d2-3 (=2 when d2=5).
    """
    alpha, gamma = euclid(beta ** 2, h, y)
    # (7)
    Pg = sp.Poly(sp.expand(gamma), y)
    deg_gamma = Pg.degree() if gamma != 0 else -1
    eqs7 = []
    max_ok = d2 - 3  # 2 when d2=5
    if deg_gamma > max_ok:
        for d in range(max_ok + 1, deg_gamma + 1):
            co = sp.expand(Pg.coeff_monomial(y ** d))
            if co == 0:
                continue
            cx = sp.Poly(co, x) if co.has(x) or (not co.free_symbols) else None
            if cx is None:
                e = sp.expand(sp.numer(sp.together(co)))
                if e != 0:
                    eqs7.append(e)
            else:
                for t in cx.coeffs():
                    e = sp.expand(sp.numer(sp.together(t)))
                    if e != 0:
                        eqs7.append(e)
    # (3): quot(beta^3, h^2) - 3 gamma  is a constant
    c2, rem = euclid(beta ** 3, h ** 2, y)
    res = sp.expand(c2 - 3 * gamma)
    eqs3 = eqs_from_poly(res, x, y, drop_constant=True)
    # remainder degree: rem = eps h + delta with deg eps,delta < d2-1
    # i.e. deg_y rem <= (d2-2) + d2 = 2 d2 - 2, but more sharply
    # deg_y (eps h) <= (d2-2) + d2 = 2 d2 - 2, and division by h^2 already
    # gives deg rem < 2 d2.  The extra vanishing is y^{2 d2 - 1} of rem
    # (already < 2 d2) and we further require the presentation
    # rem = eps*h + delta with deg eps < d2-1, deg delta < d2-1,
    # so deg rem <= d2 + (d2-2) = 2 d2 - 2, i.e. coeff of y^{2 d2 - 1} = 0.
    eqs_rem = []
    Pr = sp.Poly(sp.expand(rem), y)
    if rem != 0 and Pr.degree() >= 2 * d2 - 1:
        co = sp.expand(Pr.coeff_monomial(y ** (2 * d2 - 1)))
        if co != 0:
            eqs_rem += eqs_from_poly(co, x, y, drop_constant=False)
    return dict(
        alpha=alpha, gamma=gamma, c2=c2, rem=rem, res=res,
        deg_gamma=int(deg_gamma),
        eqs7=eqs7, eqs3=eqs3, eqs_rem=eqs_rem,
        eqs=eqs7 + eqs3 + eqs_rem,
    )


# ---------------------------------------------------------------------------
# tail cancellation, (m*, n*) = (3, 4)  -- Moh p.209
# ---------------------------------------------------------------------------

def tail_m3n4(h, beta2, beta3, a2, x, y):
    """f = h^3 + beta2 h + beta3; g from the p.209 display.

    beta2 * beta3 = gamma h + gamma_star,  deg gamma_star < deg h
    beta2^3      = delta h^2 + delta_star
    g = h^4 + (4/3)(beta2 h^2 + beta3 h) + (2/9)(beta2^3 + 2 gamma)
        - (4/81) delta + a2 h^2
    """
    gamma, gstar = euclid(beta2 * beta3, h, y)
    delta, dstar = euclid(beta2 ** 3, h ** 2, y)
    f = sp.expand(h ** 3 + beta2 * h + beta3)
    g = sp.expand(
        h ** 4
        + sp.Rational(4, 3) * (beta2 * h ** 2 + beta3 * h)
        + sp.Rational(2, 9) * (beta2 ** 3 + 2 * gamma)
        - sp.Rational(4, 81) * delta
        + a2 * h ** 2
    )
    return dict(f=f, g=g, gamma=gamma, delta=delta, gstar=gstar, dstar=dstar)


def jac_eqs(f, g, c, k, x, y):
    J = sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
    R = sp.expand(J - c * x ** k)
    eqs = eqs_from_poly(R, x, y, drop_constant=False)
    return eqs, J


# ---------------------------------------------------------------------------
# Singular Groebner
# ---------------------------------------------------------------------------

def _sing_poly(expr):
    """Sympy expression -> Singular polynomial string over Q.

    Clears denominators (Groebner over Q is unaffected) and avoids `x/2`
    which Singular parses as a poly/poly quotient.
    """
    e = sp.expand(sp.numer(sp.together(expr)))
    if e == 0:
        return "0"

    def rec(t):
        if t.is_Integer:
            return str(int(t))
        if t.is_Rational:
            return "(%d/%d)" % (int(t.p), int(t.q))
        if t.is_Symbol:
            return str(t)
        if t.is_Pow:
            b, ex = t.as_base_exp()
            return "(%s)^(%s)" % (rec(b), rec(ex))
        if t.is_Mul:
            return "*".join("(%s)" % rec(a) for a in t.args)
        if t.is_Add:
            return "+".join("(%s)" % rec(a) for a in t.args)
        raise ValueError("unprintable for Singular: %r" % (t,))

    return rec(e)


def singular_sat(eqs, varnames, sat_name, order="dp", timeout=90, extra_elim=None):
    """Groebner of (eqs, T*sat-1) over Q[vars, T].  Returns dict.

    Ring declaration: Q, grevlex (dp) or lex (lp).  Rabinowitsch T*sat-1.
    """
    t0 = time.time()
    # unique, stable generator order
    vs = list(varnames)
    if sat_name not in vs:
        vs = vs + [sat_name]
    # T last
    vs_ext = [v for v in vs if v != "T"] + ["T"]
    ring_ord = "dp" if order in ("grevlex", "dp") else "lp"
    gens = []
    for e in eqs:
        s = _sing_poly(e)
        if s != "0":
            gens.append(s)
    gens.append("T*" + sat_name + "-1")
    body = []
    body.append("option(redSB);")
    body.append("ring r = 0,(%s),%s;" % (",".join(vs_ext), ring_ord))
    body.append("ideal I;")
    for i, g in enumerate(gens, 1):
        body.append("I[%d] = %s;" % (i, g))
    body.append("ideal G = groebner(I);")
    body.append("int nG = size(G);")
    body.append("int isone = (nG == 1) && (G[1] == 1);")
    body.append('print("BEGIN_GB");')
    body.append("G;")
    body.append('print("N_G");')
    body.append("nG;")
    body.append('print("IS_ONE");')
    body.append("isone;")
    body.append('print("END_GB");')
    text = "\n".join(body) + "\n"
    try:
        keep = os.path.join(HERE, "results")
        os.makedirs(keep, exist_ok=True)
        with open(os.path.join(keep, "last.sing"), "w") as f:
            f.write(text)
    except OSError:
        pass
    with tempfile.TemporaryDirectory(prefix="appii-sing-") as td:
        path = os.path.join(td, "job.sing")
        with open(path, "w") as f:
            f.write(text)
        try:
            r = subprocess.run(
                ["Singular", "-q", "--no-tty", path],
                capture_output=True, text=True, timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return dict(
                verdict="TIMEOUT", elapsed=time.time() - t0, n_eqs=len(eqs),
                n_vars=len(vs_ext), order=ring_ord,
                ring="Q[%s]" % ",".join(vs_ext),
                rabinowitsch="T*%s-1" % sat_name,
                timeout=timeout, stdout="",
            )
        out = (r.stdout or "") + ("\n" + r.stderr if r.stderr else "")
        elapsed = time.time() - t0
        empty = False
        size = None
        isone = None
        lines = [ln.strip() for ln in out.splitlines()]
        def after(tag):
            try:
                i = lines.index(tag)
            except ValueError:
                return None
            for ln in lines[i + 1:]:
                if ln:
                    return ln
            return None
        ng_s = after("N_G")
        io_s = after("IS_ONE")
        if ng_s is not None and ng_s.lstrip("-").isdigit():
            size = int(ng_s)
        if io_s is not None and io_s in ("0", "1"):
            isone = int(io_s)
        if isone == 1 or (size == 1 and "_[1]=1" in out):
            empty = True
        first = []
        for ln in lines:
            if ln.startswith("_["):
                first.append(ln)
            if len(first) >= 8:
                break
        return dict(
            verdict="SATURATED-EMPTY" if empty else "SURVIVES",
            empty=empty, basis_size=size, elapsed=elapsed,
            n_eqs=len(eqs), n_vars=len(vs_ext), order=ring_ord,
            ring="Q[%s]" % ",".join(vs_ext),
            rabinowitsch="T*%s-1" % sat_name,
            rc=r.returncode, first=first[:8],
            stdout_tail=out[-1500:],
        )


def sympy_sat(eqs, vars_, sat_var, order="grevlex", timeout=90):
    """In-process sympy groebner with SIGALRM cap."""
    import signal

    class _T(Exception):
        pass

    def _al(s, f):
        raise _T("cap")

    t0 = time.time()
    T = sp.Symbol("T")
    ring = list(vars_) + [T]
    if sat_var not in ring:
        ring = list(vars_) + [sat_var, T]
    prev = signal.signal(signal.SIGALRM, _al)
    signal.alarm(int(timeout))
    try:
        Gb = sp.groebner(list(eqs) + [T * sat_var - 1], *ring, order=order, field=True)
        L = list(Gb)
        empty = L == [1] or (len(L) == 1 and L[0] == 1)
        return dict(
            verdict="SATURATED-EMPTY" if empty else "SURVIVES",
            empty=empty, basis_size=len(L), elapsed=time.time() - t0,
            n_eqs=len(eqs), n_vars=len(ring), order=order,
            ring="Q[%s]" % ",".join(str(v) for v in ring),
            rabinowitsch="T*%s-1" % sat_var,
            first=[str(t) for t in L[:8]],
            basis=L,
        )
    except _T:
        return dict(verdict="TIMEOUT", elapsed=time.time() - t0,
                    n_eqs=len(eqs), order=order,
                    ring="Q[%s]" % ",".join(str(v) for v in ring),
                    rabinowitsch="T*%s-1" % sat_var)
    except Exception as e:
        return dict(verdict="ERROR", error="%s: %s" % (type(e).__name__, e),
                    elapsed=time.time() - t0)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, prev)


def groebner_sat(eqs, varnames, sat_name, order="grevlex", timeout=90, engine="singular"):
    if engine == "sympy":
        vs = [sp.Symbol(v) if not isinstance(v, sp.Symbol) else v for v in varnames]
        sat = sat_name if isinstance(sat_name, sp.Symbol) else sp.Symbol(sat_name)
        return sympy_sat(eqs, vs, sat, order=order, timeout=timeout)
    names = [str(v) for v in varnames]
    return singular_sat(eqs, names, str(sat_name),
                        order=("dp" if order == "grevlex" else "lp"),
                        timeout=timeout)
