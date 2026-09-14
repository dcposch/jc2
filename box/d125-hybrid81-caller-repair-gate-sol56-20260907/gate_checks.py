#!/usr/bin/env python3
"""Independent two-delta controls. Reads only the charged frozen input bundle."""
from contextlib import ExitStack, contextmanager, redirect_stdout
from datetime import datetime, timezone
import ast
import difflib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import resource
import signal
import subprocess
import sys
import tempfile
import time
import types
from unittest.mock import patch


HERE = Path(__file__).resolve().parent
FROZEN = Path('/tmp/jc2-lane.q9z0fq/inputs')
DRIVER_SHA = 'ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a'
OLD_DRIVER_SHA = 'faf7a1e08fa7fafac09160b57587eb325ef4542da30a7defbf5165bc329569d9'
PATCH_SHA = '5daab0735fd9fceb83acf6886a4364c3f533c7fb67dc88baea7885526a7ce2df'
FIXTURE_SHA = 'd00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf'
EXPECTED_FROZEN = {
    'alarm-semantics.md': 'a11183911c23292165732b7db2afb17919fb22505db55f8aea238616f0d761eb',
    'd125-hybrid81-caller-repair-astra-20260907.md': 'feb918be39485ad3bd2377397122787ea149c402333d9f477367e577bfeff256',
    'd125-hybrid81-solver-gate-sol56-20260907.md': 'b4198c3689e0d713eca6a1a7dfe95854f88bb48f45217b737adb29e03c4fcc46',
    'driver-two-bugs.patch': PATCH_SHA,
    'driver.py': DRIVER_SHA,
    'exact.py': '7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
    'hybrid.py': 'c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3',
    'test_caller.py': '53471683826c4fbc2e35440a08f9b062791c0eee2e8facb721e68bc3c2fad1f1',
    'timed_probe.py': '9c7508c39d3e56690e4398a0247adb48983fbe94165ad27ebbba3c30a7f8b635',
    'tiny-engine-fixture.jsonl': FIXTURE_SHA,
}
PATCH_EOF_CONTEXT_COMPLETION_LINES = 0


def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def replace_once(text, old, new, label):
    need(text.count(old) == 1, 'reverse-delta cardinality: '+label)
    return text.replace(old, new, 1)


def reconstruct_old(new):
    text = new
    text = replace_once(text, 'import resource\nimport signal\nimport subprocess\n',
                        'import resource\nimport subprocess\n', 'signal import')
    text = replace_once(text, '''def arm_deadline(a, duration):
    """One wall timer covers source parsing and survives execve; never reset."""
    end = datetime.fromisoformat(a['deadline_utc'].replace('Z', '+00:00')).timestamp()
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_UNBLOCK, {signal.SIGALRM})
    remaining = min(duration, end-time.time())
    E.need(remaining > 0, 'absolute payload deadline expired')
    signal.setitimer(signal.ITIMER_REAL, remaining)


''', '', 'arm_deadline definition')
    text = replace_once(text,
                        '    a, authority_sha, duration = context(authority_path, phase)\n'
                        '    arm_deadline(a, duration)\n',
                        '    a, authority_sha, duration = context(authority_path, phase)\n',
                        'payload arm call')
    text = replace_once(text, '''            E.need(receipt['authority_sha256'] == authority_sha and receipt['runner_rc'] == 0
                   and receipt.get('phase') == 'decision'
                   and receipt.get('source_pins_after') == {'jsonl': H.CONSTRUCTION_SHA},
                   'decision custody/return/source status')
''', '''            E.need(receipt['authority_sha256'] == authority_sha and receipt['runner_rc'] == 0,
                   'decision custody/return status')
''', 'verify receipt binding')
    text = replace_once(text, '''    after = {} if phase == 'control' else {'jsonl': file_sha(SOURCE)}
    if after:
        E.need(after == {'jsonl': H.CONSTRUCTION_SHA}, 'post-run frozen source drift')
    write_new(phase+'.result.json', E.canonical({'authority_sha256': authority_sha,
              'runner_rc': result.returncode, 'outputs': outputs, 'artifacts': artifacts,
              'source_pins_after': after, 'phase': phase}))
    return result.returncode
''', '''    after = {} if phase == 'control' else {'jsonl': file_sha(SOURCE)}
    write_new(phase+'.result.json', E.canonical({'authority_sha256': authority_sha,
              'runner_rc': result.returncode, 'outputs': outputs, 'artifacts': artifacts,
              'source_pins_after': after, 'phase': phase}))
    if after:
        E.need(after == {'jsonl': H.CONSTRUCTION_SHA}, 'post-run frozen source drift')
    return result.returncode
''', 'posthash publication order')
    return text


