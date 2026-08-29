#!/usr/bin/env python3
from __future__ import annotations
import argparse
from hashlib import sha256
import json
from pathlib import Path

def digest(path: Path) -> str: return sha256(path.read_bytes()).hexdigest()

def main() -> None:
    cli=argparse.ArgumentParser(); cli.add_argument("--result",type=Path,required=True); cli.add_argument("--stdout",type=Path,required=True)
    cli.add_argument("--stderr",type=Path,required=True); cli.add_argument("--characteristic",type=int,choices=(0,65521),required=True); cli.add_argument("--output",type=Path,required=True)
    args=cli.parse_args(); result=json.loads(args.result.read_text())
    if (result.get("status")!="PASS-A1-BOUNDARY-PROLONG-G18-V33-COMPILER" or result.get("characteristic")!=args.characteristic
            or result.get("old_bridges")!=56 or result.get("old_point_zero_rows")!=56 or result.get("outcome") not in {"consistent","inconsistent"}
            or set(result.get("coefficient_paths",{}))!={f"Tg18_{r}" for r in range(1,8)}): raise RuntimeError("result contract")
    for kind in ("coefficient","affine"):
        for name,raw in result[f"{kind}_paths"].items():
            if digest(Path(raw))!=result[f"{kind}_sha256"][name]: raise RuntimeError((kind,name))
    control=Path(result["control_script"])
    if digest(control)!=result["control_script_sha256"]: raise RuntimeError("control hash")
    stdout=args.stdout.read_text(); stderr=args.stderr.read_text()
    if stderr.count("Command being timed:")!=1 or stderr.count("Exit status: 0")!=1: raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("FAIL_","?","error occurred","Killed","out of memory")): raise RuntimeError("diagnostic token")
    required=["V33_POINT_MUTATION=1",f"V33_OUTCOME={result['outcome']}","PASS_A1_BOUNDARY_PROLONG_G18_V33"]
    required += [f"V33_EXTENSION_Tg18_{r}=1" for r in range(1,8)] if result["outcome"]=="consistent" else ["V33_DUAL=1"]
    if any(stdout.count(token)!=1 for token in required): raise RuntimeError("required token")
    final={"status":"PASS-A1-BOUNDARY-PROLONG-G18-V33","characteristic":args.characteristic,"outcome":result["outcome"],
           "result_sha256":digest(args.result),"control_script_sha256":digest(control),"stdout_sha256":digest(args.stdout),"resource_stderr_sha256":digest(args.stderr),
           "new_variables":result["new_variables"],"linear_rank":result["linear_rank"]}
    args.output.write_text(json.dumps(final,sort_keys=True,indent=2)+"\n"); print("PASS-A1-BOUNDARY-PROLONG-G18-V33-VALIDATOR")

if __name__=="__main__": main()

