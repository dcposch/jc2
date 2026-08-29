# Reducer-safe quotient rank r5

R5 changes only the backend fixture identifier `NF` to `REDUCED` relative to
r4; the mathematical compiler is byte-identical.  The `Q1P03` pilot passed
its literal-q2 negative/mutation control and full exact rank contract, after
which the other five frozen payloads ran independently.

Four branches produced complete exact quotient normal-form rank
certificates.  `P` and `C8P02` exposed a second, branch-local adapter gap:
their support rank is 10 but both structurally possible 10-minors reduce to
zero, so the adapter must descend to size 9 before it can issue a rank
certificate.  Those two branches remain quarantined `NO_VERDICT`; see
`RESULT.md`.

