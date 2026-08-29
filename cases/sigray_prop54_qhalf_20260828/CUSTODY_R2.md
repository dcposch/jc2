# Frozen custody — repaired Sigray Proposition 5.4, R2

Date: 2026-08-28

## Sealed R2 artifacts

```text
be9e4b747e02ba97a30b8d6254514f568dec8a197dcbbc4a49446ba5fdb38a9e  xmodel/sigray-prop54-qhalf-sol-ultra-20260828-r2.md
4d15680faf3301d9dfc645141c9fbc4a8ee7a4b5f0eb06ea3a74a9baf2ca77ac  cases/sigray_prop54_qhalf_20260828/verify_degree_pin_r2.py
```

The R2 checker is standard-library exact arithmetic only and passes **943**
assertions.  The frozen R1 checker independently passes **1,788** grouped
assertions:

```text
4c6164b9cf01a797ca6d1029e038f44d7e9f32b34e405c38ec53b2c2f2256bea  cases/sigray_prop54_qhalf_20260828/verify_qhalf.py
```

Replay:

```sh
python3 cases/sigray_prop54_qhalf_20260828/verify_qhalf.py
python3 cases/sigray_prop54_qhalf_20260828/verify_degree_pin_r2.py
```

## Frozen predecessor and hostile review

```text
f2ee74b5c8f07048488c3b78e5f76bc293beae4b7199614ce75b8e1c18165f75  xmodel/sigray-prop54-qhalf-sol-ultra-20260828.md
c3f0bfde24fb265e6ece9fce40089868fd64b01b3f6f5eac3ef0ee5df43e1f30  xmodel/sigray-prop54-qhalf-hostile-review-opus5-20260828-r1.md
```

The independent Opus 5 verdict was `REPAIR`: it confirmed the deck-projector
and kernel proof, the sharp `alpha=1` controls, and the direct consumers, but
found the printed Proposition 5.3(iv) linear/constant gap.  R2 incorporates
its degree-pin repair, with the branch coefficient sourced from Notation 3.8
rather than the inapplicable vertex-predecessor notation of Proposition 3.2.
The review's reproducible body digest is:

```text
e024d4117309ec7482e0b9ad74ba7ddee0622d497fbf9307cde592810ca6f102
```

Recompute it with:

```sh
sed '$d' xmodel/sigray-prop54-qhalf-hostile-review-opus5-20260828-r1.md | shasum -a 256
```

## Primary-source custody

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

Printed-page custody (PDF page number equals printed page number):

- p. 4, extraction line 5: Notation 1.1 makes the suppressed bracket scalar
  an unspecified element of `C*`.
- pp. 8--9, extraction lines 1--94: Lemma 2.1, Notation 2.4, and Statement
  2.1 give the normalized type, coprimality, and `alpha>=2`.
- p. 12, extraction lines 29--42: suitable denominators and Notation 3.8's
  one-grid-step operations.
- pp. 14--18, extraction lines 17--43, 72--104, 112--120, 207--210, and
  227--230: Proposition 3.1; Statement 3.9's polynomial-dependent hypothesis
  and multiplicity transport; Statement 3.10's monotone-decreasing order;
  Statement 3.16's vertex/deck form; and Statement 3.18's root condition.
- pp. 19--23, extraction lines 1--21, 70--97, 154--169, 223--240, and
  255--265: Proposition 4.2's first approximate-root relation and stopping
  data, Propositions 4.4--4.5's exponent comparison, and Proposition 4.6's
  bracket and exceptional degree branch.
- pp. 23--26, extraction lines 44--65, 102--149, and 152--185: Proposition
  5.1's threshold, the definition of `T_{a,pole}`, Proposition 5.3 (including
  its incomplete printed (iv)), Proposition 5.4, and Statement 5.2.

Reproducible extractions:

```sh
pdftotext -f 4 -l 4 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 8 -l 9 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 12 -l 12 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 14 -l 18 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 19 -l 23 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 23 -l 26 -layout refs/sigray_full.pdf - | nl -ba
```

No canonical ledger was edited for this package.  The checkers do not inspect
or modify `jc2-lean`, invoke a CAS, or substitute computation for the source
typing proof.
