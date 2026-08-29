# TD6 V87R1 exact V87-to-V86 q2-specialization repair result

Date: 2026-08-26

Producer verdict: **PASS on Box02 and r6d.**  This result repairs the one
custody/proof gap charged by the independent V87 hostile review.  It is not a
new total-source or unit-q theorem.

## Exact comparison

The client rebuilt the live V87 literal degree-12 raw P12 source, all 38
packed raw FIRST sources, `h_F`, and the augmentation quotient `h_2` over the
untruncated 22-q polynomial ring.  It then set every q coordinate except q2
to zero and serialized the result in the frozen V86
`(parameter monomial, beta degree, exact E3 coefficient)` encoding.

All 39 source comparisons passed:

- each live V87 full source digest reproduced the frozen V87 inventory;
- the q2-only slice of P12 and every FIRST source reproduced the corresponding
  frozen V86 full-beta digest;
- the beta-zero digest of every slice reproduced the frozen V86 beta-zero
  digest.

The exact comparison table has 39 data rows plus its header and SHA-256

```text
e60173b3e8f224d6fab09f0ef3a831c846a27137718ba1d188d08b009453fae4.
```

## Quotient comparison

The client independently rebuilt the V87 total identity and residual before
extracting `h_F` and `h_2`.  The residual again had total q-degree one.  It
then specialized to q2, cleared both quotients by the same exact factor

```text
U*H = C*U-3*U^3,
```

and emitted the actual coefficient tables.  They are byte-identical to the
frozen reviewed V86 outputs:

| object | terms | scalar coordinates | SHA-256 |
|---|---:|---:|---|
| V87 q2-slice `h_F`, cleared | 2,797 | 50,346 | `89ecec18cea6547fe465fc4f6088f7f94ec9b6d717eefb33386f5b3fab6d49e0` |
| V87 q2-slice `h_2`, cleared | 3,330 | 59,940 | `590f88a20183a4d4363a4e14397084cae347838331abc6df536f60129f2f0384` |

The localized digests also reproduce the frozen V86 exact-result pins:

```text
h_F:    d42fd41927eaa8b89feb97ca5e78f23b21f267e07bbcc6cb1f0a8cf8ae9d6359
h_beta: ff283ad8cd4b8ba277459c168c5dbc74473cea7714be1473232681e7eaf928d8
```

No inverse of F, q2, or any q expression was taken.  Every cleared scalar
coefficient was required to be polynomial.

## Frozen dependency custody

The repair consumes the corrected V86 hostile review and promotion, rather
than an unreviewed producer banner:

```text
V86 corrected hostile review  9e70d6ceef3572cecada81160357684c8478fb8994cfe7d6176793d58ca1532e
V86 promotion                 677513a291a64f577740bfc8852a94d9ac1218bd5a21aac69d5ef4fcdb0c0260
V86 RESULT                    22fb1c6c437e26f212a38857157050f68e773dcee8482e3d384da47fffc09c02
V86 FREEZE                    82083dd26b44766779beb2fec64e34f0842769a8f81fe73aee1f105cb8510c79
V87 RESULT                    6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda
V87 FREEZE                    ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9
```

The exact-result record has SHA-256
`64147317dedd7c79a64e7ee95875c966e5f82c5e2232db721c876fa1c4d3749c`.

## Dual AWS custody

Both clients returned `rc=0` with the
`TD6-V87R1-EXACT-V87-TO-V86-Q2-SPECIALIZATION PASS` banner.  Mathematical
stdout and all four output files are byte-identical.  The common stdout hash
is `c0104ec08b10e9349ca4b4fa8267eb858785a4b5da45e7ac0a0e654be6f9d4f1`.

- Box02: 9:16.96 elapsed, 1,173,092 KiB maximum RSS, zero swap;
- r6d: 9:06.28 elapsed, 1,172,144 KiB maximum RSS, zero swap.

The nonempty stderr files are the expected `/usr/bin/time -v` resource
records; both report exit status zero.

## Consequence and firewall

This exact output-explicit comparison supplies the smallest repair requested
by `xmodel/td6-v87-total-f-allq-hostile-review-20260826.md`: the represented
V87 q2-only family and both quotient tables are exactly the promoted,
hostile-reviewed V86 total-`(F,q2)` family under a documented common
encoding.  A controlling addendum and a fresh hostile review must consume
this frozen package before V87 is promoted.

Nothing here supplies a unit-q chart, totalizes q15 (handled separately by
V88), or covers dead stretch, correction, orbit/pole, centering,
deck/torsion, other boundary data, a total-Rees chart, whole fixed A3, TD6,
SP-2, or JC2.
