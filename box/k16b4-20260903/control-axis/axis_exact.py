#!/usr/bin/env python3
"""Exact b4-axis replay of the frozen coefficient-array recurrence.

This is a control driver, not a replacement definition.  It ports the array
operations in the charged ``terminal_array_recurrence.py`` from GF(p) to the
quadratic Q-algebra A_t=Q[y]/(H_t), sets b3=q_{2,0}=...=0 and b4=1, and hence
computes the coefficient of b4^(4t+1-k) in every terminal row.  The sign is
the question/report convention T=[X^k]E; the frozen JSON stores R=-E.
"""

from __future__ import annotations

import argparse
import dataclasses
from fractions import Fraction
import importlib.util
import json
import math
import pathlib
import sympy as sp
from typing import Any


FROZEN = pathlib.Path("/tmp/jc2-lane.6VGazO/inputs")


@dataclasses.dataclass(frozen=True)
class Quad:
    """a+b*y in Q[y]/(H_t), represented in the basis (1,y)."""

    t: int
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(t: int, value: Any) -> "Quad":
        if isinstance(value, Quad):
            if value.t != t:
                raise TypeError("quadratic-algebra mismatch")
            return value
        return Quad(t, Fraction(value), Fraction(0))

    @property
    def q(self) -> int:
        return 2 * self.t + 1

    @property
    def ysum(self) -> Fraction:
        return Fraction(self.t + 1, self.q)

    @property
    def y2_constant(self) -> Fraction:
        return -Fraction((self.t + 1) * (3 * self.t + 2), 12 * self.q**2)

    def __add__(self, other: Any) -> "Quad":
        z = self.coerce(self.t, other)
        return Quad(self.t, self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self) -> "Quad":
        return Quad(self.t, -self.a, -self.b)

    def __sub__(self, other: Any) -> "Quad":
        return self + (-self.coerce(self.t, other))

    def __rsub__(self, other: Any) -> "Quad":
        return self.coerce(self.t, other) - self

    def __mul__(self, other: Any) -> "Quad":
        z = self.coerce(self.t, other)
        return Quad(
            self.t,
            self.a * z.a + self.b * z.b * self.y2_constant,
            self.a * z.b + self.b * z.a + self.b * z.b * self.ysum,
        )

    __rmul__ = __mul__

    def norm(self) -> Fraction:
        # Product under y -> ysum-y.  This is the quotient-algebra norm.
        return self.a * self.a + self.a * self.b * self.ysum - self.b * self.b * self.y2_constant

    def inverse(self) -> "Quad":
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError(f"zero divisor in A_{self.t}: {self}")
        return Quad(self.t, (self.a + self.b * self.ysum) / n, -self.b / n)

    def __truediv__(self, other: Any) -> "Quad":
        return self * self.coerce(self.t, other).inverse()

    def __rtruediv__(self, other: Any) -> "Quad":
        return self.coerce(self.t, other) / self

    def __pow__(self, exponent: int) -> "Quad":
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        answer = Quad.coerce(self.t, 1)
        base = self
        n = exponent
        while n:
            if n & 1:
                answer *= base
            base *= base
            n >>= 1
        return answer

    def d_coordinates(self) -> tuple[Fraction, Fraction]:
        # d=2*q*y-(t+1).
        return self.a + self.b * Fraction(self.t + 1, 2 * self.q), self.b / (2 * self.q)

    def at_rational_y(self, value: Fraction) -> Fraction:
        return self.a + self.b * value

    def at_mod(self, value: int, prime: int) -> int:
        def fmod(x: Fraction) -> int:
            return (x.numerator % prime) * pow(x.denominator % prime, -1, prime) % prime

        return (fmod(self.a) + fmod(self.b) * value) % prime


def qzero(t: int) -> Quad:
    return Quad.coerce(t, 0)


def qone(t: int) -> Quad:
    return Quad.coerce(t, 1)


def derivative(array: list[Quad]) -> list[Quad]:
    return [(index + 1) * array[index + 1] for index in range(len(array) - 1)]


def convolution(left: list[Quad], right: list[Quad], degree: int, t: int) -> Quad:
    return sum(
        (left[index] * right[degree - index]
         for index in range(degree + 1)
         if index < len(left) and degree - index < len(right)),
        qzero(t),
    )


