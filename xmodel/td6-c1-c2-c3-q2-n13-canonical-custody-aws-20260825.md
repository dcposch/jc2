# TD6 generic-center staged N13: canonical duplicate AWS replay

Verdict: **exact duplicate custody PASS, localization debt preserved**.

The V47 producer was run independently on r6d and Box03 from source archive
SHA-256
`2466aca804cb1ef6a0deaad55d646796878ac311265cc9e8898bbb665a886fa3`.
Both runs returned rc zero.  Their mathematical stdout is byte-identical,
SHA-256
`0549ce7be47ba6c0bbb8dca95a930b4da571e1f1ddff5bcad348319c299aa75f`;
the timing stderr SHAs are respectively `5f9da042...` and `b8bac432...`.

The exact replay confirms:

- transport rank `3470/3602`, first rank `38/132`, previous/pole rank
  `38/94`, and current rank `25/56`;
- all current compatibility rows replay against their stage-original rows;
- the target compatibility is exactly `N13=(k/25) beta`, not its negative;
- the full-stage common denominator has degree 731 and 29,782 terms, with
  canonical polynomial SHA `4fa9cae7e7a22cc35b49901e3c267bcfc507b1fafc98ada4ade4de755ab0810d`;
- `raw_substrata_from_emitted_denominators_still_charged=true` and every
  family/global conclusion flag remains false.

This result supersedes only the process-address-contaminated certificate
digests of the earlier reporter.  It does not remove any denominator factor
or repair the cross-stage localization gap identified in
`td6-c1-c2-c3-q2-n13-localization-scope-erratum-20260825.md`.  The active V48
successor composes the entire staged N13 ancestry into the genuine-P12 source
identity and emits its actual post-cancellation denominators.
