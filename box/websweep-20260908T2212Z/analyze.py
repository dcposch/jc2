import sys
sys.dont_write_bytecode=True
import json,xml.etree.ElementTree as ET,re,datetime,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent; OLD=P.parent/'websweep-20260907T0735Z'/'sources'; out={}
for f in sorted((P/'sources').iterdir()):
 try:
  if f.suffix=='.xml':
   t=ET.fromstring(f.read_bytes()); ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
   entries=[{k:e.findtext('a:'+k,default='',namespaces=ns) for k in ('id','title','updated','published','summary')} for e in t.findall('a:entry',ns)]
   out[f.name]={'total':t.findtext('o:totalResults',namespaces=ns),'entries':entries}
   if 'author-' not in f.name: print(f.name, out[f.name]['total'], [(e['id'],e['title'],e['updated']) for e in entries[:4]])
  elif f.suffix=='.json' and f.stat().st_size:
   t=json.loads(f.read_bytes()); name=f.name.removeprefix('retry-'); old=OLD/name; prev=json.loads(old.read_bytes()) if old.exists() and old.stat().st_size else None
   if 'head' in name:
    v=t[0] if isinstance(t,list) and t else t
    oldsha=prev[0]['sha'] if isinstance(prev,list) and prev else None
    out[f.name]={'sha':v.get('sha'),'oldsha':oldsha,'commit':v.get('commit')};print(f.name,out[f.name])
   elif name.startswith('zenodo'):
    hits=t.get('hits',{}); es=[{k:e.get(k) for k in ('id','created','updated','metadata','files','links')} for e in hits.get('hits',[])];out[f.name]={'total':hits.get('total'),'entries':es}
    print(f.name,hits.get('total'),[(e['id'],e['created'],e['updated'],e['metadata'].get('title')) for e in es[:6]])
   elif name.startswith('gh-'):
    out[f.name]=t;print(f.name,t.get('total_count'),[(e.get('full_name',e.get('title')),e.get('updated_at')) for e in t.get('items',[])[:12]])
   elif name.startswith(('mo-','mse-')):
    out[f.name]=t;print(f.name,[(e.get('title'),e.get('last_activity_date')) for e in t.get('items',[])])
   elif name.startswith('masto'):
    es=t if isinstance(t,list) else t.get('statuses',[]); recent=[e for e in es if e.get('created_at','')>'2026-09-07T07:56:45'];out[f.name]=recent
    print(f.name,len(es),'recent',len(recent),[(e.get('created_at'),re.sub('<[^>]+>',' ',e.get('content',''))[:700]) for e in recent[:6]])
 except Exception as e:out[f.name]={'parse_error':str(e)}
with (P/'analysis.json').open('wb') as f:f.write(json.dumps(out,indent=2).encode())
