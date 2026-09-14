"""Exact Q sparse-polynomial certificate checker. No CAS or execution API."""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import re
import defect_order as O

JSON_SHA = 'b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac'
SING_SHA = 'c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718'
ENDING = ';\nprint("D125_COMPLETE_LITERAL_IMPORT_ONLY");\nprint(size(I));\nquit;\n'
ONE = {(): F(1)}


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(',', ':'))+'\n').encode()


def strict_json(data):
    def unique(items):
        out = {}
        for k, v in items:
            need(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    return json.loads(data, object_pairs_hook=unique)


def add(a, b, scale=F(1)):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, F(0))+scale*c
        if not out[m]:
            del out[m]
    return out


def mul(a, b):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            k = tuple(sorted(m+n))
            out[k] = out.get(k, F(0))+c*d
            if not out[k]:
                del out[k]
    return out


class Parser:
    """Explicit +,-,*,constant division,^,parentheses; never eval/implicit products."""
    def __init__(self, text, variables):
        self.names = {v: i for i, v in enumerate(variables)}
        self.tokens = re.findall(r'[A-Za-z_][A-Za-z_0-9]*|[0-9]+|[+*/^()\-]', text)
        need(''.join(self.tokens) == re.sub(r'\s+', '', text), 'invalid polynomial syntax')
        need(bool(self.tokens), 'empty polynomial')
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ''

    def pop(self):
        need(self.pos < len(self.tokens), 'short polynomial')
        t = self.tokens[self.pos]
        self.pos += 1
        return t

    def expression(self):
        p = self.product()
        while self.peek() in ('+', '-'):
            sign = self.pop()
            p = add(p, self.product(), F(1 if sign == '+' else -1))
        return p

    def product(self):
        p = self.unary()
        while self.peek() in ('*', '/'):
            op, q = self.pop(), self.unary()
            if op == '*':
                p = mul(p, q)
            else:
                need(set(q) == {()} and q[()] != 0, 'nonconstant/zero denominator')
                p = {m: c/q[()] for m, c in p.items()}
        return p

    def unary(self):
        if self.peek() in ('+', '-'):
            sign = self.pop()
            return {m: c*(1 if sign == '+' else -1) for m, c in self.unary().items()}
        token = self.pop()
        if token == '(':
            p = self.expression()
            need(self.pop() == ')', 'unclosed polynomial')
        elif token.isdigit():
            p = {(): F(token)} if int(token) else {}
        else:
            need(token in self.names, 'unknown variable '+token)
            p = {(self.names[token],): F(1)}
        if self.peek() == '^':
            self.pop()
            power = self.pop()
            need(power.isdigit() and int(power) <= 10000, 'bad exponent')
            result, exponent = dict(ONE), int(power)
            while exponent:
                if exponent & 1:
                    result = mul(result, p)
                exponent //= 2
                if exponent:
                    p = mul(p, p)
            p = result
        return p


def polynomial(text, variables):
    parser = Parser(text, variables)
    result = parser.expression()
    need(parser.pos == len(parser.tokens), 'trailing/implicit polynomial syntax')
    return result


def key(m, nvars, weights=()):
    counts = Counter(m)
    return tuple(sum(row[i] for i in m) for row in weights)+(len(m),
           tuple(-counts[i] for i in range(nvars-1, -1, -1)))


def quotient(a, b):
    counts = Counter(a)
    counts.subtract(b)
    if any(c < 0 for c in counts.values()):
        return None
    return tuple(i for i, c in sorted(counts.items()) for _ in range(c))


def normal_form(p, basis, nvars, weights=()):
    p, remainder = dict(p), {}
    divisors = [(g, max(g, key=lambda m: key(m, nvars, weights))) for g in basis if g]
    while p:
        m = max(p, key=lambda t: key(t, nvars, weights))
        for g, lead in divisors:
            q = quotient(m, lead)
            if q is not None:
                p = add(p, mul({q: p[m]/g[lead]}, g), F(-1))
                break
        else:
            remainder[m] = p.pop(m)
    return remainder


def proper_certificate(rows, basis, nvars, weights=()):
    basis = [g for g in basis if g]
    for i, a in enumerate(basis):
        am = max(a, key=lambda m: key(m, nvars, weights))
        for b in basis[:i]:
            bm = max(b, key=lambda m: key(m, nvars, weights))
            common = Counter(am) | Counter(bm)
            lcm = tuple(k for k, v in sorted(common.items()) for _ in range(v))
            s = add(mul({quotient(lcm, am): 1/a[am]}, a),
                    mul({quotient(lcm, bm): 1/b[bm]}, b), F(-1))
            need(not normal_form(s, basis, nvars, weights), 'Buchberger failure')
    need(bool(normal_form(ONE, basis, nvars, weights)), 'unit basis, not proper')
    for index, row in enumerate(rows):
        need(not normal_form(row, basis, nvars, weights), 'original equation missing '+str(index))
    return 'EXACT_Q_PROPER_SUPERIDEAL_CERTIFICATE'


def engine_map(rows, engine):
    lookup = {}
    for i, row in enumerate(rows):
        lookup.setdefault(tuple(sorted(row.items())), i)
    mapping = []
    for row in engine:
        signature = tuple(sorted(row.items()))
        need(signature in lookup, 'engine equation not original')
        mapping.append(lookup[signature])
    available = {tuple(sorted(row.items())) for row in engine}
    need(all(not row or tuple(sorted(row.items())) in available for row in rows),
         'original nonzero equation absent from engine list')
    return mapping


