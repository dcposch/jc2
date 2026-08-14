# NF-D.md — the neutral-word depth cap

Status: **PROVED for the H8-synchronized pure-neutral slice, relative
to CONS, with per-entry computable `D`; honest reductions NF-D-OB1/OB2
for the unported 13-x packets and non-synchronized words (2026-08-14,
round 1 of the depth-cap program).**

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

Machine gate: `cases/nfd_check.py` (19 checks, exit 0; count printed).
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

where `S(entry)` is the **live scale window** (§3): the finite set of
final synchronized degrees admitted by the entry's H8 scale law and
letter-domain valuations, and `Omega` counts prime factors with
multiplicity. Instances: `D = 4` for the td-7 direct entry; `D = 0`
for all three td-11 entries (§5).

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
* **Mechanism B (valuation window).** H8 equal quotient requires
  `v_p(P_0^{(1)} Pi_1) = v_p(P_0^{(2)} Pi_2)` for every prime `p`
  (the 11-A consumer). The letter domains pin `v_p(Pi_i)` for the
  packet's small primes (BOOK-N1/L6, `sol-td11-13-scope.md:278-288`):
  `w = 2` and `w = 3/2` force `u` odd (`v_2(Pi) = 0`); `w = 3`
  forces `3 ∤ u`; `w = 4/3` forces `3 | u+1`, so `3 ∤ u`
  (`v_3(Pi) = 0` in both). If the pinned valuations mismatch for
  some `p`, the system is unsatisfiable at EVERY depth including
  zero: `S = ∅` and `D = 0` — no live synchronized neutral stack
  exists at all.

`S` is computable per entry: finitely many primes appear in the
packet degrees, the valuation system is finite linear arithmetic, and
mechanism-A pins are certificate rows.

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

## 5. Instances

| entry | mechanism | live window `S` | `D` |
|---|---|---|---|
| td-7 direct `(9,15,7,3)@2` | A: ladder `2 -> 22610` | `{22610}`, `Pi = 11305 = 5·7·17·19` | **4** |
| 11-A `(2,3)`: `[1@2;2]+[2@3;4]` | B at `p = 2` (promoted) | `v_2(2 Pi) = 1` vs resonance-side `>= 3`: `∅` | **0** |
| 11-B `(2,5)`: `[1@3;2]+[3@4/3;6]` | B at `p = 3` | `v_3(2 Pi_1) = 0` vs `v_3(6 Pi_2) = 1` for ALL domain stacks: `∅` | **0** |
| 11-C `(2,3)`: `[1@2;2]+2[2@3/2;4]` | B at `p = 2` | `v_2(2 Pi_1) = 1` vs `v_2(4 Pi_2) = 2` for ALL domain stacks (either opponent): `∅` | **0** |

td-7 remarks. (i) The 15 factorization multisets of `11305` into
parts `>= 3` (all parts odd — N2-consistent) are the complete
neutral-stack menu; maximal depth 4, attained only by `{5,7,17,19}`.
CE3's letter `323 = 17·19` is one of the depth-lowering groupings.
(ii) The uniform tower theorem already kills every td-7 cell, so
there `D` is structural rather than load-bearing; it is the number a
compiler would have used.

td-11 remarks. `D = 0` means the synchronized-leg neutral
enumeration is EMPTY — it does not by itself kill the entries: their
other legs (charged/resonant and non-synchronized routes) are NF-P /
refile obligations. 11-B's legal `3 -> 2` resonance is a charged
step, outside the pure-neutral slice (same carve as 11-A's `5/8`);
11-A and 11-C are strict `w = 2` freezes, so their pure-neutral
verdict is unconditional within the slice.

## 6. The three counterexamples, run forward (consistency with NF-D)

NF-D predicts: no CE exhibits a live deep word. Verified exactly
(gate block E) — every one of the six configurations violates at
least one promoted boolean:

| CE | order | violated boolean(s) |
|---|---|---|
| CE1 `(3,5,7,9)` / `(3,7,5,9)` @ `P_0=2` | both | degree pin: `P_0 Pi = 1890 ≠ 22610`; window-zone placement also under the promoted Case-C X-refusal |
| CE2 `(5,3,7,11)` @ `P_0=30002` | A | pin: `30002·1155 ≠ 22610` (and `P_0 = 30002` is no filed packet) |
| CE2 `(5,7,3,11)` | B | pin, AND its own flipped prefix-δ atom (a failed delta-integrality is a refusal) |
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

## 8. Compiler consequence

For an entry with computed `D`: enumerate neutral stacks to depth
`D` on the exact fat record — finitely many words (td-7: the 15
multisets and their orderings), no quotient, no free-zone
identification, CE1–CE3 irrelevant by construction. `D = 0` entries
contribute an empty synchronized enumeration. Everything outside the
slice (OB1/OB2, multi-word deep zones, resonances) remains
fail-closed under the standing policies. NF-Z.md survives as the
record of the quotient program and for its in-zone results (`Z`,
`L*`, `theta*`), which round 4 left standing.

## 9. Reproduction

```bash
python3 cases/nfd_check.py     # 19 checks, exit 0 (count printed)
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
odd, max depth 4); D the td-11 valuation windows (letter-domain
`v_p` pins exhaustive over domain stacks incl. empty; 11-B `0 ≠ 1`
at `p=3`; 11-C `1 ≠ 2` at `p=2`; 11-A promoted numbers); E the six
CE configurations run forward — all dead, with the specific violated
booleans of §6. No git commit.
