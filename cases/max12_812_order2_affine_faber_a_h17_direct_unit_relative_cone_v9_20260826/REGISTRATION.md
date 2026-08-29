# Registration: H17 direct-unit relative cone V9

Date: 2026-08-26

Status: preregistered exact-support successor; no total-source claim.

V9 repairs only the displayed affine-weight labels in the V7 `result.json`.
V7 selected the correct monomials and exact interval, but its reporting loop
reused the final temporary `(const,slope)` pair for every displayed label.
V9 recomputes and fail-closed validates `34+4q` on the lower block and
`93-6q` on the upper block.  V7 is diagnostic only.  V8 correctly repaired
the reporting loop but preregistered the wrong expected upper label and
therefore failed closed before emitting a result.

Subtract the complete abstract supports for the two H16 row functionals to
form

```text
Hseries=G-32F
       =2 E^2 P3+16 E P5+64 P7-(E^3/2)P1.
```

The fixed H16 computation indicates that its unique leading abstract monomial
is `-2 lambda^3 M^3 E^2`.  This client checks the complete exact-Q support and
its `F65521` reduction, then substitutes the H17 equality-wall valuation

```text
ord(lambda)=17, ord(X)=ord(Y)=q,
ord(Ri)=ord(Si)=2q, ord(a)=17-2q,
ord(K10)=ord(K6)=ord(K2)=42, ord(J)=57.
```

It computes all strict inequalities against grade `51=3H` from every support
monomial, without sampling, and reports the exact maximal interval on which
the intrinsic monomial is uniquely least.  Expected navigation answer:
`17/4<q<7`, inside the mixed equality domain `4<q<17/2`.

Stop on any hash/support/coefficient-reduction mismatch, nonunique intrinsic
term, unexpected q-independent competitor, or different interval.  This is
an internal normalized graph-support result only, not rational-regrading or
literal total-Rees/source coverage.
