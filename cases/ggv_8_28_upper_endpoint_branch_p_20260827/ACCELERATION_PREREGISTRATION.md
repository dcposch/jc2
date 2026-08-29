# Preregistration: literal row-RREF acceleration

Date: 2026-08-27

The authoritative object remains the frozen 303-variable, 513-generator
literal raw coefficient ideal with SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.
This successor performs only invertible constant-`Q` row operations within
each coefficient row `D4,...,D21`; it does not substitute a pivot, remove a
raw variable, impose `D23`, add `G22`, specialize a parameter, or use the
endpoint-transfer identity as an equation.

For each weight, the compiler must serialize the exact sparse matrix taking
the original coefficient generators to the row-RREF generators.  Every
retained accelerated generator must replay as that displayed `Q`-linear
combination of literal raw generators.  The pivot variables are reordered
ahead of all free variables and a block order `(lp(pivots),dp(free))` is used
only to expose the already-recorded triangularity.

An accelerated positive result is not promotable until a complete rational
assignment replays in `verify_endpoint.py`.  An accelerated negative result
is not promotable until tracked exact-`Q` cofactors are composed with the
serialized row-operation matrices to give `1` as an explicit combination of
the authoritative raw generators.  Finite-field output remains guidance
only.  Resource custody is unchanged: audited Box03, fresh immutable source
and output namespaces, one global six-hour wall cap, zero swap, and one core.
The exact `std` lane is capped at 128 GiB VM; the independent exact `slimgb`
lane is capped at 100 GiB VM.  No canonical edits are allowed.

Before launch, also preregister an independent exact-`Q` engine lane on this
identical serialized row-RREF ideal and identical `(lp(202),dp(101))` block
order, replacing only Singular `std` by `slimgb`.  Its output has exactly the
same promotion firewall: a proper ideal must yield a complete raw rational
witness, while a unit result only licenses a fresh tracked raw-certificate
run.  It may not change the generators, specialize a free coordinate, or
inherit evidence from a finite-field lane.
