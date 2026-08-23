#!/usr/bin/env python3
"""TOWER-ROLLOUT.md clash-window arithmetic for the 16 remaining td-7
s11a cells (post-(9,15,7,3)@2 tower kill).  Prediction engine, NOT a
certificate: quantifiers over parametric families are probed (minimal
instantiation + exact small-deg scan), not closed.

Reuses px2/px5 READ-ONLY (step menus, closure, feasible). Computes per cell:
  * identity checks (kbar, E5 pin, X, N1, P3 divisibility)
  * arrival states/menus/routes (must match the s11a census)
  * chain-2 charged-DAG enumeration with exact deg p_f transport
      deg p_f(P2) = 4;  deg p_f(child) = deg p_f(parent) * dp_child / l_child
    (St 8.3(ii) + Prop 8.1(i): deg p_{f,parent} = i_child * l_child)
  * min deg p_f at the arrival vertex U over all realizations ->
      i_G = deg p_{f,U}/mu0 (H8), chain-1 stack product P = i_G/2
  * P = 1 (empty-stack) escape scan: exact enumeration of ALL realizations
    with deg p_{f,U} <= 50 = 2*mu0_max
  * window arithmetic: first-step gap menu, max chain-2 gap vs 1/2,
    gap(X) = (nu+1)/(2nu) family, Case-A pair, prefix menu deltas.
No files modified outside scratchpad. No git.
"""
import os
import sys
from fractions import Fraction as Fr
from math import gcd

HERE = '/Users/dc/code/math/jc72108/cases/scratch_offaxis_pricing'
sys.path.insert(0, HERE)
import px2  # noqa: E402
import px5  # noqa: E402

ENTRY = (Fr(3, 2), 2)
DEG_P2 = 4          # deg p_f at the chain-2 pole (2,3)*M, M=2 (entry state)
DEG_P1 = 2          # deg p_f at the chain-1 pole (2,3), M=1 (frozen (1,2,1))

# the 16 remaining cells: (dp, dq, nuG, MG, mu0)
CELLS = [
    (10, 15, 7, 5, 3), (15, 25, 12, 5, 3), (18, 27, 13, 9, 5),
    (21, 35, 17, 7, 4), (25, 35, 17, 5, 8), (26, 39, 19, 13, 7),
    (27, 45, 22, 9, 5), (34, 51, 25, 17, 9), (42, 63, 31, 21, 11),
    (50, 75, 37, 25, 13), (58, 87, 43, 29, 15), (66, 99, 49, 33, 17),
    (74, 111, 55, 37, 19), (82, 123, 61, 41, 21), (90, 135, 67, 45, 23),
    (98, 147, 73, 49, 25)]

# census expectations (s11a table): routes raw(eq)
CENSUS = {
    (10, 15, 7, 5): (47, 29), (15, 25, 12, 5): (2, 2),
    (18, 27, 13, 9): (37, 33), (21, 35, 17, 7): (2, 2),
    (25, 35, 17, 5): (3, 2), (26, 39, 19, 13): (63, 53),
    (27, 45, 22, 9): (2, 2), (34, 51, 25, 17): (18, 17),
    (42, 63, 31, 21): (23, 22), (50, 75, 37, 25): (31, 30),
    (58, 87, 43, 29): (1, 1), (66, 99, 49, 33): (1, 1),
    (74, 111, 55, 37): (1, 1), (82, 123, 61, 41): (1, 1),
    (90, 135, 67, 45): (1, 1), (98, 147, 73, 49): (1, 1)}


