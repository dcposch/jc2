#!/usr/bin/env python3
"""Independent (99,66) band run.  usage: run_bands.py delta2|delta52 NSTAGES"""
import sys, json, time, os
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fractions import Fraction as Fr
import indep_engine as E
from ring import *
from math import comb

BR = sys.argv[1]; NSTAGES = int(sys.argv[2])
t00 = time.time(); LOG = {'branch': BR, 'NT': E.NT, 'stages': []}
br = E.Branch(BR)

def rank_key(v):        # prefer inert (r >= NT) chart columns as pivots
    if os.environ.get('LEX_ORDER'): return (1, 0, v)   # plain lexicographic name order
    if v.startswith(('K2c_', 'B1c_')):
        r = int(v.split('_')[1]); return (0 if r >= E.NT else 1, -r, v)
    return (1, 0, v)

# ---------- 1. inner: h3 minor-leader reduction ----------
K3full = E.build_K3(12)                      # leader rows need t^0..t^9 (delta2) / s^21
el = E.Elim(forbidden={br.leadvar}); el.rank_key = rank_key
lstat = {'zero': 0, 'pivot': 0, 'residue': 0}
for lab, p in E.leader_rows(br, K3full): lstat[el.feed(lab, p)] += 1
LOG['h3_leader'] = {'rows': sum(lstat.values()), **lstat}
free_h3 = [E.hname(*s) for s in E.H_FREE if E.hname(*s) not in el.sub]
if BR == 'delta52' and not os.environ.get('NO_XU_ODE'):
    el.feed('xu_ode_n1_Hc_11_0', var('Hc_11_0'))     # charged design compatibility
    free_h3 = [v for v in free_h3 if v != 'Hc_11_0']
LOG['free_h3'] = free_h3
assert not el.residues, el.residues

K3 = E.series_subst(E.build_K3(E.NT), el.sub)
K2, lowq_free, lowq_const, viol = E.build_K2(K3); assert not viol, viol
B1, _ = E.build_B1(E.NT)
print('[K3 sub] %.1fs' % (time.time() - t00), flush=True)
KF, KG = E.build_KFKG(K2, B1)
print('[KF,KG] %.1fs' % (time.time() - t00), flush=True)
KJ = E.build_KJ_factored(KF, B1, K2)
for n in range(1, E.NT):
    w = E.to_w(KJ[n])
    assert not w or max(w) <= 163 - n, (n, max(w))     # [x^i y^j], i = 163-n-j >= 0
print('[KJ] %.1fs' % (time.time() - t00), flush=True)

# ---------- 2. the seven h2 D1 rows ----------
h2rows = []
for lab, p in E.h2_d1_rows(K2):
    W = int(lab.split('_W')[1].split('_')[0]); j = int(lab.split('_j')[1])
    for (r, q) in E.K2_SLOTS:
        if 3 * r + 4 * q == W and r >= E.NT and q >= j:
            p = add(p, smul(var(E.kname(r, q)), comb(q, j)))
    h2rows.append((lab, p))
n0 = len(el.pivots)
for lab, p in h2rows: el.feed(lab, p)
h2_rank = len(el.pivots) - n0
LOG['h2_D1_rank'] = h2_rank
inner = len(free_h3) + (2 if BR == 'delta2' else 3) + 106 - h2_rank
LOG['inner_dimension'] = inner
print('[h2 D1] rank %d  inner %d  pre-outer joint %d'
      % (h2_rank, inner, inner + 6600), flush=True)

# ---------- 3. outer D1 rows by offset ----------
OUT = {'A2': (65, 33, Fr(-2), Fr(-2, 9)), 'A3': (98, 33, Fr(-3), Fr(-1, 3)),
       'B1': (32, 33, Fr(-1), Fr(-1, 9)), 'B2': (65, 33, Fr(-2), Fr(-2, 9))}
d1 = {}
for k, (D, r0, a, b) in OUT.items():
    for (off, lab, p) in E.d1_rows_for(k, D, r0, a, b,
                                       (lambda r, q, k=k: '%sc_%d_%d' % (k, r, q))):
        d1.setdefault(off, []).append((k, lab, p))
