# Research lane: reducible rank-four branch component-tree ledger

You are a bounded primary research lane, not a reviewer. Build the exact
finite ledger of reducible branch-component configurations still admissible
for a hypothetical rank-four proper-block plane Keller counterexample, and
kill every row that an already promoted theorem closes. Do not edit
canonical ledgers, any charged file, or inspect `jc2-lean`.

Read your context from the repository at the recorded basis; start from:

- `xmodel/block-descent-a1-genus-three-combined-hostile-review-packet-20260831.md`
  and `xmodel/block-descent-a1-genus-four-cable-b1-hostile-review-packet-20260831.md`
  (curated frozen context for the promoted genus-three and genus-four
  `b1=1` row closures, and the rank-four `S4` frontier integration
  `5d7df7ce...` they cite);
- the top current-state section of `AUDIT.md` (2026-08-30/31 entries) for
  the promoted constraints: every rank-four proper block has `G=S4`
  monodromy, `b1(B)>=1`, at least one `(2,2)` conductor fibre,
  `n22>=h-k+1`, `m>=2h-1`; the all-degree theorem that some reduced branch
  component has nontrivial `pi1`; and the one-node meridional obstruction
  with its exact scope;
- the newest `LIVE STATE` block in `notes.md` for what is promoted versus
  provisional. The genus-ladder conductor exclusions and the one-cusp
  Poisson narrowing are `PROVISIONAL`; if you use them, label the
  dependence `PROVISIONAL` and keep a variant row alive without them.

The irreducible one-place census does not transfer through the
normalization-fibre formula — that is exactly why this lane exists. Task,
in order:

1. Fix the exact combinatorial type of a reducible charged branch: number
   of components, each component's normalization genus, places at and away
   from infinity, affine singularity budget, and its meridional `S4` image,
   all constrained by the saturated Orevkov--Chau budget and the promoted
   fibre and Euler ledgers cited above. Derive the finite bound that makes
   the ledger finite, and state it as an exact lemma with proof.
2. Enumerate the resulting component trees exactly. For each row record:
   the per-component data, the tree of intersections, which promoted or
   provisional theorem (if any) kills it, and the exact citation.
3. For surviving rows, rank them by apparent fragility and name the single
   cheapest discriminator computation or lemma per row.
4. Keep transposition-versus-nonsimple inertia distinctions explicit; the
   promoted one-node obstruction charges only simple covers of degree at
   least four in its stated scope — do not overapply it.

Stop conditions: if the exact enumeration cannot be bounded by a proved
lemma, report the precise unbounded direction and stop rather than
truncating silently; if any check needs more than desk-scale exact
computation, freeze its design for AWS registration instead of running it.
Never run Singular, msolve, any CAS, or any uncertain-duration computation
on this machine. You may write one deterministic pure-stdlib enumeration
script as `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py`,
passing normal, `-O`, and `-OO`, with a documented mutation control.

Write one report and no other file except the named replay script:

```text
xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 7,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this lane
asserts no new exit price.