def apply_unified(old, patch_text):
    """Apply the supplied unified hunks in memory, validating every old/context line."""
    source = old.splitlines(keepends=True)
    patch_lines = patch_text.splitlines(keepends=True)
    output = []
    cursor = 0
    index = 2
    while index < len(patch_lines):
        header = re.fullmatch(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@.*\n?',
                              patch_lines[index])
        need(header is not None, 'bad unified hunk header')
        old_start = int(header.group(1))-1
        expected_old = int(header.group(2) or 1)
        expected_new = int(header.group(4) or 1)
        need(old_start >= cursor, 'overlapping unified hunks')
        output.extend(source[cursor:old_start])
        cursor = old_start
        seen_old = seen_new = 0
        index += 1
        while index < len(patch_lines) and not patch_lines[index].startswith('@@ '):
            line = patch_lines[index]
            need(line and line[0] in ' +-', 'unsupported unified patch marker')
            body = line[1:]
            if line[0] in ' -':
                need(cursor < len(source) and source[cursor] == body,
                     'unified patch old/context mismatch')
                cursor += 1
                seen_old += 1
            if line[0] in ' +':
                output.append(body)
                seen_new += 1
            index += 1
        if (seen_old, seen_new) != (expected_old, expected_new):
            global PATCH_EOF_CONTEXT_COMPLETION_LINES
            missing_old = expected_old-seen_old
            missing_new = expected_new-seen_new
            need(index == len(patch_lines) and missing_old == missing_new
                 and missing_old > 0 and source[cursor:cursor+missing_old] == ['\n']*missing_old,
                 'unified hunk count mismatch')
            output.extend(source[cursor:cursor+missing_old])
            cursor += missing_old
            seen_old += missing_old
            seen_new += missing_new
            PATCH_EOF_CONTEXT_COMPLETION_LINES = missing_old
        need((seen_old, seen_new) == (expected_old, expected_new),
             'unified hunk completion mismatch')
    output.extend(source[cursor:])
    return ''.join(output)


def module_from_source(name, source):
    module = types.ModuleType(name)
    module.__file__ = str(FROZEN/'driver.py')
    module.__package__ = ''
    sys.modules[name] = module
    exec(compile(source, module.__file__, 'exec'), module.__dict__)
    return module


need(FROZEN.is_dir(), 'frozen directory absent')
sys.path.insert(0, str(FROZEN))
import exact as E
import hybrid as H

NEW_TEXT = (FROZEN/'driver.py').read_text(encoding='utf-8')
OLD_TEXT = reconstruct_old(NEW_TEXT)
D = module_from_source('gate_repaired_driver', NEW_TEXT)
O = module_from_source('gate_old_driver', OLD_TEXT)
FIXTURE = (FROZEN/'tiny-engine-fixture.jsonl').read_bytes()


@contextmanager
def scratch():
    previous = Path.cwd()
    with tempfile.TemporaryDirectory(prefix='gate-tiny-', dir=HERE) as name:
        os.chdir(name)
        try:
            yield Path(name)
        finally:
            os.chdir(previous)


def save_json(name, value):
    Path(name).write_bytes(E.canonical(value))


