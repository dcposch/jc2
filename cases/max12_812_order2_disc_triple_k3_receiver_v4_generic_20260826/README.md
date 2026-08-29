# K3 receiver V4: generic `D(b*t)` coefficient-field control

Date: 2026-08-26

Status: **IMMUTABLE AWS-ONLY GENERIC-OPEN CONTROL; NO RESULT.**

The V3 polynomial-ring elimination is live but needlessly asks Groebner
elimination to rediscover generic inversion of `b*t`.  V4 changes the ring to
the exact coefficient field `Q(b,t,C,S)` (or its good-prime analogue), keeps
all correction/load/target variables polynomial, and removes the now-vacuous
final `b,t` saturations.  Every source row, K3 correction, valuation sentinel,
and V3 syntax/API repair is unchanged.

V4 decides only the generic point of the reduced K2 survivor on `D(b*t)`.
It says nothing about divisors in the parameter base, and cannot replace the
polynomial-ring V3 closure endpoint.
