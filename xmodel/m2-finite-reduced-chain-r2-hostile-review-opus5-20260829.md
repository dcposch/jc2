# Hostile review: finite reduced P0 chain skeleton R2 (implementation repair)

Date: 2026-08-29 UTC (session date 2026-08-28 local).  Reviewer: Opus 5,
different-model adversarial referee.  Producer: Sol 5.6, integration lane.

Subject:
`xmodel/m2-finite-reduced-chain-skeleton-r2-repair-sol56-20260829.md` +
`cases/m2_finite_reduced_chain_skeleton_r2_20260829/`, against the frozen R1
packet `cases/m2_finite_reduced_chain_skeleton_r1_20260829/`, the R1 producer
report, and the two passing R1 reviews (Fable5, Grok 4.6).

Charge honored as written: theorem promotion is treated as already fixed at
the narrow `AUDIT.md` scope; this review does not re-vote on the theorem.  The
question decided here is whether R2 is a faithful and complete *implementation*
repair.  No web, AWS, commit, push, canonical edit, heavy CAS, or long/
high-memory local process.  `jc2-lean` was never accessed, listed, searched,
built, statused, or controlled.  No global `git status` and no workspace-wide
search were run; `git` was used only in two path-restricted read commands
(`git diff --stat -- ladder/BOOK-OFFAXIS.md cases/book_offaxis.py`,
`git ls-files -- <the two packet dirs>`).  All mutation work on private `/tmp`
copies.  The only file modified is this report.

## VERDICT: `PASS_IMPLEMENTATION_R2`

R2 is a faithful, complete, and minimal implementation repair of the two
findings the R1 reviews raised (Grok F2, Fable §5/§9.2).  Both repairs are
real and both are effective: the exact R1 defect is now caught by a new gate
that fires on it, and the `lex <= 0` semantic cap that passed R1's full
35-check suite byte-identically now fails R2's suite.  The promoted theorem is
untouched and legacy edge semantics are unchanged — verified byte-wise on a
360-cell grid, not just at the charged instance.

Three errata are recorded in §9.  One of them (E1) is a false attestation in
the R2 report about what the shipped test checks; the underlying property it
claims is nevertheless **true and independently verified here (151/151)**, so
it is an erratum rather than a repair blocker, on the same footing as the
`case-III`/`case-II` wording erratum that Fable recorded against R1 while
returning `PASS_WITH_NARROWING`.

**R2 can replace R1 as the canonical executable implementation.**  It does not
change the promoted theorem, and it does not change legacy edge semantics: on
every one of 360 sampled `(w0, M0, B)` cells the full canonical payload is
byte-identical to R1's after deleting exactly two fields, `schema` and
`first_predecessor`.

---

## 1. Custody — every charged hash recomputed, all exact

Body convention confirmed by construction: bytes strictly before the final
`\n---\n` separator, **including** the trailing newline of the last body line
(`before_sep_excl_nl` reproduces nothing).

| item | claimed | recomputed | match |
|---|---|---|---|
| R1 report, full | `239393d7…` | `239393d7747b6166544342100cfe56b9353860fc7f36cd31620f8fdd04299bad` | YES |
| R1 report, body | `8587625b…` | `8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb` | YES |
| Fable5 review, full | `3dab7f08…` | `3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f` | YES |
| Fable5 review, body | `28fc400c…` | `28fc400c6879a288f3f09a85668d3cd8e56ea88e518dfcdaaa41f26692651320` | YES |
| Grok 4.6 review, full | `bf4c56ae…` | `bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912` | YES |
| Grok 4.6 review, body | `c95fbe40…` | `c95fbe402dd4d9791290e914f7fbb9d12632400ae898ec2d9cc873db990f86a1` | YES |
| R2 repair report, full | (AUDIT `3a7c604b…`) | `3a7c604b1972681ef90982a94a10c61076d1f16502603ac39cefc802d7439398` | YES |
| R2 repair report, body | `995f310e…` | `995f310e19c20e373280c5328805f2261249150c9d0cb45d813107fa9c3f90c4` | YES |
| `finite_chain_skeleton_r2.py` | `b6f36340…` | `b6f363407af9ea16f83bb5c0b7ff5c659e0e69b372ef2ace47d1f53b8b768afb` | YES |
| `test_finite_chain_skeleton_r2.py` | `99670c46…` | `99670c469b66e7639f3046169ca3a7f8bbcda24890b19fe2018674adc23f7e19` | YES |
| R2 `README.md` | `f269eaeb…` | `f269eaeb33cd5bc5bacdcc6feab803025c4294c720401606ff67dc73c3d2ee5e` | YES |
| `td7_caseiii_special_nu_r1.py` (R2 copy) | `f064e093…` | `f064e0930dc11d05c7276fa0420418ecf1efc62eed9a9b10a69bc626b88fa558` | YES |
| `test_td7_caseiii_special_nu_r1.py` (R2 copy) | `f4cfa83d…` | `f4cfa83df42cd38975482160848bc35146f8c26a5c66a7f5b5190638201ab7a8` | YES |
| charged R2 JSON (`--w 3/2 --M 2 --budget 5`) | `13fc996f…` | `13fc996f56747a8e4b314da42007a15d89604860e3c89ba984fa35d18ee01df4` | YES |
| secondary R2 JSON (`--w 2 --M 4 --budget 4`) | `5eecfc4c…` | `5eecfc4c7d8478ab78c6a5db0dbb8611e008da452bedf41a8cae5183cf2797d7` | YES |
| charged state-table hash | `c2835aaf…` | `c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad` | YES |
| secondary state-table hash | `255f1fe2…` | `255f1fe24efce6921703a80155646f5a78f949f678c96043d47c0beec6ddfd7d` | YES |

