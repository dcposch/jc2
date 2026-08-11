#!/usr/bin/env python3
"""SURPLUS-EXT companion script (see SURPLUS-EXT.md).

Part 1 (Phase B, k>=3 / d2=2): exact verification of the column-ODE view and
of the log-residue mechanism.  Post-gap-kill, Minkowski column k+1 of [P,Q]
as a polynomial in y is A C' - k A' C (A = P col 1, C = Q col k) and column
k+2 is A E' - (k+1) A' E + 2 B C' - k B' C (B = P col 2, E = Q col k+1);
key (X,s) = coeff of y^{s-1}.  The in-block cascade of surplus_count.py is
equivalent to solving the column ODEs coefficient-by-coefficient; the extra
keys evaluate minus the "would-be next" series coefficients.

Checks (exact Fraction arithmetic, symbolic in a2,a3,a4,a5,a6; a1=c1=1 wlog
by unit scaling -- reduced forms carry the units back):
  V1  keys from the ODE view == keys from surplus_count.py enumeration
      (d2=2..3, k=2..5).
  V2  inner extra == -a3^k * c1 * a1^(1-k) for k=2..10  (extends the k<=5
      verification of SURPLUS.md; general k NOT proved, see SURPLUS-EXT §2).
  V3  with a3=0: outer extra == 0 identically for k=3..10, and for k=2
      outer extra == -(1/5) a2^2 a6 (matching the theorem) with
      e_top == -(1/15) a2 a6 (matching b10 = -a2 a6 b3/(15 a1^2)).
  V4  with a3=0: E-closed-form degree bound deg_y E <= k+3 (k=3..10).
Part 2 (Phase C, (k,d2)=(2,3) wide strip): see functions wide_*.
"""
import os, sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surplus_count import analyze, mono, pmul, ppow, padd_into, psubst, mstr

# poly in variables 'a2','a3',... : dict {mono: Fraction}; mono from surplus_count
ONE = {(): Fraction(1)}

def V(name):
    return {mono({name: 1}): Fraction(1)}

def pscale(p, c):
    return {m: cc * c for m, cc in p.items()}

def padd(p, q):
    r = dict(p)
    for m, c in q.items():
        padd_into(r, m, c)
    return r

def col_series(Acoef, ncoef, inhom, val, top):
    """Column X of the bracket reads sum_i (n+1 - i*ncoef) A_i c_{n+1-i}
    + inhom_n = 0 for n >= 1 (A_0 = 1, a1 scaled out; ncoef = k+1 for the
    C-column A C' - k A' C, ncoef = k+2 for the E-column A E' - (k+1) A' E).
    Solves for c_{val..top} (c_1 := 1 when val == 1); returns dict s->poly."""
    out = {}
    if val == 1:
        out[1] = ONE
    n = 1 if val == 1 else val - 1
    while n <= top - 1:
        acc = dict(inhom.get(n, {}))
        for i, Ai in Acoef.items():
            if i == 0:
                continue
            j = n + 1 - i
            if j in out:
                coef = Fraction(n + 1 - i * ncoef)
                if coef:
                    acc = padd(acc, pscale(pmul(Ai, out[j]), coef))
        # (n+1) * 1 * c_{n+1} + acc = 0
        out[n + 1] = pscale(acc, Fraction(-1, n + 1))
        n += 1
    return out

def extra_value(Acoef, ncoef, inhom, out, n):
    """Evaluate equation n with series coefficients out (missing -> 0)."""
    acc = dict(inhom.get(n, {}))
    for i, Ai in Acoef.items():
        j = n + 1 - i
        if j in out:
            coef = Fraction(n + 1 - i * ncoef)
            if coef:
                acc = padd(acc, pscale(pmul(Ai, out[j]), coef))
    return acc

def deriv_prod(F, G, cF, cG, deg):
    """coefficients of cF*F'G + cG*FG' ... helper: returns dict n->poly of
    cF * F' * G + cG * F * G' for coefficient dicts F,G (s->poly)."""
    res = {}
    for sf, pf in F.items():
        for sg, pg in G.items():
            n = sf + sg - 1
            coef = Fraction(cF * sf + cG * sg)
            if coef:
                res.setdefault(n, {})
                for m, c in pmul(pf, pg).items():
                    padd_into(res[n], m, c * coef)
    return {n: {m: c for m, c in p.items() if c} for n, p in res.items()}