def parse_step(w, M, w2, M2, lam, tag, exact_cap=None):
    """Yield (mult_num, mult_den, cellinfo) deg-multipliers for one menu step.
    mult = dp/l.  cellinfo = (nu, M2, kind, l, dp, dq).
    Parametric families (pure-b, neutral-drop) are instantiated: minimal nu
    if exact_cap is None, else all nu with resulting deg-mult num <= cap."""
    outs = []
    if tag.startswith('clean'):
        # tag 'clean D{Delta}n{n}nu{nu}': dp = l*nu, dq = n*nu+1;
        # deg-multiplier dp/l = nu (l-free)
        nu = int(tag.split('nu')[-1])
        D = int(tag.split('D')[1].split('n')[0])
        n = (D - 1) // nu + 1
        dq_ = n * nu + 1
        outs.append((nu, 1, (nu, M2, 'clean', None, None, dq_)))
    elif tag.startswith('st96'):
        body = tag[5:]
        l = int(body.split('e')[0][1:])
        cell = body.split('(')[1].rstrip(')')
        dp, dq = (int(x) for x in cell.split(','))
        nu = int(body.split('nu')[1].split('(')[0])
        outs.append((dp, l, (nu, M2, 'st96', l, dp, dq)))
    elif tag.startswith('pure-b'):
        body = tag[7:]
        l = int(body.split('e')[0][1:])
        eps = int(body.split('e')[1])
        E = l - eps
        # M2 = gcd(E, nu+1) (E>1) else 1; nu >= 2
        cap = 60 if exact_cap is None else exact_cap
        found = 0
        for nu in range(2, cap + 1):
            g = gcd(E, nu + 1) if E > 1 else 1
            if g != M2:
                continue
            dp = eps + l * nu
            outs.append((dp, l, (nu, M2, 'pure-b', l, dp, nu + 1)))
            found += 1
            if exact_cap is None and found >= 1:
                break
        # parametric: nu unbounded upward (deg only grows)
    elif tag.startswith('neutral-drop'):
        a, b = tag.split()[-1].split('->')
        Mfrom, Mto = int(a), int(b)
        if Mto == Mfrom:
            return []          # identity pad: excluded from min paths
        cap = 60 if exact_cap is None else exact_cap
        found = 0
        for nu in range(2, cap + 1):
            ok = False
            for l in px5.divisors(Mfrom):
                if l % Mto == 0 and gcd(l, nu + 1) == Mto:
                    ok = True
                    break
            if not ok:
                continue
            outs.append((nu, 1, (nu, Mto, 'ndrop', None, None, nu + 1)))
            found += 1
            if exact_cap is None and found >= 1:
                break
    return outs


def enumerate_paths(budget=5, deg_cap=10**7, exact_cap=None, maxlen=9):
    """All chain-2 realization paths from ENTRY: returns list of
    (w, M, lam, deg, first_tag, last_cell, depth, tagseq).
    exact_cap: if set, instantiate parametric nu up to it and cap deg."""
    from collections import deque
    start = (ENTRY[0], ENTRY[1], 0, DEG_P2, None, None, 0, ())
    seen = set()
    out = []
    dq_ = deque([start])
    while dq_:
        w, M, lam, deg, ft, lc, depth, seq = dq_.popleft()
        key = (w, M, lam, deg, ft, lc)
        if key in seen:
            continue
        seen.add(key)
        if depth > 0:
            out.append((w, M, lam, deg, ft, lc, depth, seq))
        if depth >= maxlen:
            continue
        for (w2, M2, dl, tag) in set(px2.chain_steps(w, M)):
            l2 = lam + dl
            if l2 > budget:
                continue
            for (mn, md, cellinfo) in parse_step(w, M, w2, M2, dl, tag,
                                                 exact_cap):
                num = deg * mn
                if num % md:
                    continue        # deg p_f integrality (Prop 8.1)
                nd = num // md
                cap = deg_cap if exact_cap is None else exact_cap
                if nd > cap:
                    continue
                nft = ft if ft is not None else tag
                dq_.append((w2, M2, l2, nd, nft, cellinfo, depth + 1,
                            seq + (tag,)))
    return out