R1-side custody (§5 below): all five R1 files hash to the values recorded in
the R1 report and in Fable's §1 table, including the `README.md` value
`f467f3da…` that only Fable recorded.  R1 charged JSON reproduces
`74f82b75fade7464dde5e9b57adb418110c0c8fc576a62a4898ef678c487cb18`; td-7
emitted JSON reproduces `1e70f2e384eace6b325753a752e1db9247f7e07ba29dbdc2548440bdbba4f3b5`
(the trailing newline of `print` is inside the hashed bytes).

**Custody note on cited canonicals (not an R2 defect).**  Two files the R1
reviews hashed have changed on disk since: `ladder/BOOK-OFFAXIS.md`
`34f5ea9d…` → `7679db8a…` and `cases/book_offaxis.py` `11567cee…` →
`c22e3a1f…`.  I checked what this costs:

- Grok's citation `BOOK-OFFAXIS.md:480-509` still lands exactly on P0 (`480`
  is the `**P0 (priced step menu …)**` line, `509` the last sanity line), and
  the printed step laws there are verbatim the ones R2 implements.  The
  working-tree hunks skip the whole P0 block (they jump from new-line 432 to
  new-line 550).
- The change is the *post-review correction being folded in*: P5 (now at
  line 634) carries a dated `2026-08-29 correction` paragraph stating 69 not
  70, citing both review hashes and Fable's resolvent identity.  The stale
  "70 states" prose is gone.  So the R1/R2 reports' "P5 says 70" sentence is
  now historical, not current.
- The legacy match survives the `book_offaxis.py` edit: on the current tree
  `close_p(Fraction(3,2), 2, 5)` returns 69 states, `capped=False`, and its
  `{(w,M): λ_min}` map is **equal** to the R2 packet map (checked key-by-key,
  22 vertex-realization entries alongside).

---

## 2. Replay — normal and optimized, independently

```text
python3    test_finite_chain_skeleton_r2.py   -> FINITE_CHAIN_SKELETON_R2_TEST_PASS checks=46
python3 -O test_finite_chain_skeleton_r2.py   -> FINITE_CHAIN_SKELETON_R2_TEST_PASS checks=46
python3    test_td7_caseiii_special_nu_r1.py  -> TD7_CASEIII_SPECIAL_NU_R1_TEST_PASS checks=17
python3 -O test_td7_caseiii_special_nu_r1.py  -> TD7_CASEIII_SPECIAL_NU_R1_TEST_PASS checks=17
python3    test_finite_chain_skeleton_r1.py   -> FINITE_CHAIN_SKELETON_R1_TEST_PASS checks=35
python3 -O test_finite_chain_skeleton_r1.py   -> FINITE_CHAIN_SKELETON_R1_TEST_PASS checks=35
```

Host `Python 3.9.6` (Clang 15).  Whole R2 suite 0.17 s wall including its
`-O` subprocess; charged closure 0.07 s.  No CAS, no long or high-memory
process.  `-O` is meaningful here because `require` is a real function, not
`assert`; I re-confirmed that on the R2 source line 40-42.

Check budget audited by hand and it reconciles to 46 exactly:
`divisors` 2, `pure_epsilon_congruences` 3, `derived_lex_bounds` 7
(1 + 3 `eps-T-positive-{0,1,2}` + 1 + 1 + 1), `charged_closure` 14 (8 golden
keys + 6), `predecessors_are_minimal` 2, `secondary_lex_regression` 9
(8 golden keys + monotonicity), `no_historical_caps` 6, `optimized_replay` 3.

Observed payload lines, both instances, reproduced exactly:

```text
(3/2, 2, B=5) 69 states  295 edges  maxnum 3  maxM 25  max_k 2  max_lex 0  derived-lex-max 27
(2,   4, B=4) 152 states 658 edges  maxnum 8  maxM 25  max_k 4  max_lex 2  derived-lex-max 99
```

---

