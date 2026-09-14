# Independent code gate: D125 hybrid affine construction and literal cover replay

2026-09-07, frozen-lane review. **Overall code verdict: CONFIRMED. REFUTED: none.** The producer’s provisional-review label is stale for this code gate. The execution and external-dependency GAPs below remain; this is not launch authority.

I read all eleven charged files, including all 250 constructor lines, 145 replay lines, 141 test lines, 281 baseline lines, and the complete contract. I used only `/tmp/jc2-lane.5eg5Cq/inputs`; its hashes match the charged report (`18f983a…`), code pins, accepted hybrid desk gate and normalization gate. The stipulated transaction `3749ac…`, root verification, producer TERMINAL/IDLE state, and receipt `4ed10b…` are custody premises, not live-peer observations. The two accepted math gates are consumed, not re-hardened. No original EBS source, CAS, network, subprocess, solver, deployment path, or shared ledger was touched.

## 1. Constructor — CONFIRMED

`layout` selects the 33/94 odd free A/B slots, removes 13/34 standalone Hermite pivots and the whole-shear B(0,15) slot, and orders 20 A, 59 B, `k,z`: exactly 81 coordinates. `reconstruct` starts every fixed/zero face literally, assigns only retained coordinates, and solves odd levels in descending order. The exceptional B15 columns are `[1,2,3]`; the code’s signed matrix is `[[1,-1,1],[-14,13,-12],[91,-78,66]]`, determinant −1, with inverse `[[78,12,1],[168,25,2],[91,13,1]]`. Pivots must initially be zero and forcing is `-M^-1 rhs`. There is no nonlinear B92 reconstruction path.

The actual shape gates restrict A maps to 22 affine terms over `{1,k,a_i}`, B maps to 62 over `{1,k,k²,b_j}`, with denominator lattices 1 and 9. `jshape` admits exactly the stated A–B, k–A, k–B and pure-k families, at most 1,362 terms and degree three; `jrow` inserts `+5k³/9` only at J/2/0. Own controls changed a pivot, inverse entry, forcing coefficient, support, denominator and target sign; each changed object was rejected.

## 2. Complete normalized stream — CONFIRMED

The emission order is all 31 FIX positions, 660 J positions, 105 LIFT positions, six vertex guards and the scalar guard: all 803 original labels, followed by only `UNIT/kz` as position 804. All post-Hermite LIFT and FIX residuals must be zero; wrong-parity J/LIFT rows require both normalized and literal sides to vanish. Fixed-map metadata is retained for every entry. The target string is exact.

Moving guards are `(kz)^r-1`, for r=1,2,3, and carry the literal geometric cofactor; unchanged guards remain zero. The stream uses exclusive creation, canonical rational wires, sorted monomials, a prefix digest and complete footer. Replay rejects duplicate JSON keys, noncanonical lines/terms, missing footer, reordered/omitted labels, malformed field coefficients and post-footer bytes. No whole-stream cubic claim is encoded.

## 3. Literal original-cover replay — CONFIRMED; GAP-RUN

Replay constructs each old coefficient as `ell^((D-d)/2)` times its normalized map, then independently substitutes `k=ell^-6`, `z=ell^6`, `lambda2=0`, `lambda3=ell` into each literal source polynomial. It does not call the constructor’s J or lift generators. Row factors are independently implemented as `(38-I-J)/2` and `(D+e-5t)/2`; parity-odd factors force zero on both sides. J/2/0 therefore transports the target correctly. All 267 coefficient variables plus the two lambda variables, every coefficient metadata record, and every source label/index are mandatory.

The 31 fixed maps receive a separate old-value pullback check, essential because literal FIX rows are zero. Both source hashes are checked, before and after replay. Guard polynomials are checked as objects and as exact multiples of `kz-1`. Replay shares representation/cap/shape helpers and redundant fixed/guard constructors, but the decisive row equality uses separate Laurent arithmetic over the literal original JSONL and never calls the normalized J/lift generators. The fixed pullback and geometric-cofactor controls are independent. This is not a shared-generator self-replay.

**GAP-RUN:** the pinned original stream is intentionally absent from the frozen lane, and neither a full map nor an 803-row loop was run. Thus the code’s fail-closed enforcement is confirmed, but actual source/stream compatibility, output counts and a current replay result remain unobserved.

## 4. Composed main and stale outputs — CONFIRMED

`main` authorizes before hashing or opening the source. Authorization binds exact Linux/EC2 instance, boot, cwd, three code hashes, source path/hash, registration and root-GREEN hashes, exact mode, and bounded caps. Gate hashes are syntactically checked strings plus a root-set acceptance bit: cooperative root trust, not same-UID authentication.

One absolute expiry is shared by construction and replay. RLIMITs cap CPU at 300 s, address space at 4 GiB, each file at 128 MiB and cores at zero; arithmetic gates impose 100k terms, 1m pairs, 1m retained terms and 4096-bit coefficients. Stage context is set before capped work. There is one process, no solver, child, retry or alternate mode. Partial construction/replay cannot print success.

Both outputs use `xb`. An own filesystem mutation confirmed that an existing construction or replay-result file is never overwritten. A stale replay result is detected only at final receipt creation: it survives unchanged and forces nonzero exit. Therefore file existence alone is not success; the external runner must require the current process’s zero exit and receipt, as the contract says.

## 5. External controls — GAP-HOST; scope dependency

Unchanged CAPRUN still owns process-group RSS and reaping. Actual-host controls, new registration, new authority and new root GREEN are absent; no actual run occurred. Stage stderr is intentional telemetry and is not governed by an empty-stderr solver contract. The graph/shear and faithful-cover implications remain the explicitly external, already accepted mathematical dependencies.

## 6. Independent evidence

Frozen producer tests: 20/20 normal and 20/20 `-O`, 0.10/0.32 s, peak RSS below 27 MiB. Own `gate_controls.py`: 20/20 in both modes, 0.09/0.25 s, peak RSS below 28 MiB, `python -B`, 30 s wall / 25 s CPU / 512 MiB caps, zero `Assert` nodes, zero source rows and zero `baseline.make_contract` calls. Tests use only a 3×3 constant matrix, physical toys of degree at most seven, and literal fixed metadata; mutations exercise actual producer/replay objects.

Artifacts: `box/d125-hybrid-affine-code-gate-sol56-20260907/`; control SHA-256 `b8a5d4c…`, input pins `f892fef7…`. STOP after gate.

<!-- BODY-END -->
