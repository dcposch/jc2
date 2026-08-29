#!/usr/bin/env python3
"""Ordinary and -O tests for the td=12 U1 first trunk consumer packet."""

from __future__ import annotations

import io
import sys
from fractions import Fraction
from math import gcd

from polyexact import Poly, require
from trunk_consumer import (
    CAP_TOKENS,
    admissible_merge_indices,
    dirty_cell,
    emit_payload,
    main,
    merge_cell,
    one_step_menu,
    refuse_cap_tokens,
    solve_dirty_t1,
    t1_identity_holds,
    t1_linear_form,
    t1_poly,
    t1_ratio,
)


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    require(condition, message)
    CHECKS += 1


def run() -> int:
    # --- merge family, index n distinct from nu_F ---
    cell5 = merge_cell(5)
    check(cell5["w_tr"] == Fraction(9, 2), "w_tr")
    check(cell5["M"] == 2, "M identically 2 at n=5")
    check(cell5["lambda_G"] == 0, "merge lambda floor 0")
    check(cell5["E"] == 2, "E=mu-eps=2")
    adm = admissible_merge_indices(40)
    check(adm[:8] == [5, 7, 11, 13, 17, 19, 23, 25], "AP residues")
    check(all(n % 6 in (1, 5) for n in adm), "n mod 6 in {1,5}")
    check(25 in adm, "n=25 is an admissible MERGE index, distinct object")
    for n in (5, 7, 11, 13, 17, 19, 23, 25):
        c = merge_cell(n)
        check(c["M"] == 2, f"M=2 at n={n}")
        check(c["kbar_integral"] and c["N1"] and c["S"] and c["MP2"],
              f"legality at n={n}")
        check(c["dp"] == 6 * n and c["dq"] == 3 * n + 1, f"dp/dq at n={n}")
        check(c["kbar"] == 3 * (3 * n + 1) / 2, f"kbar at n={n}")
        check(c["X"] == 9 * n, f"X at n={n}")

    # --- displayed dirty cell ---
    d = dirty_cell()
    check(d["nu_F"] == 25, "trunk nu_F")
    check(d["nu_F"] != d["l"] and d["nu_F"] != d["k"], "nu_F not a local exponent")
    check(d["dp"] == 75 and d["dq"] == 51 and d["E"] == 27, "dp dq E")
    check(d["kbar"] == 17 and d["X"] == 25, "kbar X")
    check(d["w_child"] == Fraction(2, 3) and d["M_child"] == 3, "successor")
    check(d["C_P0"] == 1 and d["T"] == 3, "P0 C,T")
    check(d["E_divides"] and d["dividend"] == 54, "E | 54")
    check(d["resolvent_ok"] and d["resolvent_lhs"] == 54, "Fable resolvent")
    check(d["N1"] and d["S"] and d["NE"] and d["R"] and d["MP2"], "filters")
    check(d["gcd_M_nu"] == 1, "R1.0 gcd(M,nu)=1")
    check(d["lambda_floor"] == 8, "lambda floor")
    check(d["j"] == 1 and d["psi"] == 2, "P1 j,psi")
    check(d["budget_ceiling"] == 9 and d["slack_lower_bound"] == 1, "budget")
    check(d["rho"] == Fraction(25, 17), "rho")
    check(d["gap"] == 8, "exact integer gap")
    check(d["eps"] == 0, "no free 0-root")

    # --- T1 exact solve ---
    t1 = solve_dirty_t1()
    check(t1["verdict"] == "TRUNK_T1_SURVIVES", "cell verdict")
    check(t1["ratio_B_over_A"] == "9/8", "ratio")
    check(t1["C_iv"] == "1800/17", "C_iv at gauge (8,9)")
    check(t1["t2_coeff"] == "0", "t^2 cancelled")
    check(t1["linear_coeff_A"] == "225/17", "coeff A")
    check(t1["linear_coeff_B"] == "-200/17", "coeff B")
    check(t1["residual_zero"], "identity")
    check(t1["zero_root_in_p"] is False, "no p 0-root")
    check(t1["eta_divides_q"] is True, "eta || q")
    check(t1_ratio(25) == Fraction(9, 8), "closed form at 25")
    check(t1_ratio(7) == Fraction(3, 2), "TEMPLATE F_s ratio B=(3/2)A")
    for nu in (3, 5, 7, 11, 13, 17, 19, 25):
        rho = Fraction(3 * nu, 2 * nu + 1)
        ca, cb = t1_linear_form(nu, rho)
        check(rho + nu * (2 * rho - 3) == 0, f"t2 cancel nu={nu}")
        check(-ca / cb == t1_ratio(nu), f"ratio formula nu={nu}")
        a = Fraction(nu - 1)
        b = Fraction(nu + 2)
        check(t1_identity_holds(a, b, nu, rho), f"identity at nu={nu}")

    # uniqueness: a wrong ratio fails the identity
    rho25 = Fraction(25, 17)
    check(not t1_identity_holds(Fraction(8), Fraction(8), 25, rho25),
          "A=B is not a solution")
    check(not t1_identity_holds(Fraction(8), Fraction(7), 25, rho25),
          "off-ratio fails")
    check(not t1_identity_holds(Fraction(0), Fraction(9), 25, rho25),
          "A=0 excluded")
    # C_iv formula at gauge
    polys = t1_poly(Fraction(8), Fraction(9), 25, rho25)
    check(polys["Pfull"].degree() == 3, "Pfull deg")
    check(polys["W"].degree() == 2, "W deg")
    check(polys["E"].degree() == 3, "E deg after cancel")
    check(polys["Pfull"].eval(8) == 0 and polys["Pfull"].eval(9) == 0, "roots")
    # p(0) != 0
    check(polys["Pfull"].eval(0) != 0, "no t=0 root of Pfull")

    # mutations of the identity (sign of nu, swapped roles of rho)
    bad = t1_poly(Fraction(8), Fraction(9), -25, rho25)
    c_wrong = rho25 * 8 * 9
    check(not (bad["E"] - bad["Pfull"].scale(c_wrong)).is_zero(),
          "nu sign mutation detected")
    # drop the nu t Pfull_t W term
    pfull = polys["Pfull"]
    w = polys["W"]
    dropped = (pfull * w).scale(rho25) + (pfull * w.deriv()).shift().scale(25 * rho25)
    check(not (dropped - pfull.scale(c_wrong)).is_zero(),
          "dropped Pfull_t term detected")

    # --- one-step menu completeness ---
    menu = one_step_menu(Fraction(9, 2), 2, 9)
    dirty = [r for r in menu if r["family"] == "dirty"]
    check(len([r for r in menu if r["family"] == "clean-resonant"]) == 0,
          "no clean resonant edge")
    check(len(dirty) == 10, "ten dirty edges at budget 9")
    check(any(r["w"] == Fraction(2, 3) and r["M"] == 3
              and r["witness"]["nu_F"] == 25 and r["lambda"] == 8
              for r in dirty), "displayed cell in menu")
    fitting = [r for r in dirty if r.get("fits_own_P1")]
    check(len(fitting) == 2, "two one-step P1-fitting terminals")
    fit_keys = {(r["w"], r["M"], r["lambda"], r["witness"]["nu_F"])
                for r in fitting}
    check((Fraction(2, 3), 3, 8, 25) in fit_keys, "2/3 terminal fits")
    check((Fraction(3, 4), 4, 8, 17) in fit_keys,
          "3/4 terminal fits own P1 with slack 0")
    # over-budget P1 shapes present as reduced edges but do not fit St 9.4
    over = [r for r in dirty if "P1" in r and not r["fits_own_P1"]]
    check(len(over) == 2, "two P1-shaped over-budget edges")
    check(all(r["M"] == 1 for r in dirty if r["witness"]["eps"] == 1),
          "eps=1 dirty children are M=1")
    # independent divisor scan for the displayed parameters
    l, k, sm, lex, eps = 2, 1, 1, 0, 0
    t = sm + l
    c_p0 = l * (k + lex) - sm
    hits = []
    for e in range(1, 2 * 9 * t + 1):
        if (2 * 9 * t) % e:
            continue
        num = e - (l - eps)
        if num >= 2 * c_p0 and num % c_p0 == 0:
            nu = num // c_p0
            dq = (1 + k + lex) * nu + 1
            dp = eps + nu * (l + sm)
            if l * dq - dp != e:
                continue
            kbar = Fraction(l) * Fraction(9, 2) * dq / e
            if kbar.denominator == 1 and kbar >= 1:
                hits.append(nu)
    check(25 in hits and 7 in hits, "independent E-scan finds nu_F=25 and 7")
    check(sorted(r["witness"]["nu_F"] for r in dirty
                 if r["witness"]["k"] == 1 and r["witness"]["eps"] == 0)
          == [7, 25], "k=1 eps=0 dirty nu_F pair")

    # n-independence: menu is a function of (w,M,budget) only
    check(merge_cell(5)["w_tr"] == merge_cell(11)["w_tr"] == Fraction(9, 2),
          "w_tr constant on AP")
    check(merge_cell(5)["M"] == merge_cell(13)["M"] == 2, "M constant on AP")

    # --- cap-token rejection ---
    for token in CAP_TOKENS:
        thrown = False
        try:
            refuse_cap_tokens([f"--{token}", "10"])
        except SystemExit as exc:
            thrown = str(exc).startswith("CAP_TOKEN_REJECTED")
        check(thrown, f"reject {token}")

    # --- emit stability ---
    payload = emit_payload()
    check(payload["lead_verdict"] == "FAMILY_SURVIVES_FIRST_TRUNK", "lead")
    check(payload["cell_verdict"] == "TRUNK_T1_SURVIVES", "cell")
    check(payload["menu_from_9_2_budget_9"]["displayed_in_menu"], "emit menu")
    check(payload["cap_free"] is True and payload["hard_loop_caps"] == [],
          "cap-free flag")
    check(payload["firewall"]["jc2"] is False, "jc2 firewall")
    check(len(payload["payload_sha256"]) == 64, "payload hash")

    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    rc = main(["--emit", ""])
    sys.stdout = old
    check(rc == 0 and "EMIT_PASS" in buf.getvalue(), "cli emit")

    print(f"TD12_U1_TRUNK_CONSUMER_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
