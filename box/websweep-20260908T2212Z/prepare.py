import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,datetime,hashlib,urllib.parse
R=Path('/home/ubuntu/jc2');B=Path(__file__).resolve().parent;OLD=R/'box/websweep-20260907T0735Z'
items=[]
for fn in ('batch1.json','batch2.json'):
    for name,url in json.loads((OLD/fn).read_bytes()):
        if name in ('new-sma-tree.json','new-opg-tree.json','strinz-repos.json','ipitch-repos.json','azofeifa.html'):continue
        url=url.replace('1788686580','1788767805')
        items.append((name,url))
items += [('tao-primary.html','https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/'),('gao-abs.html','https://arxiv.org/abs/2608.00222'),('gao-primary.html','https://arxiv.org/html/2608.00222v1'),('gao-primary.pdf','https://arxiv.org/pdf/2608.00222v1'),('shaska-primary.html','https://arxiv.org/html/2607.20210v2'),('furter-head.json','https://api.github.com/repos/blueberryvertigo/polynomial-composition-rigidity/commits?per_page=1'),('strinz75-head.json','https://api.github.com/repos/wstrinz/plane-jacobian-75-125/commits?per_page=1'),('strinz75-branches.json','https://api.github.com/repos/wstrinz/plane-jacobian-75-125/branches?per_page=100'),('gh-issues.json','https://api.github.com/search/issues?q=%22Jacobian+conjecture%22+updated:%3E2026-09-07&sort=updated&per_page=100')]
for q,tag in [('("Jacobian conjecture") AND (created:[2026-09-07 TO 2026-09-08])','zenodo-created'),('("Jacobian conjecture") AND (updated:[2026-09-07 TO 2026-09-08])','zenodo-updated'),('("plane Jacobian" OR "Keller map") AND (updated:[2026-09-07 TO 2026-09-08])','zenodo-plane-updated')]:
    items.append((tag+'.json','https://zenodo.org/api/records?'+urllib.parse.urlencode({'q':q,'size':25,'sort':'mostrecent'})))
for a in ('Orevkov','Guccione','Valqui','Horruitiner','Pissolato','Shaska','Migus','Jelonek','Xavier','Gao','Meng','Charbonnel','Kowalczyk','Alpoge','Ni','van Dobben','van den Essen','de Bondt','Zhao','Truong'):
    items.append(('author-'+a.replace(' ','-')+'.xml','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'au:"'+a+'"','sortBy':'lastUpdatedDate','sortOrder':'descending','max_results':10})))
for start in range(0,len(items),12):
    with (B/('batch'+str(start//12+1)+'.json')).open('xb') as f:f.write((json.dumps(items[start:start+12],indent=2)+'\n').encode())
pins=[]
for n in ('COORDINATION.md','APPROACHES.md','README.md','xmodel/websweep-20260907T0735Z-astra.md','xmodel/ideation-20260908T0200Z-synthesis.md'):
    p=R/n;b=p.read_bytes();q=B/('charged-'+p.name)
    with q.open('xb') as f:f.write(b)
    pins.append({'source':n,'snapshot':q.name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
with (B/'charged-pins.json').open('xb') as f:f.write((json.dumps(pins,indent=2)+'\n').encode())
print(json.dumps({'requests':len(items),'batches':(len(items)+11)//12}))
