# TD6 V85TF1 literal total-`F` raw-source result

Date: 2026-08-26

Producer verdict: **PASS on Box02 q2 and Box03 q10.**

## Exact result

Put

```text
F  = C*U - V^2 + U^3,
H  = C - 3*U^2,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6.
```

On the normalized total-`F` slice with all 132 transport-free section
coordinates retained, the rebuilt genuine raw P12 and 38 packed raw FIRST
source maps satisfy an exact identity in
`Q[C,V,U]_{U*H*B3}`:

```text
U^12*H^3*B3 = a_P*P12 + sum_i a_i*FIRST_i + F*h.
```

Here `F` is an independent base variable after localizing at `U`, because

```text
Q[t,U,V,U^-1] ~= Q[C,U,V,U^-1],
t |-> F,  C |-> (V^2-U^3+t)/U.
```

The common denominator needed for every source term, multiplier, and `h` is
exactly

```text
C*U-3*U^3 = U*H.
```

Thus no `F` factor is inverted, no unregistered denominator occurs, and the
allowed `B3` factor is not needed for coefficient clearing.  Multiplying the
displayed identity once by `U*H` gives the emitted polynomial certificate;
`TOTAL_F_H_CLEARED.tsv` contains `(U*H)*h`.

## Literal specialization and replay gates

The client independently rebuilt both total and `F=0` sources from the frozen
original compiler.  Coefficientwise substitution
`C=(V^2-U^3)/U` agrees exactly on every one of the 38 raw FIRST maps and on
the genuine 2,893-term P12.  All parameter labels `0..131` occur.

The frozen V82QST3 special-fibre certificate then replays exactly, and

```text
U^12*H^3*B3 |_(F=0) = U^9*V^4*(V^2-4*U^3)^3.
```

The total residual has 2,797 parameter monomials and 50,346 scalar
coordinates.  Every coordinate divides by `F`; replay after division and
after the single `U*H` clearing is exact.  The audit covers 742,446 scalar
coordinates before clearing and 663,174 polynomial scalar coordinates after
clearing.  Omitting P12 or the first active FIRST row makes replay fail.

Because `U^12*H^3*B3` is a unit on `D(U*H*B3)` and `h` is regular there, this
producer identity excludes positive-valuation `F` arcs satisfying this
retained raw family on this normalized slice.

## Certificate hashes

- generic P12 polynomial:
  `8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da`;
- localized quotient `h`:
  `7434b0a7434288e421ad300e93c5da8084f69f19a801298ec6ec05bf9b85bb70`;
- cleared quotient `(U*H)*h`:
  `462257a90e652defcb197a08e4a3a4282b4c40aaef48c068d5c6e8c6de234c11`;
- emitted 2,797-term cleared-`h` table:
  `92b927d365d15a5c061acd4db37f819a1e6cba8f81004a068bc910c1eee20fa5`;
- emitted total/special source inventory:
  `9a612bb64ee974a506a1f3b7fcb471fb8924220ca6d24320af0fc9b8a7de6b7a`.

The cleared-`h` table and source inventory are byte-identical across Box02
q2 and Box03 q10.  The exact-result files differ only in their registered
`q_exponent` line; after deleting that one metadata line, both streams have
SHA-256
`4f1da6dd92a2dae0eb177b212010ad0cafbfb8eada0421b07683f07b2743f08a`.

## AWS custody

Both lanes used source archive
`18cd49f51cc925bab52a37315eb1cce72b3f34a776e122aa7ee2a67d44d82d21`,
returned `rc=0`, and ended on the distinct banner
`TD6-V85TF1-LITERAL-TOTAL-F-RAW-P12-SOURCE PASS`.

- Box02 q2: 16:30.30 elapsed, 613,712 KiB maximum RSS, zero swap;
- Box03 q10: 16:30.41 elapsed, 615,324 KiB maximum RSS, zero swap.

The failed or deliberately stopped pre-authoritative deployments are
quarantined in `DEPLOYMENT_ERRATUM.md`; none reached a mathematical verdict.

## Scope firewall

This is a propagation-qualified identity only for one normalized total-`F`
slice with the 132 transport-free section coordinates retained.  The q base
direction, dead stretch, correction, F1 orbit/pole data, centering, and
boundary moduli remain frozen.  The result does not supply a total chart or
finite cover in those directions and proves no whole fixed A3, TD6, SP-2, or
JC2 claim.
