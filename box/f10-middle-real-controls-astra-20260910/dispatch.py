"""Exactly four semantic controls; metadata dispatcher, DISABLED without ROOT authority."""
import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import resource
import shutil
import signal
import socket
import stat
import subprocess
import sys
import time

JOB = 'f10-middle-real-certificate-20260910'
CONTROL_JOB = 'f10-middle-real-controls-20260910'
ORIGINAL_SHA = '219151792c8ffbbaab2e745fa60bd72e9c05c705fcc2ded992bcd97badf05470'
POSITIVE_RECEIPT_SHA = '1a9bb0f58e96fa5a0be086e72a725f3e1f7eabad89248888c3d8acc13323cf44'
CONTROLS = [('U','positive V cancellation'),('R','full cofactor identity'),
            ('j','wrong maximal excluded-edge factor'),('bernstein','full Bernstein expansion')]
LIMIT = 16777216
RSS = 2147483648
CAPRUN_SHA = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
SCIENCE = {
 'f10-middle-real-domain-astra-20260910.md':'3f79cabecdb2c0f480bde3db644eac91ea5c8d3d472a3477f575b356993347ea',
 'f10-middle-real-domain-gate-fable5-20260910.md':'f04c174e4b3111b2b9ee3e22e4ecceb619f0cfd2b9374e99a9ec9065cc52d21f',
 'f10-middle-resonance-unit-astra-20260910.md':'8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012',
 'f10-middle-resonance-unit-gate-fable5-20260910.md':'dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad',
 'f10-middle-full-boundary-astra-20260910.md':'82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6',
 'f10-middle-full-boundary-gate-fable5-20260910.md':'8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491',
 'f10-middle-univariate-unit-astra-20260910.md':'890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5',
 'f10-middle-septic-gate-fable5-20260910.md':'cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62'}
REQUIRED = dict(SCIENCE, **{
 'producer.py':'44859af3084c3445522c8e73a88c0fc96a710375bcd9c9e50340fd4ce5de0dd2',
 'checker.py':'9369f0f311da9848f7d708a77413cda9115a4d8376aa626d7efaf017b4f8043c',
 'authority.py':'4587133176acc66842f9ded5c6b6a6e37683ff9ffe980bf9f46e42088359d73d',
 'f10-middle-real-code-astra-20260910.md':'c3111895d6d9c8ea217124aad44aefb351faf244ea13037935673f8f8fd785e9',
 'f10-middle-real-code-gate-fable5-20260910.md':'d3b8c09234d50b51b9dbcfaa7a9f341f34263540bd35e798c9f794137640c932',
 'f10-middle-real-runtime-gate-fable5-20260910.md':'0562b82afa2b6f6da1e2c488d261fc65f22f705629c12446bbfeaf85bdccbef2'})
JOINT = {'aggregate_wall_seconds':360, 'aggregate_cpu_seconds':330,
         'rss_bytes':RSS, 'aggregate_wire_bytes':LIMIT}
PROFILES = {'preflight':[5,3,RSS], 'dummy':[5,3,33554432],
            'mutate':[10,9,RSS], 'check':[45,49,RSS]}

def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)

def now():
    return datetime.datetime.now(datetime.timezone.utc)

def strict_pairs(items):
    result = {}
    for k,v in items:
        need(k not in result, 'duplicate metadata key')
        result[k] = v
    return result

