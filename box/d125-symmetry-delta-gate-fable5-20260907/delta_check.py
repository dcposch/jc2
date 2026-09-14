#!/usr/bin/env python3
"""Independent mu2 fixed-locus delta checks (Fable 5.1 gate). Explicit frozen paths.
Tiny exact Laurent/polygon/matrix computations only; no full row expansion, no solver."""
import ast, hashlib, json, random, resource, subprocess, sys
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

FROZEN = Path('/tmp/jc2-lane.kcXJUO/inputs')
HERE = Path(__file__).resolve().parent
PINS = {'client.py': 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
        'exact-witnesses-v2.json': '07b4ce881b4f90f9a41a3f8cb01fcd3a120ff64a4f04969e60126dbdb6e7f246',
        'witness.json': '9c3708294dc3c0df25cb256598436db5736a9737a2504dada04d0777171c2e4a'}

def need(ok, msg):
    if not ok:
        raise ValueError(msg)

def clean(d): return {k: v for k, v in d.items() if v != 0}
def padd(a, b):
    out = dict(a)
    for k, v in b.items(): out[k] = out.get(k, 0)+v
    return clean(out)
def pmul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            out[(i+k, j+l)] = out.get((i+k, j+l), 0)+x*y
    return clean(out)
def pscale(a, c): return clean({k: v*c for k, v in a.items()})
def pdiff(a, var):
    out = {}
    for (i, j), x in a.items():
        if var == 0 and i: out[(i-1, j)] = out.get((i-1, j), 0)+i*x
        if var == 1 and j: out[(i, j-1)] = out.get((i, j-1), 0)+j*x
    return clean(out)
def jac(a, b): return padd(pmul(pdiff(a, 0), pdiff(b, 1)), pscale(pmul(pdiff(a, 1), pdiff(b, 0)), -1))
def ppow(a, n):
    out = {(0, 0): Fr(1)}
    for _ in range(n): out = pmul(out, a)
    return out

DEG = {'A': 15, 'B': 25}; TOP = {'A': 3, 'B': 5}
def inside(m, i, j): return i >= 0 and j >= 0 and i+j <= DEG[m] and 5*i-7*j <= TOP[m] and (m == 'B' or i <= 2*j)
def slots(m): return [(i, j) for i in range(DEG[m]+1) for j in range(DEG[m]+1-i) if inside(m, i, j)]
def is_fixed(m, i, j): return (i, j) == (0, 0) or i+j == DEG[m] or 5*i-7*j == TOP[m]
H = {(0, 5): Fr(1), (3, 2): Fr(1)}
OUTER = {'A': ppow(H, 3), 'B': ppow(H, 5)}
INNER = {'A': {(2, 1): Fr(1), (9, 6): Fr(1)}, 'B': {(1, 0): Fr(5, 9), (8, 5): Fr(5, 3), (15, 10): Fr(1)}}
def fixed_value(m, i, j):
    if (i, j) == (0, 0): return Fr(0)
    v = None
    if i+j == DEG[m]: v = OUTER[m].get((i, j), Fr(0))
    if 5*i-7*j == TOP[m]:
        w = INNER[m].get((i, j), Fr(0)); need(v is None or v == w, 'face conflict'); v = w
    return v

def lift(coeffs, l2, l3, u_power=4):
    p = {(1, u_power): Fr(1), (0, -1): Fr(-1)}
    if l2: p[(0, 2)] = -Fr(l2)
    if l3: p[(0, 1)] = -Fr(l3)
    maxj = max(j for _, j in coeffs)
    pp = [{(0, 0): Fr(1)}]
    for _ in range(maxj): pp.append(pmul(pp[-1], p))
    out = {}
    for (i, j), c in coeffs.items():
        for (t, e), x in pp[j].items():
            out[(t, e-i)] = out.get((t, e-i), 0)+c*x
    return clean(out)

