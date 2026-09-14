#!/usr/bin/env python3
"""Independent tiny stdlib gate for the frozen exact-Q checker and caller."""
import argparse
import ast
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import importlib
import json
import os
from pathlib import Path
import sys
import tempfile


EXPECTED = {
    'FALLACY-v2.md': 'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5',
    'd125-small-exact-solver-code-prep-astra-20260907.md': '80916c30244742c4562b30d4bd1e2c33e43c8ff8974da22629a5a4154a51e052',
    'd125-small-exact-solver-prep-astra-20260907.md': 'fdcd592734d19bfdc33a206ccf7b21f3b146f73581af0bd3d7be202df81d878c',
    'd125-small-polynomial-lift-gate-fable5-20260906.md': '4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122',
    'driver.py': '7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d',
    'exact.py': 'ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3',
    'run_tests.py': '90f3ae5e24c51a893af232b911d9baafb9b8f60ece1a5349807fa3332b94cd04',
    'test_exact.py': 'e1f0d6d0c0a930d8f1a2dc17709c98fd1bb37669564c1d09b2be6251a87dd588',
}


class GateFailure(Exception):
    pass


def need(condition, label):
    if not condition:
        raise GateFailure(label)


def must_reject(label, action, reasons):
    try:
        action()
    except Exception as exc:
        need(any(piece in str(exc) for piece in reasons), label + ': wrong rejection: ' + repr(exc))
        return label
    raise GateFailure(label + ': accepted corruption')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_frozen(inputs):
    need(inputs.is_dir(), 'inputs directory absent')
    actual_names = sorted(p.name for p in inputs.iterdir() if p.is_file())
    need(actual_names == sorted(EXPECTED), 'frozen input inventory drift')
    pins = {name: sha(inputs/name) for name in EXPECTED}
    need(pins == EXPECTED, 'frozen input hash drift')
    sys.path.insert(0, str(inputs))
    exact = importlib.import_module('exact')
    driver = importlib.import_module('driver')
    need(Path(exact.__file__).resolve() == (inputs/'exact.py').resolve(), 'wrong exact module')
    need(Path(driver.__file__).resolve() == (inputs/'driver.py').resolve(), 'wrong driver module')
    return exact, driver, pins


def stream(E, engine, basis, cofactors=None, variables=('x', 'y'), source='a'*64,
           stated_size=None):
    parse = lambda text: E.polynomial(text, list(variables))
    if stated_size is None:
        stated_size = sum(bool(parse(text)) for text in engine)
    lines = ['JC2CERT 1 '+source+' '+E.ring_id(list(variables)), 'I_SIZE '+str(stated_size)]
    blocks = [('I', engine), ('G', basis)]
    if cofactors is not None:
        blocks.append(('T', cofactors))
    for name, values in blocks:
        lines.append(name+'_BEGIN '+str(len(values)))
        for index, value in enumerate(values, 1):
            lines.append(name+' '+str(index)+' '+value)
        lines.append(name+'_END')
    if cofactors is None:
        lines.append('END NONUNIT')
    else:
        lines.extend(('CHECK 1', 'END UNIT'))
    return ('\n'.join(lines)+'\n').encode('ascii')


def toy_source(E):
    records = [
        {'type': 'header', 'field': 'Q',
         'order': 'global degree reverse lexicographic, displayed variable order',
         'expected_rows': 2, 'expected_variables': 2},
        {'type': 'variable', 'id': 0, 'name': 'x'},
        {'type': 'variable', 'id': 1, 'name': 'y'},
        {'type': 'row', 'label': 'R/0', 'terms': []},
        {'type': 'row', 'label': 'R/1', 'terms': [
            [[['1', '2'], ['0', '1']], [0, 0]],
            [[['-1', '1'], ['0', '1']], [1]],
        ]},
    ]
    prefix = b''.join(E.canonical(record) for record in records)
    footer = {'type': 'footer', 'complete': True, 'prefix_sha256': E.digest(prefix),
              'prefix_records': len(records), 'counts': {'rows': 2}}
    data = prefix + E.canonical(footer)
    singular = ('ring R=0,(x,y),dp;\nideal I=\n// R/0\n0,\n'
                '// R/1\n1/2*x^2-y' + E.ENDING).encode('ascii')
    return data, singular


