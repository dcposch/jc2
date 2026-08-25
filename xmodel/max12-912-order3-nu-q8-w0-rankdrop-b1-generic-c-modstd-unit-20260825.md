# Selected Q8 w=0 rank-drop b=1: exact-Q modStd unit successor

Date: 2026-08-25  
Status: producer-exact, review pending; narrow algorithmic successor only.

## Result

In the exact source ring used by the reviewed direct unit package, impose
exactly `(e1,e3,e5,e7,e2,e4)`, substitute `d4=1,d2=2+u`, work over
`Q(c)`, and adjoin

```text
inv*w*x5*(x3-2*x5)-1.
```

On AWS r6d, Singular 4.3.2 `modStd` reconstructed the exact characteristic-zero
bases

```text
GJ=(1),  GC=(1),  GL=(1),
```

with rc zero, zero generator diagnostics, zero reductions of the original,
contraction, and landing generators against their printed bases, and a passing
`Q(c)` control.  The source-regeneration/custody replay passed independently
on r6d.

This independently supports the direct `std`/`slimgb` conclusion that the
selected open of the **frozen `d4=1` slice** is empty over `Q(c)`.  It is a
rational multimodular-reconstruction algorithm, not the unsafe msolve short
circuit previously quarantined elsewhere.

## Resource and custody facts

The endpoint used wall 10:40.20, user 12413.55 seconds, average 1939% CPU, and
reported maximum RSS 37224 KiB with no swap.  Live monitoring saw roughly 36
modular workers at peak; `/usr/bin/time`'s RSS line is not asserted to be the
aggregate of every worker.  Full input, output, stderr, timing, version,
source pins, and replay are frozen in
`cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_modstd_aws_20260825/`.

## Exact limitation of the lift marker

`lift_residual_zero=1` is a lift in
`Landing=GC+(w,u,x1,x3,x5)` after `GC=(1)`.  It is not a source-generator
cofactor identity

```text
1 = sum h_i*phi(e_i) + h_7*(inv*w*x5*(x3-2*x5)-1).
```

The direct-source cofactor and its denominator polynomial `D(c)` remain the
smallest missing certificate/exceptional-locus producer.

## Firewall

The coefficient field `Q(c)` erases a finite exceptional-`c` set, and the map
freezes `d4` identically.  Nothing here covers nonconstant `d4` drift through
`(d2,d4)=(2,1)`, the whole doubled rank-drop support, arbitrary ramification,
full Hsrc, coefficient infinity, Taylor/terminal realization, trajectories,
the whole `(9,12)` cell, maximum twelve, or JC2.

The hostile ramified audit remains `NOT_CONFIRMED`; cite its immutable raw
report together with both the provenance and mathematical-scope errata.
