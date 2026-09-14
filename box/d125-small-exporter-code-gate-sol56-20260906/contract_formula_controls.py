#!/usr/bin/env python3
"""Relocatable, bounded, tiny independent controls for the D125 exporter.

This checker constructs no degree-15/25 Jacobian or lift rows.  It checks the
six coefficient contracts as metadata and exercises row arithmetic only on
degree-at-most-seven fixtures.
"""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import resource
import signal
import sys
import time


LIMITS = {
    "wall_seconds": 30,
    "cpu_seconds": 25,
    "as_bytes": 512 * 1024**2,
}
PINS = {
    "FALLACY-v2.md": "e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5",
    "baseline.py": "ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53",
    "d125-minimal-preflight-gate-sol56-20260906.md": "f1fdd20da922454b6a2fa64dc0dea2fd973c488e5652462c6d131edffd1b9d36",
    "d125-minimal-receiver-gate-fable5-20260906.md": "cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d",
    "d125-small-polynomial-lift-gate-fable5-20260906.md": "4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122",
    "d125-small-source-exporter-prep-astra-20260906.md": "eddaf82a9c793de1b4e5a223fef5d93ba3e214a0c61cf3775f95d023b99fb085",
    "exporter.py": "9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703",
    "test_exporter.py": "331e97c84f22592a1a28842df7c11e84e4f72355a906c156403eb5eaca490b2b",
}


class CheckFailure(Exception):
    pass


def require(condition, label):
    if not condition:
        raise CheckFailure(label)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class K:
    """Independent Q[rho]/(rho^2-3rho+1) pair implementation."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Q(a)
        self.b = Q(b)

    def __add__(self, other):
        other = other if isinstance(other, K) else K(other)
        return K(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self + -(other if isinstance(other, K) else K(other))

    def __rsub__(self, other):
        return (other if isinstance(other, K) else K(other)) - self

    def __mul__(self, other):
        other = other if isinstance(other, K) else K(other)
        return K(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + 3 * self.b * other.b,
        )

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a * self.a + 3 * self.a * self.b + self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("zero in independent field")
        return K((self.a + 3 * self.b) / norm, -self.b / norm)

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** -exponent
        out, base = K(1), self
        while exponent:
            if exponent & 1:
                out = out * base
            base = base * base
            exponent //= 2
        return out

    def __eq__(self, other):
        other = other if isinstance(other, K) else K(other)
        return self.a == other.a and self.b == other.b

    def wire(self):
        return [
            [str(self.a.numerator), str(self.a.denominator)],
            [str(self.b.numerator), str(self.b.denominator)],
        ]

    def pair(self):
        return self.a, self.b


ZERO, ONE, RHO = K(), K(1), K(0, 1)


def univariate_mul(left, right):
    out = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, ZERO) + a * b
    return {i: a for i, a in out.items() if a != ZERO}


def univariate_power(poly, exponent):
    out = {0: ONE}
    for _ in range(exponent):
        out = univariate_mul(out, poly)
    return out


def doubled_area(vertices):
    return abs(
        sum(
            x * next_y - y * next_x
            for (x, y), (next_x, next_y) in zip(
                vertices, vertices[1:] + vertices[:1]
            )
        )
    )


def triangle_doubled_area(left, right, point):
    return abs(
        (right[0] - left[0]) * (point[1] - left[1])
        - (right[1] - left[1]) * (point[0] - left[0])
    )


def independent_lattice(vertices):
    """Area decomposition, independent of baseline's half-plane predicate."""
    area = doubled_area(vertices)
    edges = list(zip(vertices, vertices[1:] + vertices[:1]))
    return [
        (i, j)
        for i in range(max(x for x, _ in vertices) + 1)
        for j in range(max(y for _, y in vertices) + 1)
        if sum(triangle_doubled_area(a, b, (i, j)) for a, b in edges) == area
    ]


VERTICES = {
    "unequal": (
        [(0, 0), (0, 15), (9, 6), (2, 1)],
        [(0, 0), (0, 25), (15, 10), (1, 0)],
    ),
    "common_3": (
        [(0, 0), (0, 15), (9, 6), (3, 0)],
        [(0, 0), (0, 25), (15, 10), (5, 0)],
    ),
    "common_4": (
        [(0, 0), (0, 15), (9, 6), (9, 0)],
        [(0, 0), (0, 25), (15, 10), (15, 0)],
    ),
}
INNER_NORMAL = {"unequal": (5, -7), "common_3": (1, -1), "common_4": (1, 0)}


