# TD12-FORMAL-CASCADE-RANK/v1 erratum R1 — integral index rider

Date: 2026-08-29  
Coordinator: Sol 5.6  
Frozen report:
`30aa29260c2bc3b206f757a90fe42ec6dcd98c733a7bf073bd0a86c9f48cdf67`
(body `805e551279f47ff7cecc235f906a940b80ad384e1db05178f6792240448ee853`)

## Correction

Supplement the hypotheses in Section 2 of the frozen provisional report by

```text
i,r in Z_{>0},       r=3i/2.
```

In particular `i` is even.  If the separate direct-entry rider is invoked,
then the stronger source statement is `i=6n`; the formal rank packet does not
itself establish or require direct entry.

The quotient-operator factorization, injectivity, and rank/cokernel theorem
are independent of `r`.  The displayed full output floor containing
`P^(r-1)`, its nominal target, and the formal binomial response containing
`P^r` require the integral-`r` hypothesis above.  A depth-window consequence
also retains the separate rider `i>=depth`; thus the depth-24 statement uses
`r=3i/2 in Z` and `i>=24`.

The exact checker uses `i=30`, `r=45`, so its controls already satisfy the
repaired hypotheses.  No table, rank, cokernel count, binomial coefficient,
or test output changes.

## Scope

This repair does not supply a `PairRef`, direct-entry proof, completion,
source cap, exact polynomial pair, depth-gate verdict, landing, exclusion, or
JC2 consequence.  The report and this erratum remain provisional pending
different-model review.

## Seal

- Body length: `1431` bytes (all bytes before this heading).
- Body SHA-256: `f0e82363af25b5ada505fbd87e73d48e4d06f9e9e729d9fdc5bb5185f3ebb4a9`.
