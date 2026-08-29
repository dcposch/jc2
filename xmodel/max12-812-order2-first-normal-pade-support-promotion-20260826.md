# Promotion: nonzero-load Padé lemma and complete `(8,12)` order-two first-normal support

Date: 2026-08-26

Status: **PROMOTED CHARACTERISTIC-ZERO REDUCED-SUPPORT THEOREM; NO STRICT
ARC OR ORDER-TWO VERDICT.**

## Frozen theorem, review, and coefficient control

```text
2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5
  xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md
73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6
  xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md
cd64414259598e5982e8895fdb43df91bfb11c6b47e6c99aa1c1b590930a92bb
  cases/max12_812_order2_pade_coeff_verify_20260826/RESULTS.md
8e1acd1350f036a350ccd0e94bada440c360fa305c01d1a9271e824c9bd625af
  cases/max12_812_order2_pade_coeff_verify_20260826/FREEZE.sha256
f160bce5e109fc45fffb2627affd2915e6ad4126a2c35b46bb5761a3de51b421
  cases/max12_812_order2_pade_coeff_verify_20260826/RESULTS.sha256
```

The different-model hostile review returned `CONFIRMED`, with no failing
identity and no missing hypothesis that breaks a numbered claim.  The
independent registered AWS recurrence control verifies the three finite
binomial coefficients and the final contradiction identities exactly; it
is corroboration, not a substitute for the reviewed Laurent argument.

## Promoted statement

Let

```text
K=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
F=(3/8)*N^2/K+k10*K^(5/2),
I=(q1,...,q7),
```

where the `q_l` are the reviewed first-normal Faber rows.  Over every
characteristic-zero field,

```text
k10 != 0 and q1=...=q7=0
    => c=0 and p^2=4*r
    => K=(z^2+p/2)^2.                                        (1)
```

The proof is finite.  Seven vanished tail coefficients give
`F-[F]^z_+=O(z^-8)`.  Multiplication by `K` forces the `z^-1,z^-2,z^-3`
coefficients of `K^(7/2)` to vanish.  With `d=p^2-4r`, those coefficients
are nonzero scalar multiples of

```text
c*(-5*d^3+40*p*c^2*d-8*c^4),
d^4-48*p*c^2*d^2+32*c^4*(d+2*p^2),
c*(5*p*d^3-10*c^2*d*(d+4*p^2)+24*p*c^4).
```

If `c=0`, the middle row gives `d=0`.  If `c!=0`, the first and third
give `p*c^2=5*d^2/8` and `c^4=5*d^3/2`; the middle row then becomes
`76*d^4=0`, a contradiction.

After geometric base change, define

```text
Lsq: K=(z^2+s)^2,
     N=(z^2+s)*(alpha*z+beta),
     k10 arbitrary;

D:   K=(z-a)^2*(z^2+2*a*z+e),
     N=lambda*(z-a)*(z^2+2*a*z+e),
     k10=0;

Z:   N=0, k10=0, K arbitrary.
```

Then the complete raw reduced support is

```text
V(I)_red=Lsq union D union Z.                                 (2)
```

For the exact reviewed saturation

```text
Istar=((I:(p,c,r)^infinity)
          :(n0,n1,n2,n3,k10)^infinity),
```

one has

```text
V(Istar)_red=Lsq union D.                                     (3)
```

Thus the residual set `E` of the saturation-slice erratum is empty.  The
two-prime minimal-prime agreement is no longer needed for the
characteristic-zero support claim.

## Scope firewall and successor

Equations (1)--(3) classify only the reduced support of the first nonzero
normal/load gate.  They do not determine nilpotent thickness, lift either
component through the next divided jet, cover later first contact, impose
the terminal `[6,2]` passport or either Taylor boundary, construct or
exclude a strict arc, close order two or `(8,12)`, prove maximum twelve, or
prove JC2.

The immediate successor is componentwise: compute the next divided jet on
`Lsq` and on `D`, retaining their higher-contact sections and assigning the
square/discriminant intersection to an explicit weighted chart.
