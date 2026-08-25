#!/usr/bin/env python3
"""Interpolate the 123 fixed-fibre coordinate tables and emit an exact graph test.

The degree-at-most-122 polynomial lift is deliberately only a candidate.  The
generated Singular input accepts it only if all six quotient rows, the
localizer, and the primitive-element relation reduce to zero modulo the graph
relations and the pinned candidate H(w,v).
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
SAMPLES = Path(__file__).resolve().parent / "aws_box02_shape_audit_v1/clean_samples.json"
SAMPLES_SHA256 = "27711e3e5ab0dd9927e1d8681189f31a35422e61261cf327cd91382a4d7760b6"
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
CANDIDATE = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/"
    "interpolation_candidate.json"
)
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
COORDINATES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
P = 127


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def trim(poly: list[int]) -> list[int]:
    while poly and poly[-1] % P == 0:
        poly.pop()
    return [coefficient % P for coefficient in poly]


def degree(poly: list[int]) -> int:
    return len(trim(poly[:])) - 1


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, coefficient in enumerate(left):
        out[index] = (out[index] + coefficient) % P
    for index, coefficient in enumerate(right):
        out[index] = (out[index] + coefficient) % P
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([(scalar * coefficient) % P for coefficient in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    if not left or not right:
        return []
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def divmod_poly(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    if not divisor:
        raise ZeroDivisionError
    if len(dividend) < len(divisor):
        return [], dividend
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], P - 2, P)
    while len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            dividend[shift + index] = (dividend[shift + index] - coefficient * value) % P
        trim(dividend)
    return trim(quotient), dividend


def derivative(poly: list[int]) -> list[int]:
    return trim([(index * poly[index]) % P for index in range(1, len(poly))])


def evaluate(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % P
    return result


def product_tree_linear(points: list[int]) -> list[int]:
    result = [1]
    for point in points:
        result = mul(result, [(-point) % P, 1])
    return result


def lagrange_basis(points: list[int], modulus: list[int]) -> list[list[int]]:
    derivative_modulus = derivative(modulus)
    result = []
    for point in points:
        quotient, remainder = divmod_poly(modulus, [(-point) % P, 1])
        if remainder:
            raise RuntimeError(("linear division", point, remainder))
        denominator = evaluate(derivative_modulus, point)
        if denominator == 0:
            raise RuntimeError(("repeated point", point))
        result.append(scale(quotient, pow(denominator, P - 2, P)))
    return result


def interpolate(values: list[int], basis: list[list[int]]) -> list[int]:
    result: list[int] = []
    for value, polynomial in zip(values, basis, strict=True):
        if value:
            result = add(result, scale(polynomial, value))
    return result


def monomial(coefficient: int, w_degree: int, v_degree: int) -> str:
    factors: list[str] = []
    coefficient %= P
    if coefficient != 1 or (w_degree == 0 and v_degree == 0):
        factors.append(str(coefficient))
    if w_degree:
        factors.append("w" if w_degree == 1 else f"w^{w_degree}")
    if v_degree:
        factors.append("v" if v_degree == 1 else f"v^{v_degree}")
    return "*".join(factors) if factors else "1"


def polynomial_string(support: list[tuple[int, int, int]]) -> str:
    return "+".join(monomial(c, wd, vd) for wd, vd, c in support) or "0"


def candidate_support(payload: dict) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    for raw_v_degree, entries in payload["nonzero_support"].items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            result.append((w_degree, v_degree, coefficient))
    result.sort(key=lambda term: (term[1], term[0]), reverse=True)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stats", type=Path, required=True)
    args = parser.parse_args()
    for path, expected in (
        (SAMPLES, SAMPLES_SHA256),
        (COMPILER, COMPILER_SHA256),
        (CANDIDATE, CANDIDATE_SHA256),
    ):
        got = digest(path)
        if got != expected:
            raise RuntimeError((str(path), got, expected))

    samples = json.loads(SAMPLES.read_text())
    if samples["status"] != "PASS" or samples["prime"] != P:
        raise RuntimeError("sample endpoint")
    points = samples["good_w_values"]
    if len(points) != 123 or len(set(points)) != 123:
        raise RuntimeError("sample abscissae")
    modulus = product_tree_linear(points)
    basis = lagrange_basis(points, modulus)
    if degree(modulus) != 123:
        raise RuntimeError("interpolation modulus")

    coordinate_support: dict[str, list[tuple[int, int, int]]] = {}
    coordinate_stats: dict[str, dict] = {}
    for name in COORDINATES:
        support: list[tuple[int, int, int]] = []
        maximum_w_degree = -1
        for v_degree, values in enumerate(samples["samples"][name]):
            interpolant = interpolate(values, basis)
            maximum_w_degree = max(maximum_w_degree, degree(interpolant))
            for w_degree, coefficient in enumerate(interpolant):
                if coefficient % P:
                    support.append((w_degree, v_degree, coefficient % P))
            for point, value in zip(points, values, strict=True):
                if evaluate(interpolant, point) != value:
                    raise RuntimeError(("interpolation replay", name, v_degree, point))
        coordinate_support[name] = support
        coordinate_stats[name] = {
            "support_size": len(support),
            "maximum_w_degree": maximum_w_degree,
            "maximum_v_degree": max((term[1] for term in support), default=-1),
        }

    candidate = json.loads(CANDIDATE.read_text())
    if candidate["status"] != "PASS" or candidate["degree_v"] != 190:
        raise RuntimeError("candidate endpoint")
    H_support = candidate_support(candidate)
    if (0, 190, 1) not in H_support:
        raise RuntimeError("candidate monicity")

    compiler = load(COMPILER, "q8_graph_quotient_compiler")
    _, rows, imposed, names = compiler.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)

    stats = {
        "status": "PASS",
        "scope": "degree-at-most-122 polynomial candidate; generic validity decided only by Singular remainder gate",
        "prime": P,
        "sample_sha256": SAMPLES_SHA256,
        "candidate_sha256": CANDIDATE_SHA256,
        "sample_count": len(points),
        "coordinate_stats": coordinate_stats,
        "H_support_size": len(H_support),
    }
    args.stats.write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n")

    print("ring R=127,(c,d2,d4,x1,x3,x5,inv,v,w),lp;")
    print("option(redSB);")
    print(f"poly H={polynomial_string(H_support)};")
    for name in COORDINATES:
        print(f"poly P{name}={polynomial_string(coordinate_support[name])};")
    graph_generators = [f"{name}-P{name}" for name in COORDINATES] + ["H"]
    print(f"ideal Graw={','.join(graph_generators)};")
    print("ideal G=std(Graw);")
    for ell in imposed:
        print(f"poly e{ell}={compiler.M.coeff_string(rows[ell], names)};")
    print("poly einv=inv*x5*(x3-2*x5)-1;")
    print("poly ev=v*x5-x3+2*x5;")
    print('print("Q8-P127-POLYNOMIAL-GRAPH-SUBSTITUTION");')
    print('print("graph_basis_size="+string(size(G)));')
    for label in ("e1", "e3", "e5", "e7", "e2", "e4", "einv", "ev"):
        print(f"poly rem_{label}=reduce({label},G);")
        print(f'if (rem_{label}==0) {{ print("{label}_zero=1"); }} else {{ print("{label}_zero=0"); }}')
    print('print("Q8-P127-POLYNOMIAL-GRAPH-SUBSTITUTION-END");')


if __name__ == "__main__":
    main()
