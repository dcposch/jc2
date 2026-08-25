# Hostile source audit — corrected AS post-D10 D9/D8 package

Work in `/Users/dc/code/math/jc2` as a hostile different-model reviewer. The
prior Claude attempt failed technically by exceeding its output limit and
wrote no report; it supplies no evidence. Review the frozen corrected package:

- `xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md`;
- every file in
  `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/`;
- the confirmed omitted-carry erratum and D10 producer/review;
- the old post-D10 package only to police quarantine.

Charged hashes:

```text
report      9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8
manifest    a5480d2e3d7c36db4fee735ef8f2262c3454e3e35eb348c7f097c45c59aa2cfb
freeze      bf7ce39ae1cf7cc6338c006cd2cd59d11a387d8644d740e6faee2cb63229a264
replay_all  b3564b4e34f60bba751f00de3e30420050c1e6537db3a137001b89d0ca16e5ff
```

The separately completed Grok state review
`xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md`
already confirms the abstract displayed D8 matrix and its literal-F3 census;
do not repeat that long audit. The missing gate is source lineage. Independently:

1. rederive from the integer Jacobian
   `det J-1=3L+9(K+C_x+D_y)+27M+81N`; derive the single-Frobenius part of
   `K/3 mod 3`, the vanishing of the double-Frobenius part, and the entry of
   all six degree-six Frobenius variables with the stated caps;
2. reconstruct the vertical D9 rows and global section, then the D8 `7x5`
   core *and affine column* after the six licensed pivots; decide whether the
   frozen column is exactly the next AS source row rather than an ambient or
   representative-dependent surrogate;
3. reconstruct the localized `g!=0` endpoint after its three D10 pivots,
   including its 17 rows, 14 digit unknowns, all Frobenius directions, and
   the two named degree-nine terms;
4. check the four next-carry controls directly in the integer determinant,
   especially division by 81, residual `x^4+2*x^6+2*x^8`, and pointwise
   versus fibre-wide scope; and
5. verify that the old counts/column remain quarantined and that no
   `Fbar_3`, all-depth, characteristic-zero, counterexample, or JC2 claim is
   smuggled in.

Run the portable replay as regression, but base the verdict on independent
exact source reconstruction. Use `/tmp` for scratch and do not edit producer,
case, canonical, coordination, prompt/log/run, predecessor, or other review
files. Do not use AWS.

Write exactly
`xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md`.
Keep the report concise (at most 12,000 words). Give per-item and overall
`CONFIRMED`, `GAP`, or `REFUTED`, the smallest failing source identity if any,
and exact promotion/quarantine scope.
