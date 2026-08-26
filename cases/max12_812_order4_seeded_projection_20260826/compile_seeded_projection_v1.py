#!/usr/bin/env python3
"""AWS-only compiler for seeded order-four projection certificates."""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import platform


EXPECTED_SOURCE = "d2fedf6c9b2b09787c7e45a00f1626ac10f7d4c68c44030102758021a55c9496"
EXPECTED_STDOUT = "5e780dcf82d2a3ac17c3ae7957c819c8b7b8a1a1de6231f88e4f808a2b348c45"
SOURCE_CUT = "ideal Gtail=modStd(Itail);"
BASIS_BEGIN = "SAT_BASIS_BEGIN\n"
BASIS_END = "\nSAT_BASIS_END"


def require_aws() -> None:
    vendor_path = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    if platform.system() != "Linux" or vendor != "Amazon EC2":
        raise RuntimeError("AWS EC2 only")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing registered AWS lane tag")


def checked_text(path: pathlib.Path, expected: str) -> str:
    raw = path.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise RuntimeError(f"hash mismatch for {path}: {actual}")
    return raw.decode("utf-8")


def common_suffix(basis: str) -> str:
    return f'''
ideal JQ={basis};
ideal GQ=std(JQ);
int seed_monic=1;
int seed_i;
for (seed_i=1; seed_i<=size(GQ); seed_i++)
{{
  if (leadcoef(GQ[seed_i]) != 1) {{ seed_monic=0; }}
}}
int seed_self=ideal_is_zero(reduce(JQ,GQ));
int source_to_seed=ideal_is_zero(reduce(Itail,GQ));
int seed_dim=dim(GQ);
int seed_size=size(GQ);
int seed_a6_nonzero=(reduce(a6,GQ)!=0);
print("SEEDED_Q_MONIC="+string(seed_monic));
print("SEEDED_Q_SELF_GB="+string(seed_self));
print("SOURCE_TO_SEEDED_Q="+string(source_to_seed));
print("SEEDED_Q_DIM="+string(seed_dim));
print("SEEDED_Q_SIZE="+string(seed_size));
print("SEEDED_Q_A6_NONZERO="+string(seed_a6_nonzero));
if ((seed_monic==0)||(seed_self==0)||(source_to_seed==0)||
    (seed_dim!=1)||(seed_size!=71)||(seed_a6_nonzero==0))
{{
  print("SEEDED_Q_PREFLIGHT=FAIL");
  exit(81);
}}
print("SEEDED_Q_PREFLIGHT=PASS");
'''


def a6_suffix() -> str:
    return r'''
list S6=sat(GQ,ideal(a6));
ideal J6=std(S6[1]);
int jq_to_j6=ideal_is_zero(reduce(GQ,J6));
int j6_to_jq=ideal_is_zero(reduce(J6,GQ));
print("A6_SAT_J_TO_J6="+string(jq_to_j6));
print("A6_SAT_J6_TO_J="+string(j6_to_jq));
if ((jq_to_j6==0)||(j6_to_jq==0))
{
  print("SEEDED_A6_CERTIFICATE=FAIL");
  exit(82);
}
print("SEEDED_A6_CERTIFICATE=PASS");
quit;
'''


