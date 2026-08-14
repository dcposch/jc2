# NF-D.md — the neutral-word depth cap

Status: **PROVED on mechanism-A entries (finite certificate-pinned
scale window; td-7 direct: `D = 4`, 15 multisets, 75 ordered words);
td-11 `D` is OPEN — the μ-corrected H8 windows are infinite residue
classes, not empty (2026-08-14, round 2, post
`xmodel/grok-nfd-review.md`).**

**Round-1 review verdict folded (grok-nfd-review finding 1, a
break):** round 1 computed the td-11 windows with raw
`v_p(P_0 Pi)` equality. The H8 law is **`P/μ` with `μ | M`** of the
current state (`sol-normalform.md` (1.4), line 165; the current code
sets `μ = M`, and td-7's main join, BOOK-OFFAXIS Class A, is exactly
the unequal pair `(μ_1, μ_2) = (1, 2)`). The promoted 11-A
certificate compares raw `P` only because both its arrivals have
`M = 1`. With `μ = M` every round-1 valuation mismatch EQUALIZES —
empty stacks pass H8 (`2/1 = 4/2 = 6/3 = 2`) and `Pi_1 = Pi_2` gives
an infinite legal family (`Pi = 5^k` on both poles, any depth `k`).
Round-1's "`D = 0` at all three td-11 entries" and the derived
"empty synchronized enumeration" are WITHDRAWN — that was a
fail-open emptiness certificate from a stronger-than-true
constraint. §3 now carries the μ case-split, §5 the corrected
windows and the honest OPEN, §5.3 the mechanism-C exploration, §8
the corrected compiler statement. What survives round 1 unchanged
(review-confirmed): M1 permanence, the general theorem on
mechanism-A entries, td-7 `D = 4` with the complete menu, CE1–CE3
all dead, OB2's keep-direction.

Provenance — why this document exists: the neutral-word QUOTIENT
program (NF-Z.md) is closed. Three counterexamples across four review
rounds, each flipping a different CONS-consumed field under letter
reordering with equal invariants:

* **CE1** (grok-nfz-review finding 1): the ladder register —
  `(3,5,7,9)` vs `(3,7,5,9)` at `P_0 = 2`, different `alpha_exit`.
* **CE2** (round 3, ours): prefix-δ integrality — `(5,3,7,11)` vs
  `(5,7,3,11)` at `P_0 = 30002`, `g = 7/3`, atom-2 boolean flips
  when a menu denominator misses `P_0`.
* **CE3** (grok-nfz-final finding 1): the live-factor-cap /
  μ-integrality boolean at the first free atom after the last
  skeleton death — tails `(323,13,15,17)` vs `(13,15,323,17)` after
  `Z = (3,5,7,9,11)` at `P_0 = 2`: `den(alpha_*) = 13566` carries
  `17·19`, `P_Z = 20790` does not, and only the order in which the
  tail supplies `323 = 17·19` decides the first cap.  This falsifies
  round 3's SD-conditional exchange (Lemma 4.2a is a pure-word
  statement; the interleaved tail does not inherit its hypothesis).

All three say the same thing: **the free zone carries ordered
arithmetic (menu-denominator residues, the primes of `den(theta*)`)
that no finite invariant compresses.** The census does not need to
compress it. Every one of the six CE configurations is DEAD (§6): the
flips distinguish dead words from dead words. The true theorem is a
DEPTH CAP: in a LIVE configuration, sufficiently deep neutral words
are impossible regardless of their ordered fine structure, so the
compiler can enumerate neutral words to a finite depth on the exact
fat record and never needs the quotient.

Machine gate: `cases/nfd_check.py` (22 checks, exit 0; count printed).
`cases/nfz_check.py` (39, exit 0) remains the CE record;
`cases/tower_check.py` unchanged. Sources: `xmodel/grok-nfz-final.md`,
`xmodel/sol-normalform.md` §§0–4, `xmodel/sol-td11-13-scope.md` §3,
`cases/towers/t9_15_direct.json` (`tower.obstruction`, H8 rows),
`TOWER-UNIFORM.md`, NF-Z.md (the closed quotient record). No git
commit.

## 1. Statement and setting

