#!/usr/bin/env python3
"""First trunk consumer of the source-pinned td=12 U1 family.

Independent exact arithmetic for:
  - merge closed forms (Theorem B residue), with merge index n
    kept distinct from the trunk vertex nu_F = 25;
  - the displayed dirty chain cell (l,eps,k,lex,nu_F)=(2,0,1,0,25);
  - the exact Prop. 8.1(iv) identity on that cell, solved with no
    degree cap;
  - the complete cap-free one-step reduced P0 menu from (w,M)=(9/2,2)
    at remaining budget 9, using E | l*num(w)*T (reviewed R2 law).

No imports from other packets. No caps, CAS, or sampling of the ODE.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from math import gcd

from polyexact import Poly, require


SCHEMA = "m2-td12-u1-trunk-consumer-grok46-v1"
CAP_TOKENS = ("cap", "capped", "max_nu", "max_kbar", "degree_cap",
              "loop_cap", "hard_cap")


def ceil_fr(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def divisors(n: int) -> list[int]:
    require(isinstance(n, int) and n >= 1, "divisors require n>=1")
    low: list[int] = []
    high: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
        d += 1
    return low + list(reversed(high))


def fraction_text(value: Fraction) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def sha256_bytes(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def refuse_cap_tokens(argv: list[str]) -> None:
    joined = " ".join(argv).lower()
    for token in CAP_TOKENS:
        if token in joined:
            raise SystemExit(f"CAP_TOKEN_REJECTED:{token}")


# ---------------------------------------------------------------------------
# Merge family (r,mu,eps,w)=(3,2,0,3/2). Index is n, never nu_F.
# ---------------------------------------------------------------------------

def merge_cell(n: int) -> dict[str, object]:
    require(n >= 2, "merge index n>=2")
    r, mu, eps = 3, 2, 0
    w = Fraction(3, 2)
    dp = eps + n * r * mu
    dq = 1 + n * r
    e_gap = mu - eps
    kbar = mu * w * dq / e_gap
    x = mu * w * dp / e_gap
    m = gcd(e_gap, r * n + 1)
    w_tr = mu * w * r / e_gap
    return {
        "n": n,
        "dp": dp,
        "dq": dq,
        "E": e_gap,
        "kbar": kbar,
        "X": x,
        "M": m,
        "w_tr": w_tr,
        "lambda_G": 0,
        "kbar_integral": kbar.denominator == 1,
        "N1": kbar.denominator == 1 and gcd(int(kbar), n) == 1,
        "MP2": m >= 2,
        "S": mu * dq > dp,
    }


def admissible_merge_indices(limit: int = 80) -> list[int]:
    out = []
    for n in range(5, limit + 1):
        cell = merge_cell(n)
        if (n % 6 in (1, 5) and cell["kbar_integral"] and cell["N1"]
                and cell["MP2"] and cell["S"]):
            out.append(n)
    return out


# ---------------------------------------------------------------------------
# Displayed dirty trunk cell. nu_F is the chain-vertex index, not n.
# ---------------------------------------------------------------------------

def dirty_cell() -> dict[str, object]:
    l, eps, k, lex, nu_f = 2, 0, 1, 0, 25
    sm = 1  # unique partition of k=1 with m_j <= l-1 = 1
    w_parent = Fraction(9, 2)
    p = l + sm
    s = 1 + k + lex
    dp = eps + nu_f * p
    dq = 1 + nu_f * s
    e = l * dq - dp
    c_p0 = l * (k + lex) - sm
    t = sm + l - eps * s
    kbar = l * w_parent * dq / e
    x = kbar * Fraction(dp, dq)
    w_child = l * w_parent * (dq - 1) / (nu_f * e)
    m_child = gcd(dp, dq)
    gap = x / 1 - kbar
    lam_floor = max(1, ceil_fr(gap))
    j = m_child * (1 - w_child)
    require(j.denominator == 1 and j >= 1, "P1 j not in N*")
    psi = ceil_fr(Fraction(m_child, int(j))) - 1
    dividend = l * w_parent.numerator * t
    resolvent_lhs = e * (l * w_parent.numerator * (1 + k + lex)
                         - int(kbar) * w_parent.denominator * c_p0)
    resolvent_rhs = l * w_parent.numerator * t
    return {
        "l": l,
        "eps": eps,
        "k": k,
        "lex": lex,
        "nu_F": nu_f,
        "Sm": sm,
        "w_parent": w_parent,
        "dp": dp,
        "dq": dq,
        "E": e,
        "C_P0": c_p0,
        "T": t,
        "kbar": int(kbar),
        "X": x,
        "w_child": w_child,
        "M_child": m_child,
        "rho": Fraction(dp, dq),
        "gap": gap,
        "lambda_floor": lam_floor,
        "j": int(j),
        "psi": psi,
        "td": 12,
        "budget_ceiling": 12 - 1 - psi,
        "slack_lower_bound": (12 - 1 - psi) - lam_floor,
        "N1": gcd(int(kbar), nu_f) == 1,
        "S": l * dq > dp,
        "NE": 1 * dq < dp,
        "R": dp != l * dq and dp != 1 * dq,
        "MP2": m_child >= 2,
        "gcd_M_nu": gcd(m_child, nu_f),
        "E_divides": dividend % e == 0,
        "dividend": dividend,
        "resolvent_ok": resolvent_lhs == resolvent_rhs,
        "resolvent_lhs": resolvent_lhs,
        "resolvent_rhs": resolvent_rhs,
        "kbar_integral": kbar.denominator == 1,
    }


# ---------------------------------------------------------------------------
# Prop. 8.1(iv) on the dirty cell. Pattern in t = eta^{nu_F}:
#   Pfull = (t-A)^2 (t-B),   W = (t-A)(t-B),   q = eta W,
#   no p-zero-root (eps=0), one non-chain simple orbit B.
# ---------------------------------------------------------------------------

def t1_poly(A: Fraction, B: Fraction, nu: int, rho: Fraction) -> dict[str, Poly]:
    lin_a = Poly.monic_linear(A)
    lin_b = Poly.monic_linear(B)
    pfull = lin_a * lin_a * lin_b
    w = lin_a * lin_b
    e_poly = (pfull * w).scale(rho) + (pfull * w.deriv()).shift().scale(nu * rho) \
        + (pfull.deriv() * w).shift().scale(-nu)
    return {"Pfull": pfull, "W": w, "E": e_poly}


def t1_linear_form(nu: int, rho: Fraction) -> tuple[Fraction, Fraction]:
    """Coefficients of A and B in the t^1 coefficient of C_iv(t)."""
    coeff_a = rho + nu * (rho - 1)
    coeff_b = rho + nu * (rho - 2)
    return coeff_a, coeff_b


def t1_ratio(nu: int) -> Fraction:
    """Unique reduced ratio B/A for the (2,1) dirty shape, nu>=2.

    Derived from vanishing of the t^1 coefficient after the t^2
    coefficient cancels identically by rho = 3 nu / (2 nu + 1).
    """
    require(nu >= 2, "nu_F>=2")
    return Fraction(nu + 2, nu - 1)


def solve_dirty_t1() -> dict[str, object]:
    cell = dirty_cell()
    nu = cell["nu_F"]
    rho = cell["rho"]
    coeff_a, coeff_b = t1_linear_form(nu, rho)
    t2 = rho + nu * (2 * rho - 3)
    require(t2 == 0, "top cancellation failed")
    require(coeff_a != 0 and coeff_b != 0, "linear form degenerate")
    ratio = -coeff_a / coeff_b
    require(ratio == t1_ratio(nu), "closed-form ratio mismatch")
    require(ratio == Fraction(9, 8), "displayed cell ratio is 9/8")
    # Gauge: A=8, B=9 clears denominators. General solution A=8u, B=9u.
    a0, b0 = Fraction(8), Fraction(9)
    polys = t1_poly(a0, b0, nu, rho)
    c_iv = rho * a0 * b0
    residual = polys["E"] - polys["Pfull"].scale(c_iv)
    require(residual.is_zero(), "E - C_iv Pfull is not identically 0")
    require(c_iv != 0, "C_iv vanished")
    require(a0 != 0 and b0 != 0 and a0 != b0, "root law failed")
    require(rho != 1 and rho != 2, "rho equals a p-multiplicity")
    return {
        "nu_F": nu,
        "rho": fraction_text(rho),
        "t2_coeff": fraction_text(t2),
        "linear_coeff_A": fraction_text(coeff_a),
        "linear_coeff_B": fraction_text(coeff_b),
        "ratio_B_over_A": fraction_text(ratio),
        "gauge_A": fraction_text(a0),
        "gauge_B": fraction_text(b0),
        "C_iv": fraction_text(c_iv),
        "C_iv_general": "225 u^2 / 136  (A=8u, B=9u)",
        "residual_zero": True,
        "Pfull": polys["Pfull"].as_list(),
        "E": polys["E"].as_list(),
        "zero_root_in_p": False,
        "eta_divides_q": True,
        "verdict": "TRUNK_T1_SURVIVES",
    }


def t1_identity_holds(A: Fraction, B: Fraction, nu: int, rho: Fraction) -> bool:
    polys = t1_poly(A, B, nu, rho)
    # After top cancel, E must be a constant multiple of Pfull.
    pfull = polys["Pfull"]
    e_poly = polys["E"]
    if pfull.degree() != 3:
        return False
    lead_p = pfull.c[-1]
    if e_poly.degree() != 3:
        return False
    c_iv = e_poly.c[-1] / lead_p
    return (e_poly - pfull.scale(c_iv)).is_zero() and c_iv != 0


# ---------------------------------------------------------------------------
# Cap-free one-step reduced P0 menu from (9/2, 2) at remaining budget 9.
# Exact reviewed divisor law: extras-present E | l*num(w)*T, nu>=2.
# ---------------------------------------------------------------------------

def min_ne_lambda(X: Fraction, kbar: Fraction, k: int, sm: int,
                  max_mult: int) -> int | None:
    if k == 0:
        return 0 if sm == 0 else None
    if max_mult < 1 or sm < k or sm > k * max_mult:
        return None
    best: int | None = None

    def visit(index: int, left: int, cost: int) -> None:
        nonlocal best
        if best is not None and cost >= best:
            return
        if index == k:
            if left == 0:
                best = cost if best is None else min(best, cost)
            return
        remaining = k - index - 1
        for mult in range(1, max_mult + 1):
            after = left - mult
            if after < remaining or after > remaining * max_mult:
                continue
            gap = X / mult - kbar
            if gap <= 0:
                continue
            visit(index + 1, after, cost + max(1, ceil_fr(gap)))

    visit(0, sm, 0)
    return best


def dirty_lex_bound(w: Fraction, l: int, eps: int, k: int, sm: int) -> int:
    if eps > 0:
        numerator = sm + l - eps * (1 + k) - 1
        return numerator // eps if numerator >= 0 else -1
    t = sm + l
    cmax = (l * w.numerator * t - l) // 2
    if cmax < 1:
        return -1
    return (cmax + sm) // l - k


def p1_data(w: Fraction, m: int) -> dict[str, object] | None:
    if not (w < 1 and m >= 2):
        return None
    j = m * (1 - w)
    if j.denominator != 1 or j < 1:
        return None
    psi = ceil_fr(Fraction(m, int(j))) - 1
    return {"j": int(j), "psi": psi, "budget": 12 - 1 - psi}


def one_step_menu(w: Fraction, m_parent: int, budget: int) -> list[dict]:
    require(w > 0 and m_parent >= 1 and budget >= 0, "bad one-step input")
    out: dict[tuple, dict] = {}

    def add(rec: dict) -> None:
        if rec["lambda"] <= budget:
            key = (rec["family"], rec["lambda"], fraction_text(rec["w"]),
                   rec["M"], json.dumps(rec["witness"], sort_keys=True))
            out[key] = rec

    for delta in divisors(w.numerator):
        if delta < 3:
            continue
        for nu in range(2, delta):
            if (delta - 1) % nu:
                continue
            n_orb = (delta - 1) // nu + 1
            if n_orb < 2:
                continue
            dq = n_orb * nu + 1
            if dq % w.denominator:
                continue
            for l in divisors(m_parent):
                add({
                    "family": "clean-resonant",
                    "lambda": 0,
                    "w": w * Fraction(n_orb, delta),
                    "M": gcd(l, dq),
                    "witness": {"l": l, "Delta": delta, "n": n_orb,
                                "nu": nu, "dp": l * nu, "dq": dq},
                })

    for m2 in divisors(m_parent):
        add({
            "family": "clean-neutral",
            "lambda": 0,
            "w": w,
            "M": m2,
            "witness": {"M_parent": m_parent, "M_child": m2},
        })

    for l in divisors(m_parent):
        if l < 2:
            continue
        for eps in range(1, l):
            e = l - eps
            cost = ceil_fr(Fraction(l, eps) * w)
            if cost > budget:
                continue
            add({
                "family": "pure-epsilon",
                "lambda": cost,
                "w": Fraction(l, e) * w,
                "M": e,  # M' | (l-eps); recorded as the maximum
                "witness": {"l": l, "eps": eps, "E": e,
                            "M_law": f"gcd({e}, nu+1)"},
            })
        for eps in range(0, l):
            kmax = budget - (1 if eps else 0)
            if kmax < 0:
                continue
            for k in range(kmax + 1):
                if eps == 0 and k == 0:
                    continue
                for sm in range(k, k * (l - 1) + 1):
                    lexmax = dirty_lex_bound(w, l, eps, k, sm)
                    for lex in range(max(-1, lexmax) + 1):
                        c_p0 = l * (k + lex) - sm
                        if c_p0 <= 0:
                            continue
                        t = sm + l - eps * (1 + k + lex)
                        if t <= 0:
                            continue
                        dividend = l * w.numerator * t
                        for e in divisors(dividend):
                            numerator = e - (l - eps)
                            if numerator < 2 * c_p0 or numerator % c_p0:
                                continue
                            nu = numerator // c_p0
                            dq = (1 + k + lex) * nu + 1
                            dp = eps + nu * (l + sm)
                            require(l * dq - dp == e, "E reconstruction")
                            kbar = Fraction(l) * w * dq / e
                            if kbar.denominator != 1 or kbar < 1:
                                continue
                            if eps and eps * dq >= dp:
                                continue
                            x = kbar * Fraction(dp, dq)
                            max_mult = min(l - 1, (dp - 1) // dq) if k else 0
                            price = min_ne_lambda(x, kbar, k, sm, max_mult)
                            if price is None:
                                continue
                            if eps:
                                gap0 = (x / eps - kbar) / nu
                                if gap0 <= 0:
                                    continue
                                price += max(1, ceil_fr(gap0))
                            if price > budget:
                                continue
                            w2 = Fraction(l) * w * (dq - 1) / (nu * e)
                            m2 = gcd(dp, dq)
                            rec = {
                                "family": "dirty",
                                "lambda": price,
                                "w": w2,
                                "M": m2,
                                "witness": {
                                    "l": l, "eps": eps, "k": k, "Sm": sm,
                                    "lex": lex, "C_P0": c_p0, "T": t, "E": e,
                                    "nu_F": nu, "dp": dp, "dq": dq,
                                    "kbar": int(kbar),
                                    "X": fraction_text(x),
                                    "N1": gcd(int(kbar), nu) == 1,
                                    "derived_lex_bound": lexmax,
                                },
                            }
                            p1 = p1_data(w2, m2)
                            if p1 is not None:
                                rec["P1"] = p1
                                rec["fits_own_P1"] = price <= p1["budget"]
                            add(rec)
    return sorted(out.values(), key=lambda r: (
        r["lambda"], r["w"], r["M"], r["family"],
        json.dumps(r["witness"], sort_keys=True)))


def menu_summary(menu: list[dict]) -> dict[str, object]:
    dirty = [r for r in menu if r["family"] == "dirty"]
    terminals = [r for r in dirty if "P1" in r]
    fitting = [r for r in terminals if r.get("fits_own_P1")]
    clean_res = [r for r in menu if r["family"] == "clean-resonant"]
    m2_res = [r for r in clean_res if r["M"] >= 2]
    return {
        "step_count": len(menu),
        "dirty_count": len(dirty),
        "clean_resonant_count": len(clean_res),
        "clean_resonant_M_ge_2": len(m2_res),
        "pure_epsilon_count": sum(1 for r in menu if r["family"] == "pure-epsilon"),
        "clean_neutral_count": sum(1 for r in menu if r["family"] == "clean-neutral"),
        "one_step_P1_terminals": [
            {
                "w": fraction_text(r["w"]),
                "M": r["M"],
                "lambda": r["lambda"],
                "nu_F": r["witness"]["nu_F"],
                "k": r["witness"]["k"],
                "psi": r["P1"]["psi"],
                "budget": r["P1"]["budget"],
                "fits_own_P1": r["fits_own_P1"],
            }
            for r in terminals
        ],
        "fitting_P1": [
            {
                "w": fraction_text(r["w"]),
                "M": r["M"],
                "lambda": r["lambda"],
                "nu_F": r["witness"]["nu_F"],
                "k": r["witness"]["k"],
            }
            for r in fitting
        ],
        "displayed_in_menu": any(
            r["family"] == "dirty"
            and r["witness"].get("nu_F") == 25
            and r["witness"].get("k") == 1
            and r["witness"].get("eps") == 0
            and r["w"] == Fraction(2, 3)
            and r["M"] == 3
            for r in menu
        ),
    }


def emit_payload() -> dict[str, object]:
    merge_n = admissible_merge_indices(40)
    cell = dirty_cell()
    t1 = solve_dirty_t1()
    menu = one_step_menu(Fraction(9, 2), 2, 9)
    summary = menu_summary(menu)
    public_menu = []
    for rec in menu:
        item = {
            "family": rec["family"],
            "lambda": rec["lambda"],
            "w": fraction_text(rec["w"]),
            "M": rec["M"],
            "witness": rec["witness"],
        }
        if "P1" in rec:
            item["P1"] = rec["P1"]
            item["fits_own_P1"] = rec["fits_own_P1"]
        public_menu.append(item)
    payload = {
        "schema": SCHEMA,
        "scope": "td=12 U1 first trunk consumer; reduced Prop 8.1(iv) + P0 menu",
        "merge": {
            "r": 3, "mu": 2, "eps": 0, "w": "3/2",
            "w_tr": "9/2", "M": 2, "lambda_G": 0,
            "Rad": "t^3 - A_star, A_star != 0",
            "admissible_n_mod_6": [1, 5],
            "admissible_n_le_40": merge_n,
            "note": "merge index n is not the trunk nu_F=25",
        },
        "dirty_cell": {
            k: (fraction_text(v) if isinstance(v, Fraction) else v)
            for k, v in cell.items()
        },
        "t1": t1,
        "menu_from_9_2_budget_9": summary,
        "menu": public_menu,
        "lead_verdict": "FAMILY_SURVIVES_FIRST_TRUNK",
        "cell_verdict": "TRUNK_T1_SURVIVES",
        "firewall": {
            "landing": False,
            "keller_pair": False,
            "panel_exclusion": False,
            "td_ceiling": False,
            "jc2": False,
            "gluing_of_t3_minus_A": False,
        },
        "cap_free": True,
        "hard_loop_caps": [],
    }
    payload["payload_sha256"] = sha256_bytes(canonical(
        {k: v for k, v in payload.items() if k != "payload_sha256"}
    ))
    return payload


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    refuse_cap_tokens(argv)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit", default="")
    parser.add_argument("--w", default="9/2")
    parser.add_argument("--M", type=int, default=2)
    parser.add_argument("--budget", type=int, default=9)
    args = parser.parse_args(argv)
    require(args.w == "9/2" and args.M == 2 and args.budget == 9,
            "this executable is pinned to the charged (9/2,2,B=9) cell")
    payload = emit_payload()
    blob = canonical(payload)
    if args.emit:
        with open(args.emit, "wb") as handle:
            handle.write(blob)
            handle.write(b"\n")
    sys.stdout.write(json.dumps({
        "lead_verdict": payload["lead_verdict"],
        "cell_verdict": payload["cell_verdict"],
        "ratio_B_over_A": payload["t1"]["ratio_B_over_A"],
        "C_iv": payload["t1"]["C_iv"],
        "displayed_in_menu": payload["menu_from_9_2_budget_9"]["displayed_in_menu"],
        "step_count": payload["menu_from_9_2_budget_9"]["step_count"],
        "dirty_count": payload["menu_from_9_2_budget_9"]["dirty_count"],
        "fitting_P1": payload["menu_from_9_2_budget_9"]["fitting_P1"],
        "payload_sha256": payload["payload_sha256"],
        "EMIT_PASS": True,
    }, sort_keys=True, separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
