#!/usr/bin/env python3
"""Validate two named solver identities; PIDFD TERM only; harvest custody."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import signal
import socket
import subprocess
import sys

ROOT=Path('/home/ubuntu/degree99-longsolve-stop-astra-20260906')
LANE=Path('/home/ubuntu/t2t3-longsolve')
TARGETS={20597:{'start_ticks':178713,'pgid':20596,'job':'d2-z55-msolve',
   'argv':['/tmp/msolve-patched/bin/msolve','-m','5000','-g','2','-t','64','-v','2','--random-seed','0',
           '-f',str(LANE/'presentations/d2-z55-source/99-delta2.ms'),'-o',str(LANE/'runs/d2-z55-msolve/basis.ms')],
   'binary_sha256':'da552c7c21d5339973fa6cc2157a171555af6d359ad7a4a392199702d5837530'},
   20637:{'start_ticks':179018,'pgid':20636,'job':'d2-z55-singular',
   'argv':['/usr/bin/Singular','-q','--no-rc','--no-warn','--no-shell','--threads=1','--flint-threads=1',
           str(LANE/'presentations/d2-z55-source/99-delta2-slimgb.sing')],
   'binary_sha256':'90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4'}}
HASHES={str(LANE/'msolve_m5000_wrapper.sh'):'324f4e8c8a5b112dbf6051e5bb84aff0d6de4ccc973cfca1919881766145f9b9',
 str(LANE/'run_longsolve.sh'):'a2e4779ec0e1b3f1a7ac6fe86b4052cbab213f8fb2282b95c3638096158e5ac2',
 str(LANE/'run_capped.py'):'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2',
 str(LANE/'presentations/d2-z55-source/99-delta2.ms'):'7f593b87e40f02dbdb91f9b22aace6989f4a4d2092d9903276675b3265c7b572',
 str(LANE/'presentations/d2-z55-source/99-delta2.sing'):'a604ed314ced1a33ff46e43081c2222430f24bde96a10405a3a8562ec6dccbbc',
 str(LANE/'presentations/d2-z55-source/99-delta2-slimgb.sing'):'354b9293d065035f4e3b7ca2c918eb27cb5dc2ac3407eea2f02e9e467ba3ab7c',
 str(LANE/'presentations/d2-z55-source/99-delta2.labels.tsv'):'ef8083969910b3709e084b0285d21e5a87328055a77accc3d8aacc7c895d5344'}

def need(ok,why):
    if not ok: raise RuntimeError(why)

def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()

def save(name,obj):
    with (ROOT/name).open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())

def proc(pid):
    p=Path('/proc')/str(pid)
    raw=(p/'stat').read_text(); fields=raw[raw.rindex(')')+2:].split()
    return {'pid':pid,'state':fields[0],'ppid':int(fields[1]),'pgid':int(fields[2]),
        'start_ticks':int(fields[19]),'argv':(p/'cmdline').read_bytes().decode().rstrip('\0').split('\0'),
        'cgroup':(p/'cgroup').read_text(),
        'namespaces':{n:os.readlink(p/'ns'/n) for n in ('pid','mnt','user','cgroup','net')},
        'exe':os.readlink(p/'exe'),'status':(p/'status').read_text(),'stat':raw}

def members():
    found=[]
    for p in Path('/proc').iterdir():
        if not p.name.isdigit(): continue
        try:
            raw=(p/'stat').read_text(); fields=raw[raw.rindex(')')+2:].split()
            if int(fields[2]) in (20596,20636):
                found.append({'pid':int(p.name),'state':fields[0],'pgid':int(fields[2]),'start_ticks':int(fields[19])})
        except (FileNotFoundError,ProcessLookupError,PermissionError): continue
    return found

def machine():
    return {'utc':utc(),'hostname':socket.gethostname(),'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
      'meminfo':Path('/proc/meminfo').read_text(),
      'swap_counters':{k:int(v) for k,v in (line.split() for line in Path('/proc/vmstat').read_text().splitlines()) if k in ('pswpin','pswpout')},
      'mounts':subprocess.check_output(['findmnt','-J','-T',str(LANE)],text=True),
      'tmp_mount':subprocess.check_output(['findmnt','-J','-T','/tmp/msolve-patched'],text=True),
      'block_devices':subprocess.check_output(['lsblk','-J','-b','-o','NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,SERIAL'],text=True),
      'disk_free':subprocess.check_output(['df','-B1',str(LANE),'/tmp/msolve-patched'],text=True),
      'group_members':members()}

def validate(pid,expected=None):
    record=proc(pid); target=TARGETS[pid]
    need(record['state']!='Z','solver already zombie')
    need(record['start_ticks']==target['start_ticks'] and record['pgid']==target['pgid'],'PID/start/group mismatch')
    need(record['ppid']==target['pgid'],'solver not direct child of recorded time leader')
    need(record['argv']==target['argv'],'exact solver argv mismatch')
    need(record['cgroup']=='0::/user.slice/user-1000.slice/session-87.scope\n','cgroup mismatch')
    need(record['namespaces']['pid']=='pid:[4026531836]' and record['namespaces']['mnt']=='mnt:[4026531832]','namespace mismatch')
    need(sha(Path('/proc')/str(pid)/'exe')==target['binary_sha256'],'live executable hash mismatch')
    if expected:
        for k in ('pid','ppid','pgid','start_ticks','argv','cgroup','namespaces','exe'):
            need(record[k]==expected[k],'snapshot identity drift '+k)
    return record

def snapshot():
    info=machine()
    info['targets']={str(pid):validate(pid) for pid in TARGETS}
    info['parents']={str(t['pgid']):proc(t['pgid']) for t in TARGETS.values()}
    info['hashes']={p:sha(p) for p in HASHES}
    for p,d in HASHES.items(): need(info['hashes'][p]==d,'custody file hash mismatch '+p)
    boot=int(next(line.split()[1] for line in Path('/proc/stat').read_text().splitlines() if line.startswith('btime ')))
    ticks=os.sysconf('SC_CLK_TCK')
    info['process_start_utc']={str(pid):datetime.datetime.fromtimestamp(boot+t['start_ticks']/ticks,datetime.timezone.utc).isoformat()
        for pid,t in TARGETS.items()}
    info['historical_identity_limit']='Old custody has PID/PGID/argv/hashes/preflight UTC but no raw start_ticks/ns/cgroup; current exact identities are anchored here before PIDFD signaling.'
    save('pre.json',info)
    print(json.dumps({'utc':info['utc'],'process_start_utc':info['process_start_utc'],'all_hashes_match':True,
        'groups':info['group_members'],'snapshot_sha256':sha(ROOT/'pre.json')}))

def stop():
    before=json.loads((ROOT/'pre.json').read_text())
    need(before['boot_id']==Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'boot changed')
    handles=[]
    try:
        for pid in TARGETS:
            fd=os.pidfd_open(pid,0)
            record=validate(pid,before['targets'][str(pid)])
            handles.append((pid,fd,record))
        plan={'utc':utc(),'operator_reason':'ROOT authorized METHOD_ONLY stop: actual degree99 externally closed; no named open client justifies remaining16h. Not a solver mathematical verdict.',
              'signal':'SIGTERM','targets':[record for _,_,record in handles],'snapshot_sha256':sha(ROOT/'pre.json')}
        save('signal-plan.json',plan)
        with (ROOT/'signal-actions.jsonl').open('x') as f:
            for pid,fd,record in handles:
                validate(pid,before['targets'][str(pid)])
                signal.pidfd_send_signal(fd,signal.SIGTERM,None,0)
                f.write(json.dumps({'utc':utc(),'pid':pid,'pgid':record['pgid'],'start_ticks':record['start_ticks'],'signal':'SIGTERM','mechanism':'pidfd_send_signal','status':'SENT'})+'\n')
                f.flush(); os.fsync(f.fileno())
                print('SIGTERM_SENT',pid,flush=True)
    finally:
        for _,fd,_ in handles: os.close(fd)

def post():
    info=machine()
    need(not [r for r in info['group_members'] if r['state']!='Z'],'live registered group remains')
    info['jobs']={}
    for t in TARGETS.values():
        d=LANE/'runs'/t['job']
        need((d/'runner.rc').is_file(),'wrapper has not finalized rc '+t['job'])
        files={str(p.relative_to(d)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in d.rglob('*') if p.is_file()}
        info['jobs'][t['job']]={'run_dir':str(d),'files':files,
            'runner_rc':(d/'runner.rc').read_text(),'caprun':json.loads((d/'caprun.json').read_text()),
            'stdout':(d/'solver.stdout').read_text(),'stderr':(d/'solver.stderr').read_text(),
            'time':(d/'time.txt').read_text(),'postflight':(d/'postflight.sha256').read_text()}
    info['hashes']={p:sha(p) for p in HASHES}
    for p,d in HASHES.items(): need(info['hashes'][p]==d,'preserved source/input hash drift '+p)
    info['lane_inventory']=[{'path':str(p),'bytes':p.stat().st_size} for p in LANE.rglob('*') if p.is_file()]
    info['classification']='OPERATOR_STOP / NO_COMPLETED_RESULT; neither unit nor properness evidence'
    save('post.json',info)
    print(json.dumps({'utc':info['utc'],'group_members':info['group_members'],'runner_rc':{k:v['runner_rc'] for k,v in info['jobs'].items()},
       'post_sha256':sha(ROOT/'post.json')}))

need(socket.gethostname()=='ip-172-30-0-63' and Path.cwd()==ROOT,'wrong worker/root')
need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','EC2 required')
mode=sys.argv[1]
if mode=='snapshot': snapshot()
elif mode=='stop': stop()
elif mode=='post': post()
else: raise SystemExit('unknown mode')