def algebra_controls(E, rejected):
    V = ['x', 'y', 'z']
    p = lambda text: E.polynomial(text, V)
    need(p('-x^2') == {(0, 0): F(-1)}, 'unary/power precedence')
    need(p('(-x)^2') == {(0, 0): F(1)}, 'parenthesized unary precedence')
    need(p('x/-2^2') == {(0,): F(-1, 4)}, 'division/power precedence')
    need(p('x/(2/3)') == {(0,): F(3, 2)}, 'constant rational division')
    need(p('(x-y)^2') == {(0, 0): F(1), (0, 1): F(-2), (1, 1): F(1)},
         'sparse exact expansion')
    need(E.add(p('x-y'), p('y-x')) == {}, 'exact cancellation')
    need(E.mul(p('x+y'), p('x-y')) == p('x^2-y^2'), 'exact multiplication')
    for bad in ('x/y', '2x', 'x^-1', 'x^2^3', 'x^10001', 'q', 'x;quit', '1/0'):
        rejected.append(must_reject('syntax '+bad, lambda bad=bad: p(bad),
                                    ('syntax', 'denominator', 'exponent', 'unknown', 'trailing')))

    degree_two = ('x^2', 'x*y', 'y^2', 'x*z', 'y*z', 'z^2')
    keys = [E.key(next(iter(p(text))), 3) for text in degree_two]
    need(keys == sorted(keys, reverse=True), 'dp degree-two leading order')
    need(max(p('y^2+x*z'), key=lambda m: E.key(m, 3)) == (1, 1),
         'dp reverse-lex tie breaker')
    need(E.normal_form(p('x^2+x*y+y'), [p('x')], 3) == p('y'), 'normal form')

    rows = [p('0'), p('x^2'), p('x*y'), p('0')]
    need('PROPER' in E.proper_certificate(rows, [p('x')], 3), 'strict superideal certificate')
    need('PROPER' in E.proper_certificate([{}], [], 3), 'zero ideal certificate')
    rejected.append(must_reject('Buchberger corruption',
        lambda: E.proper_certificate([p('x^2'), p('x*y-1')],
                                     [p('x^2'), p('x*y-1')], 3), ('Buchberger',)))
    rejected.append(must_reject('proper missing source row',
        lambda: E.proper_certificate([p('x'), p('y')], [p('x')], 3), ('original equation',)))
    rejected.append(must_reject('proper unit basis',
        lambda: E.proper_certificate([p('x')], [E.ONE], 3), ('unit basis',)))

    original = [p('0'), p('x'), p('0'), p('x'), p('1-x'), p('0')]
    engine = [p('0'), p('x'), p('0'), p('x'), p('1-x')]
    hs = [p('0'), p('1/2'), p('0'), p('1/2'), p('1')]
    verdict, mapping, lifted = E.unit_certificate(original, engine, hs)
    need('UNIT' in verdict and mapping == [0, 1, 0, 1, 4], 'zero/duplicate engine map')
    need(len(lifted) == 6 and lifted[1] == p('1') and lifted[4] == p('1'),
         'padded/aggregated original cofactors')
    rejected.append(must_reject('altered unit cofactor',
        lambda: E.unit_certificate(original, engine,
            [p('0'), p('1/2'), p('0'), p('3/2'), p('1')]), ('not one',)))
    rejected.append(must_reject('foreign engine row',
        lambda: E.engine_map([p('x')], [p('2*x')]), ('not original',)))


