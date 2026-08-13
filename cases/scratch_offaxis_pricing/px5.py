"""DEFINITIVE priced adjudication of the td=7 off-axis panel (exact).
Complete arrangement classification (hand-proved, doc section 10 P3):
  A. equal-(1,2) non-0 join, kbar free: nu_G>=2 cells = {(6,10) M2} exactly;
     nu_G=1 cells = the (2,2t) M2 tail (t>=2), incl. 0-slot case-I variants.
     lam_pre = 3 (epsilon-step or doubling+clean to w=2).
  B. chain-2 at 0, mu0=1, case III (nu_G>=2): nu2*w2 = 2; cells = {(3,9) M3}
     exactly ((3,5) is M1, MP2-dead).  lam_pre = min over states = 2 (w2=2/3).
  C. chain-2 at 0, mu0>=2, case III (nu_G>=2): kbar = (mu0*nu2*w2-2)/(mu0-1)
     pinned; cells dp = mu0+nu_G, dq = kbar*dp/(kbar-2); FINITE via
     nu_G | (mu0 + c - 1), c = dq-dp; kbar <= 4mu0+2 bounds nu2.
  Chain-1 at 0: dead (needs w2 = 2nu1 >= 4 > max state).  Unequal-mu non-0:
  dead (needs w2 > 2).  Root merge: dead (chain-1 w = 2 >= 1, R2.1(IV)).
Arrival law (St 8.4 + R1.1 neutral cells): (mu, nu) legal from state (w,M)
iff mu | M and (nu == -1 mod mu  [neutral vertex, M' = gcd(l, nu+1)]
or (nu, Mc) a direct step-cell realization with mu | Mc
or entry (nu=3, mu | 2)).
Budget: sum lam <= 6 - psi, psi = ceil(M_t/j)-1, j = M_t(1-w_t) in N*,
w_t < 1, M_t >= 2 at the terminal (P1).
"""
from fractions import Fraction as Fr
from math import gcd
import heapq
from px2 import chain_steps, ceil_fr, min_ne_lambda
from math import gcd

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

NCAP = 400          # per-step nu cap in tail inversion (rider; report hits)
SEEN_BOUNDARY = []

def lam0_steps(w, M):
    """clean/neutral (lam=0) steps only -- cheap, for budget-exhausted states"""
    out = []
    a, d = w.numerator, w.denominator
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
                continue
            for l in divisors(M):
                out.append((Fr(w * n, Delta), gcd(l, dq), 0,
                            f'clean D{Delta}n{n}nu{nu}'))
    for M2 in divisors(M):
        out.append((w, M2, 0, f'neutral-drop {M}->{M2}'))
    return out

def close_with_cells(seed_w, seed_M, budget=5, forbid_M1=False):
    """states (w,M) -> (lam_min, set of direct-cell (nu, M) realizations)"""
    dist, cells = {}, {}
    pq = [(0, seed_w, seed_M)]
    while pq:
        lam, w, M = heapq.heappop(pq)
        if (w, M) in dist and dist[(w, M)] <= lam:
            continue
        dist[(w, M)] = lam
        # sound pruning: at lam == budget any lam>=1 step overruns
        # (total > budget = td-2 >= 6-psi for every terminal psi >= 1)
        steps = lam0_steps(w, M) if lam >= budget else chain_steps(w, M)
        for (w2, M2, dl, tag) in steps:
            if forbid_M1 and M2 == 1:
                continue
            l2 = lam + dl
            if l2 > budget:
                continue
            if tag.startswith(('st96', 'clean')):
                nu_cell = int(tag.split('nu')[-1].split('(')[0])
                # vertex realization (any <=budget path): arrival superset
                cells.setdefault((w2, M2), set()).add((nu_cell, M2))
            if (w2, M2) not in dist or dist[(w2, M2)] > l2:
                heapq.heappush(pq, (l2, w2, M2))
    return dist, cells

