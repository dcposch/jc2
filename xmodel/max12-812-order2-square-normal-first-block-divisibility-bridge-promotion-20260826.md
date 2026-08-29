# Promotion: square-normal first-block divisibility bridge

Date: 2026-08-26

Status: **PROMOTED AFTER DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen custody

```text
56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-theorem-20260826.md
85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-hostile-review-grok-v2-20260826.md
```

The V2 review independently rederived the polynomial division, reciprocal
coefficients, UFD valuation statement, repeated-factor incidence chart,
and characteristic-zero square-normal coefficient.  Its verdict is
`CONFIRMED`.  The cancelled V1 review produced no report and is not
evidence.

## Promoted algebraic theorem

Let `k` be a field, let `Q` be a monic depressed quartic, and let
`deg(N)<=3`.  If

```text
N^2=A*Q+R,                  deg(R)<=3,
N^2/Q=A+sum_(j>=1) h_j*z^(-j),
```

then the map from the four coefficients of `R` to
`(h1,h2,h3,h4)` is triangular with diagonal one.  Consequently

```text
h1=h2=h3=h4=0
  iff Q divides N^2
  iff h1=...=h7=0.                                  (2.1)
```

The same equivalence holds for the complete initial four ordinary-Faber
rows whenever the Laurent-to-ordinary connection is lower unitriangular
with diagonal one.  Four is sharp: the realizable remainder `R=1`
annihilates the first three coefficients but not the fourth.

In the UFD `k[z]`, writing

```text
Q_half=product_f f^ceil(v_f(Q)/2),
```

one has `Q|N^2` if and only if `Q_half|N`.  Hence:

```text
Q squarefree                         => N=0;
Q=A^2*D, gcd(A,D)=1, D squarefree   => N=M*A*D,
                                      uniquely for M in k.       (2.2)
```

More-degenerate factor types are not included in the second line and are
routed by the general `Q_half` classifier.

## Promoted source use

In characteristic zero, the first unloaded quadratic term for

```text
C=Q^2+epsilon^d*N+higher
```

is `(3/8)*epsilon^(2d)*N^2/Q`.  At a grade where no load, target, or
earlier correction ties this term, vanishing of the complete first four
ordinary source rows is therefore exactly the divisibility condition
(2.1).  On the coprime repeated-root chart `Q=A^2*D` with squarefree
quadratic `D`, the only nonzero first-normal direction is the scalar line
`N=M*A*D`.

At a tied grade this theorem classifies only the unloaded summand.  All
forcing terms and the predecessor ideal must remain raw until reduction.

## Firewall

This is an ordinary-first-four divisibility and factor-routing theorem.
It does not prove higher correction absorption, a Newton or normalized-
Rees fan, a two-sided source overlap, torsion or base-change control,
coverage of degenerate factor receivers, terminal/Taylor, order two,
`(8,12)`, maximum twelve, or JC2.