def unit_certificate(rows, engine, cofactors):
    need(len(engine) == len(cofactors), 'cofactor dimension')
    mapping = engine_map(rows, engine)
    lifted = [{} for _ in rows]
    for source_id, h in zip(mapping, cofactors):
        lifted[source_id] = add(lifted[source_id], h)
    value = {}
    for f, h in zip(rows, lifted):
        value = add(value, mul(f, h))
    need(value == ONE, 'original-row cofactor identity is not one')
    return 'EXACT_Q_UNIT_COFACTOR_CERTIFICATE', mapping, lifted


def ring_id(variables, order=None):
    if order is not None:
        O.validate(order)
        need(order['variables'] == variables, 'result order variables')
        return digest(canonical(order))
    return digest(canonical({'field': 'Q', 'order': 'dp', 'variables': variables}))


def parse_result(stdout, stderr, variables, source_hash, order=None):
    need(stderr == b'', 'nonempty stderr')
    lines = stdout.decode('ascii').splitlines()
    need(lines and lines.pop(0) == 'JC2CERT 1 '+source_hash+' '+ring_id(variables, order),
         'certificate source/ring header mismatch')
    need(lines and re.fullmatch(r'I_SIZE [0-9]+', lines[0]) is not None, 'missing engine size')
    engine_size = int(lines.pop(0).split()[1])
    pos = 0
    def block(name):
        nonlocal pos
        need(pos < len(lines), 'missing '+name)
        match = re.fullmatch(name+r'_BEGIN ([0-9]+)', lines[pos])
        need(match is not None, 'bad '+name+' header')
        count = int(match[1]); pos += 1
        out = []
        for i in range(1, count+1):
            prefix = name+' '+str(i)+' '
            need(pos < len(lines) and lines[pos].startswith(prefix), 'index/short '+name)
            out.append(polynomial(lines[pos][len(prefix):], variables)); pos += 1
        need(pos < len(lines) and lines[pos] == name+'_END', 'missing '+name+' footer')
        pos += 1
        return out
    engine, basis = block('I'), block('G')
    need(engine_size == sum(bool(row) for row in engine), 'engine size/nonzero count mismatch')
    cofactors = None
    if pos < len(lines) and lines[pos].startswith('T_BEGIN '):
        cofactors = block('T')
        need(pos < len(lines) and lines[pos] == 'CHECK 1', 'internal check missing')
        pos += 1
    expected = 'END UNIT' if cofactors is not None else 'END NONUNIT'
    need(lines[pos:] == [expected], 'missing/trailing terminal stream')
    return engine, basis, cofactors


def read_source(json_data, sing_data, production=False):
    """Hash-bound parsing only: no reconstruction of J or lift coefficients."""
    if production:
        need(digest(json_data) == JSON_SHA and digest(sing_data) == SING_SHA, 'source pin drift')
    records = [strict_json(line) for line in json_data.splitlines()]
    need(records and records[0]['type'] == 'header' and records[-1]['type'] == 'footer', 'source framing')
    head, footer = records[0], records[-1]
    prefix = b''.join(canonical(row) for row in records[:-1])
    need(prefix+canonical(footer) == json_data, 'noncanonical source')
    need(footer.get('complete') is True and footer['prefix_sha256'] == digest(prefix)
         and footer['prefix_records'] == len(records)-1, 'source footer')
    need(head['field'] == 'Q' and head['order'] == 'global degree reverse lexicographic, displayed variable order', 'coefficient field/order drift')
    variables, rows, labels = [], [], []
    for row in records[1:-1]:
        if row['type'] == 'variable':
            need(row['id'] == len(variables) and re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', row['name']) is not None, 'variable index/name')
            variables.append(row['name'])
        elif row['type'] == 'row':
            p = {}
            for (a, b), monomial in row['terms']:
                need(F(*map(int, b)) == 0, 'field splitting/golden coefficient')
                c = F(*map(int, a)); m = tuple(monomial)
                need(c != 0 and list(m) == sorted(m) and m not in p and all(type(i) is int and 0 <= i < len(variables) for i in m), 'malformed term')
                p[m] = c
            rows.append(p); labels.append(row['label'])
        else:
            need(row['type'] == 'coefficient', 'unexpected source record')
    need(len(set(variables)) == len(variables) and len(set(labels)) == len(labels), 'duplicate name/row')
    need(len(rows) == head['expected_rows'] == footer['counts']['rows'] and len(variables) == head['expected_variables'], 'source dimensions')
    if production:
        need((len(variables), len(rows), head['case'], head['branch']) == (269, 803, 'unequal', 'rational'), 'wrong complete client')
    else:
        need(len(variables) <= 8 and len(rows) <= 32, 'tiny-source ceiling')
    text = sing_data.decode('ascii')
    start = 'ring R=0,('+','.join(variables)+'),dp;\nideal I=\n'
    need(text.startswith(start) and text.endswith(ENDING) and text.count(ENDING) == 1, 'literal ring/suffix drift')
    pieces = text[len(start):-len(ENDING)].split(',\n')
    need(len(pieces) == len(rows), 'literal source row count')
    for label, row, piece in zip(labels, rows, pieces):
        comment = '// '+label+'\n'
        need(piece.startswith(comment) and polynomial(piece[len(comment):], variables) == row,
             'literal source coefficient/label drift')
    return variables, rows, labels, text[:-len(ENDING)]+';\n'
