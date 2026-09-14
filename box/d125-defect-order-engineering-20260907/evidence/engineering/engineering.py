"""Registered tiny EC2-only order controls. No complete-source reader is called."""
import datetime, json, math, os, resource, signal, subprocess, sys, time
from pathlib import Path
ROOT=Path('/home/ubuntu/d125-defect-order-solver-20260907')
ENG=ROOT/'engineering'
BOOT='375d1a40-5988-4999-8cb7-a5427ad3b3a0'
sys.path.insert(0,str(ROOT))
import driver as D
import exact as E
import defect_order as O
PINS={'driver.py':'944d5a840b6e4a81e89e5bcfa0ce6e6e54684ece70f182499735b9aa8571faec',
      'exact.py':'f452a1f6a3dfcc534a14a0d2b1f162589fc928973aff5a91f7faaa88921039af',
      'defect_order.py':'d5031c04fc7fdfec1fc57285b7538747b4d0aae25fae5ac140439d01dbd99ca3',
      'run_capped.py':'4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'}
GV=['x','y','z']; GO=O.descriptor(GV,[[3,1,4],[1,0,1],[1,0,1]])
GT=['x-y^2','z-y^3']
GP=O.ring_declaration(GO)+'ideal I='+','.join(GT)+';\n'
GH=E.digest(GP.encode())
JOBS=[]

def save(path,value): D.write_new(path,E.canonical(value))

def host():
    h=D.observed_host()
    E.need(h['system']=='Linux' and h['vendor']=='Amazon EC2' and h['instance']==D.INSTANCE
           and h['boot']==BOOT and Path.cwd().resolve() in (ROOT,ENG),'exact engineering host/cwd')
    for name,pin in PINS.items(): E.need(D.file_sha(ROOT/name)==pin,'frozen code drift '+name)
    frozen=E.strict_json((ENG/'frozen-inputs.json').read_bytes())
    for name,pin in frozen.items(): E.need(D.file_sha(ENG/name)==pin,'frozen engineering drift '+name)
    E.need(D.file_sha('/usr/bin/Singular')==D.BINARY_SHA,'binary drift')
    E.need(subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip()
           =='vol0eb6450d18ffa89f1','EBS serial drift')
    return h

def identity(label):
    h=host();D.limits('control')
    out={'pid':os.getpid(),'pgid':os.getpgrp(),'start_ticks':Path('/proc/self/stat').read_text().rsplit(') ',1)[1].split()[19],
         'boot':BOOT,'host':h,'cgroup':Path('/proc/self/cgroup').read_text(),'namespace':os.readlink('/proc/self/ns/pid'),
         'argv':sys.argv,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'limits':{'AS':resource.getrlimit(resource.RLIMIT_AS),'FSIZE':resource.getrlimit(resource.RLIMIT_FSIZE),
                   'CORE':resource.getrlimit(resource.RLIMIT_CORE),'CPU':resource.getrlimit(resource.RLIMIT_CPU)}}
    save(ENG/(label+'.identity.json'),out);return out

def empty(pgid):
    for attempt in range(30):
        lines=subprocess.check_output(['ps','-eo','pid=,pgid=,stat='],text=True).splitlines()
        if not any(int(line.split()[1])==pgid for line in lines):return True
        time.sleep(.05)
    return False

def payload(mode):
    label=('replay-normal' if __debug__ else 'replay-optimized') if mode=='replay' else mode
    identity(label)
    if mode=='rss':
        read,write=os.pipe();child=os.fork()
        if child==0:
            os.close(read);signal.signal(signal.SIGTERM,signal.SIG_IGN)
            identity('rss-descendant');os.write(write,b'R');os.close(write)
            time.sleep(.2);buffer=bytearray(b'X'*(96*1024**2))
            while buffer:time.sleep(1)
            os._exit(0)
        os.close(write);E.need(os.read(read,1)==b'R','child not ready');os.close(read)
        print(json.dumps({'parent':os.getpid(),'child':child,'pgid':os.getpgrp()}),flush=True);os._exit(0)
    if mode in ('levels','graph'):
        if mode=='levels':
            order=O.descriptor(['x','y','z','t','u'],[[2,1,2,2,2],[1,0,0,1,0],[1,0,0,0,0]])
            script=O.ring_declaration(order)+'short=0;\nprint("LEVELS_BEGIN");print(attrib(basering,"global"));\n'
            script+='\n'.join('print(string(lead('+p+')));' for p in ['x+y','x+z','x+t','y^2+z','z+u'])
            script+='\nprint("LEVELS_END");quit;\n'
        else:script=GP+D.footer(GV,GH,order=GO)
        E.need(len(script)<10000,'tiny script ceiling')
        D.write_new(ENG/(mode+'.sing'),script.encode())
        os.execv('/usr/bin/Singular',['Singular','--no-rc','-q',str(ENG/(mode+'.sing'))])
    if mode=='replay':
        E.need((ENG/'levels.stderr').read_bytes()==b'','levels stderr')
        E.need((ENG/'levels.stdout').read_text()=='LEVELS_BEGIN\n1\nx\nx\nx\ny^2\nz\nLEVELS_END\n','actual order levels/global')
        raw=(ENG/'graph.stdout').read_bytes();err=(ENG/'graph.stderr').read_bytes()
        engine,basis,cofactors=E.parse_result(raw,err,GV,GH,GO)
        rows=[E.polynomial(t,GV) for t in GT];mapping=E.engine_map(rows,engine)
        E.need(cofactors is None,'proper graph unexpectedly unit')
        verdict=E.proper_certificate(rows,basis,3,GO['weight_rows'])
        bad=raw.replace(O.digest(GO).encode(),E.ring_id(GV).encode(),1)
        try:E.parse_result(bad,err,GV,GH,GO)
        except ValueError:pass
        else:raise ValueError('actual bad graph header accepted')
        control=D.check_control((ROOT/'control.stdout').read_bytes(),(ROOT/'control.stderr').read_bytes())
        c=(ROOT/'control.stdout').read_bytes();cp='ring R=0,(x),dp;\nideal I='+','.join(D.CONTROL_TEXT)+';\n'
        ce,cg,ch=E.parse_result(c,b'',D.CONTROL_VARS,E.digest(cp.encode()))
        ch=[{} for _ in ch]
        try:E.unit_certificate([E.polynomial(t,D.CONTROL_VARS) for t in D.CONTROL_TEXT],ce,ch)
        except ValueError:pass
        else:raise ValueError('actual zeroed cofactors accepted')
        print(json.dumps({'status':'ACTUAL_OUTPUT_REPLAY_PASS','optimized':not __debug__,
              'levels':5,'graph_verdict':verdict,'graph_engine_to_source':mapping,'graph_basis_count':len(basis),
              'control':control,'bad_header_rejected':True,'zeroed_cofactors_rejected':True},sort_keys=True));return
    raise ValueError('unregistered payload')

