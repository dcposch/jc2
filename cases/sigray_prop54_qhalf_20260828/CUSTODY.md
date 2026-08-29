# Frozen custody — Sigray Proposition 5.4 `q`-half repair

Frozen producer:

```text
f2ee74b5c8f07048488c3b78e5f76bc293beae4b7199614ce75b8e1c18165f75  xmodel/sigray-prop54-qhalf-sol-ultra-20260828.md
```

Frozen exact checker:

```text
4c6164b9cf01a797ca6d1029e038f44d7e9f32b34e405c38ec53b2c2f2256bea  cases/sigray_prop54_qhalf_20260828/verify_qhalf.py
```

Primary source:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

Printed page custody (PDF page number equals printed page number):

- pp. 8--9: Lemma 2.1, Notation 2.4, and Statement 2.1; in particular
  `k_f/k_g=alpha/beta`, coprimality, and `alpha!=1`, `beta!=1`;
- p. 15: Statement 3.9 and its explicit hypothesis that `kappa` is suitable
  **and has the property of Proposition 3.1**;
- p. 17: Statement 3.16, both the vertex/multiple-root equivalence and the
  `eta^l P(eta^nu)` pattern;
- p. 23: Proposition 4.6(11), the nonzero-scalar bracket
  `k p q'-l p'q \doteq p^mu`;
- pp. 25--26: Propositions 5.3--5.4 and Statement 5.2, including the
  squarefree/coprime pole patterns, omitted `q`-half, and downstream
  divisibility menu.

Reproducible extraction custody:

```sh
pdftotext -f 8 -l 9 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 15 -l 17 -layout refs/sigray_full.pdf - | nl -ba
pdftotext -f 23 -l 26 -layout refs/sigray_full.pdf - | nl -ba
```

Extraction-local locations:

- pp. 8--9 extraction: Notation 2.4 and Statement 2.1 are lines 86--94;
- pp. 15--17 extraction: Statement 3.9 is lines 15--51 and Statement 3.16
  is lines 150--153;
- pp. 23--26 extraction: Proposition 4.6(11) is lines 7--10;
  Proposition 5.3 is lines 108--149; Proposition 5.4 is lines 152--159;
  Statement 5.2 and its direct consumer proof are lines 169--185.

Supporting context frozen at production time (not primary authority):

```text
0b3ec6184b66f6c2307f36885bce86c213de9097fbfc912fccbeb3c94443ac99  ladder/SIGRAY-AUDIT.md
c043ab476de4d1dd99ee829a822b61cc9eea74843c86dd37e7c05569e11e8cb2  xmodel/ideation-20260828T1149Z-synthesis.md
```

The checker is standard-library exact arithmetic only.  It does not inspect
or modify `jc2-lean`, does not run a CAS, and is evidence for the stated
algebraic proof rather than a replacement for the primary-source typing.
