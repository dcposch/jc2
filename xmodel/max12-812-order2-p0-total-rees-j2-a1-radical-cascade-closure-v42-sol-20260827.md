# Ordered `T-a1`, `rho=0`: the two radical branches are empty through grade 19

Date: 2026-08-27  
Author: Sol cascade-extension lane  
Status: **EXACT Q CERTIFICATES; FROZEN RAW `rho=0` ROWS ONLY**

## Headline

The independently confirmed radical/field-point cascade can be completed.
Over `Q`, the frozen ordered-`a1`, `rho=0` raw equations through grade 19
have **no field point on `D(a1)`**.

The two branches die differently:

- A2 (`rs1 != 0`, hence `aa0=0`) is killed already at grade 16 by a
  two-row monomial identity that the prior review did not inspect.
- A1 (`rs1=0`) has a six-row ordinary ideal certificate
  `a1^8 in I_A1`.  It uses only `Tg13_1`, `Tg14_2`, and the diagonal
  compatibility rows `Tg15_3`, `Tg17_5`, `Tg18_6`, `Tg19_7`.

This closes the two branches before the requested two-grade stopping rule
can trigger.  It does **not** close the unspecialized-`rho` chart or an
honest Rees/Gate-T obligation.

## 1. Input split and correction to the prior review

The hostile review (SHA-256
`ede6b287bab76c00ac8d5b8e99e630a2006fcb7f252db0fa865764ad9dddb133`)
proved, at field-point/radical scope on `rho=0,D(a1)`, that

```text
e0=e1=ee0=ell1=0,  aa0*rs1=0.
```

It then described A1 (`rs1=0`) and A2 (`rs1 != 0`, so `aa0=0`) as
surviving branches.  All displayed identities in that review remain
correct.  Its statement that A2 survives the grade-16 prefix is not:
`Tg16_6` was simply not included in its selected A2 checks.  The present
result supersedes that narrow conclusion; it does not invalidate the
earlier split.

For clarity, the exact branch-cover identity itself is replayed here.  Once
the earlier cascade has forced `e0=e1=ee0=ell1=0`, the frozen row is

```text
Tg14_3 = -(3/16)*a1*aa0*rs1.
```

Thus on `D(a1)` every field point lies in the explicit cover

```text
V(rs1) union V(aa0).
```

The passage from the product equation to this union is the radical/field-
point step.  A1 is `V(rs1)`; A2 is `D(rs1) intersect V(aa0)`.

## 2. A2 dies at grade 16

After imposing only

```text
e0=e1=ee0=ell1=aa0=0,
```

the frozen rows give exact polynomial identities

```text
Tg13_2 = rs1*(-(3/32)*a1^2 + (5/1024)*k*rs1^2),
Tg16_6 = (3/256)*a1^2*rs1^2 + (15/32768)*k*rs1^4.
```

Consequently

```text
Tg16_6 - (3/32)*rs1*Tg13_2 = (21/1024)*a1^2*rs1^2.
```

The right side is nonzero on `D(a1*rs1)` over `Q`.  Thus A2 is empty.
Neither the previously derived value of `ee1` nor a guessed support is
needed.

## 3. A1 reduces to a five-variable diagonal core

Put

```text
A=a1, b=aa0, E=ee1, c=cs1, l=ell2
```

and impose the A1 branch equations

```text
e0=e1=ee0=ell1=rs1=0.
```

On `D(A)`, the two rows with unit leading coefficients eliminate `ec3`
and `rs2` exactly:

```text
ec3 = A*c - A^(-1)*b*E,

rs2 = -4*A^(-3)*b^2*E + A^(-2)*E^2
      -4*A^(-1)*b*c -4*A^(-1)*E*l.
```

Let `Fbar_g` denote the indicated frozen row after these two exact
substitutions:

```text
Fbar_15 = Tg15_3   (7 terms)
Fbar_17 = Tg17_5   (9 terms)
Fbar_18 = Tg18_6  (10 terms)
Fbar_19 = Tg19_7  (24 terms).
```

These are the successive diagonal components of the rank-five
compatibility block identified by the exact symbol report.  No sparse
coordinate restriction was made.

## 4. Compact localized unit identity

Define the Laurent multipliers

