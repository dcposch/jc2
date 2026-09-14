#!/usr/bin/env python3
"""Independent all-row gate for the six D125 small-source client streams.

Own field arithmetic, own convex support (triangle-fan barycentric test), own
face reconstruction, Jacobian rows by direct derivative-pair convolution, lift
rows by repeated finite Laurent powers, own restricted Singular parser.
No producer import; no CAS.  Explicit GateError exceptions, never assert.
"""
import argparse, hashlib, json, os, re, resource, sys, time
from fractions import Fraction as Q

PINS = {'exporter_sha256': '9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703',
        'baseline_sha256': 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
        'normalization_gate_sha256': 'cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d',
        'lift_contract_sha256': '433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
        'lift_gate_sha256': '4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122'}
MARKER = 'D125_COMPLETE_LITERAL_IMPORT_ONLY'


class GateError(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise GateError(msg)


# ---------- field Q[rho]/(rho^2-3rho+1): own pair arithmetic ----------
class K:
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a, self.b = Q(a), Q(b)

    def __add__(s, o):
        o = kk(o); return K(s.a+o.a, s.b+o.b)
    __radd__ = __add__

    def __neg__(s):
        return K(-s.a, -s.b)

    def __sub__(s, o):
        return s+(-kk(o))

    def __mul__(s, o):
        o = kk(o)
        # (a+b r)(c+d r) = ac + (ad+bc) r + bd r^2, r^2 = 3r-1
        return K(s.a*o.a-s.b*o.b, s.a*o.b+s.b*o.a+3*s.b*o.b)
    __rmul__ = __mul__

    def __eq__(s, o):
        o = kk(o); return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b))

    def zero(s):
        return s.a == 0 and s.b == 0

    def inv(s):
        n = s.a*s.a+3*s.a*s.b+s.b*s.b
        need(n != 0, 'inverse of zero')
        return K((s.a+3*s.b)/n, -s.b/n)

    def pw(s, n):
        if n < 0:
            return s.inv().pw(-n)
        r = K(1)
        for _ in range(n):
            r = r*s
        return r

    def wire(s):
        return [[str(s.a.numerator), str(s.a.denominator)], [str(s.b.numerator), str(s.b.denominator)]]


def kk(v):
    return v if isinstance(v, K) else K(v)


INTRE = re.compile(r'-?(0|[1-9][0-9]*)\Z')
DENRE = re.compile(r'[1-9][0-9]*\Z')


def decode(w):
    need(isinstance(w, list) and len(w) == 2 and all(isinstance(p, list) and len(p) == 2 for p in w), 'wire shape')
    parts = []
    for n, d in w:
        need(isinstance(n, str) and isinstance(d, str) and INTRE.match(n) and DENRE.match(d), 'wire strings')
        q = Q(int(n), int(d))
        need(str(q.numerator) == n and str(q.denominator) == d, 'noncanonical wire')
        parts.append(q)
    return K(*parts)


# ---------- coefficient polynomials {sorted id tuple: K} ----------
def padd(out, m, v):
    if v.zero():
        return
    c = out.get(m)
    c = v if c is None else c+v
    if c.zero():
        out.pop(m, None)
    else:
        out[m] = c


def pmul(p, q):
    out = {}
    for m1, v1 in p.items():
        for m2, v2 in q.items():
            padd(out, tuple(sorted(m1+m2)), v1*v2)
    return out


# ---------- bivariate polynomials {(i,j): K} in gamma^i pi^j ----------
def bmul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            c = out.get((i+k, j+l), K(0))+a*b
            out[(i+k, j+l)] = c
    return {m: c for m, c in out.items() if not c.zero()}


def bpow(p, n):
    out = {(0, 0): K(1)}
    for _ in range(n):
        out = bmul(out, p)
    return out


VERT = {'unequal': (((0, 0), (0, 15), (9, 6), (2, 1)), ((0, 0), (0, 25), (15, 10), (1, 0))),
        'common_3': (((0, 0), (0, 15), (9, 6), (3, 0)), ((0, 0), (0, 25), (15, 10), (5, 0))),
        'common_4': (((0, 0), (0, 15), (9, 6), (9, 0)), ((0, 0), (0, 25), (15, 10), (15, 0)))}
INNER_DIR = {'unequal': (5, -7), 'common_3': (1, -1), 'common_4': (1, 0)}