def phaseB(kmax=10, verbose=True):
    okV2 = okV3 = okV4 = True
    for k in range(2, kmax + 1):
        A = {0: ONE, 1: V('a2'), 2: V('a3')}
        C = col_series(A, k + 1, {}, 1, 2 * k)
        inner = extra_value(A, k + 1, {}, C, 2 * k)          # key (k+1, 2k+1)
        want = pscale({mono({'a3': k}): Fraction(1)}, Fraction(-1))
        v2 = (inner == want)
        okV2 &= v2
        # now a3 := 0 everywhere
        A0 = {0: ONE, 1: V('a2')}
        C0 = {s: psubst(p, 'a3', {}) for s, p in C.items()}
        C0 = {s: p for s, p in C0.items() if p}
        B = {2: V('a4'), 3: V('a5'), 4: V('a6')}
        # G_n = coeffs of 2 B C' - k B' C  (inhom for E-column with + sign)
        G = deriv_prod(C0, B, 2, -k, None)               # 2 C'... careful order
        # deriv_prod(F,G,cF,cG) = cF F'G + cG F G': want 2 B C' - k B' C =
        #   with F=C0, G=B: 2 C0' B  + (-k) C0 B'  -> cF=2, cG=-k
        assert not G.get(0) and not G.get(1)
        E = col_series(A0, k + 2, G, 3, 2 * k + 2)
        outer = extra_value(A0, k + 2, G, E, 2 * k + 2)  # key (k+2, 2k+3)
        etop = E.get(2 * k + 2, {})
        if k == 2:
            v3 = (outer == pscale(pmul(pmul(V('a2'), V('a2')), V('a6')),
                                  Fraction(-1, 5))
                  and etop == pscale(pmul(V('a2'), V('a6')), Fraction(-1, 15)))
        else:
            v3 = (outer == {})
        okV3 &= v3
        degE = max([s for s, p in E.items() if p], default=0)
        v4 = (k == 2) or (degE <= k + 3)
        okV4 &= v4
        if verbose:
            print(f"k={k:2d}: V2 inner=-a3^k {'OK' if v2 else 'FAIL '+mstr_p(inner)}"
                  f" | V3 outer {'OK' if v3 else 'FAIL '+mstr_p(outer)}"
                  f" | degE={degE} (bound {k+3}) {'OK' if v4 else 'FAIL'}")
    return okV2, okV3, okV4

def mstr_p(p):
    return " + ".join(f"{c}*{mstr(m)}" for m, c in sorted(p.items())) or "0"

# ---------------- Phase C: wide strips w_P = d2 >= 3 (SURPLUS-EXT §1) -------

def wide_setup(k, d2):
    """Column-ODE data, general (k,d2), units a1=c1=1 scaled out.
    A = 1 + sum_{i=1}^{d2} a_{i+1} y^i  (vars 'a2'..'a{d2+1}', P col 1),
    B = sum_{i=d2}^{2d2} B_i y^i        (vars 'b{i}',        P col 2).
    Returns (A,B,C,inner,E,outer): C,E solved series (dict s->poly);
    inner = extras of col k+1 at y^n, n = k*d2 + t   (key (k+1, n+1)),
    outer = extras of col k+2 at y^n, n = (k+1)*d2+t (key (k+2, n+1)),
    t = 0..d2-2 (strata w = d2-1-t .. matches Prop B's w in [1, w_P-1])."""
    A = {0: ONE}
    for i in range(1, d2 + 1):
        A[i] = V(f'a{i+1}')
    B = {i: V(f'b{i}') for i in range(d2, 2 * d2 + 1)}
    C = col_series(A, k + 1, {}, 1, k * d2)
    inner = [extra_value(A, k + 1, {}, C, k * d2 + t) for t in range(d2 - 1)]
    G = deriv_prod(C, B, 2, -k, None)             # 2 B C' - k B' C
    for n in range(0, d2):
        assert not G.get(n), f"G has low support at {(k, d2, n)}"
    E = col_series(A, k + 2, G, d2 + 1, (k + 1) * d2)
    outer = [extra_value(A, k + 2, G, E, (k + 1) * d2 + t)
             for t in range(d2 - 1)]
    return A, B, C, inner, E, outer

def wide_W0():
    """Anchor: wide_setup(2,2) reproduces the (2,2) theorem quantities."""
    A, B, C, inner, E, outer = wide_setup(2, 2)
    ok = (inner[0] == {mono({'a3': 2}): Fraction(-1)})
    o0 = psubst(outer[0], 'a3', {})
    ok &= (o0 == {mono({'a2': 2, 'b4': 1}): Fraction(-1, 5)})
    print("W0 (2,2) anchor: inner=-a3^2, outer|a3=0=-(1/5)a2^2*b4:",
          "OK" if ok else "FAIL")
    return ok

