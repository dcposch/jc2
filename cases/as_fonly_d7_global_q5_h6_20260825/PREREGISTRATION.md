# Global Q5/H6,J6 accepted-fibre gate

Starting from the frozen global final-G8/Q6/high source compiler, retain the
complete raw accepted state: 30 predecessor, 32 Q9, 32 Q8, 18 Q7, and 16
homogeneous degree-seven Q6 trits.  Adjoin all fourteen homogeneous
degree-six order-81 digits `(H6,J6)`.

The exact new gate charges, without row reduction:

1. all six rows of `G5 + (H6)_x + (J6)_y`;
2. all sixty-three divided terminal rows `R12,...,R7`, recomputed with the
   sum of the H7/J7 and H6/J6 source cross-carries; and
3. every parent predecessor, corrected-top, Q9, Q8, Q7, final-G8, and Q6
   row and every exact division-by-three gate.

The complete formula therefore has 142 raw ternary inputs and displayed row
inventory

```text
20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63 = 197.
```

The five-row pointwise left-null certificates are labels/navigation only;
they do not replace the full 69-row Q5 gate.  Search the full unpinned
accepted fibre with at least two independent solver variants.  A SAT model
must pass a direct nested-integer replay of all 197 rows plus recursive versus
literal determinant agreement in degrees 12 through 7.  An UNSAT endpoint is
diagnostic until the emitted formula is independently bit-blasted and its
proof checked, with a terminal-omission SAT control and direct source replay.

Fail closed on any source hash mismatch, inexact division, replay mismatch,
overflow-bound failure, missing input/domain constraint, or discrepancy
between the recursive and literal terminal rows.

Strict scope: the displayed aligned `D=7` F-only accepted fibre represented by
the frozen predecessor compiler.  This is not a complete chronological map
modulo 243, an all-depth lift, an algebraization result, or a JC2 claim.
