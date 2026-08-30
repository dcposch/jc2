# Hostile review: quadratic trace-zero basis-change coverage

You are GPT-5.5 xhigh, an independent hostile algebraist and algebraic-
geometric reviewer for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2` on frozen git basis
`002d4a88b3496838a3ff8cf3bf55ec5cedbdb5a4`.

Read and review this sealed exact provisional producer in full:

```text
b15c7c7db287ddd1b6e0aae8caa48eff9e225d910f9735f9ad9b2ab947ba4f46
  xmodel/bd-a2-quadratic-basis-change-coverage-sol56-20260830.md
  body 16198 / bef1361e4eb32211b857a67290ecf335b2f284d3938023c83dbdb121fe841130
  manifest 473539389e1c03da32685a42e24a7ff1487873906ba59abc56380c8122dfa694
```

Its authorship basis is `f43ee99da2bc9f831d94e403dcd90622e87e8756`;
its producer commit is the review basis above. Read the charged proper-block
input named in Section 4 and enforce exactly where nonmonogenicity is used.

Independently reconstruct and attack:

1. Derive the Miranda binary-cubic transformation law
   `Phi_(e*g)(x)=det(g)^-1 Phi_e(gx)` with the report's coefficient
   conventions. Verify content-ideal and trace-discriminant invariance, and
   keep coefficient degree/projective infinity non-intrinsic.
2. Audit the arbitrary-matrix leading-section theorem. Check uniqueness of
   the top degree term, generic rank one of `g_m`, passage from its image line
   to a rational section with coprime homogeneous coordinates, actual
   divisibility of `Phi_d`, the bound `e<=d`, the three `(2,3)` factor-class
   patterns, and the inverse/kernel-flag statement. Look for cancellations,
   basepoints, or rank drops missed by the argument.
3. Prove or refute the classification of every entry-degree-at-most-one
   unimodular matrix as constant-equivalent to one linear elementary shear.
   Audit the use of the nilpotent conic in `P(sl2)` and the precise left/right
   constant frame changes.
4. Re-expand the shear exactly. Verify necessity and sufficiency of
   `b in C`, `a_2=0`, and `d_2=-a_1p-(b/3)p^2`; check the degree-two and
   degree-at-least-three shear cases. Then audit the dichotomy: `b=0` is a
   fixed generic root, while `b in C*` really makes the rank-three algebra
   monogenic. Decide whether the promoted proper-block hypotheses license the
   claimed constant-only affine-linear corollary.
5. Rebuild the counterexample
   `B=C[u,v,t]/(t^3-u^2t-v^2)`: irreducibility, normality, trace-zero frame,
   both Miranda tuples, nonconstant determinant-one change, unit content,
   lack of a constant projective root, affine/projective finiteness,
   discriminant, nonreduced infinity, and monogenicity. Check that it refutes
   exactly the broad heuristic claimed and no stronger proper-block theorem.
6. State the maximum result safe to promote and the exact remaining gap for
   entry-degree-at-least-two matrices. Emphasize that classifying changes
   among quadratic frames does not prove a quadratic frame exists and that
   discriminant degree supplies a lower—not upper—bound on minimal degree.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), precise repairs, and the cheapest decisive successor. Hard cap:
8,000 tokens and 28,000 UTF-8 bytes. Do not inspect, list, search, stat, build,
modify, or control `jc2-lean`; the process sandbox also enforces this. Do not
run local heavy CAS or Singular. Do not edit inputs, canonical files, scripts,
or dependencies. Write exactly one report:

```text
xmodel/bd-a2-quadratic-basis-change-coverage-hostile-review-gpt55-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
