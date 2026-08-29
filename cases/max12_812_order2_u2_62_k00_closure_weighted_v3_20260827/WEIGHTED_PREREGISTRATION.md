# K00 closure V3: exact Faber/Lambda weight order

Date: 2026-08-27

Status: **PREREGISTERED ORDERING CONTROL; NO ENDPOINT.**

V3 computes the exact V2 g-open ideal with a different global monomial
order only:

```text
variables=(Lambda,C0,C1,C2,C3,C4,C5,C6,k10,k6,k2,mu2,mu4,mu6,Jdet)
order=wp(1,8,7,6,5,4,3,2,0,0,0,0,0,0,0).
```

These are the exact one-parameter Faber weights.  Every frozen tail term in
row `ell` has weight `12+ell`: a lower load of original weight `2,6,10`
is represented by `Lambda^(2,6,10)` times a weight-zero retained variable,
and the four targets have weights `14,16,18,19`.  Thus the source remains
weighted homogeneous.  Zero-weight retained loads are still polynomial
variables and are not projected or moved into a coefficient field.

Monomial order changes Gröbner performance and basis bytes, not any ideal,
saturation, unit endpoint, or scope.  The compiler is a hash-gated wrapper
around V2, changes the unique ring declaration, emits a unique order marker,
and otherwise preserves V2 byte-for-byte.

First screen: characteristic 65521 on AWS Box01, 20-minute / 64-GiB cap.
It is a finite-field algorithm screen, not the Q endpoint.  If decisive and
fast, launch the same frozen order over exact Q on another host.  Timeout,
OOM, source mismatch, diagnostic, missing marker, or validation failure is
no verdict.
