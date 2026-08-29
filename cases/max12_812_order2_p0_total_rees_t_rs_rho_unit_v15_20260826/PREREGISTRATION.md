# T-rs rho-unit certificate V15 deployment successor

Date: 2026-08-26

## Purpose

V15 changes no mathematics and no generated Singular program from frozen V14.
It repairs only the remote custody working directory: V14 attempted to check a
package-relative `FREEZE.sha256` while its current directory was the repository
root, so both V14 lanes stopped before compilation or algebra.

V15 invokes the frozen V14 compiler and validator byte-for-byte.  Its runner
checks both the V15 deployment manifest and the V14 mathematical-package
manifest from their respective package directories before compilation.

## Registered lanes

- characteristic zero, direct saturation encoding, Box02;
- characteristic 65521, elimination-variable encoding, r6d.

The two lanes must independently emit the frozen V14 PASS tokens, all four
artifacts, both negative controls, the explicit rho inverse, and a validating
`RESULT.json`.  Any custody, compiler, engine, or validator failure is no
verdict.

## Scope firewall

A PASS establishes only the frozen V14 statement: on the actual total-Rees
T-rs chart, after restricting to D(k), the complete grade-12 prefix forces
rho to be a unit.  It is not a global Gate-T theorem and says nothing about
the remaining standard charts.

