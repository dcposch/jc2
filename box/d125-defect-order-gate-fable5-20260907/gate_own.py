#!/usr/bin/env python3
"""Own tiny stdlib control for the D125 defect-weighted order proposal.
Explicit bracket differentiation, slot-pair forcing census, envelope rows,
descriptor/ring digests via a relocated baseline path, two GB comparator
controls. Never forms a full J or lift coefficient row. No Assert gates."""
import argparse, hashlib, importlib.util, json, sys
from fractions import Fraction as Fr
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--baseline', required=True)
ap.add_argument('--witnesses', required=True)
ap.add_argument('--out', required=True)
ap.add_argument('--mutate', choices=['w2', 'w3', 'envelope', 'tiebreak'])
A = ap.parse_args()


def need(c, why):
    if not c:
        raise ValueError('REJECT: ' + why)


def canonical(v):
    return (json.dumps(v, sort_keys=True, separators=(',', ':')) + '\n').encode()


# ---- polynomial helpers in (gamma, pi): {(i,j): Fraction} ----
def pmul(P, Q):
    R = {}
    for (i, j), a in P.items():
        for (k, l), b in Q.items():
            R[(i+k, j+l)] = R.get((i+k, j+l), 0) + a*b
    return {m: c for m, c in R.items() if c}


def ppow(P, n):
    R = {(0, 0): Fr(1)}
    for _ in range(n):
        R = pmul(R, P)
    return R


def bracket(P, Q):
    R = {}
    for (i, j), a in P.items():
        for (k, l), b in Q.items():
            det = i*l - j*k
            if det:
                m = (i+k-1, j+l-1)
                R[m] = R.get(m, 0) + det*a*b
    return {m: c for m, c in R.items() if c}


def rref(rows, cols):
    a = [list(r) for r in rows]
    piv, r0 = [], 0
    for c in cols:
        f = next((j for j in range(r0, len(a)) if a[j][c]), None)
        if f is None:
            continue
        a[r0], a[f] = a[f], a[r0]
        s = a[r0][c]
        a[r0] = [x/s for x in a[r0]]
        for j in range(len(a)):
            if j != r0 and a[j][c]:
                t = a[j][c]
                a[j] = [x-t*y for x, y in zip(a[j], a[r0])]
        piv.append(c)
        r0 += 1
    return piv, a[:r0]


def nullspace(rows, n):
    piv, red = rref(rows, list(range(n)))
    free = [c for c in range(n) if c not in piv]
    out = []
    for f in free:
        v = [Fr(0)]*n
        v[f] = Fr(1)
        for p, row in zip(piv, red):
            v[p] = -row[f]
        out.append(v)
    return out


# ---- load relocated baseline, build contract ----
base_path = Path(A.baseline)
spec = importlib.util.spec_from_file_location('baseline', base_path)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
con = base.make_contract('unequal', 'rational')
names = con['variables'] + ['lambda2', 'lambda3']
need(len(names) == 269, '269 names')
need(con['counts']['planned_all_rows'] + 105 == 803, '803 rows')
need(con['counts']['jacobian_envelope_rows'] == 660, '660 envelope')
ids = {n: k for k, n in enumerate(names)}
Amap, Bmap = con['coefficient_maps']


def val(e):
    f = base.decode(e['fixed'])
    need(f.b == 0, 'rational branch')
    return f.a


fixedA = {tuple(e['point']): val(e) for e in Amap if 'fixed' in e}
fixedB = {tuple(e['point']): val(e) for e in Bmap if 'fixed' in e}
freeA = {tuple(e['point']): e['name'] for e in Amap if 'variable' in e}
freeB = {tuple(e['point']): e['name'] for e in Bmap if 'variable' in e}
need(len(freeA) == 71 and len(freeB) == 196, 'free counts 71/196')
H = {(0, 5): Fr(1), (3, 2): Fr(1)}                     # pi^2 (pi^3 + gamma^3)
A15 = {m: c for m, c in fixedA.items() if sum(m) == 15 and c}
B25 = {m: c for m, c in fixedB.items() if sum(m) == 25 and c}
need(A15 == ppow(H, 3) and B25 == ppow(H, 5), 'outer faces are H^3, H^5')
lowA = {m: c for m, c in fixedA.items() if sum(m) < 15 and c}
lowB = {m: c for m, c in fixedB.items() if sum(m) < 25 and c}
need(lowA == {(2, 1): Fr(1)} and lowB == {(1, 0): Fr(5, 9), (8, 5): Fr(5, 3)},
     'lower fixed nonzero faces')
need(fixedA.get((0, 0)) == 0 and fixedB.get((0, 0)) == 0, 'fixed origins')

# ---- weights built from the report formulas, independent of check.py ----
W1, W2, W3 = [], [], []
for n in names:
    if n.startswith('lambda'):
        W1.append({'lambda2': 3, 'lambda3': 2}[n]); W2.append(0); W3.append(0)
        continue
    mem, g, p = n[0], int(n.split('_g')[1].split('_p')[0]), int(n.split('_p')[1])
    tot = 15 if mem == 'A' else 25
    W1.append(tot-g-p)
    W2.append(tot-g-p if mem == 'B' else 0)
    W3.append(g if mem == 'B' else 0)
