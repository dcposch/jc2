# Exact-Q modStd result: frozen d4=1, generic c

The r6d endpoint `q8_w0_rankdrop_b1_loaded_modstd_QQc_r6d_v1`
completed rc zero under Singular 4.3.2.  Singular's rational multimodular
`modStd` returned

```text
GJ[1]=1
GC[1]=1
GL[1]=1
```

and all printed original/contraction/landing reductions were zero.  The tiny
`Q(c)` control passed.  Wall time was 10:40.20, user time 12413.55 seconds,
average CPU 1939%, `/usr/bin/time` maximum resident set 37224 KiB, and no
swap.  Live monitoring observed the driver plus approximately 36 modular
worker processes at peak; the reported RSS is the timed process statistic and
must not be read as an aggregate-worker high-water mark.  Host free memory
remained hundreds of GiB.

This is a distinct exact characteristic-zero reconstruction algorithm
supporting the already-frozen direct `std`/`slimgb` unit bases.  It proves no
more than emptiness of the selected open

```text
D(w*x5*(x3-2*x5))
```

inside the frozen slice `d4=1,d2=2+u`, over `Q(c)`, at the usual Singular
standard-basis trust tier.

The printed `lift_residual_zero=1` is computed for
`Landing=GC+(w,u,x1,x3,x5)` after `GC=(1)`.  It is **not** a cofactor identity
for `1` in the original six rows plus localizer `J`.  Exceptional finite
values of `c`, nonconstant `d4` drift, the full rank-drop support, full Hsrc,
coefficient infinity, Taylor/terminal realization, trajectories, `(9,12)`,
maximum twelve, and JC2 remain open.

The Box03 mirror was stopped before computation after capacity coordination;
it is not evidence and is not part of this freeze.
