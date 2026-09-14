"""One authorized engineering batch over SSH stdin; never a source reader/main."""
from pathlib import Path
import datetime,hashlib,json,os,resource,subprocess,sys,time
W=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907');E=W/'engineering'
BOOT='bef732b9-38e5-4a9a-8f93-77203426d2b8'
GREEN='12ef766b820b4ef486b4b3286eb0d46f2b41e5630488477f67170874cc2d8a36'
REG='1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    with Path(p).open('x') as f:json.dump(v,f,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def ident(pid):
    p=Path('/proc')/str(pid);s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    return dict(pid=pid,pgid=int(s[2]),start_ticks=s[19],cgroup=(p/'cgroup').read_text(),namespace=os.readlink(p/'ns/pid'),boot=BOOT)
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
need(sha(W/'ROOT-GREEN.md')==GREEN and sha(W/'REGISTRATION.md')==REG,'physical authority/registration drift')
need(time.time()<1788759540,'GREEN dispatch window expired')
need(sha(E/'host_control.py')=='3ea4ba7cd62600ba351a27640ee44815adc70fbd27e18729c180f2a550f215ba','control pin')
sys.path.insert(0,str(E));import host_control as H
host=H.observed();H.host_check(host);H.outputs_absent(W)
pins={n:sha(W/n) for n in H.PINS};need(pins==H.PINS,'frozen payload pins')
engineering={'host_control.py':sha(E/'host_control.py'),'run_capped.py':sha(W/'run_capped.py')}
need(engineering['run_capped.py']==H.RUNNER,'CAPRUN pin')
need(sha('/usr/bin/python3')=='a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223','Python pin')
need(sha('/usr/bin/prlimit')=='17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069','prlimit pin')
resource.setrlimit(resource.RLIMIT_FSIZE,(134217728,134217728));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
save(E/'controller.claim.json',dict(controller=ident(os.getpid()),host=host,pins=pins,engineering=engineering,registration=REG,green=GREEN,source_access=False))
start=time.monotonic();deadline=start+30;jobs=[];status='INCOMPLETE'
try:
    for label,rss in [('authorize',536870912),('rss',67108864)]:
        need(time.monotonic()<deadline-11 and time.time()<1788759540,'dispatch deadline')
        H.outputs_absent(W);ap=W/'authority.json';need(not os.path.lexists(ap),'fresh authority path required')
        a=dict(schema='jc2.hybrid-affine-authority/v1',engineering_control_only=True,engineering_control=label,
               root_green=True,construction_only=True,gates_accepted=True,mode='normalized-hermite-only-slice',
               job='d125-hybrid-affine-first-attempt-20260907/engineering/'+label,boot_id=BOOT,
               source_path='/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl',
               source_sha256='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac',
               desk_sha256='b33d6944976ac934535bcc516bae82c738cd2e957665bfffb2325ec63170aa5a',
               normalization_gate_sha256='53f78754d8e567e145db4038f6f5b39f2f9a56c462178f20b1e94a2f6f0e7e10',
               hybrid_gate_sha256=H.MATH,code_gate_sha256='83bd439aa52af686514dcdd6aa4fa400d099abccc8c5d5b5967b208777e47fb4',
               registration_sha256=REG,root_green_sha256=GREEN,code_sha256=pins,engineering_code_sha256=engineering,caps=H.CAPS,
               expires_unix=time.time()+9.5)
        save(ap,a);issued_sha=sha(ap);spawn=time.time()
        cmd=['/usr/bin/prlimit','--fsize=134217728:134217728','--core=0:0','--','/usr/bin/python3','-I','-B',str(W/'run_capped.py'),
             '--wall-seconds','10','--cpu-seconds','10','--rss-bytes',str(rss),'--rss-sample-seconds','0.05','--term-grace-seconds','0.25','--cwd',str(W),
             '--stdout-file',str(E/(label+'.stdout')),'--stderr-file',str(E/(label+'.stderr')),'--telemetry-file',str(E/(label+'.telemetry.json')),
             '--','/usr/bin/python3','-I','-B',str(E/'host_control.py'),label]
        p=subprocess.Popen(cmd,cwd=W,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        launch=dict(label=label,argv=cmd,controller=ident(os.getpid()),runner=ident(p.pid),spawn_unix=spawn,expires_unix=a['expires_unix'],remaining_at_spawn=a['expires_unix']-spawn,authority_sha256=issued_sha)
        save(E/(label+'.launch.json'),launch);print(json.dumps(dict(type='LIVE_METADATA',**launch)),flush=True)
        try:out,err=p.communicate(timeout=14)
        except subprocess.TimeoutExpired:
            p.terminate();out,err=p.communicate(timeout=5);raise RuntimeError('unexpected CAPRUN wait timeout; no retry')
        t=json.loads((E/(label+'.telemetry.json')).read_bytes())
        until=time.monotonic()+2
        while members(t['pgid']) and time.monotonic()<until:time.sleep(.05)
        receipt=dict(label=label,runner_rc=p.returncode,runner_stdout=out,runner_stderr=err,telemetry=t,group_members_after=members(t['pgid']),runner_absent=not Path('/proc',str(p.pid)).exists(),payload_stdout=(E/(label+'.stdout')).read_text(),payload_stderr=(E/(label+'.stderr')).read_text())
        save(E/(label+'.receipt.json'),receipt);jobs.append(receipt)
        need(not receipt['group_members_after'] and receipt['runner_absent'] and not t['error'],'terminal cleanup gap')
        need(err=='' and receipt['payload_stderr']=='','unexpected engineering stderr')
        if label=='authorize':
            value=json.loads(receipt['payload_stdout'])
            need(p.returncode==0 and t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and value['status']=='REAL_AUTHORIZE_AND_TINY_NORMALIZED_CONTROL_PASS' and value['source_access'] is False,'authorize failed')
            dest=E/'authorize.authority.json';need(not os.path.lexists(dest) and sha(ap)==issued_sha,'spent authority custody')
            os.rename(ap,dest);need(sha(dest)==issued_sha,'moved authority hash')
        else:
            d=json.loads((E/'rss-descendant.identity.json').read_bytes());term=t['termination']
            need(p.returncode==125 and t['status']=='RESOURCE_CAP' and t['resource']=='rss' and term['term_sent'] and term['kill_sent'] and term['leader_reaped'] and term['cleanup_complete'] and d['pgid']==t['pgid'],'RSS failed')
        need(time.monotonic()<deadline,'engineering30-second batch cap')
    status='ENGINEERING_ONLY_PASS'
finally:
    save(E/'batch-result.json',dict(status=status,elapsed_seconds=time.monotonic()-start,jobs=jobs,source_access=False,construction_invoked=False,
          post_pins={**{n:sha(W/n) for n in H.PINS},'host_control.py':sha(E/'host_control.py'),'run_capped.py':sha(W/'run_capped.py')},
          construction_absent=not os.path.lexists(W/'construction.jsonl'),replay_absent=not os.path.lexists(W/'replay-result.json')))
print(json.dumps(dict(type='TERMINAL_METADATA',status=status,elapsed_seconds=time.monotonic()-start,groups=[j['telemetry']['pgid'] for j in jobs])),flush=True)
