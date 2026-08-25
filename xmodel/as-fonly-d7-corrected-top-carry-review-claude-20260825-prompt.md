# Hostile review — AS D7 divided-Frobenius erratum and corrected Q11/Q10 censuses

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable. Do not use Bash
or run any local computation. Read in full:

- `xmodel/as-fonly-d7-next-top-carry-frobenius-erratum-20260825.md` and all
  source/result files in
  `cases/as_fonly_d7_next_top_carry_frobenius_erratum_20260825/`;
- `xmodel/as-fonly-d7-vertical-next-top-corrected-shards-20260825.md` and the
  registrations, compilers, manifests, aggregate, metadata, and representative
  shard outputs in
  `cases/as_fonly_d7_vertical_next_top_corrected_shards_20260825/`;
- `xmodel/as-fonly-d7-vertical-next-top10-corrected-shards-20260825.md` and
  the analogous files in
  `cases/as_fonly_d7_vertical_next_top10_corrected_shards_20260825/`;
- only the frozen full-C5/first-Cartier predecessors pinned by these packages,
  as needed to audit state reconstruction and source provenance.

Charged hashes:

```text
erratum report         1129f2c93db930a3040e1626cc34dcfd818e824b356cbd63baac4e8d37c9ea0c
erratum result manifest a9bc12777cd1cdf708d5df713909a2a3384887e20ff9e11a40da3acf93e68d8a
erratum freeze         e23391101129c0822ed2f906053919860db02ed2ae5776285bace5764f326385
corrected Q11 report   4d9cebdaaefb7aff260d4d5bec5f24d88ec66cc8613bf5571a81778a70e10082
Q11 result manifest    a9a73b2d2b4c646a8351788595a9a43dc0b7c08f5b55c23718eb77c74c6714e3
Q11 freeze             7f06a1b9a9af468a94099de3476e7c726721e0ed0e605797a2b87d38c4c17335
corrected Q10 report   b636b00a0c6bc9673cda46efa312b311c71e70c5dd24e92823b2bff205b3a817
Q10 result manifest    7ee3ae606673ee1cf146a3c3cf45cacf82f07c8ed6e510adb27021136de9b414
Q10 freeze             e73b854b288bc18f9207a47ae4e265b429d054410c586c8ab9ee318ce24a79ec
```

All enumerations ran on AWS; do not rerun them locally. Inspect frozen source
and outputs rather than trusting PASS. Independently attack:

1. Re-derive the full integer determinant filtration before reduction and
   division. Verify the definitions of `L,K,M,N,T,S`, the two divided carries,
   and why the next residual is exactly `F1+N+T mod 3`.
2. Split `U=U0+UF,V=V0+VF` and audit the divisibility, degree support,
   orientation, and coefficients of `MF/3` and `{UF,VF}/9`. In particular,
   verify every term of corrected `Q11` and `Q10` and both nonzero controls.
   Look for any further divided Frobenius term at degrees 12, 11, or 10.
3. Audit the preservation/quarantine boundary. Only `N12` from the old shards
   may survive; old `602343` and its `729` multiple must remain wrong-source
   diagnostics. Check whether any earlier full-C5 or first-Cartier count also
   depended on the retracted degree bound.
4. Inspect both corrected compilers against the frozen predecessor system.
   Check complete reconstruction of all 1,085,103 predecessor states, the
   twelve Q11 and eleven Q10 coefficients, current-digit spectator omission,
   and the exact `3^6=729` completion factor. Search for canonical-carry or
   state-sufficiency assumptions not actually present in the stored state.
5. Audit the 27-shard partition, per-base histograms, totals, aggregate and
   Merkle construction, stderr/return-code metadata, source closure, and
   representative large and small fibres. Parallel agreement within one
   implementation is evidence, not an independent mathematical engine.
6. Scope the conclusion exactly: source-corrected survival counts are
   `629115`, `260847`, and `33225` through degrees 12, 11, 10 respectively;
   `24221025=729*33225` counts current-Frobenius spectator completions. Degree
   nine, lower rows, recurrence, all-depth lifting, characteristic-zero
   algebraization, counterexamples, and JC2 remain open.

Give separate exact promotable sentences for the erratum, corrected Q11, and
corrected Q10. State the smallest false row, count, source assumption, or
custody gap if one exists. Write exactly
`xmodel/as-fonly-d7-corrected-top-carry-review-claude-20260825.md`. Do not edit
any other file. End with exactly one verdict: `CONFIRMED`, `GAP`, or
`REFUTED`.
