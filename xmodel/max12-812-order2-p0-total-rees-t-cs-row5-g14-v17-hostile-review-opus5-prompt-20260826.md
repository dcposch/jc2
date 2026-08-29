You are a hostile independent reviewer of a producer-tier exact coefficient
export in the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2`. Do not trust producer PASS strings, prose, or
finite-field agreement. Make no repository edits except the final report at
exactly

`xmodel/max12-812-order2-p0-total-rees-t-cs-row5-g14-v17-hostile-review-opus5-20260826.md`.

Primary package:

`cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/`

Upstream inputs:

- `cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py`
- `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json`
- `cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/`

Claim to audit: V17 extends the literal total moving-p fifth source row through
grade 14, bridges its grades 10--12 exactly to the frozen V9 exports, and
exports a nonzero 304-term grade-14 coefficient. That coefficient is even in
`rho`; under

`rho=ell1=rs=a0=c1=c0=e0=0, cs=b, e1=b^2*w, k=(12/5)*w^2`

it is exactly `-(21/320)*b^5*w^2`, with all live correction terms included.

Required hostile checks:

1. Verify the package freeze and both harvested AWS evidence manifests,
   RESULT files, generated coefficient/script hashes, diagnostics, engine
   return codes, and validators. State every custody gap.
2. Trace the V17 compiler to the literal total source
   `p=-2*rho^2+sum_(i=1)^14 2*ell_i*sigma^i`, the complete A/C correction and
   load series, and the frozen 89 fifth-tail monomials. Check for omissions,
   duplicate conventions, stale specialized-source imports, or post-freeze
   mutation.
3. Independently check the grade-10, 11, and 12 coefficient bridge against
   the exact-Q V9 exports. Determine whether the known harmless V8/V9
   post-extraction TPhi rebuild defect affects any coefficient used here.
4. Independently verify the grade-14 term count, nonzeroness, rho parity, and
   the exact odd-sheet specialization `-(21/320)*b^5*w^2`. Check that changing
   `12/5` to `11/5` is a genuine negative normalization control.
5. Verify that the F65521 lane is only an independent encoding/software
   control and that no modular inference enters the characteristic-zero
   claim.
6. Enforce scope: a valid result is only a source-honest coefficient export
   and low-grade bridge. It does not make the T-cs ideal a unit, prove rho is
   a unit, close Gate T/order two/maximum twelve, or resolve JC2.

Use exact algebra for any light recomputation. Do not launch heavy local CAS
or memory-intensive Python; report any such need as a review gap. End with
exactly one verdict label:

- `VERDICT: CONFIRMED`
- `VERDICT: CORRECTED`
- `VERDICT: REFUTED`

For `CORRECTED`, give the strongest surviving exact statement. For
`REFUTED`, exhibit a concrete failed identity, omitted source term, or custody
mismatch.
