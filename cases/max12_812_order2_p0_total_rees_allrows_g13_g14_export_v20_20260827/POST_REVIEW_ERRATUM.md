# V20 post-review evidence erratum

Date: 2026-08-27

The Opus5 hostile review independently reproduced every exported polynomial
and found no incorrect numerical or mathematical output, but it identified
five repairs to the producer narrative and evidence architecture.

1. The two AWS compiler lanes are distinct executions of one exact-Q
   `Fraction` reconstruction with characteristic-dependent serialization and
   Singular rings.  They are not independent algebraic derivations.
2. The four `V20_SECTION_*_NONZERO=0` messages in generated Singular are
   unguarded echoes.  The exact section values were independently recomputed
   by the hostile review and later by the separately reviewed untruncated V21
   replay, so the conclusions stand; the original engine flags carry no
   evidentiary weight.
3. `HARVEST_CUSTODY.md` and the producer report refer to a separate
   restricted-AST replay but preserve no script, log, or hash for it.  The
   asserted counters `V20_INDEPENDENT_Q_TO_F65521_MATCH=14` and
   `V20_INDEPENDENT_QRHO_ZERO_SECTION_CHECKS=56` are retracted as custody
   evidence.  The hostile review independently supplies both checks.
4. The inference that no named section breaks below grade 15 also needed
   grades 0--9, which V20 did not test.  Opus5 independently reconstructed all
   rows through grade 14 and found grades 0--9 identically zero.  V21 then
   proved the stronger all-depth section theorem directly.
5. In the characteristic-65521 lane, `coefficient_term_counts` is inherited
   from the exact-Q sparse polynomial rather than recomputed after modular
   reduction.  This latent defect is untriggered here: the hostile review
   verified that no coefficient disappears modulo 65521 and that all fourteen
   supports and term counts agree.  Future exporters must independently count
   the serialized modular support.

Authoritative review:

```text
xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-v20-hostile-review-opus5-20260827.md
SHA-256 8665e43cd9df2b6c55aeccde72daa10ddff4768813df045feeb97cb593264bf5
Verdict CONFIRMED WITH REPAIRS
```

The immutable producer and custody reports are retained as historical inputs;
this file supersedes the five claims above.  The full grade-13/14 polynomial
exports, hashes, nonzeroness, rho parity, historical bridges, and exact named
section values are unchanged.
