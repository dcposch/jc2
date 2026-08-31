# Hostile review assignment: R1 splice-colouring census

Act as an independent hostile mathematical referee. Review exactly the R1
splice-colouring census packet named below (producer: Grok 4.6). Do not
promote, edit any charged file, edit canonical ledgers, or inspect
`jc2-lean`.

charged_input=xmodel/block-descent-a1-rank4-r1-splice-coloring-census-grok46-20260831.md
charged_input=ops/block_descent_a1_rank4_r1_splice_coloring_replay.py
charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`. Read
them there. Reproduce these SHA-256 hashes first and stop on mismatch:

```text
5d5b3d1fc1b2f7f57a59ea62c9409bec24e81e80e1e529b47612e5302aae4c11  {{LANE_INPUTS}}/block-descent-a1-rank4-r1-splice-coloring-census-grok46-20260831.md
ebafe10307564b12a17c4875bb8467a912008f46518078afe5c57e0ae1091ea7  {{LANE_INPUTS}}/block_descent_a1_rank4_r1_splice_coloring_replay.py
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

**Critical context.** The third input (the component-tree ledger) is the
census's declared parent, and the fourth input is a hostile review that
REFUTED parts of that ledger: the 16-row bookkeeping and the split rows
are dead, `m<=3` rests on the untyped hypotheses (D1)--(D4), R2/R3 kills
need an unproved premise, and connected mixed `T31/T211` rows were lost.
The finite-`T31` Euler stratum (which contains row R1's Euler packet E1),
the four-forest list conditional on `m<=3`, and the `S22`-not-on-`T31`
rule were CONFIRMED. Your first duty is a dependency audit: identify
exactly which ledger facts the census consumes, and for each, whether it
lies in the refuted, gapped, or confirmed portion. A census conclusion
resting on a refuted ledger fact must be flagged as invalid regardless of
its internal correctness.

Then independently test, recomputing rather than deferring:

1. Lemma 2.1 (the three delta chargings) and its leftover-zero premise —
   note the ledger review showed the E1 leftover argument (unibranch
   critical value) is itself an unproved premise; state what that does to
   the census's licensed-slice claim;
2. Lemma 2.2 (component knots of genus 0/1/2) against the promoted
   one-place interfaces, including the deletion of winding-one steps;
3. Lemma 2.3 (two-arrowhead splice form from Chau's unique infinite
   point, the `T(2,2n)` core, and the honesty of the unbounded linking
   direction) — this is the packet's most delicate topology; check the
   Eisenbud--Neumann/RPI citations do what is claimed for a two-component
   link at infinity without regularity of the union;
4. Lemma 2.5 (trefoil relation excludes disjoint transposition pairs) —
   verify by hand;
5. the stage-A/stage-B colouring protocol: that stage A (product relation
   only) is genuinely necessary, that stage B's individual factors are
   the right Zariski--van Kampen consequences, and that the charged
   pairing normalization `(12)|(34)` does not lose colourings that a
   different transported pairing would admit (the ledger review's
   pair-transport GAP applies here too);
6. the verdict table: recompute the F1 charged count (expected 8, all
   signs and residues, witness `(13),(12),(34)`), the `T(4,6)` control
   (72 stage-A, 0 charged), the F3 and satellite `(2,0)` emptiness, and
   Lemma 2.4's residue-collapse argument;
7. the replay: run it in normal, `-O`, and `-OO` modes (expected stdout
   SHA-256 `36d2d33f...`) and the mutation (must exit nonzero); assess
   what it actually verifies versus hard-codes — the ledger's replay was
   found semantically shallow, so apply the same standard;
8. the scope firewalls: colourable is compatibility, not existence; the
   cubic-plus-line model is a Bézout consistency check, not a curve; the
   higher `A_{2p}` slice is OPEN.

State the weakest exact hypotheses, any correction and blast radius, and
one best next falsification test. Give a per-claim verdict from
`CONFIRMED`, `REFUTED`, `GAP`, with the attack shown.

Computation rules: only the named exact-Python replay and short exact desk
arithmetic. Never run Singular, msolve, any CAS, or any computation of
uncertain duration or memory on this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-rank4-r1-splice-census-hostile-review-gpt55-20260831.md
```

Create the report file with a skeleton of section headers as your first
action and append each completed section as you finish it. Keep it under
roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line. Do
not include a `charge_basis` declaration: this review asserts no new exit
price.
