#!/usr/bin/env python3
"""Construction then literal replay in one capped process; no solver or retry.

The unchanged CAPRUN/v1 supervisor owns process-group RSS and cleanup. This
entry point creates no subprocesses. It must be reviewed before AWS use.
"""
import hashlib
import importlib
import json
import os
from pathlib import Path
import platform
import sys
import time

WORK = Path('/home/ubuntu/d125-parity-compression-pilot-20260907')
SOURCE = Path('/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl')
GATE = '3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d'
PINS = {
    'construct.py':'22173cc6a9217a90a8537081a1229b01e58017990b728291285e8cfc01a332a2',
    'replay.py':'2dbb7464fd7b59e361f34b5a705cc7359b98001bf570a80fc77f441e029c2a17',
    'baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
    'qpoly.py':'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def pipeline(C, R, authority, authority_path):
    """No external execution; mocked on tiny controls before production review."""
    need(authority['mode']=='slice', 'this pilot is slice only')
    start=time.monotonic()
    saved=sys.argv
    try:
        sys.argv=[str(WORK/'construct.py'),str(authority_path)]
        C.main()  # Authorization/limits precede every production allocation.
    finally:
        sys.argv=saved
    remaining=authority['expires_unix']-time.time()
    need(remaining>0, 'shared deadline exhausted before replay')
    ops=C.Arithmetic(authority['caps'],time.monotonic()+remaining)
    ops.production=True
    result=R.replay_frozen(SOURCE,WORK/'construction.jsonl',ops)
    need(result.get('status')=='ALL_ORIGINAL_ROWS_TRANSPORTED' and result.get('rows')==803,
         'incomplete original-source replay')
    need(time.time()<authority['expires_unix'], 'shared deadline exhausted after replay')
    result.update(elapsed_seconds=time.monotonic()-start,stats=ops.stats,
                  scope='construction and803-row substitution only; no ideal decision')
    return result

def main():
    need(len(sys.argv)==2, 'one fresh authority JSON path required')
    need(platform.system()=='Linux' and Path.cwd()==WORK, 'registered Linux cwd required')
    need('Amazon EC2' in Path('/sys/class/dmi/id/sys_vendor').read_text(), 'EC2 only')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54', 'instance mismatch')
    authority_path=Path(sys.argv[1])
    need(authority_path.resolve()==WORK/'authority.json', 'exact authority path')
    authority=json.loads(authority_path.read_bytes())
    need(authority.get('schema')=='jc2.d125-parity-construction-authority/v1', 'authority schema')
    need(authority.get('mode')=='slice' and authority.get('symmetry_gate_sha256')==GATE,
         'exact slice and accepted mathematical gate required')
    need(digest(WORK/'REGISTRATION.md')==authority['registration_sha256'], 'registration pin')
    need(digest(Path(__file__))==authority['code_sha256']['run_once.py'], 'caller pin')
    for name,pin in PINS.items():
        need(digest(WORK/name)==pin==authority['code_sha256'][name], 'frozen code pin '+name)
    sys.path.insert(0,str(WORK))
    C=importlib.import_module('construct'); R=importlib.import_module('replay')
    need(Path(C.__file__).resolve()==WORK/'construct.py' and Path(R.__file__).resolve()==WORK/'replay.py', 'module paths')
    C.authorize(authority_path)
    need(digest(SOURCE)==C.SOURCE, 'source pre-construction pin')
    # Reserve the success receipt exclusively before starting, never overwrite.
    with (WORK/'replay-result.json').open('xb') as out:
        result=pipeline(C,R,authority,authority_path)
        need(digest(SOURCE)==C.SOURCE, 'source post-replay pin')
        result.update(authority_sha256=digest(authority_path),construction_sha256=digest(WORK/'construction.jsonl'))
        need(time.time()<authority['expires_unix'], 'shared deadline exhausted before receipt')
        out.write(C.B.canonical(result));out.flush();os.fsync(out.fileno())
    print(json.dumps({'status':'CONSTRUCTED_AND_REPLAYED_NO_IDEAL_DECISION',
                      'replay_receipt_sha256':digest(WORK/'replay-result.json')}))

if __name__=='__main__':
    main()
