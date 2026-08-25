# Hostile review: selected-Q8 sparse contact forces a mod-127 component

Act as an independent hostile algebraic-geometry referee. Read these files in
full:

- `xmodel/max12-912-order3-nu-q8-sparse-contact-component-lemma-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-breadth-component-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-breadth-component-self-contained-erratum-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-hensel-order64-aws-20260825.md`
- the README, FREEZE, manifest, and summary files in
  `cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/` and
  `cases/max12_912_order3_nu_q8_p127_breadth_order8_aws_20260825/`

Do not review later bidegree or high-order-contact successors. Do not browse,
run shell commands, or perform new heavy computation. You may use repository
Read/Grep/Glob only and may write exactly the report requested below.

The claimed conclusion is deliberately narrow: over F_127, at least one
relevant irreducible source-curve component has cycle-theoretic projected
image equal to the geometrically irreducible degree-190 curve H. The final
count must use only explicitly lifted fibres: 80*8+64=704>658. It must not
rely on the earlier 123+63+68*7 count.

Try to falsify each load-bearing point:

1. Does the full-rank local calculation imply a unique one-dimensional
   reduced branch and that w-w_i is a uniformizer, hence that each relevant
   component maps generically finitely to the (w,v)-plane rather than to a
   point?
2. Can a generic pulled-back plane line be chosen so its intersections with
   the relevant cycle are isolated affine roots of the seven sparse
   equations, despite unrelated higher-dimensional components, boundary
   components, component collisions, or points at infinity?
3. Is the origin-augmented affine mixed volume 658 legitimately an upper
   bound after mod-127 support shrinkage? Check the exact use (not the
   bibliographic provenance) of the arbitrary-characteristic isolated-root
   theorem and mixed-volume monotonicity.
4. Does an exact lift over
   F_127[s,v]/(s^N,H(w_i+s,v)) at a squarefree degree-190 fibre contribute at
   least N at each of the 190 distinct plane points to I(H,pi_*Z)? Check
   direction of maps, branch uniqueness, ramification, and pushforward
   multiplicities.
5. Is projective Bezout correctly applied to an effective pushed-forward
   cycle when no component equals H, giving I(H,pi_*Z)<=190*658?
6. Are the 80 order-8 fibres distinct from w=25, and does the self-contained
   sum 704 give the strict contradiction without any unstored baseline
   hypothesis?
7. Identify any hidden properness, equidimensionality, saturation, reducedness,
   or field-extension assumption. Distinguish a repairable exposition gap
   from wrong mathematics.
8. Enforce the scope firewall: no degree-one, all-contact, characteristic-zero
   no-merger, Taylor-realization, trajectory, or JC2 conclusion.

Write only
`xmodel/max12-912-order3-nu-q8-sparse-contact-component-review-claude-20260825.md`.
Give a verdict `CONFIRMED`, `CONFIRMED WITH REPAIRS`, or `REJECTED`; enumerate
every issue and the cleanest exact repair. State explicitly which numerical
count you reviewed. Do not edit any producer or frozen artifact.
