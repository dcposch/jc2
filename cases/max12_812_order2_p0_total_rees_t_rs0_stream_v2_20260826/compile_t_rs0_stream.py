#!/usr/bin/env python3
"""AWS-only, row-streaming equivalent of the reviewed T-rs-0 client."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_discovery_20260826/compile_t_rs0_discovery.py"
OLD_SHA256 = "3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938"
REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-t-rs0-discovery-implementation-review-grok-20260826.md"
REVIEW_SHA256 = "51c294e0ae3d07ced3dac380814d4767bec1e5cc63bd1159cd76ce698f3f69ea"
PREREG = HERE / "PREREGISTRATION.md"
CHARACTERISTICS = (0, 32003, 65521, 1000033)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_stream_v2_")
    ):
        fail("streaming T-rs-0 compiler requires a registered AWS EC2 lane")
    return tag


def load_old():
    if digest(OLD) != OLD_SHA256:
        fail(("reviewed compiler hash mismatch", digest(OLD), OLD_SHA256))
    if digest(REVIEW) != REVIEW_SHA256:
        fail(("implementation review hash mismatch", digest(REVIEW), REVIEW_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_reviewed", OLD)
    if spec is None or spec.loader is None:
        fail("cannot import reviewed compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]], old) -> dict[str, object]:
    base = old.load_base()

    ell = [f"ell{i}" for i in range(1, 13)]
    cs = ["cs"] + [f"cs{i}" for i in range(1, 11)]
    rs = ["rs"] + [f"rs{i}" for i in range(1, 11)]
    az = ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 8)]
    ac = ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 8)]
    ez = ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 8)]
    ec = ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 8)]
    k10 = ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 9)]
    k6 = ["k6", "k6_1"]
    k2 = ["k2", "k2_1"]
    targets = ["mu2", "mu4", "mu6", "J"]

    frozen_ell = ell[:3]
    frozen_cs = cs[:3]
    frozen_rs = rs[:3]
    frozen_az = az[:3]
    frozen_ac = ac[:3]
    frozen_ez = ez[:3]
    frozen_ec = ec[:3]
    frozen_k10 = k10[:3]

    candidate_manifest = ell + cs + rs + az + ac + ez + ec + k10 + ["k6"]
    inactive_custody = ["k6_1", "k2", "k2_1"] + targets
    if len(candidate_manifest) != 76 or len(inactive_custody) != 7:
        fail("literal manifest census changed")

    p_total = "-2*rho^2+" + "+".join(f"2*sigma^{i}*ell{i}" for i in range(1, 13))
    p_frozen = "+".join(f"2*sigma^{i}*ell{i}" for i in range(1, 4))
    variables = ["sigma", "rho"] + ell + cs + rs + az + ac + ez + ec + k10 + k6 + k2 + targets
    if len(variables) != len(set(variables)) or len(variables) != 85:
        fail("streaming ring manifest is not the reviewed 85-name ring")

    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "ideal PrefixIdeal=std(ideal(sigma^13));",
        "qring Q=PrefixIdeal;",
        'print("T_RS0_SOURCE_HASHES=PASS");',
        'print("T_RS0_SCOPE=DISCOVERY_ONLY_MOD_SIGMA13_NO_REES_OR_CHART_VERDICT");',
        'print("T_RS0_IMPLEMENTATION=ROW_STREAM_V2");',
    ]
    lines += old.source_block("T_", p_total, cs, rs, az, ac, ez, ec, k10, k6, k2)
    lines += old.source_block(
        "F_", p_frozen, frozen_cs, frozen_rs, frozen_az,
        frozen_ac, frozen_ez, frozen_ec, frozen_k10, k6, k2,
    )
    lines += [
        "int prefixMap=1; int deck=1; int wrongLiteralDetected=0;",
        "int extraction=1; int coefficientMap=1; int syntheticOmission=0;",
        "int NZ0=0; int NZ1=0; int NZ2=0; int NZ3=0; int NZ4=0; int NZ5=0; int NZ6=0;",
        "int NZ7=0; int NZ8=0; int NZ9=0; int NZ10=0; int NZ11=0; int NZ12=0;",
    ]
    for name in candidate_manifest + inactive_custody:
        lines.append(f"int dep_{name}=0;")
    for name in (
        "TPhi", "FPhi", "TSpec", "Wrong", "TQ", "FQ", "Tg", "Fg", "TRem", "FRem",
        "KeepT10_2", "KeepT10_3", "KeepT12_6", "KeepF10_2", "KeepF10_3", "KeepF12_6",
    ):
        lines.append(f"poly {name}=0;")

    for row in range(1, 8):
        lines += [
            f"TPhi={old.phi_text(base, tails, row, 'T_')};",
            f"FPhi={old.phi_text(base, tails, row, 'F_')};",
            "TSpec=subst(TPhi,rho,0);",
            "if (TSpec-FPhi!=0) { prefixMap=0; }",
            "if (subst(TPhi,rho,-rho)-TPhi!=0) { deck=0; }",
            "Wrong=TSpec;",
        ]
        for name in ell:
            lines.append(f"Wrong=subst(Wrong,{name},0);")
        lines += [
            "if (Wrong-FPhi!=0) { wrongLiteralDetected=1; }",
            "if (subst(TSpec,ell1,0)-TSpec!=0) { syntheticOmission=1; }",
        ]
        for name in candidate_manifest + inactive_custody:
            lines.append(f"if (subst(TPhi,{name},0)-TPhi!=0) {{ dep_{name}=1; }}")
        lines += ["TQ=TPhi;", "FQ=FPhi;"]
        for grade in range(13):
            lines += [
                "Tg=subst(TQ,sigma,0);",
                "Fg=subst(FQ,sigma,0);",
                f"if (Tg!=0) {{ NZ{grade}=1; }}",
                "if (subst(Tg,rho,0)-Fg!=0) { coefficientMap=0; }",
                f'print("T_RS0_TERMS_{grade}_{row}="+string(size(Tg)));',
            ]
            if grade == 10 and row == 2:
                lines += ["KeepT10_2=Tg;", "KeepF10_2=Fg;"]
            if grade == 10 and row == 3:
                lines += ["KeepT10_3=Tg;", "KeepF10_3=Fg;"]
            if grade == 12 and row == 6:
                lines += ["KeepT12_6=Tg;", "KeepF12_6=Fg;"]
            if grade < 12:
                lines += [
                    "TRem=TQ-Tg; FRem=FQ-Fg;",
                    "TQ=TRem/sigma; FQ=FRem/sigma;",
                    "if (sigma*TQ-TRem!=0) { extraction=0; }",
                    "if (sigma*FQ-FRem!=0) { extraction=0; }",
                ]
        lines += [
            "TPhi=0; FPhi=0; TSpec=0; Wrong=0; TQ=0; FQ=0; Tg=0; Fg=0; TRem=0; FRem=0;",
            f'print("T_RS0_ROW_{row}_STREAM_RELEASED=1");',
        ]

    lines += [
        'print("T_RS0_PREFIX_SPECIALIZATION_MAP="+string(prefixMap));',
        'print("T_RS0_RHO_DECK_INVARIANCE="+string(deck));',
        'print("T_RS0_WRONG_LITERAL_P_NEGATIVE_CONTROL="+string(wrongLiteralDetected));',
        'print("T_RS0_EXTRACTION_IDENTITIES="+string(extraction));',
        'print("T_RS0_EXTRACTED_SPECIALIZATION_MAP="+string(coefficientMap));',
        'print("T_RS0_SYNTHETIC_ELL1_OMISSION_DETECTED="+string(syntheticOmission));',
        "int commonOrder=13; int orderFound=0;",
    ]
    for grade in range(13):
        lines += [
            f"if (NZ{grade}==1 && orderFound==0) {{ commonOrder={grade}; orderFound=1; }}",
            f'print("T_RS0_GRADE_{grade}_NONZERO="+string(NZ{grade}));',
        ]
    lines += [
        'print("T_RS0_COMMON_ORDER="+string(commonOrder));',
        "poly FrozenCert=32768*KeepF12_6-35*k*rs^4+4096*rs*KeepF10_2+8192*cs*KeepF10_3;",
        "poly FrozenOmit=32768*KeepF12_6-35*k*rs^4+4096*rs*KeepF10_2;",
        "int frozenCert=(FrozenCert==0);",
        "int frozenOmit=(FrozenOmit==-1536*cs*c0*c1 && FrozenOmit!=0);",
        'print("T_RS0_FROZEN_CUSP_CERTIFICATE="+string(frozenCert));',
        'print("T_RS0_FROZEN_OMIT_G10_3_NEGATIVE_CONTROL="+string(frozenOmit));',
        "poly Delta=32768*KeepT12_6-35*k*rs^4+4096*rs*KeepT10_2+8192*cs*KeepT10_3;",
        "int deltaSpecial=(subst(Delta,rho,0)==0);",
        "int deltaEven=(subst(Delta,rho,-rho)==Delta);",
        "ideal Rho2=std(ideal(rho^2));",
        "int deltaRho2=(reduce(Delta,Rho2)==0);",
        "poly DeltaQ=Delta/rho^2;",
        "int deltaMultiplyBack=(rho^2*DeltaQ-Delta==0);",
        "int deltaNonzero=(Delta!=0);",
        'print("T_RS0_DELTA_SPECIAL_FIBRE_ZERO="+string(deltaSpecial));',
        'print("T_RS0_DELTA_EVEN="+string(deltaEven));',
        'print("T_RS0_DELTA_RHO2_DIVISIBLE="+string(deltaRho2));',
        'print("T_RS0_DELTA_MULTIPLY_BACK="+string(deltaMultiplyBack));',
        'print("T_RS0_DELTA_NONZERO="+string(deltaNonzero));',
        'print("T_RS0_DELTA_QUOTIENT_TERMS="+string(size(DeltaQ)));',
    ]
    for name in candidate_manifest + inactive_custody:
        lines.append(f'print("T_RS0_DEP_{name}="+string(dep_{name}));')
    lines += [
        "if (prefixMap*deck*wrongLiteralDetected*extraction*coefficientMap*frozenCert*frozenOmit*deltaSpecial*deltaEven*deltaRho2*deltaMultiplyBack*syntheticOmission!=1) { print(\"T_RS0_FAIL=SOURCE_FIDELITY_OR_CONTROL\"); quit; }",
        'print("T_RS0_DISCOVERY_ENDPOINT=PASS_NAVIGATION_ONLY_MANIFEST_NOT_FROZEN");',
        "quit;",
    ]
    path.write_text("\n".join(lines) + "\n")
    return {
        "candidate_manifest": candidate_manifest,
        "inactive_custody": inactive_custody,
        "candidate_manifest_count": len(candidate_manifest),
        "ring_variable_count": len(variables),
        "implementation": "ROW_STREAM_V2",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()
    tag = require_aws()
    old = load_old()
    for source, expected in old.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("transitive frozen source mismatch", str(source), actual, expected))
    tails = json.loads(old.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != old.EXPECTED_CANONICAL_TAILS:
        fail("canonical tails mismatch")
    if sum(len(tails[str(row)]) for row in range(1, 8)) != 569:
        fail("frozen tail census mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"t_rs0_stream_{label}.sing"
    manifest = emit(singular, args.characteristic, tails, old)
    result = {
        "status": "PASS-T-RS0-DISCOVERY-COMPILER",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(singular),
        "tails_sha256": digest(old.TAILS),
        "canonical_tails_sha256": old.EXPECTED_CANONICAL_TAILS,
        "reviewed_compiler_sha256": OLD_SHA256,
        "implementation_review_sha256": REVIEW_SHA256,
        "preregistration_sha256": digest(PREREG),
        **manifest,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
