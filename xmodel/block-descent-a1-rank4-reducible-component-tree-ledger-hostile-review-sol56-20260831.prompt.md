# Hostile review assignment: rank-four reducible component-tree ledger

Act as an independent hostile mathematical referee. Review exactly the
reducible component-tree ledger packet named below (producer: Grok 4.6).
Do not promote it, edit any charged file, edit canonical ledgers, or
inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
charged_input=ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`. Read
them there. Before mathematical reading, reproduce these SHA-256 hashes
against the frozen copies and stop on any mismatch:

```text
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
81ed58e39ddc29a5f8ddc27e10c7cc9ab93602a080800da5b5bbf0c940374066  {{LANE_INPUTS}}/block_descent_a1_rank4_reducible_tree_ledger_replay.py
```

You may additionally read, from the live repository for interface
checking only: the current-state block of `AUDIT.md`, the rank-four `S4`
integration and Euler-ledger packets the report cites in its §0, and the
one-node review report. The charged bytes under review are only the two
frozen inputs.

Independently test, recomputing rather than deferring:

1. **The consumed-interface list (§0).** Verify every promoted constraint
   the report consumes is actually promoted at the scope used, and that
   provisional items (genus ladder, one-cusp Poisson — since promoted, and
   Lemma 2.3 itself) are correctly labeled and non-load-bearing where
   claimed. Flag any constraint used beyond its charged scope.
2. **Lemma 2.1 (Euler packet).** Recompute the nonnegative integer
   solutions of both Euler equations; check the three E-rows are exhaustive
   at `h=1` and the `sigma <= n4+(m-h)` forest estimate.
3. **Lemma 2.2 (`m<=3`).** The load-bearing chain is: every component of
   `A_F` is a dicritical image (Chau 2004 Lemma 1); each carries `mu_l>=1`;
   Orevkov's identity bounds `sum mu_l <= N-1 = 3`. Check each link against
   the packets' pinned statements, and hunt for a component of `B` realized
   only by a dicritical of multiplicity zero or shared dicritical images
   (two components, one line) that would break the count.
4. **Lemma 2.3 and its honesty.** Verify the report correctly types the
   identity (2.3) as an OPEN gap, that no row kill outside R2/R3/R15/R16
   silently uses it, and that the summation argument from (2.3) to `m=1`
   is exact (companion-sheet floor `f(B_i)>=1`, fibre census `f<=u_i`).
5. **The forest list and inertia screen.** Confirm T2/T3path/T3star/T3split
   is the complete forest list on `m<=3`, the `S22`-on-`T211`-only rule,
   the pair-aligned versus overlapping generation facts in `S4`, and rows
   R15/R16.
6. **The unbounded-family honesty.** Check `n22` really is
   Euler-cancelled and Orevkov-free, so the ledger's finiteness claim is
   about trees and inertia types only, with no silent truncation.
7. **The replay.** Run
   `python3 {{LANE_INPUTS}}/block_descent_a1_rank4_reducible_tree_ledger_replay.py`
   in normal, `-O`, and `-OO` modes (expected stdout SHA-256
   `54df64d29d363581...`) and all three documented mutations (each must
   exit nonzero). Confirm the replay checks what the report says it checks
   and no more.

Actively seek: a fifth incidence forest; an Euler row lost by the signed
`e(T31)` replacement; a shared-dicritical breakdown of `m<=3`; an
over-application of the one-node theorem; a hidden use of (2.3); and a
`(2,2)`-pairing configuration on `T31` support that the screen misses.
State weakest exact hypotheses, any correction and blast radius, and the
single best next falsification test. Give a per-claim verdict from
`CONFIRMED`, `REFUTED`, `GAP`, with the attack shown.

Computation rules: only the named exact-Python replay and short exact desk
arithmetic. Never run Singular, msolve, any CAS, or any computation of
uncertain duration or memory on this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 6,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this review
asserts no new exit price.
