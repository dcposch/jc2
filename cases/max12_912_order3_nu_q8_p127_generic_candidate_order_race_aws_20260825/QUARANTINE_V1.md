# Quarantine — r6a order-race V1

The remote r6a tree

```
/home/ubuntu/jc2doubleb/out/q8_candidate_order_race_r6a_v1
```

is a harness failure and supplies no algebraic evidence.  All fifteen
`input.sing` files are empty.  Every generator stopped with `FileNotFoundError`
because the partial remote source closure omitted
`cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py`.
No Singular lane started.  The V1 dispatcher then falsely wrote `rc=0`
because POSIX `wait` with no PID does not aggregate every background exit
status.

V1 must remain a negative control only.  V2 requires a complete pinned source
closure, a nonempty generator preflight before fanout, and explicit per-PID
status aggregation.
