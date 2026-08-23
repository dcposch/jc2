"""Tests for the Conjecture E rig (lib/conjE.py).

(a) sanity gate: a known honest pair realizing instance P1 -- Conjecture E's
    hypotheses and conclusion must both check out there, plus a negative
    control and a symbolic/fixture cross-path identity;
(b) the smallest-instance sweep from conjectureE-plan.md section 2
    (writes runs/conjE_results.txt).

Output discipline: only aggregate counts/statuses are printed.
"""
import os, sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from conjE import (Instance, Model, binom_frac, run_gate, run_sweep,
                   ptrunc, pmul, canon, xpoly_to_z)

def test_binomial_series():
    # C(1/2,k) and C(-1/2,k) against hand values ((1+t)^{+-1/2} truncations)
    half = [Fraction(x) for x in ("1", "1/2", "-1/8", "1/16", "-5/128")]
    mhalf = [Fraction(x) for x in ("1", "-1/2", "3/8", "-5/16", "35/128")]
    for k in range(5):
        assert binom_frac(Fraction(1, 2), k) == half[k]
        assert binom_frac(Fraction(-1, 2), k) == mhalf[k]
    print("binomial coefficients OK")

def test_hpow_identities():
    # formal-layer consistency: H^1 = H;  H^{1/2}*H^{1/2} = H;  H^{3/2} = H*H^{1/2}
    for i in (4, 3):     # one u=0 and one u=1 instance
        inst = Instance(2, 3, 2, 4, 1, i)
        H = ptrunc(inst.build_H(), inst.mfr)
        assert ptrunc(inst.hpow(Fraction(1)), inst.mfr) == H
        h12 = inst.hpow(Fraction(1, 2))
        sq = ptrunc(pmul(h12, h12), inst.mfr)
        assert {k: c for k, c in sq.items() if canon(c)} == \
               {k: c for k, c in H.items() if canon(c)} or _cmp(sq, H)
        h32 = inst.hpow(Fraction(3, 2))
        prod = ptrunc(pmul(H, h12), inst.mfr)
        assert _cmp(prod, h32)
    print("H^A series identities OK")

def _cmp(p, q):
    keys = set(p) | set(q)
    for k in keys:
        a, b = p.get(k, {}), q.get(k, {})
        mons = set(a) | set(b)
        for m in mons:
            if Fraction(a.get(m, 0)) != Fraction(b.get(m, 0)):
                return False
    return True

def test_instance_table():
    # the verified table in conjectureE-plan.md section 2
    want = {  # i: (u, d, e, mfr, Bmax, uE, vE, uF, vF)
        0: (0, 4, 6, 8, (2, 4, 6, 8), 1, 2, 0, -1),
        1: (1, 6, 9, 12, (3, 6, 9, 12), 1, 3, 1, 2),
        2: (0, 4, 6, 8, (2, 4, 6, 8), 1, 2, 1, 1),
        3: (1, 6, 9, 12, (3, 6, 9, 12), 1, 3, 2, 3),
        4: (0, 4, 6, 8, (2, 4, 6, 8), 1, 2, 2, 2),
    }
    for i, w in want.items():
        t = Instance(2, 3, 2, 4, 1, i)
        got = (t.u, t.d, t.e, t.mfr, t.Bmax, t.uE, t.vE, t.uF, t.vF)
        assert got == w, f"instance table mismatch at i={i}: {got} != {w}"
    # paper's own worked example: (2,3,4,8), delta=1, i=15
    t = Instance(2, 3, 4, 8, 1, 15)
    assert (t.u, t.d, t.e, t.uE, t.vE, t.uF, t.vF) == (1, 12, 18, 2, 6, 4, 7), \
        "cross-check against the paper's example failed"
    print("instance tables OK (incl. paper example (2,3,4,8), i=15)")

def test_xpoly_to_z():
    assert xpoly_to_z([0, 0, 0, 1]) == [-1, 3, -3, 1]   # x^3 -> (z-1)^3
    assert xpoly_to_z([1, 1]) == [0, 1]                 # 1+x -> z
    print("chart shift OK")

def test_gate():
    out = run_gate(log=lambda s: print(s))
    assert out["Bmax_supported"], "gate: honest pair must be supported (Magnus)"
    assert out["residual_nonzero"] == 0, "gate: supported identities must vanish"
    assert out["conclusion_P1_zero"], "gate: E-conclusion must hold at fixture"
    assert out["negative_control_unsupported"], "gate: negative control failed"
    assert out["cross_path_ok"], "gate: symbolic/fixture cross-path mismatch"
    assert out["gate_pass"]
    print("gate (a) OK: E HOLDS at the honest-pair configuration")

def test_sweep():
    gate, records = run_sweep(log=lambda s: print(s))
    assert gate["gate_pass"]
    # 7 rows: i=0 degenerate + (i,ell) in {(1,1),(1,2),(2,1),(3,2),(3,3),(4,2)}
    assert len(records) == 7, f"expected 7 instance rows, got {len(records)}"
    got = {(r["i"], r["ell"]): r["verdict"] for r in records}
    assert got[(0, None)] == "degenerate", "i=0 must be reported degenerate"
    for key in [(1, 1), (1, 2), (2, 1), (3, 2), (3, 3), (4, 2)]:
        assert key in got, f"missing sweep instance {key}"
        assert got[key] != "undecided", f"instance {key} undecided (solver issue)"
    # msolve -g can short-circuit a characteristic-zero `[1]` after its first
    # prime.  The six solver-only rows therefore stay trace-supported, not HOLD.
    assert got[(4, 2)] == "modular-trace-support", \
        "primary instance P1 must not be promoted without a Q certificate"
    assert all(got[key] == "modular-trace-support" for key in
               [(1, 1), (1, 2), (2, 1), (3, 2), (3, 3), (4, 2)])
    n_h = sum(1 for r in records if r["verdict"] == "holds")
    n_d = sum(1 for r in records if r["verdict"] == "degenerate")
    print(f"sweep (b) OK: {len(records)} instances, holds={n_h}, "
          f"degenerate={n_d}, other={len(records)-n_h-n_d}")

if __name__ == "__main__":
    test_binomial_series()
    test_hpow_identities()
    test_instance_table()
    test_xpoly_to_z()
    test_gate()
    test_sweep()
    print("ALL CONJE TESTS PASS")
