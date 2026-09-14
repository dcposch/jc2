"""Prospective controls6/10 fixture writer; NOT authority or a science verdict."""
import os
import sys

TAG = 'f10-r2-semantic-controls6-10-v1'
BASE_SHA = 'dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587'
BASE_BYTES = 1652675
CHECK_SHA = 'e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0'
ARITH_SHA = 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'
CAP = 15728640


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def main():
    # No JSON, Fraction, payload or scientific module before this interlock.
    if sys.platform != 'linux':
        raise SystemExit('REFUSED: Linux EC2 only')
    try:
        with open('/sys/class/dmi/id/sys_vendor', 'r', encoding='ascii') as f:
            vendor = f.read(128).strip()
    except OSError:
        raise SystemExit('REFUSED: no EC2 DMI identity')
    if vendor != 'Amazon EC2':
        raise SystemExit('REFUSED: off AWS')
    names = ('--registered-job', '--root-registration-sha256', '--self-sha256',
             '--checker', '--checker-arithmetic', '--input', '--output6', '--output10', '--receipt')
    if len(sys.argv) != 19 or tuple(sys.argv[1::2]) != names or sys.argv[2] != TAG:
        raise SystemExit('REFUSED: exact explicit controls6-10 vector required')
    args = dict(zip(names, sys.argv[2::2]))
    for key in ('--root-registration-sha256', '--self-sha256'):
        pin = args[key]
        need(len(pin) == 64 and all(c in '0123456789abcdef' for c in pin)
             and pin != '0' * 64, 'missing external pin')
    # ROOT must authenticate the registration; a CLI hash is NOT authority.
    import hashlib
    import stat

    def path(p):
        need(0 < len(p) <= 512 and os.path.isabs(p)
             and os.path.realpath(p) == p and '\n' not in p and '\r' not in p,
             'noncanonical path')
        return p

    def read(p, cap):
        fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, 'rb') as f:
            st = os.fstat(f.fileno())
            need(stat.S_ISREG(st.st_mode) and st.st_size <= cap, 'file type/size')
            raw = f.read(cap + 1)
            end = os.fstat(f.fileno())
            before = (st.st_dev, st.st_ino, st.st_mode, st.st_size, st.st_mtime_ns, st.st_ctime_ns)
            after = (end.st_dev, end.st_ino, end.st_mode, end.st_size, end.st_mtime_ns, end.st_ctime_ns)
            need(len(raw) <= cap and before == after, 'read drift/size')
            return raw

    def digest(raw):
        return hashlib.sha256(raw).hexdigest()

    me = path(os.path.abspath(__file__))
    cp, ap, inp, out6, out10, receipt = [path(args[k]) for k in
        ('--checker', '--checker-arithmetic', '--input', '--output6', '--output10', '--receipt')]
    need(len({me, cp, ap, inp, out6, out10, receipt}) == 7, 'paths must be distinct')
    sources = {me: args['--self-sha256'], cp: CHECK_SHA, ap: ARITH_SHA}

    def source_pins():
        for name, pin in sources.items():
            need(digest(read(name, 1048576)) == pin, 'source pin drift')

    source_pins()
    need(all(not os.path.lexists(p) for p in (out6, out10, receipt)), 'output collision')
    need(hasattr(sys, 'set_int_max_str_digits'), 'integer ceiling unavailable')
    sys.set_int_max_str_digits(4300)
    import json
    from fractions import Fraction

    def pairs(items):
        obj = {}
        for k, v in items:
            need(k not in obj, 'duplicate JSON key')
            obj[k] = v
        return obj

    def no_number(_):
        raise ValueError('numeric JSON forbidden')

    def loads(raw):
        return json.loads(raw.decode('ascii'), object_pairs_hook=pairs,
                          parse_int=no_number, parse_float=no_number,
                          parse_constant=no_number)

    def dumps(obj):
        return (json.dumps(obj, ensure_ascii=True, sort_keys=True,
                           separators=(',', ':')) + '\n').encode('ascii')

    def keys(obj, names):
        need(type(obj) is dict and set(obj) == set(names.split()), 'wire keys')

    def array(obj, n):
        need(type(obj) is list and len(obj) == n, 'wire array length')
        return obj

    def integer(s, signed=False, maximum=None):
        need(type(s) is str and 1 <= len(s) <= 4096, 'integer type/length')
        d = s[1:] if signed and s.startswith('-') else s
        need(bool(d) and all(c in '0123456789' for c in d), 'integer syntax')
        need(not (len(d) > 1 and d[0] == '0') and s != '-0', 'noncanonical integer')
        v = int(s)
        need(maximum is None or 0 <= v <= maximum, 'integer bound')
        return v

    def rational(s):
        need(type(s) is str and s.count('/') == 1, 'rational syntax')
        ns, ds = s.split('/')
        n, d = integer(ns, True), integer(ds)
        need(d > 0, 'rational denominator')
        v = Fraction(n, d)
        need(v.numerator == n and v.denominator == d, 'noncanonical rational')
        return v

    def wire(v):
        s = str(v.numerator) + '/' + str(v.denominator)
        need(rational(s) == v, 'changed coefficient exceeds wire bound')
        return s

    def elt(obj):
        for s in array(obj, 7):
            rational(s)

    terms = [0]

    def poly(obj):
        need(type(obj) is list and len(obj) <= 4096, 'polynomial term bound')
        terms[0] += len(obj)
        need(terms[0] <= 50000, 'aggregate term bound')
        previous = None
        for term in obj:
            ex, val = array(term, 2)
            e = tuple(integer(s, maximum=16) for s in array(ex, 6))
            elt(val)
            need(previous is None or previous < e, 'duplicate/unsorted term')
            need(any(s != '0/1' for s in val), 'zero sparse term')
            previous = e

    def validate(doc):
        terms[0] = 0
        keys(doc, 'format job_tag interface field source bands rows')
        need(doc['format'] == 'r2-reconstruction-19-v1'
             and doc['job_tag'] == 'f10-r2-reconstruction-v1', 'packet tag')
        f = doc['field']
        keys(f, 'P7 dL KL gamma W t5 H7 C D units')
        for v in array(f['P7'], 8):
            rational(v)
        for k in ('dL', 'KL', 'gamma', 'W', 't5', 'H7'):
            elt(f[k])
        poly(f['C']); poly(f['D'])
        units = {'dL', 'W', 't5', 'H7'} | {
            'gap' + str(h) + ':' + str(j) for h in range(1, 5) for j in range(3)}
        need(type(f['units']) is dict and set(f['units']) == units, 'unit inventory')
        for pair in f['units'].values():
            for v in array(pair, 2):
                elt(v)
        keys(doc['source'], 'Ahat Bhat U E Dpar Vpar Kpar Pihat')
        for p in doc['source'].values():
            poly(p)
        for h, b in enumerate(array(doc['bands'], 7), 1):
            if h < 5:
                keys(b, 'kind gap forcing part basisV matrix inverse rho A B')
                need(b['kind'] == ('early' if h < 4 else 'middle'), 'band kind')
                for p in array(b['basisV'], 3):
                    poly(p)
                for k in ('matrix', 'inverse'):
                    for row in array(b[k], 3):
                        for v in array(row, 3):
                            elt(v)
                ps = ('forcing', 'part', 'rho', 'A', 'B')
            else:
                keys(b, 'kind gap forcing part A_part fixed target A_var target_var B_var column lambda base value Psi A B')
                need(b['kind'] == 'column', 'column kind')
                for k in ('column', 'lambda'):
                    for v in array(b[k], 2):
                        elt(v)
                for p in array(b['base'], 2):
                    poly(p)
                ps = ('forcing', 'part', 'A_part', 'fixed', 'target', 'A_var',
                      'target_var', 'B_var', 'value', 'Psi', 'A', 'B')
            need(b['gap'] == str(h), 'ordered gap')
            for k in ps:
                poly(b[k])
        keys(doc['rows'], 'Psi K1 K0')
        for k, n in (('Psi', 3), ('K1', 7), ('K0', 9)):
            for p in array(doc['rows'][k], n):
                poly(p)

    raw = read(inp, CAP)
    need(len(raw) == BASE_BYTES and digest(raw) == BASE_SHA, 'baseline bytes/pin')
    doc = loads(raw)
    validate(doc)
    need(dumps(doc) == raw, 'noncanonical full JSON encoding')
    # Control6: bands is a seven-entry LIST, not a string-keyed dictionary.
    old_mate = doc['bands'][6]['B_var']
    theta2 = ['0', '0', '0', '0', '0', '2']
    one = ['1/1'] + ['0/1'] * 6
    need(any(e == theta2 and v == one for e, v in old_mate), 'gap7 unit theta2 missing')
    doc['bands'][6]['B_var'] = []
    raw6 = dumps(doc)
    restored6 = loads(raw6)
    validate(restored6)
    restored6['bands'][6]['B_var'] = old_mate
    need(dumps(restored6) == raw, 'control6 whole-subtree restore')
    doc = loads(raw)  # Control10 is independent, never composed with control6.
    best = None
    for family in ('Psi', 'K1', 'K0'):
        for ri, polynomial in enumerate(doc['rows'][family]):
            for ti, (ex, val) in enumerate(polynomial):
                for bi, s in enumerate(val):
                    q = rational(s)
                    if q and (best is None or abs(q) > best[0]):
                        best = (abs(q), family, ri, ti, bi, s, list(ex))
    if best is None:
        need(all(not p for family in doc['rows'].values() for p in family), 'zero-row encoding')
        term = [['0'] * 6, list(one)]
        doc['rows']['Psi'][0].append(term)
        selection = {'family': 'Psi', 'row': 0, 'term': 0, 'basis': 0,
                     'exponents': ['0'] * 6, 'old': '0/1', 'new': '1/1',
                     'fallback': 'insert constant term into empty first Psi', 'term_deleted': False}
    else:
        _, family, ri, ti, bi, old, ex = best
        val = doc['rows'][family][ri][ti][1]
        new = wire(rational(old) + 1)
        need(new != old, 'unchanged selected coefficient')
        val[bi] = new
        deleted = all(s == '0/1' for s in val)
        if deleted:
            del doc['rows'][family][ri][ti]
        selection = {'family': family, 'row': ri, 'term': ti, 'basis': bi,
                     'exponents': ex, 'old': old, 'new': new,
                     'fallback': None, 'term_deleted': deleted}
    raw10 = dumps(doc)
    restored10 = loads(raw10)
    validate(restored10)
    sel = selection
    p = restored10['rows'][sel['family']][sel['row']]
    if sel['fallback'] is not None:
        need(p == [[['0'] * 6, one]], 'fallback changed more than one term')
        p.clear()
    elif sel['term_deleted']:
        val = ['0/1'] * 7
        val[sel['basis']] = wire(rational(sel['new']) - 1)
        p.insert(sel['term'], [sel['exponents'], val])
    else:
        p[sel['term']][1][sel['basis']] = wire(
            rational(p[sel['term']][1][sel['basis']]) - 1)
    need(dumps(restored10) == raw, 'control10 whole-object inverse edit mismatch')
    for changed in (raw6, raw10):
        need(len(changed) <= CAP and digest(changed) != BASE_SHA, 'fixture bytes/digest')
    need(digest(raw6) != digest(raw10), 'fixtures not independently distinct')
    need(len(raw) + len(raw6) + len(raw10) + 32768 <= 16777216, 'joint fixture reserve')
    source_pins()
    need(read(inp, CAP) == raw, 'baseline prewrite drift')

    def write_exclusive(p, data):
        fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, 'wb') as f:
            need(f.write(data) == len(data), 'short write')
            f.flush()
            os.fchmod(f.fileno(), 0o444)
            os.fsync(f.fileno())
        dfd = os.open(os.path.dirname(p), os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)

    write_exclusive(out6, raw6)
    write_exclusive(out10, raw10)
    need(read(out6, CAP) == raw6 and read(out10, CAP) == raw10
         and read(inp, CAP) == raw, 'disk readback/drift')
    source_pins()
    meta = {'schema': 'f10-r2-controls6-10-fixtures/v1',
            'status': 'TWO_FIXTURES_WRITTEN_UNCHECKED', 'science_outcome': 'NONE',
            'job_tag': TAG, 'root_registration_sha256': args['--root-registration-sha256'],
            'sources': sources, 'input': {'path': inp, 'sha256': BASE_SHA, 'bytes': BASE_BYTES},
            'outputs': [
                {'control': 6, 'path': out6, 'sha256': digest(raw6), 'bytes': len(raw6),
                 'mutation': 'bands[6].B_var := []', 'gap': '7',
                 'old_subtree_sha256': digest(dumps(old_mate)), 'old_terms': len(old_mate)},
                {'control': 10, 'path': out10, 'sha256': digest(raw10), 'bytes': len(raw10),
                 'selection': selection}],
            'canonical_wire': True, 'inverse_edit_restores_whole_input_bytes': True,
            'checker_run': False}
    mr = dumps(meta)
    need(len(mr) <= 32768, 'receipt cap')
    write_exclusive(receipt, mr)
    need(read(receipt, 32768) == mr, 'receipt readback')
    # Silent normal exit 0 means ONLY fixture/readback metadata is complete.


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        raise SystemExit('STOP_CONTROLS6_10: ' + type(exc).__name__ + ': ' + str(exc))
