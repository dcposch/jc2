# V82QS CURRENT shard producer endpoint

Frozen scope: the source-typed fixed A3 section with symbolic center
`(C,V,U)`, the 22 licensed square-zero coordinates
`q2,...,q14,q16,...,q24`, and the staged CURRENT presentation inherited
from the reviewed V78 source.  Coefficient `q15` is excluded as the lower
target-shear gauge of fixed `p=t^15`.

The source archive SHA-256 is
`7c6e648e72eafde683cd64cbb9354d2278e4cfeb11d8c4a9d00d9fd4224e8bb6`.
The immutable AWS run roots are:

- Box03: `/home/ubuntu/runs/td6_v82qs_current_box03_20260826T065557Z`;
- r6d: `/home/ubuntu/runs/td6_v82qs_current_r6d_20260826T065557Z`.

All 22 lanes passed the fail-closed EC2/source preflight, rebuilt transport
from original rows, obtained transport rank `3470/3602`, replayed FIRST, and
obtained exact-zero FIRST and previous/pole conormal columns.  The outcomes
at CURRENT are:

| axis | rc | exact endpoint |
|---|---:|---|
| `q2`--`q10` | 1 | CURRENT was computed, but the inherited assertion `factors_only_allowed(denominator)` failed before the denominator or table was emitted.  These are exact factor-debt failures, not zero/nonzero coefficient verdicts. |
| `q11` | 0 | singleton `('X0',10)` with coefficient `11*U^6`, unit denominator, rank `1/1` |
| `q12` | 0 | singleton `('X0',11)` with coefficient `12*U^6`, unit denominator, rank `1/1` |
| `q13` | 0 | singleton `('X0',12)` with coefficient `13*U^6`, unit denominator, rank `1/1` |
| `q14` | 0 | singleton `('X0',13)` with coefficient `14*U^6`, unit denominator, rank `1/1` |
| `q16`--`q24` | 0 | empty exact table, unit denominator, rank `0/1`, kernel dimension one |

The q2--q10 traceback is the same source assertion at frozen
`replay_shard.py:815`; none is a timeout, resource failure, or sparse-missing
interpretation.  The raw stdout/stderr/rc and any emitted tables are preserved
byte-for-byte under `evidence/`.

A reporter-only diagnostic successor, V82QSD, preserves the assertion but
dumps the exact CURRENT denominator, factorization, coordinate count, rank,
and kernel dimension immediately before it.  It runs under source archive
SHA-256
`86bf989c2ac8b4e263b1f2de19004e32098cd0df10e225828f3f448b7b3b6757`
on Box03 for q2--q6 and r6d for q7--q10.  V82QSD is factor discovery only.

No union theorem is asserted here.  In particular, the q11--q14 nonzero
columns can cancel against other coordinates; the q16--q24 zero columns do
not prove higher-jet irrelevance; and no statement is made about the
simultaneous 24-dimensional q/dead CURRENT map, nonlinear deformations,
families, all TD6, SP-2, landing, or JC2.  Exact interpretation awaits the
dual V82Q monoliths, d10/d15 V82P4 controls, a complete factor ledger for
q2--q10, and the proof-carrying 24-axis reconciliation.
