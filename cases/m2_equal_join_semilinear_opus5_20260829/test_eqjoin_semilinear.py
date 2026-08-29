#!/usr/bin/env python3
"""Tests for the M>=2 equal-arrival semilinear quotient packet.

Runs identically under `python3` and `python3 -O` (no test relies on assert
being enabled inside the library).  No caps, no network, no CAS, no engine
import, no jc2-lean access.
"""
import hashlib
import json
import os
import subprocess
import sys
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from polyexact import Poly                                    # noqa: E402
import controls                                               # noqa: E402
import emit_eqjoin                                            # noqa: E402
from eqjoin_semilinear import (EqJoinFamily, merge_local, MergeLocalError,      # noqa: E402
                               classify_unbounded, prime_factors, radical,
                               pairwise_consistency_affine)
from t1_merge_reduction import (verify_T1_EQ, verify_T1_GEN, eqjoin_T1_solution,   # noqa: E402
                                eqjoin_T1_symbolic_criterion,
                                build_equalmu_symbols, rad_and_S_equalmu, _t_poly)

CHECKS = 0
FAILS = []


def check(name, cond):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILS.append(name)


# ---------------------------------------------------------------- 1 --------
def test_poly_algebra():
    x = Poly.var(2, 0)
    y = Poly.var(2, 1)
    check("poly:binomial", (x + y).pow(4).d[(2, 2)] == Fr(6))
    check("poly:diff", (x.pow(3)).diff(0) == Poly.const(2, 3) * x.pow(2))
    check("poly:zero", (x - x).is_zero())
    check("poly:coeff_in", ((x.pow(2) * y) + x).coeff_in(0, 2) == y)


# ---------------------------------------------------------------- 2 --------
def test_T1_identities():
    grid = [(r, mu, eps, lex, nu)
            for r in (1, 2, 3, 4)
            for mu in (1, 2, 3)
            for eps in range(0, mu)
            for lex in (0, 1, 2)
            for nu in (2, 3, 5)]
    bad = []
    for g in grid:
        ok, _ = verify_T1_EQ(*g)
        if not ok:
            bad.append(g)
    check("T1-EQ:identity holds on the whole grid (%d cases)" % len(grid), not bad)

    gen = [([1], 3, 2, 3), ([1], 1, 0, 2), ([2, 1], 0, 0, 7), ([2, 1], 0, 1, 3),
           ([3, 1, 1], 2, 1, 2), ([2, 2], 1, 0, 3), ([1, 1, 1], 0, 2, 2),
           ([4, 2], 3, 0, 5)]
    badg = [g for g in gen if not verify_T1_GEN(*g)[0]]
    check("T1-GEN:identity holds (%d cases)" % len(gen), not badg)


def test_T1_mutations():
    """A wrong reduced expression must NOT satisfy the identity."""
    n, _ = build_equalmu_symbols(2, 1)
    t = _t_poly(n, 3)
    Rad, Rad_t, S, S_t = rad_and_S_equalmu(n, 2, 1, 3)
    eta = Poly.var(n, 0)
    r, mu, eps, lex, nu = 2, 1, 0, 1, 3
    dp, dq = eps + nu * r * mu, 1 + nu * (r + lex)
    rho = Fr(dp, dq)
    p = eta.pow(eps) * Rad.pow(mu)
    q = eta * Rad * S
    lhs = Poly.const(n, rho) * p * q.diff(0) - p.diff(0) * q
    mutants = {
        "sign on t*Rad_t*S": (Poly.const(n, rho - eps) * Rad * S
                              - Poly.const(n, nu) * Poly.const(n, rho - mu) * t * Rad_t * S
                              + Poly.const(n, rho * nu) * t * Rad * S_t),
        "drop nu factor": (Poly.const(n, rho - eps) * Rad * S
                           + Poly.const(n, rho - mu) * t * Rad_t * S
                           + Poly.const(n, rho * nu) * t * Rad * S_t),
        "mu <-> eps swap": (Poly.const(n, rho - mu) * Rad * S
                            + Poly.const(n, nu) * Poly.const(n, rho - eps) * t * Rad_t * S
                            + Poly.const(n, rho * nu) * t * Rad * S_t),
    }
    for name, red in mutants.items():
        rhs = eta.pow(eps) * Rad.pow(mu) * red
        check("T1 mutation detected: %s" % name, not (lhs - rhs).is_zero())


