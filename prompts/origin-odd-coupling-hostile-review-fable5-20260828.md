You are Fable 5 performing a compact independent hostile audit in
`/Users/dc/code/math/jc2`. Do not enter/list/search/read/build/status/modify
`jc2-lean`. Use only standard-library exact desk computation. Preserve all
frozen bytes.

Frozen target:

- report `xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md`
  SHA256 `3e4a0f03acec2ee5e3cdfff558c481e14735408aa18486d23215958ed8d4bb3a`;
- checker
  `cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828/verify_origin_odd_coupling.py`
  SHA `f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8`;
- authoritative raw-slot source
  `cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`
  SHA `28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876`.

Do not trust/import the producer checker. Build a fresh self-contained
standard-library parser/checker and independently audit:

1. Parse every authoritative F/G raw slot and verify the upper-chart map
   `X=x*y^3`, `t=1/y`: F-weight-w slot X^i maps to
   `x^i y^(8+3i-w)` and G to `x^i y^(12+3i-w)`. Check slot names,
   exponents, nonnegative raw exponents, and the raw-window census relevant
   to weights summing to 22.
2. Starting from
   `D_n=sum_{i+j=n}((12-j)F_i'G_j+(i-8)F_iG_j')`, enumerate the COMPLETE
   coefficient of X^0 at n=22 directly from literal slots. Account for the
   derivative degree factor. Verify exactly
   `D22[X0]=F11[X1]G11[X0]-F7[X0]G15[X1]`.
3. Explicitly audit apparent neighbors: (10,12) is killed by 12-j=0 and
   (8,14) by i-8=0; prove all remaining pairs lack the required X0/X1
   slots. Check signs and ordering independently rather than copying the
   target list.
4. Verify the raw-slot identifications
   `F11[X1]=f_1_0=P_x(0)`, `F7[X0]=f_0_1=P_y(0)`,
   `G15[X1]=g_1_0=Q_x(0)`, `G11[X0]=g_0_1=Q_y(0)` and hence the expression
   is literally `P_x Q_y-P_y Q_x=J(P,Q)(0)`. Confirm the chart/endpoint
   convention gives target +1, not -1.
5. Audit parity: total raw degree is base+4i-w and therefore congruent to
   w mod 2. If every ODD RAW WEIGHT coefficient is zero, prove P,Q have
   only even-total-degree monomials, are invariant under simultaneous sign
   reversal, and have zero gradients at the origin. Then D22[X0]=0, so the
   target D22=1 is impossible.
6. Draw the firewall carefully. Vanishing of all odd de Rham q-gates alone
   does not automatically mean all odd raw-weight coefficients vanish.
   Decide whether the report ever asserts that converse; if its wording is
   ambiguous, require a precision repair. The theorem concerns the raw
   all-odd-weight-zero section and does not by itself prove the q5--q15
   fiber intersection empty, endpoint exclusion, Keller, or JC2.
7. Include mutations detecting: a sign flip; retaining either structural
   zero neighbor; omitting a true term; wrong slot/weight mapping; and a
   parity or endpoint-target sign error. Verify frozen hashes at start/end.

Create:

- `xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_origin_odd_coupling_hostile_review_fable5_20260828/`
  with README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256.

Give explicit PASS/REPAIR/FAIL; name the exact first defect if any. Make the
checker standalone, deterministic, standard-library only, run it with
`PYTHONDONTWRITEBYTECODE=1 python3 -B`, use repo-root-relative manifests,
hash final bytes, and return paths/hashes/output. Proceed directly.
