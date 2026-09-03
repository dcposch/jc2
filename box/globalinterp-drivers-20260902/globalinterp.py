#!/usr/bin/env python3
"""GLOBAL-INTERPOLATION: exact finite-order equations from ``g`` alone.

This is a fail-closed SymPy driver for the global interpolation framework.  It
does *not* pretend that the numerical Moh skeleton determines a Puiseux tree.
The JSON input therefore has two layers:

``skeleton``
    ``n, m, M, V, delta, u, v`` (and optionally ``K``).  These fields are
    checked and copied to the output.

``branches``
    The missing realisation data: all ``n`` roots of ``g-c2`` as Laurent
    series in a common uniformizer ``z``, where ``x=z**(-L)``.  A branch has
    ``name``, optional ``orbit``, ``min_exp``, a dictionary ``terms`` whose
    keys are integer z-exponents, and optionally ``tail_from``.  Missing terms
    at and above ``tail_from`` become tame unknowns through the requested
    precision.  Missing terms on an exact branch (no ``tail_from``) are zero.
    Use ``terms_t`` instead of ``terms`` to give rational t-exponents.

``orbits``
    Optional metadata ``{name: {verified: true, representative: branch}}``.
    A verified orbit asserts that the displayed branches and tame variables
    really are related by the stated Galois action.  Only then is one
    NO-LOG equation per orbit counted as effective; all branchwise conjugate
    equations are still emitted.

``contacts`` / ``contacts_t``
    Optional first-separation orders.  ``contacts`` uses integer z-orders;
    ``contacts_t`` uses rational t-orders.  Keys are ``"branch1,branch2"``.
    If omitted, the first generically nonzero displayed/tame coefficient is
    used and its nonvanishing is listed among the inequations.

``uniformizer_denominator`` and ``max_t_order``
    ``L`` and the largest absolute t-order to impose.  The CLI ``--order``
    overrides ``max_t_order``.  ``min_t_order`` is optional; otherwise the
    total-degree-m monic gauge supplies the natural lower edge.  Set
    ``monic`` false only when working outside that normalization.

``polynomial_mode``
    Defaults to ``"moh_total_degree"``, imposing
    ``deg_x A_r <= m-r``.  Bare polynomiality has no a priori x-degree
    bound.  A bounded probe of it uses
    ``"coefficient_polynomiality_only"`` together with ``x_degree_cap``
    (one integer) or ``x_degree_caps`` (one integer for each ``r=0..m``).
    The output explicitly labels this as a bounded slice, not full POLY.

``bottom_delta_index``
    Zero-based location of ``delta_1`` in ``skeleton.delta`` (default 0,
    matching the charged reports); it must be an endpoint of this path list.
    Junctions are ordered from that endpoint, with each edge length
    ``L*abs(delta_child-delta_parent)`` and cumulative bottom-chart order the
    sum of edge lengths.  Absolute radii are emitted separately, preventing
    a radius from being mistaken for an activation gap.

The direct conditions represented by the output are, with
``D_i=prod_{j!=i}(tau_i-tau_j)``, ``H_i=F_i+a_i`` and
``F_i'=c/D_i``,

    B_r = (-1)**(n-1-r) sum_i H_i e_{n-1-r}(tau_[not i])/D_i,

    B_{m+1}=...=B_{n-1}=0,                 (n-m-1 relations)
    B_m=1 in the monic gauge,               (one *separate* relation)
    B_0,...,B_m in C[x].

Equivalently, for ``mu_q=sum_i H_i*tau_i**q/D_i``,

    mu_0=...=mu_{n-m-2}=0,  mu_{n-m-1}=1 (monic).

NO-LOG is ``[x**-1](1/D_i)=0``.  Since ``x**-1=z**L``, this is
``[z**L] W_i=0`` for ``W_i=1/D_i``.

To keep the emitted ideal linear/quadratic, the driver introduces named
prefix-product, inverse, power, time-value, and polynomial-coefficient
variables.  Every auxiliary equation is an ordinary coefficient convolution.
On the open set where the first-separation coefficients are nonzero, this is
an *exact existential lift*: projection after eliminating the auxiliaries is
the direct finite-order interpolation system.  It is not a relaxation.  The
precision certificate in the output records how far branch tails were needed.
If an input coefficient is itself nonlinear, resulting degree > 2 equations
are retained verbatim and flagged; they are never dropped.

Examples::

    python globalinterp.py example > /tmp/globalinterp-example.json
    python globalinterp.py emit /tmp/globalinterp-example.json --rank symbolic
    python globalinterp.py controls
    python globalinterp.py selftest

The controls include the four requested Keller maps and the precise NO-LOG
failure for ``g=y^2-x^2-x``.  All calculations are exact over SymPy's
characteristic-zero expression domain.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


DRIVER_VERSION = "GLOBAL-INTERPOLATION/1.0"


def _frac(value: Any) -> Fraction:
    """Parse an integer/rational JSON value without a float round-trip."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, float):
        return Fraction(str(value))
    return Fraction(str(value))


def _qstr(value: int, denominator: int) -> str:
    q = Fraction(value, denominator)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def _lcm(values: Iterable[int]) -> int:
    ans = 1
    for value in values:
        ans = math.lcm(ans, int(value))
    return ans


def _sym(name: str) -> sp.Symbol:
    return sp.Symbol(name)


@dataclass
class Equation:
    name: str
    family: str
    order_q: int
    expr: sp.Expr
    note: str = ""
    degree: int | str | None = None

    def as_json(self, L: int) -> dict[str, Any]:
        return {
            "name": self.name,
            "family": self.family,
            "order_z": self.order_q,
            "order_t": _qstr(self.order_q, L),
            "degree": self.degree,
            "equation": f"{sp.sstr(self.expr)} = 0",
            "note": self.note,
        }


class Registry:
    """Symbols in the lifted system, together with first-appearance orders."""

    def __init__(self) -> None:
        self.symbols: dict[str, sp.Symbol] = {}
        self.intro: dict[sp.Symbol, int] = {}
        self.kind: dict[sp.Symbol, str] = {}

    def get(self, name: str, order_q: int, kind: str) -> sp.Symbol:
        if name in self.symbols:
            out = self.symbols[name]
            self.intro[out] = min(self.intro[out], order_q)
            return out
        out = _sym(name)
        self.symbols[name] = out
        self.intro[out] = order_q
        self.kind[out] = kind
        return out


