# M2 exit safe-floor legacy repricing R1 — aborted Opus 5 custody diagnostic

Date: 2026-08-29  
Intended reviewer lane: Opus 5 through the pinned local adapter  
Status: **INPUT_MUTATED / NO_PROMOTION**

## 0. Disposition

This is not a hostile-review pass and contains no Opus verdict.  The pinned
adapter invocation was interrupted as soon as a load-bearing cited source was
reported to have changed during the run.  The model had not written a report,
and no partial model output was preserved as mathematical evidence.

The exact custody transition is:

```text
at launch  7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77
post-edit  40104334b5e21d6495f9857a6c13a2877ad0e31a67529c5f23243e7170cfaaaa
           ladder/BOOK-OFFAXIS.md
```

The at-launch value is the LL-1 R3 frozen pin and was independently confirmed
by the checkpoint integrator as the bytes present when the invocation began.
The post-edit value is the intentional canonical safe-floor integration now in
the workspace.  A review which may have observed both versions has no coherent
single input basis.  Therefore the only admissible disposition is
`INPUT_MUTATED/NO_PROMOTION`; a fresh review must start from a newly frozen
checkpoint and must not inherit an apparent pass from this run.

## 1. Adapter custody

The launched command was the repository-pinned `ops/adapters/opus.sh`.  Its
launcher evidence was:

```text
cli=2.1.228 (Claude Code) model=opus effort=max mode=bypassPermissions
shell=yes auth=claude.ai
```

The process was stopped with an interrupt before it emitted a final response
or created the requested xmodel report.  Consequently model identity was
successfully pinned for the attempted run, but no completed Opus reasoning or
verdict exists to seal.

## 2. Completed independent replay — diagnostic only

Before the custody invalidation, a separate exact-rational replay completed.
These results are retained solely to make the aborted work auditable.  They
are not promotion evidence and must be rechecked against the next frozen
perimeter.

### 2.1 Object integrity and execution modes

```text
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7
  xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md (full)
2d873e680cfdc464fc0bc707aec5c072ba9310ee0600a98786643c0ca8c93ac5
  producer body, 12149 bytes
6ca098b8145f091884d7f11ab1d6aac49dadaab91a6ba7ed18f7c022efce99b5
  cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e
  cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json
```

The target checker exited zero under ordinary Python and `python3 -O`.
Stdout was byte-identical in the two modes, with SHA-256
`4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011`.
Its guards use an explicit `require`, not optimization-stripped assertions.
Hostile in-memory controls rejected a wrong LL-1 hash, substitution of the
legacy floor for the safe floor, and a one-unit terminal-budget shift.

### 2.2 `td=12` control

The cited frozen trunk consumer returned `step_count=13`, `dirty_count=10`
and the same payload under ordinary and optimized Python.  Its test program
passed 134 checks in each mode.  Independent exact reconstruction of all ten
dirty rows found only positive integral nonzero defects:

```text
6, 8, 3, 4, 2, 1, 6, 8, 4, 2.
```

Thus their nonzero floors do not change.  The four P1-shaped charges remain
`8,8,8,8`, with budgets `9,8,6,2`; exactly the first two fit.  The remaining
three menu rows are two clean-neutral rows and one pure-epsilon row, so none
contains a nonzero direction to reprice.

### 2.3 LL-1 arithmetic and deduplication

The frozen JSON contains 72 transition records, including 17 cell-bearing
occurrences.  There are 16 unique full cell records but only 15 unique
displayed `(dp,dq,nu)` triples.  The apparent collision `(20,16,5)` is typed
by two different source weights: one record has `(X,kbar)=(5,4)` and the
other `(5/2,2)`.  The checker's full cell key distinguishes them; comparison
against canonical full-cell JSON found 16 keys, maximum one full record per
key, and no collision.  All 32 usable `STEP` edges also remain 32 distinct
typed templates.

Repricing every unique full record over exact rationals changes exactly:

| `(dp,dq,nu)` | nonzero defect | nonzero old to safe | zero kept | total old to safe |
|---|---:|---:|---:|---:|
| `(17,5,2)` | `2/3` | `1 -> 2` | `1` | `2 -> 3` |
| `(51,15,7)` | `2/3` | `1 -> 2` | `1` | `2 -> 3` |
| `(85,25,12)` | `2/3` | `1 -> 2` | `1` | `2 -> 3` |
| `(119,35,17)` | `2/3` | `1 -> 2` | `0` | `1 -> 2` |

An independent multigraph replay reproduced all 23 frozen old terminal states
and every frozen old verdict.  The repriced graph has 17 states.  The alive
inventory changes from 13 to 7, with no added alive state.  The seven surviving
states are:

```text
ALIVE          (2/3,3,2), (2/5,5,3)
ALIVE_FRAGILE  (3/4,4,2), (2/7,7,4), (2/9,9,4),
               (3/10,10,4), (3/8,8,4)
```

The six removed states are:

```text
ALIVE          (2/7,7,3)
ALIVE_FRAGILE  (1/2,2,4), (1/2,4,4), (2/5,5,4),
               (2/11,11,4), (2/13,13,4)
```

There are two repriced paths to `(2/7,7,4)`, but they converge to one
state-keyed inventory row.  It is neither double-counted nor newly invented.
All changed costs are nondecreasing, so pooling a transition menu by reduced
source `(w,M)` does not expose an edge absent at an equal-or-lower legacy
charge; the independent old-state replay is also a direct control on that
argument.

### 2.4 Type firewall and `td=7` sample

The arithmetic checker cannot prove carrier scope: the frozen JSON records
legacy AF2 lower prices and has no machine-checked full-actual-exit-set tag.
Applying the stronger floor therefore remains conditional on the separate
Fable source review validating the full-set theorem and its first-separation
assignment at every consumed P0 step.  It must never be transferred to one
MFE representative witness, one arbitrary flag, an epsilon/zero direction,
or a pole/merge arrival, and the resulting number is a lower bound rather
than an attainment statement.

For the displayed `td=7` route only, the three nonzero defects are `2`,
`1/2`, and `1/3`; their old and conditional safe floors are respectively
`2`, `1`, and `1`.  The retained final zero summand is `1`, so the sampled
route remains `2+1+2=5`.  This says nothing about repricing the entire
17-cell `td=7` book.

## 3. Required next action

Freeze and hash the integrated source perimeter, update or explicitly resolve
every stale source pin, and then launch a fresh Opus review from that single
checkpoint.  Until both the separate Fable source review and the fresh client
review pass, do not promote this invocation and do not consume the canonical
LL-1 numerical inventory as reviewed replacement data.

No canonical file was edited by this diagnostic writer.  No commit, push,
AWS operation, web access, or access to `jc2-lean` occurred.

**Final disposition: `INPUT_MUTATED/NO_PROMOTION`.**

*End of sealed review body.*

---

## Seal (outside the sealed body)

The sealed body is exactly the first `7071` bytes of this file, ending with
the newline immediately after `*End of sealed review body.*`.

Body SHA-256:
`58964a03842bf0901b1e58e363e57ce2f3df8694a26a12660fe4c5c2677424ee`
