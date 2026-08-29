# V1 to v2 supersession record

V1 remains frozen at
`cases/d43_exact_sparse_rows_20260828/SOURCE.sha256`, whose digest is
`9b851ede56986fe3154cf962f336fda6185fb7a4a00d07888c93e9b78a06848d`.
It is retained as historical evidence and must not be launched.

The decisive v1 defect was coefficient scope: its selector used independent
HW1/HW2 and EB generators.  V2 performs the literal a00pp collapse before
expensive multiplication and eliminates EB through the exact B block.  V2
also replaces the two-manifest continuation with one immutable conditional
pipeline and corrects the displayed E5/E6 projection to E plus one W-product
unit equation with mandatory literal reconstruction replay.

The original preflight report, checker, and tests are historical v1 files.
Their old sidecar was stale after an earlier explicitly recorded revision;
the sidecar is resealed to their current bytes.  The corrected campaign
preflight is separately versioned as
`xmodel/d43-direct-exact-sparse-source-preflight-gpt56-20260828-v2.md` with
`cases/d43_exact_sparse_source_preflight_v2.py` and its v2 test.  No v1
claim is silently promoted.
