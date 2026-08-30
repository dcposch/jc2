# Coordinator integration: intrinsic cubic discriminant and normalization index

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`  
Lifecycle: **BINDING INTEGRATION / FINITE-FLAT RANK-THREE ALGEBRA SCOPE**

## 0. Disposition and custody

Opus 5 independently reconstructed the sealed producer

```text
327b1f42b3ee245d1383d0108feca4c5ae20cbdaf5a00545f1c1d7fd5cee81d7
  xmodel/bd-fix3-quadratic-discriminant-conductor-invariant-sol56-20260830.md
  body 6323 / 3362a7913801a180cf0d4ee06e9bf08ee13324ea598d72e0e8f797d59ff28ac5
```

and returned `CONFIRM_WITH_CORRECTIONS`.  Its sandbox-attested raw review
body is

```text
013af71756795a10bdb6435af5a6e790c0ee1ed9a6b99f6047af40f2a872b881
  xmodel/bd-fix3-quadratic-discriminant-conductor-invariant-hostile-review-opus5-20260830.md
```

and its sealed full-file SHA-256 is
`4241bb325de1904ef7cd10b46ff87dca489c23115c735b36137956bfcd4ebc4e`.
The clean schema-v2 receipt has exit code zero and pins unchanged prompt,
adapter, launcher, Seatbelt profile, validator, fallacy appendix, and composed
model-prompt hashes.

Nothing is refuted.  This integration adopts the review's sharpenings and
firewalls: the binary-cubic convention scalar is exactly one; the index is a
Fitting/length divisor and is not the conductor; source ramification,
different, target discriminant, and reduced branch are four distinct objects;
and a curve-delta interpretation needs an actual base-change theorem plus a
Gorenstein hypothesis where the classical conductor formula is invoked.

## 1. Intrinsic discriminant theorem

Let `A=C[u,v]` and let `B` be a finite locally free rank-three `A`-algebra
whose generic fibre is separable.  Since `3` is invertible,

```text
B=A*1 direct-sum E,             E=ker(Tr_B/A).
```

The rank-two projective module `E` is free by Quillen--Suslin.  For any
`A`-basis `e=(e_0,e_1,e_2)` of `B`, put

```text
Delta_e=det(Tr_B/A(e_i*e_j)).
```

If `h in GL_3(A)` changes the basis, then

```text
Delta_(eh)=det(h)^2*Delta_e,
```

and `det(h)` is a nonzero complex constant.  Therefore the principal ideal,
effective divisor, and zero scheme defined by `Delta` are basis-independent;
the polynomial itself is defined up to `C^*`.  This conclusion does not
depend on choosing a trace-zero basis.

In a trace-zero Miranda basis `(1,z,w)`, with multiplication coefficients
`a,b,c,d`, direct computation gives

```text
Tr(z^2)=6(a^2-bd),
Tr(zw)=-3(ad-bc),
Tr(w^2)=6(d^2-ac),

Delta = 81a^2d^2-108a^3c-108bd^3-27b^2c^2+162abcd.
```

This is exactly, with scalar one in the classical convention, the
discriminant of

```text
Phi=bX^3-3aX^2Y+3dXY^2-cY^3.
```

It is homogeneous of coefficient-degree four.  Hence

```text
max(deg(a),deg(b),deg(c),deg(d)) <= d
                  implies deg(Delta) <= 4d.          (1.1)
