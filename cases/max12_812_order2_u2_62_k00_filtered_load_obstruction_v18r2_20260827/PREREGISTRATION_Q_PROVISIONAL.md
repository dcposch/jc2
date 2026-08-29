# Preregistration: provisional exact-Q V18R2 host lane

Date: 2026-08-27

Status: **FROZEN BEFORE EXACT INPUT EXTRACTION OR RANKS.**

V17 exact-Q is live but its monolithic producer serializes the six-row
deformation images and targets only after each expensive local-colon test.
This additive input-gate repair extracts those exact objects before the colon
from the already frozen V17 exact compiled source (required SHA-256
`9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c`).
It must recompute and replay the full six-row syzygy module over `Q`, require
exactly 66 generators, and serialize `IMAGE_X` and `TARGET_X` for
`X=K10,K6,K2`.  It must not claim a completed V17-Q local-colon endpoint.

The provisional branch dependency is the immutable V17 `p=65521` endpoint,
SHA-256
`6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc`.
Therefore every exact result below remains nonpromotable until the live V17-Q
producer independently returns the same three `LOCAL_NONZERO` branches and
the exact input artifacts agree byte-for-byte.

The filtered maps are otherwise exactly V18R1: the six unloaded rows plus all
66 six-row-syzygy deformation images and all monomial multipliers in
`Q[d0,...,d5]/m^(D+1)`.  The modular first-break pattern is frozen as an exact
target and control:

```text
K10: compatible D2,D3; incompatible D4
K6:  compatible D2;    incompatible D3
K2:  incompatible D2
```

The exact runner must replay rational lifts at every compatible cutoff and a
rational left functional at every first incompatible cutoff.  Any earlier
cutoff discrepancy, missing exact dual, input/hash mismatch, timeout, or
resource-cap event fails closed.  Agreement proves only a provisional exact
calculation of three separate normalized-K00 first-load filtered classes.

Firewall: no promotion before V17-Q; no coupled loads; no honest `Lambda`
weights; no `mu/Jdet` target equations through order 19; no honest-source
reachability; no arc exclusion; no closure-incidence or JC2 conclusion.
