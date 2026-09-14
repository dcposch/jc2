"""Host-context-only literal original-row substitution replay; no CLI or CAS.

A later capped caller must supply the context from construction authority and
pin this file. This reuses exact multiplication, not the forcing/J/lift formula.
It does not by itself certify invertibility of the reconstruction graphs.
"""
import hashlib
from pathlib import Path
import construct as C


def decode_terms(terms, variables):
    out = {}
    previous = None
    for coefficient, monomial in terms:
        key = tuple(monomial)
        C.need(all(type(i) is int and 0 <= i < variables for i in key) and
               list(key) == sorted(key), 'invalid variable index/monomial')
        C.need(previous is None or previous < key, 'noncanonical term order/duplicate')
        previous = key
        value = C.rational(coefficient)
        C.need(value, 'explicit zero coefficient')
        out[key] = value
    C.need(C.wire(out) == terms, 'noncanonical coefficient wire')
    return out


def records(path):
    with Path(path).open('rb') as stream:
        digest = hashlib.sha256()
        footer_seen = False
        for line in stream:
            C.need(not footer_seen, 'bytes after footer')
            record = C.Q.strict_json(line)
            C.need(C.B.canonical(record) == line, 'noncanonical JSONL')
            if record['type'] == 'footer':
                C.need(record['complete'] is True and record['prefix_sha256'] == digest.hexdigest(),
                       'incomplete/footer hash drift')
                footer_seen = True
            else:
                digest.update(line)
            yield record
        C.need(footer_seen, 'missing complete footer')


def replay_frozen(source_path, construction_path, ops):
    C.need(ops.production, 'original-source replay requires host-authorized context')
    digest = hashlib.sha256()
    with Path(source_path).open('rb') as source:
        for block in iter(lambda: source.read(1024*1024), b''):
            ops.check({})
            digest.update(block)
    C.need(digest.hexdigest() == C.SOURCE, 'frozen original source hash mismatch')
    output = iter(records(construction_path))
    header = next(output)
    C.need(header['type'] == 'header' and header['source_sha256'] == C.SOURCE and
           header['symmetry_sha256'] == C.SYMMETRY and header['field'] == 'Q', 'construction header drift')
    names, original = header['variables'], header['original_variables']
    C.need(header['mode'] in ('slice', 'full') and
           len(names) == (22 if header['mode'] == 'slice' else 23) and len(original) == 269,
           'coordinate count drift')
    maps = {}
    for i in range(269):
        record = next(output)
        C.need(record['type'] == 'map' and record['original_index'] == i and record['name'] == original[i],
               'missing/reordered original variable map')
        maps[i] = ops.keep(decode_terms(record['terms'], len(names)))
    record = next(output)
    while record['type'] == 'graph':
        record = next(output)
    rows = residuals = terms = zeros = 0
    source_variables = []
    for literal in records(source_path):
        if literal['type'] == 'variable':
            C.need(literal['id'] == len(source_variables), 'source variable index')
            source_variables.append(literal['name'])
        if literal['type'] != 'row':
            continue
        C.need(source_variables == original, 'complete source variable names/order drift')
        p = C.transport(decode_terms(literal['terms'], 269), maps, ops)
        C.need(record['type'] == 'row' and record['original_index'] == rows and
               record['label'] == literal['label'], 'original row omission/reindexing')
        C.need(record['terms'] == C.wire(p), 'literal full-source transport mismatch')
        C.need(record['residual_index'] == (residuals if p else None), 'residual omission/reindexing')
        rows += 1
        residuals += bool(p)
        zeros += not p
        terms += len(p)
        record = next(output)
    C.need(rows == 803 and record['type'] == 'footer' and record['original_rows'] == rows and
           record['residuals'] == residuals and record['residual_terms'] == terms and
           record['zero_rows'] == zeros, 'complete original-row footer counts')
    C.need(next(output, None) is None, 'trailing construction output')
    return dict(status='ALL_ORIGINAL_ROWS_TRANSPORTED', rows=rows, residuals=residuals,
                scope='exact substitution only; graph isomorphism and source theorem externally reviewed')