def certificate_stream():
    variables = ['x', 'y', 'k', 'z']
    rows = ['0', 'x/2', '0', 'x/2', '1-x', '0', 'k*z-1']
    cofactors = ['0', '1', '0', '1', '1', '0', '0']
    lines = ['JC2CERT 1 '+FIXTURE_SHA+' '+E.ring_id(variables), 'I_SIZE 4',
             'I_BEGIN 7']
    lines.extend('I '+str(i)+' '+row for i, row in enumerate(rows, 1))
    lines.extend(['I_END', 'G_BEGIN 1', 'G 1 1', 'G_END', 'T_BEGIN 7'])
    lines.extend('T '+str(i)+' '+row for i, row in enumerate(cofactors, 1))
    lines.extend(['T_END', 'CHECK 1', 'END UNIT'])
    return ('\n'.join(lines)+'\n').encode('ascii')


OUTCOMES = []
PROBES = []
DERIVED_CONTROL = {}


def mark(name):
    OUTCOMES.append(name)


def check_frozen_and_delta():
    actual = {name: sha((FROZEN/name).read_bytes()) for name in EXPECTED_FROZEN}
    need(actual == EXPECTED_FROZEN, 'frozen pin mismatch')
    mark('all_10_frozen_pins_match')
    need(sha(NEW_TEXT.encode()) == DRIVER_SHA, 'new driver hash')
    mark('new_driver_hash')
    need(sha(OLD_TEXT.encode()) == OLD_DRIVER_SHA, 'reconstructed old driver hash')
    mark('reconstructed_old_driver_hash')
    supplied = (FROZEN/'driver-two-bugs.patch').read_text(encoding='utf-8')
    need(apply_unified(OLD_TEXT, supplied) == NEW_TEXT,
         'supplied patch does not produce exact new driver')
    need(PATCH_EOF_CONTEXT_COMPLETION_LINES == 2,
         'unexpected frozen patch EOF context condition')
    generated = ''.join(difflib.unified_diff(
        OLD_TEXT.splitlines(keepends=True), NEW_TEXT.splitlines(keepends=True),
        fromfile='old/driver.py', tofile='new/driver.py', n=3))

    def edits(diff):
        return [line for line in diff.splitlines(keepends=True)
                if line[:1] in ('+', '-') and not line.startswith(('+++', '---'))]

    need(edits(generated) == edits(supplied), 'supplied changed-line payload mismatch')
    mark('whole_delta_matches_patch_edits_with_two_blank_eof_context_lines_restored')
    for label, source in (('new_driver', NEW_TEXT), ('old_driver', OLD_TEXT),
                          ('exact', (FROZEN/'exact.py').read_text()),
                          ('hybrid', (FROZEN/'hybrid.py').read_text()),
                          ('gate_checks', Path(__file__).read_text())):
        need(not any(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(source))),
             label+' contains removable assert')
    mark('implementation_and_gate_have_no_ast_assert')
    new_tree = ast.parse(NEW_TEXT)
    payload = next(node for node in new_tree.body if isinstance(node, ast.FunctionDef) and node.name == 'payload')
    need(len(payload.body) >= 2 and isinstance(payload.body[1], ast.Expr)
         and isinstance(payload.body[1].value, ast.Call)
         and isinstance(payload.body[1].value.func, ast.Name)
         and payload.body[1].value.func.id == 'arm_deadline', 'arm is not immediate after context')
    calls = [node for node in ast.walk(new_tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute)
             and isinstance(node.func.value, ast.Name)
             and node.func.value.id == 'signal' and node.func.attr == 'setitimer']
    need(len(calls) == 1, 'ITIMER_REAL timer call count')
    mark('arm_immediate_and_one_setitimer')


def expected_value_error(call, fragment):
    try:
        call()
    except ValueError as exc:
        need(fragment in str(exc), 'wrong rejection: '+str(exc))
        return
    raise RuntimeError('expected ValueError: '+fragment)