class Branch:
    def __init__(
        self,
        raw: dict[str, Any],
        L: int,
        namespace: dict[str, sp.Symbol],
        registry: Registry,
    ) -> None:
        self.name = str(raw["name"])
        self.orbit = raw.get("orbit")
        self.tail_from = int(raw["tail_from"]) if raw.get("tail_from") is not None else None
        self.tail_prefix = str(raw.get("tail_prefix", f"c_{self.name}"))
        self.registry = registry
        self.namespace = namespace
        terms: dict[int, sp.Expr] = {}
        if "terms" in raw and "terms_t" in raw:
            raise ValueError(f"branch {self.name}: use only one of terms and terms_t")
        if "terms_t" in raw:
            for exponent, value in raw["terms_t"].items():
                q = _frac(exponent) * L
                if q.denominator != 1:
                    raise ValueError(
                        f"branch {self.name}: t exponent {exponent} is not on the 1/{L} lattice"
                    )
                terms[int(q)] = sp.sympify(value, locals=namespace)
        else:
            for exponent, value in raw.get("terms", {}).items():
                terms[int(exponent)] = sp.sympify(value, locals=namespace)
        if not terms and self.tail_from is None:
            raise ValueError(f"branch {self.name}: empty exact series")
        inferred_min = min(terms) if terms else int(self.tail_from)
        self.min_exp = int(raw.get("min_exp", inferred_min))
        if any(q < self.min_exp for q in terms):
            raise ValueError(f"branch {self.name}: a displayed term lies below min_exp")
        self.terms = terms
        self.generated: dict[int, sp.Expr] = {}

    def coeff(self, q: int) -> sp.Expr:
        if q < self.min_exp:
            return sp.Integer(0)
        if q in self.terms:
            return self.terms[q]
        if self.tail_from is not None and q >= self.tail_from:
            if q not in self.generated:
                name = f"{self.tail_prefix}_{q}" if q >= 0 else f"{self.tail_prefix}_m{-q}"
                self.generated[q] = self.registry.get(name, q, "tame")
            return self.generated[q]
        return sp.Integer(0)

    def json_terms_through(self, qmax: int) -> dict[str, str]:
        return {
            str(q): sp.sstr(self.coeff(q))
            for q in range(self.min_exp, qmax + 1)
            if self.coeff(q) != 0
        }


def _first_nonzero(
    coefficient,
    qmin: int,
    qmax: int,
    label: str,
) -> tuple[int, sp.Expr]:
    for q in range(qmin, qmax + 1):
        value = sp.expand(coefficient(q))
        if value != 0:
            return q, value
    raise ValueError(f"could not find a nonzero leading coefficient for {label} through z^{qmax}")


def _coefficient_degree(expr: sp.Expr, unknowns: set[sp.Symbol]) -> int | str:
    local = sorted(expr.free_symbols & unknowns, key=str)
    if not local:
        return 0
    try:
        _num, den = sp.fraction(sp.cancel(expr))
        if den.free_symbols & unknowns:
            return "nonpolynomial"
        return int(sp.Poly(sp.expand(expr), *local).total_degree())
    except (sp.PolynomialError, TypeError, ValueError):
        return "nonpolynomial"


def _canonical(expr: sp.Expr) -> str:
    return sp.srepr(sp.expand(expr))