def cell_report(paths_min, paths_exact, dist, cellmap):
    rows = []
    for (dp, dq, nuG, MG, mu0) in CELLS:
        kbar = Fr(2 * dq, dq - dp)
        assert kbar.denominator == 1
        kbar = int(kbar)
        X = kbar - 2
        wreq = Fr(kbar * (mu0 - 1) + 2, mu0 * nuG)
        n1 = gcd(kbar, nuG)
        p3 = (dq - 1) % nuG == 0
        states = sorted((M, dist[(wreq, M)]) for (w, M) in dist
                        if w == wreq and M % mu0 == 0)
        # routes (census parity)
        w_tr = (Fr(kbar) - Fr(X, dp)) / nuG
        routes = []
        for (M2, lam2) in states:
            px5.feasible(lam2, w_tr, MG, 'M=%d lam=%d' % (M2, lam2), routes)
        n_raw = len(routes)
        n_eq = sum(1 for (t, b, _, _) in routes if t == b)
        # min deg p_f,U per arrival state: direct + neutral realizations
        best = None            # (degU, kind, detail)
        p1_escape = []         # realizations with degU == 2*mu0 (empty stack)
        noint = 0              # realizations (exact scan) with 2*mu0 ∤ degU
        arr_int_all = True
        firsts = set()
        dags = set()
        mindepth = None
        for (w, M, lam, deg, ft, lc, depth, seq) in paths_min:
            if w != wreq or M % mu0:
                continue
            firsts.add(ft)
            dags.add(seq)
            if mindepth is None or depth < mindepth:
                mindepth = depth
            # direct arrival: U = landing vertex (nu, M) of the last step,
            # legal iff recorded in cellmap with mu0 | Mc (superset law)
            nu_l, M_l = lc[0], lc[1]
            direct_ok = any(nuc == nu_l and Mc % mu0 == 0
                            for (nuc, Mc) in cellmap.get((w, M), ()))
            if direct_ok:
                cand = (deg, 'direct', 'nu=%d %s' % (nu_l, lc[2]), lam, depth)
                if best is None or cand[0] < best[0]:
                    best = cand
            # neutral arrival: pad vertex nu ≡ -1 (mod mu0), minimal legal
            for nuU in range(max(2, mu0 - 1), 4 * mu0 + 2):
                if (nuU + 1) % mu0:
                    continue
                # pad needs l | M with mu0 | gcd(l, nuU+1); l = M works iff
                # mu0 | gcd(M, nuU+1); superset: accept mu0 | nuU+1 & mu0 | M
                cand = (deg * nuU, 'neutral', 'nuU=%d over %s' %
                        (nuU, lc[2]), lam, depth + 1)
                if best is None or cand[0] < best[0]:
                    best = cand
                break
        # exact small-deg escape scan
        for (w, M, lam, deg, ft, lc, depth, seq) in paths_exact:
            if w != wreq or M % mu0:
                continue
            nu_l, M_l = lc[0], lc[1]
            direct_ok = any(nuc == nu_l and Mc % mu0 == 0
                            for (nuc, Mc) in cellmap.get((w, M), ()))
            degUs = []
            if direct_ok:
                degUs.append(deg)
            for nuU in range(max(2, mu0 - 1), 51):
                if (nuU + 1) % mu0 == 0 and deg * nuU <= 50:
                    degUs.append(deg * nuU)
            for dU in degUs:
                if dU == 2 * mu0:
                    p1_escape.append((seq, dU))
                if dU % (2 * mu0):
                    noint += 1
        # max chain-2 vertex gap over ALL path-states reaching this cell's
        # arrival states (window audit: every gap must be < 1/2)
        maxgap = Fr(0)
        gapwit = None
        reach = set()
        for (w, M, lam, deg, ft, lc, depth, seq) in paths_min:
            if w == wreq and M % mu0 == 0:
                for i in range(1, len(seq) + 1):
                    reach.add(seq[:i])
        for (w, M, lam, deg, ft, lc, depth, seq) in paths_min:
            if seq in reach:
                dqv = lc[5]
                g = Fr(dqv, deg)
                if g > maxgap:
                    maxgap, gapwit = g, (lc[2], lc[0], dqv, deg)
        degU_min, kind, detail, lam_at, dep = best if best else \
            (None, '-', 'NO PATH', None, None)
        P_min = Fr(degU_min, 2 * mu0) if degU_min else None
        rows.append(dict(
            cell=(dp, dq, nuG, MG), mu0=mu0, kbar=kbar, X=X, wreq=wreq,
            n1=n1, p3=p3, states=states, n_raw=n_raw, n_eq=n_eq,
            firsts=sorted(firsts), n_dags=len(dags), mindepth=mindepth,
            degU_min=degU_min, arr_kind=kind, arr_detail=detail,
            P_min=P_min, p1_escape=p1_escape, w_tr=w_tr,
            maxgap=maxgap, gapwit=gapwit, noint=noint))
    return rows


def first_step_menu():
    """The universal charged one-step menu from ENTRY with gap arithmetic:
    deg p_f = 4*dp/l (P2 handoff), gap = dq/deg p_f = dq/(i*dp), i = 4/l."""
    menu = []
    for (w2, M2, lam, tag) in sorted(set(px2.chain_steps(*ENTRY))):
        if lam == 0:
            continue
        for (mn, md, ci) in parse_step(ENTRY[0], ENTRY[1], w2, M2, lam, tag,
                                       exact_cap=8):
            nu, M2c, kind, l, dp_, dq_ = ci
            deg = Fr(DEG_P2 * mn, md)
            dqv = dq_ if kind != 'pure-b' else nu + 1
            dpv = dp_ if dp_ else (mn if md == 1 else None)
            gap = Fr(dqv, int(deg)) if deg.denominator == 1 else None
            menu.append((tag, (w2, M2), lam, nu, dpv, dqv, int(deg)
                         if deg.denominator == 1 else deg, gap))
    return menu


