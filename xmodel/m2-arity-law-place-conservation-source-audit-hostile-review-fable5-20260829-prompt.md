# Hostile review: place conservation and the safe defect floor

Work only in `/Users/dc/code/math/jc2`. Independently review the sealed
Sol 5.6 source audit

`xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md`

- full SHA-256
  `05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84`;
- body SHA-256
  `1608a44660e094e0fa8cf05b4f1db3b97173243a9e8319a7f55d4c44f0f1cb85`.

Reconstruct from the printed source and pinned reviewed reports. Required
attacks:

1. Keep physical places/rays, Puiseux series on a cover, physical flags,
   direction-orbits, the full actual exit set, and the MFE selected-witness
   set distinct. Decide whether `mult(p_F,c)` counts series or places.
2. Verify/refute FULL-EXIT-COVERAGE: every physical place through an up
   child has a unique same-ray cv flag, without claiming injectivity or
   exactly `m` places/flags.
3. Reconstruct the td8 trunk and td12 B-charge arguments using only the
   corrected carrier dictionary. Decide whether both numerical conclusions
   survive and identify any missing endpoint qualification.
4. Attack the proposed universal equality
   `min(num(delta),2*ceil(delta))`. Check the audit's axiomatic delta=4/3
   counterprofile and say exactly what it does and does not refute.
5. Prove or refute the stated safe lower floor: `delta` for positive integral
   defect, `ceil(2*delta)` for nonintegral defect, for the full actual exit
   set only. Do not upgrade a floor to attainment.
6. State the exact canonical wording repairs and any remaining source-grid
   hypothesis that could strengthen the floor.

Give `PASS`, `PASS_WITH_REPAIR`, `GAP`, or `REFUTED`. Include an explicit
mutation/negative control. Write only

`xmodel/m2-arity-law-place-conservation-source-audit-hostile-review-fable5-20260829.md`

and seal it. Do not edit the target or canonical files, commit, push, browse,
use AWS/heavy compute, or enter, enumerate, search, read, build, status,
modify, or control `jc2-lean`.