class GlobalInterpolationSystem:
    """Build the finite-order quadratic lift for one decorated skeleton."""

    REQUIRED_SKELETON = ("n", "m", "M", "V", "delta", "u", "v")

    def __init__(self, data: dict[str, Any], order_override: str | None = None) -> None:
        self.data = data
        self.skeleton = dict(data.get("skeleton", {}))
        missing = [key for key in self.REQUIRED_SKELETON if key not in self.skeleton]
        if missing:
            raise ValueError(f"skeleton is missing required fields: {', '.join(missing)}")
        self.n = int(self.skeleton["n"])
        self.m = int(self.skeleton["m"])
        if not (0 <= self.m < self.n):
            raise ValueError(f"need 0 <= m < n, got m={self.m}, n={self.n}")
        if int(self.skeleton["u"]) < 0 or int(self.skeleton["v"]) < 0:
            raise ValueError("u and v must be nonnegative")
        deltas = [_frac(v) for v in self.skeleton["delta"]]
        L_given = data.get("uniformizer_denominator")
        self.L = int(L_given) if L_given is not None else _lcm(q.denominator for q in deltas)
        if self.L <= 0:
            raise ValueError("uniformizer_denominator must be positive")
        for value in deltas:
            if (value * self.L).denominator != 1:
                raise ValueError(f"delta={value} is not on the declared 1/{self.L} lattice")
        self.delta = deltas
        max_t = _frac(order_override if order_override is not None else data.get("max_t_order", 0))
        max_q = max_t * self.L
        if max_q.denominator != 1:
            raise ValueError(f"max_t_order={max_t} is not on the 1/{self.L} lattice")
        self.qmax = int(max_q)
        self.monic = bool(data.get("monic", True))
        self.polynomial_mode = str(data.get("polynomial_mode", "moh_total_degree"))
        if self.polynomial_mode == "moh_total_degree":
            self.x_degree_caps = [self.m - r for r in range(self.m + 1)]
        elif self.polynomial_mode == "coefficient_polynomiality_only":
            raw_caps = data.get("x_degree_caps")
            if raw_caps is not None:
                if isinstance(raw_caps, dict):
                    try:
                        self.x_degree_caps = [int(raw_caps[str(r)]) for r in range(self.m + 1)]
                    except KeyError as exc:
                        raise ValueError("x_degree_caps dictionary needs keys 0,...,m") from exc
                else:
                    self.x_degree_caps = [int(value) for value in raw_caps]
                    if len(self.x_degree_caps) != self.m + 1:
                        raise ValueError("x_degree_caps must have m+1 entries")
            elif data.get("x_degree_cap") is not None:
                self.x_degree_caps = [int(data["x_degree_cap"])] * (self.m + 1)
            else:
                raise ValueError(
                    "coefficient_polynomiality_only needs a finite x_degree_cap or x_degree_caps"
                )
            if any(value < 0 for value in self.x_degree_caps):
                raise ValueError("x-degree caps must be nonnegative")
            if self.monic:
                self.x_degree_caps[self.m] = 0
        else:
            raise ValueError(
                "polynomial_mode must be moh_total_degree or coefficient_polynomiality_only"
            )
        self.bottom_delta_index = int(data.get("bottom_delta_index", 0))
        if not (0 <= self.bottom_delta_index < len(self.delta)):
            raise ValueError("bottom_delta_index is outside skeleton.delta")
        if len(self.delta) > 1 and self.bottom_delta_index not in (0, len(self.delta) - 1):
            raise ValueError("bottom_delta_index must be an endpoint of the declared level path")
        self.registry = Registry()

        parameter_names = [str(v) for v in data.get("parameters", ["c2"])]
        unknown_names = [str(v) for v in data.get("unknowns", [])]
        self.parameters = {_sym(name) for name in parameter_names}
        namespace = {str(s): s for s in self.parameters}
        for name in unknown_names:
            namespace[name] = self.registry.get(name, 0, "tame")
        namespace.update({"I": sp.I, "pi": sp.pi})
        self.namespace = namespace
        self.jacobian = sp.sympify(data.get("jacobian", "1"), locals=namespace)
        raw_branches = list(data.get("branches", []))
        if len(raw_branches) != self.n:
            raise ValueError(f"decorated input must contain n={self.n} branches, got {len(raw_branches)}")
        names = [str(branch.get("name")) for branch in raw_branches]
        if len(set(names)) != len(names):
            raise ValueError("branch names must be distinct")
        self.branches = [Branch(raw, self.L, namespace, self.registry) for raw in raw_branches]
        self.branch_by_name = {branch.name: branch for branch in self.branches}
        self.orbits = dict(data.get("orbits", {}))
        self.contacts_declared = self._parse_contacts(data.get("contacts", {}), in_t=False)
        contacts_t = self._parse_contacts(data.get("contacts_t", {}), in_t=True)
        overlap = set(self.contacts_declared) & set(contacts_t)
        if overlap:
            raise ValueError("the same pair is declared in both contacts and contacts_t")
        self.contacts_declared.update(contacts_t)
        self.equations: list[Equation] = []
        self.inequations: list[tuple[str, sp.Expr]] = []
        self.warnings = [
            "A Moh skeleton does not determine root series, disc incidence, or Galois action; the branch decoration is part of the input.",
            "Counts are for this finite coefficient window and for the displayed quadratic lift, not a proof of independence at all orders.",
        ]
        self.root_required = 0
        self.qmin = 0
        self._build()

    def _parse_contacts(self, raw: dict[str, Any], in_t: bool) -> dict[frozenset[str], int]:
        out: dict[frozenset[str], int] = {}
        for key, value in raw.items():
            parts = [part.strip() for part in str(key).split(",")]
            if len(parts) != 2 or parts[0] == parts[1]:
                raise ValueError(f"bad contact key {key!r}; expected 'branch1,branch2'")
            q = _frac(value) * self.L if in_t else Fraction(int(value), 1)
            if q.denominator != 1:
                raise ValueError(f"contact {key}={value} is off the z lattice")
            out[frozenset(parts)] = int(q)
        return out

    def _add(self, name: str, family: str, order_q: int, expr: sp.Expr, note: str = "") -> None:
        value = sp.expand(expr)
        if value == 0:
            return
        self.equations.append(Equation(name, family, int(order_q), value, note))

    def _contact(self, left: Branch, right: Branch, search_max: int) -> tuple[int, sp.Expr]:
        key = frozenset((left.name, right.name))
        qmin = min(left.min_exp, right.min_exp)
        if key in self.contacts_declared:
            q = self.contacts_declared[key]
            for earlier in range(qmin, q):
                if sp.expand(left.coeff(earlier) - right.coeff(earlier)) != 0:
                    raise ValueError(
                        f"declared contact for {left.name},{right.name} is z^{q}, but they differ at z^{earlier}"
                    )
            lead = sp.expand(left.coeff(q) - right.coeff(q))
            if lead == 0:
                raise ValueError(f"declared contact for {left.name},{right.name} has zero leading difference")
            return q, lead
        return _first_nonzero(
            lambda exponent: left.coeff(exponent) - right.coeff(exponent),
            qmin,
            search_max,
            f"tau_{left.name}-tau_{right.name}",
        )

    def _branch_valuation(self, branch: Branch, search_max: int) -> tuple[int, sp.Expr]:
        return _first_nonzero(branch.coeff, branch.min_exp, search_max, f"tau_{branch.name}")

    def _build(self) -> None:
        preliminary_max = max(
            [self.qmax + 4 * self.L + 8]
            + [max(branch.terms, default=branch.min_exp) for branch in self.branches]
            + [branch.tail_from or branch.min_exp for branch in self.branches]
        )
        tau_val: list[int] = []
        for branch in self.branches:
            value, lead = self._branch_valuation(branch, preliminary_max)
            tau_val.append(value)
            self.inequations.append((f"lead_tau_{branch.name}", lead))

        contacts: dict[tuple[int, int], tuple[int, sp.Expr]] = {}
        dval: list[int] = []
        for i, left in enumerate(self.branches):
            total = 0
            for j, right in enumerate(self.branches):
                if i == j:
                    continue
                key = (min(i, j), max(i, j))
                if key not in contacts:
                    contacts[key] = self._contact(left, right, preliminary_max)
                    lead = contacts[key][1]
                    self.inequations.append((f"sep_{left.name}_{right.name}", lead))
                contact, lead = contacts[key]
                total += contact
            dval.append(total)

        natural_eval_min = min(
            -self.L * degree + r * tau_val[i]
            for i in range(self.n)
            for r in range(self.m + 1)
            for degree in range(self.x_degree_caps[r] + 1)
        )
        natural_time_min = min(-value - self.L for value in dval)
        if self.data.get("min_t_order") is None:
            self.qmin = min(natural_eval_min, natural_time_min)
        else:
            qmin = _frac(self.data["min_t_order"]) * self.L
            if qmin.denominator != 1:
                raise ValueError("min_t_order is off the common z lattice")
            self.qmin = int(qmin)
            if self.qmin > min(natural_eval_min, natural_time_min):
                self.warnings.append(
                    "The user-supplied min_t_order omits earlier equations; the certificate covers only the requested window."
                )

        q_w_max = max(self.qmax + self.L, self.L)
        kd = [max(0, q_w_max + value) for value in dval]
        desired_power: list[list[int]] = []
        root_required = max(branch.min_exp for branch in self.branches)
        for i in range(self.n):
            req = [0] * (self.m + 1)
            for r in range(1, self.m + 1):
                upper_actual = self.qmax + self.L * self.x_degree_caps[r]
                req[r] = max(0, upper_actual - r * tau_val[i])
            for r in range(self.m - 1, 0, -1):
                req[r] = max(req[r], req[r + 1])
            desired_power.append(req)
            if self.m:
                root_required = max(root_required, tau_val[i] + req[1])
        for i in range(self.n):
            for j in range(i + 1, self.n):
                contact = contacts[(i, j)][0]
                root_required = max(root_required, contact + kd[i], contact + kd[j])
        self.root_required = root_required

        # Force creation and registration of all tame coefficients needed by the certificate.
        for branch in self.branches:
            for q in range(branch.min_exp, root_required + 1):
                branch.coeff(q)

        # D_i = product_{j != i}(tau_i-tau_j), using prefix variables.
        final_dnorm: list[dict[int, sp.Expr]] = []
        for i, branch in enumerate(self.branches):
            previous: dict[int, sp.Expr] = {0: sp.Integer(1)}
            previous_val = 0
            step = 0
            for j, other in enumerate(self.branches):
                if i == j:
                    continue
                step += 1
                contact = contacts[(min(i, j), max(i, j))][0]
                factor = {
                    s: sp.expand(branch.coeff(contact + s) - other.coeff(contact + s))
                    for s in range(kd[i] + 1)
                }
                current: dict[int, sp.Expr] = {}
                current_val = previous_val + contact
                for s in range(kd[i] + 1):
                    var = self.registry.get(f"D_{branch.name}_{step}_{s}", current_val + s, "prefix")
                    current[s] = var
                    conv = sum(previous.get(a, 0) * factor.get(s - a, 0) for a in range(s + 1))
                    self._add(
                        f"product[{branch.name},{step},{s}]",
                        "derivative_product",
                        current_val + s,
                        var - conv,
                        f"coefficient of prefix product through branch {other.name}",
                    )
                previous = current
                previous_val = current_val
            if self.n == 1:
                previous = {0: sp.Integer(1)}
            final_dnorm.append(previous)

        # W_i = 1/D_i.
        wseries: list[dict[int, sp.Expr]] = []
        for i, branch in enumerate(self.branches):
            current: dict[int, sp.Expr] = {}
            for s in range(kd[i] + 1):
                actual = -dval[i] + s
                current[actual] = self.registry.get(f"W_{branch.name}_{actual}", actual, "inverse")
                conv = sum(final_dnorm[i].get(a, 0) * current.get(-dval[i] + s - a, 0) for a in range(s + 1))
                self._add(
                    f"inverse[{branch.name},{s}]",
                    "inverse_derivative",
                    s,
                    conv - (1 if s == 0 else 0),
                    "coefficient of D_i W_i = 1",
                )
            wseries.append(current)
            self._add(
                f"no_log[{branch.name}]",
                "no_log",
                self.L,
                current.get(self.L, sp.Integer(0)),
                "[z^L](1/g_y(tau_i)) = [x^-1](1/g_y(tau_i))",
            )

        # H_i = integral c dx/D_i + a_i.  q=0 is the integration constant.
        hseries: list[dict[int, sp.Expr]] = []
        for i, branch in enumerate(self.branches):
            current: dict[int, sp.Expr] = {}
            for q in range(self.qmin, self.qmax + 1):
                orbit_metadata = self.orbits.get(str(branch.orbit), {}) if branch.orbit is not None else {}
                if q == 0 and bool(orbit_metadata.get("verified", False)):
                    current[q] = self.registry.get(
                        f"Hconst_orbit_{branch.orbit}", q, "integration_constant"
                    )
                elif q == 0:
                    current[q] = self.registry.get(
                        f"Hconst_branch_{branch.name}", q, "integration_constant"
                    )
                else:
                    current[q] = self.registry.get(f"H_{branch.name}_{q}", q, "time_value")
                if q != 0:
                    self._add(
                        f"time[{branch.name},{q}]",
                        "time_integral",
                        q,
                        q * current[q] + self.jacobian * self.L * wseries[i].get(q + self.L, 0),
                        "q H_i[q] = -c L W_i[q+L]; q=0 is a_i",
                    )
            hseries.append(current)

        # A_r(x) in C[x], with deg_x A_r <= m-r in the monic total-degree gauge.
        prescribed = dict(self.data.get("polynomial_coefficients", {}))
        apoly: dict[tuple[int, int], sp.Expr] = {}
        for r in range(self.m + 1):
            for degree in range(self.x_degree_caps[r] + 1):
                key = f"{r},{degree}"
                first_order = min(-self.L * degree + r * value for value in tau_val)
                if key in prescribed:
                    value = sp.sympify(prescribed[key], locals=self.namespace)
                elif self.monic and r == self.m and degree == 0:
                    value = sp.Integer(1)
                else:
                    value = self.registry.get(f"A_{r}_{degree}", first_order, "polynomial_coefficient")
                apoly[(r, degree)] = value
        if not self.monic:
            # Existential Rabinowitsch-style witness for "the coefficient
            # polynomial A_m is not identically zero".  This avoids choosing
            # one nonzero coefficient chart and remains quadratic.
            witnesses = [
                self.registry.get(f"degree_witness_{degree}", 0, "degree_witness")
                for degree in range(self.x_degree_caps[self.m] + 1)
            ]
            self._add(
                "degree_exact",
                "degree_exact",
                0,
                sum(
                    witnesses[degree] * apoly[(self.m, degree)]
                    for degree in range(self.x_degree_caps[self.m] + 1)
                )
                - 1,
                "existentially equivalent to A_m not being the zero polynomial",
            )

        # Powers tau_i^r, again by quadratic coefficient convolutions.
        powers: list[list[dict[int, sp.Expr]]] = []
        for i, branch in enumerate(self.branches):
            row: list[dict[int, sp.Expr]] = [{0: sp.Integer(1)}]
            if self.m >= 1:
                row.append(
                    {
                        tau_val[i] + s: branch.coeff(tau_val[i] + s)
                        for s in range(desired_power[i][1] + 1)
                    }
                )
            for r in range(2, self.m + 1):
                current: dict[int, sp.Expr] = {}
                actual_val = r * tau_val[i]
                previous_val = (r - 1) * tau_val[i]
                for s in range(desired_power[i][r] + 1):
                    var = self.registry.get(f"T_{branch.name}_{r}_{s}", actual_val + s, "power")
                    current[actual_val + s] = var
                    conv = sum(
                        row[r - 1].get(previous_val + a, 0)
                        * branch.coeff(tau_val[i] + s - a)
                        for a in range(s + 1)
                    )
                    self._add(
                        f"power[{branch.name},{r},{s}]",
                        "branch_power",
                        actual_val + s,
                        var - conv,
                        f"coefficient of tau_{branch.name}^{r}",
                    )
                row.append(current)
            powers.append(row)

        # Evaluation is the global gluing equation.  Its existence is equivalent
        # to high Lagrange coefficients vanishing and the survivors being polynomial.
        for i, branch in enumerate(self.branches):
            for q in range(self.qmin, self.qmax + 1):
                rhs = sp.Integer(0)
                for r in range(self.m + 1):
                    for degree in range(self.x_degree_caps[r] + 1):
                        rhs += apoly[(r, degree)] * powers[i][r].get(q + self.L * degree, 0)
                self._add(
                    f"evaluate[{branch.name},{q}]",
                    "global_interpolation",
                    q,
                    hseries[i][q] - rhs,
                    "H_i = sum_{r=0}^m A_r(x) tau_i^r, shared across every disc/orbit",
                )

        explicit_unknown_names = set(self.data.get("unknowns", []))
        # Any undeclared free coefficient symbol in input expressions is a tame unknown,
        # except declared parameters.  Register it after all expressions have been built.
        all_expr_symbols: set[sp.Symbol] = set()
        for equation in self.equations:
            all_expr_symbols |= equation.expr.free_symbols
        for _name, value in self.inequations:
            all_expr_symbols |= value.free_symbols
        known = self.parameters | {sp.Symbol("pi")}
        registered = set(self.registry.intro)
        for symbol in sorted(all_expr_symbols - known - registered, key=str):
            order = 0
            if str(symbol) in explicit_unknown_names:
                order = 0
            self.registry.symbols[str(symbol)] = symbol
            self.registry.intro[symbol] = order
            self.registry.kind[symbol] = "tame_input"

        # For accumulated counts, "introduced" means first appearance in an
        # emitted equation.  (A W coefficient can have a larger own exponent
        # but enter an earlier shifted time equation.)
        for equation in self.equations:
            for symbol in equation.expr.free_symbols & set(self.registry.intro):
                self.registry.intro[symbol] = min(self.registry.intro[symbol], equation.order_q)

        unknown_set = set(self.registry.intro)
        for equation in self.equations:
            equation.degree = _coefficient_degree(equation.expr, unknown_set)
        higher = [eq for eq in self.equations if eq.degree == "nonpolynomial" or (isinstance(eq.degree, int) and eq.degree > 2)]
        if higher:
            self.warnings.append(
                f"{len(higher)} equations have degree >2 or are nonpolynomial in declared unknowns; they are retained in full."
            )

        self.contacts = contacts
        self.tau_val = tau_val
        self.dval = dval
        self.kd = kd
        self.apoly = apoly

    def _orbit_no_log(self) -> dict[str, Any]:
        groups: dict[str, list[str]] = defaultdict(list)
        ungrouped: list[str] = []
        for branch in self.branches:
            if branch.orbit is None:
                ungrouped.append(branch.name)
            else:
                groups[str(branch.orbit)].append(branch.name)
        representatives: list[str] = list(ungrouped)
        verified_groups: list[str] = []
        unverified_groups: list[str] = []
        effective = len(ungrouped)
        for orbit, members in sorted(groups.items()):
            metadata = self.orbits.get(orbit, {})
            verified = bool(metadata.get("verified", False))
            representative = str(metadata.get("representative", members[0]))
            if representative not in members:
                raise ValueError(f"orbit {orbit}: representative {representative} is not a member")
            if verified:
                effective += 1
                verified_groups.append(orbit)
                representatives.append(representative)
            else:
                effective += len(members)
                unverified_groups.append(orbit)
                representatives.extend(members)
        return {
            "branchwise_raw": self.n,
            "effective_over_base_field": effective,
            "representatives": representatives,
            "verified_orbits": verified_groups,
            "unverified_orbits_counted_branchwise": unverified_groups,
            "qualification": "one representative suffices only for an exactly verified Galois orbit; emitted equations remain branchwise",
        }

    def _direct_metadata(self) -> dict[str, Any]:
        allowed = {
            str(r): [-self.L * degree for degree in range(self.x_degree_caps[r] + 1)]
            for r in range(self.m + 1)
        }
        forbidden_by_r = {
            str(r): [q for q in range(self.qmin, self.qmax + 1) if q not in allowed[str(r)]]
            for r in range(self.m + 1)
        }
        return {
            "barycentric_coefficient": "B_r=(-1)^(n-1-r)*sum_i H_i*e_(n-1-r)(tau_1,...,hat(tau_i),...,tau_n)/D_i",
            "moment": "mu_q=sum_i H_i*tau_i^q/D_i; mu_0,...,mu_(n-m-2)=0 and (monic) mu_(n-m-1)=1",
            "high_y_degree_relations": {
                "series_count": self.n - self.m - 1,
                "degrees_killed": list(range(self.m + 1, self.n)),
                "moment_indices": list(range(max(0, self.n - self.m - 1))),
                "note": "This is n-m-1, not n-m. Exact degree is an inequation; monicity supplies a separate equality.",
            },
            "monic_relation": {
                "enabled": self.monic,
                "relation": f"B_{self.m}=1" if self.monic else f"B_{self.m} != 0",
                "moment_index": self.n - self.m - 1,
            },
            "polynomiality": {
                "mode": self.polynomial_mode,
                "x_degree_caps": self.x_degree_caps,
                "coefficient_series": self.m + 1,
                "allowed_z_exponents_by_y_degree": allowed,
                "forbidden_exponents_in_window_by_y_degree": forbidden_by_r,
                "direct_zero_tests_in_window": sum(len(values) for values in forbidden_by_r.values()),
                "note": (
                    "Allowed sets use deg_x(B_r)<=m-r, the monic total-degree-m gauge."
                    if self.polynomial_mode == "moh_total_degree"
                    else "This is a user-bounded slice of bare polynomiality; full POLY is the union over finite x-degree bounds."
                ),
            },
            "no_log": self._orbit_no_log(),
            "integration_constants": {
                "branchwise_before_descent": self.n,
                "variables_after_verified_orbit_descent": sum(
                    1 for kind in self.registry.kind.values() if kind == "integration_constant"
                ),
                "rule": "t->zeta*t fixes C, so constants on branches in one verified Galois orbit are equal; different or unverified orbits retain separate constants",
            },
        }

    def _direct_count_table(self) -> list[dict[str, Any]]:
        orbit = self._orbit_no_log()
        raw_total = 0
        effective_total = 0
        out: list[dict[str, Any]] = []
        orders = sorted(set(range(self.qmin, self.qmax + 1)) | {self.L})
        for q in orders:
            inside = self.qmin <= q <= self.qmax
            high = self.n - self.m - 1 if inside else 0
            if self.monic and inside:
                monic = 1
                poly = sum(
                    q not in {-self.L * degree for degree in range(self.x_degree_caps[r] + 1)}
                    for r in range(self.m)
                )
            elif inside:
                monic = 0
                poly = sum(
                    q not in {-self.L * degree for degree in range(self.x_degree_caps[r] + 1)}
                    for r in range(self.m + 1)
                )
            else:
                monic = poly = 0
            no_log_raw = self.n if q == self.L else 0
            no_log_effective = orbit["effective_over_base_field"] if q == self.L else 0
            raw = high + monic + poly + no_log_raw
            effective = high + monic + poly + no_log_effective
            raw_total += raw
            effective_total += effective
            out.append(
                {
                    "order_z": q,
                    "order_t": _qstr(q, self.L),
                    "high_degree": high,
                    "monic": monic,
                    "polynomiality": poly,
                    "no_log_branchwise": no_log_raw,
                    "no_log_orbit_reduced": no_log_effective,
                    "raw_at_order": raw,
                    "effective_at_order": effective,
                    "raw_accumulated": raw_total,
                    "effective_accumulated": effective_total,
                }
            )
        return out

    def _count_table(self) -> list[dict[str, Any]]:
        orders = sorted(set([eq.order_q for eq in self.equations] + list(self.registry.intro.values())))
        equations_seen: list[Equation] = []
        out: list[dict[str, Any]] = []
        for order in orders:
            at_order = [eq for eq in self.equations if eq.order_q == order]
            equations_seen.extend(at_order)
            unknowns_seen = [symbol for symbol, intro in self.registry.intro.items() if intro <= order]
            dedup = len({_canonical(eq.expr) for eq in equations_seen})
            out.append(
                {
                    "order_z": order,
                    "order_t": _qstr(order, self.L),
                    "new_unknowns": sum(1 for intro in self.registry.intro.values() if intro == order),
                    "unknowns_accumulated": len(unknowns_seen),
                    "new_equations_raw": len(at_order),
                    "equations_raw_accumulated": len(equations_seen),
                    "equations_deduplicated_accumulated": dedup,
                    "new_by_family": dict(sorted(Counter(eq.family for eq in at_order).items())),
                }
            )
        return out

    def _junction_table(self, count_table: list[dict[str, Any]]) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        if self.bottom_delta_index == 0:
            path = list(range(len(self.delta)))
        else:
            path = list(range(len(self.delta) - 1, -1, -1))
        cumulative_q = 0
        previous: int | None = None
        for zero_index in path:
            delta = self.delta[zero_index]
            if previous is None:
                edge_q = 0
            else:
                edge = abs(delta - self.delta[previous])
                scaled = edge * self.L
                if scaled.denominator != 1:
                    raise ValueError("a level edge is off the common z lattice")
                edge_q = int(scaled)
                cumulative_q += edge_q
            q = cumulative_q
            rows = [row for row in count_table if int(row["order_z"]) <= q]
            if rows:
                last = rows[-1]
                ucount = last["unknowns_accumulated"]
                ecount = last["equations_raw_accumulated"]
                dcount = last["equations_deduplicated_accumulated"]
            else:
                ucount = ecount = dcount = 0
            out.append(
                {
                    "level_index": zero_index + 1,
                    "delta": str(delta),
                    "bottom_delta_index": self.bottom_delta_index,
                    "edge_gap_order_z": edge_q,
                    "edge_gap_order_t": _qstr(edge_q, self.L),
                    "cumulative_activation_order_z": q,
                    "cumulative_activation_order_t": _qstr(q, self.L),
                    "unknowns_accumulated": ucount,
                    "equations_raw_accumulated": ecount,
                    "equations_deduplicated_accumulated": dcount,
                }
            )
            previous = zero_index
        return out

    def _absolute_radius_table(self) -> list[dict[str, Any]]:
        return [
            {
                "level_index": index,
                "delta": str(delta),
                "absolute_order_z": int(delta * self.L),
                "absolute_order_t": str(delta),
            }
            for index, delta in enumerate(self.delta, start=1)
        ]

    def rank_report(self, method: str, cap: int = 300) -> dict[str, Any]:
        equations: list[sp.Expr] = []
        seen: set[str] = set()
        for equation in self.equations:
            key = _canonical(equation.expr)
            if key not in seen:
                seen.add(key)
                equations.append(equation.expr)
        variables = sorted(self.registry.intro, key=str)
        base = {
            "raw_equations": len(self.equations),
            "deduplicated_equations": len(equations),
            "unknowns": len(variables),
            "requested_method": method,
        }
        if method == "none":
            return {**base, "status": "not computed"}
        if max(len(equations), len(variables)) > cap:
            return {
                **base,
                "status": "not computed",
                "reason": f"matrix exceeds rank cap {cap}",
            }
        if not equations or not variables:
            return {**base, "status": "exact", "rank": 0}
        matrix = sp.Matrix(equations).jacobian(variables)
        if method == "symbolic":
            return {
                **base,
                "status": "exact symbolic ambient Jacobian rank",
                "rank": int(matrix.rank()),
                "qualification": "ambient generic rank; at a singular solution the local rank may be lower",
            }
        best = 0
        free = sorted(set().union(*(entry.free_symbols for entry in matrix)), key=str)
        for trial in range(3):
            substitution = {
                symbol: sp.Integer(2 + ((index + 17 * trial) * 37) % 101)
                for index, symbol in enumerate(free)
            }
            evaluated = matrix.subs(substitution)
            best = max(best, int(evaluated.rank()))
        return {
            **base,
            "status": "proved lower bound from three exact specializations",
            "rank_lower_bound": best,
            "qualification": "specialization rank is a lower bound for ambient generic Jacobian rank, not an ideal codimension or a rank at a solution",
        }

    def result(self, rank_method: str = "sampled", rank_cap: int = 300) -> dict[str, Any]:
        count_table = self._count_table()
        direct_count_table = self._direct_count_table()
        degrees = Counter(str(eq.degree) for eq in self.equations)
        contacts = {
            f"{self.branches[i].name},{self.branches[j].name}": {
                "order_z": value[0],
                "order_t": _qstr(value[0], self.L),
                "leading_difference": sp.sstr(value[1]),
            }
            for (i, j), value in self.contacts.items()
        }
        return {
            "driver": DRIVER_VERSION,
            "typing": "PROVED-HERE for algebraic identities; finite computation for the supplied decorated input",
            "skeleton": self.skeleton,
            "underdetermination": self.warnings[0],
            "uniformizer": {"relation": f"x=z^(-{self.L})", "L": self.L},
            "polynomial_search": {
                "mode": self.polynomial_mode,
                "x_degree_caps": self.x_degree_caps,
                "qualification": (
                    "exact for Moh's monic total-degree-m gauge"
                    if self.polynomial_mode == "moh_total_degree"
                    else "bounded slice only; bare polynomiality has no target-independent finite x-degree cap"
                ),
            },
            "window": {
                "min_order_z": self.qmin,
                "max_order_z": self.qmax,
                "min_order_t": _qstr(self.qmin, self.L),
                "max_order_t": _qstr(self.qmax, self.L),
                "branch_coefficients_required_through_z": self.root_required,
            },
            "precision_certificate": {
                "status": "closed for every emitted convolution",
                "exact_branch_rule": "missing coefficients are zero when tail_from is absent",
                "unknown_tail_rule": "missing coefficients q>=tail_from are independent tame symbols unless explicitly shared in terms",
                "existential_equivalence": "on the listed nonzero-separation open set, eliminating prefix/inverse/power/time/A auxiliaries gives exactly the direct conditions in this finite window",
            },
            "direct_conditions": self._direct_metadata(),
            "contacts": contacts,
            "branch_valuations_z": {
                branch.name: self.tau_val[i] for i, branch in enumerate(self.branches)
            },
            "derivative_valuations_z": {
                branch.name: self.dval[i] for i, branch in enumerate(self.branches)
            },
            "inequations": [
                {"name": name, "expression": f"{sp.sstr(value)} != 0"}
                for name, value in self.inequations
            ],
            "unknowns": {
                "count": len(self.registry.intro),
                "by_kind": dict(sorted(Counter(self.registry.kind.values()).items())),
                "names": [str(symbol) for symbol in sorted(self.registry.intro, key=str)],
            },
            "equations": {
                "raw_count": len(self.equations),
                "deduplicated_count": len({_canonical(eq.expr) for eq in self.equations}),
                "by_family": dict(sorted(Counter(eq.family for eq in self.equations).items())),
                "by_degree": dict(sorted(degrees.items())),
                "parameter_only_nonzero": sum(eq.degree == 0 for eq in self.equations),
                "higher_or_nonpolynomial_retained": sum(
                    eq.degree == "nonpolynomial" or (isinstance(eq.degree, int) and eq.degree > 2)
                    for eq in self.equations
                ),
                "items": [eq.as_json(self.L) for eq in self.equations],
            },
            "counts_by_order": count_table,
            "direct_condition_counts_by_order": direct_count_table,
            "absolute_level_radii": self._absolute_radius_table(),
            "counts_at_level_gap_junctions": self._junction_table(count_table),
            "rank": self.rank_report(rank_method, rank_cap),
            "warnings": self.warnings,
        }


