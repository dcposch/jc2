# Q8 component-grouping AWS discriminator

This unexecuted producer input computes the closure of the genuine punctured
six-row quotient by

```text
Is=(I:(w*x5*(x3-2*x5))^infinity).
```

Unlike localization by an inverse, saturation removes components contained
in the boundary while retaining closure points at `w=0`.  The grouping mode
computes minimal associated primes, intersects each with `w=0`, introduces

```text
v*x5=x3-2*x5,
```

and reports the gcd of its boundary eliminant with `Q8(v)`.

Run the cheaper sizing phase first:

```sh
python3 cases/max12_912_order3_nu_q8_component_grouping_aws_20260824/generate.py \
  --prime 10007 --mode saturation --engine slimgb \
  | Singular -q
```

Then run grouping under an external wall/RSS guard:

```sh
python3 cases/max12_912_order3_nu_q8_component_grouping_aws_20260824/generate.py \
  --prime 10007 --mode grouping --engine slimgb \
  | Singular -q
```

Use independent primes, preferably including one where `Q8` has at least two
rational roots.  A component with `Q8_gcd_degree>=2` is the desired grouping
certificate.  This artifact claims no result until an exact output is frozen
and reviewed.