def protocol_controls(E, rejected, observations):
    V = ['x', 'y']
    p = lambda text: E.polynomial(text, V)
    valid = stream(E, ['0', 'x', '0', 'x', '1-x'], ['1'],
                   ['0', '1/2', '0', '1/2', '1'])
    engine, basis, cofactors = E.parse_result(valid, b'', V, 'a'*64)
    original = [p(text) for text in ('0', 'x', '0', 'x', '1-x', '0')]
    need(E.unit_certificate(original, engine, cofactors)[0].startswith('EXACT_Q_UNIT'),
         'complete unit protocol')
    corruptions = [
        ('source header', valid.replace(b'a'*64, b'b'*64, 1), ('source/ring',)),
        ('index', valid.replace(b'I 2 ', b'I 1 ', 1), ('index/short',)),
        ('unknown variable', valid.replace(b'G 1 1', b'G 1 rogue'), ('unknown variable',)),
        ('truncated block', valid.replace(b'I_END\n', b'', 1), ('missing I footer',)),
        ('trailing output', valid+b'EXTRA\n', ('terminal stream',)),
        ('cofactor count', valid.replace(b'T_BEGIN 5', b'T_BEGIN 4'), ('index/short', 'footer')),
        ('internal check', valid.replace(b'CHECK 1', b'CHECK 0'), ('internal check',)),
    ]
    for label, changed, reasons in corruptions:
        rejected.append(must_reject(label,
            lambda changed=changed: E.parse_result(changed, b'', V, 'a'*64), reasons))
    rejected.append(must_reject('stderr error',
        lambda: E.parse_result(valid, b'Singular error\n', V, 'a'*64), ('stderr',)))
    rejected.append(must_reject('ring order binding',
        lambda: E.parse_result(valid, b'', ['y', 'x'], 'a'*64), ('source/ring',)))

    whitespace_stderr_accepted = True
    try:
        E.parse_result(valid, b' \n\t', V, 'a'*64)
    except Exception:
        whitespace_stderr_accepted = False
    observations['whitespace_only_stderr_accepted'] = whitespace_stderr_accepted
    need(whitespace_stderr_accepted, 'expected frozen whitespace-stderr behavior changed')
    low_size = stream(E, ['x', '1-x'], ['1'], ['1', '1'], stated_size=0)
    E.parse_result(low_size, b'', V, 'a'*64)
    observations['underreported_I_SIZE_accepted'] = True

    marker_only = stream(E, ['x', '1-x'], ['1'], None)
    m_engine, m_basis, m_h = E.parse_result(marker_only, b'', V, 'a'*64)
    need(m_h is None, 'marker-only path shape')
    rejected.append(must_reject('basis [1] alone',
        lambda: E.proper_certificate([p('x'), p('1-x')], m_basis, 2), ('unit basis',)))
    fake_check = stream(E, ['x', '1-x'], ['1'], ['0', '0'])
    f_engine, unused, f_h = E.parse_result(fake_check, b'', V, 'a'*64)
    rejected.append(must_reject('CHECK 1 alone',
        lambda: E.unit_certificate([p('x'), p('1-x')], f_engine, f_h), ('not one',)))


def source_controls(E, rejected):
    data, singular = toy_source(E)
    variables, rows, labels, prefix = E.read_source(data, singular)
    need(variables == ['x', 'y'] and labels == ['R/0', 'R/1'] and len(rows) == 2,
         'tiny source parse')
    need((prefix + E.ENDING[2:]).encode('ascii') == singular,
         'literal source-prefix preservation')
    changed = [
        ('source coefficient', singular.replace(b'1/2*x^2-y', b'1/3*x^2-y'), ('literal source',)),
        ('source order', singular.replace(b',dp;', b',lp;'), ('literal ring/suffix',)),
        ('source label', singular.replace(b'// R/1', b'// R/X'), ('literal source',)),
        ('source suffix', singular+b'quit;\n', ('literal ring/suffix',)),
        ('source unknown variable', singular.replace(b'1/2*x^2-y', b'1/2*x^2-q'), ('unknown variable',)),
    ]
    for label, bad, reasons in changed:
        rejected.append(must_reject(label, lambda bad=bad: E.read_source(data, bad), reasons))
    first, rest = data.split(b'\n', 1)
    duplicate = first[:-1] + b',"type":"header"}\n' + rest
    rejected.append(must_reject('duplicate JSON key',
        lambda: E.read_source(duplicate, singular), ('duplicate JSON key',)))
    rejected.append(must_reject('production source pin',
        lambda: E.read_source(data, singular, production=True), ('source pin drift',)))


