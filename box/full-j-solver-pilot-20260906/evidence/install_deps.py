#!/usr/bin/env python3
"""Root-authorized missing build prerequisites; reject upgrades/removals."""
import json
import os
from pathlib import Path
import re
import socket
import subprocess

root=Path('/home/ubuntu/full-j-solver-pilot-20260906')
if socket.gethostname()!='ip-172-30-0-56' or Path.cwd()!=root:
    raise SystemExit('wrong worker/root')
packages=['autoconf','automake','libtool','pkg-config','libflint-dev','libmpfr-dev']
before=subprocess.check_output(['dpkg-query','-W','-f=${Package}\t${Version}\n'],text=True)
sim=subprocess.run(['apt-get','-s','install','--no-upgrade',*packages],capture_output=True,text=True,check=True)
(root/'apt.simulation.txt').write_text(sim.stdout+sim.stderr)
if not re.search(r'^0 upgraded, \d+ newly installed, 0 to remove',sim.stdout,re.M):
    raise SystemExit('upgrade/removal or unexpected apt summary')
if re.search(r'^(Remv |Inst \S+ \[)',sim.stdout,re.M):
    raise SystemExit('existing package would change')
env=dict(os.environ,DEBIAN_FRONTEND='noninteractive',NEEDRESTART_SUSPEND='1')
done=subprocess.run(['sudo','-n','--preserve-env=DEBIAN_FRONTEND,NEEDRESTART_SUSPEND',
    'apt-get','-y','install','--no-upgrade','--no-remove',*packages],env=env,check=False)
after=subprocess.check_output(['dpkg-query','-W','-f=${Package}\t${Version}\n'],text=True)
def parse(text):return dict(line.split('\t',1) for line in text.splitlines())
b,a=parse(before),parse(after)
changed={k:[v,a.get(k)] for k,v in b.items() if a.get(k)!=v}
record={'authorization':'root parent 2026-09-06, missing prerequisites only; simulation inspected',
        'returncode':done.returncode,'added':{k:v for k,v in a.items() if k not in b},'changed_existing':changed,
        'requested':packages}
(root/'apt.custody.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
if done.returncode or changed:raise SystemExit('install failure or unexpected package mutation')
print('MISSING_PREREQUISITES_ONLY_PASS',flush=True)
