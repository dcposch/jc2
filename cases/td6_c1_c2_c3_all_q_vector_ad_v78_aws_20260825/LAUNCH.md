# V78 AWS launch ledger

The immutable source archive has SHA-256
`a523edad0fb2962cc689a01132b56f71a3623d028f6d0698cfc2583b525cdca9`.
Its embedded source-manifest bytes have SHA-256
`b0ee4b66dc68013df904c03a87649dca28ac352d71edba210b2536a639c7ad8f`;
the V78 producer source has SHA-256
`5e642b5d0cbdea1e642355649fd14990834add3621c9c933b70a4f01988b0c0e`.
Both clean remote payloads passed the complete embedded source manifest,
remote `py_compile`, and import-closure smoke (`V78_IMPORT_SMOKE_PASS`) with
about 35 MiB maximum RSS before launch.

The complementary proof-bearing lanes are:

| mode | AWS host | registered tag / run directory | shell PID | cap |
|---|---|---|---:|---:|
| `p12` | Box02, `ip-172-30-0-186` | `/home/ubuntu/runs/td6_v78_all_q_p12_box02_20260825T2311Z` | 242052 | 32 GiB, 12 h |
| `staged` | Box03, `ip-172-30-0-249` | `/home/ubuntu/runs/td6_v78_all_q_staged_box03_20260825T2311Z` | 122197 | 32 GiB, 12 h |

Both use `/home/ubuntu/venvs/td6/bin/python`, a fail-closed Linux/AWS-hostname
and registered-tag preflight, `/usr/bin/time -v`, and immutable disjoint
output directories.  These are complementary producer modes, not duplicate
independent mathematical implementations.  A decisive endpoint will be
mirrored independently before promotion.

## Fail-closed endpoint and scope correction

The Box02 `p12` lane terminated rc 1 after 82.61 seconds (maximum RSS
301,484 KiB) at its preregistered V32/V77 selected-minor projection control,
before compiling or asserting any P12 result.  Its stdout SHA-256 is
`c379e78d59de3e0845607feb4de4b1e527cc6a668f86f660ab6ad3fcba6ea1d2`;
stderr is `9089ded0d4c2be29ce93a8316aa2faae75fc48fc189f6caae8c28e877d590f4b`;
the rc file is `4355a46b...` (body `1`).  The immediate failure was a sparse
zero handling bug: the code indexed `first_minor.derivatives[2]`, but the
exact derivative is zero and therefore absent; `c0730fa1...`, which the
assertion expected, is itself the digest of zero.  Auditing that failed
control separately exposed V77's q3 source mistyping through the q2-specific
`qd.B` variable.  See the frozen V77 erratum case and report.  The Box02
output is negative discovery/custody evidence only; V78 has no P12 result.

The Box03 `staged` lane remains live.  It uses the source-correct simultaneous
assignment `qd.B=eps_2`, with each exponent `e` also carried by its own exact
transport RHS and direct q-prime column.  Its execution path does not call
the failed V77 projection assertion.  Nevertheless it remains a provisional
tangent/conormal discriminator under the preregistered fixed-A3 generic-open
scope; it cannot repair V77, prove a polynomial family, or broaden V76.  Any
terminal output requires a corrected source freeze and independent mirror
before promotion.
