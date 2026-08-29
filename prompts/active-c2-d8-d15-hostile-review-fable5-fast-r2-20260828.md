You are Fable 5. Produce a compact independent hostile review of one exact
algebra result in `/Users/dc/code/math/jc2`. Do not enter/list/search/read/
build/status/modify `jc2-lean`. Preserve all existing files. Use only light
standard-library exact Python; no CAS or local parallel/heavy computation.

Frozen target:

- authoritative recurrence
  `cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py`
  SHA `fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119`;
- report
  `xmodel/ggv-upper-endpoint-active-c2-d8-d13-independent-audit-extension-20260828.md`
  SHA `da189b7fa2ce12656dfbd965c2ed76a0f26b90255a4c99e0fa1322d0c98d5577`;
- producer checker
  `cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py`
  SHA `112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26`;
- original charged report/checker SHAs `e3b777f851dcb49c1a2caeafa3048fd20771319ecd9f74e8ca74321602b4d1f6`
  and `00111feefcddd0532aa70204b69d90e5943b3e08b5ef7d97b44fcfa62f5b0372`.

Act now rather than drafting a plan. Build a NEW self-contained exact checker
that does not import producer code. Implement sparse Laurent/polynomial
arithmetic and `F*y'=a*F'*y`; register all c2,c4,...,c20 modes through D15.
Independently check these load-bearing statements:

1. On V0=AS,T=AU, K=64F4-Z^2: deepest D8 is
   `3K^2/(32768A^2)`; K=AR leaves complete D8 pole
   `-5c2(S^2-2Z)^3/(65536A)`. On c2!=0 lift H=AQ.
2. For D=R-4SU, P=256F5-RS+2S^2U: complete D9 is
   `3DP/(65536A)` and deepest D10 is
   `3P(P-2SD)/(524288A^2)`, forcing A|P rootwise.
3. With P=AP1, verify residual D10 and deepest D11 exactly as displayed in
   the target report. Explicitly confirm or refute: A|D by itself clears
   `D*B11/A^2`. (Expected repair: it generally leaves a simple pole; exact
   polynomial equation D=0 is the branch actually extended.)
4. On exact D=0 verify COMPLETE D11 negative part
   `N11/(4194304A)` and deepest D12
   `(3E^2-2S*N11)/(33554432A^2)` with the report's E,L,M,N11. Audit that at
   characteristic-zero field points these force A|E and A|L when c2!=0.
5. After E=Ae1,L=Aell verify all D11 poles vanish, complete residual D12
   `J(20c2J+3N)/(8388608A)`, and D13 A^-2 class equal `-S/4` times that
   numerator over A^2. Retain c6 and all predecessor/born modes.
6. Rebuild the exact A=X^4-1 fixture literally. Verify characteristic
   polynomiality, raw D0..D15=0, every legal F/G window, G12=4093/268435456,
   G13=G14=G15=0, and uniqueness of
   `c14=-6139/17179869184` under frozen remaining data. Check the point is
   non-q1 by solving V0=A'R0+2AR0', deg R0<=4.
7. Separately at c2=0 verify complete D9/D10 formulas with H,D,P0 and the
   field-rootwise conclusion A|P0 and H*D^2=0. Do not use the active H-lift.
8. Add mutations catching a wrong D8 term, A|D versus D=0, dropped c6,
   wrong c14/F7, and an omitted born/predecessor mode.

Give explicit PASS/REPAIR/FAIL. Distinguish exact identities, field/radical
necessities, and the one literal point. No scheme, endpoint, branch-P,
Keller, counterexample, or JC2 overclaim.

Use distinct latency-hedge outputs (do not touch any other review outputs):

- `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-fast-r2-20260828.md`
- `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-fast-r2-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_active_c2_d8_d15_hostile_review_fable5_fast_r2_20260828/`
  with README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256.

Run checker with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, finalize hashes and
manifests, recheck frozen hashes, and return verdict/paths/hashes/output. Keep
the report concise. Start tool construction promptly so partial progress is
durable if a later model request times out.
