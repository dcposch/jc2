# Instrument re-strategy round 4 (GPT 5.6 Sol, equal co-researcher)

Repo /Users/dc/code/math/jc72108, full access. NEW DATA since your
round 3 (read notes.md tail + SHEET6-DIRECTIONB sections 7.S-8.S):
(1) your CORE2 diagnosis was right — the fixed presentation solved in
11 SECONDS per fiber: D21 window NONEMPTY mod p at all 3 primes,
13-dimensional, point-rich, pole scales pinned; (2) 12/12 sampled
points DIE at the D23 Row_22 block; (3) the D23-core (hybrid: 38
compressed + 22 pivot + 10 QUADRATIC Row_22 rows; 87v/77eq/59.3k
terms/deg<=13) TIMED OUT at 12h/-t4 on all 3 lanes, mains plateaued
at 121G for ~5h (a 48h extension lane now runs with -v2 telemetry at
box01 ~/jc72108/core23_ext.v2log); (4) DEPTH-STAB banked: the kill is
depth-free; a live verdict needs a point with Jacobian-minor
valuation e <= 11 at D23.

THE QUESTION: how to decide the D23 system? Options (rank, add your
own, name the single best move with gates):
(a) the running 48h extension;
(b) smarter D23 presentation: partial elimination into Row_22 (your
    round 3 rejected the FULL version at 4.97M terms — sweet spot?);
    FIX the GB-pinned W1/W2 values as equations (shrinks the system);
    chamber the 13 free directions of the D21 locus;
(c) FIBER-FIRST RESTRICTION — likely the big one: the D21 fiber
    solves instantly and its solution variety is 13-dimensional;
    parameterize the 397-element GB's solution set and evaluate the
    10 Row_22 rows ON the parameterization: the decision becomes an
    elimination in ~13 parameters instead of 87 variables;
(d) a different engine on the D23-core;
(e) rent iron.

Deliverable: xmodel/sol-instrument4.md. No repo modifications except
it. No git.
