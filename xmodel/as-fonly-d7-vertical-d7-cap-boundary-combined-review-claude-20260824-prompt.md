# Hostile combined review — AS D7 source license and 13-component boundary

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`.  Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable.  This review has
two frozen targets whose conjunction is required:

1. `xmodel/as-fonly-d7-vertical-d7-cap-boundary-20260824.md`, SHA-256
   `3576de6cfba306230477fe7955e2ae159cc3dd241b4613b96d0ff57a05bbbfad`,
   case `cases/as_fonly_d7_vertical_d7_cap_boundary_20260824/`, manifest
   `5dfd46d47b27fb6d9bc094b24389ef39255e6a073fc7ef09ab8941b30ff49f65`,
   freeze `91a5c0a947d32287abb6223f41ceb385aaee4744e666e21748f77ae9ec70827a`.
2. `xmodel/as-fonly-d7-vertical-d7-source-license-20260824.md`, SHA-256
   `772d3627965037846f291ca5289c3cab26375e7bcea9edb095a95381fed84b27`,
   case `cases/as_fonly_d7_vertical_d7_source_license_20260824/`, manifest
   `7c23f45df72ec3cdbf7ff75ebeda50281fe140d0fe346277801873560f73135c`,
   freeze `bc1c126701bf8741e5d4171726c13d414a52bf462fe0d540e44d1947605a5a38`.

Run both manifests and both portable replays.  Inspect the programs rather
than trusting PASS, and independently attack:

1. The full integer source at order 27.  Starting from
   `(det J-1)/27=E1+M+3N` and `E=L/3+K+C_x+D_y=3E1`, verify the charged degree
   bounds `deg(L/3)<=5`, `deg(C_x+D_y)<=6`, `deg K(U0,V0)<=6`; verify that the
   double-Frobenius bracket divided by three vanishes modulo three and that
   derivatives of all degree-six Frobenius directions are three-divisible.
   Confirm independently that the complete degree-seven source is exactly the
   single-Frobenius `K/3` cross plus `M`, not a circular extrapolation of the
   D9/D8 generator.  Recompute or attack internal hashes
   `c5e95b5e...` for `[E1]_7` and `4cf87c8c...` for `[E1+M]_7`.
2. The eight D7 rows and forced substitutions.  Audit every accepted-row,
   D9/D8 pivot, and triangular-coordinate substitution, signs and factors in
   characteristic three, and the deduction
   `fua=fc=fd=R=0`, `T+fb+fv*h=0`, `d6_1=fa*h`, `d6_4=fb*h`.
3. The reconstruction of the seven displayed D8 equations in the eleven
   variables `(P,Q,s,w,h,fa,fb,fv,X0,X1,X2)`.  Ensure it is source-linked and
   that no radicalization or division by `h` altered the original scheme.
4. The stratified support proof.  Independently rerun/audit the eight minimal
   primes over `F3(h)`, their graph closures and dimensions; the six minimal
   primes of the `h=0` fibre; the equality of `H2` with the fibre of the stated
   global prime; all containment/noncontainment and dimension arguments that
   leave exactly five new boundary primes.  Look especially for a global
   component supported at `h=0` that the localization/fibre gluing could miss,
   or an embedded/nonreduced structure being misreported as a minimal prime.
5. The exact conclusion: thirteen global support components with histogram
   `dim4=8, dim5=3, dim6=1, dim7=1`.  The three optional direct full-ring
   decompositions are regressions only; neither their completion nor their
   noncompletion may be used as a proof dependency.
6. The literal-F3 census: independently check the rank table, 1245 compatible
   states, 3507 points, h-slices, rank-zero description, projection histogram,
   representative controls, and the one-row shrink.  Do not confuse literal
   F3 points with algebraic-closure geometry.
7. Scope: this is one D7 carry checkpoint only.  It supplies no next carry,
   recurrent bounded state, all-depth lift/no-lift, characteristic-zero map,
   counterexample, or JC2 conclusion.

State the smallest false identity or missing hypothesis if one exists, and
give the exact promotable sentence with strict scope.  Write exactly
`xmodel/as-fonly-d7-vertical-d7-cap-boundary-combined-review-claude-20260824.md`.
Do not edit any other file.  End with exactly one verdict: `CONFIRMED`, `GAP`,
or `REFUTED`.
