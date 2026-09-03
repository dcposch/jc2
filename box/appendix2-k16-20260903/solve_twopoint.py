#!/usr/bin/env python3
"""Approximate-root Jacobian solvers for s_eff=2 descended pairs.

Two branches, both J = c x^k, saturate T*c-1, FALLACY-v2 controls:

  d2e3:  d'=2, e'=3.  f = h^2+2β, g = h^3+3βh+(3/2)α.
         two-point: β = pA+qy+rx+s (charged solve_d2e3_ab).
         otherwise: β runs over D1 monomials (n_ord unknowns).

  horner_cap: p.208 chart, t-uniform h = y^{V2}(y-x)^{u} + y-polynomial
         when u=1, K=4 (the K16 ray).  α_i / β_i in Horner spans.
         α1 absorbed.  Last α_{e'} uses {A,B,y-x} (no constant).

Singular backend (char 0 or GF(p)); sympy grevlex fallback.
Prime marks are labels.
"""
from __future__ import annotations

import os
import subprocess
import tempfile
import time
from fractions import Fraction as F

import sympy as sp

from shape import shape_bundle, leading_support
from solve import (
    Alarm, Timeout, _gb_empty, build_h_two_point, build_beta_ab, jac_eqs,
    solve_d2e3_ab, solve_1612,
)


def _poly_mons(mons, coeffs, x, y):
    acc = 0
    for (i, j), c in zip(mons, coeffs):
        acc += c * x ** i * y ** j
    return sp.expand(acc)


def build_h_d1(C, x, y):
    """Monic h = y^K + D1-free (no two-point leading split)."""
    K = C["K"]
    h = y ** K
    frees = []
    for (i, j) in C["h_free"]:
        a = sp.Dummy("h_%d_%d" % (i, j))
        frees.append(a)
        h += a * x ** i * y ** j
    return sp.expand(h), frees, sp.Integer(1)


def build_beta_d1(C, x, y):
    coeffs = []
    beta = 0
    for (i, j) in C["beta_all"]:
        b = sp.Dummy("b_%d_%d" % (i, j))
        coeffs.append(b)
        beta += b * x ** i * y ** j
    return sp.expand(beta), coeffs


def solve_d2e3_d1(n, m, M2, V2, k, timeout=180, order="grevlex"):
    """d'=2, e'=3, D1 h and D1 β (no A,B).  Used when delta2' != -1."""
    t0 = time.time()
    C = shape_bundle(n, m, M2, V2, k)
    if not C["ok"] or C["dprime"] != 2:
        return dict(verdict="SKIP", reason="not d'=2", elapsed=0,
                    n=n, m=m, M2=M2, V2=V2, k=k)
    nunk = C["n_ord"]
    if nunk > 40:
        return dict(verdict="COUNTING-BOUND", n_unknowns=nunk, elapsed=0,
                    reason="n_ord>40", two_point=C["two_point"])
    x, y = sp.symbols("x y")
    c, T = sp.symbols("c T")
    if C["two_point"]:
        h, hfrees, lc = build_h_two_point(C, x, y)
    else:
        h, hfrees, lc = build_h_d1(C, x, y)
    beta, bfrees = build_beta_d1(C, x, y)
    qdiv, rdiv = sp.div(sp.Poly(sp.expand(beta ** 2), y), sp.Poly(h, y), y)
    alpha = sp.expand(qdiv.as_expr())
    f = sp.expand(h ** 2 + 2 * beta)
    g = sp.expand(h ** 3 + 3 * beta * h + sp.Rational(3, 2) * alpha)
    unk = list(hfrees) + list(bfrees) + [c]
    ring = unk + [T]
    try:
        with Alarm(timeout):
            eqs, J = jac_eqs(f, g, c, k, x, y)
            n_eqs = len(eqs)
            Gb = sp.groebner(eqs + [T * c - 1], *ring, order=order, field=True)
            empty, Gbl = _gb_empty(Gb)
            Gb0 = sp.groebner(eqs, *unk, order=order, field=True)
            unsat_empty, Gbl0 = _gb_empty(Gb0)
            GbN = sp.groebner([c - 1, T * c - 1], *ring, order=order, field=True)
            neg_empty, _ = _gb_empty(GbN)
    except Timeout:
        return dict(
            verdict="TIMEOUT", n_unknowns=nunk, elapsed=time.time() - t0,
            ring="Q[%d h-free + %d beta + c,T]" % (len(hfrees), len(bfrees)),
            order=order, two_point=C["two_point"],
        )
    except Exception as e:
        return dict(
            verdict="ERROR", error="%s: %s" % (type(e).__name__, e),
            n_unknowns=nunk, elapsed=time.time() - t0,
        )
    verdict = "SATURATED-EMPTY" if empty else "SURVIVES"
    family = None if empty else [str(t) for t in Gbl[:12]]
    return dict(
        verdict=verdict, n_unknowns=nunk, n_eqs=n_eqs,
        ring="Q[h_free(%d), beta(%d), c, T]" % (len(hfrees), len(bfrees)),
        order=order, rabinowitsch="T*c-1",
        empty=empty, basis_size=len(Gbl),
        unsaturated_empty=unsat_empty, unsaturated_size=len(Gbl0),
        negative_nontrivial=(not neg_empty),
        family=family, elapsed=time.time() - t0,
        two_point=C["two_point"],
        C_summary=dict(n=n, m=m, M2=M2, V2=V2, k=k, n_h=C["n_h"],
                       n_ord=C["n_ord"], n_ab=C["n_ab"], dprime=C["dprime"]),
        solver="d2e3_d1",
    )


