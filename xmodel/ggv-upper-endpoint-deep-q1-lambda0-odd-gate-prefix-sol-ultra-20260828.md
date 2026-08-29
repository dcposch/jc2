# Deep q1 lambda-zero branch: exact q5, q7, and q9 prefix

Date: 2026-08-28  
Author: Sol Ultra / coordinator  
Status: **EXACT PROVISIONAL PRODUCER; INDEPENDENT ODD-TAIL AUDIT RUNNING**

## 1. Result

Continue on the reviewed characteristic-zero, squarefree branch-P locus
with `c2!=0`, exact `D=0`, and the full-system q1/q3 consequences

```text
lambda=0,  S=U=0.
```

The common-root Newton theorem gives `A|P1` and `A|F7`.  Hence, with the
authoritative degree windows,

```text
F2=-A^3 Q/8,                 deg Q<=2,
F4= A^2 Q^2/256,
F5= A^2 r/256,               deg r<=3,
F7= A f,                     deg f<=5.                 (1)
```

The next three odd de Rham coefficients are exactly

```text
q5 =p^3 r/1024,                                      (2)
q7 =p^3(f/4-Qr/65536),                               (3)
q9 =p^3(F9/4-3Qf/256-3Q^2r/2^23),                   (4)
```

where `p^2=A` after base extension.  Formula (2), together with exactness
of `q5 dX`, forces

```text
r in K*A'.                                             (5)
```

Formula (3) turns the q7 gate into a three-dimensional polynomial
connection image.  If

```text
w7=f/4-Qr/65536,
```

then q7 is exact iff

```text
w7 in { (5A'd+2Ad')/2 : deg d<=2 }.                   (6)
```

The harmless factor `1/2` may be absorbed into `d`.  Formula (4) is the
next affine input for the authoritative `F9` window `X*K[X]_(<=6)`.

These are real compressions, not an exclusion.  q9, q11, q13, the even
gates, the half-step Newton rows, and the endpoint face equations have not
yet been jointly solved.

## 2. Coefficient derivation

The reviewed Lagrange formula is

```text
q_n=2/(n+2) [t^n] F^((n+2)/8).                        (7)
```

With `F1=F3=0`, the weight-five coefficient has no nonlinear partition,
so

```text
q5=F5/(4p)=p^3r/1024.
```

At weight seven the only nonlinear odd partition is `2+5`, giving

```text
q7=pF7/4+F2F5/(32p^7),
```

which reduces to (3) under (1).  At weight nine the odd partitions are

```text
9,  2+7,  4+5,  2+2+5.
```

The generalized-binomial coefficients from exponent `11/8` give

```text
q9=p^3 F9/4
   +3(F2F7+F4F5)/(32p^5)
   -15F2^2F5/(512p^13),
```

and substitution of (1) gives (4).  An exact rational checker evaluates
(7) independently on three unrelated square-valued scalar fixtures and
rejects the `2^23 -> 2^22` mutation.

## 3. q5 connection-image collapse

Since `q5=p^3r/1024`, exactness of `q5 dX` is equivalent, after a nonzero
scalar rescaling of the primitive, to

```text
2A C'+3A'C=A r,              C in K[X,1/A].            (8)
```

At a simple root of `A`, a pole of positive order `m` in `C` would have
uncancelled leading coefficient `(3-2m)A'`; this never vanishes for
integral `m`.  Thus `C` is polynomial.  Degree comparison in (8) gives
`deg C<=4`.  Reduction modulo `A` gives `A|C`, so `C=A d` with `d` a
scalar.  Equation (8) becomes

```text
r=5d A',
```

which proves (5); conversely this choice supplies a primitive.

## 4. q7 connection image

Write `q7=p^3w7`.  The identical primitive calculation gives

```text
2A C'+3A'C=2A w7.                                    (9)
```

Again `C` is polynomial and `A|C`.  Now `deg w7<=5`, so `deg C<=6` and
`C=A d` with `deg d<=2`.  Substitution in (9) gives exactly (6), including
sufficiency.  The checker verifies that this image has rank three for two
different squarefree quartics.

## 5. Reproducibility and next target

Checker:

```text
cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gates_20260828/
  verify_lambda0_odd_gates.py
```

Expected marker:

```text
PASS_EXACT_LAMBDA0_ODD_GATE_PREFIX
```

The checker SHA-256 is

```text
d93ca0c7753097c4dcf6aae1cc58d1966780256700df4179e6e6fda9e30e1f64
```

The sharp successor is to derive q11 and q13 with the literal lower-window
floors retained, solve the five odd gates together, and then append the
four-root endpoint face equations.  D27, D29, and D31 are the licenses for
q5, q7, and q9 respectively; no formula here may be imported into a
shorter endpoint truncation.

No result is asserted on `lambda!=0`, another D-valuation branch, `c2=0`,
the unrestricted deep locus, all branch P, a Keller pair, or JC2.
