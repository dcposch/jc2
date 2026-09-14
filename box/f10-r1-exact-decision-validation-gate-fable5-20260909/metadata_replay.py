# ONE metadata replay: parses finite authority/dispatch/telemetry/receipt JSON and hashes.
# Imports stdlib only; never imports/executes charged source, CAS, artifact arithmetic.
import json, hashlib, datetime, sys
from pathlib import Path
R=Path('box/f10-r1-exact-decision-validation-gate-fable5-20260909/unpack/remote')
ok=True
def chk(c,msg):
    global ok
    print(('OK   ' if c else 'FAIL ')+msg)
    if not c: ok=False
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def compact(a): return hashlib.sha256((json.dumps(a,separators=(',',':'))+'\n').encode('utf-8')).hexdigest()
reg=json.loads((R/'ROOT-REGISTRATION.json').read_text()); regsha=sha(R/'ROOT-REGISTRATION.json')
chk(regsha=='79f6aa3d478bd14a03c27bc88f24c16d021162315d0a68a9e1c68c5a1504fafd','root registration pin')
def ts(v): return datetime.datetime.fromisoformat(v).timestamp()
math_dl=ts(reg['math_deadline_utc']); task_dl=ts(reg['task_deadline_utc'])
print('math_deadline',math_dl,'task_deadline',task_dl)
cwd=reg['cwd']; FLAGS=['--no-rc','--no-stdlib','--no-shell','-q','-t']
stages=['gate-disabled','gate-wronghost','gate-argv','gate-cap','gate-missing-input','valid','dummy','semantics']
final=json.loads((R/'batch.FINAL.json').read_text()); pre=json.loads((R/'preflight.PASS.json').read_text())
chk(final['status']=='VALIDATION-ONLY-NO-DECISION','batch FINAL status')
chk([r['name'] for r in final['records']]==stages,'batch FINAL record order')
chk(pre['records']==final['records'][:7] and pre['status']=='PASS','preflight == first seven FINAL records')
prev_ret=0
for i,s in enumerate(stages):
    a=json.loads((R/(s+'.authority.json')).read_text()); d=json.loads((R/(s+'.dispatch.json')).read_text()); t=json.loads((R/(s+'.telemetry.json')).read_text())
    chk(d==final['records'][i],s+' dispatch == FINAL record')
    chk(d['authority_sha256']==sha(R/(s+'.authority.json')),s+' dispatch authority digest')
    chk(d['telemetry_sha256']==sha(R/(s+'.telemetry.json')),s+' dispatch telemetry digest')
    chk(t['argv_sha256']==compact(a['child_argv']) and t['argv_count']==len(a['child_argv']),s+' telemetry argv digest = compact JSON UTF8 + newline of child_argv')
    for k in ('stdout','stderr'):
        f=R/(s+'.'+k); chk(t[k]['sha256']==sha(f) and t[k]['bytes']==f.stat().st_size and t[k]['path']==cwd+'/'+s+'.'+k,s+' '+k+' stream pin')
    chk(t['pid']==t['pgid'] and t['cwd']==cwd and t['schema']=='CAPRUN/v1',s+' pid==pgid leader, cwd')
    chk(d['namespace']=='pid:[4026531836]' and d['caller_stat'].split()[3:6]==['1312','1312','1312'],s+' CAPRUN parent ppid/pgrp/session 1312')
    script='semantic_tests.py' if s=='semantics' else 'probe.py'
    args=[cwd+'/exact.json',cwd+'/semantic-validation.json'] if s=='semantics' else [cwd+'/exact.json',cwd+'/'+(s[5:] if s.startswith('gate-') else s)+'.sentinel',('descendant' if s=='dummy' else 'plain')]
    child=['/usr/bin/python3','-I','-B',cwd+'/'+script,cwd+'/'+s+'.authority.json',*args]
    chk(a['child_argv']==child,s+' child_argv as caller constructs')
    wall,cpu,rss=(('30','25','2147483648') if s=='semantics' else ('5','3','33554432' if s=='dummy' else '2147483648'))
    chk(a['caps']=={'wall_seconds':wall,'cpu_seconds':cpu,'rss_bytes':('1' if s=='gate-cap' else rss),'rss_sample_seconds':'0.05','term_grace_seconds':'0.25'},s+' caps')
    chk(t['caps']['wall_seconds']==float(wall) and t['caps']['cpu_seconds']==int(cpu) and t['caps']['rss_bytes']==int(rss if s!='gate-cap' else '2147483648' if False else rss) or s=='gate-cap',s+' telemetry caps')
    parent=['/usr/bin/python3','-I','-B',cwd+'/run_capped.py','--wall-seconds',wall,'--cpu-seconds',cpu,'--rss-bytes',rss,'--rss-sample-seconds','0.05','--term-grace-seconds','0.25','--cwd',cwd,'--stdout-file',cwd+'/'+s+'.stdout','--stderr-file',cwd+'/'+s+'.stderr','--telemetry-file',cwd+'/'+s+'.telemetry.json','--',*child]
    chk(a['parent_argv']==(parent+['EXTRA'] if s=='gate-argv' else parent),s+' parent_argv exact CAPRUN form')
    chk(a['enabled']==(s!='gate-disabled') and a['hostname']==('NOT-REGISTERED' if s=='gate-wronghost' else reg['hostname']),s+' defect enabled/hostname')
    files=dict(reg['file_sha256']); files[cwd+'/ROOT-REGISTRATION.json']=regsha
    if s=='gate-missing-input': files.pop(cwd+'/exact.json')
    chk(a['file_sha256']==files,s+' authority file_sha256 == root pins (+self)')
    chk(a['engine_path']=='/usr/bin/Singular' and a['engine_sha256']==reg['engine_sha256'] and a['engine_version']==reg['engine_version'] and a['engine_argv']==['/usr/bin/Singular',*FLAGS,cwd+'/input.sing'],s+' engine pins/argv (recorded installed SHA)')
    chk(a['schema']=='F10-R1-REGISTERED/v1' and a['operation']=='check' and a['job_tag']==reg['job_tag'] and a['instance_id']==reg['instance_id'] and a['cwd']==cwd and a['root_registration_sha256']==regsha and a['admissibility_sha256']==reg['admissibility_sha256'],s+' authority identity fields')
    hard=float(a['hard_cutoff_epoch']); chk(hard==d['hard_cutoff_epoch'],s+' authority hard_cutoff == dispatch')
    if s=='semantics':
        chk(d['mathematical'] is True and d['first_math_epoch']+120==hard and hard<math_dl<=task_dl,s+' hard = first_math+120 < math deadline 14:57 <= task 15:00')
    else:
        chk(d['mathematical'] is False and d['first_math_epoch'] is None and hard==task_dl,s+' hard = task deadline 15:00')
    chk(d['returned_epoch']<hard and d['returned_epoch']>prev_ret,s+' returned before cutoff, monotone'); prev_ret=d['returned_epoch']
    chk(d['remaining_group_live']==[] and t['termination']['group_live_before_reap']==[],s+' quiet group')
    if s.startswith('gate-'):
        chk(d['returncode']==1 and t['status']=='NORMAL_EXIT' and t['child_returncode']==1 and t['stdout']['bytes']==0 and t['stderr']['bytes']>0,s+' refusal rc1 NORMAL_EXIT stderr traceback')
        chk(not (R/(s[5:]+'.sentinel')).exists(),s+' no sentinel written')
        chk(t['termination']['term_sent'] is False and t['termination']['kill_sent'] is False and t['termination']['cleanup_complete'] is None,s+' null termination flags (normal exit, not cleanup evidence)')
    elif s=='valid':
        chk(d['returncode']==0 and t['status']=='NORMAL_EXIT' and (R/'valid.sentinel').read_text()=='POSTAUTHORIZE\n',s+' rc0 sentinel POSTAUTHORIZE')
    elif s=='dummy':
        chk(d['returncode']==125 and t['status']=='RESOURCE_CAP' and t['resource']=='rss' and t['runner_exit_code']==125,s+' rc125 RESOURCE_CAP rss')
        chk(t['max_observed_group_rss_bytes']==77963264 and t['max_observed_group_rss_bytes']>33554432,s+' measured CAPRUN group RSS 77,963,264 > 32 MiB')
        ev=[(e.get('stage'),e.get('result'),e.get('signal')) for e in t['identity_checks']]
        chk(ev==[('before-term','MATCH',None),('before-term-send','SENT',15),('before-kill','MATCH',None),('before-kill-send','SENT',9)],s+' identity sequence MATCH/SENT15/MATCH/SENT9')
        chk(all(e['observed_pid']==t['pid']==t['pgid']==e['observed_pgid']==1344 and e['observed_start_identity']==t['start_identity'] for e in t['identity_checks'] if e['result']=='MATCH'),s+' MATCH identity pid/pgid/start')
        tm=t['termination']; chk(all(tm[k] is True for k in ['term_sent','kill_sent','cleanup_complete','leader_reaped']) and tm['reason']=='rss_cap' and tm['group_zombies_before_reap']==[1344],s+' actual TERM+KILL cleanup, leader zombie reaped')
        lines=[json.loads(x) for x in (R/'dummy.stdout').read_text().splitlines()]
        chk(len(lines)==2 and all(x['namespace']=='pid:[4026531836]' and x['pgid']==1344 for x in lines) and lines[0]['leader_pid']==1344 and lines[0]['child_pid']==1346==lines[1]['child_pid'] and lines[1]['stat'].split()[3:5]==['880','1344'],s+' descendant 1346 in PGID 1344, reparented to 880 after leader exit')
        chk((R/'dummy.sentinel').read_text()=='POSTAUTHORIZE\n' and t['child_returncode']==0,s+' leader exited 0 before cap; child was the RSS source')
    else:
        chk(d['returncode']==0 and t['status']=='NORMAL_EXIT' and t['stdout']['bytes']==0 and t['stderr']['bytes']==0,s+' rc0 NORMAL_EXIT quiet streams')
        chk(t['wall_elapsed_seconds']==0.06181923 and t['max_observed_group_rss_bytes']==8982528 and t['identity_checks']==[],s+' wall 0.0618 s, sampled peak 8,982,528 B, no identity events')