## 3. Independent from-scratch reimplementation (the decisive anti-hardcoding check)

I wrote a third implementation directly from the printed P0 laws
(`ladder/BOOK-OFFAXIS.md:480-509`), deliberately different from the packet on
four axes:

1. **No `Δ` parametrization.**  The clean-resonant family is *derived* inside
   one uniform `(l, ε, k, Sm, lex, ν)` scan rather than special-cased; the
   packet's `Δ | num(w)` + `den(w) | dq` route is never used.
2. **Neutral children derived, not asserted.**  Instead of emitting
   `divisors(M)`, I compute `gcd(l, N)` over an explicit `N`-window with
   `den(w) | N` from the neutral vertex's own `κ̄ = w(ν+1) ∈ ℤ`.
3. **Different price minimizer.**  A forward DP over `(parts used, remaining
   Sm)` instead of the packet's pruned branch-and-bound.
4. **Pure-ε by direct `N`-window scan**, not by residue algebra.

Result:

```text
(3/2,2,B=5): states=69  edges=295  maxnum=3 maxM=25 max_k=2 max_lex=0
             sha c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad
(2,  4,B=4): states=152 edges=658 maxnum=8 maxM=25 max_k=4 max_lex=2
             sha 255f1fe24efce6921703a80155646f5a78f949f678c96043d47c0beec6ddfd7d
```

Both state-table hashes **and both expanded-edge counts** reproduce.  The
edge-count agreement is stronger than Fable's §1 independent check (which
matched states/hash/maxima); it means the packet's menu-dedup granularity —
`(w, M, cost, family, canonical(witness))` — collapses no distinct legal
parameter tuple and invents none.

Additionally, `152`, `658`, `99`, `255f1fe2…` and `c2835aaf…` appear **nowhere
in `finite_chain_skeleton_r2.py`** (grepped).  They live only in the test's
`expected` dicts, and they are reproduced by an implementation that has never
seen them.  The secondary regression is not hardcoded.

---

## 4. The Dijkstra predecessor defect, reconstructed and closed

### 4.1 The R1 defect, mechanically

R1 pushed on `child not in distance or child_spent < distance[child]`.
Because `distance[·]` is written only at *finalization*, the first disjunct is
true for every unfinalized child, so R1 pushed on **every** edge and recorded
the witness with `predecessor.setdefault(child, …)` — i.e. the **first push**,
which is the first-popped parent that has *any* edge to the child.  Dijkstra
pops parents in nondecreasing `distance`, but the edge cost is not accounted
for, so a parent at distance 3 with a cost-2 edge outranks a parent at
distance 4 with a cost-0 edge.  That is exactly the failure mode.

Reproduced at the charged instance, matching Grok's F2 reproducers to the digit:

```text
R1 (3/2,2,B=5):  2 of 68 non-root records are non-minimal
  (2/9, 9): λ_min = 4, record says (2/7,7)@3 --dirty,cost 2--> 5
  (1/2, 1): λ_min = 4, record says (3/10,10)@4 --pure-ε,cost 1--> 5
```

The defect is far from confined to those two: across a 360-cell
`(w0, M0, B)` grid R1 emits **895** non-minimal predecessor records.

### 4.2 R2 records minimum-cost witnesses — argument, then verification

R2 tracks `best_seen` (tentative distance), writes `best_seen[child]` and
`predecessor[child]` together on every *strict* improvement, and guards the pop
with `key in distance or spent != best_seen.get(key)`.  The correctness chain:

- Every push sets `best_seen[child] = child_spent` in the same statement, and
  `best_seen` is monotonically nonincreasing per key.  Hence any queued entry
  satisfies `spent >= best_seen[key]`, so `spent != best_seen[key]` is
  equivalent to `spent > best_seen[key]` — the pop guard discards exactly the
  stale entries and nothing else.  `best_seen.get(key)` is never `None` for a
  popped key: the root is seeded at line 294 and every other key enters
  `best_seen` at push time.
- At finalization `distance[key] = spent = best_seen[key]`, and with
  nonnegative costs `best_seen[key]` is then final.  The expansion writes
  `parent.lambda = spent = distance[parent]`, an already-finalized value.
- `predecessor[child]` is rewritten on precisely the strict decreases of
  `best_seen[child]`, so the surviving record is the one attached to the final
  `best_seen[child] = distance[child]`.  A zero-cost self-loop cannot write the
  root's record because `child_spent < best_seen[child]` is then false; the
  root therefore has no record, and the census is `state_count - 1`.

Verified independently — I did **not** reuse the packet's own gate.  My audit
adds four checks the packet does not make (P2, P3, P5, P6) plus a Bellman-Ford
control (P7):

