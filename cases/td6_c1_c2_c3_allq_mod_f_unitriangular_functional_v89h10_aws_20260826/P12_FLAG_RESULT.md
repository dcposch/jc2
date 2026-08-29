# TD6 V89H11 all-q literal-P12 flag-functional result

Date: 2026-08-26

Verdict: **PASS as an exact producer-tier quotient-functional theorem.**

In the frozen V89H10T `F=0` scope on `D(U*H*B3)`, retain all 22
independent, untruncated q coordinates

```text
q2,...,q14,q16,...,q24
```

with q15 absent only under the reviewed target shear.  The replay rebuilds
literal P12 and all 38 literal FIRST rows, reconstructs the frozen common
flag, and solves the affine FIRST equations at zero nonpivot parameters by
strict-upper back-substitution.  The exact pivot solution has 37 nonzero
entries, 219 q terms, and total q degree one.  Direct substitution in the
original 38-by-38 FIRST coefficient matrix recovers the original right-hand
side exactly.

Evaluating literal P12 at that solution gives the empty-parameter
coefficient of its unique original-FIRST normal form.  The complete result
is unexpectedly small: it has total q degree one, no mixed q terms, and
support exactly

```text
(), q3, q4, ..., q14.
```

Thus this one quotient functional is independent of q2 and q16,...,q24.
Its full 13-term artifact has SHA
`530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8`.
The pure-q14 E3-coordinate-0 coefficient equals the promoted V89H7 value
exactly and is nonzero.  On specialization `q2=...=q13=0`, the complete
positive support is exactly pure q14, also matching the V89H7 scope.

The denominator firewall is fail-closed.  Up to units the two common
denominators are

```text
pivot solution:             U^7 V^4 (V^2-4U^3)^2
empty-parameter functional: U^5 V^4 (V^2-4U^3)^2.
```

No factor outside the registered `D(U*H*B3)` radical occurs.  Both R1 AWS
runs returned rc 0 with byte-identical stdout and every mathematical
artifact.  V1 stopped during module initialization because of a one-line
attribute-path error and computed no algebra; it is deployment-negative
only.

Custody:

- R1 source archive SHA `51575970a5d7ba2cc6056a0a70ecd744d88d571bd9c2995f1a65ba38fdc4f0fa`.
- `SOURCE_P12_FLAG.sha256` SHA `ac37d22986ab4257f95c50eef593865ef90b603cda97886ffe6fda500390eba8`.
- R1 client SHA `8b87985d2071c40b295e280fce94a6465826dd06478089adca34e70df123fcba`.
- Byte-identical stdout SHA `5b8bd72496314e97bc80296fdefa07703021bfa40f59ea9040221dc3f2eceeda`.
- Pivot solution SHA `ea9537bef63e65241978b82b8e08f0653b21751508194725cc9494b798a571a9`.
- Full functional SHA `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8`.
- Functional denominator ledger SHA `b4113c145223061669954852fcfa7e5a5a8392fa070135c79e6ee0624c4d9151`.
- Result artifact SHA `591d6ac5ffe86ffd11a2aea99f94814f4c4ae5cf64a489709e6a99314b132101`.

This theorem computes only the empty-parameter coefficient, not the full
normal form in the remaining free jet parameters.  It does not prove a unit
ideal or source-point exclusion, cover a unit-q chart, license q15 as a
source coordinate, supply a total-Rees map, close TD6, or resolve JC2.  All
substantive computation ran on AWS; `jc2-lean` was not touched.
