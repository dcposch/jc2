# Pre-run diagnostic: `K48` is not a standalone unit test

Date: 2026-08-26

Status: **HAND REDUCTION AND MANDATORY NEGATIVE CONTROL; NOT PRODUCER
EVIDENCE.**  This note was added after the V2 source archive was frozen and
is intentionally not part of its `FREEZE.sha256`; it does not alter the
live compiler bytes.

The earlier byte version with SHA
`63192d95d96cf38b4c4b5a585194f7caf12f103b97fd254a62cf761a60e1378d`
is **SUPERSEDED**: it contained a factor-two slip in the `d6` coefficient
(`-p^5/16` instead of `-p^5/32`).  No producer consumed that version, and
the qualitative cancellation conclusion was unchanged.

Write the grade-44 rows from the frozen `H=16,q=6` predecessor as in
`RESULT.md` of the preceding mixed-face package.  On `D(p*m)`, rows `C6`
and `C2` give successively

```text
d2=d6*p^2/4+6*(r0*m^2-y^2)/p^2,

dm=3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8.
```

Therefore the transverse-deviation combination in the raw equality
functional reduces to

```text
L=-9*d6*p^5/128+d2*p^3/8-p*dm
 =-d6*p^5/32+(15*p/8)*(r0*m^2-y^2).
```

Using the two grade-44 survivor charts gives

```text
D(x): y=0, r0=x^2/(2*p)
  K48=(-2*p*m^3+a*(-d6*p^5+18*m^2*x^2))/32;

D(y): x=0, r0=-y^2/m^2
  K48=(-2*p*m^3+a*(-d6*p^5-72*p*y^2))/32.
```

On either chart `d6` is still free at grade 44 and has coefficient
`-a*p^5/32`, a unit on the registered equality open.  Hence `K48` alone
can be cancelled and must never be reported as a direct unit.  This is the
mandatory negative control for the V2 output.

Only the complete source rows at grades 45--48 can determine whether
earlier lifting equations constrain `d6`, whether another grade-48 row is
a unit, or whether both charts survive.  If the full system leaves `d6`
free, the correct producer verdict is survivor, not exclusion.
