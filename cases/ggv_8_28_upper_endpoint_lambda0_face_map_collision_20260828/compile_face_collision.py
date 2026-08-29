#!/usr/bin/env python3
"""Compile the lambda=0 born-mode face-map collision charts exactly."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
DEEP_NEWTON = ROOT / "cases/ggv_8_28_upper_endpoint_deep_newton_kernel_family_20260828/verify_deep_newton_kernel_family.py"
DEEP_Q1_R1 = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py"
PINS = {
    BASE: "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    DEEP_NEWTON: "0b873f2b4e0cdd4f55312dea6bf2d69d4fcbb3bb03c5725c082028148847c99f",
    DEEP_Q1_R1: "a5e6479f20cd7fcd50b317e174fd192512e5295de9c2126e717c005cb22acf69",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_base():
    spec = importlib.util.spec_from_file_location("ggv_face_collision_base", BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ce = load_base()
MV = ce.MV


def series_add(left, right, maximum):
    return [(left[i] if i < len(left) else MV.zero())
            + (right[i] if i < len(right) else MV.zero())
            for i in range(maximum + 1)]


def series_mul(left, right, maximum):
    out = [MV.zero() for _ in range(maximum + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] = out[i + j] + a * b
    return out


def series_scale(poly, scalar, maximum):
    return [poly[i].scale(scalar) if i < len(poly) else MV.zero()
            for i in range(maximum + 1)]


def series_power(base, exponent, maximum):
    assert base[0] == MV.const(1)
    u = list(base[:maximum + 1]) + [MV.zero()] * max(0, maximum + 1 - len(base))
    u[0] = u[0] - MV.const(1)
    out = [MV.zero() for _ in range(maximum + 1)]
    power = [MV.const(1)] + [MV.zero() for _ in range(maximum)]
    choose = Q(1)
    for k in range(maximum + 1):
        if k:
            power = series_mul(power, u, maximum)
            choose *= (exponent - (k - 1)) / k
        out = series_add(out, series_scale(power, choose, maximum), maximum)
    return out


def face_map(prefix: str, maximum=11):
    a = MV.var(f"{prefix}a")
    b = MV.var(f"{prefix}b")
    c = MV.var(f"{prefix}c")
    # The rescaled face coordinates are literal:
    #     p(z)=(1+a*z)^2+b*z^3+c*z^4.
    p = [MV.const(1), a.scale(2), a * a, b, c]
    result = series_power(p, Q(3, 2), maximum)
    # Only the shared lower modes occurring on this face are retained.
    # In particular d2=d6=0; silently reintroducing them changes the map.
    for k in (1, 3, 4, 5):
        power = series_power(p, Q(6 - k, 4), maximum - k)
        shifted = [MV.zero()] * k + [value * MV.var(f"d{k}") for value in power]
        result = series_add(result, shifted, maximum)
    born = {}
    for k in range(7, 11):
        born[k] = -result[k]
        power = series_power(p, Q(6 - k, 4), maximum - k)
        shifted = [MV.zero()] * k + [value * born[k] for value in power]
        result = series_add(result, shifted, maximum)
        assert not result[k].terms
    # Root derivation predicts that the recursively born tenth mode vanishes
    # identically on this rescaled face, not merely at the desk-check seed.
    assert not born[10].terms
    return born, result[11]


def evaluate(poly, assignments):
    total = Q(0)
    for mon, coefficient in poly.terms.items():
        value = coefficient
        for name in mon:
            value *= Q(assignments.get(name, 0))
        total += value
    return total


def desk_check():
    for path, expected in PINS.items():
        assert sha256(path) == expected, path
    born, rho = face_map("u")
    seed = {"ua": Q(-1, 16), "ub": 0, "uc": 0, "d1": 1, "d3": 1}
    expected = {
        7: Q(-6139, 17179869184),
        8: Q(0),
        9: Q(16369, 140737488355328),
        10: Q(0),
    }
    actual = {k: evaluate(born[k], seed) for k in born}
    assert actual == expected
    assert evaluate(rho, seed) == Q(9207, 144115188075855872)
    return {
        "status": "DESK_CHECK_PASS",
        "seed_born_modes": {str(k): str(value) for k, value in actual.items()},
        "seed_rho": str(evaluate(rho, seed)),
        "pins": {str(path.relative_to(ROOT)): sha256(path) for path in PINS},
    }


def system():
    born_u, rho_u = face_map("u")
    born_v, rho_v = face_map("v")
    equations = []
    for k in range(7, 10):
        poly = born_u[k] - born_v[k]
        encoded = poly.encode()
        equations.append({
            "kind": "collision", "born_mode": k, "terms": encoded,
            "sha256": hashlib.sha256(ce.compact(encoded)).hexdigest(),
        })
    return {
        "schema": "GGV-8_28-UPPER-LAMBDA0-FACE-COLLISION-v2",
        "field": "Q",
        "coordinates": "p(z)=(1+a*z)^2+b*z^3+c*z^4",
        "variables": ["ua", "ub", "uc", "va", "vb", "vc",
                      "d1", "d3", "d4", "d5"],
        "equations": equations,
        "born_u": {str(k): born_u[k].encode() for k in born_u},
        "born_v": {str(k): born_v[k].encode() for k in born_v},
        "rho_u": rho_u.encode(),
        "rho_v": rho_v.encode(),
        "born_10_identity": not born_u[10].terms and not born_v[10].terms,
        "rho_difference": (rho_u - rho_v).encode(),
        "open_conditions": {"c2": "d1!=0", "off_diagonal": "(ua-va,ub-vb,uc-vc)!=0"},
        "chart_cover": ["a", "b", "c"],
        "scope": "lambda=0 rescaled face map only; B7/B8/B9 collision existence discriminator; B10 is identically zero",
        "pins": {str(path.relative_to(ROOT)): digest for path, digest in PINS.items()},
    }


def decode(encoded):
    return MV({tuple(mon): Q(coefficient) for mon, coefficient in encoded})


def singular(system_data, chart, prime, include_rho=False, decompose=False, tracked=False):
    assert chart in ("a", "b", "c")
    diff = {"a": "ua-va", "b": "ub-vb", "c": "uc-vc"}[chart]
    variables = ["invdelta", "invc2"] + system_data["variables"]
    expressions = [decode(item["terms"]).expression(prime)
                   for item in system_data["equations"]]
    if include_rho:
        expressions.append(decode(system_data["rho_difference"]).expression(prime))
    expressions += ["invc2*d1-1", f"invdelta*({diff})-1"]
    lines = [
        f"ring collision={prime},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(expressions) + ";",
        f'print("CHART={chart} PRIME={prime} RHO_EQUAL={int(include_rho)}");',
        'print("VARIABLES="+string(nvars(basering))+" GENERATORS="+string(size(I)));',
        "int start_time=timer;",
    ]
    if tracked:
        lines += [
            "matrix T; ideal J=liftstd(I,T);",
            "matrix basis_replay=matrix(I)*T-matrix(J);",
            'print("BASIS_REPLAY_ZERO="+string(size(module(basis_replay))==0));',
        ]
    else:
        lines.append("ideal J=std(I);")
    lines += [
        "int elapsed=timer-start_time;",
        'print("SECONDS="+string(elapsed));',
        'int is_unit=(size(J)==1 && J[1]==1);',
        'print("UNIT="+string(is_unit));',
        'print("BASIS_SIZE="+string(size(J)));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
    ]
    if tracked:
        lines += [
            "if(is_unit){",
            "  matrix H=lift(J,ideal(1)); matrix C=T*H;",
            "  matrix replay=matrix(I)*C-matrix(ideal(1));",
            '  print("UNIT_REPLAY_ZERO="+string(size(module(replay))==0));',
            '  write("unit_cofactors.txt",C);',
            "}",
        ]
    if decompose:
        lines += [
            'if(!is_unit){LIB "primdec.lib"; list L=minAssGTZ(I);',
            'print("MINASS_COUNT="+string(size(L)));',
            'for(int ii=1;ii<=size(L);ii++){print("COMPONENT="+string(ii)); print(L[ii]);}}',
        ]
    lines += ["quit;", ""]
    return "\n".join(lines)


def write_outputs(output_dir: Path):
    audit = desk_check()
    data = system()
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        "DESK_CHECK.json": ce.pretty(audit),
        "COLLISION_SYSTEM.json": ce.pretty(data),
        "FORMULAS.txt": (
            "p_u(z)=(1+ua*z)^2+ub*z^3+uc*z^4\n"
            "p_v(z)=(1+va*z)^2+vb*z^3+vc*z^4\n"
            + "\n".join(
                f"B{k}_u={face_map('u')[0][k].expression(0)}"
                for k in range(7, 11)
            )
            + "\n"
            + "\n".join(
                f"B{k}_v={face_map('v')[0][k].expression(0)}"
                for k in range(7, 11)
            )
            + f"\nrho_u={face_map('u')[1].expression(0)}\n"
            + f"rho_v={face_map('v')[1].expression(0)}\n"
        ).encode(),
    }
    for chart in ("a", "b", "c"):
        for prime in (65521, 65519, 65497):
            payloads[f"chart_{chart}_p{prime}.sing"] = singular(
                data, chart, prime).encode()
            payloads[f"chart_{chart}_rho_equal_p{prime}.sing"] = singular(
                data, chart, prime, include_rho=True).encode()
        payloads[f"chart_{chart}_factor_p65521.sing"] = singular(
            data, chart, 65521, decompose=True).encode()
        payloads[f"chart_{chart}_q_tracked.sing"] = singular(
            data, chart, 0, tracked=True).encode()
    manifest = {}
    for name, payload in payloads.items():
        (output_dir / name).write_bytes(payload)
        manifest[name] = hashlib.sha256(payload).hexdigest()
    (output_dir / "GENERATED.sha256.json").write_bytes(ce.pretty(manifest))
    print(json.dumps({
        "status": "COMPILE_PASS", "variables": len(data["variables"]),
        "equations": len(data["equations"]), "charts": 3,
        "born_10_identity": data["born_10_identity"],
        "system_sha256": manifest["COLLISION_SYSTEM.json"],
    }, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desk-check", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.desk_check == (args.output_dir is not None):
        parser.error("choose exactly one of --desk-check or --output-dir")
    if args.desk_check:
        print(json.dumps(desk_check(), indent=2, sort_keys=True))
    else:
        write_outputs(args.output_dir)


if __name__ == "__main__":
    main()