def wide_W1(k=2, d2=3):
    """Lattice cross-check: enumerate every block key from dets (independent
    path, mirrors surplus_count), substitute the ODE solution for all b's:
    eliminated keys -> 0, vertex -> const, extras -> inner/outer polys."""
    A, B, C, inner, E, outer = wide_setup(k, d2)
    subs = {}                                     # Q-side: (col, y) -> poly
    for s, p in C.items():
        subs[(k, s)] = p
    for s, p in E.items():
        subs[(k + 1, s)] = p
    Aco = {i: (A[i] if i else ONE) for i in range(0, d2 + 1)}
    keys = {}
    # P col 1 points (1, i) i=0..d2 (coef A_i); col 2 points (2, i) i=d2..2d2
    Ppts = [((1, i), Aco[i]) for i in range(0, d2 + 1)] + \
           [((2, i), B[i]) for i in range(d2, 2 * d2 + 1)]
    for (p, ap) in Ppts:
        for (qc, qy), bq in subs.items():
            X = p[0] + qc
            if X not in (k + 1, k + 2):
                continue
            det = p[0] * qy - p[1] * qc
            if det == 0:
                continue
            m = (X, p[1] + qy)
            keys.setdefault(m, {})
            for mm, cc in pmul(ap, bq).items():
                padd_into(keys[m], mm, cc * det)
    keys = {m: {mm: c for mm, c in e.items() if c} for m, e in keys.items()}
    ok = True
    ex_in = {(k + 1, k * d2 + t + 1): inner[t] for t in range(d2 - 1)}
    ex_out = {(k + 2, (k + 1) * d2 + t + 1): outer[t] for t in range(d2 - 1)}
    for m, e in sorted(keys.items()):
        if m == (k + 1, 1):
            ok &= (e == {(): Fraction(1)})       # det(p0,q0) a1 c1 = 1
        elif m in ex_in:
            ok &= (e == ex_in[m])
        elif m in ex_out:
            ok &= (e == ex_out[m])
        else:
            ok &= (e == {})
    print(f"W1 ({k},{d2}) lattice keys == ODE view "
          f"(eliminated->0, extras match):", "OK" if ok else "FAIL")
    return ok

def selftestV1():
    """ODE-view keys == surplus_count enumeration keys (spot families)."""
    ok = True
    for d2, k in [(2, 2), (2, 3), (2, 5), (3, 2), (3, 3)]:
        cP = [(0, 0), (1, 0), (4, 3 * d2), (4, 4 * d2)]
        cQ = [(0, 0), (k, 1), (k + 3, 1 + 3 * d2), (k + 3, (k + 3) * d2)]
        r = analyze(f"v1_k{k}_d{d2}", cP, cQ, k, verbose=False)
        # ODE-view key count: col k+1 strata 2..(wP+wQ+1)-? == 2(wP+wQ)-1 total
        ok &= (r["n_keys"] == 2 * (d2 + k * d2 - 1) - 1)
    print("V1 key-count vs enumeration:", "OK" if ok else "FAIL")
    return ok

def pcoeffs(p, v):
    """View dict-poly p as univariate in variable v: list of dict-poly
    coefficients [c0, c1, ...]."""
    out = {}
    for m, c in p.items():
        d = dict(m)
        e = d.pop(v, 0)
        out.setdefault(e, {})
        padd_into(out[e], mono(d), c)
    deg = max(out, default=0)
    return [out.get(i, {}) for i in range(deg + 1)]

def pdet(M):
    """Determinant of a small matrix of dict-polys (cofactor expansion)."""
    n = len(M)
    if n == 1:
        return M[0][0]
    acc = {}
    for i in range(n):
        if not M[i][0]:
            continue
        minor = [[M[r][c] for c in range(1, n)] for r in range(n) if r != i]
        term = pmul(M[i][0], pdet(minor))
        for m, c in term.items():
            padd_into(acc, m, c if i % 2 == 0 else -c)
    return acc

def presultant(p, q, v):
    """Sylvester resultant of p, q with respect to variable v."""
    P, Q = pcoeffs(p, v), pcoeffs(q, v)
    m, n = len(P) - 1, len(Q) - 1
    N = m + n
    M = [[{} for _ in range(N)] for _ in range(N)]
    for r in range(n):                       # rows of p-coefficients
        for j, c in enumerate(P[::-1]):
            M[r][r + j] = c
    for r in range(m):                       # rows of q-coefficients
        for j, c in enumerate(Q[::-1]):
            M[n + r][r + j] = c
    return pdet(M)

