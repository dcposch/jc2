#!/usr/bin/env python3
"""DISABLED client-specific ROOT caller; no registration is supplied here."""
import datetime, hashlib, json, math, os, pathlib, stat, subprocess, sys
from fractions import Fraction

JOB="f10-mixed-univariate-bezout-20260912"
LABELS=("dummy","parser-negative","produce","check-positive","identity-negative","exception-negative")
def need(x,s):
    if not x: raise ValueError(s)
def digest(b): return hashlib.sha256(b).hexdigest()
def canon(x): return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")
def pairs(rows):
    d={}
    for k,v in rows: need(k not in d,"duplicate key"); d[k]=v
    return d
def read(path,limit):
    fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
    with os.fdopen(fd,"rb") as f:
        s=os.fstat(f.fileno()); need(stat.S_ISREG(s.st_mode) and s.st_size<=limit,"bounded regular input")
        b=f.read(limit+1); need(len(b)<=limit,"input cap"); return b
def frozen(path,sha,limit=268435456):
    p=pathlib.Path(path); need(p.is_absolute() and str(p.resolve())==path,"canonical path")
    s=p.stat(); need(s.st_uid==0 and s.st_mode&0o022==0,"immutable ROOT input")
    b=read(path,limit); need(digest(b)==sha,"pin mismatch"); return b
def exclusive(path,b):
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,"wb") as f: f.write(b); f.flush(); os.fsync(f.fileno())
    os.chmod(path,0o444)
    need(read(path,len(b))==b,"write readback"); return digest(b)
def utc(s): return datetime.datetime.fromisoformat(s)
def now(): return datetime.datetime.now(datetime.timezone.utc)
def mutate_identity(raw):
    d=json.loads(raw,object_pairs_hook=pairs); rows=d["A1"]
    terms={(int(i),int(j)):Fraction(*map(int,q.split("/"))) for i,j,q in rows}
    terms[(0,0)]=terms.get((0,0),Fraction(0))+1
    d["A1"]=[[str(i),str(j),str(q.numerator)+"/"+str(q.denominator)] for (i,j),q in sorted(terms.items()) if q]
    return canon(d)
def times_factor(rows):
    out={}
    for st,sx,sq in rows:
        q=Fraction(*map(int,sq.split("/"))); i,j=int(st),int(sx)
        out[(i+1,j)]=out.get((i+1,j),Fraction(0))+7*q
        out[(i,j)]=out.get((i,j),Fraction(0))-12*q
    return [[str(i),str(j),str(q.numerator)+"/"+str(q.denominator)] for (i,j),q in sorted(out.items()) if q]
def mutate_exception(raw):
    d=json.loads(raw,object_pairs_hook=pairs)
    for k in ("A1","A2","N"): d[k]=times_factor(d[k])
    return canon(d)

