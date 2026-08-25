# Hostile source review — TD6 fixed three-center `A^3` union

You are the hostile reviewer.  Work read-only except for writing the single
report requested below.  Do not use Bash, a shell, web access, or external
computation.  Read the byte-readable sources and frozen outputs directly;
do hand algebra where useful.  Do not edit any producer, case, canonical,
ledger, prompt, or run file.

## Charged claim

At the fixed source-typed normalized TD6 section

```text
y=s^-1, x=C s+V s^2+U s^3+t s^4,
p=t^15, q=t+t^25,
```

with the frozen F1/pole data and zero dead stretch, the exact constructible
union

```text
A^3_{C,V,U}=D(U H B3) union V(U) union V(H) union V(B3),
H=C-3U^2,
B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6,
```

contains no point satisfying the transported first-band/genuine-P12
necessary equations.  This is only a fixed normalized three-center-section
kill; it is not a neighborhood, boundary/dead-stretch, whole-TD6, SP-2,
maximum-degree, or JC2 theorem.

## Frozen charge

Read in full:

- `cases/td6_c1_c2_c3_b3_raw_divisor_aws_20260825/README.md`;
- `cases/td6_c1_c2_c3_b3_raw_divisor_aws_20260825/MANIFEST.sha256`
  (SHA-256 `86102e8c906436afcf6a2397fb8b0ea736ee7acdbae3232c330ec10c536e2b70`);
- `cases/td6_c1_c2_c3_b3_raw_divisor_aws_20260825/FREEZE.sha256`
  (SHA-256 `43a708f7c05b84a7669a78a2c9a1ce0eb2f345bd6936e3c47770e26b3d9a1fcb`);
- `xmodel/td6-c1-c2-c3-b3-raw-divisor-aws-20260825.md`
  (SHA-256 `eb127a581c660ab273d344af610d38507b02e476fd3bd92d002ff482af8f10f2`);
- every relevant file in the byte-readable source supplement
  `cases/td6_c1_c2_c3_b3_raw_divisor_source_snapshot_20260825/`, whose
  MANIFEST SHA-256 is
  `82b2593f5ed3b2ec829827d792993cb6bdb7d4711e9ce03382b87f8790b5c573`
  and FREEZE SHA-256 is
  `47247dec81d31582bba87c2211782be0628f83c6011fa3f9f59c5d161be9becf`;
- the pinned trivariate checkpoint erratum and both confirmed P3 reviews in
  the primary package's `DEPENDENCIES.sha256`.

The theorem-producing stdout hashes are V27 generic
`f79c616901a39b27d7e00d6ad27a80f5f4f9f3947290d861e4ba803a85721221`,
V22 quadratic ascending
`d9041a6a22cdc4ad69d4bcdc2b2f9620e7e3454dd0916a61247979d692b5c6cf`,
V22 quadratic reverse
`c45ccff3b839b4917b8499c19ded7c5ef06b6edecdd572f809719eb51dc7c5c9`,
and clean V26 half reverse
`ad8725eb63e1112651145eed3f48c82e70c469fa35404f07eef1c0363ef14b74`.

## Mandatory attacks

1. **Source typing.**  Verify the exact center map and that no source scaling,
   weighted-projective identification, stale center cache, or unlicensed
   gauge enters V22/V26/V27.  Track the full recursive import closure and
   distinguish the fixed normalized section from a full TD6 source family.
2. **Birational coverage.**  Re-derive
   `B3=U^6 b(C/U^2,V^2/U^3)`, the line parametrization through `(-5,0)`, its
   inverse, and its exact missed/boundary loci.  Attack `U=0`, `V=0`,
   `tau=0`, `tau=2`, `w=0`, the base point, and points at infinity.  Decide
   whether the union leaves any affine `B3=0` point uncovered.
3. **Generic certificate.**  Inspect V27's original-row replay, unit
   remainder, per-slot denominator clearing, sentinel descent, and complete
   factorization
   `tau^51 w^19 (tau-2)^16 (2tau-1)(tau^2-4tau+2)^6`.  Look for a pivot or
   source denominator absent from that divisor.
4. **Raw factors.**  Inspect the V22 exact quadratic field and V26 rational
   half branch.  Verify genuine P12, original-row lift, negative controls,
   all denominator factors, auxiliary-field descent, and that `w=0` is only
   the already frozen origin.  Explain why one clean V26 reverse-pivot
   original-row identity is logically sufficient on `D(w)`; treat the live
   ascending lane only as redundancy, not a hidden hypothesis.
5. **Cross-package union.**  Use the trivariate erratum rather than its
   superseded V14 B3 interpretation.  Verify that the generic `D(UHB3)`,
   whole `U=0`, reviewed whole `H=0`, and new whole `B3=0` statements are at
   exactly the same source-typed gate and really cover all `A^3`.  Track the
   P3 origin terminology erratum (transport-band, not first-band).
6. **Scope and falsifier.**  State the smallest actual error or missing
   hypothesis.  Give one promotable sentence with every load-bearing scope
   qualifier.  End the report with exactly `CONFIRMED`, `REFUTED`, or
   `INCONCLUSIVE` on its own line.

Disclose explicitly that this no-shell session cannot recompute hashes or
rerun AWS algebra.  Write the report only to
`xmodel/td6-c1-c2-c3-fixed-section-review-claude-20260825.md`.
