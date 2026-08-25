# Erratum: V14 B3-local replay is a denominator/pivot diagnostic only

Status: **SOURCE-AUDITED SCOPE CORRECTION; FROZEN V14 BYTES UNCHANGED.**

This erratum narrows only the interpretation of the V14 B3-local lane in the
frozen three-center checkpoint.  It does not alter the archive, replay,
stdout, manifest, or freeze.  Their relevant SHA-256 values are:

```text
checkpoint README                         8b2e2f5852f51853c8f52d66c03d0d5196ed0072c121c647eede6e25a2dc2a5b
B_LOCAL_RESULTANT_STRATA                  46a2a02cd8a66273836f5c770dece7870fc52e5ebc1cf88989ca6ea8b923f194
V14 b-local stdout                        e4f44d3e2e0881c95e3721138d8e71f1827b0de4e4b5f8c1d95724cff517e9e7
checkpoint MANIFEST                       d70e8942bd457bcb2cac8a00b5775fd09c530ff2ca37bbdcb1ab41b4984beb6f
checkpoint FREEZE                         cbb6fee9be655335cb63127d5686308ad0b0516bffdf38d30359bf2924ad93e4
checkpoint xmodel report                  c27c3965b7e4bd67341fe880c34f9ff68a0684fa79c812ed35267b9d98a62b45
```

## Unsupported frozen wording

The frozen README says:

> “The corrected B3-local V14 source replay again gives P12 `-k/50`.”

That sentence is false as a description of the emitted B3-local normal form.
The frozen stratum ledger also calls three denominator-resultant curves “the
complete new B3-local debt”; that completeness claim is unsupported.  The
xmodel checkpoint's shorter statement that the corrected B3-local
denominator “leaves three exact raw curves” must likewise be read as a list
of denominator-resultant components only, not as the full uncovered B3
locus.

## Exact evidence and corrected interpretation

The immutable V14 stdout itself records:

```text
remainder_terms=1681
remainder_degree=2
remainder_is_expected_constant=false
remainder_is_constant_unit=false
stratum_localization_killed=false
whole_stratum_killed=false
generic_open_killed=false
```

It also records a valid original-row identity and plus-one negative control.
Thus V14 exactly proves that genuine P12 reduces, in that pivot chart, to a
specific 1,681-term degree-two remainder `R`; it does **not** prove
`R=-k/50` and does not prove that `R` is nonvanishing for all 94 free
first-band variables.  A nonconstant polynomial with a nonzero constant term
is not a unit in that affine-variable ring.  The PASS marker certifies the
exact compilation/source replay, not an incompatibility theorem.

The printed resultant factors are the intersection of `B3=0` with the
relation-denominator divisor.  They do not test the zero locus of `R` and
therefore cannot be promoted to a complete exceptional cover.  Raw quotient
replays on those curves remain useful independent local tests, but even if
all pass they do not close generic `B3=0`.

V14 is henceforth licensed only as:

- an exact transport/first-pivot and original-row source-replay diagnostic;
- an exact factorization of its actual relation denominator and its
  resultant with `B3`;
- a negative control against treating a denominator cover as a compatibility
  obstruction.

The generic three-center unit certificate off `U*(C-3U^2)*B3=0`, and the raw
`U=0`, `V=0`, and separately certified `H=0` opens, are unaffected.  The raw
generic `B3=0` divisor remains open.  Its licensed successor is a direct
birational quotient replay over `Q(t,w)` with full source replay and chart
audit.  No complete three-center section, TD6, SP2, or JC2 claim is made.
