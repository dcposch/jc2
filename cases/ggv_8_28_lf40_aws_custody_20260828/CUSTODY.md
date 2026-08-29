# LF40 exact AWS terminal custody

This standalone namespace preserves the terminal Box02 exact-`Q` `std/dp`
cross-check without changing the frozen LF40 producer source case.

## Box02 target-fix R1 `std/dp`

- Tag:
  `ggv_8_28_lf40_targetfix_r1_std_dp_20260827T212404Z_box02`.
- Audited host: Box02, `i-010201a5da47795c4`, `x2idn.32xlarge`.
- Start/end: `2026-08-27T21:24:42Z` / `2026-08-28T03:14:48Z`.
- Exact presentation: 409 variables, 740 target generators, and one
  Rabinowitsch equation; field `QQ`, `std` algorithm, `dp` order, one worker.
- Caps: 943718400 KiB virtual memory, 21600-second outer timeout,
  21000-second solver timeout, and nice level 5.  `/usr/bin/time` records
  4,495,208 KiB maximum RSS, zero swaps, and 5:50:00 elapsed solver wall.
- Source freeze SHA-256:
  `336a5295394dc3d84aebf268e720ac4ec0b7906a282f9ac527cff3b33e80992f`;
  source archive SHA-256:
  `a5fc34dca5898c6e2d4c990f541ce3ddef4f3d90cd2e524ecdc283b0b5773b65`;
  exact accelerated program SHA-256:
  `7256fcaddcdc2875ca6c31b2033f0e6950a598b8a22d3cc338c92069a89f21a5`.
- Literal solver stdout ends after the field/census and synthetic-control
  banners, `LF40_STAGE_ROW_0_BEGIN`, `LF40_CUMULATIVE_TARGET_GENERATORS=0`,
  the syntax/empty-ideal display `1`, `LF40_STAGE_ROW_0_END`, a blank line,
  and wrapper `halt 1`.  The displayed `1` is not a unit-ideal verdict.
- Terminal state: solver exit 124; validator exit zero with literal
  `RESOURCE_CAP_NO_VERDICT`; `RESULT.json` records `completed_rows=[]` and
  `producer_result_not_promoted_evidence=true`.
- Remote evidence-manifest SHA-256:
  `32aecd8e7fd21d9bb50744a228b558ea2b2f242f05b6907e8c1983fa17748a43`.
  Its 31 entries verified remotely and again after transfer.  This custody
  directory contains those 31 files plus the manifest itself.

The lane produced no LF40 conclusion and is not promotable evidence.