```text
                                R1(3/2,2,5)   R2(3/2,2,5)   R2(2,4,4)
P1 census + root absent            True          True          True
P2 parent is a closure state       0 bad         0 bad         0 bad
P3 parent.lambda == λ_min(parent)  0 bad         0 bad         0 bad     [not gated by packet]
P4 parent.λ + step.λ == λ_min      2 BAD         0 bad         0 bad
P5 step literally in one_step()    0 bad         0 bad         0 bad     [not gated by packet]
P6 acyclic + rooted at entry       True          True          True      [not gated by packet]
P7 Bellman-Ford == λ_min table     True          True          True
records checked                    68            68            151
```

So R2's witness tree is a genuine minimum-cost shortest-path tree: every
record names a real parent at its true `λ_min` and a step that literally
occurs in that parent's `one_step` menu at that parent's remaining budget, and
the whole predecessor graph is an acyclic tree rooted at the entry.  The
independent Bellman-Ford relaxation over the expanded menu graph reproduces
the `λ_min` column at all three runs.

### 4.3 The repair changes nothing else

Structural diff of the two charged JSONs:

```text
first_predecessor : differs at 2 of 68 records -> ['1/2|1', '2/9|9']
schema            : 'm2-…-r1' -> 'm2-…-r2'
(every other key byte-equal)
```

Grid sweep, 360 cells (`w0` in 10 values incl. integers and `< 1` fractions;
`M0 ∈ {1,2,3,4,5,6,8,9,12}`; `B ∈ 0..3`), comparing full canonical payloads
after deleting only `schema` and `first_predecessor`:

```text
grid cells                 : 360
R1/R2 payload divergences  : 0
R1 non-minimal pred records: 895
R2 non-minimal pred records: 0
independent-impl agreement : 240/240   (states, edges, and state-table hash)
```

This is the concrete evidence for "no change to legacy edge semantics."

---

## 5. R1 is byte-untouched

Both packets are **untracked** in git (`git ls-files` on the two directories
returns empty), so there is no committed baseline; custody rests on hashes and
timestamps, both of which agree:

- All five R1 files hash to the values in the R1 report and Fable's §1 table,
  including `README.md` = `f467f3dae75c3e938c5c8abc8c365a1a3b668256cf516bb59499fb23d3911d55`,
  which the R1 report deliberately omitted and only Fable recorded.  Any edit
  after either review would have to be a SHA-256 preimage collision on five
  files simultaneously.
- mtimes: every R1 file is `18:27:33`–`18:31:37`; the Fable review is
  `18:57:48`, the Grok review `19:02:42`, the R2 repair report `19:07:25`, and
  the R2 sources `19:04`–`19:06`.  Nothing in R1 was touched after `18:31`.
- R1's suite still passes 35/35 under both modes and still emits
  `74f82b75…` for the charged JSON.

R2 also correctly re-ships the td-7 consumer pair **unchanged** (`f064e093…`,
`f4cfa83d…`), so that theorem's attestation is not silently re-derived.

---

## 6. Attack on the `(w,M,B) = (2,4,4)` secondary regression

**Not hardcoded** — see §3; an implementation that never saw the constants
reproduces `152 / 658 / 255f1fe2… / (8, 25, 4, 2)`.

**It genuinely exercises `lex`.**  Full census of the expanded menus:

```text
(3/2,2,B=5)  families: neutral 135, pure-ε 107, dirty  49, resonant  4
             dirty lex histogram      {0: 49}
             resonant implied-lex hist {1: 4}
(2,  4,B=4)  families: neutral 285, pure-ε 156, dirty 181, resonant 36
             dirty lex histogram      {0: 175, 1: 5, 2: 1}
             resonant implied-lex hist {1: 32, 2: 4}
```

`lex = 2` is realized by exactly one dirty step and it is legal under P0 by
hand-checkable arithmetic:

```text
(8/11, 11) at λ=3 :  l=11, ε=0, k=1, Sm=2, lex=2, ν=3
   C = 11·3 − 2 = 31          T = 2 + 11 = 13
   dq = 4·3+1 = 13            dp = 0 + 3·13 = 39      E = 11·13 − 39 = 104
   E = (l−ε) + νC = 11 + 93 = 104                     ✓
   l·a·T = 11·8·13 = 1144 = 104 · 11                  ✓  E | l·num(w)·T
   κ̄ = 11·(8/11)·13 / 104 = 1                        ✓  ∈ ℤ, ≥ 1
   w′ = 11·(8/11)·12/(3·104) = 4/13   M′ = gcd(39,13) = 13   price 1
```

with `lex = 1` at five further steps, e.g. `(2,4) --l=4,ε=0,k=2,Sm=2,ν=2-->
(4/3,3)` at price 2 — Fable's §5 exemplar, reproduced.  All six verified
against the printed transport, the strict NE laws, and Fable's resolvent
identity.

