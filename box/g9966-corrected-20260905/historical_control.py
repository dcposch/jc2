#!/usr/bin/env python3
"""Execute the mechanically verified frozen arithmetic engine at its OLD face.
Only obsolete input-location wrappers are replaced; mathematical functions are unchanged.
"""
import importlib.util,sys,json,hashlib,argparse
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("frozen_band",HERE/"frozen/band_engine.py")
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
def custody():
    digest=hashlib.sha256((HERE/"frozen/band_engine.py").read_bytes()).hexdigest()
    assert digest=="3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"
    return {"frozen_engine_sha256":digest,"verified":True}
m.verify_inputs=custody
m.reproduce_charged_endpoint=lambda:{"not_run":"unrelated earlier first_global_band endpoint; current task controls full frozen engine"}
a=argparse.ArgumentParser();a.add_argument("branch");a.add_argument("stage",type=int);args=a.parse_args()
result=m.run(args.branch,args.stage,HERE/f"historical-{args.branch}-stage{args.stage}.sing")
expected=6264 if args.branch=="delta2" else 64
label="stage4_J_d159_k35" if args.branch=="delta2" else "stage8_G_local16_coord0"
rows={r["label"]:r["expression"] for r in result["joint_elimination"]["residual_rows"]}
assert rows[label]==str(expected),(label,rows.get(label))
assert result["joint_elimination"]["singular"]["unit_ideal"]
result["historical_unit_control"]={"expected":expected,"actual":rows[label],"label":label,"PASS":True}
(HERE/f"historical-{args.branch}-stage{args.stage}.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({"branch":args.branch,"stage":args.stage,"control":result["historical_unit_control"],"resources":result["resources"]},indent=2))
