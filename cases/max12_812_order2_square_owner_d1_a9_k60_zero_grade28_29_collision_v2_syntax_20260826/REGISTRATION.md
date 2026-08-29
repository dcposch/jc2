# Registration: D1 `a=9`, `V(k60)` collision V2 syntax repair

Date: 2026-08-26

Status: **PREREGISTERED IMMUTABLE V1 REPAIR; DUAL AWS REQUIRED.**

V1 is frozen as a fail-closed negative control.  Both independent engines
reached the same Singular precedence error before any branch endpoint.  V2
imports V1 byte-for-byte and changes only:

```text
p^2/32        -> (p^2)/32                 exactly 2 occurrences
p^3/128       -> (p^3)/128                exactly 2 occurrences
3*p^2*ell1/64 -> 3*(p^2)*ell1/64          exactly 1 occurrence
(p,k0,...     -> (z,p,k0,...              exactly 1 compact-ring header
```

The first three changes prevent rational-exponent parsing.  The fourth adds
the symbol used only by the isolated Chebyshev/Pell positive control.  No
source row, compact generator, witness, open condition, acceptance marker,
or firewall changes.

V2 must assert all pre/post cardinalities and rerun exact Q on Box03 and
`F_65521` on r6d under the original caps.  A PASS has exactly the narrow V1
scope: grade-28/29 classification only, with survivors routed to grade 30.

