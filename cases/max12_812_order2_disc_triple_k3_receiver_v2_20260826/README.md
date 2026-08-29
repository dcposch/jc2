# K3 receiver V2: Singular rational-literal repair

Date: 2026-08-26

Status: **IMMUTABLE AWS-ONLY V2; NO RESULT.**

V1 source package SHA-256 is
`9f1740a447183453b661cbe07b854b796d6fab6b274ab288de56ac9ecb088a6f`.
Both V1 retry lanes failed closed before any mathematical calculation because
Singular parsed `-3*b^2/16` as a polynomial raised to a noninteger number;
every later diagnostic was a cascade from the undefined `dd` polynomial.

V2 changes exactly that emitted line to

```text
poly dd=(-3/16)*b^2+rho*jd;
```

and adds a unique V2 endpoint sentinel.  All mathematical substitutions,
source hashes, rows, typing checks, elimination, caps, and firewalls are
unchanged.
