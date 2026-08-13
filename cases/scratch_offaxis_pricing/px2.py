"""Priced off-axis chain/merge calculus for td=7 (exact rationals).

Pricing (AF2-derived from St 9.3 (24), corrected E6; SHEET6-AF2 §2):
every non-continuation root direction c* of the pattern at a searrow
vertex F climbs and prices lambda_F >= ceil(gap) with
gap(c*) = X_F/mult(c*) - kbar_F  (> 0 for NE roots: regularity-free),
0-root prices ceil(gap(0)/nu_F).  Budget: St 9.4 (25):
sum lambda <= td - 1 - psi over pairwise-distinct searrow vertices;
psi certified at the case-IV terminal by H3-psi with
R = deg p_G / d_F = 1/(1 - w_G)  (see doc P1), psi = ceil(R) - 1.
Terminal laws: w_t < 1 (R2.1 IV), M_t*(1-w_t) in N* (9.3(m)),
M_t >= 2 (MP2 trunk).
"""
from fractions import Fraction as Fr
from math import gcd, ceil
from itertools import product

def ceil_fr(x):
    return -((-x.numerator) // x.denominator)

def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return sorted(out)

BUDGET = 5          # td - 2 = 5 at td 7 (St 9.5); psi-sharpened per-terminal

_CS = {}
def chain_steps(w, M):
    """All one-step transitions from chain state (w, M):
    yields (w', M', lam, tag).  Complete at printed tier + R1.0:
    shapes are p = eps-power * (nu-orbit)^l * NE extras (R1.3 eps-extended),
    q = eta * simple orbits (R1.0).  Clean/neutral steps lam=0 handled
    separately (M-drop + resonance)."""
    if (w, M) in _CS:
        return _CS[(w, M)]
    out = []
    a, d = w.numerator, w.denominator
    # --- clean resonant (R1.2): lam = 0, w' = w*n/Delta
    for Delta in range(3, a + 1):
        if a % Delta:
            continue
        for nu in range(2, Delta):
            if (Delta - 1) % nu:
                continue
            n = (Delta - 1) // nu + 1
            if n < 2:
                continue
            dq = n * nu + 1
            if dq % d:
                continue                      # den(w) | dq
            for l in divisors(M):
                M2 = gcd(l, dq)               # M' = gcd(l*nu, n*nu+1)
                out.append((Fr(w * n, Delta), M2, 0, f'clean D{Delta}n{n}nu{nu}'))
    # --- M-drop via neutral step (n=1, cell (l*nu, nu+1)): w fixed, lam 0
    for l in divisors(M):
        for M2 in divisors(l):
            out.append((w, M2, 0, f'neutral-drop {M}->{M2}'))
    # (neutral with M2 = M always available: identity state)
    # --- pure (b): k=lex=Sm=0, 1<=eps<l: E = l-eps, nu free
    for l in divisors(M):
        if l < 2:
            continue
        for eps in range(1, l):
            E = l - eps
            # kbar = l*w*(nu+1)/E in Z for suitable nu (nu free); w'=lw/E
            w2 = Fr(l * w, E)
            lam = ceil_fr(Fr(l * w, eps))
            for M2 in divisors(E) if E > 1 else [1]:
                out.append((w2, M2, lam, f'pure-b l{l}e{eps}'))
    # --- dirty (a) / (b)-with-extras: finite Diophantine menu
    for l in divisors(M):
        if l < 2:
            continue
        for eps in range(0, l):
            for k in range(0, 7):
                if eps == 0 and k == 0:
                    continue                  # clean shape
                smin, smax = (k, k * (l - 1)) if k else (0, 0)
                for Sm in range(smin, smax + 1):
                    for lex in range(0, 41):
                        C = l * (k + lex) - Sm
                        if C <= 0:
                            continue          # pure-(b) already done
                        T = Sm + l - eps * (1 + k + lex)
                        if T <= 0:
                            continue          # dp <= eps*dq: excluded (R1.0/NE)
                        Emax = l * a * T      # d*E | l*a*T
                        if 2 * C > Emax:
                            break             # nu>=2 impossible; larger lex worse
                        for E in divisors(l * a * T):
                            nuq, rem = divmod(E - (l - eps), C)
                            if rem or nuq < 2:
                                continue
                            nu = nuq
                            dq = (1 + k + lex) * nu + 1
                            dp = eps + nu * (l + Sm)
                            assert l * dq - dp == E
                            kb = Fr(l * w * dq, E)
                            if kb.denominator != 1 or kb < 1:
                                continue
                            if eps and eps * dq >= dp:
                                continue      # 0-root must be NE (strict, R1.0)
                            X = kb * Fr(dp, dq)
                            # NE mults m_j >= 1, <= min(l-1,(dp-1)//dq), sum Sm
                            mm = min(l - 1, (dp - 1) // dq) if k else 0
                            if k and (mm < 1 or Sm > k * mm or Sm < k):
                                continue
                            lam = min_ne_lambda(X, kb, k, Sm, mm)
                            if lam is None:
                                continue
                            if eps:
                                g0 = Fr(X, eps) - kb
                                lam += max(1, ceil_fr(Fr(g0, nu)))
                            w2 = Fr(l * w * (dq - 1), nu * E)
                            M2 = gcd(dp, dq)
                            out.append((w2, M2, lam,
                                        f'st96 l{l}e{eps}k{k}S{Sm}x{lex}nu{nu}'
                                        f'({dp},{dq})'))
    _CS[(w, M)] = out
    return out

def min_ne_lambda(X, kb, k, Sm, mm):
    """min over partitions Sm = m_1+..+m_k (1<=m_j<=mm) of
    sum ceil(X/m_j - kb); gap > 0 guaranteed (NE)."""
    if k == 0:
        return 0
    best = None
    def rec(j, left, acc):
        nonlocal best
        if j == k:
            if left == 0:
                if best is None or acc < best:
                    best = acc
            return
        rem = k - j - 1
        for m in range(1, mm + 1):
            if left - m < rem or left - m > rem * mm:
                continue
            g = Fr(X, m) - kb
            if g <= 0:
                return None                   # impossible: NE => gap>0
            rec(j + 1, left - m, acc + max(1, ceil_fr(g)))
    rec(0, Sm, 0)
    return best

def close_states(seeds, budget=BUDGET, forbid_M1=False):
    """Dijkstra closure of chain states {(w,M): lam_min} from seeds."""
    import heapq
    dist = {}
    pq = [(lam, w, M) for ((w, M), lam) in seeds.items()]
    heapq.heapify(pq)
    while pq:
        lam, w, M = heapq.heappop(pq)
        if (w, M) in dist and dist[(w, M)] <= lam:
            continue
        dist[(w, M)] = lam
        for (w2, M2, dl, tag) in chain_steps(w, M):
            if forbid_M1 and M2 == 1:
                continue
            l2 = lam + dl
            if l2 > budget:
                continue
            if (w2, M2) not in dist or dist[(w2, M2)] > l2:
                heapq.heappush(pq, (l2, w2, M2))
    return dist

if __name__ == '__main__':
    # chain-2 priced alphabet from (3/2, M=2)
    st = close_states({(Fr(3, 2), 2): 0})
    print("chain-2 priced states (w, M) -> lambda_min:")
    for (w, M), lam in sorted(st.items(), key=lambda kv: (kv[1], kv[0][0])):
        print(f"  w={w} M={M} lam={lam}")
    print()
    print("one-step menu from (3/2, 2):")
    for t in sorted(set(chain_steps(Fr(3, 2), 2))):
        if t[2] > 0:
            print("  ", t)
