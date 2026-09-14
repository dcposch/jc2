#!/usr/bin/env python3
"""Terminal-only custody and compact artifact archive; no solve or row rebuild."""
import hashlib,json,os,subprocess,tarfile,time
from pathlib import Path
import payload
ROOT=payload.ROOT
auth,ready,identity=payload.identity()
def need(ok,s):
    if not ok:raise RuntimeError(s)
def sha(path):return payload.digest(path)

result=json.loads((ROOT/'construction.result.json').read_text())
telemetries={k:json.loads((ROOT/(k+'.telemetry.json')).read_text()) for k in ('construct','import')}
process_lines=subprocess.check_output(['ps','-eo','pid=,ppid=,pgid=,stat=,rss=,args='],text=True)
groups={}
for stage,t in telemetries.items():
    need(t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and t['error'] is None,'stage not successful')
    members=[]
    for line in process_lines.splitlines():
        fields=line.split(None,5)
        if len(fields)==6 and int(fields[2])==t['pgid']:members.append(line)
    need(not members,'stage group still has members')
    groups[stage]={'pid':t['pid'],'pgid':t['pgid'],'start_identity':t['start_identity'],
                   'process_path_absent':not Path('/proc',str(t['pid'])).exists(),'all_group_members':members,
                   'reaping_evidence':'CAPRUN normal branch calls process.wait before NORMAL_EXIT; false default termination.leader_reaped is cleanup-only telemetry defect'}
for name,digest in result['manifest']['files'].items():need(sha(ROOT/'complete'/name)==digest,'complete input changed')
need((ROOT/'import.stdout').read_bytes()==b'D125_IMPORT_ONLY_NO_SOLVE\n','unexpected import stdout/error text')
need((ROOT/'import.stderr').read_bytes()==b'','nonempty import stderr')
need((ROOT/'construct.stderr').read_bytes()==b'','nonempty construction stderr')
with (ROOT/'complete/literal.jsonl').open('rb') as f:header=json.loads(f.readline())
with (ROOT/'export-header.json').open('x') as f:json.dump(header,f,sort_keys=True,indent=2);f.write('\n')
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    need(not p.is_symlink(),'unexpected symlink in task artifacts')
    files.append({'path':str(p),'relative':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
custody={'schema':'jc2.d125-physical-export-pilot/v1','status':'TERMINAL_COMPLETE_IMPORT_ONLY',
 'utc':time.time(),'worker':auth['worker'],'root_retains_instance':True,'instance_actions_by_lane':[],
 'source_license':auth['normalization_license'],'normalization_gate_sha256':auth['normalization_gate_sha256'],
 'header_license_preserved':header['normalized_equivalence_status'],'authority_sha256':sha(ROOT/'authority.json'),
 'construction':result,'telemetries':telemetries,'groups':groups,'process_snapshot':process_lines,
 'audit_timeout_incident':{'read_only_reader_pid_pgid':1421,'local_ssh_timeout_seconds':60,
     'observed_state_after_timeout':'D, ~18MiB RSS; cold EBS read of retained source hashes',
     'reader_now_absent':not Path('/proc/1421').exists(),'signal_sent':False,
     'followup_readiness':'fresh read-only audit completed; both retained source hashes exact; no arithmetic retry'},
 'storage':{'mount':ready['mount'],'volume':'vol-0eb6450d18ffa89f1','ephemeral_files':[],
            'ebs_delete_on_termination':True,'stop_retains_files':True,'large_inputs_stay_remote':True},
 'all_artifacts':files,'owned_arithmetic_writers_terminal':True,
 'claim_boundary':'Complete self-replayed literal source ideal and successful exact-Q import only; no independent full certification, no GB/unit/properness/witness theorem'}
with (ROOT/'custody.json').open('x') as f:json.dump(custody,f,sort_keys=True,indent=2);f.write('\n')
# Mechanical archive, excluding only the two explicitly retained dense inputs.
with tarfile.open(ROOT/'evidence.tar','x') as tar:
    for rec in files:
        if rec['relative'] in ('complete/literal.jsonl','complete/import.sing'):continue
        tar.add(rec['path'],arcname=rec['relative'],recursive=False)
    tar.add(ROOT/'custody.json',arcname='custody.json',recursive=False)
for rec in files:os.chmod(rec['path'],0o444)
os.chmod(ROOT/'custody.json',0o444);os.chmod(ROOT/'evidence.tar',0o444)
print(json.dumps({'status':custody['status'],'groups':groups,'custody_sha256':sha(ROOT/'custody.json'),
 'archive_sha256':sha(ROOT/'evidence.tar'),'archive_bytes':(ROOT/'evidence.tar').stat().st_size,
 'large_inputs':result['manifest']['files'],'import_telemetry':telemetries['import']},sort_keys=True))
