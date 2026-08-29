# V82QSD CURRENT denominator diagnostic — producer report

## Verdict

All nine bounded AWS lanes reached the single-axis CURRENT conormal calculation,
emitted its exact denominator ledger, and then exited `rc=1` at the unchanged
foreign-factor assertion.  This is a proof-carrying localization diagnostic,
not a CURRENT coefficient theorem: **no CURRENT conormal table was accepted or
emitted after the assertion**.

FIRST and PREVIOUS/POLE have denominator `1` in every lane.  CURRENT has rank
`1/1`, kernel dimension `0`, and a denominator of the form

```text
(1/256) F G L U^a V^b,
```

where

```text
F = C*U - V^2 + U^3

G = 4*C^2*U^2 - 8*C*V^2*U + 8*C*U^4
    + 5*V^4 - 8*V^2*U^3 + 4*U^6

L = 64*C^4*U^7 - 256*C^3*V^2*U^6 + 256*C^3*U^9
    + 4*C^2*V^6*U^2 + 432*C^2*V^4*U^5
    - 768*C^2*V^2*U^8 + 384*C^2*U^11
    - 4*C*V^8*U - 328*C*V^6*U^4 + 864*C*V^4*U^7
    - 768*C*V^2*U^10 + 256*C*U^13 + V^10
    + 100*V^8*U^3 - 332*V^6*U^6 + 432*V^4*U^9
    - 256*V^2*U^12 + 64*U^15.
```

The exact per-axis ledger is:

| axis | coordinates before assert | rank | `(a,b)` in `U^a V^b` | diagnostic SHA-256 |
|---|---:|---:|---:|---|
| q2 | 10 | 1/1 | (4,3) | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q3 | 10 | 1/1 | (4,3) | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q4 | 10 | 1/1 | (4,3) | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q5 | 7 | 1/1 | (4,3) | `44ed62a320d72e458ecd98100776bfe537def1fcd357275b6b68e578f1073742` |
| q6 | 6 | 1/1 | (4,3) | `0218b12341163000b92786aedcd74f5e16b603cc05bb4cb8455db8cd188766bd` |
| q7 | 5 | 1/1 | (3,3) | `0fc17fe56ff6504fae9d9d3e09eca1015c3b754aa4114ad3ccff357ed8b3ab89` |
| q8 | 4 | 1/1 | (3,3) | `db33df15feb1074e851fa2fb4a54ec0c653a3a886c3a8099d94be2faf54c597f` |
| q9 | 3 | 1/1 | (2,3) | `e871d8f38ba054c120f9e7e858c3843393929a897e73a6dfb3a6c172e92a1a41` |
| q10 | 2 | 1/1 | (2,2) | `c8c24573d54df557990418dd2305723f89609b9cd41517d802517f8302e91d2b` |

The factorization engine reports each of `F`, `G`, and `L` with multiplicity
one.  Consequently the inherited assertion
`denominator_radical_subset_U_H_B3` is false on every axis.  Each resulting
divisor is retained as explicit source/pivot-localization debt; this package
does not silently enlarge the generic open.

## Controls and custody

- The wrapper changes reporter placement only; the hash-pinned parent is
  `336b9228378e990f896ea82729fef6a9384135a75a01af349574cb9a5ef42c0c`.
- Source archive SHA-256 is
  `86bf989c2ac8b4e263b1f2de19004e32098cd0df10e225828f3f448b7b3b6757`;
  source-closure manifest SHA-256 is
  `8cf8174d554e0e728254fe803c964ad96c5fca26c667f2b7728635fab56fcd9a`.
- Each lane ran on a registered Amazon EC2 host under a 2 GiB cap and a
  two-hour timeout.  All nine terminated by the expected assertion, not by the
  timeout.
- Exact AWS stdout, stderr, rc, launch metadata, timing, and diagnostic files
  are retained under `evidence/box03` and `evidence/r6d`.

## Scope firewall

This package establishes only the exact rank/pivot denominator debt of nine
single-q CURRENT presentations on the fixed source-typed symbolic-center
section.  It does not establish a coefficient, an obstruction, an escape,
coverage of any factor-zero fibre, a 22- or 24-dimensional CURRENT kernel, a
family statement, TD6, SP-2, landing, or JC2.  The required successors are
original-source rebuilds on `F=0`, `G=0`, and `L=0`, or an independent
denominator-free/covering presentation with explicit glue.
