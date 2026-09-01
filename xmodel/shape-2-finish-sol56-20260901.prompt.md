# Research lane: SHAPE-2-FINISH — the u≡3 (mod 6) residual and the g>=3 inner case

You are a bounded primary research lane finishing family 2 of the
shape cage. The reviewed state (SHAPE-KILL + its review, both
charged): at g=2, (d,n)=(2u,4), u odd — dead unless u ≡ 3 (mod 6),
and in every surviving outer configuration Π is a double
transposition (in V_4), with identity (3.3) on the surviving outer
data; the whole (2u,2) column is dead (Lemma SK-2/2'); g>=3 inner is
OPEN[SHAPE-2-INNER-g>=3].

charged_input=xmodel/shape-kill-uniform-opus5-20260901.md
charged_input=xmodel/shape-kill-hostile-review-grok46-20260901.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
189bc45d83c97df3614c65450a8c6e926938e50f7ccc0b2bacd78a7fd8d11c4d  {{LANE_INPUTS}}/shape-kill-uniform-opus5-20260901.md
0213fcae67bbde4d426a50f2d5d17c71db907d78718860459f14ff50e2ce4a01  {{LANE_INPUTS}}/shape-kill-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Tasks, fail closed: (1) the u≡3(6), g=2 residual: with Π pinned in
V_4 and the (3.3) identity, run the INF-TRIVIAL-style analysis — Π a
double transposition means the S_3-resolvent image of gamma_inf is
TRIVIAL (V_4 = kernel!), so psi descends to pi_1(P^2 - Dbar) exactly
as in ROW-KILL — the branch degree is now 2u+4... wait, derive it:
deg D = d = 2u with u≡3(6), u>=9, so deg >= 18; the Shirane
classification was degree-6; determine the degree-2u analogue: a
normal S_3 triple cover of P^2 with branch degree 2u — the Cardano/
Tokunaga T91 framework gives F = G_a^3 + G_b^2 shapes: derive the
degree constraints (3|deg G_a-type divisibility: 2u = 6k needs
u≡0(3) — and u≡3(6) MEANS u≡3(3)=0(3)! so 2u = 6(u/3): the torus
form is numerically possible — the kill must then come from the
NO-TORUS side: run the torus-type test on the family-2 residual
curves (their delta-sequences/AG-S data at u≡3(6): does an
A^3-B^2=F identity with the required degrees contradict the
infinity germ as in the promoted degree-6 case? The promoted
TRIPLE-COVER-CLOSE §4 valuation bookkeeping generalizes — the germ
orders achievable by 4A^3+27B^2 at a one-place infinity versus the
family's required germ — work it at general u≡3(6)); (2) the g>=3
inner case: type exactly what SK-2's fixedness argument needs and
whether the inner cable at g>=3 admits an analogous pinning (the
review noted a trivial-product block is not B_g-fixed at g>=3 —
find the correct invariant); (3) verdict per case: KILLED uniformly
/ pinned further / OPEN at a named tool.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 5 hours hard budget.

Write one report and no other file:

```text
xmodel/shape-2-finish-sol56-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