def launch_mismatch(module):
    with scratch() as work:
        source = work/'source.jsonl'
        source.write_bytes(b'ACTUAL_DIFFERENT_TINY_BYTES\n')
        with patch.object(module, 'context', return_value=({}, 'a'*64, 10)), \
             patch.object(module, 'SOURCE', source), \
             patch.object(module.subprocess, 'run',
                          return_value=subprocess.CompletedProcess([], 0)):
            expected_value_error(lambda: module.launch('MOCK_ONLY', 'decision'),
                                 'post-run frozen source drift')
        return Path('decision.result.json').exists()


def check_publication_order():
    need(launch_mismatch(O) is True, 'old control did not publish rejected receipt')
    mark('old_mismatch_publishes_result')
    need(launch_mismatch(D) is False, 'repaired driver published rejected receipt')
    mark('new_mismatch_has_no_result')
    with scratch() as work:
        source = work/'source.jsonl'
        source.write_bytes(FIXTURE)
        with patch.object(D, 'context', return_value=({}, 'a'*64, 10)), \
             patch.object(D, 'SOURCE', source), \
             patch.object(H, 'CONSTRUCTION_SHA', FIXTURE_SHA), \
             patch.object(D.subprocess, 'run',
                          return_value=subprocess.CompletedProcess([], 0)):
            need(D.launch('MOCK_ONLY', 'decision') == 0, 'matching launch return')
        receipt = E.strict_json(Path('decision.result.json').read_bytes())
        need(receipt.get('phase') == 'decision', 'matching receipt phase')
        need(receipt.get('source_pins_after') == {'jsonl': FIXTURE_SHA},
             'matching receipt exact post-pin')
    mark('new_match_publishes_exact_phase_and_postpin')


def verify_case(module, mutate, should_accept):
    with scratch() as work, ExitStack() as stack:
        source = work/'tiny.jsonl'
        source.write_bytes(FIXTURE)
        stack.enter_context(patch.object(module, 'context', return_value=({}, 'a'*64, 10)))
        stack.enter_context(patch.object(module, 'arm_deadline', lambda a, d: None, create=True))
        stack.enter_context(patch.object(module, 'SOURCE', source))
        stack.enter_context(patch.object(module, 'limits', lambda phase: None))
        stack.enter_context(patch.object(module, 'observed_host', lambda: {'boot': 'toy'}))
        stack.enter_context(patch.object(module.os, 'getpgrp', return_value=os.getpid()))
        original_read = Path.read_bytes

        def read(path):
            if str(path) == f'/proc/{os.getppid()}/cmdline':
                return (module.CWD+'/run_capped.py').encode()+b'\0'
            return original_read(path)

        stack.enter_context(patch.object(Path, 'read_bytes', read))
        actual_hybrid = H.read_hybrid
        stack.enter_context(patch.object(H, 'read_hybrid',
                                         lambda data, production: actual_hybrid(data, False)))
        stack.enter_context(patch.object(H, 'CONSTRUCTION_SHA', FIXTURE_SHA))
        identity = {'pid': 42, 'pgid': 42, 'authority_sha256': 'a'*64,
                    'host': {'boot': 'toy'}, 'start_ticks': '7'}
        telemetry = {'schema': 'CAPRUN/v1', 'error': None, 'status': 'NORMAL_EXIT',
                     'child_returncode': 0, 'pid': 42, 'pgid': 42,
                     'cwd': module.CWD, 'start_identity': 'boot=toy;start_ticks=7'}
        save_json('decision.identity.json', identity)
        save_json('decision.telemetry.json', telemetry)
        Path('decision.stdout').write_bytes(certificate_stream())
        Path('decision.stderr').write_bytes(b'')
        receipt = {
            'phase': 'decision',
            'source_pins_after': {'jsonl': FIXTURE_SHA},
            'authority_sha256': 'a'*64,
            'runner_rc': 0,
            'artifacts': {'identity.json': module.file_sha('decision.identity.json')},
            'outputs': {name: module.file_sha('decision.'+name)
                        for name in ('stdout', 'stderr', 'telemetry.json')},
        }
        mutate(receipt)
        save_json('decision.result.json', receipt)
        output = io.StringIO()
        if should_accept:
            with redirect_stdout(output):
                module.payload('MOCK_ONLY', 'verify')
            parsed = json.loads(output.getvalue())
            need(parsed['verdict'] == 'EXACT_Q_UNIT_COFACTOR_CERTIFICATE',
                 'accepted toy certificate verdict')
        else:
            expected_value_error(
                lambda: module.payload('MOCK_ONLY', 'verify'),
                'decision custody/return/source status')


