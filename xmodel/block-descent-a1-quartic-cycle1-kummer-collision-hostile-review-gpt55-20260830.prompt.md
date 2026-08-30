# Hostile review assignment: quartic inverse-Kummer collision control

You are GPT-5.5, acting as an independent hostile mathematical referee. Work
only from the exact charged files below, plus a narrow primary-source check of
Formanek's theorem if needed. Do not inspect any sibling model report, `.log`,
`.run`, receipt, live ledger, uncharged file, or excluded nested workspace.
Do not modify Git or any repository file except the single required report.

Write your complete report to exactly:

`xmodel/block-descent-a1-quartic-cycle1-kummer-collision-hostile-review-gpt55-20260830.md`

and write no other file. End the mathematical body with a standalone
`<!-- BODY-END -->` line. Do not add a seal; the coordinator will custody-seal
the returned bytes after exit.

## Charged files

```text
bcc5148aba1a6cb095401ae8871e184ba6bb3e540395a23c40edc16cb0e363a8
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md
2e8e73514d1743cdc90934f099eccffc75ef2c4d5a07a5956bbb71cf8dc08aa5
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md.artifact.json
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
70c1e16270564af7138cdc9f4b4ef396a17b398698694330ee5146ec8a273f5d
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md.artifact.json
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190
  xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
baaf9e2253135c9885ccc420e99f3538441c8d664dfe724686a6d5b968e500b6
  xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md.artifact.json
```

First reproduce every hash and every seal/manifest. If any charged byte
differs, stop with `CUSTODY_FAIL`.

## Review obligations

Reconstruct rather than paraphrase every major implication and mark it
`CONFIRMED`, `REFUTED`, or `GAP`.

1. From `div(t-a)=mu Phi` and `div(c0 o pi)=Phi+E`, verify regularity of
   `r=(c0 o pi)^mu/(t-a)`, `div(r)=mu E`, the class calculation, and the claim
   that the two Kummer extensions are identical. Check normality, units,
   components, and multiplicities.
2. Audit the source factorizations `c0(F)=P S_F` and `c0(H)=xS`, including
   reducedness, squarefreeness, gcd claims, and the inference that `S(0,y)`
   has two distinct but not necessarily simple roots.
3. Recompute the full Euler ledger for `D0=Supp(Phi+E)`, especially
   `e(E)=3-3 delta_top+s-2o-3 epsilon_c`. Check constructible-fibre counts,
   intersection cardinalities versus multiplicities, omitted points, and
   tangential/multibranch singularities.
4. Locate and check Formanek, “Observations About the Jacobian Conjecture,”
   Houston J. Math. 20 (1994), Theorem 2. Verify that it applies to the Keller
   pair `H` and the chosen coordinate `x` exactly as used. Then audit the tower
   argument `M=K(t)`, degree arithmetic, and irreducibility of
   `c^-4 P_t(a+cX^mu)`.
5. Check that `t` is regular/integral over `V=A2-B`, that the coefficients of
   its minimal polynomial lie in `O(V)`, and that `O(V)[t]` is a free
   rank-four order normalized by the finite-etale algebra. Identify any
   hidden separability, connectedness, or field-versus-product issue.
6. Audit the norm identity `P_t(a)=lambda b^k c0^mu`, including the divisor at
   the generic point of `C0`, the unit group of `O(V)`, the meaning and sign
   of `k`, and behavior at the ramification boundary.
7. Audit the discriminant/index identity and the claim that a self-collision
   forces monogenic-order nonnormality locally along `u^mu-v^mu=0` without
   ramifying the normalized etale cover. Check transverse and tangent cases,
   and whether equality of two `t` values really follows on the asserted
   sheets.
8. Verify or refute each completed-local rank-four control, including
   regularity/flatness, fibre partitions `(2,1,1)`, `(3,1)`, `(2,2)`, the
   inverse-Kummer factors, and precisely what they fail to globalize.
9. Check the `K_U~0`, adjunction, normal-bundle, duality, and conductor
   firewalls. Look for a genuine overlooked global intersection or canonical
   contradiction; do not import projective degrees without boundary terms.
10. Seek a decisive successor: test the index-at-infinity, second-fibration,
    and companion-resultant gates. If none follows, identify the smallest
    exact missing lemma or counter-control. State the maximum-safe theorem,
    every correction and blast radius, and whether the one-cusp horn remains
    open.

Do not infer an independent `mu^2` divisibility, a second bad ruling fibre, a
global cover from local models, a counterexample, or JC2 unless actually
proved.

No `charge_basis` line is expected unless you assert a genuinely new rational
exit price under the campaign schema; ordinary hashes and geometry are not a
charge basis.
