# Result: coefficient-only H16 grade-48 odd functional

Date: 2026-08-26

Status: **DUAL-AWS PASS; EXACT FIVE-TERM FUNCTIONAL.  PRODUCER-TIER RAW
COEFFICIENT, NOT AN EQUALITY-FACE VERDICT.**

The exact-Q Box02 lane and the independent `F65521` r6d lane completed in
under three seconds, with engine rc `0`, validator PASS, zero swap, three
abstract scalar controls, a direct raw-tail numeric series control, and both
previous rational witness controls.  All five modular coefficients are the
reductions of the exact-Q coefficients and the monomial supports agree.

Writing the leading source coefficients without suffixes, the exact output is

```text
[s^48](P7-E(s)^2 P3/32+E(s)^3 P1/64)
 = (3/32) a p^2 m^2 r0 -(3/32) a p^2 y^2
   -(1/16) a p^4 d2 +(3/128) a p^6 d6
   -(1/64) p^2 m^3.                                  (1)
```

The direct sparse route collected 663 abstract graph monomials, retained only
nine whose registered valuation can reach grade 48, and reduced their
coefficient to the five terms in (1).  It did not materialize a substituted
Faber row or compute a standard basis.

Both old witnesses evaluate to `-1/32`, as required.  However, (1) is not a
unit on the complete grade-44 survivor.  For example:

```text
D(x): a=p=m=x=1, y=0, r0=1/2,
      d6=20, d2=8, dm=-23/32;
D(y): a=p=m=y=1, x=0, r0=-1,
      d6=-70, d2=-59/2, dm=179/64
```

satisfy the grade-44 rows and make (1) zero.  These are inputs to the separate
seven-row odd-null controls; they prevent promoting the earlier two nonzero
witnesses into a general unit claim.

Exact sparse polynomial SHA:

```text
d71d23a8d88add84dc5e579b1fdcc3570fdde71c6d77440b68c5495f178f1386
```

This result is one fixed-representative raw grade-48 coefficient only.  It
does not prove predecessor reduction, equality-wall exhaustiveness, rational
regrading, source/Rees coverage, order two, maximum twelve, or JC2.

