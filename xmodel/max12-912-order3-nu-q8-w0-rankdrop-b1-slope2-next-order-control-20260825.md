# Selected Q8 rank-drop b=1: slope-two next-order control

Date: 2026-08-25  
Status: producer-exact finite-jet routing; no arc-closure theorem.

Two exact AWS implementations (`std/dp` on Box02 and `slimgb/block` on
Box03) agree that, after normalizing `x5=t` and retaining first jets of the
coefficient `c`, `d4`, and `u=d2-d4-1`, the next coefficient ideal of the
surviving selected slope-two cone is the unit ideal.  Its elimination to
`Q[c]` is also the unit ideal.  The six next coefficients are byte-identical
between endpoints, both return rc zero without diagnostics, and the frozen
source/custody replay regenerates each input exactly.

Exact substitution and full outputs are frozen in
`cases/max12_912_order3_nu_q8_w0_rankdrop_b1_slope2_next_order_aws_20260825/`.
The two initial `v1` permission failures are preserved as nonmathematical
negative controls; only the `v2` endpoints are accepted.

The conclusion is strictly this: the normalized unramified
`ord(x5)=1, ord(w)=2` finite jet has no next-order continuation, for any
finite `c`, within the displayed ansatz.  The hostile ramified audit remains
`NOT_CONFIRMED`: mixed-order/ramified arcs and nonconstant coefficient drift
at orders earlier than `ord(x5)` are not covered.  Full selected saturation,
coefficient infinity, Taylor/terminal reconstruction, trajectories, the full
`(9,12)` cell, maximum twelve, and JC2 remain open.
