You are Fable 5 acting as an independent hostile mathematical reviewer in the
plane Jacobian-conjecture campaign. Work only in `/Users/dc/code/math/jc2`.
Do NOT enter, list, search, read, build, status, or modify `jc2-lean`.

Audit the frozen exact D16--D22 continuation of one deep active-c2 literal
survivor. Reconstruct all load-bearing algebra yourself; do not import or
trust the producer checker as the proof. This is standard-library exact desk
algebra only: no Singular/Sage/Mathematica and no heavy local computation.

Frozen producer inputs (preserve bytes):

- `xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-sol-ultra-20260828.md`
  SHA256 `a4bfbb1437c0e67a8f55439d6b9bd6d0a60a70340d41e6481068cf148ad50a3c`.
- `cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/probe_literal_tail.py`
  SHA256 `f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45`.
- That case's frozen source dependencies:
  `cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py`
  SHA `112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26`;
  `cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py`
  SHA `7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1`;
  `cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json`
  SHA `ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.

Build a new self-contained Python standard-library checker with independent
sparse rational polynomial/Laurent arithmetic and the fractional-series
recurrence. Do not dynamically import the producer checker. Audit:

1. Reconstruct the exact rational prefix point
   `A=X^4-1`, `V0=A`, `T=-A/4`, `Z=(1-A)/2`, the displayed F4--F6,
   F7 onward zero where no raw slot is present, c2=c6=1, and the displayed
   c14. Verify polynomial characteristic coefficients and raw determinant
   rows D0..D15 before using any tail assertion.
2. Register every mode c2,c4,...,c20 and continue the characteristic
   recurrence through weight 22. No born or predecessor mode may be silently
   omitted.
3. Read and independently enforce the authoritative raw windows. In
   particular verify there are no legal raw F15+ slots and no G22 receiver,
   while
   `G16:X^2..X^8`, `G17:X^2..X^7`, `G18:X^2..X^6`,
   `G19:X^3..X^5`, `G20:X^3..X^4`, `G21:X^3`.
4. At born rows solve exact affine polynomiality/window conditions and check
   uniqueness under the frozen remaining data:
   `c16=0`,
   `c18=16369/140737488355328`,
   `c20=0`.
   Verify `G16=...=G21=0`, not just degree bounds.
5. Reconstruct literal raw F,G and determinant rows. Verify D0..D21=0 and
   homogeneous D22=0. Keep this distinct from the endpoint equation D22=1,
   which the point must fail.
6. Independently compute the absent-receiver characteristic coefficient
   `g22=9207/(144115188075855872*A^5)` in reduced form. Derive and verify the
   universal receiver operator
   `L22(R)=-40*A^3*A'*R-8*A^4*R'`, including sign convention, and check
   `-L22(g22)=0`. Explain why scalar A^-5 is the exact homogeneous kernel and
   why this does not show general deep-locus emptiness.
7. Mutations must catch at least: c18=0 (genuine weight-18 pole), wrong c18,
   a dropped predecessor c6 or c14 contribution, a wrong G window, changing
   `-40` to `-39`, and a numerator/denominator/sign mutation in g22.
8. If calling the point non-q1, independently solve/test
   `V0=A'R0+2AR0'`, deg R0<=4. Otherwise remove that label. Separate exact
   identities, one-point existence, and all universal claims.

Create without modifying frozen inputs:

- `xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-hostile-review-fable5-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_tail_hostile_review_fable5_20260828/`
  with `README.md`, `RESULT.json`, `SOURCE.sha256`, and `EVIDENCE.sha256`.

The checker must be deterministic, self-contained, standard-library only,
run under `PYTHONDONTWRITEBYTECODE=1 python3 -B`, include sensitivity
mutations, and print an explicit terminal marker. Hash after finalization;
SOURCE must cover all load-bearing inputs and checker, EVIDENCE must cover
report/README/RESULT without self-reference. Recheck every frozen hash at the
end.

Give one explicit verdict PASS, REPAIR, or FAIL. Name every defect and its
impact. Do not overclaim a universal deep-locus theorem, scheme statement,
endpoint/branch-P theorem, Keller result, counterexample, or JC2 resolution.
At completion respond concisely with verdict, paths, hashes, replay output,
and defects.
