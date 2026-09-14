"""Future root-operated ONE tiny engineering control; never production authority."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,platform,resource,subprocess,sys,time,uuid
W=Path('/home/ubuntu/d125-hybrid81-exact-solver-20260907');ENG=W/'engineering'
ENGINE='8d8da939caf88c75ae167fa6cf862011c76a593c105c88970efcd9baf16c7cdf'
REG='364a5d8c57a967d6dc3467db13eb0b19ba6c7924a573dc5b3ea67da7eb6f1ee5'
PINS={'driver.py':'ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a',
 'exact.py':'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
 'hybrid.py':'c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3',
 'engine.py':ENGINE,'run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2',
 'engineering/REGISTRATION.md':REG,
 'engineering/tiny-engine-fixture.jsonl':'d00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf'}
BIN={'/usr/bin/Singular':'90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4',
 '/usr/bin/python3':'a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223',
 '/usr/bin/prlimit':'17064f67e650d6152a6902b013aab496b54c87587c8eea6f5023aafee6154069'}
def need(ok,msg):
 if not ok:raise ValueError(msg)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
 with Path(p).open('x') as f:json.dump(v,f,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def valid_digest(s):return isinstance(s,str) and len(s)==64 and s!='0'*64 and all(c in '0123456789abcdef' for c in s)
def validate(op,boot,green,selfpin,accepted,until,now):
 need(op in ('hybrid','alarm'),'fixed engineering operation')
 need(str(uuid.UUID(boot))==boot and boot!='00000000-0000-0000-0000-000000000000','fresh boot required')
 need(valid_digest(green) and valid_digest(selfpin),'physical root GREEN/controller pins required')
 need(0<until-now<=60,'fresh bounded dispatch window')
 need((op=='hybrid' and accepted is None) or (op=='alarm' and valid_digest(accepted)),'alarm needs separately accepted hybrid receipt')
def vector(op):
 need(op in ('hybrid','alarm'),'fixed operation')
 return ['/usr/bin/python3','-I','-B',str(W/'run_capped.py'),'--wall-seconds','10','--cpu-seconds','10',
 '--rss-bytes','536870912','--rss-sample-seconds','0.05','--term-grace-seconds','0.25','--cwd',str(W),
 '--stdout-file',str(ENG/(op+'.stdout')),'--stderr-file',str(ENG/(op+'.stderr')),
 '--telemetry-file',str(ENG/(op+'.telemetry.json')),'--','/usr/bin/python3','-I','-B',str(W/'engine.py'),op,str(ENG/(op+'.authority.json'))]
def compare_vector(op,expected):need([s.encode('ascii') for s in vector(op)]==expected,'frozen parent argv drift')
def ident(pid):
 p=Path('/proc')/str(pid);s=(p/'stat').read_text().rsplit(') ',1)[1].split()
 return {'pid':pid,'pgid':int(s[2]),'start_ticks':s[19],'namespace':os.readlink(p/'ns/pid'),
 'cgroup':(p/'cgroup').read_text(),'argv':[s.decode() for s in (p/'cmdline').read_bytes().split(b'\0')[:-1]],
 'boot':Path('/proc/sys/kernel/random/boot_id').read_text().strip()}
def members(group):
 out=[]
 for p in Path('/proc').iterdir():
  if not p.name.isdigit():continue
  try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
  except (FileNotFoundError,ProcessLookupError):continue
  if int(s[2])==group:out.append(int(p.name))
 return sorted(out)
def main():
 p=argparse.ArgumentParser();p.add_argument('operation',choices=['hybrid','alarm']);p.add_argument('--boot',required=True)
 p.add_argument('--green-sha256',required=True);p.add_argument('--controller-sha256',required=True)
 p.add_argument('--dispatch-before',required=True,type=float);p.add_argument('--accepted-hybrid-receipt')
 q=p.parse_args();op=q.operation
 validate(op,q.boot,q.green_sha256,q.controller_sha256,q.accepted_hybrid_receipt,q.dispatch_before,time.time())
 need(Path.cwd().resolve()==W and Path(__file__).resolve()==W/'controller.py','registered controller/cwd only')
 need(platform.system()=='Linux' and Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2'
  and Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54','exact Linux EC2')
 need(Path('/proc/sys/kernel/random/boot_id').read_text().strip()==q.boot,'boot drift')
 need(digest(__file__)==q.controller_sha256 and digest(ENG/'ROOT-GREEN.md')==q.green_sha256,'physical GREEN/controller drift')
 need({n:digest(W/n) for n in PINS}==PINS and {n:digest(n) for n in BIN}==BIN,'frozen code/fixture/binary pins')
 sys.path.insert(0,str(W));import engine as E;import driver as D
 compare_vector(op,E.expected_parent_argv(op))
 paths={s:ENG/(op+'.'+s) for s in ('authority.json','claim.json','stdout','stderr','telemetry.json','launch.json','receipt.json','sing','identity.json')}
 need(not any(os.path.lexists(v) for v in paths.values()),'exclusive fresh operation paths')
 if op=='hybrid':need(not os.path.lexists(ENG/'alarm.authority.json'),'future alarm authority already exists')
 else:
  rp=ENG/'hybrid.receipt.json';need(digest(rp)==q.accepted_hybrid_receipt,'accepted hybrid receipt drift')
  h=json.loads(rp.read_bytes());need(h.get('status')=='ENGINEERING_HYBRID_PASS' and h.get('boot')==q.boot,'hybrid prerequisite')
 resource.setrlimit(resource.RLIMIT_FSIZE,(67108864,67108864));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 host=D.observed_host();host['hostname']=platform.node()
 save(paths['claim.json'],{'controller':ident(os.getpid()),'host':host,'code':PINS,'binaries':BIN,'green':q.green_sha256,'source_access':False})
 now=time.time();need(now<q.dispatch_before,'dispatch expired before authority')
 iso=lambda t:datetime.datetime.fromtimestamp(t,datetime.timezone.utc).isoformat()
 a={'schema':'jc2.d125-hybrid81-solver-authority/v1','root_green':True,'mode':'engineering_control',
 'job_id':'d125-hybrid81-engineering/'+op,'instance_id':D.INSTANCE,'cwd':str(W),'boot_id':q.boot,
 'pins':D.pins(),'caps':D.CAPS,'started_utc':iso(now),'deadline_utc':iso(now+9.5),
 'engineering':{'operation':op,'helper_sha256':ENGINE,'fixture_sha256':E.FIXTURE_SHA,'root_green_sha256':q.green_sha256}}
 D.authority_check(a,'control',host|{'now':now},D.pins());E.control_binding(a,op,ENGINE,q.green_sha256)
 save(paths['authority.json'],a);authority_sha=digest(paths['authority.json'])
 command=['/usr/bin/prlimit','--fsize=67108864:67108864','--core=0:0','--']+vector(op)
 compare_vector(op,E.expected_parent_argv(op));need(time.time()<q.dispatch_before,'dispatch expired')
 child=subprocess.Popen(command,cwd=W,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 live_runner=live_child=None;capture_end=time.monotonic()+1.5
 while child.poll() is None and time.monotonic()<capture_end:
  try:
   candidate=ident(child.pid)
   if candidate['argv']==vector(op):live_runner=candidate
   if paths['identity.json'].is_file():
    hi=json.loads(paths['identity.json'].read_bytes());candidate=ident(hi['pid'])
    if candidate['start_ticks']==hi['start_ticks'] and candidate['boot']==q.boot:live_child=candidate
  except (FileNotFoundError,ProcessLookupError,json.JSONDecodeError):pass
  if live_runner and live_child:break
  time.sleep(.005)
 launch={'command':command,'controller':ident(os.getpid()),'runner':live_runner,'payload':live_child,
 'spawn_pid':child.pid,'authority_sha256':authority_sha,'deadline_utc':a['deadline_utc'],'caps':{'wall':10,'cpu':10,'rss':536870912,'as':536870912,'file':67108864}}
 save(paths['launch.json'],launch);print(json.dumps({'type':'LIVE_OR_TERMINAL_IDENTITY','operation':op,**launch}),flush=True)
 # CAPRUN owns the child group and cleanup. A rare controller wait failure is
 # retained as a GAP for the operator; never kill a runner while bypassing custody.
 try:out,err=child.communicate(timeout=14)
 except subprocess.TimeoutExpired:
  save(paths['receipt.json'],{'status':'GAP_RUNNER_STILL_LIVE','runner_pid':child.pid,'boot':q.boot,'source_access':False});raise
 try:t=json.loads(paths['telemetry.json'].read_bytes()) # receipt first, before payload output
 except (FileNotFoundError,json.JSONDecodeError):
  save(paths['receipt.json'],{'status':'GAP_TERMINAL_TELEMETRY','runner_rc':child.returncode,'boot':q.boot,'source_access':False});raise
 try:hi=json.loads(paths['identity.json'].read_bytes())
 except (FileNotFoundError,json.JSONDecodeError):hi={}
 remain=members(t['pgid']) if isinstance(t.get('pgid'),int) else ['UNKNOWN_GROUP']
 stdout=paths['stdout'].read_bytes() if paths['stdout'].is_file() else b''
 stderr=paths['stderr'].read_bytes() if paths['stderr'].is_file() else b'';status='GAP';checks=[]
 try:
  need(all(paths[s].is_file() for s in ('authority.json','stdout','stderr','telemetry.json','sing','identity.json','launch.json','claim.json')),'required artifact absent')
  need(live_runner is not None and live_child is not None,'required live identity capture absent')
  need(not remain and not Path('/proc',str(child.pid)).exists(),'group/runner not absent')
  need(t['schema']=='CAPRUN/v1' and t['error'] is None and err==b'' and stderr==b'','telemetry/stderr failure')
  need(t['pid']==t['pgid']==hi['pid']==hi['pgid'] and hi['authority_sha256']==authority_sha and hi['source_access'] is False,'payload custody mismatch')
  need(t['start_identity']=='boot='+q.boot+';start_ticks='+hi['start_ticks'],'start identity drift')
  need({n:digest(W/n) for n in PINS}==PINS and {n:digest(n) for n in BIN}==BIN,'post pins drift')
  need(digest(ENG/'ROOT-GREEN.md')==q.green_sha256 and digest(__file__)==q.controller_sha256,'post physical authority/controller drift')
  if op=='hybrid':
   need(child.returncode==0 and t['status']=='NORMAL_EXIT' and t['child_returncode']==0,'hybrid not normal')
   # Identical tiny output replay under both Python optimization modes, no CAS.
   code='import sys;from pathlib import Path;sys.path.insert(0,"'+str(W)+'");import engine as E;print(E.check_hybrid(Path("'+str(ENG/'tiny-engine-fixture.jsonl')+'").read_bytes(),Path("'+str(paths['stdout'])+'").read_bytes(),Path("'+str(paths['stderr'])+'").read_bytes()))'
   for flags in ([],['-O']):
    v=subprocess.run(['/usr/bin/prlimit','--as=536870912:536870912','--cpu=2:2','--fsize=67108864:67108864','--core=0:0','--','/usr/bin/python3','-I','-B']+flags+['-c',code],cwd=W,capture_output=True,timeout=3)
    checks.append({'flags':flags,'rc':v.returncode,'stdout':v.stdout.decode(),'stderr':v.stderr.decode()});need(v.returncode==0 and v.stderr==b'','tiny verifier failed')
   status='ENGINEERING_HYBRID_PASS'
  else:
   need(child.returncode==142 and t['status']=='SIGNAL' and t['child_returncode']==-14 and t['child_signal']==14,'not actual SIGALRM')
   need(stdout==b'JC2_HYBRID81_ALARM_READY\n' and 0<hi['timer_remaining'][0]<=1 and t['wall_elapsed_seconds']<2,'alarm marker/timer/duration')
   status='ENGINEERING_ALARM_PASS'
 except Exception as exc:checks.append({'gap':type(exc).__name__+': '+str(exc)})
 save(paths['receipt.json'],{'status':status,'operation':op,'boot':q.boot,'authority_sha256':authority_sha,'runner_rc':child.returncode,'runner_stdout':out.decode(),'runner_stderr':err.decode(),'telemetry':t,'group_members_after':remain,'checks':checks,'source_access':False,
 'hashes':{s:digest(v) for s,v in paths.items() if s!='receipt.json' and v.is_file()}})
 print(json.dumps({'type':'TERMINAL','operation':op,'status':status,'group_members_after':remain}),flush=True)
 need(status!='GAP','engineering failed; STOP no retry')
if __name__=='__main__':main()
