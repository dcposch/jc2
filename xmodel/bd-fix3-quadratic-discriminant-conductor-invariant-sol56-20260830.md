# Cubic blocks: basis-invariant discriminant and conductor index

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra coordinator  
Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`  
Lifecycle: **EXACT ALGEBRAIC PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Coefficient degree in a Miranda trace-zero basis is not intrinsic.  The full
trace-discriminant divisor is.  For a rank-three finite-flat algebra over

```text
A=C[u,v]
```

with a free global trace-zero module, every global basis change multiplies the
trace discriminant by a nonzero complex constant.  Thus its zero divisor is
basis-independent.  If one basis has Miranda coefficients of total degree at
most two, this intrinsic discriminant polynomial has total degree at most
eight.

For a full order inside its normalization, the discriminant divisor also
splits height-one-locally as

```text
Disc(order/A)=Disc(normalization/A)+2*Index.           (0.1)
```

The index is the determinant/Fitting divisor of the lattice quotient.  This
identity makes the intrinsic degree-eight divisor a possible interface to
normalization/conductor and full-boundary calculations.  It does not identify
the index with a curve delta invariant without a separate base-change and
local-order proof.

## 1. Trace-discriminant invariance

Let `B` be a finite locally free rank-three `A`-algebra, generically separable,
with trace splitting

```text
B=A*1 direct-sum E,             E=A*z direct-sum A*w.
```

For the ordered basis `e=(1,z,w)`, put

```text
Delta_e=det(Tr_B/A(e_i*e_j)) in A.                    (1.1)
```

If `g in GL_2(A)` changes the trace-zero basis, the full basis-change matrix
is `M=diag(1,g)`.  Therefore its trace Gram matrix becomes `M^T G M`, and

```text
Delta_(eM)=det(g)^2*Delta_e.                           (1.2)
```

But `det(g) in A^*=C^*`.  Hence the principal divisor and zero scheme cut by
`Delta_e` are independent of the chosen global trace-zero basis.  The
polynomial itself is defined only up to a nonzero scalar, which is sufficient
for branch/discriminant support and multiplicity.

This proof avoids convention choices in the binary-cubic tensor.  In raw
binary-cubic coordinates, ordinary variable substitution has discriminant
weight six, while the Miranda determinant twist changes the net exponent;
the trace-pairing calculation fixes the algebra invariant directly.

## 2. Degree-eight bound in a quadratic presentation

In a trace-zero Miranda basis, write

```text
Phi(X,Y)=bX^3-3aX^2Y+3dXY^2-cY^3.
```

The ordinary binary-cubic discriminant is, up to a fixed nonzero convention
scalar,

```text
81a^2d^2-108bd^3-108a^3c-27b^2c^2+162abcd.           (2.1)
```

For the Miranda multiplication table one can check the agreement directly:

```text
Tr(z^2)=6(a^2-bd),       Tr(zw)=-3(ad-bc),
Tr(w^2)=6(d^2-ac).
```

The determinant of the resulting `3 by 3` trace Gram matrix is exactly
(2.1), not merely support-equivalent.  Every term there has coefficient-
degree four.  Consequently

```text
deg_u,v(a,b,c,d)<=2       =>       deg_u,v(Delta)<=8. (2.2)
```

Cancellation may lower the degree or make the leading homogeneous
discriminant a square; neither event lowers coefficient degree in another
basis or makes the generic cubic extension Galois.  The bound applies to the
full affine discriminant, not merely the discriminant of the leading infinity
binary cubic.

For a generically separable finite-flat algebra, the trace discriminant is a
nonzero polynomial and its support is the non-etale/branch divisor.  Its
multiplicities are not automatically the reduced ramification support or the
target discriminant with multiplicity one.

## 3. Height-one order/normalization identity

Let `A` now be a normal noetherian domain with fraction field `K`, and let

```text
O subset O_tilde
```

be finite torsion-free full-rank `A`-orders in the same finite separable
`K`-algebra.  At a height-one prime `p`, `A_p` is a DVR and both orders are
free.  Choose bases so that inclusion `O_p -> O_tilde_p` is represented by a
matrix `M_p`.  The two trace Gram matrices obey

```text
G_O=M_p^T*G_Otilde*M_p,
ord_p(det G_O)=ord_p(det G_Otilde)+2ord_p(det M_p).    (3.1)
```

The effective Weil divisor with coefficient `ord_p(det M_p)` is the
determinant index divisor; equivalently it is the divisorial part of
`Fitt_0(O_tilde/O)`.  Summing (3.1) over height-one primes gives (0.1).
When `O_tilde` is the integral closure, the first term is the normalized-cover
trace discriminant/different contribution and the second records failure of
the chosen order to be normal.

No equality with a curve normalization length is automatic.  Such an
equality requires an actual one-dimensional slice or conductor stalk,
flat base change without hidden `Tor`, and proof that the compared order is
the curve coordinate order.  Vertical components, projective coefficient
basepoints, nonreduced infinity, and singular ambient closures can all break
a naive identification.

## 4. Exact campaign interface

For a fixed-basis quadratic cubic-block presentation, the pair

```text
(intrinsic discriminant divisor of degree <=8,
 height-one normalization index divisor)
```

is basis-safe input to the promoted rational-forest/full-boundary program.
The next finite calculation may stratify the promoted squarefree
bidegree-`(2,3)` infinity types by:

1. factorization and support of the full discriminant;
2. its intersection branches and multiplicities at infinity;
3. the order-to-normalization index divisor;
4. reduced ramification components and their divisor classes; and
5. the resolved dual graph of infinity union ramification.

Before any broad CAS elimination, one strict-henselian smooth control and one
singular rational-tree control must verify the base-change/conductor typing.
Any universal subresultant or primary-decomposition job is heavy/uncertain and
therefore AWS-only.

## 5. Nonclaims

This packet proves no bound on the minimum degree of Miranda coefficients over
all bases.  A degree-at-most-eight or square discriminant is not a
contradiction and does not imply a Galois cubic.  The conductor index formula
does not itself supply a boundary cycle, a one-place theorem, or an `A^2`
first leg.  No quadratic/cubic block closure, primitivity statement, map,
counterexample, or JC2 result follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6323`.
- Body SHA-256:
  `3362a7913801a180cf0d4ee06e9bf08ee13324ea598d72e0e8f797d59ff28ac5`.
- Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.
