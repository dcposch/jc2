# Task: hostile independent review of the claimed direct ordered `T-cs` certificate

Work in `/Users/dc/code/math/jc2`.

Review, adversarially and independently, the new producer report

`xmodel/max12-812-order2-p0-total-rees-t-cs-direct-total-certificate-opus5-20260827.md`

whose claimed SHA-256 is
`7af66e58a7262ca05bf140919ed3d6ff4e0357bdb6db3378d494907ff33baa8f`.

The claimed result is the exact polynomial containment

```text
cs^447*k^164 in
(Tg10_1,...,Tg12_7,Tg14_5,
 rs-cs*qrs,c0-cs*qc0,c1-cs*qc1,qrs)
```

over `Q`, equivalently a direct certificate of the requested
`cs^N*k^M*(1+rho*W)` type with `W=0`.  Do not trust the report's verdict,
hash table, parser, reductions, or logical composition.

Required hostile checks:

1. Rehash the report and every frozen V9/V17 input it actually charges.  Pin
   the literal generator order and distinguish the honest ordered chart from
   the substituted presentation.
2. Independently parse the frozen polynomial bytes with exact rational
   arithmetic.  Check Lemma 0 for every one of the 22 rows, including signs
   and the four bilinear/`qrs` cofactors.  Reject any hidden division by `cs`,
   `k`, or `rho`.
3. Re-expand the complete grade-10 branch-(a) identity and verify exactly
   `cs^6*k^2*rho^6`, including its translation back to the honest chart.
4. Audit every branch-(b) solved form and reduction in sections 5.1--5.5.
   Verify the claimed ideal containments over `Q`, the exponents
   `cs^147*k^54`, and the lift from `rho=0` to an honest
   `cs^147*k^54 + rho^2 H` containment.  Pay special attention to any
   unprinted quotient/remainder, saturation, radical, division, or
   coefficient-denominator assumption.
5. Verify the composition identity in section 6.1 and the final exponents
   `(447,164)`.  Decide whether the printed generating data really suffices
   to establish existence of polynomial cofactors even though the expanded
   final cofactors are not serialized.
6. Check the geometric conclusion and scope.  In particular distinguish
   outright emptiness on `D(cs*k)` from special-fibre emptiness, and evaluate
   the report's warning that the staged-calculus converse about saturation
   and adjoining `rho` was too broad.
7. Separately audit the V19 typing criticism: after inverse-variable clearing,
   what exactly is certified, what extra divisibility of the `rho` cofactor
   would be needed for the direct unit-plus-`rho` type, and whether Lemma 0 is
   genuinely missing from the V18/V19 acceptance predicates.

Use a fresh exact `fractions.Fraction` parser/replay where useful.  This is a
small exact audit, not a CAS job: do not run Singular/Groebner, do not launch
AWS, and do not access or modify `jc2-lean`.  Do not read V18R1/V19 engine
outputs.  Read only the producer report and its explicitly frozen source
inputs plus directly relevant promotion/interface files needed for scope.

Write exactly one file and no other file:

`xmodel/max12-812-order2-p0-total-rees-t-cs-direct-total-certificate-hostile-review-fable5-20260827.md`

Start with a one-line verdict chosen from `CONFIRMED`, `REPAIRABLE`, or
`REFUTED`.  Give a claim-by-claim table, exact independent check telemetry,
all defects ranked HIGH/MEDIUM/LOW, the narrowest accepted theorem, and a
firewall of nonclaims.  A banner or matching sample values are not evidence.
