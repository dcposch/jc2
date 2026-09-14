from pathlib import Path
import hashlib,json,datetime
root=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
ans=[]
for f in sorted(root.glob('**/status.json')):
 d=json.loads(f.read_text());q=Path(d['input']); checks=[]
 if 'input_sha256' in d:checks.append(dict(kind='input',path=str(q),ok=q.exists() and sha(q)==d['input_sha256']))
 for fn,val in d.get('outputs',{}).items():
  p=f.parent/fn;checks.append(dict(kind='output',path=str(p),ok=p.exists() and p.stat().st_size==val['bytes'] and sha(p)==val['sha256']))
 stop=f.parent/'manual-stop.json'
 ans.append(dict(status=str(f.relative_to(root)),state=d.get('state'),returncode=d.get('returncode'),host=d.get('host'),field=d.get('field'),representation=d.get('representation'),input=str(q),elapsed_seconds=d.get('elapsed_seconds'),memory_gib=d.get('memory_gib'),all_declared_hashes_match=all(t['ok'] for t in checks),checks=checks,manual_stop=json.loads(stop.read_text()) if stop.exists() else None))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),execution_count=len(ans),all_finished=all(d['state']=='FINISHED' for d in ans),all_declared_hashes_match=all(d['all_declared_hashes_match'] for d in ans),runs=ans)
(root/'resume-r2/execution-custody.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='runs'}))
for d in ans:
 if not d['all_declared_hashes_match'] or d['state']!='FINISHED':print(d['status'],d['state'],d['all_declared_hashes_match'],[c for c in d['checks'] if not c['ok']])