def inner_face(case, member, exponent, kappa):
    if case == "unequal":
        if member == "A":
            return {(2, 1): ONE, (9, 6): kappa**3}
        return {
            (1, 0): K(Q(5, 9)) * kappa**-1,
            (8, 5): K(Q(5, 3)) * kappa**2,
            (15, 10): kappa**5,
        }
    if case == "common_3":
        return {
            (exponent + r, r): kappa**exponent
            * K(comb(2 * exponent, r) * (-1) ** (2 * exponent - r))
            for r in range(2 * exponent + 1)
        }
    return {
        (3 * exponent, r): kappa**exponent
        * K(comb(2 * exponent, r) * (-1) ** (2 * exponent - r))
        for r in range(2 * exponent + 1)
    }


def expected_contract(case, branch):
    kappa = ONE if branch == "rational" else RHO
    cubic = (
        {0: ONE, 3: ONE}
        if branch == "rational"
        else {0: ONE, 1: K(3) - 2 * RHO, 2: K(2) - RHO, 3: RHO}
    )
    outer_faces = (univariate_power(cubic, 3), univariate_power(cubic, 5))
    variables, maps, fixed_counts, guards = [], [], [], []
    for member, vertices, degree, exponent, outer in zip(
        ("A", "B"), VERTICES[case], (15, 25), (3, 5), outer_faces
    ):
        points = independent_lattice(vertices)
        nx, ny = INNER_NORMAL[case]
        top = max(nx * i + ny * j for i, j in vertices)
        inner = inner_face(case, member, exponent, kappa)
        entries = []
        for i, j in points:
            specifications = []
            if i + j == degree:
                specifications.append(("outer", outer.get(i, ZERO)))
            if nx * i + ny * j == top:
                specifications.append(("inner", inner.get((i, j), ZERO)))
            if (i, j) == (0, 0):
                specifications.append(("target_constant", ZERO))
            name = f"{member}_g{i}_p{j}"
            if specifications:
                value = specifications[0][1]
                require(
                    all(candidate == value for _, candidate in specifications),
                    "independent face intersection conflict",
                )
                entries.append(
                    {
                        "point": [i, j],
                        "name": name,
                        "fixed": value.wire(),
                        "reasons": [reason for reason, _ in specifications],
                    }
                )
            else:
                entries.append(
                    {"point": [i, j], "name": name, "variable": len(variables)}
                )
                variables.append(name)
        by_point = {tuple(entry["point"]): entry for entry in entries}
        for point in vertices[1:]:
            value_wire = by_point[point]["fixed"]
            value = K(Q(value_wire[0][0]) / Q(value_wire[0][1]),
                      Q(value_wire[1][0]) / Q(value_wire[1][1]))
            require(value != ZERO, "independent zero vertex")
            guards.append(
                {
                    "label": f"GUARD/{member}/{point[0]}/{point[1]}",
                    "value": value.wire(),
                    "inverse": value.inverse().wire(),
                }
            )
        maps.append(entries)
        fixed_counts.append(sum("fixed" in entry for entry in entries))
    free = len(variables)
    if case == "unequal":
        scalar = -K(Q(5, 9)) * kappa**-1
        scalar_data = {"fixed": scalar.wire(), "inverse": scalar.inverse().wire()}
    else:
        variables += ["c", "z"]
        scalar_data = {"variable": free, "inverse_variable": free + 1, "row": "z*c-1"}
    return {
        "schema": "jc2.minimal-receiver-preflight/v1",
        "status": "PROVISIONAL_PREP_ONLY_NO_PRODUCTION_AUTHORITY",
        "case": case,
        "branch": branch,
        "field": "Q" if branch == "rational" else "Q[rho]/(rho^2-3*rho+1)",
        "geometric_scope": "algebraically closed characteristic zero",
        "order": "global degree reverse lexicographic, displayed variable order",
        "variables": variables,
        "coefficient_maps": maps,
        "vertex_guards": guards,
        "scalar": scalar_data,
        "counts": {
            "raw": [len(entries) for entries in maps],
            "fixed": fixed_counts,
            "free": free,
            "variables": len(variables),
            "raw_pair_upper_bound": len(maps[0]) * len(maps[1]),
            "jacobian_envelope_rows": 660,
            "planned_all_rows": 660 + sum(fixed_counts) + 7,
        },
        "target": "J(A,B)-c*gamma^2; J=A_gamma*B_pi-A_pi*B_gamma",
        "row_envelope": "0<=I<=23, 0<=J, I+J<=38; all 660 rows including zero",
        "degree_guards": "A_(0,15)=B_(0,25)=1; six nonorigin vertices guarded",
        "production_export_implemented": False,
    }


