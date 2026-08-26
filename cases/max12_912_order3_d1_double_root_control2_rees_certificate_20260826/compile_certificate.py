#!/usr/bin/env python3
"""AWS-only source-preserving compiler for the Rees monomial certificate."""

from hashlib import sha256
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
BASE = HERE / "base_B.sing"
BASE_SHA256 = "c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b"
OLD_TAG = "max12_912_order3_d1_double_root_control2_rees_v2_20260826T005028Z_r6d_B"
ANCHOR = "poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;\n"


def main() -> None:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_control2_rees_certificate_"):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    if sha256(BASE.read_bytes()).hexdigest() != BASE_SHA256:
        raise SystemExit("REFUSE_BASE_HASH")
    source = BASE.read_text()
    if source.count(OLD_TAG) != 1 or source.count(ANCHOR) != 1:
        raise SystemExit("REFUSE_ANCHOR_COUNT")
    source = source.replace(OLD_TAG, tag)
    certificate = ANCHOR + """print(\"FULL_SPECIAL_FIBRE_BASIS_BEGIN\");
GH;
print(\"FULL_SPECIAL_FIBRE_BASIS_END\");
ideal CT=TORUS;
list SW=sat_with_exp(GH,CT);
ideal GSAT=std(SW[1]);
int SATEXP=SW[2];
print(\"TORUS_SATURATION_EXPONENT=\"+string(SATEXP));
if (reduce(1,GSAT)!=0) { print(\"FAIL_CERTIFICATE_TORUS_SAT_NOT_UNIT\"); quit; }
poly MONWIT=TORUS^SATEXP;
if (reduce(MONWIT,GH)!=0) { print(\"FAIL_CERTIFICATE_MONOMIAL_NOT_IN_GH\"); quit; }
print(\"MONOMIAL_WITNESS=TORUS^\"+string(SATEXP));
print(\"PASS_CONTROL2_REES_MONOMIAL_CERTIFICATE\");
"""
    source = source.replace(ANCHOR, certificate)
    output = HERE / "compiled_certificate.sing"
    output.write_text(source)
    print(f"base_sha256={BASE_SHA256}")
    print(f"output_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("PASS_CONTROL2_REES_CERTIFICATE_COMPILER")


if __name__ == "__main__":
    main()

