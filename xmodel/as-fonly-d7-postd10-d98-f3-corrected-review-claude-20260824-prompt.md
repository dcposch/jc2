# Hostile different-model review — source-corrected AS post-D10 D9/D8 gate

Work in `/Users/dc/code/math/jc2`.  Review the frozen corrected producer, not
the quarantined predecessor.  Read in full:

- `xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md`;
- every file in
  `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/`;
- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md`;
- the confirmed D10 producer and hostile review;
- the earlier post-D10 producer only to verify its quarantine boundary.

Charged hashes:

```text
corrected report  9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8
MANIFEST          a5480d2e3d7c36db4fee735ef8f2262c3454e3e35eb348c7f097c45c59aa2cfb
FREEZE            bf7ce39ae1cf7cc6338c006cd2cd59d11a387d8644d740e6faee2cb63229a264
replay_all.sh     b3564b4e34f60bba751f00de3e30420050c1e6537db3a137001b89d0ca16e5ff
```

Verify hashes and run the portable replay as regression.  Then attack the
mathematics and compiler independently:

1. Starting from the integer Jacobian, rederive
   `det J-1=3L+9(K+C_x+D_y)+27M+81N`.  After the accepted divisions, derive
   the single-Frobenius contribution to `K/3 mod 3`, verify the double-
   Frobenius term vanishes, and confirm all six degree-six Frobenius variables
   enter the regenerated source rows with the claimed degree ceilings.
2. Rebuild the vertical D9 four-row matrix and prove the displayed global
   section, including every rank-changing locus.  Rebuild the D8 `7 x 5`
   matrix after the six licensed unit pivots.  Independently verify that its
   geometric ranks are exactly `0,2,3,5` and audit all radical/minor and
   algebraic-closure claims.
3. Independently audit the affine-projection formula.  For each structural
   base, check why the number of compatible six-variable Frobenius choices is
   `0` when `c<d` and `3^(6+r-c)` otherwise.  Reproduce the vertical
   structural histogram, rank triples, twelve empty bases, full
   `314127/1594323` literal-F3 count, and deterministic hashes.  Look for
   coordinate omissions, representative dependence, or an unjustified
   finite-field-to-scheme inference.
4. Rebuild the localized `g!=0` endpoint from source after its three D10
   pivots.  Confirm it really has `17` rows and `14` current-digit unknowns,
   retains all Frobenius directions, and contains the two named degree-nine
   terms.  Independently reproduce the structural/rank tables, exact
   `918/354294` count, and hashes.
5. Reconstruct the four next-carry controls.  For the two full mod-81 maps,
   verify the determinant exactly, division by 81, the
   `x^4+2*x^6+2*x^8` residual, and the cap-seven divergence degree bound.
   Check that terminality is genuinely pointwise and is not accidentally
   asserted for a whole fibre.
6. Audit dependency and refusal scope: the D10 theorem must remain intact;
   the old post-D10 counts stay quarantined; literal `F3` counts do not imply
   `Fbar_3` compatibility, full D7 coverage, an all-depth obstruction or
   survivor, characteristic-zero algebraization, a counterexample, or JC2.

Use exact arithmetic and independent scratch files outside tracked paths.
Do not edit producer, case, canonical, prompt/log/run, coordination, or any
predecessor.  Do not launch AWS.  Write exactly:

`xmodel/as-fonly-d7-postd10-d98-f3-corrected-review-claude-20260824.md`

Give one overall and per-item verdict from `CONFIRMED`, `GAP`, or `REFUTED`;
checked hashes; exact commands/results; the smallest failing identity or
missing hypothesis; and precise promotion/quarantine language.