def prime_suffix() -> str:
    return r'''
def QR=R;
ring P=32003,(a0,a1,a2,a3,a4,a5,a6),dp;
option(redSB);
proc ideal_is_zero_p(ideal A)
{
  int i;
  for (i=1; i<=size(A); i++)
  {
    if (A[i] != 0) { return(0); }
  }
  return(1);
}
ideal Ip=imap(QR,Itail);
poly r7p=imap(QR,r7);
ideal GredRaw=imap(QR,GQ);
ideal Gred=std(GredRaw);
list SSP=sat(Ip,ideal(r7p));
ideal Jp=std(SSP[1]);
int red_to_native=ideal_is_zero_p(reduce(Gred,Jp));
int native_to_red=ideal_is_zero_p(reduce(Jp,Gred));
ideal Lred=std(lead(Gred));
ideal Lnative=std(lead(Jp));
int lm_red_to_native=ideal_is_zero_p(reduce(Lred,Lnative));
int lm_native_to_red=ideal_is_zero_p(reduce(Lnative,Lred));
print("P=32003");
print("P_SAT_UNIT="+string(reduce(1,Jp)==0));
print("P_SAT_DIM="+string(dim(Jp)));
print("P_SAT_SIZE="+string(size(Jp)));
print("QRED_RAW_SIZE="+string(size(GredRaw)));
print("QRED_STD_SIZE="+string(size(Gred)));
print("QRED_TO_NATIVE="+string(red_to_native));
print("NATIVE_TO_QRED="+string(native_to_red));
print("QRED_LM_TO_NATIVE="+string(lm_red_to_native));
print("NATIVE_LM_TO_QRED="+string(lm_native_to_red));
LIB "primdec.lib";
list PA=minAssGTZ(Jp);
print("MINASS_COUNT="+string(size(PA)));
int prime_equal=0;
if (size(PA)==1)
{
  ideal PP=std(PA[1]);
  int jp_to_pp=ideal_is_zero_p(reduce(Jp,PP));
  int pp_to_jp=ideal_is_zero_p(reduce(PP,Jp));
  prime_equal=(jp_to_pp && pp_to_jp);
  print("JP_TO_MINASS="+string(jp_to_pp));
  print("MINASS_TO_JP="+string(pp_to_jp));
}
print("SPECIAL_FIBRE_PRIME="+string(prime_equal));
ideal EP=std(eliminate(Jp,a0*a1*a2*a3*a4));
int plane_nonzero=((size(EP)==1)&&(EP[1]!=0));
int plane_irred=0;
print("PLANE_SIZE="+string(size(EP)));
if (plane_nonzero)
{
  list FF=factorize(EP[1],1);
  print("PLANE_FACTOR_COUNT="+string(size(FF[1])));
  plane_irred=(size(FF[1])==1);
  print("PLANE_BEGIN"); print(EP); print("PLANE_END");
}
int lift_ok=(red_to_native && native_to_red && lm_red_to_native &&
             lm_native_to_red && prime_equal && plane_nonzero &&
             plane_irred && (dim(Jp)==1) && (size(GredRaw)==71));
print("SEEDED_MONIC_GOOD_REDUCTION_PRIME_LIFT="+string(lift_ok));
if (lift_ok==0)
{
  print("SEEDED_PROJECTION_CERTIFICATE=FAIL");
  exit(83);
}
print("SEEDED_PROJECTION_CERTIFICATE=PASS");
quit;
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("stdout", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("--mode", choices=("seeded-a6", "seeded-prime"), required=True)
    args = parser.parse_args()
    require_aws()
    source = checked_text(args.source, EXPECTED_SOURCE)
    prior = checked_text(args.stdout, EXPECTED_STDOUT)
    if source.count(SOURCE_CUT) != 1:
        raise RuntimeError("source cut marker is not unique")
    required = (
        "SOURCE_EQUIVALENCE=PASS",
        "SAT_IS_UNIT=0",
        "SAT_DIM=1",
        "SAT_BASIS_SIZE=71",
    )
    if any(prior.count(token) != 1 for token in required):
        raise RuntimeError("prior exact-Q sentinels missing or nonunique")
    if prior.count(BASIS_BEGIN) != 1 or prior.count(BASIS_END) != 1:
        raise RuntimeError("basis delimiters missing or nonunique")
    basis = prior.split(BASIS_BEGIN, 1)[1].split(BASIS_END, 1)[0].strip()
    lines = basis.splitlines()
    if len(lines) != 71 or any(not line.strip() for line in lines):
        raise RuntimeError(f"expected 71 one-line basis elements, got {len(lines)}")
    if any(not line.endswith(",") for line in lines[:-1]) or lines[-1].endswith(","):
        raise RuntimeError("unexpected printed ideal punctuation")
    prefix = source.split(SOURCE_CUT, 1)[0]
    tail = a6_suffix() if args.mode == "seeded-a6" else prime_suffix()
    emitted = prefix + common_suffix(basis) + tail
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(emitted, encoding="utf-8")
    print(f"mode={args.mode}")
    print(f"source_sha256={EXPECTED_SOURCE}")
    print(f"stdout_sha256={EXPECTED_STDOUT}")
    print(f"basis_elements={len(lines)}")
    print(f"output_sha256={hashlib.sha256(emitted.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
