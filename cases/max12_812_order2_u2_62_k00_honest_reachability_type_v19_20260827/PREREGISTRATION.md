# Preregistration: V19 honest `Lambda<=19` reachability type intersection

Date: 2026-08-27

Status: **FROZEN BEFORE AWS REPLAY.**

Consume the three serialized V18R1 `p=65521` separating duals at their first
filtered breaks (`K10:D4`, `K6:D3`, `K2:D2`) and the reviewed one-parameter
source type

```text
Phi_l=r_l(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
      -Lambda^(12+l)*delta_l,
delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

Before forming any scalar pairing, decide whether each dual is actually
typed as a covector on a serialized honest-source reachable jet map through
`Lambda^19`.  The allowed endpoints per direction are:

```text
NONZERO_ON_REACHABLE_IMAGE
ZERO_ON_REACHABLE_IMAGE
NOT_TYPED_COMPOSABLE
```

`NONZERO` or `ZERO` requires an explicit, hash-gated common mixed six-row
jet map with columns labelled by coefficient, simultaneous-load, target,
and `Jdet` source jets and a replayed matrix composition.  The separate
direction-specific V18 quotient maps may not be silently identified or
added.  If the consumed packet contains only covectors on
`F_65521[d0,...,d5]_{<=D}`, the mandatory endpoint is
`NOT_TYPED_COMPOSABLE`, together with the exact missing interface.

This audit is modular and diagnostic.  It cannot promote a filtered class,
exclude an arc, or decide closure incidence or JC2.  Its successor, if the
map is absent, is a frozen common mixed six-row `Lambda<=19` Kuranishi map;
valuation slogans or raw dual target pairings are not substitutes.
