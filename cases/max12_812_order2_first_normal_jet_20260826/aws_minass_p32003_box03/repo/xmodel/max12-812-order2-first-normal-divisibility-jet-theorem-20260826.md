# `(8,12)` order two: first exact normal/divisibility jet of the one-parameter Rees family

Date: 2026-08-26

Status: **PRODUCER THEOREM AND AWS CLIENT CONTRACT; NO EMPTINESS VERDICT.**

## 0. Charged inputs

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md
0fa0dc4afb160ae4b9ed6bc195e1158e44b92cdc5bb5ea1619a146e9d52aac96
  xmodel/max12-812-order2-u2-62-oneparameter-rees-runit-delta-review-grok-20260826.md
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e
  xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md
aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495
  xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
```

The promoted one-parameter family is

```text
Phi_l = r_l(C,Lambda^2 k10,Lambda^6 k6,Lambda^10 k2)
        -Lambda^(12+l) delta_l,
(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4).
```

All seven finite loads are retained.  The source audit and its erratum give
the common-quartic reduced support and the exact fact that the unloaded tail
map has zero first differential in every coefficient direction there.

## 1. Exact normal chart

Write

```text
K=z^4+p z^2+c z+r.
```

Use the following polynomial coordinates over `Q`:

```text
C6 = 2p,
C5 = 2c,
C4 = p^2+2r,
C3 = 2pc       + Lambda n3,
C2 = c^2+2pr   + Lambda n2,
C1 = 2cr       + Lambda n1,
C0 = r^2       + Lambda n0.                         (1.1)
```

At `Lambda=0`, these are exactly the coefficients of `K^2`.  Conversely,
on `D(Lambda)` the transformation is invertible:

```text
p=C6/2,
c=C5/2,
r=C4/2-C6^2/8,
n_i=(C_i-[K^2]_i)/Lambda,  0<=i<=3.                 (1.2)
```

Thus (1.1) is an exact blow-up/divisibility chart, not a projection of a
load and not a truncation of a formal series.  The zero section
`n0=n1=n2=n3=0` records arcs with higher normal contact; it must not be
discarded when discussing all strict arcs.

## 2. Universal `Lambda^2` divisibility

Pull every `Phi_l` back by (1.1).  Then

```text
Lambda^2 divides Phi_l                  for 1<=l<=7.  (2.1)
```

Proof: at `Lambda=0` the unloaded coefficient is `K^2`, so every unloaded
tail vanishes.  Its first coefficient differential is zero along the whole
common-quartic locus, so substituting a displacement `Lambda*n` makes the
unloaded part divisible by `Lambda^2`.  The `k10` contribution already has
the factor `Lambda^2`; the `k6` and `k2` contributions have factors
`Lambda^6` and `Lambda^10`; and every nonzero target has exponent at least
`14`.  Affine linearity of the exact tails in the three lower loads rules
out a hidden lower power.  This proves (2.1) as a polynomial identity.

Define the exact divided rows

```text
Theta_l = Phi_l(1.1)/Lambda^2.                         (2.2)
```

On `D(Lambda)`, `(Phi_1,...,Phi_7)` and
`(Theta_1,...,Theta_7)` define the same scheme because `Lambda^2` is a
unit.  Hence any strict arc in this chart specializes to the boundary of
the divided family after the usual `Lambda` and `J` saturations.

## 3. First normal gate

Put

```text
q_l = Theta_l mod Lambda,
Q1  = (q_1,...,q_7).                                  (3.1)
```

Every `q_l` is a quadratic form in `n0,n1,n2,n3` plus `k10` times the exact
`k10` load derivative at `K^2`.  It is independent of
`k6,k2,mu2,mu4,mu6,J`.  This independence is a direct exponent statement,
not an elimination or generic-chart projection; the full first boundary is
the product with the affine space in those six variables.

Let

```text
mK=(p,c,r),
mN=(n0,n1,n2,n3,k10).
```

The first nonzero-normal-direction gate is

```text
Q1^* = (Q1:mK^infinity):mN^infinity.                  (3.2)
```

Saturation by `mK` removes only the projective common-quartic origin;
saturation by `mN` isolates contact exactly one in this normal/load chart.
Any genuine strict arc whose first nonzero normal/load contact occurs at
order one gives a point of `V(Q1^*)`.  Therefore `Q1^*=(1)` would force
higher contact; it would not exclude arcs of order at least two.  A nonunit
`Q1^*` is a finite exact stratum list for the next divided jet.

For exact chart closure rather than this necessary first gate, one must use

```text
((Theta_1,...,Theta_7):Lambda^infinity):J^infinity
```

before imposing `Lambda=0`.  The AWS probe may compute that stronger object
only as a separately labelled endpoint.  It may not identify unsaturated
`Q1` with the full Rees boundary.

## 4. AWS compiler contract

An AWS-only compiler must:

1. pin all charged bytes and the canonical all-tail digest;
2. reconstruct all seven exact tails, verifying weight and affine lower-load
   dependence;
3. emit (1.1), the exact pulled-back `Phi_l`, and fail unless every remainder
   modulo `Lambda^2` is zero;
4. form the divided `Theta_l` and independently verify
   `Lambda^2 Theta_l=Phi_l`;
5. form `Q1`, fail if any forbidden variable
   `k6,k2,mu2,mu4,mu6,J` occurs, and compute (3.2);
6. print basis size, dimension, unit test, and a factor/minimal-prime probe
   only within a registered memory/time cap;
7. preserve the distinction between `Q1^*`, the zero normal section, and the
   fully saturated divided-family boundary.

## 5. Firewall

This theorem is an exact first divisibility jet.  It is independent of the
terminal value of `U`, so it may stratify the five order-two `U=4` terminal
classes simultaneously, but it does not test their terminal maps or Taylor
boundaries.  It does not prove the one-parameter boundary empty or nonempty,
exclude `[6,2]`, close order two, close `(8,12)`, prove maximum twelve, or
prove JC2.