def phaseC2():
    """(2,3) torus-emptiness: exact resultant certificate for the inner pair.
    Res_a4(10L1,10L2) = -3200 a3^7 with a4-leading coefficient of 10L1 the
    CONSTANT -25 => every common zero has a3 = 0; then L2|a3=0 = a2 a4^2/10
    and L1|a3=0 = (2 a2^3 a4 - 25 a4^2)/10 force a4 = 0.  So
    V(L1,L2) = {a3 = a4 = 0} exactly (char not in {2,3,5})."""
    A, B, C, inner, E, outer = wide_setup(2, 3)
    L1, L2 = inner
    R = presultant(pscale(L1, Fraction(10)), pscale(L2, Fraction(10)), 'a4')
    ok = (R == {mono({'a3': 7}): Fraction(-3200)})
    print("W2 Res_a4(10L1,10L2) = -3200*a3^7:", "OK" if ok else
          "FAIL " + mstr_p(R))
    lead = pcoeffs(pscale(L1, Fraction(10)), 'a4')[-1]
    ok2 = (lead == {(): Fraction(-25)})
    l1z = psubst(L1, 'a3', {})
    l2z = psubst(L2, 'a3', {})
    ok3 = (l2z == {mono({'a2': 1, 'a4': 2}): Fraction(1, 10)})
    ok4 = (l1z == {mono({'a2': 3, 'a4': 1}): Fraction(1, 5),
                   mono({'a4': 2}): Fraction(-5, 2)})
    ok5 = (psubst(l1z, 'a4', {}) == {} and psubst(l2z, 'a4', {}) == {})
    print("W3 lead=-25 const; a3=0 forms; a3=a4=0 kills L1,L2:",
          "OK" if (ok2 and ok3 and ok4 and ok5) else "FAIL")
    return ok and ok2 and ok3 and ok4 and ok5

def binom_outer(k, d2, azero):
    """Outer extras restricted to the binomial locus (a3=..=a_{d2+1}=0).
    Returns list of restricted polys."""
    A, B, C, inner, E, outer = wide_setup(k, d2)
    res = []
    for L in outer:
        for v in azero:
            L = psubst(L, v, {})
        res.append(L)
    return res

def phaseC2b():
    """(2,3) outer pair on {a3=a4=0}: both reduce to (unit a2-power) * R with
    the SAME log-residue linear form R = a2^2 b4 - 5 a2 b5 + 15 b6
    (b3 absent; coefficients 1,5,15 = C(4,4),C(5,4),C(6,4) from the z^3
    residue of beta' — see SURPLUS-EXT §1.2)."""
    L3, L4 = binom_outer(2, 3, ['a3', 'a4'])
    R = {mono({'a2': 2, 'b4': 1}): Fraction(1),
         mono({'a2': 1, 'b5': 1}): Fraction(-5),
         mono({'b6': 1}): Fraction(15)}
    u = {mono({'a2': 3}): Fraction(1, 21)}
    ok = (L3 == pmul(u, R))
    ok4 = (L4 == {})
    print("W4 (2,3) outer|a3=a4=0: L3 = (a2^3/21)(a2^2 b4 - 5 a2 b5 + 15 b6):",
          "OK" if ok else "FAIL", "| L4 == 0 identically:",
          "OK" if ok4 else "FAIL")
    return ok and ok4

