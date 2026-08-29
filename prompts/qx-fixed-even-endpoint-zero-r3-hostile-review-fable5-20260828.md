You are Fable 5 performing an independent hostile audit in
`/Users/dc/code/math/jc2`. Do not enter/list/search/read/build/status/modify
`jc2-lean`. Use only standard-library exact desk computation. Preserve all
frozen producer bytes.

Charged frozen target (supersedes the one-point r2 packet):

- report
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-sol-ultra-20260828.md`
  SHA256 `a6e49a08a6fc92c71f9f9ee34079b5626f6a00a20499b06e50c8b8451f3338be`;
- producer checker
  `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_fixed_even_endpoint_zero_20260828/verify_qx_fixed_even_endpoint_zero.py`
  SHA256 `49e61d547e8b30e6ffc3c792f1dffdb6ae8e960aec490047e5c544fee222adf1`.

Pinned upstream/control inputs:

- q15 report
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-q15-independent-sol-ultra-20260828.md`
  SHA256 `188317138e60224f5a7e9dc1de18ab339384c5246c1cabf12acc20657dac7d5f`;
- q15 checker
  `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/verify_lambda0_q15.py`
  SHA256 `6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a`;
- r2 one-point mutation report
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-g13-obstruction-r2-sol-ultra-20260828.md`
  SHA256 `b5433f4e4a76f48d8899d59b28290dc7075ac591b89913323e5102a998e73a08`;
- r2 checker
  `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_g13_obstruction_20260828/verify_qx_g13_obstruction.py`
  SHA256 `fb29dec1a7eb08a41818c8ea802c984f893d8a222d38aade6fdf4af9bc272638`;
- authoritative raw slots
  `cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`
  SHA256 `28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876`.

The theorem scope is exactly characteristic zero and
`A=X^4-1,Q=X,r=e=F8=F10=F12=F14=0`, with
`F1=F3=F5=F6=0`, the displayed fixed F2,F4, all literal odd raw floors,
q7/q9/q11/q13/q15 exactness, and arbitrary scalar characteristic modes.
It is not a universal lambda=0 theorem.

Do not trust/import/execute either producer checker. Build a fresh
self-contained standard-library exact checker. Audit from the q formulas,
fractional characteristic, raw windows, and recurrence rather than from the
producer narrative:

1. Build the complete 50-by-55 rational linear system for the five gates.
   Include exactly the 20 raw variables in f,F9,F11,F13 and all 35 primitive
   variables d7,d9,d11,d13,d15 with authoritative floors/degree bounds.
   Independently exact-RREF it and verify rank 50, dimension 5, pivot/free
   sets, and that the free coordinates are precisely
   d15[X4],d15[X5],d15[X6],d15[X8],d15[X9]. Do not merely compare these five
   names: verify every basis vector replays all 50 original equations and
   report a canonical full-basis digest or exact census. Derive
   `f0=-(2^29/75)a1+(2^28/225)a4` and all other raw coordinates needed below.
2. From the complete characteristic
   `G=F^(3/2)+sum_{k=1..10}c_(2k)t^(2k)F^((6-k)/4)`, independently compute on
   every one of the five odd-fiber basis vectors and every relevant mode the
   full rows needed for G11[X0], G13[X0], G15[X1], and the complete Laurent
   pole/remainder at G15. Verify no odd predecessor/born mode is silently
   dropped. Explicitly census c10,c12,c14: they are born by weight 15 but
   vanish for distinct reasons (residual t5 with F5/partitions zero,
   positive coefficient of F^0 zero, residual t1 with F1 zero), whereas
   c16..c20 are genuinely unborn. The producer checker comment loosely calls
   later modes unborn; classify whether this needs a precision repair while
   separating it from theorem soundness.
3. Verify basis-level identities
   `G11[X0]=-c4*f0`, `G13[X0]=(3/4)c6*f0`, and the c4 load
   `G15[X1]=c4*F11[X1]+...`. Compute all base,c2,c4,c6,c8 row vectors, not
   only the nonzero rows. Confirm the c4 endpoint cancellation and derive
   exactly
   `E=f0*(c6*(-2^21*a1/5-2^19*a4/3)+c8*(2^29*a2/75))`.
4. Normalize every possible G15 pole, reduce the COMPLETE A^-1 numerator
   modulo A coefficientwise, and verify its X1 coordinate
   `R15=-(7*2^19/3)c6*a4+(2^29/15)c8*a2`. Check that base,c2,c4 and every
   other scalar mode have zero load in this coordinate for proved reasons.
   Ensure G15 polynomiality really implies R15=0 over the stated coefficient
   domain.
5. Verify the exact polynomial/ideal identity
   `E=(f0/5)R15+(4/3)(-2^21*a1/5+2^20*a4/15)G13[X0]` coefficientwise as a
   quadratic identity. Determine whether this is ring/scheme-level ideal
   containment or only a field/radical consequence. Verify that the literal
   G13 lower floor gives G13[X0]=0 and the endpoint target is +1, hence the
   fixed-prefix fiber is excluded with no case split. Audit every constant,
   sign, and normalization.
6. Replay the r2 Q=X point as a mutation/control and locate it in the
   five-dimensional basis. Confirm it passes the q gates and G8..G12, fails
   first at G13[X0] for c6=1, c6=0 repairs G13, and directly compute the
   endpoint before/after c6=0. Verify the charged r3 theorem explains the
   control rather than contradicting it.
7. Scope firewall: arbitrary scalar modes are allowed, including c2=0 or
   c2!=0, but the even prefix is fixed. Do not promote to arbitrary Q/e/F8,
   full lambda=0, full endpoint/Keller, or JC2. Identify exactly which fixed
   assumptions enter.
8. Include mutations detecting: one dropped q row/variable; wrong pivot/free
   set; omitted characteristic mode; treating c12/c14 as genuinely unborn;
   one G13 or residue coefficient/sign change; deleting c4 cancellation;
   wrong endpoint target sign; and a nonzero remainder incorrectly accepted
   as polynomial. Verify frozen hashes at start/end.

Create:

- `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-hostile-review-fable5-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_fixed_even_endpoint_zero_r3_hostile_review_fable5_20260828/`
  with README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256.

Give explicit PASS/REPAIR/FAIL, the exact first questionable line, and the
surviving theorem scope. Make the checker standalone, deterministic,
standard-library only, run with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, use
repo-root-relative manifests, hash final bytes, and return paths/hashes/output.
Proceed directly.
