# Hostile review mandate: `BD-GAL` / closure of `BD-D2`

You are Opus 5 acting as a different-model hostile mathematical reviewer in
the plane Jacobian-conjecture campaign.  Work autonomously in
`/Users/dc/code/math/jc2` on frozen git basis
`0d7544ebd5cb12def6bac892646010301098be3c`.

Review in full:

```text
766a843a25eaf560840f15afa8971dd39246fc8b15290491d18e7f4a4c6bb7f7
  xmodel/block-descent-d2-galois-obstruction-producer-sol56-20260830.md
  body 13338 bytes / f03368f61177ea1cd1819832184d6df559412e3afdc20d30cef5aeb43f3d2bf8
```

Its binding dependency is:

```text
xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The claimed result is conditional on a hypothetical noninvertible Keller map
and a proper intermediate block field.  It says every irreducible branch
component of the finite-flat map `g2` has an unramified generic sheet; hence
`K/C(f,g)` is never Galois, and in particular `d2=2` / a two-block quotient
is impossible.  It explicitly does not exclude `d1=2`, even total degree,
non-Galois `d2>=3`, all imprimitivity, or prove JC2.

Independently reconstruct and adversarially audit all of the following.

1. Verify all charged hashes, basis, and the producer seal before using it.
2. Reprove or refute the missed-principal-divisor lemma, including whether a
   nowhere-zero regular function on source `A2` must be constant and whether
   injectivity is being used in the right ring.
3. Reprove the fixed-sheet theorem from an irreducible component of
   `V(p(f,g))`.  Attack the dimension/quasi-finiteness argument, dominance
   over the branch curve, closure inside `Y`, the claim that this closure is
   a component of `g2^{-1}(D)`, and the closed-to-generic unramified step.
4. Check the equivalence with a fixed block of geometric divisorial inertia,
   including residue-field/geometric-generic-point issues.
5. Audit the Galois-uniformity step for a possibly singular normal finite-flat
   surface over `C[u,v]`; identify exactly where characteristic zero,
   separability, and branch nonemptiness enter.
6. Independently derive the rank-two trace-zero normal form.  Check trace
   splitting, projectivity and `Pic(A2)=0`, the equation `w^2=h`, domain and
   normality consequences, squarefreeness, `R=V(w)`, and the final unit
   contradiction without assuming `Y` smooth or `g1` proper.
7. Attack the broader corollaries `Cl(Y)!=0` and nonmonogenicity.  A flaw in a
   decoration must not be conflated with a flaw in `BD-GAL`; itemize them.
8. Check the exact group-theoretic translation: `d1=[J:H]` is block size,
   `d2=[G:J]` is number of blocks; an index-two `J` is normal.  Test that the
   report does not accidentally exclude two-element blocks.
9. Try explicit algebraic/permutation countercontrols in degrees 2 and 3.
   In particular verify why degree-three transposition inertia with a fixed
   sheet evades the quadratic contradiction.
10. Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`,
    `GAP`, or `REFUTED`) and the maximum exact statement safe to promote.
    Name the cheapest decisive successor, with `BD-FIX3` only if justified.

Do not inspect, list, search, stat, build, modify, or control `jc2-lean` in
any way.  Do not run local heavy CAS or local Singular.  Desk algebra and
seconds-scale exact controls are allowed.  Do not edit canonical files,
scripts, or the producer.  Write exactly one report:

```text
xmodel/block-descent-d2-galois-obstruction-hostile-review-opus5-20260830.md
```

End the report with one standalone `<!-- BODY-END -->` line and no seal
block.  Formal data are not maps; finite fibres are not attainment; branch,
ramification, discriminant, image, and nonproperness loci must remain
distinct.