def shift_to_l(coefficients: dict[int, Quad], b4: Quad, maximum: int, t: int) -> list[Quad]:
    answer = [qzero(t) for _ in range(maximum + 1)]
    for exponent, coefficient in coefficients.items():
        for degree in range(exponent + 1):
            answer[degree] += coefficient * math.comb(exponent, degree) * b4 ** (exponent - degree)
    return answer


def closed_pivot(t: int, weight: int, y: Quad) -> Quad:
    q, e = 2 * t + 1, 3 * t + 1
    d = 2 * q * y - (t + 1)
    if weight < t:
        j = weight
        aa = (9*j*j*t + 18*j*j - 54*j*t*t - 81*j*t - 26*j
              + 72*t**3 + 144*t*t + 88*t + 16)
        bb = (-9*j*j*t - 10*j*j + 24*j*t*t + 33*j*t + 10*j
              - 12*t**3 - 20*t*t - 8*t)
        return Fraction(3*t*e, (t+1)*(3*t+2)**3*(4*t-2*j+1)) * (aa*d + bb)
    if weight <= 2*t:
        j = weight
        aa = 12*t*t + 16*t + 4 - j*(3*t+4)
        bb = 2*(t+1)*(j-t)
        return -Fraction(3*t*e*(q-j), (t+1)*q*(3*t+2)**2*(4*t-2*j+1)) * (aa*d + bb)
    g = Fraction(e*t, q*q) * y - Fraction(e*t*(t+1), 6*q**3)
    return g * d / (2*y)


def l_arrays(t: int, y: Quad, b3: Quad, b4: Quad,
             residual: dict[int, Quad], solved_c: dict[int, Quad],
             solved_u: dict[int, Quad], b2: Quad) -> tuple[list[Quad], list[Quad]]:
    q, e, top = 2*t+1, 3*t+1, 4*t+1
    g = Fraction(e*t, q*q) * y - Fraction(e*t*(t+1), 6*q**3)
    ux = {q: qone(t)}
    for index in range(2, 2*t+1):
        ux[q-index] = residual.get(index, qzero(t)) if index < t else solved_u.get(index, qzero(t))
    cx = {t-1: qone(t)}
    for index in range(1, t):
        cx[t-1-index] = solved_c.get(index, qzero(t))
    uu = shift_to_l(ux, b4, q, t)
    cc = shift_to_l(cx, b4, t-1, t)

    bb = [qzero(t) for _ in range(t+1)]
    for degree in range(t):
        bb[degree+1] = g*(3*degree+5)*cc[degree] / (2*y*(degree+1))

    ss = [qzero(t) for _ in range(2*t+1)]
    for degree in range(2*t+1):
        value = 3*g*(degree+1)*(uu[degree+1] if degree+1 < len(uu) else qzero(t))
        for aa in range(t):
            bb_index = degree-1-aa
            if 0 <= bb_index < len(bb):
                value += (3+2*aa-bb_index)*cc[aa]*bb[bb_index]
        if degree < len(cc):
            value += g*b3*(5*degree+7)*cc[degree]/2
        ss[degree] = value/(y*(2*degree+1))

    vv = [qzero(t) for _ in range(t+2)]
    vv[0] = -y*b3
    for degree in range(2, t+2):
        vv[degree] = cc[degree-2]
    yy = [qzero(t) for _ in range(2*t+2)]
    yy[0] = -g*b2
    for degree in range(1, len(yy)):
        yy[degree] = ss[degree-1]
    for degree in range(min(len(yy), len(bb))):
        yy[degree] -= b3*bb[degree]
    zz = [qzero(t) for _ in range(t+2)]
    zz[0] = -g*b3
    for degree in range(1, len(zz)):
        zz[degree] = bb[degree-1] if degree-1 < len(bb) else qzero(t)

    vp, yp, up = derivative(vv), derivative(yy), derivative(uu)
    nn = [qzero(t) for _ in range(e+1)]
    for degree in range(e+1):
        nn[degree] = (-convolution(vv, yp, degree, t)
                      + convolution(vp, yy, degree, t)
                      + 2*convolution(up, zz, degree, t))
    pp = [nn[degree+1]/(2*y) for degree in range(e)]
    rr = [qzero(t) for _ in range(top+1)]
    for degree in range(top+1):
        rr[degree] = (convolution(vv, pp, degree, t)
                      - convolution(up, yy, degree, t))
    rr[0] -= y*g

    rx = [qzero(t) for _ in range(top+1)]
    for degree in range(top+1):
        rx[degree] = sum(
            (math.comb(higher, degree) * (-b4) ** (higher-degree) * rr[higher]
             for higher in range(degree, top+1)),
            qzero(t),
        )
    return rr, rx


