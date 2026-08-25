# Hostile different-model review — AS post-D10 omitted Frobenius cross-carry erratum

Work in `/Users/dc/code/math/jc2`.  The earlier post-D10 D9/D8 package is
frozen but quarantined; review the retraction, not its old compatibility
claims.  Read in full:

- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md`;
- every file in
  `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/`;
- the quarantined producer
  `xmodel/as-fonly-d7-postd10-d98-f3-20260824.md` and its frozen generator;
- the confirmed D10 producer/review and corrected divided-carry predecessor.

Charged hashes:

```text
erratum report  26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d
MANIFEST        5a3d0f9f4587064988cfa7ae3a6be399b4d8f24908d0033367e220f07d935978
FREEZE          cd3009992df83be446c2ffbab6249137e6fbbc7096f5b6d29a3cc885dbdd487e
witness replay  0bc6d3913fedf322a48a8d79acef1af56d6b3b41f078aa49ecf1b60bc0b463d8
```

Verify hashes and replay only as regression.  Independently:

1. Expand the integer Jacobian through division by 27 and derive the exact
   residual `(det J-1)/27=E1+M+3N` after `L=3L1` and
   `E=L1+K+C_x+D_y=3E1`.
2. Split `U=U0+UF`, `V=V0+VF` with degree-six Frobenius directions.  Derive
   the full single-cross expression for `[K_Frob/3] mod 3`, prove the
   double-Frobenius cross vanishes after division, and determine its maximum
   degrees on the vertical and `g` endpoint branches.
3. Rebuild the two integer witnesses from scratch and verify exactly
   `2*x^7+2*x^8` and `2*x*y^6+2*x^4*y^5` modulo 3.  Confirm that these terms
   were absent from the quarantined generator rather than merely expressed
   in another coordinate.
4. Audit every preservation/retraction boundary.  In particular, decide
   independently whether the vertical D9 global section, six D8 unit pivots,
   D8 coefficient matrix, and its geometric rank loci really survive, while
   the vertical inhomogeneous column/counts and the entire stated g-endpoint
   reduction/counts do not.  Check all six Frobenius directions.
5. Confirm the erratum does not alter the reviewed D10 theorem and makes no
   corrected census, next-carry, full-D7, lift/no-lift, characteristic-zero,
   counterexample, or JC2 claim.

Use exact arithmetic and independent scratch work outside tracked paths.  Do
not edit producer, erratum, case, canonical, prompt/log/run, coordination, or
predecessor files.  Do not launch AWS.  Write exactly:

`xmodel/as-fonly-d7-postd10-d98-f3-erratum-review-grok-20260824.md`

Give one overall and per-item verdict from `CONFIRMED`, `GAP`, or `REFUTED`,
checked hashes, the smallest failing identity or missing hypothesis, exact
preservation/retraction language, and quarantine language.

