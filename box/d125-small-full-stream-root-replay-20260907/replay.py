"""Root outer harness; imports the frozen independent Fable math unchanged."""
import ast
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

ROOT = Path('/home/ubuntu/d125-small-full-stream-root-replay-20260907')
SOURCE = Path('/home/ubuntu/d125-small-source-construction-pilot-20260906')
GATE = 'f88d0665bbe7e4f0dd519167c1f99c4a519235c2c127b76c35273d4b533118c6'
CUSTODY = '601643fcd066c19a24b04e22a0374c7e9fd5f106b0bfb5be43c695eb8c1b23b9'
BOOT = '69938ee6-48bb-4e45-bdf2-efb08c655368'

def need(ok, why):
    if not ok:
        raise RuntimeError(why)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(name, obj):
    data = (json.dumps(obj, sort_keys=True, indent=1)+'\n').encode()
    need(len(data) < 1024**2, 'receipt ceiling')
    with Path(name).open('xb') as f:
        f.write(data)

def identity():
    need(Path.cwd().resolve() == ROOT, 'wrong cwd')
    need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2', 'not EC2')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() == 'i-0da0cebfc97c9fd54', 'wrong instance')
    need(Path('/proc/sys/kernel/random/boot_id').read_text().strip() == BOOT, 'wrong boot')
    return {'pid': os.getpid(), 'pgid': os.getpgrp(), 'boot': BOOT,
            'start_ticks': Path('/proc/self/stat').read_text().split(') ', 1)[1].split()[19],
            'pid_namespace': os.readlink('/proc/self/ns/pid'), 'cwd': str(ROOT)}

def main():
    ident = identity()
    need(ident['pid'] == ident['pgid'], 'not exact group leader')
    resource.setrlimit(resource.RLIMIT_FSIZE, (64*1024**2,)*2)
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    if sys.argv[1:] == ['dummy']:
        resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
        save('dummy.identity.json', ident)
        child = os.fork()
        if child == 0:
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
            occupied = bytearray(32*1024**2)
            for i in range(0, len(occupied), 4096):
                occupied[i] = 1
            save('dummy.descendant.json', identity())
            time.sleep(10)
            os._exit(0)
        os._exit(0)
    need(sys.argv[1:] == ['verify'], 'unregistered mode')
    resource.setrlimit(resource.RLIMIT_AS, (8*1024**3,)*2)
    need(sha(ROOT/'gate.py') == GATE, 'gate pin')
    need(sha(ROOT/'source-custody.json') == CUSTODY, 'custody pin')
    for filename in ('replay.py', 'gate.py'):
        need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse((ROOT/filename).read_text()))), 'removable assertion')
    sys.path.insert(0, str(ROOT))
    import gate as g
    custody = json.loads((ROOT/'source-custody.json').read_bytes())
    expected_pins = {a['path']: a['sha256'] for a in custody['artifacts_before_custody']
                     if a['relative'].endswith(('.jsonl', '.sing'))}
    need(len(expected_pins) == 12, 'complete source pin roster')
    for path, digest in expected_pins.items():
        need(Path(path).parent.parent == SOURCE and sha(path) == digest, 'source pin '+path)
    results = []
    start = time.monotonic()
    for case in ('unequal', 'common_3', 'common_4'):
        for branch in ('rational', 'golden'):
            directory = SOURCE/(case+'-'+branch)
            prefix = directory/('client-'+case+'-'+branch)
            data = prefix.with_suffix('.jsonl').read_bytes()
            text = prefix.with_suffix('.sing').read_text('ascii')
            actual = g.parse_jsonl(data)
            expected, variables = g.reconstruct(case, branch)
            authority = sha(directory/'authority.json')
            g.need(actual[0]['authority_sha256'] == authority, 'sibling authority mismatch')
            expected[0]['authority_sha256'] = authority
            expected.append(g.footer_for(expected))
            g.compare(expected, actual)
            rows = [r for r in actual if r['type'] == 'row']
            counts = g.check_singular(text, variables, branch == 'golden', rows)
            controls, skipped = [], []
            for name, fn, sfn in g.mutations(actual, text, variables, branch == 'golden'):
                if name == 'fixed_zero_face' and not any(r.get('type') == 'coefficient' and
                   'fixed' in r and g.decode(r['fixed']).zero() and r['point'] != [0, 0] for r in actual):
                    skipped.append({'control': name, 'reason': 'no nonorigin fixed-zero coefficient exists'})
                    continue
                if fn is not None:
                    changed = b''.join(g.canon(r) for r in fn())
                    need(changed != data, 'mutation not applied: '+name)
                    try:
                        g.compare(expected, g.parse_jsonl(changed))
                    except g.GateError as err:
                        controls.append({'control': name, 'error': str(err)})
                    else:
                        raise RuntimeError('mutation accepted: '+name)
                else:
                    changed = sfn(text)
                    need(changed != text, 'mutation not applied: '+name)
                    try:
                        g.check_singular(changed, variables, branch == 'golden', rows)
                    except g.GateError as err:
                        controls.append({'control': name, 'error': str(err)})
                    else:
                        raise RuntimeError('mutation accepted: '+name)
            duplicate = data.replace(b'{"authority_sha256":', b'{"authority_sha256":"duplicate","authority_sha256":', 1)
            for name, changed in [('duplicate_json_key', duplicate),
                                  ('trailing_json', data+g.canon(actual[-1])),
                                  ('truncated_no_footer', data[:-len(g.canon(actual[-1]))])]:
                need(changed != data, 'raw mutation not applied: '+name)
                try:
                    g.compare(expected, g.parse_jsonl(changed))
                except g.GateError as err:
                    if name == 'duplicate_json_key':
                        need('duplicate JSON key' in str(err), 'wrong duplicate rejection')
                    controls.append({'control': name, 'error': str(err)})
                else:
                    raise RuntimeError('raw mutation accepted: '+name)
            result = {'case': case, 'branch': branch, 'variables': len(variables),
                      'counts': actual[-1]['counts'], 'singular_rows': counts[0],
                      'singular_nonzero': counts[1], 'rejected_controls': controls,
                      'inapplicable_controls': skipped, 'verdict': 'ALL_ACTUAL_ROWS_MATCH'}
            results.append(result)
            print(json.dumps({k: result[k] for k in ('case', 'branch', 'variables', 'counts', 'verdict')}), flush=True)
    for path, digest in expected_pins.items():
        need(sha(path) == digest, 'post source drift')
    save('verification.json', {'status': 'ALL_SIX_ACTUAL_STREAMS_MATCH_CONTROLS_REJECT', 'identity': ident,
         'checker_sha256': GATE, 'harness_sha256': sha(__file__), 'source_pins': expected_pins,
         'seconds': time.monotonic()-start, 'results': results, 'mode': 'normal'})

if __name__ == '__main__':
    main()
