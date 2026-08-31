# Research lane: ROW-SWEEP — kill the surviving residual rows one by one

You are a bounded primary research lane sweeping the N=4 residual
cage. Surviving rows after wave 10 (all else closed or provisional-
closed): noncoprime pairs `(6,4); (8,2),(8,4),(8,6); (9,3),(9,6)`
plus the leftover `(6,3)` tangential configurations
`(beta_1,T) in {(7,4),(8,3)}` and the nodal `(6,4)` row (returned
to OPEN by the M-INF review's counterexample — which however has an
ordinary TRIPLE point, outside the residual class where every
affine singularity is a double point of two smooth branches).

charged_input=xmodel/d1-degree-bound-sol56-20260831.md
charged_input=xmodel/d1-degree-hostile-review-gpt55-20260831.md
charged_input=xmodel/m-inf-hostile-review-sol56-20260831.md
charged_input=xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
0549dfafe339d20c67fe0d64a0bc713c1e64850013fbaab9f07f654c7fbf8fc2  {{LANE_INPUTS}}/d1-degree-bound-sol56-20260831.md
028b1c03489791f8cd674cc371c8b43c8994784aa65a05c8cfbb6dae269d3129  {{LANE_INPUTS}}/d1-degree-hostile-review-gpt55-20260831.md
8b9fe37f142afeb204d356d49dbb3bf535e59ff14a460851486b586b8ec5022a  {{LANE_INPUTS}}/m-inf-hostile-review-sol56-20260831.md
aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0  {{LANE_INPUTS}}/pi1s4-close-residual-hostile-review-sol56-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

For each row, in this order — (6,4) nodal, (6,3)-(7,4), (6,3)-(8,3),
(8,2), (8,4), (8,6), (9,3), (9,6) — run the full constraint battery
and stop on a kill:

1. Infinity-germ census: with `a = d-n`, enumerate the admissible
   characteristic sequences at infinity (AM/delta-sequence
   constraints; the reviewed contact lemma: contact of a smooth
   tangent germ is a multiple of `a` below beta_1 or equals beta_1),
   computing for each: delta_infty, delta_aff = (d-1)(d-2)/2 -
   delta_infty, M_infty (via the PROMOTED-AS-CORRECTED piece-1
   identity M_emb = mult + beta_h - 1 and cluster sums), and the
   gates (M-INF) `M_infty <= 3d-3` (nodal) and (M-INF-T)
   `M_infty + 2T <= 3d-3` (tangential; PROVISIONAL pending the
   N-A review — type conclusions that use it as CONDITIONAL).
2. Class filter: delta_aff must be realizable ENTIRELY by double
   points of smooth branches (delta_p = k_p): in particular
   delta_aff >= 1; a unibranch or >=3-branch singularity anywhere
   kills the configuration out of the class, NOT the row — track
   the distinction. The banked (6,4) counterexample curve is
   out-of-class; determine whether ANY in-class curve attains its
   infinity type (S_aff = <3,4> forced delta_aff = 3 there — can
   three double points of smooth branches coexist with that
   parametrization structure? derive the double-point scheme).
3. Structural filters from the promoted cage: shapes
   (d/g, n/g) in (u,1)/(odd u,2)/(4,3); `d = 2g_L + c(Pi) + 2`
   with c(Pi) in {2,3} (Pi of order 3 or 4 per promoted Theorem
   A(3) — careful: that was coprime-stratum; use only what the
   promoted block theorems A'(1)-(4) give off it: n|d forces all
   block products equal); `g <= gcd(deg P, deg Q) - 2`; the S_4
   representation constraints at each double point.
4. Verdict per row: KILLED (name the killing gate), SURVIVES-AS
   (the exact residual configurations with all invariants), or
   OPEN (name the missing lemma).

Fail closed; every constraint consumption cited to its integration
or review; conditional items typed as such.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/row-sweep-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
