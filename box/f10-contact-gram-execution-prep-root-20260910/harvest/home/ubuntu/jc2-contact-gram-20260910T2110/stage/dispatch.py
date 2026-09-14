"""Fixed contact-certificate dispatcher. Metadata only; DISABLED without ROOT authority."""
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

JOB = 'f10-contact-gram-certificate-20260910'
LIMIT = 16777216
RSS = 2147483648
CAPRUN_SHA = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
SCIENCE = {
 'f10-contact-real-window-astra-20260910.md':'f87a2189ceacbca0d58e84aa5e32838b89c47ff249ea9acb5d757ae184e6a2d2',
 'f10-contact-quartic-gram-gate-fable5-20260910.md':'ce14c6a789086419f88a601faf10bfd388639697cd693a1deb12160c955f5068',
 'f10-contact-symmetric-remainder-astra-20260910.md':'96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13'}
CODE = {
 'producer.py':'afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee',
 'checker.py':'ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06',
 'authority.py':'96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141'}
ROLE_PINS = {'producer':CODE['producer.py'],'checker':CODE['checker.py'],
 'authority':CODE['authority.py'],
 'probe':'d0df7ba6d9e0e082bed92321dd390fe91bc4bf8f32ce68cdf9c8a9180b4e39f4',
 'mutator':'70857a11be5e21d63d8bb476663dd3587332d1968f5f26912e6851aa51d5d77c'}
JOINT = {'aggregate_wall_seconds':600, 'aggregate_cpu_seconds':550,
         'rss_bytes':RSS, 'aggregate_wire_bytes':LIMIT}
