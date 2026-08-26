#!/usr/bin/env python3
"""AWS-only compiler for the order-four projection/source certificates."""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import platform


EXPECTED_SOURCE = "5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47"
SAT_MARKER = "list SS=sat(Itail,ideal(r7));"


def require_aws() -> None:
    vendor_path = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    if platform.system() != "Linux" or vendor != "Amazon EC2":
        raise RuntimeError("AWS EC2 only")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing registered AWS lane tag")


def common_exact_suffix() -> str:
    return r'''
list SSQ=sat(Itail,ideal(r7));
ideal JQ=std(SSQ[1]);
print("Q_SAT_UNIT="+string(reduce(1,JQ)==0));
print("Q_SAT_DIM="+string(dim(JQ)));
print("Q_SAT_SIZE="+string(size(JQ)));
'''


def a6_suffix() -> str:
    return common_exact_suffix() + r'''
list S6=sat(JQ,ideal(a6));
ideal J6=std(S6[1]);
int j_to_j6=ideal_is_zero(reduce(JQ,J6));
int j6_to_j=ideal_is_zero(reduce(J6,JQ));
ideal Za6=std(JQ+ideal(a6));
print("A6_SAT_J_TO_J6="+string(j_to_j6));
print("A6_SAT_J6_TO_J="+string(j6_to_j));
print("A6_CHART_LOSS="+string((j_to_j6==0)||(j6_to_j==0)));
print("A6_SECTION_UNIT="+string(reduce(1,Za6)==0));
print("A6_SECTION_DIM="+string(dim(Za6)));
if ((j_to_j6==0)||(j6_to_j==0))
{
  print("A6_CERTIFICATE=FAIL");
  quit;
}
print("A6_CERTIFICATE=PASS");
quit;
'''


def prime_lift_suffix() -> str:
    return common_exact_suffix() + r'''
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
ideal Gred=imap(QR,JQ);
ideal GredStd=std(Gred);
list SSP=sat(Ip,ideal(r7p));
ideal Jp=std(SSP[1]);
int red_to_native=ideal_is_zero_p(reduce(GredStd,Jp));
int native_to_red=ideal_is_zero_p(reduce(Jp,GredStd));
ideal Lred=std(lead(Gred));
ideal Lnative=std(lead(Jp));
int lm_red_to_native=ideal_is_zero_p(reduce(Lred,Lnative));
int lm_native_to_red=ideal_is_zero_p(reduce(Lnative,Lred));
print("P=32003");
print("P_SAT_UNIT="+string(reduce(1,Jp)==0));
print("P_SAT_DIM="+string(dim(Jp)));
print("P_SAT_SIZE="+string(size(Jp)));
print("QRED_SIZE="+string(size(Gred)));
print("QRED_STD_SIZE="+string(size(GredStd)));
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
print("PLANE_SIZE="+string(size(EP)));
print("PLANE_BEGIN");
print(EP);
print("PLANE_END");
int plane_irred=0;
if (size(EP)==1)
{
  list FF=factorize(EP[1],1);
  print("PLANE_FACTOR_COUNT="+string(size(FF[1])));
  plane_irred=(size(FF[1])==1);
}
int lift_ok=(red_to_native && native_to_red && lm_red_to_native && lm_native_to_red && prime_equal && plane_irred);
print("MONIC_GOOD_REDUCTION_PRIME_LIFT="+string(lift_ok));
if (lift_ok==0)
{
  print("PROJECTION_CERTIFICATE=FAIL");
  quit;
}
print("PROJECTION_CERTIFICATE=PASS");
quit;
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("--mode", choices=("a6", "prime-lift"), required=True)
    args = parser.parse_args()
    require_aws()
    raw = args.source.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SOURCE:
        raise RuntimeError(f"source hash mismatch: {actual}")
    text = raw.decode("utf-8")
    if text.count(SAT_MARKER) != 1:
        raise RuntimeError("missing unique source saturation marker")
    prefix = text.split(SAT_MARKER, 1)[0]
    suffix = a6_suffix() if args.mode == "a6" else prime_lift_suffix()
    emitted = prefix + suffix
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(emitted, encoding="utf-8")
    print(f"mode={args.mode}")
    print(f"source_sha256={actual}")
    print(f"output_sha256={hashlib.sha256(emitted.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
