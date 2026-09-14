#!/usr/bin/env python3
"""CONTROL B: rad(I_sat_T8) = <u,v> EXACTLY, verified in Singular over Q.

This is the licence for the locus restriction: if the radical of the saturated
T=8 residual ideal is <u,v>, then the SET of points satisfying every saturated
row is exactly V(u,v) (intersected with the resolved Q* pivots), so restricting
to V(u,v) discards no point of any extension field.
"""
import json, subprocess
from pathlib import Path
OUT = Path("/home/ubuntu/jc2/box/d108-survivor-deep-20260905")
R = json.load(open("/home/ubuntu/jc2/box/d108-rekill-20260905/work/sat_wz5_jet0pinned_T8.json"))
gens = [v.replace("**", "^") for v in R["residual"].values()]
vars_ = R["residual_variables"]
u = "K2c_3_26+8*jet2"
v = "K2c_4_25-K2c_4_26-20*jet1^2"
script = f"""LIB "primdec.lib";
ring Rr=0,({",".join(vars_)}),dp;
ideal I={",".join(gens)};
ideal UV={u},{v};
ideal SI=std(I); ideal SUV=std(UV);
print("BEGIN_ICONT");                 // I contained in <u,v> ?
print(size(reduce(I,SUV)));
print("END_ICONT");
ideal Rad=radical(I); ideal SR=std(Rad);
print("BEGIN_RADEQ");                 // rad(I) == <u,v> ?  both inclusions
print(size(reduce(Rad,SUV)));
print(size(reduce(UV,SR)));
print("END_RADEQ");
print("BEGIN_DIMS");
print(dim(SI)); print(dim(SUV)); print(nvars(Rr));
print("END_DIMS");
print("BEGIN_NOTUNIT");
print(reduce(1,SI)); print(reduce(1,SUV));
print("END_NOTUNIT");
print("BEGIN_PROPER");                // <u,v> is a PROPER ideal, I != <u,v>
print(size(reduce(UV,SI)));
print("END_PROPER");
quit;
"""
(OUT / "ctl_radical.sing").write_text(script)
r = subprocess.run(["Singular", "-q"], input=script, text=True, capture_output=True, timeout=1200)
(OUT / "ctl_radical.sing.out").write_text(r.stdout + "\n--STDERR--\n" + r.stderr)
def sec(n):
    return r.stdout.split(f"BEGIN_{n}\n", 1)[1].split(f"\nEND_{n}", 1)[0].strip().splitlines()
icont, radeq, dims, notunit, proper = (sec(x) for x in
    ("ICONT", "RADEQ", "DIMS", "NOTUNIT", "PROPER"))
rec = {"control": "rad(I_sat_T8) == <u,v>",
       "generators": list(R["residual"].values()), "u": u, "v": v,
       "I_reduces_to_0_mod_uv": icont[-1] == "0",
       "rad_I_contained_in_uv": radeq[-2] == "0",
       "uv_contained_in_rad_I": radeq[-1] == "0",
       "RADICAL_EQUALS_UV": radeq[-2] == "0" and radeq[-1] == "0",
       "dim_I": int(dims[-3]), "dim_uv": int(dims[-2]), "nvars": int(dims[-1]),
       "I_not_unit": notunit[-2] == "1", "uv_not_unit": notunit[-1] == "1",
       "uv_strictly_larger_than_I": proper[-1] != "0",
       "raw": r.stdout[-1500:]}
(OUT / "ctl-radical.json").write_text(json.dumps(rec, indent=2) + "\n")
print(json.dumps({k: v for k, v in rec.items() if k != "raw"}, indent=2))
