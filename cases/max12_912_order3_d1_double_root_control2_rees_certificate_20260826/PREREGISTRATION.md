# Preregistration: control-2 initial-ideal monomial certificate

Date: 2026-08-26  
Execution: registered Amazon EC2 only

This source-identical follow-up consumes the pinned expanded Rees-v2 B input
and does not change any equation, weight, load, support mask, or residue.  It
prints the complete standard basis `GH` of the special fibre before torus
localization, recomputes localization independently with `sat_with_exp`, and
requires:

```text
GH : TORUS^infinity = (1),
TORUS^e reduces to zero modulo GH,
TORUS=Lambda*tau*rho*q1*q0*r2*r1*r0,
```

where `e` is the exact saturation exponent emitted by Singular.  It retains
the original inverse-variable torus computation as a second check in the same
run.  A clean result is an explicit monomial-in-initial-ideal certificate for
the one frozen support and weight only; it is not whole-fan coverage.

Pinned base input:

```text
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