**Sharp caveat, and why the regression still works.**  I checked whether the
`lex ≥ 1` steps are *min-cost critical*: they are **not**.  Every `lex ≥ 1`
child at `(2,4,B=4)` also has a `lex = 0` route at the same minimum cost, so a
`lex ≤ 0` cap leaves 152 states with the same `λ_min` column — the state-table
hash alone would still be silent.  What kills the cap is the regression's
*other* pins.  Measured:

```text
MX1  dirty lex<=0 cap : secondary 142 states / 612 edges / hash 73bcf697 / max_lex 0   -> FAILS
MX2  dirty lex<=1 cap : secondary 152 states / 657 edges / hash 255f1fe2 / max_lex 1   -> FAILS
```

MX1 does move the state count (152 → 142) because at `B = 4` some `lex ≥ 1`
*resonant* and downstream states lose their only source; MX2 is caught only by
the edge count and `max_lex_observed`.  So the regression is effective, but its
effectiveness rests on `expanded_edge_count` and `max_lex_observed`, not on the
state hash.  Anyone who later prunes the golden dict down to "states + hash"
reopens Fable's M6 blind spot.  Recorded as risk R3.

**Divisor and congruence laws still exactly as validated by the R1 reviews.**
I machine-checked every emitted step of *both* charged closures — 953 steps
(neutral 420, dirty 230, pure-ε 263, resonant 40) — against, per family:
`l | M`; `ν ≥ 2`; `E = l·dq − dp > 0`; `E = (l−ε) + νC`; `T ≥ 1`; `C ≥ 1`;
`κ̄ = l·w·dq/E ∈ ℤ` and `≥ 1`; `E | l·num(w)·T`; **Fable's resolvent identity
`E·(l·a·(1+k+lex) − κ̄·d·C) = l·a·T`**; strict ε-NE `ε·dq < dp`;
`M′ = gcd(dp,dq)`; `w′ = l·w(dq−1)/(νE)`; the AF2 lower bound
`λ ≥ k + [ε ≥ 1]`; for resonance `Δ = (n−1)ν+1 ≥ 3`, `Δ | num(w)`,
`den(w) | dq`, `E = lΔ`, cost 0; for pure-ε `E = l−ε`, modulus
`lcm(E, d·E/gcd(d·E, l·a))`, `M′ = gcd(E, residue)`, cost `⌈l·w/ε⌉`, plus a
two-period completeness sweep confirming every legal `N` falls in a listed
class.  **Violations: NONE.**

I also re-derived the resolvent identity by hand rather than trusting Fable.
With `u = 1+k+lex`: `E = νC + (l−ε)` and
`E·u − dq·C = u(νC + l − ε) − (uν+1)C = u(l−ε) − C = l + Sm − uε = T`,
so `E·(l·a·u − κ̄·d·C) = l·a·(E·u − dq·C) = l·a·T`.  Since the parenthesis is
an integer whenever `κ̄ ∈ ℤ` and equals `l·a·T/E > 0`, we get both
`E | l·num(w)·T` **and** `E ≤ l·num(w)·T`.  The packet's enumeration of `E`
over `divisors(l·a·T)` is therefore provably complete, with no overshoot scan
needed; and the packet does not assume the converse — it recomputes `ν`,
re-derives `dp, dq`, asserts `l·dq − dp == E`, and re-tests `κ̄ ∈ ℤ`.

---

## 7. Hostile mutation battery

34 valid mutants on private `/tmp` copies (one wave-1 patch was syntactically
invalid and was re-done correctly in wave 2).  Each mutant runs the full
46-check suite and is separately probed for `(states, edges, sha8, max_lex,
max_k, max_num, max_M)` at both charged instances.

### 7.1 Predecessor updates

| mutant | suite | charged / secondary golden |
|---|---|---|
| MP1 revert to R1 `setdefault`-on-first-push | `CHECK_FAILED:predecessor-minimum-cost-coherence` | **unchanged at both** |
| MP2 truthful cost, lie about *which* parent | **PASS** | unchanged |
| MP3 non-strict improvement (`<=`) | `CHECK_FAILED:predecessor-tree-census` | unchanged |
| MP4 drop the root `best_seen` seed | hard `ValueError` (empty closure) | crash |
| MP5 predecessor overwritten on every edge | `CHECK_FAILED:predecessor-tree-census` | unchanged |
| MP6 parent λ inflated by 1 | `CHECK_FAILED:predecessor-minimum-cost-coherence` | unchanged |
| MP7 step λ recorded as 0 | `CHECK_FAILED:predecessor-minimum-cost-coherence` | unchanged |
| MP8 predecessor omitted for zero-cost steps | `CHECK_FAILED:charged-state_count` | 44 states |
| MP9 fabricated but arithmetically consistent step | **PASS** | unchanged |

MP1 is the headline: the exact R1 defect leaves **every** golden value
byte-identical at both instances and is caught *only* by the new gate.  MP6/MP7
confirm the gate is not vacuous.  MP2 and MP9 are the residual gap (§9 E2).

