# Preregistration: `T-rs` actual-chart base-change discovery V10

Date: 2026-08-26

Status: **PREFIXED SATURATION DISCOVERY ONLY.  NO REES-CHART, MOVING-`p`,
ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## Charged source

Use only the exact grade-10--12 coefficient exports from frozen V9. Pin the
two independently generated input manifests byte-for-byte:

```text
Q       COEFFICIENTS.json  86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e
F65521  COEFFICIENTS.json  dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4
```

The compiler must rehash every `.poly` file against its pinned manifest. In
characteristic 65521 it must additionally compare the reduction of every
exact-Q expression with the independently compiled finite-field expression.

## Exact chart representation

On `D_+(rs)`, quotienting by the three monic bilinear relations identifies

```text
cs=rs*qcs,  c0=rs*qc0,  c1=rs*qc1.
```

Consequently the actual chart ideal is represented, without retaining the
three eliminable source names, by

```text
Jtot_g = (E_tot,<=g | chart substitution) : rs^infinity.
```

This is isomorphic to eliminating `cs,c0,c1` from the full bilinear
presentation and then saturating. It is not the unsaturated symmetric
presentation. In the same named ratio coordinates compare

```text
Kafter_g  = Jtot_g + (rho),
Kbefore_g = ((E_0,<=g | chart substitution):rs^infinity) + (rho).
```

The comparison is literal two-way ideal membership, never radical equality.
Run independent prefixes `g=10,11,12` so the earliest discrepancy is visible.

## Two algorithms

The discovery has two independent saturation encodings:

1. `sat`: `elim.lib` saturation by the principal ideal `(rs)`;
2. `elim`: eliminate an inverse variable from `(E,1-u*rs)` in a block order.

Each script strips only generatorwise common powers of `rs` before the costly
step; this does not change the saturation and the raw unstripped ideal is
retained for the symmetric-presentation diagnostic. Both algorithms must
pass synthetic vertical and factor saturation controls. Quotient rings are
forbidden.

## Required diagnostics

- all total rows specialize coefficientwise to their frozen rows;
- all total rows are invariant under `rho -> -rho`;
- exact-Q reduction equals the independent F65521 compilation in the prime
  lane;
- two-way membership for `Kafter_g` and `Kbefore_g`;
- two-way comparison with the unsaturated presentation, with difference
  witnesses written whether equality holds or fails;
- basis and witness artifacts hash-bound by the validator;
- only ordinary polynomial rings; no `qring` comparisons.

Equality is not preregistered as the expected outcome. Either equality or a
nonzero membership remainder is a valid discovery result. A timeout,
Singular diagnostic, missing artifact, source mismatch, or control failure is
no verdict.

## Firewall

Even exact equality through grade 12 establishes only prefix base-change for
the first `D_+(rs)` chart. It does not yet prove the two-sided frozen cusp
map, the localized total unit identity, any later chart, terminal receiver,
whole order two, maximum twelve, or JC2.