def authority_fixture(D, mode):
    now = 100.0
    observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': D.INSTANCE,
                'cwd': D.CWD, 'boot': 'boot-test', 'now': now}
    pins = {'frozen': 'pins'}
    authority = {'schema': 'jc2.d125-exact-solver-authority/v1', 'root_green': True,
                 'mode': mode, 'job_id': 'job', 'pins': pins, 'caps': D.CAPS,
                 'instance_id': D.INSTANCE, 'cwd': D.CWD, 'boot_id': 'boot-test',
                 'started_utc': '1970-01-01T00:01:30Z',
                 'deadline_utc': '1970-01-01T00:07:20Z'}
    return authority, observed, pins


def caller_controls(E, D, inputs, rejected):
    control, observed, pins = authority_fixture(D, 'engineering_control')
    need(D.authority_check(control, 'control', observed, pins) == 10,
         'engineering authority acceptance')
    rejected.append(must_reject('control cannot decide',
        lambda: D.authority_check(control, 'decision', observed, pins), ('separation',)))
    solver = dict(control)
    solver.update({'mode': 'solver', 'full_stream_gate_accepted': True})
    for key in ('full_stream_gate_sha256', 'engine_index_control_sha256',
                'output_limit_control_sha256', 'descendant_control_sha256'):
        solver[key] = 'c'*64
    need(D.authority_check(solver, 'decision', observed, pins) == 300,
         'decision duration cap')
    need(D.authority_check(solver, 'verify', observed, pins) == 120,
         'verification duration cap')
    for label, changed in (
        ('root GREEN', {**solver, 'root_green': False}),
        ('solver mode', {**solver, 'mode': 'engineering_control'}),
        ('accepted stream gate', {**solver, 'full_stream_gate_accepted': False}),
        ('accepted control pin', {**solver, 'descendant_control_sha256': ''}),
        ('boot binding', solver),
        ('instance binding', solver),
        ('cwd binding', solver),
    ):
        changed_observed = dict(observed)
        if label == 'boot binding':
            changed_observed['boot'] = 'other'
        elif label == 'instance binding':
            changed_observed['instance'] = 'i-other'
        elif label == 'cwd binding':
            changed_observed['cwd'] = '/tmp'
        rejected.append(must_reject(label,
            lambda changed=changed, changed_observed=changed_observed:
                D.authority_check(changed, 'decision', changed_observed, pins),
            ('GREEN', 'separation', 'stream gate', 'accepted control', 'registered Linux EC2', 'cwd/boot')))
    too_long = {**solver, 'deadline_utc': '1970-01-01T00:10:00Z'}
    rejected.append(must_reject('450-second deadline',
        lambda: D.authority_check(too_long, 'decision', observed, pins), ('deadline',)))

    calls = []
    original_setrlimit = D.resource.setrlimit
    D.resource.setrlimit = lambda which, value: calls.append((which, value))
    try:
        D.limits('decision')
    finally:
        D.resource.setrlimit = original_setrlimit
    need(calls == [
        (D.resource.RLIMIT_AS, (16*1024**3,)*2),
        (D.resource.RLIMIT_FSIZE, (64*1024**2,)*2),
        (D.resource.RLIMIT_CORE, (0, 0)),
    ], 'decision resource limits')

    production = D.footer(['x', 'y'], 'a'*64)
    need(production.count('slimgb(I)') == 1, 'one slimgb')
    need(production.count('lift(I,ideal(1))') == 1, 'one conditional lift')
    need(production.index('G_END') < production.index('if(hasunit){') < production.index('lift(I'),
         'basis completion before conditional lift')
    for forbidden in ('system(', 'write(', 'link ', 'LIB ', 'execute(', 'read(', 'std('):
        need(forbidden not in production, 'forbidden Singular command '+forbidden)
    control_text = D.control_input()
    need('slimgb' not in control_text and 'ideal I=0,x,0,x,1-x,0;' in control_text,
         'fixed isolated engineering control')

    exact_tree = ast.parse((inputs/'exact.py').read_text())
    driver_tree = ast.parse((inputs/'driver.py').read_text())
    need(not any(isinstance(node, ast.Assert) for tree in (exact_tree, driver_tree)
                 for node in ast.walk(tree)), 'removable assert in enforcement code')

    captured = {}
    original_context = D.context
    original_run = D.subprocess.run
    D.context = lambda authority_path, phase: ({}, 'd'*64, 7)
    class Result:
        returncode = 0
    def fake_run(command, check=False):
        captured['command'] = command
        captured['check'] = check
        return Result()
    D.subprocess.run = fake_run
    old_cwd = Path.cwd()
    try:
        with tempfile.TemporaryDirectory(dir=old_cwd) as tmp:
            os.chdir(tmp)
            need(D.launch('authority.json', 'control') == 0, 'launch return status')
            command = captured['command']
            need(command[:4] == [sys.executable, '-I', '-B', str(Path(D.CWD)/'run_capped.py')],
                 'CAPRUN executable prefix')
            expected_flags = ['--wall-seconds', '7', '--cpu-seconds', '7', '--rss-bytes',
                              str(512*1024**2), '--cwd', D.CWD, '--stdout-file', 'control.stdout',
                              '--stderr-file', 'control.stderr', '--telemetry-file',
                              'control.telemetry.json', '--']
            need(command[4:4+len(expected_flags)] == expected_flags, 'CAPRUN bounded argv')
            child = command[4+len(expected_flags):]
            need(child[:3] == [sys.executable, '-I', '-B'] and child[4:7] ==
                 ['payload', '--phase', 'control'] and captured['check'] is False,
                 'exact isolated child argv')
            rejected.append(must_reject('exclusive phase artifacts',
                lambda: D.launch('authority.json', 'control'), ('fresh exclusive',)))
    finally:
        os.chdir(old_cwd)
        D.context = original_context
        D.subprocess.run = original_run