def read_json(p, ceiling=65536):
    need(p.stat().st_size <= ceiling, 'metadata size cap')
    return json.loads(p.read_bytes(), object_pairs_hook=strict_pairs)

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as stream:
        for chunk in iter(lambda:stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()

def canonical(name):
    p = pathlib.Path(name)
    need(p.is_absolute() and re.fullmatch(r'/[A-Za-z0-9_./-]+', str(p)) is not None,
         'literal absolute path required')
    need(str(p.resolve()) == str(p) and not p.is_symlink(), 'canonical nonsymlink path required')
    return p

def immutable(p, strict=False):
    p = canonical(p)
    st = p.stat()
    need(stat.S_ISREG(st.st_mode) and st.st_uid == 0 and not st.st_mode & 0o022,
         'root-owned immutable-to-writer file required')
    if strict:
        need(not st.st_mode & 0o222, 'readonly source or authority required')
    for parent in p.parents:
        st = parent.stat()
        need(st.st_uid == 0 and not st.st_mode & 0o022, 'immutable root-owned ancestry required')
    return p

def write_json(p, obj, mode=0o444):
    raw = (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    need(len(raw) <= 65536, 'metadata record exceeds 64KiB')
    fd = os.open(p, os.O_WRONLY|os.O_CREAT|os.O_EXCL, mode)
    with os.fdopen(fd,'wb') as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        os.fchmod(stream.fileno(),mode)
    return sha(p)

def utc_deadline(text):
    need(type(text) is str and text.endswith('+00:00'), 'explicit UTC offset required')
    return datetime.datetime.fromisoformat(text)

def mount_type(path):
    matches=[]
    for line in pathlib.Path('/proc/self/mountinfo').read_text().splitlines():
        left,right=line.split(' - ',1); fields=left.split(); mount=fields[4]
        if str(path)==mount or str(path).startswith(mount.rstrip('/')+'/'):
            matches.append((len(mount),mount,right.split()[0]))
    need(matches,'mount record missing')
    return max(matches)[1:]

def proc_identity(pid):
    try:
        raw=pathlib.Path('/proc/'+str(pid)+'/stat').read_text()
        f=raw[raw.rfind(')')+2:].split()
        boot=pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()
        return {'pid':pid,'pgid':int(f[2]),'state':f[0],
                'start_identity':'boot='+boot+';start_ticks='+f[19],
                'pid_namespace':os.readlink('/proc/'+str(pid)+'/ns/pid')}
    except FileNotFoundError:
        return None

class Batch:
    def __init__(self, path):
        need(os.geteuid()==0 and sys.platform=='linux', 'ROOT Linux dispatcher required')
        self.path=immutable(path,True)
        need(stat.S_IMODE(self.path.stat().st_mode)==0o444,'registration mode must be 0444')
        self.root_sha=sha(self.path); self.r=read_json(self.path)
        r=self.r
        need(r.get('schema')=='f10-middle-real-controls/v1' and r.get('enabled') is True,
             'disabled root registration')
        need(r['jobtag']==CONTROL_JOB and r['exclusive_no_concurrent_writer'] is True,'root job/exclusivity')
        need(r['caps']==JOINT and r['profiles']==PROFILES and r['preflight_wall_seconds']==180,
             'fixed profiles or joint cap mismatch')
        labels={'refuse-disabled','refuse-wronghost','refuse-argv','refuse-caps','refuse-missing',
                'valid','startup-producer','startup-checker','dummy','mutate',
                'check-U','check-R','check-j','check-bernstein'}
        need(type(r['commands']) is dict and set(r['commands'])==labels,'exact fourteen command inventory')
        need(type(r['uid']) is int and type(r['gid']) is int and r['uid']>0 and r['gid']>0,
             'nonroot science uid/gid required')
        need(pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2', 'EC2 vendor')
        instance=pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()
        need(re.fullmatch(r'i-[0-9a-f]+',instance) and instance==r['instance_id'],'EC2 instance')
        need(socket.gethostname()==r['hostname'],'hostname')
        self.files={k:immutable(v,k in ('producer','checker','authority','probe','dispatcher','mutator','caprun'))
                    for k,v in r['files'].items()}
        need(set(self.files)=={'python','setpriv','caprun','producer','checker','authority','probe','dispatcher','mutator'},
             'exact executable/source roles')
        need(str(self.files['python'])==os.path.realpath(sys.executable),'resolved interpreter')
        need(str(self.files['dispatcher'])==str(pathlib.Path(__file__).resolve()),'dispatcher path')
        outer=[self.files['python'].as_posix(),'-I','-S','-B',str(self.files['dispatcher']),
               '--registration',str(self.path)]
        observed=pathlib.Path('/proc/self/cmdline').read_bytes().rstrip(b'\0').decode().split('\0')
        need(r['outer_argv']==outer and observed==outer,'full dispatcher argv/flags')
        self.source=canonical(r['source_root'])
        for role in ('producer','checker','authority','probe','dispatcher','mutator'):
            need(self.files[role].parent==self.source,'immutable sibling source directory')
        need(os.getcwd()==str(self.source),'dispatcher cwd')
        self.mount=canonical(r['output_mount']); self.writer=canonical(r['writer_dir'])
        self.frozen=canonical(r['frozen_dir']); self.auth=canonical(r['authority_dir'])
        need(self.writer.parent==self.mount and self.frozen.parent==self.mount and self.auth.parent==self.mount,
             'exact working output children')
        need(len({self.writer,self.frozen,self.auth})==3,'distinct working directories')
        mount,kind=mount_type(self.mount)
        need(mount==str(self.mount) and kind=='tmpfs','dedicated exact tmpfs required')
        need(self.mount.stat().st_uid==0 and not self.mount.stat().st_mode&0o022,
             'root-owned working mount parent')
        self.mount_identity=(self.mount.stat().st_dev,self.mount.stat().st_ino)
        fs=os.statvfs(self.mount)
        need(0 < fs.f_blocks*fs.f_frsize <= LIMIT,'aggregate tmpfs capacity')
        for d in (self.frozen,self.auth):
            need(d.is_dir() and d.stat().st_uid==0 and not d.stat().st_mode&0o022 and not list(d.iterdir()),
                 'fresh root-only output directory')
        need(self.writer.is_dir() and self.writer.stat().st_uid==r['uid'] and
             self.writer.stat().st_gid==r['gid'] and stat.S_IMODE(self.writer.stat().st_mode)==0o700 and
             not list(self.writer.iterdir()),'fresh science writer directory')
        self.durable=canonical(r['durable_dir'])
        need(not self.durable.exists() and self.durable.parent.is_dir(),'absent durable custody target')
        need(self.durable.parent.stat().st_uid==0 and not self.durable.parent.stat().st_mode&0o022,
             'root-only durable parent')
        need(mount_type(self.durable.parent)[1] in ('ext4','xfs') and
             self.durable.parent.stat().st_dev==r['durable_device'],'registered durable EBS filesystem')
        self.cg=canonical(r['cgroup_path'])
        need(str(self.cg).startswith('/sys/fs/cgroup/') and str(self.cg)!='/sys/fs/cgroup', 'owned nonroot cgroup')
        own=pathlib.Path('/proc/self/cgroup').read_text().strip()
        need(own=='0::'+str(self.cg)[len('/sys/fs/cgroup'):],'exact systemd cgroup membership')
        need(os.readlink('/proc/self/ns/pid')==r['pid_namespace'],'registered PID namespace')
        self.absolute=utc_deadline(r['mathematical_deadline_utc'])
        self.task_end=utc_deadline(r['task_deadline_utc'])
        need(now()<self.absolute<self.task_end,'future original deadlines')
        self.begin=time.monotonic(); self.math_begin=None; self.math_cpu_start=None
        self.runs=[]; self.quiet=True
        self.native_path=immutable(r['native_manifest'],True)
        self.native=read_json(self.native_path,262144)
        need(self.native.get('schema')=='f10-native-closure/v1' and type(self.native.get('files')) is dict,
             'native closure schema')
        need(1<=len(self.native['files'])<=1500,'native closure entry bound')
        self.pins=r['pins']
        need(type(self.pins) is dict and self.pins.get(str(self.native_path))==sha(self.native_path),
             'native manifest pin')
        for file in self.files.values():
            need(str(file) in self.pins,'required executable/source pin absent')
        need(self.pins[str(self.files['caprun'])]==CAPRUN_SHA,'unchanged CAPRUN pin')
        for role in ('producer','checker','authority'):
            need(self.pins[str(self.files[role])]==REQUIRED[role+'.py'] and self.files[role].name==role+'.py',
                 'accepted scientific role-path pin')
        need(self.pins[str(self.files['probe'])]=='d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4',
             'unchanged probe pin')
        for name,h in REQUIRED.items():
            matches=[p for p,v in self.pins.items() if pathlib.Path(p).name==name and v==h]
            need(len(matches)==1,'actual science/report file pin missing: '+name)
        self.original=immutable(r['original_input'],True)
        self.positive_receipt=immutable(r['positive_receipt'],True)
        need(self.mount not in self.original.parents and self.mount not in self.positive_receipt.parents,
             'baseline inputs must be outside working tmpfs')
        need(self.pins.get(str(self.original))==ORIGINAL_SHA and self.original.stat().st_size==854264,
             'literal original input pin/size')
        need(self.pins.get(str(self.positive_receipt))==POSITIVE_RECEIPT_SHA,'literal positive receipt pin')
        self.revalidate(); self.group_quiet()
        positive=read_json(self.positive_receipt,4096)
        need(positive.get('schema')=='f10-middle-real-check/v1' and positive.get('status')=='CERTIFIED_NONRESONANCE'
             and positive.get('input_sha256')==ORIGINAL_SHA and positive.get('j')=='4'
             and positive.get('code')=={role+'.py':REQUIRED[role+'.py'] for role in ('producer','checker','authority')},
             'positive baseline metadata/code binding')

    def revalidate(self):
        need(sha(self.path)==self.root_sha,'root registration drift')
        for p,h in list(self.pins.items())+list(self.native['files'].items()):
            need(re.fullmatch(r'[0-9a-f]{64}',h) is not None and sha(immutable(p))==h,'current file pin mismatch')
        need(sha(self.native_path)==self.pins[str(self.native_path)],'native manifest drift')
        need((self.mount.stat().st_dev,self.mount.stat().st_ino)==self.mount_identity,'working mount identity changed')
        need(mount_type(self.mount)==(str(self.mount),'tmpfs'),'working mount changed')
        fs=os.statvfs(self.mount)
        need(fs.f_blocks*fs.f_frsize<=LIMIT,'working output capacity changed')
        need(now()<self.task_end,'original task deadline expired')

    def group_quiet(self):
        pids=[int(p) for p in (self.cg/'cgroup.procs').read_text().split()]
        for pid in pids:
            if pid==os.getpid():
                continue
            item=proc_identity(pid)
            need(item is None or item['state']=='Z','owned cgroup still has nonzombie child')
        self.quiet=True

    def authority(self,label,script_argv,operation,outputs,mutation=None,input_pin=None):
        pins=dict(self.pins)
        if input_pin:
            pins[str(input_pin)]=sha(immutable(input_pin,True))
        obj={'enabled':True,'jobtag':JOB,'operation':operation,'exclusive_no_concurrent_writer':True,
             'instance_id':self.r['instance_id'],'hostname':self.r['hostname'],'cwd':str(self.source),
             'argv':script_argv,'executable':str(self.files['python']),'science':SCIENCE,
             'caps':JOINT,'deadline_utc':self.r['mathematical_deadline_utc'],'pins':pins,
             'outputs':[str(p) for p in outputs]}
        if mutation=='disabled': obj['enabled']=False
        elif mutation=='wronghost': obj['hostname']+='-WRONG'
        elif mutation=='argv': obj['argv']=script_argv+['WRONG']
        elif mutation=='caps': obj['caps']=dict(JOINT,rss_bytes=1)
        elif mutation=='missing': del obj['pins'][str(self.files['producer'])]
        path=self.auth/(label+'.authority.json')
        write_json(path,obj); immutable(path,True)
        return path,sha(path)

    def run(self,label,role,tail,profile,mutation=None,input_pin=None,math_phase=False):
        wall,cpu,rss=PROFILES[profile]
        self.group_quiet(); self.revalidate()
        if math_phase:
            if self.math_begin is None:
                self.math_begin=time.monotonic()
                usage=resource.getrusage(resource.RUSAGE_CHILDREN)
                self.math_cpu_start=usage.ru_utime+usage.ru_stime
            remaining=360-(time.monotonic()-self.math_begin)
        else:
            remaining=180-(time.monotonic()-self.begin)
        need(remaining>=wall+15 and (self.absolute-now()).total_seconds()>=wall+15,
             'original fixed admission refusal')
        output=self.writer/(label+'.payload')
        authpath=self.auth/(label+'.authority.json')
        args=[str(self.files[role])]+tail+['--registration',str(authpath)]
        outputs=[output]
        if role=='mutator':
            args+=['--input',str(self.original),'--positive-receipt',str(self.positive_receipt),
                   '--output-dir',str(self.writer),'--receipt',str(output)]
            outputs += [self.writer/('mutated-'+name+'.json') for name,_ in CONTROLS]
        elif role=='checker':
            input_name=input_pin if input_pin is not None else self.frozen/'startup-absent.input'
            args+=['--input',str(input_name),'--receipt',str(output)]
        else:
            args+=['--output',str(output)]
        operation={'probe':'probe','producer':'produce','checker':'check','mutator':'mutate'}[role]
        authority_path,authority_sha=self.authority(label,args,operation,outputs,mutation,input_pin)
        py=[str(self.files['python']),'-E','-s','-S','-B']+args
        child=[str(self.files['setpriv']),'--reuid',str(self.r['uid']),'--regid',str(self.r['gid']),
               '--clear-groups','--no-new-privs','--']+py
        out=self.mount/(label+'.stdout'); err=self.mount/(label+'.stderr'); tel=self.mount/(label+'.telemetry.json')
        command=[str(self.files['python']),'-I','-S','-B',str(self.files['caprun']),
                 '--wall-seconds',str(wall),'--cpu-seconds',str(cpu),'--rss-bytes',str(rss),
                 '--rss-sample-seconds','0.05','--term-grace-seconds','1',
                 '--stdout-file',str(out),'--stderr-file',str(err),'--telemetry-file',str(tel),
                 '--cwd',str(self.source),'--']+child
        need(command==self.r['commands'][label],'ROOT full CAPRUN/setpriv/Python argv mismatch')
        pre={'utc':now().isoformat(),'authority_path':str(authority_path),'authority_sha256':authority_sha,
             'root_registration_sha256':self.root_sha,'pins':self.pins,
             'native_manifest_sha256':sha(self.native_path),'full_argv':command,'child_argv':child,
             'python_argv':py,'profile':PROFILES[profile],'pid_namespace':self.r['pid_namespace']}
        if input_pin is not None:
            pre['frozen_input_sha256']=sha(input_pin)
        write_json(self.mount/(label+'.pre.json'),pre)
        need(sha(authority_path)==authority_sha,'authority hash BEFORE launch')
        env=dict(os.environ)
        for key in ('PYTHONPATH','LD_PRELOAD','LD_LIBRARY_PATH'):
            env.pop(key,None)
        env['LD_PRELOAD']=''; env['LD_LIBRARY_PATH']=''; env['PYTHONPATH']=''
        def file_cap():
            resource.setrlimit(resource.RLIMIT_FSIZE,(LIMIT,LIMIT))
        self.quiet=False
        before=time.monotonic()
        with open(self.mount/(label+'.runner.stdout'),'xb') as rout, open(self.mount/(label+'.runner.stderr'),'xb') as rerr:
            process=subprocess.Popen(command,cwd=self.source,env=env,stdin=subprocess.DEVNULL,
                                     stdout=rout,stderr=rerr,preexec_fn=file_cap,close_fds=True)
            write_json(self.mount/(label+'.runner-live.json'),{'utc':now().isoformat(),
                       'identity':proc_identity(process.pid),'argv':command})
            live_written=False
            while process.poll() is None:
                if not live_written:
                    childfile=pathlib.Path('/proc/'+str(process.pid)+'/task/'+str(process.pid)+'/children')
                    try:
                        for text in childfile.read_text().split():
                            pid=int(text); item=proc_identity(pid)
                            if item is None or item['pgid']!=pid:
                                continue
                            cmd=pathlib.Path('/proc/'+text+'/cmdline').read_bytes().rstrip(b'\0').decode().split('\0')
                            if cmd==py:
                                write_json(self.mount/(label+'.python-live.json'),{'utc':now().isoformat(),
                                           'identity':item,'argv':cmd}); live_written=True; break
                    except FileNotFoundError:
                        pass
                if time.monotonic()-before>wall+15 or now()>=self.absolute:
                    process.send_signal(signal.SIGTERM)
                    try: process.wait(timeout=15)
                    except subprocess.TimeoutExpired: raise RuntimeError('CAPRUN still live; ROOT cgroup cleanup required')
                    raise RuntimeError('late CAPRUN return; STOP without result acceptance')
                time.sleep(0.05)
            rc=process.returncode
        self.group_quiet()
        need(sha(authority_path)==authority_sha,'post authority drift')
        self.revalidate()
        if input_pin is not None:
            need(sha(immutable(input_pin,True))==pre['frozen_input_sha256'],'post frozen input drift')
        need(now()<self.absolute,'post-return original UTC deadline')
        if math_phase:
            need(time.monotonic()-self.math_begin<=360,'post-return joint wall exceeded')
            usage=resource.getrusage(resource.RUSAGE_CHILDREN)
            accounted=usage.ru_utime+usage.ru_stime-self.math_cpu_start
            need(accounted<=330,'conservative aggregate CPU including wrappers exceeded')
        else:
            need(time.monotonic()-self.begin<=180,'preflight aggregate wall exceeded')
        t=read_json(tel)
        ah=hashlib.sha256((json.dumps(child,ensure_ascii=False,separators=(',',':'))+'\n').encode()).hexdigest()
        need(t.get('schema')=='CAPRUN/v1' and t['argv_sha256']==ah and t['argv_count']==len(child),
             'CAPRUN argv telemetry binding')
        need(t['runner_exit_code']==rc and t['cwd']==str(self.source) and
             t['caps']['wall_seconds']==wall and t['caps']['cpu_seconds']==cpu and
             t['caps']['rss_bytes']==rss,'CAPRUN result/caps binding')
        need(type(t['pid']) is int and t['pid']==t['pgid'] and type(t['start_identity']) is str,
             'CAPRUN child identity')
        current=proc_identity(t['pid'])
        need(current is None or current['start_identity']!=t['start_identity'], 'CAPRUN leader not reaped')
        for key,path in (('stdout',out),('stderr',err)):
            need(t[key]['path']==str(path) and t[key]['sha256']==sha(path) and t[key]['bytes']==path.stat().st_size,
                 'terminal stream hash binding')
        write_json(self.mount/(label+'.post.json'),{'utc':now().isoformat(),'authority_sha256':sha(authority_path),
                   'telemetry_sha256':sha(tel),'native_manifest_sha256':sha(self.native_path),
                   'all_current_pins':self.pins,'actual_python_live_observed':live_written,'owned_cgroup_quiet':True})
        self.runs.append({'label':label,'telemetry_sha256':sha(tel),'status':t['status'],
                          'resource':t['resource'],'child_returncode':t['child_returncode']})
        return t,out,err,output

    def normal(self,t,code):
        need(t['status']=='NORMAL_EXIT' and t['resource'] is None and t['child_returncode']==code,
             'unexpected non-normal or child return')

    def execute(self):
        expected={'disabled':'disabled or mismatched registration','wronghost':'registered physical identity mismatch',
                  'argv':'cwd or full script argv mismatch','caps':'caps mismatch','missing':'required input pin mismatch'}
        for mutation,reason in expected.items():
            t,out,err,payload=self.run('refuse-'+mutation,'probe',['--mode','authorize','--job',JOB],'preflight',mutation)
            self.normal(t,2)
            need(not payload.exists() and out.read_bytes()==b'' and err.read_text()=='REFUSAL: '+reason+'\n',
                 'exact refusal/sentinel absence')
        t,out,err,payload=self.run('valid','probe',['--mode','authorize','--job',JOB],'preflight')
        self.normal(t,0); data=read_json(payload)
        need(data['status']=='POST_AUTHORIZE' and data['identity']['uid']==self.r['uid'] and
             data['identity']['gid']==self.r['gid'],'valid nonroot sentinel')
        for role in ('producer','checker'):
            # Wrong job must fail before checker input inspection: no placeholder file or pin is needed.
            t,out,err,payload=self.run('startup-'+role,role,['--job','WRONG-JOB'],'preflight',input_pin=None)
            self.normal(t,2)
            need(not payload.exists() and out.read_bytes()==b'' and
                 err.read_text()=='INCONCLUSIVE: wrong job or platform\n','actual science startup refusal')
        t,out,err,payload=self.run('dummy','probe',['--mode','dummy','--job',JOB],'dummy')
        need(t['status']=='RESOURCE_CAP' and t['resource']=='rss' and t['termination']['term_sent'] is True and
             t['termination']['kill_sent'] is True and t['termination']['leader_reaped'] is True and
             t['termination']['cleanup_complete'] is True and not t['termination']['group_live_before_reap'],
             'dummy descendant cleanup outcome')
        checks=t['identity_checks']
        for stage,signum in (('before-term',15),('before-kill',9)):
            matches=[e for e in checks if e.get('stage')==stage]
            sends=[e for e in checks if e.get('stage')==stage+'-send']
            need(len(matches)==1 and matches[0].get('result')=='MATCH' and
                 matches[0].get('observed_pid')==t['pid'] and matches[0].get('observed_pgid')==t['pgid'] and
                 matches[0].get('observed_start_identity')==t['start_identity'],'dummy signal identity')
            need(len(sends)==1 and sends[0].get('result')=='SENT' and type(sends[0].get('signal')) is int and
                 sends[0]['signal']==signum,'dummy exact signal')
        events=[json.loads(line) for line in payload.read_text().splitlines()]
        need([e['event'] for e in events]==['parent_started','child_ready_ignoring_term','parent_exit_pending','orphan_allocated_64MiB'],
             'dummy four-event sequence')
        for e in events:
            need(e['identity']['pgid']==t['pgid'] and e['identity']['pid_namespace']==self.r['pid_namespace'],
                 'dummy group/namespace')
        need(events[0]['identity']['pid']==t['pid'] and events[2]['identity']==events[0]['identity'] and
             events[1]['identity']==events[3]['identity'] and events[1]['identity']['pid']!=t['pid'],
             'dummy parent-exit/child identity')
        need(t['max_observed_group_rss_bytes']>33554432,'dummy RSS observed')
        t,out,err,payload=self.run('mutate','mutator',['--job',JOB],'mutate',input_pin=self.original,math_phase=True)
        self.normal(t,0)
        mutation=read_json(payload,8192)
        expected_code={role+'.py':REQUIRED[role+'.py'] for role in ('producer','checker','authority')}
        need(mutation.get('schema')=='f10-middle-real-mutator/v1' and mutation.get('status')=='FOUR_CHANGED_FIXTURES'
             and mutation.get('original_sha256')==ORIGINAL_SHA
             and mutation.get('positive_receipt_sha256')==POSITIVE_RECEIPT_SHA
             and mutation.get('code')==expected_code
             and mutation.get('mutator_sha256')==self.pins[str(self.files['mutator'])], 'mutator receipt binding')
        entries=mutation.get('fixtures')
        need(type(entries) is list and len(entries)==4,'exact four fixture inventory')
        frozen=[]
        for item,(name,reason) in zip(entries,CONTROLS):
            source=self.writer/('mutated-'+name+'.json'); target=self.frozen/('mutated-'+name+'.json')
            need(item['name']==name and item['path']==str(source) and item['expected_error']==reason
                 and item['changed'] is True and item['readback']=='EXACT','literal changed fixture metadata')
            need(source.is_file() and not source.is_symlink() and sha(source)==item['sha256']
                 and str(source.stat().st_size)==item['bytes'] and item['sha256']!=ORIGINAL_SHA,'changed fixture hash')
            need(not target.exists() and not target.is_symlink(),'fresh frozen fixture target')
            os.rename(source,target); os.chown(target,0,0); os.chmod(target,0o444)
            need(sha(immutable(target,True))==item['sha256'],'frozen fixture move/hash')
            frozen.append((name,reason,target,item['sha256']))
        os.chmod(self.frozen,0o555)
        checks=[]
        for name,reason,target,fixture_sha in frozen:
            t,out,err,receipt=self.run('check-'+name,'checker',['--job',JOB],'check',input_pin=target,math_phase=True)
            self.normal(t,2)
            need(not receipt.exists() and not receipt.is_symlink() and out.read_bytes()==b''
                 and err.read_text()=='INCONCLUSIVE: '+reason+'\n', 'exact semantic rejection: '+name)
            need(sha(target)==fixture_sha,'post semantic fixture pin')
            checks.append({'name':name,'fixture_sha256':fixture_sha,'normal_exit':2,
                           'expected_error':reason,'stderr_sha256':sha(err),
                           'telemetry_sha256':self.runs[-1]['telemetry_sha256'],'receipt_absent':True})
        used=resource.getrusage(resource.RUSAGE_CHILDREN); own=resource.getrusage(resource.RUSAGE_SELF)
        return {'status':'FOUR_SEMANTIC_REJECTIONS_CONFIRMED','original_input_sha256':ORIGINAL_SHA,
                'positive_baseline_receipt_sha256':POSITIVE_RECEIPT_SHA,'mutator_receipt_sha256':sha(payload),
                'checks':checks,'positive_science_reruns':0,
                'math_window_wall_seconds':time.monotonic()-self.math_begin,
                'conservative_cpu_including_caprun_and_ps':used.ru_utime+used.ru_stime-self.math_cpu_start,
                'dispatcher_cpu_seconds_separate':own.ru_utime+own.ru_stime,
                'scope':'four semantic controls only; no certificate, source or JC2 promotion'}

    def durable_copy(self,result):
        self.group_quiet()
        need(now()<self.task_end,'terminal custody admission after task cutoff')
        self.durable.mkdir(mode=0o700)
        records=[]
        # Exact owned working mount only. No deletion, unmount or worker stop.
        for parent,dirs,names in os.walk(self.mount,followlinks=False):
            need(all(not (pathlib.Path(parent)/d).is_symlink() for d in dirs),'working directory symlink')
            for name in sorted(names):
                need(now()<self.task_end,'terminal custody exceeded original task cutoff')
                source=pathlib.Path(parent)/name
                need(source.is_file() and not source.is_symlink(),'regular custody file required')
                relative=source.relative_to(self.mount); target=self.durable/relative
                target.parent.mkdir(mode=0o700,parents=True,exist_ok=True)
                with open(source,'rb') as src, open(target,'xb') as dst:
                    shutil.copyfileobj(src,dst,1048576); dst.flush(); os.fsync(dst.fileno())
                os.chmod(target,0o444)
                need(sha(target)==sha(source),'durable byte copy mismatch')
                records.append({'path':str(relative),'bytes':source.stat().st_size,'sha256':sha(target)})
                need(len(records)<=200,'bounded custody inventory')
        manifest={'schema':'f10-real-durable-custody/v1','utc':now().isoformat(),
                  'root_registration_sha256':self.root_sha,'result':result,'runs':self.runs,
                  'working_budget_bytes':LIMIT,'replicas_are_not_scientific_outputs':True,'files':records}
        write_json(self.durable/'CUSTODY.json',manifest)
        for parent,dirs,names in os.walk(self.durable,topdown=False):
            fd=os.open(parent,os.O_RDONLY); os.fsync(fd); os.close(fd)
        fd=os.open(self.durable.parent,os.O_RDONLY); os.fsync(fd); os.close(fd)
        need(now()<self.task_end,'durable finalization exceeded original task cutoff')
        return sha(self.durable/'CUSTODY.json')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--registration',required=True); a=p.parse_args()
    batch=None; result={'status':'STOP_NONDECISION','reason':'not launched'}
    try:
        batch=Batch(a.registration)
        result=batch.execute()
    except Exception as exc:
        result={'status':'STOP_NONDECISION','reason':str(exc)[:500]}
    if batch is not None:
        try:
            digest=batch.durable_copy(result)
            # No post-copy stdout write: registered stdout is itself a custodied working file.
            # ROOT reads the durable manifest only after this dispatcher is terminal.
        except Exception as exc:
            print(json.dumps({'status':'STOP_CUSTODY_INCOMPLETE','reason':str(exc)[:500],
                              'root_terminal_cleanup_and_capture_required':True}))
            return 2
    else:
        print(json.dumps(result))
    return 0 if result['status']=='FOUR_SEMANTIC_REJECTIONS_CONFIRMED' else 2

if __name__=='__main__':
    raise SystemExit(main())
