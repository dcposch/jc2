#!/usr/bin/env python3
"""AWS-only exact H17 upper graph-load relative-cone analysis."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V4Q = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/evidence/Box02/aws_qdag/output/abstract_functional_support.json"
V4P = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/evidence/r6d/aws_pdag/output/abstract_functional_support.json"
V6Q = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/evidence/Box02/aws_qsecondary/output/abstract_secondary_support.json"
V6P = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/evidence/r6d/aws_psecondary/output/abstract_secondary_support.json"
EXPECTED = {
    V4Q: "9ee52ed12c5ca75b0f36fdaf4292be6165d6a4380550c87faab3a654b23306bc",
    V4P: "b6eafc795464b7e7e077df2b2ea0fd58d7c963b14988e3d5322b312cafdf19a9",
    V6Q: "357829d292056e823c102446b8e95f5822dad961859e832a689160bca1e3fbcd",
    V6P: "742783f9679cea0e9bcb946d16d6aeaa6104f99e638283a1661c8929794dd197",
}
PRIME = 65521
H = 17


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only upper-graph analyzer refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only upper-graph analyzer refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load(path: Path, prime: bool):
    data = json.loads(path.read_text())
    poly = {}
    for record in data["terms"]:
        exponent = tuple(int(value) for value in record["exponents"])
        coefficient = int(record["coefficient"]) if prime else Fraction(record["coefficient"])
        poly[exponent] = coefficient
    return tuple(data["variables"]), poly


def subtract(left, right, prime: bool):
    result = dict(left)
    for exponent, coefficient in right.items():
        value = result.get(exponent, 0) - 32 * coefficient
        if prime:
            value %= PRIME
        if value:
            result[exponent] = value
        else:
            result.pop(exponent, None)
    return result


def graph_reduce(names, poly, prime: bool):
    index = {name: offset for offset, name in enumerate(names)}
    ratio6 = (15 * pow(32, -1, PRIME)) % PRIME if prime else Fraction(15, 32)
    ratio2 = (15 * pow(256, -1, PRIME)) % PRIME if prime else Fraction(15, 256)
    result = {}
    for exponent, coefficient in poly.items():
        reduced = list(exponent)
        k2 = reduced[index["K2"]]
        k6 = reduced[index["K6"]]
        reduced[index["K2"]] = 0
        reduced[index["K6"]] = 0
        reduced[index["K10"]] += k2 + k6
        reduced[index["E"]] += 4 * k2 + 2 * k6
        value = coefficient * pow(ratio2, k2) * pow(ratio6, k6)
        if prime:
            value %= PRIME
        key = tuple(reduced)
        value = result.get(key, 0) + value
        if prime:
            value %= PRIME
        if value:
            result[key] = value
        else:
            result.pop(key, None)
    return result


def mod_fraction(value: Fraction) -> int:
    return value.numerator % PRIME * pow(value.denominator % PRIME, -1, PRIME) % PRIME


def monomial(names, exponent):
    parts = []
    for name, power in zip(names, exponent):
        if power:
            parts.append(name if power == 1 else f"{name}^{power}")
    return "*".join(parts) or "1"


def line(names, exponent):
    index = {name: offset for offset, name in enumerate(names)}
    const = Fraction(57 * exponent[index["J"]])
    const += Fraction(42 * exponent[index["K10"]])
    const += Fraction(H * (exponent[index["a"]] + exponent[index["lambda"]]))
    slope = Fraction(2 * sum(exponent[index[name]] for name in ("S0", "S1", "R0", "R1")))
    slope += Fraction(exponent[index["Y"]] + exponent[index["X"]])
    slope -= Fraction(2 * exponent[index["a"]])
    return const, slope


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen support mismatch", path, digest(path), expected))
    names, f_q = load(V4Q, False)
    names6, g_q = load(V6Q, False)
    namesp, f_p = load(V4P, True)
    names6p, g_p = load(V6P, True)
    if not (names == names6 == namesp == names6p):
        fail("variable-order mismatch")
    h_q = graph_reduce(names, subtract(g_q, f_q, False), False)
    h_p = graph_reduce(names, subtract(g_p, f_p, True), True)
    if not h_q or len(h_q) > 630 or set(h_q) != set(h_p):
        fail(("graph-reduced support mismatch", len(h_q), len(h_p)))
    for exponent, coefficient in h_q.items():
        if mod_fraction(coefficient) != h_p[exponent]:
            fail(("coefficient reduction mismatch", exponent, coefficient, h_p[exponent]))
    index = {name: offset for offset, name in enumerate(names)}
    load_exp = [0] * len(names)
    load_exp[index["K10"]] = 1
    load_exp[index["a"]] = 3
    load_exp[index["E"]] = 7
    load_exp = tuple(load_exp)
    intrinsic_exp = [0] * len(names)
    intrinsic_exp[index["lambda"]] = 3
    intrinsic_exp[index["M"]] = 3
    intrinsic_exp[index["E"]] = 2
    intrinsic_exp = tuple(intrinsic_exp)
    if h_q.get(load_exp) != Fraction(5, 4):
        fail(("load coefficient mismatch", h_q.get(load_exp)))
    if h_q.get(intrinsic_exp) != Fraction(-2):
        fail(("intrinsic coefficient mismatch", h_q.get(intrinsic_exp)))

    base_const, base_slope = line(names, load_exp)
    lower, upper = Fraction(7), Fraction(17, 2)
    active_lower = []
    active_upper = []
    for exponent, coefficient in h_q.items():
        if exponent == load_exp:
            continue
        const, slope = line(names, exponent)
        dconst, dslope = const - base_const, slope - base_slope
        if dslope > 0:
            bound = -dconst / dslope
            if bound > lower:
                active_lower.append((bound, exponent, coefficient))
        elif dslope < 0:
            bound = -dconst / dslope
            if bound < upper:
                active_upper.append((bound, exponent, coefficient))
        elif dconst <= 0:
            fail(("q-independent load competitor", exponent, coefficient, dconst))
    sharp_lower = max([lower] + [item[0] for item in active_lower])
    sharp_upper = min([upper] + [item[0] for item in active_upper])
    if (sharp_lower, sharp_upper) != (lower, upper):
        fail(("unexpected upper graph interval", sharp_lower, sharp_upper))
    ties7 = []
    for exponent, coefficient in h_q.items():
        const, slope = line(names, exponent)
        if const + slope * lower == base_const + base_slope * lower:
            ties7.append((exponent, coefficient, const, slope))
    if len(ties7) != 2 or {item[0] for item in ties7} != {load_exp, intrinsic_exp}:
        fail(("q7 tie mismatch", [(monomial(names, e), c) for e, c, _, _ in ties7]))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    payload = {
        "variables": list(names),
        "terms": [
            {"exponents": list(exponent), "coefficient": str(coefficient)}
            for exponent, coefficient in sorted(h_q.items())
        ],
    }
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "hseries_affine_graph_support.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H17-UPPER-GRAPH-LOAD-UNIT-V10",
        "registered_aws_lane": tag,
        "support_count": len(h_q),
        "support_sha256": sha256(payload_bytes).hexdigest(),
        "leading_load": {"coefficient": "5/4", "monomial": monomial(names, load_exp), "line": "93-6q"},
        "unique_interval": "7<q<17/2",
        "q7_ties": [
            {"coefficient": str(coefficient), "monomial": monomial(names, exponent), "line": f"{const}+({slope})q"}
            for exponent, coefficient, const, slope in ties7
        ],
        "input_sha256": {str(path.relative_to(ROOT)): expected for path, expected in EXPECTED.items()},
        "scope": "INTERNAL_AFFINE_GRAPH_SPECIAL_FIBRE_H17_UPPER_CONE_ONLY_NO_POSITIVE_DEVIATION_COMPOSITION_BOUNDARY_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17_UPPER_GRAPH_SUPPORT=" + str(len(h_q)))
    print("A_H17_UPPER_GRAPH_LOAD=5/4*K10*a^3*E^7")
    print("A_H17_UPPER_GRAPH_UNIQUE=7<q<17/2")
    print("A_H17_UPPER_GRAPH_Q7_TIES=2")
    print("A_H17_UPPER_GRAPH_SUPPORT_SHA256=" + result["support_sha256"])
    print("A_H17_UPPER_GRAPH_ENDPOINT=PASS_EXACT_GRAPH_LOAD_UNIT")
    print("A_H17_UPPER_GRAPH_DONE=1")
    print("A_H17_UPPER_GRAPH_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
