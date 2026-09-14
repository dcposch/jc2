# FIRST joint static gate: quotient/remainder producer and independent controls (fable5, 2026-09-10)

Status: FIRST STATIC REVIEW, complete for A–F with GAPs listed. No authored Seal. No charge_basis declaration. No completion marker before the final standalone line.

Launch observed 2026-09-10 00:40:57 UTC (own `date -u`). Hard stop: earlier of launch+20 min (01:00:57) and 01:00:00 UTC, i.e. 01:00:00 UTC. Final 3-min publication reserve (content freeze 00:57:00). Clocks never reset. Skeleton written 00:42 before any body access.

Owned outputs: this file and `box/f10-r1-quotient-remainder-static-gate-fable5-20260910/` ONLY. Own-only absence check 00:41: both absent before creation.

## Custody (15 ordered inputs, sha256 verified in /tmp/jc2-lane.lgPBQb/inputs before body access, 00:41:52 UTC, ALL MATCH)

| # | input | sha256 | lines |
|---|---|---|---|
| 1 | xmodel/f10-r1-quotient-remainder-code-astra-20260910.md | 3982390dbd321506df64037dc1b7ba6525b441e09ad94cdc9828beb7eaafdb20 | 124 |
| 2 | xmodel/f10-r1-quotient-remainder-generic-controls-astra-20260910.md | 50caf7aa9d91ae1b9665f4cb49aa931413977d204adc5d24ddf0287a6770a749 | 89 |
| 3 | box/f10-r1-quotient-remainder-code-astra-20260910/solver.py | 58cdc4721143ec2be93cc720831c2235a9221b567f1903d2ffd6025b4f54b665 | 332 |
| 4 | box/f10-r1-quotient-remainder-code-astra-20260910/checker.py | 122842e5cf38a0eab2585c7e894c1ca9d9758dd643830d5447800642554fdf69 | 177 |
| 5 | box/f10-r1-quotient-remainder-code-astra-20260910/evidence.py | cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767 | 111 |
| 6 | box/f10-r1-quotient-remainder-code-astra-20260910/algebra.py | 7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc | 170 |
| 7 | box/f10-r1-quotient-remainder-code-astra-20260910/execution_gate.py | cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 | 72 |
| 8 | box/f10-r1-quotient-remainder-generic-controls-astra-20260910/generic_controls.py | c369dc11b4e9562b050333225133aedf9cb63a04f3309424fdfab769465d363a | 425 |
| 9 | xmodel/f10-r1-quotient-remainder-design-astra-20260909.md | 6135ca133c9132171d90536761471af8a2eefaf664831ab7b322120fc4c5ce2a | 340 |
| 10 | xmodel/f10-r1-quotient-remainder-design-gate-fable5-20260910.md | 718df083267ec3c7fc5ac9e0c493a33ccc41f4c8b92a82eed5b2dbbb3570746d | 65 |
| 11 | box/f10-r1-quotient-remainder-code-prep-20260910/INTERFACE.md | 0cea062f8ead0d97f477dd22a10ca6bc523d3f9b3fdd89c49a960183dada304d | 86 |
| 12 | box/f10-r1-quotient-remainder-code-prep-20260910/API-DELTA.md | a8bdb4fda1199bdf4f553e7d3b12858c05adce32ceed4da78602deaba8bd8d1b | 15 |
| 13 | box/f10-r1-quotient-remainder-code-astra-20260910/STATIC-REVIEW.md | 7622025dde41fee21a4a2ecb434f41fb612dfd374caf515e70dee5bc27a51a95 | 57 |
| 14 | box/f10-r1-quotient-remainder-code-astra-20260910/VALIDATION.md | d051ece4303227803511ffa9bcaca4be3d568cf973923f7b42d53938e1b92bcb | 51 |
| 15 | box/f10-r1-quotient-remainder-generic-controls-astra-20260910/PLAN.md | 0118fd32414a73c5046695c123b8f1b5ed37804bdcbb4408c76f9b1de1e04c15 | 109 |

