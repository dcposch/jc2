"""Read-only bounded public fetches, exclusive snapshots and UTC/hash receipts."""
import concurrent.futures,datetime,hashlib,json,sys,urllib.request,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
def fetch(item):
    name,url=item;started=utc();body=b'';error=None;status=None;final=url;headers={}
    if 'jc2-lean' in url.lower():raise RuntimeError('protected endpoint forbidden')
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'JC2-literature-sweep/1.0 (read-only metadata)','Accept':'*/*'})
        try:r=urllib.request.urlopen(req,timeout=25)
        except urllib.error.HTTPError as exc:r=exc
        with r:
            status=r.status;final=r.url;headers=dict(r.headers);body=r.read(5*1024*1024+1)
        if len(body)>5*1024*1024:raise RuntimeError('5MiB response cap')
    except Exception as exc:error=type(exc).__name__+': '+str(exc)
    path=ROOT/'sources'/name;path.parent.mkdir(exist_ok=True)
    with path.open('xb') as f:f.write(body)
    result={'file':str(path.relative_to(ROOT)),'url':url,'final_url':final,'started_utc':started,'ended_utc':utc(),'status':status,'error':error,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'headers':headers}
    print(json.dumps({k:v for k,v in result.items() if k!='headers'}),flush=True)
    return result
if __name__=='__main__':
    config=ROOT/sys.argv[1];items=json.loads(config.read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:result=list(pool.map(fetch,items))
    with (ROOT/(config.stem+'-receipts.json')).open('xb') as f:f.write(json.dumps(result,indent=2,sort_keys=True).encode()+b'\n')