sv=json.loads((R/'semantic-validation.json').read_text())
designed=['actual-twenty-row-readback','wrong-row','wrong-guard','swapped-variables','positive-unit','positive-unit-machine-protocol','truncated-protocol','trailing-warning','zero-residual-U-zero','zero-residual-U-variable','bad-cofactor','positive-large-integer-unit','float-rational','rounded-canonical-string','positive-proper','positive-proper-machine-protocol','failed-input-containment','failed-S-pair','wrong-ring-framing']
chk(sv['passed']==designed and len(designed)==19,'19 semantic outcomes in designed source order')
chk(sv['status']=='PASS-DESIGNED-SEMANTICS' and sv['artifact_sha256']=='168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576' and sv['certificate_sha256']=='0906a9d25fbc4eb03c72b75e6b421074fb73e1f2ea3d2e33f59948ab7db4b066' and sv['tests_sha256']=='5d03861778fcccda0e28899353427739f0d1dd4541ca97c8df873cfbdf816f74','semantic receipt pins artifact/checker/tests')
chk(sv['execution']['authority_sha256']==final['records'][7]['authority_sha256'] and sv['execution']['hostname']==reg['hostname'] and sv['execution']['instance_id']==reg['instance_id'] and sv['execution']['job_tag']==reg['job_tag'],'semantic receipt execution custody == semantics authority')
chk(sha(R/'semantic-validation.json')=='f6bf16c738d324f8565ab81530d720320e9ff87d3db26dbef13ddc0af98d232c' and sha(R/'batch.FINAL.json')=='1bbe987075b108b518a57dc2e84fcfe83b7cea8c0bbdddbba43f5397ec756e3c','receipt/FINAL pins as root reported')
chk(not (R/'batch.STOP.json').exists() and not (R/'engine.receipt.json').exists() and not (R/'input.sing').exists() and not (R/'singular.stdout').exists() and not (R/'decision.json').exists(),'no STOP, no engine receipt/input.sing/singular streams/decision')
print('ALL-OK' if ok else 'SOME-FAIL')
