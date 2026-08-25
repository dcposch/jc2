# Hostile review — AS vertical D8 state sufficiency

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Read in full:

- `xmodel/as-fonly-d7-vertical-state-sufficiency-20260824.md`;
- every file in `cases/as_fonly_d7_vertical_state_sufficiency_20260824/`;
- the frozen corrected post-D10 D9/D8 producer package and the confirmed
  omitted-Frobenius erratum; and
- the currently active corrected-package review only if it has completed.

Charged hashes:

```text
report    410235081a54470a377d8d107a1982d34d507040718b945d11ee99dc4d1e5fe4
manifest  ba28e9132b30a9cb7a794dc3da1a55c518c1b9c1253817ffde5fdbb90f539e36
freeze    b842a03e35bab622939dc22f69c5eafbcd59e6ea2c4aba227c49df9db99b9aee
```

Independently reconstruct and attack:

1. `Msharp*M=M*Msharp=(A^2+H*B)I`, including all signs;
2. necessity and sufficiency of the divisibility plus quotient-cap criterion
   on `Delta!=0`, with cancellation hypotheses stated correctly;
3. both `Delta=0` criteria, including degree bounds, `H!=0`, `A=0` when
   `H=0`, and the `B=0` subcase;
4. the claimed possible ranks `5,3,2,0` and absence of ranks one and four;
5. independent regeneration of the corrected matrix/column from the frozen
   integer-source package, rather than trusting copied rows;
6. exhaustive literal-`F3` agreement: all `1,594,323` assignments, all
   `314,127` compatible cases, stratum totals, fibre histogram, and stream
   hashes; and
7. the no-cap negative control with exactly `202,176` false positives and
   the stated degree-pattern table.

Run `./replay_all.sh`, but independently recompute representative points in
every stratum and at least one no-cap false positive.  Distinguish the
unconditional algebraic theorem for the displayed matrix from the still
review-gated claim that the corrected column is the exact AS successor.
Attack radicalization, lost embedded structure, accidental finite-field-only
cancellation, endpoint degree conventions, and any all-depth/lift inference.

Write exactly
`xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md`.
Do not edit producer, case, canonical, coordination, or other review files.
End with exactly one verdict: `CONFIRMED`, `GAP`, or `REFUTED`, and identify
the smallest failing identity or hypothesis if applicable.
