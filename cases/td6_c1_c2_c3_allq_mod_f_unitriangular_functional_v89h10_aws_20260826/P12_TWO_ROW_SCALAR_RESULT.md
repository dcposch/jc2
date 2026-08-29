# TD6 V89H14 exact two-row/six-scalar P12 quotient split

Date: 2026-08-26

Verdict: **PASS as an exact producer-tier structure theorem.**

## Exact split

In the frozen V89H12 all-q, `F=0`, `D(U*H*B3)` scope, write the complete
P12/FIRST normal form as

```text
R(q,y) = c(q) + A(q)y
```

in the 18 frozen E3 coordinates, where y denotes the 16 quotient variables
that actually survive.  Literal inspection of all 166 exact normal-form
records proves:

- every entry of `A(q)` is zero outside coordinates 0 and 1;
- `c(q)` is zero outside coordinates 0 through 7;
- coordinates 8 through 17 vanish identically;
- coordinates 2 through 7 are six y-independent affine-linear compatibility
  equations, supported exactly in q3 through q14 and independent of q2.

The q2 coefficient block in rows `(0,1)` and columns `(y24,y27)` is exactly

```text
[[6, 8],
 [0, 4]].
```

Therefore the corresponding 2-by-2 determinant has q2-squared coefficient
24.  In particular `A(q)` has rank exactly two over the rational function
field `Q(U,V,q2,...,q14)`; the modular rank-two observation in V89H13 is an
exact structural fact, not a bad-prime accident.

The six scalar equations are frozen verbatim in
`P12_SIX_SCALAR_COMPATIBILITY_EQUATIONS.tsv`, SHA256
`2f888859f6a4f2e383cd43812b3f48e28aa6c1885ff66374f5e458aa138a2e51`.
Their 6-by-12 coefficient matrix in q3 through q14 has generic rank six over
`Q(U,V)`: at the denominator-safe rational point `(U,V)=(1,3)`, the columns

```text
q3,q4,q5,q6,q7,q9
```

have exact determinant

```text
-1656161280873829337287680.
```

One nonzero denominator-safe evaluation proves the symbolic determinant is
not the zero rational function.  It does not make that determinant a unit on
the entire registered open.

## Consequence for the P12-only route

Over the relevant fraction field, the six scalar equations can be solved for
`q3,q4,q5,q6,q7,q9` in terms of the other q variables.  Since q2 is absent
from them, leave q2 transcendental; the displayed 2-by-2 determinant remains
a nonzero polynomial with leading term `24 q2^2`.  After localizing at it,
the remaining two P12 coordinates can be solved for `y24,y27`, with the other
y variables free.

Thus the literal P12/FIRST/`F=0` system has a generic mixed-low-q rational
section after two explicit nonzero localizations.  In particular, a global
certificate placing the entire q-augmentation ideal in the radical of this
P12/FIRST system cannot exist.  Pure-axis obstructions such as V89H7 remain
valid; the section necessarily uses mixed low q.

This is a negative routing result for P12-only exclusion, not a JC2
counterexample: later CURRENT grades and literal total-source/source-map
conditions have not been imposed.

## Custody and firewall

Box02 and r6d both returned rc 0 with byte-identical stdout and all exact
artifacts.  The result artifact has SHA256
`48a3f53722df716affbb36445468293cd7e0a7be5198699f61df13d547088cea`.
No Singular qring was used.  No new factor was inverted as part of the global
theorem; the two nonzero determinants enter only in the explicitly localized
fraction-field corollary.

This theorem does not give a literal source point, total-Rees map, later-grade
solution, whole-TD6 closure, or JC2 result.  All computation ran on AWS and
`jc2-lean` was not touched.