def main():
    need(os.geteuid()==0 and len(sys.argv)==5 and sys.argv[1]=="--registration" and sys.argv[3]=="--sha256","ROOT CLI")
    raw=frozen(sys.argv[2],sys.argv[4],65536); r=json.loads(raw,object_pairs_hook=pairs)
    keys={"schema","enabled","job","worker","boot_id","hostname","not_before","deadline","uid","gid","paths","pins","native_manifest","library_paths","qualification","caps"}
    need(set(r)==keys and r["schema"]=="f10-mixed-univariate-runtime/v1" and r["enabled"] is True and r["job"]==JOB,"registration")
    need(sys.platform=="linux" and pathlib.Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","AWS")
    need(pathlib.Path("/sys/class/dmi/id/board_asset_tag").read_text().strip()==r["worker"] and os.uname().nodename==r["hostname"],"host")
    need(pathlib.Path("/proc/sys/kernel/random/boot_id").read_text().strip()==r["boot_id"],"boot")
    need(utc(r["not_before"])<=now()<utc(r["deadline"]) and (utc(r["deadline"])-utc(r["not_before"])).total_seconds()<=3540,"original wall")
    need(r["caps"]=={"wall":3540,"cpu_quota":"80000 100000","cpu_burst":"0","memory":34359738368,"tmpfs":268435456},"caps")
    p=r["paths"]; need(set(p)=={"work","tmpfs","admin","python","setpriv","caprun","authority","produce","check","probe"},"paths")
    pins=r["pins"]; need(set(pins)==set(p)-{"work","tmpfs","admin"},"pin vector")
    for k in pins: frozen(p[k],pins[k],67108864)
    work=pathlib.Path(p["work"]); tmp=pathlib.Path(p["tmpfs"]); admin=pathlib.Path(p["admin"])
    need(work.is_dir() and tmp.is_dir() and admin.is_dir() and str(work.resolve())==str(work) and str(tmp.resolve())==str(tmp) and str(admin.resolve())==str(admin),"directories")
    need(os.stat(work).st_uid==0 and os.stat(work).st_mode&0o022==0,"immutable work")
    need(os.stat(tmp).st_uid==r["uid"] and os.stat(tmp).st_mode&0o077==0,"private output tmpfs")
    need(os.stat(admin).st_uid==0 and os.stat(admin).st_mode&0o077==0,"private ROOT admin")
    # ROOT qualification is the reviewed physical proof of cgroup ancestry,
    # cpu.max/burst, memory.max, tmpfs mount/size, native/import closure and timer.
    q=r["qualification"]; frozen(q["path"],q["sha256"],65536)
    n=r["native_manifest"]; frozen(n["path"],n["sha256"],262144)
    need(type(r["library_paths"]) is list and 1<=len(r["library_paths"])<=4,"libraries")
    for x in r["library_paths"]: need(pathlib.Path(x).is_dir() and os.stat(x).st_uid==0 and os.stat(x).st_mode&0o022==0,"library ancestry")
    common={"schema":"f10-mixed-univariate-authority/v1","enabled":True,"job":JOB,"worker":r["worker"],"boot_id":r["boot_id"],"hostname":r["hostname"],"not_before":r["not_before"],"deadline":r["deadline"],"limits":{"wall":3600,"cpu":3300,"memory":34359738368,"wire":268435456},"sources":{p[k]:pins[k] for k in ("authority","produce","check","python")},"native_manifest":n,"library_paths":r["library_paths"],"qualification":q}
    records=[]
    def run(label,role,input_path=None,input_sha=None,expect=0,rss=32212254720,cpu=3290,script=None,extra=None):
        need(label==LABELS[len(records)] and now()<utc(r["deadline"]),"phase/order/deadline")
        base=str(tmp/(label+".")); out=base+"output.json"; receipt=base+"receipt.json"; auth=str(admin/(label+".authority.json"))
        science=[p["python"],"-E","-s","-S","-B",script,"--job",JOB,"--authority",auth,"--authority-sha256","ROOT_AUTHORITY_SHA256","--output",out,"--receipt",receipt]
        if input_path is not None: science += ["--input",input_path]
        a=dict(common); a.update({"role":role,"argv":science[5:],"input_sha256":input_sha})
        ab=canon(a); ash=exclusive(auth,ab); science[11]=ash
        cmd=[p["python"],p["caprun"],"--wall-seconds",str(max(1,int((utc(r["deadline"])-now()).total_seconds()))),"--cpu-seconds",str(cpu),"--rss-bytes",str(rss),"--stdout-file",base+"stdout","--stderr-file",base+"stderr","--telemetry-file",base+"telemetry.json","--cwd",str(tmp),"--",p["setpriv"],"--reuid="+str(r["uid"]),"--regid="+str(r["gid"]),"--clear-groups","--no-new-privs"]+science
        cp=subprocess.run(cmd,stdin=subprocess.DEVNULL,check=False)
        need(cp.returncode==expect and now()<utc(r["deadline"]),"phase result/deadline")
        tele=json.loads(read(base+"telemetry.json",65536),object_pairs_hook=pairs)
        need(tele["status"]=="NORMAL_EXIT" and tele["child_exit_code"]==expect,"CAPRUN terminal evidence")
        records.append({"label":label,"returncode":cp.returncode,"authority_sha256":ash,"telemetry_sha256":digest(read(base+"telemetry.json",65536)),"output_sha256":digest(read(out,16777216)) if os.path.exists(out) else None,"receipt_sha256":digest(read(receipt,32768)) if os.path.exists(receipt) else None})
        return out,receipt
    # Mandatory fresh descendant regression precedes every scientific import.
    base=str(tmp/"dummy.")
    dcmd=[p["python"],p["caprun"],"--wall-seconds","5","--cpu-seconds","3","--rss-bytes","33554432","--stdout-file",base+"stdout","--stderr-file",base+"stderr","--telemetry-file",base+"telemetry.json","--cwd",str(tmp),"--",p["setpriv"],"--reuid="+str(r["uid"]),"--regid="+str(r["gid"]),"--clear-groups","--no-new-privs",p["python"],"-E","-s","-S","-B",p["probe"],"--descendant-rss-term-kill"]
    cp=subprocess.run(dcmd,stdin=subprocess.DEVNULL,check=False); need(cp.returncode==125,"dummy cap")
    tele=json.loads(read(base+"telemetry.json",65536)); need(tele["status"]=="RESOURCE_CAP" and tele["resource"]=="rss" and tele["termination"]["term_sent"] and tele["termination"]["kill_sent"] and tele["termination"]["cleanup_complete"] and tele["termination"]["leader_reaped"] and not tele["termination"]["group_live_before_reap"],"dummy evidence")
    records.append({"label":"dummy","telemetry_sha256":digest(read(base+"telemetry.json",65536))})
    malformed=admin/"parser-negative.input.json"; exclusive(str(malformed),b'{"status":"PASS","executable":"exit(0)"}\n')
    po,pr=run("parser-negative","check",str(malformed),digest(read(str(malformed),65536)),1,script=p["check"])
    need(not os.path.exists(po) and not os.path.exists(pr),"parser negative branch")
    candidate,prodreceipt=run("produce","produce",script=p["produce"])
    cb=read(candidate,16777216); csha=digest(cb); os.chown(candidate,0,0); os.chmod(candidate,0o444)
    prod=json.loads(read(prodreceipt,32768),object_pairs_hook=pairs); need(prod["status"]=="CANDIDATE_UNCHECKED" and prod["artifact_sha256"]==csha,"producer receipt")
    co,cr=run("check-positive","check",candidate,csha,0,script=p["check"])
    checked=json.loads(read(co,32768),object_pairs_hook=pairs); need(checked["status"]=="MIXED_UNIT_ALL_INTEGER_R_CHECKED" and checked["artifact_sha256"]==csha,"positive checker receipt")
    ident=admin/"identity-negative.input.json"; ib=mutate_identity(cb); exclusive(str(ident),ib)
    io,ir=run("identity-negative","check",str(ident),digest(ib),1,script=p["check"])
    need(not os.path.exists(io) and not os.path.exists(ir),"identity negative branch")
    exc=admin/"exception-negative.input.json"; eb=mutate_exception(cb); exclusive(str(exc),eb)
    eo,er=run("exception-negative","check",str(exc),digest(eb),2,script=p["check"])
    exceptional=json.loads(read(eo,32768),object_pairs_hook=pairs); need(exceptional["status"]=="INCONCLUSIVE_ACTUAL_R_EXCEPTION" and exceptional["exceptional_r"]==["2"],"exception branch")
    summary={"schema":"f10-mixed-univariate-runtime-summary/v1","status":"CANDIDATE_AND_CONTROLS_COMPLETE_NOT_YET_ROOT_ACCEPTED","registration_sha256":digest(raw),"candidate_sha256":csha,"records":records}
    exclusive(str(admin/"SUMMARY.json"),canon(summary)); return 0
if __name__=="__main__":
    try: sys.exit(main())
    except Exception as e: print("STOP: "+str(e),file=sys.stderr); sys.exit(1)
