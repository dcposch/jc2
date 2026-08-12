#!/usr/bin/env python3
"""RESIDUE.md companion: is R_{k,d2} a residue?  Exact Fraction arithmetic.

Tests (see RESIDUE.md for statements):
  T0  anchor: repo's binom_outer (general solve, then restrict) agrees with
      the direct binomial-locus solve used here (cells (2,2),(2,3),(3,3)).
  T1  (interp b1) Res_{y=-1/a2}[G/A^{k+2} dy] == (k+2)(-1)^k a2^{-2d2-1} R.
  T2  (interp b2) residue theorem: Res_{y0} == -Res_infty (independent
      Laurent-at-infinity computation).
  T3  (interp a) T3a Jac(P, x^k C) == x^k + x^{k+1} G;  T3b the E-part
      (AE'-(k+1)A'E)/A^{k+2} has residue 0 for arbitrary symbolic E
      (exactness => Res2 of dP^dQ/(x^{k+2}A^{k+2}) is E-independent);
      T3c the naive dP^dQ/P^{k+2} variant has TOTAL iterated residue 0.
  T4  (interp c) mu o L == 0 (moment functional kills im ad_{xA});
      left-null-space of L on the window is 2-dim = span{mu, top functional
      supported above deg G}  =>  obstruction <=> mu(G) = 0.
  T5  (uniform outer theorem) on the binomial locus, for each cell:
      G_n == 0 for n >= (k+1)d2;  extras t>=1 == 0;  extra_0 ==
      a2 (k+1)(d2-1) e_top;  and the closed form
      extra_0 == (-1)^(k+(k+1)(d2-1)) (k+2)/C((k+1)d2,k+1) a2^((k-1)d2) R.
      Cells include (4,4),(5,4),(2,5),(3,5): NEW, beyond the repo grid.
"""
import os, sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surplus_count import mono, pmul, ppow, padd_into, psubst
from surplus_ext import (V, ONE, pscale, padd, col_series, extra_value,
                         deriv_prod, wide_setup, binom_outer, mstr_p)

def cmb(n, r):
    return comb(n, r) if 0 <= r <= n else 0

def a2pow(e):
    return {mono({'a2': e}): F(1)}

def Rpoly(k, d2):
    """R_{k,d2} = sum_{j=k+2}^{2d2} (-1)^j C(j,k+2) a2^(2d2-j) b_j."""
    R = {}
    for j in range(max(k + 2, d2), 2 * d2 + 1):   # b_j exists only for j>=d2

        padd_into(R, mono({'a2': 2 * d2 - j, f'b{j}': 1}),
                  F((-1) ** j * comb(j, k + 2)))
    return R

def binom_C(k):
    """Exact solution of AC'-kA'C=1 on the binomial locus:
    C = ((1+a2 y)^k - 1)/(k a2) = sum_{i=1}^k C(k,i)/k a2^(i-1) y^i."""
    return {i: {mono({'a2': i - 1}): F(comb(k, i), k)} for i in range(1, k + 1)}

def Bpoly(d2):
    return {j: V(f'b{j}') for j in range(d2, 2 * d2 + 1)}

def res_S(H, p):
    """Res_{y=-1/a2}[H(y)/A^p dy], A = 1+a2y.  Returns (S, N) with
    Res = S * a2^(-(N+1)):  S = [w^(p-1)] sum_n H_n a2^(N-n) (w-1)^n."""
    N = max(H.keys())
    S = {}
    for n, hn in H.items():
        c = F(cmb(n, p - 1) * (-1) ** (n - p + 1))     # [w^(p-1)](w-1)^n
        if c:
            for m, cc in pmul(hn, a2pow(N - n)).items():
                padd_into(S, m, cc * c)
    return {m: c for m, c in S.items() if c}, N

def res_inf_S(H, p):
    """-[y^(-1)] of H/A^p expanded at infinity: (S', N) with
    Res_inf = S' * a2^(-(N+1)); independent path (binomial series)."""
    N = max(H.keys())
    S = {}
    for n, hn in H.items():
        t = n - p + 1                                   # y^(n-p-t) = y^-1
        if t < 0:
            continue
        c = F(-((-1) ** t) * cmb(p + t - 1, t))         # -C(-p,t)
        if c:
            # a2^(-p-t) * a2^... total a2 exponent -(n+1); scale to N
            for m, cc in pmul(hn, a2pow(N - n)).items():
                padd_into(S, m, cc * c)
    return {m: c for m, c in S.items() if c}, N

