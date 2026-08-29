# Exact result: unloaded K00 row-7 global nonmembership V8

Date: 2026-08-27

Status: **TWO EXACT-Q ENDPOINTS PASS.  GLOBAL UNLOADED NONMEMBERSHIP ONLY.**

After the frozen K00 transverse change, both exact presentations give

```text
r7 not in (r1,...,r6).
```

The direct lane computes over
`Q[t,C6,d0,...,d5]/(1-t*C6)` and is literally the question on `D(C6)`.
The second lane uses the registered faithfully flat weighted Kummer
normalization `C6=1`; its answer agrees.

| lane | basis size | residual terms | lowest degree of frozen `dp` remainder | terms in that piece | hashes |
|---|---:|---:|---:|---:|---|
| direct `D(C6)` | 337 | 53 | 3 | 19 | residual `ebc1c27d...693a5`; piece `5cd154a9...d9b6` |
| normalized `C6=1` | 117 | 32 | 2 | 7 | residual `e5b08388...f8347`; piece `1bbf72de...0c8f` |

Both external validators passed with no Singular diagnostic or failure
marker.  Transverse decomposition and homogeneity replayed exactly.  The
direct computation used 30,100 KiB peak RSS in 9.96 seconds; the normalized
computation used 15,912 KiB in 0.58 seconds; both had zero swap.

The displayed remainder degrees are properties of the frozen global `dp`
normal forms, not invariants of the transverse filtration.  In particular,
the normalized degree-2 piece does not contradict the exact identity

```text
Q7=-(1/512)Q1-(1/128)Q3  at C6=1.
```

The later filtered Macaulay calculation proves compatibility through degree
7, so neither raw remainder piece is promoted as the first local
compatibility obstruction.

This theorem excludes polynomial ideal membership on the generic
`D(C6)` coefficient chart.  It does not decide membership in the local ring
at the K00 point, mixed `Lambda`/load closure, Taylor realization, or JC2.
