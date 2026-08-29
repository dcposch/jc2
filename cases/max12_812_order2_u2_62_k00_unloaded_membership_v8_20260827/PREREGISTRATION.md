# Preregistration: repaired exact unloaded K00 membership and normal telemetry V8

Date: 2026-08-27

Status: **FROZEN REPAIR/MEASUREMENT DESIGN; NO ACCEPTED V8 RESULT AT REGISTRATION.**

V7's two raw executions were rejected because the generated Singular source
used unsupported `exit(N)` syntax.  Their unvalidated stdout suggested a
nonzero row-7 normal form, so V8 is not a blinded experiment.  V8 makes only
the registered syntax repair (`quit;`, with explicit fail markers checked by
an external validator) and adds frozen transverse-normal telemetry.  It does
not change the frozen tails, K00 coordinate map, source ideal, characteristic,
localization, or monomial order.

Let `r1,...,r7` be the unloaded (`k10=k6=k2=0`) frozen ordinary tails after

```text
C5=d5,                    C4=(3*C6^2+d4)/8,
C3=d3,                    C2=(C6^3+d2)/16,
C1=d1,                    C0=(C6^4+d0)/256.
```

The two exact-Q AWS lanes are:

1. **Direct localized:** standard basis of
   `(r1,...,r6,1-t*C6)` in
   `Q[t,C6,d0,...,d5,h]`, with the inert bookkeeping variable `h` last in the
   same global `dp` order.
2. **Kummer normalized:** set `C6=1` using the faithfully flat weighted Kummer
   normalization registered in V7, and compute in
   `Q[d0,...,d5,h]`, again with inert `h` last and global `dp`.

In either nonmembership branch, after the frozen reduced normal form `R` is
computed, substitute `di -> h*di` for all six transverse variables.  The first
nonzero coefficient of `h` defines the **lowest transverse-degree piece of
this frozen reduced normal form**.  Save and report:

- full residual term count;
- lowest transverse degree;
- leading-piece term count;
- exact leading-piece polynomial and its SHA-256;
- exact reconstruction and homogeneity checks.

This reduced-normal-form piece is order/presentation dependent.  It is not by
itself asserted to be the canonical associated-graded obstruction.  In
particular, the already proved symbolic quadratic syzygies must be respected
before interpreting a degree-2 piece.  If either accepted lane exposes a
first unresolved degree above the quadratic syzygies, the next bounded step
is a separate compatibility quotient modulo the lower-degree pieces of rows
1--6, followed by the registered K00 arc/divisibility reachability test at
`Lambda^19` retaining loads, `mu`, and `Jdet`.

Both lanes fail closed on any source/hash/type mismatch, unit source ideal,
Singular diagnostic, failure marker, timeout, missing/nonunique endpoint,
failed lift replay, failed transverse decomposition/homogeneity check, or
missing evidence.

Membership would say only that the unloaded row-7 coefficient polynomial is
redundant on `D(C6)`.  Nonmembership would identify a pure unloaded separator
for that ideal.  Neither outcome decides the full closure, Taylor
realizability, or JC2.