def horner_chart(K, V2, u, x, y, bsyms):
    """p.208 (1) for u=1, K=V2+u.  Returns h, A, B, z, bsyms used."""
    z = y - x
    # B = y^{V2-1} z + b1 y^{V2-1} + ...  for V2=3: B = y(y-x)+b1 y+b2
    # Build from the bottom of the y-Horner of y^{V2}(y-x) + sum b_j y^j.
    # For the K16 ray, V2=3, u=1, K=4, four b's.
    if not (u == 1 and K == 4 and V2 == 3 and len(bsyms) == 4):
        raise ValueError("horner_chart only implemented for K16 u=1 V2=3 K=4")
    b1, b2, b3, b4 = bsyms
    B = sp.expand(y * z + b1 * y + b2)
    A = sp.expand(y * B + b3)
    h = sp.expand(y * A + b4)
    return h, A, B, z


def horner_span_alpha(i, eprime, one, A, B, z, K=4):
    """p.208: α1 absorbed; α_i (i<e') {1,A,...,} dim min(i,K); last {A,B,z}."""
    if i == 1:
        return []  # absorbed
    if i == eprime:
        return [A, B, z]  # no constant; K=4
    pieces = [one]
    chain = [A, B, z]
    # dim = min(i, K); pieces already has 1, need min(i,K)-1 more from chain
    need = min(i, K) - 1
    pieces.extend(chain[:need])
    return pieces


def horner_span_beta(i, dprime, one, A, B, z, K=4):
    """p.208 β2={A,1}, β3={A,B,1}; cap at K including constant."""
    pieces = [one]
    chain = [A, B, z]
    need = min(i, K) - 1
    pieces.extend(chain[:need])
    return pieces


