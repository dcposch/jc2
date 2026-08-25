# Box02 V1 failure / V2 replay controls

Archive SHA-256:
`5472c2b476d3e8ba39ed576b4fefbb99e62ad56b5e21da69ad113e0e037d6a7f`.

The archive preserves two V1 fail-closed `NameError: P is not defined`
controls and the corresponding two V2 PASS controls at the known base-513
and base-519 Q6/high models with `q5_0,...,q5_13=0`.

V2 verifies every parent row, finds respectively

```text
base 513 Q5 rows = [1,0,0,1,1,1];
base 519 Q5 rows = [0,1,1,0,1,0];
```

and checks recursive/literal `/243` agreement in degrees 12 through 7.  The
nonzero Q5 rows make these exact omission controls; they are not Q5 survivors.
