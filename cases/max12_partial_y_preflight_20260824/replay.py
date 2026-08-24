#!/usr/bin/env python3
"""Exact bounded preflight for primitive partial-y frontiers (8,12),(9,12).

Only the reviewed shear/UFD history is a theorem input.  Later Kummer,
depression, boundary, and binary-W identities are reconstructed here.  The
script does not integrate the full high-row systems or claim either cell is
empty.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_HASHES = {
    "xmodel/as109-partial-y-history-stop-20260824.md":
        "6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe",
    "xmodel/as109-partial-y-history-review-grok-20260824.md":
        "f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd",
}

Poly = dict[int, Fraction]


class PreflightFailure(RuntimeError):
    pass


def pin_inputs() -> dict[str, str]:
    out: dict[str, str] = {}
    for rel, expected in EXPECTED_HASHES.items():
        got = sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != expected:
            raise PreflightFailure(f"UNCLAIMED hash mismatch {rel}: {got}")
        out[rel] = got
    return out


def clean(poly: Poly) -> Poly:
    return {i: c for i, c in poly.items() if c}


def add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for i, value in right.items():
        out[i] = out.get(i, Fraction(0)) + value
    return clean(out)


def scale(value: Fraction | int, poly: Poly) -> Poly:
    value = Fraction(value)
    return clean({i: value * c for i, c in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, Fraction(0)) + a * b
    return clean(out)


def power(poly: Poly, exponent: int) -> Poly:
    out: Poly = {0: Fraction(1)}
    base = dict(poly)
    n = exponent
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def derivative(poly: Poly) -> Poly:
    return clean({i - 1: i * c for i, c in poly.items() if i})


def degree(poly: Poly) -> int:
    return max(poly) if poly else -1


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    a = [list(row) for row in rows]
    row = 0
    columns = len(a[0])
    for column in range(columns):
        pivot = next((i for i in range(row, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        pivot_value = a[row][column]
        a[row] = [value / pivot_value for value in a[row]]
        for i in range(len(a)):
            if i == row or not a[i][column]:
                continue
            factor = a[i][column]
            a[i] = [x - factor * y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def top_row(m: int, n: int) -> dict[str, int]:
    """Return the next Jacobian row after factoring u^(m+n-1)."""
    terms = (
        {"log_u*B": m * (n - 1)},
        {"A_prime": n, "log_u*A": n * (m - 1)},
        {"B_prime": -m, "log_u*B": -m * (n - 1)},
        {"log_u*A": -n * (m - 1)},
    )
    out: dict[str, int] = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def class_order(d: int, valuations: list[int]) -> int:
    """Order of a P1 Kummer class from its divisor residues modulo d."""
    for exponent in range(1, d + 1):
        if all((exponent * value) % d == 0 for value in valuations):
            return exponent
    raise PreflightFailure((d, valuations))


def linearized_constant_w_rank(d: int, r: int, s: int) -> dict[str, int]:
    """Rank at K=z^d+z+1 of positive-degree coefficients of dW.

    W=r*f*g_z-s*f_z*g.  Monicity and the z^(degree-1) depressions are fixed.
    """
    m, n = d * r, d * s
    K = {d: Fraction(1), 1: Fraction(1), 0: Fraction(1)}
    f, g = power(K, r), power(K, s)
    W = add(scale(r, mul(f, derivative(g))), scale(-s, mul(derivative(f), g)))
    if W:
        raise PreflightFailure("common-power Wronskian is nonzero")

    columns: list[Poly] = []
    for i in range(m - 1):
        df = {i: Fraction(1)}
        dW = add(
            scale(r, mul(df, derivative(g))),
            scale(-s, mul(derivative(df), g)),
        )
        columns.append(dW)
    for j in range(n - 1):
        dg = {j: Fraction(1)}
        dW = add(
            scale(r, mul(f, derivative(dg))),
            scale(-s, mul(derivative(f), dg)),
        )
        columns.append(dW)

    max_degree = max((degree(column) for column in columns), default=0)
    rows = [
        [column.get(exponent, Fraction(0)) for column in columns]
        for exponent in range(1, max_degree + 1)
    ]
    rank = matrix_rank(rows)
    ambient = len(columns)
    return {
        "ambient_depressed_coefficients": ambient,
        "positive_W_rows": len(rows),
        "tangent_rank": rank,
        "tangent_kernel_dimension": ambient - rank,
        "common_K_parameters": d - 1,
    }


@dataclass(frozen=True)
class Frontier:
    m: int
    n: int

    @property
    def d(self) -> int:
        return gcd(self.m, self.n)

    @property
    def r(self) -> int:
        return self.m // self.d

    @property
    def s(self) -> int:
        return self.n // self.d

    def audit(self) -> dict[str, object]:
        d, r, s = self.d, self.r, self.s
        normalized = top_row(self.m, self.n)
        expected = {"A_prime": d * s, "B_prime": -d * r}
        if normalized != expected:
            raise PreflightFailure((self, normalized, expected))

        open_H = [H for H in range(0, 4 * d + 1) if gcd(H, d) not in (1, 2)]
        if d == 4 and open_H != [0, 4, 8, 12, 16]:
            raise PreflightFailure((self, open_H))
        if d == 3 and open_H != [0, 3, 6, 9, 12]:
            raise PreflightFailure((self, open_H))

        orders = (4, 2, 1) if d == 4 else (3, 1)
        branches = []
        for e in orders:
            weight_A = (-(self.m - 1)) % e if e > 1 else 0
            weight_B = (-(self.n - 1)) % e if e > 1 else 0
            if e > 1 and (weight_A, weight_B) != (1, 1):
                raise PreflightFailure((self, e, weight_A, weight_B))
            branches.append(
                {
                    "Kummer_class_order": e,
                    "minimal_extension_degree": e,
                    "A_weight": weight_A,
                    "B_weight": weight_B,
                    "delta_forced_zero": e > 1,
                    "potential_weight_zero_constant_indices": [
                        # The z^(n-1) slot is the depression mismatch and is
                        # already zero on every nontrivial Kummer branch.
                        # Later lower target constants have 0<=j<=n-2.
                        j for j in range(self.n - 1)
                        if e == 1 or (-j) % e == 0
                    ],
                }
            )

        tangent = linearized_constant_w_rank(d, r, s)
        return {
            "degrees": [self.m, self.n],
            "d_r_s": [d, r, s],
            "history_residual": f"gcd(H,{d})={d}",
            "equivalent_H_condition": f"{d}|H",
            "leading_powers": [f"a{self.m}=h^{r}", f"b{self.n}=h^{s}"],
            "root": f"u^{d}=h",
            "top_row_after_u_power": normalized,
            "top_row_u_exponent": self.m + self.n - 1,
            "delta": f"{s}A-{r}B",
            "depression": f"z=u*y+A/{self.m}",
            "second_mismatch": f"-delta/{r}",
            "Kummer_branches": branches,
            "boundary_jets": {
                "P": f"u^ell/ell! * d_z^ell f(A/{self.m}) in k[x], 0<=ell<={self.m}",
                "Q": f"u^ell/ell! * d_z^ell g(A/{self.m}) in k[x], 0<=ell<={self.n}",
            },
            "binary_W": f"{r}*f*g_z-{s}*f_z*g",
            "binary_H": f"f^{s}-g^{r}",
            "common_power": f"f=K^{r},g=K^{s},deg(K)={d}",
            "constant_W_tangent": tangent,
        }


def main() -> None:
    hashes = pin_inputs()

    # Exact branch-typing examples at the residual degrees.
    examples = {
        "d4_order4": class_order(4, [1, 1, 1, 1, -4]),
        "d4_order2": class_order(4, [2, 2, -4]),
        "d4_order1": class_order(4, [4, -4]),
        "d3_order3": class_order(3, [1, 1, 1, -3]),
        "d3_order1": class_order(3, [3, -3]),
    }
    expected_examples = {
        "d4_order4": 4,
        "d4_order2": 2,
        "d4_order1": 1,
        "d3_order3": 3,
        "d3_order1": 1,
    }
    if examples != expected_examples:
        raise PreflightFailure(examples)

    f812 = Frontier(8, 12).audit()
    f912 = Frontier(9, 12).audit()

    # Verify the general binary identity on exact non-common test pairs:
    # f*(f^s-g^r)' - s*f'*(f^s-g^r) = -W*g^(r-1).
    identity_checks = {}
    for frontier in (Frontier(8, 12), Frontier(9, 12)):
        m, n, r, s = frontier.m, frontier.n, frontier.r, frontier.s
        f = {m: Fraction(1), 2: Fraction(2), 0: Fraction(1)}
        g = {n: Fraction(1), 3: Fraction(3), 0: Fraction(-1)}
        Hpoly = add(power(f, s), scale(-1, power(g, r)))
        Wpoly = add(
            scale(r, mul(f, derivative(g))),
            scale(-s, mul(derivative(f), g)),
        )
        left = add(
            mul(f, derivative(Hpoly)),
            scale(-s, mul(derivative(f), Hpoly)),
        )
        right = scale(-1, mul(Wpoly, power(g, r - 1)))
        if left != right:
            raise PreflightFailure(f"binary identity failed: {(m, n)}")
        identity_checks[f"{m},{n}"] = True

    payload = {
        "input_hashes": hashes,
        "umbrella": {
            "degrees": "(d*r,d*s),gcd(r,s)=1",
            "leading": "a_(dr)=h^r,b_(ds)=h^s,u^d=h",
            "next_row": "d*u^(d(r+s)-1)*(s*A-r*B)'",
            "delta": "s*A-r*B",
            "mismatch_after_z=u*y+A/(dr)": "-delta/r",
            "nontrivial_class_order_e_divides_d": "A,B,delta have weight one; delta=0",
            "trivial_class": "h is a polynomial dth power after Gauss; mismatch is weight-unforced",
            "boundary": "all original Taylor jets remain polynomial",
            "binary_identity": "f*(f^s-g^r)'-s*f'*(f^s-g^r)=-W*g^(r-1)",
        },
        "branch_examples": {
            "d4_order4": "h=x(x-1)(x-2)(x-3)",
            "d4_order2": "h=x^2(x-1)^2",
            "d4_order1": "h=x^4",
            "d3_order3": "h=x(x-1)(x-2)",
            "d3_order1": "h=x^3",
        },
        "branch_example_orders": examples,
        "frontiers": {"8,12": f812, "9,12": f912},
        "binary_identity_checks": identity_checks,
        "ranking": {
            "exact_raw_first_nonlinear_gate": "(8,12)",
            "raw_gate_reason": [
                "18 depressed coefficients and 17 positive-W rows versus 19 and 18",
                "at K=z^d+z+1 both tangent ranks are 11, leaving kernel 7 versus 8",
                "the 2:3 signature directly reuses the binary-W/Faber template",
            ],
            "simpler_Kummer_branch_tree": "(9,12)",
            "branch_tree_reason": [
                "two Kummer orders (3,1) versus three (4,2,1)",
                "no quadratic intermediate branch",
                "nontrivial order-3 weight-zero slots 4 versus order-2 slots 6",
            ],
            "whole_cell_cost": "NOT_ORDERED_BEFORE_HIGH_ROW_INTEGRATION",
        },
        "scope": {
            "full_high_row_integration": "NOT_DONE",
            "constant_W_components": "NOT_CLASSIFIED",
            "either_frontier_empty": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-MAX12-PARTIAL-Y-PREFLIGHT")
    print("frontier_8_12=H_MULTIPLE_4;KUMMER_ORDERS_4_2_1")
    print("frontier_9_12=H_MULTIPLE_3;KUMMER_ORDERS_3_1")
    print("delta_nontrivial_Kummer=FORCED_ZERO")
    print("boundaries=ALL-TAYLOR-JETS-CHARGED")
    print("smaller_raw_first_nonlinear_gate=(8,12)")
    print("simpler_Kummer_branch_tree=(9,12)")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