def check_receipt_binding():
    mutations = [
        ('phase_control', lambda r: r.update(phase='control')),
        ('phase_verify', lambda r: r.update(phase='verify')),
        ('phase_missing', lambda r: r.pop('phase')),
        ('postpin_wrong', lambda r: r.update(source_pins_after={'jsonl': 'b'*64})),
        ('postpin_empty', lambda r: r.update(source_pins_after={})),
        ('postpin_extra', lambda r: r.update(source_pins_after={'jsonl': FIXTURE_SHA, 'extra': 'x'})),
        ('postpin_missing', lambda r: r.pop('source_pins_after')),
    ]
    for name, mutation in mutations:
        verify_case(O, mutation, True)
        mark('old_accepts_'+name)
        verify_case(D, mutation, False)
        mark('new_rejects_'+name)
    verify_case(D, lambda receipt: None, True)
    mark('new_accepts_exact_decision_phase_and_postpin')


def check_arm_unit_path():
    deadline = datetime.fromtimestamp(100, timezone.utc).isoformat()
    with patch.object(D.time, 'time', return_value=98.75), \
         patch.object(D.signal, 'signal') as disposition, \
         patch.object(D.signal, 'pthread_sigmask') as mask, \
         patch.object(D.signal, 'setitimer') as timer:
        D.arm_deadline({'deadline_utc': deadline}, 5)
        need(disposition.call_args.args == (signal.SIGALRM, signal.SIG_DFL),
             'SIGALRM disposition')
        need(mask.call_args.args == (signal.SIG_UNBLOCK, {signal.SIGALRM}),
             'SIGALRM unblock')
        need(timer.call_count == 1 and timer.call_args.args[0] == signal.ITIMER_REAL
             and abs(timer.call_args.args[1]-1.25) < 1e-12, 'fresh absolute minimum')
    mark('arm_sets_default_unblocks_and_uses_fresh_absolute_minimum')
    with patch.object(D.time, 'time', return_value=98.75), \
         patch.object(D.signal, 'signal'), \
         patch.object(D.signal, 'pthread_sigmask'), \
         patch.object(D.signal, 'setitimer') as timer:
        D.arm_deadline({'deadline_utc': deadline}, .5)
        need(timer.call_count == 1 and abs(timer.call_args.args[1]-.5) < 1e-12,
             'phase duration minimum')
    mark('arm_preserves_smaller_phase_duration')
    with patch.object(D.time, 'time', return_value=100), \
         patch.object(D.signal, 'signal'), \
         patch.object(D.signal, 'pthread_sigmask'), \
         patch.object(D.signal, 'setitimer') as timer:
        expected_value_error(lambda: D.arm_deadline({'deadline_utc': deadline}, 5),
                             'absolute payload deadline expired')
        need(timer.call_count == 0, 'zero accidentally disarmed timer')
    mark('expired_arm_rejects_without_zero_setitimer')


