"""Shared strict serialization only; no field, column or solver arithmetic."""
import json
import os


class WireError(ValueError):
    pass


def require(ok, label):
    if not ok:
        raise WireError(label)


def keys(obj, expected):
    require(isinstance(obj, dict) and set(obj) == set(expected.split()), 'object keys')


def array(obj, n):
    require(isinstance(obj, list) and len(obj) == n, 'fixed array length')
    return obj


def integer(s, bound=None, signed=False):
    require(isinstance(s, str) and 1 <= len(s) <= 4096, 'integer type/length')
    d = s[1:] if signed and s.startswith('-') else s
    require(bool(d) and all(c in '0123456789' for c in d), 'integer syntax')
    require((len(d) == 1 or d[0] != '0') and s != '-0', 'integer canonical')
    n = int(s)
    require(bound is None or 0 <= n <= bound, 'integer bound')
    return n


def rational(s):
    from math import gcd
    require(isinstance(s, str) and s.count('/') == 1, 'rational syntax')
    a, b = s.split('/')
    n, d = integer(a, signed=True), integer(b)
    require(d > 0 and gcd(n, d) == 1, 'rational reduced/positive')
    return n, d


def decode(raw):
    def pairs(xs):
        out = {}
        for k, v in xs:
            require(k not in out, 'duplicate JSON key')
            out[k] = v
        return out

    def bad(_):
        raise WireError('native JSON number/constant')

    try:
        doc = json.loads(raw, object_pairs_hook=pairs, parse_int=bad,
                         parse_float=bad, parse_constant=bad)
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise WireError('strict JSON') from exc
    stack, count = [(doc, 0)], 0
    while stack:
        item, depth = stack.pop()
        count += 1
        require(count <= 16000000 and depth <= 32, 'JSON node/depth cap')
        if isinstance(item, str):
            require(len(item) <= 8193, 'string cap')
        elif isinstance(item, list):
            require(len(item) <= 400000, 'array cap')
            stack.extend((v, depth + 1) for v in item)
        elif isinstance(item, dict):
            require(len(item) <= 256, 'object cap')
            require(all(isinstance(k, str) and len(k) <= 256 for k in item), 'key cap')
            stack.extend((v, depth + 1) for v in item.values())
        else:
            raise WireError('non-string scalar, including bool/null')
    return doc


def load(path, cap, expected_sha):
    import hashlib
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, 'rb') as f:
        raw = f.read(cap + 1)
    require(len(raw) <= cap, 'byte cap')
    require(hashlib.sha256(raw).hexdigest() == expected_sha, 'whole input readback hash')
    return decode(raw)


def encode(doc):
    return (json.dumps(doc, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode('ascii')


def baseline(doc):
    keys(doc, 'format job_tag interface base source bands raw graph')
    require(doc['format'] == 'r3-source-cone-reconstruction-v1'
            and doc['job_tag'] == 'f10-source-cone-r3-reconstruction-v1', 'source format/job')
    labels = ['K8', 'K9', 'K10'] + ['A1_' + str(i) for i in range(1, 10)] + ['A0_' + str(i) for i in range(1, 13)] + ['T']
    expected = {'raw_variables': ['X1', 'X2', 'X3', 'X4', 'z', 'S', 'theta'],
        'raw_weights': ['1', '2', '3', '4', '7', '1', '3'],
        'graph_variables': ['X1', 'X2', 'X3', 'X4'], 'graph_weights': ['1', '2', '3', '4'],
        'base': 'WHOLE Q[V]/P7; basis 1,V,...,V^6', 'scale': 'z=s^2; s invertible',
        'targets': ['P1_0-U*s^5', 'P0_0-s^7'], 'guard': 'omega=W*t5*s^8',
        'graph_guard': 'g=Hq*ell', 'graph_rows': labels,
        'jacobian_order': 'j=0..7;i=0..23-3j', 'low_order': 'P1:i=0..20;P0:i=0..23'}
    require(doc['interface'] == expected, 'literal source interface')
    keys(doc['base'], 'P7 dL KL gamma W t5 middleH7 C D units')
    keys(doc['source'], 'Ahat Bhat U E Dpar Vpar Kpar Pihat')
    array(doc['bands'], 10)
    keys(doc['raw'], 'Psi P1 P0 jacobian_slots')
    for name, n in (('Psi', 4), ('P1', 21), ('P0', 24), ('jacobian_slots', 108)):
        array(doc['raw'][name], n)
    keys(doc['graph'], 'Hq c c_inverse zeta slots ell g U')
    modulus = [rational(s) for s in array(doc['base']['P7'], 8)]
    total = [0]

    def poly(a):
        require(isinstance(a, list) and len(a) <= 20000, 'polynomial term cap')
        total[0] += len(a)
        require(total[0] <= 400000, 'graph aggregate term cap')
        out, prior = [], None
        for term in a:
            e, v = array(term, 2)
            ex = tuple(integer(s, cap) for s, cap in zip(array(e, 4), (30, 15, 10, 7)))
            coeff = tuple(rational(s) for s in array(v, 7))
            require((prior is None or prior < ex) and any(n for n, _ in coeff), 'sparse order/nonzero')
            prior = ex
            out.append((ex, coeff))
        return out

    graph = doc['graph']
    polys = [poly(v) for v in array(graph['slots'], 25)]
    extras = {name: poly(graph[name]) for name in ('Hq', 'zeta', 'ell', 'g', 'U')}
    constants = {name: tuple(rational(s) for s in array(graph[name], 7)) for name in ('c', 'c_inverse')}
    # This validates the extracted wire, not the original Euler/raw equations.
    # The ROOT-qualified source-checker binding is a separate required premise.
    return modulus, polys, extras, constants
