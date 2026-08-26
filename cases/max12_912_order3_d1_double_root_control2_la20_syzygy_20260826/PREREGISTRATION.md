# Preregistration: explicit `la^20` Rees preimage

## Objective

Extract a proof-carrying polynomial identity behind the fixed-weight
`la^20` initial-ideal obstruction.  The source is the pinned reviewed
expanded control-2 B polynomial system; this first extractor uses direct
principal saturation in the independent `(lp(1),dp(8))` order.

The computation must return the exact principal saturation exponent `N`, a
lift of `la^20` through `H=(I:<s>^infinity)+<s>`, the subset of saturation
generators actually used, lifts of `s^N` times those generators back into the
nine submitted Rees generators, and the composed identity

```text
s^N*la^20
  = sum_i FINAL_i*I_i + s^(N+1)*TAIL.
```

Equivalently

```text
G = la^20-s*TAIL
```

lies in the contracted Rees ideal and has special fibre `la^20`.  Setting
`s=1` gives an explicit polynomial consequence of the unscaled finite ideal.
The follow-up cone compiler must still audit every term weight of that
dehomogenized polynomial before claiming any open Gröbner cone.

## Fail-closed checks

1. Pin the expanded B source at SHA-256
   `c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b`
   and extract exactly `E1,...,E8,LT`.
2. In the exact target ring, a tiny principal-saturation/lift control must
   verify the fleet APIs and matrix orientation.
3. `sat_with_exp(I,<s>)` and direct `sat(I,<s>)` must agree by mutual
   reduction.
4. Every `lift` must be checked by multiplying the returned matrix back into
   the original ideals.
5. The final composed identity must be literally zero before any coefficient
   is printed as a certificate.
6. Compiler and Singular return code zero, empty stderr, and all unique PASS
   markers are required.

## Scope firewall

This is a certificate for the same fixed
`a=1,h=q2=k=nu=0,mu=2/3`, support and weight
`(4,1,1,22,22,30,30,30)` only.  It does not yet certify the inequalities of
an adjacent Gröbner cone, moving parameters, another support/weight, the
whole fan, D1, or JC2.

All compilation and Singular execution are AWS-only.  The remote host, job
directory, worker PID, resource caps, and complete source closure must be
recorded before any GO sentinel is sent.

