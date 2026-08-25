# Selected-Q8 characteristic-zero specialization and scheme-identity gap audit

Date: 2026-08-25  
Status: **producer dependency audit; no new component or trajectory theorem**

## 1. Audited target

This note audits items 6 and 7 of
`max12-912-order3-nu-q8-good-reduction-no-merger-erratum-20260825.md`.
It uses the reviewed corrected-Q8 formal branch, normalization/Taylor/terminal
jet, global quotient gate, infinity/passport theorem, and
Galois-primitivity/infinity review.  It also inventories the producer-exact
characteristic-127 full-contact Jacobian certificate.  It does not infer an
integral branch from a projected `(w,v)` root.

The audit finds no conceptual need for an all-orders integrality calculation.
The smallest sufficient item-6 certificate is an **integral contact plus an
arithmetic implicit-function unit**.  That certificate has not yet been
frozen across characteristic zero and characteristic 127.

## 2. One common source scheme

Let `R0=Z_(127)`.  After clearing only 127-unit scalar denominators, define

```text
Y_R0 = Spec R0[w,c,d2,d4,x1,x3,x5,inv,v] /
  (e1,e3,e5,e7,e2,e4,
   v*x5-x3+2*x5,
   inv*x5*(x3-2*x5)-1).
```

Here `(e1,e3,e5,e7,e2,e4)` are, in that order,

```text
r1/t, r3/t, r5/t, r7/t, r2, r4
```

from the reviewed approximate-cubic quotient compiler, with

```text
t=x0,  w=t^2,  q_c=t*c,  x2=t*d2,  x4=t*d4,  p=1.
```

The localizer deliberately does **not** invert `w`.  The reviewed punctured
open used `inv*w*x5*(x3-2*x5)-1`; over the generic base `Q(w)` this is the
same open, but it has no `w=0` contact.  The arithmetic closure needed for
specialization is obtained by keeping the divided six rows and inverting only
`x5*(x3-2*x5)`.  The redundant `v` equation and `inv` equation are eliminable
on this open, so they do not change its geometric components.

This displayed `Y_R0` is the required scheme for both missing bridges.  A
certificate about a plane curve `H(w,v)` alone is not a substitute.

## 3. Item 6: the sufficient arithmetic-local argument

Normalize the corrected octic to a monic polynomial over `R0`.  Its leading
coefficient `-999` is a 127-unit, and the frozen reduction `Q8bar` is
squarefree.  Thus

```text
R0[v]/(Q8_monic)
```

is finite etale at 127.  After one common finite unramified DVR extension
whose residue field splits `Q8bar` (and, if desired, a further strict
henselian/complete DVR base change), its eight roots give eight integral,
pairwise distinct sections `v_i`.

For each `v_i`, the explicit corrected formulas

```text
x5=-36*v_i^2*(3*v_i^2+3*v_i+1)/(3*v_i^2-2),
x3=x5*(v_i+2),
x1=x5*(v_i+1)+x5^2*(3*v_i+1)/(9*v_i)
```

are integral provided the already displayed mod-127 unit tests for
`v_i`, `3*v_i^2-2`, and the localization factors are lifted into one
cross-characteristic replay.  At `w=0`, the three normal divided rows solve
`(c,d2,d4)` uniquely because their `3 x 3` solve determinant is a 127-unit.
This proves integrality of the contact coordinates directly; it does not
require integrality of an infinite series.

Now use the eight equations defining `Y_R0` and the eight internal variables

```text
(c,d2,d4,x1,x3,x5,inv,v).
```

If their relative determinant at the integral contact is a 127-unit, formal
implicit functions give

```text
completed local arithmetic source = R[[w]],
special fibre completion           = k[[w]],
generic fibre completion           = K[[w]].
```

Consequences are exactly the ones needed by the repaired no-merger lemma:

1. the full special-fibre source is regular of dimension one and has one
   local component through the contact in every dimension;