def run(label,argv,cwd,rss=512*1024**2):
    E.need(time.monotonic()<DEADLINE,'batch120-second deadline')
    wall=min(10,max(1,math.floor(DEADLINE-time.monotonic())))
    command=[sys.executable,'-I','-B',str(ROOT/'run_capped.py'),'--wall-seconds',str(wall),'--cpu-seconds',str(wall),
             '--rss-bytes',str(rss),'--term-grace-seconds','.25','--cwd',str(cwd),
             '--stdout-file',str(ENG/(label+'.stdout')),'--stderr-file',str(ENG/(label+'.stderr')),
             '--telemetry-file',str(ENG/(label+'.telemetry.json')),'--']+argv
    result=subprocess.run(command,capture_output=True,text=True)
    telemetry=E.strict_json((ENG/(label+'.telemetry.json')).read_bytes())
    item={'label':label,'command':command,'runner_rc':result.returncode,'runner_stdout':result.stdout,
          'runner_stderr':result.stderr,'telemetry':telemetry,'group_absent':empty(telemetry['pgid'])}
    JOBS.append(item);save(ENG/(label+'.receipt.json'),item)
    E.need(item['group_absent'] and telemetry['error'] is None,'lifecycle failure '+label)
    return item

def main():
    global DEADLINE
    host();identity('controller');DEADLINE=time.monotonic()+120;start=datetime.datetime.now(datetime.timezone.utc)
    save(ENG/'pre-pins.json',{**PINS,'Singular':D.file_sha('/usr/bin/Singular'),'engineering.py':D.file_sha(__file__)})
    argv=[sys.executable,'-I','-B',str(Path(__file__).resolve()),'payload']
    item=run('rss',argv+['rss'],ENG,rss=64*1024**2);t=item['telemetry'];term=t['termination']
    desc=E.strict_json((ENG/'rss-descendant.identity.json').read_bytes())
    E.need(item['runner_rc']==125 and t['status']=='RESOURCE_CAP' and t['resource']=='rss' and
           term['term_sent'] and term['kill_sent'] and term['leader_reaped'] and term['cleanup_complete']
           and desc['pgid']==t['pgid'],'descendant RSS/TERM/KILL control failed')
    for label in ('levels','graph'):
        item=run(label,argv+[label],ENG)
        E.need(item['runner_rc']==0 and item['telemetry']['status']=='NORMAL_EXIT' and
               item['telemetry']['child_returncode']==0 and (ENG/(label+'.stderr')).read_bytes()==b'',
               'tiny engine failed '+label)
        if label=='levels':
            E.need((ENG/'levels.stdout').read_text()=='LEVELS_BEGIN\n1\nx\nx\nx\ny^2\nz\nLEVELS_END\n',
                   'actual order levels/global')
        else:
            engine,basis,cofactors=E.parse_result((ENG/'graph.stdout').read_bytes(),b'',GV,GH,GO)
            E.need(cofactors is None,'graph unexpectedly unit')
            rows=[E.polynomial(t,GV) for t in GT];E.engine_map(rows,engine)
            E.proper_certificate(rows,basis,3,GO['weight_rows'])
    authority={'schema':D.AUTHORITY_SCHEMA,'root_green':True,'mode':'engineering_control',
          'execution_order_sha256':O.ORDER_SHA,'job_id':'d125-defect-order-engineering-20260907/zero-index',
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
    for label,flags in [('replay-normal',[]),('replay-optimized',['-O'])]:
        item=run(label,[sys.executable,'-I','-B',*flags,str(Path(__file__).resolve()),'payload','replay'],ENG)
        E.need(item['runner_rc']==0 and item['telemetry']['child_returncode']==0,'actual output replay failed')
    host();save(ENG/'post-pins.json',{**{name:D.file_sha(ROOT/name) for name in PINS},'Singular':D.file_sha('/usr/bin/Singular')})
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