def inside(p, verts):
    """Exact barycentric triangle-fan membership (closed convex polygon)."""
    x, y = p
    v0 = verts[0]
    for a, b in zip(verts[1:], verts[2:]):
        det = (a[0]-v0[0])*(b[1]-v0[1])-(b[0]-v0[0])*(a[1]-v0[1])
        need(det != 0, 'degenerate fan triangle')
        s = Q((x-v0[0])*(b[1]-v0[1])-(b[0]-v0[0])*(y-v0[1]), det)
        t = Q((a[0]-v0[0])*(y-v0[1])-(x-v0[0])*(a[1]-v0[1]), det)
        if s >= 0 and t >= 0 and s+t <= 1:
            return True
    return False


def reconstruct(case, branch):
    """Own reconstruction of the complete literal contract and all rows."""
    need(case in VERT and branch in ('rational', 'golden'), 'unknown client')
    kappa = K(1) if branch == 'rational' else K(0, 1)
    rho = K(0, 1)
    if branch == 'rational':
        cubic = {(0, 3): K(1), (3, 0): K(1)}
    else:
        cubic = {(0, 3): K(1), (1, 2): K(3)-2*rho, (2, 1): K(2)-rho, (3, 0): rho}
    h = {(i, j+2): v for (i, j), v in cubic.items()}
    outer = (bpow(h, 3), bpow(h, 5))
    if case == 'unequal':
        inner = ({(2, 1): K(1), (9, 6): kappa.pw(3)},
                 {(1, 0): K(Q(5, 9))*kappa.inv(), (8, 5): K(Q(5, 3))*kappa.pw(2), (15, 10): kappa.pw(5)})
        scalar = -K(Q(5, 9))*kappa.inv()
    else:
        root = ({(3, 2): K(1), (2, 1): K(-2), (1, 0): K(1)} if case == 'common_3'
                else {(3, 2): K(1), (3, 1): K(-2), (3, 0): K(1)})
        inner = tuple({pt: kappa.pw(n)*v for pt, v in bpow(root, n).items()} for n in (3, 5))
        scalar = None
    variables, maps, guards, polys = [], [], [], []
    for member, verts, degree, oface, iface in zip('AB', VERT[case], (15, 25), outer, inner):
        nx, ny = INNER_DIR[case]
        top = max(nx*i+ny*j for i, j in verts)
        pts = [(i, j) for i in range(max(v[0] for v in verts)+1) for j in range(max(v[1] for v in verts)+1)
               if inside((i, j), verts)]
        entries, poly = [], {}
        for i, j in pts:
            specs = []
            if i+j == degree:
                specs.append(('outer', oface.get((i, j), K(0))))
            if nx*i+ny*j == top:
                specs.append(('inner', iface.get((i, j), K(0))))
            if (i, j) == (0, 0):
                specs.append(('target_constant', K(0)))
            name = f'{member}_g{i}_p{j}'
            if specs:
                val = specs[0][1]
                need(all(v == val for _, v in specs), 'face conflict')
                entries.append({'type': 'coefficient', 'member': member, 'point': [i, j], 'name': name,
                                'fixed': val.wire(), 'reasons': [s for s, _ in specs]})
                if not val.zero():
                    poly[(i, j)] = {(): val}
            else:
                entries.append({'type': 'coefficient', 'member': member, 'point': [i, j], 'name': name,
                                'variable': len(variables)})
                poly[(i, j)] = {(len(variables),): K(1)}
                variables.append(name)
        for v in verts[1:]:
            e = next(e for e in entries if tuple(e['point']) == v)
            need('fixed' in e, 'vertex not fixed')
            val = decode(e['fixed'])
            need(not val.zero(), 'zero vertex')
            guards.append({'label': f'GUARD/{member}/{v[0]}/{v[1]}', 'value': val.wire(), 'inverse': val.inv().wire()})
        maps.append(entries)
        polys.append(poly)
    free = len(variables)
    if scalar is None:
        variables += ['c', 'z']
        jscalar = {'variable': free, 'inverse_variable': free+1, 'row': 'z*c-1'}
        scalar_poly = {(free,): K(1)}
        scalar_guard = {(): K(-1), (free, free+1): K(1)}
    else:
        jscalar = {'fixed': scalar.wire(), 'inverse': scalar.inv().wire()}
        scalar_poly = {(): scalar}
        scalar_guard = {}
    variables += ['lambda2', 'lambda3']
    l2, l3 = len(variables)-2, len(variables)-1
    nfixed = sum('fixed' in e for m in maps for e in m)
    header = {'type': 'header', 'schema': 'jc2.d125-small-source-literal/v1',
              'status': 'GATED_SUFFICIENT_CLIENT_NO_POINT_OR_CE_CLAIM',
              'implementation_gate': 'PENDING_AT_SOURCE_SEAL', 'mode': 'production', 'case': case,
              'branch': branch, 'field': 'Q' if branch == 'rational' else 'Q[rho]/(rho^2-3*rho+1)',
              'index_base': 0, 'order': 'global degree reverse lexicographic, displayed variable order',
              'target': 'J(A,B)-c*gamma^2; J=A_gamma*B_pi-A_pi*B_gamma', 'jacobian_scalar': jscalar,
              'pins': PINS, 'expected_rows': 660+nfixed+7+105, 'expected_jacobian_rows': 660,
              'expected_lift_rows': 105, 'expected_variables': len(variables),
              'lambda_guard': 'NONE: lambda2 and lambda3 are unrestricted',
              'lift': 'g=v^-1,p=v^4*u-lambda2*v^2-lambda3*v-v^-1'}
    recs = [header]
    recs += [{'type': 'variable', 'id': i, 'name': n} for i, n in enumerate(variables)]
    for m in maps:
        recs += m
    for m in maps:
        for e in m:
            if 'fixed' in e:
                recs.append(row('FIX/'+e['name'], {}, 'fixed_assignment'))
    # Jacobian by derivative-pair convolution
    A, B = polys
    Ag = {(i-1, j): {m: i*v for m, v in c.items()} for (i, j), c in A.items() if i >= 1}
    Ap = {(i, j-1): {m: j*v for m, v in c.items()} for (i, j), c in A.items() if j >= 1}
    Bg = {(i-1, j): {m: i*v for m, v in c.items()} for (i, j), c in B.items() if i >= 1}
    Bp = {(i, j-1): {m: j*v for m, v in c.items()} for (i, j), c in B.items() if j >= 1}
    bracket = {}
    for P, S, sign in ((Ag, Bp, 1), (Ap, Bg, -1)):
        for (i, j), c in P.items():
            for (k, l), d in S.items():
                slot = bracket.setdefault((i+k, j+l), {})
                for m, v in pmul(c, d).items():
                    padd(slot, m, sign*v)
    slot = bracket.setdefault((2, 0), {})
    for m, v in scalar_poly.items():
        padd(slot, m, -v)
    stray = [s for s, p in bracket.items() if p and not (0 <= s[0] <= 23 and s[1] >= 0 and s[0]+s[1] <= 38)]
    need(not stray, 'nonzero bracket slot outside the 660 envelope: '+str(stray[:3]))
    outside = sum(1 for I in range(39) for J in range(39-I) if I >= 24)
    need(outside == 120 and max(i for i, j in A) <= 9 and max(i for i, j in B) <= 15, 'gamma-degree bound')
    for I in range(24):
        for J in range(39-I):
            recs.append(row(f'J/{I}/{J}', bracket.get((I, J), {}), 'jacobian'))
    # lift rows by repeated finite Laurent powers of pi_sub = v^4 u - l2 v^2 - l3 v - v^-1
    pisub = {(1, 4, 0, 0): 1, (0, 2, 1, 0): -1, (0, 1, 0, 1): -1, (0, -1, 0, 0): -1}
    powers = [{(0, 0, 0, 0): 1}]
    for _ in range(25):
        nxt = {}
        for (t, e, b, d), c in powers[-1].items():
            for (t2, e2, b2, d2), c2 in pisub.items():
                key = (t+t2, e+e2, b+b2, d+d2)
                nxt[key] = nxt.get(key, 0)+c*c2
        powers.append({k: v for k, v in nxt.items() if v})
    for member, poly, degree in zip('AB', polys, (15, 25)):
        rows = {}
        for (i, j), c in poly.items():
            for (t, e, b, d), mult in powers[j].items():
                e -= i
                if e >= 0:
                    continue
                slot = rows.setdefault((t, e), {})
                lam = (l2,)*b+(l3,)*d
                for m, v in c.items():
                    padd(slot, tuple(sorted(m+lam)), mult*v)
        roster = [(t, e) for t in range((degree-1)//5+1) for e in range(5*t-degree, 0)]
        stray = [s for s, p in rows.items() if p and s not in roster]
        need(not stray, 'negative lift slot outside roster '+str(stray[:3]))
        for t, e in roster:
            recs.append(row(f'LIFT/{member}/{t}/{e}', rows.get((t, e), {}), 'polynomiality'))
    for g in guards:
        recs.append({**row(g['label'], {}, 'fixed_unit_guard'), 'value': g['value'], 'inverse': g['inverse']})
    recs.append(row('GUARD/c', scalar_guard, 'scalar_guard'))
    return recs, variables


def row(label, poly, kind):
    return {'type': 'row', 'kind': kind, 'label': label,
            'terms': [[c.wire(), list(m)] for m, c in sorted(poly.items()) if not c.zero()]}


def canon(rec):
    return (json.dumps(rec, sort_keys=True, separators=(',', ':'))+'\n').encode()


def footer_for(recs):
    dig = hashlib.sha256()
    counts = {'rows': 0, 'terms': 0, 'zero_rows': 0}
    used = set()
    nvar = sum(1 for r in recs if r['type'] == 'variable')
    for r in recs:
        if r['type'] == 'row':
            counts['rows'] += 1
            counts[r['kind']] = counts.get(r['kind'], 0)+1
            counts['terms'] += len(r['terms'])
            counts['zero_rows'] += 0 if r['terms'] else 1
            for _, m in r['terms']:
                used.update(m)
        dig.update(canon(r))
    return {'type': 'footer', 'complete': True, 'prefix_sha256': dig.hexdigest(), 'prefix_records': len(recs),
            'counts': counts, 'unused_variables': [i for i in range(nvar) if i not in used]}


# ---------- strict JSONL parsing ----------
def strict_load(line):
    def hook(pairs):
        out = {}
        for k, v in pairs:
            need(k not in out, 'duplicate JSON key '+k)
            out[k] = v
        return out
    try:
        rec = json.loads(line, object_pairs_hook=hook)
    except ValueError as err:
        raise GateError('JSON parse: '+str(err))
    need(canon(rec) == line, 'noncanonical JSONL line')
    return rec


def parse_jsonl(data):
    need(data.endswith(b'\n'), 'missing final newline')
    recs = [strict_load(l+b'\n') for l in data[:-1].split(b'\n')]
    need(recs and recs[-1].get('type') == 'footer', 'missing footer')
    need(all(r.get('type') != 'footer' for r in recs[:-1]), 'trailing data after complete footer')
    return recs


def compare(expected, got):
    """Byte-exact comparison of an independently reconstructed record list (footer included)."""
    need(got[0].get('type') == 'header', 'header absent')
    need(canon(got[0]) == canon(expected[0]), 'header mismatch')
    need(len(got) == len(expected), f'record count {len(got)} != {len(expected)}')
    nvar = sum(1 for r in expected if r['type'] == 'variable')
    for idx, (e, g) in enumerate(zip(expected[1:], got[1:]), 1):
        if g.get('type') == 'row':
            for c, m in g.get('terms', []):
                need(not decode(c).zero(), 'explicit zero term')
                need(m == sorted(m) and all(type(i) is int and 0 <= i < nvar for i in m), 'invalid variable id in '+str(g.get('label')))
        if canon(e) != canon(g):
            what = e.get('label') or e.get('name') or e.get('type')
            raise GateError(f'record {idx} mismatch at {e["type"]} {what}')
    need(got[-1]['unused_variables'] == [], 'unused variables present')


# ---------- restricted Singular grammar ----------
TOK = re.compile(r'\(|\)|\+|\*|\^|/|-?[0-9]+|[A-Za-z_][A-Za-z0-9_]*')
RESERVED = {'rho', 'ring', 'ideal', 'I', 'R', 'minpoly', 'dp', 'print', 'size', 'quit', 'std', 'poly', 'int',
            'number', 'list', 'if', 'else', 'for', 'while', 'proc', 'return', 'def', 'matrix', 'vector', 'module'}
RESERVED |= {'basering', 'setring', 'char', 'nvars', 'var', 'map', 'kill', 'exit', 'execute', 'system', 'read', 'write'}


class SingParser:
    def __init__(self, text, variables, golden):
        self.t, self.i, self.vars, self.golden = TOK.findall(text), 0, {n: k for k, n in enumerate(variables)}, golden
        need(''.join(self.t) == text.replace(' ', ''), 'illegal characters in Singular polynomial')

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def take(self, want=None):
        tok = self.peek()
        need(tok is not None and (want is None or tok == want), f'Singular grammar: expected {want!r} got {tok!r}')
        self.i += 1
        return tok

    def integer(self):
        tok = self.take()
        need(INTRE.match(tok), 'integer expected')
        return int(tok)

    def rat(self):
        if self.peek() == '(':
            self.take('('); n = self.integer(); self.take('/'); d = self.integer(); self.take(')')
            need(d > 1 and Q(n, d).denominator == d and Q(n, d).numerator == n, 'noncanonical Singular fraction')
            return Q(n, d)
        return Q(self.integer())

    def coeff(self):
        """factor '(' X ')' with X := INT | '(' INT '/' INT ')' | '(' rat '+' '(' rat ')' '*' rho ')'."""
        self.take('(')
        if self.peek() == '(':
            self.take('(')
            if self.peek() != '(' and self.i+1 < len(self.t) and self.t[self.i+1] == '/':
                n = self.integer(); self.take('/'); d = self.integer(); self.take(')')
                need(d > 1 and Q(n, d).denominator == d and Q(n, d).numerator == n, 'noncanonical Singular fraction')
                val = K(Q(n, d))
            else:
                need(self.golden, 'rho coefficient in rational ring')
                a = self.rat()
                self.take('+'); self.take('('); b = self.rat(); self.take(')'); self.take('*'); self.take('rho'); self.take(')')
                need(b != 0, 'zero rho part written')
                val = K(a, b)
        else:
            val = K(Q(self.integer()))
        self.take(')')
        return val

    def poly(self):
        if self.peek() == '0' and self.i+1 == len(self.t):
            self.take('0'); return {}
        out = {}
        while True:
            c = self.coeff()
            need(not c.zero(), 'zero coefficient term')
            mono, last = [], -1
            while self.peek() == '*':
                self.take('*')
                name = self.take()
                need(name in self.vars, 'undeclared variable '+name)
                vid = self.vars[name]
                need(vid > last, 'variable order/repeat in monomial')
                last = vid
                p = 1
                if self.peek() == '^':
                    self.take('^'); p = self.integer(); need(p >= 2, 'exponent must be >=2')
                mono += [vid]*p
            need(tuple(mono) not in out, 'duplicate monomial')
            out[tuple(mono)] = c
            if self.peek() is None:
                return out
            self.take('+')


def check_singular(text, variables, golden, rows):
    lines = text.split('\n')
    need(lines[-1] == '' and len(lines) >= 6, 'Singular file must end with newline')
    lines = lines[:-1]
    m = re.fullmatch(r'ring R=(0|\(0,rho\)),\(([A-Za-z0-9_,]+)\),dp;', lines[0])
    need(m, 'ring declaration')
    need((m.group(1) == '(0,rho)') == golden, 'coefficient field/branch mismatch')
    need(m.group(2).split(',') == variables, 'declared variables/order differ from JSONL')
    for v in variables:
        need(re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', v) and v not in RESERVED, 'unsafe variable name '+v)
    pos = 1
    if golden:
        need(lines[pos] == 'minpoly=rho^2-3*rho+1;', 'minimal polynomial'); pos += 1
    else:
        need(not lines[pos].startswith('minpoly'), 'unexpected minpoly in rational ring')
    need(lines[pos] == 'ideal I=', 'ideal opening'); pos += 1
    got = []
    while True:
        need(pos+1 < len(lines) and lines[pos].startswith('// '), 'row label comment expected at line '+str(pos+1))
        label = lines[pos][3:]
        body = lines[pos+1]
        need(body and body[-1] in ',;', 'row terminator')
        got.append((label, SingParser(body[:-1], variables, golden).poly()))
        pos += 2
        if body[-1] == ';':
            break
    need(lines[pos:] == [f'print("{MARKER}");', 'print(size(I));', 'quit;'], 'permitted trailer/commands only')
    need(len(got) == len(rows), f'Singular row count {len(got)} != JSONL {len(rows)}')
    for (label, poly), r in zip(got, rows):
        need(label == r['label'], f'Singular label {label} != {r["label"]}')
        jp = {tuple(m): decode(c) for c, m in r['terms']}
        need(len(jp) == len(r['terms']), 'duplicate JSONL monomial')
        need(poly == jp, 'Singular polynomial != JSONL row '+label)
    return len(got), sum(1 for _, p in got if p)


# ---------- mutation suite (repaired footers) ----------
def repaired(recs):
    return recs[:-1]+[footer_for(recs[:-1])]


class MutationError(Exception):
    pass


def mutations(recs, sing, variables, golden):
    import copy
    l2, l3 = len(variables)-2, len(variables)-1
    labels = {r.get('label'): i for i, r in enumerate(recs) if r.get('type') == 'row'}
    jnz = next(r['label'] for r in recs if r.get('kind') == 'jacobian' and r['terms'])
    jint = next(m.group(1) for m in re.finditer(r'// (J/[0-9]+/[0-9]+)\n\((-?[0-9]+)\)\*', sing))
    out = []
    def rec(fn):
        r = copy.deepcopy(recs[:-1]); fn(r); return repaired(r+[recs[-1]])
    def drop_row(r): del r[labels['LIFT/A/0/-1']]
    out.append(('missing_row', lambda: rec(drop_row), None))
    def zero_row(r): r[labels[jnz]]['terms'] = []
    out.append(('zero_row', lambda: rec(zero_row), None))
    def lam_term(r):
        for term in r[labels['LIFT/B/4/-1']]['terms']:
            if l3 in term[1]:
                return term
        raise MutationError('no lambda3 term')
    def lam_swap(r):
        term = lam_term(r); term[1][term[1].index(l3)] = l2; term[1].sort()
    out.append(('lambda_swap', lambda: rec(lam_swap), None))
    def lam_exp(r):
        term = lam_term(r); term[1].append(l3); term[1].sort()
    out.append(('lambda_exponent', lambda: rec(lam_exp), None))
    def lam_sign(r):
        term = lam_term(r); term[0] = (-decode(term[0])).wire()
    out.append(('lambda_sign', lambda: rec(lam_sign), None))
    def sign(r):
        t = r[labels[jnz]]['terms']; t[0][0] = (-decode(t[0][0])).wire()
    out.append(('jacobian_sign', lambda: rec(sign), None))
    if golden:
        def split(r):
            for i, x in enumerate(r):
                if x.get('type') == 'row' and any(decode(c).b != 0 for c, m in x['terms']):
                    a = {**x, 'label': x['label']+'/re', 'terms': [[K(decode(c2).a).wire(), m2] for c2, m2 in x['terms'] if decode(c2).a != 0]}
                    b = {**x, 'label': x['label']+'/im', 'terms': [[K(decode(c2).b).wire(), m2] for c2, m2 in x['terms'] if decode(c2).b != 0]}
                    r[i:i+1] = [a, b]; return
            raise MutationError('no golden row')
        out.append(('field_split', lambda: rec(split), None))
        out.append(('minpoly', None, lambda s: s.replace('minpoly=rho^2-3*rho+1;', 'minpoly=rho^2-3*rho-1;', 1)))
        out.append(('minpoly_removed', None, lambda s: s.replace('minpoly=rho^2-3*rho+1;\n', '', 1)))
    else:
        def inject_rho(r):
            t = r[labels[jnz]]['terms']; t[0][0] = (decode(t[0][0])+K(0, 1)).wire()
        out.append(('rho_in_rational', lambda: rec(inject_rho), None))
        out.append(('minpoly_added', None, lambda s: s.replace('ideal I=', 'minpoly=rho^2-3*rho+1;\nideal I=', 1)))
        out.append(('rho_in_rational_sing', None, lambda s: s.replace('// '+jint+'\n(', '// '+jint+'\n((1+(1)*rho))*lambda2+(', 1)))
    def monic(r):
        for x in r:
            if x.get('type') == 'coefficient' and x['name'] == 'A_g0_p15':
                x['fixed'] = K(2).wire()
            if x.get('label') == 'GUARD/A/0/15':
                x['value'], x['inverse'] = K(2).wire(), K(Q(1, 2)).wire()
    out.append(('monicity', lambda: rec(monic), None))
    def fixed_zero(r):
        for x in r:
            if x.get('type') == 'coefficient' and 'fixed' in x and decode(x['fixed']).zero() and x['point'] != [0, 0]:
                x['fixed'] = K(1).wire(); return
        raise MutationError('no fixed zero')
    out.append(('fixed_zero_face', lambda: rec(fixed_zero), None))
    def vguard(r): r[labels['GUARD/B/0/25']]['inverse'] = K(2).wire()
    out.append(('vertex_guard', lambda: rec(vguard), None))
    def ctarget(r):
        js = r[0]['jacobian_scalar']
        if 'fixed' in js:
            c = decode(js['fixed'])
            r[0]['jacobian_scalar'] = {'fixed': (-c).wire(), 'inverse': (-c).inv().wire()}
            t = r[labels['J/2/0']]['terms']
            const = [x for x in t if x[1] == []]
            if const:
                const[0][0] = (decode(const[0][0])+2*c).wire()
            else:
                t.insert(0, [(2*c).wire(), []])
        else:
            for term in r[labels['J/2/0']]['terms']:
                if term[1] == [js['variable']]:
                    term[0] = (-decode(term[0])).wire(); return
            raise MutationError('no c term')
    out.append(('c_target', lambda: rec(ctarget), None))
    def sguard(r):
        g = r[labels['GUARD/c']]
        g['terms'] = [x for x in g['terms'] if x[1] != []] if g['terms'] else [[K(1).wire(), []]]
    out.append(('scalar_guard', lambda: rec(sguard), None))
    def unknown(r): r[labels[jnz]]['terms'][0][1] = [len(variables)+5]
    out.append(('unknown_variable_id', lambda: rec(unknown), None))
    out.append(('unknown_variable_sing', None, lambda s: s.replace('*lambda3', '*lambda9', 1)))
    def sing_sign(s):
        m = re.search(r'// '+re.escape(jint)+r'\n\((-?[0-9]+)\)\*', s)
        v = int(m.group(1))
        return s[:m.start(1)]+str(-v)+s[m.end(1):]
    out.append(('sing_sign', None, sing_sign))
    out.append(('sing_missing_row', None, lambda s: re.sub(r'// LIFT/A/0/-1\n[^\n]*\n', '', s, count=1)))
    out.append(('sing_zero_row', None, lambda s: re.sub(r'(// '+re.escape(jint)+r'\n)[^\n]*,\n', r'\g<1>0,\n', s, count=1)))
    out.append(('sing_variable_order', None, lambda s: s.replace(',lambda2,lambda3),dp;', ',lambda3,lambda2),dp;', 1)))
    out.append(('trailing_command', None, lambda s: s.replace('quit;\n', 'quit;\nstd(I);\n', 1)))
    out.append(('inserted_command', None, lambda s: s.replace('print(size(I));', 'print(size(I));\nstd(I);', 1)))
    out.append(('duplicate_sing_row', None, lambda s: s.replace('// GUARD/c\n', '// GUARD/c\n0,\n// GUARD/c\n', 1)))
    return out


def run_case(root, case, branch, results):
    d = os.path.join(root, f'{case}-{branch}')
    t0 = time.time()
    jpath, spath = os.path.join(d, f'client-{case}-{branch}.jsonl'), os.path.join(d, f'client-{case}-{branch}.sing')
    data = open(jpath, 'rb').read(); stext = open(spath, 'rb').read()
    apath = os.path.join(d, 'authority.json')
    asha = hashlib.sha256(open(apath, 'rb').read()).hexdigest() if os.path.exists(apath) else None
    res = {'case': case, 'branch': branch, 'jsonl_sha256': hashlib.sha256(data).hexdigest(),
           'jsonl_bytes': len(data), 'sing_sha256': hashlib.sha256(stext).hexdigest(), 'sing_bytes': len(stext),
           'authority_sha256': asha}
    golden = branch == 'golden'
    expected, variables = reconstruct(case, branch)
    res['reconstruct_seconds'] = round(time.time()-t0, 3)
    got = parse_jsonl(data)
    need(got[0].get('type') == 'header' and re.fullmatch(r'[0-9a-f]{64}', str(got[0].get('authority_sha256', ''))), 'authority sha absent')
    need(asha is None or got[0]['authority_sha256'] == asha, 'header authority sha != sibling authority.json')
    expected[0]['authority_sha256'] = got[0]['authority_sha256']
    expected.append(footer_for(expected))
    compare(expected, got)
    rows = [r for r in got if r['type'] == 'row']
    need(len(rows) == got[-1]['counts']['rows'], 'footer row count')
    text = stext.decode('ascii')
    nrows, nonzero = check_singular(text, variables, golden, rows)
    res.update({'rows': len(rows), 'terms': got[-1]['counts']['terms'], 'zero_rows': got[-1]['counts']['zero_rows'],
                'variables': len(variables), 'counts': got[-1]['counts'], 'prefix_sha256': got[-1]['prefix_sha256'],
                'singular_rows': nrows, 'singular_nonzero_generators': nonzero, 'jacobian_slots_outside_envelope_nonzero': 0,
                'verify_seconds': round(time.time()-t0, 3), 'verdict': 'MATCH'})
    controls = []
    for name, fn, sfn in mutations(got, text, variables, golden):
        try:
            if fn is not None:
                mut = fn()
                data2 = b''.join(canon(r) for r in mut)
                need(data2 != data, 'mutation did not change the object')
                got2 = parse_jsonl(data2)
                compare(expected, got2)
            else:
                s2 = sfn(text)
                need(s2 != text, 'mutation did not change the object')
                check_singular(s2, variables, golden, rows)
            controls.append({'control': name, 'rejected': False, 'error': None})
        except GateError as err:
            ok = 'did not change' not in str(err)
            controls.append({'control': name, 'rejected': ok, 'error': str(err)})
        except MutationError as err:
            controls.append({'control': name, 'rejected': False, 'error': 'MUTATION NOT APPLIED: '+str(err)})
    # structural controls on raw bytes
    for name, data2 in (('duplicate_json_key', data.replace(b'{"branch":', b'{"branch":"x","branch":', 1)),
                        ('trailing_json', data+canon(got[-1])),
                        ('truncated_no_footer', data[:-len(canon(got[-1]))])):
        try:
            got2 = parse_jsonl(data2); compare(expected, got2)
            controls.append({'control': name, 'rejected': False, 'error': None})
        except GateError as err:
            controls.append({'control': name, 'rejected': True, 'error': str(err)})
    res['controls'] = controls
    res['controls_all_rejected'] = all(c['rejected'] for c in controls)
    res['control_seconds'] = round(time.time()-t0-res['verify_seconds'], 3)
    results.append(res)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-root', required=True, help='pilot root holding CASE-BRANCH/client-*.jsonl|.sing')
    ap.add_argument('--out', required=True)
    ap.add_argument('--cases', default='unequal-rational,unequal-golden,common_3-rational,common_3-golden,common_4-rational,common_4-golden')
    ap.add_argument('--self-sha', action='store_true')
    ap.add_argument('--as-bytes', type=int, default=8*1024**3)
    a = ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS, (a.as_bytes, a.as_bytes))
    results = []
    summary = {'schema': 'jc2.d125-small-full-stream-gate/v1', 'checker_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
               'source_root': os.path.abspath(a.source_root), 'pid': os.getpid(), 'pgid': os.getpgid(0),
               'start_ticks': open('/proc/self/stat').read().split(') ', 1)[1].split()[19],
               'boot_id': open('/proc/sys/kernel/random/boot_id').read().strip(),
               'board_asset_tag': open('/sys/class/dmi/id/board_asset_tag').read().strip(),
               'cwd': os.getcwd(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               'python': sys.version.split()[0], 'results': results, 'status': None, 'failure': None}
    try:
        for cb in a.cases.split(','):
            case, branch = cb.rsplit('-', 1)
            r = run_case(a.source_root, case, branch, results)
            print(json.dumps({k: r[k] for k in ('case', 'branch', 'rows', 'terms', 'zero_rows', 'verdict', 'controls_all_rejected', 'verify_seconds', 'control_seconds')}), flush=True)
            need(r['controls_all_rejected'], 'a corruption control was NOT rejected: '+cb)
        summary['status'] = 'ALL_SIX_MATCH_ALL_CONTROLS_REJECTED'
    except GateError as err:
        summary['status'], summary['failure'] = 'REFUTED_OR_CHECKER_FAILURE', str(err)
        print('GATE_ERROR: '+str(err), flush=True)
    summary['end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    summary['max_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    summary['cpu_seconds'] = round(resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime, 3)
    with open(a.out, 'xb') as f:
        f.write((json.dumps(summary, sort_keys=True, indent=1)+'\n').encode())
    print('STATUS '+summary['status'], flush=True)
    return 0 if summary['failure'] is None else 1


if __name__ == '__main__':
    sys.exit(main())
