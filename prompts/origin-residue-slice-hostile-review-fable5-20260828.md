You are Fable 5 performing a compact independent hostile audit in
`/Users/dc/code/math/jc2`. Do not enter/list/search/read/build/status/modify
`jc2-lean`. Use only standard-library exact desk computation. Preserve all
frozen producer bytes.

Frozen target:

- report `xmodel/ggv-upper-endpoint-origin-residue-slice-sol-ultra-20260828.md`
  SHA256 `7202f70380c8379d85dab82e4ef06f47b1312ba840775d8581eaa629ed328e30`;
- producer checker
  `cases/ggv_8_28_upper_endpoint_origin_residue_slice_20260828/verify_origin_residue_slice.py`
  SHA256 `de371953d4bc22da7cfc39c4e94221097eac7612b7b4a8b44afe0fd14ecb76e0`;
- exact arbitrary-Q negative control
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-even-subbranch-origin-coupling-independent-sol-ultra-20260828.md`
  SHA256 `c940ba048f5edf60b3018670c8914acc469f55f30101f211a6aedb5d591b6714`.

The theorem scope is STRICTLY
`A=X^4-1, lambda=0, c2!=0, exact D=0, Q=e=F8=r=0`.
Do not promote it to arbitrary Q, another A, another branch, the full
endpoint, Keller, or JC2.

Do not trust or import the producer checker. Build a fresh self-contained
standard-library exact checker from the formulas and audited recurrence.
Independently audit:

1. The characteristic-zero exactness theorem for
   `T5(d)=(5*A'*d+2*A*d')/2`, including zero kernel and the degree bounds
   needed here. On the fixed slice derive, rather than assume, every literal
   q7/q9/q11/q13 solution and prove completeness of
   `f=4T5(a0+a1X+a2X^2)`,
   `F9=4T5(b0+b2X^2+b3X^3+b4X^4)`,
   `F11=4T5(A(k0+k2X^2))/A`, and
   `F13=4T5(A^2 ell13)/A^2`.
   Verify exactly why the missing X coefficients in the q9 and q11
   primitives are forced by the authoritative raw constant floors. Check
   all window supports and ensure no legal primitive/raw mode is omitted.
   Verify q5 and q15 really are automatic under the named specialization.
2. Reconstruct the COMPLETE characteristic coefficients G11 and G15 from
   `G=F^(3/2)+sum_{birth=2,4,...,20} c_birth*t^birth*F^((6-birth)/4)`.
   Do not silently drop born or predecessor modes. Check exactly
   `G11=(3/2)A^2F11+(5/4)c2*A*F9+c4*F7` and
   `G15=(5/4)c2*A*F13+c4*F11
          +(1/A)((3/4)c6*F9+(1/2)c8*f)`;
   justify that c10,c12,c14 contribute zero because F5=F3=F1=0 and that
   later modes are unborn.
3. Perform exact division of the G15 pole numerator by A and independently
   derive the full remainder. Verify its X coefficient
   `R[X1]=10*(3*c6*b2+2*c8*a2)` and the polynomial identity
   `5*D22[X0]+6*F7[X0]*R[X1]=0`, with
   `D22[X0]=F11[X1]G11[X0]-F7[X0]G15[X1]`.
   Audit every normalization, derivative coefficient, sign, and endpoint
   target. Confirm coefficientwise polynomiality forces R=0 and hence
   D22[X0]=0, contradicting target +1.
4. Check the field versus scheme scope. State what coefficient domain and
   characteristic are required. Do not use c2!=0 if the proof does not need
   it; report that as harmless scope narrowing rather than silently treating
   it as load-bearing.
5. Explicitly compare the frozen arbitrary-Q `Q=X` mutation. Independently
   replay enough exact formulas to confirm it has legal q7--q15 primitives,
   legal G11/G15 windows, and nonzero origin pairing, so the fixed-slice
   residue identity cannot be generalized to arbitrary Q. Do not claim it
   is a full endpoint survivor.
6. Include hostile mutations detecting at least: restoring the forbidden
   primitive X coefficient; dropping a characteristic mode; changing one
   fractional coefficient; changing a residue coefficient/sign; replacing
   target +1 by -1; and substituting Q=X into the fixed-slice conclusion.
   Verify frozen hashes at start/end.

Create:

- `xmodel/ggv-upper-endpoint-origin-residue-slice-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-origin-residue-slice-hostile-review-fable5-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_origin_residue_slice_hostile_review_fable5_20260828/`
  with README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256.

Give explicit PASS/REPAIR/FAIL; name the exact first defect if any. Make the
checker standalone, deterministic, standard-library only, run it with
`PYTHONDONTWRITEBYTECODE=1 python3 -B`, use repo-root-relative manifests,
hash final bytes, and return paths/hashes/output. Proceed directly.
