#!/usr/bin/env python3
"""Worker-only exact row parse and safe rational Singular serialization; no solve."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import socket
import time


def require(ok, why):
    if not ok: raise ValueError(why)


def safe_polynomial(text):
    require(re.search(r"\^\d+/", text) is None, "fraction after exponent")
    return re.sub(r"(?<![A-Za-z0-9_^])(\d+)/(\d+)", r"(\1/\2)", text)


def main():
    require(socket.gethostname() == "ip-172-30-0-56", "Allocated worker required")
    require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip() == "Amazon EC2", "EC2 required")
    require(os.environ.get("JC2_REGISTERED_JOB") == "factored-jacobian-pilot-astra-20260906", "Registration required")
    from flint import fmpq_mpoly, fmpq_mpoly_ctx
    started=time.monotonic()
    try:
        safe_polynomial("x^9/32768")
    except ValueError:
        pass
    else:
        raise ValueError("Unsafe-power negative control accepted")
    require(safe_polynomial("1/2*x^9-3/4*y") == "(1/2)*x^9-(3/4)*y", "Rational formatter control")
    partial=Path("complete_checked.sing.partial")
    target=Path("complete_checked.sing")
    require(not target.exists() and not partial.exists(), "No overwrite")
    export=json.loads(Path("complete_export.json").read_text())
    count=terms=graph_count=0
    labels=set()
    digest=hashlib.sha256()
    with Path("complete_export.generators.jsonl").open() as source, partial.open("w",buffering=1024*1024) as output:
        header=json.loads(next(source))
        require(header["field"]=="Q" and header["order"]=="global dp", "Ring mismatch")
        names=header["variables"]
        require(len(names)==len(set(names))==600 and names[-1]=="Zj", "Variable census")
        require(names==export["coordinate_order"] and header["source_sha256"]==export["source_sha256"], "Header/export map mismatch")
        ctx=fmpq_mpoly_ctx.get(tuple(names), ordering="degrevlex")
        gens=ctx.gens()
        auxiliary=[i for i,n in enumerate(names) if n.startswith("Hfact_")]
        require(len(auxiliary)==160,"Auxiliary census")
        output.write("ring R=0,("+",".join(names)+"),dp;\nideal I=\n")
        footer=None
        for line in source:
            row=json.loads(line)
            if row["type"]=="complete":
                footer=row
                require(not source.read().strip(),"Trailing undeclared data")
                break
            require(row["type"]=="generator" and row["index"]==count,"Row sequence")
            label=row["label"]
            require(label not in labels,"Duplicate label")
            labels.add(label)
            p=fmpq_mpoly(row["polynomial"],ctx=ctx)
            require(bool(p) and len(p)==row["terms"] and int(p.total_degree())==row["degree"],"Exact row parse mismatch")
            if label.startswith("define_"):
                variable=label[len("define_"):]
                i=names.index(variable)
                residual=p-gens[i]
                degrees=residual.degrees()
                require(all(degrees[j]<=0 for j in auxiliary+[len(names)-1]),"Non-monic/non-source auxiliary definition")
                graph_count+=1
            elif label=="inverse_J":
                j0=json.loads(Path("complete_export.J0.json").read_text())
                require(p==gens[-1]*fmpq_mpoly(j0["lifted"],ctx=ctx)-1,"Inverse-J row mismatch")
            else:
                require(re.fullmatch(r"J_\d+_\d+",label) is not None and label!="J_0_0","Wrong Jacobian row label")
                require(sum(map(int,label.split("_")[1:]))<=99,"Wrong physical degree")
            require("Zj" not in row["polynomial"] or label=="inverse_J","Undeclared inverse use")
            safe=safe_polynomial(row["polynomial"])
            # Reparse the wrapped form in the independent native parser too.
            require(fmpq_mpoly(safe,ctx=ctx)==p,"Rational wrapping changed polynomial")
            output.write(("," if count else "")+safe+"\n")
            digest.update(line.encode())
            count+=1;terms+=len(p)
            if count%200==0:
                print(json.dumps({"rows":count,"terms":terms,"wall":time.monotonic()-started,"rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
        require(footer is not None and graph_count==160 and count==1629,"Missing full footer/census")
        require(count==footer["generators"] and terms==footer["terms"] and digest.hexdigest()==footer["generator_stream_sha256"],"Full stream mismatch")
        require(footer==export["complete_ideal"],"Export metadata mismatch")
        output.write(';\nprint("ALL_ROWS_PARSED"); print("GENERATORS="+string(size(I))); print("VARIABLES="+string(nvars(basering))); print("TERM_COUNT="+string(sum(size(I[1..size(I)])))); print("END_PARSE"); quit;\n'.replace(' print("TERM_COUNT="+string(sum(size(I[1..size(I)]))));',''))
        output.flush();os.fsync(output.fileno())
    os.replace(partial,target)
    raw_digest=hashlib.sha256()
    with target.open("rb") as source:
        for chunk in iter(lambda:source.read(1024*1024),b""):raw_digest.update(chunk)
    record={"status":"EXACT_PARSE_AND_SERIALIZATION_PASS","generators":count,"terms":terms,
            "monic_source_only_definitions":graph_count,"variables":600,"order":"global dp",
            "singular_path":str(target.resolve()),"singular_bytes":target.stat().st_size,
            "singular_sha256":raw_digest.hexdigest(),"wall_seconds":time.monotonic()-started,
            "peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "negative_control_unsafe_power_rejected":True,"solver_launched":False}
    Path("serialization_check.json").write_text(json.dumps(record,sort_keys=True,indent=2)+"\n")
    print(json.dumps(record,sort_keys=True),flush=True)


if __name__=="__main__":main()