Fix an entry with its labelled hierarchy, poleward anchors `P_0^(i)`
(the pole-pattern degrees `p = b·alpha` of `sol-td11-13-scope.md`
§3.1), and the promoted consumer list CONS (NF-Z.md §0). A neutral
word is a stack of cylinder-(2.5) letters `(l_j, u_j)`, `u_j >= 2`,
price 0, `w`-frozen; its running degree is `P_j = P_0·u_1···u_j`. A
configuration is **LIVE** if its downstream tower/census future is
not already dead: every death step satisfies delta-integrality at
every still-alive vertex, the cap/μ-integrality and aliveness laws
hold with integral factor exponents, and the terminal laws hold — in
particular the **H8 equal-quotient/scale synchronization** between
the entry's pole collapses, the consumer promoted as the td-7
f-degree ladder (`2 -> 22610`, `t9_15_direct.json:729`) and as
`H8_EQUAL_QUOTIENT_VP_MISMATCH` (11-A row).

**Conjecture NF-D (the reframe).** There is a computable bound
`D(entry)` such that every neutral word of depth `> D(entry)`
occurring in a live configuration is impossible — deep neutral words
are dead regardless of their ordered fine structure.

**Theorem (this round).** NF-D holds for the H8-synchronized
pure-neutral slice — the slice on which every promoted X/tower
statement is conditioned ("nonempty H8 synchronization stack",
`sol-td11-13-scope.md:304`) — with

```text
D(entry) = max { Omega(s / P_0) : s in S(entry) },    D = 0 if S = ∅,
```

where `S(entry)` is the **live scale window** (§3): the set of final
synchronized degrees admitted by the entry's H8 `P/μ` scale law
(μ-case-split, round 2) and letter-domain valuations, and `Omega`
counts prime factors with multiplicity. The theorem produces a
finite `D` exactly when `S` is finite — by a mechanism-A certificate
pin, or by mechanism-B unsatisfiability. Instances: `D = 4` for the
td-7 direct entry (mechanism A); the three td-11 entries have
INFINITE `S` under the corrected law and their `D` is **OPEN** (§5).

## 2. The monotone quantity

Each letter multiplies the running degree: `P_j = P_{j-1}·u_j` with
`u_j >= 2`. Hence

* **M1 (monotone exit).** `Omega(P_j) = Omega(P_0) + sum_i
  Omega(u_i)` is strictly increasing in `j` (by `>= 1` per letter,
  `>= 2` per composite letter), and `P_j` itself is strictly
  increasing — leaving any finite set of admissible scales is
  PERMANENT. A word of depth `r` forces `Omega(P_r/P_0) >= r`.
* **M2 (window-zone growth — the depth-0 instance).** Z2 gives
  consecutive word deaths in one run `k' >= u_j·u_{j+1} >= 4`, so any
  entry whose window cap is `c_0 < 4` (td-7: `k | 2`) refuses every
  window-zone run of length `>= 2` outright — the promoted
  neutral-depth rigidity corollary (N-closure), which is NF-D at
  depth 0 for the window zone. The in-zone segment is in any case
  bounded by `L* = floor(log2(3/(2 theta* P_0))) + 1` (NF-Z.md §2,
  survives review round 4).

M1 is the monotone quantity the depth cap runs on; M2 shows the same
growth mechanism already kills shallow structure wherever the cap is
small. What remains is to bound the admissible FINAL scale.

## 3. The live scale window `S(entry)`

The H8 synchronization law compares the two pole collapses' scales;
its promoted instantiations are:

