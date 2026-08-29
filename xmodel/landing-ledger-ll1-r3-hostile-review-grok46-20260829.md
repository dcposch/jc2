# Hostile review: Fable5 LANDING-LEDGER LL-1 R3 provenance repair (2026-08-29)

Reviewer: Grok 4.6, independent adversarial mathematical referee.
Subject: `xmodel/landing-ledger-ll1-r3-provenance-repair-fable5-20260829.md`
together with packet `cases/landing_ledger_ll1_r3_20260829/`.
Date: 2026-08-29 (UTC).

Charge: verify that R3 repairs the two R2 findings (stale
`BOOK-OFFAXIS`/`REDUCTION` pins; tautological A1 engine-parity gate),
that parsed fixture facts are genuine source assertions, that the
R2-to-R3 mathematical-function identity and empty decision-change list
are true, that mutation fail-closed claims hold, and that the boundary
between proved mathematics, engine-record evidence, and still-unproved
completeness/landing/JC2 claims is exact. Review, do not repair. R2
mathematics is not re-litigated; it is checked for preservation.

Sealed-body verification (computed this session, SHA-256; body = every
byte through the final `---\n` separator, reproduced, not reinterpreted):

- producer full file:
  `f501bf91815aa7862fe36f665ea7ec7d379bc4c5f26502c4a0273bf97eff9aa6`;
- producer body through `---\n`:
  `d2876414c67a5b9fd692fb79977094bca4c6424eaf979f7f3455fe36785bffa1`
  (matches the printed self-hash).

Prior sealed inputs, rehashed this session (all match their pins):

- `xmodel/landing-ledger-ll1-r2-hostile-review-grok46-20260829.md`
  full `8f56d1e4f2b159bbddf170010d9ac85337639e00e3b4ea537e0cc218a7b9bcf0`,
  body `3673da4736301d645edc4ab08ea3cb60b1563df6c565200eac7cdaa57972472f`;
- `xmodel/landing-ledger-ll1-r2-repair-fable5-20260829.md`
  full `19df817d055f4124fb92ce5ba2d08d7610814a9c3c11d8fcf4da6a0711457530`,
  body `29e892dab4fa31c6ff122706fc751cde32108b200af30f116dce9949b3fecd2b`.

R2 packet `cases/landing_ledger_ll1_r2_20260829/` rehashed this session:
all six `MANIFEST.sha256` entries OK; hashes equal the R2 review's
packet table. R2 was not edited.

No web, AWS, CAS, canonical edit, commit, or push. No nested
formalization tree and no `jc2-lean` access. No global `git status`.
Targeted `git show HEAD:<pinned-file>` was used only on the five R3
source pins to reconstruct the R2 miss. Local computation was exact
integer/`Fraction` Python inside the packet directory plus in-memory
`readers=` mutations that never write the packet tree.

---

## 0. Verdict

**PASS.**