elo = E.Elim(forbidden=set()); elo.rank_key = rank_key; elo._prev = 0

# ---------- 4. stage loop ----------
def jac_rows(n, ks):
    P = E.to_w(KJ[n])
    return [('J_d%d_k%d' % (163 - n, j), P.get(j, {})) for j in ks]
def pole_rows(stage):
    """[t^{4+k}] (resp [s^{8+k}]) of KF, KG after the minor substitution.
       Labels are emitted for every branch-coordinate power the support allows."""
    m = (4 if BR == 'delta2' else 8) + stage
    emax = m // (3 if BR == 'delta2' else 7)     # zeta at t^3 / pi at s^7
    out = []
    for nm, S in (('F', KF), ('G', KG)):
        d = E.split_z(br.sub_series(S, m).get(m, {}), br.zvar)
        for e in range(emax + 1):
            out.append(('%s_local%d_%s^%d' % (nm, m, br.zvar, e), d.get(e, {})))
    return out

cum_outer = cum_joint = 0
for st in range(NSTAGES + 1):
    t0 = time.time(); n0 = len(el.pivots); raw_out = 0
    for (k, lab, p) in d1.get(st, []):
        raw_out += 1
        (el if k == 'B1' else elo).feed(lab, p)
    o_rank = (len(el.pivots) - n0) + (len(elo.pivots) - elo._prev)
    elo._prev = len(elo.pivots)
    n1 = len(el.pivots)
    rows = [] if os.environ.get('NO_POLE') else pole_rows(st)
    npole = len(rows)
    tp = 1 if st <= 1 else st
    ks = [27] if st == 0 else (list(range(28, 163)) if st == 1
                               else sorted(E.to_w(KJ[tp]).keys()) or [0])
    if not os.environ.get('NO_JAC'): rows += jac_rows(tp, ks)
    else: ks = []
    stats = {'zero': 0, 'pivot': 0, 'residue': 0}
    for lab, p in rows: stats[el.feed(lab, p)] += 1
    j_new = len(el.pivots) - n1
    cum_outer += o_rank; cum_joint += j_new
    dim = inner + 6600 - 5598 - cum_outer - cum_joint
    res = el.residues[:]
    rec = {'stage': st, 'outer_raw': raw_out, 'outer_rank': o_rank,
           'outer_cum': cum_outer, 'pole_labels': npole, 'jac_labels': len(ks),
           'joint_new': j_new, 'joint_cum': cum_joint,
           'zero_or_dependent': stats['zero'], 'n_residues': len(res),
           'formal_dimension': dim, 'dimension': None if res else dim,
           'new_pivots': [(l, v, c) for (l, v, c) in el.pivots[n1:]],
           'secs': round(time.time() - t0, 1)}
    if res:
        rec['residues'] = [(l, {str(m): str(c) for m, c in p.items()}) for l, p in res]
        consts = [(l, as_const(p)) for l, p in res if as_const(p) not in (None, Fr(0))]
        rec['constant_unit_certificates'] = [(l, str(c)) for l, c in consts]
        rec['verdict'] = 'DEAD' if consts else 'RESIDUE-NONCONSTANT'
    LOG['stages'].append(rec)
    print('[stage %d] outer %d/%d cum %d | pole %d jac %d | joint new %d cum %d | dim %s | res %d | %.1fs'
          % (st, raw_out, o_rank, cum_outer, npole, len(ks), j_new, cum_joint,
             rec['dimension'], len(res), rec['secs']), flush=True)
    if res:
        for l, p in res[:8]:
            print('    RESIDUE %s -> %s' % (l, {str(m): str(c) for m, c in p.items()}))
        break
LOG['total_secs'] = round(time.time() - t00, 1)
json.dump(LOG, open('box/g9966indep-20260903/run_%s%s.json' % (BR, os.environ.get('TAG','')), 'w'), indent=1)
print('[done] %.1fs' % LOG['total_secs'])
