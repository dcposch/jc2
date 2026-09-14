#!/usr/bin/env python3
"""Fable gate: specialisation CONTROL by a different route (direct, unfactored Jacobian of
explicit bivariate F,G with rational coefficients; no bracket identity) plus explicit
negative mutation controls.  A specialisation is a control only; exact identity is
review_reconstruct.py.  Read-only on producer files."""
import json, ast, math, time, resource
from fractions import Fraction
from pathlib import Path
import os, socket
if socket.gethostname() != 'ip-172-30-0-56' or Path('/sys/class/dmi/id/sys_vendor').read_text().strip() != 'Amazon EC2' or os.environ.get('JC2_REGISTERED_JOB') != 'factored-jacobian-root-replay-20260906':
    raise RuntimeError('Registered AWS worker only')
from flint import fmpq_mpoly, fmpq_mpoly_ctx, fmpq
PILOT = Path('/home/ubuntu/factored-jacobian-pilot-20260906'); OUT = Path('/home/ubuntu/factored-jacobian-root-replay-20260906')
T0 = time.monotonic()
def log(**kw): print(json.dumps({"t": round(time.monotonic()-T0, 1), **kw}, sort_keys=True), flush=True)
data = json.loads((PILOT/'delta2_stage8.strongest.json').read_bytes()); maps = data['maps']; NORM = {'h3': 11, 'C2': 22, 'C3': 33, 'B2': 65, 'A3': 98}
with (PILOT/'complete_export.generators.jsonl').open() as f: header = json.loads(f.readline())
names = header['variables']; src = [n for n in names if not n.startswith('Hfact_') and n != 'Zj']
point = {n: Fraction(((k*37+11) % 23)+1) for k, n in enumerate(src)}
def evn(node, env):
    if isinstance(node, ast.Constant): return Fraction(node.value)
    if isinstance(node, ast.Name): return env[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -evn(node.operand, env)
    if isinstance(node, ast.BinOp):
        l, r = evn(node.left, env), evn(node.right, env)
        if isinstance(node.op, ast.Add): return l+r
        if isinstance(node.op, ast.Sub): return l-r
        if isinstance(node.op, ast.Mult): return l*r
        if isinstance(node.op, ast.Div): return l/r
        if isinstance(node.op, ast.Pow): return l**int(r)
    raise ValueError(ast.dump(node))
def table(key, env, wsign=1):
    N = NORM[key]; out = {}
    for r, z, e in maps[key]:
        v = evn(ast.parse(str(e).replace('^', '**'), mode='eval').body, env)
        if v: out[(N-int(r)-int(z), int(z))] = v*(wsign**int(z))
    return out
def tmul(a, b):
    out = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            p = (i+k, j+l); out[p] = out.get(p, 0)+u*v
    return {p: v for p, v in out.items() if v}
def tadd(*ts):
    out = {}
    for t, s in ts:
        for p, v in t.items(): out[p] = out.get(p, 0)+s*v
    return {p: v for p, v in out.items() if v}
def dX(t): return {(i-1, j): v*i for (i, j), v in t.items() if i}
def dW(t): return {(i, j-1): v*j for (i, j), v in t.items() if j}
def integral(t):
    d = 1
    for v in t.values(): d = d*v.denominator//math.gcd(d, v.denominator)
    return {p: int(v*d) for p, v in t.items()}, d
def jac(F, G):
    Fi, dF = integral(F); Gi, dG = integral(G)
    J = tadd((tmul(dX(Fi), dW(Gi)), 1), (tmul(dW(Fi), dX(Gi)), -1))
    return {p: Fraction(v, dF*dG) for p, v in J.items()}
def build(env, wsign=1, asign=1):
    h3, c2, c3 = table('h3', env, wsign), table('C2', env, wsign), table('C3', env, wsign)
    h = tadd((tmul(tmul(h3, h3), h3), 1), (tmul(c2, h3), 1), (c3, 1)); D = table('B2', env, wsign); C = table('A3', env, wsign)
    a, b = env['target_a'], env['target_b']
    F = tadd((tmul(tmul(h, h), h), 1), (tmul(tadd((D, Fraction(3, 2)), ({(0, 0): Fraction(1)}, asign*a/2)), h), 1), (C, 1))
    G = tadd((tmul(h, h), 1), (h, -b/3), (D, 1))
    return h, F, G
h, F, G = build(point)
log(msg='built F,G at point', degF=max(map(sum, F)), degG=max(map(sum, G)), suppF=len(F), suppG=len(G))
Jdirect = jac(F, G); log(msg='direct Jacobian', support=len(Jdirect), maxdeg=max(map(sum, Jdirect)))
J0 = Jdirect.get((0, 0), Fraction(0))
vals = {}
for n in names:
    if n.startswith('Hfact_'):
        i, j = map(int, n[6:].split('_')); vals[n] = h.get((i, j), Fraction(0))
    elif n == 'Zj': vals[n] = (1/J0) if J0 else Fraction(1)
    else: vals[n] = point[n]
ctx = fmpq_mpoly_ctx.get(tuple(names), ordering='degrevlex')
fv = [fmpq(v.numerator, v.denominator) for v in (vals[n] for n in names)]
def evaluate(p):
    try: return Fraction(str(p(*fv)))
    except Exception:
        consts = [ctx.constant(v.numerator)/v.denominator for v in (vals[n] for n in names)]
        return Fraction(str(p.compose(*consts, ctx=ctx)))
lit = {}; ndef_zero = 0; ndef = 0; inv_val = None; count = 0
with (PILOT/'complete_export.generators.jsonl').open() as f:
    next(f)
    for line in f:
        row = json.loads(line)
        if row['type'] == 'complete': break
        p = fmpq_mpoly(row['polynomial'], ctx=ctx); v = evaluate(p); lab = row['label']
        if lab.startswith('define_'): ndef += 1; ndef_zero += (v == 0)
        elif lab == 'inverse_J': inv_val = v
        else:
            i, j = map(int, lab[2:].split('_')); lit[(i, j)] = v
        count += 1
        if count % 400 == 0: log(rows=count)
log(msg='literal rows evaluated', rows=count)
def compare(J, ref=lit):
    mism = sum(1 for p, v in ref.items() if J.get(p, Fraction(0)) != v)
    extra = sum(1 for p, v in J.items() if p != (0, 0) and p not in ref and v != 0)
    return mism, extra
res = {"point_first_values": {n: str(point[n]) for n in src[:3]}, "J0_at_point": str(J0), "J0_nonzero": J0 != 0,
       "define_rows": ndef, "define_rows_zero_at_point": ndef_zero, "inverse_row_value": str(inv_val),
       "positive_rows": len(lit), "positive_rows_nonzero_at_point": sum(1 for v in lit.values() if v != 0)}
m, e = compare(Jdirect); res['direct_vs_literal'] = {"mismatches": m, "unlisted_nonzero_positions": e, "ok": m == 0 and e == 0}
res['inverse_row_ok'] = (inv_val == vals['Zj']*J0-1 == 0) if J0 else None
# negative controls (each should produce mismatches)
m1, e1 = compare(jac(G, F)); res['control_orientation_J(G,F)'] = {"mismatches": m1, "unlisted": e1}
_, F2, G2 = build(point, asign=-1); m2, e2 = compare(jac(F2, G2)); res['control_a_sign_flipped'] = {"mismatches": m2, "unlisted": e2}
_, F3, G3 = build(point, wsign=-1); m3, e3 = compare(jac(F3, G3)); res['control_W_sign_convention_flipped'] = {"mismatches": m3, "unlisted": e3}
lit2 = dict(lit); k0 = (8, 52); lit2[k0] = lit2[k0]+1; m4, e4 = compare(Jdirect, lit2); res['control_perturbed_row_J_8_52'] = {"mismatches": m4, "unlisted": e4}
lit3 = dict(lit); del lit3[(1, 0)]; m5, e5 = compare(Jdirect, lit3); res['control_dropped_row_J_1_0'] = {"mismatches": m5, "unlisted_nonzero_positions": e5}
res['all_controls_fire'] = all(x > 0 for x in (m1, m2, m3, m4)) and e5 > 0
res['ok'] = res['direct_vs_literal']['ok'] and ndef_zero == ndef == 160 and res['inverse_row_ok'] is True and res['all_controls_fire']
res['wall_seconds'] = time.monotonic()-T0; res['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
(OUT/'scalar_direct_result.json').write_text(json.dumps(res, sort_keys=True, indent=1)+'\n'); log(msg='done', **{k: v for k, v in res.items() if k != 'point_first_values'})
if not res['ok']:
    raise RuntimeError('Direct control failed')
