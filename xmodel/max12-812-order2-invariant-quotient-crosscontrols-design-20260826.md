# Exact-order-two invariant quotient: prime/load cross-controls

Date: 2026-08-26

Status: **PREREGISTERED MODULAR NAVIGATION; NO GENUS OR ELIMINATION CLAIM.**

The original fixed-load probes use

```text
A=(2,3,5,7,11,13)       at p=32003,
B=(17,19,23,29,31,37)   at p=65521,
```

in the coordinate order `(k10,k6,k2,mu2,mu4,mu6)`.  Those two samples
confound load specialization with characteristic.  The frozen cross-control
matrix is

```text
A at p=65521,
B at p=32003,
C=(41,43,47,53,59,61) at p=32003,
C=(41,43,47,53,59,61) at p=65521.
```

All four lanes use one compiler which pins the original tuple-A compiler and
exact tails.  Before reconstructing every tail it patches the three lower
Faber loads; afterward it exact-transforms only the declared ring
characteristic, printed load sentinel, and even target constants.  Every
transformation site must occur exactly once.

The comparison fields are identical across all six samples:

1. saturated coefficient-fibre dimension and basis size;
2. generator parity and saturated-ideal deck stability;
3. affine involution-fixed-locus dimension and basis size;
4. invariant-plane image dimension, basis size, factor count, and printed
   eliminant.

Prime disagreement at fixed loads signals bad reduction or an unstable
projection.  Load disagreement stable at both primes signals a load-space
discriminant.  Six-way agreement licenses a generic-load/exact-Q successor,
but does not itself prove generic flatness, normalization genus, component
coverage, source nonconstancy, or any exclusion.
