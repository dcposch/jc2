# Hostile review mandate: `BD-A2-FIRSTLEG` log-Kodaira obstruction

You are Opus 5 acting as a different-model hostile mathematical reviewer in
the plane Jacobian-conjecture campaign. Work autonomously in
`/Users/dc/code/math/jc2` on frozen git basis
`0d7544ebd5cb12def6bac892646010301098be3c`.

Review in full:

```text
cc836852f92ee0a30dab9bfef3cb37b6f818ea2bb76d125ad95c8eecab44248f
  xmodel/bd-a2-firstleg-log-kodaira-obstruction-producer-sol56-20260830.md
  body 11262 bytes / 0238ee718560116ef9672f05de7bad23d75dfefba5d302ce10bfd0f1d1127ef6
```

Its geometric premise is provisionally supplied by:

```text
67e1305ba8dc452af6e120b37e24c102856ac5236d9140ffae9a0446c28261bc
  xmodel/bd-fix3-affine-linear-residual-control-producer-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The claimed theorem is stronger than the original first-leg gate: for an
affine-line torsor over `P1` with a horizontal punctured section whose closure
collides with the infinity section over at least two base points, the
complement has nonnegative logarithmic Kodaira dimension. Hence no dominant
generically finite morphism `A2->U` exists. Combined with the separately
reviewing affine-linear reduction, it would exclude every affine-linear
Miranda cubic block.

Independently reconstruct and adversarially audit:

1. Verify the charged hashes, basis, seal, exact dependency scope, and that the
   theorem does not consume an unreviewed stronger premise than stated.
2. Check that an affine-line torsor under a line bundle admits the asserted
   smooth ruled completion with infinity section, and that the closure of
   `R ~= P1\S` is genuinely a smooth section meeting infinity precisely over
   `S`; attack finiteness, possible vertical components, singular closure,
   and multiplicity issues.
3. Prove or refute `D_infinity-D_0=q^*E` in the Picard group and the existence
   of a rational `phi` with the stated divisor, including what vertical
   zeros/poles do to `q^*eta wedge dlog(phi)`.
4. Check existence and dimension of nonzero
   `eta in H0(P1,Omega^1(log S))` for exactly `#S>=2`, including the
   borderline two-point case.
5. Recompute the local tangency formula for arbitrary contact order `m`.
   Follow every blowup chart or give an invariant divisor calculation; verify
   that after an SNC resolution the pullback has at most simple poles on all
   horizontal, vertical, and exceptional components and no hidden interior
   pole. Look especially for an off-by-one in `t^(m-k-1)`.
6. Decide whether one nonzero log-canonical section really gives
   `bar-kappa(U)>=0`, and whether the chosen compactification/resolution has
   exactly the open surface `U`.
7. Hostile-check logarithmic Kodaira monotonicity for a dominant nonproper
   generically finite morphism. Is it always true in this direction? Can the
   rational extension be resolved using only boundary centers, does pullback
   of log pluricanonical forms remain logarithmic, and is pullback injective?
8. Recompute `bar-kappa(A2)=-infinity` from `(P2,H_infinity)` and confirm that
   a dominant morphism of irreducible surfaces is generically finite.
9. Audit the explicit cubic control form (5.1), its order-two boundary
   collision at zero/infinity, and whether it supplies a genuine independent
   sanity check rather than circular restatement.
10. Try to construct a counterexample to the abstract two-section theorem
    among ruled surfaces/torsors, or identify a missing hypothesis. Keep the
    redundant-sheet control separate because its target may have
    `bar-kappa=-infinity`.
11. Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`,
    `GAP`, or `REFUTED`), the maximum exact theorem safe to promote, and the
    cheapest successor if the affine-linear cubic family closes.

Do not inspect, list, search, stat, build, modify, or control `jc2-lean` in
any way; in particular do not run an unscoped parent `git status`. Do not run
local heavy CAS or local Singular. Desk algebra and seconds-scale symbolic
controls are allowed. Do not edit canonical files, scripts, dependencies, or
the producer. Write exactly one report:

```text
xmodel/bd-a2-firstleg-log-kodaira-obstruction-hostile-review-opus5-20260830.md
```

End the report with one standalone `<!-- BODY-END -->` line and no seal
block. A cover-side model is not a Keller map, and closure of the
affine-linear cubic subfamily is not primitivity or JC2.
