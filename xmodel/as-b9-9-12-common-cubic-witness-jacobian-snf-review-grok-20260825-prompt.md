# Hostile review charge: common-cubic witness Jacobian/SNF

Review the producer report and case

- `xmodel/as-b9-9-12-common-cubic-witness-jacobian-snf-producer-20260825.md`;
- `cases/as_b9_9_12_common_cubic_witness_jacobian_snf_20260825/`.

Run every substantive replay on AWS only.  Do not run local Bash, Python,
CAS, or solver commands.

Independently audit:

1. reconstruction and orientation of all 276 determinant rows and all 23
   common-cubic top-form rows in 149 variables;
2. exact ranks `146` over `Q` and `94` over `F3`;
3. the full Smith valuation histogram, especially the distinction between
   determinantal-ideal valuation `205` and largest invariant valuation `13`;
4. the residual-threshold/rank argument proving failure of every classical
   maximal-minor inequality at this one witness;
5. the exact rational-kernel classification as two translations plus the
   degree-compatible target shear `Q -> Q+tP`;
6. the scaling negative control and why congruential common-core equations
   make it nonzero over `Z` but zero modulo `3^11`;
7. whether any sentence overreads failure of a maximal-minor criterion as
   failure of a Smith-coordinate/dilatation route, lifting, or nonexistence;
8. source hashes, result hashes, timing/custody, and exact one-witness scope.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`, with a concise
list of every mathematical, source, custody, or scope defect.  A replay of the
same source is useful custody but not an independent source construction.
