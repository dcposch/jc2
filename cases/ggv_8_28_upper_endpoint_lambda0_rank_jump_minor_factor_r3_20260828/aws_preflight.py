#!/usr/bin/env python3
"""Fail-closed preflight for one r3 residual-minor worker."""

from __future__ import annotations
import argparse, hashlib, json, os, shutil, sys, time
from pathlib import Path


def item(host, instance, product, nproc, memory, tag): return {"host":host,"instance":instance,"product":product,"nproc":nproc,"min_mem_gib":memory,"tag":tag}
LANES={
"c8":item("ip-172-30-0-34","i-02cb2b4a379ffcc64","r6i.4xlarge",16,110,"ggv_lambda0_minor_c8_r3_20260828T153000Z_r6a"),
"c8_q1":item("ip-172-30-0-34","i-02cb2b4a379ffcc64","r6i.4xlarge",16,110,"ggv_lambda0_minor_c8_q1_r3_20260828T153000Z_r6a2"),
"q1":item("ip-172-30-0-106","i-0f089e64c378f5da3","r6i.4xlarge",16,110,"ggv_lambda0_minor_q1_r3_20260828T153000Z_r6b"),
"p":item("ip-172-30-0-150","i-040b7a1c2ed72d4cc","r6i.4xlarge",16,110,"ggv_lambda0_minor_p_r3_20260828T153000Z_r6c"),
"c8p02":item("ip-172-30-0-131","i-0793fef088620f2c1","r6i.4xlarge",16,110,"ggv_lambda0_minor_c8p02_r3_20260828T153000Z_r6e"),
"q1p02":item("ip-172-30-0-79","i-0fdde459d4ab36b95","r6i.4xlarge",16,110,"ggv_lambda0_minor_q1p02_r3_20260828T153000Z_r6f"),
"q1p03":item("ip-172-30-0-248","i-0c73ac7019fe3eef2","r6i.4xlarge",16,110,"ggv_lambda0_minor_q1p03_r3_20260828T153000Z_r6g"),
"triple02":item("ip-172-30-0-220","i-0d71d73e0fe8a8cae","r6i.4xlarge",16,110,"ggv_lambda0_minor_triple02_r3_20260828T153000Z_r6h"),
"triple03":item("ip-172-30-0-128","i-072ccec67b0933088","r6i.4xlarge",16,110,"ggv_lambda0_minor_triple03_r3_20260828T153000Z_r6i")}
SINGULAR_SHA256="90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4"
def stat(pid):
 raw=Path(f"/proc/{pid}/stat").read_text(); f=raw[raw.rfind(")")+2:].split(); return {"ppid":int(f[1]),"pgrp":int(f[2]),"session":int(f[3]),"starttime":int(f[19])}
def ancestors():
 out={os.getpid()}; p=os.getpid()
 while p>1:
  try:p=stat(p)["ppid"]
  except (FileNotFoundError,PermissionError,ProcessLookupError):break
  out.add(p)
 return out
def meminfo():
 out={}
 for line in Path('/proc/meminfo').read_text().splitlines(): k,v=line.split(':',1); out[k]=int(v.split()[0])
 return out
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as s:
  for b in iter(lambda:s.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def conflicts(run_dir):
 own=ancestors(); tokens=("python","sage","singular","msolve","magma","/home/ubuntu/jobs/","timeout","prlimit"); out=[]
 for e in Path('/proc').iterdir():
  if not e.name.isdigit() or int(e.name) in own:continue
  try:
   st={x.split(':',1)[0]:x.split(':',1)[1].strip() for x in (e/'status').read_text().splitlines() if ':' in x}
   if int(st['Uid'].split()[0])!=os.getuid():continue
   cmd=(e/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace'); rss=int(st.get('VmRSS','0 kB').split()[0])
  except (FileNotFoundError,PermissionError,ProcessLookupError,KeyError,ValueError):continue
  if str(run_dir) in cmd:continue
  if rss>=1024*1024 or any(t in cmd.lower() for t in tokens):out.append({'pid':int(e.name),'rss_kib':rss,'command':cmd})
 return out
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--run-dir',type=Path,required=True); ap.add_argument('--job-tag',required=True); ap.add_argument('--component',choices=sorted(LANES),required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
 run=a.run_dir.resolve(); exp=LANES[a.component]; mem=meminfo(); disk=shutil.disk_usage(run).free; singular=Path(shutil.which('Singular') or ''); active=conflicts(run)
 facts={'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'platform':sys.platform,'host':os.uname().nodename,'vendor':Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),'product':Path('/sys/class/dmi/id/product_name').read_text().strip(),'instance':Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),'nproc':os.cpu_count(),'job_tag':a.job_tag,'component':a.component,'run_dir':str(run),'mem_available_kib':mem['MemAvailable'],'swap_total_kib':mem['SwapTotal'],'swap_free_kib':mem['SwapFree'],'disk_available_bytes':disk,'singular':str(singular),'singular_sha256':sha(singular) if singular.is_file() else None,'conflicts':active}
 checks={'linux':sys.platform.startswith('linux'),'vendor':facts['vendor']=='Amazon EC2','product':facts['product']==exp['product'],'host':facts['host']==exp['host'],'instance':facts['instance']==exp['instance'],'nproc':facts['nproc']==exp['nproc'],'job_tag':a.job_tag==exp['tag']==run.name and os.environ.get('AWS_RUN_TAG')==exp['tag'] and os.environ.get('AWS_RUN_COMPONENT')==a.component,'memory':mem['MemAvailable']>=exp['min_mem_gib']*1024*1024,'zero_swap':mem['SwapTotal']==0 and mem['SwapFree']==0,'disk':disk>=50*1024**3,'singular':facts['singular_sha256']==SINGULAR_SHA256,'idle':not active}
 facts['checks']=checks; facts['pass']=all(checks.values()); a.output.write_text(json.dumps(facts,indent=2,sort_keys=True)+'\n'); print(json.dumps(facts,sort_keys=True))
 if not facts['pass']:raise SystemExit(40)
if __name__=='__main__':main()