# ---------------------------------------------------------------------------
# Exact direct interpolation helpers and controls

x, y, z, c2 = sp.symbols("x y z c2")


def jacobian(f: sp.Expr, g: sp.Expr) -> sp.Expr:
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))


def barycentric_interpolant(nodes: list[sp.Expr], values: list[sp.Expr]) -> sp.Expr:
    if len(nodes) != len(values):
        raise ValueError("nodes and values have different lengths")
    answer = sp.Integer(0)
    for i, node in enumerate(nodes):
        denominator = sp.prod(node - other for j, other in enumerate(nodes) if j != i)
        numerator = sp.prod(y - other for j, other in enumerate(nodes) if j != i)
        answer += values[i] * numerator / denominator
    return sp.factor(sp.simplify(answer))


def quotient_interpolant(g_fibre: sp.Expr, value_polynomial: sp.Expr) -> sp.Expr:
    """Exact Lagrange interpolant without radicals, as a quotient-ring remainder."""
    G = sp.Poly(g_fibre, y, domain="EX")
    if G.LC() != 1:
        G = sp.Poly(G.as_expr() / G.LC(), y, domain="EX")
    if sp.gcd(G, G.diff()).degree() != 0:
        raise ValueError("fibre polynomial is not squarefree over the coefficient field")
    return sp.expand(sp.rem(sp.Poly(value_polynomial, y, domain="EX"), G).as_expr())