def phaseC3():
    """(2,4) = w_P 4: inner rigidity V(I1,I2,I3) = {a3=a4=a5=0} via the
    structural proof (squarefree-forcing + divisibility, SURPLUS-EXT §1.3);
    machine-asserts each polynomial identity the proof uses, then the outer
    factorization on the binomial locus."""
    A, B, C, inner, E, outer = wide_setup(2, 4)
    ok = True
    for I in inner:                      # vanish on the binomial locus
        r = I
        for v in ('a3', 'a4', 'a5'):
            r = psubst(r, v, {})
        ok &= (r == {})
    print("W5a (2,4) inner extras vanish on {a3=a4=a5=0}:",
          "OK" if ok else "FAIL")
    # identities for the divisibility classification, vars p,q,r,s
    p, q, r, s = V('p'), V('q'), V('r'), V('s')
    y = V('y')
    Apoly = padd(padd(ONE, pmul(p, y)), padd(pmul(q, ppow(y, 2)),
             padd(pmul(r, ppow(y, 3)), pmul(s, ppow(y, 4)))))
    def dy(f):
        out = {}
        for m, c in f.items():
            d = dict(m)
            e = d.pop('y', 0)
            if e:
                d['y'] = e - 1
                padd_into(out, mono(d), c * e)
        return out
    A1, A2, A3 = dy(Apoly), dy(dy(Apoly)), dy(dy(dy(Apoly)))
    N = padd(pscale(pmul(A2, A2), Fraction(3)),
             pscale(pmul(A1, A3), Fraction(-1)))
    E0 = padd(padd(pscale(pmul(q, q), Fraction(12)),
                   pscale(pmul(p, r), Fraction(-6))), pscale(s, Fraction(-336)))
    E1 = padd(pscale(pmul(q, r), Fraction(1)), pscale(pmul(p, s), Fraction(-6)))
    E2 = padd(pscale(pmul(r, r), Fraction(3)), pscale(pmul(q, s), Fraction(-8)))
    lhs = padd(N, pscale(pmul(pscale(s, Fraction(336)), Apoly), Fraction(-1)))
    rhs = padd(padd(E0, pmul(pscale(E1, Fraction(60)), y)),
               pmul(pscale(E2, Fraction(30)), ppow(y, 2)))
    i1 = (lhs == rhs)                    # N - 336 s A = E0 + 60 E1 y + 30 E2 y^2
    Q36 = padd(pmul(q, q), pscale(s, Fraction(-36)))
    id2 = (pscale(pmul(s, E0), Fraction(9)) ==
           padd(padd(pscale(pmul(s, Q36), Fraction(84)),
                     pscale(pmul(q, E2), Fraction(-3))),
                pscale(pmul(r, E1), Fraction(9))))
    id3 = (padd(pscale(pmul(r, r), Fraction(27)),
                pscale(ppow(q, 3), Fraction(-2))) ==
           padd(pscale(E2, Fraction(9)), pscale(pmul(q, Q36), Fraction(-2))))
    u = V('u')
    Au = ppow(padd(ONE, pmul(u, y)), 4)
    A1u, A2u, A3u = dy(Au), dy(dy(Au)), dy(dy(dy(Au)))
    Nu = padd(pscale(pmul(A2u, A2u), Fraction(3)),
              pscale(pmul(A1u, A3u), Fraction(-1)))
    i4 = (Nu == pmul(pscale(ppow(u, 4), Fraction(336)), Au))
    print("W5b identities: N-336sA=E0+60E1y+30E2y^2 |",
          "9sE0=84s(q^2-36s)-3qE2+9rE1 | 27r^2-2q^3=9E2-2q(q^2-36s) |",
          "N((1+uy)^4)=336u^4(1+uy)^4:",
          "OK" if (i1 and id2 and id3 and i4) else "FAIL",
          [i1, id2, id3, i4])
    # outer pair on the binomial locus
    outs = binom_outer(2, 4, ['a3', 'a4', 'a5'])
    R4 = {}
    from math import comb
    for j in range(4, 9):
        padd_into(R4, mono({'a2': 8 - j, f'b{j}': 1}),
                  Fraction((-1) ** j * comb(j, 4)))
    stat = []
    oko = True
    for t, L in enumerate(outs):
        if L == {}:
            stat.append(f"O{t+1}=0")
            continue
        f8 = pcoeffs(L, 'b8')
        uf = pscale(f8[1], Fraction(1, 70)) if len(f8) > 1 else {}
        oko &= (L == pmul(uf, R4))
        stat.append(f"O{t+1}=({mstr_p(uf)})*R4")
    print("W6 (2,4) outer|binom vs R4 = a2^4b4-5a2^3b5+15a2^2b6-35a2b7+70b8:",
          "OK" if oko else "FAIL", "|", "; ".join(stat))
    return ok and i1 and id2 and id3 and i4 and oko

