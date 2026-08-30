# Hostile review: reduced finite normal-quadratic F5 bridge

You are GPT-5.5 xhigh, an independent hostile algebraic-geometric reviewer
for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2` on frozen review basis
`06d8f99967ffb3ce34145d30f1e27e23dd07331b`.

Read and review in full:

```text
413489b037be9533337f53e6bd104549c2ef663c4afd27927230d469ac1b1128
  xmodel/bd-a2-normal-singular-reduced-finite-f5-bridge-sol56-20260830.md
  body 12123 / 7b5ab1f2cc6c2419f9325882f080d22d0cf53e55ae4fd250dfd5aafe80f424f7
  manifest 46028e2beaf995df1988c33cfa137bb485d7da5d003cd63ca844f2ebea377b5e
```

Read the five charged integrations in its Section 0 and enforce their exact
hypotheses. This packet was written specifically after correcting the false
shortcut that all ADE singularities lie at infinity: missed affine
ramification/singular loci remain allowed.

Independently reconstruct and attack:

1. In a finite hypersurface chart `f(u,v,z)=0`, verify at isolated normal
   singular points that the ramification Cartier divisor is still represented
   by `f_z`, that `H cap R` is `h=h_z=0`, and that a component common to
   reduced H and R would be z-independent and contradict projective
   finiteness. Identify any hidden smoothness, flatness, purity, or coordinate
   assumption.
2. Verify that connected total transforms of H and R inside the first-leg
   rational forest still make two separated boundary-critical support sites
   impossible when X has Du Val singularities or affine singular trees.
   Treat reducible ramification, shared exceptional trunks, coincident
   branches at one site, and common strict carriers correctly. The theorem
   claims only one support site, not one ramification branch.
3. Recheck the intrinsic F1--F9 projection-critical counts and decide whether
   exactly F5 remains under reducedness plus finiteness. In particular attack
   F1's Riemann--Hurwitz step, F2/F4/F7 site separation, and the typing of
   F3/F6 as nonfinite rather than eliminated.
4. Conditional on the F5 point itself being Du Val, prove or refute
   `sum a=3`, the saturated distinct-line identity, and
   `delta_p(H)=h^t a/2+sum delta(H')`. Independently enumerate all connected
   local rows with `sum a=3` and `h^t a<=8`, including the two A3 embedding
   tags, and verify the claimed A2--A8, D4--D6 table and exclusions of A1 and
   D7--D9.
5. Enforce the correction: ADE trees on affine ramification remain live;
   smooth-point F5 `3+5` does not restore the old smooth global lattice when
   X is singular elsewhere. State the maximum safe theorem and exact next
   carrier/effectivity problem.

Small exact desk checks are allowed; no heavy local CAS or Singular. Return
an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), precise repairs, and a promotion-ready maximum theorem. Hard cap:
8,000 tokens and 28,000 UTF-8 bytes. Do not inspect, list, search, stat, build,
modify, or control `jc2-lean`; the process sandbox also enforces this. Do not
edit inputs or dependencies. Write exactly one report:

```text
xmodel/bd-a2-normal-singular-reduced-finite-f5-bridge-hostile-review-gpt55-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