def terminal_psi(w, M):
    if w >= 1 or w <= 0 or M < 2:
        return None
    j = M * (1 - w)
    if j.denominator != 1 or j < 1:
        return None
    return ceil_fr(Fr(M, int(j))) - 1

TRUNKS = {}
def trunk_routes(w0, M0, bleft):
    """all (lam_trunk, psi, w_t, M_t) reachable within bleft; memoized."""
    if M0 < 2 or bleft < 0:
        return []
    key = (w0, M0, bleft)
    if key in TRUNKS:
        return TRUNKS[key]
    dist, _ = close_with_cells(w0, M0, budget=bleft, forbid_M1=True)
    out = []
    for (w, M), lam in dist.items():
        p = terminal_psi(w, M)
        if p is not None:
            out.append((lam, p, w, M))
    TRUNKS[key] = sorted(out)
    return TRUNKS[key]

def feasible(lam_pre, w_tr, M_G, ctx, out):
    """record all budget-fitting completions; lam_trunk <= 5 - lam_pre
    (psi >= 1 makes 6-psi <= 5, so total <= 5 is necessary)."""
    for (lt, psi, wt, Mt) in trunk_routes(w_tr, M_G, max(0, 5 - lam_pre)):
        tot = lam_pre + lt
        if tot <= 6 - psi:
            out.append((tot, 6 - psi, ctx, f'trunk({w_tr},{M_G})+{lt} '
                        f'-> terminal(w={wt},M={Mt},psi={psi})'))

def cls_C_cells(kbar, mu0):
    """cells for X = kbar-2, eps=mu0, one mu=1 edge, nu_G >= 2 (proved
    complete: c = dq-dp, nu_G | mu0+c-1, kbar>=5 => c <= (4mu0-2)/(kbar-4);
    kbar in {3,4}: nu_G | 3mu0-1 resp. 2mu0-1)."""
    X = kbar - 2
    cells = []
    if X <= 0:
        return cells
    cmax = 4 * mu0 * 10 if kbar <= 4 else (4 * mu0 - 2) // (kbar - 4)
    for c in range(1, cmax + 1):
        num = c * (kbar - 2)
        if num % 2:
            continue
        dp = num // 2
        nu = dp - mu0
        if nu < 2:
            continue
        if (mu0 + c - 1) % nu:
            continue
        dq = dp + c
        if (dq - 1) % nu:
            continue
        M = gcd(dp, dq)
        if M < 2:
            continue
        w_tr = (Fr(kbar) - Fr(X, dp)) / nu
        cells.append((dp, dq, nu, M, w_tr))
    return cells

def tail_first_steps(lam_pre, out):
    """(2,2t) family: seeds w_u = (2u+1)/u, M=2 (u = t-1 >= 1).
    Complete first-step inversion; then normal closure."""
    # dirty/eps l=2 first steps
    for k in range(0, 4):
        for eps in (0, 1):
            if eps == 0 and k == 0:
                continue
            if eps == 1 and k == 0:
                continue        # pure-b: lam = ceil(2w) >= 5: over budget
            Sm = k              # l=2: m_j = 1
            for lex in range(0, 7):
                for nu in range(2, NCAP + 1):
                    dq = (1 + k + lex) * nu + 1
                    dp = eps + nu * (2 + k)
                    E = 2 * dq - dp
                    if E <= 0:
                        continue
                    if k and dq >= dp:
                        continue            # NE needs dq < dp
                    if eps and eps * dq >= dp:
                        continue
                    for u in divisors(2 * dq):
                        kb = Fr(2 * (2 * u + 1) * dq, u * E)
                        if kb.denominator != 1 or kb < 1:
                            continue
                        X = kb * Fr(dp, dq)
                        lam = min_ne_lambda(X, kb, k, Sm, 1) if k else 0
                        if lam is None:
                            continue
                        if eps:
                            lam += max(1, ceil_fr((Fr(X, eps) - kb) / nu))
                        M2 = gcd(dp, dq)
                        if M2 < 2 or lam_pre + lam > 5:
                            continue
                        w2 = Fr(2 * (2 * u + 1) * (dq - 1), u * nu * E)
                        if nu > NCAP - 20:
                            SEEN_BOUNDARY.append(('tail-dirty', nu))
                        feasible(lam_pre + lam, w2, M2,
                                 f'tail u={u} step({dp},{dq})nu{nu}'
                                 f'e{eps}k{k} lam{lam}', out)
    # clean l=2 first steps (M'=2 needs dq even; den u | dq; D | 2u+1)
    for nu in range(3, 301, 2):
        for n in range(3, 301, 2):      # n,nu odd => dq = n*nu+1 even
            dq = n * nu + 1
            D = (n - 1) * nu + 1
            for u in divisors(dq):
                if u < 1 or (2 * u + 1) % D:
                    continue
                w_u = Fr(2 * u + 1, u)
                w2 = w_u * n / D
                if w2 >= w_u:
                    continue
                feasible(lam_pre, w2, 2,
                         f'tail u={u} clean nu{nu}n{n}', out)