### 7.2 Pure-ε phantom handling and residue classes

| mutant | suite | charged / secondary |
|---|---|---|
| ME1 legacy all-divisors-of-`E` phantoms | `charged-expanded_edge_count` | 295→**347**, 658→**721**, *both hashes unchanged* |
| ME2 drop the residue-0 class | `pure-class-set` (then hard `ValueError`) | crash |
| ME3 `required_multiple` forgets `gcd(·, l·num(w))` | `pure-class-set` | 295→268, 658→610, hashes unchanged |
| ME4 `required_multiple` forgets the `l` factor | `charged-expanded_edge_count` | 295→294, 658→656 |
| MR1 modulus `= E` only | `pure-class-set` | 295→293, 658→656 |
| MR2 modulus `= required_multiple` only | `pure-class-set` | 295→268, 658→610 |
| MR3 residue window off-by-one | hard `ValueError: pure epsilon congruence census is empty` | crash |
| MR4 `M′ = gcd(E, residue+1)` (literal-`N` confusion) | `pure-bruteforce-residues` | 69→59 / 152→140, **both hashes change** |

ME1 independently re-confirms Fable's phantom-absorption lemma, now at **both**
instances: forcing legacy all-divisor semantics adds 52 and 63 edges
respectively and leaves both state-table hashes bit-identical.  R2 keeps the
exact congruence data and does not copy the over-emission, as its report says.

MR4 is worth flagging as a *positive*: Grok's warning that "residue 0 means
`N ≡ 0 (mod modulus)`, not `ν = −1`" is handled correctly.  `E | modulus` by
construction, so `gcd(E, 0) = E` is the right value for that class, and
`gcd(E, N) = gcd(E, N mod E)` makes the class label well defined; shifting the
label by one is caught immediately.

### 7.3 Budget accounting

| mutant | suite | charged / secondary |
|---|---|---|
| MB1 `kmax` without the ε subtraction | **PASS** | unchanged (sound loosening) |
| MB2 `kmax + 1` | **PASS** | unchanged (sound loosening) |
| MB3 `kmax − 1` | `charged-state_count` | 69→**52** / 152→**87** |
| MB4 admission `cost < remaining` | `charged-state_count` | 69→**33** / 152→**54** |
| MB5 menu built at full budget, ignoring spend | non-terminating | diverges (>25 s even at `B=2`) |
| MB6 NE-orbit price floor `max(1,·)` removed | **PASS** | unchanged |
| MB7 ε-root price floor `max(1,·)` removed | **PASS** | unchanged |

MB1/MB2 reproduce Grok's finding that the `k` bound is a tightener, not a
completeness patch; MB3 shows it is sharp from below.  MB6/MB7 are **not** blind
spots: the code gates `gap > 0` and `gap0 > 0` before the ceiling, and a
positive rational has `⌈·⌉ ≥ 1`, so `max(1, ⌈g⌉) ≡ ⌈g⌉` there.  These two
mutants are provably semantics-preserving rewrites — the printed AF2 `max(1,·)`
is redundant under strict NE.  MB5 is unsound (a state at spend `s` gets
`remaining = B`, so `child_spent` can exceed `B` and the budget never decays);
it does not fail closed, it diverges.

### 7.4 State deduplication and the pop guard

| mutant | suite | charged / secondary |
|---|---|---|
| MD1 menu deduped by child only | `charged-state_count` | 69→65 / 152 with 658→562, both hashes change |
| MD2 `step.key()` drops the witness | `charged-expanded_edge_count` | 295→290 / 658→632, hashes unchanged |
| MD3 pop guard drops the stale-entry clause | **PASS** | unchanged |
| MD4 pop guard drops the finalized clause | **PASS** | unchanged |

MD3/MD4 are also not blind spots: in a nonnegative-weight lazy-deletion
Dijkstra each clause is individually sufficient (a strictly-cheaper entry would
have been popped first, so a first pop of an unfinalized key always carries
`spent == best_seen[key]`; and pushes only happen on strict improvement, so no
key is ever pushed twice at the same cost).  The two-clause guard is
defence-in-depth, and R2 correctly did not *weaken* the guard while adding
`best_seen`.

### 7.5 Blind-spot probes carried forward from Fable's M-series

| mutant | suite | charged / secondary |
|---|---|---|
| MX1 semantic dirty `lex ≤ 0` cap (Fable M6) | `secondary-state_count` | charged **unchanged**; secondary 152→142 |
| MX2 semantic dirty `lex ≤ 1` cap | `secondary-expanded_edge_count` | charged unchanged; 658→657, max_lex 2→1 |
| MX3 resonant implied-`lex ≤ 1` cap (*uncounted* family) | `secondary-expanded_edge_count` | charged unchanged; 658→646, hash→`ffa9e2c3` |
| MX4 `ν ≥ 1` admitted in dirty (Fable M2) | `charged-expanded_edge_count` | 295→305 / 658→693, hashes unchanged |
| MX5 drop `den(w) | dq` in resonance (Fable M7) | `charged-expanded_edge_count` | 295→330, hash changes; 152→**153** |
| MX6 drop `κ̄ ∈ ℤ` in dirty (Fable M3) | `charged-state_count` | 69→**635**, maxnum 3→27 |

