# Exact source-identity negative control

The registered r6d AWS job
`max12_912_order3_d1_double_root_control2_rees_source_identity_20260826T012642Z_r6d`
completed its compiler and Singular commands with return code zero and empty
stderr.  It compared the frozen factored A source (SHA `2b416cb8...`) and
expanded B source (SHA `c905f1b5...`) as exact polynomials in both relevant
ring orders.

The first `dp` block passed `E1,...,E7` and then failed closed at `E8`,
printing

```text
-25134148616192/43046721
```

for `A_E8-B_E8`.  Because this is already a nonzero constant, the LPDP block
was intentionally not reached.  The output is an exact negative control, not
a failed computation and not a geometric endpoint.

```text
7baf7e60702fbe8589ad075f263d941c2ddf0b62ebe34721a9e662d4a0b39671  aws_r6d/singular.stdout
0f1314e960c62e4c4b6a7deb0a72325bb06ecbec26cbb8875b874aaf006d1505  aws_r6d/source_identity.sing
```

