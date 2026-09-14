#!/usr/bin/env python3
"""Read-only bounded worker-process custody snapshot for this lane's drivers."""
import argparse,datetime,hashlib,json,subprocess
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
pgids={14494,14776,16594,16598,19599,19603,20429,21023,21245}
run=subprocess.run(['ps','-eo','pid,pgid,stat,etime,pcpu,rss,args'],text=True,capture_output=True,check=True)
lines=[];present=set();proc_stat={}
for line in run.stdout.splitlines()[1:]:
 fields=line.split(None,6)
 if len(fields)>=7 and int(fields[1]) in pgids:
  lines.append(line);present.add(int(fields[1]));p=Path('/proc')/fields[0]/'stat'
  try:proc_stat[fields[0]]=p.read_text()
  except FileNotFoundError:pass
out={'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'owned_process_groups':sorted(pgids),'present_groups':sorted(present),'absent_groups':sorted(pgids-present),'ps_columns':'pid pgid stat etime pcpu rss args','matching_ps_rows':lines,'read_only_proc_stat':proc_stat,'timing_note':'Launches used GNU timeout, not GNU time; process snapshots provide observed wall/runtime counters and do not invent exit statuses.'}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'captured_utc':out['captured_utc'],'present_groups':out['present_groups']}))