**MX1 is the precise measurement of what R2 bought.**  Under R1's 35-check
suite that mutant produced a byte-identical payload and passed; under R2's
suite it fails on the secondary state count.  Fable's recommendation is
discharged.

**MX3 is a new probe of mine.**  `max_lex_observed` counts only
`family == "dirty"`, so the clean-resonant family's implied `lex = (Δ−1)/ν`
(36 steps at the secondary instance, four of them with implied `lex = 2`) is
invisible to that metric.  A cap on the *resonant* branch would slip past
`max_lex_observed` entirely — but it is still caught, by the secondary edge
count and the secondary state hash.  So the blind spot in the metric does not
translate into a blind spot in the suite.  Worth stating explicitly because the
R2 report's phrase "records … `max_lex = 2`" invites the wrong reading.

**Battery totals:** 34 valid mutants — 25 killed by a named check or a hard
exception, 1 diverged without failing closed (MB5), 8 survived all 46 checks.
Of the 8 survivors, 6 (MB1, MB2, MB6, MB7, MD3, MD4) are provably
semantics-preserving or sound-loosening and are not defects; 2 (MP2, MP9) are
genuine gate gaps, recorded as E2.

---

## 8. What R2 did *not* change

Confirmed by reading the two diffs end to end and by §4.3:

- `finite_chain_skeleton_r2.py` differs from R1 in exactly two places: the
  `SCHEMA` string, and the seven-line predecessor/queue block.  No formula, no
  bound, no gate, no enumeration order, no price, no dedup key.
- `test_finite_chain_skeleton_r2.py` adds two functions and rewires the source
  path/banner; the 35 R1 checks are carried over verbatim, including
  `test_no_historical_caps`' forbidden-token list.
- `td7_caseiii_special_nu_r1.py` and its test are byte-identical copies.
- The R2 README's substantive claims all check out; it does drop R1's "Both
  ordinary and optimized test runs pass 35 fail-closed checks" line without
  replacing it with the new count (erratum E3).

The R2 report's sentence "Only the predecessor portion of its JSON changes" is
one field short: `schema` also changes.  Trivial, noted for exactness.

---

## 9. Errata (none blocking; E1 must be corrected in the record)

**E1 — the R2 report overstates the new gate's coverage.**  It says:

> "A new gate checks all 151/151 non-root predecessor records against
> finalized costs in the secondary run and all 68/68 in the charged run."

`test_predecessors_are_minimal()` calls `close_reduced_skeleton(Fraction(3,2),
2, 5)` and nothing else.  The 151 secondary records are **never gated** by the
shipped suite; `test_secondary_lex_regression()` checks eight golden keys plus
the monotonicity flag and does not touch `first_predecessor`.  The charged
`68/68` half of the sentence is accurate.

The claimed *property* is nevertheless true: I verified all **151/151**
secondary records here, against a stronger predicate than the packet's
(§4.2, P2–P6), plus full-payload determinism of the secondary run.  So the
conclusion stands and only the attestation is wrong.  Repair is two lines —
either parametrize `test_predecessors_are_minimal` over both instances, or
strike the words "in the secondary run and" from the report.  I recommend the
former, since it is the version the record already claims.

**E2 — the new gate is a cost-arithmetic gate, not a witness-realizability
gate.**  It checks only `parent.lambda + step.lambda == λ_min(child)` and the
census.  Two independent fabrications survive all 46 checks:

- MP2: keep the true parent cost but name the **root** as the parent;
- MP9: keep the true parent and cost but replace the step by a fabricated
  `clean-neutral` record with witness `{"fabricated": true}`.

The shipped R2 code is correct — my P2/P3/P5/P6 audit passes on all 68 charged
and all 151 secondary records — but a future regression in the witness payload
would not be caught.  Cheap hardening: assert `parent.lambda ==
λ_min(parent)` and that the recorded step is a member of
`one_step(parent, B − λ_min(parent))`.  That is the P3/P5 pair and it costs
two lines.

**E3 — cosmetic staleness in the R2 test file.**  Its module docstring still
reads "…tests for `finite_chain_skeleton_r1.py`" (line 2) and `load_module`
still registers the module under the name `"finite_chain_skeleton_r1"`
(line 19) while loading the R2 source.  Harmless in isolation — the suites are
never run in one process — but it is exactly the kind of name reuse that makes
a later co-import silently resolve to the wrong module.  The R2 README also
dropped the check-count sentence without restating `46`.

