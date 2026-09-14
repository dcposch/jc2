#!/usr/bin/env python3
"""Fable gate reviewer script (independent of producer code).
Differently organised exact reconstruction: ONE 602-variable flint polynomial
(600 ideal variables + physical X, W), flint-native derivatives and products,
compared as a single exact sparse identity against the tagged sum of the literal
JSONL rows.  Read-only on producer files.  No solve."""
import json, hashlib, ast, re, sys, time, resource
from pathlib import Path
from fractions import Fraction
import os, socket
if socket.gethostname() != 'ip-172-30-0-56' or Path('/sys/class/dmi/id/sys_vendor').read_text().strip() != 'Amazon EC2' or os.environ.get('JC2_REGISTERED_JOB') != 'factored-jacobian-root-replay-20260906':
    raise RuntimeError('Registered AWS worker only')
from flint import fmpq_mpoly, fmpq_mpoly_ctx

PILOT = Path('/home/ubuntu/factored-jacobian-pilot-20260906')
OUT = Path('/home/ubuntu/factored-jacobian-root-replay-20260906')
T0 = time.monotonic()
def rss(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
def log(msg, **kw):
    print(json.dumps({"t": round(time.monotonic()-T0, 2), "rss_kib": rss(), "msg": msg, **kw}, sort_keys=True), flush=True)
res = {"checks": {}}
def rec(name, ok, **kw):
    res["checks"][name] = {"ok": bool(ok), **kw}
    log(("PASS " if ok else "FAIL ") + name, **kw)
    if not ok: res["any_fail"] = True

raw = (PILOT/'delta2_stage8.strongest.json').read_bytes()
res['source_sha256'] = hashlib.sha256(raw).hexdigest()
rec('source_hash', res['source_sha256'] == '778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea')
data = json.loads(raw)
rec('residual_rows_empty', data['residual_rows'] == [])
rec('normalization', data['normalization'] == {'A3': 98, 'B2': 65, 'C2': 22, 'C3': 33, 'h2': 33, 'h3': 11})
maps = data['maps']; NORM = {'h3': 11, 'C2': 22, 'C3': 33, 'B2': 65, 'A3': 98}
ident = re.compile(r'[A-Za-z_][A-Za-z_0-9]*')
srcnames = set()
for k in NORM:
    for r, z, e in maps[k]: srcnames |= set(ident.findall(str(e)))
srcnames = sorted(srcnames | {'target_a', 'target_b'})
rec('source_name_census', len(srcnames) == 439 and set(srcnames) <= set(data['full_free_coordinates']),
    unused=sorted(set(data['full_free_coordinates']) - set(srcnames)))
with (PILOT/'complete_export.generators.jsonl').open() as f: header = json.loads(f.readline())
names = header['variables']
hf = [n for n in names if n.startswith('Hfact_')]
rec('header_ring', header['field'] == 'Q' and header['order'] == 'global dp' and len(names) == 600 and names[-1] == 'Zj'
    and header['source_sha256'] == res['source_sha256'] and header['localizers'] == ['Zj*J0-1'])
rec('variable_order_literal', names == srcnames + hf + ['Zj'], n_source=len(srcnames), n_hfact=len(hf))
allnames = names + ['X', 'W']
ctx = fmpq_mpoly_ctx.get(tuple(allnames), ordering='degrevlex')
G = dict(zip(allnames, ctx.gens())); X = G['X']; W = G['W']; Zj = G['Zj']
one = ctx.constant(1); zero = ctx.constant(0)

def num(node):
    if isinstance(node, ast.Constant) and type(node.value) is int: return Fraction(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -num(node.operand)
    if isinstance(node, ast.BinOp):
        a, b = num(node.left), num(node.right)
        if isinstance(node.op, ast.Add): return a+b
        if isinstance(node.op, ast.Sub): return a-b
        if isinstance(node.op, ast.Mult): return a*b
        if isinstance(node.op, ast.Div): return a/b
        if isinstance(node.op, ast.Pow):
            assert b.denominator == 1 and b >= 0; return a**int(b)
    raise ValueError('non-numeric: ' + ast.dump(node))
def ev(node):
    if isinstance(node, ast.Constant):
        assert type(node.value) is int, 'non-integer literal'; return one*node.value
    if isinstance(node, ast.Name): return G[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -ev(node.operand)
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Pow):
            e = node.right; assert isinstance(e, ast.Constant) and type(e.value) is int and e.value >= 0
            return ev(node.left)**e.value
        if isinstance(node.op, ast.Div):
            assert not any(isinstance(t, ast.Name) for t in ast.walk(node.right)), 'parameter denominator'
            q = num(node.right); return ev(node.left)*q.denominator/q.numerator
        a, b = ev(node.left), ev(node.right)
        if isinstance(node.op, ast.Add): return a+b
        if isinstance(node.op, ast.Sub): return a-b
        if isinstance(node.op, ast.Mult): return a*b
    raise ValueError(ast.dump(node))
def parse_expr(e): return ev(ast.parse(str(e).replace('^', '**'), mode='eval').body)
def table(key):
    N = NORM[key]; out = {}
    for r, z, e in maps[key]:
        r, z = int(r), int(z); assert 0 <= r and 0 <= z and r+z <= N, 'negative physical exponent'
        pos = (N-r-z, z); assert pos not in out, 'duplicate monomial'
        v = parse_expr(e)
        if v: out[pos] = v
    return out
def tmul(a, b):
    out = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            p = (i+k, j+l); out[p] = out.get(p, zero) + u*v
    return {p: v for p, v in out.items() if v}
def tadd(*ts):
    out = {}
    for t in ts:
        for p, v in t.items(): out[p] = out.get(p, zero) + v
    return {p: v for p, v in out.items() if v}
def tdeg(t): return max(i+j for i, j in t)
def poly(t): 
    s = zero
    for (i, j), v in t.items(): s += v*X**i*W**j
    return s

h3, c2, c3 = table('h3'), table('C2'), table('C3'); Dt, Ct = table('B2'), table('A3')
hsrc = tadd(tmul(tmul(h3, h3), h3), tmul(c2, h3), c3)
res['physical'] = {"deg_h3": tdeg(h3), "deg_C2": tdeg(c2), "deg_C3": tdeg(c3), "deg_h": tdeg(hsrc), "deg_D": tdeg(Dt), "deg_C": tdeg(Ct),
                   "support_h": len(hsrc), "support_D": len(Dt), "support_C": len(Ct),
                   "terms_h_source": sum(len(v) for v in hsrc.values()), "max_semdeg_h_source": max(int(v.total_degree()) for v in hsrc.values()),
                   "terms_D": sum(len(v) for v in Dt.values()), "terms_C": sum(len(v) for v in Ct.values()),
                   "max_semdeg_D": max(int(v.total_degree()) for v in Dt.values()), "max_semdeg_C": max(int(v.total_degree()) for v in Ct.values())}
rec('physical_degrees', res['physical']['deg_h'] == 33 and res['physical']['deg_D'] == 34 and res['physical']['deg_C'] == 35 and res['physical']['deg_h3'] == 11
    and res['physical']['deg_C2'] <= 14 and res['physical']['deg_C3'] <= 14, **res['physical'])
htop = poly({p: v for p, v in hsrc.items() if p[0]+p[1] == 33})
rec('h_top_form_fixed', htop == W**24*(X+W)**9 and all(v.total_degree() <= 0 for p, v in hsrc.items() if p[0]+p[1] == 33))
# F,G degrees: h^3 top = htop^3 (nonzero, degree 99); other F terms deg <= max(34+33, 33, 35) = 67; G: h^2 top deg 66, others <= 34
rec('FG_exact_degrees', bool(htop**3) and bool(htop**2) and max(res['physical']['deg_D']+res['physical']['deg_h'], res['physical']['deg_C']) < 99
    and max(res['physical']['deg_D'], res['physical']['deg_h']) < 66, F_top="W^72*(X+W)^27", G_top="W^48*(X+W)^18")
sites = sorted(p for p, v in hsrc.items() if v.total_degree() > 0)
consts = {p: v for p, v in hsrc.items() if v.total_degree() <= 0}
rec('sites_match_Hfact_list', [f'Hfact_{i}_{j}' for i, j in sites] == hf and len(sites) == 160 and len(consts) == 18,
    n_sites=len(sites), constants={f"{i}_{j}": str(v) for (i, j), v in sorted(consts.items())})
Ht = {p: (G[f'Hfact_{p[0]}_{p[1]}'] if p in sites else v) for p, v in hsrc.items()}
Hp, Dp, Cp = poly(Ht), poly(Dt), poly(Ct)
a, b = G['target_a'], G['target_b']
IX = allnames.index('X'); IW = allnames.index('W')
def dX(p):
    try: return p.derivative('X')
    except Exception: return p.derivative(IX)
def dW(p):
    try: return p.derivative('W')
    except Exception: return p.derivative(IW)
def jac(u, v): return dX(u)*dW(v) - dW(u)*dX(v)
log('building brackets')
hd = jac(Hp, Dp); ch = jac(Cp, Hp); cd = jac(Cp, Dp)
log('brackets', hd=len(hd), ch=len(ch), cd=len(cd))
A = (Dp*3 + a + b*Hp)/2; B = Hp*2 - b/3
Ahd = A*hd; log('A*hd', terms=len(Ahd))
Bch = B*ch; log('B*ch', terms=len(Bch))
Jmine = Ahd + Bch + cd; del Ahd
log('Jmine', terms=len(Jmine), semdeg=int(Jmine.total_degree()))
# independent J0 from linear jets of F and G
def jet(t, p): return t.get(p, zero)
def j0_from(ht):
    h0, hx, hw = jet(ht, (0, 0)), jet(ht, (1, 0)), jet(ht, (0, 1))
    d0, dx, dw = jet(Dt, (0, 0)), jet(Dt, (1, 0)), jet(Dt, (0, 1))
    cx, cw = jet(Ct, (1, 0)), jet(Ct, (0, 1))
    Fx = (3*h0*h0 + (3*d0 + a)/2)*hx + (3*h0/2)*dx + cx
    Fw = (3*h0*h0 + (3*d0 + a)/2)*hw + (3*h0/2)*dw + cw
    Gx = (2*h0 - b/3)*hx + dx
    Gw = (2*h0 - b/3)*hw + dw
    return Fx*Gw - Fw*Gx
J0_lift = j0_from(Ht); J0_src = j0_from(hsrc)
images = list(ctx.gens())
for (i, j) in sites: images[allnames.index(f'Hfact_{i}_{j}')] = hsrc[(i, j)]
rec('J0_lift_compose_equals_source', J0_lift.compose(*images, ctx=ctx) == J0_src, lifted_terms=len(J0_lift), source_terms=len(J0_src), source_degree=int(J0_src.total_degree()))
j0json = json.loads((PILOT/'complete_export.J0.json').read_text())
rec('J0_json_texts', fmpq_mpoly(j0json['lifted'], ctx=ctx) == J0_lift and fmpq_mpoly(j0json['source'], ctx=ctx) == J0_src and j0json['variables'] == names,
    lifted_sha=hashlib.sha256(j0json['lifted'].encode()).hexdigest(), source_sha=hashlib.sha256(j0json['source'].encode()).hexdigest())
res['J0_lifted_text'] = str(J0_lift)
# ---- literal rows
log('streaming literal rows')
tagged = []; labels = []; positions = set(); n_def = n_inv = n_J = 0; def_ok = True; inv_ok = None
digest = hashlib.sha256(); count = 0; terms = 0; footer = None; label_set = set()
with (PILOT/'complete_export.generators.jsonl').open() as f:
    next(f)
    for line in f:
        row = json.loads(line)
        if row['type'] == 'complete':
            footer = row; rest = f.read(); rec('no_trailing_data', rest.strip() == ''); break
        assert row['type'] == 'generator' and row['index'] == count, 'row sequence'
        lab = row['label']; assert lab not in label_set, 'duplicate label'; label_set.add(lab)
        p = fmpq_mpoly(row['polynomial'], ctx=ctx)
        assert bool(p) and len(p) == row['terms'] and int(p.total_degree()) == row['degree'], 'row field mismatch'
        if lab.startswith('define_Hfact_'):
            i, j = map(int, lab[len('define_Hfact_'):].split('_'))
            if p != G[f'Hfact_{i}_{j}'] - hsrc[(i, j)]: def_ok = False; log('graph row mismatch', label=lab)
            n_def += 1
        elif lab == 'inverse_J':
            inv_ok = (p == Zj*J0_lift - 1); n_inv += 1
        else:
            m = re.fullmatch(r'J_(\d+)_(\d+)', lab); assert m, 'label'
            i, j = int(m.group(1)), int(m.group(2)); assert (i, j) != (0, 0) and i+j <= 99
            assert (i, j) not in positions; positions.add((i, j))
            tagged.append(p*X**i*W**j); n_J += 1
        digest.update(line.encode()); count += 1; terms += len(p)
        if count % 300 == 0: log('rows', rows=count, terms=terms)
rec('graph_rows_exact', def_ok and n_def == 160, n_def=n_def)
rec('inverse_row_exact', inv_ok is True and n_inv == 1)
rec('footer_counts_and_hash', footer is not None and count == footer['generators'] == 1629 and terms == footer['terms'] == 11299180
    and digest.hexdigest() == footer['generator_stream_sha256'] and footer['maximum_semantic_degree'] == 12,
    generators=count, terms=terms, stream_sha=digest.hexdigest())
rec('J_row_census', n_J == 1468 and len(positions) == 1468, n_J=n_J, max_phys_degree=max(i+j for i, j in positions))
log('tree sum of tagged rows', n=len(tagged))
keep_first = tagged[0]
lvl = tagged
while len(lvl) > 1:
    lvl = [lvl[k]+lvl[k+1] if k+1 < len(lvl) else lvl[k] for k in range(0, len(lvl), 2)]
    log('level', n=len(lvl), rss_kib=rss())
Jlit = lvl[0]; del tagged, lvl
log('Jlit', terms=len(Jlit))
diff = Jmine - Jlit
rec('EXACT_IDENTITY_full_J', diff == J0_lift, diff_terms=len(diff), J0_terms=len(J0_lift))
# ---- negative mutation controls
del Jmine, Jlit
rec('control_sign_flip_detected', (diff - 2*Bch) != J0_lift); del Bch
pert = X**8*W**52*G[names[0]]   # perturb the largest row J_8_52 by one term
rec('control_row_perturbation_detected', (diff - pert) != J0_lift)
rec('control_dropped_row_detected', (diff + keep_first) != J0_lift, dropped_row_terms=len(keep_first))
res['controls_note'] = 'sign flip, one-term perturbation of J_8_52 and dropping the first J row all break the identity'
# ---- source-zero control (rho=1, all other source coordinates 0) with Fraction arithmetic, independent of flint
def evnum(node, env):
    if isinstance(node, ast.Constant): return Fraction(node.value)
    if isinstance(node, ast.Name): return env.get(node.id, Fraction(0))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -evnum(node.operand, env)
    if isinstance(node, ast.BinOp):
        l, r = evnum(node.left, env), evnum(node.right, env)
        return {ast.Add: l+r, ast.Sub: l-r, ast.Mult: l*r, ast.Div: (l/r if r else None), ast.Pow: l**int(r)}[type(node.op)]
    raise ValueError
env = {'rho': Fraction(1)}
def ntable(key):
    N = NORM[key]; out = {}
    for r, z, e in maps[key]:
        v = evnum(ast.parse(str(e).replace('^', '**'), mode='eval').body, env)
        if v: out[(N-int(r)-int(z), int(z))] = v
    return out
nD, nC = ntable('B2'), ntable('A3')
rec('source_zero_control_D_C_vanish_at_rho1', not nD and not nC, note='then J(F,G)=J(h^3,h^2)=0: all positive rows vanish, J0=0, inverse row = -1: correctly NOT a point')
res['wall_seconds'] = time.monotonic()-T0; res['peak_rss_kib'] = rss()
res['ring'] = {"variables": 602, "order": "degrevlex (flint) on names+[X,W]", "field": "Q"}
(OUT/'reconstruct_result.json').write_text(json.dumps(res, sort_keys=True, indent=1)+'\n')
log('done', any_fail=res.get('any_fail', False))
if res.get('any_fail', False):
    raise RuntimeError('Exact reconstruction check failed')