* **Mechanism A (exact degree pin).** When the entry's f-degree
  ladder pins the synchronized chain's final degree to exact values,
  `S` is that value set. td-7 direct: the ladder `2 -> 22610` forces
  `P_0·Pi = 22610`, i.e. `Pi = 11305`, exactly
  (`t9_15_direct.json:729`: "its nu-product is forced to 11305 (odd)
  by the f-degree ladder 2 -> 22610").
* **Mechanism B (valuation window, μ-corrected in round 2).** H8
  equal quotient compares the scales **`P/μ` with `μ | M`** of the
  current state — NOT raw `P` (grok-nfd-review finding 1; the raw-`P`
  form is the `M = 1` specialization the promoted 11-A certificate
  happens to live in). Computing `S` therefore case-splits over the
  finitely many divisor assignments `μ_i | M_i`:
  `v_p(P_0^{(1)} Pi_1) − v_p(μ_1) = v_p(P_0^{(2)} Pi_2) − v_p(μ_2)`
  for every prime `p`, with the letter domains pinning `v_p(Pi_i)`
  (BOOK-N1/L6, `sol-td11-13-scope.md:278-288`: `w = 2` and `w = 3/2`
  force `u` odd, `v_2(Pi) = 0`; `w = 3` and `w = 4/3` force `3 ∤ u`,
  `v_3(Pi) = 0`) and the M-ledger constraining which `μ` survive a
  given stack (`M' = gcd(l, u+1)`, non-increasing — §5.3). If EVERY
  μ-branch is unsatisfiable, `S = ∅` and `D = 0`. If some branch is
  satisfiable, `S` is a RESIDUE CLASS — an infinite set unless a
  mechanism-A pin also holds — and mechanism B alone yields NO depth
  cap. A finite `D` from mechanism B is an unsat certificate, never
  a computation on a satisfiable system.

`S` is computable per entry as a constraint system (finitely many
primes, finitely many μ-branches, finite linear valuation
arithmetic) — but a computable SYSTEM is a finite SET of scales only
when unsatisfiable or mechanism-A-pinned (round-1's conflation of
these, flagged by the review, is withdrawn).

## 4. Theorem NF-D (synchronized pure-neutral slice) — proof

*Claim.* A live configuration cannot contain a synchronized neutral
word of depth `> D(entry) = max_{s ∈ S} Omega(s/P_0)`.

*Proof.* Liveness includes the H8 scale law, so the word's final
degree satisfies `P_r = P_0·Pi ∈ S`. Each letter contributes at
least one prime factor (M1), so `r <= Omega(Pi) = Omega(P_r/P_0)
<= D`. If `S = ∅` no synchronized stack of any depth (including the
bare route, depth 0, when even that fails the valuation system) is
live. Monotonicity makes the bound effective for enumeration: once
`Omega(P_j/P_0) > D` the configuration is dead no matter how it
continues, because `P` never decreases (M1) — the exit is permanent
and order-independent. ∎

Note what is NOT claimed: no completeness of any finite quotient
below `theta*` (that program is closed — header), and nothing about
the ordered fine structure of words of depth `<= D`; those are
enumerated on the exact fat record.

## 5. Instances (round 2: td-11 corrected to the `P/μ` law)

| entry | μ-branch | window under H8 `= P/μ` | verdict |
|---|---|---|---|
| td-7 direct `(9,15,7,3)@2` | chain-1 frozen `(μ,w,M) = (1,2,1)` — μ-clean | mechanism A: ladder `2 -> 22610` pins `S = {22610}`, `Pi = 11305 = 5·7·17·19` | **`D = 4`** |
| 11-A `[1@2;2]+[2@3;4]` | `μ = (1,1)` | `Pi_1 = 2 Pi_2` with `Pi_1` odd: UNSAT (`v_2`: `0` vs `>= 1`) | branch empty |
| | `μ = (1,2)` (Class-A shape, `M` preserved) | `2Pi_1 = 4Pi_2/2` ⇒ `Pi_1 = Pi_2`, `Pi` odd and `3`-free: INFINITE residue class; empty stack passes (`2 = 4/2`); `Pi = 5^k` legal at every `k` | **`D` OPEN** |
| 11-B `[1@3;2]+[3@4/3;6]` | `μ = (1,1)` | `Pi_1 = 3 Pi_2` with `v_3(Pi_i) = 0`: UNSAT (`v_3`: `0` vs `1`) | branch empty |
| | `μ = (1,3)` (`M` preserved) | `2Pi_1 = 6Pi_2/3` ⇒ `Pi_1 = Pi_2`, `3`-free, side-2 letters `≡ 2 (mod 3)`: INFINITE; empty stack passes (`2 = 6/3`); `Pi = 5^k` legal | **`D` OPEN** |
| 11-C `[1@2;2]+2[2@3/2;4]` | `μ = (1,1)` | `Pi_1 = 2 Pi_2`, both odd: UNSAT (`v_2`: `0` vs `>= 1`) | branch empty |
| | `μ = (1,2)` (either opponent, `M` preserved) | `2Pi_1 = 4Pi_2/2` ⇒ `Pi_1 = Pi_2`, odd and `3`-free: INFINITE; empty stack passes; `Pi = 5^k` legal | **`D` OPEN** |

The round-1 unsat computations are exactly the `μ = (1,1)` rows —
true as raw-`P` statements, and NOT the H8 law on packets with
`M ∈ {2,3}`. The promoted 11-A row "`v_2(2Pi) = 1` vs `>= 3`" is the
MIXED charged/neutral resonance certificate
(`H8_EQUAL_QUOTIENT_VP_MISMATCH`, `sol-normalform.md:584-599`); it
stands as promoted but it is not a pure-neutral window computation
and is no longer cited as one (review repair (ii)).

### 5.1 td-7 remarks (unchanged, review-confirmed)

(i) The 15 factorization multisets of `11305` into parts `>= 3` (all
parts odd — N2-consistent) are the complete neutral-stack menu;
maximal depth 4, attained only by `{5,7,17,19}`; all parts distinct,
so the ordered census is `4! + 6·3! + 7·2! + 1 = 75` words. CE3's
letter `323 = 17·19` is one of the depth-lowering groupings. (ii)
The pin is μ-clean: chain-1 is frozen at `μ = 1` and the opponent
side's `22610` is charged/certificate-rigid. (iii) The uniform tower
theorem already kills every td-7 cell, so there `D` is structural
rather than load-bearing; it is the number a compiler would have
used.

### 5.2 td-11: why there is no pin (the structural dichotomy)

Mechanism A worked on td-7 because ONE synchronized side is
neutrally rigid — its scale `22610` is fixed by charged data, so the
neutral side must hit it exactly. On all three td-11 entries BOTH
synchronized sides are pole collapses that carry neutral stacks, and
the μ-corrected law makes them CO-SCALE (`Pi_1 = Pi_2`): padding
both poles in step stays in the window at every depth. That is
exactly why `S` is infinite: there is no rigid side to exhaust.
`D(11-A) = D(11-B) = D(11-C) = ` **OPEN**, and the entries'
pure-neutral synchronized legs are NOT empty. (11-B's `3 -> 2`
resonance remains a charged step outside this slice, as before.)

### 5.3 Mechanism C explored (per the pivot instruction): what it
gives and what it cannot

* **A real monotone fact (machine row D5): the M-ledger.**
  `M' = gcd(l, u+1)` is non-increasing along any stack and drops are
  irreversible. The live μ-branch of every td-11 window REQUIRES the
  arrival `M` (μ = M available at exit), so a single M-dropping
  letter (`l = 1` on the `M = 2` side) moves the configuration
  permanently into the unsat `μ = (1,1)` window: DEAD. Hence the
  live window forces `M` CONSTANT along the entire stack — a genuine
  cycle-flavored rigidity (the M-state may never move), and a
  per-letter constraint the compiler can enforce. It narrows the
  window; it does not bound depth (M-preserving letters exist at
  every depth: `l = M`, `M | u+1`).
* **A verdict-period ("depth beyond one period revisits a state")
  would be a quotient-completeness claim.** The residue data
  `(Pi mod 2, mod 3, μ-branch, M)` is indeed eventually periodic —
  finite state space — but concluding "same residue state ⇒ same
  live/dead verdict" is exactly the finite-invariant compression
  that CE1–CE3 refuted at the consumed-boolean level (the flips live
  in `den(theta*)`-primes and ordered prefix products, OUTSIDE any
  fixed finite modulus). A cycle argument on verdicts is therefore
  NOT available today; claiming it would repeat the NF-Z error with
  a period in place of an invariant. Explored and honestly declined.
* **What WOULD close td-11 depth** (either suffices):
  (a) a **depth-uniform kill** — the td-11 analog of the td-7
  uniform tower theorem: port the A/B/C window exhaustion to the
  `(2,3)`/`(2,5)` packets with the μ-corrected windows and kill
  every synchronized stack regardless of depth (then `D` is moot,
  as it is on td-7's cells); or
  (b) a **rigid-side certificate** — a mechanism-A pin from the
  11-x f-degree ladders, i.e. a charged/certificate-fixed scale on
  one synchronized side (nothing currently forces one; the co-scaling
  structure above is evidence against).
  Until one lands: OPEN, fail-closed (§7/§8).

## 6. The three counterexamples, run forward (consistency with NF-D)

NF-D predicts: no CE exhibits a live deep word. Verified exactly
(gate block E) — every one of the six configurations violates at
least one promoted boolean:

| CE | order | violated boolean(s) |
|---|---|---|
| CE1 `(3,5,7,9)` / `(3,7,5,9)` @ `P_0=2` | both | degree pin: `P_0 Pi = 1890 ≠ 22610`; window-zone placement also under the promoted Case-C X-refusal |
| CE2 `(5,3,7,11)` @ `P_0=30002` | A | pin: `30002·1155 ≠ 22610` (`P_0 = 30002` is no filed packet); prefix-δ atom 1 ALSO fails (`3 ∤ 30002·5` — both orders share this refusal) |
| CE2 `(5,7,3,11)` | B | pin, atom 1, AND the flipped atom 2 (the flip is atom 2; atom 1 fails in both orders — review round-1 precision note folded) |
| CE3 `(323,13,15,17)` after `Z` @ `P_0=2` | A | pin: `20790·1070745 ≠ 22610` |
| CE3 `(13,15,323,17)` after `Z` | B | pin, AND the flipped first-atom cap `k = 87297210 ∤ 270270` / μ-boolean `13566 ∤ P_1` |

So each CE flip distinguishes HOW a dead configuration dies, never a
live one from a dead one — exactly the data an emptiness census does
not consume once depth is capped. This is consistency evidence, not
a proof of NF-D beyond §4's slice.

## 7. Honest reductions and policy

* **NF-D-OB1 (13-x ports).** The 13-x packet menus, `alpha_1`, caps,
  and scale-law instantiations are NOT derivable from type `(2,3)`
  (port obligation, `sol-td11-13-scope.md:203-206`; Grok's round-4
  finding 2 makes the same point against G8-style hardcoding). Their
  `S`/`D` values await the ports. No number is claimed here.
* **NF-D-OB2 (non-synchronized words).** Neutral words on chains not
  carrying the H8 requirement are not covered by §4; a second pin
  (terminal M / E5F junction ladder) is plausible but NOT claimed.
  **POLICY (fail-closed, Sol rule 6, same interface as NF-Z†):**
  non-synchronized deep words stay on the exact fat record; no
  emptiness certificate may assume a depth cap there.
* Relative to CONS as a list; the H8 scale law is used exactly in
  its two promoted instantiations (mechanism A: td-7 f-degree
  ladder; mechanism B: 11-A `v_p` comparison). A different
  synchronization law re-opens §3.
* Resonance-bearing chains (`w`-changing steps) are NF-P's, as
  before.

## 8. Compiler consequence (round 2: the honest td-11 status)

What the arithmetic supports (the review's own closing formulation,
adopted):

* **td-7 (mechanism A): enumerate the 75 ordered synchronized words**
  (15 multisets) on the exact fat record — no quotient, no free-zone
  identification, CE1–CE3 irrelevant by construction.
* **td-11: do NOT discard synchronized neutrals.** The round-1
  claim "`D = 0` entries contribute an empty synchronized
  enumeration" is STRUCK — under the `P/μ` law the windows are
  inhabited (empty stack passes; `Pi = 5^k` at every depth), and
  emitting an empty synchronized-leg panel from the raw-`P`
  predicate would be a fail-open emptiness certificate
  (grok-nfd-review findings 1–2). td-11 synchronized neutrals are
  KEEP-AS-POSSIBLY-LIVE on the exact fat record (Rule 6), with the
  one proved narrowing that `M` must stay constant (§5.3, gate D5),
  until §5.3(a) or (b) closes the depth question.
* **Everything outside the slice** (OB1 13-x ports, OB2
  non-synchronized words, multi-word deep zones, resonances) remains
  fail-closed under the standing policies.

NF-Z.md survives as the record of the quotient program and for its
in-zone results (`Z`, `L*`, `theta*`), which round 4 left standing.

## 9. Reproduction

```bash
python3 cases/nfd_check.py     # 22 checks, exit 0 (count printed)
python3 cases/nfz_check.py     # 39 checks, exit 0 (CE record, unchanged)
python3 cases/tower_check.py   # promoted tower gate (unchanged)
```

`nfd_check.py` blocks: A CE3 replayed exactly on the interleaved
td-7 ladder (`den(alpha_*) = 13566` forced for every integer
register — `13566(l+1)−1 ≡ −1 (mod 17, 19)`; cap booleans
`[T,T,T,T]` with first `k = 39270` vs `[F,T,T,T]` with first
`k = 87297210`; μ-boolean flip; equal `I`; both tails legal, free,
sub-`theta*`); B the monotone quantity (M1 strict growth over all
orders, permanence, M2 `k' >= u u' >= 4 > 2`); C the td-7 window
(`22610 = 2·11305`, `Omega = 4`, the 15 factorization multisets, all
odd, max depth 4, 75 ordered words); D the μ-corrected td-11 windows
(letter-domain `v_p` pins as raw-`P` facts; the `μ = (1,1)` branches
UNSAT — the round-1 content, relabelled; the `μ = (1,M)` branches
INHABITED: empty-stack `P/μ` equality `2 = 4/2 = 6/3`, the
`Pi = 5^k` family legal on both poles at every scanned depth with
`M` preserved — `S` infinite, `D` OPEN; D5 the M-ledger
monotone/irreversible-drop fact and the drop-kills-branch row); E
the six CE configurations run forward — all dead, with the specific
violated booleans of §6 (CE2 atom-1 refusal shared by both orders).
No git commit.