def exact_terminal_axis(t: int) -> tuple[list[Quad], list[dict[str, Any]]]:
    y = Quad(t, Fraction(0), Fraction(1))
    b3, b4 = qzero(t), qone(t)
    residual = {index: qzero(t) for index in range(2, t)}
    solved_c: dict[int, Quad] = {}
    solved_u: dict[int, Quad] = {}
    b2 = qzero(t)
    controls: list[dict[str, Any]] = []
    top = 4*t+1
    for weight in range(1, 2*t+2):
        def band_at(value: int) -> Quad:
            trial_c, trial_u, trial_b2 = dict(solved_c), dict(solved_u), b2
            if weight < t:
                trial_c[weight] = Quad.coerce(t, value)
            elif weight <= 2*t:
                trial_u[weight] = Quad.coerce(t, value)
            else:
                trial_b2 = Quad.coerce(t, value)
            return l_arrays(t, y, b3, b4, residual, trial_c, trial_u, trial_b2)[1][top-weight]

        rho = band_at(0)
        measured = band_at(1)-rho
        expected = closed_pivot(t, weight, y)
        if measured != expected:
            raise AssertionError(("pivot mismatch", t, weight, measured, expected))
        value = -rho/measured
        if weight < t:
            solved_c[weight] = value
            variable = f"C{weight}"
        elif weight <= 2*t:
            solved_u[weight] = value
            variable = f"q{weight}_0"
        else:
            b2 = value
            variable = "b2"
        controls.append({"weight": weight, "variable": variable, "pivot_norm": frac(measured.norm())})
    _rl, rx = l_arrays(t, y, b3, b4, residual, solved_c, solved_u, b2)
    if any(rx[degree] != qzero(t) for degree in range(2*t, top+1)):
        raise AssertionError(("nonzero high band", t))
    return [-rx[degree] for degree in range(2*t)], controls


