#!/usr/bin/env python3
"""Fable5 independent parent-argv delta controls. Mocked inputs only: no launch,
authority, timer, limit, write, exec, network, CAS or Singular. Prints one JSON."""
import sys
sys.dont_write_bytecode = True
import ast, hashlib, json
from pathlib import Path
from unittest.mock import patch

INPUTS = Path('/tmp/jc2-lane.Fwngeq/inputs')
sys.path.insert(0, str(INPUTS))
import engine as NEW
import original_engine as OLD
import driver as D

def need(ok, msg):
    if not ok:
        raise RuntimeError(msg)

ROOT = '/home/ubuntu/d125-hybrid81-exact-solver-20260907'
ENG = ROOT + '/engineering'
PRLIMIT_PREFIX = ['/usr/bin/prlimit', '--fsize=67108864:67108864', '--core=0:0', '--']

def registered(op):
    """Own derivation: single-space split of the one literal line, explicit 4-token prefix drop."""
    lines = [l for l in (INPUTS/'REGISTRATION.md').read_text().splitlines() if l.startswith('/usr/bin/prlimit ')]
    need(len(lines) == 1, 'exactly one literal command line')
    toks = lines[0].split(' ')
    need(all(toks) and '"' not in lines[0] and "'" not in lines[0], 'plain unquoted tokens')
    need(toks[:4] == PRLIMIT_PREFIX, 'outer prlimit exec prefix')
    body = toks[4:]
    need(len(body) == 29, '29 tokens after the prefix')
    need(sum('OP' in t for t in body) == 5 and 'OP' not in ROOT, 'five OP slots, none inside ROOT')
    return [t.replace('OP', op).encode('ascii') for t in body]

def handwritten(op):
    return [x.encode('ascii') for x in [
        '/usr/bin/python3', '-I', '-B', ROOT+'/run_capped.py',
        '--wall-seconds', '10', '--cpu-seconds', '10', '--rss-bytes', '536870912',
        '--rss-sample-seconds', '0.05', '--term-grace-seconds', '0.25', '--cwd', ROOT,
        '--stdout-file', ENG+'/'+op+'.stdout', '--stderr-file', ENG+'/'+op+'.stderr',
        '--telemetry-file', ENG+'/'+op+'.telemetry.json',
        '--', '/usr/bin/python3', '-I', '-B', ROOT+'/engine.py', op, ENG+'/'+op+'.authority.json']]

SLOTS = {0:'parent interpreter',1:'parent -I',2:'parent -B',3:'runner path',4:'--wall-seconds',5:'wall value',
         6:'--cpu-seconds',7:'cpu value',8:'--rss-bytes',9:'rss value',10:'--rss-sample-seconds',11:'sample value',
         12:'--term-grace-seconds',13:'grace value',14:'--cwd',15:'cwd value',16:'--stdout-file',17:'stdout path',
         18:'--stderr-file',19:'stderr path',20:'--telemetry-file',21:'telemetry path',22:'separator --',
         23:'child interpreter',24:'child -I',25:'child -B',26:'child engine.py',27:'operation',28:'authority path'}

class Sentinel(Exception):
    pass

def probe(module, op, raw):
    """Real module.payload under own mocks; stops at arm_deadline, forbids limits/writes/exec."""
    a = {'mode':'engineering_control','engineering':{'operation':op,'helper_sha256':'e'*64,
         'fixture_sha256':module.FIXTURE_SHA,'root_green_sha256':'f'*64}}
    effects = []
    def sha(path):
        name = Path(path).name
        if name in module.PINS: return module.PINS[name]
        if name == 'engine.py': return 'e'*64
        if name == 'ROOT-GREEN.md': return 'f'*64
        raise RuntimeError('unexpected hash '+str(path))
    def rb(self):
        need(str(self) == '/proc/777/cmdline', 'unexpected read '+str(self))
        return raw
    def forbid(*args, **kw):
        effects.append('effect'); raise RuntimeError('effect past sentinel')
    def stop(a_, duration):
        effects.append(('deadline', duration)); raise Sentinel()
    with patch.object(module, '__file__', ROOT+'/engine.py'), \
         patch.object(Path, 'cwd', return_value=Path(ROOT)), \
         patch.object(Path, 'read_bytes', rb), \
         patch.object(D, 'context', return_value=(a, 'd'*64, 3.5)), \
         patch.object(D, 'file_sha', side_effect=sha), \
         patch.object(module.os, 'getpid', return_value=999), \
         patch.object(module.os, 'getpgrp', return_value=999), \
         patch.object(module.os, 'getppid', return_value=777), \
         patch.object(module.os.path, 'lexists', return_value=False), \
         patch.object(D, 'arm_deadline', side_effect=stop), \
         patch.object(D, 'limits', side_effect=forbid), \
         patch.object(D, 'write_new', side_effect=forbid), \
         patch.object(module.os, 'execve', side_effect=forbid):
        try:
            module.payload(op, ENG+'/'+op+'.authority.json')
        except Sentinel:
            need(effects == [('deadline', 1.0 if op == 'alarm' else 3.5)], 'deadline argument')
            return 'ACCEPT'
        except ValueError as e:
            need(effects == [], 'effect before reject')
            return 'REJECT:'+str(e)
    raise RuntimeError('payload returned')

