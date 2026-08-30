# Hostile review: F5 local different and `3+5` attachment split

You are Opus 5, an independent hostile algebraic-geometry reviewer for the
plane Jacobian-conjecture campaign. Work in `/Users/dc/code/math/jc2` on
frozen git basis `1efd7a76538e3fcdf51b999563262afc40d58947`.

Review this sealed exact producer and its promoted dependencies:

```text
8a1c3c50281a9c55b4dcf21c7c5a33ef574b4bfc59d10eb18456528171bbbb72
  xmodel/bd-a2-f5-local-different-two-branch-producer-sol56-20260830.md
  body 9253 / 61931ec73f0b6bd13cfef1d75e9c6c4bdd6d36a2364631b898131f66b19aa897

255bd0ba04e1c0a428a18caa70e73bc35895026c5857f629ed855cee79a8f803
  xmodel/bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md
  body 8727 / f334970e50271ce851c55ec55cfc30ba9f00054b4d81179e437b669350dd878b

e3dc96f07825ea882edc3d2701e9f0a0357ae863c062ad695d9377a37aa2b761
  xmodel/bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md

410de2f569e2ad5599152fdd9414198f012dbdced7d17c5a51dde0096fe4601e
  xmodel/bd-fix3-quadratic-discriminant-conductor-coordinator-integration-sol56-20260830.md
```

Independently reconstruct and attack:

1. Derive the exact local normal form for an F5 divisor
   `(0,1)+(1,1)+(1,1)`: after allowable projective/local coordinate changes,
   can its three branches always be written
   `z`, `z-v`, and `(1+v)z-v`? Check the nonzero derivative, contact-two,
   global intersection-number, and unit claims. Identify any hidden moduli or
   coordinate hypothesis that affects the different.
2. Starting from a smooth incidence equation restricting to this divisor,
   justify `f=h+u*g`, `g(0)!=0`, the identification of the source different
   with `f_z|X`, and `u=U(v,z)` of order at least three. Recompute the tangent
   cone of `r=f_z|X`; decide rigorously whether distinct factors
   `(z-v)(3z-v)` force exactly two reduced smooth analytic branches in the
   completed local ring, independently of all higher coefficients.
3. Recompute the local intersection length. Verify
   `disc_z(z(z-v)((1+v)z-v))=v^8`, the resultant/length passage, and the
   branchwise split `3+5`. Check carefully that the symbols `D_tr,D_tan`
   denote the actual Hensel branches rather than their tangent lines and that
   tangency lower bounds plus additivity really force exact `3` and `5` for
   arbitrary unit `g`.
4. Audit object typing: source Cartier ramification/different versus its
   reduced support, target trace discriminant/reduced branch,
   normalization-index divisor, and conductor. Check the statement that the
   target discriminant restriction is only a numerical norm control.
5. Rebuild the global inference. If the two local germs lie on one global
   irreducible `Rbar`, do they give two normalization branches over the F5
   point and trigger the promoted multigraph cycle lemma? If they lie on
   distinct components, does `R_red` necessarily become reducible? Verify all
   smoothness, finiteness, reduced/squarefree infinity, first-leg, and
   no-boundary-component hypotheses, and state the maximum safe composition
   with the promoted F1/F2/F4/F7 exclusions.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), the maximum exact theorem safe to promote, every correction, and
the cheapest next finite component-lattice control. No coefficient
realization, occurrence, map, block closure, counterexample, or JC2 claim.

Hard output cap: at most 7,000 tokens and 25,000 UTF-8 bytes. Do not restate
long inputs. Do not inspect, list, search, stat, build, modify, or control
`jc2-lean`; the process sandbox also enforces this. Do not run local heavy CAS
or Singular. Do not edit any input, canonical file, script, or dependency.
Write exactly one report:

```text
xmodel/bd-a2-f5-local-different-two-branch-hostile-review-opus5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