if A.mutate == 'w2':
    W2 = [0]*269
if A.mutate == 'w3':
    W3 = [-w for w in W3]
need(min(W1) == 1 and max(W1) == 24, 'W1 range 1..24')


def key(mono):
    cnt = {}
    for v in mono:
        cnt[v] = cnt.get(v, 0) + 1
    return (sum(W1[v] for v in mono), sum(W2[v] for v in mono), sum(W3[v] for v in mono),
            len(mono)) + tuple(-cnt.get(v, 0) for v in range(268, -1, -1))


# ---- descriptor / ring digests ----
wit = json.loads(Path(A.witnesses).read_text())
need(wit['order']['variables'] == names, 'witness names equal contract names')
tie = 'lp' if A.mutate == 'tiebreak' else 'dp'
desc = {'schema': 'jc2.d125-defect-order/v1', 'field': 'Q', 'variables': names,
        'weight_rows': [W1, W2, W3], 'tie_break': tie,
        'comparison': 'lexicographically larger (W1,W2,W3,total,-last,...,-first)'}
order_sha = hashlib.sha256(canonical(desc)).hexdigest()
ring = 'ring R=0,(' + ','.join(names) + '),(' + ','.join(
    'a(' + ','.join(map(str, r)) + ')' for r in (W1, W2, W3)) + ',' + tie + ');\n'
ring_sha = hashlib.sha256(ring.encode()).hexdigest()
if A.mutate not in ('w2', 'w3'):
    need(wit['order']['weight_rows'] == [W1, W2, W3], 'witness weight rows equal own rows')
if A.mutate not in ('w2', 'w3'):
    need(order_sha == '64c212c26a9883d1c0f674b93f0246f67e22a8b742b643c6628fd3c14014db66',
         'order descriptor digest')
if A.mutate not in ('w2', 'w3'):
    need(ring_sha == 'd894d6427d39b774c403165c83bffddbe993b96345ee00d652f5af7a06219bca',
         'ring declaration digest')
    need(wit['ring_declaration'] == ring, 'witness ring string')

