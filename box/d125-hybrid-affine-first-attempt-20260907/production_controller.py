"""One ROOT-GREEN production dispatch; controller supplied over SSH stdin."""
from pathlib import Path
import hashlib,json,os,resource,subprocess,sys,time
W=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907');BOOT='bef732b9-38e5-4a9a-8f93-77203426d2b8'
GREEN='cdc48d29ec0037cceca2c75ab0712a40d49cf1004ec80b2a7ea513392d60567e'
REG='1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6'
PINS={'construct.py':'aa65e7104d3fcf5ad868eea952587a6841d784c6f9469c6c42ea2a02913ef264','replay.py':'06475a2a566b4ed617068d65f3a0473ef83c16e2cb357dcb959ee46716781c23','baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'}
SOURCE='/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl'
SOURCE_SHA='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
def save(p,v):
    with Path(p).open('x') as f:json.dump(v,f,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def ident(pid):
    p=Path('/proc')/str(pid);s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    return dict(pid=pid,pgid=int(s[2]),start_ticks=s[19],namespace=os.readlink(p/'ns/pid'),cgroup=(p/'cgroup').read_text(),boot=BOOT,argv=(p/'cmdline').read_bytes().replace(b'\0',b' ').decode())
def members(pgid):
    ids=[]
    for p in Path('/proc').iterdir():
        if not p.name.isdigit():continue
        try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
        except (FileNotFoundError,ProcessLookupError):continue
        if int(s[2])==pgid:ids.append(int(p.name))
    return sorted(ids)
os.chdir(W)
need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2' and Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54' and Path('/proc/sys/kernel/random/boot_id').read_text().strip()==BOOT,'host/boot')
need(time.time()<1788760260,'dispatch window ended')
need(hashlib.sha256(GREEN_BYTES).hexdigest()==GREEN,'new physical GREEN bytes')
need(sha(W/'REGISTRATION.md')==REG and {n:sha(W/n) for n in PINS}==PINS,'registered code drift')
need(sha(W/'run_capped.py')=='4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2','runner drift')
need(sha('/usr/bin/python3')=='a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223' and sha('/usr/bin/prlimit')=='17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069','binary drift')
need(sha(SOURCE)==SOURCE_SHA,'source pre-pin')
for n in ('construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr','pilot.telemetry.json','production.claim.json','production.launch.json','production.receipt.json','engineering/rss.authority.json','engineering/ROOT-GREEN.md'):need(not os.path.lexists(W/n),'occupied '+n)
save(W/'production.claim.json',dict(controller=ident(os.getpid()),utc=time.time(),green=GREEN,registration=REG,pins=PINS,source_sha256=SOURCE_SHA))
for name,dest,pin in [('authority.json','engineering/rss.authority.json','d3a16840b13b51bb503c26416cab1fa79c316599acf1e0d4b9fb9ffb8e0e1f17'),('ROOT-GREEN.md','engineering/ROOT-GREEN.md','12ef766b820b4ef486b4b3286eb0d46f2b41e5630488477f67170874cc2d8a36')]:
    need(sha(W/name)==pin and not os.path.lexists(W/dest),'archive boundary');os.rename(W/name,W/dest);need(sha(W/dest)==pin,'archive post-pin')
with (W/'ROOT-GREEN.md').open('xb') as f:f.write(GREEN_BYTES);f.flush();os.fsync(f.fileno())
caps=dict(wall_seconds=300,cpu_seconds=300,address_bytes=4294967296,file_bytes=134217728,polynomial_terms=100000,multiply_pairs=1000000,retained_terms=1000000,coefficient_bits=4096)
a=dict(schema='jc2.hybrid-affine-authority/v1',root_green=True,construction_only=True,gates_accepted=True,engineering_control_only=False,mode='normalized-hermite-only-slice',job='d125-hybrid-affine-first-attempt-20260907/production',boot_id=BOOT,registration_sha256=REG,root_green_sha256=GREEN,code_sha256=PINS,source_path=SOURCE,source_sha256=SOURCE_SHA,desk_sha256='b33d6944976ac934535bcc516bae82c738cd2e957665bfffb2325ec63170aa5a',normalization_gate_sha256='53f78754d8e567e145db4038f6f5b39f2f9a56c462178f20b1e94a2f6f0e7e10',hybrid_gate_sha256='bff1b2073c3fb878458de346fa1b3c87ab378ce5b7a5320e3a634b7b7da0950c',code_gate_sha256='83bd439aa52af686514dcdd6aa4fa400d099abccc8c5d5b5967b208777e47fb4',caps=caps,expires_unix=time.time()+299.5)
save(W/'authority.json',a);spawn=time.time()
cmd=['/usr/bin/prlimit','--fsize=134217728:134217728','--core=0:0','--','/usr/bin/python3','-I','-B',str(W/'run_capped.py'),'--wall-seconds','300','--cpu-seconds','300','--rss-bytes','4294967296','--rss-sample-seconds','0.05','--term-grace-seconds','0.25','--cwd',str(W),'--stdout-file',str(W/'pilot.stdout'),'--stderr-file',str(W/'pilot.stderr'),'--telemetry-file',str(W/'pilot.telemetry.json'),'--','/usr/bin/python3','-E','-s','-B',str(W/'construct.py'),str(W/'authority.json')]
resource.setrlimit(resource.RLIMIT_FSIZE,(134217728,134217728));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
p=subprocess.Popen(cmd,cwd=W,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
launch=dict(controller=ident(os.getpid()),runner=ident(p.pid),argv=cmd,spawn_unix=spawn,expires_unix=a['expires_unix'],remaining_at_spawn=a['expires_unix']-spawn,authority_sha256=sha(W/'authority.json'))
for _ in range(50):
    try:children=(Path('/proc')/str(p.pid)/'task'/str(p.pid)/'children').read_text().split()
    except FileNotFoundError:break
    if children:
        try:launch['payload']=ident(int(children[0]));break
        except FileNotFoundError:pass
    time.sleep(.01)
save(W/'production.launch.json',launch);print(json.dumps(dict(type='LIVE_METADATA',**launch)),flush=True)
try:out,err=p.communicate(timeout=305)
except subprocess.TimeoutExpired:
    p.terminate();out,err=p.communicate(timeout=5);raise RuntimeError('unexpected runner wait timeout; no retry')
t=json.loads((W/'pilot.telemetry.json').read_bytes())
until=time.monotonic()+2
while members(t['pgid']) and time.monotonic()<until:time.sleep(.05)
receipt=dict(utc=time.time(),runner_rc=p.returncode,runner_stdout=out,runner_stderr=err,telemetry=t,group_members_after=members(t['pgid']),runner_absent=not Path('/proc',str(p.pid)).exists(),source_post_sha256=sha(SOURCE),post_pins={n:sha(W/n) for n in PINS},files={n:dict(bytes=(W/n).stat().st_size,sha256=sha(W/n)) for n in ('construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr') if (W/n).exists()})
save(W/'production.receipt.json',receipt)
need(not receipt['group_members_after'] and receipt['runner_absent'],'terminal group gap')
print(json.dumps(dict(type='TERMINAL_METADATA',runner_rc=p.returncode,status=t['status'],child_returncode=t['child_returncode'],pgid=t['pgid'],files=receipt['files'])),flush=True)
