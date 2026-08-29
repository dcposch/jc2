# V27 BASE4 R0 Singular-minor storage erratum

Status: **FAILED CLOSED BEFORE TARGET STANDARD BASIS / NO VERDICT**.

The first immutable r6a launch used source-freeze SHA-256
`b292f78a9ab3b0c9c051ce1c9f1de921ce19d705d60f416c9883dcbe86635174`.
It stopped in 1.87 seconds, at 509,120 KiB maximum RSS and zero swaps, before
the `B+I5(A)+I4(A)` standard-basis calculation.  The guard incorrectly
required `size(minor(A,r))` to equal the number of all row/column subsets.

On Singular 4.3.2, `minor(A,r)` omits zero polynomial entries from the stored
ideal.  A read-only diagnostic streamed from the frozen failed script reports

```text
I6SIZE=0
I5SIZE=90
I5NZ=90
I4SIZE=594
I4NZ=594
```

These are exactly the reviewed/frozen nonzero-occurrence censuses.  The full
combinatorial source-label counts remain 49, 441, and 1,225; the additive
`MINOR_SOURCE_LABELS.json` retains every row/column subset, including those
whose recomputed determinant is zero.

R1 changes only the typed storage guards to require `0`, `90`, and `594`
stored nonzero entries for `I6(A)`, `I5(A)`, and `I4(A)`.  It does not alter
`A`, `B`, any determinant, the target ideal, term order, algorithm, resource
envelope, mutations, replay requirements, or firewall.  R0 and its evidence
manifest are retained as infrastructure evidence only; they imply no rank,
compatibility, jet, arc, closure, counterexample, or JC2 conclusion.