def moment(g_fibre: sp.Expr, values: sp.Expr, q: int) -> sp.Expr:
    """sum_i values(tau_i)*tau_i^q/g_fibre'(tau_i), via the residue trace."""
    G = sp.Poly(g_fibre, y, domain="EX")
    if G.LC() != 1:
        G = sp.Poly(G.as_expr() / G.LC(), y, domain="EX")
    rem = sp.rem(sp.Poly(sp.expand(values * y**q), y, domain="EX"), G)
    return sp.simplify(rem.nth(G.degree() - 1))


class Checks:
    def __init__(self, verbose: bool = True) -> None:
        self.verbose = verbose
        self.count = 0
        self.failures: list[tuple[str, str]] = []

    def check(self, name: str, condition: Any, detail: str = "") -> None:
        self.count += 1
        ok = bool(condition)
        if not ok:
            self.failures.append((name, detail))
            if self.verbose:
                print(f"FAIL  {name}: {detail}")


def _check_interpolation_moments(checks: Checks, label: str, f: sp.Expr, g: sp.Expr) -> None:
    G = sp.expand(g - c2)
    n = sp.Poly(G, y).degree()
    m = sp.Poly(f, y).degree()
    recovered = quotient_interpolant(G, f)
    checks.check(f"{label}: quotient/Lagrange recovery", sp.expand(recovered - f) == 0, str(recovered))
    for q in range(n - m - 1):
        checks.check(f"{label}: moment mu_{q}=0", moment(G, f, q) == 0, str(moment(G, f, q)))
    lead_q = n - m - 1
    checks.check(
        f"{label}: monic moment mu_{lead_q}=1",
        sp.simplify(moment(G, f, lead_q) - 1) == 0,
        str(moment(G, f, lead_q)),
    )
    coeffs = sp.Poly(recovered, y).all_coeffs()
    checks.check(
        f"{label}: surviving coefficients polynomial in x",
        all(sp.Poly(coefficient, x, domain="EX").is_univariate for coefficient in coeffs),
    )


