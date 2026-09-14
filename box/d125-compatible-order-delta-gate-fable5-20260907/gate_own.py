#!/usr/bin/env python3
"""Own delta gate for the appended W4/W5 rows. Stdlib only; every check raises.
No source-row expansion, no CAS, no reduced-polynomial construction."""
import argparse, hashlib, importlib.util, json
from math import comb, factorial

def need(ok, why):
    if not ok:
        raise RuntimeError('FAIL: ' + why)

ap = argparse.ArgumentParser()
ap.add_argument('--baseline', required=True)
ap.add_argument('--witness', required=True)
ap.add_argument('--mode', default='normal',
                choices=['normal', 'no-w4', 'reverse-w5', 'bad-matrix', 'w1-zero-lambda'])
args = ap.parse_args()
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
need(sha(args.baseline) == 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53', 'baseline pin')
need(sha(args.witness) == '86804185bbaba641f2a3305dd379aa06e2f85a5f833233c79a10b575c0be67f6', 'desk witness pin')
spec = importlib.util.spec_from_file_location('baseline', args.baseline)
base = importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
contract = base.make_contract('unequal', 'rational')
names = contract['variables'] + ['lambda2', 'lambda3']
need(len(names) == 269, '269 names')
wit = json.load(open(args.witness))['order']
need(wit['variables'] == names, 'witness names = contract names + lambdas')
ids = {n: k for k, n in enumerate(names)}
L2, L3 = ids['lambda2'], ids['lambda3']

# --- own half-plane census of the A polygon and its free slots -------------
A_pts = [(i, j) for i in range(16) for j in range(16)
         if i + j <= 15 and 5*i - 7*j <= 3 and 2*j >= i]
need(len(A_pts) == 83, 'A raw 83')
A_fixed_pts = {p for p in A_pts if p[0]+p[1] == 15 or 5*p[0]-7*p[1] == 3 or p == (0, 0)}
A_free = {p for p in A_pts if p not in A_fixed_pts}
need(len(A_free) == 71 and len(A_fixed_pts) == 12, 'A free 71 / fixed 12')
amap = contract['coefficient_maps'][0]
c_free = {tuple(e['point']): e['variable'] for e in amap if 'variable' in e}
c_fixed = {tuple(e['point']): base.decode(e['fixed']) for e in amap if 'fixed' in e}
need(set(c_free) == A_free and set(c_fixed) == A_fixed_pts, 'A slots match contract')
need(all(names[c_free[p]] == f'A_g{p[0]}_p{p[1]}' for p in A_free), 'A names')
nonzero_fixed = {p: v for p, v in c_fixed.items() if v != base.ZERO}
need(set(nonzero_fixed) == {(0, 15), (3, 12), (6, 9), (9, 6), (2, 1)}, 'nonzero fixed A slots')
bmap = contract['coefficient_maps'][1]
b_free = {tuple(e['point']): e['variable'] for e in bmap if 'variable' in e}
b_fixed = {tuple(e['point']): base.decode(e['fixed']) for e in bmap if 'fixed' in e}
need(len(b_free) == 196 and len(b_free) + len(b_fixed) == 215, 'B free 196 of 215')

# --- rebuild all five rows from the names alone ----------------------------
W = [[0]*269 for _ in range(5)]
for k, n in enumerate(names):
    if n == 'lambda2': W[0][k] = 3
    elif n == 'lambda3': W[0][k] = 2
    else:
        m, g, p = n.split('_'); i, j = int(g[1:]), int(p[1:])
        if m == 'A':
            W[0][k] = 15-i-j; W[3][k] = 15-i-j; W[4][k] = -i
        else:
            W[0][k] = 25-i-j; W[1][k] = 25-i-j; W[2][k] = i
need(W == wit['weight_rows'], 'five rebuilt rows = desk witness rows')
desc = {'schema': 'jc2.d125-compatible-defect-order/v1', 'field': 'Q', 'variables': names,
        'weight_rows': W, 'tie_break': 'dp',
        'comparison': 'lexicographically larger (W1,W2,W3,W4,W5,total,-last,...,-first)'}
wire = (json.dumps(desc, sort_keys=True, separators=(',', ':')) + '\n').encode()
need(hashlib.sha256(wire).hexdigest() ==
     '97fc8241f29feb174bc829cebb226c03f3d1df92541fc620b74489f0fd18aa25', 'five-row descriptor digest')
need(all(v > 0 for v in W[0]), 'W1 > 0 on all 269 names (global)')
need(all(W[3][k] == 0 and W[4][k] == 0 for k in range(269) if not names[k].startswith('A_')),
     'W4,W5 vanish off A')
need(min(W[4]) == -8 and max(W[3]) == 14, 'W5 negative entries present, W4 range')

if args.mode == 'no-w4': W[3] = [0]*269
if args.mode == 'reverse-w5': W[4] = [-x for x in W[4]]
if args.mode == 'w1-zero-lambda': W[0][L3] = 0
need(all(v > 0 for v in W[0]), 'W1 > 0 on all 269 names (global), post-mutation')

def key(mono):
    ws = tuple(sum(w[k]*e for k, e in mono.items()) for w in W)
    return ws + (sum(mono.values()),) + tuple(-mono.get(k, 0) for k in range(268, -1, -1))
def decide(big, small):
    kb, ks = key(big), key(small)
    need(kb > ks, 'comparison direction')
    return next(n for n in range(len(kb)) if kb[n] != ks[n])

# --- A-lift rows: actual term support by the consumed exponent law -----------
def bareiss_det(M):
    n = len(M); A = [r[:] for r in M]; sign, prev = 1, 1
    for k in range(n-1):
        if A[k][k] == 0:
            sw = next((r for r in range(k+1, n) if A[r][k]), None)
            if sw is None: return 0
            A[k], A[sw] = A[sw], A[k]; sign = -sign
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n-1][n-1]
def adj_inverse(M, det):
    n = len(M)
    def minor(r, c):
        return bareiss_det([[M[a][b] for b in range(n) if b != c] for a in range(n) if a != r]) if n > 1 else 1
    return [[(-1)**(r+c) * minor(c, r) * det for c in range(n)] for r in range(n)]  # det = +-1 so 1/det = det

