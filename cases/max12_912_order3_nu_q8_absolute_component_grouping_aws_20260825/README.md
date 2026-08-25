# Selected-Q8 absolute component grouping (AWS-only producer input)

This package is the exact characteristic-zero successor to the modular
component-sizing lane.  It saturates the six-row quotient by
`w*x5*(x3-2*x5)`, calls Singular `absPrimdecGTZ`, and intersects every
absolute component class with the genuine Q8 boundary conditions

```text
w=0,   v*x5=x3-2*x5,   Q8(v)=0.
```

It must run only on AWS under the supplied 24-hour / 256-GiB guard.  The
current estimate is one core, uncertain wall time up to 24 hours, and a hard
RSS ceiling of 256 GiB.  Run the already-active modular saturation sizing
phase first.

If the unique Q-rational component containing the irreducible Q8 closed point
splits into `d_abs` conjugate absolute components, smooth uniqueness at all
eight Q8 contacts and Galois transitivity give exactly `8/d_abs` contacts per
absolute component.  A result `d_abs in {1,2,4}` would therefore combine with
the frozen infinity-contact theorem to exclude that selected component;
`d_abs=8` leaves one contact per component.  Any nondivisor of eight,
nonzero-dimensional boundary hit, ambiguous multiple hit class, timeout, or
engine error is fail-closed.

Modular minimal-prime grouping cannot prove this statement because distinct
characteristic-zero components may merge after reduction.  Only the exact
characteristic-zero absolute decomposition is eligible for promotion, and it
still requires a hostile review and an audit of the returned extension-field
component encoding.

Example remote launch after syncing the exact tree:

```sh
nohup cases/max12_912_order3_nu_q8_absolute_component_grouping_aws_20260825/run_remote.sh \
  "$PWD" "$HOME/q8-absolute-out" q8_abs_group_char0_v1 slimgb \
  > "$HOME/q8-absolute-out-launch.log" 2>&1 &
```

This package claims no computed result.
