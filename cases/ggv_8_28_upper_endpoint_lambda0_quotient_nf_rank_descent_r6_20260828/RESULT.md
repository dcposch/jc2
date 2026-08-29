# Result

Strict verdict: **NO_VERDICT_QUOTIENT_NF_RANK_CERTIFICATE_ONLY**.

Both independent AWS branches passed exact host/resource-tag/source/backend,
one-core, no-orphan, and zero-total-swap gates.  Each independently replayed
95 rational-unit pivots, 816,427 explicit normal-form entry/update
reductions, an 11 by 10 residual with 75 nonzero support slots, zero NF drift,
and zero pivot-invariant failures.

For each branch, all 11 formal size-10 minors are exactly zero in the stratum
ring: nine are structural zeros after NF support replay, and both matchable
raw determinants have normal form zero.  At size 9, all 550 formal slots are
preserved: 378 structural zeros and 172 matchable signed raw/NF determinants.

| Branch | Matchable size-9 minors with NF zero | Matchable size-9 minors with NF nonzero | Exact residual rank | Total receiver rank |
| --- | ---: | ---: | ---: | ---: |
| `P` | 19 | 153 | 9 | 104 |
| `C8P02` | 53 | 119 | 9 | 104 |

An explicit nonzero-normal-form size-9 witness is preserved for each branch.
Together with the complete size-10 zero certificate, this proves exact rank
9 for each residual over its exact coordinate-ring stratum; adding the 95
replayed unit pivots gives total receiver rank 104.

The `P` determinant stage used 20,600 KiB maximum RSS and 42.61 seconds; the
`C8P02` determinant stage used 16,472 KiB and 0.97 seconds.  Both report zero
swaps and exit status zero.  Final process censuses are empty and validated.

No mathematical conclusion beyond these two exact rank certificates is
licensed here.  In particular, the endpoint quadratic was not pulled back
and no deeper Fitting stratum or rank-locus component was computed.

