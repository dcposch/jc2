# Erratum v4 — additional self-reported review windows

Date: 2026-08-24
Status: **FROZEN CUMULATIVE METADATA CORRECTION**

This successor preserves the byte-frozen corrections in
`xmodel/review-window-erratum-20260824.md`,
`xmodel/review-window-erratum-20260824-v2.md`, and
`xmodel/review-window-erratum-20260824-v3.md`. The additional Grok reports
below self-reported approximate UTC windows that differ from the timestamps
written automatically by `ops/lane.sh`. Runner timestamps are authoritative;
the review reports and run records remain byte-frozen. No mathematical
verdict changes.

| review | frozen report SHA-256 | frozen run SHA-256 | report says | authoritative runner window |
|---|---|---|---|---|
| `td6-boundary-qb-pencil-review-grok-20260824` | `5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319` | `2e0761fb51b19eeef9866610da601792b59152bb70a3271de92ff44c5ac739e6` | `15:43:37--15:59:52Z` | `15:38:55--16:03:20Z` |
| `as-gauge-growth-p3-depth5-d8-survivor-review-grok-20260824` | `2c3f961a5f0e537abef82db9243723289864d3ae901179adedaa554617d975c7` | `af5c661e6c95a5e82d2125f84f595c27b991a268df39464dd29d6abecc16d5f1` | `15:54:37--16:02:00Z` | `15:49:44--16:02:45Z` |
| `as-gauge-growth-p3-depth5-d7-minimum-review-grok-20260824` | `7006d82c4f6ff9943433bb4447bb95d3f94d6a76ea28ba1088bcc9aac774621f` | `5ca0628139381d6f92e1982e706ec36c11037e378d76e11da353b0eb8bc60d4b` | `16:06:41--16:12:16Z` | `16:02:42--16:15:06Z` |
| `as-gauge-growth-p3-depth6-cartier-d7-point-review-grok-20260824` | `99f703a8c97afde81ff41065c1f69e34b7739d321f2020ce54949ea144adf567` | `8c534278454a759f53dab1d2deba4a4958f3dc3ea338d11f808fe1cc235354bb` | `16:07:58--16:16:30Z` | `16:05:42--16:17:23Z` |

All four additional runner records have exit code zero,
`final_status=DONE`, and matching embedded report hashes. The frozen v1--v3
files plus this successor jointly cover 40 reports. No input hash,
computation, source audit, verdict, or scope statement is affected.
