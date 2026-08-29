# TD6 V89H10Q full-q transported-FIRST nilpotence quick gate

Date: 2026-08-26

Status: exact producer diagnostic only.

Rebuild literal FIRST with all 22 licensed untruncated q variables, impose
exactly F=0 on D(U), form the registered pivot endomorphism
`B=A(0)^(-1)A(q)`, and compute every power of `N=B-I` through power 38.
Emit each exact digest and size immediately.  If a power is zero, require
the finite Neumann inverse to pass both products and emit it explicitly.

This skips the separately running raw q-prime basis replay and all P12
compilation/division.  It is a viability/acceleration gate, not a theorem
about P12, a functional, denominator localization after pivot inversion,
source points, total Rees, whole TD6, or JC2.
