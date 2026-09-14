"""Tiny registered EC2-only controls; never loads the complete source or solves."""
import datetime, hashlib, json, math, os, resource, signal, subprocess, sys, time
from pathlib import Path
ROOT=Path('/home/ubuntu/d125-small-exact-solver-20260907')
ENG=ROOT/'engineering'
BOOT='69938ee6-48bb-4e45-bdf2-efb08c655368'
sys.path.insert(0,str(ROOT))
import driver as D
import exact as E
PINS={'driver.py':'7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d',
      'exact.py':'ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3',
      'run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'}
VARS=['long_gamma_coefficient_name_0123456789','long_pi_coefficient_name_9876543210']
TERMS=[f'({10**55+37*i}/{i+167})*{VARS[0]}^{i}*{VARS[1]}^{160-i}' for i in range(161)]
RATIONAL=f'{10**70+39}/1000000007'

def save(path,value):
    D.write_new(path,E.canonical(value))

def host():
    h=D.observed_host()
    E.need(h['system']=='Linux' and h['vendor']=='Amazon EC2' and h['instance']==D.INSTANCE
           and h['boot']==BOOT and Path.cwd().resolve() in (ROOT,ENG),'exact engineering host/cwd')
    for name,pin in PINS.items(): E.need(D.file_sha(ROOT/name)==pin,'frozen code drift '+name)
    E.need(D.file_sha('/usr/bin/Singular')==D.BINARY_SHA,'binary drift')
    E.need(subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip()
           =='vol0eb6450d18ffa89f1','EBS serial drift')
    return h

