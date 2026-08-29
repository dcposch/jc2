#!/usr/bin/env python3
"""Compile the small discriminant half-weight support eliminator (AWS only)."""

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
        fail("AWS-only support compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only support compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def source(characteristic: int) -> str:
    return f'''LIB "elim.lib";
ring R={characteristic},(b,e,h,y,k),dp;
print("DISC_HALF_SUPPORT_SOURCE_HASH=PASS");
list c;
c[1]=1;
c[2]=(5/2)*b;
for (int n=1; n<=16; n++) {{ c[n+2]=(b*(5/2-n)*c[n+1]+e*(6-n)*c[n])/(n+1); }}
list u;
u[1]=0; u[2]=0; u[3]=y^2;
u[4]=-2*y*h-b*u[3];
u[5]=h^2-b*u[4]-e*u[3];
for (n=5; n<=7; n++) {{ u[n+1]=-b*u[n]-e*u[n-1]; }}
poly g3=6*u[4]-1+16*k*c[14];
poly g4=6*u[5]+16*k*c[15];
poly g5=6*u[6]+16*k*c[16];
poly g6=6*u[7]+16*k*c[17];
poly g7=6*u[8]+16*k*c[18];
poly P1=b*c[16]+2*e*c[15];
poly P2=b*c[17]+2*e*c[16];
poly comb6=g6+b*g5+e*g4-(7/2)*k*P1;
poly comb7=g7+b*g6+e*g5-(56/17)*k*P2;
print("DISC_HALF_SUPPORT_COMB6_ZERO="+string(comb6==0));
print("DISC_HALF_SUPPORT_COMB7_ZERO="+string(comb7==0));
print("DISC_HALF_SUPPORT_P1_FACTOR_BEGIN"); print(factorize(P1)); print("DISC_HALF_SUPPORT_P1_FACTOR_END");
print("DISC_HALF_SUPPORT_P2_FACTOR_BEGIN"); print(factorize(P2)); print("DISC_HALF_SUPPORT_P2_FACTOR_END");
ideal G=g3,g4,g5,g6,g7;
print("DISC_HALF_SUPPORT_K0_START");
ideal G0=subst(G,k,0); G0=std(G0);
print("DISC_HALF_SUPPORT_K0_DIM="+string(dim(G0)));
print("DISC_HALF_SUPPORT_K0_BASIS_BEGIN"); print(G0); print("DISC_HALF_SUPPORT_K0_BASIS_END");
ideal G0e=sat(G0,ideal(e)); G0e=std(G0e);
print("DISC_HALF_SUPPORT_K0_E_NONZERO_UNIT="+string(reduce(1,G0e)==0));
ideal G0t=subst(G0,e,0); G0t=std(G0t);
print("DISC_HALF_SUPPORT_K0_TRIPLE_DIM="+string(dim(G0t)));
print("DISC_HALF_SUPPORT_K0_TRIPLE_BASIS_BEGIN"); print(G0t); print("DISC_HALF_SUPPORT_K0_TRIPLE_BASIS_END");
print("DISC_HALF_SUPPORT_KNZ_START");
ideal GK=sat(G,ideal(k)); GK=std(GK);
print("DISC_HALF_SUPPORT_KNZ_DIM="+string(dim(GK)));
ideal GKe=sat(GK,ideal(e)); GKe=std(GKe);
print("DISC_HALF_SUPPORT_KNZ_E_NONZERO_UNIT="+string(reduce(1,GKe)==0));
poly Delta=b^2-4*e;
ideal GKgen=sat(GKe,ideal(Delta)); GKgen=std(GKgen);
print("DISC_HALF_SUPPORT_KNZ_GENERIC_UNIT="+string(reduce(1,GKgen)==0));
print("DISC_HALF_SUPPORT_KNZ_GENERIC_BASIS_BEGIN"); print(GKgen); print("DISC_HALF_SUPPORT_KNZ_GENERIC_BASIS_END");
ideal GKt=subst(GK,e,0); GKt=std(GKt);
print("DISC_HALF_SUPPORT_KNZ_TRIPLE_DIM="+string(dim(GKt)));
print("DISC_HALF_SUPPORT_KNZ_TRIPLE_BASIS_BEGIN"); print(GKt); print("DISC_HALF_SUPPORT_KNZ_TRIPLE_BASIS_END");
print("DISC_HALF_SUPPORT_ENDPOINT=PASS_NAVIGATION_ONLY");
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
    target = output / f"disc_halfweight_support_p{args.characteristic}.sing"
    target.write_text(source(args.characteristic))
    payload = {
        "status": "PASS-DISC-HALFWEIGHT-SUPPORT-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "theorem_sha256": digest(THEOREM),
        "input_sha256": digest(target),
        "scope": "KURANISHI_INITIAL_SUPPORT_NAVIGATION_ONLY",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
