# Erratum v3 — additional self-reported review windows

Date: 2026-08-24
Status: **FROZEN CUMULATIVE METADATA CORRECTION**

This successor preserves the byte-frozen corrections in
`xmodel/review-window-erratum-20260824.md` and
`xmodel/review-window-erratum-20260824-v2.md`. The additional Grok reports
below self-reported approximate UTC windows that differ from the timestamps
written automatically by `ops/lane.sh`. Runner timestamps are authoritative;
the review reports and run records remain byte-frozen. No mathematical
verdict changes.

| review | frozen report SHA-256 | frozen run SHA-256 | report says | authoritative runner window |
|---|---|---|---|---|
| `gcd3-69-lower-pfaffian-successor-review-grok-20260824` | `a000619d8b5597add21716d525856c459ff57d5a2b2ab75b85de5d9d08970b27` | `a8a24c402b26adb07fa009e28373c06dffaab4df3bf74ef711bce6d063fce95d` | `14:21:13--14:38:03Z` | `14:21:13--14:41:34Z` |
| `gcd3-69-target-translation-erratum-review-grok-20260824` | `f4cb57ca765138ed2decab01b12a7f884c37f9a847d80e90162ee751bb3df837` | `2c51716b0de1d85c81c1cec9d0e459b3feabdbde18d084cc6881ca0e60bbd45a` | `14:33:17--14:40:00Z` | `14:29:35--14:40:58Z` |
| `as-gauge-growth-p3-depth4-review-grok-20260824` | `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919` | `d2bc61b24fbd197199dc01ae95a7e739030595b118652d59300916ab2ab215c6` | `14:57:21--15:08:10Z` | `14:53:27--15:08:29Z` |
| `gcd3-69-cube-mismatch-review-grok-20260824` | `2648eef3b8091970655a94743c6c181343a94534b6454f43c579b310331ba7d7` | `58719ca5f35c24bb5238ec1bff4545a9aafd8e0809dfe44a5aaed4a40adf5028` | `14:50:47--15:13:05Z` | `14:50:47--15:16:40Z` |
| `td6-jet-orbit-adjoint-review-grok-20260824` | `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` | `f59673dfe9ce99924cc263dc7c437d4b8e0bdd4d5ebb64f6b44d0a74037f840f` | `14:56:08--15:29:41Z` | `14:56:08--15:32:31Z` |

All five additional runner records have exit code zero,
`final_status=DONE`, and matching embedded report hashes. The frozen v1 and
v2 files plus this successor jointly cover 36 reports. No input hash,
computation, source audit, verdict, or scope statement is affected.