def main():
    dist, cells = close_with_cells(Fr(3, 2), 2)
    surv = []
    # ---- class A: equal join; cells (6,10) M2 + tail(lam_pre=3)
    lamA = dist.get((Fr(2), 1))
    print("lam_pre(A) =", lamA)
    if lamA is not None:
        feasible(lamA, Fr(3, 2), 2, 'A eq-join cell (6,10)M2', surv)
        tail_first_steps(lamA, surv)
    # ---- class B: c2at0 mu0=1; cell (3,9) M3; lam_pre = min over nu2*w2=2
    lamB = None
    for (w, M), lam in dist.items():
        r = Fr(2) / w
        if r.denominator == 1 and r >= 2:
            lamB = lam if lamB is None else min(lamB, lam)
    print("lam_pre(B) =", lamB)
    if lamB is not None:
        feasible(lamB, Fr(4, 3), 3, 'B c2at0 cell (3,9)M3', surv)
        tail_first_steps(lamB, surv)     # 0-slot nu_G=1 variant needs w2=2:
                                         # lam_pre=lamA; also run at lamB if
                                         # lamB < lamA (conservative superset)
    # ---- class C: mu0 >= 2 pinned
    for (w2, M2), lam2 in sorted(dist.items(), key=lambda kv: kv[1]):
        for mu0 in divisors(M2):
            if mu0 < 2:
                continue
            numax = ((4 * mu0 + 2) * (mu0 - 1) + 2) / (mu0 * w2) + 1
            nu2 = 2
            while nu2 <= numax:
                ok = ((nu2 + 1) % mu0 == 0)          # neutral arrival
                for (nuc, Mc) in cells.get((w2, M2), ()):
                    if nuc == nu2 and Mc % mu0 == 0:
                        ok = True                     # direct arrival
                if nu2 == 3 and (w2, M2) == (Fr(3, 2), 2) and 2 % mu0 == 0:
                    ok = True                         # entry
                if ok:
                    kb = Fr(mu0 * nu2 * w2 - 2, mu0 - 1)
                    if kb.denominator == 1 and kb >= 3:
                        for (dp, dq, nuG, MG, w_tr) in cls_C_cells(int(kb),
                                                                   mu0):
                            feasible(lam2, w_tr, MG,
                                     f'C mu0={mu0} w2={w2}(lam{lam2}) '
                                     f'nu2={nu2} cell({dp},{dq})nu{nuG}M{MG}',
                                     surv)
                nu2 += 1
    print()
    print("==== SURVIVING (budget-fitting) ROUTES ====")
    seen = set()
    for (tot, bud, ctx, t) in sorted(surv):
        key = (ctx.split(' lam')[0], t.split('->')[-1])
        if key in seen:
            continue
        seen.add(key)
        print(f"  lam={tot} <= budget={bud}: {ctx} | {t}")
    print(f"total routes (deduped): {len(seen)}; raw: {len(surv)}")
    if SEEN_BOUNDARY:
        print("BOUNDARY HITS (rider):", set(SEEN_BOUNDARY))

if __name__ == '__main__':
    main()
