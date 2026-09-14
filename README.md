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

## Repository layout

| Location | Contents |
| --- | --- |
| [jc2-lean/](jc2-lean/README.md) | Formal proofs, including the former standalone Lean certificate |
| `lib/`, `tests/` | Shared computational code and tests |
| `cases/`, `box/` | Case-specific computations and research artifacts |
| `avenues/`, `ladder/`, `papers/` | Research approaches, reductions, and papers |
| [refs/](refs/README.md) | Third-party references and source snapshots |
| `ops/`, `xmodel/`, `prompts/` | Orchestration and model research records |
| `history/` | Historical research notes |
| `archive/` (local, Git-ignored) | Research backups and external certificate packages |
| [dist/](dist/README.md) | Original release archives and reproduction instructions |

The root campaign documents describe current strategy, evidence, and progress.
Old release snapshots are historical; current corrections live in `AUDIT.md`.

[Retired (72,108) campaign](history/jc72108/README.md): preserved evidence and
old-to-new paths. Its obsolete standalone workflow has been removed.
