# Preregistration: symbolic global-predecessor raw-Q7 gate

Date: 2026-08-25Z

## Frozen question

Within the aligned vertical `F`-only `D=7` chain, impose in one formula:

1. all 20 frozen full-C5/first-Cartier predecessor equations on the 30 raw
   predecessor trits;
2. the corrected degree-12, degree-11, and degree-10 source rows;
3. all 23 degree-nine source rows on 32 raw Q9 restoration trits;
4. all 22 Q8 source rows on 32 raw Q8 restoration trits;
5. all 19 Q7 source rows on 18 raw Q7 restoration trits; and
6. all 46 terminal rows in degrees 12, 11, 10, and 9.

The global formula has 112 ternary inputs.  It does not parameterize a
rank-stratum section and does not assume that the Q9/Q8/Q7 matrices are
constant across predecessors.  The exact integer-carry reconstruction also
reimposes the degree-12/11/10 rows as a source-honesty audit.

## Preregistered outcomes

- `SAT`: immediately freeze the model, then require independent direct
  integer replay of every predecessor/Q9/Q8/Q7 row, exact divided carry,
  recursive-versus-literal `/243`, and all 46 terminal coefficients before
  treating it as a survivor.
- `UNSAT`: treat it only as solver evidence until the exact SMT is bit-blasted
  to pinned CNF, a proof-producing solver emits DRAT/LRAT, an independent
  checker verifies the proof, and a hostile source/compiler review passes.
- `UNKNOWN`, timeout, overflow assertion, inexact division, missing source
  name, or failed control: stop with no mathematical conclusion.

## Required controls

1. Pin the first predecessor (`c5_5=2`, the other 29 coordinates zero) and
   recover the already frozen complete-fibre UNSAT result.
2. On the same pinned predecessor, omit only the 46 terminal rows; require
   SAT and direct integer source replay with at least one nonzero terminal
   coefficient.
3. If the global run is nonterminal, formulas may be pinned by a complete
   seven-trit structural base for a 79-base falsification/control fanout.
   Basewise negatives are not global coverage without an exact base list,
   disjoint manifest, checked certificates, and aggregate coverage proof.

## Refusal scope

Even a checked global UNSAT result would cover only the frozen aligned
vertical predecessor locus represented by the 11,881 Q9-compatible states.
The separate `a` and `g` endpoint families, nonreduced intersections, other
associated-top branches, cube mismatch, all-depth lifting, bounded support,
characteristic-zero algebraization, a counterexample, and JC2 remain open.

All formula emission, solving, proof production, and direct replay run on
AWS.  The local host is used only for source editing, hashing, and bounded
syntax checks.
