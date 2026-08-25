# Preregistration: whole-Q5 Cartier/Fitting preprocessing

Date: 2026-08-25

## Source and target

Consume exactly

```text
../as_fonly_d7_global_q5_q4_cartier_20260825/
    solve_global_q5_q4_cartier.py
```

at SHA-256
`161287467d04d9ba769a09844405d7fcc7f0d90b53099217e836fd4e9febcdaf`,
and the exact 79 compatible structural bases at SHA-256
`bc9d6c9ed4f9103fe0a30bccddf1f73bfaaa5be87f6f060eb26b43f7cb0e7b52`.
The parent internally pins its complete transitive compiler ancestry.

The target is the same complete 198-row aligned Q5/Q4 formula.  No source
row, divided-carry constraint, terminal row, nilpotent state, or rank-drop
stratum may be removed by generic division or radicalization.

## Exact preprocessing gate

1. Reconstruct the parent solver and identify every assertion involving the
   16 Q6 and 14 Q5 restoration digits.
2. Separate only their digit bounds from the source equations.  Every other
   restoration-dependent assertion must be an equality modulo three.
3. Extract the exact affine coefficient matrix and right column by evaluation
   at zero and the 30 coordinate basis points.  Prove in one symbolic solver
   query that the reconstruction agrees on the whole ternary input cube.
4. Record the dependency set of every matrix entry.  It is an error, not a
   heuristic surprise, if it extends beyond the named predecessor digits.
5. Over all 79 compatible structural bases and every assignment of whatever
   remaining matrix-control digits the source actually exposes, exhaust the
   coefficient matrices.  Canonicalize each by exact F3 rank and left-null
   data; retain all rank strata.
6. Record the Q4 `[x^2y^2]` Cartier expression, its exact dependencies, and
   the assertion tying it to zero.  Do not infer that it is a unit or that
   its zero locus is empty merely from matrix rank.

The first run is a compiler/stratification theorem and a generator input for
later reduced formulas.  A reduced formula may replace the 30 restoration
variables only by an equivalent complete left-cokernel system on each exact
matrix stratum.  SAT still requires reconstruction and direct integer replay;
UNSAT still requires a checked proof or independent algebraic certificate.

## Controls and refusal scope

- The parent omission control remains load-bearing.
- Preserve rank-zero, rank-drop, repeated, and nonreduced predecessor states.
- Any non-affine restoration row or matrix entry with an unclassified
  dependency fails closed.
- This neither restores Q3--Q0 nor proves all-depth survival/no-lift,
  characteristic-zero algebraization, a counterexample, or JC2.
- All substantive execution is AWS-only.

