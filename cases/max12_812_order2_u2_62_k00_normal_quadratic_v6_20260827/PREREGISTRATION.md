# Preregistration: symbolic K00 quadratic-normal replay V6

Date: 2026-08-27

Status: **FROZEN SOURCE REPLAY; NO RESULT AT REGISTRATION.**

From the frozen ordinary tails, discard every lower-load monomial and make
the exact K00 transverse substitution

```text
C5=d5,                    C4=(3*C6^2+d4)/8,
C3=d3,                    C2=(C6^3+d2)/16,
C1=d1,                    C0=(C6^4+d0)/256.
```

Expand each of the seven unloaded tails through total normal degree two,
leaving `C6` symbolic.  Fail unless every constant and linear-normal term
is identically zero.  With `Qi` the exact quadratic-normal part of row `i`,
test the preregistered polynomial identities

```text
Q5 = -(3*C6^2/128)*Q1-(C6/8)*Q3,
Q6 = 0,
Q7 = -(C6^3/512)*Q1-(C6^2/128)*Q3.
```

This is an independent exact source replay, not a fit at `C6=1`.  It runs
only on registered AWS EC2, pins the tail JSON and reviewed one-parameter
source, writes canonical coefficient dictionaries for all seven `Qi`, and
fails closed on any source, type, truncation, or identity discrepancy.

Either outcome is local in scope.  A pass only removes redundant pure
quadratic equations from the next K00 normal-jet compiler.  A failure rejects
the proposed simplification.  Neither outcome decides K00 closure incidence,
constructs a strict arc, tests Taylor realization, or has a JC2 consequence.
