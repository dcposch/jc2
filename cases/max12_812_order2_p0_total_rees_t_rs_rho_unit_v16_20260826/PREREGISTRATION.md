# T-rs rho-unit certificate V16

Date: 2026-08-26

## Purpose

V16 is the one-line semantic successor to frozen V14, executed with the
corrected V15 remote custody path.  V15 reached Singular in both registered
lanes and passed the coefficient, chart-division, four-term identity,
certificate, saturation/elimination membership, special-fiber, and explicit
rho-inverse checks.  It then failed closed before its final unit-ideal check:

```text
std(J,rho,1-v*k)
```

is parsed by Singular 4.3.2 as the three-argument `std(ideal,intvec,intvec)`
signature.  V16 replaces exactly that single occurrence by the sequential
ideal extension

```text
std(std(J,rho),1-v*k)
```

which is the intended standard basis of `J+(rho,1-v*k)`.  No coefficient,
generator, term order, certificate, negative control, or scope changes.

## Registered lanes

- characteristic zero, direct saturation encoding, Box02;
- characteristic 65521, elimination-variable encoding, r6d.

Both must pass independently, produce all four nonempty artifacts, contain no
Singular diagnostic token, and validate under the frozen source hashes.  Any
failure is no verdict.

## Scope firewall

A PASS establishes only: on the actual total-Rees T-rs chart, after
restriction to D(k), the complete grade-12 prefix forces rho to be a unit.
It does not establish the other standard charts or global Gate T.

