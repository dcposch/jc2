# Erratum — model-evaluation freeze maximum-12 scope

Date: 2026-08-26T23:01Z

Item 7 of `xmodel/ideation-20260826T2230Z-model-eval-freeze.md` incorrectly
classifies all maximum-12 work as method control under the classical
total-degree cutoff.  The correct split is:

- explicitly fixed/capped actual-total-degree-at-most-12 scopes are
  `METHOD_CONTROL_ONLY`;
- the historical `max12` partial-`y` `(8,12)` and `(9,12)` families with
  unbounded coefficient-`x`/total degree are
  `NOT_CLOSED_BY_THIS_GATE`.

Both blinded models independently detected this bad packet premise, so the
error is retained as an evaluation finding rather than silently changing the
sealed inputs.  Their local-route rankings are navigation only and must be
reconciled against this erratum before allocation.  Their detection of the
premise remains scoreable.

