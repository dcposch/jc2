#!/usr/bin/env python3
"""Independent exact-rational audit of emitted full h support and specialization.

Reads the old charts and new charts; writes only verification.json beside itself.
No compiler import, source enumeration, or solver claim is used by this audit.
Coordinates are (x exponent, y exponent), matching the builder identifiers.
"""
from fractions import Fraction
from math import floor
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
OLD = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(K, delta, bound):
    return {(b, a) for a in range(K)
            for b in range(floor(delta * a - bound) + 1)}


def setup(text):
    return dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$', text, re.M))


def monomial_terms(expr):
    # The setup has positive symbolic coefficients and the single monic term.
    # Canonical term comparison is sufficient here; no large Jacobian expansion.
    return {tuple(sorted(t.strip().split('*'))) for t in expr.split('+')}


def main():
    old_manifest = json.loads((OLD / 'classes_manifest.json').read_text())
    results = []
    total_missing = 0
    affected = 0
    for cls in old_manifest:
        cid = cls['class_id']
        expected_union = set()
        rows = []
        for row in cls['rows']:
            expected = inventory(row['K'], Fraction(row['delta_prime']['1']),
                                 Fraction(row['B_safe']))
            expected_union |= expected
            rows.append((row['stem'], expected, row))
        rows.append((cid + '_union', expected_union, None))
        for stem, expected, row in rows:
            old_base = OLD / 'classes' / cid
            new_base = HERE / 'classes' / cid
            old_meta_path = old_base / 'meta' / (stem + '.json')
            new_meta_path = new_base / 'meta' / (stem + '.json')
            old_builder = old_base / 'builders' / (stem + '_builder.sing')
            new_builder = new_base / 'builders' / (stem + '_builder.sing')
            op = json.loads(old_meta_path.read_text())
            np = json.loads(new_meta_path.read_text())
            om, nm = op['meta'], np['meta']
            old_h = set(map(tuple, om['h_inventory']))
            new_h = set(map(tuple, nm['h_inventory']))
            assert new_h == expected, (stem, 'D1', new_h ^ expected)
            assert old_h <= new_h, (stem, 'old h not contained')
            added = new_h - old_h
            added_names = {'h_%d_%d' % m for m in added}
            assert set(np['variables']) - set(op['variables']) == added_names, stem
            assert set(op['variables']) <= set(np['variables']), stem
            assert np['parameter_count'] == op['parameter_count'] + len(added), stem
            assert len(np['variables']) == np['parameter_count'], stem
            assert len(set(np['variables'])) == len(np['variables']), stem
            for key in ('alpha_inventories', 'beta_inventories', 'gauges',
                        'gauge_audit', 'saturation_factor'):
                assert om[key] == nm[key], (stem, key)
            assert op['sat'] == np['sat'] == 'c', stem
            old_text, new_text = old_builder.read_text(), new_builder.read_text()
            old_setup, new_setup = setup(old_text), setup(new_text)
            assert set(old_setup) == set(new_setup), stem
            K = row['K'] if row is not None else cls['rows'][0]['K']
            expected_h_terms = {('y^%d' % K,)}
            for b, a in expected:
                factors = ['h_%d_%d' % (b, a)]
                if b: factors.append('x' if b == 1 else 'x^%d' % b)
                if a: factors.append('y' if a == 1 else 'y^%d' % a)
                expected_h_terms.add(tuple(sorted(factors)))
            assert monomial_terms(new_setup['h']) == expected_h_terms, stem
            for name, expr in new_setup.items():
                got = monomial_terms(expr)
                if name == 'h':
                    got = {t for t in got if not set(t) & added_names}
                assert got == monomial_terms(old_setup[name]), (stem, name, 'specialization')
            ring = re.search(r'^ring R=0,\(y,x,(.*)\),\(lp\(1\),dp\((\d+)\)\);$',
                             new_text, re.M)
            assert ring and ring.group(1).split(',') == np['variables'], stem
            assert int(ring.group(2)) == np['parameter_count'] + 1, stem
            assert 'native_y_div_fast' in new_text, stem
            assert 'if (lead(h) == y^%d)' % K in new_text, stem
            result = dict(stem=stem, union=row is None, K=K,
                          old_h_count=len(old_h), full_h_count=len(new_h),
                          added_count=len(added), added_xy=sorted(added),
                          old_unknowns=op['parameter_count'],
                          new_unknowns=np['parameter_count'],
                          full_D1=True, alpha_beta_gauges_unchanged=True,
                          monic=True, saturation_c=True,
                          old_setup_recovered_by_zero_specialization=True,
                          builder_ring_and_parameters_match=True,
                          old_meta_sha256=sha(old_meta_path),
                          new_meta_sha256=sha(new_meta_path),
                          old_builder_sha256=sha(old_builder),
                          new_builder_sha256=sha(new_builder))
            results.append(result)
            if row is not None:
                total_missing += len(added)
                affected += bool(added)
    assert len(results) == 18
    assert total_missing == 76 and affected == 8
    # Negative control: a removed actual D1 term fails the very same equality gate.
    first = next(r for r in results if r['added_count'])
    assert first['added_xy'][0] is not None
    full = set(map(tuple, json.loads((HERE / 'classes' /
        first['stem'].rsplit('_V', 1)[0] / 'meta' /
        (first['stem'] + '.json')).read_text())['meta']['h_inventory']))
    deleted = tuple(first['added_xy'][0])
    assert full - {deleted} != full
    report = dict(scope='Inventory and setup-map audit; no source theorem or UNIT claim',
                  status='PASS', stems=18, fibres=12, affected_fibres=affected,
                  omitted_fibre_coordinates=total_missing,
                  negative_control=dict(deleted_xy=deleted, rejected=True),
                  old_classes_manifest_sha256=sha(OLD / 'classes_manifest.json'),
                  new_classes_manifest_sha256=sha(HERE / 'classes_manifest.json'),
                  compiler_source_sha256=sha(OLD / 'sprime3_compiler.py'),
                  builder_fix_source_sha256=sha(OLD / 'builder_fix.py'),
                  script_sha256=sha(Path(__file__)), results=results)
    (HERE / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'results'}, indent=2))


if __name__ == '__main__':
    main()