def direct_cell(k, d2):
    """Binomial-locus data: A=1+a2y, C exact, G, solved E, extras."""
    A0 = {0: ONE, 1: V('a2')}
    C = binom_C(k)
    # cross-check C against the series solver
    Cs = col_series(A0, k + 1, {}, 1, k * d2)
    Cs = {s: p for s, p in Cs.items() if p}
    assert Cs == C, f"C mismatch at {(k, d2)}"
    B = Bpoly(d2)
    G = deriv_prod(C, B, 2, -k, None)                   # 2BC' - kB'C
    E = col_series(A0, k + 2, G, d2 + 1, (k + 1) * d2)
    extras = [extra_value(A0, k + 2, G, E, (k + 1) * d2 + t)
              for t in range(d2 - 1)]
    return A0, B, C, G, E, extras

def t0_anchor():
    ok = True
    for (k, d2, azero) in [(2, 2, ['a3']), (2, 3, ['a3', 'a4']),
                           (3, 3, ['a3', 'a4'])]:
        rep = binom_outer(k, d2, azero)
        _, _, _, _, _, extras = direct_cell(k, d2)
        ok &= (rep == extras)
        print(f"T0 ({k},{d2}): general-solve|binomial == direct binomial "
              f"solve: {'OK' if rep == extras else 'FAIL'}")
    return ok

def t1_t2_residue(k, d2, G):
    R = Rpoly(k, d2)
    S, N = res_S(G, k + 2)
    # claim: S * a2^-(N+1) == (k+2)(-1)^k a2^(-2d2-1) R
    lhs = pmul(S, a2pow(2 * d2))
    rhs = pscale(pmul(a2pow(N), R), F((k + 2) * (-1) ** k))
    ok1 = (lhs == rhs)
    Si, Ni = res_inf_S(G, k + 2)
    ok2 = (pmul(S, a2pow(Ni)) == pscale(pmul(Si, a2pow(N)), F(-1)))
    print(f"T1 ({k},{d2}): Res_y0[G/A^(k+2)] == (k+2)(-1)^k a2^(-2d2-1) R:"
          f" {'OK' if ok1 else 'FAIL'} | T2 Res_y0 == -Res_inf:"
          f" {'OK' if ok2 else 'FAIL'}")
    return ok1 and ok2

def t3_groth(k, d2, A0, B, C, G):
    # T3a: AC' - kA'C == 1  (=> Jac(P, x^k C) = x^k + x^(k+1) G exactly,
    # G being by construction the x^(k+1)-column)
    dd = {n: p for n, p in deriv_prod(C, A0, 1, -k, None).items() if p}
    ok_a = (dd == {0: ONE})
    # T3b: arbitrary symbolic E-part has residue 0 (exactness)
    Esym = {m: V(f'e{m}') for m in range(d2 + 1, (k + 1) * d2 + 1)}
    LE = deriv_prod(Esym, A0, 1, -(k + 1), None)        # AE' - (k+1)A'E
    S_LE, _ = res_S(LE, k + 2)
    ok_b = (S_LE == {})
    # T3c: naive dP^dQ/P^(k+2): Res_x gives G/A^(k+2) - (k+2) B/A^(k+3);
    # total y-residue must vanish (the form is exact).
    S_G, N_G = res_S(G, k + 2)
    S_B, N_B = res_S(B, k + 3)
    tot = padd(pmul(S_G, a2pow(N_B)),
               pscale(pmul(S_B, a2pow(N_G)), F(-(k + 2))))
    tot = {m: c for m, c in tot.items() if c}
    ok_c = (tot == {})
    print(f"T3 ({k},{d2}): a) Jac identity {'OK' if ok_a else 'FAIL'}"
          f" | b) E-part residue 0 (any E): {'OK' if ok_b else 'FAIL'}"
          f" | c) dP^dQ/P^(k+2) residue == 0: {'OK' if ok_c else 'FAIL'}")
    return ok_a and ok_b and ok_c

