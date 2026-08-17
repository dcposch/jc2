# BOOK-TD12.md — the td-12 type-(3,5) book

Status: **ALL 14 ENTRY-LEVEL CELLS TOWER-DEAD (2026-08-17, round 1;
entry/merge-cell tier, conditional on the named fail-closed
classes).** The last below-bound filed entry (TDBOUND's single
`td <= mn` discriminator) is adjudicated. Machine gate:
`cases/td12_book.py` (11 checks, exit 0). Sizing and skeleton per
`xmodel/sol-tdbound-review.md` §8. No git commit.

## 1. Entry data

```text
td = 12, r = 2, (alpha,beta) = (3,5), poles 2 x (6,1,2,5),
M = b = 2, w0 = 3/2, pole degree p = b*alpha = 6,
L6: gcd(8,5) = 1, budget td-2 = 10.
Packet (P1/Z1): (k0,l0) = (3,5), g_top = 8/3, alpha_1 = 10/3
(den 3 | p = 6 -- entry compatibility).
ONE two-leaf hierarchy; 14 cells: (1,1)x3, (1,2)x3, (2,1)x3,
(2,2)x5 (9 root + 5 interior; 11 orbits under the pole swap).
```

## 2. The window arithmetic — NO X EXISTS (the structural difference)

Both poles are identical `M = 2` seeds: there is no `M = 1` L-A
carrier, and the pole degree 6 caps every gap:

* the `(3/2,2)@6` one-step menu: `{5/21, 4/15, 5/21, 1/5}` — max
  `4/15 < 1/2`; no clean resonance at the seed;
* the neutral family `(u+1)/(6u) <= 1/5` (domain: `u` odd,
  `3 ∤ u`, `u >= 5`);
* merge-cell vertex gaps at worst-case index (`i_G = 6Π/μ >= 3`):
  the BB menus (identical to the td-11 rounds — they depend only on
  `(μ, w = 3/2)`) give a maximum of **`5/9`** (the cylinder family
  `(2ν+1)/(4ν+1)` at `i = 3`);
* budget-10 exact-core audit: zero steps at `>= 1/2` on the core.

The td-7/td-11 "X dies first and is refused" pattern does not apply.
The kill is the

**FIRST-DEATH REFUSAL THEOREM (entry tier).** *Whatever a
configuration's maximal gap is, its death step is refused: for every
candidate first death `g` (the menu, the whole neutral tower, every
merge-cell vertex including the cylinder family, and the audited
core strata), `den(alpha_m − 1 + g)` divides no cap candidate
`c | 6`, over the full register lattice (`alpha_1 = 10/3`; prefix
steps with `k | c` keep `den | lcm(3,c) ∈ {3,6}`).* Load-bearing
arithmetic: the menu gaps carry 5- and 7-parts; the **neutral
lemma** kills the whole tower in one line (`num ≡ 1 (mod u)` so
`u | den`, and `u` is coprime to 6); the cylinder's `(4ν+1)`-part
survives every cap. 54 candidates swept, zero unrefused.

## 3. Per-cell stamps

| arrivals | cells | stamp | instrument |
|---|---:|---|---|
| `(1,2)`, `(2,1)` | 6 | SPINE-DEAD-H8 | `6Π₁ = 3Π₂ ⇒ Π₂ = 2Π₁`; odd-letter domain forces `v₂(Π) = 0` both sides: `0 = 1` unsat |
| `(1,1)`, `(2,2)` | 8 | CLASH-DEAD-FIRSTDEATH | co-scaling inhabited (empty stacks pass); every candidate first death den-refused (§2) |

**14/14 dead. 0 LIVE, 0 DEFERRED.**

## 4. Fail-closed classes (KEEP-AS-POSSIBLY-LIVE, Rule 6)

(a) budget-10 beyond-core strata — the fleet FC1 lane is budget-9;
a td-12 lane needs `B = 10` (same two-tier design ports); (b) the
Q+E5/E5F refile; (c) `ν = 1`/NF-P modes (the NF-P classification
applies verbatim — same `(μ, 3/2)` menus); (d) current-state
arrivals beyond the audited core (the FC4-D sync-agnostic dichotomy
pattern applies with this entry's constants); (e) post-merge strata
via the FC5-D emission law (the cylinder family emits `w = 6`
constant), joining (a).

## 5. Consequence for TDBOUND

The single below-bound filed entry is now adjudicated: **the filed
ladder's live frontier is exactly {residue-A} plus the unadjudicated
above-bound entries (td 8, 10, 12-(2,3)/(2,5), 14).** Honest note
for the conjecture: this entry died CHEAPLY (entry-tier arithmetic),
i.e. `td <= mn` did NOT protect it — the bound is an upper bound,
not a realizability criterion; the only equality row (`td = mn`)
remains residue-A, and the sharpened frontier observation narrows to
that single realized point.

## 6. Reproduction

```bash
python3 cases/td12_book.py     # 11 checks, exit 0
```

P1 packet; S1 skeleton (14 = 3+3+3+5, 9/5, 11 orbits); W1 the menu
and no-X structure; F1–F4 the first-death refusal (lattice closure,
the neutral lemma, the 54-candidate sweep, the cylinder algebra);
H1 the spine kills; B1 the budget-10 core audit; C1–C2 stamps and
certificate. No git commit.
