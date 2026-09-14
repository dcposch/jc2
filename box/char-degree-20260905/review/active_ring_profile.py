#!/usr/bin/env python3
"""Bounded paired stage-0 first-division profile; not a chart verdict."""
import hashlib,json,os,re,resource,signal,subprocess,time
from pathlib import Path
from active_ring_backend import active_normalized_script

HERE=Path(__file__).resolve().parent
source=HERE.parent/'d108/d108_totalface_stage0.sing'
original=source.read_text()
lines=original.splitlines()
assert lines[0].startswith('ring R=0,(zz,tt,')
names=lines[0].split('ring R=0,(zz,tt,',1)[1].split('),',1)[0].split(',')
raw=lines[2]
assert raw.startswith('poly h=') and raw.endswith(';')
hexpr,tail=raw[len('poly h='):].split(';poly D=',1)
Dexpr,Cexpr=tail.split(';poly C=',1);Cexpr=Cexpr[:-1]
sourceI=next(l for l in lines if l.startswith('ideal I='))
assert sourceI=='ideal I=0;',sourceI
kwargs={'h_expr':hexpr,'D_expr':Dexpr,'C_expr':Cexpr,'residual_strings':[],
        'names':names,'k':36,'target':63,'face_expr':'zz^21*(1+zz)^6'}
active,mapping=active_normalized_script(**kwargs)
(HERE/'d108_stage0_active.sing').write_text(active)
(HERE/'d108_stage0_active.map.json').write_text(json.dumps(mapping,indent=2,sort_keys=True)+'\n')
(HERE/'d108-stage0-active-input.json').write_text(json.dumps(kwargs,indent=2)+'\n')

def prefix(text):
    cut=text.index('print("BEGIN_DIVIDE_vvU")')
    return text[:cut]+'print("FIRST_DIVISION_PROFILE_COMPLETE");quit;\n'
records=[];jobs=[];limit_kib=16*1024*1024;timeout=180
for mode,text in [('full',original),('active',active)]:
    script=prefix(text);path=HERE/f'profile_d108_stage0_{mode}.sing';path.write_text(script)
    log=path.with_suffix('.out');timing=path.with_suffix('.time.json')
    stream=log.open('w')
    def limits():resource.setrlimit(resource.RLIMIT_AS,(limit_kib*1024,limit_kib*1024))
    start=time.monotonic()
    # GNU time reports the child's maximum resident set without perturbing
    # its algebra. The parent owns and later stops the process group.
    proc=subprocess.Popen(['/usr/bin/time','-f','{"wall_seconds":%e,"max_rss_kib":%M,"exit_status":%x}',
                           '-o',str(timing),'Singular','-q',str(path)],stdout=stream,stderr=subprocess.STDOUT,
                          start_new_session=True,preexec_fn=limits)
    jobs.append((mode,path,script,proc,stream,start,log,timing))
    print(mode,'START',proc.pid,flush=True)
while jobs:
    for job in list(jobs):
        mode,path,script,proc,stream,start,log,timing=job
        timed=False
        if proc.poll() is None and time.monotonic()-start>timeout:
            timed=True;os.killpg(proc.pid,signal.SIGTERM)
            try:proc.wait(timeout=5)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
        if proc.poll() is None:continue
        stream.close();output=log.read_text();rawtime=timing.read_text() if timing.exists() else ''
        parsed=None
        for line in rawtime.splitlines():
            if line.startswith('{'):
                try:parsed=json.loads(line)
                except json.JSONDecodeError:pass
        record={'mode':mode,'returncode':proc.returncode,'timed_out':timed,
                'elapsed_seconds':round(time.monotonic()-start,3),'time':parsed,
                'complete':'FIRST_DIVISION_PROFILE_COMPLETE' in output,
                'last_marker':next((l for l in reversed(output.splitlines()) if l.startswith(('BEGIN_','END_'))),None),
                'errors':[l for l in output.splitlines() if l.lstrip().startswith('?')][:10],
                'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
                'log_sha256':hashlib.sha256(output.encode()).hexdigest()}
        records.append(record);jobs.remove(job);print(mode,record,flush=True)
    if jobs:time.sleep(1)
result={'field':'Q','purpose':'performance profile only, no chart outcome','stage':0,
        'active_generators':len(mapping['active_generator_order']),'full_generators':len(mapping['full_generator_order']),
        'address_space_limit_kib_per_job':limit_kib,'timeout_seconds':timeout,
        'source_script_sha256':hashlib.sha256(original.encode()).hexdigest(),'runs':records}
(HERE/'active-ring-profile.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
