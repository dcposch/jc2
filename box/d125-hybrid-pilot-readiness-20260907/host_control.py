"""PREP ONLY: exact engineering dispatch, not production-token isolation.

The frozen authorizer uses a shared schema/path; see GAP-AUTH in registration.
No authority is generated. No source/production metadata is accessed by this file.
"""
from datetime import datetime,timezone
import hashlib,importlib,json,os,platform,resource,signal,socket,sys,time
from pathlib import Path

WORK=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907')
ENG=WORK/'engineering'
INSTANCE='i-0da0cebfc97c9fd54'
MATH='bff1b2073c3fb878458de346fa1b3c87ab378ce5b7a5320e3a634b7b7da0950c'
RUNNER='4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
PINS={'construct.py':'aa65e7104d3fcf5ad868eea952587a6841d784c6f9469c6c42ea2a02913ef264',
      'replay.py':'06475a2a566b4ed617068d65f3a0473ef83c16e2cb357dcb959ee46716781c23',
      'baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'}
CAPS=dict(wall_seconds=10,cpu_seconds=10,address_bytes=512*1024**2,file_bytes=128*1024**2,
          polynomial_terms=100000,multiply_pairs=1000000,retained_terms=1000000,coefficient_bits=4096)
PRODUCTION_OUTPUTS=('construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr','pilot.telemetry.json')

def need(ok,message):
    if not ok:raise ValueError(message)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def observed():
    return dict(system=platform.system(),vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),
                instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),
                boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                cwd=str(Path.cwd()),hostname=socket.gethostname(),now=time.time())
def host_check(h):
    need(h['system']=='Linux' and h['vendor']=='Amazon EC2' and h['instance']==INSTANCE and h['cwd']==str(WORK),'exact registered host/cwd')
    need(bool(h['boot']) and bool(h['hostname']),'fresh boot/hostname missing')
def outputs_absent(root):
    # lexists rejects dangling symlinks as well as stale regular files/directories.
    occupied=[name for name in PRODUCTION_OUTPUTS if os.path.lexists(Path(root)/name)]
    need(not occupied,'production output already present: '+','.join(occupied))
    return list(PRODUCTION_OUTPUTS)
def validate(a,h,reg,green,code,engineering,control):
    host_check(h);need(control in ('authorize','rss'),'unknown engineering control')
    need(a.get('schema')=='jc2.hybrid-affine-authority/v1' and a.get('engineering_control_only') is True and a.get('engineering_control')==control,'exact engineering dispatch scope absent')
    need(a.get('root_green') is True and a.get('construction_only') is True,'explicit control GREEN absent')
    need(a.get('boot_id')==h['boot'] and a.get('registration_sha256')==reg and a.get('root_green_sha256')==green,'boot/registration/GREEN mismatch')
    need(a.get('code_sha256')==code==PINS,'frozen payload pins')
    need(a.get('engineering_code_sha256')==engineering and engineering.get('run_capped.py')==RUNNER and len(engineering.get('host_control.py',''))==64,'engineering/runner pins')
    need(a.get('hybrid_gate_sha256')==MATH and a.get('gates_accepted') is True,'accepted hybrid mathematics absent')
    gate=a.get('code_gate_sha256','');need(len(gate)==64 and all(c in '0123456789abcdef' for c in gate),'accepted code gate missing')
    need(a.get('caps')==CAPS and 0<a.get('expires_unix',0)-h['now']<=10,'tiny engineering caps/expiry')

def deny_production(*args,**kwargs):raise RuntimeError('ENGINEERING FORBIDS SOURCE/METADATA/PRODUCTION')
def install_tripwires(C):
    # Process-local guards, not edits to any frozen file. The separate C.main
    # invocation remains outside this guard and is the explicit GAP-AUTH.
    for name in ('main','build','reconstruct','layout','rows'):setattr(C,name,deny_production)
    C.B.make_contract=deny_production;C.B.validate_contract=deny_production
    forbidden={os.path.abspath(C.SOURCE_PATH),str(WORK/'construction.jsonl'),str(WORK/'replay-result.json')}
    def audit(event,args):
        if event=='open' and args and isinstance(args[0],(str,bytes,os.PathLike)):
            need(os.path.abspath(os.fsdecode(args[0])) not in forbidden,'ENGINEERING source/output access forbidden')
    sys.addaudithook(audit)

