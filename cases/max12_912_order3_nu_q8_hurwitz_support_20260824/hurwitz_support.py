#!/usr/bin/env python3
"""Unordered-Hurwitz invariant support on the corrected Q8 branch."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / "cases/max12_912_order3_nu_q8_invariant_support_20260824"
WORKER = ACTIVE / "modular_support.py"
PINS = {
    WORKER: "c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0",
    ACTIVE / "order48-p2003-v522.json":
        "e67c39e5394eb4ef285fcae722e318b75d5e2c02dd8638a7920d0dc4ce97841d",
    ROOT / "xmodel/max12-912-order3-critical-value-norm-20260824.md":
        "7339478798e00894c7b975c60aca821ec7ff2da383ffe5165a93cfa361bb6cb6",
    ROOT / "xmodel/max12-912-order3-critical-value-norm-review-grok-20260824.md":
        "b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e",
    ROOT / "cases/max12_912_order3_critical_value_norm_20260824/replay.py":
        "88f4e2145defe8b548cd5794d171ee7919da77257811a51271df7dbb68e7e4df",
    ROOT / "cases/max12_912_order3_critical_value_norm_20260824/replay.json":
        "98967e2ea85c47cdb96f7406edaf9a76c5eb8b932a65fa72c9460936f342a4d6",
}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


for path, expected in PINS.items():
    got = sha256(path.read_bytes()).hexdigest()
    if got != expected:
        raise RuntimeError((str(path), got, expected))
MS = load("q8_hurwitz_support_parent", WORKER)


def reconstruct(prime, root, order):
    data = MS.lift_branch(prime, root, order)
    t_order = 2 * order
    zero = [0] * t_order
    one = [1] + [0] * (t_order - 1)

    def add(left, right):
        return MS.series_add(left, right, prime)

    def mul(left, right):
        return MS.series_mul(left, right, prime)

    def power(value, exponent):
        return MS.series_pow(value, exponent, prime)

    def inverse(value):
        return MS.series_inv(value, prime)

    def scale(scalar, value):
        return [scalar * entry % prime for entry in value]

    def subtract(left, right):
        return [(a - b) % prime for a, b in zip(left, right)]

    def divide(left, right):
        return mul(left, inverse(right))

    def embed(value):
        out = [0] * t_order
        for index, coefficient in enumerate(value):
            out[2 * index] = coefficient
        return out

    t = [0] * t_order
    t[1] = 1
    coordinates = {
        name: embed(value) for name, value in data["coordinates"].items()
    }
    c, d2, d4, x1, x3, x5 = [
        coordinates[name] for name in ("c", "d2", "d4", "x1", "x3", "x5")
    ]
    qc = mul(t, c)
    qc2, qc3 = mul(qc, qc), power(qc, 3)
    raw = {
        0: add(t, qc3),
        1: add(x1, scale(3, qc2)),
        2: add(scale(3, qc), mul(t, d2)),
        3: add(add(one, x3), scale(3, qc2)),
        4: add(scale(6, qc), mul(t, d4)),
        5: add(scale(3, one), x5),
        6: scale(3, qc),
        7: scale(3, one),
    }
    f = {9: one, **raw}

    source = MS.M.Ring([f"a{i}" for i in range(8)] + ["k"])
    U = {index - 9: source.var(f"a{index}") for index in range(8)}
    g_source = MS.P.faber(source, 9, 12, U)
    raw_bases = [raw[index] for index in range(8)] + [zero]

    def evaluate_coefficient(poly):
        result = zero
        powers = []
        for index, base in enumerate(raw_bases):
            maximum = max((monomial[index] for monomial in poly), default=0)
            row = [one]
            for _ in range(maximum):
                row.append(mul(row[-1], base))
            powers.append(row)
        for monomial, scalar in poly.items():
            term = scale(MS.fraction_mod(scalar, prime), one)
            for index, exponent in enumerate(monomial):
                if exponent:
                    term = mul(term, powers[index][exponent])
            result = add(result, term)
        return result

    g = {
        exponent: evaluate_coefficient(poly)
        for exponent, poly in g_source.items()
    }
    n, q = embed(data["n"]), embed(data["q"])
    s = scale(-1, add(
        scale(pow(3, -1, prime), one),
        scale(10 * pow(9, -1, prime) % prime, divide(q, n)),
    ))

    def reduce_quadratic(poly):
        s_powers = [one]
        for _ in range(max(poly) // 2):
            s_powers.append(mul(s_powers[-1], s))
        even, odd = zero, zero
        for exponent, coefficient in poly.items():
            term = mul(coefficient, s_powers[exponent // 2])
            if exponent % 2:
                odd = add(odd, term)
            else:
                even = add(even, term)
        return even, odd

    def pair_multiply(left, right):
        a, b = left
        c0, d = right
        return (
            add(mul(a, c0), mul(s, mul(b, d))),
            add(mul(a, d), mul(b, c0)),
        )

    def pair_power(value, exponent):
        result = (one, zero)
        for _ in range(exponent):
            result = pair_multiply(result, value)
        return result

    def norm(value):
        return subtract(mul(value[0], value[0]), mul(s, mul(value[1], value[1])))

    F = pair_power(reduce_quadratic(f), 4)
    G = pair_power(reduce_quadratic(g), 3)
    normF = norm(F)
    E = subtract(mul(G[0], F[1]), mul(G[1], F[0]))
    W = (subtract(G[0], F[0]), subtract(G[1], F[1]))
    normW = norm(W)
    tau = scale(2, divide(
        subtract(mul(G[0], F[0]), mul(s, mul(G[1], F[1]))),
        normF,
    ))
    Delta = divide(
        scale(4, mul(s, mul(E, E))), mul(normF, normF)
    )
    for name, value in (("tau", tau), ("Delta", Delta)):
        odd_support = [index for index, coefficient in enumerate(value)
                       if index % 2 and coefficient]
        if odd_support:
            raise RuntimeError((name, "not parity-even", odd_support[:8]))

    def compress(value):
        return [value[2 * index] for index in range(order)]

    tau_w, Delta_w = compress(tau), compress(Delta)
    if not Delta_w[1] or not tau_w[1] or not E[1]:
        raise RuntimeError("non-etale Hurwitz reduction")
    if not s[0] or not normF[0] or not normW[0]:
        raise RuntimeError("left generic Hurwitz leaf")
    return {
        **data,
        "tau": tau_w,
        "Delta": Delta_w,
        "hurwitz_checks": {
            "all_tau_odd_t_coefficients_zero": True,
            "all_Delta_odd_t_coefficients_zero": True,
            "s_constant": s[0],
            "NormF_constant": normF[0],
            "NormW_constant": normW[0],
            "E_t_coefficient": E[1],
            "tau_w_coefficient": tau_w[1],
            "Delta_w_coefficient": Delta_w[1],
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=2003)
    parser.add_argument("--root", type=int, default=522)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--max-left", type=int, default=10)
    parser.add_argument("--max-right", type=int, default=10)
    parser.add_argument("--max-columns", type=int, default=36)
    parser.add_argument("--holdout", type=int, default=8)
    args = parser.parse_args()
    if not MS.is_prime(args.prime) or MS.q8_mod(args.root, args.prime):
        raise RuntimeError("not a prime Q8 specialization")
    data = reconstruct(args.prime, args.root, args.order)
    searches = {}
    for left_name, right_name in (
        ("theta", "Delta"), ("Delta", "Z"),
        ("tau", "Delta"), ("theta", "tau"),
    ):
        searches[f"{left_name},{right_name}"] = MS.relation_search(
            data[left_name], data[right_name], args.prime,
            args.max_left, args.max_right, args.max_columns, args.holdout,
        )
    payload = {
        "case": "max12_912_order3_nu_q8_hurwitz_support_20260824",
        "input_sha256": {str(path.relative_to(ROOT)): digest
                         for path, digest in PINS.items()},
        "prime": args.prime,
        "q8_root": args.root,
        "order": args.order,
        "holdout": args.holdout,
        "max_degrees": [args.max_left, args.max_right],
        "max_columns": args.max_columns,
        "good_reduction": {
            "prime_by_trial_division": True,
            "Q8_at_root": MS.q8_mod(args.root, args.prime),
            "six_by_six_jacobian_determinant": data["jacobian_determinant"],
            "all_fraction_denominators_inverted": True,
        },
        "hurwitz_checks": data["hurwitz_checks"],
        "series_prefix": {
            name: data[name][:8]
            for name in ("theta", "Z", "tau", "Delta")
        },
        "relation_searches": searches,
        "scope": (
            "bounded unordered-Hurwitz relation exclusion only; no global "
            "equation, normalization, projective boundary, genus, or trajectory"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
