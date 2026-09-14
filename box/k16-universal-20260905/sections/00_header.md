# UNIFORM lane: (UF) as ONE universal termination problem — the recursion is quadratic with unit pivots on both sides, the connection/residue route yields exactly (UT), the L-side is algebraic (a quartic with a tacnode) with its own resonance-free recursion; no uniform theorem, the obstruction restated, the instrument unchanged

Lane: `k16-universal-series-fable5-20260905`. Fable 5.1. 2026-09-05. Basis `e00b2002`.

**VERDICT: NO uniform-in-t theorem is obtained; (R) is not proved; theorem (T) is not promoted for any new index.**
The universal recursion is written out and its structure proved (quadratic; the L-jets enter each row two orders
late, linearly, with a k-independent pivot); the 0–∞ connection problem is Theorem H's system and its only residue
identity is (UT); eliminating P is algebraic — L is a root of a quartic attached to P with a tacnode at (0, −b) whose
degeneracy is the new pivot — and the t = 2 family is exactly P = −L²/4. All verified against the frozen t = 3, 4, 5
certificates.

```text
REQUESTED  (1) Φ_k explicitly; linear? denominators? the k = 3 resonance vs R_boundary = y·eta/3;  (2) P as the ODE solution
           through the marked jets, 0 vs ∞, a residue/monodromy obstruction?;  (3) eliminate P: the resultant on L, its
           structure;  (4) exact verification at t = 3, 4, 5;  (5) verdict.
ANSWER     (1) Φ_k = [ (k−3) Σ_{i=1}^{k−1} P_i P_{k−i} + Σ_{i=1}^{k} G_i P_{k−i} − R_k ]·2/((k−3)b²): QUADRATIC in the P-coefficients,
               denominators 4b², 4b⁴, 12b⁶, 16b⁸, 120b¹⁰, 1440b¹² (k = 4..9). NEW: l_k, l_{k−1} cancel in row k and row k is LINEAR
               in l_{k−2} with the k-INDEPENDENT pivot −(b/4)(4 eta + 3 b l_2) (Prop. 2.2). The k = 3 compatibility is an identity
               (B·eta enters twice and cancels); it is NOT R_boundary = y·eta/3, which is the SOURCE of the jet linkage P_2 = eta.
           (2) Briot–Bouquet exponents 3 at x = 0 and 4N + 6d at x = ∞ (irrational off the split indices: the ∞-germ is unique and
               convergent); polynomial solution ⟺ that germ is entire ⟺ Theorem H's E_k. The residue theorem for P'/P gives
               2N = 3/2 − 3/(4p) + 3/(32p²) — EXACTLY (UT) — and nothing else (Prop. 3.1).
           (3) L is never differentiated: the eliminant is algebraic (Theorem H's E_k; quasi-homogeneous; no Hankel/Wronskian form).
               Dually (UF) ⟺ Q_P(x, L(x)) ≡ 0 for the quartic Q_P = R − GP − (theta−3)P²: Q_P(0, L) = (3/16)(L+b)²(L²+b²), the
               tacnode is non-degenerate iff 4 eta + 3 b l_2 ≠ 0, a second branch L̃ is a formal solution with the SAME P
               (involution), and the dual recursion L-from-P has a k-independent pivot. P = −L²/4 forces N = 3 (the t = 2 family).
           (4) frozen rows/B/eta/target reproduced (t = 3, 4, 5 exact); bottom-up numerators in J with b-power 0 (only k = 4 is
               non-vacuous: socle degrees 14, 21, 30); dual chart UNIT at t = 3 (mod p; exact in §9) with non-unit negative control.
           (5) No uniform theorem; obstruction restated in three charts (§6); fixed-t instrument unchanged; one new uniform
               handle, OPEN[K16-UF-DEGENERATE-TACNODE].
CUSTODY    4/4 input hashes OK (awk manifest, sha256sum -c); frozen controls_t{3,4,5}_raw.sing reproduced by imap under the identity
           map; every structural claim machine-checked with generic jets to k = 12 (universal_recursion.json: ALL_PASS).
NOTIFY     not warranted (no new index, no exit claim; charge_basis inapplicable).
```
