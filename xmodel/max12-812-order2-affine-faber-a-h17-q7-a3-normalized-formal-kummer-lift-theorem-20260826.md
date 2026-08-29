# Provisional theorem: the H17/q7/a3 normalized Kummer receiver lifts formally

Date: 2026-08-26

Status: **PROVISIONAL THEOREM.**  The grade-48 predecessor is
hostile-review confirmed.  The finite grade-51 reduction is dual-AWS PASS
and under hostile review.  This all-orders composition requires its own
hostile review before promotion.

## 1. Exact scope and coordinates

Work over a complete local characteristic-zero algebra with uniformizer
`t`.  Use only the already registered two-sided normalized affine-Faber
coordinate chart.  Write

```text
a=t^3 A,       lambda=t^17,
X=t^7 Xbar,    Y=t^7 Ybar,
R_i=t^14 Rbar_i,  S_i=t^14 Sbar_i,

K10=t^42 kappa,
K6=t^42((15/32)kappa E^2+t^6 d6),
K2=t^42((15/256)kappa E^4+t^6 d2),
mu2=t^42(-(5/4096)kappa E^6+t^6 dm),
mu4=t^48 d4.
```

The remaining even target begins with `mu6=t^54 nu6`; the odd target
begins with `J=t^57 j`.  They and all unlisted tangent/complement series
are free inputs.  Let

```text
A(0)=a3, E(0)=p, M(0)=m.
```

On the `X` chart assume `a3*p*m*Xbar(0)` is a unit.  On the `Y` chart
assume `a3*p*m*Ybar(0)` is a unit.  No inversion of `kappa` is needed in
the proof; the constant equation below implies that it is a unit at the
displayed receiver.

The theorem is internal to this complete normalized graph.  In
particular, `t` is not identified with the original source parameter and
this statement does not assert a total-Rees point.

## 2. First implicit block

Let `P1,...,P7` be the seven complete normalized ordinary-Faber row
series after the exact substitution above.  Divide the five rows

```text
(P1,P3,P6,P2,P4)
```

by their common first weight `t^48`.  On the `X` chart take dependent
series

```text
(Sbar0,Ybar,d2,dm,d4),
```

and on the `Y` chart replace `Ybar` by `Xbar`.  At `t=0`, after the
preceding variables in this order have been eliminated, the diagonal
Jacobian entries are respectively

```text
3m/4,  -3*x*m/8,  p^4/128,  -1,  -1             (X chart),
3m/4,  -3*y*m/8,  p^4/128,  -1,  -1             (Y chart).
```

Here `x=Xbar(0)` and `y=Ybar(0)`.  Thus the first five equations uniquely
solve the five dependent series over either registered localization.
This is a formal implicit-function statement, not merely a coefficient
count: once the constant face is fixed, the same unit Jacobian solves the
next coefficient at every order.

The confirmed grade-48 predecessor supplies the constant solution and
the two projective charts.  The complete grade-48--51 replay verifies that
the two remaining transformed equations have no coefficient before
weight 51 after this first solve.

## 3. Second implicit block

Use the exact row combinations

```text
K = E*H3+H5,
H = 2*E^2*P3+16*E*P5+64*P7-(E^3/2)*P1,
```

where `H3,H5` are the registered inverse-Faber combinations.  After the
first block is solved, define

```text
Khat=t^-51 K,   Hhat=t^-51 H.
```

Their constant terms are the complete grade-51 equations.  In the
dependent variables `(d6,kappa)`, their triangular Jacobian at `t=0` is

```text
[ -a3*p^5/32       *             ]
[       0       5*a3^3*p^7/4     ].
```

The `*` is irrelevant.  The two diagonal entries are units on the stated
open.  Consequently `Khat=Hhat=0` uniquely solve the full series
`d6(t),kappa(t)` for arbitrary values of every free input series,
including arbitrary `nu6(t)` and `j(t)`.

Combining the two stages, a triangular representative of the full
seven-by-seven dependent Jacobian has determinant

```text
45*x*m^2*a3^4*p^16 / 2^19
```

on the `X` chart and the same expression with `x` replaced by `y` on the
`Y` chart.  These are characteristic-zero units exactly on the registered
opens.

## 4. Constant receiver and formal conclusion

At the constant level, `Hhat(0)=0` gives

```text
kappa(0)=8*m^3/(5*a3^3*p^5).
```

After the first five solves, `Khat(0)=0` gives

```text
d6(0)=36*(Rbar0(0)*m^2-Ybar(0)^2)/p^4
      -5*kappa(0)*a3^2*p-2*m^3/(a3*p^4).
```

On the `X` chart the first-block cross pivot has `Ybar(0)=0`; on the
`Y` chart its displayed square remains.  These are precisely the two
finite grade-51 reductions.

Therefore the normalized receiver

```text
5*kappa(0)*a3^3*p^5-8*m^3=0
```

has a unique all-orders formal lift in the seven dependent series, for
every choice of the other formal inputs sufficiently centered at the
registered point.  Because `j(t)` is a free input and first enters only at
weight 57, one may choose `j(0)` to be a unit.  The resulting normalized
ordinary-Faber formal solution has `J=t^57 j(t)` generically nonzero.

As an algebraic constant sheet, this receiver is rational when the
campaign load `kappa(0)` is allowed to vary, by solving for it.  Over fixed
`kappa(0)` it is the indicated cubic Kummer relation.  No deck action or
global component statement is needed for the lift.

## 5. Proof of the all-orders step

For completeness, the only formal lemma being used is the standard
coefficient form of the complete-local implicit-function theorem.  If
`F(t,U,V)=0` has a solution modulo `t`, and the Jacobian in the dependent
coordinates `U` is a unit modulo `t`, then, for every fixed free series
`V`, the coefficient of `t^n` is affine linear in the new coefficient
`U_n` with the same invertible Jacobian.  Induction gives a unique
compatible solution modulo every `t^n`, and completeness gives the
unique formal solution.  The first and second blocks above meet this
hypothesis separately; substituting the first block before applying the
second is legitimate because its solution is a formal coordinate graph.

The finite V6 calculation is used only to certify the constant second
block, its two pivots, and divisibility through weight 50.  No finite
calculation is being mistaken for an all-orders truncation proof.

## 6. Explicit nonclaims and next gates

This theorem does **not** show that the formal normalized solution is in
the image of a literal unspecialized source/total-Rees chart.  It does not
settle moving-source/ramified overlap, symmetric-algebra torsion, or
blowup/base-change compatibility.  It does not impose terminal `[6,2]`
or either finite Taylor pullback.  It therefore is neither a polynomial
Jacobian pair nor a counterexample, and it does not close order two,
`(8,12)`, maximum twelve, or JC2.

The next independent gates are:

1. hostile review of the finite grade-51 reduction and then of this
   complete-local composition;
2. literal total-Rees/source accessibility of the receiver;
3. exact terminal `[6,2]` pullback;
4. both finite Taylor pullbacks, with all targets and load corrections
   retained.

Until those gates pass, this is a strong normalized receiver theorem only.