def build_horner_cap(n, m, M2, V2, k, max_unknowns=None, drop_high=0):
    """Build (f,g,eqs,unk,c,meta) for the p.208 Horner-cap chart.

    drop_high: omit the highest `drop_high` of (alpha_{e'}, alpha_{e'-1}, ...
    then beta_{d'}, ...) to fit a Newton-tight budget.  0 = full cap.
    """
    C = shape_bundle(n, m, M2, V2, k)
    if not C["ok"] or not C["two_point"] or C["u"] != 1 or C["K"] != 4:
        return dict(ok=False, reason="not two-point u=1 K=4", C=C)
    x, y = sp.symbols("x y")
    b1, b2, b3, b4 = bsyms = sp.symbols("b1:5")
    h, A, B, z = horner_chart(4, 3, 1, x, y, bsyms)
    one = sp.Integer(1)
    ep, dp = C["eprime"], C["dprime"]
    params = list(bsyms)
    alpha = {}
    beta = {}

    def add_span(prefix, index, span):
        if not span:
            return 0
        coeffs = []
        for j in range(len(span)):
            s = sp.Symbol("%s%d_%d" % (prefix, index, j))
            coeffs.append(s)
            params.append(s)
        return sp.Add(*(cj * sj for cj, sj in zip(coeffs, span)))

    # which remainders to keep
    alpha_idx = list(range(1, ep + 1))
    beta_idx = list(range(2, dp + 1))
    # Newton-tight: drop highest remainders of g and f interleaved, so the
    # p.208 (16,12) chart {α2,α3,α4, β2,β3} is the first 18-unknown slice.
    dropped = []
    a_high = [i for i in reversed(alpha_idx) if i != 1]
    b_high = list(reversed(beta_idx))
    seq = []
    ia = ib = 0
    while ia < len(a_high) or ib < len(b_high):
        if ia < len(a_high):
            seq.append(("a", a_high[ia])); ia += 1
        if ib < len(b_high):
            seq.append(("q", b_high[ib])); ib += 1
    skip = set()
    for name, i in seq[:drop_high]:
        skip.add((name, i))
        dropped.append((name, i))

    for i in alpha_idx:
        if ("a", i) in skip:
            continue
        span = horner_span_alpha(i, ep, one, A, B, z)
        val = add_span("a", i, span)
        if val != 0:
            alpha[i] = val
    for i in beta_idx:
        if ("q", i) in skip:
            continue
        span = horner_span_beta(i, dp, one, A, B, z)
        val = add_span("q", i, span)
        if val != 0:
            beta[i] = val

    c = sp.Symbol("c")
    nunk = len(params) + 1  # +c
    if max_unknowns is not None and nunk > max_unknowns:
        return dict(ok=False, reason="over-budget", n_unknowns=nunk,
                    drop_high=drop_high, C=C)

    f_terms = [(sp.Integer(1), dp)] + [(beta[i], dp - i) for i in sorted(beta)]
    g_terms = [(sp.Integer(1), ep)] + [(alpha[i], ep - i) for i in sorted(alpha)]
    # expanded f,g only for small degrees (t=1 control); t>=2 uses h-adic
    f = g = None
    if dp <= 3 and ep <= 4:
        f = h ** dp
        for i, bi in beta.items():
            f += bi * h ** (dp - i)
        g = h ** ep
        for i, ai in alpha.items():
            g += ai * h ** (ep - i)
        f = sp.expand(f)
        g = sp.expand(g)
    return dict(
        ok=True, C=C, x=x, y=y, h=h, A=A, B=B, z=z,
        f=f, g=g, f_terms=f_terms, g_terms=g_terms,
        alpha=alpha, beta=beta, params=params, c=c,
        n_unknowns=nunk, drop_high=drop_high, dropped=dropped,
        dprime=dp, eprime=ep, k=k, n=n, m=m, M2=M2, V2=V2,
    )


def jac(f, g, x, y):
    return sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x)


def hadic_jac_eqs(h, f_terms, g_terms, c, kexp, x, y):
    """Exact h-adic Jacobian.  f_terms/g_terms are (coeff, h-power) lists.

    J(a h^r, b h^s) = h^{r+s} J(a,b) + h^{r+s-1}(s b J(a,h) + r a J(h,b)).
    Then monic division by h in y.  Remainder of h^0 equals c x^k.
    """
    by_power = {}
    for aa, r in f_terms:
        for bb, s in g_terms:
            v = jac(aa, bb, x, y)
            if v:
                by_power[r + s] = by_power.get(r + s, 0) + v
            v = s * bb * jac(aa, h, x, y) + r * aa * jac(h, bb, x, y)
            if v:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + v
    if not by_power:
        by_power = {0: 0}
    if 0 not in by_power:
        by_power[0] = 0
    kmax = max(by_power)
    k = 0
    while k <= kmax:
        rem = sp.expand(by_power.get(k, 0))
        if rem == 0:
            k += 1
            continue
        quotient, remainder = sp.div(sp.Poly(rem, y), sp.Poly(h, y), y)
        by_power[k] = sp.expand(remainder.as_expr())
        if quotient != 0:
            qe = sp.expand(quotient.as_expr())
            by_power[k + 1] = by_power.get(k + 1, 0) + qe
            if k + 1 > kmax:
                kmax = k + 1
        k += 1
    eqs = []
    by_power[0] = sp.expand(by_power.get(0, 0) - c * x ** kexp)
    for hpow in sorted(by_power):
        remainder = sp.expand(by_power[hpow])
        if remainder == 0:
            continue
        poly = sp.Poly(remainder, x, y)
        for mon, co in poly.terms():
            co = sp.expand(co)
            if co != 0:
                eqs.append(co)
    return eqs, by_power


def jac_coeff_eqs(f, g, c, k, x, y):
    eqs, J = jac_eqs(f, g, c, k, x, y)
    return eqs, J


def _singular_str(expr):
    p = sp.together(sp.expand(expr))
    num, den = sp.fraction(p)
    num = sp.expand(num)
    den = sp.expand(den)
    if den == 1 or den == -1:
        s = str(num if den == 1 else -num)
    else:
        # keep as (num)/(den) — Singular accepts Q
        s = "(%s)/(%s)" % (num, den)
    return s.replace("**", "^").replace("Dummy", "D")


