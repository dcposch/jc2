# Slope-uniform strict-boundary gate

Only the hardened AWS wrapper is licensed.  Direct Python, Singular, or
local execution is not evidence.

After staging the exact source closure on a registered Amazon EC2 host:

```sh
export JC2_AWS_TAG=max12_912_order3_d1_slope_uniform_<UTC>_<HOST>_global
export D1_SLOPE_RUN_DIR=/home/ubuntu/jobs/$JC2_AWS_TAG
export D1_SLOPE_COORDINATES=normal
export D1_SLOPE_CHART=global
export D1_SLOPE_CONTROL_ONLY=0
export D1_SLOPE_TIMEOUT_SECONDS=14400
export D1_SLOPE_VM_KIB=268435456
bash cases/max12_912_order3_d1_weighted_infinity_20260825/run_slope_uniform_aws.sh
```

The default `normal` coordinates are an exact polynomial automorphism over
`Q`, not a generic-point specialization.  `B` coordinates are reserved for
an independently requested source-equivalence mirror.  If and only if the
global endpoint is nonunit or resource-inconclusive, the registered `p` and
`c` charts mean `B7!=0` and `B6!=0`; together they cover the independently
reviewed common-cubic projective radical.  Do not launch other charts or
modular approximations before the global characteristic-zero endpoint is
harvested and adjudicated.

Before source freeze, the same wrapper may be run once with
`D1_SLOPE_CONTROL_ONLY=1`: it reconstructs and parses all eight source
polynomials, but substitutes the registered synthetic strict arc for the
expensive source ideal so that every saturation/control branch terminates.
It is placement/syntax/control evidence only.  The theorem-sized run must
use `D1_SLOPE_CONTROL_ONLY=0`.