def frac(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def linear_string(a: Fraction, b: Fraction, symbol: str) -> str:
    if b == 0:
        return frac(a)
    return f"({frac(a)})+({frac(b)})*{symbol}"


def resultant_h_linear(z: Quad) -> Fraction:
    # Every coefficient encountered here has nonzero y-part.  For linear g,
    # Res_y(H_t,g)=lc(H_t)*Norm(g)=12(2t+1)^2*Norm(g).
    if z.b == 0:
        return z.a*z.a
    return 12*z.q*z.q*z.norm()


def json_axis_value(t: int, expression: str) -> Quad:
    y = sp.Symbol("y")
    locals_: dict[str, Any] = {f"q{2*t+1}_1": y, "b3": 0, "b4": 1}
    locals_.update({f"q{j}_0": 0 for j in range(2, t)})
    value = sp.cancel(sp.sympify(expression, locals=locals_))
    numer, denom = value.as_numer_denom()

    def poly_to_quad(poly_expr: sp.Expr) -> Quad:
        p = sp.Poly(sp.expand(poly_expr), y, domain=sp.QQ)
        h = sp.Poly(12*(2*t+1)**2*y**2 - 12*(2*t+1)*(t+1)*y
                    + (t+1)*(3*t+2), y, domain=sp.QQ)
        p = p.rem(h)
        a = p.nth(0)
        b = p.nth(1)
        return Quad(t, Fraction(int(a.p), int(a.q)), Fraction(int(b.p), int(b.q)))

    return poly_to_quad(numer)/poly_to_quad(denom)


def load_finite_driver():
    path = FROZEN/"terminal_array_recurrence.py"
    spec = importlib.util.spec_from_file_location("charged_terminal_array_recurrence", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=pathlib.Path)
    parser.add_argument("--prime", type=int, default=1009)
    args = parser.parse_args()
    finite = load_finite_driver()
    result: dict[str, Any] = {
        "convention": "T[k]=[X^k]E; frozen terminal_laurent JSON expr is -T[k]",
        "specialization": "b3=0, q(j,0)=0 (2<=j<t), b4=1",
        "homogeneity": "T[t,k]|axis = coefficient*b4^(4t+1-k)",
        "prime_control": args.prime,
        "cases": [],
    }
    for t in range(2, 8):
        values, pivots = exact_terminal_axis(t)
        case: dict[str, Any] = {
            "t": t,
            "H": f"{12*(2*t+1)**2}*y^2-{12*(2*t+1)*(t+1)}*y+{(t+1)*(3*t+2)}",
            "pivot_closed_form_checks": len(pivots),
            "pivot_norms": pivots,
            "axis_rows": [],
        }
        for k, value in enumerate(values):
            da, db = value.d_coordinates()
            case["axis_rows"].append({
                "k": k,
                "power_b4": 4*t+1-k,
                "coefficient_y": linear_string(value.a, value.b, "y"),
                "coefficient_d": linear_string(da, db, "d"),
                "norm": frac(value.norm()),
                "resultant_y_H": frac(resultant_h_linear(value)),
                "unit_in_A_t": value.norm() != 0,
            })
        case["all_positive_axis_coefficients_units"] = all(z.norm() != 0 for z in values[1:])
        witness = values[2*t-1]
        case["witness"] = {
            "k": 2*t-1,
            "power_b4": 2*t+2,
            "coefficient_d": linear_string(*witness.d_coordinates(), "d"),
            "norm": frac(witness.norm()),
        }

        record_path = FROZEN/f"terminal_laurent_t{t}.json"
        if record_path.exists():
            record = json.loads(record_path.read_text(encoding="utf-8"))
            stored = [json_axis_value(t, item["expr"]) for item in record["terminal"]]
            matches = [values[k] == -stored[k] for k in range(2*t)]
            case["frozen_json"] = {
                "file": record_path.name,
                "sign_relation": "exact_T = -frozen_expr",
                "row_matches": matches,
                "all_match": all(matches),
            }

        roots = finite.roots(t, args.prime)
        modular: list[dict[str, Any]] = []
        for branch, root in enumerate(roots):
            charged_values, charged_pivots = finite.terminal_values(
                t, args.prime, root, 0, 1, {j: 0 for j in range(2, t)}
            )
            reduced = [z.at_mod(root, args.prime) for z in values]
            modular.append({
                "branch": branch,
                "y": root,
                "all_rows_match_frozen_array_recurrence": reduced == charged_values,
                "all_pivots_nonzero": all(p["coefficient"] != 0 for p in charged_pivots),
                "values": charged_values,
            })
        case["finite_array_control"] = modular

        if t == 2:
            fibres = []
            for yy in (Fraction(1, 5), Fraction(2, 5)):
                fibres.append({
                    "y": frac(yy),
                    "positive_coefficients": [frac(z.at_rational_y(yy)) for z in values[1:]],
                    "top_witness": frac(witness.at_rational_y(yy)),
                    "b4_axis_killed": any(z.at_rational_y(yy) != 0 for z in values[1:]),
                })
            case["rational_fibres"] = fibres
        result["cases"].append(case)

        print(
            f"AXIS_EXACT t={t} pivots={len(pivots)} "
            f"all_positive_units={int(case['all_positive_axis_coefficients_units'])} "
            f"witness_k={2*t-1} witness_d={case['witness']['coefficient_d']} "
            f"norm={case['witness']['norm']}"
        )
        if "frozen_json" in case:
            print(f"FROZEN_JSON_MATCH t={t} all={int(case['frozen_json']['all_match'])}")
        print(f"FINITE_ARRAY_MATCH t={t} all={int(all(x['all_rows_match_frozen_array_recurrence'] for x in modular))}")
    t2 = result["cases"][0]["rational_fibres"]
    for fibre in t2:
        print(
            f"T2_FIBRE y={fibre['y']} positive_coefficients={','.join(fibre['positive_coefficients'])} "
            f"top_witness={fibre['top_witness']} killed={int(fibre['b4_axis_killed'])}"
        )
    print("CONTROL_STATUS=PASS")
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.write_text(payload, encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
