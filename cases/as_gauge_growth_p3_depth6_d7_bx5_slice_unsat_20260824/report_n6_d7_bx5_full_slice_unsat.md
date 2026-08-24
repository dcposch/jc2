# AS gauge growth at p=3: the fixed a=0, b=x^5, depth-six cap-seven slice

Date: 2026-08-24

Status: **PROVISIONAL EXACT FINITE UNSAT**, pending an independent hostile
review or independently checked UNSAT certificate.

## Verdict

There is no simultaneous-gauge-cap-seven depth-six lift in the fixed
first-digit slice

\[
  a=0,\qquad b=x^5.
\]

More precisely, the exact finite system over base-three digits has no point
whose depth-five residue obeys all cap-seven support and determinant equations
and whose depth-six obstruction obeys both:

1. the exact cap-seven support conditions for \(P=A-A^3\) and
   \(Q=B S_6(A)\); and
2. the complete bounded-divergence/Cartier condition needed to correct the
   determinant by cap-seven final digits.

This closes only this fixed \((a,b)=(0,x^5)\) component.  It is not an
emptiness result for the full cap-seven locus.

## Exact setup

All arithmetic is coefficientwise modulo \(3^6=729\).  Write the depth-five
residue as

\[
 A=x+9c+27e+81g,
 \qquad
 B=y+3x^5+9d+27f+81h,
\]

where \(c\) has total degree at most five and \(d,e,f,g,h\) have total
degree at most seven.  The smaller cap on \(c\) is forced by the cap-seven
support of \(A-A^3\): a degree-six or degree-seven monomial of \(c\) creates
an uncancellable shifted term in \(-27x^2c\).

At depth six, possible final gauge digits are

\[
 A^+=A+243k,\qquad B^+=B+243\ell,
 \qquad \deg k,\deg\ell\le 7.
\]

The map and gauge definitions are

\[
 P=A-A^3,
 \qquad
 S_6(A)=\sum_{j=0}^{5}3^jA^{2j},
 \qquad
 Q=B S_6(A).
\]

The script first imposes the complete depth-five conditions modulo 243:

\[
 \deg A,\deg B,\deg P,\deg Q\le7,
 \qquad J(A,B)=1.
\]

It then imposes the exact depth-six conditions described below.

## Why the final digits can be eliminated exactly

Modulo 729,

\[
 P(A+243k)=P(A)+243k,
 \qquad
 Q(A+243k,B+243\ell)=Q(A,B)+243\ell.
\]

The omitted terms are multiples of 729.  Since \(k,\ell\) themselves obey
the cap, neither can cancel a support term of total degree greater than seven.
Thus the high-support rows of \(P(A)\) and \(Q(A,B)\) are exact invariants of
the depth-five residue.

For the determinant, put

\[
 R=\frac{J(A,B)-1}{243}\pmod3.
\]

Then

\[
 \frac{J(A+243k,B+243\ell)-1}{243}
 =R+k_x+\ell_y\pmod3.
\]

For total-degree cap seven, a polynomial is in the image of
\((k,\ell)\mapsto k_x+\ell_y\) exactly when:

- it has no term of degree greater than six; and
- every Cartier-cokernel coefficient
  \([x^{3r+2}y^{3s+2}]R\) vanishes.

Indeed, every remaining monomial can be integrated in \(x\) unless its
\(x\)-exponent is 2 modulo 3, and then it can be integrated in \(y\) because
the simultaneous Cartier case was excluded.  The resulting primitive has
degree at most seven.  Consequently the eliminated determinant rows are
necessary and sufficient for the existence of cap-seven \(k,\ell\).

## Exact p-adic support formulas

The solver uses the following identities rather than a generic symbolic power
expansion:

\[
\begin{aligned}
P={}&x-x^3+9c+27e+81g-27x^2c-81x^2e\\
   &-243x^2g-243x c^2 \pmod{729},
\end{aligned}
\]

and, with

\[
 S_0=1+3x^2+9x^4+27x^6+81x^8+243x^{10},
\]

\[
\begin{aligned}
Q={}&B S_0
 +54yx c+162yx e+486yx g+243y c^2\\
 &+324yx^3c+243yx^3e
 +162x^6c+486x^6e\\
 &+243x^8c+486dxc \pmod{729}.
\end{aligned}
\]

The portable negative-control replay independently expands the original
definitions and asserts that these Taylor formulas agree coefficientwise.

## Finite-system size

The digit variables are:

- \(21\) coefficients for \(c\) (degree at most five);
- \(3\cdot36=108\) coefficients for \(d,e,f\);
- \(2\cdot36=72\) coefficients for \(g,h\).

Thus there are **201 trit variables**.  The exact solver contains 546 Z3
assertions:

- 201 trit-domain assertions;
- 80 depth-five support/affine rows;
- 66 exact depth-five determinant monomial rows;
- 64 depth-six high-degree or Cartier determinant rows;
- 38 depth-six high-support rows for \(P\); and
- 97 depth-six high-support rows for \(Q\).

The five mathematical blocks total **345 equation assertions**.  No rectangle
of extraneous coefficients is used; every digit lives in the indicated
total-degree simplex.

## Result and resources

Z3 4.16.0 returns `unsat` on the frozen system.  On the producer machine the
frozen run used:

- 105.46 seconds wall time;
- 93.13 seconds user time and 9.35 seconds system time;
- 6,318,948,352 bytes maximum resident set size as reported by macOS
  `/usr/bin/time -l`; and
- 11,030,172,160 bytes peak-memory-footprint counter.

The frozen rerun transcript and resource file pin the corresponding values for
the exact frozen bytes.

## Negative control: Cartier alone is not enough

Before adding the map-support rows, the determinant/Cartier system had a SAT
residue in the same fixed slice.  Direct integer reconstruction gives

\[
 \deg(A),\deg(B),\deg(P),\deg(Q)=(7,7,9,11).
\]

Its determinant obstruction has no Cartier monomial, but its high support is
nonzero.  In particular,

\[
 P_{>7}=486x^5y^3+486x^8+243x^8y+486x^9,
\]

and \(Q_{>7}\) has thirteen nonzero monomials through degree eleven.  This is
an exact negative control for the temptation to identify Cartier solvability
with a full \(\mathcal B_{(3,6)}(7,7)\) lift.

## Replay

From the case directory, with Python 3 and `z3-solver` 4.16.0 available:

```sh
FULL_N6=1 python3 solve_n6_d7_bx5_full_slice.py
python3 probe_n6_bx5_cartier_survivor.py
```

The first command must print the five row counts and `full_status unsat`.
The second independently reconstructs the discarded Cartier-clean point and
prints its nonzero high support.

For a count-only build that does not invoke the SAT solver:

```sh
FULL_N6=1 COUNT_ONLY=1 python3 solve_n6_d7_bx5_full_slice.py
```

## Refusal scope

This package does **not** establish:

- emptiness for another first-digit pair \((a,b)\), or for the full
  simultaneous-gauge-cap-seven locus;
- emptiness at cap eight or higher;
- anything about the F-only tower in which \(P,Q\) are capped but canonical
  gauge variables \(A,B\) may grow;
- any statement at depth seven or above;
- existence or nonexistence of a compatible inverse-limit/polynomial lift;
- an \(A_\infty\) identification, a no-lift theorem, or a Jacobian-conjecture
  consequence.

The UNSAT result is exact for the displayed finite bit-vector system, but no
independently checked DRAT/LRAT-style certificate is included.  Promotion
should wait for hostile review of both the reduction and the solver encoding.
