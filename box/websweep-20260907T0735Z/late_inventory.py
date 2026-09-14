"""Close late discovery receipts, preserving the earlier coverage checkpoint."""
import datetime,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
rs=[]
for p in R.glob('batch*-receipts.json'):rs.extend(json.loads(p.read_text()))
rs.sort(key=lambda e:(e['ended_utc'],e['file']))
for e in rs:
 b=(R/e['file']).read_bytes()
 if len(b)!=e['bytes'] or sha(b)!=e['sha256']:raise ValueError(e['file'])
x=json.loads((R/'coverage.json').read_text())
x.update({'cutoff':max(e['ended_utc'] for e in rs),'requests':len(rs),
 'http_status_counts':{str(s):sum(e['status']==s for e in rs) for s in sorted(set(e['status'] for e in rs),key=str)},
 'errors':[e for e in rs if e['error'] or e['status']!=200]})
head=json.loads((R/'sources/furter-head.json').read_text())
x['heads']['furter']={'sha':head['sha'],'date':head['commit']['committer']['date'],'message':head['commit']['message']}
x['x_account_posts']=[]
s=(R/'sources/x-octonion.html').read_text()
for m in re.finditer(r'full_text:("(?:[^"\\]|\\.)*")',s):
 text=json.loads(m.group(1));dt=re.search(r'created_at_ms:(\d+)',s[m.end():m.end()+2500])
 if dt is None:raise ValueError('missing account-post timestamp')
 x['x_account_posts'].append({'utc':datetime.datetime.fromtimestamp(int(dt[1])/1000,datetime.timezone.utc).isoformat(),'text':text})
x['coverage_cautions']=['X global search remains a JS shell; nine account posts are partial recovery, not exhaustive replies/search coverage.',
 'Bluesky search remains HTTP403; Palomar web-public API still HTTP401 even with server-documented narrow. Both holes carried from 2026-09-03T10:17Z.',
 'arXiv publication times are not submission/update timestamps; Monday lists were read separately.',
 'Unfiltered Zenodo mostrecent/newest omitted date-scoped hits; use both date filters and direct records.',
 'Public listings can contain the excluded campaign repository; no protected contents were followed or inspected.']
for name,obj in [('coverage-final.json',x)]:
 with (R/name).open('xb') as f:f.write(json.dumps(obj,indent=2,sort_keys=True).encode()+b'\n')
with (R/'source-index-final.tsv').open('x') as f:
 f.write('filename\tbytes\tsha256\tended_utc\thttp\turl\n')
 for e in rs:f.write('\t'.join(str(e[k]) for k in ('file','bytes','sha256','ended_utc','status','url'))+'\n')
pins={str(p.relative_to(R)):{'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sorted(R.rglob('*')) if p.is_file()}
manifest={'schema':'jc2.websweep-custody/v1','cutoff':x['cutoff'],'network_writers_terminal':True,'arithmetic_jobs':0,'remote_state_changes':0,'protected_contents_read':False,'files':pins}
with (R/'custody.json').open('xb') as f:f.write(json.dumps(manifest,indent=2,sort_keys=True).encode()+b'\n')
print(json.dumps({'requests':len(rs),'cutoff':x['cutoff'],'status':x['http_status_counts'],'files':len(pins),'pins':{n:sha((R/n).read_bytes()) for n in ('coverage-final.json','source-index-final.tsv','custody.json')}},indent=2))