# ---- blocks by explicit bracket; envelope; pivots; kernels ----
I_MAX = 21 if A.mutate == 'envelope' else 23
blocks, ranks, cols_total, pivkey = [], 0, 0, {}
for d in range(1, 25):
    cols = sorted(i for (i, j) in freeB if i+j == d)
    q = (7*d+4)//12
    need(cols == list(range(q+1)), f'free columns d={d}')
    mats = {}
    used_rows = set()
    for i in cols:
        br = bracket(A15, {(i, d-i): Fr(1)})
        for (r, s), c in br.items():
            need(r+s == d+13, 'layer degree')
            need(r <= I_MAX and r+s <= 38 and s >= 0, f'row outside envelope d={d} r={r}')
            mats[(r, i)] = c
            # report formula M[r,i]=(p*d-15*i)*h_p, p=r+1-i
            p = r+1-i
            hp = {0: 1, 3: 3, 6: 3, 9: 1}.get(p, 0)
            need(c == (p*d-15*i)*hp, 'matrix entry formula')
            used_rows.add(r)
    nrow = d+14
    M = [[mats.get((r, i), Fr(0)) for i in cols] for r in range(nrow)]
    piv, red = rref(M, list(reversed(cols)))
    exp = list(range(q, 0, -1)) if d % 5 == 0 else list(range(q, -1, -1))
    need(piv == exp, f'pivot columns d={d}')
    ranks += len(piv); cols_total += len(cols)
    # leading monomial of each reduced row's free-B_d part must be the pivot
    for pc, row in zip(piv, red):
        support = [c for c in cols if row[c]]
        need(row[pc] == 1, 'monic pivot')
        lead = max(support, key=lambda c: key((ids[freeB[(c, d-c)]],)))
        need(lead == pc, f'reduced row leads at pivot d={d} col={pc}')
        pk = key((ids[freeB[(pc, d-pc)]],))
        pivkey[d] = min(pivkey.get(d, pk), pk)
    kern = None
    if d % 5 == 0:
        ns = nullspace(M, len(cols))
        need(len(ns) == 1, 'kernel dimension 1')
        Hr = ppow(H, d//5)
        vec = [Hr.get((i, d-i), Fr(0)) for i in cols]
        need(all(i <= q for (i, j) in Hr), 'H^r inside free columns')
        need(vec[0] == 1, 'monic pi^d kernel scalar')
        v = ns[0]
        need(all(v[k]*vec[0] == vec[k]*v[0] for k in range(len(cols))), 'kernel is H^(d/5)')
        kern = freeB[(0, d)]
    else:
        need(not nullspace(M, len(cols)), 'no kernel off multiples of 5')
    blocks.append({'d': d, 'columns': len(cols), 'rank': len(piv), 'pivots': piv,
                   'kernel_scalar': kern, 'max_row_gamma': max(used_rows)})
need(cols_total == 196 and ranks == 192, 'sums 196/192')
need([b['kernel_scalar'] for b in blocks if b['kernel_scalar']] ==
     ['B_g0_p5', 'B_g0_p10', 'B_g0_p15', 'B_g0_p20'], 'four kernel scalars')

# ---- actual slot-pair forcing census (no J coefficient formed) ----
pairs = 0; worst = None
Aslots = [(m, freeA.get(m)) for m in list(freeA) + list(lowA)]
Bslots = [(m, freeB.get(m)) for m in list(freeB) + list(lowB) + list(B25)]
for (i, j), an in Aslots:
    if i+j >= 15:
        continue
    for (k, l), bn in Bslots:
        d = i+j+k+l-15
        if not 1 <= d <= 24 or i*l-j*k == 0:
            continue
        mono = tuple(sorted(ids[x] for x in (an, bn) if x))
        kk = key(mono)
        need(kk < pivkey[d], f'forcing monomial not below every pivot of block d={d}: {an},{bn}')
        pairs += 1
        gap = (25-d, 25-d, 0, 0)  # smallest pivot key prefix has W3>=0 (nonkernel col 0)
        if worst is None or kk[:2] > worst[0]:
            worst = (kk[:2], d, an, bn)
# K_d forcing is a constant: [H^3,K_d] has no variable, key prefix (0,0).
for m, c in lowB.items():
    need(bracket(A15, {m: c}), 'K_d bracket nonzero constant forcing')
# kernel marking: B_g3_p2 must exceed B_g0_p5
need(key((ids['B_g3_p2'],)) > key((ids['B_g0_p5'],)), 'W3 kernel marking')

# ---- tiny GB comparator controls in Q[x,y,z] ----
def gb_key(m, w):
    return (sum(a*b for a, b in zip(m, w)), sum(m)) + tuple(-e for e in reversed(m))


def lm(f, w):
    return max(f, key=lambda m: gb_key(m, w))


def nf(f, G, w):
    f = dict(f); r = {}
    while f:
        m = lm(f, w); c = f[m]
        for g in G:
            gm = lm(g, w)
            if all(a >= b for a, b in zip(m, gm)):
                q = tuple(a-b for a, b in zip(m, gm)); s = c/g[gm]
                for gm2, gc in g.items():
                    mm = tuple(a+b for a, b in zip(gm2, q))
                    f[mm] = f.get(mm, 0) - s*gc
                    if not f[mm]:
                        del f[mm]
                break
        else:
            r[m] = c; del f[m]
    return r


def spoly(f, g, w):
    a, b = lm(f, w), lm(g, w)
    L = tuple(max(x, y) for x, y in zip(a, b))
    out = {}
    for h, lead, sign in ((f, a, 1), (g, b, -1)):
        q = tuple(x-y for x, y in zip(L, lead)); s = Fr(sign)/h[lead]
        for m, c in h.items():
            mm = tuple(x+y for x, y in zip(m, q))
            out[mm] = out.get(mm, 0) + s*c
    return {m: c for m, c in out.items() if c}


def is_gb(G, w):
    return all(not nf(spoly(G[i], G[j], w), G, w) for i in range(len(G)) for j in range(i+1, len(G)))


x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
Gb = [{x: Fr(1), (0, 2, 0): Fr(-1)}, {z: Fr(1), (0, 3, 0): Fr(-1)}]
wt, dp = (3, 1, 4), (0, 0, 0)
need([lm(g, wt) for g in Gb] == [x, z], 'control b: weighted leaders x,z')
need(is_gb(Gb, wt) and nf({(0, 0, 0): Fr(1)}, Gb, wt), 'control b: weighted GB, NF(1) nonzero')
need(not is_gb(Gb, dp), 'control b: not a dp GB')
rem = nf(spoly(Gb[0], Gb[1], dp), Gb, dp)
need(set(rem) == {(1, 1, 0), z}, 'control b: dp S remainder is x*y-z up to sign')
Gd = [{(1, 1, 0): Fr(1), (0, 0, 0): Fr(-1)}, {(2, 0, 0): Fr(1)}]
need(not is_gb(Gd, wt) and not is_gb(Gd, dp), 'control d: (xy-1,x^2) fails Buchberger')

out = {'status': 'OWN_GATE_PASS', 'mutate': A.mutate, 'order_sha256': order_sha,
       'ring_declaration_sha256': ring_sha, 'blocks': blocks, 'free_B': cols_total,
       'B_linear_leaders': ranks, 'forcing_slot_pairs': pairs,
       'largest_forcing_W1W2': [worst[0], worst[1], worst[2], worst[3]],
       'envelope_gamma_max_used': max(b['max_row_gamma'] for b in blocks),
       'graph_complement': 269-ranks}
Path(A.out).write_bytes(canonical(out))
print(canonical({k: v for k, v in out.items() if k != 'blocks'}).decode(), end='')
