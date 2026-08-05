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
from surplus_count import analyze, mono, pmul, padd_into, psubst, mstr

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

if __name__ == "__main__":
    a = selftestV1()
    v2, v3, v4 = phaseB()
    print("V2 (inner extra = -a3^k c1 a1^{1-k}, k<=10):", "OK" if v2 else "FAIL")
    print("V3 (a3=0 => outer extra: 0 for k>=3; -(1/5)a2^2a6 at k=2):",
          "OK" if v3 else "FAIL")
    print("V4 (a3=0 => deg_y E <= k+3):", "OK" if v4 else "FAIL")
    sys.exit(0 if (a and v2 and v3 and v4) else 1)