def rank_kernel(matrix, ncols):
    a = [[Fr(x) for x in row] for row in matrix]; r = 0; piv = []
    for c in range(ncols):
        k = next((k for k in range(r, len(a)) if a[k][c]), None)
        if k is None: continue
        a[r], a[k] = a[k], a[r]; z = a[r][c]; a[r] = [x/z for x in a[r]]
        for k2 in range(len(a)):
            if k2 != r and a[k2][c]:
                z = a[k2][c]; a[k2] = [x-z*y for x, y in zip(a[k2], a[r])]
        piv.append(c); r += 1
    return r, piv

def det(matrix):
    a = [[Fr(x) for x in row] for row in matrix]; d = Fr(1)
    for i in range(len(a)):
        k = next((k for k in range(i, len(a)) if a[k][i]), None)
        if k is None: return Fr(0)
        if k != i: a[i], a[k] = a[k], a[i]; d = -d
        d *= a[i][i]
        for k in range(i+1, len(a)):
            f = a[k][i]/a[i][i]; a[k] = [x-f*y for x, y in zip(a[k], a[i])]
    return d

def compose(F, G):  # F=(F1,F2) in (x,y); substitute x=G1,y=G2
    out = []
    for f in F:
        acc = {}
        for (i, j), c in f.items():
            acc = padd(acc, pscale(pmul(ppow(G[0], i), ppow(G[1], j)), c))
        out.append(acc)
    return out

