# Global final-G8/Q6/divided-high successor

Starting from the exact raw global-predecessor compiler, retain all 30
predecessor, 32 Q9, 32 Q8, and 18 Q7 trits.  After the Q7 restoration:

1. reimpose the final nine G8 source rows;
2. adjoin all 16 homogeneous degree-seven `(H7,J7)` trits;
3. impose all seven Q6 source rows; and
4. impose the complete following divided-carry rows in degrees 12 through 7.

The compiler must retain every exact division-by-three gate and all parent
source rows.  Search pinned structural base `0201020` first.  Every SAT model
must be replayed from the nested integer source and compared with the literal
degree-12-through-7 coefficients of `(det J(P,Q)-1)/243` after adjoining
`81(H7,J7)`.  UNSAT is diagnostic absent an independently checked proof.

No claim extends below degree seven, to all structural bases, to all depth,
to algebraization, to a counterexample, or to JC2.
