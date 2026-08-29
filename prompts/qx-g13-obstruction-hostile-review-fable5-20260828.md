You are Fable 5 performing a compact independent hostile audit in
`/Users/dc/code/math/jc2`. Do not enter/list/search/read/build/status/modify
`jc2-lean`. Use only standard-library exact desk computation. Preserve all
frozen producer bytes.

Frozen target:

- report
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-g13-obstruction-r2-sol-ultra-20260828.md`
  SHA256 `b5433f4e4a76f48d8899d59b28290dc7075ac591b89913323e5102a998e73a08`;
- producer checker
  `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_g13_obstruction_20260828/verify_qx_g13_obstruction.py`
  SHA256 `fb29dec1a7eb08a41818c8ea802c984f893d8a222d38aade6fdf4af9bc272638`;
- frozen mutation report
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-even-subbranch-origin-coupling-independent-sol-ultra-20260828.md`
  SHA256 `c940ba048f5edf60b3018670c8914acc469f55f30101f211a6aedb5d591b6714`;
- its checker
  `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_even_subbranch_20260828/verify_even_subbranch_reduction.py`
  SHA256 `23f46a95170fb77f2f5c340b1c6fb570881062d67102fca6dfdeae2f5ea37c4d`.

This is a FIXED-FIXTURE obstruction only, not a universal exclusion. The
fixture is exactly
`A=X^4-1,Q=X,r=e=F8=0,c2=c6=1`, all other displayed modes zero, with the
frozen f,F7,F9,F11=F13=0 and q primitives in the report.

Do not trust/import/execute either producer checker. Build a fresh
self-contained standard-library exact checker from the authoritative
fractional characteristic and raw recurrence. Independently audit:

1. Reconstruct the complete characteristic through at least G15 from
   `G=F^(3/2)+sum_{k=1..10} c_(2k)t^(2k)F^((6-k)/4)` with the exact fixture.
   Verify all born and predecessor modes, both Laurent/polynomial status and
   authoritative lower/upper raw windows. Confirm G8,...,G12 pass and that
   no earlier G receiver fails.
2. Derive the displayed G13 polynomial coefficientwise. Verify its only
   illegal slot is `G13[X0]=-2^27/25`, while all nonconstant support lies in
   the literal degrees 1..11. Distinguish a receiver-window failure from a
   determinant recurrence failure, and directly replay D0,...,D13=0.
3. Holding the raw F fixture fixed, decompose G13[X0] independently into
   the base trajectory and every born scalar mode c2,c4,c6,c8,c10,c12.
   Confirm the vector `(0,0,0,-2^27/25,0,0,0)` in that order and justify why
   later modes are unborn. Audit the claim that scalar-mode changes alone
   force c6=0, including its exact coefficient-domain scope.
4. Set c6=0 with the other fixture data unchanged. Verify the entire G13
   receiver is repaired. Then compute the origin coupling
   `D22[X0]=F11[X1]G11[X0]-F7[X0]G15[X1]` before and after the change.
   The producer prose says the old endpoint coupling used c6; determine the
   exact before/after values and whether `c6=0` truly destroys the displayed
   target-one-after-scaling fixture. Treat failure to substantiate this as a
   repair even if the G13 obstruction itself is sound.
5. Reconstruct G14 after c6=0 and verify the claimed genuine normalized
   pole `A^-1*(-5*X^6/2^34)`: audit that there are no deeper hidden poles and
   that the numerator is not divisible by A. Check whether any other born
   mode or regular term changes this conclusion under the strictly unchanged
   fixture; do not generalize after releasing raw data/modes.
6. Verify field/radical/scheme and branch scope. This packet must not imply
   arbitrary-Q/e/F8/primitive/mode impossibility, full endpoint emptiness,
   Keller, or JC2.
7. Include mutations detecting: dropped predecessor/born mode; wrong
   fractional exponent or coefficient; omitted receiver lower floor;
   restoring c6; a fake cancellation of G13[X0] by another scalar mode;
   endpoint impact sign/value error; and treating the G14 numerator as
   divisible by A. Verify frozen hashes at start/end.

Create:

- `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-g13-obstruction-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-g13-obstruction-hostile-review-fable5-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_g13_obstruction_hostile_review_fable5_20260828/`
  with README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256.

Give explicit PASS/REPAIR/FAIL and exact first questionable line if any.
Make the checker standalone, deterministic, standard-library only, run it
with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, use repo-root-relative manifests,
hash final bytes, and return paths/hashes/output. Proceed directly.
