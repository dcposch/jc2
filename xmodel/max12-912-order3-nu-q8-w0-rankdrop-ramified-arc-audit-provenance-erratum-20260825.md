# Provenance erratum — Q8 rank-drop ramified-arc audit

The immutable report
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-claude-20260825.md`
(SHA-256
`01891db1277f0d8f79e694696e117c44f7ea1dfecd705373e457626e0cb75330`)
was produced by **Grok**, not Claude.  Its filename and the `Auditor:` field in
its header are stale labels inherited from the original Claude-targeted run.

The Claude adapter failed immediately because its monthly API quota was
exhausted; it produced no audit report.  The same frozen prompt (SHA-256
`1184a0196f6cf364cf753201cca602b90adc3812569af7c752e60dfd784f082d`)
was then rerouted to Grok, which wrote the immutable report above and returned
the verdict `NOT_CONFIRMED`.

This erratum corrects provenance only.  It does not alter the report's
mathematics or verdict.  In particular, the report's narrow conclusions remain:
generic slope two is excluded; a selected slope-two leading cone survives at
`b=1`; and the residual `-108` excludes only the frozen `x5=t` continuation,
not arbitrary ramified or mixed-order Puiseux arcs.
