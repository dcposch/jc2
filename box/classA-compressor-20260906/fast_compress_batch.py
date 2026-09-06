#!/usr/bin/env python3
"""Worker-only exact-Q elimination with batches of whole coefficient rows.

Every pivot is a scalar-monic whole coefficient row. Substitution fixes x,y,
so it commutes with differentiation and coefficient extraction: regenerating
J from the substituted h/A/B blocks is exactly mapping every old constraint.
No unknown coefficient is treated as a coefficient-field transcendental.
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
from collections import defaultdict
from pathlib import Path
from flint import fmpq

EXTRACTOR_SHA = 'a1c24fc7b7b4732ec3a78efe968763abe9846418bab80fff8e7128a224386516'
ROSTER_SHA = 'cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf'

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def substitute(poly, variable, rhs):
    """Exact arbitrary polynomial substitution in tuple-monomial storage."""
    out = {}
    powers = {0: {(): fmpq(1)}, 1: rhs}
    for mon, coeff in poly.items():
        exponent = mon.count(variable)
        if not exponent:
            value = out.get(mon, 0) + coeff
            if value: out[mon] = value
            else: out.pop(mon, None)
            continue
        if not rhs: continue
        for e in range(2, exponent + 1):
            if e not in powers: powers[e] = SP.pp_mul(powers[e-1], rhs)
        other = tuple(i for i in mon if i != variable)
        for rm, rc in powers[exponent].items():
            product = SP.merge_monomials(other, rm)
            value = out.get(product, 0) + coeff * rc
            if value: out[product] = value
            else: out.pop(product, None)
    return out

def subst_blocks(blocks, variable, rhs):
    result = {}
    for name, table in blocks.items():
        result[name] = {}
        for xy, poly in table.items():
            value = substitute(poly, variable, rhs)
            if value: result[name][xy] = value
    return result

def derivative(poly, variable):
    out = {}
    for mon, coeff in poly.items():
        e = mon.count(variable)
        if e:
            j = mon.index(variable)
            out[mon[:j] + mon[j+1:]] = coeff * e
    return out

def candidate(poly, forbidden):
    possible = {m[0] for m in poly if len(m) == 1 and m[0] not in forbidden}
    for mon in poly:
        if len(mon) > 1:
            possible.difference_update(mon)
            if not possible: return None
    return min(possible) if possible else None

def regenerate(blocks, e, q, c_index, ell):
    one = {(0, 0): {(): fmpq(1)}}
    P = [(one, e)] + [(blocks[f'AA{i}'], e-i) for i in range(1, e+1)]
    Q = [(one, q)] + [(blocks[f'BB{i}'], q-i) for i in range(2, q+1)]
    levels = defaultdict(dict)
    h = blocks['h']
    for left, r in P:
        for right, s in Q:
            SP.bp_addto(levels[r+s], SP.bp_jac(left, right))
            if r+s:
                lower = {}
                if s: SP.bp_addto(lower, SP.bp_scaled_product(right, SP.bp_jac(left, h), s))
                if r: SP.bp_addto(lower, SP.bp_scaled_product(left, SP.bp_jac(h, right), r))
                SP.bp_addto(levels[r+s-1], lower)
    powers = {0: one}
    top = max((i for i, table in levels.items() if table), default=0)
    for i in range(1, top+1): powers[i] = SP.bp_mul(powers[i-1], h)
    result = {}
    for level in sorted(levels):
        if levels[level]: SP.bp_addto(result, SP.bp_mul(levels[level], powers[level]))
    target = result.setdefault((ell, 0), {})
    SP.pp_addto(target, {(c_index,): fmpq(1)}, -1)
    if not target: del result[(ell, 0)]
    return result

def controls():
    a, b, c = 0, 1, 2
    f = {(a,a,b): fmpq(1), (a,): fmpq(3), (b,): fmpq(1)}
    rhs = {(b,): fmpq(1), (): fmpq(1)}
    assert substitute(f, a, rhs) == {(b,b,b): 1, (b,b): 2, (b,): 5, (): 3}
    positive = {(a,): fmpq(3), (b,b): fmpq(1), (): fmpq(-2)}
    assert candidate(positive, {c}) == a
    right = {(b,b): fmpq(-1,3), (): fmpq(2,3)}
    assert derivative(positive, a) == {(): 3}
    assert not substitute(positive, a, right)
    assert candidate({(a,): 1, (a,a): 1}, {c}) is None
    assert candidate({(a,): 1, (a,b): 1}, {c}) is None
    assert candidate({(c,): 1, (a,a): 1}, {c}) is None
    toy = {'h': {(0,2): {(): fmpq(1)}, (1,0): {(a,): fmpq(1)}, (0,0): {(b,): fmpq(1)}},
           'AA1': {(0,1): {(a,): fmpq(1)}, (1,0): {(b,): fmpq(1)}},
           'AA2': {(0,0): {(b,): fmpq(1)}},
           'AA3': {(1,1): {(a,): fmpq(1)}},
           'BB2': {(1,0): {(a,): fmpq(1)}, (0,1): {(b,): fmpq(1)}}}
    before = regenerate(toy, 3, 2, c, 0)
    mapped = {xy: substitute(poly, a, right) for xy, poly in before.items()}
    mapped = {xy: poly for xy, poly in mapped.items() if poly}
    assert regenerate(subst_blocks(toy, a, right), 3, 2, c, 0) == mapped
    print('CONTROL_ARBITRARY_SUBSTITUTION=PASS', flush=True)
    print('CONTROL_NONLINEAR_MIXED_AND_C_PIVOTS_REJECTED=PASS', flush=True)
    print('CONTROL_REGENERATION_EQUALS_ROW_MAP=PASS', flush=True)

def main():
    global SP
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory', required=True, type=Path)
    ap.add_argument('--roster', required=True, type=Path)
    ap.add_argument('--extractor', required=True, type=Path)
    ap.add_argument('--output', required=True, type=Path)
    ap.add_argument('--cache-limit', type=int, default=1000)
    ap.add_argument('--seed-transcript', type=Path)
    ap.add_argument('--seed-pivots', type=int, default=0)
    ap.add_argument('--seed-expected-generators', type=int)
    ap.add_argument('--seed-expected-terms', type=int)
    args = ap.parse_args()
    assert args.cache_limit > 0 and args.seed_pivots >= 0
    started = time.monotonic()
    assert sha(args.extractor) == EXTRACTOR_SHA
    assert sha(args.roster) == ROSTER_SHA
    spec = importlib.util.spec_from_file_location('fast_sparse_exact', args.extractor)
    SP = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SP)
    controls()
    source = args.directory.resolve()
    out = args.output.resolve()
    out.mkdir(exist_ok=False)
    meta = json.loads((source/'meta.json').read_text())
    row = next(json.loads(l) for l in args.roster.read_text().splitlines()
               if json.loads(l)['row_id'] == meta['row_id'])
    rc = row['receiver_chart']
    program = (source/'pinned-builder.sing').read_text()
    assert hashlib.sha256(program.encode()).hexdigest() == rc['production_emitter_dry_run']['emitted_program_sha256']
    names = meta['variables']
    assert len(names) == len(set(names)) == rc['unknowns_without_T']
    assert names[-1] == 'c'
    match = re.search(r'^ring R=0,\((.*?)\),\(lp\(1\),dp\((\d+)\)\);$', program, re.M)
    assert match and match[1].split(',') == ['y','x'] + names
    indices = {v: i for i, v in enumerate(names)}
    setup = dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$', program, re.M))
    blocks = {name: SP.parse_base_polynomial(expr, indices) for name, expr in setup.items()}
    for table in blocks.values():
        for poly in table.values():
            for mon in poly: poly[mon] = fmpq(poly[mon])
    original_blocks = {name: {xy: dict(poly) for xy, poly in table.items()} for name, table in blocks.items()}
    e, q, ell, ci = rc['e'], rc['q'], row['own_child']['ell'], indices['c']
    current = regenerate(blocks, e, q, ci, ell)
    initial_terms = SP.count_terms(current)
    # Exact byte comparison with the independently differentiated sparse source.
    source_audit = json.loads((source/'sparse-ordinary.json').read_text())
    initial_hash = hashlib.sha256()
    initial_hash.update(b'index|x_power|y_power|expr\n')
    for k, ((x,y), poly) in enumerate(sorted(current.items()), 1):
        initial_hash.update(f'{k}|{x}|{y}|{SP.pp_text(poly,names)}\n'.encode())
    assert initial_hash.hexdigest() == source_audit['ordinary_stream_sha256']
    assert len(current) == source_audit['rows'] and initial_terms == source_audit['terms']
    print('DIRECT_ORIENTATION=PASS', flush=True)
    print(f'DIRECT_J_TERMS={initial_terms}', flush=True)
    print(f'ORDINARY_GENERATORS={len(current)}', flush=True)
    print(f'ORDINARY_TERMS={initial_terms}', flush=True)
    images = [{(i,): fmpq(1)} for i in range(len(names))]
    gone = set()
    audit = (out/'pivot-audit.tsv').open('w', buffering=1)
    xy_audit = (out/'pivot-coordinates.tsv').open('w', buffering=1)
    audit.write('step|row_slot|variable|unit|row_terms|rhs_terms|rhs\n')
    xy_audit.write('step|x_power|y_power|derivative_scalar_check|image_zero_check\n')
    original_xy = set(current)
    chosen = set()
    if args.seed_pivots:
        assert args.seed_transcript is not None
        ss = importlib.util.spec_from_file_location('batch_snapshot_checks', Path(__file__).with_name('snapshot_rebase.py'))
        snapshot = importlib.util.module_from_spec(ss); ss.loader.exec_module(snapshot); snapshot.SP = SP
        seed_lines = (args.seed_transcript/'pivot-audit.tsv').read_text().splitlines()
        seed_xy = (args.seed_transcript/'pivot-coordinates.tsv').read_text().splitlines()
        assert len(seed_lines) >= args.seed_pivots+2 and len(seed_xy) >= args.seed_pivots+2
        seed_lines = seed_lines[:args.seed_pivots+1]; seed_xy = seed_xy[:args.seed_pivots+1]
        (out/'seed-pivot-audit.tsv').write_text('\n'.join(seed_lines)+'\n')
        (out/'seed-pivot-coordinates.tsv').write_text('\n'.join(seed_xy)+'\n')
        for step, (line, xyline) in enumerate(zip(seed_lines[1:],seed_xy[1:]),1):
            f = line.split('|',6); pos = xyline.split('|')
            assert int(f[0]) == int(pos[0]) == step and pos[3:] == ['PASS','PASS']
            v = indices[f[2]]; unit = fmpq(f[3]); rhs = snapshot.parse_q(f[6],indices)
            xy = int(pos[1]),int(pos[2])
            assert v not in gone and v != ci and xy not in chosen
            assert not any((gone|{v}).intersection(mon) for mon in rhs)
            actual = snapshot.coefficient_at(blocks,e,q,ci,ell,xy)
            reconstructed = {(v,):unit}; SP.pp_addto(reconstructed,rhs,-unit)
            assert actual == reconstructed and len(actual) == int(f[4]) and len(rhs) == int(f[5])
            assert derivative(actual,v) == {():unit} and not substitute(actual,v,rhs)
            blocks = subst_blocks(blocks,v,rhs)
            images = [substitute(image,v,rhs) for image in images]
            gone.add(v); chosen.add(xy)
            audit.write(line+'\n'); xy_audit.write(xyline+'\n')
            print(f'SEED_REPLAY_PIVOT={step} var={names[v]} wall_seconds={time.monotonic()-started:.3f}',flush=True)
        current = regenerate(blocks,e,q,ci,ell)
        assert not chosen.intersection(current) and set(current) <= original_xy
        assert args.seed_expected_generators is not None and len(current) == args.seed_expected_generators
        assert args.seed_expected_terms is not None and SP.count_terms(current) == args.seed_expected_terms
        print(f'SEED_REPLAY_MATCH=PASS pivots={len(gone)} generators={len(current)} terms={SP.count_terms(current)}',flush=True)
    cache = {}
    dirty = False
    refreshes = 0
    while True:
        selected = None
        for xy, poly in sorted(cache.items(), key=lambda item: (len(item[1]), item[0])):
            v = candidate(poly, gone | {ci})
            if v is not None:
                selected = xy, poly, v
                break
        if selected is None:
            if dirty:
                current = regenerate(blocks,e,q,ci,ell)
                refreshes += 1
                assert not chosen.intersection(current) and set(current) <= original_xy
                dirty = False
                print(f'BATCH_REFRESH={refreshes} pivots={len(gone)} generators={len(current)} terms={SP.count_terms(current)} '
                      f'wall_seconds={time.monotonic()-started:.3f} peak_rss_kib={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}',flush=True)
            # A fixed point is claimed only after inspecting every genuine row.
            for xy, poly in sorted(current.items(), key=lambda item: (len(item[1]), item[0])):
                v = candidate(poly, gone | {ci})
                if v is not None:
                    selected = xy, poly, v
                    break
            if selected is None:
                print('FULL_ROW_SCALAR_MONIC_FIXED_POINT=PASS',flush=True)
                break
            slots = {xy:k for k,xy in enumerate(sorted(current),1)}
            cache = {xy:poly for xy,poly in current.items() if len(poly) <= args.cache_limit}
            cache[selected[0]] = selected[1]
        xy, poly, v = selected
        unit = poly[(v,)]
        assert unit and derivative(poly,v) == {():unit}
        rhs = {mon:-coeff/unit for mon,coeff in poly.items() if mon != (v,)}
        assert not derivative(rhs,v) and not substitute(poly,v,rhs)
        assert v not in gone and xy not in chosen
        gone.add(v); chosen.add(xy)
        step = len(gone)
        audit.write(f'{step}|{slots[xy]}|{names[v]}|{unit}|{len(poly)}|{len(rhs)}|{SP.pp_text(rhs,names)}\n')
        xy_audit.write(f'{step}|{xy[0]}|{xy[1]}|PASS|PASS\n')
        blocks = subst_blocks(blocks,v,rhs)
        images = [substitute(image,v,rhs) for image in images]
        updated_cache = {}
        for pos, cached in cache.items():
            mapped = substitute(cached,v,rhs)
            # Eviction changes scheduling only; no polynomial is truncated.
            if mapped and len(mapped) <= 10*args.cache_limit: updated_cache[pos] = mapped
        cache = updated_cache
        assert not chosen.intersection(cache)
        dirty = True
        print(f'PIVOT={step} var={names[v]} cache_rows={len(cache)} cache_terms={SP.count_terms(cache)} '
              f'full_counts_pending=1 wall_seconds={time.monotonic()-started:.3f}',flush=True)
    # Cheap independent image check on every original coefficient slot.
    for name, table in original_blocks.items():
        assert set(blocks[name]) <= set(table)
        for xy, poly in table.items():
            evaluated = {}
            for mon, coefficient in poly.items():
                assert len(mon) <= 1
                image = images[mon[0]] if mon else {():fmpq(1)}
                SP.pp_addto(evaluated,image,coefficient)
            assert evaluated == blocks[name].get(xy,{})
    print('FINAL_BLOCKS_EQUAL_ORIGINAL_SLOT_IMAGES=PASS',flush=True)
    audit.close(); xy_audit.close()
    for image in images:
        assert all(not gone.intersection(mon) for mon in image)
    for table in list(blocks.values()) + [current]:
        for poly in table.values(): assert all(not gone.intersection(mon) for mon in poly)
    assert images[ci] == {(ci,): 1}
    for i in set(range(len(names))) - gone: assert images[i] == {(i,): 1}
    with (out/'images.tsv').open('w') as f:
        f.write('variable|image\n')
        for name, image in zip(names, images): f.write(name+'|'+SP.pp_text(image,names)+'\n')
    full_terms = SP.count_terms(current)
    c1 = {}
    for xy, poly in current.items():
        value = substitute(poly, ci, {(): fmpq(1)})
        if value: c1[xy] = value
    with (out/'compressed-Q.tsv').open('w', buffering=1<<20) as f, (out/'compress.sing').open('w', buffering=1<<20) as sf:
        f.write('index|expr\n')
        sf.write('// Final presentation generated by fast_compress.py, not its execution driver.\n')
        sf.write(match[0]+'\nideal I=\n')
        for k, (xy, poly) in enumerate(sorted(current.items()), 1):
            expr = SP.pp_text(poly,names)
            f.write(f'{k}|{expr}\n')
            if k > 1: sf.write(',\n')
            sf.write(expr)
        if not current: sf.write('0')
        sf.write(';\nprint("SPARSE_POSTCOMPRESSION_PRESENTATION=1");\nquit;\n')
    with (out/'compressed-c1.tsv').open('w', buffering=1<<20) as f:
        f.write('index|expr\n')
        for k, (xy, poly) in enumerate(sorted(c1.items()), 1):
            f.write(f'{k}|{SP.pp_text(poly,names)}\n')
    (out/'pinned-builder.sing').write_text(program)
    meta.update(compression_engine='exact fmpq whole-row batches with block regeneration',
                compression_driver_sha256=sha(__file__),
                cache_limit=args.cache_limit, batch_refreshes=refreshes, seed_pivots=args.seed_pivots,
                compression_program_sha256=sha(out/'compress.sing'),
                initial_ordinary_stream_sha256=initial_hash.hexdigest(),
                sparse_extractor_sha256=EXTRACTOR_SHA,
                controls='arbitrary substitution; rejected nonlinear/mixed/c pivots; regeneration commutes on exact toy; final original-slot image equality',
                regeneration_lemma='x,y fixed; coefficient substitution commutes with J and coefficient extraction')
    dump(out/'meta.json', meta)
    print(f'COMPRESSED_VARIABLES={len(names)-len(gone)}', flush=True)
    print(f'COMPRESSED_GENERATORS={len(current)}', flush=True)
    print(f'COMPRESSED_TERMS={full_terms}', flush=True)
    print(f'C1_VARIABLES={len(names)-len(gone)-1}', flush=True)
    print(f'C1_GENERATORS={len(c1)}', flush=True)
    print(f'C1_TERMS={SP.count_terms(c1)}', flush=True)
    dump(out/'engine.json', dict(driver_sha256=sha(__file__), initial_ordinary_terms=initial_terms,
        pivots=len(gone), full_variables=len(names)-len(gone), full_generators=len(current),
        full_terms=full_terms, c1_variables=len(names)-len(gone)-1, c1_generators=len(c1),
        c1_terms=SP.count_terms(c1), wall_seconds=round(time.monotonic()-started,3),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    print('COMPRESSION_COMPLETE=1', flush=True)

if __name__ == '__main__': main()