def main(mutation):
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))), 'Assert node')
    hashes = {k: hashlib.sha256((FROZEN/k).read_bytes()).hexdigest() for k in PINS}
    need(hashes == PINS, 'frozen input pins')
    prod = json.loads((FROZEN/'witness.json').read_bytes())
    comp = json.loads((FROZEN/'composition-witness.json').read_bytes())
    repaired = json.loads((FROZEN/'exact-witnesses-v2.json').read_bytes())
    rng = random.Random(20260907)
    rnd = lambda: Fr(rng.randint(-9, 9), rng.randint(1, 5))
    lam_w = [-3, -2]
    if mutation == '--mutate-lambda-weight': lam_w = [-2, -2]
    u_power = 4 if mutation != '--mutate-source-action' else 3
    tau = Fr(3)
    W = {}
    for m in 'AB':
        D = DEG[m]; pts = slots(m); free = [p for p in pts if not is_fixed(m, *p)]
        nzfixed = [(p, fixed_value(m, *p)) for p in pts if is_fixed(m, *p) and fixed_value(m, *p) != 0]
        need(all((i+j-D) % 12 == 0 for (i, j), _ in nzfixed), 'nonzero fixed slot outside mu12 character 0')
        vals = {p: fixed_value(m, *p) for p in pts if is_fixed(m, *p)}
        need(all(vals[p] != 0 for p in ((0, D), (9, 6) if m == 'A' else (15, 10), (2, 1) if m == 'A' else (1, 0))), 'vertex guard zero')
        # 1. exact torus covariance of the literal lift on a random full point (all slots, both lambdas)
        coeffs = {p: (vals[p] if p in vals else rnd()) for p in pts}; l2, l3 = rnd(), rnd()
        P = lift(coeffs, l2, l3, u_power)
        ct = {(i, j): c*tau**(i+j-D) for (i, j), c in coeffs.items()}
        Pt = lift(ct, l2*tau**lam_w[0], l3*tau**lam_w[1], u_power)
        need(Pt == {(t, e): c*tau**(5*t-e-D) for (t, e), c in P.items()}, 'source action covariance u->tau^5 u, v->tau^-1 v')
        negrows = [(t, e) for t in range((D-1)//5+1) for e in range(5*t-D, 0)]
        need(set(k for k in P if k[1] < 0) <= set(negrows), 'negative-row envelope')
        # top rows: outer face alone, all-lambda-free, vanish by multiplicity of H^k at p=-1
        top = lift({p: OUTER[m].get(p, Fr(0)) for p in pts if sum(p) == D}, 0, 0)
        tops = [(t, 5*t-D) for t in range((D-1)//5+1)]
        need(all(top.get(r, 0) == 0 for r in tops), 'fixed-top rows vanish')
        # Hermite levels by actual expansion (lambda-free part)
        levels = {}
        for s in range(1, D):
            r = (s+4)//5; piv = [(i, s-i) for i in range(r)]
            need(all(inside(m, *p) and not is_fixed(m, *p) for p in piv), 'pivot slot not free')
            M = [[lift({piv[i]: Fr(1)}, 0, 0).get((t, 5*t-s), 0) for i in range(r)] for t in range(r)]
            need(abs(det(M)) == 1, 'Hermite block not unimodular')
            need(M == [[(-1)**(s-i-t)*comb(s-i, t) for i in range(r)] for t in range(r)], 'closed-form block')
            levels[s] = piv
        loci = {}
        for n in (2, 3, 4, 6, 12):
            sel = [p for p in free if (sum(p)-D) % n == 0]
            pv = [p for s, ps in levels.items() if (s-D) % n == 0 for p in ps]
            need(set(pv) <= set(sel), 'pivot outside fixed locus')
            rows = [r for r in negrows if (5*r[0]-r[1]-D) % n == 0]
            loci[n] = {'free': len(sel), 'pivots': len(pv), 'neg_rows': len(rows), 'sel': sel}
        need(loci[2]['neg_rows']-len(tops) == loci[2]['pivots'], 'surviving mu2 negative rows != top + pivots')
        W[m] = {'raw': len(pts), 'free': len(free), 'hermite_all': sum(len(v) for v in levels.values()), 'neg_rows': len(negrows),
                'loci': {n: {k: v for k, v in d.items() if k != 'sel'} for n, d in loci.items()}, '_loci': loci, '_vals': vals, '_pts': pts}
    need([W['A']['free'], W['B']['free']] == [71, 196] and [W['A']['hermite_all'], W['B']['hermite_all']] == [27, 70], 'baseline counts')
    counts = {n: {'raw': sum(w % n == 0 for w in (-3, -2))+W['A']['loci'][n]['free']+W['B']['loci'][n]['free'],
                  'hermite': sum(w % n == 0 for w in (-3, -2))+sum(W[m]['loci'][n]['free']-W[m]['loci'][n]['pivots'] for m in 'AB')} for n in (2, 3, 4, 6, 12)}
    need(counts[2] == {'raw': 128, 'hermite': 81} and counts[3] == {'raw': 81, 'hermite': 51}, 'mu2/mu3 counts')
    need([W[m]['loci'][2]['pivots'] for m in 'AB'] == [13, 34] and [W[m]['loci'][2]['neg_rows'] for m in 'AB'] == [16, 39], 'mu2 pivot/row counts')
    need(all(prod['counts'][str(n)]['raw_variables'] == counts[n]['raw'] and prod['counts'][str(n)]['hermite_variables'] == counts[n]['hermite'] for n in (2, 3, 4, 6, 12)), 'producer count agreement')
    # 2. mu3 origin: random fixed-locus point, lambda3=0, lambda2 free: all four linear jets vanish and J constant term vanishes without negative rows
    pt3 = {m: {p: (W[m]['_vals'][p] if p in W[m]['_vals'] else rnd()) for p in W[m]['_pts'] if (sum(p)-DEG[m]) % 3 == 0} for m in 'AB'}
    P3, Q3 = lift(pt3['A'], rnd(), 0), lift(pt3['B'], rnd(), 0)
    need(all(f.get(k, 0) == 0 for f in (P3, Q3) for k in ((1, 0), (0, 1))), 'mu3 linear jet survives')
    poly = lambda f: {k: v for k, v in f.items() if k[1] >= 0}  # the full system imposes every negative row
    need(jac(poly(P3), poly(Q3)).get((0, 0), 0) == 0, 'mu3 Jacobian constant term on the full system')
    # NOTE: without the negative rows the cross terms p(1,-k) q(0,1+k), k=1 mod 3, are both character-allowed (checked below)
    need(any(((k-10) % 3 == 0) and ((-26-k) % 3 == 0) for k in range(1, 16)), 'cross-term bookkeeping')
    # mu4: both lambdas zero, characters mod 4: [u]P and [v]Q vanish, no v-linear term anywhere
    pt4 = {m: {p: (W[m]['_vals'][p] if p in W[m]['_vals'] else rnd()) for p in W[m]['_pts'] if (sum(p)-DEG[m]) % 4 == 0} for m in 'AB'}
    P4, Q4 = lift(pt4['A'], 0, 0), lift(pt4['B'], 0, 0)
    need(P4.get((1, 0), 0) == 0 and Q4.get((0, 1), 0) == 0 and P4.get((0, 1), 0) == 0 and Q4.get((0, 1), 0) == 0, 'mu4 linear jets')
    # 3. mu2 odd toy: receivers g^4p+g^5+g^3, p+g with lambda2=0, lambda3=1 give P=u, Q=uv^4-v, J(0)=-1
    Pt_, Qt_ = lift({(4, 1): Fr(1), (5, 0): Fr(1), (3, 0): Fr(1)}, 0, 1), lift({(0, 1): Fr(1), (1, 0): Fr(1)}, 0, 1)
    need(Pt_ == {(1, 0): 1} and Qt_ == {(1, 4): 1, (0, 1): -1} and jac(Pt_, Qt_) == {(1, 3): 4, (0, 0): -1}, 'odd toy')
    # 4. B graph: [H^3, B_d] on actual odd free columns by real differentiation; rank, kernel, character
    H3 = ppow(H, 3); rows = []; kern = {}
    oddfree = set(W['B']['_loci'][2]['sel'])
    need(oddfree == {tuple(p) for p in prod['members']['B']['fixed_loci']['2']['free_slots']}, 'producer odd B slots')
    for d in range(1, 25, 2):
        cols = sorted(i for i, j in oddfree if i+j == d)
        M = [[jac(H3, {(i, d-i): Fr(1)}).get((r, d+13-r), 0) for i in cols] for r in range(d+14)]
        rk, _ = rank_kernel(M, len(cols)); rows.append([d, len(cols), rk])
        need(rk == len(cols)-(1 if d % 5 == 0 else 0), 'odd B rank')
        if d % 5 == 0:
            hk = ppow(H, d//5); need(set(hk) <= {(i, d-i) for i in cols}, 'H-power outside free columns')
            vec = [hk.get((i, d-i), 0) for i in cols]
            need(all(sum(x*y for x, y in zip(row, vec)) == 0 for row in M), 'H-power not in kernel'); kern[d] = vec
        need(repaired['tables']['unequal'][d-1] == [d, len(cols), rk], 'repaired witness rank row')
    need(rows == comp['odd_B_degree_columns_ranks'] and sum(r[1] for r in rows) == 94 and sum(r[2] for r in rows) == 92, 'odd B totals')
    need(all((d-25) % 2 == 0 for d in kern) and all((d-25) % 2 for d in (10, 20)) and sorted(kern) == [5, 15], 'kernel characters')
    need(all((s-15)+(j-25) == d-25 for d in range(1, 25) for s in range(1, 15) for j in [d+15-s] if d < j <= 25), 'forcing character')
    # 5. whole shear on a random mu2 point: Jacobian, B fixed slots, polygon, parity, kernel slots, inverse; s invariant
    pt2 = {m: {p: (W[m]['_vals'][p] if p in W[m]['_vals'] else rnd()) for p in W[m]['_pts'] if (sum(p)-DEG[m]) % 2 == 0} for m in 'AB'}
    A2, B2 = pt2['A'], pt2['B']; s = B2[(0, 15)]; sign = -1 if mutation != '--mutate-shear-sign' else 1
    Bs = padd(B2, pscale(A2, sign*s))
    need(jac(A2, Bs) == jac(A2, B2), 'shear changes Jacobian')
    need(all(Bs.get(p, 0) == W['B']['_vals'][p] for p in W['B']['_vals']), 'shear moves a fixed B slot')
    need(all(inside('B', *p) and (sum(p)-25) % 2 == 0 for p in Bs), 'shear leaves polygon/parity')
    need(Bs.get((0, 15), 0) == 0 and Bs.get((0, 5), 0) == B2.get((0, 5), 0)-s*A2.get((0, 5), 0), 'shear kernel-slot action')
    need(Bs.get((0, 10), 0) == 0 and Bs.get((0, 20), 0) == 0 and A2.get((0, 10), 0) == 0, 'even kernel slots')
    need(padd(Bs, pscale(A2, s)) == clean(B2) and (15-25) % 2 == 0, 'inverse / s character')
    need(all(A2.get(p, 0) == 0 for p in W['B']['_vals']), 'A support meets B fixed slots')
    # 6. envelopes
    env = [(i, j) for i in range(24) for j in range(39-i)]; tri = [(i, j) for i in range(39) for j in range(39-i)]
    Jfull = jac({p: (W['A']['_vals'].get(p, rnd())) for p in W['A']['_pts']}, {p: (W['B']['_vals'].get(p, rnd())) for p in W['B']['_pts']})
    need(len(env) == 660 and len(tri) == 780 and sum(sum(p) % 2 == 0 for p in env) == 336 and set(Jfull) <= set(env) and max(i for i, _ in Jfull) <= 23, 'Jacobian envelope')
    gmax = max(i for i, _ in Jfull)
    # 7. involution conjugacy invariant: det J is preserved by polynomial conjugation
    phi = [{(1, 0): Fr(1), (0, 2): Fr(1)}, {(0, 1): Fr(1)}]; phinv = [{(1, 0): Fr(1), (0, 2): Fr(-1)}, {(0, 1): Fr(1)}]
    ex = [{(0, 1): Fr(1)}, {(1, 0): Fr(1)}]; ci = [{(1, 0): Fr(-1)}, {(0, 1): Fr(-1)}]
    dets = {}
    for name, sig in (('exchange', ex), ('central', ci)):
        c = compose(phi, compose(sig, phinv)); dets[name] = jac(c[0], c[1])
    need(dets['exchange'] == {(0, 0): -1} and dets['central'] == {(0, 0): 1}, 'conjugacy determinant')
    out = {'status': 'PASS', 'frozen_sha256': hashes, 'members': {m: {k: v for k, v in W[m].items() if not k.startswith('_')} for m in 'AB'},
           'counts': counts, 'odd_B_rows': rows, 'kernel_degrees': sorted(kern), 'slice_coordinates': 33-13+1+1,
           'before_gauge': 33-13+2+1, 'jacobian_envelope': [660, 336, 780], 'generic_J_gdegree_max': gmax, 'conjugacy_dets': {k: str(v[(0, 0)]) for k, v in dets.items()},
           'assert_nodes': 0, 'scope': 'characters/slots/constant matrices/gauge on random exact points; no ideal, point, dimension or runtime claim'}
    return out

def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25)); resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))

MUTS = {'--mutate-lambda-weight': b'source action covariance', '--mutate-source-action': b'source action covariance',
        '--mutate-shear-sign': b'shear kernel-slot action'}
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode == '--record':
        runs = []
        for opt in (False, True):
            for mut in ('',)+tuple(MUTS):
                args = [sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mut] if mut else [])
                run = subprocess.run(args, capture_output=True, timeout=30, preexec_fn=cap)
                need((run.returncode != 0) == bool(mut), 'control exit '+mut)
                if mut: need(MUTS[mut] in run.stderr, 'unrelated failure '+mut)
                else: (HERE/('delta-witness-O.json' if opt else 'delta-witness.json')).write_bytes(run.stdout)
                runs.append({'optimized': opt, 'mutation': mut or None, 'returncode': run.returncode,
                             'stdout_sha256': hashlib.sha256(run.stdout).hexdigest(), 'stderr_tail': run.stderr.decode()[-120:]})
        need((HERE/'delta-witness.json').read_bytes() == (HERE/'delta-witness-O.json').read_bytes(), 'normal/-O mismatch')
        (HERE/'delta-replay.json').write_text(json.dumps({'status': 'PASS', 'runs': runs}, sort_keys=True, indent=1)+'\n')
        print(json.dumps({'status': 'PASS', 'runs': len(runs), 'witness_sha256': hashlib.sha256((HERE/'delta-witness.json').read_bytes()).hexdigest()}))
    else:
        if mode and mode not in MUTS: raise ValueError('unknown mutation')
        print(json.dumps(main(mode), sort_keys=True, indent=1, default=str))
