# `(8,12)` order-two square fan: shifted-factor lift reduces unique `d=3`

Date: 2026-08-26

Status: **HAND LOCAL TRUNCATED-DIVISIBILITY LEMMA, CONDITIONAL ON COMPLETE
SOURCE/FABER TIMING AND NONZERO-COEFFICIENT REPLAY.  NO BRANCH VERDICT.**

## Scope and claim

Work on the generic unit-load chart `D(p*k0)` after the reviewed vertical
contact gates.  Put

```text
a=ord_sigma(A)>=1,  c=ord_sigma(C)>=3,
r=ord_sigma(R)>=2,  d=c-a,  s=r-a.
```

On the unique-`AC` family `d=3`, the hand argument below eliminates every
integral valuation vector except

```text
(a,c,r)=(1,4,2), (2,5,3), (4,7,4), (5,8,5).       (E)
```

This conclusion remains conditional until an exact source client verifies
the complete timing and shifted-factor identities.  The four vectors in (E)
remain live exact clients.

## Local lifting principle

The first `AC` equation gives, over the etale root algebra and up to deck
swap,

```text
L0=u*v,  A0=alpha*u,  C0=gamma*v,
alpha*gamma!=0.                                    (1)
```

Work in the local ring at `u=0`, where `v` and `C0` are units.  If all
coefficients through order `j` of a quotient `X(sigma)*Y(sigma)/L(sigma)`
are regular there, truncated division shows that its next coefficient has
at most a simple pole.  Terms already regular at `u=0` do not interfere with
this conclusion: the source equation forces the quotient coefficient itself
to remain regular after those terms are moved to the other side.

For `d=3`, the exact successor gaps are

```text
A2:   1,
RC:   1+s,
C2:   3,
R3:   a+3*s-3,
RA2:  a+s-1,
A3:   a+2.                                         (2)
```

The coefficient ratios in the frozen Laurent receiver are

```text
(kA2)/(AC)=(5/32)/(3/4)=5/24,
(kRC)/(AC)=(5/8)/(3/4)=5/6.                        (3)
```

Thus the apparent early cancellations are coefficients of shifted products,
not free double-pole terms.

## Case `s>=2`

Put

```text
Ctilde=C+(5/24)*sigma*k*A.                          (4)
```

The full `AC` and `kA2` quotient families combine as

```text
(3/4)*A*C/L+sigma*(5/32)*k*A^2/L
  =(3/4)*A*Ctilde/L.                               (5)
```

Before gap three, `RC` and `R3` are absent.  The only possible early `RA2`
case is `(a,s)=(1,2)` at gap two, but `R*A0^2/L0^2` is regular at `u=0`
because `A0^2` cancels the `u^2` denominator.  Hence (5) is regular at
`u=0` through order two.

At gap three the nonzero `C2` term is

```text
(3/8)*C0^2/L0^2=(3/8)*gamma^2/u^2.                 (6)
```

It has a double pole.  The residual coefficient of (5) has at most a simple
pole.  `RC` when `s=2` and `R3` if present have only denominator `L0`;
`RA2` and `A3` are regular at `u=0` because their numerators contain
respectively `A0^2` and `A0^3`.  Thus (6) is unmatched and all `s>=2`
vectors are impossible.

## Case `s=1`

Now `RC` enters at gap two.  Through that order put

```text
Ctilde=C+(5/24)*sigma*k*A,
Atilde=A+(5/6)*sigma^2*k*R.                         (7)
```

Then `(3/4)*Atilde*Ctilde/L` reproduces `AC`, `kA2`, and `kRC` through
gap two.  Its first extra cross term occurs at gap three and is a scalar
multiple of `k^2*R*A/L`, which is regular at `u=0` by (1).

The only nonregular term that can occur before gap three is `R3/L`, whose
gap is `a`.  Therefore the shifted quotient is regular through order two
when `a>=3`; at gap three the same unmatched double pole (6) gives a
contradiction.  The two cases `a=1,2` are precisely the first two vectors
in (E).

## Case `s=0`

Here uniqueness of `AC` requires `a>=4`, and both `kA2` and `kRC` enter at
gap one.  Put

```text
Ctilde=C+(5/24)*sigma*k*A,
Atilde=A+(5/6)*sigma*k*R.                           (8)
```

Again `(3/4)*Atilde*Ctilde/L` reproduces the two corrections.  Its gap-two
cross term is a scalar multiple of `k^2*R*A/L`, regular at `u=0`.  The
only possible nonregular interruption before gap three is `R3/L`, now at
gap `a-3`.  For `a>=6` it occurs no earlier than the target grade and has
only a simple pole, so (6) is again unmatched.  The cases `a=4,5` are the
last two vectors in (E).

## Exact client acceptance test

A dual-field client should fail closed unless it verifies:

1. all seven complete source rows and the moving lower-unitriangular
   Laurent/Faber bridge through the first `AC` grade plus three;
2. the symbolic gap table (2), with no finite-box substitution for `a,s`;
3. the exact coefficient ratios (3) and shifted-product identities
   (5), (7), and (8), including moving `p`, moving `k`, and every correction
   which can reach the charged grades;
4. local regularity at the nominated root of the `RA2`, `A3`, and shifted
   cross terms, rather than merely comparing global denominator powers;
5. the exact nonzero double-pole coefficient `3/8` in (6), both root
   orientations, and the exception list (E);
6. exact `Q` as the proof endpoint and one good-prime software control.

## Firewall

Conditional on exact replay, this lemma eliminates only the unique-`AC`
`d=3` family outside (E).  It does not eliminate the four exceptional
vectors, any tied first face, unique `RC`, positive-order or ramified loads,
`p=0`, `k0=0`, the exact-square zero section, terminal/Taylor conditions,
fan exhaustiveness, order two, maximum twelve, or JC2.
