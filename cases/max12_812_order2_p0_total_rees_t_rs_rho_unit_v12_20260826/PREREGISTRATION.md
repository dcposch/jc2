# Preregistration: total-Rees `T-rs` rho-unit certificate V12

Date: 2026-08-26

Status: **EXPLICIT PREFIX CERTIFICATE ON THE ACTUAL SATURATED `D_+(rs)`
CHART.  NO OTHER CHART, WHOLE ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## Charged input

Consume only the four grade-10/12 coefficient files

```text
Tg10_1, Tg10_2, Tg10_3, Tg12_6
```

from the frozen V9 exact-Q and independently compiled F65521 manifests:

```text
Q       86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e
F65521  dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4
```

Every coefficient file must rehash against its manifest.  The prime client
must also compare its four inputs coefficientwise with reduction of the
exact-Q files.  Quotient rings are forbidden.

## Exact certificate

Make the actual `D_+(rs)` chart substitution

```text
cs=rs*qcs,  c0=rs*qc0,  c1=rs*qc1
```

and divide the four charted rows by their generatorwise common powers:

```text
P1   = Tg10_1 / rs,
P2   = Tg10_2 / rs,
P3   = Tg10_3 / rs^2,
P126 = Tg12_6 / rs^2.
```

Each division must have an exact multiplication-back check.  Put

```text
V = 8*rho^2*qcs^2+3,
U = 1+32*rho^2*qcs^2*V.
```

The client must test, by ordinary polynomial arithmetic, the identity

```text
35*rs^2*k*U
 = 32768*P126 + 4096*P2 + 8192*rs*qcs*P3
   + 12288*rho^2*qcs*P1.                         (1)
```

It must independently reconstruct the four-term total correction and the
intermediate decomposition

```text
B = -12288*qcs*P1 + 1120*rs^2*qcs^2*k*V.         (2)
```

Dropping the `P1` term in (1), or replacing `32` by `31` in `U`, must leave
a nonzero polynomial.

Let `E=(P1,P2,P3,P126)` and let

```text
J = E:rs^infinity.
```

Compute `J` by `elim.lib` saturation or independently by eliminating an
inverse variable from `(E,1-u*rs)`.  Equation (1) predicts
`35*k*U in J`.  The computation must verify this membership and then verify

```text
k in J+(rho),
U in J[1/k],
rho*(-32*rho*qcs^2*V)=1 in J[1/k],
1 in J+(rho)+(1-v*k).
```

No outcome is accepted from a banner alone; bases and certificate
polynomials must be written and hash-bound.

## Meaning if PASS

On the registered `D(k)` open of the actual saturated `D_+(rs)` prefix,
(1) gives `U=0`.  Since `U=1+rho^2*(...)`, it gives an explicit inverse for
`rho`.  Hence no DVR arc centered at `rho=0` can lie in this chart.  This
proves the `T-rs` Gate-T obligation at the complete grade-12 prefix on
`D(k)` even if saturation and specialization disagree at an earlier prefix.

The conclusion depends on the already audited completeness of the total
source through grade 12 and on the standard saturated-chart theorem.  It
does not cover `k=0`, the other five Rees charts, the secondary `A` fan, the
terminal/Taylor receiver, another order-two component, maximum twelve, or
JC2.
