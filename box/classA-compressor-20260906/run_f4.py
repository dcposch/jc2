#!/usr/bin/env python3
"""Bounded worker-local modular F4; a modular unit is SIGNAL only."""
import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory',type=Path)
    ap.add_argument('--msolve',type=Path,required=True);ap.add_argument('--seconds',type=int,default=3590)
    ap.add_argument('--threads',type=int,default=32)
    a=ap.parse_args();assert 1<=a.seconds<=3590
    d=a.directory.resolve();j=json.loads((d/'result.json').read_text())
    assert j['f4_threshold_pass'] and j['term_count']<=1000000
    assert j['counts']['C1_VARIABLES']<=600
    assert sha(d/'c1.msolve')==j['artifacts']['c1.msolve']['sha256']
    scratch=d/'f4-tmp';scratch.mkdir(exist_ok=True)
    command=['/usr/bin/time','-v','-o',str(d/'f4.time'),'/usr/bin/timeout','-k','10s',str(a.seconds)+'s',
        str(a.msolve.resolve()),'-f',str(d/'c1.msolve'),'-o',str(d/'f4.basis'),
        '-g','2','-t',str(a.threads),'-v','2','--random-seed','0']
    env=dict(os.environ,TMPDIR=str(scratch));start=time.monotonic()
    utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    (d/'f4-command.json').write_text(json.dumps(dict(command=command,start_utc=utc,timeout_seconds=a.seconds),indent=2)+'\n')
    with (d/'f4.log').open('w') as log:
        cp=subprocess.run(command,stdout=log,stderr=log,env=env,cwd=d)
    elapsed=time.monotonic()-start
    logtext=(d/'f4.log').read_text(errors='replace')
    timetext=(d/'f4.time').read_text(errors='replace')
    basis=(d/'f4.basis').read_text(errors='replace') if (d/'f4.basis').exists() else ''
    # Preserve all potential degree/matrix lines for human interpretation;
    # do not infer a completed round from a partial last line.
    telemetry=[l for l in logtext.splitlines() if re.search(r'(?i)degree|matrix|[0-9]+\s*x\s*[0-9]+|reduce|\bdeg\b',l)]
    rss=re.search(r'Maximum resident set size \(kbytes\): (\d+)',timetext)
    basisdata='\n'.join(l for l in basis.splitlines() if not l.lstrip().startswith('#'))
    unit=bool(re.fullmatch(r'\s*\[\s*1\s*\]\s*:?\s*',basisdata))
    status='SIGNAL_MODULAR_UNIT_ONLY' if cp.returncode==0 and unit else (
        'COMPLETED_MODULAR_BASIS_REQUIRES_INSPECTION' if cp.returncode==0 and basis else
        'OPEN_F4_TIMEOUT' if cp.returncode==124 else 'OPEN_F4_NO_CERTIFIED_RESULT')
    result=dict(status=status,returncode=cp.returncode,elapsed_seconds=elapsed,start_utc=utc,
        end_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        peak_rss_kib=int(rss[1]) if rss else None,unit_pattern=unit,
        prime=j['prime'],variables=j['counts']['C1_VARIABLES'],generators=j['generator_count'],
        terms=j['term_count'],threads=a.threads,command=command,
        basis_bytes=(d/'f4.basis').stat().st_size if (d/'f4.basis').exists() else 0,
        telemetry_lines=telemetry,log_sha256=sha(d/'f4.log'),time_sha256=sha(d/'f4.time'))
    if (d/'f4.basis').exists():result['basis_sha256']=sha(d/'f4.basis')
    (d/'f4-result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='telemetry_lines'}))

if __name__=='__main__':main()
