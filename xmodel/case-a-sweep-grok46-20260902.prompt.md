# Research lane: CASE-A-SWEEP — chart the case-(A) survivors at 8 <= N <= 16

The reviewed CUSP-A-EMPTY (charged transfer report + review):
MPRIME case (A) — A_F a quasi-homogeneous cusp {x^p = y^q},
pi_1 = torus-knot group — is EMPTY for 4 <= N <= 7, first
survivors at N = 8. Your task: chart the survivor structure for
8 <= N <= 16 with the reviewed machinery (CENTRAL-RANK r = j-1;
CUSP-PARITY sgn formulas; ORBIFOLD-CAGE s + s' = M + 2 - j; the
repaired Kurosh divisor structure):
(1) For each N in 8..16, enumerate the admissible
    (p, q, j, M, rho-cycle-data) tuples passing every reviewed
    constraint (exact integer enumeration; python in-lane;
    print counts and the full tuple list verbatim for N = 8, 9;
    counts only for 10..16 with the list in a machine-readable
    appendix).
(2) For the N = 8 survivors: what additional promoted constraint
    (7.B budget, Lemma A/H3, the (K) excess ledger from the
    charged MPRIME report) kills them, if any? Apply each
    honestly; report survivors of the FULL promoted arsenal.
(3) Structure analysis: do survivor counts grow, stabilize, or
    show a killable pattern (parity/congruence)? A conjecture
    with evidence is welcome, TYPED as conjecture.
(4) Controls: re-derive the N <= 7 emptiness with your
    enumerator (must match the reviewed result exactly); one
    deliberately weakened-constraint run showing survivors
    appear (negative control for over-constraining).
Report: xmodel/case-a-sweep-grok46-20260902.md
Seal-at-completion; target 15-25KB.
charged_input=xmodel/homcover-transfer-opus5-20260902.md
charged_input=xmodel/homcover-transfer-review-gpt55-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  {{LANE_INPUTS}}/homcover-transfer-opus5-20260902.md
fadc17c809e72d64a493fc1fb16a739d441474b401f191081303de3b003d7d62  {{LANE_INPUTS}}/homcover-transfer-review-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
```