def t4_koszul(k, d2, G):
    lo, hi = d2 + 1, (k + 1) * d2                       # E-support
    tlo, thi = d2, (k + 1) * d2 + 1                     # window
    # mu o L == 0: m C(m-1,k+1) == (m-k-1) C(m,k+1) for all m in source
    ok_mu = all(m * cmb(m - 1, k + 1) == (m - k - 1) * cmb(m, k + 1)
                for m in range(lo, hi + 1))
    # exact left null space at generic a2 = 3/7 (and 5/3 as guard)
    ok_rank = True
    for a2v in (F(3, 7), F(5, 3)):
        rows = list(range(tlo, thi + 1))
        cols = list(range(lo, hi + 1))
        M = [[F(0)] * len(cols) for _ in rows]          # M[n][m] = L coeff
        for jc, m in enumerate(cols):
            M[rows.index(m - 1)][jc] += m               # m y^(m-1)
            M[rows.index(m)][jc] += a2v * (m - k - 1)   # a2(m-k-1) y^m
        # left null space = null space of transpose
        A = [list(r) for r in map(list, zip(*M))]       # cols x rows
        nr, nc = len(A), len(A[0])
        piv = []
        r = 0
        for c in range(nc):
            pr = next((i for i in range(r, nr) if A[i][c]), None)
            if pr is None:
                continue
            A[r], A[pr] = A[pr], A[r]
            A[r] = [x / A[r][c] for x in A[r]]
            for i in range(nr):
                if i != r and A[i][c]:
                    A[i] = [x - A[i][c] * y for x, y in zip(A[i], A[r])]
            piv.append(c)
            r += 1
        free = [c for c in range(nc) if c not in piv]
        null = []
        for fc in free:
            v = [F(0)] * nc
            v[fc] = F(1)
            for i, pc in enumerate(piv):
                v[pc] = -A[i][fc]
            null.append(v)
        ok_rank &= (len(null) == 2)
        # mu in null space?
        mu = [F((-1) ** (n - k - 1) * cmb(n, k + 1)) * a2v ** (-(n + 1))
              for n in rows]
        for v in null:                                  # reduce mu by null
            pass
        # check mu satisfies mu.M == 0 directly
        okm = all(sum(mu[i] * M[i][jc] for i in range(len(rows))) == 0
                  for jc in range(len(cols)))
        ok_rank &= okm
        # second functional supported above deg G: eliminate to get a null
        # vector vanishing on all n <= degG
        degG = max(G.keys())
        span = [list(v) for v in null]
        # gaussian-eliminate span on coordinates n <= degG
        r = 0
        for i, n in enumerate(rows):
            if n > degG:
                continue
            pr = next((j for j in range(r, len(span)) if span[j][i]), None)
            if pr is None:
                continue
            span[r], span[pr] = span[pr], span[r]
            for j in range(len(span)):
                if j != r and span[j][i]:
                    fpiv = span[j][i] / span[r][i]
                    span[j] = [x - fpiv * y for x, y in zip(span[j], span[r])]
            r += 1
        # after elimination, vectors span[r:] vanish on n <= degG
        ok_rank &= (len(span) - r == 1)
    print(f"T4 ({k},{d2}): mu o L == 0: {'OK' if ok_mu else 'FAIL'}"
          f" | coker dim 2, mu in ann(im L), 2nd functional above deg G:"
          f" {'OK' if ok_rank else 'FAIL'}")
    return ok_mu and ok_rank

def t5_uniform(k, d2, G, E, extras):
    n0 = (k + 1) * d2
    ok_deg = all(n < n0 for n in G.keys())
    ok_hi = all(extras[t] == {} for t in range(1, d2 - 1))
    etop = E.get(n0, {})
    pred_e = pscale(pmul(a2pow(1), etop), F((k + 1) * (d2 - 1)))
    ok_e = (extras[0] == pred_e)
    sign = (-1) ** (k + (k + 1) * (d2 - 1))
    closed = pscale(pmul(a2pow((k - 1) * d2), Rpoly(k, d2)),
                    F(sign * (k + 2), comb(n0, k + 1)))
    ok_cf = (extras[0] == closed)
    print(f"T5 ({k},{d2}): deg G < (k+1)d2: {'OK' if ok_deg else 'FAIL'}"
          f" | extras t>=1 == 0: {'OK' if ok_hi else 'FAIL'}"
          f" | extra_0 == a2(k+1)(d2-1) e_top: {'OK' if ok_e else 'FAIL'}"
          f" | closed form (+/-)(k+2)/C({n0},{k + 1}) a2^{(k - 1) * d2} R:"
          f" {'OK' if ok_cf else 'FAIL'}")
    return ok_deg and ok_hi and ok_e and ok_cf

