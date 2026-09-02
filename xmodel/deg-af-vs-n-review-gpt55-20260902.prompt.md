# Hostile review lane: DEG-AF-VS-N — every PROVED-HERE item, the family, the consequences

The charged producer report (Opus 5, flagship) retypes the campaign's
degree gate. Claims (all PROVED-HERE/UNREVIEWED): THEOREM SG-INV (the
semigroup at infinity Gamma of the one-place parametrisation of A_F is
Aut(C^2)-invariant and #gaps = delta_aff); BUDGET=IDENT (the
delta-budget merely computes delta_infty); DEG-DELTA(a) (delta_aff <=
(n-1)(n-2)/2 in every gauge); DEG-DELTA(b) (b_1 | b_0 or
n <= 2 delta_aff + b_1 - 1 <= 3 delta_aff, sharp at (t^2, t^{2d+1}),
consuming the banked (AM-SG)); (R1)-(R4) necessary conditions on a
minimal gauge; MERIDIAN-FLOOR (n_min >= ceil((N-1)/(W - sum s_l)) >=
ceil((N-1)/(W-1)), from the meridian cycle type and transitivity only);
the half of OPEN[N-VS-MAPDEG] this gives; beta <= floor(delta_aff/2) in
(B2) and k <= delta_aff - delta_c in (B3), both delta_infty-free;
2 g(E) = 1 + N nu - n_infty(E); the non-derivability certificate (a
satisfying assignment of every banked constraint at fixed N with
k -> infinity); the explicit family of rational one-place plane curves
with one (2,3) cusp and exactly k nodes (verified k <= 11); the
sharpening of the Chau lane's (B3) list (n = 4, (2,3), k = 1 EMPTY since
delta_aff = 2 forces n_min = 5).
Your task, hostile and computational: CONFIRMED / GAP / REFUTED per item
with the exact line and repair. Mandatory: (1) SG-INV — Aut-invariance
of Gamma under BOTH target automorphisms and reparametrisation, and the
gap-count identity (which classical fact is it, and does it need the
curve to be unibranch at infinity only, or also something at the affine
singularities?); (2) DEG-DELTA(b) — the exact statement of (AM-SG) it
consumes and the Tschirnhausen step; (3) MERIDIAN-FLOOR — reprove it;
check the cycle-type input against CUSP-PARITY/ORBIFOLD-CAGE typings;
(4) the k-node family — verify by your own CAS at k = 2, 3, 5 (degree,
one-place at infinity, exactly one (2,3) cusp, exactly k ordinary nodes,
no other singularity) and check that it satisfies every banked profile
constraint at some fixed N as claimed; (5) the (B2) consequence
beta <= floor(delta_aff/2) and the resulting death condition; (6) the
(B3) list sharpening at n = 4; (7) the literature custody claims (Jelonek
in (deg f, deg g); absence of a curve-degree-by-etale-degree theorem).
Deliver a typed verdict block with a promotion recommendation per item.
Desk-scale CAS only; do not edit canonical ledgers; do not inspect
jc2-lean. For any OPEN you raise, state the quantity it bounds (ops/
open_collision.py contract).
Report: xmodel/deg-af-vs-n-review-gpt55-20260902.md
Seal-at-completion; bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/chau-delta-budget-gpt55-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/b3-e-geometry-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  {{LANE_INPUTS}}/chau-delta-budget-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  {{LANE_INPUTS}}/b3-e-geometry-opus5-20260902.md
```
