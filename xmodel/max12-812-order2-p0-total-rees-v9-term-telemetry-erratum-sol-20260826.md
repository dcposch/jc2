# Erratum: V9 coefficient-term telemetry

Date: 2026-08-26

Status: **DISPLAY-ONLY CORRECTION; NO COEFFICIENT OR THEOREM CHANGES.**

The frozen V9 validator computed a nonzero polynomial's displayed term count
as

```python
value.count("+") + value.count("-") + 1
```

so a leading minus sign was incorrectly counted as a separator.  Exactly 14
of the 42 exact-Q coefficient files are affected:

```text
Fg11_1 Fg11_2 Fg11_3 Fg11_4 Fg11_5
Fg12_1 Fg12_2 Fg12_4 Fg12_5 Fg12_7
Tg10_5 Tg11_5 Tg12_4 Tg12_5
```

For each listed file the recorded telemetry is one larger than the actual
monomial count.  In particular, the V17 bridge coefficients have actual
counts `5,18,58`, not `6,19,59`.  Every affected file and only an affected
file begins with `-`; the file bytes, SHA-256 manifests, Singular polynomial
sizes, bridge equalities, saturation certificates, and downstream results are
unchanged.

The historical validator and evidence remain immutable.  Future consumers
must parse polynomial syntax or ignore one initial sign before separator
counting.  This correction was independently identified in both V17 hostile
reviews, SHAs `b4540858...` and `f0d8a9cd...`.
