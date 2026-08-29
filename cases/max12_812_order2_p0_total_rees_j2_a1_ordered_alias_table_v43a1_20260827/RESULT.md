# Additive ordered-`a1` alias-table pin V43A1

This case adds a machine-readable crosswalk without changing V37, V43, V46,
or any frozen producer.  Its load-bearing naming rule is:

`k2c = total.k10[2]`, while `k2 = total.k2[0]` and
`k2load = D1.k2[0]`.

The three symbols are pairwise distinct.  Through grade 19, `k2c` is present
in both the 65-symbol rho-zero and 66-symbol total ordered-`a1` alphabets;
neither `k2` nor `k2load` is present.  The total alphabet differs from the
rho-zero alphabet only by the general-only symbol `ez9`.  The coefficient
symbol `rho` has sigma weight zero, and the repackaging symbol `t=rho^2` is
not a positive-weight source symbol.

The desk verifier reconstructs both alphabets from the pinned V37/V43 bytes,
checks all source hashes, checks the sigma weights, and compares the three
collision-firewall entries to the normative actual-total V46 schema at SHA
`796eb0847e7b0bb7972c2fd7b3db10bd2dcfd2fd85c5bbaa47e3a239f8b02673`.

This artifact is a software/custody guard only.  It changes no mathematical
claim and does not retrospectively alter any frozen input.
