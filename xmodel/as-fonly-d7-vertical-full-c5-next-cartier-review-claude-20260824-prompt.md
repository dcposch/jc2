# Hostile review — AS full-C5 D7 gate and first following Cartier gate

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable. Do not use Bash
or run any local computation. Read in full:

- `xmodel/as-fonly-d7-vertical-full-c5-d7-gate-20260824.md`;
- every file in `cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824/`;
- `xmodel/as-fonly-d7-vertical-next-cartier-20260824.md`;
- every file in `cases/as_fonly_d7_vertical_next_cartier_20260824/`;
- only the frozen parents pinned by those manifests as needed.

Charged top-level hashes:

```text
full-C5 report      907dcc72523eb228a7ac6581826460601030e56c996d4df583b2fad274f09a6e
full-C5 manifest    9454ffa7cc0f14c2eaa5095b8ba45f78d3033c2022967d6c0011550e5e198cb7
full-C5 freeze      c0299b4637131bb1e8f637f25d692a4d41ff86a6c6567d258f567917032858e3
next report         cfd77aacacf5c47c74e001c26cfb5369e69b7545bd1d301627135f06fd30af15
next manifest       0c0d88b80038ed266bc57431cde7d395ebe592497ccdd0e9830480d26a41551f
next freeze         e7742fbfaee95fa4e2e88cd34635fb3c38374ac3cd3d637257eaa563beb88444
```

The producer replays were short, bounded, and passed before freeze. Do not
rerun them locally. Inspect the source and frozen expected outputs rather
than trusting PASS. Independently attack:

1. Rebuild conceptually the integer divided-carry source before reduction
   modulo three. Verify that adjoining all twelve homogeneous `C5,D5`
   coefficients gives the advertised eight D7 rows, including why six rows
   change from the zero-C5 slice and why `fc=fd=0` remain invariant. Look for
   premature reduction, a lost divided term, or use of an unlicensed carry
   representative.
2. Audit the accepted degree-four block, especially the identically zero
   `x^2y^2` coefficient, and the divergence-rank/cokernel argument completing
   all lower degrees. Check that degree-six spectators and divergence kernels
   are correctly omitted from the visible count without affecting
   solvability.
3. Derive the `19 x 17` affine rank formula. Check the exponents in
   `3^(6+r-c)` and `3^(23-c)`, the literal `3^6` Frobenius enumeration, every
   histogram total, and the meaning of 24,303 compatible base/Frobenius
   states and 3,253,689 visible solutions.
4. For the following gate, derive over the integers
   `[x^2y^2]E1=c5_3+d5_2+2h^2` and `[x^2y^2]M=0`. Verify that all other lower
   accepted rows decouple and that this is the unique divergence cokernel
   class through total degree six.
5. Audit the sufficiency claim: after prior high rows and this class vanish,
   show a cap-seven pair `W,Z` exists and adding `27W,27Z` changes the
   order-27 Jacobian coefficient by exactly `W_x+Z_y`. Search for missing
   cross terms, an off-by-one p-adic order, or a degree overflow.
6. Check the `20 x 17` compiler and all stated counts/hashes, and distinguish
   one finite next-digit lift from recurrence, all-depth lifting,
   characteristic-zero algebraization, a counterexample, or JC2.

State the smallest false identity or missing hypothesis if one exists. Give
separate exact promotable sentences for the parent and successor, with strict
scope. Write exactly
`xmodel/as-fonly-d7-vertical-full-c5-next-cartier-review-claude-20260824.md`.
Do not edit any other file. End with exactly one verdict: `CONFIRMED`, `GAP`,
or `REFUTED`.