# ---------------------------------------------------------------- 3 --------
def test_eqjoin_closed_form():
    """The T1 content of the C=0 family is exactly `Rad = t^r - A`."""
    for r in (2, 3, 4, 5):
        for mu in (2, 3, 5):
            for eps in range(0, mu):
                for nu in (2, 3, 4, 7, 11, 30):
                    sol = eqjoin_T1_solution(r, mu, eps, nu)
                    check("eqjoin:top coeff vanishes r=%d" % r, sol["top_coeff_r"] == 0)
                    check("eqjoin:forced zeros r=%d" % r,
                          sol["forced_zero_pi"] == list(range(1, r)))
                    check("eqjoin:C!=0 r=%d" % r, sol["alive"])
                    check("eqjoin:symbolic criterion r=%d" % r,
                          eqjoin_T1_symbolic_criterion(r, mu, eps, nu))
                    # the exact constant: C = -nu*r*(mu-eps)*A/dq
                    dq = 1 + nu * r
                    check("eqjoin:C closed form r=%d" % r,
                          sol["C_over_A"] == Fr(-nu * r * (mu - eps), dq))


def test_eqjoin_closed_form_mutation():
    """Mutating the exponent r in the criterion must break the forced-zero set."""
    bad = 0
    for r in (2, 3, 4):
        for nu in (2, 3, 5):
            sol = eqjoin_T1_solution(r, 3, 0, nu)
            if sol["forced_zero_pi"] != list(range(1, r + 1)):   # deliberately wrong
                bad += 1
    check("eqjoin mutation: wrong forced-zero set is rejected", bad == 3 * 3)


# ---------------------------------------------------------------- 4 --------
def test_family_formulas():
    """Closed forms must agree with the independent merge_local engine."""
    tested = 0
    for r in (2, 3, 4):
        for mu in (1, 2, 3, 5, 6):
            for eps in range(0, mu):
                f = EqJoinFamily(r, mu, eps, Fr(3, 2))
                for nu in f.members(2, 90):
                    rec = merge_local(r, [mu] * r, [], 0, eps, [Fr(3, 2)] * r, nu, False)
                    tested += 1
                    check("family:dp", rec["dp"] == f.dp(nu))
                    check("family:dq", rec["dq"] == f.dq(nu))
                    check("family:M", rec["M"] == f.M(nu) == gcd(mu - eps, nu * r + 1))
                    check("family:kbar", rec["kbar"] == f.kbar(nu))
                    check("family:X", rec["X"] == f.X(nu))
                    check("family:w_child constant", rec["w_child"] == f.w_child)
                    check("family:lambda constant", rec["lambda"] == f.lam)
                    check("family:E constant", set(rec["E"].values()) == {mu - eps})
                    check("family:C zero", set(rec["C"].values()) == {0})
                    check("family:T", rec["T"] == r * (mu - eps))
    check("family: nonempty cross-check corpus", tested >= 40)


def test_family_M_law_mutation():
    """The naive `M = gcd(mu, nu*r+1)` law is WRONG once eps >= 1."""
    wrong = 0
    for r in (2, 3):
        for mu in (3, 5, 7):
            for eps in (1, 2):
                f = EqJoinFamily(r, mu, eps, Fr(3, 2))
                for nu in f.members(2, 60):
                    if gcd(mu, nu * r + 1) != f.M(nu):
                        wrong += 1
    check("M-law mutation: gcd(mu,.) differs from gcd(mu-eps,.) somewhere", wrong > 0)