**Carried forward, still true of R2 (not new):** Fable's R1 erratum that
chain-1's handshake is **case II**, not case III, is unrepaired in the td-7
docstring/JSON prose, which R2 re-ships byte-identically.  Correct to leave the
files frozen; correct in a successor rev to fix the word.

---

## 10. Answer to the charge

**Can R2 replace R1 as the canonical executable implementation without
changing the promoted theorem or legacy edge semantics?  Yes.**

- *Promoted theorem*: untouched.  R2 introduces no mathematical content.  The
  charged payload `(3/2, 2, B=5)` — 69 states, 295 edges, max numerator 3,
  max `M = 25`, hash `c2835aaf…` — is bit-identical to R1's, and the
  `AUDIT.md` promotion paragraph already anticipates R2 in exactly these terms.
- *Legacy edge semantics*: unchanged, and this is now measured rather than
  asserted — 360 grid cells with zero divergence after deleting only `schema`
  and `first_predecessor`, plus the current-tree `close_p` map equality.
- *The two review-requested repairs*: both implemented, both effective, both
  minimal.  MP1 and MX1 are the direct proofs.
- *Residual defects*: three errata, all in the report/test layer, none touching
  the executable's outputs.

---

## 11. Residual risks

**R1 — E1 stands in the record until corrected.**  `AUDIT.md` cites R2's body
hash `995f310e…` as an unreviewed source successor.  If that report is later
read as attestation that the suite gates secondary predecessors, a regression
there would go unnoticed.  This review is the correction of record; a
successor rev should carry the two-line test change.

**R2 — the golden dict is load-bearing in a way the state hash is not.**  At
`(2,4,B=4)` no `lex ≥ 1` dirty step is min-cost critical, so `lex` protection
rides on `expanded_edge_count` and `max_lex_observed`, not on
`state_table_sha256`.  Any future trimming of the `expected` dicts to
"states + hash" silently reopens Fable's M6.

**R3 — `max_lex_observed` and `max_k_observed` count only the `dirty` family.**
36 resonant steps at the secondary instance carry implied `lex ∈ {1,2}` and are
excluded from the metric.  The suite still catches a resonant-`lex` cap (MX3)
via edges/hash, but the *metric* under-reports and should not be cited as "the
largest `lex` reached."

**R4 — MB5-class errors diverge instead of failing closed.**  Making the menu
budget-independent produces a non-terminating closure rather than a caught
error.  There is no wall-clock or state-count tripwire anywhere in the packet.
For a desk-scale instrument this is acceptable; it should not be inherited by
anything that runs unattended.

**R5 — cited-canonical drift.**  `ladder/BOOK-OFFAXIS.md` and
`cases/book_offaxis.py` no longer hash to the values the R1 reviews recorded.
I checked the consequences (§1) and found the P0 block untouched, the P5 prose
already corrected, and the legacy 69-state map still equal — but future
reviewers must re-verify rather than trust the R1 review hash table.

**R6 — scope, unchanged.**  Everything the R1 reviews put outside the theorem
stays outside: last-vertex `ν`, `κ̄` along consumers, full pattern degree,
merge q-extra families, partner-dependent merge legality, generic-AP consumer
uniformity, full-configuration landing, `G2-BD`, a cofinal topological-degree
bound, realizability, a Keller counterexample, JC2.  R2 asserts none of these
and this review promotes none of them.

---

## 12. Artifacts and boundaries

Scratch, all under `/tmp/opus5-r2/` (nothing canonical written except this
report):

- `indep.py` — independent from-scratch closure (§3);
- `pred_audit.py` — P1–P7 predecessor audit incl. Bellman-Ford control (§4.2);
- `grid_equiv.py` — 360-cell R1/R2 equivalence + 240-cell independent
  agreement (§4.3);
- `lex_census.py` — lex/resonance census and P0 hand-checks (§6);
- `laws.py` — 953-step law and resolvent-identity conformance (§6);
- `mutate.py`, `mutate2.py`, `golden_probe.py`, `mut/`, `mut2/` — the 34-mutant
  battery (§7);
- replayed JSONs `charged-r2.json` `13fc996f…`, `secondary-r2.json`
  `5eecfc4c…`, `charged-r1.json` `74f82b75…`, `td7.json` `1e70f2e3…`.

No web, no AWS, no commit, no push, no canonical edit, no heavy CAS, no long or
high-memory local process (longest single command 65 s; peak working set a few
tens of MB).  `jc2-lean` was not accessed, listed, searched, built, statused, or
controlled.  No global `git status`; no workspace-wide search.  `git` was used
only in the two path-restricted read-only commands named in the header.

---
Report-body SHA-256 (bytes before the separator line above): `2f51e5d7b56c995496509767a24f9ec1824987f07b30f7b76d688e2b9726c32e`