def injected_failure(E, D, name):
    V = ['x', 'y']
    p = lambda text: E.polynomial(text, V)
    if name == 'cofactor':
        E.unit_certificate([p('x'), p('1-x')], [p('x'), p('1-x')], [p('2'), p('1')])
    elif name == 'buchberger':
        E.proper_certificate([p('x^2'), p('x*y-1')], [p('x^2'), p('x*y-1')], 2)
    elif name == 'protocol':
        bad = stream(E, ['x', '1-x'], ['1'], ['1', '1']).replace(b'I 2 ', b'I 1 ', 1)
        E.parse_result(bad, b'', V, 'a'*64)
    elif name == 'source':
        data, singular = toy_source(E)
        E.read_source(data, singular+b'quit;\n')
    elif name == 'authority':
        authority, observed, pins = authority_fixture(D, 'engineering_control')
        D.authority_check(authority, 'decision', observed, pins)
    else:
        need(name == 'none', 'unknown injected corruption')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', required=True)
    parser.add_argument('--inject', choices=('none', 'cofactor', 'buchberger', 'protocol',
                                             'source', 'authority'), default='none')
    args = parser.parse_args()
    inputs = Path(args.inputs).resolve()
    E, D, pins = load_frozen(inputs)
    rejected = []
    observations = {}
    algebra_controls(E, rejected)
    protocol_controls(E, rejected, observations)
    source_controls(E, rejected)
    caller_controls(E, D, inputs, rejected)
    if args.inject != 'none':
        injected_failure(E, D, args.inject)
        raise GateFailure('injected corruption unexpectedly accepted: '+args.inject)
    report = {'status': 'PASS_WITH_PROTOCOL_OBSERVATIONS',
              'caught_rejections': len(rejected), 'pins': pins, 'observations': observations,
              'python_optimized': not __debug__, 'utc': datetime.now(timezone.utc).isoformat()}
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(type(exc).__name__+': '+str(exc), file=sys.stderr)
        raise SystemExit(1)