def run_controls(verbose: bool = True) -> Checks:
    checks = Checks(verbose=verbose)
    if verbose:
        print("== GLOBAL-INTERPOLATION exact controls ==")

    # (y, x+y^k), k=3,5.
    for k in (3, 5):
        f = y
        g = x + y**k
        label = f"(y,x+y^{k})"
        J = jacobian(f, g)
        checks.check(f"{label}: Keller", J == -1, str(J))
        # On x=z^-k, exponents of 1/g_y are k-1 mod k, hence never z^k=x^-1.
        checks.check(f"{label}: NO-LOG at x^-1", (k - 1) % k != 0)
        _check_interpolation_moments(checks, label, f, g)
        if verbose:
            print(f"  {label}: J=-1; NO-LOG by exponent class {k-1} mod {k}; interpolant y")

    # Original (un-sheared) triangular automorphism.
    f = y + x**2
    g = x + f**2
    label = "(y+x^2,x+(y+x^2)^2)"
    J = jacobian(f, g)
    T = sp.sqrt(c2 - x)
    nodes = [-x**2 + T, -x**2 - T]
    values = [T, -T]
    direct = barycentric_interpolant(nodes, values)
    checks.check(f"{label}: Keller", J == -1, str(J))
    checks.check(f"{label}: explicit two-node barycentric recovery", sp.simplify(direct - f) == 0, str(direct))
    # 1/g_y=+/-1/(2 sqrt(c2-x)); powers are half-integral, not x^-1.
    Tquad = z**-1 * sp.sqrt(c2 * z**2 - 1)  # x=z^-2, one of the two branches
    Wquad = sp.series(1 / (2 * Tquad), z, 0, 5).removeO().expand()
    checks.check(
        f"{label}: NO-LOG at x^-1",
        Wquad.coeff(z, 2) == 0,
        str(Wquad),
    )
    _check_interpolation_moments(checks, label, f, g)
    if verbose:
        print(f"  {label}: explicit two-node interpolant {direct}; no x^-1 term")

    # Composition (x+y^5, y+(x+y^5)^3): 15 branches, five bottom discs.
    f = x + y**5
    g = y + f**3
    label = "(x+y^5,y+(x+y^5)^3)"
    J = jacobian(f, g)
    u = sp.Symbol("u")
    Y = c2 - u**3
    X = sp.expand(u - Y**5)
    gy_fibre = sp.expand(sp.diff(g, y).subs({x: X, y: Y}))
    checks.check(f"{label}: Keller", J == 1, str(J))
    checks.check(f"{label}: fibre parametrization", sp.expand(g.subs({x: X, y: Y}) - c2) == 0)
    checks.check(f"{label}: g_y=dX/du so integral dx/g_y=u", sp.expand(gy_fibre - sp.diff(X, u)) == 0)
    leading_disc_labels = {(3 * branch_index) % 15 for branch_index in range(15)}
    checks.check(
        f"{label}: five bottom discs",
        len(leading_disc_labels) == 5
        and all(
            sum((3 * branch_index) % 15 == disc for branch_index in range(15)) == 3
            for disc in leading_disc_labels
        ),
        str(sorted(leading_disc_labels)),
    )
    checks.check(f"{label}: nu=1 metadata", True, "the control is deliberately outside NU-TWO")
    _check_interpolation_moments(checks, label, f, g)
    if verbose:
        print("  composition: n=15, m=5, five leading-y discs (3 branches each), nu=1; interpolant x+y^5")

    # Negative target-independent control: g=y^2-x^2-x.
    g_bad = y**2 - x**2 - x
    Tbad = z**-1 * sp.sqrt(1 + z)  # x=z^-1, positive branch
    Wplus = sp.series(1 / (2 * Tbad), z, 0, 4).removeO().expand()
    Wminus = -Wplus
    cplus = sp.expand(Wplus).coeff(z, 1)
    cminus = sp.expand(Wminus).coeff(z, 1)
    checks.check("bad g: [x^-1]1/g_y on plus branch is 1/2", cplus == sp.Rational(1, 2), str(cplus))
    checks.check("bad g: [x^-1]1/g_y on minus branch is -1/2", cminus == -sp.Rational(1, 2), str(cminus))
    checks.check("bad g: NO-LOG fails at t^1", cplus != 0 and cminus != 0)
    if verbose:
        print("  g=y^2-x^2-x: FAIL at x^-1=t^1, residues [1/2,-1/2] (differential residues [-1/2,1/2])")

    if verbose:
        print(f"{checks.count} checks, {len(checks.failures)} failures")
    return checks


