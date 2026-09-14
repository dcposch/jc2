#!/usr/bin/env python3
"""Literal Q source-coefficient exporter. Production requires explicit authority.

No solve, coefficient elimination, circuit variables, or implicit gauge.
JSONL monomials are [numerator-string, denominator-string, variable-id-list].
The empty variable list denotes 1. Repeated ids denote powers.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import comb
import os
from pathlib import Path
import resource
import time

SCHEMA = "jc2.d125-physical-literal/v1"
SOURCES = {
    "d125-client-interface-astra-20260906.md": "0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255",
    "d125-source-contract-gate-fable5-20260906.md": "a802587179b6f105bb47555ceb0e6a1d20c94c68a76c6ac4a26bbea1fce7b4e4",
    "d125-triangular-source-normalization-astra-20260906.md": "8ea55aaf26acbd4992aee9d14cce8712fda1c7590cd876ee974194c76bb3ad9e",
}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()

def digest_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def production_spec(mode):
    require(mode in ("original", "normalized"), "unknown production mode")
    return {"name": "D125", "mode": mode, "target": ["1", "5"],
            "sides": {"P": {"degree":75, "weight_cap":15, "terminal_h":3,
                              "vertical_cap":60, "guard":[15,60]},
                      "Q": {"degree":125, "weight_cap":25, "terminal_h":5,
                              "vertical_cap":100, "guard":[25,100]}},
            "pins": [["P",3,4,"1","1"], ["P",15,21,"1","1"],
                     ["Q",1,1,"-1","1"], ["Q",13,18,"-3","1"],
                     ["Q",25,35,"-9","5"]]}

def toy_spec(mode="original"):
    return {"name":"TOY_NOT_D125", "mode":mode, "target":["1","5"],
            "sides":{"P":{"degree":3,"weight_cap":5,"terminal_h":0,
                             "vertical_cap":2,"guard":[1,2]},
                     "Q":{"degree":4,"weight_cap":8,"terminal_h":1,
                             "vertical_cap":2,"guard":[2,2]}},
            "pins":[["P",3,3,"1","1"], ["P",-2,-1,"2","3"],
                    ["Q",8,8,"-1","1"], ["Q",-1,0,"-3","1"],
                    ["Q",2,3,"-9","5"]]}

def support(side, normalized):
    D,U=side["degree"],side["weight_cap"]
    result=[]
    for ell in range(-D,U+1):
        for i in range(max(0,-(-ell//5)),(D+ell)//6+1):
            j=5*i-ell
            if normalized and (j>side["vertical_cap"] or
                    (j==side["vertical_cap"] and i!=side["guard"][0])):
                continue
            require(i>=0 and j>=0 and i+j<=D and ell<=U,"bad source support")
            result.append((i,j))
    return result

def variables(spec):
    records=[]
    maps={}
    for side in ("P","Q"):
        maps[side]={}
        for i,j in support(spec["sides"][side],spec["mode"]=="normalized"):
            idx=len(records)
            maps[side][i,j]=idx
            records.append({"type":"variable","id":idx,"side":side,
                            "name":f"{side}_u{i}_v{j}", "source_exponent":[i,j],
                            "public_name":f"{side}_{5*i-j}_{i}",
                            "additive_constant":i==0 and j==0})
        require(tuple(spec["sides"][side]["guard"]) in maps[side],"missing degree endpoint")
        require(sum(spec["sides"][side]["guard"])==spec["sides"][side]["degree"],
                "degree endpoint is not on original total-degree boundary")
    records.append({"type":"variable","id":len(records),"side":"guard",
                    "name":"Z_degree_guard"})
    return records,maps

def term(c,ids=()):
    c=Fraction(c)
    require(c!=0,"zero term must not be encoded")
    return [str(c.numerator),str(c.denominator),list(ids)]

def linear_terms(source_map,ell,order):
    if order<0:
        return []
    return [term(comb(j,order),(idx,)) for (i,j),idx in source_map.items()
            if 5*i-j==ell and order<=j]

def row(label,kind,terms,**metadata):
    return {"type":"row","label":label,"kind":kind,"terms":terms,**metadata}

def jacobian_indices(spec):
    p,q=(spec["sides"][s] for s in ("P","Q"))
    degree=p["degree"]+q["degree"]-2
    weight=p["weight_cap"]+q["weight_cap"]-4
    max_i=(p["degree"]+p["weight_cap"])//6+(q["degree"]+q["weight_cap"])//6-1
    for I in range(max_i+1):
        hi=degree-I
        if spec["mode"]=="normalized":
            hi=min(hi,p["vertical_cap"]+q["vertical_cap"]-1)
        for J in range(max(0,5*I-weight),hi+1):
            yield I,J

def rows(spec,records,maps):
    # Iterate ORIGINAL bands/jets in both modes, retaining zero specialized rows.
    for side in ("P","Q"):
        d=spec["sides"][side]
        for ell in range(-d["degree"],d["weight_cap"]+1):
            r=max(0,-(-(5*ell-d["terminal_h"])//12))
            for k in range(r):
                yield row(f"jet_{side}_ell{ell}_order{k}","jet",
                          linear_terms(maps[side],ell,k),side=side,ell=ell,order=k)
    for n,(side,ell,power,num,den) in enumerate(spec["pins"]):
        terms=linear_terms(maps[side],ell,power-ell)
        value=Fraction(int(num),int(den))
        if value:
            terms.append(term(-value))
        yield row(f"pin_{n}_{side}_ell{ell}_t{power}","pin",terms,
                  side=side,ell=ell,t_power=power,target=[num,den])
    target=Fraction(*map(int,spec["target"]))
    target_seen=False
    for I,J in jacobian_indices(spec):
        terms=[]
        # Each output and P monomial forces the only possible Q monomial.
        for (i,j),pid in maps["P"].items():
            k,s=I+1-i,J+1-j
            qid=maps["Q"].get((k,s))
            determinant=i*s-j*k
            if qid is not None and determinant:
                terms.append(term(determinant,(pid,qid)))
        if (I,J)==(0,0):
            target_seen=True
            if target:
                terms.append(term(-target))
        yield row(f"J_u{I}_v{J}","physical_J",terms,output_exponent=[I,J])
    require(target_seen,"target index absent from envelope")
    ids=[maps[s][tuple(spec["sides"][s]["guard"])] for s in ("P","Q")]
    ids.append(len(records)-1)
    yield row("original_degree_guard","degree_guard",[term(1,ids),term(-1)],
              original_degrees=[spec["sides"][s]["degree"] for s in ("P","Q")])

def singular_polynomial(terms,names):
    if not terms:
        return "0"
    return "+".join("("+n+"/"+d+")"+"".join("*"+names[i] for i in ids)
                    for n,d,ids in terms)

def make_header(spec,records,maps,authority=None):
    return {"type":"header","schema":SCHEMA,"coefficient_field":"Q",
            "global_order":"dp","spec":spec,"source_hashes":SOURCES,
            "builder_sha256":digest_file(__file__),"variable_count":len(records),
            "production_authority_canonical_sha256":hashlib.sha256(canonical(authority)).hexdigest()
                 if authority is not None else None,
            "source_counts":{s:len(maps[s]) for s in ("P","Q")},
            "normalized_equivalence_status":"PROVISIONAL_UNLICENSED" if
                 spec["mode"]=="normalized" else "NOT_REQUIRED",
            "zero_policy":"all envelope and original linear rows retained",
            "constants_policy":"both source additive constants retained",
            "semantics":"ALL ordinary coefficients of J(P,Q)-1/5 plus every jet, pin, guard; no solve"}

def check_authority(spec,authority):
    if spec["name"]!="D125":
        require(max(d["degree"] for d in spec["sides"].values())<=8,"nonproduction fixture too large")
        return
    require(authority is not None,"NO_PRODUCTION_AUTHORITY: root GREEN required")
    require(authority.get("schema")=="jc2.d125-export-authority/v1" and
            authority.get("mode")==spec["mode"] and authority.get("root_green") is True and
            authority.get("builder_sha256")==digest_file(__file__),"invalid production authority")
    require(all(type(authority.get(k)) is int and authority[k]>0 for k in
                ("max_output_bytes","max_wall_seconds","max_address_space_bytes")),"invalid authority caps")
    require(spec==production_spec(spec["mode"]),"production contract drift")

def build(spec,outdir,max_bytes=10*1024**2,max_seconds=25,singular=False,authority=None):
    require(spec["mode"] in ("original","normalized"),"bad mode")
    check_authority(spec,authority)
    if spec["name"]=="D125":
        require(max_bytes==authority["max_output_bytes"] and
                max_seconds==authority["max_wall_seconds"],"caps disagree with authority")
    start=time.monotonic()
    records,maps=variables(spec)
    header=make_header(spec,records,maps,authority)
    os.mkdir(outdir)  # fresh directory only; no overwrite/resume.
    outdir=Path(outdir)
    counts=Counter();zero=Counter();terms=Counter();used=set()
    sha=hashlib.sha256();written=0
    stream=open(outdir/"literal.jsonl","xb")
    try:
        sing=open(outdir/"import.sing","xb") if singular else None
    except BaseException:
        stream.close()
        raise
    def write_bytes(f,data):
        nonlocal written
        require(time.monotonic()-start<=max_seconds,"wall cap")
        require(written+len(data)<=max_bytes,"output byte cap")
        f.write(data);written+=len(data)
    def emit(obj,hashed=True):
        data=canonical(obj)
        write_bytes(stream,data)
        if hashed: sha.update(data)
    try:
        emit(header)
        for rec in records: emit(rec)
        names=[r["name"] for r in records]
        if sing:
            write_bytes(sing,("// IMPORT ONLY: no standard basis or solve\nring R=0,("+
                       ",".join(names)+"),dp;\nideal I=\n").encode())
        first=True
        for rec in rows(spec,records,maps):
            emit(rec);kind=rec["kind"]
            counts[kind]+=1;zero[kind]+=not rec["terms"];terms[kind]+=len(rec["terms"])
            for _,_,ids in rec["terms"]: used.update(ids)
            if sing:
                text=("" if first else ",\n")+"// "+rec["label"]+"\n"+singular_polynomial(rec["terms"],names)
                write_bytes(sing,text.encode());first=False
        footer={"type":"footer","complete":True,"prefix_sha256":sha.hexdigest(),
                "variable_count":len(records),"row_counts":dict(counts),
                "zero_row_counts":dict(zero),"term_counts":dict(terms),
                "unused_variable_ids":[i for i in range(len(records)) if i not in used]}
        emit(footer,False)
        if sing: write_bytes(sing,(";\n// COMPLETE prefix_sha256="+footer["prefix_sha256"]+
                                   '\nprint("D125_IMPORT_ONLY_NO_SOLVE");\nquit;\n').encode())
        for f in (stream,sing):
            if f: f.flush();os.fsync(f.fileno())
    finally:
        stream.close()
        if sing: sing.close()
    manifest={"schema":SCHEMA,"complete":True,"elapsed_seconds":time.monotonic()-start,
              "limits":{"combined_output_bytes":max_bytes,"wall_seconds":max_seconds},
              "files":{"literal.jsonl":digest_file(outdir/"literal.jsonl")},"footer":footer}
    if singular: manifest["files"]["import.sing"]=digest_file(outdir/"import.sing")
    with open(outdir/"manifest.json","xb") as f: f.write(canonical(manifest));f.flush();os.fsync(f.fileno())
    return manifest

def verify(path,expected_spec,authority=None):
    """Strict complete-stream replay, including literal coefficients and EOF.

    This reuses the exporter formula; independent toy controls are separate.
    A production replay is a full arithmetic run and also needs root authority.
    """
    check_authority(expected_spec,authority)
    records,maps=variables(expected_spec)
    expected=iter(records)  # rows remain streaming, never materialized.
    digest=hashlib.sha256()
    counts=Counter();zero=Counter();terms=Counter();used=set()
    with open(path,"rb") as f:
        line=f.readline();header=json.loads(line)
        require(line==canonical(make_header(expected_spec,records,maps,authority)),"header contract/encoding drift")
        digest.update(line)
        for rec in expected:
            line=f.readline();require(line==canonical(rec),"variable map drift");digest.update(line)
        for rec in rows(expected_spec,records,maps):
            line=f.readline();require(line==canonical(rec),"literal row missing/reordered/changed");digest.update(line)
            k=rec["kind"];counts[k]+=1;zero[k]+=not rec["terms"];terms[k]+=len(rec["terms"])
            for _,_,ids in rec["terms"]: used.update(ids)
        line=f.readline();footer=json.loads(line)
        require(line==canonical(footer) and footer.get("type")=="footer" and footer.get("complete") is True,"missing footer")
        require(footer.get("prefix_sha256")==digest.hexdigest(),"prefix digest")
        require(footer.get("variable_count")==len(records) and footer.get("row_counts")==dict(counts)
                and footer.get("zero_row_counts")==dict(zero) and footer.get("term_counts")==dict(terms),"footer counts")
        require(footer.get("unused_variable_ids")==[i for i in range(len(records)) if i not in used],"unused variables")
        require(f.read(1)==b"","trailing bytes")
    return footer

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode",choices=["toy","original","normalized"],required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--singular",action="store_true")
    ap.add_argument("--production-authority")
    args=ap.parse_args()
    max_bytes,max_seconds,memory=10*1024**2,25,512*1024**2
    authority=None
    if args.mode!="toy":
        require(args.production_authority is not None,"NO_PRODUCTION_AUTHORITY: root GREEN required")
        authority=json.loads(Path(args.production_authority).read_text())
        require(authority.get("schema")=="jc2.d125-export-authority/v1" and
                authority.get("mode")==args.mode and authority.get("root_green") is True and
                authority.get("builder_sha256")==digest_file(__file__),"invalid production authority")
        max_bytes,max_seconds,memory=(authority[k] for k in
               ("max_output_bytes","max_wall_seconds","max_address_space_bytes"))
        require(all(type(v) is int and v>0 for v in (max_bytes,max_seconds,memory)),"invalid caps")
    resource.setrlimit(resource.RLIMIT_AS,(memory,memory))
    spec=toy_spec() if args.mode=="toy" else production_spec(args.mode)
    manifest=build(spec,args.output,max_bytes,max_seconds,args.singular,authority)
    print(json.dumps(manifest,sort_keys=True))

if __name__=="__main__":
    main()
