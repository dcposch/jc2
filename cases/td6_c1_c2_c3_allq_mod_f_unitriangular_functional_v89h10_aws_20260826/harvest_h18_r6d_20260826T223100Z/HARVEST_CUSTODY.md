# H18 r6d harvest custody

Lifecycle: harvested producer output only; no mathematical promotion.

- AWS instance: `i-07eeaf8ba6f0bc419` (`r6d`)
- Remote root: `/home/ubuntu/td6_v89h18_r6d_20260826T223100Z`
- Remote completion time: `2026-08-26T22:13:11Z`
- Exit code: `0`
- Frozen source archive SHA-256: `a5b6f7306e4f1df434c53149d10d504332ca7266487cf0f854a83171ffc3d317`
- Output TSV SHA-256: `c5d136d942177882424a75a47c631fbd386d7fff6dbb09187effd32f1be4687f`
- Result SHA-256: `9df97904ea47f484494abf544bdf1dafbfeb9fe9352e88f4c3447c2599e185d4`
- Standard output SHA-256: `bc5defb2ca6fa239fd24d35cb7f104006764363a9685125b2eca0032b7bf2519`
- Resource log SHA-256: `293bfb447f98f3b190def5b858a1935340975e33fb2ea6b2e015400cc66bfabf`
- Peak RSS: `16844 KiB`; elapsed: `0.05 s`; swaps: `0`

The source manifest passed all six entries before execution. The immutable
remote root was read and copied without modification.

The H15 predecessor's phrase “238 nonzero scalar-coordinate terms” is
superseded by `P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md`: there are 238
vector records and 535 nonzero scalar entries. Coordinate 12 still has exactly
one nonzero record, so this correction does not alter the H18 output.
