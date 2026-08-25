# AS F-only `D=7`: a pinned Q5 survivor has a one-row Q4 Cartier obstruction

**Status: PRODUCER EXACT AT ONE DISPLAYED Q5 STATE; PROVISIONAL PENDING
DIFFERENT-MODEL SOURCE/REPLAY REVIEW.**

## Result

Start with the corrected, direct-replayed base-513 Q5 SAT state and adjoin
all twelve coefficients of homogeneous degree-five order-81 digits
`(H5,J5)`.  The charged successor consists of

```text
5 rows:   G4 + (H5)_x + (J5)_y = 0;
63 rows:  recomputed terminal degrees 12,...,7,
197 rows: every displayed parent row, retained in the solver formula.
```

For the 68 new rows, exact source evaluation gives an affine system over
`F3` with 12 columns and rank pair

```text
rank(M) = 8,       rank([M|b]) = 9.
```

In fact the entire inconsistency has a one-row certificate.  With the row
convention `slot i = [x^i y^(d-i)]`,

```text
[x^2 y^2] (G4 + (H5)_x + (J5)_y) = 1.
```

The coefficient of every one of the twelve new variables in this row is
zero.  This is the characteristic-three Cartier/divergence row: the only
two possible contributions from a degree-five pair are
`3 [x^3 y^2]H5` and `3 [x^2 y^3]J5`, hence vanish in `F3`.  Thus no choice
of `(H5,J5)` restores Q4 at this parent state.  The terminal subsystem by
itself is consistent (rank pair `4/4`); the Q4 subsystem already has rank
pair `4/5`.

## Exact source and orientation checks

The replay first runs the frozen Q5 V2 integer replay, whose JSON SHA-256 is
`b5938b0529e994b7d1ff5755dce96baf8e97d6f5354a62f5892b50f4319564e1`.
It then evaluates zero, every basis vector, every doubled basis vector, and
all 66 pair sums in the twelve Q4 variables.  For every design point it
reconstructs the literal integer determinant and proves

```text
degree 4:      recursive Q4 row = [(det J(P,Q)-1)/81]_4 mod 3;
degrees 7..12: recursive terminal rows = [(det J(P,Q)-1)/243]_d mod 3.
```

This independently fixes the sign, quotient, monomial orientation, and all
nonlinear cross-carries used by the compiler.  The exact analyzer SHA-256 is
`b0196c3f4d6f758fdcdfb3a724f05b1beb38388f5529635058f0024b34622134`;
the result JSON SHA-256 is
`343ccec22361168a19ff97b3f1e162ef561e62464f0fefcdbb504ec127276d93`.
Boolector and Z3 also return UNSAT on the pinned 202-row SMT formula, but the
sparse exact certificate is the load-bearing evidence.

## Scope firewall

This kills exactly one displayed base-513 Q5 parent state.  It does **not**
kill the full Q5 solution fibre, any other structural base, all `D=7`, or an
all-depth lift.  Q3 through Q0 have not been restored.  Consequently this is
not a complete determinant-one map modulo 243, the residue-ball collision
theorem does not attach, and there is no no-lift or Jacobian-conjecture
inference.

The next exact gate is to express the same Cartier coordinate as a function
on the full Q5 survivor fibre.  If it is identically nonzero, the whole fibre
dies at Q4; otherwise its zero locus is the only licensed successor.

## Replay and custody

Source and wrapper are frozen under
`cases/as_fonly_d7_global_q4_h5_20260825/`.  On an AWS worker with the exact
pinned Q5 model:

```bash
MODEL_OUTPUT=/path/to/solver.stdout \
OUTPUT_DIR=/tmp/q4_affine_replay \
bash cases/as_fonly_d7_global_q4_h5_20260825/run_affine_certificate.sh
```

The Box02 custody archive has SHA-256
`3f952888d46e88b26e857220601fa2b3b7cbe26fad172bf3f5345ec61325e389`.
