# D1 weighted coefficient-infinity gate

This case consumes the exact V2 eight-row source and attacks only the strict
weighted pole sector left open by the classical degree split.

`compile_exceptional.py` is an AWS-guarded source compiler.  It checks every
row weight, emits a canonical payload, and emits a characteristic-zero or
finite-field Singular job for the unsaturated exceptional divisor.  The
Singular job saturates the irrelevant origin and compares its radical support
with the full depressed-cubic power graph, retaining every axis and
discriminant stratum.  It can emit either the global saturation or one of the
eight exact `B_i!=0` charts.

`run_exceptional_aws.sh` refuses non-EC2 hosts, unregistered tags, and
pre-existing result directories.  Run only from a closure-complete staged
repository:

```sh
export JC2_AWS_TAG=max12_912_order3_d1_infty_exceptional_<UTC>_<HOST>
export D1_INFINITY_RUN_DIR=/home/ubuntu/jobs/$JC2_AWS_TAG
export D1_INFINITY_CHARACTERISTIC=0
export D1_INFINITY_CHART=global   # or 0,...,7 under a fresh tag
bash cases/max12_912_order3_d1_weighted_infinity_20260825/run_exceptional_aws.sh
```

Characteristic `32003` is an optional navigation mirror.  It cannot replace
the characteristic-zero minimal-prime/containment certificate.  No normal
deformation theorem is implemented in this first slice.  In particular,
the rational slope `m/n>3` has unbounded numerator `m`, so the package makes
no false uniform weight-20 jet claim.
