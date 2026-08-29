# Result

Strict overall verdict: **NO_VERDICT_QUOTIENT_NF_RANK_CERTIFICATE_ONLY**.

Every lane used the same source archive and passed its independent
prelaunch q2 control: displayed `q2` is ambient-nonzero but has normal form
zero modulo `(q2)`; a raw q2 determinant has normal form zero; and the `+1`
mutation has nonzero normal form.  Every lane passed exact EC2 identity,
resource tag, source, preregistration, Singular, one-core, idle, memory,
disk, no-orphan, and zero-total-swap gates.

All six branches have 95 exact rational-unit pivots and an 11 by 10 residual
whose 110 entries were explicitly normalized against the pinned `std(I)`
after 816,427 entry/update reductions.  No normal-form drift or pivot
invariant failure occurred.

| Branch | Residual certificate | Total receiver rank | Strict branch status |
| --- | --- | ---: | --- |
| `Q1P02` | rank 6; 1,060 of 1,100 support-matchable 6-minors have nonzero NF; all 39,600 formal 7-minors structurally zero | 101 | exact quotient NF rank certificate only |
| `Q1P03` (`q2=0`) | rank 4; all 18 support-matchable 4-minors have nonzero NF; all 116,424 formal 5-minors structurally zero | 99 | exact quotient NF rank certificate only |
| `TRIPLE02` | rank 6; 1,040 of 1,100 support-matchable 6-minors have nonzero NF; all 39,600 formal 7-minors structurally zero | 101 | exact quotient NF rank certificate only |
| `TRIPLE03` (`q2=0`) | rank 4; all 18 support-matchable 4-minors have nonzero NF; all 116,424 formal 5-minors structurally zero | 99 | exact quotient NF rank certificate only |
| `P` | support bound 10; both support-matchable 10-minors have NF zero | not certified | **adapter descent required / NO_VERDICT** |
| `C8P02` | support bound 10; both support-matchable 10-minors have NF zero | not certified | **adapter descent required / NO_VERDICT** |

For the four complete branches, an explicit nonzero-NF minor is preserved as
the lower-rank witness and the exact support replay is the upper-rank
certificate.  For `P` and `C8P02`, the zero normal forms at size 10 are an
exact diagnostic intermediate, but the registered adapter stopped instead
of descending to size 9; no final rank is assigned until that descent
replays all size-10 zeros and finds a nonzero size-9 witness.

No endpoint quadratic pullback, deeper Fitting stratum, gcd, factor,
saturation, radical, component, or endpoint-survival/death inference is made
in r5.