def main():
    dist, cellmap = px5.close_with_cells(*ENTRY)
    print('closure: %d states' % len(dist))
    print()
    print('=== universal first-charged-step menu from ENTRY (3/2,2) ===')
    print('    (deg p_f,P2 = 4; i_V1 = 4/l; gap = dq/(i*dp) = dq/deg p_f)')
    for row in first_step_menu():
        tag, st, lam, nu, dpv, dqv, deg, gap = row
        print('  %-22s -> state %-12s lam=%d nu=%-2d cell(%s,%s) '
              'deg p_f=%-3s gap=%s' % (tag, st, lam, nu, dpv, dqv, deg, gap))
    print()
    # closure-wide resonance/gap audit
    print('=== closure-wide window audit ===')
    big_nums = sorted({(w, M) for (w, M) in dist if w.numerator >= 13})
    print('  states with num(w) >= 13 (resonance n>=7 fuel): %s'
          % (big_nums if big_nums else 'NONE'))
    res = []
    for (w, M) in dist:
        for (w2, M2, dl, tag) in set(px2.chain_steps(w, M)):
            if tag.startswith('clean'):
                D = int(tag.split('D')[1].split('n')[0])
                nu = int(tag.split('nu')[-1])
                n = (D - 1) // nu + 1
                if n >= 2:
                    res.append(((w, M), tag))
    print('  resonant (n>=2) steps anywhere in closure: %d %s'
          % (len(res), sorted(set(res))[:6]))
    print()
    print('enumerating realization paths (min-deg mode)...')
    paths_min = enumerate_paths(deg_cap=10**7, maxlen=8)
    print('  %d path-states' % len(paths_min))
    print('enumerating exact small-deg paths (deg <= 50 escape scan)...')
    paths_exact = enumerate_paths(deg_cap=50, exact_cap=50, maxlen=8)
    print('  %d small-deg path-states' % len(paths_exact))
    print()
    rows = cell_report(paths_min, paths_exact, dist, cellmap)
    print('=== PER-CELL TABLE ===')
    ok_census = True
    for r in rows:
        exp = CENSUS[r['cell']]
        match = (r['n_raw'], r['n_eq']) == exp
        ok_census &= match
        print('%-18s@%-2d kbar=%d X=%d w_req=%-5s N1=%d P3=%s' %
              (r['cell'], r['mu0'], r['kbar'], r['X'], r['wreq'],
               r['n1'], r['p3']))
        print('   states(M,lam)=%s routes=%d(%d eq) [census %s: %s]' %
              (r['states'], r['n_raw'], r['n_eq'], exp,
               'match' if match else 'MISMATCH'))
        print('   DAGs<=lam5: %d  min chain-2 depth: %s  first-steps: %s' %
              (r['n_dags'], r['mindepth'],
               [f.split('(')[0] for f in r['firsts']]))
        print('   min deg p_f,U = %s (%s %s) -> i_G = %s, stack product '
              'P_min = %s' %
              (r['degU_min'], r['arr_kind'], r['arr_detail'],
               Fr(r['degU_min'], r['mu0']) if r['degU_min'] else '-',
               r['P_min']))
        print('   P=1 empty-stack realizations (deg_U = 2mu0 exact scan): %s'
              % (r['p1_escape'] if r['p1_escape'] else 'NONE'))
        print('   max chain-2 vertex gap on its routes: %s (witness %s)'
              ' -> %s 1/2' %
              (r['maxgap'], r['gapwit'],
               '<' if r['maxgap'] < Fr(1, 2) else '>=NOT-BELOW'))
    print()
    print('census parity over 16 cells: %s' % ('PASS' if ok_census else
                                               'FAIL'))
    allgap = max(r['maxgap'] for r in rows)
    allP = min(r['P_min'] for r in rows)
    print('GLOBAL: max chain-2 gap over all 16 cells = %s (< 1/2: %s); '
          'min stack product = %s; empty-stack escapes: %d'
          % (allgap, allgap < Fr(1, 2), allP,
             sum(len(r['p1_escape']) for r in rows)))


if __name__ == '__main__':
    main()
