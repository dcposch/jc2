#!/usr/bin/env python3
"""Direct-m characteristic-zero support and scheme client (AWS only)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
THEOREM = ROOT / "xmodel/max12-812-order2-discriminant-rank-halfweight-kuranishi-20260826.md"
THEOREM_SHA = "ddbc758039621f70eae586b5482be3bfdd92754e990cdb015fa4c6d2e0eac0b1"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only support V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only support V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def source(characteristic: int) -> str:
    return f'''LIB "elim.lib";
LIB "primdec.lib";
ring R={characteristic},(b,e,h,y,k,m),dp;
print("DISC_HALF_SUPPORT_V2_SOURCE_HASH=PASS");
list c;
c[1]=1;
c[2]=(5/2)*b;
for (int n=1; n<=16; n++) {{ c[n+2]=(b*(5/2-n)*c[n+1]+e*(6-n)*c[n])/(n+1); }}
list u;
u[1]=0; u[2]=0; u[3]=y^2;
u[4]=-2*y*h-b*u[3];
u[5]=h^2-b*u[4]-e*u[3];
for (n=5; n<=7; n++) {{ u[n+1]=-b*u[n]-e*u[n-1]; }}
poly g3=6*u[4]-m^3+16*k*c[14];
poly g4=6*u[5]+16*k*c[15];
poly g5=6*u[6]+16*k*c[16];
poly g6=6*u[7]+16*k*c[17];
poly g7=6*u[8]+16*k*c[18];
ideal G=g3,g4,g5,g6,g7;
ideal Gm=sat(G,ideal(m)); Gm=std(Gm);
print("DISC_HALF_SUPPORT_V2_M_NONZERO_DIM="+string(dim(Gm)));
ideal GK=sat(Gm,ideal(k)); GK=std(GK);
print("DISC_HALF_SUPPORT_V2_K_NONZERO_UNIT="+string(reduce(1,GK)==0));
ideal G0=G,ideal(k); G0=sat(G0,ideal(m)); G0=std(G0);
print("DISC_HALF_SUPPORT_V2_K0_DIM="+string(dim(G0)));
print("DISC_HALF_SUPPORT_V2_K0_BASIS_BEGIN"); print(G0); print("DISC_HALF_SUPPORT_V2_K0_BASIS_END");
ideal G0e=sat(G0,ideal(e)); G0e=std(G0e);
print("DISC_HALF_SUPPORT_V2_K0_E_NONZERO_UNIT="+string(reduce(1,G0e)==0));
ideal G0bm=sat(G0,ideal(b)); G0bm=sat(G0bm,ideal(m)); G0bm=std(G0bm);
print("DISC_HALF_SUPPORT_V2_TRIPLE_OPEN_DIM="+string(dim(G0bm)));
print("DISC_HALF_SUPPORT_V2_TRIPLE_OPEN_BASIS_BEGIN"); print(G0bm); print("DISC_HALF_SUPPORT_V2_TRIPLE_OPEN_BASIS_END");
ideal RG=radical(G0bm); RG=std(RG);
print("DISC_HALF_SUPPORT_V2_TRIPLE_RADICAL_DIM="+string(dim(RG)));
print("DISC_HALF_SUPPORT_V2_TRIPLE_RADICAL_BASIS_BEGIN"); print(RG); print("DISC_HALF_SUPPORT_V2_TRIPLE_RADICAL_BASIS_END");
ideal Expected=e,k,h+b*y,6*b*y^2-m^3; Expected=sat(Expected,ideal(b)); Expected=sat(Expected,ideal(m)); Expected=std(Expected);
int rg_in_expected=1;
int expected_in_rg=1;
for (int ci=1; ci<=size(RG); ci++) {{ if (reduce(RG[ci],Expected)!=0) {{ rg_in_expected=0; }} }}
for (ci=1; ci<=size(Expected); ci++) {{ if (reduce(Expected[ci],RG)!=0) {{ expected_in_rg=0; }} }}
print("DISC_HALF_SUPPORT_V2_RADICAL_IN_EXPECTED="+string(rg_in_expected));
print("DISC_HALF_SUPPORT_V2_EXPECTED_IN_RADICAL="+string(expected_in_rg));
if (rg_in_expected!=1 || expected_in_rg!=1) {{ print("DISC_HALF_SUPPORT_V2_FAIL=RADICAL_COMPARE"); quit; }}
print("DISC_HALF_SUPPORT_V2_ENDPOINT=PASS_DIRECT_M_SUPPORT_AND_SCHEME");
quit;
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003), required=True)
    args = parser.parse_args()
    tag = require_aws()
    if digest(THEOREM) != THEOREM_SHA:
        fail(("theorem hash mismatch", digest(THEOREM), THEOREM_SHA))
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_halfweight_support_v2_p{args.characteristic}.sing"
    target.write_text(source(args.characteristic))
    payload = {
        "status": "PASS-DISC-HALFWEIGHT-SUPPORT-V2-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "theorem_sha256": digest(THEOREM),
        "input_sha256": digest(target),
        "scope": "DIRECT_M_KURANISHI_INITIAL_SUPPORT_AND_SCHEME_ONLY",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
