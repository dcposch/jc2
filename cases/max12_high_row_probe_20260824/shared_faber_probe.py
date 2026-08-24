#!/usr/bin/env python3
"""Shared exact high-row/Faber probe for (8,12) and (9,12).

The coefficient ring is a sparse multivariate polynomial ring over Q,
implemented with the standard library.  The probe reconstructs the Faber
solution of every high Jacobian row, verifies those rows by differentiating
with respect to every live coefficient of f, and then computes the exact
constant-character/target-quotient widths of each Kummer route.

It does not analyze the lower Laurent fibres or claim either frontier empty.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_HASHES = {
    "xmodel/as109-partial-y-history-stop-20260824.md":
        "6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe",
    "xmodel/as109-partial-y-history-review-grok-20260824.md":
        "f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd",
    "xmodel/max12-partial-y-kummer-preflight-20260824.md":
        "30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07",
    "cases/max12_partial_y_preflight_20260824/FREEZE.sha256":
        "59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558",
}


class ProbeFailure(RuntimeError):
    pass


# A coefficient polynomial is {exponent tuple: rational coefficient}.
Coeff = dict[tuple[int, ...], Fraction]
# A z-polynomial/Laurent polynomial is {z exponent: coefficient polynomial}.
ZPoly = dict[int, Coeff]


def cclean(value: Coeff) -> Coeff:
    return {mon: coeff for mon, coeff in value.items() if coeff}


def cadd(left: Coeff, right: Coeff) -> Coeff:
    out = dict(left)
    for mon, coeff in right.items():
        out[mon] = out.get(mon, Fraction(0)) + coeff
    return cclean(out)


def cscale(scalar: Fraction | int, value: Coeff) -> Coeff:
    scalar = Fraction(scalar)
    return cclean({mon: scalar * coeff for mon, coeff in value.items()})


def cmul(left: Coeff, right: Coeff) -> Coeff:
    out: Coeff = {}
    for lmon, lcoeff in left.items():
        for rmon, rcoeff in right.items():
            mon = tuple(a + b for a, b in zip(lmon, rmon))
            out[mon] = out.get(mon, Fraction(0)) + lcoeff * rcoeff
    return cclean(out)


def cpartial(value: Coeff, variable: int) -> Coeff:
    out: Coeff = {}
    for mon, coeff in value.items():
        exponent = mon[variable]
        if not exponent:
            continue
        new_mon = list(mon)
        new_mon[variable] -= 1
        key = tuple(new_mon)
        out[key] = out.get(key, Fraction(0)) + exponent * coeff
    return cclean(out)


def cspecialize_zero(value: Coeff, zero_variables: set[int]) -> Coeff:
    return cclean({mon: coeff for mon, coeff in value.items()
                   if all(mon[index] == 0 for index in zero_variables)})


def cevaluate(value: Coeff, point: list[Fraction]) -> Fraction:
    out = Fraction(0)
    for mon, coeff in value.items():
        term = coeff
        for exponent, coordinate in zip(mon, point):
            term *= coordinate ** exponent
        out += term
    return out


def zclean(value: ZPoly) -> ZPoly:
    return {exponent: cclean(coeff) for exponent, coeff in value.items() if cclean(coeff)}


def zadd(left: ZPoly, right: ZPoly) -> ZPoly:
    out = {exponent: dict(coeff) for exponent, coeff in left.items()}
    for exponent, coeff in right.items():
        out[exponent] = cadd(out.get(exponent, {}), coeff)
    return zclean(out)


def zscale(scalar: Fraction | int, value: ZPoly) -> ZPoly:
    return zclean({exponent: cscale(scalar, coeff) for exponent, coeff in value.items()})


def zmul(left: ZPoly, right: ZPoly) -> ZPoly:
    out: ZPoly = {}
    for lexp, lcoeff in left.items():
        for rexp, rcoeff in right.items():
            exponent = lexp + rexp
            out[exponent] = cadd(out.get(exponent, {}), cmul(lcoeff, rcoeff))
    return zclean(out)


def zpower(value: ZPoly, exponent: int, one: Coeff) -> ZPoly:
    out: ZPoly = {0: one}
    base = value
    n = exponent
    while n:
        if n & 1:
            out = zmul(out, base)
        base = zmul(base, base)
        n //= 2
    return out


def zderivative(value: ZPoly) -> ZPoly:
    return zclean({exponent - 1: cscale(exponent, coeff)
                   for exponent, coeff in value.items() if exponent})


def zpartial(value: ZPoly, variable: int) -> ZPoly:
    return zclean({exponent: cpartial(coeff, variable)
                   for exponent, coeff in value.items()})


def binomial(q: Fraction, k: int) -> Fraction:
    out = Fraction(1)
    for j in range(k):
        out *= q - j
        out /= j + 1
    return out


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    a = [list(row) for row in rows]
    row = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][column]
        a[row] = [entry / scale for entry in a[row]]
        for i in range(len(a)):
            if i == row or not a[i][column]:
                continue
            factor = a[i][column]
            a[i] = [left - factor * right
                    for left, right in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def zpower_coefficient(zseries: ZPoly, exponent: int, target: int,
                       one: Coeff) -> Coeff:
    """Coefficient of w^target in z(w)^exponent, with exact memoization."""
    memo: dict[tuple[int, int], Coeff] = {}

    def recurse(power_left: int, needed: int) -> Coeff:
        key = (power_left, needed)
        if key in memo:
            return memo[key]
        if power_left == 0:
            out = one if needed == 0 else {}
        else:
            out: Coeff = {}
            for z_exponent, z_coefficient in zseries.items():
                tail = recurse(power_left - 1, needed - z_exponent)
                if tail:
                    out = cadd(out, cmul(z_coefficient, tail))
        memo[key] = out
        return out

    return recurse(exponent, target)


def inverse_root_series(ring: "Ring", m: int, n: int) -> ZPoly:
    """Solve f(z(w))=w^m through the order needed for r_1,r_2."""
    one = ring.one
    zseries: ZPoly = {1: one}
    # A correction t_q*w^-q first appears in z^m at w^(m-1-q).
    # q<=n+1 is necessary and sufficient for g(z(w)) through w^-2.
    for q in range(1, n + 2):
        target = m - 1 - q
        residual = zpower_coefficient(zseries, m, target, one)
        for i in range(m - 1):
            term = cmul(
                ring.var(f"a{i}"),
                zpower_coefficient(zseries, i, target, one),
            )
            residual = cadd(residual, term)
        correction = cscale(Fraction(-1, m), residual)
        if correction:
            zseries[-q] = correction
    return zseries


def coefficient_digest(value: Coeff) -> str:
    serial = [
        [list(mon), str(coeff)] for mon, coeff in sorted(value.items())
    ]
    return sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest()


def coeff_string(value: Coeff, variables: list[str]) -> str:
    if not value:
        return "0"
    terms = []
    ordered = sorted(value.items(), key=lambda item: item[0], reverse=True)
    for mon, coeff in ordered:
        factors = []
        for name, exponent in zip(variables, mon):
            if exponent == 1:
                factors.append(name)
            elif exponent:
                factors.append(f"{name}^{exponent}")
        body = "*".join(factors) or "1"
        if coeff == 1 and factors:
            term = body
        elif coeff == -1 and factors:
            term = "-" + body
        else:
            term = f"{coeff}*{body}" if factors else str(coeff)
        terms.append(term)
    return "+".join(terms).replace("+-", "-")


@dataclass
class Ring:
    names: list[str]

    @property
    def one(self) -> Coeff:
        return {(0,) * len(self.names): Fraction(1)}

    def var(self, name: str) -> Coeff:
        index = self.names.index(name)
        mon = [0] * len(self.names)
        mon[index] = 1
        return {tuple(mon): Fraction(1)}


@dataclass(frozen=True)
class Frontier:
    m: int
    n: int
    d: int
    r: int
    s: int
    orders: tuple[int, ...]

    def compile(self) -> dict[str, object]:
        names = (
            [f"a{i}" for i in range(self.m - 1)]
            + ["delta0"]
            + [f"c{i}" for i in range(self.n - 1)]
        )
        ring = Ring(names)
        one = ring.one

        # f=z^m+sum_(i=0)^(m-2) a_i z^i.  Its root is
        # w=z(1+U)^(1/m), U=sum a_i z^(i-m).
        f: ZPoly = {self.m: one}
        U: ZPoly = {}
        for i in range(self.m - 1):
            ai = ring.var(f"a{i}")
            f[i] = ai
            U[i - self.m] = ai

        faber: dict[int, ZPoly] = {}
        for j in range(self.n + 1):
            Fj: ZPoly = {j: one}
            Upower: ZPoly = {0: one}
            # U lowers z-degree by at least two.
            for k in range(1, j // 2 + 1):
                Upower = zmul(Upower, U)
                term = {exponent + j: coeff for exponent, coeff in Upower.items()
                        if exponent + j >= 0}
                Fj = zadd(Fj, zscale(binomial(Fraction(j, self.m), k), term))
            faber[j] = zclean(Fj)

        # H(T)=T^n+delta0*T^(n-1)+sum c_j*T^j.
        g = dict(faber[self.n])
        g = zadd(g, {exp: cmul(ring.var("delta0"), coeff)
                     for exp, coeff in faber[self.n - 1].items()})
        for j in range(self.n - 1):
            cj = ring.var(f"c{j}")
            g = zadd(g, {exp: cmul(cj, coeff)
                         for exp, coeff in faber[j].items()})

        if g.get(self.n) != one or g.get(self.n - 1) != ring.var("delta0"):
            raise ProbeFailure("monic/mismatch rows failed")

        # Verify every high J_(x,z) row.  Constants in H have zero x
        # derivative, so it suffices to differentiate along every a_i.
        fz = zderivative(f)
        high_min = self.m - 1
        high_max = self.m + self.n - 3
        for i in range(self.m - 1):
            variable = names.index(f"a{i}")
            fi = zpartial(f, variable)
            gi = zpartial(g, variable)
            Ji = zadd(zmul(fi, zderivative(g)), zscale(-1, zmul(fz, gi)))
            bad = sorted(exp for exp, coeff in Ji.items()
                         if coeff and high_min <= exp <= high_max)
            if bad:
                raise ProbeFailure((self.m, self.n, i, bad))

        # First two triangular integrations, reconstructed rather than
        # inserted as formulas.
        first_index = self.n - 2
        second_index = self.n - 3
        first = g.get(first_index, {})
        second = g.get(second_index, {})
        expected_first = cadd(
            cscale(Fraction(self.n, self.m), ring.var(f"a{self.m - 2}")),
            ring.var(f"c{first_index}"),
        )
        expected_second = cadd(
            cadd(
                cscale(Fraction(self.n, self.m), ring.var(f"a{self.m - 3}")),
                cscale(
                    Fraction(self.n - 1, self.m),
                    cmul(ring.var("delta0"), ring.var(f"a{self.m - 2}")),
                ),
            ),
            ring.var(f"c{second_index}"),
        )
        if first != expected_first or second != expected_second:
            raise ProbeFailure("first two integrations failed")

        # Independent two-lower-row control.  Revert f(z)=w^m just far
        # enough to compute H(w)-g(z(w)) at w^-1,w^-2.  This is deliberately
        # not a full lower-fibre expansion.
        z_of_w = inverse_root_series(ring, self.m, self.n)
        for q in range(1, self.n + 2):
            target = self.m - 1 - q
            residual = zpower_coefficient(z_of_w, self.m, target, one)
            for i in range(self.m - 1):
                residual = cadd(
                    residual,
                    cmul(
                        ring.var(f"a{i}"),
                        zpower_coefficient(z_of_w, i, target, one),
                    ),
                )
            if residual:
                raise ProbeFailure(("inverse root residual", target))
        lower_tail: dict[int, Coeff] = {}
        for ell in (1, 2):
            coefficient: Coeff = {}
            for z_exponent, g_coefficient in g.items():
                coefficient = cadd(
                    coefficient,
                    cmul(
                        g_coefficient,
                        zpower_coefficient(
                            z_of_w, z_exponent, -ell, one
                        ),
                    ),
                )
            # H(w) has no negative powers, hence r_ell=-[w^-ell]g(z(w)).
            lower_tail[ell] = cscale(-1, coefficient)

        # Target translations remove c_m, c_0, and c_(n-m).  The last follows
        # from P->P+q: c_k -> c_k-(k+m)c_(k+m)q/m, with c_n=1.
        gauge_indices = (self.m, 0, self.n - self.m)
        if len(set(gauge_indices)) != 3:
            raise ProbeFailure("target gauges not independent")

        branches = []
        for e in self.orders:
            allowed = [j for j in range(self.n)
                       if e == 1 or j % e == 0]
            if any(index not in allowed for index in gauge_indices):
                raise ProbeFailure((e, allowed, gauge_indices))
            remaining = [j for j in allowed if j not in gauge_indices]

            zero_names = set()
            for j in range(self.n - 1):
                if j not in allowed or j in gauge_indices:
                    zero_names.add(names.index(f"c{j}"))
            if self.n - 1 not in allowed:
                zero_names.add(names.index("delta0"))
            specialized = {
                ell: cspecialize_zero(lower_tail[ell], zero_names)
                for ell in (1, 2)
            }
            live_names = [f"a{i}" for i in range(self.m - 1)] + [
                "delta0" if j == self.n - 1 else f"c{j}"
                for j in remaining
            ]
            live_indices = [names.index(name) for name in live_names]
            point = [Fraction(index + 2) for index in range(len(names))]
            jacobian = [
                [cevaluate(cpartial(specialized[ell], index), point)
                 for index in live_indices]
                for ell in (1, 2)
            ]
            rank = matrix_rank(jacobian)
            branches.append({
                "Kummer_order": e,
                "allowed_H_constants_before_target_quotient": allowed,
                "target_gauge_indices": list(gauge_indices),
                "remaining_constant_indices": remaining,
                "remaining_constant_dimension": len(remaining),
                "coefficient_function_dimension": self.m - 1,
                "high_row_quotient_dimension": self.m - 1 + len(remaining),
                "two_lower_row_supports": {
                    "r1": len(specialized[1]), "r2": len(specialized[2])
                },
                "two_lower_row_sha256": {
                    "r1": coefficient_digest(specialized[1]),
                    "r2": coefficient_digest(specialized[2]),
                },
                "two_lower_row_test_rank": rank,
                "two_lower_row_local_width_at_test_point": (
                    self.m - 1 + len(remaining) - rank
                ),
            })

        relation_supports = {
            f"b{j}": len(g.get(j, {})) for j in range(self.n - 1)
        }
        return {
            "degrees": [self.m, self.n],
            "d_r_s": [self.d, self.r, self.s],
            "high_J_row_range": [high_min, high_max],
            "high_J_row_count": high_max - high_min + 1,
            "f_coefficient_functions": self.m - 1,
            "H_constants_before_character_filter": self.n,
            "first_two_integrated_rows": {
                f"b{first_index}": coeff_string(first, names),
                f"b{second_index}": coeff_string(second, names),
            },
            "all_high_rows_exactly_zero": True,
            "two_lower_rows_reconstructed": True,
            "inverse_root_terms_through_w_minus_n_plus_1": len(z_of_w),
            "relation_support_total": sum(relation_supports.values()),
            "relation_support_max": max(relation_supports.values()),
            "relation_supports": relation_supports,
            "P_translation": {
                "formula": "c_k -> c_k-(k+m)*c_(k+m)*q/m",
                "universal_slice": f"c{self.n-self.m}=0",
            },
            "branches": branches,
        }


def pin_inputs() -> dict[str, str]:
    out = {}
    for rel, expected in EXPECTED_HASHES.items():
        got = sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != expected:
            raise ProbeFailure(f"input hash mismatch {rel}: {got}")
        out[rel] = got
    return out


def main() -> None:
    inputs = pin_inputs()
    frontiers = [
        Frontier(8, 12, 4, 2, 3, (4, 2, 1)),
        Frontier(9, 12, 3, 3, 4, (3, 1)),
    ]
    compiled = {f"{item.m},{item.n}": item.compile() for item in frontiers}

    def widths(key: str) -> list[int]:
        return [branch["high_row_quotient_dimension"]
                for branch in compiled[key]["branches"]]

    widths_812 = widths("8,12")
    widths_912 = widths("9,12")
    if widths_812 != [7, 10, 16] or widths_912 != [9, 17]:
        raise ProbeFailure((widths_812, widths_912))

    payload = {
        "input_hashes": inputs,
        "compiler": {
            "formula": "g=[H(f^(1/m))]_+",
            "verification": "all high J_(x,z) rows vanish along every a_i derivative",
            "target_gauges": ["Q->Q-c_m*P", "Q->Q-c_0", "P->P+q"],
            "universal_differential_identity": (
                "D=-f_z*sum(h_j'*w^j)+f_z*sum(r_l'*w^-l)"
            ),
            "terminal_rows": (
                "r_1'=...=r_(m-2)'=0; m*r_(m-1)'=j/u"
            ),
        },
        "frontiers": compiled,
        "comparison": {
            "raw_first_gate": "(8,12)",
            "mandatory_branch_widths": {"8,12": widths_812, "9,12": widths_912},
            "maximum_width": {"8,12": max(widths_812), "9,12": max(widths_912)},
            "aggregate_width": {"8,12": sum(widths_812), "9,12": sum(widths_912)},
            "nontrivial_maximum_width": {
                "8,12": max(widths_812[:-1]), "9,12": widths_912[0]
            },
            "nontrivial_aggregate_width": {
                "8,12": sum(widths_812[:-1]), "9,12": widths_912[0]
            },
            "two_lower_row_local_widths": {
                key: [branch["two_lower_row_local_width_at_test_point"]
                      for branch in compiled[key]["branches"]]
                for key in ("8,12", "9,12")
            },
            "speed_allocation": "(9,12) first by aggregate mandatory-route quotient width",
            "no_overall_complexity_theorem": True,
        },
        "scope": {
            "lower_Laurent_rows": "ONLY_R1_R2_CONTROL_RECONSTRUCTED",
            "components": "NOT_CLASSIFIED",
            "frontier_emptiness": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-MAX12-SHARED-HIGH-ROW-PROBE")
    print("frontier_8_12_quotient_widths=7,10,16")
    print("frontier_9_12_quotient_widths=9,17")
    print("all_high_rows=EXACT_FABER")
    print("speed_allocation_by_aggregate_width=(9,12)")
    print("overall_cheaper_cell=NOT_CLAIMED")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
