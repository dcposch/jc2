# Hostile review assignment: coordinate-fibre connectedness theorem

Act as an independent hostile mathematical referee. Review exactly the
Sol connectedness packet named below. Its central claim: for the charged
pair `f,g` on `R=C[A,U,Z]/(U^2-A-A^2Z)` with `{f,g}=kappa in C^*` and
`[Frac(R):C(f,g)]=4`, the relative algebraic closures of `C(f)` and
`C(g)` in `Frac(R)` are trivial, hence the general coordinate fibres are
geometrically irreducible — proved NOT by the boundary route (which the
packet honestly types OPEN at a census-exhaustivity interface) but by an
independent argument from rationality and the unit group of the exact
ring together with `{f,g}=kappa`. It then restates the repaired
Riemann--Hurwitz identities, the partition table with the consistency
clause `gamma_h=(d_h-r_h-2)/2`, and the valuation packet's corrections.
Do not promote, edit any charged file, edit canonical ledgers, or
inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`.
Reproduce these SHA-256 hashes first and stop on mismatch:

```text
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  {{LANE_INPUTS}}/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
8abde87c3e9320ae1b75e90d4c4c26e4a7a16dc685398bf446b5b33b230f9787  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
```

Independently recompute, hunting hardest for:

1. the main algebraic argument: triviality of the relative algebraic
   closure of `C(f)` in `Frac(R)` — check every step (primitivity,
   Stein/closure structure, where rationality of `Spec R` and
   `R^*=C^*` enter, and where `{f,g}=kappa` is genuinely needed versus
   decorative); construct a candidate intermediate field and show
   exactly where the argument kills it;
2. the symmetry claim for `g`;
3. the honest OPEN typing of the boundary route: verify the
   census-exhaustivity interface is truly not in the frozen inputs
   (rather than present but overlooked), and that nothing in the main
   proof silently uses it;
4. the repaired identities and table (§5): re-derive (2.5)/(3.2)/(3.6)
   from the now-proved connectedness, including the consistency
   clause, and check against the pre-review's multi-component formulas
   at `delta=1`;
5. the special-fibre and bad-value handling (finitely many exceptional
   `a_f`), and the OPEN typings in §7.

State the weakest exact hypotheses, any correction and blast radius, and
one best next falsification test. Give a per-claim verdict from
`CONFIRMED`, `REFUTED`, `GAP`, with the attack shown.

Computation rules: desk-scale exact algebra only. Never run Singular,
msolve, any CAS, or any computation of uncertain duration or memory on
this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-fibre-connectedness-hostile-review-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your first
action and append each completed section as you finish it. Keep it under
roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration: this review asserts no new
exit price.
