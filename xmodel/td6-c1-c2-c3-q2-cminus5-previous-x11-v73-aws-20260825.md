# Producer report: V73K source reconstruction on `C=-5U^2,V=0,D(U)`

Status: **dual-AWS producer-exact; hostile review pending.**

## The exact endpoint

In the already fixed, source-typed A3 section with
`q_beta=t+beta*t^2+t^25`, the V73K replay rebuilds the dependent previous
row `('X-1',11)` from original rows on
`V=0,C=-5U^2,D(U)`.  Transport has rank `3470/3602`, first stage rank
`38/132`, and previous/pole rank `37/94`.  The row residual has beta degree
zero, SHA-256
`3884ec0ce04a7b1488cce725551377ed5ef8e3ea20159eb98efe96ce880f552e`,
numerator factor set `{U}`, no residual denominator, and inverse denominator
only `U`.  Its normalized value is `-1`.

The proof DAG uses all original previous rows `('X-1',d)`, `0<=d<=11`,
and thirteen original first rows.  It keeps direct
`q_beta'=1+2 beta t+25 t^24`; the degree-11 direct contribution is exactly
`4*beta*f2[10]`.  The aggregate reduction, lift, one full original-row
convolution, and exact scalar normalization all replay.  Omitting one source
path, adding one to a multiplier, or replacing the selected row produces an
exact nonzero integral-domain delta.

Therefore the licensed TD6 source equations are incompatible on this raw
open line for every beta.  This statement does not consume the endpoint
`U=0`.

## Dual-host custody

- Box02 stdout:
  `d4bb078cc98e42e120898ae09dbc6e5d9c349c6ef85ccedc7c946a04fb10cc76`.
- Box03 stdout:
  `35b88e5a2ba27dc5a6d7db1bee3727d6642d74b9a8a522ed86b2f383865ef6f3`.
- Both return-code files hash to
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
  and contain zero.
- Proof DAG:
  `27a26a20773fb4f417ed9a3292c483c9668fa3af5f61933e9aa880c48d84d5c9`.
- Normalized identity:
  `be5b6bc8bd09dc9b59f42270a6725236fe0f96392030d88a1a1a3c5323ab40f9`.
- Leaf-denominator ledger:
  `112776f2544b3b3501eedfd9ce4d6fe41b4e13aa53ff07f7d2bcf37f3306e2d9`.
- Residual-factor ledger:
  `8763f53f12a8f52705a29a0b99b525df358fc46fd1d3f42c31ea2bd38a989bcf`.
- Portable archive:
  `2af9d2dc54cd1f4fc2aab674aa28704732994c6ffe7c2b21a465066eb2569dd5`.
- Source manifest:
  `d26fcec169ddbeed1b52024343750ba1636643235da4b2ff31902a6298a9c470`.
- Executed replay:
  `dcaa920a85fcfdfbc4c4e3975c00b45f6ff7e540be21685df59ff2ae36af1672`.

The two theorem outputs differ only in registered hostname/run-tag and
absolute artifact paths.  All remaining lines and all four theorem
artifacts agree exactly.  The separately frozen direct-q-prime omission run
is a support control, not a theorem run.

## Scope firewall

The conclusion is only `V=0,C=-5U^2,D(U)` for all beta in this fixed
source-typed A3 q2-beta section.  It proves no whole `B3`, whole A3, other
TD6 modulus, TD6, SP-2, landing theorem, or JC2 result.
