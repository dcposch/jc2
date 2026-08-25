# Selected-Q8 seeded-quotient degree-one shortcut

Date: 2026-08-25  
Status: **COORDINATOR CONDITIONAL LEMMA; seeded AWS endpoint and coordinate
regularity certificate pending independent review**

## 1. Setup

Let

```text
k = Fbar_127,                 K = k(w),
A = the selected localized source algebra over K,
h = H(w,v) in A.
```

The reviewed mod-127 component theorem supplies a `w`-dominant integral
source component `C` whose plane image is the geometrically integral curve
`H=0`.  Let `P` be the corresponding prime of `A`.  Then

```text
h in P,
ker(K[v] -> A/P) = (H),
```

and therefore `K[v]/(H)` embeds in the finite field `A/P`.  Since `H` has
`v`-degree 190,

```text
dim_K(A/P) = 190*m                                      (1)
```

for the positive source-to-image degree `m` of `C` over `H`.

## 2. Seeded length forces reduced field degree one

Assume an exact standard-basis calculation of the **seeded** algebra proves

```text
B = A/(h),             dim_K(B)=190.                    (2)
```

Because `h in P`, there is a surjection

```text
B -> A/P.
```

Equations (1)--(2) give

```text
190 >= 190*m,
```

so `m=1`.  Here `m` is the field degree of the **reduced component** over
`H`, not yet its scheme-theoretic multiplicity in the full source.  Moreover,
the surjection is between 190-dimensional
`K`-vector spaces and is therefore an isomorphism.  Consequently:

- `B` is the field `K[v]/(H)`;
- `I+(H)=P` in the generic localized polynomial ring;
- the known reduced `H`-supported component is birational to `H`; and
- it is the only generic source-component **support** over `H`.

The seeded length alone does not prove multiplicity one in `A`.  The control

```text
A=E[epsilon]/(epsilon^2),       h=epsilon
```

has `A/(h)=E` although the sole component has generic multiplicity two.
Thus no cycle-multiplicity claim is licensed until the component closure is
shown to meet a full-source Jacobian-unit point.  At such a point the full
source is regular and reduced.  A coherent nilpotent or multiplicity module
present at the generic point would have support containing the whole
component closure, contradicting reducedness there; one verified regular
contact therefore supplies generic multiplicity one.

This argument does **not** require an upper bound on the length of the whole
generic source algebra `A`.  It also does not prove `H in I`: on unrelated
dominant components `H` may be a unit.  That distinction is why this shortcut
is stronger for the selected component than the older `H in I` routing note,
but narrower for the whole source scheme.

The standard-basis endpoint must be exact and fail closed:

```text
seeded_dim=0,       seeded_vdim=190,
```

with the original eight localized generators and the pinned monic candidate
`H`.  A candidate-seeded computation of any other length, an interrupted
run, or a basis over a different localization does not discharge (2).

## 3. Finite boundary values give all eight contacts

Degree one alone gives rational coordinate functions on `H`; it does not
make them regular at `w=0`.  From the seeded basis, express every internal
coordinate as an element of

```text
K[v]/(H).
```

For each coordinate, exhibit a representative `a(w,v)/b(w,v)` such that

```text
gcd(b(0,v),Q8bar(v))=1,                                (3)
```

and verify modulo `Q8bar` that its value is the frozen full-contact value.
Also recheck the two source equations introducing `v` and the inverse
localizer.  Condition (3) proves that the graph of `C` extends in the affine
localized source through all eight corrected-Q8 points.

At each such point the frozen full `8 x 8` relative Jacobian is a unit.  Thus
the completed local source ring is `k[[w]]`, so there is a unique local
irreducible component in every dimension.  The closure of `C`, once shown to
contain the point by (3), must be that unique component.  Hence the eight
points all lie on the same mod-127 source component.

This last conclusion requires the coordinate regularity/value certificate;
`seeded_vdim=190` by itself proves degree one but not all-contact affine
extension.  Poles may otherwise send some points of the projective graph to
the localization boundary.

## 4. Relationship to the other live routes

This is a logical bypass for the slow unseeded generic-length and saturated
projective-special-fibre computations.  Those computations remain valuable
independent certificates and should continue in the background.  A passing
seeded endpoint plus Section 3 is sufficient for the mod-127 reduced
field-degree-one, generic-multiplicity-one, and all-contact bridge even if
unrelated generic source components exist.

Characteristic-zero specialization still requires the separate common
`Z_(127)` source identity and integral-contact/Jacobian replay.  The repaired
no-merger lemma, primitive contact grouping, infinity theorem, trajectory
realization, maximum-twelve reduction, and JC2 remain separate gates.