def probe_main(version, mode):
    module = O if version == 'old' else D
    need(version in ('old', 'new') and mode in ('parse', 'exec'), 'probe arguments')
    started = time.time()
    deadline = started+.75
    authority = {'deadline_utc': datetime.fromtimestamp(deadline, timezone.utc).isoformat()}
    actual_read = Path.read_bytes
    actual_hybrid = H.read_hybrid
    actual_exec = os.execve

    def context(unused, phase):
        time.sleep(.20)
        return authority, 'a'*64, 10

    def read(path):
        if str(path) == f'/proc/{os.getppid()}/cmdline':
            return (module.CWD+'/run_capped.py').encode()+b'\0'
        return actual_read(path)

    def tiny(data, production):
        need(production is True, 'payload did not request production parse')
        print(json.dumps({'marker': 'PARSE_ENTER', 'utc': time.time(),
                          'timer': signal.getitimer(signal.ITIMER_REAL)}), flush=True)
        time.sleep(.90 if mode == 'parse' else .10)
        print(json.dumps({'marker': 'PARSE_DONE', 'utc': time.time()}), flush=True)
        return actual_hybrid(data, production=False)

    def exec_python(path, args, env):
        need(path == '/usr/bin/Singular', 'unexpected nominal exec target')
        code = ('import json,os,signal,time; '
                'mask=signal.pthread_sigmask(signal.SIG_BLOCK,set()); '
                'print(json.dumps({"marker":"EXEC_ALIVE","pid":os.getpid(),'
                '"utc":time.time(),"timer":signal.getitimer(signal.ITIMER_REAL),'
                '"default":signal.getsignal(signal.SIGALRM)==signal.SIG_DFL,'
                '"blocked":signal.SIGALRM in mask}),flush=True); '
                'time.sleep(.80); print("SURVIVED",flush=True)')
        flags = ['-O'] if sys.flags.optimize else []
        actual_exec(sys.executable, [sys.executable, '-I', '-B', *flags, '-c', code], env)

    print(json.dumps({'marker': 'START', 'pid': os.getpid(), 'pgid': os.getpgrp(),
                      'utc': started, 'deadline': deadline, 'version': version,
                      'case': mode}), flush=True)
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGALRM})
    with patch.object(module, 'context', context), \
         patch.object(module, 'SOURCE', FROZEN/'tiny-engine-fixture.jsonl'), \
         patch.object(module, 'limits', lambda phase: None), \
         patch.object(module, 'observed_host', lambda: {'boot': 'MOCK_ONLY'}), \
         patch.object(Path, 'read_bytes', read), \
         patch.object(H, 'read_hybrid', tiny), \
         patch.object(H, 'CONSTRUCTION_SHA', FIXTURE_SHA), \
         patch.object(module.os, 'execve', exec_python):
        module.payload('NO_AUTHORITY_MOCK', 'decision')
    raise RuntimeError('payload exec unexpectedly returned')


def check_real_timer_paths():
    flags = ['-O'] if sys.flags.optimize else []
    for mode in ('parse', 'exec'):
        for version in ('old', 'new'):
            with scratch() as work:
                command = [sys.executable, '-B', *flags, str(Path(__file__).resolve()),
                           '--probe', version, mode]
                result = subprocess.run(command, cwd=work, capture_output=True, text=True,
                                        start_new_session=True, timeout=4)
                finished = time.time()
            lines = result.stdout.splitlines()
            events = [json.loads(line) for line in lines if line.startswith('{')]
            need(events and events[0].get('marker') == 'START', 'probe missing start')
            start = events[0]
            need(start['pid'] == start['pgid'], 'probe not session/process-group leader')
            need(not Path('/proc', str(start['pid'])).exists(), 'probe child not reaped')
            survived = 'SURVIVED' in lines
            lag = finished-start['deadline']
            record = {'mode': mode, 'version': version, 'returncode': result.returncode,
                      'events': events, 'deadline_return_lag_seconds': lag,
                      'survived': survived, 'stderr': result.stderr}
            PROBES.append(record)
            if version == 'old':
                need(result.returncode == 0 and survived and lag > 0,
                     'old deadline-handoff control did not survive expiry')
            else:
                need(result.returncode == -signal.SIGALRM and not survived,
                     'repaired probe was not terminated by SIGALRM')
                need(lag >= -.01 and lag < .50, 'timer test returned outside bounded observation window')
                if mode == 'parse':
                    need(not any(event.get('marker') == 'PARSE_DONE' for event in events),
                         'repaired parse crossed deadline')
                else:
                    alive = next((event for event in events
                                  if event.get('marker') == 'EXEC_ALIVE'), None)
                    need(alive is not None and alive['pid'] == start['pid'],
                         'same-PID exec observation absent')
                    need(alive['default'] is True and alive['blocked'] is False,
                         'exec disposition/mask')
                    need(0 < alive['timer'][0] < .75 and alive['utc'] < start['deadline'],
                         'exec inherited timer is not live/decreasing')
            mark(version+'_'+mode+'_actual_timed_python_path')