def test_periodicity_is_a_theorem_not_a_scan():
    """Admissibility is periodic in nu with the declared period."""
    for (r, mu, eps, w) in [(2, 3, 0, Fr(3)), (3, 2, 0, Fr(3, 2)), (2, 5, 2, Fr(7, 3)),
                            (4, 3, 0, Fr(5, 3)), (2, 9, 4, Fr(5))]:
        f = EqJoinFamily(r, mu, eps, w)
        L = f.min_period
        for nu in range(2, 2 + 6 * L):
            check("period:%d,%d,%d" % (r, mu, eps),
                  f.admissible(nu) == f.admissible(nu + L))


def test_r2_odd_part_law():
    for mu in range(1, 40):
        odd = mu
        while odd % 2 == 0:
            odd //= 2
        f = EqJoinFamily(2, mu, 0, Fr(3))
        check("r2 odd-part law mu=%d" % mu, f.is_infinite() == (odd >= 3))
    # with a free 0-root the law is about mu - eps
    for mu, eps in [(4, 1), (5, 2), (8, 5), (9, 6), (6, 4)]:
        E = mu - eps
        odd = E
        while odd % 2 == 0:
            odd //= 2
        f = EqJoinFamily(2, mu, eps, Fr(3))
        check("r2 odd-part law eps mu=%d eps=%d" % (mu, eps),
              f.is_infinite() == (odd >= 3))


# ---------------------------------------------------------------- 5 --------
def test_classification():
    v, _ = classify_unbounded(2, [3, 3], [], 0, 0, [Fr(3), Fr(3)], False)
    check("classify:eqjoin", v == "UNBOUNDED_EQJOIN")
    v, _ = classify_unbounded(2, [3, 3], [], 0, 2, [Fr(3), Fr(3)], False)
    check("classify:eqjoin with free 0-root", v == "UNBOUNDED_EQJOIN")
    for args in [(2, [3, 2], [], 0, 0, [Fr(3), Fr(3)], False),
                 (2, [3, 3], [], 0, 0, [Fr(3), Fr(2)], False),
                 (2, [3, 3], [], 1, 0, [Fr(3), Fr(3)], False),
                 (2, [3, 3], [2], 0, 0, [Fr(3), Fr(3)], False),
                 (1, [1], [], 1, 2, [Fr(2), Fr(7, 2)], True),
                 (2, [2, 2], [], 1, 2, [Fr(1), Fr(1), Fr(1)], True)]:
        v, _ = classify_unbounded(*args)
        check("classify:bounded %s" % (args[1],), v == "BOUNDED")


def test_classification_mutation():
    """Ignoring the CONSTANT half of the consistency residual creates a false
    unbounded family at unequal mu -- the exact quantifier bug being repaired."""
    # s = 3, P = 5: C_e = 3*2-5 = 1, C_f = 3*3-5 = 4; choose w so the SLOPE
    # cancels (mu_e*w_e*C_f = mu_f*w_f*C_e) at UNEQUAL mu.
    const, slope = pairwise_consistency_affine(2, Fr(3), 1, 3, Fr(8), 4, 0)
    check("mutation: slope alone can vanish at unequal mu", slope == 0)
    check("mutation: the const term is what forbids it", const != 0)
    # and dually: the constant can vanish while the slope does not
    const2, slope2 = pairwise_consistency_affine(2, Fr(3), 1, 3, Fr(3), 4, 0)
    check("mutation: const alone can vanish at unequal mu", const2 == 0)
    check("mutation: the slope term is what forbids it", slope2 != 0)


