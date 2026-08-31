# Research lane: R1 two-component splice-colouring census at `n22=1`

You are a bounded primary research lane, not a reviewer. Execute the
cheapest discriminator for the most fragile surviving reducible rank-four
row: row R1 of the provisional component-tree ledger. Do not edit
canonical ledgers, any charged file, or inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md

Your charged input is a frozen read-only copy in `{{LANE_INPUTS}}`; verify
its SHA-256 first and stop on mismatch:

```text
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
```

The ledger is `PROVISIONAL` and under separate hostile review; label every
dependence on it `PROVISIONAL`. Row R1's data (its §4.1 and §5.1): target
branch `B=B1 union B2`, both components `A1`-normalized one-place, meeting
at one affine point, both passing through the single point at infinity
(Chau); one affine `(3,1)` unibranch point (a cusp) on one component,
exactly one `(2,2)` conductor node (`n22=1`), all generic meridians
transpositions in `S4`, Euler packet E1 (`C=A1`, `Q=0`, `n4=0`, `t=1`).

Task, in order:

1. **Enumerate the candidate links at infinity.** The link of `B` at
   infinity is a two-component algebraic link determined by a splice
   (Eisenbud--Neumann) diagram with two arrowheads through the unique
   infinite point. Derive the exact finite parameter space of such
   diagrams consistent with: both components rational one-place, the total
   genus/conductor budget of row R1 (one cusp of the minimal `(2,3)` type
   upward, one ordinary node from the conductor pairing, both charged to
   the correct component), and the Orevkov leftover 0 of E1. Make the
   finiteness bound a proved lemma, not an assumption. If the honest
   parameter space is infinite in a direction (e.g. cabling depth at
   infinity), say so exactly and enumerate the bounded slice that the
   conductor/delta budget licenses.
2. **Build the fundamental-group presentations.** For each diagram, give
   the Wirtinger-type presentation of the link-complement group with both
   meridian classes marked, plus the affine relations at the node and
   cusp, following the same Zariski--van Kampen interface the promoted
   irreducible packets use (individual braid relations; boundary imposes
   their product).
3. **Colour.** For each diagram, count transposition assignments to both
   meridian classes generating full `S4` and respecting the relations,
   with the `(2,2)` pairing charged at the node. Exact linear/group
   computation; reuse the promoted `V4 -> S4 -> S3` split reduction where
   strand counts make direct enumeration expensive.
4. **Report the verdict per diagram**: colourable (R1 survives that
   diagram, with the witness) or empty (that diagram dies). An all-empty
   census provisionally closes row R1 at `n22=1` pending review; any
   colourable diagram is a sharpened surviving target, not an existence
   proof of a curve or map.
5. Write a deterministic pure-stdlib replay
   `ops/block_descent_a1_rank4_r1_splice_coloring_replay.py`, byte-stable
   in normal, `-O`, and `-OO` modes, with at least one documented
   old-pass/new-fail mutation.

Stop conditions: if the proved diagram census exceeds roughly 10,000
diagrams or the colouring exceeds about five minutes on one core, freeze
the enumeration design and report the exact object needing AWS
registration instead of running it. Never run Singular, msolve, any CAS,
or any computation of uncertain duration or memory on this machine.

Write one report and no other file except the named replay script:

```text
xmodel/block-descent-a1-rank4-r1-splice-coloring-census-grok46-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 7,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this lane
asserts no new exit price.