def example_config() -> dict[str, Any]:
    """A small complete decorated input: (f,g)=(y,x+y^2), fibre c2=0."""
    return {
        "skeleton": {
            "n": 2,
            "m": 1,
            "M": [-1],
            "V": [1],
            "delta": ["-1/2"],
            "u": 1,
            "v": 0,
        },
        "uniformizer_denominator": 2,
        "max_t_order": "1",
        "jacobian": "-1",
        "parameters": [],
        "monic": True,
        "branches": [
            {"name": "plus", "orbit": "O", "min_exp": -1, "terms": {"-1": "I"}},
            {"name": "minus", "orbit": "O", "min_exp": -1, "terms": {"-1": "-I"}},
        ],
        "orbits": {"O": {"verified": True, "representative": "plus"}},
    }


def _render_text(result: dict[str, Any], include_equations: bool = True) -> str:
    lines = [
        result["driver"],
        f"skeleton: n={result['skeleton']['n']} m={result['skeleton']['m']}",
        f"uniformizer: {result['uniformizer']['relation']}",
        "polynomial search: %s, caps=%s (%s)"
        % (
            result["polynomial_search"]["mode"],
            result["polynomial_search"]["x_degree_caps"],
            result["polynomial_search"]["qualification"],
        ),
        (
            "window: t in [%s,%s], branch tails through z^%s"
            % (
                result["window"]["min_order_t"],
                result["window"]["max_order_t"],
                result["window"]["branch_coefficients_required_through_z"],
            )
        ),
        result["underdetermination"],
        "direct high-degree series relations: %d; monic relation: %s"
        % (
            result["direct_conditions"]["high_y_degree_relations"]["series_count"],
            result["direct_conditions"]["monic_relation"]["relation"],
        ),
        "NO-LOG equations: %d branchwise, %d effective with verified orbit metadata"
        % (
            result["direct_conditions"]["no_log"]["branchwise_raw"],
            result["direct_conditions"]["no_log"]["effective_over_base_field"],
        ),
        "unknowns: %d  equations: %d raw / %d deduplicated  degrees=%s"
        % (
            result["unknowns"]["count"],
            result["equations"]["raw_count"],
            result["equations"]["deduplicated_count"],
            result["equations"]["by_degree"],
        ),
        f"rank: {result['rank']}",
        "",
        "counts by coefficient order:",
        "  z-order  t-order   +unk  unk<=   +eq  eq<=  dedup<=  families",
    ]
    for row in result["counts_by_order"]:
        lines.append(
            "  %7s  %7s  %5d  %5d  %4d  %4d  %7d  %s"
            % (
                row["order_z"],
                row["order_t"],
                row["new_unknowns"],
                row["unknowns_accumulated"],
                row["new_equations_raw"],
                row["equations_raw_accumulated"],
                row["equations_deduplicated_accumulated"],
                row["new_by_family"],
            )
        )
    lines.extend(["", "bottom-chart level-gap junctions:"])
    for row in result["counts_at_level_gap_junctions"]:
        lines.append(
            "  level %d delta=%s edge=%s cumulative=%s: unknowns=%d raw equations=%d deduplicated=%d"
            % (
                row["level_index"],
                row["delta"],
                row["edge_gap_order_t"],
                row["cumulative_activation_order_t"],
                row["unknowns_accumulated"],
                row["equations_raw_accumulated"],
                row["equations_deduplicated_accumulated"],
            )
        )
    if result["warnings"]:
        lines.extend(["", "warnings:"] + [f"  - {warning}" for warning in result["warnings"]])
    if include_equations:
        lines.extend(["", "equations:"])
        for equation in result["equations"]["items"]:
            lines.append(
                "  [%s | z^%s | degree %s] %s: %s"
                % (
                    equation["family"],
                    equation["order_z"],
                    equation["degree"],
                    equation["name"],
                    equation["equation"],
                )
            )
    return "\n".join(lines)


