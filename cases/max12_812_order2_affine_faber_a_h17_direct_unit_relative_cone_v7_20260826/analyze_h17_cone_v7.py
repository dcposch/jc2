#!/usr/bin/env python3
"""AWS-only exact relative-cone analysis of the H17 direct-unit functional."""

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
BASELINE = 51


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only H17 cone analyzer refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H17 cone analyzer refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load(path: Path, prime: bool):
    data = json.loads(path.read_text())
    result = {}
    for record in data["terms"]:
        exponent = tuple(int(value) for value in record["exponents"])
        coefficient = int(record["coefficient"]) if prime else Fraction(record["coefficient"])
        result[exponent] = coefficient
    return tuple(data["variables"]), result


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


def mod_fraction(value: Fraction) -> int:
    return value.numerator % PRIME * pow(value.denominator % PRIME, -1, PRIME) % PRIME


def monomial_text(names, exponent):
    pieces = []
    for name, power in zip(names, exponent):
        if power:
            pieces.append(name if power == 1 else f"{name}^{power}")
    return "*".join(pieces) or "1"


def line(names, exponent):
    index = {name: offset for offset, name in enumerate(names)}
    const = Fraction(57 * exponent[index["J"]])
    const += Fraction(42 * sum(exponent[index[name]] for name in ("K2", "K6", "K10")))
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
    h_q = subtract(g_q, f_q, False)
    h_p = subtract(g_p, f_p, True)
    if set(h_q) != set(h_p):
        fail(("Q/prime support mismatch", len(h_q), len(h_p)))
    for exponent, coefficient in h_q.items():
        if mod_fraction(coefficient) != h_p[exponent]:
            fail(("coefficient reduction mismatch", exponent, coefficient, h_p[exponent]))
    if len(h_q) != 630:
        fail(("unexpected H support", len(h_q)))
    index = {name: offset for offset, name in enumerate(names)}
    intrinsic_exp = [0] * len(names)
    intrinsic_exp[index["lambda"]] = 3
    intrinsic_exp[index["M"]] = 3
    intrinsic_exp[index["E"]] = 2
    intrinsic_exp = tuple(intrinsic_exp)
    if h_q.get(intrinsic_exp) != Fraction(-2):
        fail(("intrinsic mismatch", h_q.get(intrinsic_exp)))

    lower = Fraction(4)  # mixed graph domain: q>21-H
    upper = Fraction(17, 2)  # a=17-2q>0
    active_lower = []
    active_upper = []
    equality_blocks = {}
    for exponent, coefficient in h_q.items():
        if exponent == intrinsic_exp:
            continue
        const, slope = line(names, exponent)
        if slope > 0:
            bound = Fraction(BASELINE - const, slope)
            if bound > lower:
                active_lower.append((bound, exponent, coefficient, const, slope))
        elif slope < 0:
            bound = Fraction(BASELINE - const, slope)
            if bound < upper:
                active_upper.append((bound, exponent, coefficient, const, slope))
        elif const <= BASELINE:
            fail(("q-independent competitor", exponent, coefficient, const))
    sharp_lower = max([lower] + [item[0] for item in active_lower])
    sharp_upper = min([upper] + [item[0] for item in active_upper])
    if (sharp_lower, sharp_upper) != (Fraction(17, 4), Fraction(7)):
        fail(("unexpected unique interval", sharp_lower, sharp_upper))
    for boundary in (sharp_lower, sharp_upper):
        equality_blocks[str(boundary)] = [
            {
                "coefficient": str(coefficient),
                "monomial": monomial_text(names, exponent),
                "line": f"{const}+({slope})q",
            }
            for exponent, coefficient in h_q.items()
            if exponent != intrinsic_exp and Fraction(line(names, exponent)[0] + line(names, exponent)[1] * boundary) == BASELINE
        ]
    if len(equality_blocks[str(sharp_lower)]) != 5 or len(equality_blocks[str(sharp_upper)]) != 3:
        fail(("boundary block size", equality_blocks))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    support = {
        "variables": list(names),
        "terms": [
            {"exponents": list(exponent), "coefficient": str(coefficient)}
            for exponent, coefficient in sorted(h_q.items())
        ],
    }
    support_bytes = (json.dumps(support, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "hseries_exact_support.json").write_bytes(support_bytes)
    result = {
        "status": "PASS-A-H17-DIRECT-UNIT-RELATIVE-CONE-V7",
        "registered_aws_lane": tag,
        "support_count": len(h_q),
        "support_sha256": sha256(support_bytes).hexdigest(),
        "intrinsic": {"coefficient": "-2", "monomial": "lambda^3*M^3*E^2", "grade": 51},
        "mixed_equality_domain": "4<q<17/2",
        "unique_intrinsic_interval": "17/4<q<7",
        "lower_boundary_block": equality_blocks[str(sharp_lower)],
        "upper_boundary_block": equality_blocks[str(sharp_upper)],
        "input_sha256": {str(path.relative_to(ROOT)): expected for path, expected in EXPECTED.items()},
        "scope": "INTERNAL_NORMALIZED_GRAPH_SUPPORT_H17_EQUALITY_VALUATION_ONLY_NO_RATIONAL_REGRADING_TOTAL_REES_SOURCE_COVER_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17_CONE_SUPPORT=630")
    print("A_H17_CONE_INTRINSIC=-2*lambda^3*M^3*E^2")
    print("A_H17_CONE_DOMAIN=4<q<17/2")
    print("A_H17_CONE_UNIQUE=17/4<q<7")
    print("A_H17_CONE_LOWER_BLOCK=5")
    print("A_H17_CONE_UPPER_BLOCK=3")
    print("A_H17_CONE_SUPPORT_SHA256=" + result["support_sha256"])
    print("A_H17_CONE_ENDPOINT=PASS_EXACT_RELATIVE_CONE")
    print("A_H17_CONE_DONE=1")
    print("A_H17_CONE_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()

