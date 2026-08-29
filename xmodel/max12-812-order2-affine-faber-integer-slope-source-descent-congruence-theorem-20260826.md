# Order-two affine-Faber integer-slope source-descent congruence

Date: 2026-08-26

Status: **PROVISIONAL ELEMENTARY THEOREM; HOSTILE REVIEW REQUIRED.**

## 1. Statement

Work at either unramified coefficient-infinity point of the fixed
order-two `U=2,[6,2]` source.  Let `tau=T-1` (or its unit-equivalent
opposite-sheet coordinate), so every actual rational source coefficient
has a Laurent expansion in `L((tau))`.  On an integer strict ray write

```text
Lambda=tau^alpha*u(tau),       alpha in Z, alpha>3,
u(0) != 0.                                           (1.1)
```

After the ordinary unit twist, let `C` be the scaled centered monic octic
and perform exact monic square division

```text
C=Q^2+Delta,       deg_z(Delta)<=3.                  (1.2)
```

Choose a cube root `sigma` of `Lambda` after a harmless finite constant or
complete-local extension, and suppose a normalized cell declares

```text
ord_sigma(Delta)=H<infinity.                         (1.3)
```

Then every literal rational-source germ in this cell satisfies

```text
3 divides alpha*H.                                   (1.4)
```

In particular, when `gcd(alpha,3)=1`, one must have `3|H`.  On the
balanced strict ray used by the provisional H17 Gate-A composition,

```text
varrho=tau*(unit),       Lambda=tau^3*varrho,
alpha=4,                                               (1.5)
```

so neither `H=16` nor `H=17` can descend to an actual rational coefficient
germ.  The next integral normalized normal order after the compatible
`H=15` cell is `H=18`.

## 2. Proof

For an actual source trajectory, every invariant coefficient `A_i` is a
rational function of the base coordinate.  Since the selected infinity
place is unramified, its completion is `L((tau))`.  On the integer ray
(1.1), `Lambda` also lies in `L((tau))`.  Hence every scaled coefficient
`B_i=Lambda^(8-i)A_i`, every ordinary coefficient
`C_i=(1+tau)^(i mod 2)B_i`, and every coefficient of the monic quotient
`Q` and remainder `Delta` in (1.2) lies in `L((tau))`.  Monic square
division uses only addition, multiplication, and division by `2`, so it
does not enlarge this complete field.

Consequently the nonzero vector `Delta` has an integral `tau`-valuation.
On the other hand, `sigma^3=Lambda` and (1.1) give

```text
ord_tau(sigma)=alpha/3.
```

The normalized declaration (1.3) therefore gives

```text
ord_tau(Delta)=alpha*H/3.
```

This number must be an integer, proving (1.4).  Multiplication by the unit
`u(tau)`, extraction of its Henselian cube root, and the odd-coefficient
unit twist do not change any valuation.

Equivalently on the balanced ray, take the common ramification

```text
tau=s^3,       varrho=s^3*(unit),       sigma=s^4*(unit).
```

Every pulled-back literal source coefficient lies in `L((s^3))`, so its
nonzero valuation is divisible by three.  But a normalized `H`-normal has
valuation `4H`; hence `3|4H`, or `3|H`.

## 3. Consequence for the H17 artifacts

The normalized complete-local H17/q7/a3 theorem and its finite exact
prolongations are not contradicted.  They concern a solution over the
ramified field `L((s))`.  What fails is descent of that solution to the
literal rational coefficient field `L((tau))` on the balanced source ray.

Accordingly the statement

```text
tau=s^3, varrho=s^3, sigma=s^4
```

does produce a point after ramified base change, but flatness of the toric
map does not imply that its coefficient series are fixed by the descent
group `s -> zeta_3*s`.  Without that fixed-locus condition it is not a
rational-source germ.  The provisional artifact

```text
xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-arcwise-gate-a-composition-theorem-20260826.md
```

must therefore be quarantined at **ramified formal source-row** scope and
its literal rational-source accessibility conclusion withdrawn on the
balanced ray.

## 4. Exact scope and nonclaims

This obstruction applies to integer strict slopes (and in particular the
named slope-four lift).  It does not exclude the same normalized `H` on a
different toric slope for which `3|alpha*H`, and it does not by itself
classify fractional slopes.  It does not refute the normalized IFT,
finite-grade identities, or fixed-branch grade-72 prolongation.  It does
not solve the `H=18` predecessor, the finite Taylor families, the other
source fan cells, order two, `(8,12)`, maximum twelve, or JC2.

No CAS is used in this theorem.
