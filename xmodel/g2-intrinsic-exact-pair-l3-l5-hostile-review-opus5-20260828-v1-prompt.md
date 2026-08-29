You are Opus 5 acting as a genuinely different-model hostile mathematical
reviewer in the plane Jacobian conjecture campaign.  Work in
`/Users/dc/code/math/jc2`.

Review these frozen packets, whose live hashes you must recompute before use:

1. `xmodel/g2-intrinsic-exact-pair-l3-l5-newton-puiseux-sol-ultra-20260828.md`
   expected SHA256
   `841c848eb98aa234fe6429006b3f84958c042869db395d61f2394a6c6c7c81d0`.
2. `xmodel/g2-intrinsic-exact-pair-l5-reduced-denominator-independent-review-sol-ultra-20260828.md`
   expected SHA256
   `5e8bc3c54007e9c471a8cb86b51929172c0b749156b1843c013c259d41ea70d9`.
3. The primary source `refs/sigray_full.pdf`, expected SHA256
   `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`.

Do not treat either Sol report's conclusion as evidence.  Reconstruct the
theorem independently from local normalization/completion, tame Kummer base
change, and the cited primary-source statements.  You may extract only the
relevant PDF pages/text.  Attack all of the following:

- Does the actual plane coordinate `y` generate the completed local factor,
  so that its reduced Puiseux denominator is exactly the ramification index
  `e_S=ord_S(1/x)`, not merely a divisor?  Cover the constant-series and
  horizontal-line edge cases.
- For a common `kappa`, prove or refute orbit size `e_S` and stabilizer size
  `kappa/e_S`, including oversized covers, nontrivial support gcd, and the
  zero/constant-support convention.
- Prove no deck orbit can collide across distinct normalized places or
  irreducible components.  Audit reducible squarefree curves and vertical
  components, and the swapped-chart union/no-duplication claim.
- Read Sigray Proposition 3.1 and Statement 3.9 closely.  Decide whether they
  count base-changed Puiseux presentations, original normalized places, or
  something else; verify the all-root multiplicity recursion and strict
  truncation claim, including zero residual roots.
- Audit the finite terminal replacement carefully.  Is an exact local factor
  plus a prefix longer than every pairwise contact (including deck conjugates)
  sufficient and necessary for a leaf/place record?  Could Hensel lifting or
  inverse/Laurent behavior leave an ambiguity?
- Enforce the hybrid firewall: no result about the intrinsic exact-pair
  algorithm may silently prove that a selected VGG/GGV translation corridor
  is an actual fibre truncation or is source/place complete.

Look actively for counterexamples: oversized Kummer covers, premature common
prefixes, nonprimitive coordinate functions, reducible factors, vertical or
horizontal lines, and chart overlap.  Separate theorem-level reasoning from
finite examples.  If the theorem is sound only after a wording/typing repair,
give the smallest exact repair and state whether L3/L4/L5 can be marked
available for the intrinsic exact-pair route.

Write a self-contained report to exactly

`xmodel/g2-intrinsic-exact-pair-l3-l5-hostile-review-opus5-20260828-v1.md`

with a terminal verdict exactly one of `PASS`, `REPAIR`, or `REFUTE`.  State
that you are Opus 5 and that this is different-model review.  Include live
hashes and precise source-page/statement references.  If you make a finite
arithmetic claim, either show it transparently or create a light independent
standard-library checker under
`cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/`; mutations are
preferred.  Do not edit either target, any canonical/top-level campaign file,
or any other existing artifact.

Never enter, list, search, read, build, status, or modify `jc2-lean`.  Do not
run heavy local CAS or use AWS.  Preserve the dirty shared worktree.  Your only
writes may be the required review and, if needed, the new checker directory;
the lane wrapper owns `.log` and `.run` files.