PROFILES = {'preflight':[5,3,RSS], 'dummy':[5,3,33554432],
            'produce':[400,359,RSS], 'check':[90,89,RSS],
            'mutate':[10,9,RSS], 'negative':[30,29,RSS]}

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
        need(r.get('schema')=='f10-contact-gram-runtime/v1' and r.get('enabled') is True,
             'disabled root registration')
        need(r['jobtag']==JOB and r['exclusive_no_concurrent_writer'] is True,'root job/exclusivity')
        need(r['caps']==JOINT and r['profiles']==PROFILES and r['preflight_wall_seconds']==180,
             'fixed profiles or joint cap mismatch')
        need(type(r['uid']) is int and type(r['gid']) is int and r['uid']>0 and r['gid']>0,
             'nonroot science uid/gid required')
        need(pathlib.Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2', 'EC2 vendor')
        instance=pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()
        need(re.fullmatch(r'i-[0-9a-f]+',instance) and instance==r['instance_id'],'EC2 instance')
        need(socket.gethostname()==r['hostname'],'hostname')
        self.files={k:immutable(v,k in ('producer','checker','authority','probe','mutator','dispatcher','caprun'))
                    for k,v in r['files'].items()}
        need(set(self.files)=={'python','setpriv','caprun','producer','checker','authority','probe','mutator','dispatcher'},
             'exact executable/source roles')
        need(str(self.files['python'])==os.path.realpath(sys.executable),'resolved interpreter')
        need(str(self.files['dispatcher'])==str(pathlib.Path(__file__).resolve()),'dispatcher path')
        outer=[self.files['python'].as_posix(),'-I','-S','-B',str(self.files['dispatcher']),
               '--registration',str(self.path)]
        observed=pathlib.Path('/proc/self/cmdline').read_bytes().rstrip(b'\0').decode().split('\0')
        need(r['outer_argv']==outer and observed==outer,'full dispatcher argv/flags')
        self.source=canonical(r['source_root'])
        for role in ('producer','checker','authority','probe','mutator','dispatcher'):
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
        self.runs=[]; self.quiet=True; self.authority_shas={}
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
        for role,h in ROLE_PINS.items():
            need(self.pins[str(self.files[role])]==h,'exact installed role pin: '+role)
        self.science_paths=r['science_paths']
        need(type(self.science_paths) is dict and set(self.science_paths)==set(SCIENCE),'science path inventory')
        for name,h in SCIENCE.items():
            p=immutable(self.science_paths[name],True)
            need(p.name==name and self.pins.get(str(p))==h,'exact science path pin')
        need({role:self.files[role].name for role in ROLE_PINS}==
             {'producer':'producer.py','checker':'checker.py','authority':'authority.py',
              'probe':'probe.py','mutator':'mutate.py'},'literal sibling role basenames')
        self.revalidate(); self.group_quiet()

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

    def authority(self,label,script_argv,operation,outputs,mutation=None,input_pin=None,extra_pin=None):
        pins=dict(self.pins)
        if input_pin:
            pins[str(input_pin)]=sha(immutable(input_pin,True))
        if extra_pin:
            pins[str(extra_pin)]=sha(immutable(extra_pin,True))
        obj={'enabled':True,'jobtag':JOB,'operation':operation,'exclusive_no_concurrent_writer':True,
             'instance_id':self.r['instance_id'],'hostname':self.r['hostname'],'cwd':str(self.source),
             'argv':script_argv,'executable':str(self.files['python']),'science':SCIENCE,
             'python_flags':['-E','-s','-S','-B'],
             'full_argv':[str(self.files['python']),'-E','-s','-S','-B']+script_argv,
             'science_paths':self.science_paths,
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
            remaining=600-(time.monotonic()-self.math_begin)
        else:
            remaining=180-(time.monotonic()-self.begin)
        need(remaining>=wall+15 and (self.absolute-now()).total_seconds()>=wall+15,
             'original fixed admission refusal')
        output=self.writer/(label+'.payload')
        authpath=self.auth/(label+'.authority.json')
        args=[str(self.files[role])]+tail+['--registration',str(authpath)]
        outputs=[output]; extra_pin=None
        if role=='checker':
            input_name=input_pin if input_pin is not None else self.frozen/'startup-absent.input'
            args+=['--input',str(input_name),'--receipt',str(output)]
        elif role=='mutator':
            extra_pin=self.frozen/'positive.receipt.json'
            outputs=[self.writer/'uphi.json',self.writer/'bernstein.json',output]
            args+=['--input',str(input_pin),'--positive-receipt',str(extra_pin),
                   '--uphi',str(outputs[0]),'--bernstein',str(outputs[1]),'--receipt',str(output)]
        else:
            args+=['--output',str(output)]
        operation={'probe':'probe','producer':'produce','checker':'check','mutator':'mutate'}[role]
        authority_path,authority_sha=self.authority(label,args,operation,outputs,mutation,input_pin,extra_pin)
        self.authority_shas[label]=authority_sha
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
        if extra_pin is not None:
            pre['positive_receipt_sha256']=sha(extra_pin)
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
        if extra_pin is not None:
            need(sha(immutable(extra_pin,True))==pre['positive_receipt_sha256'],'post positive receipt drift')
        need(now()<self.absolute,'post-return original UTC deadline')
        if math_phase:
            need(time.monotonic()-self.math_begin<=600,'post-return joint wall exceeded')
            usage=resource.getrusage(resource.RUSAGE_CHILDREN)
            accounted=usage.ru_utime+usage.ru_stime-self.math_cpu_start
            need(accounted<=550,'conservative aggregate CPU including wrappers exceeded')
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
        t,out,err,payload=self.run('produce','producer',['--job',JOB],'produce',math_phase=True)
        need(t['child_returncode'] in (0,2),'producer return')
        self.normal(t,t['child_returncode'])
        need(payload.is_file() and not payload.is_symlink() and payload.stat().st_size<=LIMIT-4096,
             'complete producer artifact required')
        before_sha=sha(payload); size=payload.stat().st_size
        label='CANDIDATE' if t['child_returncode']==0 else 'INCONCLUSIVE'
        need(err.read_bytes()==b'' and out.read_text()==
             'PRODUCER_'+label+' sha256='+before_sha+' bytes='+str(size)+'\n',
             'exact complete producer output binding')
        target=self.freeze(payload,'certificate.json',before_sha)
        t,out,err,receipt=self.run('check','checker',['--job',JOB],'check',input_pin=target,math_phase=True)
        need(t['child_returncode'] in (0,2),'checker return')
        self.normal(t,t['child_returncode'])
        result=read_json(receipt,4096)
        common={'schema','status','input_sha256','code','registration_sha256'}
        need(result.get('schema')=='f10-contact-gram-check/v1' and result.get('code')==CODE
             and result.get('input_sha256')==before_sha
             and result.get('registration_sha256')==self.authority_shas['check'],
             'checker receipt bindings')
        need(err.read_bytes()==b'' and out.read_text()==result['status']+'\n','checker exact streams')
        if t['child_returncode']==2:
            need(set(result)==common|{'reason'} and result['status']=='INCONCLUSIVE'
                 and result['reason'] in (
                 'nonpositive endpoint; full identity and expansion checked',
                 'negative Bernstein coefficient; full identity and expansion checked'),
                 'complete checked inconclusive receipt required')
            terminal_receipt=self.freeze(receipt,'checked-inconclusive.receipt.json',sha(receipt))
            return self.result('CHECKED_INCONCLUSIVE_NO_SOURCE_OUTCOME',before_sha,sha(terminal_receipt),False)
        need(set(result)==common|{'scope','identity','j','degree_t','degree_v','bernstein_entries','retained_edges'}
             and result['status']=='PRESCRIBED_CONTACT_EXCLUDED_BY_CERTIFICATE'
             and result['scope']=='prescribed triangle t<1 only; not full-window equivalence, source or JC2'
             and result['identity']=='full contact cofactor identity; Gram determinant equality NOT independently checked'
             and result['degree_v']=='52' and result['retained_edges']==['t=0','v=0','v=1'],
             'positive exact status/scope')
        for key in ('j','degree_t','bernstein_entries'):
            need(type(result[key]) is str and re.fullmatch(r'(0|[1-9][0-9]{0,3})',result[key]),
                 'bounded receipt integer strings')
        j=int(result['j'])
        need(0<=j<=52 and int(result['degree_t'])==52-j
             and int(result['bernstein_entries'])==(53-j)*53,'positive rectangle receipt')
        positive=self.freeze(receipt,'positive.receipt.json',sha(receipt))
        t,out,err,receipt=self.run('mutate','mutator',['--job',JOB],'mutate',input_pin=target,math_phase=True)
        self.normal(t,0)
        need(out.read_bytes()==b'TWO_MUTATIONS_PREPARED_NO_SCIENCE\n' and err.read_bytes()==b'',
             'mutator exact normal streams')
        mr=read_json(receipt,32768)
        keys={'schema','status','input_sha256','input_bytes','code','science','mutator_sha256',
              'positive_receipt_sha256','registration_sha256','variants','whole_byte_inverse_restored'}
        need(set(mr)==keys and mr['schema']=='f10-contact-gram-mutations/v1'
             and mr['status']=='TWO_MUTATIONS_PREPARED_NO_SCIENCE'
             and mr['input_sha256']==before_sha and type(mr['input_bytes']) is int and mr['input_bytes']==size
             and mr['code']==CODE and mr['science']==SCIENCE
             and mr['mutator_sha256']==ROLE_PINS['mutator']
             and mr['positive_receipt_sha256']==sha(positive)
             and mr['registration_sha256']==self.authority_shas['mutate']
             and mr['whole_byte_inverse_restored'] is True,'mutator receipt bindings')
        need(type(mr['variants']) is list and len(mr['variants'])==2,'exactly two variants')
        variants=[]; hashes={before_sha}
        for index,(control,name) in enumerate((('Uphi+1','uphi.json'),('Bernstein+1','bernstein.json'))):
            item=mr['variants'][index]; original=self.writer/name
            base={'control','path','sha256','bytes','old','new'}
            extra={'constant_existed','term_deleted'} if index==0 else {'row','column'}
            need(type(item) is dict and set(item)==base|extra and item['control']==control
                 and item['path']==str(original),'variant exact selection/path')
            if index==0:
                need(type(item['constant_existed']) is bool and type(item['term_deleted']) is bool,
                     'cofactor slot metadata')
            else:
                need(type(item['row']) is int and type(item['column']) is int
                     and item['row']==item['column']==0,'fixed existing Bernstein entry')
            for field in ('old','new'):
                pair=item[field]
                need(type(pair) is list and len(pair)==2 and all(type(v) is str and len(v)<=4096 for v in pair)
                     and re.fullmatch(r'(0|-?[1-9][0-9]*)',pair[0])
                     and re.fullmatch(r'[1-9][0-9]*',pair[1]),'canonical pair metadata only')
            need(item['old']!=item['new'] and type(item['bytes']) is int and 0<item['bytes']<=LIMIT-4096
                 and original.is_file() and not original.is_symlink()
                 and item['bytes']==original.stat().st_size and item['sha256']==sha(original)
                 and item['sha256'] not in hashes,'actual changed variant bytes')
            hashes.add(item['sha256'])
            variants.append(self.freeze(original,name,item['sha256']))
        need(size+sum(p.stat().st_size for p in variants)+receipt.stat().st_size<=LIMIT,
             'triple copies within aggregate bound')
        for label,input_path,message in (
            ('negative-uphi',variants[0],'full contact cofactor identity'),
            ('negative-bernstein',variants[1],'full Bernstein expansion')):
            t,out,err,absent=self.run(label,'checker',['--job',JOB],'negative',
                                    input_pin=input_path,math_phase=True)
            self.normal(t,2)
            need(not absent.exists() and not absent.is_symlink() and out.read_bytes()==b''
                 and err.read_text()=='INCONCLUSIVE: '+message+'\n','exact semantic negative, no receipt')
        return self.result('CONTACT_CERTIFICATE_CHECKED_NEGATIVES_CONFIRMED',before_sha,sha(positive),True)

    def freeze(self,source,name,expected):
        need(source.is_file() and not source.is_symlink() and sha(source)==expected,'source freeze pin')
        target=self.frozen/name
        need(not target.exists() and not target.is_symlink(),'absent frozen target')
        os.rename(source,target); os.chown(target,0,0); os.chmod(target,0o444)
        need(sha(immutable(target,True))==expected,'frozen move/readback pin')
        for parent in (self.writer,self.frozen):
            fd=os.open(parent,os.O_RDONLY); os.fsync(fd); os.close(fd)
        return target

    def result(self,status,source_sha,receipt_sha,controls):
        self.group_quiet(); self.revalidate()
        used=resource.getrusage(resource.RUSAGE_CHILDREN); own=resource.getrusage(resource.RUSAGE_SELF)
        elapsed=time.monotonic()-self.math_begin
        accounted=used.ru_utime+used.ru_stime-self.math_cpu_start
        need(elapsed<=600 and accounted<=550 and now()<self.absolute,'terminal phase budget')
        return {'status':status,'science':'NONE','checker_receipt_sha256':receipt_sha,
                'input_sha256':source_sha,'two_semantic_negatives_confirmed':controls,
                'math_window_wall_seconds':elapsed,'conservative_cpu_including_caprun_and_ps':accounted,
                'dispatcher_cpu_seconds_separate':own.ru_utime+own.ru_stime,
                'scope':'prescribed-contact certificate only; no source, determinant-equality or JC2 promotion'}

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
        manifest={'schema':'f10-contact-durable-custody/v1','utc':now().isoformat(),
                  'root_registration_sha256':self.root_sha,'result':result,'runs':self.runs,
                  'working_budget_bytes':LIMIT,'replicas_are_not_scientific_outputs':True,'files':records}
        write_json(self.durable/'CUSTODY.json',manifest)
        for parent,dirs,names in os.walk(self.durable,topdown=False):
            fd=os.open(parent,os.O_RDONLY); os.fsync(fd); os.close(fd)
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
    return 0 if result['status']=='CONTACT_CERTIFICATE_CHECKED_NEGATIVES_CONFIRMED' else 2

if __name__=='__main__':
    raise SystemExit(main())
