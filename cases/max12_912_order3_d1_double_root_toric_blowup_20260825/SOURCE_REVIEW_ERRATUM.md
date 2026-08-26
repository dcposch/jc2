# Hostile source-review erratum

The report

```text
c31cb5f1b42080bc9d9975f74669246c436d0ad9db34de98d3a4037287ce9eb7  xmodel/max12-912-order3-d1-double-root-toric-blowup-source-review-grok-20260825.md
```

is useful only for its audit of the displayed compiler/source equations and
scheme encodings.  Two parts are quarantined:

1. Its claimed re-proof that only `alpha=2 beta` survives omits higher
   coefficients of an earlier polynomial `QR/K` layer.  The exact correction
   controls in the mandatory scope erratum disprove that fan-completeness
   claim.
2. The report states that it ran substantive sparse reconstruction with host
   CPython on Darwin.  That violates the campaign's absolute AWS-only compute
   policy.  No computational claim from that local replay is evidence-grade.

The report does not invalidate the frozen tied-chart compiler: those equations
were independently compiled on AWS and remain correct under
`SCOPE_ERRATUM.md`.  It cannot be cited for whole-fan coverage.
