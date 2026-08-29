# Registration: c2 localized rootwise-delta diagnostic

Date: 2026-08-26

Frozen namespaced V3 proved the complete c1 rootwise identity, but its c2
ideal-membership sentinel was nonzero over both Q and `F_65521`.  V3 did not
localize its root ideal even though the argument uses `D(p*k0)`.  This thin
exact-Q diagnostic pins V3, saturates the c2 root ideal by `p*k0`, verifies
the localized ideal remains proper, and prints both the raw and localized
remainders.  It changes no source/Faber or moving-divisor row.

The result is diagnostic unless localized membership passes.  Even a pass is
only the generic-square c2 contact gate on `D(p*k0)`, not square/order-two
closure.

