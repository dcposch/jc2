# D125 parity-compression construction code gate (Sol 5.6, 2026-09-07)

Status: **CONFIRMED for the frozen slice construction and literal-substitution code path, with the bounded GAPs below; nothing REFUTED.** This is a desk/code gate for the restricted mu2-fixed sufficient CE subfamily, not an actual construction or engine test. It neither enlarges the accepted mathematics nor makes a point, unit/properness, dimension, performance, or mathematical-openness claim.

## Custody and scope

I read all 13 charged files from `/tmp/jc2-lane.8nFKkf/inputs`, including all 421 lines of `construct.py`, 95 lines of `replay.py`, both test files and both runners. Each frozen file and its charged workspace source matched the listed SHA-256 before and after controls. In particular the terminal Astra report is `80240044afd0e5c0eef979fe3a80c12a34d1efc5140aa6597059265aafd7090c`, and `run_once.py` is `d164af0b576fd7d8f7e3c3a294da8211df996595677aeac75267d2bf9546d40f`. I accept root's verified transaction `b2390242dcf286317682a9853a9680bd996248f865602b9537bfdb7219409c50`, receipt `5226f233246e9ebf4dc6b106a363cd9c642fb869238ae94001f975220afc459d`, and the terminal Fable gate `3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d` as supplied interfaces.

I did not invoke `construct.metadata`, `reconstruct`, `original_rows`, or `replay_frozen`; did not read the 803-row source stream; and did not use AWS, SSH, CAS, a solver, deployment, live peers, ledgers, adapters, guardrails, or protected projects. The sole contract census was the permitted tiny `baseline.make_contract('unequal','rational')` call.

## CONFIRMED

**Literal presentation and A graph.** Independent metadata census gives literal polygon slots 83/215, free slots 71/196, fixed slots 12/19, odd free slots 33/94, 13 A pivots, and 20 retained A slots. The slice order is those 20 names in original order, `beta5_slice`, then `lambda3`: 22 presentation coordinates, while full-library order inserts `shear_s` before `lambda3`. The 267 coefficient variables plus the two lambdas give exactly 269 original maps; even A/B variables and `lambda2` map to zero, while `lambda3` remains a generator.

For every odd level 1 through 13 I independently expanded the lift and matched
`(-1)^(s-i-t) binom(s-i,t)` in the implemented row/column orientation; all blocks have full constant rank. A mutated sign failed. The loop descends 13 to 1, evaluates each row before installing its current pivots, and its `liftrow` includes current nonpivot fixed/free terms and already reconstructed higher levels. A tiny exact fixture containing both a current term and a higher lambda term vanished after solve; deleting the higher term made the row nonzero. The inverse uses only constant rationals, so there is no parameter division or hidden normalization.

**B graph and shear.** Direct differentiation of `H^3` against every actual odd-degree B monomial reproduced `b_matrix` for degrees 1 through 23. The full-column ranks lose exactly one at degrees 5 and 15; the recorded kernel coordinates are precisely `(0,5)` and `(0,15)`. Removing those g-exponent-zero columns gives 92 pivots. Deterministic row reduction selects 92 distinct literal `J/r/(d+13-r)` rows, and each selected square matrix is nonsingular. A coefficient mutation broke the direct matrix comparison. Descending reconstruction uses the complete current `a,b` dictionaries, hence includes higher B terms and every current fixed face, and never performs B-Hermite subtraction.

Full-library mode applies `B -> B+sA` through every B coefficient, not merely the leading face. The support census shows every fixed B position meets A only outside A support or at A's fixed zero, so all B fixed faces survive. The code therefore gives original beta5 as `beta5_slice+s*[p^5]A` and beta15 as `s`; subtracting the whole `sA` is its inverse. A partial-lower-shear mutation failed. `run_once` separately requires `mode == 'slice'`, so the pilot keeps original `lambda3` and fixed `c=-5/9`; it exposes no moving-face or normalized variant.

**Rows and literal replay.** Independently generated labels in implementation order give 31 `FIX`, 660 `J`, 30 A-lift, 75 B-lift, and 7 guard rows: 803 unique indexed positions. The target contribution is exactly `+5/9` at `J/2/0`, corresponding to `[A,B]+5g^2/9`. Constructor completion requires every selected B graph row and all A-lift rows to vanish. Every other high or low row remains traced. Only an exact empty polynomial receives a null residual index and may be absent from a later solver list; equal nonzero polynomials at different original positions remain separately indexed.

`replay.py` hashes the pinned original source before parsing, checks canonical JSONL and prefix digests, consumes all 269 maps in name/index order, and transports each of the 803 literal source polynomials in source order. It compares exact rational wires and zero/nonzero residual numbering, reconciles footer row/residual/term/zero counts, requires both complete footers, and forces iterator exhaustion, which rejects any trailing byte. This is complete literal substitution, not a second proof that the graph maps are invertible.

**Limits and caller.** Multiplication-pair checks precede multiplication; term, coefficient-bit, retained-term, wall, address-space, CPU, file-size, and aggregate-byte ceilings are enforced; polynomial wire allocation has a conservative pre-wire bound. Outputs use exclusive creation. The construction footer is reached only after graph identities and the 803-row count; exceptions close an incomplete prefix without writing it.

Across `construct.authorize` plus `run_once.main`, the path binds Linux/EC2 instance, exact cwd, boot, nonempty job, root construction authority, source/symmetry values, caps/expiry, registration digest, accepted gate, and frozen caller/library hashes. This is cooperative root trust, not same-UID authentication. The caller reserves its receipt exclusively, invokes construction then literal replay in one process under the same expiry, performs source hashes before and after, never retries or spawns anything, and prints success only after the replay receipt is flushed. Process-group RSS accounting and cleanup correctly remain the external unchanged CAPRUN/v1 responsibility.

## REFUTED

None within the stated implementation delta.

## GAP

1. No authorized host construction or 803-row replay has run here. Consequently actual expansion, ceiling headroom, output integrity under a real cap termination, and the planned tiny actual-host caller control remain unobserved.
2. Literal replay deliberately does not establish graph invertibility; that obligation is supplied by the accepted Fable parity/composition theorem. Full mode was checked by code, metadata, and tiny shear controls, not by a full symbolic run.
3. The complete policy boundary is compositional: `construct.authorize` alone accepts nonempty registration/gate fields, while `run_once.main` checks the registration file and exact `3940ba00...` gate. Thus this confirmation applies to the pinned `run_once` pilot entry, not direct standalone execution of `construct.py`.
4. Both unrestricted-order attempts remain timed out. Nothing here establishes a unit, properness, or any solver conclusion.

## Controls

The frozen producer suite passed all 13 methods normally and under `-O`; the frozen caller suite passed all six methods in both modes. Independent `control.py` passed normally and under `-O`, checking all A matrices and actual B blocks, row/map censuses, fixed-face compatibility, exact target, whole shear, and six caller sequence/failure/expiry controls. Ten meaningful mutations were rejected, including A sign, omitted higher forcing, B matrix, partial shear, target position, build failure, expiry, incomplete rows/status, and wrong mode. The reviewed scripts contain zero AST `Assert` nodes. Combined frozen-suite wall time was 0.751 s; independent modes were 0.061/0.099 s, within 30 wall seconds, 25 CPU seconds, and 512 MiB. Evidence is confined to `box/d125-parity-compression-code-gate-sol56-20260907/`; final control hashes are `a5b7ecf5...` and `befe3469...`, suite receipt `6f449879...`, control `01929666...`, and runner `c28e6f23...`.
<!-- BODY-END -->