R3 does the narrow provenance/test-quality repair the R2 review
required. The two R2 pins that did not reproduce are re-issued against
the exact current bytes (and equal that review's own session hashes).
The tautological A1 check `all(2 * nu + 2 == 2 * nu + 2 ...)` is gone.
The charged 26-shape / 351-route family claim is parsed from pinned
fixture sentences with count-free regexes, cross-checked, compared to
derived packet data, and explicitly removed from proved scope. Source
drift and in-book tampering fail closed. Every listed
mathematical/classification function is byte-identical to R2. The
emitted LL-1 decision table is identical to R2 except for the
documented provenance annotations on the two chain records.

Maximum licensed promotion: **SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW**
of the R3 LL-1 (`td=6`, `m=2`) packet only. No AWS launch and no
canonical promotion are authorized by this review. A PASS may carry
nonblocking errata; none of E1–E4 falsifies the repair or warrants an
R4.

---

## 1. Clause-level findings

| id | clause / claim | verdict | independent status |
|---|---|---|---|
| F1 | Five source pins match current `ladder/` bytes | **PASS** | this-session SHA-256 equals `SOURCE_PINS` and the producer table |
| F2 | R2 stale pins (`34f5ea9d…`, `6b9376e0…`) superseded, not verified | **PASS** | recorded under `provenance.r2_superseded_pins`; match neither HEAD nor worktree |
| F3 | Re-pins equal the R2 review's session hashes | **PASS** | `BOOK-OFFAXIS` `7679db8a…`, `REDUCTION` `0a88db0d…` |
| F4 | 43 consumed-clause anchors present in the pinned bytes | **PASS** | compile and an independent membership scan: 0 missing |
| F5 | T7 mass / ν-menu / finite-entry formulas are in current `REDUCTION.md` | **PASS** | anchors `T7/mass-formula` … `T7/finite-menu` present; packet `entry_menu(6,2)` still unique on-axis `(3,3)`, type `(2,3)`, poles `(1,1,2)` twice |
| F6 | BOOK-OFFAXIS §4 off-axis empty at td=6 | **PASS** | verbatim `**td 6, 9 (all m); m=4 td 12**: off-axis sector EMPTY (0 raw entries).`; `offaxis == []` |
| F7 | P0 transport / AF2 / finiteness / four-escape menu | **PASS** | anchors present; `dirty_cells((3/2),2,4)` still exactly `{(21,15),(20,16),(7,5)}` plus pure-b |
| F8 | P1 ψ / shared St 9.4 budget | **PASS** | anchors present; terminals `(2/3,3)` budget 3 and `(3/4,4)` budget 2 unchanged |
| F9 | A1 tautology deleted | **PASS** | R2 `test_ll1_r2.py:80` had `2 * nu + 2 == 2 * nu + 2`; R3 has no such check (mentions only in docstrings) |
| F10 | A1 honest fixture-parity gate (8 checks) | **PASS** | pins, count-free re-parse, regression pin of parsed figures, residue child, 6-row parity table, DS4 on parsed inputs, not-re-run scope, empty `decision_changes` |
| F11 | 26/351 removed from proved scope | **PASS** | `ENGINE-REC` source string and `scope_firewall[6]` both say FIXTURE-CITED; engine is not re-run |
| F12 | Parsed figures are source assertions, not regex/count circularity | **PASS** with E2 | regexes contain no `26`/`351`/`24`/`276`/`601`; numbers are captured groups except `nu1_zch_shapes` (E2) |
| F13 | R2→R3 mathematical-function identity | **PASS** | all 33 listed functions byte-identical by AST source segment |
| F14 | `decision_changes = []` is true of the LL-1 book | **PASS** with E3 | list is hardcoded empty; independently confirmed: every merge/suffix/entry/residue verdict and the full residue JSON are identical to R2 |
| F15 | A6 source-drift / in-book tamper fail-closed (10) | **PASS** | packet tests plus an independent in-memory replay of all 10, plus 4 extra probes, 14/14 raise/fail as claimed |
| F16 | Ordinary and `-O` compile / validate / test | **PASS** | 139/139 both modes; validator and compiler exit 0 under `-O`; recompile byte-identical |
| F17 | Packet manifest | **PASS** | `shasum -a 256 -c MANIFEST.sha256` all six OK; this-session hashes equal the manifest |
| F18 | Completeness / landing / JC2 still unproved | **PASS** | firewall restated; packet does not claim them |
| E1 | Parity check 5's `ν=2..26` loop | **ERRATUM** (nonblocking) | algebraically `(aν+b−b)/ν==a`; the derived entry-frame half of the same `par(...)` is honest |
| E2 | `nu1_zch_shapes = shapes − mu1` | **ERRATUM** (nonblocking) | not a captured group; producer overclaim that every `engine_record` figure is a captured group |
| E3 | `decision_changes` is not a computed diff | **ERRATUM** (nonblocking) | schema-enforced empty list; truth of emptiness verified outside the packet |
| E4 | `ENGINE-REC` trust tier is `promoted` | **ERRATUM** (nonblocking) | cited on COVERED chain records; source string and firewall still say FIXTURE-CITED |

---

## 2. Replay census

Cwd `cases/landing_ledger_ll1_r3_20260829/` unless noted. Packet tree
not edited; `out/*.json` was rewritten by recompile and remained
byte-identical to the sealed artifacts.

| command | result this session |
|---|---|
| independent SHA-256 of all six packet files vs `MANIFEST.sha256` | all OK |
| independent SHA-256 of the five pinned `ladder/` files vs `SOURCE_PINS` | all MATCH |
| `shasum -a 256 -c MANIFEST.sha256` | all six OK |
| `python3 ll1_compiler.py` | `LL1-R3 compile OK (5 pins, 43 anchors, fixture parsed + parity)`; out-hashes `205e7f58…` / `7c7cfd3b…` |
| `python3 -O ll1_compiler.py` | same banner; same out-hashes |
| `python3 ll1_validator.py` | exit 0 |
| `python3 -O ll1_validator.py` | exit 0 (validator is assert-free; AST scan: 0 `Assert` nodes) |
| `python3 test_ll1_r3.py` | `mode: ordinary   passed: 139   failed: 0` |
| `python3 -O test_ll1_r3.py` | `mode: OPTIMIZED (-O)  passed: 139   failed: 0` |
| second `python3 ll1_compiler.py` | book `205e7f58…`, summary `7c7cfd3b…`, identity True |
| R2 `MANIFEST.sha256` recheck | all six OK, hashes equal the R2 review table |
| producer / R2-review body hashes | match printed self-hashes |
| AST `Assert` scan of compiler, validator, tests | empty |
| in-memory A6 + 4 extra mutations (`readers=` / book copies) | 14/14 fail closed |
| AST function-body identity of 33 math functions vs R2 | 33/33 identical |
| R2 vs R3 book decision comparison | residue JSON identical; 11 merge verdicts identical; suffix/entry/uncovered/synthetic identical; only chain `why`/`cert_chain`, `provenance`, `ENGINE-REC`, packet string, and one firewall line differ |

139 = 122 (R2) − 1 (deleted tautology) + 8 (A1 honest gate) + 10 (A6).
Confirmed by the `chk` helper's printed count, not by `assert`. Compiler
/ validator / tests contain no `Assert` AST nodes, so `-O` is not a
silent skip.

Packet hashes (this session = MANIFEST):

    839d3801757b40f405bde985766ff702d0f9f116860b126fb3d866c5cf8080b6  ll1_compiler.py
    76cfec348a5eed39e1fa0f9b95c0b761741234d33275eac06bc2c45b6e0f7cae  ll1_validator.py
    2cebe74b47b5ecd29e467a8d5f7c34bf7dae7dcef71aabe5f10872ab718d851a  test_ll1_r3.py
    5acc4b79a85173820c69f83cf01a758eb3deb57e8ee53f08b87bb6cbf87faf72  INVENTORY.md
    205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  out/ll1_book.json
    7c7cfd3b8feab21ec4d08da8a765458ffbbf43652e57c56c7da6069ef6cb9a04  out/ll1_summary.json

Source pins (this session = `SOURCE_PINS` = producer table):

    93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
    ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d  ladder/SHEET6-DEPTH.md
    7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77  ladder/BOOK-OFFAXIS.md
    0a88db0d136001a6c18343f941a80ecfaef5ceffcbe84e05c739a853d13c1936  ladder/REDUCTION.md
    841fa120fa2ae801578834c7b52c5aad600eb48df73b683e1db5c954caf7f7ac  ladder/SHEET6-DEPTH-REVIEW.md

HEAD blobs of the two re-pinned files, targeted `git show` (SHA-256 of
the HEAD payload, not a worktree hash):

    26f0c64e8cb80ee6bac62e69f91d21dea74b01187150fbc786551f6885a35eb0  HEAD:ladder/BOOK-OFFAXIS.md
    f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371  HEAD:ladder/REDUCTION.md

These equal the producer's reconstruction. R2's printed pins match
neither HEAD nor the current worktree. Targeted `git diff --numstat
HEAD --` on those two files is 64/29 and 229/69 (93 and 298 lines),
matching the producer. Four consumed anchors (`MRW/root-window`,
`MRW/root-window-open`, `MRW/header-2026-08-28`, `SEC3/mixed-menu-open`)
are absent from HEAD and present in the pinned worktree; that is why R3
must pin the current bytes. It is not a new LL-1 decision: R2 already
consumed the mixed-root window from this worktree without pinning it.

---

## 3. The two R2 findings, independently re-checked

### 3.1 Stale pins

The R2 review recorded `BOOK-OFFAXIS.md` pin `34f5ea9d…` against session
hash `7679db8a…`, and `REDUCTION.md` pin `6b9376e0…` against session
hash `0a88db0d…`. R3's `SOURCE_PINS` now holds exactly those session
hashes. Compile-time and validate-time both re-hash the files on disk
and raise `SOURCE DRIFT` on mismatch. The stale R2 values survive only
as `R2_SUPERSEDED_PINS` and are never verified — confirmed by reading
`verify_source_pins` (it iterates `SOURCE_PINS` only) and by the
validator's audit-trail equality check against `R2_SUPERSEDED_PINS`.

MULTIPOLE and DEPTH pins are unchanged from R2 and still reproduce.
`SHEET6-DEPTH-REVIEW.md` is a new fifth pin, required by the A1 fixture
gate, and reproduces.

The consumed T7 / P0 / P1 / §4 sentences the R2 review already
re-derived against these bytes are still in the files. Independent
spot-check of the load-bearing quotes:

- `REDUCTION.md` T7 aligned block contains
  `\Lambda(F)=\frac{a_Fb_F\alpha\beta}{\nu_F}`, `M_F&=b_F,`, the two
  ν-menu lines, `\Lambda(F)\ge\beta\ge3`, and "only finitely many entry
  data \(E\) occur".
- `BOOK-OFFAXIS.md` §4 still prints the empty td-6 off-axis sentence.
- `BOOK-OFFAXIS.md` §10 still prints the P0 four-escape menu
  `(21,15)→(2/3,3) λ≥2`, `(20,16)→(3/4,4) λ≥2`, `(7,5)`, pure-b, the
  finiteness bound `E | l·num(w_G)·T`, and P1
  `ψ = ⌈1/(1−w_G)⌉ − 1` with the worked `w=2/3` / `w=3/4` budgets.

R3 does not re-prove those formulas from Sigray. It pins them and
re-runs the R2 machinery against them. That is the charged repair.

### 3.2 Tautological A1 gate

R2 `test_ll1_r2.py` line 80 is exactly

    chk(all(2 * nu + 2 == 2 * nu + 2 for nu in range(2, 27)),
        "A1: reachable chain frames (2,nu,2nu+2) family formula")

That line is deleted. In its place A1 runs eight `chk` calls: disk pins
equal `SOURCE_PINS` and the book; a count-free re-parse equals the
compiled `engine_record`; a regression pin of the parsed figures; the
parsed residue child `(1/2,3,2,5)`; the six-row `engine_parity` table
all `OK`; DS4 on the parsed `(w,dq,dp,Δ)=(2,10,6,4)` recovering
`(5,3,1/2)` and the derived IIa cell; explicit `NOT re-run` /
`FIXTURE-CITED` scope; empty `decision_changes`.

`engine_parity_checks` compares derived packet data to parsed fixture
fields, never a constant to itself, except for the nonblocking
sub-loop in E1. The six recorded rows are:

1. parsed residue child equals derived IIa `Q=(6,12,3,2,5)` in shape
   space (`ρ=6/12`, `M=gcd(6,10)=2`, `κ̄=5`);
2. parsed DS4 inputs are the derived cell `(dp,dq)=(6,10)`, `Δ=4`,
   `w∈W(2)`;
3. DS4 recomputed on those inputs equals both parsed outputs and
   derived `(κ̄,X,X/dp)`;
4. parsed family first component equals derived `w0=2` with `W(2)={2}`
   and ν-coefficient equal to that `w`;
5. w-map on the family plus the derived entry frame `(ρ,ν,κ̄)=(1,2,5)`;
6. scope honesty (`NOT re-run`, cited from the two fixture files).

Rows 1–4 and 6 are honest derived-versus-parsed. Row 5's derived
entry-frame half is honest: `(5−1)/2=2`. Row 5's `ν=2..26` half is E1.
That does not restore the R2 tautology as the sole A1 engine-parity
check, and it does not put 26/351 back into proved scope.

---

## 4. Fixture facts are genuine source assertions

The seven `_RX_*` patterns contain no expected count. Every integer they
emit is a regex group from the pinned bytes. Confirmed by reading the
compiled patterns and by searching them for `26`, `351`, `24`, `276`,
`601`, `18427`, `17199` (none).

The sentences actually matched, quoted from the pinned files:

- `SHEET6-DEPTH.md` §6: `reachable frames are exactly {(2, ν, 2ν+2) : ν ≥ 2}`
  (the phase-4 record's 24 μ1-shapes; check 6); `351/351 pair
  depth-invariance`.
- `SHEET6-DEPTH.md` check 6: `all 26 promoted twopole_check phase-4 shapes
  have w = 2 at every instance`.
- `SHEET6-DEPTH-REVIEW.md` header: `l1only (byte-match: 26 pre-merge shapes,
  18427/17199/601/276 merge ledger, RESIDUE child (1/2, 3, 2, 5) at
  **351 parent pairs**`.
- `SHEET6-DEPTH-REVIEW.md` re-run bullet: `351/351: twopole_check.py l1only
  re-run — 26 shapes, RESIDUE child (1/2, 3, 2, 5) at 351 parent pairs,
  ZCH suffix-DEAD ×276, ν=1 ODE-dead 601` and
  `the w-formula PREDICTS the child: 2·(10, 6, 1)/4 = (κ̄, D/i, ρ) = (5, 3, 1/2)`.

Cross-consistency is across independent sentences, not inside one
regex: shape counts agree between DEPTH check 6 and both DEPTH-REVIEW
records; 351 agrees between DEPTH's `351/351 pair depth-invariance`,
the review header, and the re-run bullet; the residue-child 5-tuple
agrees between header and re-run; ledger `601`/`276` agree with the
named ODE-dead / ZCH-suffix-dead counts; the printed prediction
identity is arithmetically true as integers.

The A1 regression pin (`rec["shapes"]==26` etc.) hardcodes the parsed
values in the test file. That is a pin of parse *output*, which is the
anti-circularity design: a drifted source that still matches the
count-free pattern emits a different integer and fails the pin. A
regex that itself contained `26` would be the circularity the charge
forbade. It does not.

**E2.** `engine_record["nu1_zch_shapes"]` is `shapes - mu1_shapes`
(26−24=2), not a captured group. DEPTH never independently asserts
"2 ν=1-zch shapes"; it asserts 26 total and 24 μ1, plus that the 26
include "the ν=1 zch over-generation". The producer sentence "every
figure in the emitted `engine_record` is a captured group" is therefore
false for this one field. It is not count-circularity of 26/351, and
the test pin of `== 2` still fails if either captured count moves. Not
an R4.

The DEPTH frame tuple `{(2, ν, 2ν+2)}` sits next to an entry labelled
`(ρ, ν, κ̄)=(1, 2, 5)` and next to check 6's `w=2`. The compiler stores
the first component as `frame_family["w"]`. Numerically `w=ρ=2` on this
family, so the derived-versus-parsed equalities still hold either
reading. The packet's own chain record writes
`(w,nu,kbar)=(2, nu, 2nu+2)`. No decision hangs on the label.

---

## 5. Mathematical-function identity and the empty decision-change list

`INVENTORY.md` lists 33 unchanged functions. AST `get_source_segment`
comparison against the immutable R2 compiler: 33/33 byte-identical,
including `entry_menu`, `dirty_cells`, `terminal`,
`residue_enumeration`, `classify_family_I`, `iia_admitted`, `d9_*`,
`normalize_nu1_merge`, `synthetic_cap_probe`, and `canonical_json`.
New functions are only the provenance layer. `cert` is identical;
`TRUST` gains exactly one id, `ENGINE-REC`; no existing `TRUST` entry
is touched.

R3 `compile_book` / `derive_summary` / `validate` / `test_a1` / `main`
are changed as inventoried. Line counts match the inventory
(1204→1639, 305→351, 571→728). Tests `test_a2`, `test_a3`, `test_d9`,
`test_a4`, `test_a5`, `test_determinism`, `test_ll2_pointer` are
byte-identical to R2.

Independent book comparison (R2 sealed `out/` vs R3 sealed `out/`):

- `sections.residue_terminals` full JSON identical (23 rows);
- `sections.residue_steps` full JSON identical (72 rows);
- all 11 merge `record_id`/`verdict`/`classification` identical, and
  every non-`why`/non-`cert_chain` field identical;
- suffix rows fully identical (8 records);
- entry record fully identical;
- `uncovered == []`, synthetic probe UNCOVERED, unused registry,
  `obligations_ll2`, `w_cert_tokens`, `root_kill_certs` identical;
- first six `scope_firewall` lines identical; R3 adds a seventh
  FIXTURE-CITED line for 26/351.

The only decision-adjacent deltas are the two chain records:
`cert_chain` gains `ENGINE-REC`, and `why` grows the R-7 pointer.
Verdict remains `ADMITTED`. That is a provenance annotation, not a
changed LL-1 decision.

**E3.** `build_provenance` writes `"decision_changes": []` as a
literal. The validator rejects any nonempty list. The packet therefore
cannot record a decision change without failing SOURCE_READY; it does
not compute a diff against R2. The *claim* that the list is empty is
nonetheless true, because the independent comparison above found no
LL-1 decision change. An R4 that computed the diff would be diction
about bookkeeping, not a repair of a false mathematical claim.

---

## 6. Mutation fail-closed

The packet A6 battery (10 checks) passed under ordinary and `-O`. An
independent in-memory replay, importing the packet and never writing
it, reproduced all ten and added four extra probes:

| probe | result |
|---|---|
| A6-1 flipped byte in `BOOK-OFFAXIS` | `SOURCE DRIFT` at `verify_source_pins` |
| A6-2 `compile_book(readers=tampered)` | `LLError`, no book emitted |
| A6-3 `351 parent pairs` → `352` in DEPTH-REVIEW only (hash gate aside) | `ENGINE FIXTURE INCONSISTENT: parent-pair / depth-invariance agreement` |
| A6-4 deleted DEPTH `pair depth-invariance` sentence | `PARSE FAILED`, no silent default |
| A6-5 P0 finiteness anchor deleted | `CONSUMED CLAUSE MISSING` independent of the hash |
| A6-6 in-book pin replaced by `0*64` | validator `source_pins drift` |
| A6-7 in-book `parent_pairs=352` | validator `engine_record drift` against re-parse |
| A6-8 deleted `provenance` | `provenance section missing` |
| A6-9 fabricated `decision_changes` entry | rejected |
| A6-10 validator `readers=` of drifted bytes | `provenance fail-closed: SOURCE DRIFT` |
| extra: DEPTH-only `351/351` → `352/352` | `INCONSISTENT` |
| extra: `24 μ1-shapes` deleted | `PARSE FAILED` |
| extra: MULTIPOLE flipped byte at the validator | `SOURCE DRIFT` |
| extra: DEPTH-REVIEW flipped byte at compile | `SOURCE DRIFT` |

Retained R2 batteries still pass inside the 139: inverted A2 with empty
UNCOVERED as a pass and the planted sealed-5.4 row theorem-killed; four
presentations of `(2,8)` and the family-I split; D9 `n=2..6`; cap
firewall; residue regression and route-death fixpoint; the 17-mutation
A4 battery; recompile identity and no absolute paths. Those are R2
mathematics preserved, not re-proved here.

What A6 does *not* claim, and this review does not grant: fail-closed
on a source edit that preserves every pin, every anchor substring, and
every captured fixture integer. That is the ordinary limitation of
substring pins. The charged drift classes (byte flip, charged-count
tamper, deleted sentence, deleted consumed clause, in-book pin/record
tamper) are covered.

---

## 7. Exact claim boundary

Three layers, not two.

**Proved at this header (`td=6`, `m=2`), by the R2 mathematics R3
preserves and this review confirmed is unchanged.**

Unique on-axis T7 entry `Λ=(3,3)`, type `(2,3)`, poles `(1,1,2)` twice,
frame `(κ̄,M,ρ,w0)=(5,1,1,2)`, `W(2)={2}`, off-axis empty. Eleven-way
merge partition with a unique admitted interior cell IIa `(2,3,1)`,
child `Q=(6,12,3,2,5)`, `w_trunk=3/2`, `w_cert=W-CLOSED-FORM`. Family I
identified with MP6(c) before classification; odd `L` MP2-dead, even
`L` D9-dead including `s(0)=0`, `L=0` MP7-rejected. Empty real
`UNCOVERED`. First-step P0 menu exactly the four printed escapes.
Residue book 13 admissible terminals (2 boundary + 2 deeper slack-1 +
9 equality-fragile) and 9 route-dead states, byte-identical to R2.
Caps cannot reject. `M` is `gcd(dp,dq)` of the child. Derived-versus-
parsed parity of the frozen residue child and the DS4 identity against
that cell.

**Engine-record evidence, fixture-cited, not re-derived.**

The integers 26, 24, 351, 18427, 17199, 601, 276, and the historical
`twopole_check.py l1only` / phase-4 run that produced them. R3 parses
those sentences from pinned bytes, checks they agree with each other
and with the derived IIa child / `w0` / DS4, and refuses to compile if
they drift. It does not re-run the engine and does not prove those
counts. Citing `ENGINE-REC` on the COVERED chain records (E4) does not
change that, because the chain admission is the `W(2)={2}` closure, not
the count.

**Still unproved, and not licensed by R3 or by this review.**

`Cand(s)=CFG`. Any bound on segment depth. Any source landing, ceiling,
Keller, or JC2 statement. `G2-PSC`, `G2-BD`, `RPMC(C)`, the cofinal
degree ceiling. P0 menu completeness as a theorem at a general state
(still a cited BOOK-OFFAXIS §10 certificate; what is proved is the
superset search at this one state). Mixed all-`μ≥2` emission
completeness wherever reachable. Single-pole composite configurations
(REDUCTION HIGH 1). Realizability of ALIVE rows; recorded `λ` remain
AF2 lower bounds. LL-2 at `td=7`, `m=2`, including the off-axis entry
`Λ=(3,4)`, `(1,1,2)+(1,2,3)`, W-PRICED certification, dirty pre-merge
steps, case-III/E5 with the `H5a_reading` pin, and the 17-versus-2
books. MP8 equality rhetoric stays quarantined.

R3's own verdict is `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`. This
review agrees and does not raise it.

---

## 8. Nonblocking errata (not an R4)

**E1.** Parity row 5's loop is `(κ̄ − kbar_const)/ν == w` with
`κ̄ = aν + kbar_const`, hence `a == w`, which row 4 already requires.
The check message calls `kbar_const` "chain ρ". The derived half
`(5−1)/2 == 2` is the actual work. Do not read the `ν=2..26` loop as
independent engine replay.

**E2.** `nu1_zch_shapes` is a difference of captured counts. Correct
the producer sentence "every figure is a captured group" to "every
charged count other than this remainder is a captured group".

**E3.** `decision_changes` is a schema constant. The emptiness claim is
true by the §5 comparison, not by a packet-computed diff.

**E4.** `TRUST["ENGINE-REC"]["tier"]` is `promoted` while the source
string says FIXTURE-CITED. A COVERED chain record may cite it. Readers
must take the source string and `scope_firewall[6]`, not the tier
token, as the epistemic status of 26/351.

None of these restores a stale pin or a tautological 26/351 gate. None
changes an LL-1 decision. Diction is not an R4.

---

## 9. Promotion-safe wording

This review licenses a different-model review of the R3 packet at
`td=6`, `m=2` only. It does not license AWS, canonical promotion, a
landing lemma, a cofinal ceiling, or any JC2 claim. It does not
re-open or re-prove the R2 LL-1 mathematics; it verifies that
mathematics is preserved and that the two R2 provenance/test-quality
items are repaired. The phrase "complete derived residue book" remains
scoped to P0+P1+St 9.4 at this header, as in the R2 review. The phrase
"engine parity" means derived-versus-parsed agreement with a frozen
fixture, not a re-run of `twopole_check.py`.

---

## 10. Verdict restated

**PASS.** Both R2 findings are repaired: the pins now reproduce against
the exact current bytes, and A1 is an honest frozen-fixture parity gate
with the 26/351 counts out of proved scope and a fail-closed drift
firewall. The R2-to-R3 mathematical-function identity holds. The
decision-change list is empty as a fact about the book. Maximum
promotion: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`. Next obligation
is still LL-2 at `td=7` as specified in the R2 review §5. E1–E4 are
nonblocking errata; they do not justify an R4.

No JC2, landing, or ceiling claim is licensed by the sealed R3 body or
by this review.

---
Report-body self-hash (sha256 of every byte above this line): 618b609fe21a3812137815cbe380aec865186fe9cc9e29be4013c9dfdd34e006
Report-full self-hash (sha256 of every byte above this line): d3591ddf5598e06245e45df144a8d2d63ec7ef36881ad13076d689e92df8e21d
