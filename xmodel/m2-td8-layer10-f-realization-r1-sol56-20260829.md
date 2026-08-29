# `td=8` reduced layer-10 f-side realization

Author: Sol 5.6 coordinator/primary. Date: 2026-08-29 UTC.
Lifecycle: `PRODUCER_CHECKED`; different-model review required.

## 0. Result

The reduced layer-10 question isolated by the provisional `(0,y)` report has
an explicit positive answer on the f-side. It is not a source-realization
obstruction.

**Theorem (`TD8-LAYER10-F-REALIZED`).** Let `i>=1`, `A,C in C*`, and set

```text
Phi_A(U)=(U-A)^3(U-(4/3)A)^2,
Z=x^17 y^10,
f_face(x,y)=C y^i Phi_A(Z)^i.                         (0.1)
```

Then `f_face` lies in the Newton rectangle

```text
0<=deg_x<=85i,  0<=deg_y<=51i,
```

has the root top `C eta^(85i)` at `(0,y)`, has no split on the first nine
elementary faces `j/17`, and at `j=10` has leading polynomial

```text
C ((eta^17-A)^3(eta^17-(4/3)A)^2)^i.                 (0.2)
```

For the reviewed route, take `i=i_tr=28(4+3t)`. This realizes the exact
f-side target uniformly for every integer `t>=0`.

More generally, any polynomial supported strictly below the tenth face may
be added without changing these ten layers. Thus the construction is an
affine family, not an isolated power. The genuine next gate is a *joint*
`(f,g)` source jet satisfying the common approximate-root tower and exact
Jacobian equations; an f-only layer-10 solve cannot kill the route.

## 1. Inputs and typing

The charged producer is Grok's provisional `(0,y)` initialization report

```text
xmodel/m2-td8-equal-join-zero-side-initialization-primary-grok46-20260829.md
full SHA-256 741b7198dd06b86ae7a8366163db56b473cd2929964a93a661e626301c84218f
body SHA-256 3d07291357a266225f6e269d876c62dc6a18c7271ac3a730999fede430c696f1.
```

It derives, provisionally and pending Opus review,

```text
k_f=85 i_tr,  l_f=51 i_tr,
P_1=...=P_9=0,
P_10=C ((eta^17-A)^3(eta^17-(4/3)A)^2)^i_tr.
```

At the y-pole root `(0,y)`, the elementary coordinate at height `j/17` is

```text
eta_j=y^(j/17) x,  equivalently x=y^(-j/17) eta_j.    (1.1)
```

This is the literal Puiseux coordinate of Notation 3.9 applied to the zero
branch. No assertion below uses the producer's gauge count, the g-side
initialization, exact total lambda, or polynomial landing.

## 2. Newton support

Expand `Phi_A(U)^i=sum_{q=0}^{5i} c_q U^q`. Every monomial of (0.1) is

```text
C c_q x^(17q) y^(i+10q),  0<=q<=5i.                 (2.1)
```

Hence

```text
0<=17q<=85i,
i<=i+10q<=51i.
```

The endpoint `q=5i` is the required corner
`C x^(85i)y^(51i)`, and `q=0` is nonzero because `A,C!=0`. Therefore the
entire support lies inside the exact f rectangle and spans its charged
corner-to-tenth-face segment.

## 3. The ten elementary faces

Substitute (1.1). Then

```text
Z=eta_j^17 y^(10-j),
f_face=C y^i Phi_A(eta_j^17 y^(10-j))^i.             (3.1)
```

For `0<=j<10`, the unique highest y-power in (3.1) comes from the monic
term `U^(5i)`. Thus

```text
d_j=i+5i(10-j)=(51-5j)i,
p_j(eta_j)=C eta_j^(85i).                            (3.2)
```

There is one root, zero, with full multiplicity at each of these faces; no
new characteristic coefficient or split occurs. The degree drops by
`5i=(85i)/17` at every microstep, exactly as the provisional transport
requires.

At `j=10`, every monomial (2.1) has the same y-degree `i`, so the whole face
survives:

```text
f_face(y^(-10/17)eta_10,y)
  =C y^i Phi_A(eta_10^17)^i,
```

which is (0.2). This proves the theorem without a coefficient solver.

## 4. Lower-face freedom

Let `R(x,y)` have Newton support inside the same rectangle and satisfy

```text
b-(10/17)a<i                                      (4.1)
```

for every monomial `x^a y^b` in `R`. It is below the tenth face. At a prior
height `j<10`,

```text
b-(j/17)a
  =(b-(10/17)a)+((10-j)/17)a
  <i+5i(10-j)=d_j,
```

because `a<=85i`. Thus `f_face+R` has exactly the same leading polynomials
through `j=10`. The allowed region is nonempty (it contains constants and
many interior monomials), so generic lower coefficients can be used for
squarefreeness or later joint equations without changing the charged jet.

This also identifies the full f-side solution space at the only scope needed
here: the fixed boundary polynomial plus the vector space of strictly
lower-face terms.

## 5. Consequence and exclusions

The earlier question “can a Newton-rectangle f realize the reduced tenth
layer?” is answered `YES` explicitly. It should not receive CAS or AWS time.
This does **not** establish the producer's stronger common 7-tuple claim;
that claim remains under Opus review.

In particular, this report constructs neither

- the corresponding g-side tenth face and lower layers;
- simultaneous approximate roots `h_j` from one global pair;
- the exact coefficientwise identity `J(f,g)=c0`;
- a normalized/irreducible Keller pair, source landing, finite total degree
  counterexample, or any JC2 conclusion.

The next honest object is the joint tenth-face module: write both Newton
rectangles, impose the reviewed g/trunk face, eliminate the enslaved tower
coefficients, and compute the first coefficient of
`J(f,g)-c0` not already forced by the top product law. A contradiction there
kills the initialization at source-jet scope; a solution only advances to the
next joint layer.

## 6. Review risks

A different model should verify:

1. the `(0,y)` orientation and coordinate `eta_j=y^(j/17)x` against the
   printed chart convention;
2. that the producer's `P_1,...,P_10` mean these consecutive elementary
   faces, rather than ordinary y-coefficient bands;
3. the rectangle labels `(85i,51i)` and absence of an additional
   normalization forbidding the lower-face perturbations.

If item 2 uses a different indexing convention, equations (2.1)--(3.2) still
give the literal geometric ten-face realization; only the label `P_10` must
be repaired. No web, AWS, heavy computation, or canonical edit was used.
This report does not access or depend on the separately owned formalization
repository.

---

Report-body SHA-256 (all bytes before the separator line above):
`8062dc8fc72f55ca2378ff39354f1c603b021bfe1558195b3673452313d0689e`.
