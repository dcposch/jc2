#!/usr/bin/env python3
"""Independent integer modular evaluation; no CAS is imported or called."""
import hashlib
import itertools
import json
from pathlib import Path
import re
import time

ROOT = Path('/home/ubuntu/jc2')
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'box/k16rank-20260903/terminal_t8_exact_none.out'
SYSTEMS = {
    32003: (11288, ROOT / 'box/k16t8-20260905/msolve_t8_affinew_p32003_b0.ms'),
    32027: (23825, ROOT / 'box/k16-t8-gate-20260905/affinew_p32027.ms'),
}
TOKEN = re.compile(r'\d+|[A-Za-z][A-Za-z_0-9]*|[()+*/^\-]')
PREC = {'+': 1, '-': 1, '*': 2, '/': 2, 'u+': 3, 'u-': 3, '^': 4}
POINTS = [
    (2, 3, 5, 7, 11, 13),  # calibration only: determines fixed signed minor index map
    (17, 19, 23, 29, 31, 37),
    (41, 43, 47, 53, 59, 61),
    (67, 71, 73, 79, 83, 89),
    (97, 101, 103, 107, 109, 113),
    (127, 131, 137, 139, 149, 151),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse(text):
    """Strict shunting-yard parser, integer literals and + - * / ^ only."""
    tokens = TOKEN.findall(text)
    assert ''.join(tokens) == re.sub(r'\s+', '', text)
    out, ops, operand_expected = [], [], True
    for tok in tokens:
        if tok.isdigit():
            assert operand_expected
            out.append(int(tok))
            operand_expected = False
        elif tok[0].isalpha():
            assert operand_expected
            out.append(tok)
            operand_expected = False
        elif tok == '(':
            assert operand_expected
            ops.append(tok)
        elif tok == ')':
            assert not operand_expected
            while ops[-1] != '(':
                out.append(ops.pop())
            ops.pop()
            operand_expected = False
        elif operand_expected:
            assert tok in ['+', '-']
            ops.append('u' + tok)
        else:
            while ops and ops[-1] != '(' and (PREC[ops[-1]] > PREC[tok] or
                                               (PREC[ops[-1]] == PREC[tok] and tok != '^')):
                out.append(ops.pop())
            ops.append(tok)
            operand_expected = True
    assert not operand_expected
    while ops:
        assert ops[-1] != '('
        out.append(ops.pop())
    return out


def ev(program, values, p):
    stack = []
    for tok in program:
        if isinstance(tok, int):
            stack.append(tok % p)
        elif tok in values:
            stack.append(values[tok] % p)
        elif tok == 'u+':
            pass
        elif tok == 'u-':
            stack[-1] = -stack[-1] % p
        else:
            b, a = stack.pop(), stack.pop()
            if tok == '+':
                v = a + b
            elif tok == '-':
                v = a - b
            elif tok == '*':
                v = a * b
            elif tok == '/':
                assert b != 0, 'nonintegral rational coefficient'
                v = a * pow(b, -1, p)
            elif tok == '^':
                assert b <= 100, 'unexpected exponent'
                v = pow(a, b, p)
            else:
                raise ValueError(tok)
            stack.append(v % p)
    assert len(stack) == 1
    return stack[0]


for expr, expected in [('2+3*4', 14), ('(2+3)*4', 20), ('2^3^2', 512),
                       ('-2^2', -4), ('(-2)^2', 4), ('1/2+1/3', 5 * pow(6, -1, 32003)),
                       ('2*-3+5', -1), ('(1/2*yy-3/4)*q2_0^2', 21)]:
    vals = {'yy': 12, 'q2_0': 2}
    assert ev(parse(expr), vals, 32003) == expected % 32003

started = time.time()
raw = SOURCE.read_text()
assert 'RECURRENCE_PASS' in raw and 'DRIVER_DONE' in raw
source_lines = raw.splitlines()
rows = {}
for i, line in enumerate(source_lines):
    m = re.fullmatch(r'TROW band=(\d+)', line)
    if m:
        rows[int(m.group(1))] = source_lines[i + 1].strip()
assert set(rows) == set(range(16))
programs = [parse(rows[k]) for k in range(15, 7, -1)]
pairs = list(itertools.combinations(range(1, 8), 2))
summary = {'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': sha(SOURCE),
           'script_sha256': sha(__file__), 'calibration_point': POINTS[0],
           'holdout_points': POINTS[1:], 'matrix_rows': [f'(C{r},B{r})' for r in range(1, 8)],
           'checks': []}
fixed_map = None
for p, (yy, path) in SYSTEMS.items():
    assert (3468 * yy * yy - 1836 * yy + 234) % p == 0
    lines = path.read_text().splitlines()
    assert lines[:2] == ['q2,q3,q4,q5,q6,q7', str(p)]
    polynomials = [line.rstrip(',') for line in lines[2:] if line.strip()]
    assert len(polynomials) == 28
    assert set(TOKEN.findall(' '.join(re.findall(r'[A-Za-z][A-Za-z_0-9]*', '\n'.join(polynomials))))) == {
        'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
    images = [parse(poly) for poly in polynomials]
    for point_number, point in enumerate(POINTS):
        values = {'b4': 1, 'yy': yy, **{f'q{j}_0': point[j - 2] for j in range(2, 8)}}
        abc = []
        for program in programs:
            c = ev(program, {**values, 'b3': 0}, p)
            plus = ev(program, {**values, 'b3': 1}, p)
            minus = ev(program, {**values, 'b3': -1}, p)
            a = (plus + minus - 2 * c) * pow(2, -1, p) % p
            b = (plus - minus) * pow(2, -1, p) % p
            # Extra b3=2 detects an incorrectly assumed quadratic split.
            assert ev(program, {**values, 'b3': 2}, p) == (4 * a + 2 * b + c) % p
            abc.append((a, b, c))
        a0, b0, c0 = abc[0]
        assert a0
        bc = [(a0 * b - a * b0, a0 * c - a * c0) for a, b, c in abc[1:]]
        bc = [(b % p, c % p) for b, c in bc]
        minors = [(bc[r-1][1] * bc[s-1][0] - bc[s-1][1] * bc[r-1][0]) % p for r, s in pairs]
        ws = [(a0*c*c - b0*b*c + c0*b*b) % p for b, c in bc]
        actual = [ev(program, {f'q{j}': point[j - 2] for j in range(2, 8)}, p) for program in images]
        if fixed_map is None:
            fixed_map = []
            for observed in actual[:21]:
                candidates = [(i, sign) for i, value in enumerate(minors) for sign in [1, -1]
                              if observed == sign * value % p]
                assert len(candidates) == 1, candidates
                fixed_map.append(candidates[0])
            assert len(set(i for i, _ in fixed_map)) == 21
            summary['minor_order'] = [
                {'image_index': k+1, 'row_pair': pairs[i], 'sign': sign,
                 'definition': f'{sign}*(C{pairs[i][0]}*B{pairs[i][1]}-C{pairs[i][1]}*B{pairs[i][0]})'}
                for k, (i, sign) in enumerate(fixed_map)]
        expected = [sign * minors[i] % p for i, sign in fixed_map] + ws
        assert actual == expected, {'p': p, 'point': point,
                                    'mismatches': [i+1 for i in range(28) if actual[i] != expected[i]]}
        item = {'prime': p, 'yy': yy, 'point_number': point_number,
                'role': 'calibration' if point_number == 0 and p == 32003 else 'validation',
                'q2_through_q7': point, 'a0': a0, 'all_28_images_match': True,
                'exact_expected_and_observed_values': actual}
        summary['checks'].append(item)
        print(json.dumps(item), flush=True)
    summary.setdefault('systems', []).append({'path': str(path.relative_to(ROOT)), 'sha256': sha(path)})
summary['wall_seconds'] = round(time.time() - started, 3)
summary['verdict'] = 'PASS: fixed indexed signed minor map and W1..W7 match at every validation sample'
(OUT / 't8_images.json').write_text(json.dumps(summary, indent=2) + '\n')
print(summary['verdict'], 'wall_seconds', summary['wall_seconds'], flush=True)
