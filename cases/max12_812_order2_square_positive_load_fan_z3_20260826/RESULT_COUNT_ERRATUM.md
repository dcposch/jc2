# Result counting erratum

The earlier report bytes, preserved in `RESULT_V1_PRE_COUNT_CORRECTION.md`,
incorrectly called the input an eight-form fan and described all 1,016 solver
queries as active sets.  The preregistration and source list seven forms:

```text
AC,C2,RA2,A3,kR3,kRC,kA2.
```

The exact count is

```text
(2^7-1) nonempty active sets * 8 zero/positive boundary patterns = 1016
```

candidate active-set/boundary pairs.  The numerical output—80 feasible, 936
UNSAT, 39 distinct feasible active sets—and every witness are unchanged.
`RESULT.md` is the corrected report.  Both versions already state that this
seven-form arrangement is source-incomplete and navigation-only.
