# Acquisition lane: decide OPEN[B0-N4-REDUCIBLE-PI1]

You are a literature acquisition-and-check lane on the campaign's
cheapest decisive item. The boxed lemma:

> Let `D ⊂ C^2` be an irreducible affine plane curve whose
> normalization is `A^1` or `C^*`, all of whose affine branches are
> smooth (double points of smooth branches allowed, tangency NOT
> excluded). Is `pi_1(C^2 - D)` abelian?
>
> Weaker sufficient form (all that is needed): no surjection
> `pi_1(C^2-D) -> S_4` sends every meridian of `D` to a transposition
> with the two local meridians at each double point mapping to
> DISJOINT transpositions.

A YES (either form) closes B0 at `N=4` unconditionally, promotes
`A_F=B` at rank four, and completes the (M) programme in both classes.

charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
charged_input=xmodel/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  {{LANE_INPUTS}}/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

Tasks, fail closed:

1. Acquire and hash: Deligne, Sem. Bourbaki 543 (1979/80) "Le groupe
   fondamental du complement d'une courbe plane n'ayant que des points
   doubles ordinaires est abelien"; Fulton, Ann. of Math. 111 (1980)
   407-409; Nori, Ann. Sci. ENS 16 (1983) 305-344 (weak Lefschetz /
   `C^2 > 2 sum` abelianness). Record exact statements with hypotheses.
2. The two flagged caveats, from the charged report §6: (a) these are
   PROJECTIVE nodal statements — our `D` is affine with one place at
   infinity, so `bar D ∪ L_infty` is generally NOT nodal at the
   infinity point; determine precisely what each theorem gives for
   `pi_1(C^2-D) = pi_1(P^2 - (bar D ∪ L_infty))`-adjacent groups
   (Nori's local versions and his Weak Lefschetz variants are the
   candidates — his paper contains affine/local refinements; read
   them, do not guess). (b) our double points allow TANGENT smooth
   branches (A_{2k-1} germs, k>=2), which are NOT ordinary nodes —
   find whether Nori's or any later result (Dimca, Libgober, Nemethi,
   Artal Bartolo surveys; Dimca "Singularities and Topology of
   Hypersurfaces"; Libgober's braid monodromy papers) covers
   tangential double points of smooth branches, or exhibits a
   COUNTEREXAMPLE (a curve of this class with non-abelian affine
   complement group — line arrangements are excluded by
   irreducibility, but tangential conics/rational curves are known
   sources: check the standard examples, e.g. Zariski's tangent-conics
   families, Artal Bartolo's torus-type sextics — restricted to
   IRREDUCIBLE D with normalization A^1 or C^*).
3. If the general lemma is undecided by sources, attack the WEAKER
   form directly: Zariski-van Kampen on a generic pencil — meridians
   all conjugate, braid relations at double points; determine whether
   a transposition-valued S_4 representation with disjoint images at a
   tangential double point can satisfy the braid relations (at an
   ordinary node the relation is commutation [check]; at a tacnode it
   is a longer braid relation [derive it]; disjoint transpositions
   commute — so what do the relations force?). This is desk-scale
   group theory once the local braid relations are written; carry it
   through as far as sources + hand derivation allow, flagging every
   step that is your inference rather than a sourced statement.
4. Verdict: LEMMA-YES (sourced or proved, with the full chain),
   LEMMA-NO (countermodel curve in the exact class), or OPEN (name
   the single missing local input). Plus the acquisition ledger with
   hashes.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/b0-pi1-acquisition-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