def identity(label):
    h=host(); f=Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()
    out={'pid':os.getpid(),'pgid':os.getpgrp(),'start_ticks':f[19],'boot':BOOT,'host':h,
         'cgroup':Path('/proc/self/cgroup').read_text(),'namespace':os.readlink('/proc/self/ns/pid'),
         'argv':sys.argv,'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    save(ENG/(label+'.identity.json'),out);return out

def empty(pgid):
    for attempt in range(30):
        lines=subprocess.check_output(['ps','-eo','pid=,pgid=,stat='],text=True).splitlines()
        found=[l for l in lines if int(l.split()[1])==pgid]
        if not found:return True
        time.sleep(.05)
    return False

def payload(mode):
    label=('replay-normal' if __debug__ else 'replay-optimized') if mode=='replay' else mode
    identity(label);D.limits('control')
    if mode=='rss':
        read,write=os.pipe();child=os.fork()
        if child==0:
            os.close(read);signal.signal(signal.SIGTERM,signal.SIG_IGN)
            identity('rss-descendant');os.write(write,b'R');os.close(write)
            time.sleep(.2);buffer=bytearray(b'X'*(96*1024**2))
            while buffer:time.sleep(1)
            os._exit(0)
        os.close(write);E.need(os.read(read,1)==b'R','child not ready');os.close(read)
        print(json.dumps({'parent':os.getpid(),'child':child,'pgid':os.getpgrp()}),flush=True)
        os._exit(0)
    if mode in ('stdout-limit','stderr-limit'):
        # Isolated in-memory parameter only; unchanged driver.limits code path.
        # Limit was already64MiB; lower hard/soft limit together is permitted.
        D.CAPS={**D.CAPS,'stream_bytes':4096};D.limits('control')
        fd=1 if mode=='stdout-limit' else 2
        program='import os,resource,signal\nif resource.getrlimit(resource.RLIMIT_FSIZE)!=(4096,4096) or resource.getrlimit(resource.RLIMIT_CORE)!=(0,0): raise RuntimeError("inherited limit drift")\nsignal.signal(signal.SIGXFSZ,signal.SIG_DFL);os.write('+str(fd)+',b"X"*8192);os.write('+str(fd)+',b"Y")'
        os.execv(sys.executable,[sys.executable,'-I','-B','-c',program])
    if mode=='long':
        script='ring R=0,('+','.join(VARS)+'),dp;\nshort=0;\npoly P='+'+'.join(TERMS)+';\n'
        script+='print("LONG_BEGIN");print(string(P));print("LONG_END");\n'
        script+='number q='+RATIONAL+';print("RATIONAL_BEGIN");print(string(q));print("RATIONAL_END");quit;\n'
        E.need(len(script)<100000 and not any(t in script for t in ('slimgb','std(','lift(')),'tiny print only')
        D.write_new(ENG/'long.sing',script.encode())
        os.execv('/usr/bin/Singular',['Singular','--no-rc','-q',str(ENG/'long.sing')])
    if mode=='replay':
        control=D.check_control((ROOT/'control.stdout').read_bytes(),(ROOT/'control.stderr').read_bytes())
        E.need((ENG/'long.stderr').read_bytes()==b'','long stderr')
        text=(ENG/'long.stdout').read_text();prefix='LONG_BEGIN\n';middle='\nLONG_END\nRATIONAL_BEGIN\n';end='\nRATIONAL_END\n'
        E.need(text.startswith(prefix) and text.endswith(end) and text.count(middle)==1,'long print framing')
        actual,rational=text[len(prefix):-len(end)].split(middle)
        E.need(E.polynomial(actual,VARS)==E.polynomial('+'.join(TERMS),VARS),'long exact polynomial mismatch')
        E.need(E.polynomial(rational,VARS)==E.polynomial(RATIONAL,VARS),'long rational mismatch')
        print(json.dumps({'status':'ACTUAL_OUTPUT_REPLAY_PASS','optimized':not __debug__,
                          'control':control,'long_terms':161,'long_total_degree':160},sort_keys=True))
        return
    raise ValueError('unregistered payload')

JOBS=[]
def run(label,argv,cwd,wall=10,rss=512*1024**2):
    E.need(time.monotonic()<DEADLINE,'batch120-second deadline')
    wall=min(wall,max(1,math.floor(DEADLINE-time.monotonic())))
    command=[sys.executable,'-I','-B',str(ROOT/'run_capped.py'),'--wall-seconds',str(wall),'--cpu-seconds',str(wall),
             '--rss-bytes',str(rss),'--term-grace-seconds','.25','--cwd',str(cwd),
             '--stdout-file',str(ENG/(label+'.stdout')),'--stderr-file',str(ENG/(label+'.stderr')),
             '--telemetry-file',str(ENG/(label+'.telemetry.json')),'--']+argv
    start=time.monotonic();result=subprocess.run(command,capture_output=True,text=True)
    telemetry=E.strict_json((ENG/(label+'.telemetry.json')).read_bytes())
    item={'label':label,'command':command,'runner_rc':result.returncode,'runner_stdout':result.stdout,
          'runner_stderr':result.stderr,'telemetry':telemetry,'group_absent':empty(telemetry['pgid']),
          'elapsed':time.monotonic()-start}
    JOBS.append(item);save(ENG/(label+'.receipt.json'),item)
    E.need(item['group_absent'] and telemetry['error'] is None,'lifecycle failure '+label)
    return item

def main():
    global DEADLINE
    host();identity('controller');DEADLINE=time.monotonic()+120;start=datetime.datetime.now(datetime.timezone.utc)
    save(ENG/'pre-pins.json',{**PINS,'Singular':D.file_sha('/usr/bin/Singular'),'engineering.py':D.file_sha(__file__)})
    argv=[sys.executable,'-I','-B',str(Path(__file__).resolve()),'payload']
    rss=run('rss',argv+['rss'],ENG,rss=64*1024**2)
    t=rss['telemetry'];term=t['termination'];desc=E.strict_json((ENG/'rss-descendant.identity.json').read_bytes())
    E.need(rss['runner_rc']==125 and t['status']=='RESOURCE_CAP' and t['resource']=='rss' and
           term['term_sent'] and term['kill_sent'] and term['leader_reaped'] and term['cleanup_complete']
           and desc['pgid']==t['pgid'],'descendant RSS/TERM/KILL control failed')
    for label,fd in [('stdout-limit','stdout'),('stderr-limit','stderr')]:
        item=run(label,argv+[label],ENG);t=item['telemetry']
        E.need(item['runner_rc']==128+signal.SIGXFSZ and t['status']=='SIGNAL' and t['child_signal']==signal.SIGXFSZ,
               'inherited file limit did not signal')
        E.need((ENG/(label+'.'+fd)).stat().st_size==4096 and
               (ENG/(label+'.'+('stderr' if fd=='stdout' else 'stdout'))).stat().st_size==0,'overflow stream length')
    now=datetime.datetime.now(datetime.timezone.utc)
    authority={'schema':'jc2.d125-exact-solver-authority/v1','root_green':True,'mode':'engineering_control',
          'job_id':'d125-small-exact-solver-engineering-20260907/actual-zero-index',
          'pins':D.pins(),'caps':D.CAPS,'instance_id':D.INSTANCE,'cwd':str(ROOT),'boot_id':BOOT,
          'started_utc':start.isoformat(),'deadline_utc':(start+datetime.timedelta(seconds=120)).isoformat()}
    save(ROOT/'control.authority.json',authority)
    command=[sys.executable,'-I','-B',str(ROOT/'driver.py'),'launch','--phase','control','--authority',str(ROOT/'control.authority.json')]
    result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    t=E.strict_json((ROOT/'control.telemetry.json').read_bytes())
    item={'label':'actual-index','command':command,'runner_rc':result.returncode,'runner_stdout':result.stdout,
          'runner_stderr':result.stderr,'telemetry':t,'group_absent':empty(t['pgid'])}
    JOBS.append(item);save(ENG/'actual-index.receipt.json',item)
    E.need(result.returncode==0 and t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and item['group_absent'],
           'frozen control driver failed')
    long=run('long',argv+['long'],ENG)
    E.need(long['runner_rc']==0 and long['telemetry']['child_returncode']==0,'long print engine failed')
    for label,flags in [('replay-normal',[]),('replay-optimized',['-O'])]:
        item=run(label,[sys.executable,'-I','-B',*flags,str(Path(__file__).resolve()),'payload','replay'],ENG)
        E.need(item['runner_rc']==0 and item['telemetry']['child_returncode']==0,'actual output replay failed')
    host();save(ENG/'post-pins.json',{**{name:D.file_sha(ROOT/name) for name in PINS},
              'Singular':D.file_sha('/usr/bin/Singular'),'engineering.py':D.file_sha(__file__)})
    save(ENG/'batch.result.json',{'status':'ALL_ENGINEERING_CONTROLS_PASS','start':start.isoformat(),
          'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':120-(DEADLINE-time.monotonic()),'jobs':JOBS})
    print('ALL_ENGINEERING_CONTROLS_PASS',flush=True)

if __name__=='__main__':
    if len(sys.argv)==3 and sys.argv[1]=='payload':payload(sys.argv[2])
    else:
        try:main()
        except BaseException as error:
            save(ENG/'failure.json',{'error':repr(error),'jobs':JOBS,'no_retry':True});raise
        finally:save(ENG/'terminal-jobs.json',{'jobs':JOBS,'groups_absent':all(j['group_absent'] for j in JOBS)})
