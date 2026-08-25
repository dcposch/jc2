# FT2/Faber deduplication V3: no new maximum-12 high row

Date: 2026-08-25  
Owner: cube trajectory  
Status: **FAIL-CLOSED DEDUPLICATION; RANKING CORRECTION**

This note supersedes the dedicated `15%` FT2 allocation proposed in
`ideation-20260825T1950Z-cube-classical-closure-v2.md` (SHA-256
`6053690012ed023f17e455821a93a178795b4410325c402566517bc55257082d`).
The V2 closed-core criterion is mathematically useful, but it does not buy a
new row on the maximum-12 partial-`y` cells because a stronger universal
theorem is already frozen and different-model confirmed.

## Exact duplication

Charged parent:

- `max12-partial-y-shared-faber-probe-20260824.md`, SHA-256
  `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036`;
- its `CONFIRMED` review, SHA-256
  `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c`.

That theorem works over the differential Kummer root field for every monic
depressed partial-`y` pair, without assuming that the polynomial core has
rational centralizer `k(K)`.  It already proves:

```text
w=f^(1/m),                    g=sum h_j [w^j]_+,
h_j'=0,
r_1'=...=r_(m-2)'=0,         m r_(m-1)'=j/u.
```

For `(m,n)=(9,12)` on the order-three leaf, put `R=w^3=f^(1/3)`.  Kummer
character and the three reviewed target gauges leave only `h_12=1` and
`h_6=k`.  Hence the proposed FT2 formula is exactly

```text
g=[w^12+k w^6]_+=[R^4+k R^2]_+.
```

Before quotient, the other terms `R^3,R,1` are precisely the already-known
Faber constants at indices `9,3,0`.  Thus the fractional-power four-resonance
normal form is a change of notation for the universal Faber integration.
It proves none of the eleven high rows anew at a broader scope.

The lower differential consequence also duplicates.  On the order-three
leaf the reviewed character calculation already gives

```text
r1=r2=r4=r5=r7=0,       r3=mu,       r6=nu,
9 r8'=j/u.
```

The existing exact order-three compiler reconstructs all eight `r_l`.
Therefore computing `r3`, `r6`, or merely rewriting the terminal row through
`R` is not a new successor.  The strict-total squarefree rows 18--12 remain a
useful independent method/control, but their transfer to partial `y` adds no
scope to the Faber theorem.

## First genuinely new consequence

The first new theorem must cross the boundary explicitly left open by the
Faber review: **classify an algebraic lower-Laurent fibre and impose the
original Taylor polynomiality families on it.**  Merely expanding another
Laurent coefficient is insufficient.

The smallest nonduplicate `(9,12)` target is a source-honest component of

```text
r1=r2=r4=r5=r7=0,       r3=mu,       r6=nu,
```

outside the already reviewed selected `k=mu=0,nu!=0` Q8 component.  The clean
first split is the previously unhandled `k!=0` chart, retaining `k` as a
constant/localized parameter until a normalization is licensed.  Every
candidate component must then carry:

```text
u^ell/ell! * partial_z^ell f(A/9) in k[x]   (0<=ell<=9),
u^ell/ell! * partial_z^ell g(A/9) in k[x]   (0<=ell<=12),
9 r8'=j/u.
```

A genuinely new bounded endpoint would be one of:

1. an exact component/pole-prime classification showing that every
   normalization has positive genus or at least two Taylor pole primes;
2. an exact finite-pole valuation contradiction using one of the two Taylor
   families and the terminal row; or
3. a smallest rational one-pole survivor with all 23 Taylor coefficients and
   `r8` reconstructed.

The existing `r1,r2` rank controls, a new `r3` formula, dimension of an
unloaded coefficient ideal, or a recurrence match alone do not pass this
gate.  The order-four `(8,12)` lower fibre remains the cheapest independent
control, exactly as the Faber review recommends.

## Revised rank and allocation

FT2 is demoted from a standalone discovery lane to an algebraic
reparameterization/software accelerator inside the lower-fibre work.  No
dedicated heavy FT2 generator should launch.

```text
general max12 lower fibres + Taylor boundary   45%
TD6 source-complete cover                      25%
AS support-growing/unbounded tower             20%
global landing/cofinality                      10%
standalone FT2                                 0%
```

A small hand/formal audit of the FT2--Faber equivalence is enough; any later
code must be justified by a named lower component and accepted only if it
reduces the Taylor/pole-support calculation.

## Firewall

This deduplication does not classify the `k!=0` chart, show that either Taylor
family is polynomial, exclude the order-one leaf or `(8,12)`, alter the
selected-Q8 theorem, close maximum twelve, or prove JC2.  No computation was
launched for this note.
