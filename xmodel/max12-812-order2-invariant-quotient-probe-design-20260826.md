# `(8,12)` exact order two: invariant-quotient probe over load space

Date: 2026-08-26

Status: **SOURCE-TYPED NAVIGATION DESIGN; NO GENUS OR ELIMINATION CLAIM.**

## 0. Necessary coefficient curve

For a fixed six-load tuple

```text
lambda_load=(k10,k6,k2,mu2,mu4,mu6),
```

let `r_ell(a;k)` be the exact ordinary tails reconstructed from

```text
f=z^8+sum_(i=0)^6 a_i z^i,
g=F12(f)+k10 F10(f)+k6 F6(f)+k2 F2(f).
```

Every exact-order-two source has coefficient image in the `r7!=0` curve

```text
X_lambda:
(r1,r2-mu2,r3,r4-mu4,r5,r6-mu6):r7^infinity.       (0.1)
```

This is a necessary coefficient curve, not a source-existence scheme.  The
complete source audit retains all six loads and does not import `(9,12)`.

## 1. Deck quotient obstruction

The order-two deck involution acts by

```text
iota(a_i)=(-1)^i a_i.                                (1.1)
```

Ordinary equivariance gives `iota(r_ell)=(-1)^ell r_ell`.  Hence (0.1) is
stable under `iota`: odd target rows are zero, even target rows are invariant,
and saturation by the odd `r7` is unchanged.

A genuine source map `C -> X_lambda` is equivariant.  It therefore descends
to a rational map

```text
P1_x=C/<deck iota>  -->>  X_lambda/<iota>.           (1.2)
```

If the relevant complete quotient component has positive normalization
genus and (1.2) is nonconstant, properness and the regular-differential
argument exclude that source component.  This is the same abstract receptor
used in the now-confirmed order-four theorem, but none of its load-space
premises has yet been proved here.

If the generic quotient over the six-load base has positive genus, every
source must lie in an exceptional discriminant locus where the curve,
quotient, component coverage, or projection degenerates.  Exact-Q generic
flatness, normalization, and componentwise nonconstancy are required before
making that inference.

## 2. Tiny modular navigation probe

The first AWS-only probe fixes the deterministic rational tuple

```text
(k10,k6,k2,mu2,mu4,mu6)=(2,3,5,7,11,13)             (2.1)
```

and works in characteristic `32003`.  It must:

1. pin the exact seven-tail JSON and canonical all-tail digest;
2. verify every tail weight, affine lower-load dependence, and involution
   parity before emission;
3. form (0.1), print its dimension/size, and verify the six generators and
   saturated ideal are involution-stable;
4. inspect the affine fixed locus `a1=a3=a5=0`;
5. eliminate to two deterministic invariant functions built from
   `a0,a2,a4,a6` and the six quadratic odd products;
6. report the invariant-plane eliminant and factor count with fail-closed
   source/symmetry sentinels.

This probe deliberately does not call a plane degree a normalization genus.
It omits toric/projective boundary branches, local delta corrections, exact-Q
lifting, generic-load flatness, and source-component coverage.  A promising
plane is only a target for an exact normalization/Riemann--Hurwitz client; a
rational or vertical plane is a cheap falsifier of this chosen projection,
not of all invariant quotients.

## 3. Prioritized successor

If the modular curve is one-dimensional and the invariant image is a
nontrivial irreducible plane, replay at a second tuple and prime.  Then freeze
the generic load-parameter ideal, find the precise discriminant open on which
the quotient normalization genus and projection degree are constant, and
lift one monic good reduction to exact Q.  Audit fixed and boundary points
before Riemann--Hurwitz.

Only after those steps may the exceptional load locus be stratified and fed
to the one-parameter Rees/Taylor clients.

## 4. Firewall

Neither a high-degree plane eliminant nor a modular positive genus proves a
source impossible.  This design does not eliminate any load tuple, the
`U=2,[6,2]` profile, exact order two, `(8,12)`, maximum twelve, or JC2.