2. the generic selected branch has an integral formal section;
3. the scheme-theoretic closure of its geometric generic component contains
   the full special point `q_i`;
4. after a common DVR extension the argument applies simultaneously to all
   eight contacts.

The generic formal branch here is the reviewed selected branch: over
characteristic zero, the same six divided rows have a unique completed local
solution with `w` a parameter.  Adjoining `t` with `t^2=w` reconstructs the
reviewed non-parity branch in coefficient space; this ramification is in the
branch parameter, not in the arithmetic uniformizer 127.

## 4. Exact item-6 gap

The current two endpoints do not yet compose:

- the reviewed characteristic-zero quotient replay constructs the contact
  and its unique `Q[v]/(Q8)[[w]]` branch, but records coefficient digests and
  characteristic-zero unit statements, not 127-adic denominator units or
  reduction to the frozen full contact;
- the producer-exact mod-127 full-contact replay independently solves the
  same-looking rows and proves an `8 x 8` determinant unit, but does not prove
  that its point is the reduction of the reviewed characteristic-zero point.

The smallest missing portable certificate must therefore do all of the
following in one pinned source:

1. emit the six divided rows over `R0` and prove their reductions are byte-
   identical to the rows used by the mod-127 full-contact case;
2. compute the characteristic-zero contact in the etale `Q8` algebra,
   prove every scalar and polynomial denominator is a 127-unit, and reduce
   all eight coordinates;
3. compare those reductions coefficient-for-coefficient with the frozen
   mod-127 contact section;
4. evaluate all eight source equations over the integral etale algebra and
   prove the full relative Jacobian determinant reduces to the frozen unit.

Once this passes, the arithmetic `R[[w]]` conclusion is formal; no higher
Taylor coefficient or whole-series denominator audit is needed for item 6.
The existing full-contact endpoint is producer-exact, not yet a reviewed
cross-characteristic certificate.

## 5. Item 7: exact scheme identity needed at the endpoint

The reviewed primitivity theorem groups the eight characteristic-zero
contacts by geometric components of the **six-row divided quotient scheme**.
The reviewed infinity theorem is conditional on an actual trajectory whose
quotient image lies in the algebraic component selected by that same local
branch.  To feed them from the mod-127 component theorem, one source-identity
manifest must state and check:

1. `Y_R0 tensor Q`, after eliminating `(v,inv)`, is exactly the six-row
   characteristic-zero quotient used in the reviewed global gate;
2. its open `w!=0` is exactly the reversible parity quotient of the original
   approximate-cubic coefficient fibre; taking scheme-theoretic closure in
   `Y_R0 tensor Q` restores the eight `w=0` contacts;
3. `Y_R0 tensor F_127` is exactly the full selected localized source used by
   the reviewed sparse-contact component theorem and the full-contact
   Jacobian case, not merely its projection `H=0`;
4. the component labels in the primitivity theorem, the selected component
   in the infinity theorem, and the horizontal components in the no-merger
   lemma all mean geometric irreducible components of these two base changes
   of `Y_R0`.

The main trap is saturation/localization order: inverting `w` before taking
the closure deletes every marked contact.  The other trap is replacing the
source component by the candidate plane component `H`; projection roots and
even a degree-one function-field statement do not by themselves prove this
scheme identity without the graph/source verification.

## 6. Dependency verdict

Items 6 and 7 are **not yet discharged**, but their remaining certificates
are narrow:

```text
item 6 = one cross-characteristic integral-contact/Jacobian replay;
item 7 = one exact row/localizer/base-change identity manifest.
```

If those pass, the repaired no-merger lemma can use the arithmetic
`R[[w]]` neighborhoods to attach each characteristic-zero branch closure to
the corresponding full mod-127 contact.  Only after the separate mod-127
degree-one/all-contact component bridge passes may primitivity select the
all-eight alternative and the reviewed infinity theorem exclude an actual
trajectory at its registered scope.  No Taylor realization, all-`(9,12)`,
maximum-twelve, counterexample, or JC2 conclusion is asserted here.
