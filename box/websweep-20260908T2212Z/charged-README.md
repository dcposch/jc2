# jc2

Our goal is to resolve the plane Jacobian conjecture.

Either prove that every polynomial map ℂ² → ℂ² with constant nonzero Jacobian
is invertible, or find a counterexample. After the July 2026 counterexample in
dimension 3, the plane case is the last one standing. This repo is a sustained
campaign to settle the question.

## Approach

- **Multi-model research.** Frontier AI models work as peer co-researchers
  under a common protocol: any model can coordinate, implement, or review, and
  no result is promoted until it survives hostile review by a model other than
  the one that produced it. `AUDIT.md` records promoted and load-bearing claims
  with their evidence tiers and review chains; `APPROACHES.md` maps the
  avenues; `COORDINATION.md` defines the protocol.
- **Software as a first-class citizen.** The fleet continuously improves its
  own software. Heavy computations run on cloud servers. Every mathematical
  claim comes with replayable artifacts. Key results are machine-verified in
  Lean 4.

## Public progress

For public progress, see [jc2-lean](https://github.com/dcposch/jc2-lean).

## Start here

New coordinators should use [COORDINATOR.md](COORDINATOR.md) for the reading
order and latest handoff. [APPROACHES.md](APPROACHES.md) contains the current
strategy; [PROGRESS.md](PROGRESS.md) contains recent daily digests. The newest
`LIVE STATE` at the bottom of [notes.md](notes.md) owns live jobs and clocks.

The current record does not resolve JC2. The 64 residual configurations are
necessary arithmetic data in the window n <= 200, not 64 externally open
cases. Actual degree-(99,66) counterexamples are excluded by the external
GGHV theorem; our internal computations have not produced a unit certificate.
The literal D=108 physical-Keller family is now retired conditionally on
the named external reductions and retained certificates; no internal unit
certificate is claimed. K16 is proved only through t = 8. See
[AUDIT.md](AUDIT.md) for exact scope, literature dependencies and review chains.
Older closure announcements are preserved as history and are superseded by
later corrections. [History index](history/README.md).