def write_singular(path, eqs, gens, sat_extra, char=0, order="dp"):
    """gens includes c and T last.  sat_extra unused (always T*c-1)."""
    names = []
    rename = {}
    for g in gens:
        nm = str(g)
        nm = "".join(ch if ch.isalnum() else "u" for ch in nm)
        if not nm or nm[0].isdigit():
            nm = "v" + nm
        base, kk = nm, 0
        while nm in names:
            kk += 1
            nm = base + str(kk)
        names.append(nm)
        rename[g] = nm
    subs = {g: sp.Symbol(rename[g]) for g in gens}
    cname, Tname = names[-2], names[-1]
    gens_s = []
    for e in eqs:
        es = e.subs(subs)
        gens_s.append(_singular_str(es))
    gens_s.append("%s*%s-1" % (Tname, cname))
    with open(path, "w") as fh:
        fh.write("ring R=%s,(%s),%s;\n" % (char, ",".join(names), order))
        fh.write("option(redSB);\n")
        fh.write('print("CONTROL_EMPTY_START");\n')
        fh.write("ideal CE=%s,%s*%s-1;\n" % (cname, Tname, cname))
        fh.write("ideal GE=std(CE);\n")
        fh.write('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }\n')
        fh.write('print("CONTROL_NONEMPTY_START");\n')
        fh.write("ideal CN=%s-1,%s*%s-1;\n" % (cname, Tname, cname))
        fh.write("ideal GN=std(CN);\n")
        fh.write('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }\n')
        fh.write('print("MAIN_START n_eqs=%d n_unk=%d");\n' % (len(eqs), len(gens) - 1))
        fh.write("ideal I=%s;\n" % ",\n".join(gens_s))
        fh.write("ideal G=std(I);\n")
        fh.write('print("MAIN_DONE basis_size="); size(G);\n')
        fh.write('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); }\n')
        if eqs:
            fh.write("ideal I0=%s;\n" % ",\n".join(gens_s[:-1]))
        else:
            fh.write("ideal I0=0;\n")
        fh.write("ideal G0=std(I0);\n")
        fh.write('print("UNSAT_DONE basis_size="); size(G0);\n')
        fh.write('if (reduce(1,G0)==0) { print("UNSAT_EMPTY"); } else { print("UNSAT_NONTRIVIAL"); }\n')
        fh.write("quit;\n")
    return names


def run_singular(sing_path, timeout=180):
    t0 = time.time()
    try:
        r = subprocess.run(
            ["Singular", "-q", "--no-rc", sing_path],
            capture_output=True, text=True, timeout=timeout,
        )
        out = (r.stdout or "") + (r.stderr or "")
        elapsed = time.time() - t0
        empty = "MAIN_SATURATED_EMPTY" in out
        nontrivial = "MAIN_NONTRIVIAL" in out
        unsat_empty = "UNSAT_EMPTY" in out
        unsat_nt = "UNSAT_NONTRIVIAL" in out
        neg_ok = "CONTROL_NONEMPTY_PASS" in out
        pos_empty_ok = "CONTROL_EMPTY_PASS" in out
        if empty:
            verdict = "SATURATED-EMPTY"
        elif nontrivial:
            verdict = "SURVIVES"
        else:
            verdict = "ERROR"
        return dict(
            verdict=verdict, empty=empty, unsaturated_empty=unsat_empty,
            negative_nontrivial=neg_ok, control_empty_pass=pos_empty_ok,
            unsaturated_nontrivial=unsat_nt,
            elapsed=elapsed, rc=r.returncode, stdout_tail=out[-2500:],
            backend="Singular",
        )
    except subprocess.TimeoutExpired:
        return dict(verdict="TIMEOUT", elapsed=timeout, backend="Singular",
                    notes="Singular cap %ss" % timeout)
    except Exception as e:
        return dict(verdict="ERROR", error="%s: %s" % (type(e).__name__, e),
                    elapsed=time.time() - t0, backend="Singular")