def check_control_derivation_without_engine():
    variables, rows, labels, prefix = H.read_hybrid(FIXTURE, production=False)
    script = prefix+D.footer(variables, FIXTURE_SHA, control=True)
    encoded = script.encode('ascii')
    need(len(variables) == 4 and len(rows) == 7 and labels[-1] == 'UNIT/kz',
         'tiny fixture census')
    need('slimgb(I)' not in script and script.count('ideal G=ideal(1);') == 1,
         'control footer solver substitution')
    need(script.count('matrix T=lift(I,ideal(1));') == 1,
         'control footer is not direct lift-to-one')
    DERIVED_CONTROL.update({'bytes': len(encoded), 'sha256': sha(encoded),
                            'variables': len(variables), 'rows': len(rows),
                            'engine_executed': False})
    mark('tiny_control_footer_derived_in_memory_not_executed')


def run_batch():
    started = time.perf_counter()
    before_self = resource.getrusage(resource.RUSAGE_SELF)
    before_child = resource.getrusage(resource.RUSAGE_CHILDREN)
    checks = [
        ('frozen_and_delta', check_frozen_and_delta),
        ('publication_order', check_publication_order),
        ('receipt_binding', check_receipt_binding),
        ('arm_unit_path', check_arm_unit_path),
        ('real_timer_paths', check_real_timer_paths),
        ('control_derivation_without_engine', check_control_derivation_without_engine),
    ]
    sections = []
    for name, function in checks:
        section_start = time.perf_counter()
        function()
        sections.append({'name': name, 'status': 'PASS',
                         'wall_seconds': time.perf_counter()-section_start})
    frozen_after = {name: sha((FROZEN/name).read_bytes()) for name in EXPECTED_FROZEN}
    need(frozen_after == EXPECTED_FROZEN, 'frozen pins changed during controls')
    mark('all_frozen_pins_unchanged_after_controls')
    after_self = resource.getrusage(resource.RUSAGE_SELF)
    after_child = resource.getrusage(resource.RUSAGE_CHILDREN)
    child_cpu = ((after_child.ru_utime+after_child.ru_stime)
                 -(before_child.ru_utime+before_child.ru_stime))
    self_cpu = ((after_self.ru_utime+after_self.ru_stime)
                -(before_self.ru_utime+before_self.ru_stime))
    summary = {
        'schema': 'jc2.caller-repair-delta-gate-controls/v1',
        'status': 'PASS',
        'python_optimize': sys.flags.optimize,
        'sections': sections,
        'outcomes': OUTCOMES,
        'outcome_count': len(OUTCOMES),
        'probes': PROBES,
        'derived_control': DERIVED_CONTROL,
        'patch_eof_context_completion_lines': PATCH_EOF_CONTEXT_COMPLETION_LINES,
        'frozen_sha256': frozen_after,
        'metrics': {
            'wall_seconds': time.perf_counter()-started,
            'self_cpu_seconds': self_cpu,
            'child_cpu_seconds': child_cpu,
            'self_maxrss_kib': after_self.ru_maxrss,
            'child_maxrss_kib': after_child.ru_maxrss,
        },
        'bounds': {'wall_seconds': 30, 'cpu_seconds': 25, 'as_bytes': 512*1024**2},
        'engine_executed': False,
    }
    need(summary['metrics']['wall_seconds'] < 30, 'batch wall bound')
    need(self_cpu+child_cpu < 25, 'batch CPU bound')
    print(json.dumps(summary, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == '--probe':
        probe_main(sys.argv[2], sys.argv[3])
    else:
        need(len(sys.argv) == 1, 'unexpected arguments')
        run_batch()
