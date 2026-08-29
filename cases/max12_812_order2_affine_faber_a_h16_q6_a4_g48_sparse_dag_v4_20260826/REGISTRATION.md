# Registration: coefficient-only sparse DAG for the H16 equality wall

Date: 2026-08-26

Status: preregistered producer; no theorem claim.

## Question

Compute exactly the single coefficient

```text
[s^48] (P7-E(s)^2 P3/32+E(s)^3 P1/64)
```

on the fixed `H=16,q=6,ord(a)=4` moving-discriminant source family.  The
previous complete-row, three-row, and quotient-ring clients all materialized
large substituted Faber rows and timed out.  They remain immutable timeout or
long-running controls and are not inputs to this client.

## Method

The client imports the frozen complete `tails.json`, reconstructs only rows
`1,3,7`, and immediately collects their displayed functional in the exact
abstract graph coordinates

```text
(J,K2,K6,K10,S0,S1,R0,R1,Y,X,a,lambda,M,E).
```

It then discards abstract monomials whose registered source valuation exceeds
48 and extracts only grade 48 by memoized sparse-series convolution.  It never
creates any complete substituted row and never computes a standard basis.
The output is a canonical sparse polynomial in all retained source jets.

The literal substitutions are the complete registered ones:

```text
a=s^4(a0+...+s^6 a6),       E=p+s e1+...+s^6 e6,
M=m+s m1+...+s^4 m4,        X=s^6(x0+...+s^4 x4),
Y=s^6(y0+...+s^4 y4),       Ri,Si=s^12(... through relative 4),
lambda=s^16,
K10=s^42 KK,
K6=s^42((15/32) KK E^2+D6),
K2=s^42((15/256) KK E^4+D2),
J=s^57 jt.
```

Thus `J` cannot reach grade 48.  No `mu2,mu4,mu6` target occurs in the three
raw rows used by this functional.  The client does not infer this functional
from the target-bearing `E H3+H5` expression.

## Mandatory controls

- frozen compiler and tail hashes plus exact tail counts `36,58,131`;
- direct scalar evaluation of the raw tail DAG versus the collected abstract
  polynomial at three deterministic points;
- direct numeric raw-tail series convolution versus the emitted sparse
  grade-48 polynomial at a deterministic complete-jet point;
- the two already certified rational witness slices both evaluate to
  `-1/32`;
- exact `Q` on Box03 and an independent `F65521` run on r6d, with identical
  monomial support and coefficient reduction checked after custody;
- fail closed on a support cap, frozen-input mismatch, failed control,
  timeout, diagnostic, or missing/nonunique endpoint.

## Scope firewall

This is fixed-representative producer evidence for one raw grade-48 row
functional.  It is not predecessor reduction, equality-wall exhaustiveness,
rational regrading, total-Rees/source coverage, an order-two or maximum-twelve
conclusion, or a JC2 verdict.

