#!/usr/bin/env python3
"""Bounded exact parser/ring-map controls; no Groebner or solver invocation."""
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/home/ubuntu/t2t3-compressor-gate')
SCRATCH = ROOT / 'prefix-controls'
HELPER = ROOT / 'make_sound_prefix.py'
HELPER_SHA = '92710ff81699850cd2b9fa93363bdda6d16b796db80f13365bd32e13c0174af2'
NAMES = ['leader55', 'rho', 'lambda3', 'Z55', 'Zrho', 'Z3']
ALIASES = ['v' + str(i) for i in range(len(NAMES))]
NAME_MAP = dict(zip(NAMES, ALIASES))
IDENT = re.compile(r'\b[A-Za-z_]\w*\b')
RING = 'ring R=0,(' + ','.join(NAMES) + '),(M(1,1,1,0,1,2,0,0,1),dp(3));\n'
ROWS = ['leader55^2+rho', 'leader55*rho-lambda3', 'lambda3^2+1',
        'leader55*Z55-1', 'lambda3*Z3-1', 'rho*Zrho-1']


def mapped(row):
    return IDENT.sub(lambda m: NAME_MAP.get(m.group(), m.group()), row)


def poly(expression, names):
    """Canonical small commutative Z polynomial, independent of the helper."""
    n = len(names)
    zero = (0,) * n
    index = {name: i for i, name in enumerate(names)}

    def add(a, b, scale=1):
        out = dict(a)
        for mon, c in b.items():
            out[mon] = out.get(mon, 0) + scale*c
            if out[mon] == 0:
                del out[mon]
        return out

    def mul(a, b):
        out = {}
        for x, c in a.items():
            for y, d in b.items():
                mon = tuple(i+j for i, j in zip(x, y))
                out[mon] = out.get(mon, 0) + c*d
                if out[mon] == 0:
                    del out[mon]
        return out

    def walk(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return {} if node.value == 0 else {zero: node.value}
        if isinstance(node, ast.Name):
            mon = list(zero)
            mon[index[node.id]] = 1
            return {tuple(mon): 1}
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return {m: -c for m, c in walk(node.operand).items()}
        if isinstance(node, ast.BinOp):
            a = walk(node.left)
            if isinstance(node.op, ast.Pow):
                assert isinstance(node.right, ast.Constant) and type(node.right.value) is int
                assert node.right.value >= 0
                out = {zero: 1}
                for _ in range(node.right.value):
                    out = mul(out, a)
                return out
            b = walk(node.right)
            if isinstance(node.op, ast.Add):
                return add(a, b)
            if isinstance(node.op, ast.Sub):
                return add(a, b, -1)
            if isinstance(node.op, ast.Mult):
                return mul(a, b)
        raise AssertionError(ast.dump(node))
    return walk(ast.parse(expression.replace('^', '**'), mode='eval').body)


def write_source(name, original, alias):
    folder = SCRATCH / name
    folder.mkdir()
    (folder / '99-delta2.sing').write_text(RING + 'option(redSB);\nideal I=\n' + original)
    (folder / '99-delta2.ms').write_text(','.join(ALIASES) + '\n1073741827\n' + alias)
    return folder


def invoke(source, output):
    return subprocess.run([sys.executable, str(HELPER), '--case', '99-delta2',
                           '--rows', '2', '--source-dir', str(source),
                           '--output-dir', str(output)], text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)


def main():
    assert hashlib.sha256(HELPER.read_bytes()).hexdigest() == HELPER_SHA
    SCRATCH.mkdir(exist_ok=True)
    assert all(path.resolve() == Path(__file__).resolve() for path in SCRATCH.iterdir())
    # The known complete source has later rows and its production localizers.
    original = ',\n'.join(ROWS) + ';\nquit;\n'
    alias = ',\n'.join(mapped(row) for row in ROWS) + '\n'
    source = write_source('positive-source', original, alias)
    positive_dir = SCRATCH / 'positive-output'
    positive = invoke(source, positive_dir)
    assert positive.returncode == 0, positive.stderr
    meta = json.loads(positive.stdout)
    sing = (positive_dir / '99-delta2-prefix2.sing').read_text().splitlines()
    ms = (positive_dir / '99-delta2-prefix2.ms').read_text().splitlines()
    assert sing[0] + '\n' == RING
    assert sing[1:3] == ['option(redSB);', 'ideal I=']
    assert ms[:2] == [','.join(ALIASES), '1073741827']
    selected = [line.rstrip(',;') for line in sing[3:8]]
    aliased = [line.rstrip(',;') for line in ms[2:7]]
    assert selected[:2] == ROWS[:2]
    assert 'lambda3^2+1' not in selected
    assert len(selected) == len(aliased) == meta['generator_count'] == 5
    assert len(NAMES) == len(set(NAMES)) == len(ALIASES) == len(set(ALIASES))
    source_polys = [poly(row, NAMES) for row in ROWS]
    for qrow, prow in zip(selected, aliased):
        assert poly(qrow, NAMES) == poly(prow, ALIASES)
        assert poly(qrow, NAMES) in source_polys
    assert selected[2:] == ['Z55*leader55-1', 'Z3*lambda3-1', 'Zrho*rho-1']
    # Localizer text need not have the emitter's factor order. Equality is
    # literal equality of polynomials in the copied polynomial ring.
    assert selected[2] != ROWS[3]
    assert poly(selected[2], NAMES) == poly(ROWS[3], NAMES)

    alias_bad = alias.replace(mapped(ROWS[0]), mapped(ROWS[0]) + '+1', 1)
    bad_source = write_source('alias-mismatch-source', original, alias_bad)
    bad = invoke(bad_source, SCRATCH / 'alias-mismatch-output')
    assert bad.returncode != 0 and 'paired row mismatch at index 0' in bad.stderr
    assert not (SCRATCH / 'alias-mismatch-output' / '99-delta2-prefix2.sing').exists()

    short_original = ',\n'.join(ROWS[:2]) + '\n'
    short_alias = ',\n'.join(mapped(row) for row in ROWS[:2]) + '\n'
    short_source = write_source('missing-later-source', short_original, short_alias)
    short = invoke(short_source, SCRATCH / 'missing-later-output')
    assert short.returncode != 0 and 'source does not yet contain a flushed later row' in short.stderr
    assert not (SCRATCH / 'missing-later-output' / '99-delta2-prefix2.sing').exists()

    result = {
        'status': 'PASS', 'worker_scratch': str(SCRATCH), 'helper_sha256': HELPER_SHA,
        'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'positive': {'returncode': positive.returncode, 'copied_ring_bytes_exact': True,
                     'semantic_alias_bijection': True, 'paired_polynomial_images_exact': True,
                     'all_5_selected_polynomials_literal_source_members': True,
                     'selected_later_completion_row_excluded': True,
                     'localizer_factor_reordering_is_exact_polynomial_equality': True},
        'negative_alias_mismatch': {'returncode': bad.returncode,
                                    'rejection': 'paired row mismatch at index 0'},
        'negative_missing_later_row': {'returncode': short.returncode,
                                     'rejection': 'source does not yet contain a flushed later row'},
        'scope': 'Synthetic positive/negative parser controls only; production subset identity audited separately.',
        'solver_jobs_launched': 0,
    }
    (SCRATCH / 'result.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
