Act as an independent hostile arithmetic/algebraic-geometry referee.  The
producer is GPT-family; you are the required different-model reviewer.  Read
in full:

- `xmodel/as-fonly-residue-ball-collision-compactness-theorem-20260825.md`;
- every text/source/result/metadata file under
  `cases/as_fonly_residue_ball_collision_20260825/`;
- only the minimum surrounding campaign material needed to understand what a
  complete fixed-support AS lift means.  Do not credit filtered carry states
  or incomplete determinant-row systems.

Audit, rather than merely summarize, the exact theorem and its firewalls.

1. For a polynomial map over `R_n=Z/3^n Z` with literal polynomial identity
   `det J(F)=1` and reduction `(x-x^3,y)`, prove or refute that each of the
   three source residue balls over `(0,0),(1,0),(2,0)` maps bijectively onto
   the target ball over `(0,0)`.  Check the Taylor induction over a
   non-domain, uniqueness at every digit, and the unit x-separation.
2. Distinguish moving Hensel preimages from collisions at fixed marked source
   representatives.  Check that no compatibility of independently found
   finite-level collision points is being assumed.
3. Attack the fixed-support compactness step.  Determine whether nonempty
   complete coefficient schemes modulo arbitrarily deep powers (with one
   fixed finite support and one fixed AS residue component) really yield a
   compatible `Z_3` coefficient vector, even if the exhibited finite-level
   solutions are unrelated.  Check the nested closed-set and finite-tree
   formulations, determinant coefficientwise exactness, and every hidden
   finiteness hypothesis.
4. Attack the transfer from the resulting `Q_3` collision point to a
   `Qbar`, then complex, point of the finite-type coefficient/collision
   scheme.  Check properness under field extension, the unit localizer,
   constant Jacobian, support/degree preservation, and whether the result is
   genuinely a JC2 counterexample conditional on all-depth map survival.
5. Audit the mod-9/mod-27 positive controls and singular-J negative control
   from source.  These controls are regressions only, not evidence for
   all-depth survival; enforce that distinction.
6. Search for scope leakage involving filtered rows, changing supports,
   gauge states, depth-dependent normalization, or denominators.  State the
   smallest repair for every defect, including terminology such as
   `finite integral scheme` versus `finite-type affine scheme`.

Give one final verdict: `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `BLOCKED`.
Do not use Bash, CAS, network access, or write/edit any file; disclose that
limitation.  Return a self-contained review on stdout, at most 10,000 words.
End with exactly one verdict token on its own line.
