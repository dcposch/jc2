# AS F-only `D=7`: raw-Q7 global accepted-chart exclusion

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL
SOURCE/COMPILER REVIEW.**

## Exact scoped result

For the frozen accepted Q9 chart

```text
free coordinates  (t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t14,t16,t18)
fixed coordinates t10=t11=t12=t13=t15=0,  t17=1,
```

there is no simultaneous assignment over `F3` to the 32 raw Q8 digits and
the 18 raw Q7 restoration digits satisfying all of the following equations:

```text
23 explicit Q9 source rows,
22 explicit Q8 source rows,
19 explicit Q7 source rows,
46 terminal coefficient rows in total degrees 9,10,11,12.       (1)
```

Thus the complete `3^13` accepted chart, including every Q8 and Q7 fibre over
it, is empty at the terminal-high gate encoded in (1).  In particular, this
is not a zero-section or sampled-fibre statement.  The formula contains all
13 chart trits, all 32 Q8 trits, and all 18 Q7 trits symbolically.  It does
not consume the earlier sampled claim that the Q7 restoration matrix is
constant over the chart.

The 23 Q9 equations are imposed explicitly even though the origin-plus-kernel
chart parametrization already implies them.  This makes the chart compiler
self-auditing.  Likewise the 22 Q8 and 19 Q7 rows are imposed directly; no
RREF substitution or fixed-matrix premise is used.

## Exact circuit and UNSAT certificate

The source-pinned integer carry compiler emits one 32-bit QF_BV formula over
residues modulo 729.  Every addition and multiplication is reduced at its
gate.  The largest unreduced product is `728^2 = 529984 < 2^20`, so 32-bit
multiplication cannot wrap.  There are 35 exact divisibility-by-three gates.
The SMT2 payload is 851,228 bytes with SHA-256

```text
46b755e1e274203f838ad663675075379f4df93068e0a7f0028728178edbb417.
```

System Z3 4.8.12 timed out after the preregistered ten-second smoke test; that
`unknown` is retained and is not evidence.  Boolector 1.5.118 independently
returned `unsat` in 8.56 seconds with 83,460 KiB maximum RSS.

For proof production, pinned `z3-solver` 4.16.0 applied
`simplify -> bit-blast -> tseitin-cnf` deterministically.  The resulting CNF
has

```text
4,723,508 variables
22,454,514 clauses
SHA-256 19c1551cb284c6f55a32dff2f703426f15eb1001f229f0853c59330a59db79d6.
```

CaDiCaL 1.7.3 produced the textual DRAT trace with SHA-256
`5b36f87705de3ba823b44797fc635ec2073a206b3428fb669bd3f5a884387350`.
Independent `drat-trim`, built from commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985` with binary SHA-256
`92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a`,
reports

```text
s VERIFIED
39,393 / 22,454,514 clauses in core
7,508 / 9,165,105 lemmas in core
8,815,141 resolution steps
0 RAT lemmas in core.
```

## Positive and omission controls

Deleting only the 46 terminal rows leaves a SAT formula.  Boolector found a
model in 2.75 seconds.  An independent integer replay of that model verifies
all 23 Q9, 22 Q8, and 19 Q7 rows, verifies recursive versus literal divided
`/243` determinant computation, and obtains exactly one nonzero terminal
coefficient.  The model stdout and replay JSON hashes are respectively

```text
6cd687baf9835ab7814af17c6d4825dec5a7e0e9ab96e2f3e2508e3c54d01e5f
877641bb3bd1d39af275be5cea057048cd3be8e1f8b880f6776e34303290c866.
```

This control checks that UNSAT does not come from a broken predecessor chart,
a missing Q7 fibre, or an accidental source-row contradiction.  It also pins
the terminal-row orientation.  The prior reduced-Q7 certificate remains
quarantined: its fixed-matrix premise had only been sampled on an affine-rank
11 subset of the 13-dimensional chart.  The present raw-18 formula removes
that premise rather than repairing it by extrapolation.

## Custody and strict refusal scope

All computation ran on Box02 at
`/home/ubuntu/jobs/as_global_chart_rawq7_qfbv_20260825T0650Z`.  The full
custody archive includes the transitive source closure, formula, control
model and direct replay, SMT/CNF/DRAT bytes, solver metadata, Z3 wheel,
`drat-trim` source snapshot and binary, and manifests.  Its remote path is
`/home/ubuntu/jobs/as_global_chart_rawq7_full_custody_20260825T070253Z.tar.zst`
and its SHA-256 is
`e61d2c3dfb5aa1254d0df5fdb05156d3da51db8164e6874b2b5506360ec9a9ab`.

The result excludes only the displayed accepted aligned F-only `D=7` chart
and its encoded next terminal-high gate.  It does not yet prove that this
chart exhausts every F-only `D=7` boundary component, every simultaneous
gauge-capped branch, or every AS/Witt lift.  It gives no no-lift theorem and
no Jacobian-conjecture inference.  The next gate is a source-honest coverage
ledger: identify which original nonreduced boundary components map into this
chart and construct the next canonical chart for every component not covered.

