#!/usr/bin/env python3
"""Root-authorized cleanup of one exact orphan monitor and its sleeps."""
from pathlib import Path
import datetime
import json
import os
import signal
import socket
import time
root=Path('/home/ubuntu/fleet-recoverable-stop-20260906')
if socket.gethostname()!='ip-172-30-0-63' or Path.cwd()!=root: raise SystemExit('wrong worker')
EXPECTED=['bash','-c','cd /home/ubuntu/t2t3-longsolve/runs; until [ -s d2-z55-msolve/solver.stdout ] && grep -q "BEGIN_STD" d2-z55-singular/solver.stdout 2>/dev/null; do sleep 15; done; date -u +"FIRSTLINES_AT %H:%M:%SZ"; echo "=== MSOLVE ==="; head -25 d2-z55-msolve/solver.stdout; echo "=== SINGULAR ==="; head -8 d2-z55-singular/solver.stdout']
def need(ok,why):
    if not ok: raise SystemExit(why)
def proc(pid):
    p=Path('/proc')/str(pid); raw=(p/'stat').read_text(); f=raw[raw.rindex(')')+2:].split()
    return {'pid':pid,'state':f[0],'ppid':int(f[1]),'pgid':int(f[2]),'start_ticks':int(f[19]),
        'argv':(p/'cmdline').read_bytes().decode().rstrip('\0').split('\0'),
        'cgroup':(p/'cgroup').read_text(),'namespaces':{n:os.readlink(p/'ns'/n) for n in ('pid','mnt','user','net','cgroup')}}
def check(r,bash):
    need(r['pgid']==24286 and r['state']!='Z','wrong group/state')
    need(r['cgroup']=='0::/user.slice/user-1000.slice/session-91.scope\n','wrong cgroup')
    need(r['namespaces']['pid']=='pid:[4026531836]' and r['namespaces']['mnt']=='mnt:[4026531832]','wrong namespace')
    if bash: need(r['pid']==24286 and r['start_ticks']==197859 and r['argv']==EXPECTED,'wrong monitor identity')
    else: need(r['argv']==['sleep','15'],'unexpected group member: stop')
def members():
    out=[]
    for p in Path('/proc').iterdir():
        if not p.name.isdigit(): continue
        try:
            raw=(p/'stat').read_text(); f=raw[raw.rindex(')')+2:].split()
            if int(f[2])==24286 and f[0]!='Z': out.append(proc(int(p.name)))
        except (FileNotFoundError,ProcessLookupError): continue
    return out
initial=members()
need(any(r['pid']==24286 for r in initial),'monitor missing before scoped cleanup')
for r in initial: check(r,r['pid']==24286)
actions=[]
def term(pid,bash):
    try: fd=os.pidfd_open(pid,0)
    except ProcessLookupError: return
    try:
        r=proc(pid); check(r,bash); again=proc(pid)
        for k in ('pid','pgid','start_ticks','argv','cgroup','namespaces'): need(r[k]==again[k],'identity drift')
        signal.pidfd_send_signal(fd,signal.SIGTERM,None,0)
        actions.append({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'signal':'SIGTERM','mechanism':'pidfd_send_signal','identity':r})
    finally: os.close(fd)
term(24286,True)
for r in initial:
    if r['pid']!=24286:
        try: term(r['pid'],False)
        except (FileNotFoundError,ProcessLookupError): pass
for _ in range(20):
    remaining=members()
    if not remaining: break
    time.sleep(0.1)
need(not remaining,'scoped group still live; no instance action')
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'authorization':'ROOT explicit stale monitor PID/PGID24286 cleanup, start_ticks197859; no other process scope',
 'before':initial,'actions':actions,'after':remaining}
with (root/'monitor-cleanup.json').open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'actions':[(r['identity']['pid'],r['signal']) for r in actions],'remaining':remaining},sort_keys=True))
