# Selected-Q8 fixed-fibre `msolve` discriminator

Date: 2026-08-25

This producer package gives a second, independent finite-field route to the
fixed-`w` quotient fibres used in the selected-Q8 component-grouping test.  It
generates the same six exact high-row equations and the same localization

```text
x5*(x3-2*x5) != 0,
v=(x3-2*x5)/x5,
```

as the pinned Singular fixed-fibre package, but hands the zero-dimensional
system to `msolve`.  The `elim` mode requests a two-block Gröbner basis
eliminating the first seven variables and retaining `v`; `param` requests
`msolve`'s finite-field rational parametrization.

This is a bounded modular discriminator only.  A fixed fibre does not by
itself prove generic or characteristic-zero irreducibility.  A useful positive
result must also be degree-preserving relative to the generic fibre, and every
lift to characteristic zero remains charged.  No selected component,
trajectory, `(9,12)`, maximum-twelve, or JC2 conclusion is asserted by this
package alone.

Remote invocation:

```sh
cases/max12_912_order3_nu_q8_fibre_msolve_aws_20260825/run_remote.sh \
  /home/ubuntu/jc2q8-generic/repo \
  /home/ubuntu/jc2q8-generic/out/fixed-msolve \
  q8_fixed_p89_w1_msolve_elim_v1 89 1 elim 8
```

Resource envelope per shard: 4 wall-clock hours, 64 GiB virtual memory, and
the explicitly supplied thread count.  Run only on an authorized remote host.

