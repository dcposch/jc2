#!/usr/bin/env python3
"""Worker-only generic ordinary-coefficient audit prerequisite for sparse compression.

Replays the digest-pinned h/A/B setup. Pair-block regeneration is checked by
an independent direct derivative of fully expanded P and Q, exactly over Q.
Writes a physical coefficient stream and compact custody, preserving xy order.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import importlib.util
import json
import re
import resource
import time
from pathlib import Path
from flint import fmpq

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def imp(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory', type=Path, required=True)
    ap.add_argument('--roster', type=Path, required=True)
    ap.add_argument('--extractor', type=Path, required=True)
    ap.add_argument('--engine', type=Path, default=Path(__file__).with_name('fast_compress.py'))
    a = ap.parse_args()
    started = time.monotonic()
    engine = imp('ordinary_audit_engine', a.engine)
    assert sha(a.roster) == engine.ROSTER_SHA
    assert sha(a.extractor) == engine.EXTRACTOR_SHA
    sp = imp('ordinary_audit_sparse', a.extractor)
    engine.SP = sp
    d = a.directory.resolve()
    meta = json.loads((d/'meta.json').read_text())
    row = next(json.loads(l) for l in a.roster.read_text().splitlines()
               if json.loads(l)['row_id'] == meta['row_id'])
    rc = row['receiver_chart']
    program = (d/'pinned-builder.sing').read_text()
    program_sha = hashlib.sha256(program.encode()).hexdigest()
    assert program_sha == rc['production_emitter_dry_run']['emitted_program_sha256']
    names = meta['variables']
    assert len(names) == len(set(names)) == rc['unknowns_without_T']
    match = re.search(r'^ring R=0,\((.*?)\),\(lp\(1\),dp\((\d+)\)\);$', program, re.M)
    assert match and match[1].split(',') == ['y','x'] + names and names[-1] == 'c'
    nums = {v: i for i, v in enumerate(names)}
    setup = dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$', program, re.M))
    base = {k: sp.parse_base_polynomial(v, nums) for k, v in setup.items()}
    for table in base.values():
        for poly in table.values():
            for mon in poly: poly[mon] = fmpq(poly[mon])
    e, q, ell = rc['e'], rc['q'], row['own_child']['ell']
    ordinary = engine.regenerate(base, e, q, nums['c'], ell)
    total = sp.count_terms(ordinary)
    print(json.dumps(dict(phase='pair_expanded',row_id=row['row_id'],rows=len(ordinary),
        terms=total,wall_seconds=round(time.monotonic()-started,3))),flush=True)
    one = {(0,0): {(): fmpq(1)}}
    hp = {0: one}
    for i in range(1, max(e,q)+1): hp[i] = sp.bp_mul(hp[i-1], base['h'])
    P = {}; Q = {}
    sp.bp_addto(P,hp[e]); sp.bp_addto(Q,hp[q])
    for i in range(1,e+1): sp.bp_addto(P,sp.bp_mul(base[f'AA{i}'],hp[e-i]))
    for i in range(2,q+1): sp.bp_addto(Q,sp.bp_mul(base[f'BB{i}'],hp[q-i]))
    control = sp.bp_jac(P,Q)
    target = control.setdefault((ell,0),{})
    sp.pp_addto(target,{(nums['c'],): fmpq(1)},-1)
    if not target: del control[(ell,0)]
    assert control == ordinary
    expected_terms = {'R005':2902778,'R006':3743297,'R008':6373619}
    if row['row_id'] in expected_terms: assert total == expected_terms[row['row_id']]
    expected_rows = {'R005':484,'R006':494}
    if row['row_id'] in expected_rows: assert len(ordinary) == expected_rows[row['row_id']]
    del control,P,Q,hp
    stream = d/'sparse-ordinary.tsv'
    audit = d/'sparse-ordinary.json'
    assert not stream.exists() and not audit.exists()
    coords = []
    with stream.open('w',buffering=1<<20) as f:
        f.write('index|x_power|y_power|expr\n')
        for i, ((x,y), poly) in enumerate(sorted(ordinary.items()),1):
            assert poly
            f.write(f'{i}|{x}|{y}|{sp.pp_text(poly,names)}\n')
            coords.append((x,y))
    physical_rows = physical_terms = 0
    with stream.open() as f:
        assert next(f).strip() == 'index|x_power|y_power|expr'
        for line in f:
            idx,x,y,expr = line.rstrip().split('|',3)
            assert int(idx) == physical_rows+1
            assert (int(x),int(y)) == coords[physical_rows]
            physical_rows += 1
            physical_terms += sum(1 for _ in re.finditer(r'[+-]?[^+-]+',expr))
    assert physical_rows == len(ordinary) and physical_terms == total
    result = dict(schema='classA-sparse-ordinary/v1',row_id=row['row_id'],
        status='EXACT_Z_PAIR_LEVELS_AND_DIRECT_DERIVATIVE_EQUAL',
        rows=physical_rows,terms=physical_terms,native_hadic_generators=rc['coefficient_generators'],
        ordinary_stream_bytes=stream.stat().st_size,ordinary_stream_sha256=sha(stream),
        ordinary_coordinate_sha256=hashlib.sha256(''.join(f'{x}|{y}\n' for x,y in coords).encode()).hexdigest(),
        source_program_sha256=program_sha,worker_script_sha256=sha(__file__),
        engine_sha256=sha(a.engine),extractor_sha256=sha(a.extractor),
        wall_seconds=round(time.monotonic()-started,3),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    audit.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result),flush=True)

if __name__ == '__main__': main()
