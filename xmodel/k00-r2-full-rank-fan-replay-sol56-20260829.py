#!/usr/bin/env python3
"""Exact stdlib replay for the provisional V20R2 valuation-two rank fan.

This program reconstructs the seven affine K00 rows directly from the frozen
569-tail JSON, using the V20R2 coordinate map pinned by the frozen compiler.
It then checks the leading-rank and old-plane next-coefficient rank fans over
Q and Q(i).  It uses no CAS and writes no files.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[1]
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
COMPILER = (
    ROOT
    / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827"
    / "compile_contracted_source_v20r2.py"
)
TAILS_SHA256 = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
COMPILER_SHA256 = "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b"
TAIL_WEIGHTS = (8, 7, 6, 5, 4, 3, 2, 2, 6, 10)
LOAD_INDEX = {"K10": 7, "K6": 8, "K2": 9}
N_D = 6
D_ZERO = (0,) * N_D


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


# Sparse Q[d0,...,d5].
DPoly = dict[tuple[int, ...], F]


def dclean(poly: DPoly) -> DPoly:
    return {key: value for key, value in poly.items() if value}


def dadd(left: DPoly, right: DPoly, scale: F = F(1)) -> DPoly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, F(0)) + scale * value
    return dclean(out)


def dscale(poly: DPoly, value: F | int) -> DPoly:
    value = F(value)
    return dclean({key: value * coefficient for key, coefficient in poly.items()})


def dmul(left: DPoly, right: DPoly) -> DPoly:
    out: DPoly = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            out[key] = out.get(key, F(0)) + avalue * bvalue
    return dclean(out)


def dpow(poly: DPoly, exponent: int) -> DPoly:
    out: DPoly = {D_ZERO: F(1)}
    base = poly
    while exponent:
        if exponent & 1:
            out = dmul(out, base)
        exponent >>= 1
        if exponent:
            base = dmul(base, base)
    return out


def dvar(index: int) -> DPoly:
    key = [0] * N_D
    key[index] = 1
    return {tuple(key): F(1)}


def dhom(poly: DPoly, degree: int) -> DPoly:
    return {key: value for key, value in poly.items() if sum(key) == degree}


def dderivative(poly: DPoly, index: int) -> DPoly:
    out: DPoly = {}
    for key, value in poly.items():
        if key[index]:
            new = list(key)
            value *= new[index]
            new[index] -= 1
            tnew = tuple(new)
            out[tnew] = out.get(tnew, F(0)) + value
    return dclean(out)


def coordinate_images() -> list[DPoly]:
    one = {D_ZERO: F(1)}
    three = {D_ZERO: F(3)}
    return [
        dscale(dadd(one, dvar(0)), F(1, 256)),
        dvar(1),
        dscale(dadd(one, dvar(2)), F(1, 16)),
        dvar(3),
        dscale(dadd(three, dvar(4)), F(1, 8)),
        dvar(5),
        one,
    ]


def reconstruct_rows() -> tuple[list[DPoly], dict[str, list[DPoly]], int]:
    raw = json.loads(TAILS.read_text())
    if set(raw) != {str(i) for i in range(1, 8)}:
        fail("row labels")
    images = coordinate_images()
    rows: list[DPoly] = [{} for _ in range(7)]
    loads = {label: [{} for _ in range(7)] for label in LOAD_INDEX}
    terms = 0
    for ell in range(1, 8):
        for raw_monomial, raw_coefficient in raw[str(ell)]:
            terms += 1
            monomial = tuple(int(value) for value in raw_monomial)
            if len(monomial) != 10 or any(value < 0 for value in monomial):
                fail(("malformed monomial", ell, monomial))
            if sum(a * b for a, b in zip(monomial, TAIL_WEIGHTS)) != 12 + ell:
                fail(("weight", ell, monomial))
            if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
                fail(("load nonlinearity", ell, monomial))
            poly: DPoly = {D_ZERO: F(str(raw_coefficient))}
            for index, exponent in enumerate(monomial[:7]):
                if exponent:
                    poly = dmul(poly, dpow(images[index], exponent))
            active = [label for label, index in LOAD_INDEX.items() if monomial[index]]
            if not active:
                rows[ell - 1] = dadd(rows[ell - 1], poly)
            elif len(active) == 1:
                label = active[0]
                loads[label][ell - 1] = dadd(loads[label][ell - 1], poly)
            else:
                fail(("multiple loads", ell, active))
    if terms != 569:
        fail(("tail census", terms))
    return rows, loads, terms


# Gaussian rational coefficients, represented by (real, imaginary).
G = tuple[F, F]


def g(value: F | int = 0, imag: F | int = 0) -> G:
    return F(value), F(imag)


def gadd(left: G, right: G) -> G:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: G, right: G) -> G:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gpow(value: G, exponent: int) -> G:
    out = g(1)
    base = value
    while exponent:
        if exponent & 1:
            out = gmul(out, base)
        exponent >>= 1
        if exponent:
            base = gmul(base, base)
    return out


def giszero(value: G) -> bool:
    return value == g()


GPoly = dict[tuple[int, ...], G]


class Ring:
    def __init__(self, names: tuple[str, ...]):
        self.names = names
        self.n = len(names)
        self.zero_key = (0,) * self.n
        self.index = {name: index for index, name in enumerate(names)}

    def coerce(self, value: G | F | int) -> G:
        if isinstance(value, tuple):
            return value
        return g(value)

    def const(self, value: G | F | int = 0) -> GPoly:
        coefficient = self.coerce(value)
        return {} if giszero(coefficient) else {self.zero_key: coefficient}

    def var(self, name: str) -> GPoly:
        key = [0] * self.n
        key[self.index[name]] = 1
        return {tuple(key): g(1)}

    def clean(self, poly: GPoly) -> GPoly:
        return {key: value for key, value in poly.items() if not giszero(value)}

    def add(self, left: GPoly, right: GPoly, scale: G | F | int = 1) -> GPoly:
        factor = self.coerce(scale)
        out = dict(left)
        for key, value in right.items():
            out[key] = gadd(out.get(key, g()), gmul(factor, value))
        return self.clean(out)

    def sub(self, left: GPoly, right: GPoly) -> GPoly:
        return self.add(left, right, -1)

    def scale(self, poly: GPoly, value: G | F | int) -> GPoly:
        factor = self.coerce(value)
        return self.clean({key: gmul(factor, coefficient) for key, coefficient in poly.items()})

    def mul(self, left: GPoly, right: GPoly) -> GPoly:
        out: GPoly = {}
        for akey, avalue in left.items():
            for bkey, bvalue in right.items():
                key = tuple(a + b for a, b in zip(akey, bkey))
                out[key] = gadd(out.get(key, g()), gmul(avalue, bvalue))
        return self.clean(out)

    def power(self, poly: GPoly, exponent: int) -> GPoly:
        out = self.const(1)
        base = poly
        while exponent:
            if exponent & 1:
                out = self.mul(out, base)
            exponent >>= 1
            if exponent:
                base = self.mul(base, base)
        return out

    def linear(self, *terms: tuple[G | F | int, GPoly]) -> GPoly:
        out: GPoly = {}
        for coefficient, poly in terms:
            out = self.add(out, poly, coefficient)
        return out

    def monomial(self, powers: dict[str, int], coefficient: G | F | int = 1) -> GPoly:
        key = [0] * self.n
        for name, exponent in powers.items():
            key[self.index[name]] = exponent
        value = self.coerce(coefficient)
        return {} if giszero(value) else {tuple(key): value}

    def zero_vars(self, poly: GPoly, names: tuple[str, ...]) -> GPoly:
        indices = tuple(self.index[name] for name in names)
        return {key: value for key, value in poly.items() if all(key[index] == 0 for index in indices)}

    def depends_on(self, poly: GPoly, name: str) -> bool:
        index = self.index[name]
        return any(key[index] for key in poly)

    def replace_by_scaled_var(
        self,
        poly: GPoly,
        replacements: dict[str, tuple[G, str]],
        zeros: tuple[str, ...] = (),
    ) -> GPoly:
        zero_indices = {self.index[name] for name in zeros}
        replacement_indices = {
            self.index[name]: (coefficient, self.index[target])
            for name, (coefficient, target) in replacements.items()
        }
        out: GPoly = {}
        for key, coefficient in poly.items():
            if any(key[index] for index in zero_indices):
                continue
            new = list(key)
            for index, (factor, target) in replacement_indices.items():
                exponent = new[index]
                if exponent:
                    coefficient = gmul(coefficient, gpow(factor, exponent))
                    new[target] += exponent
                    new[index] = 0
            tnew = tuple(new)
            out[tnew] = gadd(out.get(tnew, g()), coefficient)
        return self.clean(out)


def eval_dpoly(poly: DPoly, values: list[GPoly], ring: Ring) -> GPoly:
    out: GPoly = {}
    powers: dict[tuple[int, int], GPoly] = {}
    for key, coefficient in poly.items():
        term = ring.const(coefficient)
        for index, exponent in enumerate(key):
            if exponent:
                cache_key = index, exponent
                if cache_key not in powers:
                    powers[cache_key] = ring.power(values[index], exponent)
                term = ring.mul(term, powers[cache_key])
        out = ring.add(out, term)
    return out


def series_zero(truncation: int) -> list[GPoly]:
    return [{} for _ in range(truncation)]


def series_add(left: list[GPoly], right: list[GPoly], ring: Ring) -> list[GPoly]:
    return [ring.add(a, b) for a, b in zip(left, right)]


def series_mul(left: list[GPoly], right: list[GPoly], ring: Ring) -> list[GPoly]:
    out = series_zero(len(left))
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: len(left) - i]):
            if b:
                out[i + j] = ring.add(out[i + j], ring.mul(a, b))
    return out


def series_power(series: list[GPoly], exponent: int, ring: Ring) -> list[GPoly]:
    out = series_zero(len(series))
    out[0] = ring.const(1)
    base = series
    while exponent:
        if exponent & 1:
            out = series_mul(out, base, ring)
        exponent >>= 1
        if exponent:
            base = series_mul(base, base, ring)
    return out


def eval_dpoly_series(poly: DPoly, values: list[list[GPoly]], ring: Ring) -> list[GPoly]:
    truncation = len(values[0])
    out = series_zero(truncation)
    powers: dict[tuple[int, int], list[GPoly]] = {}
    for key, coefficient in poly.items():
        term = series_zero(truncation)
        term[0] = ring.const(coefficient)
        for index, exponent in enumerate(key):
            if exponent:
                cache_key = index, exponent
                if cache_key not in powers:
                    powers[cache_key] = series_power(values[index], exponent, ring)
                term = series_mul(term, powers[cache_key], ring)
        out = series_add(out, term, ring)
    return out


def lambda_rows(
    rows: list[DPoly],
    k10_rows: list[DPoly],
    coefficients: list[dict[int, GPoly]],
    kappa: GPoly,
    ring: Ring,
    truncation: int = 9,
) -> list[list[GPoly]]:
    dseries: list[list[GPoly]] = []
    for entries in coefficients:
        series = series_zero(truncation)
        for grade, value in entries.items():
            series[grade] = value
        dseries.append(series)
    answer: list[list[GPoly]] = []
    for unloaded, load in zip(rows, k10_rows):
        total = eval_dpoly_series(unloaded, dseries, ring)
        load_series = eval_dpoly_series(load, dseries, ring)
        for grade in range(truncation - 2):
            total[grade + 2] = ring.add(
                total[grade + 2], ring.mul(kappa, load_series[grade])
            )
        answer.append(total)
    return answer


def cone_vector(ring: Ring, a: GPoly, b: GPoly, u: GPoly, v: GPoly) -> list[GPoly]:
    return [
        ring.linear((2, b), (2, u)),
        a,
        b,
        ring.linear((8, a), (1, v)),
        ring.sub(b, u),
        ring.linear((16, a), (4, v)),
    ]


def old_plane(ring: Ring, s: GPoly, t: GPoly) -> list[GPoly]:
    return [ring.scale(s, 2), ring.scale(t, F(1, 8)), s, t, s, ring.scale(t, 2)]


def vector_with_ab(
    ring: Ring,
    aval: GPoly,
    bval: GPoly,
    q1: GPoly,
    q2: GPoly,
    q3: GPoly,
    q4: GPoly,
) -> list[GPoly]:
    """Vector z with A(z)=aval and B(z)=bval."""
    return [
        ring.linear((1, bval), (4, q2), (-2, q4)),
        q1,
        q2,
        q3,
        q4,
        ring.linear((1, aval), (-16, q1), (4, q3)),
    ]


def assert_zero(poly: GPoly, label: str) -> None:
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(left: GPoly, right: GPoly, ring: Ring, label: str) -> None:
    assert_zero(ring.sub(left, right), label)


def qpair_branch_reduce(poly: GPoly, ring: Ring) -> dict[tuple[int, int], tuple[F, F]]:
    """Set v=1,u=r,a=A,b=-2r(1+4A),k=K in Q[r]/(r^2-192)."""

    # Polynomials in A,K with coefficients c0+c1*r.
    QP = dict[tuple[int, int], tuple[F, F]]

    def qadd(left: tuple[F, F], right: tuple[F, F]) -> tuple[F, F]:
        return left[0] + right[0], left[1] + right[1]

    def qmul(left: tuple[F, F], right: tuple[F, F]) -> tuple[F, F]:
        return (
            left[0] * right[0] + F(192) * left[1] * right[1],
            left[0] * right[1] + left[1] * right[0],
        )

    def padd(left: QP, right: QP) -> QP:
        out = dict(left)
        for key, value in right.items():
            out[key] = qadd(out.get(key, (F(0), F(0))), value)
        return {key: value for key, value in out.items() if value != (F(0), F(0))}

    def pmul(left: QP, right: QP) -> QP:
        out: QP = {}
        for akey, avalue in left.items():
            for bkey, bvalue in right.items():
                key = akey[0] + bkey[0], akey[1] + bkey[1]
                out[key] = qadd(out.get(key, (F(0), F(0))), qmul(avalue, bvalue))
        return {key: value for key, value in out.items() if value != (F(0), F(0))}

    def ppow(value: QP, exponent: int) -> QP:
        out: QP = {(0, 0): (F(1), F(0))}
        base = value
        while exponent:
            if exponent & 1:
                out = pmul(out, base)
            exponent >>= 1
            if exponent:
                base = pmul(base, base)
        return out

    one: QP = {(0, 0): (F(1), F(0))}
    aa: QP = {(1, 0): (F(1), F(0))}
    kk: QP = {(0, 1): (F(1), F(0))}
    rr: QP = {(0, 0): (F(0), F(1))}
    bb: QP = {
        (0, 0): (F(0), F(-2)),
        (1, 0): (F(0), F(-8)),
    }
    substitutions = {
        "a": aa,
        "b": bb,
        "u": rr,
        "v": one,
        "k": kk,
    }
    out: QP = {}
    for key, gaussian in poly.items():
        if gaussian[1]:
            fail("unexpected imaginary coefficient in rational branch")
        term: QP = {(0, 0): (gaussian[0], F(0))}
        for name, exponent in zip(ring.names, key):
            if exponent:
                term = pmul(term, ppow(substitutions[name], exponent))
        out = padd(out, term)
    return out


def leading_rank_fan(
    rows: list[DPoly], loads: dict[str, list[DPoly]]
) -> tuple[dict[str, object], tuple[int, ...]]:
    ring = Ring(("a", "b", "u", "v", "k"))
    a, b, u, v, k = (ring.var(name) for name in ring.names)
    x = cone_vector(ring, a, b, u, v)
    quadrics = [dhom(row, 2) for row in rows]
    cubics = [dhom(row, 3) for row in rows]
    m4 = [dhom(row, 2) for row in loads["K10"]]
    for index, quadric in enumerate(quadrics, 1):
        assert_zero(eval_dpoly(quadric, x, ring), f"Q{index}(cone)")

    alpha = [eval_dpoly(dderivative(quadric, 5), x, ring) for quadric in quadrics]
    beta = [eval_dpoly(dderivative(quadric, 0), x, ring) for quadric in quadrics]
    expected_alpha = [
        ring.scale(u, F(3, 1024)),
        ring.scale(v, F(3, 256)),
        ring.scale(u, F(-3, 8192)),
        {},
        ring.scale(u, F(-3, 131072)),
        {},
        ring.scale(u, F(-3, 1048576)),
    ]
    expected_beta = [
        ring.scale(v, F(-3, 1024)),
        ring.scale(u, F(3, 16384)),
        ring.scale(v, F(3, 8192)),
        {},
        ring.scale(v, F(3, 131072)),
        {},
        ring.scale(v, F(3, 1048576)),
    ]
    for index in range(7):
        assert_equal(alpha[index], expected_alpha[index], ring, f"alpha{index + 1}")
        assert_equal(beta[index], expected_beta[index], ring, f"beta{index + 1}")

    avec = (0, 16, 0, -4, 0, 1)
    bvec = (1, 0, -4, 0, 2, 0)
    basis = []
    for column in range(6):
        point = [ring.const(1 if index == column else 0) for index in range(6)]
        basis.append(point)
    for row_index, quadric in enumerate(quadrics):
        for column in range(6):
            actual = eval_dpoly(dderivative(quadric, column), x, ring)
            expected = ring.linear(
                (avec[column], alpha[row_index]),
                (bvec[column], beta[row_index]),
            )
            assert_equal(actual, expected, ring, f"DQ factor row{row_index + 1} col{column}")

    delta = ring.add(ring.mul(u, u), ring.scale(ring.mul(v, v), 64))
    nonzero_minors = 0
    for i in range(7):
        for j in range(i + 1, 7):
            minor = ring.sub(ring.mul(alpha[i], beta[j]), ring.mul(beta[i], alpha[j]))
            if minor:
                nonzero_minors += 1
                key_u2 = tuple(2 if n == "u" else 0 for n in ring.names)
                key_v2 = tuple(2 if n == "v" else 0 for n in ring.names)
                coefficient = minor.get(key_u2, g())
                if giszero(coefficient):
                    fail(("minor lacks u2", i, j))
                assert_equal(minor, ring.scale(delta, coefficient), ring, f"minor {i},{j}")
    if nonzero_minors == 0:
        fail("no rank-two minor")

    rhs = [
        ring.add(eval_dpoly(cubics[index], x, ring), ring.mul(k, eval_dpoly(m4[index], x, ring)))
        for index in range(7)
    ]
    h6 = ring.scale(
        ring.mul(u, ring.sub(ring.scale(ring.mul(v, v), 192), ring.mul(u, u))),
        F(1, 65536),
    )
    assert_equal(rhs[5], h6, ring, "leading rank-one row6")
    h4_core = ring.linear(
        (1, ring.power(u, 3)),
        (-448, ring.mul(u, ring.mul(v, v))),
        (64, ring.mul(b, ring.mul(v, v))),
        (-1, ring.mul(b, ring.mul(u, u))),
        (-1024, ring.mul(a, ring.mul(u, v))),
    )
    assert_equal(rhs[3], ring.scale(h4_core, F(3, 32768)), ring, "leading row4")

    # Delta=0, (u,v)!=0: u=+/-8iv and row 6 is +/- i*v^3/32.
    rank1_values = []
    for sign in (1, -1):
        specialized = ring.replace_by_scaled_var(rhs[5], {"u": (g(0, 8 * sign), "v")})
        expected = ring.monomial({"v": 3}, g(0, F(sign, 32)))
        assert_equal(specialized, expected, ring, f"leading rank1 sign {sign}")
        rank1_values.append(specialized)

    # Delta!=0 and u=0: row4 gives b=0, then two cokernel rows disagree.
    s3 = ring.add(rhs[2], rhs[0], F(1, 8))
    s5_u0 = ring.add(rhs[4], rhs[0], F(1, 128))
    s3_u0 = ring.zero_vars(s3, ("u", "b"))
    s5_u0 = ring.zero_vars(s5_u0, ("u", "b"))
    expected_s3 = ring.scale(ring.mul(ring.mul(v, v), ring.add(v, ring.scale(a, 3))), F(1, 4))
    expected_s5_u0 = ring.scale(
        ring.mul(ring.mul(v, v), ring.add(v, ring.scale(a, 2))), F(-3, 64)
    )
    assert_equal(s3_u0, expected_s3, ring, "rank2 u0 S3")
    assert_equal(s5_u0, expected_s5_u0, ring, "rank2 u0 S5")

    # Delta!=0 and u^2=192v^2: row4 fixes b, and global syzygies are constants.
    s5 = ring.add(ring.add(rhs[4], rhs[0], F(3, 128)), rhs[2], F(1, 8))
    s7 = ring.add(ring.add(rhs[6], rhs[0], F(1, 512)), rhs[2], F(1, 128))
    reduced_s5 = qpair_branch_reduce(s5, ring)
    reduced_s7 = qpair_branch_reduce(s7, ring)
    if reduced_s5 != {(0, 0): (F(1, 8), F(0))}:
        fail(("rank2 r^2=192 S5", reduced_s5))
    if reduced_s7 != {(0, 0): (F(-1, 64), F(0))}:
        fail(("rank2 r^2=192 S7", reduced_s7))

    # Meaningful in-memory mutation: perturb one row-6 cubic coefficient that
    # reaches the rank-one branch; the exact row-6 identity must fail.
    mutation_key: tuple[int, ...] | None = None
    for key in sorted(cubics[5]):
        mutated = dict(cubics[5])
        mutated[key] += 1
        bad_rhs = ring.add(
            eval_dpoly(mutated, x, ring), ring.mul(k, eval_dpoly(m4[5], x, ring))
        )
        bad_specialized = ring.replace_by_scaled_var(bad_rhs, {"u": (g(0, 8), "v")})
        if bad_specialized != rank1_values[0]:
            mutation_key = key
            break
    if mutation_key is None:
        fail("vacuous row6 mutation")

    return {
        "quadrics": quadrics,
        "cubics": cubics,
        "m4": m4,
        "nonzero_minors": nonzero_minors,
        "mutation_key": mutation_key,
    }, mutation_key


def old_plane_rank2(
    rows: list[DPoly], loads: dict[str, list[DPoly]]
) -> dict[str, object]:
    names = (
        "s", "t", "a", "b", "u", "v", "z1", "z2", "z3", "z4",
        "Ap", "Bp", "p1", "p2", "p3", "p4", "k",
    )
    ring = Ring(names)
    var = {name: ring.var(name) for name in names}
    s, t, a, b, u, v = (var[name] for name in ("s", "t", "a", "b", "u", "v"))
    leading = old_plane(ring, s, t)
    y = cone_vector(ring, a, b, u, v)
    az = ring.scale(ring.mul(s, t), 2)
    bz = ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 64))
    z = vector_with_ab(ring, az, bz, var["z1"], var["z2"], var["z3"], var["z4"])
    p = vector_with_ab(ring, var["Ap"], var["Bp"], var["p1"], var["p2"], var["p3"], var["p4"])
    coefficients = [{2: leading[index], 3: y[index], 4: z[index], 5: p[index]} for index in range(6)]
    equations = lambda_rows(rows, loads["K10"], coefficients, var["k"], ring)
    for row, equation in enumerate(equations, 1):
        for grade in range(4, 8):
            assert_zero(equation[grade], f"old-plane rank2 row{row} grade{grade}")
    grade8 = [equation[8] for equation in equations]
    dform = ring.linear(
        (1, ring.mul(t, ring.mul(u, u))),
        (-64, ring.mul(t, ring.mul(v, v))),
        (-2, ring.mul(s, ring.mul(u, v))),
    )
    fform = ring.linear(
        (1, ring.mul(s, ring.mul(u, u))),
        (-64, ring.mul(s, ring.mul(v, v))),
        (128, ring.mul(t, ring.mul(u, v))),
    )
    assert_equal(
        ring.add(grade8[0], grade8[2], 8),
        ring.scale(dform, F(-3, 256)),
        ring,
        "old-plane rank2 D",
    )
    assert_equal(grade8[3], ring.scale(fform, F(-3, 32768)), ring, "old-plane rank2 F")
    sigma = ring.add(ring.mul(s, s), ring.scale(ring.mul(t, t), 64))
    assert_equal(
        ring.sub(ring.mul(s, dform), ring.mul(t, fform)),
        ring.scale(ring.mul(ring.mul(u, v), sigma), -2),
        ring,
        "D/F identity one",
    )
    assert_equal(
        ring.add(ring.mul(s, fform), ring.scale(ring.mul(t, dform), 64)),
        ring.mul(ring.sub(ring.mul(u, u), ring.scale(ring.mul(v, v), 64)), sigma),
        ring,
        "D/F identity two",
    )
    for sign in (1, -1):
        branch = ring.replace_by_scaled_var(dform, {"s": (g(0, 8 * sign), "t")})
        square = ring.power(ring.add(u, ring.scale(v, g(0, -8 * sign))), 2)
        assert_equal(branch, ring.mul(t, square), ring, f"isotropic D sign {sign}")
    return {"ring": ring, "grade8": grade8, "D": dform, "F": fform}


def old_plane_rank0(
    rows: list[DPoly], loads: dict[str, list[DPoly]]
) -> dict[str, object]:
    names = (
        "s", "t", "a", "b", "WA", "WB", "w1", "w2", "w3", "w4", "k",
    )
    ring = Ring(names)
    var = {name: ring.var(name) for name in names}
    s, t, a, b = (var[name] for name in ("s", "t", "a", "b"))
    leading = old_plane(ring, s, t)
    y = old_plane(ring, a, b)
    shift = [
        ring.mul(s, s),
        ring.scale(ring.mul(s, t), F(1, 8)),
        ring.scale(ring.mul(t, t), 16),
        {}, {}, {},
    ]
    w = vector_with_ab(
        ring,
        var["WA"],
        var["WB"],
        var["w1"],
        var["w2"],
        var["w3"],
        var["w4"],
    )
    z = [ring.add(shift[index], w[index]) for index in range(6)]
    coefficients = [{2: leading[index], 3: y[index], 4: z[index]} for index in range(6)]
    equations = lambda_rows(rows, loads["K10"], coefficients, var["k"], ring)
    for row, equation in enumerate(equations, 1):
        for grade in range(4, 8):
            assert_zero(equation[grade], f"old-plane rank0 row{row} grade{grade}")
    grade8 = [equation[8] for equation in equations]
    for index, equation in enumerate(grade8, 1):
        if ring.depends_on(equation, "a") or ring.depends_on(equation, "b"):
            fail(("old-plane-y invariance", index))
    wa, wb, k = var["WA"], var["WB"], var["k"]
    assert_equal(
        ring.add(grade8[0], grade8[2], 8),
        ring.scale(ring.mul(wa, wb), F(3, 2048)),
        ring,
        "rank0 AB identity",
    )
    assert_equal(
        grade8[3],
        ring.scale(ring.sub(ring.mul(wb, wb), ring.scale(ring.mul(wa, wa), 64)), F(3, 524288)),
        ring,
        "rank0 square identity",
    )
    e1_restricted = ring.zero_vars(grade8[0], ("WA", "WB", "w1", "w2", "w3", "w4"))
    e2_restricted = ring.zero_vars(grade8[1], ("WA", "WB", "w1", "w2", "w3", "w4"))
    expected1 = ring.scale(
        ring.mul(ring.mul(k, t), ring.sub(ring.scale(ring.mul(s, s), 3), ring.scale(ring.mul(t, t), 64))),
        F(5, 4096),
    )
    expected2 = ring.scale(
        ring.mul(ring.mul(k, s), ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 192))),
        F(5, 65536),
    )
    assert_equal(e1_restricted, expected1, ring, "rank0 cubic E1")
    assert_equal(e2_restricted, expected2, ring, "rank0 cubic E2")
    return {"ring": ring, "grade8": grade8}


def old_plane_rank1(
    rows: list[DPoly], loads: dict[str, list[DPoly]], sign: int
) -> dict[str, object]:
    names = (
        "s", "t", "a", "b", "v", "lam", "z1", "z2", "z3", "z4",
        "Ap", "Bp", "p1", "p2", "p3", "p4", "k",
    )
    ring = Ring(names)
    var = {name: ring.var(name) for name in names}
    s, t, a, b, v, lam = (var[name] for name in ("s", "t", "a", "b", "v", "lam"))
    u = ring.scale(v, g(0, 8 * sign))
    leading = old_plane(ring, s, t)
    y = cone_vector(ring, a, b, u, v)
    az = ring.add(ring.scale(ring.mul(s, t), 2), ring.mul(lam, v))
    bz = ring.add(
        ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 64)),
        ring.scale(ring.mul(lam, v), g(0, 8 * sign)),
    )
    z = vector_with_ab(ring, az, bz, var["z1"], var["z2"], var["z3"], var["z4"])
    p = vector_with_ab(ring, var["Ap"], var["Bp"], var["p1"], var["p2"], var["p3"], var["p4"])
    coefficients = [{2: leading[index], 3: y[index], 4: z[index], 5: p[index]} for index in range(6)]
    equations = lambda_rows(rows, loads["K10"], coefficients, var["k"], ring)
    for row, equation in enumerate(equations, 1):
        for grade in range(4, 8):
            assert_zero(equation[grade], f"old-plane rank1 sign{sign} row{row} grade{grade}")
    grade8 = [equation[8] for equation in equations]
    first = ring.add(grade8[0], grade8[2], 8)
    expected_first = ring.scale(
        ring.mul(
            ring.mul(v, v),
            ring.linear(
                (128, t),
                (g(0, 16 * sign), s),
                (g(0, sign), ring.mul(lam, lam)),
            ),
        ),
        F(3, 256),
    )
    expected_fourth = ring.scale(
        ring.mul(
            ring.mul(v, v),
            ring.linear(
                (g(0, -128 * sign), t),
                (16, s),
                (-1, ring.mul(lam, lam)),
            ),
        ),
        F(3, 4096),
    )
    assert_equal(first, expected_first, ring, f"rank1 first sign {sign}")
    assert_equal(grade8[3], expected_fourth, ring, f"rank1 fourth sign {sign}")

    # The first two equations imply lam=0 and s=sign*8*i*t.  Under those
    # substitutions the remaining compatibility is a nonzero kappa cubic.
    compatibility = ring.add(grade8[1], grade8[0], g(0, F(sign, 2)))
    compatibility = ring.replace_by_scaled_var(
        compatibility,
        {"s": (g(0, 8 * sign), "t")},
        zeros=("lam",),
    )
    expected = ring.monomial({"k": 1, "t": 3}, g(0, F(-5 * sign, 16)))
    assert_equal(compatibility, expected, ring, f"rank1 terminal sign {sign}")

    # Controls: kappa is load-bearing, and a wrong sign in B(z) must already
    # fail at grade seven.
    no_kappa = ring.zero_vars(compatibility, ("k",))
    assert_zero(no_kappa, f"kappa load-bearing sign {sign}")
    wrong_bz = ring.add(
        ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 64)),
        ring.scale(ring.mul(lam, v), g(0, -8 * sign)),
    )
    wrong_z = vector_with_ab(ring, az, wrong_bz, var["z1"], var["z2"], var["z3"], var["z4"])
    wrong_coefficients = [
        {2: leading[index], 3: y[index], 4: wrong_z[index], 5: p[index]}
        for index in range(6)
    ]
    wrong_equations = lambda_rows(rows, loads["K10"], wrong_coefficients, var["k"], ring)
    if all(not equation[7] for equation in wrong_equations):
        fail(("wrong B(z) sign undetected", sign))
    return {"ring": ring, "grade8": grade8, "terminal": compatibility}


def omitted_coefficient_checks(rows: list[DPoly], loads: dict[str, list[DPoly]]) -> None:
    ring = Ring(("s", "t", "a", "b", "u", "v"))
    var = {name: ring.var(name) for name in ring.names}
    leading = old_plane(ring, var["s"], var["t"])
    cone = cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    quadrics = [dhom(row, 2) for row in rows]
    cubics = [dhom(row, 3) for row in rows]
    m4 = [dhom(row, 2) for row in loads["K10"]]
    for index in range(7):
        assert_zero(eval_dpoly(cubics[index], leading, ring), f"C3 old plane {index + 1}")
        assert_zero(eval_dpoly(m4[index], leading, ring), f"M4 old plane {index + 1}")
        for column in range(6):
            assert_zero(
                eval_dpoly(dderivative(quadrics[index], column), leading, ring),
                f"DQ old plane {index + 1},{column}",
            )
        # k10[1] at grade eight is proportional to the M4 polarization of
        # leading with the next cone coefficient; it must vanish.
        polar = eval_dpoly(m4[index], [ring.add(x, y) for x, y in zip(leading, cone)], ring)
        polar = ring.sub(ring.sub(polar, eval_dpoly(m4[index], leading, ring)), eval_dpoly(m4[index], cone, ring))
        assert_zero(polar, f"M4 polar oldplane/cone {index + 1}")


def main() -> None:
    start = time.perf_counter()
    if digest(TAILS) != TAILS_SHA256:
        fail("tails custody")
    if digest(COMPILER) != COMPILER_SHA256:
        fail("compiler custody")
    # A one-byte in-memory change must be detected by the custody gate.
    if sha256(TAILS.read_bytes() + b"\n").hexdigest() == TAILS_SHA256:
        fail("vacuous custody mutation")

    rows, loads, term_count = reconstruct_rows()
    if dhom(rows[5], 2):
        fail("Q6 is not zero")
    omitted_coefficient_checks(rows, loads)
    leading, mutation_key = leading_rank_fan(rows, loads)
    old_plane_rank2(rows, loads)
    old_plane_rank0(rows, loads)
    old_plane_rank1(rows, loads, 1)
    old_plane_rank1(rows, loads, -1)

    elapsed = time.perf_counter() - start
    print("K00_R2_FULL_RANK_FAN_REPLAY=PASS")
    print(f"TAILS_SHA256={TAILS_SHA256}")
    print(f"COMPILER_SHA256={COMPILER_SHA256}")
    print(f"TAIL_TERM_COUNT={term_count}")
    print(f"NONZERO_RANK2_MINORS={leading['nonzero_minors']}")
    print("LEADING_RANK1_G6=ROW6_UNIT_ON_BOTH_QI_BRANCHES")
    print("LEADING_RANK2_G6=EMPTY_BY_TWO_EXACT_BRANCHES")
    print("OLD_PLANE_NEXT_RANK2_G8=EMPTY_BY_D_F")
    print("OLD_PLANE_NEXT_RANK0_G8=EMPTY_BY_TWO_CUBICS")
    print("OLD_PLANE_NEXT_RANK1_G8=EMPTY_BY_KAPPA_CUBIC")
    print(f"ROW6_MUTATION_KEY={','.join(str(value) for value in mutation_key)}")
    print("MUTATION_CONTROLS=PASS")
    print(f"RUNTIME_SECONDS={elapsed:.6f}")


if __name__ == "__main__":
    main()
