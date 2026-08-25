# Max12 `(9,12)` Q8 Hurwitz-support and Taylor-freeness gate

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Result and strict scope

On the selected corrected-Q8 branch, the reviewed unordered critical-value
coordinates `tau` and `Delta` have been reconstructed through order `w^47`
from the exact six-row approximate-cubic quotient.  They descend evenly from
the auxiliary cover `t^2=w`, remain etale at the Q8 contact, and lie in the
generic unequal-value leaf.  At the good specialization

```text
prime=2003,       v=522,       Q8(522)=0,
```

all bounded plane-relation matrices described below have full column rank.
This exactly excludes rational relations in those finite rectangles for the
characteristic-zero selected branch.

The report also isolates a structural point: the complete Taylor families at
the true center are an invertible affine-coordinate change locally.  They
cannot impose a new coefficient-fibre equation; only their global
`C[x]` pole/integrality conditions can cut a trajectory.

No global equation, normalization, projective boundary, genus, rational
trajectory, all-`(9,12)`, maximum-twelve, counterexample, or JC2 conclusion
is claimed.

## 2. Exact unordered-Hurwitz reconstruction

In the frozen `p=1` approximate-cubic chart, write

```text
K=z^3+z+q_c,       q_c=t*c,       t^2=w,
f=K^3+x5*z^5+t*d4*z^4+x3*z^3+t*d2*z^2+x1*z+t.
```

Expanding gives the original depressed coefficients exactly:

```text
a0=t+q_c^3,                  a1=x1+3*q_c^2,
a2=3*q_c+t*d2,              a3=1+x3+3*q_c^2,
a4=6*q_c+t*d4,              a5=3+x5,
a6=3*q_c,                   a7=3.                    (2.1)
```

The replay reconstructs `g` from the pinned Faber compiler, not from a
spectral approximation.  With

```text
n=r6/p^9,       q=r8/p^10,       p=1,
s=-1/3-10*q/(9*n),
```

reduce in the reviewed quadratic algebra `z^2=s`:

```text
f^4=F0+F1*z,       g^3=G0+G1*z,
E=G0*F1-G1*F0,
Norm(F)=F0^2-s*F1^2,
Norm(W)=Norm((G0-F0)+(G1-F1)*z),

tau   =2*(G0*F0-s*G1*F1)/Norm(F),
Delta =4*s*E^2/Norm(F)^2.                            (2.2)
```

Every odd `t` coefficient of both `tau` and `Delta` through the reconstructed
order vanishes.  Thus they compress to series in `w`.  The exact modular
unit data are

```text
s(0)=334,          Norm(F)(0)=1491,    Norm(W)(0)=130,
[t]E=1556,         [w]tau=934,         [w]Delta=551       mod 2003.  (2.3)
```

Hence the reduction remains in the reviewed generic leaf
`s*Norm(F)*Norm(W)*E!=0` off the node, and `tau` and `Delta` are etale local
coordinates.  The calculation uses the reviewed norm identity with
`k=0`; no missing `W_k J(f,k)` term can occur.

## 3. Exact bounded relation exclusions

The replay checks by trial division that `2003` is prime, checks
`Q8(522)=0`, inverts every rational denominator encountered, and obtains

```text
det(six-row quotient Jacobian)=1296 !=0 mod 2003.      (3.1)
```

Hensel uniqueness therefore identifies the reduction of the selected Q8
formal branch.  For each of

```text
(theta,Delta),       (Delta,Z),
(tau,Delta),         (theta,tau),                     (3.2)
```

where

```text
theta=a0^2/p^9=w*(1+w*c^3)^2,       Z=q^9/n^10,
```

the replay forms all monomial rectangles satisfying

```text
1<=deg_left,deg_right<=10,
(deg_left+1)*(deg_right+1)<=36.                       (3.3)
```

There are `53` rectangles per pair.  In every one, the matrix of coefficients
`w^0,...,w^39` has full column rank.  Coefficients `w^40,...,w^47` are held
out for any discovered nullvector; there are no nullvectors to test.

This is a characteristic-zero exclusion, not merely heuristic modular
evidence.  If a nonzero `H in Q[X,Y]` in one of (3.3) vanished on the selected
branch, clear denominators and divide the integer coefficients by their gcd.
Its reduction modulo `2003` remains a nonzero coefficient vector.  The good
specialization and Hensel uniqueness would place that vector in the kernel
of the corresponding matrix, contradicting full column rank.  A single Q8
contact suffices because a rational-coefficient relation on the
characteristic-zero branch must survive every good conjugate specialization.

Nothing is excluded outside (3.3).  In particular, algebraicity of the
one-dimensional selected component guarantees some relation after a large
enough projection; this gate only proves that the natural Hurwitz/tail plane
models are not small.

## 4. Why no formal-local Taylor kill can exist

Let `R` be any characteristic-zero coefficient ring, let `u` be a unit, and
let `r in R`.  For a degree-`d` polynomial

```text
f(z)=sum_{i=0}^d a_i*z^i,
```

the substitution `P(y)=f(u*y+r)` has

```text
[y^ell]P=u^ell*sum_{i=ell}^d binom(i,ell)*a_i*r^(i-ell)
             =u^ell*f^(ell)(r)/ell!.                  (4.1)
```

After adjoining `u^(-1)`, this coefficient transformation is invertible:

```text
f(z)=P((z-r)/u).                                      (4.2)
```

Applying (4.1)--(4.2) simultaneously in degrees `9` and `12` proves that
the two complete Taylor families are a triangular coefficient-ring
automorphism with shared affine parameters `(u,r)`.  Therefore they create
no new formal-local equation on the depressed Q8 coefficient branch.  This
explains, rather than assumes, why the exact Q8 Taylor reconstruction did not
empty the branch.

Along an actual order-three trajectory one writes `u^3=h` and `r=u*R0`.
Kummer character makes the expressions (4.1) descend to `C(x)`, but the
original problem requires them to lie in `C[x]`.  Absence of finite poles and
the behavior at infinity are global divisor conditions and are not detected
by the local coefficient automorphism.  Thus the Taylor families remain
fully charged, but only at the global normalization/projective-boundary tier.

## 5. Next gate

The four new pairs and the four tail pairs in the frozen predecessor all
escape the `36`-monomial box.  More raw characteristic-zero elimination is
therefore poorly targeted.  The honest successor is either:

1. multi-prime higher-order support learning followed by exact lifting if a
   support stabilizes; or
2. a projective divisor/normalization calculation retaining the removed
   boundaries `w=0`, `x5=0`, `x3-2*x5=0`, `p=0`, together with the global
   Taylor pole conditions and terminal identity
   `nu^10*h^3*(Z')^9=j^9*Z^8`.

The currently running order-128 tail matrix is independent evidence and is
not an input to this frozen order-48 Hurwitz gate.

## 6. Replay

```sh
python3 cases/max12_912_order3_nu_q8_hurwitz_support_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_hurwitz_support_20260824/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_hurwitz_support_20260824/MANIFEST.sha256
```

The replay pins the reviewed norm theorem and immutable quotient-support
worker, rebuilds `f` and `g` from the exact coefficients, checks even descent
and generic-leaf units, and recomputes all `212` rank certificates.
