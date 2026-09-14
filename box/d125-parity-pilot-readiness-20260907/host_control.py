#!/usr/bin/env python3
"""Actual-host authorization/tiny arithmetic and isolated CAPRUN RSS fixture.
No production constructor, original-source access, CAS, or solver entry point.
"""
from datetime import datetime, timezone
import hashlib
import importlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import socket
import sys
import time

WORK = Path('/home/ubuntu/d125-parity-compression-pilot-20260907')
ENG = WORK/'engineering'
INSTANCE = 'i-0da0cebfc97c9fd54'
GATE = '3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d'
SOURCE = 'b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac'
PINS = {
    'construct.py':'22173cc6a9217a90a8537081a1229b01e58017990b728291285e8cfc01a332a2',
    'replay.py':'2dbb7464fd7b59e361f34b5a705cc7359b98001bf570a80fc77f441e029c2a17',
    'baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
    'qpoly.py':'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
    'run_once.py':'d164af0b576fd7d8f7e3c3a294da8211df996595677aeac75267d2bf9546d40f',
    'run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2',
}
CAPS = dict(wall_seconds=10,cpu_seconds=10,address_bytes=512*1024**2,
            output_bytes=128*1024**2,polynomial_terms=100000,multiply_pairs=1000000,
            coefficient_bits=4096,retained_terms=1000000)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def observed():
    return dict(system=platform.system(),vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),
                instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),
                boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                cwd=str(Path.cwd().resolve()),hostname=socket.gethostname(),now=time.time())


def validate(authority, host, registration_sha, code, control):
    need(control in ('authorize','rss'), 'unknown engineering control')
    need(host['system']=='Linux' and host['vendor']=='Amazon EC2' and
         host['instance']==INSTANCE and host['cwd']==str(WORK), 'exact EC2 host/cwd')
    need(authority.get('schema')=='jc2.d125-parity-engineering-authority/v1' and
         authority.get('engineering_control_only') is True and authority.get('control')==control,
         'engineering-only authority required')
    need(authority.get('root_green') is True and authority.get('construction_only') is True,
         'explicit root engineering GREEN absent')
    need(host['boot']==authority.get('boot_id') and bool(host['boot']), 'boot mismatch')
    need(authority.get('mode')=='slice' and authority.get('symmetry_gate_accepted') is True and
         authority.get('symmetry_gate_sha256')==GATE, 'wrong mathematical gate/slice')
    need(authority.get('registration_sha256')==registration_sha and len(registration_sha)==64,
         'wrong registration pin')
    need(authority.get('job') and authority.get('source_sha256')==SOURCE,
         'registered job/source pin absent')
    need(all(code.get(k)==v==authority['code_sha256'].get(k) for k,v in PINS.items()), 'frozen code drift')
    need(code.get('host_control.py')==authority['code_sha256'].get('host_control.py'), 'control code drift')
    need(authority.get('caps')==CAPS and 0<authority.get('expires_unix',0)-host['now']<=10,
         'engineering caps/deadline drift')


def tiny(C, authority_path):
    # Deliberately the real, frozen authorize function, never C.main.
    authority = C.authorize(authority_path)
    ops = C.Arithmetic(authority['caps'],time.monotonic()+2)
    x = {(0,):C.F(1)}
    value = ops.mul(ops.add(C.const(1),x),ops.add(C.const(1),x,-1))
    need(value=={():C.F(1),(0,0):C.F(-1)}, 'tiny exact arithmetic failed')
    need(ops.production is False, 'control acquired production arithmetic context')
    return authority


def write_identity(control, host, authority_sha):
    record = dict(pid=os.getpid(),pgid=os.getpgrp(),
                  start_ticks=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()[19],
                  cgroup=Path('/proc/self/cgroup').read_text(),
                  pid_namespace=os.readlink('/proc/self/ns/pid'),
                  host=host,argv=sys.argv,authority_sha256=authority_sha,
                  utc=datetime.now(timezone.utc).isoformat(),
                  limits={name:resource.getrlimit(value) for name,value in
                          [('AS',resource.RLIMIT_AS),('CPU',resource.RLIMIT_CPU),
                           ('FSIZE',resource.RLIMIT_FSIZE),('CORE',resource.RLIMIT_CORE)]})
    with (ENG/(control+'.identity.json')).open('x') as stream:
        json.dump(record,stream,sort_keys=True);stream.write('\n');stream.flush();os.fsync(stream.fileno())


def main():
    need(len(sys.argv)==3, 'control and exact engineering authority path required')
    control=sys.argv[1]
    path=Path(sys.argv[2])
    need(path.resolve()==ENG/(control+'.authority.json'), 'exact engineering authority path')
    authority=json.loads(path.read_bytes())
    host=observed()
    code={name:sha(WORK/name) for name in PINS}
    code['host_control.py']=sha(__file__)
    validate(authority,host,sha(WORK/'REGISTRATION.md'),code,control)
    sys.path.insert(0,str(WORK))
    C=importlib.import_module('construct')
    need(Path(C.__file__).resolve()==WORK/'construct.py', 'frozen construct import path')
    # Hostname and exact identity are captured before the arithmetic payload.
    write_identity(control+'-pre',host,sha(path))
    tiny(C,path)
    write_identity(control,host,sha(path))
    if control=='authorize':
        print(json.dumps(dict(status='AUTHORIZATION_AND_TINY_Q_ONLY_PASS',hostname=host['hostname'],
                              construction_invoked=False,source_read=False),sort_keys=True))
        return
    # Same reviewed mechanism as the terminal defect-order RSS control:
    # parent exits; same-PGID descendant ignores TERM and requires scoped KILL.
    read,write=os.pipe();child=os.fork()
    if child==0:
        os.close(read);signal.signal(signal.SIGTERM,signal.SIG_IGN)
        write_identity('rss-descendant',host,sha(path))
        os.write(write,b'R');os.close(write)
        time.sleep(.2);buffer=bytearray(b'X'*(96*1024**2))
        while buffer:
            time.sleep(1)
        os._exit(0)
    os.close(write);need(os.read(read,1)==b'R','RSS descendant not ready');os.close(read)
    print(json.dumps(dict(parent=os.getpid(),child=child,pgid=os.getpgrp())),flush=True)
    os._exit(0)


if __name__=='__main__':
    main()