def laurent_mul(left, right):
    out = {}
    for (u, v, b, d), coefficient in left.items():
        for (other_u, other_v, other_b, other_d), other_coefficient in right.items():
            key = (u + other_u, v + other_v, b + other_b, d + other_d)
            out[key] = out.get(key, 0) + coefficient * other_coefficient
            if out[key] == 0:
                del out[key]
    return out


def repeated_inverse_power(i, j):
    pi = {
        (1, 4, 0, 0): 1,
        (0, 2, 1, 0): -1,
        (0, 1, 0, 1): -1,
        (0, -1, 0, 0): -1,
    }
    out = {(0, -i, 0, 0): 1}
    for _ in range(j):
        out = laurent_mul(out, pi)
    return out


def actual_field_pair(value):
    return Q(value.a), Q(value.b)


def actual_polynomial_pairs(polynomial):
    return {monomial: actual_field_pair(value) for monomial, value in polynomial.items()}


def independent_coefficient_product(left, right):
    out = {}
    for left_monomial, left_value in left.items():
        for right_monomial, right_value in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            out[monomial] = out.get(monomial, ZERO) + left_value * right_value
            if out[monomial] == ZERO:
                del out[monomial]
    return out


def independent_pair_jacobian(left, right):
    out = {}
    for (i, j), left_coefficient in left.items():
        for (k, ell), right_coefficient in right.items():
            determinant = i * ell - j * k
            if determinant == 0:
                continue
            row = out.setdefault((i + k - 1, j + ell - 1), {})
            for monomial, value in independent_coefficient_product(
                left_coefficient, right_coefficient
            ).items():
                row[monomial] = row.get(monomial, ZERO) + determinant * value
                if row[monomial] == ZERO:
                    del row[monomial]
    return {point: row for point, row in out.items() if row}


def to_producer_polynomial(polynomial, baseline):
    return {
        monomial: baseline.F(value.a, value.b)
        for monomial, value in polynomial.items()
    }


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, "module load specification")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def toy_target_spec(exporter, fixed_scalar):
    baseline = exporter.B
    variables = ["a", "b", "lambda2", "lambda3"] if fixed_scalar else [
        "a", "b", "c", "z", "lambda2", "lambda3"
    ]
    lambda_ids = (2, 3) if fixed_scalar else (4, 5)
    scalar = {(): -baseline.F(Q(5, 9)) * baseline.RHO**-1} if fixed_scalar else {
        (2,): baseline.ONE
    }
    scalar_guard = {} if fixed_scalar else {(2, 3): baseline.ONE, (): -baseline.ONE}
    sources = [
        {(1, 0): {(0,): baseline.ONE}},
        {(2, 1): {(1,): baseline.ONE}},
    ]
    return {
        "header": {
            "schema": exporter.SCHEMA,
            "mode": "toy",
            "case": "DECLARED_TINY_TARGET",
            "branch": "golden",
            "field": "Q[rho]/(rho^2-3*rho+1)",
            "expected_rows": 8,
            "expected_jacobian_rows": 1,
            "expected_lift_rows": 6,
            "expected_variables": len(variables),
            "target": "J-c*gamma^2",
            "status": "TOY_ONLY",
        },
        "variables": variables,
        "maps": [[], []],
        "sources": sources,
        "degrees": (3, 3),
        "jac_indices": [(2, 0)],
        "lambda_ids": lambda_ids,
        "scalar": scalar,
        "scalar_guard": scalar_guard,
        "guards": [],
    }


