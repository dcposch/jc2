# Result: `sat()` list coercion preserves the full ideal

AWS r6d completed the frozen probe with rc 0, empty CAS stderr, and
`PASS_SAT_RETURN_TYPE_PROBE`.

In both the exact `dp` ring and the exact A-fast block-order ring
`(lp(1),dp(8))`:

- direct `sat(I,J)` has type `ideal` and two generators;
- `list L=sat(I,J)` has size one;
- `L[1]` has type `ideal` and contains both generators;
- the direct ideal and `L[1]` reduce to zero against one another generator by
  generator.

Separately, `sat_with_exp(I,J)` has type `list`, size two, with an ideal in
entry 1 and an integer exponent in entry 2.

Therefore the earlier diagnosis of first-generator truncation was wrong for
the installed Singular/elim.lib version.  The list wrapper is a documentation
type mismatch, but it is semantically harmless here.  The A-fast `(1)` versus
inverse-B nonunit-special-fibre discrepancy must have another cause.  No other
claim is quarantined merely because it uses `list L=sat(...); L[1]`.

Custody:

- input SHA-256: `b1ac23c8d3e6bb86009c751978ff65b4861e1e39a0954bfdfaf59a0ebf7a6a26`
- stdout SHA-256: `d61dd1d541b8def2c9ade6f9ee82a38551cbc7b184d3b7ea17a34a1d633bfe60`
- stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- job tag:
  `max12_912_order3_d1_sat_return_type_probe_20260826T011921Z_r6d`

This is a software/API control, not a D1 mathematical endpoint.
