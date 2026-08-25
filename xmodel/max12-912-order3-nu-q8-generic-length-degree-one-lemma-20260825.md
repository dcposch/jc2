# Selected-Q8 generic-length degree-one lemma

Date: 2026-08-25  
Status: **PRODUCER-EXACT CONDITIONAL LEMMA; generic-length endpoint pending**

## 1. Setup and exact hypotheses

Let `k=F_127`, `K=k(w)`, and let `A` be the generic localized selected-Q8
source algebra defined by the same six divided rows used in the reviewed
component theorem, after

```text
x3=(v+2)*x5,        u=inv*x5,
```

and localization by

```text
u*x5*v=1.
```

On this open set `x5` and `v` are units, so this is an invertible coordinate
change from the full-contact presentation

```text
v*x5-x3+2*x5=0,
inv*x5*(x3-2*x5)-1=0.
```

Assume an exact generic computation proves

```text
dim(A)=0,       length_K(A)=190.                         (1)
```

The computational acceptance gate is an rc-zero pure-Singular endpoint from
the pinned source ideal, with `source_fail=0`, `dimension=0`, `vdim=190`, no
unresolved-symbol diagnostic, and a nonempty hash-pinned input.  A timeout,
memory failure, partial standard basis, or a fixed-fibre length is not (1).

Consume these already reviewed/frozen inputs:

1. `H(w,v)` is geometrically irreducible, monic of `v`-degree `190`, over
   `k`;
2. over `kbar`, at least one irreducible component of the same localized
   source has plane image `H=0`;
3. at each of the eight corrected-Q8 contacts at `w=0`, the full eight-row
   source presentation and localizer vanish, and the relative `8 x 8`
   Jacobian in `(c,d2,d4,x1,x3,x5,inv,v)` is a unit.

The conclusion below is conditional only on (1), not on a rational
reconstruction of the seven internal coordinates.

## 2. Length accounting over the geometric generic fibre

Base-change (1) from `K` to `Kbar=kbar(w)`.  Vector-space length is preserved,
so

```text
length_Kbar(A tensor_K Kbar)=190.                        (2)
```

Let `P` be the generic support point supplied by an `H`-dominant source
component.  Its residue field `L` contains the plane function field

```text
E=Kbar[v]/(H),        [E:Kbar]=190.
```

Because a dominant map of integral curves is generically finite, write
`[L:E]=d>=1`; this is the full field degree, so no separability assumption is
needed.  If `m>=1` is the scheme multiplicity at `P`, the contribution of
this one support point to (2) is

```text
m*[L:Kbar] = m*d*190.                                   (3)
```

Equations (2)--(3) force

```text
m=1,        d=1.
```

They also leave length zero for every other generic support point.  Thus the
geometric generic localized source has exactly one support point, is reduced
there, and its residue field is exactly `E`.  Equivalently:

- there is one and only one `w`-dominant geometric source component in the
  localized chart;
- it occurs with multiplicity one; and
- its map to `H` has degree one and induces equality of function fields.

This argument also rules out a nontrivial constant-field orbit: two geometric
conjugate source components mapping to `H` would already contribute at least
`2*190` to (2).

## 3. Why every corrected-Q8 contact lies on that component

At a corrected contact `q_i`, the full relative Jacobian unit and the unit
localizer give, by the formal implicit-function theorem,

```text
Ohat_(X_kbar,q_i) = kbar[[w]].                           (4)
```

The elimination of `x3` and the change `u=inv*x5` above are isomorphisms in
this local ring.  Hence (4) is a statement about the same localized source
whose generic algebra is `A`.

In particular, `q_i` lies on one reduced one-dimensional local branch and
`w` is its uniformizer.  That branch is `w`-dominant; because the localizer is
a unit at `q_i`, its generic point survives in `A tensor_K Kbar`.  Section 2
shows there is only one such generic component.  Therefore all eight
corrected-Q8 contacts lie on the unique multiplicity-one, degree-one
`H`-component.

This also rules out a higher-dimensional special-fibre component through a
contact: the local ring in (4) is regular of dimension one.  Vertical or
boundary components away from the eight contacts are not classified.

## 4. Exact conclusion and firewall

Conditional on the exact endpoint (1), the selected localized source over
`Fbar_127` has a unique `w`-dominant component; it maps birationally and with
cycle multiplicity one to `H`, and it contains all eight full corrected-Q8
contacts.

This is a characteristic-127 theorem.  Degree one gives rational internal
coordinate functions in the function field of `H`, but does not by itself
prove that they are regular at every projective boundary.  It does not prove
the repaired characteristic-zero no-merger hypotheses, integral
specialization of the reviewed characteristic-zero branches, identity with
the components in the primitive-grouping/infinity theorems, either Taylor
family, the terminal differential row, a rational trajectory, a maximum-12
exclusion, or JC2.

## 5. Pending producer lanes

Six independent AWS-only pure-Singular order/algorithm races currently test
(1).  Until one returns the complete accepted endpoint, this file is a
conditional implication and supplies no new unconditional component claim.
