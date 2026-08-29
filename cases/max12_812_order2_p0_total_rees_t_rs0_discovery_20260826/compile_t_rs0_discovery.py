#!/usr/bin/env python3
"""Compile the AWS-only T-rs-0 moving-source discovery client."""

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
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
BASE = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
OWNER = ROOT / "cases/max12_812_order2_p0_cusp_g10_g11_20260826/compile_p0_cusp_g10_g11.py"
RAW_V2 = ROOT / "cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/compile_raw_cusp_g12_cech_v2.py"
AUDIT = ROOT / "xmodel/max12-812-order2-p0-total-rees-t-rs-implementation-audit-codex-20260826.md"
GATE = ROOT / "xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md"
PREREG = HERE / "PREREGISTRATION.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    OWNER: "9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4",
    RAW_V2: "8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d",
    AUDIT: "5e91571d84b1bae92306bad0a31924a2b4fe3bf183ee8d75ace558bc2dd52c0d",
    GATE: "50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4",
}
EXPECTED_CANONICAL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
MAX_GRADE = 12


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
        or not tag
    ):
        fail("T-rs-0 compiler is restricted to a registered AWS EC2 lane")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("t_rs0_tail_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot import frozen tail compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def series(names: list[str]) -> str:
    return "+".join(name if index == 0 else f"sigma^{index}*{name}" for index, name in enumerate(names))


def shifted_series(shift: int, names: list[str]) -> str:
    return f"sigma^{shift}*({series(names)})"


def source_block(prefix: str, p: str, c_names: list[str], r_names: list[str],
                 az_names: list[str], ac_names: list[str], ez_names: list[str],
                 ec_names: list[str], k10_names: list[str], k6_names: list[str],
                 k2_names: list[str]) -> list[str]:
    c = shifted_series(2, c_names)
    rr = f"(({p})^2+sigma^2*({series(r_names)}))/4"
    az = series(az_names)
    ac = series(ac_names)
    ez = series(ez_names)
    ec = series(ec_names)
    return [
        f"poly {prefix}p={p};",
        f"poly {prefix}c={c};",
        f"poly {prefix}r={rr};",
        f"poly {prefix}n3=sigma^3*({az});",
        f"poly {prefix}n2=sigma^3*({ac});",
        f"poly {prefix}n1=sigma^3*(({prefix}p*({az})+({ez}))/2);",
        f"poly {prefix}n0=sigma^3*(({prefix}p*({ac})+({ec}))/2);",
        f"poly {prefix}F6=2*{prefix}p;",
        f"poly {prefix}F5=2*{prefix}c;",
        f"poly {prefix}F4={prefix}p^2+2*{prefix}r;",
        f"poly {prefix}F3=2*{prefix}p*{prefix}c+sigma^2*{prefix}n3;",
        f"poly {prefix}F2={prefix}c^2+2*{prefix}p*{prefix}r+sigma^2*{prefix}n2;",
        f"poly {prefix}F1=2*{prefix}c*{prefix}r+sigma^2*{prefix}n1;",
        f"poly {prefix}F0={prefix}r^2+sigma^2*{prefix}n0;",
        f"poly {prefix}K10={series(k10_names)};",
        f"poly {prefix}K6={series(k6_names)};",
        f"poly {prefix}K2={series(k2_names)};",
    ]


def phi_text(base, tails: dict[str, list[list[object]]], row: int, prefix: str) -> str:
    coeffs = {index: f"{prefix}F{index}" for index in range(7)}
    loads = {"k10": f"{prefix}K10", "k6": f"{prefix}K6", "k2": f"{prefix}K2"}
    expression = base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    if targets[row] != "0":
        expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
    return expression


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> dict[str, object]:
    base = load_base()

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

    p_total = "-2*rho^2+" + "+".join(f"2*sigma^{i}*ell{i}" for i in range(1, 13))
    p_frozen = "+".join(f"2*sigma^{i}*ell{i}" for i in range(1, 4))
    variables = ["sigma", "rho"] + ell + cs + rs + az + ac + ez + ec + k10 + k6 + k2 + targets
    if len(variables) != len(set(variables)):
        fail("duplicate Singular variable in total-source manifest")

    candidate_manifest = ell + cs + rs + az + ac + ez + ec + k10 + ["k6"]
    inactive_custody = ["k6_1", "k2", "k2_1"] + targets

    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "ideal PrefixIdeal=std(ideal(sigma^13));",
        "qring Q=PrefixIdeal;",
        'print("T_RS0_SOURCE_HASHES=PASS");',
        'print("T_RS0_SCOPE=DISCOVERY_ONLY_MOD_SIGMA13_NO_REES_OR_CHART_VERDICT");',
    ]
    lines += source_block("T_", p_total, cs, rs, az, ac, ez, ec, k10, k6, k2)
    lines += source_block("F_", p_frozen, frozen_cs, frozen_rs, frozen_az,
                          frozen_ac, frozen_ez, frozen_ec, frozen_k10, k6, k2)

    for row in range(1, 8):
        lines.append(f"poly TPhi{row}={phi_text(base, tails, row, 'T_')};")
        lines.append(f"poly FPhi{row}={phi_text(base, tails, row, 'F_')};")

    lines += [
        "int prefixMap=1; int deck=1; int wrongLiteralDetected=0;",
    ]
    for row in range(1, 8):
        lines += [
            f"poly TSpec{row}=subst(TPhi{row},rho,0);",
            f"if (TSpec{row}-FPhi{row}!=0) {{ prefixMap=0; }}",
            f"if (subst(TPhi{row},rho,-rho)-TPhi{row}!=0) {{ deck=0; }}",
            f"poly Wrong{row}=TSpec{row};",
        ]
        for name in ell:
            lines.append(f"Wrong{row}=subst(Wrong{row},{name},0);")
        lines.append(f"if (Wrong{row}-FPhi{row}!=0) {{ wrongLiteralDetected=1; }}")

    lines += [
        'print("T_RS0_PREFIX_SPECIALIZATION_MAP="+string(prefixMap));',
        'print("T_RS0_RHO_DECK_INVARIANCE="+string(deck));',
        'print("T_RS0_WRONG_LITERAL_P_NEGATIVE_CONTROL="+string(wrongLiteralDetected));',
        "int extraction=1; int coefficientMap=1; int commonOrder=13; int orderFound=0;",
    ]

    for row in range(1, 8):
        lines.append(f"poly TQ0_{row}=TPhi{row}; poly FQ0_{row}=FPhi{row};")
    for grade in range(MAX_GRADE + 1):
        lines.append(f"int NZ{grade}=0;")
        for row in range(1, 8):
            lines += [
                f"poly Tg{grade}_{row}=subst(TQ{grade}_{row},sigma,0);",
                f"poly Fg{grade}_{row}=subst(FQ{grade}_{row},sigma,0);",
                f"if (Tg{grade}_{row}!=0) {{ NZ{grade}=1; }}",
                f"if (subst(Tg{grade}_{row},rho,0)-Fg{grade}_{row}!=0) {{ coefficientMap=0; }}",
                f'print("T_RS0_TERMS_{grade}_{row}="+string(size(Tg{grade}_{row})));',
            ]
            if grade < MAX_GRADE:
                lines += [
                    f"poly TRem{grade + 1}_{row}=TQ{grade}_{row}-Tg{grade}_{row};",
                    f"poly FRem{grade + 1}_{row}=FQ{grade}_{row}-Fg{grade}_{row};",
                    f"poly TQ{grade + 1}_{row}=TRem{grade + 1}_{row}/sigma;",
                    f"poly FQ{grade + 1}_{row}=FRem{grade + 1}_{row}/sigma;",
                    f"if (sigma*TQ{grade + 1}_{row}-TRem{grade + 1}_{row}!=0) {{ extraction=0; }}",
                    f"if (sigma*FQ{grade + 1}_{row}-FRem{grade + 1}_{row}!=0) {{ extraction=0; }}",
                ]
        lines += [
            f"if (NZ{grade}==1 && orderFound==0) {{ commonOrder={grade}; orderFound=1; }}",
            f'print("T_RS0_GRADE_{grade}_NONZERO="+string(NZ{grade}));',
        ]

    lines += [
        'print("T_RS0_COMMON_ORDER="+string(commonOrder));',
        'print("T_RS0_EXTRACTION_IDENTITIES="+string(extraction));',
        'print("T_RS0_EXTRACTED_SPECIALIZATION_MAP="+string(coefficientMap));',
        "poly FrozenCert=32768*Fg12_6-35*k*rs^4+4096*rs*Fg10_2+8192*cs*Fg10_3;",
        "poly FrozenOmit=32768*Fg12_6-35*k*rs^4+4096*rs*Fg10_2;",
        "int frozenCert=(FrozenCert==0);",
        "int frozenOmit=(FrozenOmit==-1536*cs*c0*c1 && FrozenOmit!=0);",
        'print("T_RS0_FROZEN_CUSP_CERTIFICATE="+string(frozenCert));',
        'print("T_RS0_FROZEN_OMIT_G10_3_NEGATIVE_CONTROL="+string(frozenOmit));',
        "poly Delta=32768*Tg12_6-35*k*rs^4+4096*rs*Tg10_2+8192*cs*Tg10_3;",
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
        "int syntheticOmission=0;",
    ]
    for row in range(1, 8):
        lines.append(f"if (subst(TSpec{row},ell1,0)-TSpec{row}!=0) {{ syntheticOmission=1; }}")
    lines.append('print("T_RS0_SYNTHETIC_ELL1_OMISSION_DETECTED="+string(syntheticOmission));')

    for name in candidate_manifest + inactive_custody:
        flag = "dep_" + name
        lines.append(f"int {flag}=0;")
        for row in range(1, 8):
            lines.append(f"if (subst(TPhi{row},{name},0)-TPhi{row}!=0) {{ {flag}=1; }}")
        lines.append(f'print("T_RS0_DEP_{name}="+string({flag}));')

    lines += [
        "if (prefixMap*deck*wrongLiteralDetected*extraction*coefficientMap*frozenCert*frozenOmit*deltaSpecial*deltaEven*deltaRho2*deltaMultiplyBack*syntheticOmission!=1) { print(\"T_RS0_FAIL=SOURCE_FIDELITY_OR_CONTROL\"); quit; }",
        'print("T_RS0_DISCOVERY_ENDPOINT=PASS_NAVIGATION_ONLY_MANIFEST_NOT_FROZEN");',
        "quit;",
    ]
    path.write_text("\n".join(lines) + "\n")
    return {
        "candidate_manifest": candidate_manifest,
        "inactive_custody": inactive_custody,
        "ring_variable_count": len(variables),
        "candidate_manifest_count": len(candidate_manifest),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_CANONICAL_TAILS:
        fail("canonical tails mismatch")
    if sum(len(tails[str(row)]) for row in range(1, 8)) != 569:
        fail("frozen tail count mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"t_rs0_discovery_{label}.sing"
    manifest = emit(singular, args.characteristic, tails)
    result = {
        "status": "PASS-T-RS0-DISCOVERY-COMPILER",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(singular),
        "tails_sha256": digest(TAILS),
        "canonical_tails_sha256": EXPECTED_CANONICAL_TAILS,
        "preregistration_sha256": digest(PREREG),
        **manifest,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
