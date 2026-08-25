# Hostile review: squarefree cubic Poisson/fractional-power recurrence

Write the verdict to
`xmodel/max12-912-squarefree-poisson-truncation-review-grok-20260825.md`.
Do not mutate producer files.  Do not run substantive computation locally;
any CAS or long exact replay must run on AWS and record custody.

Audit the provisional producer note
`xmodel/sol-max12-912-squarefree-poisson-recurrence-20260825.md`, pinned at
SHA-256
`ff082a2c6607d33b0d117ca5e745dd8b88f267752670b364a1c434eb6d125e88`.
If its bytes differ, stop and report a custody failure rather than reviewing
a moving target.

Independently rederive, rather than merely pattern-match, these charges.

1. Check the polynomial and rational homogeneous centralizer lemma for a
   squarefree binary cubic `K`, including roots at infinity, localization at
   `K`, negative degrees, and every field/characteristic hypothesis.

2. Check that the decreasing-degree completion and the unique root
   `R=P^(1/3)` are well-defined, and that
   `[R,Q-R^4]=c/(3R^2)` implies

   ```text
   Q=[R^4+(lambda/3)R^3+mu R^2+nu R+delta]_>=0.
   ```

   Charge the degree bookkeeping carefully: the right side starts in degree
   `-6`, the leading bracket with a degree-`d` remainder is degree `d+1`,
   the resonances are exactly `9,6,3,0`, and a noncommuting remainder may
   first affect the constant Jacobian at degree `-7`.  Identify any missing
   completeness, domain, or centralizer premise.

3. From the original homogeneous Jacobian rows or an independently expanded
   fractional-power series, verify equations (1)--(9), including all signs,
   coefficients, and the target-shear terms.  Confirm or reject the predicted
   squarefree degree-15 dimensions `16+6=22`.  Treat the old degree-14 hash
   `e46d3204...` and its dimensionally invalid `(lambda/3)V` as a disclosed
   negative control, not as the current formula.

4. Independently verify the corrected degree-14 formulas (10)--(12):

   ```text
   C=B-A^2/3,
   W=T-AB/3+2A^3/27,
   Q7=4KV/3+4AU/9+4CW/(9K)+(lambda/3)KB,
   K | C W.
   ```

   Check that the eight squarefree root-allocation pieces are a set-theoretic
   union, that the triangular parametrizations and `19+5=24` dimension count
   are honest, and that no scheme/radical assertion is silently made.

5. Independently verify the preregistered degree-13 formulas (13)--(16).
   In particular, under `K|CW`, decide whether polynomiality of

   ```text
   4CU/(9K)+(2/81)(9W^2-6ACW-2C^3)/K^2
   ```

   is equivalent to `K|C` and `K|W`, and whether this makes the complete
   numerator divisible by `K^2` with no hidden condition on `U`.  Check the
   polynomial Q6 formula and `21+5=26` dimension count.

6. Independently verify the degree-12 formulas (17)--(19): with

   ```text
   N=M-AL/3,
   R5=9U-A^2L-3AN-3KL^2,
   ```

   check the exact Q5 coefficient, the identity for the scaled pole
   numerator, equivalence to `K|N R5`, and the `23+3=26` branch dimension.

7. State exactly what this would license for the squarefree order-one
   fixed-D12 `(9,12)` coefficient stratum.  Do not infer completion of lower
   rows, a perfect cube, a maximum-12 theorem, a counterexample, or JC2.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`; list every exact
mathematical/software/custody defect; separate set-theoretic statements from
scheme statements; and propose the cleanest next row or general induction.
