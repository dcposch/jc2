# Hostile review task — B9 fixed-D12 leading shear/order-one/Q8 interface V2

Review read-only report

```text
xmodel/as-b9-max12-leading-shear-q8-interface-audit-v2-20260825.md
SHA-256 82c701474a9d1605097910f7947deb99d70908934fa93d26a73103b4b2440e40
```

The superseded V1 note at SHA
`9f7eb4bfd61aa5ecd61a9f53939327c2ec268956e45eac2885d78b82832ce56a`
is a negative scope control only.  Do not repair or consume its fixed-D12
order-one/order-three ambiguity claim.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`, with the
smallest counterexample or missing hypothesis for every failure.  Review the
following claims adversarially and independently from the prose conclusion.

1. **Conditional scope.**  The input is an exact fixed-total-D12 Keller pair
   over a finite extension of `Q_3`, reducing to B9.  Finite congruence
   families do not satisfy this hypothesis.
2. **Equal-degree proportionality.**  Check directly that
   `J(P12,Q12)=0` for two nonzero homogeneous binary degree-12 forms forces
   `P12=cQ12`; attack zero faces, characteristic assumptions, and the
   dehomogenization argument.
3. **Unique integral scalar and target shear.**  The `y^12` coefficient of
   `Q12` is a unit, all coefficients of `P12` are divisible by three, hence
   `c in 3O`; `(P-cQ,Q)` is integral, determinant preserving, identity
   modulo three, and removes the whole degree-12 face.
4. **Exact displayed-witness failure.**  Against the frozen mod-`3^11`
   witness, verify that the unit-coefficient ratio is
   `c=27702 mod177147` and that the `x^3 y^9` residual is
   `59049 mod177147`, nonzero.  Confirm that this kills only that point as an
   exact-lift representative, not the complete `3^183` family.
5. **Broad-cell-only landing.**  Check the precise imported degree-routing
   hypothesis used to retain partial `y`-degree nine after shear and remove
   the ten/eleven alternatives.  Reject any silent inference to the stricter
   total-degree-`(9,12)` box.
6. **Fixed-D12 Kummer collapse.**  Starting from the reviewed identities
   `a9=h^3,b12=h^4`, check that total degree at most 12 makes `b12(x)` a
   nonzero constant, hence `h` constant, and after the licensed finite scalar
   extension the Kummer class has order one.  Check the B8 analogue
   `a8=h^2,b12=h^3`.  Attack the distinction between this partial-`y`
   coefficient `h` and the still-variable total-homogeneous common cubic or
   quartic `K`.
7. **Selected-Q8 scope conflict.**  Check that the selected corrected-Q8
   source is genuinely order three and `p=1`, excludes the order-one core,
   and uses divided odd rows.  Verify that neither the `p=q=0` degeneration
   nor denominator clearing licenses specialization into that source.
8. **Successor honesty.**  The only claimed bridge is complete-family
   leading-face incidence followed by an integral shear and an original-row
   order-one common-core compiler.  No divided generic substitution, Taylor,
   terminal, all-depth, counterexample, maximum-12, or JC2 conclusion is
   allowed.

Check the report's refusal scope and identify any sentence that is stronger
than these eight items.  Local heavy CAS, solver, Lean, or long Python is
prohibited; use source reading and hand algebra, or explicitly stage any
substantive replay on AWS.  The review output must be written to a distinct
report path and must not mutate the producer or V1 bytes.

