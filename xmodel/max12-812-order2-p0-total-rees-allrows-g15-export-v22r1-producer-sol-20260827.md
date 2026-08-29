# Producer report: actual-total all-row grade-15 export V22R1

Producer: Sol Ultra

Date: 2026-08-27

Status: **DUAL-AWS PRODUCER PASS; DIFFERENT-MODEL REVIEW PENDING.**

## Result

The repaired V22R1 export produced all seven full literal grade-15
coefficients of the frozen 569-tail actual-total source model.  Both capped
AWS lanes passed the full frozen chain, and a separate restricted-AST
post-harvest verifier matched every exact-Q coefficient to its reduction in
the characteristic-65521 serialization.

```text
row                         1    2    3    4    5    6    7
grade-15 term count       133  224  355  140  585  200  759
contributing frozen tails  35   50   55   72   83  104  119
```

Exact-Q coefficient SHA-256 values:

```text
Tg15_1  4d237049cdd6fbaf05a14dcda0710fdb1660058241b0b3a72e1c0c473e7a40ba
Tg15_2  5a438032b3d558131246d3022006b68cc424f4c09bfcef0215e8ce8ea76e0e69
Tg15_3  53d513df5003c5b0e60a50aff59779d9c921374e8878dea8e7ba9f3152d294d4
Tg15_4  2cf0b1d34df224ba0df2b60bdd7b8144fd733d35133edd851c91d27a9b830748
Tg15_5  26e2f4ef586955dddd1d694343f1bf29f28f050e4da61f386b2e11fb44a08f08
Tg15_6  786c6bb976305614cc0945b2ebf0d78600fb9a96aefa1553248ff8f473b5c51e
Tg15_7  1b3eb2ae0963ee0044a209d91f8dc3ca9ef4d11c3dd47633d799219449bfcddd
```

Every coefficient is nonzero, rho-even, and homogeneous of literal
sigma-weight 15.  No exact-Q term disappears modulo 65521.  The independent
byte parser found coefficientwise Q-to-F_65521 agreement in all seven files.

## Historical and section bridges

All 35 historical grade-10--14 coefficients passed exact polynomial equality
against the frozen V9 and V20 exports in ordinary Singular in both rings.
The grade-15 named-point residuals are exactly:

```text
CS0: all seven rows zero
Z00: all seven rows zero
A00: Tg15_6 = -1/16; every other row zero
A10: Tg15_3 = -1/16
     Tg15_5 = -(3/32) rho^2
     Tg15_7 = -(3/128) rho^4
     every other row zero
```

These agree with the independently reviewed, untruncated V21 section
calculation.  Thus grade 15 is the first source grade breaking each pure
`J2=(a0,a1)` direction `A00` and `A10`.  The same finite source never breaks
`CS0` or `Z00` at any depth; that persistence is a V21 theorem, not an
inference from this finite export.

## V1 failure and exact repair

The original V22 jobs were rejected before any grade-15 output was accepted.
V1 demanded byte-identical historical polynomial text and encountered the
same polynomial with different term/factor order.  The quarantine record is

```text
cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/
  V22_V1_SERIALIZATION_BRIDGE_ERRATUM.md
SHA-256 caf6261223c8b196d43806112d4d3534e05269c5911a60f92e74921095015d13
```

R1 pins and imports the entire V1 exporter at SHA-256
`c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6`.
It defers only failures tagged exactly `old coefficient byte bridge`, records
their distinct `(grade,row)` labels, and leaves every other failure fatal.
Nineteen historical serializations differ; the generated ordinary-Singular
script nevertheless requires all 35 semantic equalities before PASS.

## Custody

The complete custody record is

```text
cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/HARVEST_CUSTODY.md
```

Key hashes:

```text
R1 freeze manifest                    f58db2ff91c83bf3b52357889bb91d01f90dde2770eb0516fc89937f9db6ffb2
shared source archive                 4f56f8cf355c54195e452d43826f5693a1e22e1ff6b03d679e2fbfb43a24f54e
Q RESULT.json                         829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8
F_65521 RESULT.json                   04c777e97b9113da9848c2c47fcfb3d880cc7b11319b74a0030dcc92aa92c94c
Q EVIDENCE.sha256                     f213026a454c8f3171c0ce3c8b6cdfb6fe1a22e663caec08d47d08666309def9
F_65521 EVIDENCE.sha256               7e862a38d91ee12913ab35af62ab1ed229f3335a2a375604b03e5ab47dc64d40
independent verifier                  08b4cbabd1260b6c1b7c5b3999908eab3235c5a7114e451614309d62b08794d4
independent verification result       4a0b1f81a8b74b066b157487f238d01c935a7a1a703b42720a7b3b8898929d85
```

Every 24-entry evidence manifest rehashed fully after remote-to-local path
remapping, and each harvested root contains no unlisted file other than the
manifest itself.  The two AWS runs used distinct hosts and pids.  The two
compiler lanes are independent executions of the same exact-`Fraction`
reconstruction with different serializations, not independent derivations;
the separate restricted-AST verifier supplies the coefficientwise modular
comparison.

## Interpretation and next experiment

The useful new input is not merely that `A00` and `A10` die, but the typed
cubic leading pattern visible in the full rows: row 6 detects the `a0`
direction and rows 3, 5, 7 detect the `a1` direction with successive even-rho
weights.  Once hostile review passes, these seven polynomials should feed a
typed stage-two chart search immediately; broader geometric review need not
block that provisional successor.

The result does not empty either `J2` chart and does not establish any
exceptional-power containment.  It is an export of a frozen finite source,
not a proof of completeness of all Rees equations or extension/nonextension
of a formal arc.  It proves nothing directly about Gate T, order two, maximum
twelve, or JC2.
