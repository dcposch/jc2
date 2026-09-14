# D125 hybrid81 → exact-Q solver adapter/caller hostile gate

Status: **SEALED — adapter/exact interface CONFIRMED; current caller REFUTED
pending two lifecycle corrections; engine/size evidence remains GAP.** This is
not solver or deployment authority.

## Scope and custody

I read all eleven charged files in `/tmp/jc2-lane.0Jg3tv/inputs` in full,
including all 83 `hybrid.py` lines and the complete appended FALLACY-v2. Input
and own-artifact hashes are in
`box/d125-hybrid81-solver-gate-sol56-20260907/PINS.json`. The stipulated
producer/manifest/receipt/PASS facts are custody premises, not proof. The
accepted exact-Q checker, certificate criteria, old footer algorithm and prior
affine-cover results are consumed dependencies; I did not reopen their whole
foundations. No mathematical exit-price assertion is made.

No live report, shared ledger, protected tree, network, AWS, SSH, CAS, solver,
production source, worker, authority file or production execution was accessed.
Only frozen bytes and private copies were read or run. No frozen input was
modified.

## Interface verdicts

| Boundary | Verdict | Result |
|---|---|---|
| hybrid construction → literal Q/dp rows | **CONFIRMED** | Production digest precedes interpretation; canonical framing, source/target/field/order, exact coefficients, indices, counts and frozen census are fail-closed. |
| literal rows → unchanged exact checker | **CONFIRMED** | Construction and ring digests bind the stream; complete equality mapping handles zeros/duplicates; unit and proper-superideal paths invoke the accepted exact obligations. |
| Python ordinary serialization → actual Singular import | **GAP-SINGULAR-LEX** | Local exact reparse succeeds, but actual Singular parsing/index behavior has not run. |
| caller post-run source custody | **REFUTED — POSTHASH-RECEIPT** | A result receipt is published before post-hash acceptance and verification ignores its post-source field. |
| caller absolute aggregate deadline | **REFUTED — DEADLINE-HANDOFF** | CAPRUN receives an earlier allowance; the payload's fresher allowance is unused. |
| actual 81-variable generated size | **GAP-SIZE** | Unmeasured. The unchanged 2 MiB whole-script cap remains binding and a hit is INCONCLUSIVE. |

## Adapter review

`hybrid.py:36-45` requires bytes and checks the exact construction SHA
`4ea526b2…` before production interpretation, then canonical JSONL bytes,
complete footer/prefix hash, schema `jc2.hybrid-affine/v1`, Q, dp, the exact
target and original-source SHA `b8db2766…`. `hybrid.py:46-68` enforces unique
safe displayed names, phased maps/graphs/rows, literal original indices, unique
labels ending in `UNIT/kz`, all-row/term/zero/map counts, the
81/804/298/19 production census, 269 original names, 58,684 terms, 578 zero
original slots, final `k,z`, and literal `kz-1`.

`decode` accepts only canonical rational pairs, requires the golden component
to be zero, and rejects zero, duplicate, unsorted or out-of-range monomials.
Every one of the 804 slots is retained; `ordinary` emits explicit rational
syntax and line 72 reparses it exactly before return. The adapter does not infer
cofactor positions. `checked_certificate` parses a construction/ring-bound
JC2CERT1 stream, equality-maps engine I into the complete literal vector, and
then calls either exact unit recomposition or rational Buchberger + nonzero
NF(1) + every-row zero NF. An engine header, modular result or displayed `[1]`
alone reaches no verdict.

Map/graph/guard metadata is decoded/count-bound rather than independently
reconstructed. That is acceptable only because production bytes are pinned and
the accepted source-transport chain remains an explicit dependency, as charged;
it creates no new theorem here. The local serializer emits forms including
`1+-1*x`. Its own parser accepts them, but this is not evidence that Singular
does, hence the specifically retained `GAP-SINGULAR-LEX` rather than an inferred
failure.

## Caller, caps and custody findings

The delta uses one fixed construction path and `H.read_hybrid(...,
production=True)` in both decision and verification (`driver.py:154`). Footer
and parser use the construction SHA, while `ring_id` binds Q/dp/displayed order
(`driver.py:99,172-183`; `exact.py:201-209`). Rebound stale-I controls show that
changing a row sign, zero, rational coefficient, row membership or variable
image and merely rebinding the certificate header still fails engine equality.

