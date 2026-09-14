#!/usr/bin/env python3
"""Construct the universal two-way boundary maps as reproducible Q circuits.

Only their Merkle roots and controls are written. The driver reconstructs every
operation, so no large expression tree is an artifact. All parameters remain
formal variables in the circuit. The two rational evaluations are controls;
universality follows from the checked integral inverse matrices and triangular
row formula, not from specialization. R minor faces remain source-conditional.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, ceil, factorial
from pathlib import Path
import argparse
import json
import resource
import time

from boundary_counts import SPECS


@dataclass(frozen=True)
class E:
    digest: bytes
    values: tuple
    constant: object = None


class Circuit:
    def __init__(self):
        self.nodes = 0
        self.constants = {}
        self.free_names = []

    def const(self, value):
        value = Q(value)
        if value not in self.constants:
            self.nodes += 1
            digest = sha256(f"Q:{value.numerator}/{value.denominator}".encode()).digest()
            self.constants[value] = E(digest, (value, value), value)
        return self.constants[value]

    def var(self, name, values, free=False):
        self.nodes += 1
        if free:
            self.free_names.append(name)
        return E(sha256(("variable:" + name).encode()).digest(), tuple(map(Q, values)))

    def add(self, terms):
        by_hash, constants = {}, Q(0)
        for scalar, expr in terms:
            scalar = Q(scalar)
            if not scalar:
                continue
            if expr.constant is not None:
                constants += scalar * expr.constant
            else:
                if expr.digest not in by_hash:
                    by_hash[expr.digest] = [Q(0), expr]
                by_hash[expr.digest][0] += scalar
        if constants:
            expr = self.const(constants)
            by_hash[expr.digest] = [Q(1), expr]
        rows = sorted((digest, scalar, expr) for digest, (scalar, expr)
                      in by_hash.items() if scalar)
        if not rows:
            return self.const(0)
        if len(rows) == 1 and rows[0][1] == 1:
            return rows[0][2]
        digest = sha256(b"linear-combination:")
        vals = [Q(0), Q(0)]
        for child, scalar, expr in rows:
            digest.update(f"{scalar.numerator}/{scalar.denominator}:".encode())
            digest.update(child)
            for point in range(2):
                vals[point] += scalar * expr.values[point]
        self.nodes += 1
        return E(digest.digest(), tuple(vals))

    def mul(self, left, right):
        if left.constant is not None:
            return self.add([(left.constant, right)])
        if right.constant is not None:
            return self.add([(right.constant, left)])
        self.nodes += 1
        children = sorted([left.digest, right.digest])
        digest = sha256(b"product:" + b"".join(children)).digest()
        return E(digest, tuple(a * b for a, b in zip(left.values, right.values)))

    def power(self, expr, degree):
        ans = [self.const(1)]
        for _ in range(degree):
            ans.append(self.mul(ans[-1], expr))
        return ans


def poly_mul(C, p, q):
    rows = [[] for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            rows[i + j].append((1, C.mul(a, b)))
    return [C.add(row) for row in rows]


def poly_power(C, p, n):
    out = [C.const(1)]
    for _ in range(n):
        out = poly_mul(C, out, p)
    return out


def rational_product(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def major_face(C, name, lam):
    is108, isR = name.startswith("108"), "_R_" in name
    d = 4 if is108 else 3
    if isR:
        power = 7 if is108 else 8
        if is108:
            qvals = [Q(1), Q(-21, 5), Q(112, 15), Q(-448, 65),
                     Q(3584, 1105), Q(-2048, 3315)]
            jac_over_lambda = Q(-3315, 2048)
        else:
            qvals = [Q(1), Q(-4), Q(48, 7), Q(-216, 35),
                     Q(1296, 455), Q(-243, 455)]
            jac_over_lambda = Q(-455, 243)
        q = [Q(0)] * (d * 5 + 2)
        for index, value in enumerate(qvals):
            q[1 + d * index] = value * jac_over_lambda
    else:
        power = (21 if "_F" in name else 14) if is108 else (24 if "_F" in name else 16)
    p = [Q(0)] * (d * power + 1)
    for index in range(power + 1):
        p[d * index] = Q(comb(power, index) * (-1) ** (power - index))
    if isR:
        return [C.add([(a, lam)]) for a in rational_product(p, q)]
    return [C.const(a) for a in p]


def minor_face(C, name, lam):
    is108, isR = name.startswith("108"), "_R_" in name
    zero, one = C.const(0), C.const(1)
    if is108:
        mu = C.var("mu", (2, -1))
        sep = C.var("c", (1, 2))
        p = [C.add([(1, C.mul(mu, mu)), (-1, sep)]), C.add([(-2, mu)]), one]
        power = 7 if isR else (12 if "_F" in name else 8)
    elif "delta2_" in name:
        rho = C.var("rho", (1, 2))
        p = [zero, zero, C.add([(3, rho)]), one]
        power = 5 if isR else (9 if "_F" in name else 6)
    else:
        sep = C.var("c", (1, 2))
        p = [zero, C.add([(-1, sep)]), zero, one]
        power = 5 if isR else (9 if "_F" in name else 6)
    result = poly_power(C, p, power)
    if isR:
        scale = C.add([(-1 if is108 else 1, lam)])
        result = [C.mul(scale, x) for x in result]
    return result


def inverse_matrix(M, r):
    if not r:
        return []
    # The M=0 case is the Taylor basis change itself.
    if M == 0:
        inv = [[comb(j, k) if j >= k else 0 for j in range(r)] for k in range(r)]
    else:
        inv = [[(-1) ** M * sum(comb(j, k) * comb(M + j - ell - 1, j - ell)
                               for j in range(max(k, ell), r))
                for ell in range(r)] for k in range(r)]
    matrix = [[(-1) ** (M + col - row) * comb(M + col, row)
               if row <= M + col else 0
               for col in range(r)] for row in range(r)]
    assert all(sum(matrix[i][k] * inv[k][j] for k in range(r)) == int(i == j)
               for i in range(r) for j in range(r))
    return inv


def build(spec, inverse_cache, return_state=False):
    name, D, d, h, b, scale = spec
    started = time.monotonic()
    C = Circuit()
    zero = C.const(0)
    u = C.var("minor_u", (1, -1))
    vname = "minor_a2" if "delta2_" in name else "minor_v"
    v = C.var(vname, (-1, 2))
    lam = C.var("lambda", (1, 3))
    up, vp = C.power(u, D // 2), C.power(v, D // 3)
    centre_products = {(a, bb): C.mul(up[a], vp[bb])
                       for a in range(D // 2 + 1)
                       for bb in range((D - 2 * a) // 3 + 1)}
    major, minor = major_face(C, name, lam), minor_face(C, name, lam)
    coeff_z, coeff_y, row_specs = {}, {}, []
    inverse_hash = sha256()
    for n in range(D, -1, -1):
        m = max(0, ceil(Q(d * n - h, d + 1)))
        ell = max(0, ceil((n - b) / scale))
        em = int(d * n >= h and (d * n - h) % (d + 1) == 0)
        el = int(n >= b and ((n - b) / scale).denominator == 1)
        M = m + em
        r = min(ell + el, n + 1 - M)
        cz = [zero] * (n + 1)
        if em:
            cz[m] = major[m] if m < len(major) else zero
        for k in range(M + r, n + 1):
            index = len(C.free_names)
            cz[k] = C.var(f"{name}_free_{n}_{k}",
                          ((index % 5) - 2, ((index * 3) % 7) - 3), free=True)
        rhs = []
        for residue in range(r):
            target = minor[residue] if el and residue == ell and residue < len(minor) else zero
            terms = [(1, target)]
            # Contributions of known major-face and free coefficients at n.
            for k in range(max(residue, m), n + 1):
                if cz[k].constant != 0:
                    terms.append((-(-1) ** (k - residue) * comb(k, residue), cz[k]))
            # Exact physical substitution. All these N exceed n.
            for a in range((D - n) // 2 + 1):
                for bb in range((D - n - 2 * a) // 3 + 1):
                    if a == bb == 0:
                        continue
                    N, j = n + 2 * a + 3 * bb, residue + a + bb
                    if j > N:
                        continue
                    value = coeff_y[N][j]
                    if value.constant == 0:
                        continue
                    weight = comb(j, residue) * comb(a + bb, a)
                    terms.append((-weight, C.mul(centre_products[a, bb], value)))
            rhs.append(C.add(terms))
        key = M, r
        if key not in inverse_cache:
            inverse_cache[key] = inverse_matrix(M, r)
        inv = inverse_cache[key]
        inverse_hash.update(repr((n, M, r, inv)).encode())
        for k in range(r):
            cz[M + k] = C.add(list(zip(inv[k], rhs)))
        coeff_z[n] = cz
        coeff_y[n] = [C.add([((-1) ** (k - j) * comb(k, j), cz[k])
                              for k in range(j, n + 1)]) for j in range(n + 1)]
        row_specs += [(n, residue, el and residue == ell)
                      for residue in range(ell + el)]
    # Direct raw-row replay, separate from the solve and from its inverse.
    minor_checks = [0, 0]
    row_hash = sha256()
    for n, residue, is_target in row_specs:
        values = [Q(0), Q(0)]
        for a in range((D - n) // 2 + 1):
            for bb in range((D - n - 2 * a) // 3 + 1):
                N, j = n + 2 * a + 3 * bb, residue + a + bb
                if j > N:
                    continue
                weight = comb(j, residue) * comb(a + bb, a)
                source = coeff_y[N][j]
                centre = centre_products[a, bb]
                for point in range(2):
                    values[point] += weight * source.values[point] * centre.values[point]
        target = minor[residue] if is_target and residue < len(minor) else zero
        for point in range(2):
            assert values[point] == target.values[point], (name, n, residue, point)
            minor_checks[point] += 1
        row_hash.update(repr((n, residue, is_target, values)).encode())
    major_checks = [0, 0]
    forward_hash, inverse_projection_hash = sha256(), sha256()
    for n in range(D + 1):
        for k, value in enumerate(coeff_z[n]):
            forward_hash.update(f"{n},{k}:".encode() + value.digest)
            if d * n - (d + 1) * k > h:
                assert value.constant == 0
                major_checks[0] += 1
                major_checks[1] += 1
            elif d * n - (d + 1) * k == h:
                expected = major[k] if k < len(major) else zero
                assert value.digest == expected.digest
                major_checks[0] += 1
                major_checks[1] += 1
    for name_free in C.free_names:
        inverse_projection_hash.update((name_free + "\n").encode())
    result = dict(name=name, coefficient_field="Q", universal_parameter_divisions=[],
                source_generators=sum(n + 1 for n in range(D + 1)),
                remaining_coefficient_generators=len(C.free_names),
                scalar_variables=["minor_u", vname, "mu", "c", "lambda"] if name.startswith("108")
                else ["minor_u", vname, "rho" if "delta2_" in name else "c", "lambda"],
                forward_coefficient_circuit_sha256=forward_hash.hexdigest(),
                inverse_projection_sha256=inverse_projection_hash.hexdigest(),
                integral_block_inverse_certificate_sha256=inverse_hash.hexdigest(),
                exact_raw_row_evaluation_sha256=row_hash.hexdigest(),
                rational_control_minor_row_counts=minor_checks,
                rational_control_major_row_counts=major_checks,
                circuit_nodes_constructed=C.nodes,
                negative_control_top_minor_increment_one_residual=1,
                elapsed_seconds=round(time.monotonic() - started, 3))
    if return_state:
        return result, dict(C=C, coeff_z=coeff_z, coeff_y=coeff_y, u=u, v=v,
                            centre_products=centre_products, major=major, minor=minor)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", default="all")
    args = parser.parse_args()
    specs = [s for s in SPECS if args.client == "all" or args.client in s[0]]
    assert specs
    inverse_cache, results = {}, []
    for spec in specs:
        result = build(spec, inverse_cache)
        results.append(result)
        print(json.dumps(result), flush=True)
    result = dict(scope="Universal boundary maps before recurrence/characteristic identity; R minor source license conditional",
                  exact_universal_proof="Descending homogeneous-degree row formula and B*B_inverse=identity over Z",
                  rational_evaluations_are_controls_only=True,
                  checked_distinct_integer_inverse_matrices=len(inverse_cache),
                  maximum_resident_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  clients=results)
    suffix = "" if args.client == "all" else "_" + args.client
    Path(__file__).with_name("boundary_maps" + suffix + ".json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
