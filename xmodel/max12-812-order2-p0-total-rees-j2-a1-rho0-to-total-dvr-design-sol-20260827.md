# Ordered `T-a1`: exact route from the raw `rho=0` closure to a total chart certificate

Date: 2026-08-27  
Author: Sol total-lift design lane  
Status: **EXACT RING/MAP REDUCTION; WEIGHT-30 AWS DISCRIMINATOR AUTHORIZED, RESULT PENDING**

## Headline

V42 does not automatically close the honest ordered `T-a1` chart.  It proves
that the raw rows after `rho=0` have no point on `D(a1)`, hence that some
power of `a1` belongs to the *specialized* raw ideal.  The honest total chart
instead requires saturation by `a1` **before** specialization, and these two
operations need not commute.

There is, however, a much smaller exact conversion problem than a general
multivariate Groebner saturation.  Put `t=rho^2`.  At each sigma weight
`w=5N`, all complementary-weight multiples of the literal total rows form a
finite matrix over the PID `Q[t]`.  A typed total certificate exists at
exponent `N` exactly when the target vector for `a1^N` belongs to that column
module over the DVR `Q[t]_(t)`.  Equivalently, its class in the cokernel is
annihilated by a polynomial `U(t)` with `U(0) != 0`.  Normalizing gives the
literal identity

```text
a1^N * U(rho^2) in J,
U(0)=1,
U(rho^2)=1+rho*(rho*(U(rho^2)-1)/rho^2).
```

Thus this is exactly the requested `a1^N*(1+rho*W)` certificate type, with
no genuine localizer.  The first permitted exponent is `N=6`: V38 proves
`a1^N` is not in the raw grade-through-19 ideal for `N<=5`.

## 1. Ambient rings, chart presentation, and maps

Let `X_19` be the 65 positive-sigma-weight coefficient variables occurring
in the ordered-`a1` source through grade 19.  The only weight-zero variable
left on this ordered stratum is `rho`.  Work first in

```text
S = Q[rho, X_19],                    wt(rho)=0, wt(x)>0 for x in X_19.
```

The literal actual-total emitter gives homogeneous rows
`F_{g,r} in S`, `10<=g<=19`, `1<=r<=7`, after applying the source quotient

```text
rs=cs=c0=c1=a0=0.                   (ordered T-a1 restriction)
```

Let `J=(F_{g,r})` in `S`.  In the unreduced second-stage presentation one
adjoins the `a1`-chart ratio `q=a0/a1`, the bilinear `a1*q-a0`, the four
`J1` equations, and the ordered equation `q=0` (equivalently `a0=0` after
`a1`-saturation).  Eliminating these displayed variables gives the honest
ordered chart ring

```text
C = S / K,                 K = J : a1^infinity.          (1)
```

Here `a1` is the exceptional coordinate.  It is absorbed by saturation; it
is **not** inverted in `C`.

Specialization is the graded map

```text
sp : S -> S0=Q[X_19],      rho |-> 0,
J0 = sp(J).
```

V42 (report `5d4c42ff...`, replay `f4ec7293...`) proves

```text
(J0 : a1^infinity) = (1)                                  (2)
```

over characteristic zero at radical/no-field-point scope, and supplies an
ordinary `a1^8` certificate only after its A1 branch specializations.  It
does **not** supply a global `a1^8` membership in `J0`.

The honest total special fibre is instead

```text
C/rho*C = S / (K+(rho)).                                  (3)
```

There is only the safe inclusion

```text
(K+(rho))/(rho)  subseteq  J0:a1^infinity.                (4)
```

The right side being the unit ideal does not force the left side to be the
unit ideal.  This is precisely the promoted staged-calculus converse
correction `593f953b...`.

## 2. Exact equivalence with a typed total certificate

The following conditions are equivalent.

1. The honest ordered total chart has empty `rho=0` fibre:
   `K+(rho)=(1)`.
2. There are `N>=0` and `W in S` with
   `a1^N*(1+rho*W) in J`.
3. There are `N>=0` and `U(rho) in Q[rho]`, `U(0)=1`, with
   `a1^N*U(rho) in J`.
4. There are `N>=0` and `U(t) in Q[t]`, `U(0)=1`, with
   `a1^N*U(rho^2) in J`.

