#!/usr/bin/env python3
"""PREP ONLY: exact six-client metadata and a deliberately toy-capped row kernel.

No production exporter, CAS adapter, solve, authority promotion, or source lift.
Coefficient field is Q[r]/(r*r-3*r+1); rational clients use its Q subfield.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json


@dataclass(frozen=True)
class F:
    a: Q = Q(0)
    b: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', Q(self.a))
        object.__setattr__(self, 'b', Q(self.b))

    def __add__(self, other):
        other = field(other)
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + -field(other)

    def __rsub__(self, other):
        return field(other) + -self

    def __mul__(self, other):
        other = field(other)
        return F(self.a*other.a-self.b*other.b,
                 self.a*other.b+self.b*other.a+3*self.b*other.b)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a*self.a + 3*self.a*self.b + self.b*self.b
        if not norm:
            raise ZeroDivisionError('zero field element')
        return F((self.a+3*self.b)/norm, -self.b/norm)

    def __pow__(self, n):
        if n < 0:
            return self.inverse() ** (-n)
        result, base = F(1), self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def wire(self):
        return [[str(self.a.numerator), str(self.a.denominator)],
                [str(self.b.numerator), str(self.b.denominator)]]


def field(value):
    return value if isinstance(value, F) else F(value)


ZERO, ONE, RHO = F(), F(1), F(0, 1)


def poly_mul(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            key = (i+k, j+l)
            out[key] = out.get(key, ZERO) + a*b
    return {key: value for key, value in out.items() if value != ZERO}


def poly_pow(poly, n):
    out = {(0, 0): ONE}
    for _ in range(n):
        out = poly_mul(out, poly)
    return out


VERTICES = {
    'unequal': (((0, 0), (0, 15), (9, 6), (2, 1)),
                ((0, 0), (0, 25), (15, 10), (1, 0))),
    'common_3': (((0, 0), (0, 15), (9, 6), (3, 0)),
                 ((0, 0), (0, 25), (15, 10), (5, 0))),
    'common_4': (((0, 0), (0, 15), (9, 6), (9, 0)),
                 ((0, 0), (0, 25), (15, 10), (15, 0))),
}
INNER = {'unequal': (5, -7), 'common_3': (1, -1), 'common_4': (1, 0)}


def lattice(vertices):
    """Small closed polygon census only; no coefficient-pair enumeration."""
    edges = list(zip(vertices, vertices[1:]+vertices[:1]))
    def inside(i, j):
        cross = [(b[0]-a[0])*(j-a[1])-(b[1]-a[1])*(i-a[0])
                 for a, b in edges]
        return all(t >= 0 for t in cross) or all(t <= 0 for t in cross)
    return [(i, j) for i in range(max(p[0] for p in vertices)+1)
            for j in range(max(p[1] for p in vertices)+1) if inside(i, j)]


def make_contract(case, branch):
    if case not in VERTICES or branch not in ('rational', 'golden'):
        raise ValueError('unknown exact client')
    kappa = ONE if branch == 'rational' else RHO
    cubic = {(0, 3): ONE, (3, 0): ONE} if branch == 'rational' else {
        (0, 3): ONE, (1, 2): F(3)-2*RHO,
        (2, 1): F(2)-RHO, (3, 0): RHO}
    h = {(i, j+2): value for (i, j), value in cubic.items()}
    outer = (poly_pow(h, 3), poly_pow(h, 5))
    if case == 'unequal':
        inner = ({(2, 1): ONE, (9, 6): kappa**3},
                 {(1, 0): F(Q(5, 9))*kappa**-1,
                  (8, 5): F(Q(5, 3))*kappa**2, (15, 10): kappa**5})
        scalar = -F(Q(5, 9))*kappa**-1
    else:
        root = ({(3, 2): ONE, (2, 1): F(-2), (1, 0): ONE}
                if case == 'common_3' else
                {(3, 2): ONE, (3, 1): F(-2), (3, 0): ONE})
        inner = tuple({point: kappa**n*value for point, value in
                       poly_pow(root, n).items()} for n in (3, 5))
        scalar = None
    variables, maps, fixed_counts, guards = [], [], [], []
    for member, vertices, degree, outface, inface in zip(
            ('A', 'B'), VERTICES[case], (15, 25), outer, inner):
        points = lattice(vertices)
        nx, ny = INNER[case]
        top = max(nx*i+ny*j for i, j in vertices)
        entries = []
        for i, j in points:
            specifications = []
            if i+j == degree:
                specifications.append(('outer', outface.get((i, j), ZERO)))
            if nx*i+ny*j == top:
                specifications.append(('inner', inface.get((i, j), ZERO)))
            if (i, j) == (0, 0):
                specifications.append(('target_constant', ZERO))
            label = f'{member}_g{i}_p{j}'
            if specifications:
                value = specifications[0][1]
                if any(v != value for _, v in specifications):
                    raise ValueError('face intersection conflict')
                entries.append({'point': [i, j], 'name': label,
                                'fixed': value.wire(),
                                'reasons': [s for s, _ in specifications]})
            else:
                entries.append({'point': [i, j], 'name': label,
                                'variable': len(variables)})
                variables.append(label)
        bypoint = {tuple(e['point']): e for e in entries}
        for point in vertices[1:]:
            value = decode(bypoint[point]['fixed'])
            if value == ZERO:
                raise ValueError('zero required vertex')
            guards.append({'label': f'GUARD/{member}/{point[0]}/{point[1]}',
                           'value': value.wire(), 'inverse': value.inverse().wire()})
        maps.append(entries)
        fixed_counts.append(sum('fixed' in e for e in entries))
    free = len(variables)
    if scalar is None:
        variables += ['c', 'z']
        scalar_data = {'variable': free, 'inverse_variable': free+1,
                       'row': 'z*c-1'}
    else:
        scalar_data = {'fixed': scalar.wire(), 'inverse': scalar.inverse().wire()}
    return {'schema': 'jc2.minimal-receiver-preflight/v1',
            'status': 'PROVISIONAL_PREP_ONLY_NO_PRODUCTION_AUTHORITY',
            'case': case, 'branch': branch,
            'field': 'Q' if branch == 'rational' else 'Q[rho]/(rho^2-3*rho+1)',
            'geometric_scope': 'algebraically closed characteristic zero',
            'order': 'global degree reverse lexicographic, displayed variable order',
            'variables': variables, 'coefficient_maps': maps,
            'vertex_guards': guards, 'scalar': scalar_data,
            'counts': {'raw': [len(m) for m in maps], 'fixed': fixed_counts,
                       'free': free, 'variables': len(variables),
                       'raw_pair_upper_bound': len(maps[0])*len(maps[1]),
                       'jacobian_envelope_rows': 660,
                       'planned_all_rows': 660+sum(fixed_counts)+7},
            'target': 'J(A,B)-c*gamma^2; J=A_gamma*B_pi-A_pi*B_gamma',
            'row_envelope': '0<=I<=23, 0<=J, I+J<=38; all 660 rows including zero',
            'degree_guards': 'A_(0,15)=B_(0,25)=1; six nonorigin vertices guarded',
            'production_export_implemented': False}


def decode(wire):
    if len(wire) != 2 or any(len(p) != 2 for p in wire):
        raise ValueError('field wire shape')
    value = F(Q(int(wire[0][0]), int(wire[0][1])),
              Q(int(wire[1][0]), int(wire[1][1])))
    if value.wire() != wire:
        raise ValueError('noncanonical field wire')
    return value


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode()


def validate_contract(contract):
    expected = make_contract(contract['case'], contract['branch'])
    if canonical(expected) != canonical(contract):
        raise ValueError('contract differs from full fixed-face/source support specification')


def coefficient_row(left, right, output):
    """Forced-Q-exponent kernel; input values are coefficient polynomials.

    Coefficient polynomial: {sorted variable-id tuple: F}. A field constant
    uses (). Deliberate hard cap prevents production receiver expansion.
    """
    if len(left)*len(right) > 64:
        raise ValueError('PREP_ONLY: production-sized row assembly forbidden')
    I, J = output
    if I < 0 or J < 0:
        raise ValueError('ordinary coefficient index required')
    result = {}
    for (i, j), a in sorted(left.items()):
        k, l = I+1-i, J+1-j
        b = right.get((k, l))
        if b is None or k < 0 or l < 0:
            continue
        determinant = i*l-j*k
        if not determinant:
            continue
        for am, av in a.items():
            for bm, bv in b.items():
                monomial = tuple(sorted(am+bm))
                result[monomial] = result.get(monomial, ZERO)+determinant*av*bv
    return {m: c for m, c in result.items() if c != ZERO}


def toy_stream(left, right, outputs, scalar, variables):
    """Complete declared TOY row stream; preserves zeros and target obligation."""
    if len(left)*len(right) > 64 or len(outputs) > 64 or (2, 0) not in outputs:
        raise ValueError('invalid toy envelope or production attempt')
    if len(set(outputs)) != len(outputs):
        raise ValueError('duplicate row')
    records = [{'type': 'header', 'schema': 'jc2.toy-literal-field/v1',
                'field': 'Q[rho]/(rho^2-3*rho+1)', 'index_base': 0,
                'variables': variables, 'status': 'TOY_NOT_A_RECEIVER_EXPORT'}]
    term_count = zero_count = 0
    for I, J in sorted(outputs):
        terms = coefficient_row(left, right, (I, J))
        if (I, J) == (2, 0):
            for monomial, value in scalar.items():
                terms[monomial] = terms.get(monomial, ZERO)-value
        terms = {m: c for m, c in terms.items() if c != ZERO}
        term_count += len(terms)
        zero_count += not terms
        records.append({'type': 'row', 'label': f'J/{I}/{J}',
                        'terms': [[value.wire(), list(monomial)]
                                  for monomial, value in sorted(terms.items())]})
    prefix = b''.join(map(canonical, records))
    records.append({'type': 'footer', 'complete': True, 'rows': len(outputs),
                    'terms': term_count, 'zero_rows': zero_count,
                    'prefix_sha256': hashlib.sha256(prefix).hexdigest()})
    return b''.join(map(canonical, records))


def production_export(*args, **kwargs):
    raise RuntimeError('PREP_ONLY: production export is absent and unauthorized')


def verify_toy_stream(data, left, right, outputs, scalar, variables):
    """Strict complete-file self-replay, not independent certification."""
    records = [json.loads(line) for line in data.splitlines()]
    if b''.join(map(canonical, records)) != data:
        raise ValueError('noncanonical or truncated stream')
    if not records or records[-1].get('type') != 'footer':
        raise ValueError('missing terminal footer')
    if data != toy_stream(left, right, outputs, scalar, variables):
        raise ValueError('strict full toy replay mismatch')
