#!/usr/bin/env python3
"""OPEN[OLD-CAP-REGRESSION-alpha/beta]  --  definitive (fibre, block) regression list.

Three inventories, all read in ONE coordinate (the chart's), per fibre/block:

 I_cap  (pre-17(nnnnn) EMITTED state; what the banked kills of 17(zzzzzz)/(aaaaaaa) used)
     h    : hsupport-gate-20260905/before/sprime3_compiler.py :: h_inventory_necessary
            {(b,a): 0<=b<=max(u,0), 0<=a<=K, b+a<=K, (b,a)!=(0,K), -b+d1*a >= B_safe}
            [box/orderbasis-20260903/order_basis_full.py::h_inventory uses b+a<K, a SUBSET]
     a_i/b_i : ...::coeff_inventory_envelope(C,i)
            {(b,a): 0<=a<K, 0<=b<=floor(d1*a - i*B_safe), b+a <= i*K}     (no u-cut)
 I_D1   (17(nnnnn)-repaired state = moh14-charts classes/) : same, total-degree cap dropped.
 G_i    PROVED-NECESSARY support after phi=(x,y+eta):
            {(b,a): 0<=a<K, 0<=b<=floor(d*(i*K-a))},  d = -delta_s = (ell+1)/(n'-M_s'-1)

Gauge: constant (0,0) removed from alpha_e and beta_q (verify_source_complete.py:62-63).
Each escapee is attributed to EVERY old conjunct it violates (not a priority split).
"""
from fractions import Fraction as F
from math import floor, gcd
import json

ROOT = '/home/ubuntu/jc2/'
MAN = ROOT + 'box/moh14-charts-20260905/hsupport-gate-20260905/classes_manifest.json'
COMP = ROOT + 'box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/support-completion.json'
OUT = ROOT + 'box/source-support-closeout-20260905/alpha_beta_regression.json'

def G(K, d, i):
    return {(b, a) for a in range(K) for b in range(floor(d * (i * K - a)) + 1)}

def d1_ok(d1, B, i, b, a):
    return -F(b) + d1 * a >= i * B

