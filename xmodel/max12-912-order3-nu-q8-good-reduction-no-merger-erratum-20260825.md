# Erratum: selected-Q8 good-reduction no-merger lemma

Date: 2026-08-25  
Status: **coordinator counterexample and repaired lemma; the first hostile
independent review attempt failed closed at its output limit; no Q8
computational hypothesis is discharged here**

This note is nonmutating: it does not alter the frozen producer lemma
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`.
It supersedes that note's abstract lemma and checklist wherever they differ.

## 1. The stated lemma is false

The phrase

> `C` is the unique one-dimensional local irreducible component

does not exclude a higher-dimensional vertical component through the marked
point.  Horizontal curve components can specialize into that vertical
component instead of dominating `C`.

Let `k` be algebraically closed, `R=k[[pi]]`, and

```text
X = Spec R[x,y,z]/(x*z, y*z, pi*x*y).
```

The special fibre is

```text
X_k = Spec k[x,y,z]/(x*z,y*z),
(x*z,y*z) = (z) intersect (x,y).
```

It is reduced.  Its irreducible components are the plane
`D=V(z)` and the line `C=V(x,y)`.  At the origin `q`, `C` is the unique
**one-dimensional** component, but `D` is also present.

The generic fibre has `pi` invertible, hence

```text
X_K = Spec K[x,y,z]/(x*y,x*z,y*z),
```

the union of the three coordinate axes.  The closures of the generic `x`-
and `y`-axes both contain `q`, but they are distinct geometric irreducible
components.  At the generic point of the special `z`-axis `C`, `z` is a unit,
so `x=y=0`; there `X` is flat over `R` and the special fibre is reduced.
Thus every hypothesis of the displayed producer lemma is satisfied while its
conclusion fails.

The proof fails exactly where a one-dimensional special-fibre germ of a
horizontal closure is asserted to lie on `C`: it may instead lie inside the
higher-dimensional component `D` and therefore need not contain `eta_C`.

## 2. Corrected no-merger lemma

Let `R` be an **excellent** DVR with uniformizer `pi`, fraction field `K`, and
algebraically closed residue field `k`.  Let `X` be a finite-type `R`-scheme and let `C` be
an integral one-dimensional irreducible component of `X_k`.  Assume:

1. `X -> Spec R` is flat at the generic point `eta_C`;
2. `X_k` is reduced at `eta_C`;
3. for each marked point `q_i in C`, **`C` is the unique irreducible
   component of `X_k` through `q_i`, in every dimension**; and
4. `Y_i` is a geometric irreducible curve component of the generic fibre
   whose scheme-theoretic closure `Z_i` in a common finite-DVR model contains
   `q_i`.

After making the common finite DVR extension and rechecking hypotheses 1--3
there, all `Y_i` are the same geometric irreducible component.

A stronger sufficient replacement for hypothesis 3 is that
`O_(X_k,q_i)` is a regular local ring of dimension one and `C` is its unique
local branch.  This is the form intended for the selected-Q8 application.

## 3. Proof of the corrected lemma

Work after the common DVR extension on which the finitely many geometric
components are defined.  Write

```text
A = O_(X,eta_C).
```

Flatness makes `pi` a non-zero-divisor in `A`.  Since `C` is an irreducible
component and `X_k` is reduced at its generic point, `A/pi*A` is a field.
Hence `A` is a domain.  Indeed, `A` is `pi`-adically separated by Krull
intersection.  Every nonzero element has a finite maximal `pi`-adic order;
after removing those powers from a hypothetical product `a*b=0`, both
factors are nonzero modulo `pi`, contradicting that `A/pi*A` is a domain.

For each `i`, `Z_i` is integral and dominates the DVR.  Its coordinate rings
are torsion-free over the DVR and therefore flat.  Since its generic fibre is
a curve, the dimension formula for a finite-type flat scheme over a DVR says
that every irreducible component of `(Z_i)_k` through `q_i` has dimension
one.  Such a component is contained in an irreducible component of `X_k`
through `q_i`; by hypothesis 3 that component is `C`.  Equal dimension and
irreducibility force the component of `(Z_i)_k` to be dense in `C`, so
`Z_i` contains `eta_C`.

Localizing at `eta_C`, each `Z_i` therefore gives a prime of `A` not
containing `pi`.  Because `A/pi*A` is a field, `A` is a one-dimensional local
domain and its only prime not containing `pi` is `(0)`.  Thus all closures
have the same generic prime near `eta_C`; their generic fibres agree on a
nonempty open set and are the same irreducible component.  This proves the
corrected lemma.

The earlier phrase “integral closure inside `X`” is also replaced throughout
by **scheme-theoretic closure**.  Normalization is neither required nor in
general a closed subscheme of `X`.

## 4. Revised selected-Q8 discharge checklist

1. **One common integral source scheme.**  Define the exact selected localized
   quotient `X` over a DVR above 127 from the divided original rows.  Every
   coefficient and contact expression is integral, every advertised
   localizer/contact denominator is a unit, and the corrected octic remains
   squarefree after residue extension.
2. **Actual graph/component, not a projection.**  Reconstruct all seven
   coordinate functions on the geometrically integral plane curve `H=0` and
   verify all original rows, the retained `v` relation, and the localizer
   identically modulo `H`.  The graph has function field
   `F_127(w)[v]/(H)`.  A full internal Jacobian unit at one graph point, in the
   full source presentation, must certify that its closure is a genuine
   one-dimensional component and that `X` is flat/reduced at `eta_C`.
3. **Standalone `H` hypotheses.**  Arithmetic irreducibility uses that `H` is
   monic in `v`, lies in `F_127[w,v]`, and both squarefree specializations keep
   `v`-degree 190; monic factors therefore specialize without degree drop and
   their degrees must be subset sums of the displayed irreducible factors.
   A smooth rational point then proves geometric irreducibility over the
   perfect finite field.  This concerns `H` only until item 2 passes.
4. **All eight full contacts.**  On the simple `Q8bar` factor of `H(0,v)`,
   every reconstructed coordinate is regular and has the exact corrected
   contact value.  `H_v != 0` supplies only plane-projection smoothness.
5. **Unique special-fibre component in every dimension.**  At each full
   contact `q_i`, prove that the local ring of the **full source quotient
   special fibre** is regular of dimension one (or prove an equivalent
   completed-local-ring statement).  A rank-eight internal Jacobian can do
   this only after the ambient variables, selected original rows, extra rows,
   and localizer are all checked.  This condition rules out the counterexample
   above and supplies the corrected lemma's hypothesis 3.
6. **Integral specialization of the characteristic-zero branches.**  Over a
   common finite DVR extension, construct the reviewed characteristic-zero
   contact branch as an integral formal section or otherwise prove that the
   scheme-theoretic closure of its geometric generic component contains the
   corresponding full `q_i`.  Unit implicit-function minors and explicit
   integral contact formulas are the intended certificate; a projected root
   alone is insufficient.
7. **Scheme identity at the end.**  Verify that the components used in the
   primitive all-eight/singleton theorem and the infinity theorem are exactly
   the geometric components of this same localized source scheme.  Only then
   may the corrected lemma select the all-eight alternative and feed the
   registered trajectory exclusion.

## 5. Current scope

Current exact evidence supplies the standalone plane arithmetic/geometric
integrality and the `(w,v)` boundary factorization only.  It does not yet
supply items 2, 4, 5, or 6.  Consequently this erratum repairs the proposed
logical bridge but proves no Q8 component lift, selected-trajectory exclusion,
maximum-twelve theorem, or JC2 theorem.