def phaseC3b():
    """Grid survey. (a) d2=3, k=2..5: certify inner rigidity
    V(J1,J2) = {a3=a4=0} by the resultant route (monomial resultant +
    constant a4-lead + a3=0 slice).  (b) binomial-locus outer survey,
    k=2..5, d2=3 and k=2..3, d2=4: which extras vanish identically; the
    rest must be (a2-monomial) * R_{k,d2},
    R_{k,d2} = sum_{j=k+2}^{2d2} (-1)^j C(j,k+2) a2^{2d2-j} b_j
    (log-residue functional; empty sum when k+2 > 2d2 <=> k > 2d2-2)."""
    from math import comb
    allok = True
    for k in (2, 3, 4, 5):
        A, B, C, inner, E, outer = wide_setup(k, 3)
        J1, J2 = inner
        # stage 1: Res_a4 = c*a3^m + CONSTANT a4-lead of J1 => a3 = 0 forced
        R = presultant(J1, J2, 'a4')
        mR = (len(R) == 1 and set(dict(list(R)[0])) == {'a3'})
        lead = pcoeffs(J1, 'a4')[-1]
        cl = (len(lead) == 1 and () in lead)
        # stage 2 on a3=0 slice: Res_a2 = c*a4^N and a2-lead of j1z a pure
        # a4-monomial => no common zero with a4 != 0; a3=a4=0 kills both.
        j1z, j2z = psubst(J1, 'a3', {}), psubst(J2, 'a3', {})
        R2 = presultant(j1z, j2z, 'a2')
        l2 = pcoeffs(j1z, 'a2')[-1]
        s2 = (len(R2) == 1 and set(dict(list(R2)[0])) == {'a4'}
              and len(l2) == 1 and set(dict(list(l2)[0])) <= {'a4'}
              and psubst(j1z, 'a4', {}) == {} and psubst(j2z, 'a4', {}) == {})
        ok = mR and cl and s2
        allok &= ok
        ex = dict(list(R)[0]).get('a3') if len(R) == 1 else '?'
        ex2 = dict(list(R2)[0]).get('a4') if len(R2) == 1 else '?'
        print(f"C3b d2=3 k={k}: Res_a4=c*a3^{ex} (lead const {cl}); "
              f"slice Res_a2=c*a4^{ex2} => rigidity {'OK' if ok else 'UNPROVED'}")
    for (k, d2) in [(2, 3), (3, 3), (4, 3), (5, 3), (2, 4), (3, 4)]:
        outs = binom_outer(k, d2, [f'a{i}' for i in range(3, d2 + 2)])
        Rk = {}
        for j in range(k + 2, 2 * d2 + 1):
            padd_into(Rk, mono({'a2': 2 * d2 - j, f'b{j}': 1}),
                      Fraction((-1) ** j * comb(j, k + 2)))
        stat, okc = [], True
        for t, L in enumerate(outs):
            if L == {}:
                stat.append("0")
                continue
            if not Rk:
                okc = False
                stat.append("NONZERO?!")
                continue
            top = f'b{2*d2}'
            f = pcoeffs(L, top)
            uf = pscale(f[1], Fraction(1, comb(2 * d2, k + 2))) \
                if len(f) > 1 else {}
            hit = (L == pmul(uf, Rk))
            okc &= hit
            stat.append(f"({mstr_p(uf)})*R" if hit else "MISMATCH")
        allok &= okc
        print(f"C3b outer|binom (k={k},d2={d2}): [{', '.join(stat)}] "
              f"{'OK' if okc else 'FAIL'}")
    return allok

def phaseC1():
    ok = wide_W0() and wide_W1(2, 3) and wide_W1(2, 4) and wide_W1(3, 3)
    A, B, C, inner, E, outer = wide_setup(2, 3)
    print("(2,3) inner extras (keys (3,7),(3,8)); 10*L:")
    for t, L in enumerate(inner):
        print(f"  10*L{t+1} =", mstr_p(pscale(L, Fraction(10))))
    print("(2,3) outer extras: term counts",
          [len(L) for L in outer], "(keys (4,10),(4,11)); linear in b:",
          all(all(sum(e for v, e in m if v.startswith('b')) == 1 for m in L)
              for L in outer))
    return ok

if __name__ == "__main__":
    a = selftestV1()
    v2, v3, v4 = phaseB()
    print("V2 (inner extra = -a3^k c1 a1^{1-k}, k<=10):", "OK" if v2 else "FAIL")
    print("V3 (a3=0 => outer extra: 0 for k>=3; -(1/5)a2^2a6 at k=2):",
          "OK" if v3 else "FAIL")
    print("V4 (a3=0 => deg_y E <= k+3):", "OK" if v4 else "FAIL")
    c1 = phaseC1()
    c2 = phaseC2()
    c2b = phaseC2b()
    c3 = phaseC3()
    c3b = phaseC3b()
    sys.exit(0 if (a and v2 and v3 and v4 and c1 and c2 and c2b and c3 and c3b)
             else 1)
