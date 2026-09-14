#!/usr/bin/env python3
"""Delta-only mocked payload controls; no authority, process launch, or writes."""
import sys
sys.dont_write_bytecode = True
import ast
import hashlib
import json
import shlex
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as N
import original_engine as OLD
import driver as D

def need(condition, message):
    if not condition:
        raise RuntimeError(message)

class BeforeDeadline(Exception):
    pass

def probe(module, operation, raw):
    """Run the real payload to its deadline call under explicit input mocks."""
    root, eng = module.ROOT, module.ENG
    a = {'mode': 'engineering_control', 'engineering': {
        'operation': operation, 'helper_sha256': 'a'*64,
        'fixture_sha256': module.FIXTURE_SHA, 'root_green_sha256': 'b'*64}}
    effects = []
    def fake_hash(path):
        name = Path(path).name
        if name in module.PINS:
            return module.PINS[name]
        if name == 'engine.py':
            return 'a'*64
        if name == 'ROOT-GREEN.md':
            return 'b'*64
        raise RuntimeError('unexpected hash read: '+str(path))
    def fake_read(path):
        need(str(path) == '/proc/8765/cmdline', 'unexpected payload byte read')
        return raw
    def forbidden(*args, **kwargs):
        effects.append('forbidden effect')
        raise RuntimeError('payload passed deadline sentinel')
    def stop(*args):
        effects.append(('deadline', args[1]))
        raise BeforeDeadline()
    with patch.object(module, '__file__', str(root/'engine.py')), \
         patch.object(Path, 'cwd', return_value=root), \
         patch.object(Path, 'read_bytes', fake_read), \
         patch.object(D, 'context', return_value=(a, 'c'*64, 7.0)), \
         patch.object(D, 'file_sha', side_effect=fake_hash), \
         patch.object(module.os, 'getpid', return_value=4321), \
         patch.object(module.os, 'getpgrp', return_value=4321), \
         patch.object(module.os, 'getppid', return_value=8765), \
         patch.object(module.os.path, 'lexists', return_value=False), \
         patch.object(D, 'arm_deadline', side_effect=stop), \
         patch.object(D, 'limits', side_effect=forbidden), \
         patch.object(D, 'write_new', side_effect=forbidden), \
         patch.object(module.os, 'execve', side_effect=forbidden):
        try:
            module.payload(operation, eng/(operation+'.authority.json'))
        except BeforeDeadline:
            need(effects == [('deadline', 1.0 if operation == 'alarm' else 7.0)],
                 'deadline argument or pre-deadline effect changed')
            return 'REACHED_BEFORE_DEADLINE'
        except ValueError as error:
            need(str(error) == 'exact registered CAPRUN parent argv',
                 'rejected at a different predicate: '+str(error))
            need(effects == [], 'reject after an effect')
            return 'REJECTED_BEFORE_DEADLINE_AND_WRITES'
    raise RuntimeError('unexpected payload return')

def raw_argv(argv):
    return b'\0'.join(argv)+b'\0'

def main():
    source = (HERE/'engine.py').read_text()
    old = (HERE/'original_engine.py').read_text()
    start = source.index('def expected_parent_argv(operation):')
    end = source.index('def payload(operation,authority_path):')
    new_line = "    E.need((parent/'cmdline').read_bytes().split(b'\\0')==expected_parent_argv(operation)+[b''],'exact registered CAPRUN parent argv')"
    old_line = "    E.need(str(ROOT/'run_capped.py').encode() in (parent/'cmdline').read_bytes().split(b'\\0'),'CAPRUN parent')"
    restored = (source[:start]+source[end:]).replace(new_line, old_line)
    need(restored == old, 'delta is not exactly helper insertion plus predicate replacement')
    for filename in ('engine.py', 'original_engine.py', 'driver.py', 'exact.py', 'hybrid.py', 'check.py'):
        need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse((HERE/filename).read_text()))),
             'Assert node in '+filename)
    for filename, expected in N.PINS.items():
        need(hashlib.sha256((HERE/filename).read_bytes()).hexdigest() == expected, 'dependency pin '+filename)
    command = next(line for line in (HERE/'REGISTRATION.md').read_text().splitlines()
                   if line.startswith('/usr/bin/prlimit '))
    registration = shlex.split(command)
    registration = registration[registration.index('--')+1:]
    results = []
    for operation in ('hybrid', 'alarm'):
        expected = [x.replace('OP', operation).encode('ascii') for x in registration]
        need(N.expected_parent_argv(operation) == expected, 'literal registered vector '+operation)
        results.append((operation+'/exact', probe(N, operation, raw_argv(expected))))
        need(results[-1][1] == 'REACHED_BEFORE_DEADLINE', 'valid vector rejected')
        mutations = {}
        # Every scalar or path element, including both interpreters and flags.
        for index, value in enumerate(expected):
            changed = expected.copy()
            changed[index] = value+b'_CHANGED'
            mutations['changed-element-'+str(index)] = raw_argv(changed)
        for option in ('--wall-seconds', '--cpu-seconds', '--rss-bytes',
                       '--rss-sample-seconds', '--term-grace-seconds', '--cwd',
                       '--stdout-file', '--stderr-file', '--telemetry-file'):
            index = expected.index(option.encode())+1
            mutations['missing-value-'+option] = raw_argv(expected[:index]+expected[index+1:])
        mutations['extra-value'] = raw_argv(expected+[b'extra'])
        mutations['missing-child-authority'] = raw_argv(expected[:-1])
        mutations['missing-final-NUL'] = raw_argv(expected)[:-1]
        mutations['extra-final-NUL'] = raw_argv(expected)+b'\0'
        mutations['interior-empty-value'] = raw_argv(expected[:2]+[b'']+expected[2:])
        swapped = expected.copy()
        swapped[1], swapped[2] = swapped[2], swapped[1]
        mutations['reordered-flags'] = raw_argv(swapped)
        decimal = expected.copy()
        decimal[decimal.index(b'--wall-seconds')+1] = b'10.0'
        mutations['numeric-equivalent-not-literal'] = raw_argv(decimal)
        for name, raw in mutations.items():
            verdict = probe(N, operation, raw)
            need(verdict == 'REJECTED_BEFORE_DEADLINE_AND_WRITES', operation+'/'+name)
            results.append((operation+'/'+name, verdict))
        changed = expected.copy()
        changed[changed.index(b'--wall-seconds')+1] = b'999'
        changed[changed.index(b'--stdout-file')+1] = b'/tmp/WRONG-OUTPUT-NOT-CREATED'
        raw = raw_argv(changed)
        need(probe(OLD, operation, raw) == 'REACHED_BEFORE_DEADLINE', 'old defect not reproduced')
        need(probe(N, operation, raw) == 'REJECTED_BEFORE_DEADLINE_AND_WRITES', 'repair did not reject old-pass object')
        results.append((operation+'/old-pass-new-fail-caps-output', 'PASS'))
    try:
        N.expected_parent_argv('decision')
    except ValueError:
        pass
    else:
        raise RuntimeError('unexpected operation admitted')
    print(json.dumps({'status': 'PASS', 'payload_cases': len(results), 'results': results,
                      'exact_delta': True, 'zero_assert_nodes': True,
                      'actual_engine_run': False, 'authority_issued': False}, sort_keys=True))

if __name__ == '__main__':
    main()
