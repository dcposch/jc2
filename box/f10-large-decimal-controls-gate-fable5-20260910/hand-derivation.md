# Hand derivation and static checks (no execution), 2026-09-10 05:19-05:27 UTC

Fixture: p = monic algebra.modulus() (rank 7, premise), f1 = T^2, f2 = 1 + N T + T^3, f3..f9 = 0, q = 1, N = 10^7421 + 1.

Solver path (solver.py generic_candidate, by reading only):
- project: f1 degree 2, f2 degree 3; minimum nonzero degree 2, pivot 0; leading coefficient [1] is a unit, no split; one leaf, d = 2, e = 7.
- rows = 7*2 = 14, columns = 8*14 = 112, one rref; target q^5 = 1 -> vector (1,0,...,0).
- f2 columns mod T^2: j=0: v^l (1 + N T) -> (v^l, N v^l); j=1: v^l T -> (0, v^l). 14 independent columns, target column not a pivot -> UNIT.
- solution: h2 = 1 - N T. numerator = 1 - h2 f2 = N^2 T^2 - T^3 + N T^4; / T^2 -> h1 = N^2 - T + N T^2, remainder 0; inverse 1; CRT idempotent 1.
- identity: (N^2 - T + N T^2) T^2 + (1 - N T)(1 + N T + T^3) = 1.
- witness index (i*26+j)*7+ell: 0 -> N^2, 7 -> -1, 14 -> N, 182 -> 1, 189 -> -N, others 0. Matches helper 252-255.

Old solver first decimal site (predicted, not observed): fmpq built from integer arguments (179-180); str() of the fmpq entry is FLINT output; int(pieces[0]) at rational() (old numbering ~218-220) on -N (7422 digits) trips the 4300 limit with ValueError containing both required substrings.

Mutation: h1 constant N^2 -> N^2 + 1 adds T^2 to total[2][0]; canonical spelling; checker.py:135 message is the exact expected failure.

Astra report seal check: head -c 9799 of the charged report hashes to 01d1064403a43eb73ff58dbfe60da7f70efd693ee289dcd8136c0eb4fe43ff00, equal to its Seal line.

Interface omission found: helper line 130 requires INPUT absolute with parent == package root; EXECUTION-INTERFACE.md says this only for OUTPUT.
