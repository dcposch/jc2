#!/usr/bin/env python3
"""AWS-only mechanical compiler for the order-four invariant graph client."""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import platform


EXPECTED_INPUT_SHA256 = (
    "5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47"
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one occurrence, found {count}: {old!r}")
    return text.replace(old, new, 1)


def require_aws() -> None:
    if platform.system() != "Linux":
        raise RuntimeError("AWS-only compiler refused non-Linux host")
    vendor_path = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    if vendor != "Amazon EC2":
        raise RuntimeError(f"AWS-only compiler refused vendor={vendor or 'unknown'}")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing JC2_REGISTERED_AWS_LANE")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()

    require_aws()
    raw = args.source.read_bytes()
    actual = sha256(raw)
    if actual != EXPECTED_INPUT_SHA256:
        raise RuntimeError(f"input SHA mismatch: {actual}")
    text = raw.decode("utf-8")

    text = replace_once(
        text,
        'LIB "elim.lib";\n',
        'LIB "elim.lib";\nLIB "modstd.lib";\nLIB "moddiq.lib";\n',
    )
    text = replace_once(
        text,
        "ring R=0,(a0,a1,a2,a3,a4,a5,a6),dp;",
        "ring R=0,(a0,a1,a2,a3,a4,a5,a6,q,y,v,rho,R16),(dp(7),dp(5));",
    )
    text = replace_once(text, "ideal Gtail=std(Itail);", "ideal Gtail=modStd(Itail);")
    text = replace_once(text, "ideal Gcoef=std(Icoef);", "ideal Gcoef=modStd(Icoef);")

    marker = "list SS=sat(Itail,ideal(r7));"
    if text.count(marker) != 1:
        raise RuntimeError("could not find unique saturation marker")
    text = text.split(marker, 1)[0]
    text += r'''
list SS=modSat(Itail,ideal(r7));
ideal J=modStd(SS[1]);
int source_unit=(reduce(1,J)==0);
print("SOURCE_SAT_UNIT="+string(source_unit));
print("SOURCE_SAT_DIM="+string(dim(J)));
print("SOURCE_SAT_BASIS_SIZE="+string(size(J)));
if (source_unit==1)
{
  print("SOURCE_SATURATION=FAIL_UNIT");
  quit;
}

list S6=modSat(J,ideal(a6));
ideal J6=modStd(S6[1]);
int j_to_j6=ideal_is_zero(reduce(J,J6));
int j6_to_j=ideal_is_zero(reduce(J6,J));
int chart_loss=1-(j_to_j6*j6_to_j);
print("A6_SAT_J_TO_J6="+string(j_to_j6));
print("A6_SAT_J6_TO_J="+string(j6_to_j));
print("A6_CHART_LOSS="+string(chart_loss));
if (chart_loss!=0)
{
  print("INVARIANT_GRAPH=NO_VERDICT_CHART_LOSS");
  quit;
}

ideal K=J,
  q*a6^3-a5^2,
  y-a6^2,
  v-y^4,
  rho-r7^4,
  R16-rho^4;
list SK=modSat(K,ideal(a6));
ideal KG=modStd(SK[1]);
int inv_q=(reduce(q*a6^3-a5^2,KG)==0);
int inv_y=(reduce(y-a6^2,KG)==0);
int inv_v=(reduce(v-y^4,KG)==0);
int inv_rho=(reduce(rho-r7^4,KG)==0);
int inv_R16=(reduce(R16-rho^4,KG)==0);
print("INVARIANT_Q="+string(inv_q));
print("INVARIANT_Y="+string(inv_y));
print("INVARIANT_V="+string(inv_v));
print("INVARIANT_RHO="+string(inv_rho));
print("INVARIANT_R16="+string(inv_R16));
if ((inv_q*inv_y*inv_v*inv_rho*inv_R16)==0)
{
  print("INVARIANT_GRAPH=FAIL_RELATION");
  quit;
}

ideal Eall=eliminate(KG,a0*a1*a2*a3*a4*a5*a6);
Eall=std(Eall);
print("FULL_GRAPH_DIM="+string(dim(Eall)));
print("FULL_GRAPH_SIZE="+string(size(Eall)));
print("FULL_GRAPH_BEGIN");
print(Eall);
print("FULL_GRAPH_END");

ideal Edeckgraph=eliminate(Eall,v*R16);
Edeckgraph=std(Edeckgraph);
print("DECK_GRAPH_DIM="+string(dim(Edeckgraph)));
print("DECK_GRAPH_SIZE="+string(size(Edeckgraph)));
print("DECK_GRAPH_BEGIN");
print(Edeckgraph);
print("DECK_GRAPH_END");

ideal Edeck=eliminate(Edeckgraph,rho);
Edeck=std(Edeck);
print("DECK_CURVE_DIM="+string(dim(Edeck)));
print("DECK_CURVE_SIZE="+string(size(Edeck)));
print("DECK_CURVE_BEGIN");
print(Edeck);
print("DECK_CURVE_END");

ideal Eresgraph=eliminate(Eall,y*rho);
Eresgraph=std(Eresgraph);
print("RESIDUAL_GRAPH_DIM="+string(dim(Eresgraph)));
print("RESIDUAL_GRAPH_SIZE="+string(size(Eresgraph)));
print("RESIDUAL_GRAPH_BEGIN");
print(Eresgraph);
print("RESIDUAL_GRAPH_END");

ideal Eres=eliminate(Eresgraph,R16);
Eres=std(Eres);
print("RESIDUAL_CURVE_DIM="+string(dim(Eres)));
print("RESIDUAL_CURVE_SIZE="+string(size(Eres)));
print("RESIDUAL_CURVE_BEGIN");
print(Eres);
print("RESIDUAL_CURVE_END");
print("INVARIANT_GRAPH=PASS_EXACT_PRESENTATIONS");
quit;
'''

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"input_sha256={actual}")
    print(f"output_sha256={sha256(text.encode('utf-8'))}")


if __name__ == "__main__":
    main()
