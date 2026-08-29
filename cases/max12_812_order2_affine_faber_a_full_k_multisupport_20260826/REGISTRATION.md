# Registration: full affine-Faber `K` multigraded support

Date: 2026-08-26

Status: preregistered navigation client; no theorem or fan-coverage claim.

## Purpose

Reconstruct all seven frozen complete ordinary-Faber rows in the exact
moving-discriminant coordinates, retain every load and all four targets, and
emit the complete monomial support of

```text
K=E*H3+H5
```

before imposing a one-parameter valuation.  The result is input for a
coefficient-stratified relative Newton fan.  It is not itself a Newton-cone,
predecessor-ideal, Rees, source-overlap, order-two, maximum-twelve, or JC2
theorem.

## Required controls

- exact depressed `Q,N` substitution with independent center, kernel, and
  complement variables;
- all seven complete tails and targets `mu2,mu4,mu6,J/4`;
- exact identities `dK/dmu6=dK/dJ=0`, `dK/dmu4=4a`, and the displayed
  `mu2` coefficient;
- central intrinsic slice `K=-E*lambda^3*M^3/16`;
- one support term per leading-monomial extraction, with exponent vector;
- exact Q as evidence and F65521 only as a support/software control.

Stop on a frozen-input mismatch, missing or duplicate endpoint, target
control failure, zero support, engine diagnostic, timeout, or memory cap.

## AWS lanes

```text
Box03: exact Q
r6d:   F65521 software control
```

No heavy local computation is permitted.
