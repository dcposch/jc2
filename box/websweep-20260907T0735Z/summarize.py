"""Replay only frozen public metadata; no network, mathematics or protected paths."""
import datetime, hashlib, html, json, re, xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(__file__).resolve().parent
S = ROOT / 'sources'
START = '2026-09-06T09:23:00Z'
NS = {'a':'http://www.w3.org/2005/Atom', 'o':'http://a9.com/-/spec/opensearch/1.1/'}
def read(name): return json.loads((S/name).read_text())
def sha(data): return hashlib.sha256(data).hexdigest()
def atom(name):
    r=ET.parse(S/name).getroot()
    rows=[{k:e.findtext('a:'+k,namespaces=NS) for k in ('id','title','updated','published')} for e in r.findall('a:entry',NS)]
    return {'total':int(r.findtext('o:totalResults',namespaces=NS)), 'rows':rows,
            'window_updates':[e for e in rows if e['updated']>=START]}
def clean(value): return html.unescape(re.sub('<[^>]*>',' ',value))
receipts=[]
for p in sorted(ROOT.glob('batch*-receipts.json')):
    receipts.extend(json.loads(p.read_text()))
for r in receipts:
    b=(ROOT/r['file']).read_bytes()
    if len(b)!=r['bytes'] or sha(b)!=r['sha256']: raise ValueError('receipt mismatch: '+r['file'])
out={'window_start':START,'cutoff':max(r['ended_utc'] for r in receipts),
     'requests':len(receipts),'http_status_counts':{str(s):sum(r['status']==s for r in receipts) for s in sorted(set(r['status'] for r in receipts),key=str)},
     'errors':[r for r in receipts if r['error'] or r['status']!=200],
     'arxiv':{p.name:atom(p.name) for p in sorted(S.glob('arxiv-*.xml'))},
     'authors':{p.name:atom(p.name) for p in sorted(S.glob('author-*.xml'))}}
out['monday']={}
for cat in ('AG','AC','CV'):
    st=(S/f'arxiv-math-{cat}-new.html').read_text()
    headings=[clean(t).strip() for t in re.findall(r'<h3.*?</h3>',st,re.S)]
    out['monday'][cat]={'headings':headings,'keyword_blocks':[]}
    for block in re.findall(r'<dd>.*?</dd>',st,re.S):
        txt=clean(block)
        if re.search(r'Jacobian|Keller|Hessian|polynomial automorph|Abhyankar',txt,re.I):
            out['monday'][cat]['keyword_blocks'].append(txt)
out['heads']={}
for name in ('supermind','strinz72','strinz75','collision','roy','ipitch','aejon','snap','caos','new-sma','new-opg'):
    e=read(name+'-head.json')
    if isinstance(e,list): e=e[0]
    out['heads'][name]={'sha':e['sha'],'date':e['commit']['committer']['date'],'message':e['commit']['message']}
out['branches']={name:read(name+'-branches.json') for name in ('strinz72','strinz75')}
old={e['id']:e for e in read('roy-math-status-old-correct.json')['entries']}
new={e['id']:e for e in read('roy-math-status.json')['entries']}
match=lambda e:bool(re.search(r'plane.?jc|jc2|hc4|Jacobian conjecture|Hessian conjecture',json.dumps(e),re.I))
changed=[k for k,v in new.items() if old.get(k)!=v]
out['roy']={'old_entries':len(old),'new_entries':len(new),'changed_entries':len(changed),
 'relevant_entries':sum(match(e) for e in new.values()),
 'changed_relevant':[k for k in changed if match(new[k]) or match(old.get(k,{}))],
 'removed_relevant':[k for k,v in old.items() if k not in new and match(v)],
 'plane_path_window':read('roy-plane-commits.json'),'extended_geometry_path_window':read('roy-hc4-commits.json'),
 'compare_commits':read('roy-compare.json')['total_commits'],'compare_files_returned':len(read('roy-compare.json')['files'])}
out['palomar']={}
for name in ('palomar-recent-final.json','palomar-14R15.json','palomar-math-AG.json'):
    es=read(name)['entries']
    # Public indexes may mention an excluded repository; do not follow or emit it.
    win=[e for e in es if e.get('published_at','')>=START and 'jc2-lean' not in json.dumps(e)]
    out['palomar'][name]={'entries':len(es),'window_entries':win}
out['zenodo']={}
for name in ('zenodo-jc-window.json','zenodo-jc-modified-window.json','zenodo-plane-window.json','zenodo-jc-cutoff.json'):
    h=read(name)['hits'];out['zenodo'][name]={'total':h['total'],'records':[{'id':e['id'],'created':e['created'],'updated':e['updated'],'title':e['metadata']['title']} for e in h['hits']]}
out['mastodon']={}
for name in ('masto-jc.json','masto-jacobian.json','masto-keller.json','masto-lean.json','masto-tao.json'):
    es=read(name);win=[e for e in es if e['created_at']>=START]
    out['mastodon'][name]={'returned':len(es),'newest':es[0]['created_at'] if es else None,'window_count':len(win),'window_keyword_hits':[{'id':e['id'],'created_at':e['created_at'],'text':clean(e['content'])} for e in win if re.search('Jacobian|Keller|Hessian',e['content'],re.I)]}
out['tao_feeds']={}
for name in ('tao-jc-rss.xml','tao-palomar-feed.xml'):
    out['tao_feeds'][name]=[{'date':e.findtext('pubDate'),'link':e.findtext('link'),'description':clean(e.findtext('description') or '')} for e in ET.parse(S/name).getroot().findall('./channel/item')]
out['stackexchange']={n:read(n) for n in ('mo-search.json','mse-search.json','mo-513413.json','mo-513413-answers.json','mo-user.json','mo-user-posts.json')}
with (ROOT/'coverage.json').open('xb') as f:f.write(json.dumps(out,indent=2,sort_keys=True).encode()+b'\n')
with (ROOT/'source-index.tsv').open('x') as f:
    f.write('filename\tbytes\tsha256\tended_utc\thttp\turl\n')
    for r in receipts:f.write('\t'.join(str(r[k]) for k in ('file','bytes','sha256','ended_utc','status','url'))+'\n')
pins={str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sorted((ROOT/'charged').iterdir()) if p.is_file()}
with (ROOT/'charged-pins.json').open('xb') as f:f.write(json.dumps(pins,indent=2,sort_keys=True).encode()+b'\n')
print(json.dumps({'requests':out['requests'],'cutoff':out['cutoff'],'statuses':out['http_status_counts'],'arxiv_window_updates':len(out['arxiv']['arxiv-jc-cutoff.xml']['window_updates']),'roy':out['roy'],'coverage_sha256':sha((ROOT/'coverage.json').read_bytes()),'source_index_sha256':sha((ROOT/'source-index.tsv').read_bytes())},indent=2))
