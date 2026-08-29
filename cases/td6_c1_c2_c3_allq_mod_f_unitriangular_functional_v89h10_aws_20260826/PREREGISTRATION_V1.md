# TD6 V89H10 full-q unitriangular FIRST and q14 functional

Date: 2026-08-26

Status: producer diagnostic; no result claimed before AWS replay.

## Exact source scope

Retain all 22 licensed q jets

```text
q2,...,q14,q16,...,q24
```

as independent, untruncated base variables.  q15 remains absent only under
the reviewed target shear.  Rebuild literal P12 and all 38 original FIRST
rows from the frozen V85/V87 source chain, audit their registered
denominators before specialization, and then impose exactly F=0 on D(U).

## Raw q-prime basis gate

In degrees 0 through 39 construct

```text
q'(z)=1 + sum(e*q_e*z^(e-1)) + 25*z^24
q'_0(z)=1+25*z^24.
```

Compute both truncated reciprocals literally.  Emit and verify the two-sided
Toeplitz row map `R=q'/q'_0` and the induced two-sided g-coefficient column
map.  Require the exact raw coefficient identity

```text
M(q) * P(q) = R(q) * M(0)
```

for the forty coefficient rows of `f1*q' - 15*z^14*g1`.  This identity is a
raw FIRST statement only; it is not by itself permission to move the source
transport subspace.

## Transported FIRST gate

For the registered 38 constant pivot columns let A(q) be the specialized
original-FIRST pivot block, A0=A(0), and B=A0^(-1)A(q).  Set N=B-I.
Require exact affine-q telemetry and compute N^e over the full polynomial
ring through e=38.

- If N^e never becomes zero, stop before P12 division.  Preserve the raw
  q-prime theorem but make no transported-FIRST or functional claim.
- If N^e=0, form the finite Neumann inverse, emit it coefficient by
  coefficient, verify both products are the identity, recover all 38
  original FIRST sources, and only then reduce literal P12.

In the passing case emit the full original-FIRST relation, canonical P12
remainder, and complete q support.  Extract the pure-q14, empty-parameter,
E3-coordinate-0 coefficient and require exact equality with the frozen,
reviewed V89H7 functional.  Mixed-q terms are retained without truncation.

The result, even if passing, is confined to F=0 on D(U), with the previously
registered U/H/B3 denominator firewall.  It does not totalize q15 as a
source coordinate, prove a unit ideal or source-point exclusion, supply a
total-Rees lift, close whole TD6, or resolve JC2.
