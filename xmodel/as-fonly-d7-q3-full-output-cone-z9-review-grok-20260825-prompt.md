# Hostile review prompt — AS D7 fixed-fibre `Z/9` output-cone survivor

Review the frozen producer/case adversarially.  Do not trust prose, stored
ranks, solution counts, or booleans.  Do not edit frozen bytes.

Producer:

`xmodel/as-fonly-d7-q3-full-output-cone-z9-producer-20260825.md`

Case:

`cases/as_fonly_d7_q3_full_output_cone_z9_20260825/`

Required output:

`xmodel/as-fonly-d7-q3-full-output-cone-z9-review-grok-20260825.md`

## Charges

1. Audit the full transitive source chain in the 99-KiB frozen source archive
   (SHA `c3cb56df...`) and the immediate compiler SHA `2d2e0f5f...`.  Confirm
   the three consumed Q3 parents are exactly the previously reviewed pinned
   fibres/models `0000`, `0270`, and `0513`, not a reset or unrelated map.
2. Derive the determinant orientation and the exact identity for
   `F=F_*+27U+81V`.  Check that combining digits as `T=U+3V in Z/9` is valid
   for determinant congruence modulo 243, and that all 91 coefficient slots
   in degrees 0 through 12 and all 72 D7 output variables are present.
3. Inspect the mod-3 RREF and Bockstein construction.  Check signs, integer
   representatives, division by 3, kernel-carry columns, high digits, and
   solution reconstruction.  Independently verify the displayed ranks and
   kernel dimensions from the frozen matrices/outputs where possible.
4. Charge all linearity controls: two derivative-zero constants, doubled
   bases, all 1296 P/Q pairs with remainder divisible by 729, and every Q3
   kernel/fresh-basis mixed second difference.  Confirm each Q3-kernel
   difference is literally `81*K` with D7 support and the mixed remainder is
   divisible by 2187.  Look specifically for a hidden order-9 direction.
5. Audit the literal integer particulars and verify every coefficient of
   `det J(P,Q)-1` is divisible by 243 for all three results.  Do not accept
   the `literal_integer_replay_mod243_passed` flag without checking source and
   payload consistency.
6. Check the row-8 column list and whether degree-four digits genuinely
   explain why the prior displayed degree-at-most-three exclusions do not
   close these full output cones.
7. Audit custody: rc files, source/input/result hashes, archive, manifest,
   freeze, host/path, runtime/RSS.  Distinguish one implementation at three
   inputs from independent implementations.
8. State the strongest licensed theorem and refuse overreach.  The intended
   scope is three pinned reviewed Q3 fibres, all fixed-D7 output digits at
   orders 27/81, and determinant modulo 243.  Refuse the whole predecessor
   scheme, terminal modulus 729, order-243 digits, deeper compatibility,
   `Z_3`, collision, counterexample, no-lift, or JC2 claims.

No substantive computation may run on the local Mac.  This should be a
no-shell source/mathematical review.  If replay is essential, use AWS only and
record immutable host/path/source hashes/commands/rc/output hashes/resources.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`, classifying every
issue as mathematical, source-typing, software, custody, or wording/scope.
