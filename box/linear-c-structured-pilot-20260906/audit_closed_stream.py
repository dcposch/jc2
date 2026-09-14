#!/usr/bin/env python3
"""Audit closed partial bytes after all writers terminate; no solve."""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import socket
import time
def require(ok,why):
    if not ok:raise ValueError(why)
require(platform.system()=="Linux" and socket.gethostname()=="ip-172-30-0-56","Worker")
require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","EC2")
require(os.environ.get("JC2_REGISTERED_JOB")=="linear-c-structured-pilot-astra-20260906","Registration")
require(Path.cwd()==Path("/home/ubuntu/linear-c-structured-pilot-20260906"),"Scratch")
from flint import fmpq_mpoly_ctx,fmpq_mpoly
started=time.monotonic()
tele=json.loads(Path("structured_retry.telemetry.json").read_text())
require(tele["status"] in ("NORMAL_EXIT","WALL_TIMEOUT","RESOURCE_CAP"),"Producer is not terminal")
if tele["status"]!="NORMAL_EXIT":require(tele["termination"]["cleanup_complete"] is True,"Cleanup not complete")
else:require(tele["child_returncode"]==0,"Unexpected producer error")
path=Path("prefix_reduced_ideal.jsonl")
if not path.exists():path=Path("prefix_reduced_ideal.partial.jsonl")
whole=hashlib.sha256()
with path.open("rb") as fh:
    for chunk in iter(lambda:fh.read(1024*1024),b""):whole.update(chunk)
count=terms=degree=0;labels=[];tail=0;footer=None;maxrow={"terms":0}
with path.open("rb") as fh:
    header=json.loads(next(fh));names=header["variables"]
    require(len(names)==575 and header["field"]=="Q","Ring")
    ctx=fmpq_mpoly_ctx.get(tuple(names),ordering="degrevlex")
    for line in fh:
        try:row=json.loads(line)
        except (json.JSONDecodeError,UnicodeDecodeError):
            require(not fh.read(),"Malformed line before EOF")
            tail=len(line);break
        if row["type"]=="terminal":
            footer=row;require(not fh.read(),"Data after terminal marker");break
        require(row["type"]=="generator" and row["index"]==count,"Generator sequence")
        p=fmpq_mpoly(row["polynomial"],ctx=ctx)
        require(bool(p) and len(p)==row["terms"] and int(p.total_degree())==row["degree"],"Exact polynomial metadata")
        count+=1;terms+=len(p);degree=max(degree,int(p.total_degree()));labels.append(row["label"])
        if row["label"].startswith("J_") and len(p)>maxrow["terms"]:
            maxrow={"label":row["label"],"terms":len(p),"degree":int(p.total_degree())}
        if count%200==0:print(json.dumps({"parsed":count,"terms":terms,"wall":time.monotonic()-started}),flush=True)
require(len(labels)==len(set(labels)) and sum(x.startswith("define_Hfact_") for x in labels)==160 and "inverse_J" in labels,"Definitions and inverse")
with Path("prefix_reconstruction.jsonl").open() as fh:
    ph=json.loads(next(fh));require(ph["variables"]==names,"Prefix ring")
    prefix=[]
    for line in fh:
        row=json.loads(line)
        if row["type"]=="complete":
            require(row["reconstructed"]==24 and not fh.read(),"Prefix footer");break
        p=fmpq_mpoly(row["polynomial"],ctx=ctx)
        require(len(p)==row["terms"] and int(p.total_degree())==row["degree"],"Prefix exact parse")
        require(row["index"]==len(prefix),"Prefix sequence")
        prefix.append({k:v for k,v in row.items() if k!="polynomial"})
    require(len(prefix)==24 and sum(x["terms"] for x in prefix)==414,"Prefix census")
j0=json.loads(Path("J0.json").read_text());p=fmpq_mpoly(j0["J0"],ctx=ctx)
require(j0["variables"]==names and len(p)==j0["terms"] and int(p.total_degree())==j0["degree"],"J0 exact parse")
result={"status":"CLOSED_PARTIAL_EXACT_PARSE_PASS" if not footer or footer["status"]!="COMPLETE_EXACT_PREFIX_REDUCED_IDEAL" else "CLOSED_COMPLETE_EXACT_PARSE_PASS",
        "producer_status":tele["status"],"producer_wall_seconds":tele["wall_elapsed_seconds"],
        "producer_sampled_peak_RSS_bytes":tele["max_observed_group_rss_bytes"],
        "stream_path":str(path.resolve()),"stream_bytes":path.stat().st_size,"stream_sha256":whole.hexdigest(),
        "complete_generators_exactly_parsed":count,"positive_J_generators":count-161,"literal_terms":terms,
        "maximum_ideal_degree":degree,"maximum_J_row":maxrow,
        "last_generator":labels[-1],"unparsed_final_tail_bytes":tail,"terminal_footer":footer,
        "all_remaining_rows_complete":bool(footer and footer["status"]=="COMPLETE_EXACT_PREFIX_REDUCED_IDEAL"),
        "prefix_reconstruction":prefix,"prefix_terms":414,"J0_terms":j0["terms"],"J0_degree":j0["degree"],
        "J0_linear_jet_check":j0["linear_jet_check"],"no_smaller_ideal_claim":True,"solver_launched":False,
        "wall_seconds":time.monotonic()-started,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path("closed_stream_audit.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
print(json.dumps(result,sort_keys=True),flush=True)
