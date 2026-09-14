"""One authorized two-control batch, supplied over SSH stdin; no source reader."""
from pathlib import Path
import datetime,hashlib,json,os,resource,subprocess,sys,time
W=Path('/home/ubuntu/d125-parity-compression-pilot-20260907');E=W/'engineering'
BOOT='1a830d1e-1fa2-47f3-98bc-8c26c8cb8453'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    with Path(p).open('x') as f:json.dump(v,f,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def ident(pid):
    p=Path('/proc')/str(pid);s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    return dict(pid=pid,pgid=int(s[2]),start_ticks=s[19],cgroup=(p/'cgroup').read_text(),
                namespace=os.readlink(p/'ns/pid'),boot=BOOT)
def members(pgid):
    out=[]
    for p in Path('/proc').iterdir():
        if not p.name.isdigit():continue
        try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
        except (FileNotFoundError,ProcessLookupError):continue
        if int(s[2])==pgid:out.append(int(p.name))
    return sorted(out)
os.chdir(W)
need(Path('/proc/sys/kernel/random/boot_id').read_text().strip()==BOOT,'boot drift')
need(sha(E/'host_control.py')=='f91a2c250689330a6d8155a5704ca1b703179cb342df686d683442c858798860','control pin')
sys.path.insert(0,str(E));import host_control as H
host=H.observed();need(host['hostname']=='ip-172-30-0-56','hostname drift')
pins={k:sha(W/k) for k in H.PINS};need(pins==H.PINS,'payload pin drift')
pins['host_control.py']=sha(E/'host_control.py')
reg=sha(W/'REGISTRATION.md');need(reg=='9435f425ddd135846480dd1cdb08674de3b376803a1f73e93804a546c5b5d107','registration drift')
need(sha('/usr/bin/prlimit')=='17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069','prlimit drift')
need(sha('/usr/bin/python3')=='a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223','python drift')
save(E/'batch-pre.json',dict(host=host,controller=ident(os.getpid()),pins=pins,registration=reg,source_access=False))
start=time.monotonic();deadline=start+30;jobs=[];status='INCOMPLETE'
try:
    for label,rss in [('authorize',512*1024**2),('rss',64*1024**2)]:
        need(time.monotonic()<deadline-11,'batch deadline before control')
        a=dict(schema='jc2.d125-parity-engineering-authority/v1',engineering_control_only=True,
               control=label,root_green=True,construction_only=True,mode='slice',
               job='d125-parity-engineering-20260907/'+label,boot_id=BOOT,
               symmetry_gate_accepted=True,symmetry_gate_sha256=H.GATE,
               symmetry_sha256='9bed554644b1bd3c881ba4e289ea0950601ed6141677a45152577442fd477b12',
               source_sha256=H.SOURCE,registration_sha256=reg,code_sha256=pins,caps=H.CAPS,
               expires_unix=time.time()+9.5)
        ap=E/(label+'.authority.json');save(ap,a)
        cmd=['/usr/bin/prlimit','--fsize=134217728:134217728','--core=0:0','--',
             '/usr/bin/python3','-I','-B',str(W/'run_capped.py'),'--wall-seconds','10','--cpu-seconds','10',
             '--rss-bytes',str(rss),'--rss-sample-seconds','0.05','--term-grace-seconds','0.25','--cwd',str(W),
             '--stdout-file',str(E/(label+'.stdout')),'--stderr-file',str(E/(label+'.stderr')),
             '--telemetry-file',str(E/(label+'.telemetry.json')),'--','/usr/bin/python3','-I','-B',
             str(E/'host_control.py'),label,str(ap)]
        p=subprocess.Popen(cmd,cwd=W,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        launch=dict(label=label,argv=cmd,runner_identity=ident(p.pid),hostname=host['hostname'],
                    utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),authority_sha256=sha(ap))
        save(E/(label+'.launch.json'),launch)
        out,err=p.communicate(timeout=14)
        t=json.loads((E/(label+'.telemetry.json')).read_bytes())
        end=time.monotonic()+2
        while members(t['pgid']) and time.monotonic()<end:time.sleep(.05)
        receipt=dict(label=label,runner_rc=p.returncode,runner_stdout=out,runner_stderr=err,
                     telemetry=t,group_members_after=members(t['pgid']),runner_absent=not Path('/proc',str(p.pid)).exists())
        jobs.append(receipt);save(E/(label+'.receipt.json'),receipt)
        need(not receipt['group_members_after'] and receipt['runner_absent'] and not t['error'],'cleanup gap')
        need((E/(label+'.stderr')).read_bytes()==b'' and err=='','unexpected stderr')
        if label=='authorize':
            actual=json.loads((E/(label+'.stdout')).read_bytes())
            need(p.returncode==0 and t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and
                 actual['status']=='AUTHORIZATION_AND_TINY_Q_ONLY_PASS' and actual['source_read'] is False,
                 'authorize control failed')
        else:
            d=json.loads((E/'rss-descendant.identity.json').read_bytes());term=t['termination']
            need(p.returncode==125 and t['status']=='RESOURCE_CAP' and t['resource']=='rss' and
                 term['term_sent'] and term['kill_sent'] and term['leader_reaped'] and term['cleanup_complete']
                 and d['pgid']==t['pgid'],'RSS control failed')
        need(time.monotonic()<deadline,'combined batch exceeded30 seconds')
    status='ENGINEERING_ONLY_PASS'
finally:
    save(E/'batch-result.json',dict(status=status,elapsed_seconds=time.monotonic()-start,
          source_access=False,construction_invoked=False,jobs=jobs,
          post_pins={**{k:sha(W/k) for k in H.PINS},'host_control.py':sha(E/'host_control.py')},
          production_outputs_absent=all(not (W/n).exists() for n in ['authority.json','construction.jsonl','replay-result.json'])))
print(json.dumps(dict(status=status,elapsed_seconds=time.monotonic()-start,
                     groups=[j['telemetry']['pgid'] for j in jobs],source_access=False)))