The unchanged footer prints complete indexed I and G, runs exactly one
`slimgb(I)`, and conditionally prints a full `lift(I,ideal(1))` vector. Control
mode substitutes no solver algorithm. Engineering authority is accepted only
for control; decision and verification require solver mode and the four named
accepted-control digests (`driver.py:52-78`). AS, sampled group RSS, per-stream
FSIZE, core and phase wall/CPU values remain 16 GiB, 16 GiB, 64 MiB, zero and
300/120 seconds. The final check at `driver.py:183-185` applies after appending
the suffix, so the 2 MiB ceiling includes it and is not automatically raised.

**POSTHASH-RECEIPT is a concrete fail-closed bug.** `driver.py:210-215` computes
the post-run source hash, writes `<phase>.result.json`, and only then rejects a
hash mismatch. Verification at lines 156-181 requires child return zero,
telemetry/identity/output hashes and current source parsing, but never requires
`receipt.phase == "decision"` or
`receipt.source_pins_after == {"jsonl": H.CONSTRUCTION_SHA}`. Thus a child-zero
decision that the outer launch rejects for source drift leaves a receipt which
can be consumed after the source is restored if an external controller misses
the outer nonzero exit. This does not forge the exact algebra, but it defeats the
declared lifecycle gate. Correction: validate `after` before exclusive receipt
publication, and make verification require the exact decision phase and exact
post-source-pin object.

**DEADLINE-HANDOFF is a concrete hard-deadline bug.** Launch computes `duration`
at line 192 and passes it to CAPRUN at lines 197-198. Payload recomputes a fresher
duration at line 142 but never uses it. After a delayed handoff, payload may
start with one second left while CAPRUN retains an earlier 300-second allowance,
so execution can cross `deadline_utc`. The per-phase maximum remains bounded;
the claimed hard 450-second absolute aggregate does not. This path is inherited,
not introduced by the hybrid patch, but the charged caller/time-bound review
exposes it. Correction requires CAPRUN to enforce the absolute deadline or an
equivalent fresh payload-side wall deadline, not an unused recomputation.

## Independent bounded controls

Private byte copies of `exact.py`, `hybrid.py`, `driver.py`, `test_exact.py` and
`test_hybrid.py` match their charged hashes. The frozen 25-test suite passed in
normal and `-O` modes: 0.12/0.45 seconds wall and 26,648/29,672 KiB peak RSS.

Own `gate_controls.py` ran 23 named outcomes in both modes under 30-second wall,
25-second CPU and 512 MiB AS bounds: 0.11/0.43 seconds wall and
27,560/30,540 KiB peak RSS. It exercised source and target/sign binding; a row
sign change; fully resynchronized row omission and changed-zero mutations;
canonical-wrong and noncanonical rationals; a nonzero golden component; exact
unit-cofactor corruption; a Buchberger false basis; stale metadata/certificate
source; rebound stale I after changing the source digest; displayed-variable
order/image mismatch; both directions of authority-mode separation; whole-toy
script cap; and both caller bugs above. All intended rejects reached their named
gate in normal and optimized execution. AST inspection found no `Assert` in the
three implementation modules or own checker, so no enforcement disappears
under `-O`. Exact run metrics are retained in `RUNS.json`; the checker SHA is
`d5b208f9…`.

## Residual evidence and disposition

The unexecuted later-engine fixture is `tiny-engine-fixture.jsonl` (1,698 bytes,
SHA `d00df83b…`) plus its byte-derived unchanged-footer input
`tiny-engine-fixture.sing` (1,073 bytes, SHA `d1c33444…`). It has four variables,
seven indexed slots, three zeros, a duplicate rational row, `kz-1`, an exact
unit relation and the signed `+-` form. It was generated and byte-compared only;
it was not submitted to Singular. After caller correction/code acceptance, root
still must separately authorize this tiny actual-engine import and verify real
I_SIZE/I/T zero/duplicate correspondence. Actual ordinary production size also
remains unmeasured. Neither gap justifies a cap increase.

Fresh exact worker/cwd/boot/EBS/Owner/output custody and physical GREEN remain
disabled and external. No third full algebraic certification is demanded: the
accepted literal-original-row replay and 803-row execution are consumed at their
stated scope.

Final disposition: **CONFIRMED** for the new hybrid81 → exact-Q mathematical
interface; **REFUTED pending correction** for dispatch with this caller;
**GAP** for actual tiny-engine syntax/index evidence and actual generated size.
Root should review only the two named caller corrections, then run the already
required tiny engine fixture under separate engineering authority. No solver
decision or worker action is authorized. **STOP/IDLE.**

<!-- BODY-END -->
