# Erratum — maximum-12 degree scope in the 17:40Z synthesis

Date: 2026-08-26T23:01Z

The final paragraph of
`xmodel/ideation-significant-news-20260826T1740Z-root-synthesis.md` says that
the maximum-12 computations are method controls because of the classical
total-degree cutoff.  That blanket statement is false.

The GGV/Heitmann condition constrains
`gcd(deg_total(P),deg_total(Q))`.  It closes scopes that explicitly fix or cap
both actual total degrees at twelve, but not the campaign's live partial-`y`
families `(8,12)` and `(9,12)` when coefficient-`x` and total degrees are
unbounded.  The deterministic frontier gate returns
`NOT_CLOSED_BY_THIS_GATE` for both unbounded-total partial-`y` registrations
and `METHOD_CONTROL_ONLY` for a common actual-total cap of twelve.

No scoped producer/review algebra is withdrawn.  Read the synthesis as
follows: fixed/capped total-degree specializations are controls; normalized
work in the unbounded-total partial-`y` frontier is potentially
frontier-relevant but still requires literal landing/coverage and its own
remaining leaf closures.  It is not thereby a maximum-12 theorem or JC2.