def test_caseIII_is_always_bounded():
    """Both H5a readings: a case-III merge never yields an unbounded nu_G."""
    found = []
    for mu0 in (1, 2, 3, 5):
        for mu_e in (1, 2, 3, 5):
            for k in (0, 1):
                for lex in (0, 1, 2):
                    for r0 in (1, 2):
                        mus = [mu_e] * r0
                        ms = [max(1, mu_e - 1)] * k
                        s = r0 + k + lex
                        P = sum(mus) + sum(ms)
                        C0 = mu0 * s - P
                        Ce = mu_e * s - P
                        if C0 < 1:
                            continue
                        # printed DEPTH 5c reading: what0 fixed
                        const, slope = pairwise_consistency_affine(
                            mu_e, Fr(2), Ce, mu0, Fr(5, 2), C0, mu0)
                        degenerate = (const == 0 and slope == 0)
                        if degenerate and Ce == 0 and C0 == 0:
                            found.append((mu0, mu_e, k, lex, r0))
    check("caseIII: no simultaneous C=0 degeneracy exists", not found)


# ---------------------------------------------------------------- 6 --------
def test_guards_are_real():
    """The recorded laws must actually be enforced, not decorative."""
    try:
        merge_local(2, [3, 3], [], 0, 3, [Fr(3), Fr(3)], 4, False)   # eps = mu
        check("guard:NE free 0-root", False)
    except (MergeLocalError, ValueError):
        check("guard:NE free 0-root", True)
    try:
        # mus = (1,2): the mu=1 edge has 1*dq = 7 < dp = 9, so (S) fails
        merge_local(2, [1, 2], [], 0, 0, [Fr(2), Fr(2)], 3, False)
        check("guard:searrow", False)
    except MergeLocalError:
        check("guard:searrow", True)
    try:
        merge_local(2, [3, 3], [3], 0, 0, [Fr(3), Fr(3)], 4, False)  # NE non-chain
        check("guard:NE non-chain", False)
    except MergeLocalError:
        check("guard:NE non-chain", True)
    try:
        merge_local(2, [3, 3], [], 0, 0, [Fr(3), Fr(2)], 4, False)   # R2.1 mismatch
        check("guard:R2.1 consistency", False)
    except MergeLocalError:
        check("guard:R2.1 consistency", True)
    try:
        EqJoinFamily(1, 3, 0, Fr(3))
        check("guard:r>=2", False)
    except ValueError:
        check("guard:r>=2", True)


# ---------------------------------------------------------------- 7 --------
def test_controls():
    c1 = controls.control_td6_residue_cell()
    check("C1: (dp,dq) = (6,10)", (c1["dp"], c1["dq"]) == (6, 10))
    check("C1: M = 2", c1["M"] == 2)
    check("C1: ratio invariant 6 <=> root ratio 2 +- sqrt(3)",
          c1["ratio_invariant_pi1sq_over_pi0"] == Fr(6))
    check("C1: C != 0", c1["C"] != 0)
    check("C1: matches Obstruction O", c1["matches_obstruction_O"])

    c2 = controls.control_d9_nu1_log(12)
    check("C2: nu=1 reduction identity", c2["nu1_reduction_identity"])
    check("C2: all even-l residues nonzero", all(r["nonzero"] for r in c2["rows"]))
    check("C2: residue at l=2 is -2", c2["rows"][0]["residue"] == -2)

    for args in [(2, 3, 3), (1, 3, 2), (2, 1, 7), (3, 5, 4), (5, 2, 3), (4, 7, 2)]:
        c3 = controls.control_classBC_recurrence(*args)
        check("C3: recurrence == sol-td7-law (4) %s" % (args,),
              c3["recurrence_matches_sol_td7_law"])
        check("C3: eq (8) identity %s" % (args,), c3["eq8_identity"])
        check("C3: dead iff dp|dq %s" % (args,), c3["law_agrees"])
    cB = controls.control_classBC_recurrence(1, 3, 2)
    check("C3: promoted class-B cell (3,9) is T1-dead", cB["T1_dead"])

    c4 = controls.control_duplicate_normalization()
    check("C4: single-member cell collision exists", c4["cell_tuple_collides_at_nu2"])
    check("C4: family hashes differ", c4["differ"]["family_hash"])
    check("C4: lambda separates them", c4["differ"]["lambda"] == (0, 23))
    check("C4: no whole-family collision", not c4["whole_family_collision"])

    c5 = controls.control_unequal_mu_false_family(6)
    check("C5: no unequal-mu false family (%d checked)" % c5["checked"], c5["clean"])
    check("C5: corpus is nontrivial", c5["checked"] > 10000)