# ---------------------------------------------------------------------------
# `mathieu` mode — MATHIEU.md companion (run: python3 residue_check.py mathieu)
# Machine checks for the Mathieu-Zhao bridge and the rigidity theorem
#   Theorem A: A C' - w A' C = c (const != 0), w >= 1  =>  deg A <= 1.
# M1 rigidity dichotomy: inner extras of cell (k,d2) vanish at numeric A
#    iff deg A <= 1 (random / perfect-power / mixed A, exact Fractions).
# M2 bridge witness + linear form: y^((k+1)delta-1) not in Im(L_A) (properness
#    of the candidate Mathieu subspace), and L_A(C) = 1 inconsistent iff
#    deg A >= 2 (solvable control at deg A <= 1).
# M3 CT form: R_{k,d2} is the honest Laurent constant term
#    CT_w(beta'(w) w^-(k+1)) on the binomial locus (a2^{2d2} beta_{k+2}
#    == (-1)^k R); independently re-derives the max(k+2,d2) lower limit.
# M4 proof identities of Theorem A, symbolically: L_A(A^k) == 0 and the
#    leading-coefficient lemma lc(L_A(D)) = (deg D - k deg A) lc(A) lc(D).
# M5 per-cell tie (incl. OPEN cells (3,4),(4,4),(5,4),(2,5),(3,5),(2,6)):
#    symbolic inner extras vanish identically on the binomial locus; are
#    nonzero at perfect-power and random off-binomial points; symbolic and
#    numeric evaluation paths agree.
import random

def _num(c):
    c = F(c)
    return {(): c} if c else {}

def _ymul(P, Q):
    r = {}
    for i, p in P.items():
        for j, q in Q.items():
            r.setdefault(i + j, {})
            for m, c in pmul(p, q).items():
                padd_into(r[i + j], m, c)
    return {n: pp for n, pp in r.items() if pp}

def _ypow(P, e):
    r = {0: dict(ONE)}
    for _ in range(e):
        r = _ymul(r, P)
    return r

def _L(A, D, k):
    """L_A(D) = A D' - k A' D as a y-poly (dict n -> coefficient poly)."""
    return {n: p for n, p in deriv_prod(D, A, 1, -k, None).items() if p}

def _rand_A(delta, rng, kind):
    """Numeric A, exact degree delta, A(0)=1."""
    if delta == 0:
        return {0: dict(ONE)}
    if kind == 'power':                       # (1+uy)^delta
        u = F(rng.randint(1, 9), rng.randint(1, 9)) * rng.choice((1, -1))
        return {i: _num(F(comb(delta, i)) * u ** i) for i in range(delta + 1)}
    if kind == 'mixed':                       # (1+uy)^(delta-1) (1+vy)
        u = F(rng.randint(1, 9), rng.randint(1, 9))
        v = -F(rng.randint(1, 9), rng.randint(1, 9))
        P = _ypow({0: dict(ONE), 1: _num(u)}, delta - 1)
        return _ymul(P, {0: dict(ONE), 1: _num(v)})
    A = {0: dict(ONE)}
    for i in range(1, delta + 1):
        c = F(rng.randint(-9, 9), rng.randint(1, 9))
        if i == delta and c == 0:
            c = F(1)
        if c:
            A[i] = _num(c)
    return A

def _inner_extras(A, k, d2):
    C = col_series(A, k + 1, {}, 1, k * d2)
    return [extra_value(A, k + 1, {}, C, k * d2 + t) for t in range(d2 - 1)]

def m1_dichotomy(seed=11):
    rng = random.Random(seed)
    ok = True
    for k in range(1, 6):
        for d2 in range(2, 6):
            for delta in range(0, d2 + 1):
                for kind in ('random', 'power', 'mixed'):
                    if kind != 'random' and delta < 2:
                        continue
                    for _ in range(5 if kind == 'random' else 2):
                        A = _rand_A(delta, rng, kind)
                        ex = _inner_extras(A, k, d2)
                        vanish = all(e == {} for e in ex)
                        if vanish != (delta <= 1):
                            ok = False
                            print(f"  M1 FAIL k={k} d2={d2} delta={delta} "
                                  f"{kind}: vanish={vanish}")
    print(f"M1 rigidity dichotomy (extras==0 <=> deg A<=1), k=1..5, d2=2..5, "
          f"all deg A, random/power/mixed A: {'OK' if ok else 'FAIL'}")
    return ok

