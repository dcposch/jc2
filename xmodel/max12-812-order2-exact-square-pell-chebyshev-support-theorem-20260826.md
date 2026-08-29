# `(8,12)` order two: exact-square combined-load Pell/Chebyshev support

Date: 2026-08-26

Status: **PRODUCER THEOREM, PENDING HOSTILE REVIEW.  EXACT SEVEN-TAIL
SUPPORT ONLY; TOTAL-REES/TARGET/TAYLOR PULLBACK NOT YET PROVED.**

## 0. Frozen inputs and correction

```text
40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94
  xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md
2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5
  xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md
73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6
  xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md
82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md
2b42cf9f0f28818341ccb63de5af3accf72c5dc3026f4ebe6aec17898f1d2f85
  cases/max12_812_order2_exact_square_pell_20260826/RESULT.md
2ba3ad04ca2fb181db9d146e947cfb5aa23588e1020a79577cfc72f80e388f65
  cases/max12_812_order2_exact_square_pell_20260826/EVIDENCE.sha256
```

The source audit already records that the literal identities
`F10(K^2)=K^5`, `F6(K^2)=K^3`, and `F2(K^2)=K` are false.  They are not
used here.  What is true is that, on an exact square `f=Q^2`, the combined
negative part of the three fractional powers is the negative part of

```text
sqrt(Q)*(k10*Q^2+k6*Q+k2).                              (0.1)
```

The theorem below shows why treating the three loads separately is also
false: their first seven tails have a genuine nonsquare cancellation locus.

## 1. Statement

Let `L` be a characteristic-zero field and put

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
Delta=p^2-4*r,                                           (1.1)
```

where `sqrt(Q)=z^2+O(1)` is the formal branch at infinity.  Let `E_l` be
the coefficient of `z^-l` in `H`.  Then, after geometric base change,

```text
V(E1,...,E7)_red
 = V(c,Delta)
   union
   V(c,16*beta-5*Delta,256*gamma-5*Delta^2).             (1.2)
```

Equivalently,

```text
rad(E1,...,E7)
 = (c,
    Delta*(5*Delta-16*beta),
    Delta*(beta^2-5*gamma)).                             (1.3)
```

The first component is the square locus and permits arbitrary load ratios.
The second is a nonsquare Chebyshev component whenever `Delta!=0`.

## 2. Exact coefficient construction

For any rational exponent `alpha`, write

```text
(1+p*t^2+c*t^3+r*t^4)^alpha=sum_(n>=0) a_n(alpha)t^n.
```

Logarithmic differentiation gives the exact recurrence

```text
n*a_n(alpha)=
 ((alpha+1)*2-n)*p*a_(n-2)(alpha)
+((alpha+1)*3-n)*c*a_(n-3)(alpha)
+((alpha+1)*4-n)*r*a_(n-4)(alpha).                       (2.1)
```

Consequently

```text
E_l=a_(10+l)(5/2)
    +beta*a_(6+l)(3/2)
    +gamma*a_(2+l)(1/2),             1<=l<=7.            (2.2)
```

The producer reconstructs (2.2) over `Q`, integerizes each equation, and
forms the exact ideal.  The denominators are

```text
256,1024,512,2048,2048,32768,4096.                       (2.3)
```

An independent `F_65521` lane gives the reduction of the same recurrence.

## 3. Why `c=0`

The exact-Q standard basis contains

```text
gamma^2*c,
3*beta^2*c^3-10*gamma*c^3,
5*c^3*p^2-8*beta*c^3-20*r*c^3,
75*c^5-48*beta^2*c*p^2+192*beta^2*r*c
       +160*gamma*c*p^2+128*gamma*beta*c-640*gamma*r*c,
```

together with the displayed full basis in the frozen result.  On `D(c)`,
the first row gives `gamma=0`; the second gives `beta=0`; the third gives
`Delta=0`; the remaining rows then force `p=r=0` and finally `c=0`, a
contradiction.  The direct exact saturation `(E1,...,E7):c^infinity` is the
unit ideal.  Thus every reduced solution has `c=0`.

This paragraph uses exact standard-basis membership.  A hostile review must
either independently verify the displayed elimination from (2.2) or replace
it with a CAS-free argument; a printed PASS token is not evidence.

## 4. Hand classification after `c=0`

When `c=0`, set

```text
T=z^2+p/2,       D=Delta/4,       Q=T^2-D.
```

Write

```text
Q^2+beta*Q+gamma=T^4+B*T^2+C,
B=beta-2D,
C=D^2-beta*D+gamma.                                    (4.1)
```

Expanding in `T^-1`, the first two possible negative terms of `H` are

```text
[T^-1]H=-(D/16)*(5D^2-6beta*D+8gamma),
[T^-3]H=-(D^2/128)*(5D^2-8beta*D+16gamma).             (4.2)
```

Because `T=z^2+p/2`, the map from these two coefficients to the possibly
nonzero coefficients among `E1,...,E7`, namely the `z^-2,z^-4,z^-6`
coefficients, is triangular.  Hence seven-tail vanishing is equivalent to
both expressions in (4.2) being zero.

If `D=0`, then `Q=T^2` is square and `beta,gamma` are arbitrary.  If
`D!=0`, subtracting the two bracketed equations gives

```text
gamma=beta*D/4.
```

Substitution gives

```text
beta=5D/4,       gamma=5D^2/16,
```

which is exactly the second component of (1.2).  This also factors (1.3)
as the intersection of the two displayed prime ideals.

## 5. Chebyshev identity and sharpness

Define

```text
P(Q)=Q^2+(5*Delta/16)*Q+5*Delta^2/256,
A=T^5-(5*Delta/16)*T^3+(5*Delta^2/256)*T.              (5.1)
```

Direct multiplication gives

```text
A^2-Q*P(Q)^2=Delta^5/262144.                            (5.2)
```

This is the scaled identity
`T_5(x)^2-(x^2-1)U_4(x)^2=1`.  On `Delta!=0`, `Q` is not a square, yet

```text
A-sqrt(Q)P(Q)=O(z^-10).                                 (5.3)
```

Thus even the first nine negative coefficients vanish.  The seven-row
bound is not merely failing on a nilpotent or a closure point: it has a
two-parameter reduced nonsquare family.

## 6. Source meaning and next gate

On a chart where `k10` is the leading load, divide (0.1) by `k10` and set

```text
beta=k6/k10,       gamma=k2/k10.
```

The reviewed Laurent-to-Faber change is unitriangular through seven rows,
so (1.2) is the mandatory lower-load receiver at a simultaneous-load tie.
It supplies a negative control for every complete-source compiler.

This is not yet a total-Rees theorem.  The source weights
`Lambda^2, Lambda^6, Lambda^10`, target weights `Lambda^(13),...,Lambda^19`,
and a chosen valuation ray determine which normalized coefficients become
`1,beta,gamma`; those substitutions must be made in the literal total source
before specialization.  A target tying the same grade is a separate row and
cannot be merged into (0.1).

The correct successor is therefore:

1. pull (1.2), including (5.1), into every total-Rees load-tie chart;
2. compute the first divided coefficient after (5.3), retaining the terminal
   `J` target and both Taylor families;
3. route `Delta=0` back to the moving fourth-power center and send
   `Delta!=0` directly to the terminal/Taylor receiver.

No strict arc is constructed or excluded here.  Nothing in this theorem
closes order two, `(8,12)`, maximum twelve, or JC2.
