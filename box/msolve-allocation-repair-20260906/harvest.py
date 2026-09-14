#!/usr/bin/env python3
"""Compact terminal-only custody; never inspect another lane's report/log."""
from pathlib import Path
import hashlib
import json
import os
import socket
import subprocess
import time

root=Path('/home/ubuntu/msolve-allocation-repair-20260906')
if Path.cwd()!=root or socket.gethostname()!='ip-172-30-0-56':
    raise SystemExit('wrong custody root/worker')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
names=['dummy','build','upgrade','tests','tests-retry']
records={name:json.loads((root/(name+'.telemetry.json')).read_text()) for name in names}
groups={r['pgid'] for r in records.values()}
live=[]
for proc in Path('/proc').iterdir():
    if not proc.name.isdigit(): continue
    try:
        raw=(proc/'stat').read_text(); fields=raw[raw.rindex(')')+2:].split()
        if int(fields[2]) in groups and fields[0]!='Z':
            live.append({'pid':int(proc.name),'pgid':int(fields[2]),'state':fields[0]})
    except (FileNotFoundError,ProcessLookupError,PermissionError): continue
if live: raise SystemExit('registered live members remain: '+repr(live))
if records['dummy']['status']!='WALL_TIMEOUT' or not records['dummy']['termination']['cleanup_complete']:
    raise SystemExit('dummy failed lifecycle')
for name in ['build','upgrade','tests-retry']:
    if records[name]['status']!='NORMAL_EXIT' or records[name]['child_returncode']!=0:
        raise SystemExit('nonterminal/failed required stage '+name)
files={p.name:{'sha256':sha(p),'bytes':p.stat().st_size} for p in root.iterdir() if p.is_file()}
src=root/'msolve-source'
source_names=['src/msolve/iofiles.c','src/msolve/checked-input-size.h','src/neogb/io.c',
              'src/msolve/msolve.c','src/msolve/msolve-data.h','src/neogb/data.h']
binary_names=['.libs/msolve','msolve','src/msolve/.libs/libmsolve.so.3.0.7','src/neogb/.libs/libneogb.so.3.0.7']
rec={'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'hostname':socket.gethostname(),
    'instance':'i-0da0cebfc97c9fd54','worker_root':str(root),'owner':'/root/model_productivity',
    'coordinator_retains_instance':True,'files':files,'terminal_stages':records,'live_registered_group_members':live,
    'sources':{n:sha(src/n) for n in source_names},'binaries':{n:sha(src/n) for n in binary_names},
    'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=src,text=True).strip(),
    'build_test_elapsed_seconds':sum(records[n]['wall_elapsed_seconds'] for n in names if n!='dummy'),
    'max_observed_group_rss_bytes':max(r['max_observed_group_rss_bytes'] for r in records.values()),
    'no_giant_parser_or_complete_F4':True,'package_or_instance_changes':False,
    'remaining_hazards':'See sealed report: not a general memory-safety audit or unrestricted solver approval.'}
with (root/'custody.json').open('x') as f: json.dump(rec,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'custody_sha256':sha(root/'custody.json'),'elapsed':rec['build_test_elapsed_seconds'],
    'max_rss':rec['max_observed_group_rss_bytes'],'terminal_pgids':sorted(groups),'live':live},sort_keys=True))