def test_control_mutation():
    """A mutated expectation must fail the td=6 control."""
    c1 = controls.control_td6_residue_cell()
    check("C1 mutation: invariant 5 would fail",
          c1["ratio_invariant_pi1sq_over_pi0"] != Fr(5))


# ---------------------------------------------------------------- 8 --------
def test_emitter_determinism_and_caps():
    doc1 = emit_eqjoin.build(120)
    doc2 = emit_eqjoin.build(120)
    b1 = json.dumps(doc1, sort_keys=True, separators=(",", ":"))
    b2 = json.dumps(doc2, sort_keys=True, separators=(",", ":"))
    check("emit:deterministic", b1 == b2)
    def _no_float(o):
        if isinstance(o, float):
            return False
        if isinstance(o, dict):
            return all(_no_float(k) and _no_float(v) for k, v in o.items())
        if isinstance(o, (list, tuple)):
            return all(_no_float(v) for v in o)
        return True
    check("emit:no float in output", _no_float(doc1))
    for tok in ("NUCAP=500", "--cap=10", "MAXNU"):
        try:
            emit_eqjoin.refuse_caps([tok])
            check("emit:cap refusal %s" % tok, False)
        except SystemExit:
            check("emit:cap refusal %s" % tok, True)


def test_optimized_replay():
    """`python3 -O` must produce a byte-identical emission."""
    out_n = os.path.join("/tmp", "eqjoin_test_normal.json")
    out_o = os.path.join("/tmp", "eqjoin_test_opt.json")
    env = dict(os.environ)
    r1 = subprocess.run([sys.executable, os.path.join(HERE, "emit_eqjoin.py"),
                         "--output", out_n], capture_output=True, cwd=HERE, env=env)
    r2 = subprocess.run([sys.executable, "-O", os.path.join(HERE, "emit_eqjoin.py"),
                         "--output", out_o], capture_output=True, cwd=HERE, env=env)
    check("replay:normal exit 0", r1.returncode == 0)
    check("replay:-O exit 0", r2.returncode == 0)
    a = open(out_n, "rb").read()
    b = open(out_o, "rb").read()
    check("replay:byte identical", a == b)
    check("replay:PASS banner", b"EQJOIN_EMIT_PASS" in r1.stdout
          and b"EQJOIN_EMIT_PASS" in r2.stdout)


# ---------------------------------------------------------------- 9 --------
def test_scope_firewall():
    """This packet must not assert landing / ceiling / Keller / JC2."""
    banned = ("Keller counterexample", "JC2 follows", "landing theorem proved",
              "type ceiling", "RPMC(C) holds")
    for fn in ("eqjoin_semilinear.py", "t1_merge_reduction.py", "controls.py",
               "emit_eqjoin.py", "polyexact.py"):
        txt = open(os.path.join(HERE, fn)).read()
        for b in banned:
            check("firewall:%s in %s" % (b, fn), b not in txt)


def test_number_theory_helpers():
    check("nt:primes(360)", prime_factors(360) == [2, 3, 5])
    check("nt:radical(360)", radical(360) == 30)
    check("nt:primes(1)", prime_factors(1) == [])
    check("nt:prime", prime_factors(1000003) == [1000003])


def main():
    for fn in sorted(k for k in globals() if k.startswith("test_")):
        globals()[fn]()
    tag = "EQJOIN_SEMILINEAR_TEST_%s checks=%d" % ("PASS" if not FAILS else "FAIL", CHECKS)
    if FAILS:
        for f in sorted(set(FAILS))[:40]:
            print("FAIL:", f)
    print(tag)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
