"""Tiny terminal custody replay; no remote or source access."""
import hashlib,json,resource
from pathlib import Path
HERE=Path(__file__).resolve().parent;E=HERE/'evidence'/'engineering'
resource.setrlimit(resource.RLIMIT_CPU,(5,5));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
def need(ok,msg):
    if not ok:raise ValueError(msg)
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
remote=read(HERE/'remote-custody.json');batch=read(E/'batch-result.json')
need(remote['remaining']==[] and remote['production_outputs_absent'] and not remote['source_access'],'remote custody')
for relative,item in remote['files'].items():
    p=HERE/'evidence'/relative
    need(p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],'copy mismatch '+relative)
need(batch['status']=='ENGINEERING_ONLY_PASS' and batch['elapsed_seconds']<30 and
     batch['source_access'] is False and batch['construction_invoked'] is False,'batch status')
results=[]
for label in ('authorize','rss'):
    t=read(E/(label+'.telemetry.json'));r=read(E/(label+'.receipt.json'))
    a=read(E/(label+'.authority.json'));i=read(E/(label+'.identity.json'));launch=read(E/(label+'.launch.json'))
    argv=launch['argv'];payload=argv[len(argv)-6:]
    digest=hashlib.sha256((json.dumps(payload,ensure_ascii=False,separators=(',',':'))+'\n').encode()).hexdigest()
    need(digest==t['argv_sha256'],'CAPRUN actual argv mismatch')
    need(t['pid']==i['pid']==i['pgid']==t['pgid'] and i['host']['boot']==remote['boot'],'payload identity')
    need(t['start_identity']=='boot='+remote['boot']+';start_ticks='+i['start_ticks'],'start identity')
    need(i['limits']==dict(AS=[536870912,536870912],CPU=[10,10],CORE=[0,0],FSIZE=[134217728,134217728]),'actual limits')
    need(sha(E/(label+'.authority.json'))==i['authority_sha256']==launch['authority_sha256'],'authority custody')
    need(a['schema']=='jc2.d125-parity-engineering-authority/v1' and a['engineering_control_only'] is True,'authority role')
    need(a['registration_sha256']==sha(HERE/'evidence'/'REGISTRATION.md'),'registration pin')
    need(not r['group_members_after'] and r['runner_absent'] and not t['error'] and r['runner_stderr']=='','terminal scope')
    for suffix in ('stdout','stderr'):
        p=E/(label+'.'+suffix);need(p.stat().st_size==t[suffix]['bytes'] and sha(p)==t[suffix]['sha256'],'stream custody')
    need((E/(label+'.stderr')).read_bytes()==b'','payload stderr')
    if label=='authorize':
        q=read(E/'authorize.stdout');need(t['status']=='NORMAL_EXIT' and t['child_returncode']==r['runner_rc']==0 and
                    q['construction_invoked'] is False and q['source_read'] is False,'authorize result')
    else:
        term=t['termination'];d=read(E/'rss-descendant.identity.json')
        need(t['status']=='RESOURCE_CAP' and t['resource']=='rss' and r['runner_rc']==125 and
             term['term_sent'] and term['kill_sent'] and term['leader_reaped'] and term['cleanup_complete'] and
             d['pgid']==t['pgid'] and t['max_observed_group_rss_bytes']>67108864,'RSS cleanup result')
    results.append(dict(label=label,pid=t['pid'],pgid=t['pgid'],wall=t['wall_elapsed_seconds'],
                        max_rss=t['max_observed_group_rss_bytes'],status=t['status']))
print(json.dumps(dict(status='ACTUAL_ENGINEERING_RECEIPTS_REPLAY_PASS',optimized=not __debug__,
                      remote_files_verified=len(remote['files']),source_access=False,results=results),sort_keys=True))
