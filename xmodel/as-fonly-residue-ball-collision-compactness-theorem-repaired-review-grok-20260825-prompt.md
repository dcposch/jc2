Act as an independent hostile arithmetic/algebraic-geometry referee.  The
producer is GPT-family; you are the required different-model reviewer.  Read
in full:

- `xmodel/as-fonly-residue-ball-collision-compactness-theorem-repaired-20260825.md`;
- every file under `cases/as_fonly_residue_ball_collision_repaired_20260825/`;
- the parent theorem and first-review prompt only as needed to verify that
  all identified repairs are present.

Audit the repaired theorem, not the live filtered AS solver state.  Check:

1. the unique digit-by-digit preimage in each of the three residue balls for
   any target above `(0,0)`, over the non-domain `Z/3^n Z`;
2. unit x-separation and the moving-versus-marked distinction;
3. nested compactness/Koenig for unrelated finite-level complete solutions
   on one fixed finite support, including coefficientwise determinant
   exactness;
4. the finite-type affine collision scheme and the `Q_3 -> Qbar -> C`
   transfer, with support allowed to shrink but not grow;
5. the repaired AWS control's explicit AS-reduction assertion and its strict
   regression-only scope;
6. the firewall that Q5/H6 still owes Q4 through Q0 and therefore cannot yet
   consume the collision theorem.

List only defects affecting the repaired theorem.  End with exactly one
verdict token on its own line: `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or
`BLOCKED`.
Do not use Bash, CAS, network access, or write/edit any file; disclose that
limitation.  Return a self-contained review on stdout, at most 2,500 words.
