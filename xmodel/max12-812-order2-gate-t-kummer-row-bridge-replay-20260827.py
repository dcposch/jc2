#!/usr/bin/env python3
"""Desk replay for the Gate-T Kummer/source-row bridge.

This intentionally does no Groebner-basis or CAS work.  It checks the frozen
source custody, the universal-to-D1 primitive map, the three root-value
coordinate matrices, and the parity-only negative control used in the
accompanying report.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
TOTAL = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_discovery_20260826/compile_t_rs0_discovery.py"
SQUARE_BASE = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
D1 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py"
TOTAL_G15 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/export_allrows_g15_v22.py"
TOTAL_G13_G14 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"

PINS = {
    TOTAL: "3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938",
    SQUARE_BASE: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    D1: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    TOTAL_G15: "c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6",
    TOTAL_G13_G14: "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
}
CANONICAL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


Monomial = tuple[tuple[str, int], ...]


def _mono(items: Iterable[tuple[str, int]]) -> Monomial:
    powers: dict[str, int] = {}
    for name, exponent in items:
        powers[name] = powers.get(name, 0) + exponent
    return tuple(sorted((name, exponent) for name, exponent in powers.items() if exponent))


@dataclass(frozen=True)
class Poly:
    """Tiny exact Laurent-polynomial type; negative exponents are deliberate."""

    terms: dict[Monomial, Fraction]

    def __post_init__(self) -> None:
        clean = {m: Fraction(c) for m, c in self.terms.items() if c}
        object.__setattr__(self, "terms", clean)

    @staticmethod
    def const(value: int | Fraction) -> "Poly":
        q = Fraction(value)
        return Poly({(): q} if q else {})

    @staticmethod
    def var(name: str, exponent: int = 1) -> "Poly":
        return Poly({_mono(((name, exponent),)): Fraction(1)})

    @staticmethod
    def coerce(value: "Poly | int | Fraction") -> "Poly":
        return value if isinstance(value, Poly) else Poly.const(value)

    def __add__(self, other: "Poly | int | Fraction") -> "Poly":
        rhs = Poly.coerce(other)
        out = dict(self.terms)
        for monomial, coefficient in rhs.terms.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
        return Poly(out)

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: "Poly | int | Fraction") -> "Poly":
        return self + (-Poly.coerce(other))

    def __rsub__(self, other: "Poly | int | Fraction") -> "Poly":
        return Poly.coerce(other) - self

    def __mul__(self, other: "Poly | int | Fraction") -> "Poly":
        rhs = Poly.coerce(other)
        out: dict[Monomial, Fraction] = {}
        for lm, lc in self.terms.items():
            for rm, rc in rhs.terms.items():
                monomial = _mono((*lm, *rm))
                out[monomial] = out.get(monomial, Fraction(0)) + lc * rc
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, value: int | Fraction) -> "Poly":
        return self * (1 / Fraction(value))

    def __pow__(self, exponent: int) -> "Poly":
        if exponent < 0:
            if len(self.terms) != 1:
                raise ValueError("negative power only implemented for monomials")
            (monomial, coefficient), = self.terms.items()
            if coefficient != 1:
                raise ValueError("negative power coefficient must be one")
            return Poly({_mono((name, power * exponent) for name, power in monomial): Fraction(1)})
        out = Poly.const(1)
        base = self
        n = exponent
        while n:
            if n & 1:
                out *= base
            base *= base
            n >>= 1
        return out

    def sign_substitute(self, name: str) -> "Poly":
        out: dict[Monomial, Fraction] = {}
        for monomial, coefficient in self.terms.items():
            exponent = dict(monomial).get(name, 0)
            out[monomial] = coefficient * ((-1) ** exponent)
        return Poly(out)

    def set_zero(self, name: str) -> "Poly":
        return Poly({m: c for m, c in self.terms.items() if dict(m).get(name, 0) == 0})

    def text(self) -> str:
        if not self.terms:
            return "0"
        pieces: list[str] = []
        for monomial, coefficient in sorted(self.terms.items()):
            factors = []
            for name, exponent in monomial:
                factors.append(name if exponent == 1 else f"{name}^{exponent}")
            body = "*".join(factors) or "1"
            pieces.append(f"{coefficient}*{body}")
        return " + ".join(pieces)


def var(name: str) -> Poly:
    return Poly.var(name)


def series(sigma: Poly, coefficients: list[Poly]) -> Poly:
    return sum((sigma ** index) * coefficient for index, coefficient in enumerate(coefficients))


def f_coefficients(p: Poly, c: Poly, r: Poly, n3: Poly, n2: Poly,
                   n1: Poly, n0: Poly, sigma: Poly) -> dict[int, Poly]:
    return {
        6: 2 * p,
        5: 2 * c,
        4: p ** 2 + 2 * r,
        3: 2 * p * c + sigma ** 2 * n3,
        2: c ** 2 + 2 * p * r + sigma ** 2 * n2,
        1: 2 * c * r + sigma ** 2 * n1,
        0: r ** 2 + sigma ** 2 * n0,
    }


def source_map_check() -> dict[str, object]:
    """Check the explicit universal-total -> charged D1 source map."""

    s = var("sigma")
    p0 = var("p")
    ell1 = var("ell1")
    theta = var("theta")
    eta = var("eta")
    b1, b0 = var("b1"), var("b0")
    a1, aa1 = var("a1_D1"), var("aa1_D1")
    a0, aa0 = var("a0_D1"), var("aa0_D1")
    c1, cc1 = var("c1_D1"), var("cc1_D1")
    c0, cc0 = var("c0_D1"), var("cc0_D1")

    # Images of the total-emitter jet series.  Zero entries are the exact
    # contact specialization; factors 4 and 2 undo the total emitter's /4
    # and /2 conventions.
    p_u = p0 + 2 * s * ell1
    cs_series = series(s, [Poly.const(0), Poly.const(0), theta * eta * b1])
    rs_series = series(s, [Poly.const(0), Poly.const(0), 4 * theta * eta * b0])
    az_series = series(s, [Poly.const(0), Poly.const(0), theta * a1, theta * aa1])
    ac_series = series(s, [Poly.const(0), Poly.const(0), theta * a0, theta * aa0])
    ez_series = series(s, [Poly.const(0), Poly.const(0), Poly.const(0),
                           2 * theta * c1, 2 * theta * cc1])
    ec_series = series(s, [Poly.const(0), Poly.const(0), Poly.const(0),
                           2 * theta * c0, 2 * theta * cc0])

    c_u = s ** 2 * cs_series
    r_u = (p_u ** 2 + s ** 2 * rs_series) / 4
    n3_u = s ** 3 * az_series
    n2_u = s ** 3 * ac_series
    n1_u = s ** 3 * (p_u * az_series + ez_series) / 2
    n0_u = s ** 3 * (p_u * ac_series + ec_series) / 2
    universal = f_coefficients(p_u, c_u, r_u, n3_u, n2_u, n1_u, n0_u, s)

    # Independently spell the D1 compiler's source_coefficients substitution.
    pp = p0 + 2 * s * ell1
    az = s ** 2 * theta * (a1 + s * aa1)
    ac = s ** 2 * theta * (a0 + s * aa0)
    cz = s ** 3 * theta * (c1 + s * cc1)
    cc = s ** 3 * theta * (c0 + s * cc0)
    rz = s ** 2 * theta * eta * b1
    rc = s ** 2 * theta * eta * b0
    kc = s ** 2 * rz
    kr = pp ** 2 / 4 + s ** 2 * rc
    n3_d = s ** 3 * az
    n2_d = s ** 3 * ac
    n1_d = s ** 3 * (pp * az / 2 + cz)
    n0_d = s ** 3 * (pp * ac / 2 + cc)
    d1 = f_coefficients(pp, kc, kr, n3_d, n2_d, n1_d, n0_d, s)

    equal = {str(index): universal[index] == d1[index] for index in range(7)}
    if not all(equal.values()):
        raise AssertionError(("universal/D1 primitive mismatch", equal))
    wrong_r = (p_u ** 2 + s ** 2 * series(
        s, [Poly.const(0), Poly.const(0), theta * eta * b0]
    )) / 4
    wrong_n1 = s ** 3 * (
        p_u * az_series
        + series(s, [Poly.const(0), Poly.const(0), Poly.const(0),
                     theta * c1, theta * cc1])
    ) / 2
    negative_controls = {
        "omit_rs_factor_4_detected": wrong_r != kr,
        "omit_ez_factor_2_detected": wrong_n1 != n1_d,
        "omit_moving_2sigma_ell1_detected": 2 * p0 != d1[6],
    }
    if not all(negative_controls.values()):
        raise AssertionError(("source-map negative control failed", negative_controls))
    return {
        "F0_through_F6_equal": equal,
        "loads_map": {"k": "k0", "k6": "k6", "k2": "k2load"},
        "targets_fixed": ["mu2", "mu4", "mu6", "J"],
        "negative_controls": negative_controls,
    }


def matmul(left: list[list[Poly]], right: list[list[Poly]]) -> list[list[Poly]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def root_coordinate_check() -> dict[str, object]:
    rho = var("rho")
    rho_inv = Poly.var("rho", -1)
    one, zero = Poly.const(1), Poly.const(0)
    identity = [[one, zero], [zero, one]]
    matrices = {
        "R": (
            [[Poly.const(Fraction(1, 4)), rho],
             [Poly.const(Fraction(1, 4)), -rho]],
            [[Poly.const(2), Poly.const(2)],
             [rho_inv / 2, -rho_inv / 2]],
            -rho / 2,
        ),
        "C": (
            [[Poly.const(Fraction(1, 2)), rho / 2],
             [Poly.const(Fraction(1, 2)), -rho / 2]],
            [[one, one], [rho_inv, -rho_inv]],
            -rho / 2,
        ),
        "A": (
            [[one, rho], [one, -rho]],
            [[Poly.const(Fraction(1, 2)), Poly.const(Fraction(1, 2))],
             [rho_inv / 2, -rho_inv / 2]],
            -2 * rho,
        ),
    }
    determinants: dict[str, str] = {}
    for name, (forward, inverse, expected_det) in matrices.items():
        if matmul(forward, inverse) != identity or matmul(inverse, forward) != identity:
            raise AssertionError(("root map inverse failed", name))
        determinant = forward[0][0] * forward[1][1] - forward[0][1] * forward[1][0]
        if determinant != expected_det:
            raise AssertionError(("root map determinant failed", name))
        determinants[name] = determinant.text()

    rs, cs, c0, c1, a0, a1 = (var(name) for name in ("rs", "cs", "c0", "c1", "a0", "a1"))
    pairs = {
        "R": (rs / 4 + rho * cs, rs / 4 - rho * cs),
        "C": ((c0 + rho * c1) / 2, (c0 - rho * c1) / 2),
        "A": (a0 + rho * a1, a0 - rho * a1),
    }
    for name, (plus, minus) in pairs.items():
        if plus.sign_substitute("rho") != minus or minus.sign_substitute("rho") != plus:
            raise AssertionError(("deck did not swap roots", name))
    return {
        "matrix_inverses_on_D_2rho": True,
        "determinants": determinants,
        "deck_swaps_plus_minus": True,
        "J1_root_ideal": ["Rplus", "Rminus", "Cplus", "Cminus"],
        "J2_root_ideal": ["Aplus", "Aminus"],
    }


def parity_countermodel_check() -> dict[str, object]:
    """Both pullbacks are deck-even, but they are different ideals."""

    rho, x = var("rho"), var("x")
    i_generator = x
    j_generator = x - 2 * rho ** 2  # image of x+p0 under p0 -> -2 rho^2
    if i_generator.sign_substitute("rho") != i_generator:
        raise AssertionError("I pullback is not deck invariant")
    if j_generator.sign_substitute("rho") != j_generator:
        raise AssertionError("J pullback is not deck invariant")
    residue_mod_i = j_generator.set_zero("x")
    if not residue_mod_i.terms:
        raise AssertionError("negative control collapsed: J unexpectedly lies in (x)")
    return {
        "base_ring": "Q[p0,x]",
        "ideals": {"I": "(x)", "J": "(x+p0)"},
        "kummer_pullbacks": {"I": "(x)", "J": "(x-2*rho^2)"},
        "both_deck_invariant": True,
        "J_generator_mod_I": residue_mod_i.text(),
        "ideals_unequal": True,
    }


def main() -> None:
    actual = {str(path.relative_to(ROOT)): digest(path) for path in PINS}
    for path, expected in PINS.items():
        if actual[str(path.relative_to(ROOT))] != expected:
            raise AssertionError(("frozen source mismatch", str(path), actual[str(path.relative_to(ROOT))], expected))

    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != CANONICAL_TAILS:
        raise AssertionError("canonical tails digest mismatch")
    if sorted(tails) != [str(index) for index in range(1, 8)]:
        raise AssertionError("tail row keys mismatch")
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    census = 0
    for row_text, entries in tails.items():
        row = int(row_text)
        for monomial, _coefficient in entries:
            exponents = [int(value) for value in monomial]
            if len(exponents) != 10:
                raise AssertionError(("tail width", row, exponents))
            if sum(exponent * weight for exponent, weight in zip(exponents, weights)) != 12 + row:
                raise AssertionError(("tail weight", row, exponents))
            if sum(exponents[7:]) > 1:
                raise AssertionError(("tail load nonlinearity", row, exponents))
            census += 1
    if census != 569:
        raise AssertionError(("tail census", census))

    total_text = TOTAL.read_text()
    total_g15_text = TOTAL_G15.read_text()
    d1_text = D1.read_text()
    sentinels = {
        "total_kummer_constant": 'p_total = "-2*rho^2+"' in total_text,
        "total_universal_source_parameter": "def source_block(prefix: str, p: str" in total_text,
        "d1_unsplit_p_series": 'pp = "(p+2*sigma*ell1)"' in d1_text,
        "d1_both_orientations": "D1AC_BOTH_ROOT_ORIENTATIONS" in d1_text,
        "actual_total_grade15_series": "def build_source_series(base):" in total_g15_text,
        "actual_total_grade15_rows_1_through_7": "ROWS = tuple(range(1, 8))" in total_g15_text,
    }
    if not all(sentinels.values()):
        raise AssertionError(("source sentinel mismatch", sentinels))

    payload = {
        "status": "PASS-GATE-T-KUMMER-ROW-BRIDGE-DESK-REPLAY",
        "scope": "ELEMENTARY_MAPS_AND_D1_PRIMITIVE_SOURCE_INTERFACE_ONLY_NO_FULL_ROW_IDEAL_OR_GATE_T_VERDICT",
        "frozen_sha256": actual,
        "canonical_tails_sha256": CANONICAL_TAILS,
        "tail_census": census,
        "source_sentinels": sentinels,
        "universal_to_D1": source_map_check(),
        "root_coordinates": root_coordinate_check(),
        "parity_negative_control": parity_countermodel_check(),
        "kummer_module": {
            "map": "Q[p0] -> Q[rho], p0 |-> -2*rho^2",
            "presentation": "Q[p0,rho]/(p0+2*rho^2)",
            "basis_over_Q[p0]": ["1", "rho"],
            "rank": 2,
        },
    }
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