```

In particular a quadratic presentation has intrinsic full affine
discriminant degree at most eight.  Conversely, if `d_min` is the minimum of
the displayed maximum over all global trace-zero bases of this fixed algebra,

```text
d_min >= ceil(deg(Delta)/4).                          (1.2)
```

This is a lower bound only.  Neither a reverse inequality nor an upper bound
on `d_min` has been proved.

The nonzero divisor `V(Delta)` is exactly the non-etale locus on the base,
hence the branch locus as a set.  Its divisor multiplicities are the norms of
different exponents.  They are not in general the multiplicity-one reduced
branch, the reduced source ramification, or the source different itself.

## 2. Global normalization-index theorem over `C[u,v]`

Assume in addition that `B` is reduced and let `Btilde` be its integral
closure in its total ring of fractions.  Excellence makes `Btilde` finite
over `A`.  Its normal two-dimensional factors are Cohen--Macaulay; over the
regular ring `A`, Auslander--Buchsbaum and Quillen--Suslin make `Btilde` free
of rank three.

Choose global bases and represent `B -> Btilde` by a matrix `M`.  Then

```text
Fitt_0(Btilde/B)=(det M),
Delta_B=(det M)^2*Delta_Btilde,                       (2.1)
div(Delta_B)=div(Delta_Btilde)+2*div(det M).
```

The divisor `div(det M)` is effective, and at every height-one prime `p`,

```text
ord_p(det M)=length_Ap((Btilde/B)_p).                 (2.2)
```

Thus a quadratic presentation gives the exact numerical bounds

```text
deg(det M) <= 4,
deg(Delta_Btilde) <= 8-2deg(det M).                  (2.3)
```

For a general normal noetherian base and finite torsion-free orders, only the
height-one version is automatic: the index is the divisorial part of
`Fitt_0(Btilde/B)`, and codimension-at-least-two Fitting support is discarded.

The index divisor is not the conductor divisor.  For example, over a DVR
`R`, with `Btilde=R^3` and `B=R+pi*R^3`, the quotient has length two and
`ord(Fitt_0)=2`, while its annihilator/conductor has order one.  The two may
be identified only after an additional cyclicity or equivalent local
hypothesis.

## 3. Slice and curve firewall

Normalization need not commute with slicing.  Even when both surface orders
are free, tensoring

```text
0 -> B -> Btilde -> Btilde/B -> 0
```

with a curve `A/(L)` is exact on the left precisely when
`Tor_1^A(Btilde/B,A/(L))=0`; in matrix form this is injectivity of `M mod L`.
For a height-one slice, it is enough here that `L` not be a component of the
index divisor.  The resulting sliced lattice length is not automatically the
delta invariant of the normalization of the sliced curve.

Moreover the classical equality between conductor colength and twice delta
requires the relevant one-dimensional order to be Gorenstein.  Branch data
alone do not supply that condition.  Consequently no surface index, sliced
index, curve delta, conductor, or resolved-boundary multiplicity may be
substituted for another without a named comparison theorem.

Two strict-henselian controls are mandatory before a broad elimination:

```text
SH-1  B=R[t]/(t^3-u):
      (disc order, different order, reduced branch order, index)=(2,2,1,0).

SH-2  Btilde=R^3, B=R+uR^3:
      index order 2, conductor/annihilator order 1, disc order 4;
      the transverse slice L=(v) has Tor_1=0 and sliced index 2;
      the contained slice L=(u) has Tor_1 nonzero and must return FAIL.
```

Any computational pipeline that conflates one of these objects or fails a
control is rejected before AWS scale-up.

## 4. Binding campaign consequence

`DISC8-INDEX` is now a promoted, basis-safe client for a fixed-algebra
quadratic cubic-block presentation.  The next finite geometric packet should
jointly type:

1. the full affine discriminant divisor and its infinity branches;
2. its multiplicities as a target discriminant, separately from source
   ramification and the different;
3. the principal normalization-index divisor of degree at most four;
4. reduced ramification classes and attachments to the promoted `F1`--`F7`
   infinity types; and
5. the resolved dual graph of infinity union ramification.

The tempting shortcuts remain invalid.  A square leading homogeneous
discriminant does not make the full discriminant square and does not imply a
Galois cubic.  Degree at most eight does not imply that a quadratic Miranda
basis exists.  A candidate-first realizability test can certify the latter
failure only one-sidedly: construct an actual rank-three algebra with a fixed
degree-eight `Delta_0`, then prove that no quadratic tuple has discriminant
equal to a nonzero scalar multiple of `Delta_0`.  Such elimination is
heavy/uncertain, so it is AWS-only and remains gated behind `SH-1` and `SH-2`.

No rational-tree or ramification attachment conclusion follows from the
discriminant bound alone.  No quadratic/cubic block closure, primitivity,
block occurrence, first-leg construction, map, counterexample, or JC2 result
is promoted here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7828`.
- Body SHA-256:
  `722d21d844f08c7a49b6231263b2a5a2e5d744e369192c39d71ac4c5ab3cb5a1`.
- Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.
