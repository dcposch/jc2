import sys
sys.dont_write_bytecode=True
import concurrent.futures,datetime,hashlib,json,urllib.request,urllib.error,resource,threading
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
threading.stack_size(262144)
ROOT=Path(__file__).resolve().parent
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fetch(item):
    name,url=item;start=utc();body=b'';status=None;error=None;final=url;headers={}
    if 'jc2-lean' in url.lower():raise RuntimeError('protected endpoint forbidden')
    try:
        q=urllib.request.Request(url,headers={'User-Agent':'JC2-literature-sweep/1.0 read-only','Accept':'*/*'})
        try:r=urllib.request.urlopen(q,timeout=12)
        except urllib.error.HTTPError as e:r=e
        with r:status=r.status;final=r.url;headers=dict(r.headers);body=r.read(5*1024*1024+1)
        if len(body)>5*1024*1024:raise RuntimeError('response cap5MiB')
    except Exception as e:error=type(e).__name__+': '+str(e)
    p=ROOT/'sources'/name;p.parent.mkdir(exist_ok=True)
    with p.open('xb') as f:f.write(body)
    out={'file':str(p.relative_to(ROOT)),'url':url,'final_url':final,'start':start,'end':utc(),'status':status,'error':error,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'headers':headers}
    print(json.dumps({k:v for k,v in out.items() if k!='headers'}),flush=True);return out
config=ROOT/sys.argv[1];items=json.loads(config.read_bytes())
if len(items)>12:raise RuntimeError('max12 requests per bounded batch')
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as p:rows=list(p.map(fetch,items))
with (ROOT/(config.stem+'-receipts.json')).open('xb') as f:f.write((json.dumps(rows,indent=2,sort_keys=True)+'\n').encode())
