#!/usr/bin/env python3
"""Exact stdlib replay for the lowest Q8 non-parity normalization jet."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib.util
from math import comb
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"
GENUS_REPLAY = ROOT / "cases/max12_912_order3_nu_parity_genus5_20260824/replay.py"
GENUS_REPLAY_SHA256 = "c965bb660cf2f0f55c7ebbed3126b22bfb5d67e178565426aa94ce56f6ce1d9a"
Q8_FORMAL_REPLAY = ROOT / "cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.py"
Q8_FORMAL_REPLAY_SHA256 = "a55cfc7fe46f43287f34750b287a6dfb66f9454b8eb77b02f41e681e00b32210"
Q8_FORMAL_REPORT = ROOT / "xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md"
Q8_FORMAL_REPORT_SHA256 = "37ce842eece0e79f0768bdfd492be70905bb83ba62af93965b4c4a2a3d6f03a3"
Q8_FORMAL_REVIEW = ROOT / "xmodel/max12-912-order3-nu-q8-formal-branch-review-grok-20260824.md"
Q8_FORMAL_REVIEW_SHA256 = "32750e4e350919d7d52984feab06d3cd2d801386caec5848f7c5750bf9e8e846"
NORM_REPORT = ROOT / "xmodel/max12-912-order3-critical-value-norm-20260824.md"
NORM_REPORT_SHA256 = "7339478798e00894c7b975c60aca821ec7ff2da383ffe5165a93cfa361bb6cb6"
NORM_REVIEW = ROOT / "xmodel/max12-912-order3-critical-value-norm-review-grok-20260824.md"
NORM_REVIEW_SHA256 = "b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e"
NORM_REPLAY = ROOT / "cases/max12_912_order3_critical_value_norm_20260824/replay.py"
NORM_REPLAY_SHA256 = "88f4e2145defe8b548cd5794d171ee7919da77257811a51271df7dbb68e7e4df"


def load_module(name, path, expected_sha256):
    if sha256(path.read_bytes()).hexdigest() != expected_sha256:
        raise RuntimeError(f"dependency hash mismatch: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


P = load_module("q8_jet_parent", PARENT, PARENT_SHA256)
G = load_module("q8_jet_genus", GENUS_REPLAY, GENUS_REPLAY_SHA256)
if sha256(Q8_FORMAL_REPLAY.read_bytes()).hexdigest() != Q8_FORMAL_REPLAY_SHA256:
    raise RuntimeError("Q8 formal replay hash mismatch")
if sha256(Q8_FORMAL_REPORT.read_bytes()).hexdigest() != Q8_FORMAL_REPORT_SHA256:
    raise RuntimeError("Q8 formal report hash mismatch")
for dependency, expected in (
    (Q8_FORMAL_REVIEW, Q8_FORMAL_REVIEW_SHA256),
    (NORM_REPORT, NORM_REPORT_SHA256),
    (NORM_REVIEW, NORM_REVIEW_SHA256),
    (NORM_REPLAY, NORM_REPLAY_SHA256),
):
    if sha256(dependency.read_bytes()).hexdigest() != expected:
        raise RuntimeError(f"dependency hash mismatch: {dependency}")
M = P.M
Q8 = (
    Fraction(24), Fraction(296), Fraction(1548), Fraction(4428),
    Fraction(7320), Fraction(6498), Fraction(1782), Fraction(-1539),
    Fraction(-999),
)
MODULUS = G.pscale(Fraction(-1, 999), Q8)


def psub(left, right):
    return G.padd(left, G.pscale(-1, right))


def preduce(poly):
    return G.pdivmod(G.trim(poly), MODULUS)[1]


def pinverse(poly):
    r0, r1 = MODULUS, preduce(poly)
    s0, s1 = (Fraction(0),), (Fraction(1),)
    while G.trim(r1) != (Fraction(0),):
        quotient, remainder = G.pdivmod(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, psub(s0, G.pmul(quotient, s1))
    r0 = G.trim(r0)
    if len(r0) != 1 or not r0[0]:
        raise ZeroDivisionError(poly)
    return preduce(G.pscale(1 / r0[0], s0))


@dataclass(frozen=True)
class NF:
    poly: tuple[Fraction, ...]

    def __init__(self, value=0):
        if isinstance(value, NF):
            poly = value.poly
        elif isinstance(value, tuple):
            poly = tuple(Fraction(item) for item in value)
        else:
            poly = (Fraction(value),)
        object.__setattr__(self, "poly", preduce(poly))

    def __add__(self, other):
        return NF(G.padd(self.poly, NF(other).poly))

    __radd__ = __add__

    def __neg__(self):
        return NF(G.pscale(-1, self.poly))

    def __sub__(self, other):
        return self + (-NF(other))

    def __rsub__(self, other):
        return NF(other) - self

    def __mul__(self, other):
        return NF(G.pmul(self.poly, NF(other).poly))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        return NF(pinverse(self.poly))

    def __truediv__(self, other):
        return self * NF(other).inverse()

    def __rtruediv__(self, other):
        return NF(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base, power = NF(1), self, exponent
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power >>= 1
        return out

    def __bool__(self):
        return self.poly != (Fraction(0),)


ZERO, ONE = NF(0), NF(1)


@dataclass(frozen=True)
class Series:
    coefficients: tuple[NF, ...]

    def __init__(self, coefficients=()):
        values = [NF(value) for value in coefficients]
        values.extend([ZERO] * (4 - len(values)))
        object.__setattr__(self, "coefficients", tuple(values[:4]))

    @staticmethod
    def constant(value):
        return Series((NF(value),))

    def __add__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        return Series(tuple(a + b for a, b in zip(self.coefficients, other.coefficients)))

    __radd__ = __add__

    def __neg__(self):
        return Series(tuple(-value for value in self.coefficients))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        out = [ZERO] * 4
        for left_degree, left in enumerate(self.coefficients):
            for right_degree, right in enumerate(other.coefficients):
                if left_degree + right_degree < 4:
                    out[left_degree + right_degree] = (
                        out[left_degree + right_degree] + left * right
                    )
        return Series(tuple(out))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        out, base, power = Series.constant(1), self, exponent
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power >>= 1
        return out


def series_digest(value):
    return [digest(coefficient) for coefficient in value.coefficients]


def qseries_mul(left, right, s):
    """Multiply a+b*z modulo z^2=s, with truncated-series coefficients."""
    a, b = left
    c, d = right
    return (a * c + s * b * d, a * d + b * c)


def qseries_pow(value, exponent, s):
    out = (Series.constant(1), Series.constant(0))
    for _ in range(exponent):
        out = qseries_mul(out, value, s)
    return out


def qseries_reduce(poly, s):
    even, odd = Series.constant(0), Series.constant(0)
    for exponent, coefficient in poly.items():
        term = coefficient * (s ** (exponent // 2))
        if exponent % 2:
            odd = odd + term
        else:
            even = even + term
    return even, odd


def qseries_norm(value, s):
    a, b = value
    return a * a - s * b * b


def taylor_family(poly):
    """Hashes of f^(ell)(r)/ell!, retaining the formal center r."""
    family = []
    degree = max(poly)
    for ell in range(degree + 1):
        entries = []
        for source_degree, coefficient in sorted(poly.items()):
            if source_degree < ell:
                continue
            r_degree = source_degree - ell
            scaled = comb(source_degree, ell) * coefficient
            for t_degree, value in enumerate(scaled.coefficients):
                for v_degree, scalar in enumerate(value.poly):
                    if scalar:
                        entries.append((r_degree, t_degree, v_degree, scalar))
        encoded = ";".join(
            f"{rdeg},{tdeg},{vdeg},{value.numerator}/{value.denominator}"
            for rdeg, tdeg, vdeg, value in entries
        )
        family.append({
            "ell": ell,
            "terms": len(entries),
            "sha256": sha256(encoded.encode()).hexdigest(),
        })
    return family


def nf_eval(value, bases):
    total = ZERO
    powers = []
    for index, base in enumerate(bases):
        maximum = max((monomial[index] for monomial in value), default=0)
        row = [ONE]
        for _ in range(maximum):
            row.append(row[-1] * base)
        powers.append(row)
    for monomial, coefficient in value.items():
        term = NF(coefficient)
        for index, exponent in enumerate(monomial):
            term = term * powers[index][exponent]
        total = total + term
    return total


def series_eval(value, bases):
    total = Series.constant(0)
    powers = []
    for index, base in enumerate(bases):
        maximum = max((monomial[index] for monomial in value), default=0)
        row = [Series.constant(1)]
        for _ in range(maximum):
            row.append(row[-1] * base)
        powers.append(row)
    for monomial, coefficient in value.items():
        term = Series.constant(coefficient)
        for index, exponent in enumerate(monomial):
            term = term * powers[index][exponent]
        total = total + term
    return total


def solve(matrix, rhs):
    size = len(matrix)
    data = [list(row) + [rhs[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if data[row][column]),
            None,
        )
        if pivot is None:
            raise RuntimeError(("singular system", column))
        data[column], data[pivot] = data[pivot], data[column]
        scale = data[column][column].inverse()
        data[column] = [value * scale for value in data[column]]
        for row in range(size):
            if row == column:
                continue
            factor = data[row][column]
            if factor:
                data[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(data[row], data[column])
                ]
    return [data[index][-1] for index in range(size)]


def digest(value):
    encoded = ",".join(
        f"{coefficient.numerator}/{coefficient.denominator}"
        for coefficient in value.poly
    )
    return {
        "degree": len(value.poly) - 1,
        "nonzero": bool(value),
        "sha256": sha256(encoded.encode()).hexdigest(),
        "unit_mod_Q8": G.pgcd(value.poly, Q8) == (Fraction(1),),
    }


def make_series(base, n1, unknowns):
    p2, x1_2, x3_2, x5_2, a2_3, a4_3, a6_3 = unknowns
    p = Series((ONE, ZERO, p2))
    return [
        Series((ZERO, ONE)),
        Series((base[1], ZERO, x1_2)),
        Series((ZERO, n1[1], ZERO, a2_3)),
        Series((base[3], ZERO, 3 * p2 + x3_2)),
        Series((ZERO, n1[2], ZERO, a4_3)),
        Series((base[5], ZERO, 6 * p2 + x5_2)),
        Series((ZERO, n1[3], ZERO, a6_3)),
        3 * p,
        Series.constant(0),
    ]


def ztrim(poly):
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def zdivmod(numerator, denominator):
    numerator, denominator = ztrim(numerator), ztrim(denominator)
    quotient = {}
    degree_denominator = max(denominator)
    leading_denominator = denominator[degree_denominator]
    while numerator and max(numerator) >= degree_denominator:
        degree = max(numerator) - degree_denominator
        coefficient = numerator[max(numerator)] / leading_denominator
        quotient[degree] = quotient.get(degree, ZERO) + coefficient
        for exponent, value in denominator.items():
            target = exponent + degree
            numerator[target] = numerator.get(target, ZERO) - coefficient * value
        numerator = ztrim(numerator)
    return ztrim(quotient), numerator


def zgcd(left, right):
    while right:
        _, remainder = zdivmod(left, right)
        left, right = right, remainder
    leading = left[max(left)]
    return {exponent: value / leading for exponent, value in left.items()}


def fp_trim(poly, prime):
    values = [value % prime for value in poly]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def fp_add(left, right, prime):
    length = max(len(left), len(right))
    return fp_trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(length)
    ], prime)


def fp_sub(left, right, prime):
    return fp_add(left, [-value for value in right], prime)


def fp_mul(left, right, prime):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return fp_trim(out, prime)


def fp_divmod(numerator, denominator, prime):
    numerator, denominator = fp_trim(numerator, prime), fp_trim(denominator, prime)
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, prime)
    while len(numerator) >= len(denominator) and numerator != [0]:
        degree = len(numerator) - len(denominator)
        coefficient = numerator[-1] * inverse % prime
        quotient[degree] = coefficient
        for index, value in enumerate(denominator):
            numerator[index + degree] = (
                numerator[index + degree] - coefficient * value
            ) % prime
        numerator = fp_trim(numerator, prime)
    return fp_trim(quotient, prime), numerator


def fp_mod(value, modulus, prime):
    return fp_divmod(value, modulus, prime)[1]


def fp_powmod(value, exponent, modulus, prime):
    out, base, power = [1], value, exponent
    while power:
        if power & 1:
            out = fp_mod(fp_mul(out, base, prime), modulus, prime)
        base = fp_mod(fp_mul(base, base, prime), modulus, prime)
        power >>= 1
    return out


def fp_gcd(left, right, prime):
    while right != [0]:
        _, remainder = fp_divmod(left, right, prime)
        left, right = right, remainder
    inverse = pow(left[-1], -1, prime)
    return fp_trim([value * inverse for value in left], prime)


def irreducible_mod_7_certificate():
    prime = 7
    monic = [5, 1, 4, 2, 6, 1, 2, 4, 1]
    reduced = [int(value) % prime for value in Q8]
    leading_inverse = pow(reduced[-1], -1, prime)
    assert [value * leading_inverse % prime for value in reduced] == monic
    x = [0, 1]
    frobenius_8 = fp_sub(fp_powmod(x, prime ** 8, monic, prime), x, prime)
    frobenius_4 = fp_sub(fp_powmod(x, prime ** 4, monic, prime), x, prime)
    assert fp_mod(frobenius_8, monic, prime) == [0]
    assert fp_gcd(monic, frobenius_4, prime) == [1]
    return monic


def main():
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    monic_mod_7 = irreducible_mod_7_certificate()

    v = NF((Fraction(0), Fraction(1)))
    D = 3 * v ** 2 - 2
    A2 = 3 * v ** 2 + 3 * v + 1
    x5 = -36 * v ** 2 * A2 / D
    x3 = x5 * (v + 2)
    x1 = x5 * (v + 1) + x5 ** 2 * (3 * v + 1) / (9 * v)
    base = [ZERO, x1, ZERO, ONE + x3, ZERO, NF(3) + x5, ZERO, NF(3), ZERO]
    assert all(not nf_eval(tails[ell], base) for ell in (1, 2, 3, 4, 5, 7))
    nu = nf_eval(tails[6], base)
    rho0 = nf_eval(tails[8], base)

    normals = (0, 2, 4, 6)
    selected_odd = (3, 5, 7)
    matrix3 = [
        [nf_eval(M.cpartial(tails[ell], column), base) for column in normals[1:]]
        for ell in selected_odd
    ]
    rhs3 = [
        -nf_eval(M.cpartial(tails[ell], normals[0]), base)
        for ell in selected_odd
    ]
    tail_normal = solve(matrix3, rhs3)
    n1 = [ONE] + tail_normal
    for ell in (1, 3, 5, 7):
        residual = sum((
            nf_eval(M.cpartial(tails[ell], column), base) * direction
            for column, direction in zip(normals, n1)
        ), ZERO)
        assert not residual

    def equations(unknowns):
        values = make_series(base, n1, unknowns)
        return [
            series_eval(tails[ell], values).coefficients[2]
            for ell in (2, 4, 6)
        ] + [
            series_eval(tails[ell], values).coefficients[3]
            for ell in (1, 3, 5, 7)
        ]

    zero_unknowns = [ZERO] * 7
    source = equations(zero_unknowns)
    columns = []
    for column in range(7):
        basis = [ZERO] * 7
        basis[column] = ONE
        value = equations(basis)
        columns.append([entry - origin for entry, origin in zip(value, source)])
    matrix7 = [[columns[column][row] for column in range(7)] for row in range(7)]
    solution = solve(matrix7, [-entry for entry in source])
    assert all(not entry for entry in equations(solution))

    final_values = make_series(base, n1, solution)
    nu_series = series_eval(tails[6], final_values)
    r8_series = series_eval(tails[8], final_values)
    assert not any(nu_series.coefficients[index] for index in (1, 2, 3))
    assert nu_series.coefficients[0] == nu
    assert not r8_series.coefficients[1]
    assert not r8_series.coefficients[3]
    rho2 = r8_series.coefficients[2]
    p2, _, x3_2, x5_2, _, _, _ = solution
    v2 = x3_2 / x5 - (v + 2) * (p2 + x5_2 / x5)
    assert G.pgcd(rho2.poly, Q8) == (Fraction(1),)
    assert G.pgcd(v2.poly, Q8) == (Fraction(1),)

    # Type the corrected Q8 jet in the reviewed unordered critical-value
    # stratifier.  Before the harmless constant scaling nu->1, the leaf
    # quadratic is
    #   B/(54*nu)=z^2-s, s=-p/3-10*r8/(9*nu).
    # Vanishing of s, E, Norm(W), and Norm(F) is unchanged by that scaling.
    ring = M.Ring(compiled["ring_names"])
    f = {9: ring.one}
    U = {}
    for index in range(8):
        variable = ring.var(f"a{index}")
        f[index] = variable
        U[index - 9] = variable
    g = P.faber(ring, 9, 12, U)
    p_series = Fraction(1, 3) * final_values[7]
    s_series = -(
        Fraction(1, 3) * p_series
        + r8_series * (Fraction(10, 9) / nu)
    )
    f_series = {9: Series.constant(1)}
    for index in range(8):
        f_series[index] = final_values[index]
    g_series = {
        exponent: series_eval(value, final_values)
        for exponent, value in g.items()
    }
    f_pair = qseries_reduce(f_series, s_series)
    g_pair = qseries_reduce(g_series, s_series)
    F_pair = qseries_pow(f_pair, 4, s_series)
    G_pair = qseries_pow(g_pair, 3, s_series)
    E_series = G_pair[0] * F_pair[1] - G_pair[1] * F_pair[0]
    W_pair = (G_pair[0] - F_pair[0], G_pair[1] - F_pair[1])
    normW_series = qseries_norm(W_pair, s_series)
    normF_series = qseries_norm(F_pair, s_series)
    assert not E_series.coefficients[0]
    first_E_degree = next(
        index for index, value in enumerate(E_series.coefficients) if value
    )
    E_lead = E_series.coefficients[first_E_degree]
    assert G.pgcd(E_lead.poly, Q8) == (Fraction(1),)
    E_lead_inverse = E_lead.inverse()
    assert E_lead * E_lead_inverse == ONE
    for unit_series in (s_series, normW_series, normF_series):
        assert G.pgcd(unit_series.coefficients[0].poly, Q8) == (Fraction(1),)

    # Reconstruct every coefficient of both original Taylor families at the
    # true boundary center r=A/9.  The actual polynomial coefficients are
    # u^ell times these divided derivatives.  Keeping r formal is mandatory:
    # the spectral center z=0 is not the original y=0 boundary in general.
    f_taylor_family = taylor_family(f_series)
    g_taylor_family = taylor_family(g_series)
    assert len(f_taylor_family) == 10 and len(g_taylor_family) == 13
    assert f_taylor_family[-1]["terms"] == 1
    assert g_taylor_family[-1]["terms"] == 1
    # Negative control for the previously tempting but false z=0 boundary:
    # f(r)-f(0) and g(r)-g(0) have monic leading terms r^9 and r^12.
    assert f_series[9].coefficients[0] == ONE
    assert g_series[12].coefficients[0] == ONE

    # Reconstruct f and g=F12 at the Q8 contact and check the charged local
    # squarefree/coprime/Taylor boundary conditions.
    f_values = {exponent: nf_eval(value, base) for exponent, value in f.items()}
    g_values = {exponent: nf_eval(value, base) for exponent, value in g.items()}
    f_derivative = {
        exponent - 1: exponent * value
        for exponent, value in f_values.items() if exponent
    }
    gcd_f_fz = zgcd(f_values, f_derivative)
    gcd_f_g = zgcd(f_values, g_values)
    assert set(gcd_f_fz) == {0} and gcd_f_fz[0] == ONE
    assert set(gcd_f_g) == {0} and gcd_f_g[0] == ONE
    assert not f_values[0]
    assert G.pgcd(f_values[1].poly, Q8) == (Fraction(1),)
    assert G.pgcd(g_values[0].poly, Q8) == (Fraction(1),)

    coefficient_names = (
        "a2_t", "a4_t", "a6_t", "p_t2", "x1_t2", "x3_t2",
        "x5_t2", "a2_t3", "a4_t3", "a6_t3",
    )
    coefficient_values = tail_normal + solution
    coefficient_payload = {
        name: digest(value)
        for name, value in zip(coefficient_names, coefficient_values)
    }
    expected_hashes = {
        "a2_t": "f63e7613c430fbeadda154b1a35864c8bb6286f0450442b93a294fd9b47f1506",
        "a4_t": "58ae91e96f70c755a03a7e2173a866cb9de9ad5763bf7993c4dfc3227e7733b7",
        "a6_t": "12e20325695f24844f7f0406e96248f15399dcaa5b5fd26167e3365be198b22b",
        "p_t2": "4e230538616971fe0cdef18c2796351724d48523244c7d6e852b8f2fa68f4a07",
        "x1_t2": "e5c568fcb13df88a195de7f0fbad1b07fbd1ea2f70f4ec10784121a1e6280db5",
        "x3_t2": "adbdbae341a2d79c398abe9822871fbfb66f9adfa10e212c7a31577f1b45be8b",
        "x5_t2": "ed21e05ae06be8bab6f9902dfb711d7879bf585b8dad3dcebcb6323456cb86fc",
        "a2_t3": "e04d00c06ec07f8119af6765a80d975f9d269aac28c2afc01b0ca517b7906d37",
        "a4_t3": "6d0e6d717c73f559d9619c8caea930fe1345eb8f44263b9f561ea4a579ebe48d",
        "a6_t3": "f1d9120f3e4a289d4991741b06e382545505d217f1457e791d81d17013f55fad",
    }
    assert {name: item["sha256"] for name, item in coefficient_payload.items()} == expected_hashes

    payload = {
        "case": "max12_912_order3_nu_q8_normalization_jet_20260824",
        "dependency_sha256": {
            "genus5_replay": GENUS_REPLAY_SHA256,
            "order3_fibre_compiler": PARENT_SHA256,
            "q8_formal_replay": Q8_FORMAL_REPLAY_SHA256,
            "q8_formal_report": Q8_FORMAL_REPORT_SHA256,
            "q8_formal_review": Q8_FORMAL_REVIEW_SHA256,
            "critical_value_norm_report": NORM_REPORT_SHA256,
            "critical_value_norm_review": NORM_REVIEW_SHA256,
            "critical_value_norm_replay": NORM_REPLAY_SHA256,
        },
        "coefficient_field": {
            "Q8_irreducible_mod_7": True,
            "Q8_monic_mod_7": monic_mod_7,
            "field": "Q[v]/(Q8)",
        },
        "normalization": {
            "parameter": "t=a0",
            "involution_character": "odd",
            "Kummer_character": 0,
            "seven_rows_through_even2_odd3": "PASS",
            "coefficient_digests": coefficient_payload,
            "v_t2": digest(v2),
            "r8_t2": digest(rho2),
        },
        "critical_value_norm_leaf": {
            "quadratic": "B/(54*nu)=z^2-s",
            "s": "-p/3-10*r8/(9*nu)",
            "constant_scaling": (
                "nu->1 rescales the pair data but preserves the vanishing "
                "of s, E, Norm(W), and Norm(F)"
            ),
            "s_series": series_digest(s_series),
            "E_series": series_digest(E_series),
            "NormW_series": series_digest(normW_series),
            "NormF_series": series_digest(normF_series),
            "E_first_nonzero_degree": first_E_degree,
            "E_lead_gcd_Q8": "1",
            "E_lead_inverse_mod_Q8": digest(E_lead_inverse),
            "node_leaf": "s*Norm(F)*Norm(W)!=0 and E=0 (equal non-1 values)",
            "punctured_formal_branch_leaf": (
                "s*Norm(F)*Norm(W)*E!=0 (unabsorbed unequal values)"
            ),
        },
        "terminal_pullback": {
            "normalized": "r8=rho0+C*t^2+O(t^4), C!=0",
            "weighted": "r8=p0^10*R8(v0)+p0*C(v0)*a0^2+O(a0^4)",
            "differential": "18*p0*C(v0)*a0*a0'+O(a0^3*a0')=j/u",
            "finite_node_contact": "impossible for polynomial h",
            "infinity_if_a0_vanishes_order_e": "necessary H=3*(2*e+1)",
        },
        "boundary_control": {
            "depression": "z=u*y+r with r=A/9 and r/u in C(x)",
            "P_family": "[y^ell]P=u^ell*f^(ell)(r)/ell!, 0<=ell<=9",
            "Q_family": "[y^ell]Q=u^ell*g^(ell)(r)/ell!, 0<=ell<=12",
            "P_family_digests": f_taylor_family,
            "Q_family_digests": g_taylor_family,
            "spectral_center_only": {
                "f_at_zero": "0",
                "f_z_at_zero_unit": True,
                "g_at_zero_unit": True,
            },
            "f_squarefree": True,
            "gcd_f_g": "1",
            "source_values": "P(x,0)=f(r); Q(x,0)=g(r)",
            "old_z0_negative_control": (
                "f(r)-f(0) and g(r)-g(0) have respective monic leading "
                "terms r^9 and r^12"
            ),
            "charged_polynomiality": (
                "all 10 P-family and all 13 Q-family coefficients remain in C[x]"
            ),
        },
        "producer_conclusion": (
            "The Q8 non-parity branch has invariant parameter a0, moves "
            "quadratically in v, and has a nonzero quadratic r8 pullback. "
            "It cannot meet its parity node above a finite x-place."
        ),
        "scope": (
            "lowest formal jet and local node-contact/boundary control only; "
            "no global normalization, no exclusion of the punctured branch, "
            "and no all-(9,12), maximum-twelve, counterexample, or JC2 "
            "conclusion"
        ),
    }
    import json
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
