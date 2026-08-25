# AS F-only D7 complete `Z/9` output-cone survivor at three Q3 fibres

Date: 2026-08-25  
Status: **PRODUCER-EXACT / DIFFERENT-MODEL REVIEW PENDING**  
Case: `cases/as_fonly_d7_q3_full_output_cone_z9_20260825/`

## Result

The complete fixed-D7 output coefficient cone at orders 27 and 81 is
nonempty modulo 243 over each of the three pinned, reviewed Q3 affine fibres
`0000`, `0270`, and `0513`.

For a fixed literal Q3 particular `F_*`, write

```text
F=F_*+27U+81V.
```

There are 36 D7 monomials in each output and therefore 72 combined
coefficients `T=U+3V in Z/9`.  The compiler imposes all 91 coefficients of
`det J(F)-1` in total degrees 0 through 12 modulo 243.  At every parent the
mod-3 system has rank 27 and kernel dimension 45.  Its exact Bockstein lift is
consistent: rank/kernel are `36/81`, `43/74`, and `43/74`.  Literal integer
reconstruction then verifies every determinant coefficient modulo 243.

This result supersedes any attempted inference from the earlier displayed
degree-at-most-three row-8 obstruction to emptiness of these full output
cones.  The full matrix has live degree-four row-8 columns.

## Why the `Z/9` reduction is exact here

The determinant is quadratic in the two output corrections.  Fresh-fresh
quadratic terms carry `27^2=729`, hence vanish modulo 243; equivalently they
vanish after `/27 mod 9`.  The producer checks all 1296 left/right monomial
pairs and every doubled basis.  The complete reviewed Q3 kernel is also
absorbed: each direction changes the literal map by `81*K` inside D7, and
every mixed second difference with all 72 fresh bases is divisible by
`81*27=2187` coefficientwise.  Counts of these controls are `1008`, `720`,
and `720`.

This is a fibrewise statement.  It does not license a single constant matrix
over the global predecessor scheme, where earlier order-9 coordinates can
produce the surviving mixed quotient `(9K)(27U)/243=K U`.

## Exact outputs

- `0000`: result SHA
  `3e6a559c5b4906b489b9c43350b95259a191c1fbe529656f32b52fdc40bd4f0a`,
  `3^81` solutions.
- `0270`: result SHA
  `eb6936b975de974f26e0f571a3e1839ee118d6ed96ea12bf769ecd2f6015d97e`,
  `3^74` solutions.
- `0513`: result SHA
  `c8716a9828b42f3b97f89a41e646b5fa8b8744fe5945ebfe1b24a42141b9fd1e`,
  `3^74` solutions.
- Source archive SHA
  `c3cb56df1c9ad751bd363a79300185245681ad5524ad5f347bf412e5499c702e`.
- AWS job: r6d
  `/home/ubuntu/jobs/as_q3_full_output_cone_z9_20260825T145301Z`.

## Refusal scope

No terminal-mod-729 closure or order-243 coefficient digit is imposed.  The
other current Q5 predecessors/global scheme are not covered.  There is no
all-depth compatible tower, `Z_3` solution, collision, characteristic-zero
counterexample, no-lift theorem, or JC2 conclusion.

## Smallest successors

1. Hostile-audit the transitive source, determinant orientation, exact
   Bockstein construction, all 91 rows, mixed second-difference controls, and
   literal replay.
2. Over the whole predecessor algebra, retain an order-9 base direction and
   compute the mixed `K*U` section by Fitting strata rather than a constant
   RREF.
3. At these three survivors, add the next terminal modulus/order-243 digit
   layer and test full coefficient-scheme Jacobian/Hensel data.

