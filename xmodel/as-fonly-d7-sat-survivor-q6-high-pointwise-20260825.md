# AS F-only `D=7`: the three displayed terminal survivors die at the next source-typed gate

**Status: PRODUCER EXACT AT THREE DISPLAYED POINTS; PROVISIONAL PENDING
DIFFERENT-MODEL SOURCE/REPLAY REVIEW.**

The global-predecessor race returned three exact solver models that pass the
encoded Q9/Q8/Q7 and degree-12-through-9 terminal rows.  This report asks the
strictly next question for those points; it does not replace a whole-fibre
search.

The first omitted row is the final degree-eight source row recomputed after
the Q7 restoration.  Direct nested-source replay gives

```text
base 303: final G8 = 2*x^8,
base 513: final G8 = 2*x^8,
base 519: final G8 = 0.
```

The final G7 row and all previously encoded terminal rows remain zero in all
three controls.  Thus the first two points stop before the next division;
this also demonstrates why the filtered state cannot be treated as a
chronological mod-81 map.

For base 519, adjoin the licensed homogeneous degree-seven fourth digit
`(H7,J7)`.  The seven Q6 rows and all following divided-carry rows in degrees
12 through 7 form a 70-by-16 affine system over `F3`.  Exact elimination gives

```text
rank(matrix) = 16,
rank(augmented) = 17,

2*Q6[x^4*y^2] + 2*Q6[x^5*y] + R9[x^7*y^2] = 2,
```

and the left side annihilates every H7/J7 column.  Hence no choice of these
16 digits advances this displayed base-519 state.

The result is deliberately pointwise.  Bases 303, 513, and 519 each have
many other accepted Q9/Q8/Q7 states, and the formula that reimposes final G8
and solves Q6 globally is a separate successor.  Nothing here excludes a
structural base, all `D=7`, an all-depth formal lift, a characteristic-zero
map, a counterexample, or JC2.
