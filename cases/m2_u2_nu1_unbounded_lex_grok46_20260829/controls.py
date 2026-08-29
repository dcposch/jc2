#!/usr/bin/env python3
"""td=7 (2,2t) tail inversion and td=8 equal-w source-row death.

Cap-free: dirty menus use the Sol56 divisor bound E | l * num(w) * T with
k bounded by remaining budget, not by a search cap token.
"""
from fractions import Fraction as Fr
from math import gcd

from u2_core import (
    ceil_fr, fdiv, terminal_psi, w_tr, M_law, mp2_alive_r2, kbar_of,
    u2_degrees, r2_recurrence_S, squarefree, coprime,
)


def tail_cell(t):
    """P3 (2,2t) M2 tail: r=2, mu=1, nu=1, dq=2t, L=2t-2, w=2.
    w_tr = 2 + 1/(t-1) = (2t-1)/(t-1).
    """
    assert t >= 2
    L = 2 * t - 2
    dp, dq, E, M = u2_degrees(2, 1, L)
    w = Fr(2)
    wt = w_tr(w, 2, L)
    return dict(t=t, L=L, dp=dp, dq=dq, E=E, M=M,
                w_tr=wt, kbar=kbar_of(w, 2, 1, L),
                formula=Fr(2 * t - 1, t - 1))


def min_ne_lam(X, kb, k, Sm, mm):
    if k == 0:
        return 0
    best = [None]

    def rec(j, left, acc):
        if j == k:
            if left == 0 and (best[0] is None or acc < best[0]):
                best[0] = acc
            return
        rem = k - j - 1
        for m in range(1, mm + 1):
            if left - m < rem or left - m > rem * mm:
                continue
            g = Fr(X, m) - kb
            if g <= 0:
                return
            rec(j + 1, left - m, acc + max(1, ceil_fr(g)))

    rec(0, Sm, 0)
    return best[0]