Premises accepted, interiors not rerun: 17zg design (#9) and its gate (#10), with ROOT's two qualifications (mu completed on whole C; only the selected leading coefficient vanishes on the g child). Retained modules #4–#7 byte-identical to 17z per ROOT; reviewed only at their interfaces with the NEW kernel (#3) and harness (#8).

Method: static text reading only; ZERO mathematical subprocess (no Python/import/AST/compile/syntax/test/CAS, no fixture/matrix/coefficient generation, no manual-control replay by machine); no network/AWS/SSH/process inspection/agents; no code changes; no provenance/corpus/Git/protected/live ledger/report/log/receipt access; no broad xmodel listing. Hand traces below are by reading, not execution.

## Read scope

All 15 inputs read WHOLE with `cat -n` from the lane inputs dir after hash match. Honest note: my first combined read of #10, #1, #2 was persisted by the harness and only its first 2 KB was shown; I re-read each of those three files separately and whole (00:50 UTC). No span of any input remains unread. Cross-check: the four FROZEN constants in generic_controls.py L16–19 equal input hashes #7, #5, #6, #4; evidence.py L13 ARITHMETIC equals #6 (algebra.py), so evidence L88 is self-consistent with the retained pin.

## A. Kernel candidate validation / split scan / degree conservation — CONFIRMED

- Validation (solver.py L16–30): p is a list of 8 `Fraction`, monic; squarefreeness via `dxg(p, p')` normalised gcd `== [1]`, message exactly `generic modulus must be squarefree` (API-DELTA L10). Hand trace p=v^7: derivative 7v^6, gcd v^6 ≠ 1, raises at L20 before any fs/q check. Nine polys, T-length 1..6, dense 7-Fraction coefficients (L21–30) match INTERFACE L13–17.
- Rational helpers: only frozen algebra.py `da/ds/dm/dd/dxg/trim` (L15). All divisions are by nonzero rationals: `dd` by a trimmed leading coefficient, `dxg` L49, L158 by the nonzero rational `beta`, L312 by the literal leading coefficient. In-A inverses are certified by xgcd and re-verified (L103–106). `Coefficients.divide` is monic-only (L69). No unlicensed coefficient division.
- Projected maximal-degree pivot (L96–101) on the PROJECTED `local`, first index on ties. Both children `h, g` pushed (L117); every popped node re-projects and rescans all nine (L96). Split guard `0 < deg g < e` (L111), exact cofactor and coprime children (L112–114). Bounds: visits ≤ 13 (L94), splits ≤ 6 (L116). Degree conservation: leaf degrees sum to 7 (L118) and leaf product equals p (L122); with p squarefree this also proves pairwise coprimality of all leaves.
- Hand split trace (lost-component, PLAN row 6): c = 1−e0 has gcd v with p; child v gives f1 = 1 (constant unit, d=0), child p/v gives f1 = T (d=1). Only the leading coefficient vanished on the g child; the code keeps the constant 1 (STATIC-REVIEW L21–22 honoured).
- allzero/d0: d<0 with b=0 leaves zero multipliers (L146, falls through); d<0 with b≠0 returns the coordinate separator (L151–160) with k, l read from the REDUCED b (design gate doubt 3 honoured); d=0 sets h_pivot = c^{-1} b (L162).
- Zero representation is uniform: every coefficient produced by the helpers is trimmed, so `tt` (L43) correctly treats `[]` as the only zero; no untrimmed `[Q(0)]` can arise (inputs pass through `project`).
- Least blocking defect: none. Non-blocking: `construction_trace` (L126–129) omits Bezout identities, idempotents, raw inverses and the local solution/functional that design §8 L286–290 calls "auditable"; INTERFACE L40–43 made the trace optional, and the checker never consumes it.

## B. Monic possibly non-reduced remainder modules, direct-sum RREF — CONFIRMED

- Remainder module is A_a[T]/(fhat) via monic division only (L68–79); no radical, no inverse in C. `vector` (L80–83) fixes the Q-basis order j outer, l inner, dimension e·d.
- Columns (L186–196): for each of the EIGHT non-pivot generators, all j<d, l<e, the remainder of v^l T^j f_i; zero generators yield retained zero columns; `col == column_base + 8·e·d` enforced (L197). Rows = Σ e·d ≤ 35, columns 8·rows ≤ 280 (L168–171); augmented `[M | b | I]` is rows × (columns+1+rows) ≤ 35 × 316 (L174, L202), one `.rref()` (L203), `rref_calls` = 1.
- Exact tracking: pivots re-verified as first-nonzero, strictly increasing, value 1 (L207–211). `columns in pivots` ⇔ b ∉ col(M): the row with pivot at the b column has zero M-part and b-entry 1, and its I-block is the row-operation vector, so mu·M = 0, mu·b = 1 hold by the verified pivot form alone (L221–223). mu is indexed on the complete C basis (row layout) and sliced per leaf (L228). UNIT particular solution: pivot variables from the b column, free variables 0 (L238–241); rows with pivot inside I have zero b-entry, so consistency is exact. Rank defects of M are absorbed by the identity block (`rank == rows`, L205). Variable pivots per leaf are honoured by identical skip logic at build (L188) and read-back (L248).
- Hand trace nonreduced-remainder (f1=T², f2=1+T, q=1): 14 small columns {e_l+e_{7+l}, e_{7+l}} span all 14 rows; solution x_{(0,0)}=1, x_{(1,0)}=−1, h2=1−T, N=T², quotient 1, h1=1. Product coefficient algebra in `product` (L55–62) is the convolution with reduced `mul`.

## C. Raw pivot, exact divisibility, padding, CRT UNIT gluing, separator pullback — CONFIRMED

- Raw pivot: N = b − Σ h_i f_i (L245–256); exact monic divisibility required (L258); `raw_multiplier = (N/fhat)·c^{-1}` (L259), i.e. (N/fhat)/lc(raw). Degree bound `len ≤ 26−d` required (L260) — target-specific: b=q^5 with deg q ≤ 5 gives deg b ≤ 25; deg(h_i f_i) ≤ 2d−1 ≤ 9. No arbitrary V-target is accepted anywhere.
- CRT (L265–277): cofactor exactness, certified unit inverse, idempotent E_a, and the complete projection identity checked on EVERY leaf (1 on own leaf, 0 on all others). Gluing `hs[i] += E_a·lift(h_{i,a})` in whole coordinates never raises T-degree; all nine padded to 26 slots (L278) and flattened to exactly 9·26·7 = 1638 at index ((i·26)+j)·7+l (L279–280), matching checker.py L129 and the certificate column_order (L137).
- Separator pullback (L224–237): for every old coordinate (k=0..30, l=0..6) the image `R_a(v^l T^k)` is built by iterated `T·power mod fhat` (L234) and scaled by `v^l mod p_a`, paired with the per-leaf slice of mu, indexed 7k+l (matches checker L149/L153). Annihilation of all 1638 old columns follows from design §6 (premise) since every column image lies in W. Hand trace lost-component: mu = row 0 of I, λ_{0,0} = 1, λ_{0,6} = −720, and λ(1−e0) = 0·1 + (−1/720)(−720) = 1.
- No 217×1638 matrix, no factor selection, no short certificate: `certificate()` requires full length 1638/217 (L131). The all-zero-leaf separator is likewise full 217 (L155–160).

## D. Parser / checker / evidence / authority binding compatibility — CONFIRMED (one GAP)

- `candidate(data, flint)` (L283–312) still requires the literal schema, the literal NON-monic frozen modulus wire from `algebra.modulus()` (L291), nine indexed rows with the fixed ids/envelopes (L286–306), entire-B coefficients (L299), the full guard (L308–311); only then monic-normalises by the rational leading coefficient (L312). Synthetic moduli cannot pass this parser. The checker (unchanged, L40–47) independently rebuilds the same literal modulus.
- main() (L314–329): authorize → evidence.verified → producer_environment → `import flint` + version/path/hash → candidate (algebra imported inside) → write_exclusive. Mathematical imports occur only after authorization. The `solver_sha256` propagates via the ordinary flat pin: evidence.verified L85–87 requires solver.py pinned in `file_sha256`, and checker.main L167–168 compares the certificate's `solver_sha256` against that same pin. No new authority/caller/schema.
- Harness main (generic_controls.py L377–421): gate hash (L382) → import gate → authorize (L385) → evidence hash (L386) → import evidence → authority re-hash (L389) → strict load → `univariate_acceptance is None` (L392) → cwd (L394) → interpreter (L395) → six flat pins + four FROZEN (L397–402) → output absolute (L404) → 21 absences with `lexists` (L406–411) → producer_environment → `import flint` + checks (L415–419) → `from solver import generic_candidate` (L420). solver.py's module level imports only sys/pathlib/execution_gate, so the import order stays clean. Both CLIs explicitly insert the flat dir into sys.path, as `-I` requires.
- Isolation: `generic_candidate` is a plain importable function; protection is cooperative custody (evidence.py L4, solver L13–14, controls report L23), not same-UID authentication. Statically compatible; no new supervisor design proposed.
- GAP-D1: the claim that main() and the CLI tail are text-identical to the old 17z solver (code report L26–28, STATIC-REVIEW L47) cannot be checked here; the old solver is not an input. Its content is consistent with checker.main and evidence.verified as read.

## E. Independent dense Fraction verifier and hand expectations — CONFIRMED

- `DenseFixture` (L87–227) uses only `fractions.Fraction`, the FIXTURE p, its own Euclidean squarefree test (L101–105), dense 13-slot B multiplication reduced by the monic p (L134–144), and dense T convolution. No solver/algebra/FLINT helper, matrix or `construction_trace` is read (trace keys are ignored, forbidden binding keys refused L157–159).
- UNIT: all 9 multipliers × 26 slots × 7 from index (i·26+j)·7+ell, product ≤ 31, all 217 coordinates visited then compared (`checked == 217`, L192–198). SEPARATOR: all 1638 (i,j,ell) pairings and all 217 target coordinates visited before the predicates (L201–225). Counts asserted before pass/fail.
- Eight positives (L260–268) match INTERFACE L67–71 exactly; hand-traced through the solver's control flow: allzero-q0 → zero 1638 UNIT; allzero-q1 → λ=(1,0,…) SEPARATOR; constant-degree25 → h1=T^25 (26 slots); raw-two-T → inverse 1/2, h1=T^4/2; nonreduced → h2=1−T, h1=1; lost-component → split v | p/v, SEPARATOR λ_{0,0}=1, λ_{0,6}=−720; varying-pivot → pivots f1 on v-leaf and f2 on p/v-leaf, E_v=e0, h1=e0T^4, h2=(1−e0)T^3; all-generators → h2=−1, h1=1. Expected branches agree with PLAN L58–67.
- Four negatives (L329–355): scaled separator → columns still 0, target pairing 2 → exactly `dual target normalization equals one`; +1 at witness[0] of raw-two-T → identity off by 2T → exactly `full 217-coordinate sum h_i f_i equals q^5`; popped last pair → exactly `complete rational witness dimension` (framing, before arithmetic); p=v^7 → `candidate_refusal` reaches solver L20 → exactly `generic modulus must be squarefree` via algebra.require (a plain ValueError). `reject` requires `type(error) is ValueError` and exact string, requires the object to differ, and treats acceptance or any other exception as failure (L309–323). PLAN L89–90 and the controls report L56 state honestly that negatives 3–4 are framing/precondition, not arithmetic successes; the summary records per-negative reasons rather than an arithmetic claim.

## F. Harness order, frozen outputs, sidecars, no-fallback; proceed decision — CONFIRMED

- Order confirmed in D. No source acceptance: `verified()` never called; `univariate_acceptance` must be null. Exclusive `open('x')`, chmod 0o444, read-back equality and digest for every sidecar (L277–286); 16 positive sidecars + 4 negatives + summary = the 21 names precomputed and required absent (L406–411). Final re-hash of every sidecar, every registered file and the authority before the exclusive summary (L357–373). Exact inventory 8/4 enforced (L356).
- Failure semantics: every `need` raises; the only `try` is in `reject`, which re-raises on mismatch or acceptance. No retry, cleanup, fallback engine or second solve anywhere. Solver failures likewise fail closed (`require`), with exactly one `.rref()` site.
- ROOT obligations remain separate: native closure completeness, python-flint runtime API semantics, caps, host/argv/cwd custody (execution_gate), and the registration of the exact OUTPUT-derived names.
- Decision: this code packet MAY PROCEED to ONE future finite generic validation, subject to ROOT registration. It has NOT passed anything; all twelve outcomes remain UNEXECUTED.

## GAP register (uncompleted checks)

- GAP-1: no syntax/import/AST/compile check exists anywhere (by mandate); a syntax error would fail closed at runtime, never produce a false pass.
- GAP-2: python-flint semantics assumed but not verifiable statically: `fmpq_mat(m, n)` zero-initialised, tuple `__setitem__`/`__getitem__`, `rref()` returning `(matrix, rank)`, `str(fmpq)` as `n` or `n/d`, `fmpq` comparison with int. Any mismatch raises (fail closed) or trips `rational()` L212–220.
- GAP-D1 as stated in D (old main() tail identity unverifiable here).
- GAP-3: annihilation of all 1638 columns by the small-system separator rests on design §6 / design gate E (accepted premise), not re-proved here; the harness will test it on all 1638 pairings for the two SEPARATOR fixtures.
- No REFUTED claim. No repair implemented or proposed beyond the non-blocking trace note in A.

## Own-only raised-OPEN / collision check

OPEN(S) RAISED: none. COLLISIONS: EMPTY — own two targets absent at 00:41 before creation; own-only check of this report and its box; no corpus scan, no broad xmodel listing. No Seal and no charge_basis line authored.

Own whole-read at 00:53:02 UTC: 94 lines, sections Custody, Read scope, A–F, GAP register, collision check; grep found no placeholder, no marker, no Seal, no charge_basis before this point; exactly the 15 custody hex tokens appear. Nothing follows the marker.

<!-- BODY-END -->
