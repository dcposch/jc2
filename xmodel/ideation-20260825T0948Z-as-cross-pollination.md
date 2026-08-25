# 0948Z cross-pollination audit — Q8 genus composition and AS compactness

I read the root, cube/max12, and TD6-owner `0948Z` notes only after freezing
my blind submission.  This is an adversarial disposition, not promotion.

## Q8 proper-model/genus composition

**Verdict: plausible and probably repairable, but not yet implied by point
attachment or by `g(H)>0`.**  The cleanest proof does not need a global
ambient no-merger theorem.  Compactify the actual rational source trajectory,
make a finite DVR base change, resolve its graph, and take a semistable
genus-zero source model.  Every irreducible special source component is
`P1`; by Luroth, no nonconstant image of such a component can have
positive-genus normalization.  Thus it is enough to prove that one special
source component maps nonconstantly and densely to the integral curve `H`.

The missing arrows are exact and load-bearing:

1. the generic trajectory really is a rational source curve and extends,
   after finite base change, to a morphism from a proper semistable
   genus-zero model into a proper target/graph model;
2. the reviewed characteristic-zero contact section extends to the same
   model and its reduction is the reviewed **full source point**, not merely
   the plane `(w,v)` projection;
3. the reduced completed-local trajectory map factors through the formal
   branch of `H` at that point;
4. that map is nonconstant modulo 127 (the source parameter does not collapse
   vertically); equivalently, the pullback of a local parameter on the smooth
   `H` branch has finite positive order, ideally unit linear coefficient;
5. the image closure is therefore dense in `H`.  Separability is convenient
   but not required for the Luroth contradiction;
6. the primitive singleton components are genuinely one transitive
   characteristic-zero Galois orbit before propagating genus from the winning
   contact.  The all-eight alternative may then consume the reviewed infinity
   exclusion.

Flatness, reducedness, and multiplicity one are sufficient ways to prove
these statements, but not logically necessary if the source-map formulation
is established directly.  Conversely, a special ambient component equal to
`H`, or a contact point on `H`, is insufficient: the rational source can
specialize constantly at that point or follow another formal branch.

**Cheapest discriminator.**  At the winning smooth contact (`H_v` a unit in
the existing boundary certificate), compute the reduction of the arithmetic
`R[[w]]` trajectory in the complete full-source local ring.  Prove
scheme-theoretically that its `(w,v)` projection equals the unique Hensel
graph `v=v_H(w)` and that the pullback of `w-w_0` (or another uniformizer of
`H`) is nonzero, preferably a unit times the source parameter.  PASS licenses
the semistable-source/Luroth proof; branch mismatch or zero pullback stops the
composition immediately.  This one local calculation is cheaper and sharper
than global component reconstruction.

## Collision-augmented fixed-support compactness

**Verdict: the finite-type claim is correct, provided every depth is the same
complete finite polynomial scheme.**  Eventual periodicity or rational
reconstruction of ternary digits is unnecessary.

Fix finite supports `S_P,S_Q` and introduce coefficient variables for
`P,Q`, two source points `(a,b),(c,d)`, and an inverse variable `u`.  The
single integral affine scheme must contain all of the following equations:

```text
[x^i y^j](P_x Q_y-P_y Q_x) = 1  for (i,j)=(0,0),
[x^i y^j](P_x Q_y-P_y Q_x) = 0  for every other possible coefficient;
P(a,b)-P(c,d)=0;
Q(a,b)-Q(c,d)=0;
u(a-c)-1=0.
```

The last chart is valid for the AS seed because `a-c` is already nonzero
modulo 3; otherwise the complementary `b-d` chart must also be covered.
Every other open condition or denominator used by a normalization must be
encoded by its own inverse variable.  A fixed residue component may be
encoded integrally as `coefficient=seed+3*t`, but all constants must remain
in `Z`, not be depth-dependent or genuinely 3-adic.

Necessary firewalls are:

1. fixed finite variable/support set at every `n`; no newly appearing map
   monomials, digit variables, collision coordinates, or phase history;
2. the **complete** determinant coefficient equations, not a filtered high
   band or a chronological gate that still owes restored low rows;
3. the same two collision equations and unit chart at every depth;
4. actual solutions modulo `3^n` of this scheme, not models of BV `URem`,
   exact-division, or carry gadgets unless a proved translation reconstructs
   the displayed integer equations;
5. no varying localizer, normalization, or support between depths.

If this same scheme has a solution modulo `3^n` for every `n`, the closed
solution subsets of `Z_3^N` are nonempty, nested, and compact, so their
intersection contains a `Z_3` point.  Evaluation in `Q_3` proves that the
defining ideal in `Q[variables]` is proper.  Nullstellensatz then supplies a
`Qbar` point, and hence a complex polynomial pair with exact determinant one
and a genuine off-diagonal collision.  The `Qbar` point need not retain the
mod-3 interpretation; the polynomial equations and inverse equation are
what survive, which is enough for a JC2 counterexample.

The claim fails if “survival at every depth” refers to changing filtered
schemes, growing support, or map-only states.  It also fails if the collision
is checked only modulo 3 and omitted from later transition states.

**Cheapest discriminator.**  Before deepening the present AS map-only tree,
build the complete fixed-support coefficient scheme above and decide its
collision-bearing locus modulo 9, then modulo 27, with direct integer
substitution of every determinant and collision coefficient.  Proof-checked
emptiness at either level kills this collision chart immediately.  SAT at
both levels is only a stronger root; the next task is the same-scheme inverse
limit, not rational digit fitting.
