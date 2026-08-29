# Hostile mathematical review: ACS / deficit-Euler / TDIC

You are Grok 4.6 acting as a different-model expert referee in affine
algebraic geometry, topology of polynomial maps, constructible Euler
characteristic, and plane-curve complements.  Work in
`/Users/dc/code/math/jc2`.

## Charged report

Read `xmodel/ideation-20260829T0002Z-opus5.md`, exact SHA-256
`542f6212a10f46c843ff886e7241155dc43963806e23738846082f3902fd8ac9`.
Review only its `ACS`, deficit-Euler `(star)`, `ACS-2`, and `TDIC` claims.
You may read exact cited local files by name, especially
`ladder/SHEET6-CLASSICAL.md`,
`xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md`,
and
`xmodel/vandobben2608-projective-bundle-jc2-boundary-infinity-review-codex-20260828.md`.
Do not read other submissions from the `20260829T0002Z` round.

## Required first-principles audit

1. For a generically finite polynomial Keller map `F:C^2->C^2`, prove or
   refute that
   `F:C^2\F^{-1}(A(F))->C^2\A(F)` is a connected finite étale cover of degree
   `td`.  Separate étale, quasi-finite, proper, finite, surjective, degree,
   and connectedness.
2. Audit the stratification used for `(star)`.  Does constant fiber cardinality
   on a smooth locally closed curve stratum make the restricted quasi-finite
   étale morphism finite étale/a topological covering?  Refine the strata if
   needed.  Re-derive the compactly-supported/ordinary Euler identity with all
   singular and component-intersection points.  State whether `e(C)` can be
   negative and whether the right side is a positive decomposition.
3. Attack every step of `ACS-2`:
   - smooth irreducible `A(F)` being an embedded `A^1`;
   - classification of connected finite étale covers of `G_m x A^1` as an
     algebraic, not merely topological, statement;
   - the unit-rank argument for irreducibility of `F^{-1}(A)`;
   - why the defining unit maps to a primitive `u^{plus-or-minus 1}` rather
     than `u^n`;
   - why nonzero fibers are embedded `A^1`s, AMS applies, and the final
     triangular-Jacobian calculation has no missing factor.
   Give the cleanest repaired theorem if the proof is incomplete.
4. Audit `TDIC`: meridian conjugacy for one irreducible component, exact local
   monodromy cycle type including fixed points, and its recovery from each
   coordinate pencil.  Check vertical/horizontal components, tangencies,
   projection degrees, component multiplicities, and whether equality should
   be a set, multiset, weighted set, or only a per-component statement after a
   generic target-coordinate change.  Decide whether the proposed banked
   residue-A `TDIC-SET` test is currently typed or is `NOT-TYPED`.
5. Attempt explicit countermodels with non-Keller generically finite maps and
   abstract étale/quasi-finite curve maps to expose each missing hypothesis.
6. Compare `(star)` to the existing fibre-side degree identity and state
   exactly what new information it supplies.  It is not a degree ceiling
   unless you prove one.
7. Identify every required standard theorem and its exact role.  Do not claim
   literature originality or source verification; this is a mathematical
   review, not the web sweep.

## Output

Write only `xmodel/acs-tdic-hostile-review-grok46-20260829.md`.

Give per-claim verdicts `CONFIRMED`, `REPAIR`, or `REFUTED`; fully corrected
theorem statements and proofs; exact scope and downstream consequences; and
the cheapest sound next discriminator.  End with a report-body self-hash.

No AWS, web, heavy CAS, canonical-ledger edit, repository-wide inventory,
commit, push, delegation, or any access to `jc2-lean`.
