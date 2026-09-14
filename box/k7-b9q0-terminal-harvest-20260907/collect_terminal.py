"""Read-only K7 terminal custody collector; supplied to exact worker SSH stdin.
Never reads a job artifact while a matching process remains live. No CAS,
signal, restart, cap edit, expansion, or mathematical verdict.
"""
import datetime, hashlib, json, os, resource, sys
from pathlib import Path
ROOT=Path('/home/ubuntu/k7-b9q0-longsolve')
BOOT='8b9dfc2b-8ec9-4d8b-953a-281dc56ee218'
JOBS={
 'a_slimgb_dp':'308e6198ba6c9f8ec456be78dec500bed123af181709618f0afb754c18de3cfc',
 'b_std_wp':'4435caf9b8eb5f5eaf294dcb8fb884f7a545de39ee94d2d98bfe7245816d014d',
 'c_tri_qv69_slimgb':'50dee16947b02f7c24379d06d07a8b2c4fe6a86e9a35163cec11349269428cea'}
PINS={'runner.sh':'4165a5b8989043b6efbcf5034d27b91c625584139688a85423fd86c96a776f9b',
 'watchdog.py':'a724775f3c479f99152ae42e6a8ae5506d8af24843cb726cd8a1865982e49c52',
 'mkjobs.py':'3388baaf0f4932341e84c3903ef033701698b47ca57733d6b37ff59e81694603',
 'chart/K7_B9_Q0_p0.ms':'15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275'}
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
def need(ok,msg):
    if not ok: raise ValueError(msg)
def info(p):
    h=hashlib.sha256();n=0
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b);n+=len(b)
    return dict(bytes=n,sha256=h.hexdigest())
def read_small(p):
    need(p.is_file() and p.stat().st_size<=65536,'missing/large receipt '+str(p))
    return p.read_text()
need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0e5c65e66b8dc4dfc','instance')
need(Path('/proc/sys/kernel/random/boot_id').read_text().strip()==BOOT,'boot')
def members():
    found=[]
    for entry in Path('/proc').iterdir():
        if not entry.name.isdigit() or int(entry.name)==os.getpid():continue
        try:
            s=(entry/'stat').read_text().rsplit(') ',1)[1].split()
            argv=(entry/'cmdline').read_bytes()
        except (FileNotFoundError,ProcessLookupError):continue
        pid=int(entry.name);pgid=int(s[2])
        if pid in (3446,3447,3448,3462,3463,3464) or pgid in (3446,3447,3448,3459,3460,3461) or str(ROOT).encode() in argv:
            found.append(dict(pid=pid,ppid=int(s[1]),pgid=pgid,state=s[0],start_ticks=s[19],argv=argv.replace(b'\0',b' ').decode(errors='replace')))
    return found
before=members()
if before:
    print(json.dumps(dict(status='LIVE_NO_ARTIFACT_READ',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),members=before)))
    sys.exit(75)
# Receipts first, before output or input streams.
receipts={}
for job in JOBS:
    d=ROOT/'runs'/job
    texts={n:read_small(d/n) for n in ('runner.rc','start.utc','end.utc','time.txt','caprun.json','runner.log')}
    cap=json.loads(texts['caprun.json'])
    need(cap.get('running') is False,'watchdog receipt not terminal '+job)
    need(cap.get('cap_kib')==73400320 and cap.get('poll_interval_s')==15,'cap drift '+job)
    need(texts['runner.rc'].strip().isdigit(),'runner rc framing '+job)
    need('RUNNER_DONE '+job+' rc='+texts['runner.rc'].strip() in texts['runner.log'],'runner completion '+job)
    receipts[job]=dict(texts=texts,caprun=cap,runner_rc=int(texts['runner.rc'].strip()))
files={}; framing={}
for rel,h in PINS.items():
    files[rel]=info(ROOT/rel);need(files[rel]['sha256']==h,'input pin '+rel)
for rel in ('chart/K7_B9_Q0_p0.json','jobs-manifest.json'):
    files[rel]=info(ROOT/rel)
for job,h in JOBS.items():
    d=ROOT/'runs'/job
    for name in ('runner.rc','start.utc','end.utc','time.txt','caprun.json','runner.log','stdout.txt','stderr.txt','job.sing'):
        rel='runs/'+job+'/'+name;files[rel]=info(ROOT/rel)
        need(files[rel]['bytes']<=64<<20,'large file requires separate bounded custody '+rel)
    need(files['runs/'+job+'/job.sing']['sha256']==h,'job input pin '+job)
    # Literal framing only, never parse rational polynomials or run them.
    counts={};body=bytearray();inside=False;body_large=False
    with (d/'stdout.txt').open('rb') as f:
        for line in f:
            token=line.strip()
            if token.startswith(b'CERT__'):
                key=token.decode('ascii',errors='replace');counts[key]=counts.get(key,0)+1
            if token==b'CERT__GB_BEGIN':inside=True;continue
            if token==b'CERT__GB_END':inside=False;continue
            if inside:
                if len(body)+len(line)<=1024:body.extend(line)
                else:body_large=True
    exact=(receipts[job]['runner_rc']==0 and not receipts[job]['caprun']['rss_killed']
        and all(counts.get(s)==1 for s in ('CERT__GB_BEGIN','CERT__GB_END','CERT__GB_SIZE 1','CERT__UNIT 1','CERT__DONE 1'))
        and not any('LEADS_ONLY' in s for s in counts) and not inside and not body_large and bytes(body)==b'1\n')
    framing[job]=dict(markers=counts,body_prefix_hex=bytes(body).hex(),body_over_1024=body_large,
        unit_framing_candidate=exact,scope='literal framing only; no mathematical certificate replay')
after=members();need(not after,'matching process reappeared')
print(json.dumps(dict(status='TERMINAL_CUSTODY_ONLY',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    instance='i-0e5c65e66b8dc4dfc',boot=BOOT,root=str(ROOT),members_before=before,members_after=after,
    receipts=receipts,files=files,framing=framing,no_extra_arithmetic=True,no_worker_control=True),sort_keys=True))
