# Research lane: NORI-BC — extend Nori's 3.27 to B(C) > 0, or nodalize equisingularly

You are a flagship research lane on the last structural gap of the
N=4 residual: OPEN[PI1S4-TANGENTIAL-NONCOPRIME] (the decision
report's item (ii)). Two independent targets; either closes the
tangential noncoprime cases wherever (M-INF) is verified:

**(ii-b) Nori extension.** Nori, Ann. Sci. ENS 16 (1983), proves
Prop 3.27 for NODAL `D` with `C^2 > 2r(C)`; his own Def 3.25 defines
`A(C;P) = sum of pairwise branch intersection multiplicities` and
`B(C) = C^2 - 2 sum_P A(C;P)`, and his 3.26 proves the `B(C)>0` form
under `C ∩ R = empty`. The obstruction to extending 3.27 verbatim
(per the reviewed decision report) is that its proof needs the
normalization `H` to meet `closure(q^{-1}(R) - H)` transversally,
which fails at `A_{2k-1}` (k>=2). Work through Nori's actual proof
(re-fetch from Numdam, verify hash
`1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45`,
read §3 in full including Lemma 1.4 / the weak Lefschetz apparatus
and 3.26's proof) and determine whether the tangential double-point
case can be pushed through: candidate routes — (a) blow up ONCE at
each tacnode inside his framework (his own p.307 acknowledgement
licenses cusp blow-ups with the `6b+2a` bookkeeping; derive the
tacnode analogue: cost `4k_p` per `A_{2k-1}` point on the
self-intersection and what lands in `E`), and check his hypotheses
survive with the exceptional curves added to `E` — if yes, derive
the resulting inequality and compare with the (B') bookkeeping
already promoted; (b) replace transversality in his Lemma-1.4 step
by a local computation at a tangency (his proof is etale-local —
determine exactly where transversality is consumed); (c) determine
whether his 3.26 (`B(C)>0`, `C ∩ R = empty`) can substitute after
the infinity resolution since our `E = B_infty` might be arranged
disjoint from... type carefully what R is in his setup.

**(ii-a) Equisingular nodalization.** Alternative: for `g>=2`,
construct a locally closed subvariety of `P_{d,n}` through a given
tangential curve on which `delta_infty` is constant and whose
generic member is nodal (the decision report's Lemma 5.3 fails for
`g>=2` because `delta_infty` jumps on `P_{d,n}`); the reviewed
repair direction is an equisingular-at-infinity stratum — construct
it (fix the delta-sequence/cluster at infinity; show the affine
double-point scheme still spreads) and re-run the reviewed transport
argument (with the gate's local intersection-number conservation in
place of Lemma 5.5).

charged_input=xmodel/pi1s4-close-residual-r2-opus5-20260831.md
charged_input=xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  {{LANE_INPUTS}}/pi1s4-close-residual-r2-opus5-20260831.md
aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0  {{LANE_INPUTS}}/pi1s4-close-residual-hostile-review-sol56-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Deliver: (ii-b) proved (with the exact extended statement and its
inequality), or (ii-a) proved, or both typed OPEN at named steps
with all partials proved unconditionally. Every Nori consumption
quoted verbatim with page numbers.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/nori-bc-extension-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