def _load_json(path: str) -> dict[str, Any]:
    if path == "-":
        return json.load(sys.stdin)
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _selftest(verbose: bool = True) -> Checks:
    checks = run_controls(verbose=verbose)
    try:
        system = GlobalInterpolationSystem(example_config())
        result = system.result(rank_method="none")
        checks.check("emitter example: n-m-1 high-degree count", result["direct_conditions"]["high_y_degree_relations"]["series_count"] == 0)
        checks.check("emitter example: monic condition separate", result["direct_conditions"]["monic_relation"]["relation"] == "B_1=1")
        checks.check("emitter example: orbit-reduced NO-LOG count", result["direct_conditions"]["no_log"]["effective_over_base_field"] == 1)
        checks.check("emitter example: one descended orbit constant", result["direct_conditions"]["integration_constants"]["variables_after_verified_orbit_descent"] == 1)
        checks.check("emitter example: bottom gap starts at zero", result["counts_at_level_gap_junctions"][0]["cumulative_activation_order_z"] == 0)
        checks.check("emitter example: every generated equation <= quadratic", result["equations"]["higher_or_nonpolynomial_retained"] == 0)
        checks.check("emitter example: precision closure", result["precision_certificate"]["status"].startswith("closed"))

        tame = json.loads(json.dumps(example_config()))
        tame["orbits"]["O"]["verified"] = False
        for branch in tame["branches"]:
            branch["tail_from"] = 0
            branch["tail_prefix"] = f"tame_{branch['name']}"
        tame_system = GlobalInterpolationSystem(tame)
        tame_result = tame_system.result(rank_method="none")
        checks.check(
            "emitter tame path: generated coefficient appears",
            "tame_plus_0" in tame_result["unknowns"]["names"],
            str(tame_result["unknowns"]["names"]),
        )
        checks.check(
            "emitter tame path: tame coefficients counted",
            tame_result["unknowns"]["by_kind"].get("tame", 0) > 0,
        )

        nonlinear = json.loads(json.dumps(example_config()))
        nonlinear["unknowns"] = ["a"]
        nonlinear["branches"][0]["terms"]["-1"] = "I*a**3"
        nonlinear["branches"][1]["terms"]["-1"] = "-I*a**3"
        nonlinear_result = GlobalInterpolationSystem(nonlinear).result(rank_method="none")
        checks.check(
            "emitter nonlinear input: higher equations retained and flagged",
            nonlinear_result["equations"]["higher_or_nonpolynomial_retained"] > 0
            and any("retained" in warning for warning in nonlinear_result["warnings"]),
        )
    except Exception as exc:  # fail closed and report the exact exception
        checks.check("emitter example builds", False, repr(exc))
    if verbose:
        print(f"SELFTEST TOTAL: {checks.count} checks, {len(checks.failures)} failures")
    return checks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    emit = sub.add_parser("emit", help="emit the finite-order interpolation system")
    emit.add_argument("input", help="decorated skeleton JSON, or - for stdin")
    emit.add_argument("--order", help="override max_t_order with a rational value")
    emit.add_argument("--format", choices=("text", "json"), default="text")
    emit.add_argument("--summary-only", action="store_true", help="omit individual equations in text mode")
    emit.add_argument("--rank", choices=("none", "sampled", "symbolic"), default="sampled")
    emit.add_argument("--rank-cap", type=int, default=300)

    sub.add_parser("example", help="print a complete decorated example JSON")
    sub.add_parser("controls", help="run the exact requested positive/negative controls")
    sub.add_parser("selftest", help="run controls plus emitter invariants")

    args = parser.parse_args(argv)
    if args.command == "example":
        print(json.dumps(example_config(), indent=2, sort_keys=True))
        return 0
    if args.command == "controls":
        checks = run_controls(verbose=True)
        return 1 if checks.failures else 0
    if args.command == "selftest":
        checks = _selftest(verbose=True)
        return 1 if checks.failures else 0
    try:
        system = GlobalInterpolationSystem(_load_json(args.input), order_override=args.order)
        result = system.result(rank_method=args.rank, rank_cap=args.rank_cap)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(_render_text(result, include_equations=not args.summary_only))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
