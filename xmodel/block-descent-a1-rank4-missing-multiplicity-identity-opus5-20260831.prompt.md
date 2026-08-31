# Research lane: prove or refute the missing-multiplicity fibre identity (2.3)

You are a primary research lane on the single highest-value rank-four
target. Do not edit canonical ledgers, any charged file, or inspect
`jc2-lean`.

**The problem.** Let `F=(f,g):C^2->C^2` be a hypothetical noninvertible
Keller map of geometric degree `N` (for the charged application, the
canonical normalization with `d1=1` and `N=4`). Let `A_F` be the
nonproper-value curve, `B_i` an irreducible component of the reduced branch
`B subset A_F`, and `L_F` the set of dicritical lines at infinity with
Orevkov base multiplicities `mu_l`. Prove or refute:

```text
(2.3)  at a generic closed point z of B_i:
       N = f(z) + sum over the dicritical lines l whose image is B_i of mu_l,
```

where `f(z) = #F^{-1}(z)` counts finite source preimages. Equivalently:
the geometric preimages of a generic point of a branch component that are
missing from the finite fibre are exactly accounted, with multiplicity
`mu_l`, by the dicritical lines mapping onto that component — no missing
multiplicity escapes to boundary places whose image is the point at
infinity rather than `z`.

If (2.3) holds, the provisional Lemma 2.3 of the charged ledger empties
every reducible rank-four branch row and collapses rank four onto the
already promoted irreducible one-place ladder — this is why the lane
exists. If (2.3) fails, exhibit the exact failure mode (a boundary place
contributing to the fibre of `z` without a dicritical image through `B_i`,
or multiplicity leakage at a special point) and state the corrected
identity with proof.

charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
charged_input=xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
charged_input=xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`; read
them there and verify these SHA-256 hashes first, stopping on mismatch:

```text
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f  {{LANE_INPUTS}}/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190  {{LANE_INPUTS}}/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
```

The ledger (first input) is `PROVISIONAL`; you consume only its §0
promoted-constraint list and its exact statement of (2.3) in §2, and your
verdict on (2.3) must not assume its row bookkeeping. The function-pair
integration (third input) is reviewed; its §4 contains the analogous
missing-multiplicity comparison for a cyclic degree-`4mu` replacement —
identify precisely what specializing to `mu=1` does and does not give for
the Keller map itself.

Method requirements:

1. Work on a good compactification of the source where `F` extends; type
   every boundary curve as dicritical (image a curve), polar/constant
   (image the point at infinity), or contracted, and prove the fibre of a
   generic finite point `z` meets the boundary only in dicritical lines
   whose image passes through `z`.
2. Prove the local multiplicity of the extended map along a dicritical
   line at a generic point of its image equals the Orevkov base term
   `mu_l`, or exhibit the discrepancy. Cite Orevkov 1987 Lemma 4.2 and
   Chau's dicritical-image lemma exactly as the packets pin them; check
   both against your own construction, not by name-matching.
3. Address genericity honestly: (2.3) is claimed at generic `z` of each
   component. Show corrections are supported over finitely many `z` and
   cannot be generic, or find the counterexample.
4. Test the cheapest honest control: a non-Keller polynomial map with
   known dicritical structure (for instance a primitive polynomial with a
   nontrivial fibre at infinity) where every quantity is computable by
   hand, and verify your proved identity reproduces its numbers.
5. State the weakest exact hypotheses (Keller needed? etale-ness? `d1=1`?)
   and the exact scope of the conclusion.

Computation rules: desk-scale exact algebra only. Never run Singular,
msolve, any CAS, or any computation of uncertain duration or memory on
this machine; if one seems necessary, record exactly what is blocked and
why instead of running it. Six hours is your hard budget; bank partial
exact lemmas rather than overrunning.

Write one report and no other file:

```text
xmodel/block-descent-a1-rank4-missing-multiplicity-identity-opus5-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 7,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Include a `charge_basis` declaration only if you assert a
genuinely new exit price with a direct mathematical-source citation;
otherwise omit it entirely.