def raw_of(argv):
    return b'\0'.join(argv)+b'\0'

def main():
    out = {'python': sys.version.split()[0], 'optimize': sys.flags.optimize, 'vectors': {}, 'cases': []}
    for op in ('hybrid', 'alarm'):
        reg, hand, eng = registered(op), handwritten(op), NEW.expected_parent_argv(op)
        need(reg == hand == eng and len(eng) == 29, 'vector identity '+op)
        need(all(x and x == x.strip() and x.isascii() for x in eng), 'nonempty ascii unpadded elements')
        need(eng[27] == op.encode() and eng[28].endswith((op+'.authority.json').encode()), 'child tail literal '+op)
        out['vectors'][op] = {'elements': 29, 'raw_bytes': len(raw_of(eng)), 'nul_count': raw_of(eng).count(b'\0'),
                              'sha256_raw': hashlib.sha256(raw_of(eng)).hexdigest()}
    for op in ('hybrid', 'alarm'):
        other = 'alarm' if op == 'hybrid' else 'hybrid'
        exp = NEW.expected_parent_argv(op)
        objects = {'registered-exact': raw_of(exp)}
        objects['cross-operation-vector'] = raw_of(NEW.expected_parent_argv(other))
        objects['prlimit-prefix-retained'] = raw_of([t.encode() for t in PRLIMIT_PREFIX]+exp)
        v = exp.copy(); v[1] = b'-i'; objects['flag-case-changed'] = raw_of(v)
        v = exp.copy(); v[5] = b'10 '; objects['padded-cap-value'] = raw_of(v)
        v = exp.copy(); v[27] = other.encode(); objects['child-operation-swapped-only'] = raw_of(v)
        v = exp.copy(); v[23] = b'/usr/bin/python3.12'; objects['child-interpreter-variant'] = raw_of(v)
        objects['runner-token-alone'] = raw_of([exp[3]])
        objects['child-tail-alone'] = raw_of(exp[23:])
        objects['empty-cmdline'] = b''
        objects['duplicated-vector'] = raw_of(exp+exp)
        for name, raw in objects.items():
            new, old = probe(NEW, op, raw), probe(OLD, op, raw)
            out['cases'].append({'operation': op, 'object': name, 'new': new, 'old': old})
            if name == 'registered-exact':
                need(new == 'ACCEPT' and old == 'ACCEPT', 'valid vector must reach the deadline sentinel')
            else:
                need(new == 'REJECT:exact registered CAPRUN parent argv', 'new predicate must reject '+name)
    out['old_pass_new_fail'] = sorted({c['object'] for c in out['cases'] if c['old'] == 'ACCEPT' and c['new'] != 'ACCEPT'})
    out['both_reject'] = sorted({c['object'] for c in out['cases'] if c['old'] != 'ACCEPT' and c['new'] != 'ACCEPT'})
    out['slots'] = [SLOTS[i]+'='+NEW.expected_parent_argv('hybrid')[i].decode() for i in range(29)]
    asserts = {}
    for p in sorted(INPUTS.glob('*.py')):
        tree = ast.parse(p.read_text())
        asserts[p.name] = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
        need('__debug__' not in p.read_text(), '__debug__ use in '+p.name)
    out['assert_nodes'] = asserts
    need(sum(asserts.values()) == 0, 'Assert nodes present')
    out['status'] = 'PASS'
    print(json.dumps(out, sort_keys=True, indent=1))

if __name__ == '__main__':
    main()