def main():
    classes = json.load(open(MAN))
    comp = {r['stem']: r for r in json.load(open(COMP))}
    rows, fibres = [], 0
    for cls in classes:
        for row in cls['rows']:
            fibres += 1
            K, e, q, V2 = row['K'], row['e'], row['q'], row['V2']
            u = max(K - V2, 0)
            d1 = F(row['delta_prime']['1']); B = F(row['B_safe'])
            ds = F(row['delta_prime'][str(row['s_prime'])]); d = -ds
            n, m, ell = row['n_prime'], row['m_prime'], row['ell']
            Ms = row['M_prime'][str(row['s_prime'])]
            assert d == F(ell + 1, n - Ms - 1) and K == gcd(n, m) and e == n // K and q == m // K
            blocks = [('h', 1)] + [('a%d' % i, i) for i in range(1, e + 1)] \
                     + [('b%d' % i, i) for i in range(2, q + 1)]
            for name, i in blocks:
                Gi = G(K, d, i)
                if name in ('a%d' % e, 'b%d' % q):
                    Gi = Gi - {(0, 0)}
                v = {'D1': [], 'TOT': [], 'UCUT': []}     # escapee -> violated conjuncts
                esc_cap, esc_D1only = [], []
                for (b, a) in sorted(Gi):
                    bad = []
                    if not d1_ok(d1, B, i, b, a): bad.append('D1')
                    if name == 'h':
                        if b + a > K: bad.append('TOT')
                        if b > u: bad.append('UCUT')
                    else:
                        if b + a > i * K: bad.append('TOT')
                    if bad:
                        esc_cap.append((b, a))
                        for t in bad: v[t].append((b, a))
                    if 'D1' in bad: esc_D1only.append((b, a))
                # gate form: caps ONLY, no D1 floor (reproduces sec 3.d h-block test)
                esc_gatecaps = sorted((b, a) for (b, a) in Gi
                                      if (b + a > K or b > u) if name == 'h')
                capfalse = sorted(set(v['TOT']) | set(v['UCUT']))
                rows.append(dict(
                    stem=row['stem'], cls=cls['class_id'], block=name, i=i, K=K, e=e, q=q,
                    V2=V2, u=u, d=str(d), delta1=str(d1), B_safe=str(B), ell=ell, nG=len(Gi),
                    n_esc_cap=len(esc_cap), n_esc_D1=len(esc_D1only),
                    n_viol_TOT=len(v['TOT']), n_viol_UCUT=len(v['UCUT']),
                    FALSE_vs_I_cap=bool(esc_cap), FALSE_vs_I_D1=bool(esc_D1only),
                    CAP_REFUTED=bool(capfalse),
                    esc_cap=esc_cap, esc_D1=esc_D1only, capfalse=capfalse,
                    esc_gatecaps_h=esc_gatecaps))
    xc = []
    for r in rows:
        c = comp[r['stem']]
        if r['block'] == 'h':
            fz = sorted(map(tuple, c['h_added_beyond_raw']))
        elif r['block'][0] == 'a':
            fz = sorted(map(tuple, c['alpha_added_beyond_raw'].get(str(r['i']), [])))
        else:
            fz = sorted(map(tuple, c['beta_added_beyond_raw'].get(str(r['i']), [])))
        mine = set(r['esc_D1'])
        xc.append(dict(stem=r['stem'], block=r['block'], mine=len(mine), frozen=len(fz),
                       agree=(mine == set(fz) or mine == set(fz) - {(0, 0)})))
    out = dict(fibres=fibres, blocks=len(rows), rows=rows,
               xcheck_all_agree=all(x['agree'] for x in xc), xcheck=xc)
    json.dump(out, open(OUT, 'w'), indent=1)

    print('fibres=%d blocks=%d   xcheck(G_i\\I_D1 == frozen *_added_beyond_raw)=%s'
          % (fibres, len(rows), out['xcheck_all_agree']))
    print()
    print('=== A. CAP-REFUTED blocks: an escapee lies INSIDE the D1 floor but outside a cap ===')
    print('%-30s %-3s %2s %5s %4s %5s %5s' % ('stem', 'blk', 'K', 'd', '|G|', '#TOT', '#UCUT'))
    nA = 0
    for r in rows:
        if r['CAP_REFUTED']:
            nA += 1
            print('%-30s %-3s %2d %5s %4d %5d %5d   %s' % (
                r['stem'][2:], r['block'], r['K'], r['d'], r['nG'],
                r['n_viol_TOT'], r['n_viol_UCUT'],
                str(r['capfalse'][:4]) + ('...' if len(r['capfalse']) > 4 else '')))
    print('CAP-REFUTED blocks: %d/%d' % (nA, len(rows)))
    fib_cap = sorted({r['stem'] for r in rows if r['CAP_REFUTED']})
    print('CAP-REFUTED fibres: %d/%d  %s' % (len(fib_cap), fibres, [s[2:] for s in fib_cap]))
    print()
    print('=== B. gate sec3.d replication: G_1 vs caps-only {b+a<=K, b<=max(u,0)} at h ===')
    for r in rows:
        if r['block'] == 'h':
            print('  %-30s %-5s n_esc=%2d %s' % (
                r['stem'][2:], 'FALSE' if r['esc_gatecaps_h'] else 'ok',
                len(r['esc_gatecaps_h']), r['esc_gatecaps_h'][:5]))
    print()
    print('=== C. FALSE vs I_cap / I_D1, per fibre ===')
    print('%-30s %-28s %-28s' % ('stem', 'blocks FALSE vs I_cap', 'blocks FALSE vs I_D1'))
    for st in sorted({r['stem'] for r in rows}):
        rc = [r for r in rows if r['stem'] == st]
        print('%-30s %-28s %-28s' % (st[2:],
              ' '.join(r['block'] for r in rc if r['FALSE_vs_I_cap']) or '(none)',
              ' '.join(r['block'] for r in rc if r['FALSE_vs_I_D1']) or '(none)'))

main()
