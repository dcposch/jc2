#!/usr/bin/env python3
"""AWS-only fail-closed delta compiler for the V3 raw-reduction GB control."""

from __future__ import annotations

import argparse
import hashlib
import os
import pathlib
import platform


EXPECTED_V2_INPUT = "28721c66a0838487dc9490f1a33cd4b3d95324ffe80aaef9dcedabed3c10645a"

Q_MARKER = "int raw_to_norm=ideal_is_zero(reduce(GQraw,GQ));"
Q_REPLACEMENT = r'''attrib(GQ,"isSB",1);
print("SEEDED_Q_SCALAR_NORMALIZATION_SB_MARK=1");
int raw_to_norm=ideal_is_zero(reduce(GQraw,GQ));'''

P_MARKER = "ideal Gred=std(GredRaw);"
P_REPLACEMENT = r'''ideal Gred=std(GredRaw);
// GredRaw and Gred generate the same ideal by construction.  Equality of
// their generated leading-term ideals therefore certifies that GredRaw is
// itself a standard basis; only after that certificate do we set isSB.
ideal LrawCandidate=std(lead(GredRaw));
ideal LstdCandidate=std(lead(Gred));
int qred_raw_lm_to_std=ideal_is_zero_p(reduce(LrawCandidate,LstdCandidate));
int qred_std_lm_to_raw=ideal_is_zero_p(reduce(LstdCandidate,LrawCandidate));
int qred_raw_is_gb=(qred_raw_lm_to_std && qred_std_lm_to_raw);
ideal GredCertified=GredRaw;
int qred_marked_reduces_std=0;
if (qred_raw_is_gb==1)
{
  attrib(GredCertified,"isSB",1);
  qred_marked_reduces_std=ideal_is_zero_p(reduce(Gred,GredCertified));
}
print("QRED_RAW_LM_TO_STD="+string(qred_raw_lm_to_std));
print("QRED_STD_LM_TO_RAW="+string(qred_std_lm_to_raw));
print("QRED_RAW_IS_GB="+string(qred_raw_is_gb));
print("QRED_CERTIFIED_REDUCES_STD="+string(qred_marked_reduces_std));
if ((qred_raw_is_gb==0)||(qred_marked_reduces_std==0))
{
  print("QRED_RAW_GB_CERTIFICATE=FAIL");
  quit;
}
print("QRED_RAW_GB_CERTIFICATE=PASS");'''

LIFT_MARKER = "int lift_ok=(red_to_native && native_to_red && lm_red_to_native &&"
LIFT_REPLACEMENT = (
    "int lift_ok=(qred_raw_is_gb && qred_marked_reduces_std &&\n"
    "             red_to_native && native_to_red && lm_red_to_native &&"
)


def require_aws() -> None:
    vendor_path = pathlib.Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text(encoding="utf-8").strip() if vendor_path.exists() else ""
    if platform.system() != "Linux" or vendor != "Amazon EC2":
        raise RuntimeError("AWS EC2 only")
    if not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        raise RuntimeError("missing registered AWS lane tag")


def replace_once(text: str, marker: str, replacement: str) -> str:
    if text.count(marker) != 1:
        raise RuntimeError(f"expected one marker, found {text.count(marker)}: {marker}")
    return text.replace(marker, replacement, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("v2_input", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()
    require_aws()

    raw = args.v2_input.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_V2_INPUT:
        raise RuntimeError(f"V2 input hash mismatch: {actual}")
    text = raw.decode("utf-8")
    text = replace_once(text, Q_MARKER, Q_REPLACEMENT)
    text = replace_once(text, P_MARKER, P_REPLACEMENT)
    text = replace_once(text, LIFT_MARKER, LIFT_REPLACEMENT)

    required = (
        "SEEDED_Q_SCALAR_NORMALIZATION_SB_MARK=1",
        "QRED_RAW_GB_CERTIFICATE=PASS",
        "qred_raw_is_gb && qred_marked_reduces_std",
    )
    if any(text.count(token) != 1 for token in required):
        raise RuntimeError("V3 emitted sentinels are missing or nonunique")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"v2_input_sha256={EXPECTED_V2_INPUT}")
    print(f"output_sha256={hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