def run(inputs):
    input_hashes = {}
    for name, expected_hash in PINS.items():
        path = inputs / name
        require(path.is_file(), "missing pinned input " + name)
        actual_hash = sha256(path)
        require(actual_hash == expected_hash, "pin mismatch " + name)
        input_hashes[name] = actual_hash

    sys.dont_write_bytecode = True
    baseline = load_module("baseline", inputs / "baseline.py")
    exporter = load_module("exporter", inputs / "exporter.py")

    require(
        baseline.VERTICES
        == {case: tuple(tuple(vertex) for vertex in members) for case, members in VERTICES.items()},
        "literal polygon roster",
    )
    require(baseline.INNER == INNER_NORMAL, "literal inner normals")

    clients = {}
    total_map_records = 0
    total_fixed_records = 0
    for case in VERTICES:
        for branch in ("rational", "golden"):
            expected = expected_contract(case, branch)
            actual = baseline.make_contract(case, branch)
            require(actual == expected, "independent complete contract " + case + "/" + branch)
            key = case + "/" + branch
            clients[key] = {
                "raw": actual["counts"]["raw"],
                "fixed": actual["counts"]["fixed"],
                "free": actual["counts"]["free"],
                "variables_after_lambdas": actual["counts"]["variables"] + 2,
                "rows_after_lifts": actual["counts"]["planned_all_rows"] + 105,
            }
            total_map_records += sum(actual["counts"]["raw"])
            total_fixed_records += sum(actual["counts"]["fixed"])

    require(RHO * (K(3) - RHO) == ONE, "independent rho inverse")
    require((RHO * RHO - 3 * RHO + ONE) == ZERO, "independent rho minpoly")

    independent_15 = [(t, e) for t in range(3) for e in range(5 * t - 15, 0)]
    independent_25 = [(t, e) for t in range(5) for e in range(5 * t - 25, 0)]
    require(exporter.negative_indices(15) == independent_15, "all 30 A lift indices")
    require(exporter.negative_indices(25) == independent_25, "all 75 B lift indices")

    lift_comparisons = 0
    independent_coefficient = K(Q(2, 3), Q(-1, 2))
    producer_coefficient = baseline.F(independent_coefficient.a, independent_coefficient.b)
    degree_seven_indices = [(t, e) for t in range(2) for e in range(5 * t - 7, 0)]
    require(exporter.negative_indices(7) == degree_seven_indices, "tiny lift index envelope")
    for i in range(8):
        for j in range(8 - i):
            direct = repeated_inverse_power(i, j)
            source = {(i, j): {(): producer_coefficient}}
            for t, e in degree_seven_indices:
                expected = {}
                for (u, v, lambda2_power, lambda3_power), integer in direct.items():
                    if (u, v) == (t, e):
                        monomial = (0,) * lambda2_power + (1,) * lambda3_power
                        expected[monomial] = (integer * independent_coefficient).pair()
                actual = actual_polynomial_pairs(exporter.lift_row(source, t, e, 0, 1))
                require(actual == expected, f"tiny lift coefficient {i}/{j}/{t}/{e}")
                lift_comparisons += 1

    left_independent = {
        (0, 1): {(0,): ONE},
        (1, 0): {(): K(2)},
        (2, 1): {(1,): RHO},
        (3, 0): {(): K(-1)},
    }
    right_independent = {
        (0, 2): {(2,): ONE},
        (1, 1): {(): K(3)},
        (2, 0): {(3,): RHO},
        (3, 2): {(): ONE},
    }
    left = {point: to_producer_polynomial(poly, baseline)
            for point, poly in left_independent.items()}
    right = {point: to_producer_polynomial(poly, baseline)
             for point, poly in right_independent.items()}
    direct_jacobian = independent_pair_jacobian(left_independent, right_independent)
    jacobian_comparisons = 0
    for i in range(6):
        for j in range(4):
            expected = {
                monomial: value.pair()
                for monomial, value in direct_jacobian.get((i, j), {}).items()
            }
            actual = actual_polynomial_pairs(exporter.jac_row(left, right, i, j))
            require(actual == expected, f"tiny Jacobian coefficient {i}/{j}")
            jacobian_comparisons += 1

    common_records = list(exporter.records(toy_target_spec(exporter, False)))
    common_target = next(record for record in common_records if record.get("label") == "J/2/0")
    common_guard = next(record for record in common_records if record.get("label") == "GUARD/c")
    require(
        actual_polynomial_pairs({tuple(term[1]): baseline.decode(term[0])
                                 for term in common_target["terms"]})
        == {(0, 1): ONE.pair(), (2,): K(-1).pair()},
        "common target subtracts variable c",
    )
    require(
        actual_polynomial_pairs({tuple(term[1]): baseline.decode(term[0])
                                 for term in common_guard["terms"]})
        == {(2, 3): ONE.pair(), (): K(-1).pair()},
        "common z*c-1 guard",
    )

    fixed_records = list(exporter.records(toy_target_spec(exporter, True)))
    fixed_target = next(record for record in fixed_records if record.get("label") == "J/2/0")
    fixed_guard = next(record for record in fixed_records if record.get("label") == "GUARD/c")
    fixed_terms = {
        tuple(term[1]): baseline.decode(term[0]) for term in fixed_target["terms"]
    }
    expected_inverse_kappa = K(3) - RHO
    require(actual_field_pair(fixed_terms[()]) == (K(Q(5, 9)) * expected_inverse_kappa).pair(),
            "fixed negative c is subtracted with positive target constant")
    require(actual_field_pair(fixed_terms[(0, 1)]) == ONE.pair(), "fixed target Jacobian term")
    require(fixed_guard["terms"] == [], "fixed scalar guard is a zero identity")

    # Sensitivity checks use altered copies only; no stream is written.
    altered = copy.deepcopy(baseline.make_contract("unequal", "rational"))
    fixed_zero = next(
        entry
        for member in altered["coefficient_maps"]
        for entry in member
        if entry.get("fixed") == ZERO.wire() and "outer" in entry.get("reasons", [])
    )
    fixed_zero["fixed"] = ONE.wire()
    require(altered != expected_contract("unequal", "rational"), "fixed-zero face mutation distinguished")
    wrong_sign = copy.deepcopy(common_target)
    c_term = next(term for term in wrong_sign["terms"] if term[1] == [2])
    c_term[0] = baseline.ONE.wire()
    require(wrong_sign != common_target, "target-sign mutation distinguished")

    require(sum(39 - i for i in range(24)) == 660, "660 retained Jacobian indices")
    require(sum(39 - i for i in range(24, 39)) == 120, "120 omitted universal zeros")
    require(9 + 15 - 1 == 23 and 15 + 25 - 2 == 38,
            "Jacobian support bounds imply omitted zeros")

    return {
        "status": "PASS",
        "checks": [
            "all eight frozen input pins",
            "six independent area-lattice and closed-face contracts",
            "literal A/B then c,z ordering and lambda placement counts",
            "30 plus 75 complete lift indices",
            "independent repeated-power tiny lift coefficients",
            "independent pair-derivative tiny Jacobian coefficients",
            "common and fixed target/guard semantics",
            "field, fixed-zero-face, target-sign, and support-bound sensitivity",
        ],
        "input_hashes": input_hashes,
        "clients": clients,
        "metadata_records_checked": total_map_records,
        "fixed_records_checked": total_fixed_records,
        "tiny_lift_comparisons": lift_comparisons,
        "tiny_jacobian_comparisons": jacobian_comparisons,
        "tiny_records_generated": len(common_records) + len(fixed_records),
        "production_rows_generated": 0,
        "full_degree_lift_or_jacobian_generated": False,
        "cas_or_solver_or_aws": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    resource.setrlimit(resource.RLIMIT_AS, (LIMITS["as_bytes"], LIMITS["as_bytes"]))
    resource.setrlimit(resource.RLIMIT_CPU, (LIMITS["cpu_seconds"], LIMITS["cpu_seconds"]))
    signal.alarm(LIMITS["wall_seconds"])
    started = time.monotonic()
    result = run(args.inputs.resolve())
    result["elapsed_seconds"] = time.monotonic() - started
    result["maxrss_KiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result["limits"] = LIMITS
    result["inputs"] = str(args.inputs.resolve())
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({
        "status": result["status"],
        "elapsed_seconds": result["elapsed_seconds"],
        "maxrss_KiB": result["maxrss_KiB"],
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
