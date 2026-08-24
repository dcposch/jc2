# Hostile different-model review — AS `p=3`, depth-five cap-eight survivor

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`c327bdc8d02472feba42573760325099f34b8cdf`, with the named frozen producer
artifacts uncommitted on top. Read in full:

- `xmodel/as-gauge-growth-p3-depth5-d8-survivor-20260824.md`;
- every payload under
  `cases/as_gauge_growth_p3_depth5_d8_survivor_20260824/`;
- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` and its hostile review;
- the bounded-polar and completed-gauge producer/reviews on which the finite
  system and orientation depend.

Frozen hashes:

- report (both the xmodel copy and case copy):
  `3cca09d0c31b46ed12b8510e0d343fd097b2727e2b8ff3aef464c334d48dba6f`;
- integer replay:
  `0c030b231e6e830a7fcdd50d731db33f01ac3b15523179c5c8e063b6967357ac`;
- independent Singular replay:
  `91b347525075083a8fe1a5f9ad4ce6b35e7f00469f2808ed0c4fab0ed7d7cea8`;
- manifest:
  `7cf4df1eb4427d08fc2eb6bfa665466b05c65d7b7beaa2f0ca1ebbb81fe0e16d`;
- freeze record:
  `e64cd77214d0809fd5c5b3754d002daa687b98183362901afb4a99219baf83a9`;
- canonical replay payload:
  `b5fb3f3e48c7193ea385293ce38bbe62219a84ebd318ce72c8f47587d3c24382`.

Verify every hash and rerun the registered Python and Singular programs from
the case directory. Those are regression evidence only. Then attack every
load-bearing claim with a separate exact sparse-polynomial engine or a full
independent derivation:

1. **System and cap semantics.** Reconstruct the frozen identity-branch
   bounded system at `p=3,n=5`: `P=A-A^3`,
   `Q=B*S5(A)`, `S5=1+3A^2+9A^4+27A^6+81A^8`, modulo 243, with
   determinant-one polynomial gauge `(A,B)` and total-degree simplex caps on
   both gauge and map. Check that this is the same orientation and category
   used in the reviewed depth-four table; detect any rectangle/simplex,
   left/right composition, or map/gauge cap mismatch.
2. **Exact survivor.** Independently expand

   `A=x+9x^5-9x^5y`,

   `B=y+9x^4+198x^4y+144x^4y^2`,

   reduce coefficientwise modulo 243, and recompute every displayed monomial
   of P and Q. Verify total degrees `(6,6,8,8)`, the special fibre
   `(x-x^3,y) mod 3`, and absence of every monomial above cap eight. Do not
   import producer support tables.
3. **Inverse, orientation, and Jacobians.** Independently prove
   `(1-3A^2)S5(A)=1 mod 243`, `B=Q(1-3A^2)`, and directly recompute
   `det J(A,B)=det J(P,Q)=1 mod 243`. Check the chain-rule inference and also
   verify the latter determinant without relying only on that inference.
   Recompute `c_x+d_y`, `f_y`, `{c,d}` and the exact carry cancellation.
4. **Counter-motif.** Audit the claimed high-Q cancellation for
   `c=x^5(1-y)`, `d=x^4(1+y+y^2)`, including all contributions from the
   finite geometric series. Check that the divided divergence is absorbed by
   `f=7x^4y+5x^4y^2` and that the remaining bracket is divisible by three.
   Distinguish an exact construction from a proposed all-depth recurrence.
5. **Falsification logic.** Verify that this point belongs to
   `B_(3,5)(8,8)`, so `D_min(3,5)<=8`, while the preregistered prediction was
   nine. Decide whether the numerical law
   `(n-1)(p-1)+1` is therefore genuinely falsified at `(3,5)`. Preserve that
   cap seven is open and cap eight is not proved minimal.
6. **Scope and successor.** Attack every inference to depth six, a compatible
   inverse-limit tower, a polynomial/Tate lift, failure of the polar theorem,
   `A_infinity`, deck descent, or JC2. Assess the honest successors: exact cap
   seven and lifting this cancellation motif to depth six, starting at fixed
   cap eight.

Use exact arithmetic throughout. A producer replay plus prose comparison is
not independent evidence. Put scratch work outside tracked paths. Do not edit
producer, case, canonical, ladder, notes, prompt, log, run, or erratum files,
and do not launch AWS. Write exactly one report:

`xmodel/as-gauge-growth-p3-depth5-d8-survivor-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