def one_step_hits(w, M, budget_left):
    """Cap-free one-step (clean + dirty) to a P1 terminal.  k <= budget_left;
    lex from the Sol56 T / Cmax bound; E runs over divisors of l*num(w)*T.
    """
    hits = []
    psi0 = terminal_psi(w, M)
    if psi0 is not None:
        hits.append(('self', w, M, 0, psi0))
    a = w.numerator
    for Delta in fdiv(a):
        if Delta < 3:
            continue
        for nu in range(2, Delta):
            if (Delta - 1) % nu:
                continue
            n = (Delta - 1) // nu + 1
            if n < 2:
                continue
            dq = n * nu + 1
            if dq % w.denominator:
                continue
            for l in fdiv(M):
                w2 = Fr(w * n, Delta)
                M2 = gcd(l, dq)
                psi = terminal_psi(w2, M2)
                if psi is not None:
                    hits.append(('clean', w2, M2, 0, psi, Delta, n, nu, l))
    kmax = max(0, budget_left)
    for l in fdiv(M):
        for eps in range(0, l):
            for k in range(0, kmax + 1):
                if eps == 0 and k == 0:
                    continue
                sm_lo, sm_hi = (k, k * (l - 1)) if k else (0, 0)
                for Sm in range(sm_lo, sm_hi + 1) if k else [0]:
                    if eps > 0:
                        num = Sm + l - eps * (1 + k) - 1
                        lexmax = -1 if num < 0 else num // eps
                    else:
                        T0 = Sm + l
                        Cmax = (l * a * T0 - l) // 2 if T0 else 0
                        lexmax = int((Cmax + Sm) // l) - k if l else -1
                    if lexmax < 0:
                        continue
                    for lex in range(0, lexmax + 1):
                        C = l * (k + lex) - Sm
                        if C <= 0:
                            continue
                        T = Sm + l - eps * (1 + k + lex)
                        if T <= 0:
                            continue
                        bound = l * a * T
                        if bound <= 0:
                            continue
                        for E in fdiv(bound):
                            nuq, rem = divmod(E - (l - eps), C)
                            if rem or nuq < 2:
                                continue
                            nu = nuq
                            dq = (1 + k + lex) * nu + 1
                            dp = eps + nu * (l + Sm)
                            kb = Fr(l * w * dq, E)
                            if kb.denominator != 1 or kb < 1:
                                continue
                            if eps and eps * dq >= dp:
                                continue
                            X = kb * Fr(dp, dq)
                            mm = min(l - 1, int((dp - 1) // dq)) if k else 0
                            if k and (mm < 1 or Sm > k * mm):
                                continue
                            lam = min_ne_lam(X, kb, k, Sm, mm) if k else 0
                            if lam is None:
                                continue
                            if eps:
                                lam += max(1, ceil_fr((Fr(X, eps) - kb) / nu))
                            if lam > budget_left:
                                continue
                            w2 = Fr(l * w * (dq - 1), nu * E)
                            M2 = gcd(int(dp), int(dq))
                            psi = terminal_psi(w2, M2)
                            if psi is not None:
                                hits.append(('dirty', w2, M2, lam, psi,
                                             l, eps, k, lex, nu))
    return hits


def tail_t1_dead(t):
    """Even L = 2t-2: unique S for Rad = t^2-2 gives C = 0."""
    L = 2 * t - 2
    rec = r2_recurrence_S(L, A=Fr(2))
    if rec is None:
        return True, None
    S, C = rec
    return C == 0, C


def tail_inversion_budget(tmax=12, budget_left=2):
    """First-step inversion of the (2,2t) tail, remaining budget after the
    lambda=3 eps-step.  P4 remaining is 3-psi <= 2.  Returns (n_t, n_hits).
    """
    n_hits = 0
    n_t1_dead = 0
    for t in range(2, tmax + 1):
        cell = tail_cell(t)
        dead, C = tail_t1_dead(t)
        if dead:
            n_t1_dead += 1
        # inversion uses u = t-1, w = (2u+1)/u = cell['w_tr']
        hits = one_step_hits(cell['w_tr'], 2, budget_left)
        # a hit still has to fit the shared St 9.4 budget: spent 3 + lam
        # <= 6 - psi, i.e. lam <= 3 - psi.
        fitting = []
        for h in hits:
            lam = h[3]
            psi = h[4]
            if 3 + lam <= 6 - psi:
                fitting.append(h)
        n_hits += len(fitting)
    return dict(n_t=tmax - 1, n_t1_dead=n_t1_dead, n_budget_fitting=n_hits)


def td8_direct_death():
    """td=8 m=2 equal-w entry: both b=2, mu | 2 so mu in {1,2}, r=2.
    mu a 2-power: odd L has M = gcd(mu, L+2) = 1; even L is T1 C=0.
    """
    rows = []
    for mu in (1, 2):
        for L in range(1, 17):
            rows.append((mu, L, mp2_alive_r2(mu, L), M_law(2, mu, L),
                         L % 2 == 0))
    alive = [r for r in rows if r[2]]
    return dict(n=len(rows), n_mp2_alive=len(alive), rows_sample=rows[:8])


def td8_postA_L_scan(Ls, budget_left=3):
    """After a symmetric (A)-jump both chains sit at w=2/3, M=3, mu=3.
    L odd, L ≡ 1 (mod 6) for M=3.  w_tr = (2/3)(L+1)/L.
    """
    out = []
    for L in Ls:
        if L % 2 == 0 or L % 6 != 1:
            continue
        w = Fr(2, 3) * Fr(L + 1, L)
        M = M_law(2, 3, L)
        hits = one_step_hits(w, M, budget_left)
        # spent 4 on the two (A) steps; budget 7 - psi; need 4+lam <= 7-psi
        fitting = []
        for h in hits:
            lam, psi = h[3], h[4]
            if 4 + lam <= 7 - psi:
                fitting.append(h)
        out.append(dict(L=L, w=str(w), M=M, n_hits=len(hits),
                        n_fitting=len(fitting),
                        self_terminal=terminal_psi(w, M)))
    return out