def tiny(C,path):
    # Real frozen gate; do not use main or acquire a production arithmetic client.
    authority,authorized_ops=C.authorize(path)
    authorized_ops.production=False
    ops=C.Ops(authority['caps'],min(authorized_ops.deadline,time.monotonic()+2),False)
    x=C.mono((0,));need(ops.mul(ops.add(C.const(1),x),ops.add(C.const(1),x,-1))=={():C.F(1),(0,0):C.F(-1)},'tiny rational arithmetic')
    # Actual normalized toy lift/Hermite exercise: four slots, total degree<=3.
    c={(0,3):C.const(1),(1,2):C.const(1),(0,1):{},(1,0):x}
    C.solve_level(c,'A',1,ops);need(not C.liftrow(c,0,-1,ops),'tiny normalized Hermite/lift')
    need(not ops.production and not authorized_ops.production,'engineering retained production context')
    return authority

def identity(label,host,authority_sha):
    r=dict(utc=datetime.now(timezone.utc).isoformat(),host=host,pid=os.getpid(),pgid=os.getpgrp(),argv=sys.argv,
           start_ticks=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()[19],
           cgroup=Path('/proc/self/cgroup').read_text(),pid_namespace=os.readlink('/proc/self/ns/pid'),
           authority_sha256=authority_sha,source_access=False,production_metadata=False,
           limits={n:resource.getrlimit(k) for n,k in [('AS',resource.RLIMIT_AS),('CPU',resource.RLIMIT_CPU),('FSIZE',resource.RLIMIT_FSIZE),('CORE',resource.RLIMIT_CORE)]})
    with (ENG/(label+'.identity.json')).open('x') as f:json.dump(r,f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())

def main():
    need(len(sys.argv)==2,'one control or paths command only')
    control=sys.argv[1];host=observed();host_check(host)
    if control=='paths':
        print(json.dumps(dict(status='READ_ONLY_OUTPUT_PATH_CHECK',absent=outputs_absent(WORK),host=host)));return
    path=WORK/'authority.json';a=json.loads(path.read_bytes());code={n:sha(WORK/n) for n in PINS}
    engineering={'host_control.py':sha(__file__),'run_capped.py':sha(WORK/'run_capped.py')}
    validate(a,host,sha(WORK/'REGISTRATION.md'),sha(WORK/'ROOT-GREEN.md'),code,engineering,control)
    outputs_absent(WORK);sys.path.insert(0,str(WORK));C=importlib.import_module('construct')
    need(Path(C.__file__).resolve()==WORK/'construct.py','constructor import path')
    install_tripwires(C);identity(control+'-pre',host,sha(path));tiny(C,path);identity(control,host,sha(path))
    if control=='authorize':
        print(json.dumps(dict(status='REAL_AUTHORIZE_AND_TINY_NORMALIZED_CONTROL_PASS',source_access=False,production_metadata=False,production_invoked=False)));return
    # Only to close the named restarted-boot/current-path group custody gap.
    # This is the same accepted orphan/RSS/TERM->KILL pattern, no new supervisor.
    read,write=os.pipe();child=os.fork()
    if child==0:
        os.close(read);signal.signal(signal.SIGTERM,signal.SIG_IGN);identity('rss-descendant',host,sha(path));os.write(write,b'R');os.close(write)
        time.sleep(.2);buffer=bytearray(b'X'*(96*1024**2))
        while buffer:time.sleep(1)
        os._exit(0)
    os.close(write);need(os.read(read,1)==b'R','descendant ready handshake');os.close(read)
    print(json.dumps(dict(parent=os.getpid(),child=child,pgid=os.getpgrp())),flush=True);os._exit(0)
if __name__=='__main__':main()