def solve_horner_cap(n, m, M2, V2, k, timeout=180, drop_high=0,
                     backend="auto", char=0, order="dp"):
    """Solve the p.208 Horner-cap (or a high-remainder truncation)."""
    t0 = time.time()
    B = build_horner_cap(n, m, M2, V2, k, max_unknowns=None, drop_high=drop_high)
    if not B.get("ok"):
        return dict(verdict="SKIP", reason=B.get("reason"), elapsed=0,
                    n_unknowns=B.get("n_unknowns"), drop_high=drop_high)
    nunk = B["n_unknowns"]
    slice_p = drop_high > 0
    x, y, c = B["x"], B["y"], B["c"]
    T = sp.Symbol("T")
    try:
        with Alarm(max(30, timeout)):
            if B.get("f") is not None and B.get("g") is not None:
                eqs, J = jac_coeff_eqs(B["f"], B["g"], c, k, x, y)
            else:
                eqs, _bp = hadic_jac_eqs(B["h"], B["f_terms"], B["g_terms"], c, k, x, y)
                J = None
    except Timeout:
        return dict(verdict="TIMEOUT", error="eq-generation", n_unknowns=nunk,
                    elapsed=time.time() - t0, drop_high=drop_high, slice=slice_p)
    except Exception as e:
        return dict(verdict="ERROR", error="jac: %s: %s" % (type(e).__name__, e),
                    n_unknowns=nunk, elapsed=time.time() - t0)
    n_eqs = len(eqs)
    gens = B["params"] + [c, T]
    meta = dict(
        n=n, m=m, M2=M2, V2=V2, k=k, n_unknowns=nunk, n_eqs=n_eqs,
        drop_high=drop_high, slice=slice_p, dropped=B["dropped"],
        dprime=B["dprime"], eprime=B["eprime"],
        ring="Q[%d params + c, T]" % len(B["params"]),
        rabinowitsch="T*c-1", solver="horner_cap",
    )
    # Prefer Singular for >= 16 unknowns; sympy for small
    use_sing = backend in ("singular", "auto") and nunk >= 12
    use_sy = backend in ("sympy", "auto")
    out = dict(meta)
    if use_sing:
        td = tempfile.mkdtemp(prefix="a2k16-")
        spath = os.path.join(td, "sys.sing")
        write_singular(spath, eqs, gens, ["T*c-1"], char=char, order=order)
        sout = run_singular(spath, timeout=timeout)
        out.update(sout)
        out["sing_path"] = spath
        out["char"] = char
        out["order"] = order
        out["elapsed"] = time.time() - t0
        if sout.get("verdict") in ("SATURATED-EMPTY", "SURVIVES"):
            return out
        # fall through to sympy on Singular error/timeout if requested
    if use_sy and (backend == "sympy" or out.get("verdict") in (None, "ERROR", "TIMEOUT")):
        unk = B["params"] + [c]
        ring = unk + [T]
        try:
            with Alarm(timeout):
                Gb = sp.groebner(eqs + [T * c - 1], *ring, order="grevlex", field=True)
                empty, Gbl = _gb_empty(Gb)
                Gb0 = sp.groebner(eqs, *unk, order="grevlex", field=True)
                unsat_empty, Gbl0 = _gb_empty(Gb0)
                GbN = sp.groebner([c - 1, T * c - 1], *ring, order="grevlex", field=True)
                neg_empty, _ = _gb_empty(GbN)
        except Timeout:
            out.update(verdict="TIMEOUT", elapsed=time.time() - t0, backend="sympy")
            return out
        except Exception as e:
            out.update(verdict="ERROR", error="%s: %s" % (type(e).__name__, e),
                       elapsed=time.time() - t0, backend="sympy")
            return out
        verdict = "SATURATED-EMPTY" if empty else "SURVIVES"
        out.update(
            verdict=verdict, empty=empty, basis_size=len(Gbl),
            unsaturated_empty=unsat_empty, unsaturated_size=len(Gbl0),
            negative_nontrivial=(not neg_empty),
            family=None if empty else [str(t) for t in Gbl[:8]],
            elapsed=time.time() - t0, backend="sympy", order="grevlex",
        )
    if "verdict" not in out:
        out["verdict"] = "ERROR"
        out["elapsed"] = time.time() - t0
    return out


def newton_tight_drop_to_budget(n, m, M2, V2, k, budget=40):
    """Smallest drop_high such that Horner-cap unknowns <= budget.  0 if already."""
    info = []
    for dh in range(0, 20):
        B = build_horner_cap(n, m, M2, V2, k, max_unknowns=None, drop_high=dh)
        if not B.get("ok"):
            info.append((dh, None, B.get("reason")))
            continue
        nunk = B["n_unknowns"]
        info.append((dh, nunk, B.get("dropped")))
        if nunk <= budget:
            return dh, nunk, info
    return None, None, info