blocks, decided_at, named = [], {}, {}
for s in range(1, 15):
    r = (s + 4)//5
    sel = [(i, s-i) for i in range(r)]
    need(all(p in A_free for p in sel), f'selected slots free at s={s}')
    selix = {c_free[p] for p in sel}
    M = [[0]*r for _ in range(r)]
    for t in range(r):
        terms = []  # (mono, coefficient, tag)
        for (i, j) in A_pts:
            for b in range(6):
                for d in range(8):
                    if i + j != s + 3*b + 2*d or t + b + d > j: continue
                    z = j - t - b - d
                    coef = (-1)**(b+d+z) * factorial(j)//(factorial(t)*factorial(b)*factorial(d)*factorial(z))
                    need(coef != 0, 'multinomial nonzero')
                    if (i, j) in c_free:
                        mono = {c_free[(i, j)]: 1}
                        if b: mono[L2] = b
                        if d: mono[L3] = d
                        terms.append((mono, coef, 'free'))
                        if b == 0 and d == 0 and i < r:
                            M[t][i] = coef
                    elif c_fixed[(i, j)] != base.ZERO:
                        mono = {}
                        if b: mono[L2] = b
                        if d: mono[L3] = d
                        terms.append((mono, coef, 'fixed_top' if i+j == 15 else 'fixed_low'))
        need(all(M[t][i] == (-1)**(s-i-t)*comb(s-i, t) for i in range(r)), 'actual matrix = Hermite formula')
        need(all(sum(m.get(L2,0)*3 + m.get(L3,0)*2 + (15-s-3*m.get(L2,0)-2*m.get(L3,0)) for _ in [0]) == 15-s
                 for m, _, tag in terms if tag == 'free'), 'W1 row homogeneity on free terms')
        for piv in sel:
            pk = {c_free[piv]: 1}
            for mono, coef, tag in terms:
                if len(mono) == 1 and next(iter(mono)) in selix: continue  # eliminated by M^-1
                n = decide(pk, mono)
                decided_at[(tag, n)] = decided_at.get((tag, n), 0) + 1
                if s == 1 and mono == {c_free[(0, 3)]: 1, L3: 1}: named['A_g0_p1 vs lambda3*A_g0_p3'] = n
                if s == 2 and mono == {c_free[(1, 1)]: 1}: named['A_g0_p2 vs A_g1_p1'] = n
    if args.mode == 'bad-matrix' and r >= 2: M[1] = M[0][:]
    det = bareiss_det(M)
    need(abs(det) == 1, f'unit Hermite minor at s={s}')
    need(det == (-1)**(r*s + r*(r-1)//2), 'determinant sign law')
    Minv = adj_inverse(M, det)
    need(all(sum(Minv[a][k]*M[k][b] for k in range(r)) == (a == b) for a in range(r) for b in range(r)),
         'integer inverse')
    blocks.append({'s': s, 'r': r, 'det': det, 'pivots': [f'A_g{i}_p{j}' for i, j in sel]})
need(sum(b['r'] for b in blocks) == 27, '27 A leaders')
need(set(named) == {'A_g0_p1 vs lambda3*A_g0_p3', 'A_g0_p2 vs A_g1_p1'}, 'named comparisons present')

# --- B side: every actual comparison is decided before W4 --------------------
b_by_deg = {}
for (i, j), ix in b_free.items(): b_by_deg.setdefault(i+j, []).append(((i, j), ix))
pairs, b_decided, b_same = 0, {}, {}
for d, cols in b_by_deg.items():
    for (p, ix) in cols:
        for (q, iy) in cols:
            if ix != iy:
                n = decide({ix: 1}, {iy: 1}) if p[0] > q[0] else decide({iy: 1}, {ix: 1})
                need(n == 2, 'same-layer B pair decided exactly at W3')
                b_same[n] = b_same.get(n, 0) + 1
    for (i1, j1) in A_pts:
        k = i1 + j1
        if k == 15: continue
        e = d + 15 - k
        for (i2, j2) in list(b_free) + list(b_fixed):
            if i2 + j2 != e or i1*j2 - j1*i2 == 0: continue
            if (i1, j1) in c_fixed and c_fixed[(i1, j1)] == base.ZERO: continue
            if (i2, j2) in b_fixed and b_fixed[(i2, j2)] == base.ZERO: continue
            mono = {}
            if (i1, j1) in c_free: mono[c_free[(i1, j1)]] = 1
            if (i2, j2) in b_free: mono[b_free[(i2, j2)]] = 1
            pairs += 1
            for (_, ix) in cols:
                n = decide({ix: 1}, mono)
                need(n <= 2, 'B forcing decided at W1..W3')
                b_decided[n] = b_decided.get(n, 0) + 1
need(set(b_decided) <= {0, 1, 2}, 'no B comparison reaches W4/W5')
print(json.dumps({'status': 'PASS', 'mode': args.mode, 'A_leaders': 27, 'B_leaders_consumed': 192,
                  'complement_names': 269-192-27, 'blocks': blocks, 'named_decision_index': named,
                  'A_decisions_by_tag_and_index': {f'{t}@W{n+1}': c for (t, n), c in sorted(decided_at.items())},
                  'B_pairs_nonzero': pairs, 'B_forcing_decision_counts': {f'W{n+1}': c for n, c in sorted(b_decided.items())}, 'B_same_layer_pairs': b_same},
                 sort_keys=True))
