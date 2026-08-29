#!/usr/bin/env python3
from __future__ import annotations
import argparse
from hashlib import sha256
import json
from pathlib import Path

def digest(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()

def main() -> None:
    cli=argparse.ArgumentParser(); cli.add_argument("--result",type=Path,required=True)
    cli.add_argument("--stdout",type=Path,required=True); cli.add_argument("--stderr",type=Path,required=True)
    cli.add_argument("--characteristic",type=int,choices=(0,65521),required=True); cli.add_argument("--output",type=Path,required=True)
    args=cli.parse_args(); result=json.loads(args.result.read_text())
    if (result.get("status")!="PASS-A1-GRADE19-RATIONAL-ORBIT-V35-COMPILER" or result.get("characteristic")!=args.characteristic
            or result.get("old_bridges")!=63 or result.get("old_point_zero_rows")!=63 or result.get("mutation_nonzero_rows",0)<1
            or set(result.get("coefficient_paths",{}))!={f"Tg19_{r}" for r in range(1,8)}
            or result.get("outcome") not in {"survives","killed"}): raise RuntimeError("result contract")
    for name,raw in result["coefficient_paths"].items():
        if digest(Path(raw))!=result["coefficient_sha256"][name]: raise RuntimeError(("row hash",name))
    stdout=args.stdout.read_text(); stderr=args.stderr.read_text()
    for token in ("PASS-A1-GRADE19-RATIONAL-ORBIT-V35-COMPILER",f"V35_OUTCOME={result['outcome']}"):
        if stdout.count(token)!=1: raise RuntimeError(("stdout",token))
    if stderr.count("Command being timed:")!=1 or stderr.count("Exit status: 0")!=1: raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("FAIL_","?","error occurred","Killed","out of memory")): raise RuntimeError("diagnostic token")
    final={"status":"PASS-A1-GRADE19-RATIONAL-ORBIT-V35","characteristic":args.characteristic,"outcome":result["outcome"],
           "nonzero_rows":result["lane_nonzero_rows"],"result_sha256":digest(args.result),"stdout_sha256":digest(args.stdout),
           "resource_stderr_sha256":digest(args.stderr),"coefficient_sha256":result["coefficient_sha256"]}
    args.output.write_text(json.dumps(final,sort_keys=True,indent=2)+"\n"); print("PASS-A1-GRADE19-RATIONAL-ORBIT-V35-VALIDATOR")

if __name__=="__main__": main()