```text
H15 = -96*A^(-8)*b^3*E +24*A^(-7)*b*E^2
      -96*A^(-6)*b^2*c -192*A^(-6)*b*E*l
      +144*A^(-5)*b*l^2 +48*A^(-5)*E*c
      +48*A^(-4)*c*l -16*A^(-3),

H17 = -192*A^(-6)*b*E +192*A^(-5)*b*l +96*A^(-4)*c,
H18 = 192*A^(-5)*E,
H19 = 384*A^(-5)*b.
```

Pure exact sparse arithmetic gives the coefficientwise identity

```text
1 = H15*Fbar_15 + H17*Fbar_17 + H18*Fbar_18 + H19*Fbar_19.
```

Every `Hg` is homogeneous of sigma weight `-g`, so this is not an
inhomogeneous normalization artifact.  The replay lifts the identity back
through the `ec3` and `rs2` eliminations using exact divided differences.
The resulting direct Laurent multipliers for the six raw branch rows have
term counts

```text
grade       13  14  15  17  18  19
terms       17   8   8   3   1   1.
```

The worst denominator is `A^(-8)`.  Clearing it gives the ordinary
polynomial ideal certificate

```text
a1^8 in (
  Tg13_1, Tg14_2, Tg15_3, Tg17_5, Tg18_6, Tg19_7
)
```

after the A1 branch specialization.  Thus A1 is empty on `D(a1)`.  The
grade-16 A1 compatibility row is valid but is not needed by this smaller
certificate.

V39's 24-term `Tg19_7` compatibility residual is consistent with this
result: the grade-19 row is genuinely used here, with multiplier
`384*A^(-5)*b`; it was not silently replaced by a quotient equality from a
dual functional.

## 5. Combined conclusion and exact scope

The prior radical split sends every field point to A1 or A2.  The exact A2
identity kills A2 at grade 16, and the exact A1 saturation certificate
kills A1 at grade 19.  Therefore the complete frozen raw ordered-`a1`,
`rho=0` prefix through grade 19 has no field point on `D(a1)` over `Q`.

Scope firewalls:

- The entry into A1/A2 is radical/field-point reasoning; the A1 branch
  closure itself is an ordinary `a1^8` ideal-membership certificate.
- `rho` was set to zero in the frozen row bytes.  No conclusion is made
  about the unspecialized `rho` family.
- These are raw source rows.  No saturated-Rees/base-change, honest chart,
  Gate-T, bounded-degree, or JC2 conclusion follows without the registered
  comparison step.
- The result uses a subset of the full prefix; that is sufficient for
  emptiness, but it does not identify the full ideal or its multiplicities.

The complete localizer/division ledger is:

| step | localization or division |
|---|---|
| inherited cascade | `D(a1)` throughout; its now-discarded Case B used `D(ell1)` |
| branch cover | `D(a1)`, followed by the field-point split `aa0*rs1=0` |
| A2 kill | `D(a1*rs1)`; the two-row identity itself uses no division |
| A1 elimination/certificate | `D(a1)` only; no division by `aa0`, `ee1`, `cs1`, or `ell2` |
| denominator clearing | Laurent powers end at `a1^(-8)` and clear to the ordinary target `a1^8` |

All coefficient arithmetic is over `Q`.  No positive-characteristic claim
is being made; in particular the displayed A2 scalar `21/1024` is used as
a unit only over characteristic zero.

## 6. Replay and custody

```sh
python3 cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py
```

The replay:

1. pins the V37 loader and all three consumed reports;
2. revalidates all 70 frozen row hashes through the V37 loader;
3. checks the two A2 row formulas and their exact combination;
4. checks the A1 eliminations and the compact Laurent unit identity;
5. constructs and replays the lifted direct certificate;
6. clears denominators and verifies `a1^8` coefficientwise in the ordinary
   polynomial ring; and
7. rejects a fixed one-coefficient mutation of `Tg19_7`.

Discovery used one desk-scale local Singular reduction of the four-variable
dehomogenized core and one eight-variable lift; each took under one second.
The banked proof does not trust Singular: it is a pure-Python `Fraction`
replay and takes about 0.6 seconds.  No heavy computation, AWS job, network,
or `jc2-lean` access was used.  No canonical ledger was edited.
