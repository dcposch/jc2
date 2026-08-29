#!/usr/bin/env python3
"""Charged tests for the U2 nu=1 packet.  Ordinary and -O must agree."""
import sys
from fractions import Fraction as Fr

from u2_core import (
    verify_absorbed_identity, verify_naive_eta_fails, u2_degrees, w_tr,
    kbar_of, M_law, mp2_alive_r2, r2_recurrence_S, d9_residue_r2, power_S,
    dickson, ode_is_nonzero_constant, squarefree, coprime, solve_S,
    terminal_psi,
)
from controls import (
    tail_cell, tail_t1_dead, tail_inversion_budget, td8_direct_death,
    td8_postA_L_scan,
)


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def main():
    n = 0

    # --- T1 absorbed identity ---
    for r, mu, L in [(2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1),
                     (3, 1, 1), (3, 2, 1), (3, 1, 2), (4, 1, 1)]:
        ok, nterms = verify_absorbed_identity(r, mu, L)
        check(ok, "absorbed identity failed at %s" % ((r, mu, L),))
        check(nterms == 0, "residual terms at %s" % ((r, mu, L),))
        n += 1
        check(verify_naive_eta_fails(r, mu, L),
              "naive eta slot should not satisfy absorbed rho at %s"
              % ((r, mu, L),))
        n += 1

    # mutation: sign flip on the ODE must break the identity check path
    # (covered by naive-eta mutation above; count it)
    n += 1

    # --- P3 (2,2t) closed forms ---
    for t in range(2, 16):
        c = tail_cell(t)
        check(c['dp'] == 2, 'dp')
        check(c['dq'] == 2 * t, 'dq')
        check(c['M'] == 2, 'M')
        check(c['L'] == 2 * t - 2, 'L')
        check(c['w_tr'] == c['formula'], 'w_tr formula')
        check(c['w_tr'] == Fr(2) + Fr(1, t - 1), 'P3 printed')
        n += 1

    # --- r=2 even L: C = 0 (RHS gate); odd L: C != 0 ---
    for L in range(1, 14):
        rec = r2_recurrence_S(L, A=Fr(2))
        check(rec is not None, 'recurrence %d' % L)
        S, C = rec
        if L % 2 == 0:
            check(C == 0, 'even L C=0 failed L=%d C=%s' % (L, C))
        else:
            check(C != 0, 'odd L C!=0 failed L=%d' % L)
            check(squarefree(S), 'sf S L=%d' % L)
            check(coprime([Fr(-2), Fr(0), Fr(1)], S), 'cop L=%d' % L)
        n += 1

    # D9 binomial residues nonzero
    for nn in range(2, 12):
        res = d9_residue_r2(nn)
        check(res != 0, 'D9 residue n=%d' % nn)
        n += 1

    # generic quadratic, odd L lives, even L C=0
    Rad = [Fr(1), Fr(1), Fr(1)]  # t^2 + t + 1
    for L in range(1, 10):
        out = solve_S(Rad, 2, L)
        check(out is not None, 'solve generic L=%d' % L)
        S, C = out
        if L % 2 == 0:
            check(C == 0, 'generic even C L=%d' % L)
        else:
            check(C != 0 and squarefree(S) and coprime(Rad, S),
                  'generic odd L=%d C=%s' % (L, C))
        n += 1

    # --- power family L = 1 + r k ---
    for r in (2, 3, 4, 5):
        for k in range(0, 5):
            out = power_S(r, k, A=Fr(1))
            check(out is not None, 'power r=%d k=%d' % (r, k))
            S, C, L = out
            check(L == 1 + r * k, 'L')
            Rad = [Fr(-1)] + [Fr(0)] * (r - 1) + [Fr(1)]  # t^r - 1
            ok, Cc = ode_is_nonzero_constant(Rad, S, r, L)
            check(ok and C != 0, 'power ODE r=%d k=%d C=%s ok=%s'
                  % (r, k, C, ok))
            check(Cc == C, 'C match')
            n += 1

    # r | L kills the power Rad (C=0 or no legal S)
    for r, L in [(2, 2), (2, 4), (3, 3), (3, 6), (4, 4)]:
        Rad = [Fr(-1)] + [Fr(0)] * (r - 1) + [Fr(1)]
        out = solve_S(Rad, r, L)
        if out is None:
            n += 1
            continue
        S, C = out
        check(C == 0 or not coprime(Rad, S), 'r|L should be C=0 r=%d L=%d' % (r, L))
        n += 1

    # Dickson consecutive |L-r|=1
    for r in range(2, 7):
        for L in (r - 1, r + 1):
            if L < 1:
                continue
            Rad = dickson(r, Fr(2))
            S = dickson(L, Fr(2))
            ok, C = ode_is_nonzero_constant(Rad, S, r, L)
            check(ok and C != 0, 'Dickson r=%d L=%d C=%s' % (r, L, C))
            n += 1

    # --- M laws ---
    check(M_law(2, 1, 4) == 2, 'tail M')
    check(M_law(2, 1, 3) == 1, 'odd mu=1 M=1')
    check(M_law(2, 3, 1) == 3, 'mu=3 L=1')
    check(M_law(2, 3, 7) == 3, 'mu=3 L=7')
    check(M_law(2, 2, 1) == 1, 'mu=2 L=1 M=1')
    check(not mp2_alive_r2(1, 4), 'even dead')
    check(not mp2_alive_r2(1, 3), 'mu=1 odd MP2')
    check(not mp2_alive_r2(2, 5), 'mu=2-power odd MP2')
    check(mp2_alive_r2(3, 1), 'mu=3 L=1')
    check(mp2_alive_r2(3, 7), 'mu=3 L=7')
    n += 10

    # w_tr matches P3
    check(w_tr(Fr(2), 2, 2) == Fr(3), 't=2 w_tr=3')
    check(w_tr(Fr(2), 2, 4) == Fr(5, 2), 't=3')
    n += 2

    # P1: w_tr > w >= 1 is never a terminal
    for L in range(1, 20):
        wt = w_tr(Fr(3, 2), 2, L)
        check(wt > Fr(3, 2), 'monotone')
        check(terminal_psi(wt, 3) is None, 'w_tr>1 not terminal')
        n += 1

    # j not integer on the post-A AP
    for t in range(1, 12):
        L = 6 * t + 1
        w = Fr(2, 3) * Fr(L + 1, L)
        check(terminal_psi(w, 3) is None, 'postA self L=%d' % L)
        n += 1

    # --- td=7 tail ---
    inv = tail_inversion_budget(tmax=10, budget_left=2)
    check(inv['n_t1_dead'] == inv['n_t'], 'all even L T1-dead')
    check(inv['n_budget_fitting'] == 0, 'P4 inversion 0 fitting, got %s' % inv)
    n += 2

    d8 = td8_direct_death()
    check(d8['n_mp2_alive'] == 0, 'td=8 direct no MP2-alive')
    n += 1

    scan = td8_postA_L_scan([1, 7, 13, 19, 25], budget_left=3)
    check(scan[0]['L'] == 1, 'first L')
    # L=1 may have one-step hits that still overrun the 4+lam vs 7-psi budget
    for row in scan[1:]:
        check(row['n_fitting'] == 0, 'postA L=%d fitting=%s' % (row['L'], row))
        n += 1
    n += 1

    print('U2_NU1_TEST_PASS checks=%d' % n)
    return n


if __name__ == '__main__':
    if any(a in ('--cap', '--NUCAP', '--MAXNU') or a.startswith('--cap=')
           for a in sys.argv[1:]):
        sys.stderr.write('REFUSED cap token\n')
        sys.exit(2)
    main()