def _consistent(A, k, rhs, N):
    """Is L_A(C) = rhs solvable with C = c_0..c_N?  Exact Gaussian elim."""
    delta = max(A.keys())
    nr = N + delta + 1
    M = [[F(0)] * (N + 1) for _ in range(nr)]
    b = [F(0)] * nr
    for j in range(N + 1):
        for n, p in _L(A, {j: dict(ONE)}, k).items():
            M[n][j] = p.get((), F(0))
    for n, c in rhs.items():
        b[n] = c
    r = 0
    for c in range(N + 1):
        pr = next((i for i in range(r, nr) if M[i][c]), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        b[r], b[pr] = b[pr], b[r]
        inv = M[r][c]
        M[r] = [x / inv for x in M[r]]
        b[r] = b[r] / inv
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
                b[i] = b[i] - f * b[r]
        r += 1
    return all(b[i] == 0 for i in range(r, nr))

def m2_witness(seed=13):
    rng = random.Random(seed)
    ok = True
    for k in range(1, 5):
        for delta in range(1, 5):
            for kind in ('random', 'power'):
                if kind == 'power' and delta < 2:
                    continue
                A = _rand_A(delta, rng, kind)
                N = k * delta + 6
                # (a) properness witness: y^((k+1)delta - 1) never in Im(L_A)
                wit = {(k + 1) * delta - 1: F(1)}
                if _consistent(A, k, wit, N):
                    ok = False
                    print(f"  M2a FAIL k={k} delta={delta} {kind}")
                # (b) rigidity linear form: 1 in Im(L_A) iff delta <= 1
                sol = _consistent(A, k, {0: F(1)}, N)
                if sol != (delta <= 1):
                    ok = False
                    print(f"  M2b FAIL k={k} delta={delta} {kind}: {sol}")
    print(f"M2 bridge: y^((k+1)d-1) not in Im(L_A) (properness), and "
          f"1 in Im(L_A) <=> deg A<=1, k=1..4, deg A=1..4: "
          f"{'OK' if ok else 'FAIL'}")
    return ok

def m3_ct_form():
    ok = True
    for (k, d2) in [(2, 2), (2, 3), (2, 4), (3, 3), (4, 3), (3, 4), (5, 3),
                    (4, 4), (5, 4), (2, 5), (3, 5), (2, 6)]:
        # beta(w) = B((w-1)/a2); a2^{2d2} [w^{k+2}] beta == (-1)^k R_{k,d2}.
        T = {}
        for j in range(d2, 2 * d2 + 1):
            c = F(cmb(j, k + 2) * (-1) ** (j - k))
            if c:
                for m, cc in pmul(V(f'b{j}'), a2pow(2 * d2 - j)).items():
                    padd_into(T, m, cc * c)
        ok &= (T == pscale(Rpoly(k, d2), F((-1) ** k)))
    print(f"M3 CT form: a2^(2d2) beta_(k+2) == (-1)^k R (R is the Laurent "
          f"constant term CT_w(beta' w^-(k+1))), 12 cells: "
          f"{'OK' if ok else 'FAIL'}")
    return ok

def m4_proof_identities():
    ok = True
    for k in range(1, 5):
        for delta in range(1, 5):
            A = {0: dict(ONE)}
            for i in range(1, delta + 1):
                A[i] = V(f'a{i + 1}')
            # (a) kernel: L_A(A^k) == 0 symbolically
            if _L(A, _ypow(A, k), k) != {}:
                ok = False
                print(f"  M4a FAIL k={k} delta={delta}")
            # (b) leading-coefficient lemma on generic D
            for d in range(0, k * delta + 3):
                D = {j: V(f'd{j}') for j in range(d + 1)}
                LD = _L(A, D, k)
                top = delta + d - 1
                if any(n > top for n in LD):
                    ok = False
                    print(f"  M4b FAIL (overflow) k={k} delta={delta} d={d}")
                want = pscale(pmul(V(f'a{delta + 1}'), V(f'd{d}')),
                              F(d - k * delta))
                got = LD.get(top, {})
                if d != k * delta:
                    if got != want:
                        ok = False
                        print(f"  M4b FAIL k={k} delta={delta} d={d}")
                elif got != {}:
                    ok = False
                    print(f"  M4b FAIL (no cancel) k={k} delta={delta} d={d}")
    print(f"M4 Theorem A identities: L_A(A^k)==0 and "
          f"lc(L_A(D))==(deg D - k deg A) lc(A) lc(D), symbolic, k,deg A=1..4:"
          f" {'OK' if ok else 'FAIL'}")
    return ok

def _peval(p, env):
    tot = F(0)
    for m, c in p.items():
        v = c
        for var, e in m:
            v *= env[var] ** e
        tot += v
    return tot

def m5_cells(seed=17):
    rng = random.Random(seed)
    ok = True
    cells = [(2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 4),
             (2, 5), (3, 5), (2, 6)]
    for (k, d2) in cells:
        A = {0: dict(ONE)}
        for i in range(1, d2 + 1):
            A[i] = V(f'a{i + 1}')
        ex = _inner_extras(A, k, d2)
        # (i) binomial locus: extras vanish identically (symbolic)
        exb = ex
        for i in range(2, d2 + 1):
            exb = [psubst(e, f'a{i + 1}', {}) for e in exb]
        okb = all(e == {} for e in exb)
        # (ii) perfect-power points (the historically dangerous family)
        okp = True
        for delta in range(2, d2 + 1):
            for u in (F(1), F(-2), F(3, 7)):
                env = {f'a{i + 1}': F(comb(delta, i)) * u ** i if i <= delta
                       else F(0) for i in range(1, d2 + 1)}
                vals = [[_peval(e, env) for e in [x]][0] != 0 for x in ex]
                okp &= any(vals)
        # (iii) random off-binomial points
        okr = True
        for _ in range(20):
            env = {f'a{i + 1}': F(rng.randint(-9, 9), rng.randint(1, 9))
                   for i in range(1, d2 + 1)}
            if all(env[f'a{i + 1}'] == 0 for i in range(2, d2 + 1)):
                env[f'a{d2 + 1}'] = F(1)
            okr &= any(_peval(e, env) != 0 for e in ex)
        # (iv) symbolic vs numeric path agreement
        oka = True
        for _ in range(3):
            env = {f'a{i + 1}': F(rng.randint(-5, 5), rng.randint(1, 5))
                   for i in range(1, d2 + 1)}
            An = {0: dict(ONE)}
            for i in range(1, d2 + 1):
                if env[f'a{i + 1}']:
                    An[i] = _num(env[f'a{i + 1}'])
            exn = _inner_extras(An, k, d2)
            for e_s, e_n in zip(ex, exn):
                oka &= (_peval(e_s, env) == e_n.get((), F(0)))
        cok = okb and okp and okr and oka
        ok &= cok
        print(f"M5 ({k},{d2}): binomial extras==0: {'OK' if okb else 'FAIL'}"
              f" | perfect-power nonzero: {'OK' if okp else 'FAIL'}"
              f" | random off-binomial nonzero: {'OK' if okr else 'FAIL'}"
              f" | paths agree: {'OK' if oka else 'FAIL'}")
    return ok

def mathieu_main():
    allok = m1_dichotomy()
    allok &= m2_witness()
    allok &= m3_ct_form()
    allok &= m4_proof_identities()
    allok &= m5_cells()
    print("MATHIEU OK" if allok else "MATHIEU FAILURES PRESENT")
    return 0 if allok else 1

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mathieu":
        sys.exit(mathieu_main())
    allok = t0_anchor()
    cells = [(2, 2), (2, 3), (2, 4), (3, 3), (4, 3), (3, 4), (5, 3),
             (4, 4), (5, 4), (2, 5), (3, 5)]
    for (k, d2) in cells:
        A0, B, C, G, E, extras = direct_cell(k, d2)
        allok &= t1_t2_residue(k, d2, G)
        allok &= t3_groth(k, d2, A0, B, C, G)
        allok &= t4_koszul(k, d2, G)
        if d2 >= 2 and extras:
            allok &= t5_uniform(k, d2, G, E, extras)
    print("ALL OK" if allok else "FAILURES PRESENT")
    sys.exit(0 if allok else 1)
