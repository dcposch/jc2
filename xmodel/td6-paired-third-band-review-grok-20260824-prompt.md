# Hostile different-model review — TD6 paired third band

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/td6-paired-third-band-20260824.md`
- every file under `cases/td6_paired_third_band_20260824/`
- the TD6 moduli-uniformity producer and, if landed, its hostile review
- the earlier first-band and next-row producer/review pairs as dependencies

Frozen hashes:

- report: `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2`
- replay: `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a`
- freeze: `f509e1c500ea7f565bafd5f558589a92435d1fde81a75f06d8abaa44c3a6896f`

Independently rerun the replay and attack exactly:

1. Verify the quadratic field, all source-open conditions, and the exact
   specialization `C=1`, `D=S-22/25`, `L=3`, `A=1/9`.
2. Reconstruct rather than trust the imported 94-dimensional first-band
   family and the 56-dimensional paired-next family. Check ranks, affine
   consistency, transport, and prior rows over the quadratic field.
3. Independently derive the `[s^0]J` formula and every available `t` row.
   Prove or refute that `[s^0 t^0]J=81/15625` on the entire 56-space, with
   all parameter coefficients zero, hence residual `-15544/15625`.
4. Check the independent global differentiation route and ensure the
   parameter origin is a valid representative of the affine family.
5. Audit the `r^2` pole formula, induced supports, quadratic degree, monomial
   count, and tangent ranks, while keeping it logically irrelevant if the
   centered constant row is already inconsistent.
6. Verify all hashes, exact replay output, and scope. The only admissible
   promotion is pointwise emptiness at this single algebraic moduli point;
   no uniform moduli-curve, SP-2, terminal-class, landing, or JC2 claim.
   State the smallest valid uniform successor.

Try hard to find a sign/normalization error, an incorrect required constant
row, a hidden numerical embedding, a stale affine parameterization, or a
rank/nullity claim made for an inconsistent affine system. Do not edit
producer/canonical files, run the uniform successor, or launch AWS.

Write exactly one file:

`xmodel/td6-paired-third-band-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent recomputation, dependency status, scope exclusions,
and promotion advice.
