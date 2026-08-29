# V43G4 additive metadata and sensitivity supplement

Date: 2026-08-27

This nonmutating supplement clarifies four metadata points in the frozen V43G4
producer.  It does not alter the certificate, result, preregistration, or
their hashes.

- The raw sigma weights of the surviving row products are `15` and `20`.
  The result JSON stores the corresponding normalized levels `3` and `4`,
  obtained by division by `wt(a1)=5`.  These are two descriptions of the
  same homogeneous components.
- The symbols `H_i` in the V43G4 display are the eleven generic total-row
  cofactors.  In the special-fibre converter, the unrelated polynomial
  `(a1^M-B)/t` should be called `H_special` (or another distinct name) to
  prevent a naming collision.
- The harvested immutable AWS source manifest is
  `additive_review_supplement_20260827/AWS_SOURCE_MANIFEST.sha256`, whose
  SHA-256 is
  `89a4b9a0e33ce84b8e3dda793d2ddd37ef384951ba6fa7b1d0cccf6d94305fe7`.
- The negative control changes one literal source coefficient of `Tg15_7`
  while holding every banked cofactor and the target fixed.  Its recorded
  residual is therefore a mutation of the complete replayed sum, not a
  target-coefficient tautology.

