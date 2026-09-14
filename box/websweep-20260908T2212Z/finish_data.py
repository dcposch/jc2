import sys
sys.dont_write_bytecode=True
import json,hashlib,datetime,re,resource
from pathlib import Path
from html.parser import HTMLParser
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
P=Path(__file__).resolve().parent;S=P/'sources';OLD=P.parent/'websweep-20260907T0735Z'/'sources'
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if t in ('p','div','li','h1','h2','h3','br','tr'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip:self.parts.append(s)
for n in ('alpo-original.html','zhang-consequences.html','supermind-primary.html','poisson-primary.html','arxiv-math-AG-new.html','arxiv-math-AC-new.html','arxiv-math-CV-new.html'):
 h=Plain();h.feed((S/n).read_text(errors='replace'));t='\n'.join(x.strip() for x in ''.join(h.parts).splitlines() if x.strip())
 with (P/(n+'.txt')).open('xb') as f:f.write(t.encode())
receipts=[r for f in sorted(P.glob('*-receipts.json')) for r in json.loads(f.read_bytes())]; latest={}
for r in sorted(receipts,key=lambda x:x['end']):
 if r['status']==200 and not r['error']:latest[r['url']]=r
config=[]
for f in sorted(P.glob('*.json')):
 try:
  v=json.loads(f.read_bytes())
  if isinstance(v,list) and v and all(isinstance(x,list) and len(x)==2 and isinstance(x[0],str) and str(x[1]).startswith('https://') for x in v):config+=v
 except Exception:pass
indexed={r['file'] for r in receipts};srcs=[]
for f in sorted(S.iterdir()):srcs.append({'file':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'has_complete_receipt':str(f.relative_to(P)) in indexed})
a=json.loads((S/'roy-current-math-status.json').read_bytes())['entries'];b={e['id']:e for e in json.loads((OLD/'roy-math-status.json').read_bytes())['entries']}
focus=lambda e:not e['id'].startswith('EC-') and bool(re.search('JC2|HC4|F2-|KELLER|JACOBIAN|PLANE',e['id'],re.I))
changed=[e['id'] for e in a if focus(e) and(e['id'] not in b or e!=b[e['id']])]
dirs=[]
for n in ('roy-old-plane-tree.json','roy-plane-tree.json'):dirs.append({e['name']:e['sha'] for e in json.loads((S/n).read_bytes())})
pal=json.loads((S/'retry-palomar-recent.json').read_bytes())['entries'];new=[e for e in pal if e.get('published_at','')>'2026-09-07T07:56:45Z' and 'jc2-lean' not in json.dumps(e)]
coverage={'start':'2026-09-08T22:10:47Z','previous_cutoff':'2026-09-07T07:56:45Z','cutoff':max(r['end'] for r in receipts),'status':'PARTIAL-COVERAGE','request_slots':len(config),'distinct_requested_urls':len(set(u for n,u in config)),'complete_receipts':len(receipts),'successful_distinct_urls':len(latest),'sources':srcs,'receipts':receipts,'unrecovered_urls':sorted(set(u for n,u in config)-set(latest)),'social_global_hole_since':'2026-09-03T10:17:00Z','roy':{'new_head':'c50e0069cc38206c8dfce85aae2a3d8db03ff54d','old_head':'a293bd94849d1131eae971c6c274323f02f14fc4','commits_between':84,'entries':len(a),'strict_matched_entries':sum(map(focus,a)),'changed_ids':changed,'plane_directory_entries':len(dirs[1]),'plane_blob_changes':[k for k in dirs[0].keys()|dirs[1].keys() if dirs[0].get(k)!=dirs[1].get(k)]},'palomar':{'recent_count':len(pal),'post_cutoff_nonprotected':[{'id':e['id'],'title':e['title'],'published_at':e['published_at']} for e in new]}}
with (P/'coverage.json').open('xb') as f:f.write(json.dumps(coverage,indent=2,sort_keys=True).encode())
with (P/'source-index.tsv').open('x') as f:
 f.write('file\tbytes\tsha256\tend\tstatus\turl\terror\n')
 for r in receipts:f.write('\t'.join(str(r.get(k,'')) for k in ('file','bytes','sha256','end','status','url','error'))+'\n')
print(json.dumps({k:v for k,v in coverage.items() if k not in ('sources','receipts','palomar')},indent=2))