Proof.  (2) implies (1) by the promoted saturation theorem.  If (1) holds,
write `1=k+rho*h` with `k in K`.  Since `K` is sigma-homogeneous, its
weight-zero part gives `U(rho)=1-rho*h_0(rho) in K intersect Q[rho]`.
Membership in the saturation supplies an `N` with `a1^N*U in J`, proving
(3).  Projecting any identity in (2) to weight `5N` proves the same reduction
directly: every non-`rho` variable has positive weight, so the weight-zero
part of `W` is univariate in `rho`.  All total rows are even under
`rho -> -rho`; averaging `U(rho)` and `U(-rho)` preserves `U(0)=1` and
membership, proving (4).  Finally (4) is a special case of (2), because
`U(rho^2)-1` is divisible by `rho` (indeed by `rho^2`).

This equivalence is closure-first.  It neither assumes Rees base-change
equality nor inverts `a1`.

## 3. Why the lift is not automatic: homogeneous even counterexample

Let

```text
S_toy = Q[rho,f,x],       wt(rho)=0, wt(f)=wt(x)=1,
J_toy = (f-rho^2*x).
```

After `rho=0`, `f in sp(J_toy)`, so the raw special system is empty on
`D(f)`.  The ideal is already `f`-saturated: its quotient is the domain
`Q[rho,x]` under `f |-> rho^2*x`.  Nevertheless no identity

```text
f^N*(1+rho*W) in J_toy
```

exists.  In the quotient its left side is
`rho^(2N)*x^N*(1+rho*W(rho,rho^2*x,x))`, a nonzero polynomial.  Equivalently,
the honest total special fibre retains the entire `f=x=0` exceptional
direction.  This toy has the same sigma homogeneity and even-rho parity as
the live source, so neither property repairs the specialization/saturation
gap by itself.

At fixed weight one, its module matrix over `Q[t]` is the single column
`(1,-t)^T`, while the target is `(1,0)^T`.  The target is in the image at
`t=0`, but its first correction residual `(0,1)^T` is outside the image.
This is the exact failure mode the live discriminator must detect.

## 4. Fixed-weight DVR formulation

For `w=5N`, let `B_w` be all positive-variable monomials of sigma weight
`w`.  For every row of grade `g<=min(19,w)` and every monomial `m` of weight
`w-g`, form `m*F_{g,r}` and express it in `B_w`.  This gives

```text
A_w(t) : Q[t]^(products_w) -> Q[t]^(B_w),
b_N    : coordinate vector of a1^N.
```

Then

```text
there is a typed exponent-N total certificate
  <=> [b_N]=0 in coker(A_w) tensor_Q[t] Q[t]_(t)
  <=> (im(A_w):b_N) is not contained in (t).
```

The last colon is computed without a multivariate standard basis.  Form the
syzygy module of the columns `[A_w | b_N]` over the univariate PID.  The last
coordinates of its generators generate `(im(A_w):b_N)`.  A generator whose
last coordinate has nonzero constant term gives `U(t)` and all row
multipliers.  If every last coordinate is divisible by `t`, exponent `N`
is obstructed.  The syzygy relation itself is the exact replay certificate.

A sparse support-incidence pass first keeps only the connected component of
`b_N`.  This is exact: no column outside that component has a coordinate in
common with the target component.  Specializing `t=0` first gives a cheaper
gate.  If `a1^N` is not in the raw `rho=0` slice, then no total exponent-`N`
certificate can exist; the exact rational separating functional is already
a final negative certificate for that exponent.

## 5. Registered first run

Case:

```text
cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827
```

The first run is only `N=6`, weight 30.  It must:

1. regenerate the general-`rho` rows through grade 19 from the literal V35
   emitter and bridge all 70 `rho=0` images byte-exactly to V23/V28/V30/V33/
   V35 through the V37 loader;
2. check sigma homogeneity, even rho parity, the 65-variable census, and the
   complete complementary-weight product census;
3. run the V42 A1-branch `a1^8` replay as a real-source `rho=0` positive
   control, including its corrupted-`Tg19_7` rejection;
4. decide exact-Q `rho=0` membership first, with an independent finite-prime
   selector lane;
5. only if that gate is positive, compute the univariate syzygy/colon over
   `Q[t]` and independently over a finite field, saving the exact syzygy and
   `U(t)`; and
6. stop after six hours or 192 GiB per lane and report before trying `N>6`.

The exact-Q lane is authoritative.  A finite-field result is selector and
software-corroboration evidence only.  A positive total result still closes
only the frozen grade-through-19 ordered `T-a1` chart; it does not establish
source/landing coverage, the terminal receiver, Gate T, order two, maximum
twelve, or JC2.

