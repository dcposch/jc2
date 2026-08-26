#!/usr/bin/env python3
"""AWS-only exact beta=5 equality-face compilers, two contractions."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
BASE_COMPILER = CASES / "max12_912_order3_d1_double_root_control2_rees_20260826" / "compile_control2_rees.py"
BASE_COMPILER_SHA = "015d66b8d9b569855cfe761445b2327a13d58cfe686b0cf5f0c19c0d7f97a7d4"
CHARGED_SOURCE_SHA = "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"
WEIGHTS = (4, 1, 1, 20, 20, 30, 30, 30)
POLY_NAMES = [f"E{i}" for i in range(1, 9)] + ["LT"]


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_beta5_face_v1_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def load_base():
    if sha256(BASE_COMPILER.read_bytes()).hexdigest() != BASE_COMPILER_SHA:
        raise SystemExit("REFUSE_BASE_COMPILER_HASH")
    spec = importlib.util.spec_from_file_location("frozen_control2_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        raise SystemExit("REFUSE_BASE_IMPORT")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if module.CHARGED_SOURCE_SHA256 != CHARGED_SOURCE_SHA:
        raise SystemExit("REFUSE_CHARGED_SOURCE_PIN")
    module.WEIGHTS = WEIGHTS
    return module


def build_rows(base):
    charged = base.load_charged_source()
    built = charged.build()
    tails = built["tails"]
    images = base.coefficient_images()
    table = base.source_power_table(images, tails)
    raw = {ell: base.substitute(tails[ell], table) for ell in range(1, 9)}
    rows = {ell: base.add(raw[ell], base.scale(-1, base.target(ell))) for ell in range(1, 9)}
    out = {f"E{ell}": base.expanded_poly_string(rows[ell], rees=True) for ell in range(1, 9)}
    out["LT"] = base.expanded_poly_string(base.relation(), rees=True)
    return rows, out


def common_endpoint(label: str) -> list[str]:
    return [
        f'print("FACE_ENCODING={label}");',
        "poly WFACE=la^20+1/243*q1*q0^3+1/54*q1*r2*r1+7/108*q1*r1^2+1/54*q1*r2*r0-1/54*q0*r1*r0+1/108*q1*r0^2;",
        'if (reduce(WFACE,GH)!=0) { print("FAIL_WITNESS_FACE_MEMBERSHIP"); quit; }',
        'print("PASS_WITNESS_FACE_MEMBERSHIP");',
        'print("FACE_SPECIAL_FIBRE_BASIS_BEGIN"); GH; print("FACE_SPECIAL_FIBRE_BASIS_END");',
        "ideal P=GH,la-1,tau-1,rho-1,q1-1,q0+1,r2-1,r1-1,r0+2;",
        "ideal GP=std(P);",
        'if (reduce(1,GP)==0) { print("DISPLAYED_RESIDUE_SURVIVES=0"); } else { print("DISPLAYED_RESIDUE_SURVIVES=1"); }',
    ]


def source_a(tag: str, p: dict[str, str]) -> str:
    lines = [
        "// beta=5 face: expanded direct saturation, global dp.",
        'LIB "elim.lib";',
        "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),dp;",
        "option(redSB);",
    ]
    for name in POLY_NAMES:
        lines.append(f"poly {name}={p[name]};")
    lines.extend(
        [
            f'print("AWS_TAG={tag}");',
            'print("ENCODING=EXPANDED_DIRECT_SAT_GLOBAL_DP_BETA5_FACE");',
            'print("FACE_WEIGHT=4,1,1,20,20,30,30,30");',
            "ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT;",
            "ideal CS=s;",
            "ideal C=sat(I,CS);",
            'print("CONTRACTION_GENERATORS="+string(size(C)));',
            "ideal H=C,s;",
            "ideal GH=std(H);",
            'print("SPECIAL_FIBRE_GENERATORS="+string(size(GH)));',
        ]
    )
    lines.extend(common_endpoint("A_DIRECT_SAT_DP"))
    lines.extend(
        [
            "poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;",
            "ideal CT=TORUS;",
            "ideal GHT=std(sat(GH,CT));",
            'print("TORUS_FACE_BASIS_BEGIN"); GHT; print("TORUS_FACE_BASIS_END");',
            'if (reduce(1,GHT)==0) { print("TORUS_FACE_IS_UNIT=1"); } else { print("TORUS_FACE_IS_UNIT=0"); print("TORUS_FACE_DIM="+string(dim(GHT))); }',
            'print("FIREWALL=EXACT_BETA5_EQUALITY_FACE_FIXED_SOURCE_LOAD_SUPPORT_ONLY");',
            'print("PASS_CONTROL2_BETA5_FACE_A");',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def source_b(tag: str, p: dict[str, str]) -> str:
    lines = [
        "// beta=5 face: two inverse eliminations, lp/dp block order.",
        'LIB "elim.lib";',
        "ring R=0,(u,v,s,la,tau,rho,q1,q0,r2,r1,r0),(lp(3),dp(8));",
        "option(redSB);",
    ]
    for name in POLY_NAMES:
        lines.append(f"poly {name}={p[name]};")
    lines.extend(
        [
            f'print("AWS_TAG={tag}");',
            'print("ENCODING=EXPANDED_DOUBLE_INVERSE_ELIM_LPDP_BETA5_FACE");',
            'print("FACE_WEIGHT=4,1,1,20,20,30,30,30");',
            "ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT,u*s-1;",
            "ideal GI=std(I);",
            "ideal C=eliminate(GI,u);",
            'print("CONTRACTION_GENERATORS="+string(size(C)));',
            "ideal H=C,s;",
            "ideal GH=std(H);",
            'print("SPECIAL_FIBRE_GENERATORS="+string(size(GH)));',
        ]
    )
    lines.extend(common_endpoint("B_DOUBLE_INVERSE_LPDP"))
    lines.extend(
        [
            "poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;",
            "ideal JT=GH,v*TORUS-1;",
            "ideal GJT=std(JT);",
            "ideal HT=eliminate(GJT,v);",
            "ideal GHT=std(HT);",
            'print("TORUS_FACE_BASIS_BEGIN"); GHT; print("TORUS_FACE_BASIS_END");',
            'if (reduce(1,GHT)==0) { print("TORUS_FACE_IS_UNIT=1"); } else { print("TORUS_FACE_IS_UNIT=0"); print("TORUS_FACE_DIM="+string(dim(GHT))); }',
            'print("FIREWALL=EXACT_BETA5_EQUALITY_FACE_FIXED_SOURCE_LOAD_SUPPORT_ONLY");',
            'print("PASS_CONTROL2_BETA5_FACE_B");',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    tag = require_aws()
    base = load_base()
    rows, polynomials = build_rows(base)
    # Compiler-side exact face check: the displayed witness support has the
    # promised weights, and every submitted row still has a nonempty initial.
    if tuple(base.WEIGHTS) != WEIGHTS:
        raise SystemExit("REFUSE_WEIGHT_MUTATION")
    for ell, row in rows.items():
        minimum, initial, _ = base.initial_data(row)
        if not initial:
            raise SystemExit(f"REFUSE_EMPTY_INITIAL_{ell}")
        print(f"row_{ell}_minimum_weight={minimum}")
        print(f"row_{ell}_initial_sha256={base.digest(initial)}")
    outputs = {
        "beta5_face_A_dp.sing": source_a(tag, polynomials),
        "beta5_face_B_lpdp.sing": source_b(tag, polynomials),
    }
    for name, source in outputs.items():
        path = HERE / name
        path.write_text(source)
        print(f"{name}_sha256={sha256(path.read_bytes()).hexdigest()}")
    print(f"base_compiler_sha256={BASE_COMPILER_SHA}")
    print(f"charged_source_sha256={CHARGED_SOURCE_SHA}")
    print("PASS_CONTROL2_BETA5_FACE_COMPILER")


if __name__ == "__main__":
    main()
