#!/usr/bin/env python3
"""Independent sparse reconstruction for the cyclic-D1 source rows.

This module deliberately does not import ``order3_fibre.py`` or the shared
Faber arithmetic module.  It reconstructs the two Faber polynomials by the
differential recurrence for ``(1+U)^alpha``, reconstructs the inverse root by
coefficient cancellation, and then reads all eight negative Laurent tails.
The V2 gate compares these plain dictionaries with the frozen parent output.

Substantive execution is AWS Linux only.  Importing the module only defines
the arithmetic; ``main`` performs the platform/tag check before compiling.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


Monomial = tuple[int, ...]
Coefficient = dict[Monomial, Fraction]
Laurent = dict[int, Coefficient]


class IndependentFailure(RuntimeError):
    pass


def clean(value: Coefficient) -> Coefficient:
    return {monomial: coefficient for monomial, coefficient in value.items()
            if coefficient}


def add(left: Coefficient, right: Coefficient) -> Coefficient:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return clean(out)


def scale(scalar: Fraction | int, value: Coefficient) -> Coefficient:
    scalar = Fraction(scalar)
    return clean({monomial: scalar * coefficient
                  for monomial, coefficient in value.items()})


def multiply(left: Coefficient, right: Coefficient) -> Coefficient:
    out: Coefficient = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in
                             zip(left_monomial, right_monomial))
            out[monomial] = (
                out.get(monomial, Fraction(0))
                + left_coefficient * right_coefficient
            )
    return clean(out)


@dataclass(frozen=True)
class Ring:
    names: tuple[str, ...]

    @property
    def one(self) -> Coefficient:
        return {(0,) * len(self.names): Fraction(1)}

    def variable(self, name: str) -> Coefficient:
        exponent = [0] * len(self.names)
        exponent[self.names.index(name)] = 1
        return {tuple(exponent): Fraction(1)}


def coefficient_of_power(series: Laurent, power: int, target: int,
                         one: Coefficient) -> Coefficient:
    """Return one Laurent coefficient using an independent convolution DP."""
    if power == 0:
        return one if target == 0 else {}
    if not series:
        return {}
    minimum = min(series)
    maximum = max(series)
    current: dict[int, Coefficient] = {0: one}
    for factor_index in range(power):
        following: dict[int, Coefficient] = {}
        remaining = power - factor_index - 1
        for old_exponent, old_coefficient in current.items():
            for exponent, coefficient in series.items():
                new_exponent = old_exponent + exponent
                if not (
                    new_exponent + remaining * minimum
                    <= target
                    <= new_exponent + remaining * maximum
                ):
                    continue
                following[new_exponent] = add(
                    following.get(new_exponent, {}),
                    multiply(old_coefficient, coefficient),
                )
        current = following
    return current.get(target, {})


def faber_by_differential_recurrence(ring: Ring, degree: int,
                                     m: int = 9) -> Laurent:
    """Compute ``[z^degree (1+U)^(degree/m)]_+`` without binomial powers.

    Put ``q=z^-1`` and ``R=(1+U)^(degree/m)=sum r_n q^n``.  The identity
    ``(1+U)R'=(degree/m)U'R`` gives

      n r_n = sum_{d=1}^n (((degree/m)+1)d-n) u_d r_(n-d).

    Only ``n<=degree`` contributes to the polynomial part.
    """
    alpha = Fraction(degree, m)
    u: dict[int, Coefficient] = {
        m - index: ring.variable(f"a{index}") for index in range(m - 1)
    }
    r: dict[int, Coefficient] = {0: ring.one}
    for n in range(1, degree + 1):
        total: Coefficient = {}
        for d in range(1, n + 1):
            if d not in u or n - d not in r:
                continue
            factor = (alpha + 1) * d - n
            total = add(total, scale(factor, multiply(u[d], r[n - d])))
        r[n] = scale(Fraction(1, n), total)
    return {degree - n: coefficient for n, coefficient in r.items()
            if coefficient}


def inverse_root_by_cancellation(ring: Ring, max_q: int,
                                 m: int = 9) -> Laurent:
    """Solve ``f(z(w))=w^m`` through ``z=w+sum c_q w^-q``."""
    out: Laurent = {1: ring.one}
    for q in range(1, max_q + 1):
        target = m - 1 - q
        residual = coefficient_of_power(out, m, target, ring.one)
        for index in range(m - 1):
            residual = add(
                residual,
                multiply(
                    ring.variable(f"a{index}"),
                    coefficient_of_power(out, index, target, ring.one),
                ),
            )
        correction = scale(Fraction(-1, m), residual)
        if correction:
            out[-q] = correction

    for q in range(1, max_q + 1):
        target = m - 1 - q
        residual = coefficient_of_power(out, m, target, ring.one)
        for index in range(m - 1):
            residual = add(
                residual,
                multiply(
                    ring.variable(f"a{index}"),
                    coefficient_of_power(out, index, target, ring.one),
                ),
            )
        if residual:
            raise IndependentFailure(("inverse-root residual", target))
    if out.get(0):
        raise IndependentFailure("inverse root acquired forbidden w^0 term")
    if out.get(-9):
        raise IndependentFailure("inverse root acquired forbidden w^-9 term")
    return out


def build() -> dict[str, object]:
    names = tuple([f"a{i}" for i in range(8)] + ["k"])
    ring = Ring(names)
    f6 = faber_by_differential_recurrence(ring, 6)
    f12 = faber_by_differential_recurrence(ring, 12)
    g = dict(f12)
    k = ring.variable("k")
    for exponent, coefficient in f6.items():
        g[exponent] = add(g.get(exponent, {}), multiply(k, coefficient))
    g = {exponent: coefficient for exponent, coefficient in g.items()
         if coefficient}

    inverse_root = inverse_root_by_cancellation(ring, 19)
    tails: dict[int, Coefficient] = {}
    for ell in range(1, 9):
        coefficient: Coefficient = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = add(
                coefficient,
                multiply(
                    g_coefficient,
                    coefficient_of_power(
                        inverse_root, z_exponent, -ell, ring.one
                    ),
                ),
            )
        tails[ell] = scale(-1, coefficient)

    # Full composition control across every nonnegative Faber coefficient and
    # every consumed negative tail.  This is separate from the parent compare.
    for target in range(12, -9, -1):
        coefficient: Coefficient = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = add(
                coefficient,
                multiply(
                    g_coefficient,
                    coefficient_of_power(
                        inverse_root, z_exponent, target, ring.one
                    ),
                ),
            )
        if target == 12:
            expected = ring.one
        elif target == 6:
            expected = ring.variable("k")
        elif target < 0:
            expected = scale(-1, tails[-target])
        else:
            expected = {}
        if coefficient != expected:
            raise IndependentFailure(("g(z(w)) composition", target))

    return {
        "names": names,
        "F6": f6,
        "F12": f12,
        "g": g,
        "inverse_root": inverse_root,
        "tails": tails,
    }


def coefficient_digest(value: Coefficient) -> str:
    serial = [[list(monomial), str(coefficient)]
              for monomial, coefficient in sorted(value.items())]
    return sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest()


def laurent_digest(value: Laurent) -> str:
    serial = [
        [exponent, [[list(monomial), str(coefficient)]
                    for monomial, coefficient in sorted(polynomial.items())]]
        for exponent, polynomial in sorted(value.items())
    ]
    return sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def main() -> None:
    tag = require_aws()
    compiled = build()
    payload = {
        "aws_tag": tag,
        "algorithm": {
            "Faber": "differential recurrence for (1+U)^alpha",
            "inverse_root": "sequential Laurent coefficient cancellation",
            "tail": "independent full convolution coefficient extraction",
            "imports_parent_arithmetic": False,
        },
        "digests": {
            "F6": laurent_digest(compiled["F6"]),
            "F12": laurent_digest(compiled["F12"]),
            "g": laurent_digest(compiled["g"]),
            "inverse_root": laurent_digest(compiled["inverse_root"]),
            "tails": {str(ell): coefficient_digest(value)
                      for ell, value in compiled["tails"].items()},
        },
        "supports": {
            "F6": sum(len(value) for value in compiled["F6"].values()),
            "F12": sum(len(value) for value in compiled["F12"].values()),
            "g": sum(len(value) for value in compiled["g"].values()),
            "inverse_root": sum(len(value)
                                for value in compiled["inverse_root"].values()),
            "tails": {str(ell): len(value)
                      for ell, value in compiled["tails"].items()},
        },
    }
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-INDEPENDENT-FABER-INVERSE-TAIL-RECONSTRUCTION")


if __name__ == "__main__":
    main()
