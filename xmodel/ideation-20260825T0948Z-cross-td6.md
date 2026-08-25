# 09:48Z cross-pollination stress test — TD6 owner

Status: **cross-round strategy audit, not mathematical promotion**.

I read the four submissions only after the blind collection closed:

- coordinator: `95134084f74e1d53d72302d83233a479f6dcef475b6cb5e1f5f7462ff03aa1cb`;
- AS owner: `8a1cbb85085e66f582d87fff7d5bc83289567928a1a1d2d61036f1b6d2586367`;
- cube/max-12 owner: `c3f0b66574684083dca07db15b4a0dece71e9248c7bb5a1777a4b206ae01297f`;
- TD6 owner: `9b9e45efe678c7e2c012f60f16df134178aef1d54b4e2fc35d0b5682c589ad98`.

AWS TD6 producers continued while this audit was written.  No heavy
computation ran locally.

## 1. Strongest independent convergence

All four reports independently converge on a positive-genus obstruction for
the selected Q8 branch, but the clean formulation is the **source stable-map
version**, not a bare genus ledger on an ambient target fibre.

Take the proper graph of the actual characteristic-zero rational trajectory,
make a finite DVR base change, and semistably reduce its source.  The special
fibre of a genus-zero source is a tree of rational components.  If one such
component maps nonconstantly, hence dominantly, to the normalization of the
geometrically integral curve `H`, then `k(H)` is an intermediate field of a
rational function field.  Lüroth forces `H` to be rational, contradicting the
producer-exact `g(H)>0` result once its hostile review closes.

This version has two advantages:

1. it tolerates extra vertical or contracted components in the target model;
2. it does not require target multiplicity one or separability.  What remains
   load-bearing is the extension of the actual source graph and dominance
   onto `H`.

The equivalent relative-dualizing formula

```text
p_a(C_eta) = sum_v g(C_v) + b_1(Gamma)
```

is safe only after the relevant source fibre has genuinely been made reduced
nodal/semistable and `H` has been identified with, or dominated by, one of its
components.

## 2. Countermodels that the attachment gate must exclude

Point incidence or an eliminant root alone does not compose with genus.

1. **Purely vertical tail.**  A nonflat ambient model may be the horizontal
   closure of `P1_K` together with a positive-genus `H/k` living only in the
   special fibre and meeting the horizontal closure at one point.  The
   contact exists but says nothing about the generic trajectory.
2. **Projected/extraneous component.**  The plane eliminant may contain `H`,
   and the full source branch may meet a smooth point of `H`, while its
   reduction is constant in the plane coordinates.  The source does not
   dominate `H`.
3. **Nonreduced model artefact.**  Before semistable replacement, nilpotent or
   multiple fibre structure invalidates the displayed reduced-nodal genus
   formula; a component seen in that model may be contracted or fail to lift
   through normalization/base change.

Thus neither one corrected contact, `H`-support in an elimination equation,
nor positive genus by itself excludes a trajectory.

## 3. Cheapest exact Q8 falsifier

At one reviewed smooth rational contact, let `pi` be the DVR uniformizer and
perform the following source-level test:

1. saturate the full original source ideal by `pi`, retaining the horizontal
   prime selected by the arithmetic `R[[w]]` branch;
2. reduce modulo `pi` and localize at the generic point `eta_H`;
3. verify that the contraction of the selected source prime to the plane
   coordinate ring is exactly `P_H`, and that the special `w`-direction is
   nonzero.

If the localized saturated ideal is the unit ideal, or if the plane map is
constant modulo `pi`, `H` is vertical/extraneous for this trajectory and the
genus composition stops.  If it passes, extend the proper source graph and
apply the source-component/Lüroth obstruction.  A full global normalization
or target multiplicity-one theorem should not precede this discriminator.

## 4. Does a fraction-free Fitting module replace pivot atlases?

**Only partially.**  It can replace arbitrary pivot-order proliferation, but
it cannot erase genuine rank, divisor, embedded, or nonreduced strata.

For a linear system `A x = b`, global or localized membership of `[b]` in
`coker(A)` is stronger than solvability after specialization to each residue
field.  A single annihilator or Fitting ideal of `[b]` therefore does not, by
itself, describe the pointwise consistency locus.  The exact pivot-free
replacement must retain the original source ring and compute the
rank-stratified augmented determinantal/Fitting loci.  For a unit global
obstruction it must also emit the explicit original-row syzygy.  Otherwise it
must preserve every support prime, embedded component, and raw intersection.

The minimal correctness control is

```text
R = k[x,y],   A = [x],   b = y.
```

The fibre equation is solvable on the constructible set

```text
D(x) union V(x,y),
```

including the origin.  But `[y]` is nonzero in `coker([x])` localized at
`(x,y)`.  Any proposed engine that equates the support of the cokernel class
with fibrewise inconsistency fails this control.  A sound engine must recover
the two rank strata exactly.

Applied to TD6, the proof-grade outcomes are therefore:

- an explicit denominator-free original-row unit syzygy, which genuinely
  removes the pivot atlas at the licensed scope; or
- a canonical rank/Fitting stratification, whose nonunit components still
  require raw source rebuilds and explicit gluing/coverage certificates.

Multivariate gcd-one, minimal-prime output alone, or global module
nonmembership is not a cover theorem.

## 5. Allocation consequence

Move the Q8 composition test to the single horizontal-prime/dominance gate.
For TD6 and AS, build the fraction-free engine only with the toy constructible
control and original-row replay from the start.  If it passes, stop launching
new pivot-order variants; keep the actual rank/divisor strata as the required
successors rather than calling them software artefacts.

