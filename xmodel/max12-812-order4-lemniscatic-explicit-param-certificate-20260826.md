# `(8,12)` order-four residual target: explicit lemniscatic parameter certificate

Date: 2026-08-26

Status: **EXACT TARGET-CURVE THEOREM WITH CLEAN AWS V3 CERTIFICATE; SOURCE
PROJECTION PREMISE REMAINS OPEN.**

## 0. Charged target theorem

Let `P(q,v)` be the exact residual plane of
`max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md`, SHA-256
`cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756`.
Its independent confirmed review has SHA-256
`59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a`;
the nonmutating tangent-coordinate erratum has SHA-256
`26a083fcfa805a52fdb295ceaaf94ae7497047d8545a2323a48a688ac39e2300`.
The coordinate-free lemniscatic corollary is independently **CONFIRMED** at
target SHA-256
`97ace425a5fc0dc03aa12edb2e09f29e3143566b0939d3ce833a3872ee32a07f`
and review SHA-256
`09684e0be2784758b97f7e82e19ae9c8a33c7375d637417740d8f21b7d686425`.

Write `X` for the complete normalization of `P=0`.  The charged theorem
gives `g(X)=0`, the boundary valuations of `q`, and

```text
div_X(v)=8P_0-P_ul-P_A-6P_B.                         (0.1)
```

All statements below concern this target curve.  They do not supply the
independent source-component projection premise.

## 1. Exact rational parameter

On `P1_T`, put

```text
q=T^2(T-1),
D=(T-1)(21T-22)(3T-2)^6,
v=5184/D.                                             (1.1)
```

Direct substitution into the full displayed residual polynomial, followed
by multiplication by `D^3`, is identically zero.  Thus (1.1) gives a
nonconstant rational map to the residual plane, which extends to its
projective closure and factors through `X`.

This map is birational.  Indeed, the charged boundary theorem gives

```text
div_X(q)=2P_L+P_ul-3P_0,
```

so `q:X -> P1` has degree three.  The composition (1.1) is the degree-three
polynomial `T^2(T-1)`.  Hence the intervening map `P1_T -> X` has degree one.
In particular, (1.1) is an exact parameterization of the complete
normalization, not merely a rational curve lying in the affine plane.

The places in (0.1), together with the finite left tangency, are

```text
P_L:  T=0,       q=0,          v=81/22,
P_ul: T=1,       ord(v)=-1,
P_A:  T=22/21,   ord(v)=-1,
P_B:  T=2/3,     ord(v)=-6,
P_0:  T=infinity,ord(v)=8.                            (1.2)
```

The exact branch identities are

```text
27q+4=(3T-2)^2(3T+1),
9261q-484=(21T-22)(441T^2+21T+22).                   (1.3)
```

Equations (1.1)--(1.3) recover every point and multiplicity in (0.1).

## 2. Fourth-power removal and fixed elliptic model

Define

```text
S=24(T-1)/(3T-2).
```

Then `S=0,1,infinity` at `P_ul,P_A,P_B`, respectively, and direct
cross-multiplication gives

```text
(1/v)/(S(S-1))=(3T-2)^8/124416.                      (2.1)
```

Over the algebraic closure choose `c` with `c^4=124416`.  On `Y:y^4=v`,
put

```text
xi=c/((3T-2)^2 y).
```

Equation (2.1) is exactly

```text
xi^4=S(S-1).                                         (2.2)
```

Thus the complete normalization of the residual deck cover is the fixed
lemniscatic `(4,4,2)` Kummer curve.  Put `W=2S-1`; then

```text
W^2=1+4xi^4.
```

On a common dense chart set

```text
X_E=2(W+1)/xi^2,       Z_E=4(W+1)/xi^3.              (2.3)
```

Clearing denominators in (2.3) gives

```text
Z_E^2=X_E^3-16X_E.                                   (2.4)
```

The inverse `xi=2X_E/Z_E` makes (2.3) birational; smooth projective
completion makes it an isomorphism.  In particular `j(Y)=1728`.

Implicit differentiation of `W^2=1+4xi^4` gives
`W dW=8xi^3 dxi`.  Differentiating (2.3) and clearing denominators gives

```text
dX_E/Z_E=-dxi/W.                                     (2.5)
```

Since `dX_E/Z_E` is a nonzero regular differential on (2.4), (2.5) is an
explicit regular differential certificate on the normalized target.

## 3. Clean AWS V3 certificate

The frozen client is

```text
cases/max12_812_order4_lemniscatic_target_20260826/
  FREEZE_V3.sha256
  lemniscatic_param_v3.sing
  REGISTRATION_V3.md
```

It ran only on AWS Box03 under tag
`max12_812_order4_lemniscatic_param_v3_20260826T023700Z_box03`, launcher
PID `142619`, with an `8388608 KiB` virtual-memory cap.  The source archive
SHA-256 is
`943001f0d9df92fa6da2c3ebd77f192ad092ce07439a7aca34c0f5e750611d13`.
The lane ended cleanly with `rc=0`, `11320 KiB` maximum RSS, no swap, every
identity sentinel equal to one, and final token
`LEMNISCATIC_PARAMETER_CERTIFICATE_V3=PASS`.  Its stdout SHA-256 is
`18f18c5e164f1645a9a24c983ac0be078ca3c5569c909aacdfa1bc258ffe8f69`;
stderr SHA-256 is
`607ade63d4015ed45b68392acc58d34a8c42e1d0c6716512eb67b7759042f27a`
and contains only resource accounting.

V1 failed inside `paraPlaneCurve`; V2 passed the arithmetic but emitted a
terminal `exit(0)` engine diagnostic.  They are immutable **NO VERDICT**
controls and are not consumed.

## 4. Exact scope and next gate

This theorem completely identifies the reconstructed residual target and
its deck cover.  It becomes an exclusion theorem only after proving that
every relevant loaded order-four source component has a nonconstant
`(q,y)` map to this target.  The exact prime-lift, `dim(J)=1`, nonverticality,
and `a6`-complement jobs are independent and still required.  No target-only
identity here is used to infer source-component coverage.
