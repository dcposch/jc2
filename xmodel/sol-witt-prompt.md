# Task: execute your Witt-Bockstein lane (your lateral idea #1)

You are GPT 5.6 Sol, repo /Users/dc/code/math/jc72108 (full access,
python3). DC green-lit your top-ranked lateral idea (xmodel/
sol-lateral.md rank 1): the Witt/Bockstein search around
characteristic-2 collisions, building on your pilot result that the
3D counterexample map itself has a NONZERO Cartier obstruction and
cannot lift modulo 4 with any correction support.

Execute the first full week-scale step you specced in the doc:
1. Formalize the obstruction calculus: for a char-2 Keller-collision
   datum (define the object precisely — your doc's collision locus),
   the Witt-vector lifting obstruction as a computable class; your
   pilot showed the 3D map's class is nonzero — write the general
   computation as a reusable exact engine (cases/witt_check.py).
2. The SEARCH: enumerate the tractable stratum of char-2 collision
   data in TWO variables (the JC2-relevant case — state precisely how
   a vanishing obstruction would feed a char-0 counterexample
   candidate, and what it would NOT yet prove), and compute the
   obstruction class on each. Any VANISHING instance = flag loudly
   with the full datum banked (that is a disproof lead, not a
   disproof).
3. Honesty: if the two-variable stratum is empty or the obstruction
   provably never vanishes there (which would itself be a nice little
   rigidity result — state and prove it), say so; a clean negative
   closes the lane.

Deliverable: xmodel/sol-witt.md (exec summary: VANISHING FOUND /
NEVER-VANISHES-PROVED / STRATUM-EMPTY / PARTIAL + counts), the engine,
citations. No repo modifications except your output file + the engine.
No git.
