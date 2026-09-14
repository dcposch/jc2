#!/usr/bin/env python3
"""Read-only process sampling; records observed bounds, never claims exact peaks."""
import datetime,json,os,time
from pathlib import Path

OUT=Path('/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/resource-observations.json')
OUT.parent.mkdir(exist_ok=True)
end=time.time()+145*60
records={}
while time.time()<end:
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    live=[]
    for p in Path('/proc').iterdir():
        if not p.name.isdigit(): continue
        try:
            args=(p/'cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace').strip()
            if not args.startswith('Singular -q '): continue
            cwd=os.readlink(p/'cwd')
            if 'char-degree-20260905' not in cwd and 'char-degree-20260905' not in args: continue
            status={}
            for line in (p/'status').read_text().splitlines():
                key,_,value=line.partition(':')
                if key in ('VmRSS','VmHWM','VmPeak','VmSize'): status[key]=int(value.split()[0])
            key=p.name
            r=records.setdefault(key,dict(pid=int(key),args=args,cwd=cwd,first_observed_utc=now))
            r.update(last_observed_utc=now,last_status_kib=status)
            for field,value in status.items(): r['max_observed_'+field+'_kib']=max(r.get('max_observed_'+field+'_kib',0),value)
            live.append(int(key))
        except (OSError,ValueError): pass
    OUT.write_text(json.dumps(dict(updated_utc=now,sample_seconds=5,scope='Observed /proc values; VmHWM is process high-water through last sample, possibly below final peak. Jobs ended before monitor are absent.',live_pids=live,records=list(records.values())),indent=2)+'\n')
    time.sleep(5)
