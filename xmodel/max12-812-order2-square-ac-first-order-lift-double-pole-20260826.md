# `(8,12)` order-two square fan: first-order lift kills `d=2` except one vector

Date: 2026-08-26

Status: **HAND TRUNCATED-DIVISIBILITY LEMMA, CONDITIONAL ON COMPLETE
SOURCE/FABER TIMING AND NONZERO-COEFFICIENT REPLAY.  NO BRANCH VERDICT.**

## Scope

Work on the generic unit-load chart `D(p*k0)` after the reviewed vertical
contact gates.  Put

```text
a=ord_sigma(A)>=1,  c=ord_sigma(C)>=3,
r=ord_sigma(R)>=2,  d=c-a,  s=r-a.
```

This note treats the unique-`AC` families

```text
d=2, s>=1;  and  d=2, s=0, a>=4.
```

It complements the reviewed-design `d=1` double-pole discriminator.  The
only unique-`AC` `d=2` vector left open is
`(a,c,r)=(3,5,3)`.  Both `d=3` families and all tied first faces also remain
open.

## Truncated divisibility lemma

Let `epsilon` denote displacement from the first `AC` grade and write

```text
L(epsilon)=L0+epsilon*L1+...,
A(epsilon)=A0+epsilon*A1+...,
C(epsilon)=C0+epsilon*C1+....
```

If the negative parts of the first two coefficients of

```text
A(epsilon)*C(epsilon)/L(epsilon)
```

vanish, then there are polynomials `P0,P1` such that

```text
A(epsilon)*C(epsilon)
  =L(epsilon)*(P0+epsilon*P1)+epsilon^2*E(epsilon). (1)
```

Consequently the coefficient of `epsilon^2` in the quotient has at most a
simple pole along each root of `L0`: after subtracting the polynomial
truncation in (1), it is `E(0)/L0`.  In particular the apparent second
denominator-motion terms cannot retain a double pole once the silent
intermediate grade has imposed first-order divisibility.

This is an identity in the truncated polynomial ring; it uses neither a
radical nor a reduced-support assertion.

## Application to the `d=2,s>=1` fan

The exact lower-hull gaps after the unique first `AC` term are

```text
C2:   2,
A2:   2,
RC:   1+s,
R3:   a+3*s-2,
RA2:  a+s,
A3:   a+3.
```

Thus grade one after `AC` contains only the next coefficient of `AC/L`.
The source equations at the first two grades therefore give the hypotheses
of (1).  At grade two, orient the first divisibility over the etale root
algebra as

```text
L0=u*v,  A0=alpha*u,  C0=gamma*v,
alpha*gamma!=0.
```

The nonzero `C2` contribution is

```text
(3/8)*C0^2/L0^2=(3/8)*gamma^2/u^2,                 (2)
```

which has a double pole at `u=0`.  Every possible competitor at this grade
has pole order at most one:

- the second `AC` coefficient, by (1);
- `A2=k0*A0^2/L0`;
- `RC=k0*R0*C0/L0` when `s=1`; and
- `R3=k0*R0^3/L0` when its gap is two; and
- `RA2=R0*A0^2/L0^2` when its gap is two, because this expression is
  regular at `u=0` (its possible double pole is at the opposite root
  `v=0`).

Thus (2) is unmatched at its root even at `(a,c,r)=(1,3,2)`, where all five
displayed successor terms occur together.  Polynomiality is impossible on
the entire `d=2,s>=1` family.

## The shifted `d=2,s=0` family

Here `r=a`, `c=a+2`, and uniqueness of `AC` requires `a>=3`.  The `RC`
term occurs one grade after `AC`, but the two complete quotient families
combine exactly as

```text
(3/4)*A*C/L + sigma*(5/8)*k*R*C/L
  =(3/4)*(A+(5/6)*sigma*k*R)*C/L.                  (3)
```

Put `Atilde=A+(5/6)*sigma*k*R`.  Its leading polynomial is still `A0`.
For `a>=4`, `R3` has gap `a-2>=2`, so the intermediate grade contains only
the next coefficient of the single quotient in (3).  The truncated
divisibility lemma applies to `Atilde*C/L`.

At grade two, `C2` again has the double pole (2).  Contributions from the
residual coefficient of (3), `A2`, and (only when `a=4`) `R3` have at most
a simple pole there; `RA2` has gap `a>=4`.  Hence the same unmatched-double-
pole contradiction eliminates every `d=2,s=0,a>=4` arc.

At `a=3`, `R3` joins `RC` at the intermediate grade.  It is not contained in
the exact factorization (3), so first-order divisibility of `Atilde*C` does
not follow.  The lone vector

```text
(a,c,r)=(3,5,3)
```

therefore remains a dedicated two-successor exact client.

## Exact client acceptance test

A source client should fail closed unless it verifies:

1. the complete seven source rows and moving lower-unitriangular
   Laurent/Faber bridge through the first `AC` grade plus two;
2. symbolically, rather than by a finite valuation sample, the gap table
   above, identity (3), and absence of every other registered term at each
   claimed silent grade;
3. the truncated identity (1), for `A*C` or `Atilde*C` as applicable,
   including moving `p`, all first corrections, and its conclusion that the
   residual second coefficient has denominator at most `L0`;
4. the exact nonzero coefficient `3/8` in (2), both root orientations, and
   the fact that `RA2` is regular at the nominated `C2` pole even when
   `a+s=2`;
5. exact `Q` as the proof endpoint and one good-prime software control.

## Firewall

Conditional on the exact source replay, this lemma eliminates only the
unique-`AC` `d=2` subcone away from `(a,c,r)=(3,5,3)`.  It does not cover
that vector, either `d=3` family, a tied first face, positive-order or
ramified loads, `p=0`, `k0=0`, the exact-square zero
section, terminal/Taylor conditions, fan exhaustiveness, order two,
maximum twelve, or JC2.
