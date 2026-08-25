# Preregistration — witness-first diverse Q9/Q8 search

Run 24 deterministic, independently keyed combined-direction states in the
frozen Q9 chart.  Set raw Q9 chart trits `t6=t8=0` and the current canonical
Q8-kernel trits `s15=s17=0`, but hash-fill every other `t` and `s` coordinate.
State zero is the reviewed negative control.

At each state:

1. reconstruct Q9 from the pinned integer source and assert all 23 rows;
2. solve the exact Q8 affine system, add the selected canonical-kernel point,
   and assert all 22 rows;
3. solve Q7; if compatible, exhaust its entire `3^9` affine fibre;
4. compare the recursive high carry with the literal integer determinant
   divided by 243 at every point; and
5. emit every exact high-row-zero witness, stopping no other lane.

A hit is only a finite next-high survivor and must be replayed before a
source-derived smooth-Hensel Jacobian test.  A no-hit result is sampled scope
only, never a full-fibre exclusion.

