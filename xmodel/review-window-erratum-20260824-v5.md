# Erratum v5 — additional self-reported review windows

Date: 2026-08-24
Status: **FROZEN CUMULATIVE METADATA CORRECTION**

This successor preserves the byte-frozen corrections in
`xmodel/review-window-erratum-20260824.md` and cumulative successors `-v2`
through `-v4`. The two Grok reports below self-reported approximate UTC
windows that differ from the timestamps written automatically by
`ops/lane.sh`. Runner timestamps are authoritative; the review reports and
run records remain byte-frozen. No mathematical verdict changes.

| review | frozen report SHA-256 | frozen run SHA-256 | report says | authoritative runner window |
|---|---|---|---|---|
| `gcd3-69-cube-trajectory-kuranishi-review-grok-20260824` | `7bcf18d69344acc2277a0184ca1aeeb717ebad35c3aacf91421874b7e59f5cc9` | `59c4eb36352c2d024737510ee3c50d651b26f1d95c54c6a2a92e0729f6297a0c` | `16:37:55--16:48:09Z` | `16:31:04--16:51:58Z` |
| `as-fonly-p3-d7-depth6-triangular-terminal-review-grok-20260824` | `75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318` | `b000acdc7b55328968efe8a90cd23c3528854522ca25adfcc3920df7402fbb11` | `17:14:46--17:25:36Z` | `17:10:40--17:28:51Z` |
| `as-fonly-p3-balanced-cyclotomic-terminal-family-review-grok-20260824` | `d4803d27735b815cfb0ef3c8120def1a935912ef9427acb0c9b05d00d3d4b1dd` | `b18394680dd748c28b5ee0646962b6b3bd0aa6d624c60c5381a841bff188bcfd` | `17:36:57--17:44:52Z` | `17:33:18--17:48:41Z` |
| `as-fonly-p3-d7-associated-top-components-review-grok-20260824` | `7593a9a822c07a3d5daf67b30c46028f0ba84b7978c038d7ec1bc6af62168f8a` | `6e6bbd480a3da9fe0ad61c98b367022866e843a394c0bcb08deea1c65caaf813` | `17:30:56--17:46:57Z` | `17:30:56--17:50:36Z` |

All four additional runner records have exit code zero, `final_status=DONE`, and
matching embedded report hashes. The frozen v1--v4 files plus this successor
jointly cover 44 reports. No input hash, computation, source audit, verdict,
or scope statement is affected.
