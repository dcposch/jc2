# Hostile review — selected-Q8 infinity passport plus Galois primitivity

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable. Do not use Bash
or run any local computation. Read in full:

- `xmodel/max12-912-order3-nu-q8-infinity-contact-passport-20260824.md` and
  every file in
  `cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/`;
- `xmodel/max12-912-order3-nu-q8-galois-primitivity-20260825.md` and every
  file in
  `cases/max12_912_order3_nu_q8_galois_primitivity_aws_20260825/`;
- the reviewed global-quotient, normalization, formal-branch, and terminal
  Belyi parents cited by those registrations, including the terminal review's
  explicit `Z!=0` correction, only as needed to audit imported hypotheses.

Charged hashes:

```text
infinity report        89691023f2703eba5c0cd29d65bc8732d837905fe41b01f64ae9d3b908068168
infinity manifest      a9e8748fbb088b1cd50db7c3d73b917bc26165a5aefd7fe51b564c990b147003
infinity freeze        8d695040eb73bc8719f484a724ce4d4bbda61c650e73ec617c6bbdd713d8e298
primitivity report     9f37fc3fc7933b911bea56258f677da77a823caa8daf9ce01c03b0884c502c8f
primitivity manifest   1a3e44b912084e2c721809c0cf9c86ce55b7a300a25b6adfc2f777dbdc17b465
primitivity freeze     f25fa86f000f3f9cdcff2ec8aa6b058fc6298c83086eb35b6a153e70caaf36aa
```

The bounded replays ran on AWS or before freeze and must not be rerun
locally. Inspect their sources and frozen outputs rather than trusting PASS.
Independently attack:

1. The global map and contact claim. Verify that the invariant coordinates
   really yield a nonconstant morphism `P1_x -> normalization(C_Q8)`, that
   completeness gives surjectivity, and that the reviewed finite-contact
   valuation theorem transfers through the Kummer lift. Check carefully the
   conclusion that the complete preimage of a chosen corrected-Q8 point is
   set-theoretically the unique source point at infinity.
2. Passport parity. From `theta=a0^2/p^9` and
   `S-S0=unit*theta+O(theta^2)`, audit every unit/nonzero assertion, why
   `ord_infinity(a0)>0`, and why cubing `Z=T^3` preserves the contact order.
   Check the exact distinction between `e_pass` and Kummer order three.
3. Mason equality. Verify `deg(A_T-lambda B_T)=D-e_pass`, pairwise
   coprimality, squarefreeness of the finite lambda-fibre, the radical count
   `D+1`, and the absence of an omitted infinity contribution. Decide whether
   Mason sharpness is only a non-obstruction, as claimed.
4. The terminal/Kummer converse and `e_pass=2` control. Check all scalar,
   derivative, deck-character, noncube, and original-row identities. Search
   for a hidden constant/cube case or for use of the ninth-power equation in
   place of `9*r8'=j/u`.
5. The finite-field Galois certificates. Audit the exact octic, good-prime
   and squarefreeness conditions, the `[8]` and `[1,7]` factor patterns, and
   the use of Dedekind/Frobenius. Verify that a transitive degree-eight action
   with a seven-cycle has no block of size two or four.
6. The geometric-component inference. Verify that unique smooth selected
   branches make “lies on the same geometric irreducible component” a
   Galois-invariant equivalence relation on all eight Q8 roots, hence a block
   system. Look for reducibility over the coefficient field, branch swapping,
   intersections, non-geometric components, or normalization identifications
   that invalidate the one-component-versus-eight-singletons dichotomy.
7. The conditional combination and scope. Check that one source point cannot
   map to two distinct normalization points, but do not kill the eight
   singleton alternative. No coefficient-fibre/Taylor realization,
   `(9,12)` exclusion, maximum-twelve result, or JC2 statement is licensed.

Give separate exact promotable sentences for the infinity/passport theorem,
the primitivity theorem, and their conditional consequence. State the
smallest missing hypothesis or false step if one exists. Write exactly
`xmodel/max12-912-order3-nu-q8-infinity-primitivity-review-claude-20260825.md`.
Do not edit any other file. End with exactly one verdict: `CONFIRMED`, `GAP`,
or `REFUTED`.
