# BOOK-TD12.md — the td-12 type-(3,5) book

Status: **PROMOTED AT THE HONEST TIER (2026-08-17, round 2 —
`xmodel/grok-td12-review.md` SOUND-WITH-ERRATA folded): all 14
entry-level cells TOWER-DEAD on the ENUMERATED candidate list (74
unique gaps, 78 raw — the round-1 "54" was a stale count), 6
SPINE-DEAD-H8 + 8 CLASH-DEAD-FIRSTDEATH, conditional on the SEVEN
named fail-closed classes.** The completeness of the candidate list
is LIST-RELATIVE with the residuals named (Lemma FD-TRICHOTOMY
below); no occurring unrefused first death was found by the hostile
replay. Machine gate: `cases/td12_book.py` (14 checks, exit 0).
Sizing/skeleton per `xmodel/sol-tdbound-review.md` §8. No git
commit.

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
* budget-10 exact-core audit (round-2 rebuild with CORRECT
  neutral/pure-b multipliers — the round-1 else-branch hardcode is
  fixed): zero steps at `>= 1/2`; the core's extra gaps form an
  INDEPENDENT refused-or-dominated family, not members of the 74.

The td-7/td-11 "X dies first and is refused" pattern does not apply
(and the td-11 NF-Z† DIE-horn does NOT port — there is no X; for
neutral words the first-death argument replaces it: a pure-neutral
prefix makes the first letter, `<= 1/5`, the first death, refused by
the neutral lemma). The kill is the

**FIRST-DEATH REFUSAL THEOREM (entry tier, ENUMERATED-LIST-RELATIVE;
round-2 restatement).** *The first death of a configuration is its
MAXIMAL gap. On the enumerated candidate families — the seed menu,
the neutral tower (`u >= 5`), the merge cells with the cylinder
family, 74 unique gaps (78 raw) — every candidate is den-refused:
`den(alpha_m − 1 + g)` divides no cap candidate `c | 6` over the
full register lattice (`alpha_1 = 10/3`; prefix steps with `k | c`
keep `den | lcm(3,c) ∈ {3,6}`). On the audited budget-10 core, the
route-maximal criterion holds: every step whose gap exceeds its
route's running maximum is itself refused (dominated descendant
gaps — e.g. the `1/6` resonance at `(3,1)` under its route's
refused `1/5` — need not refuse and are not claimed to).*

**Lemma FD-TRICHOTOMY (what makes the list complete, and where it
is not).** Every vertex of an entry-tier configuration is the pole
(level 0, the packet), a chain vertex (a seed-menu child, a neutral
letter, or a descendant-strata vertex), or the merge vertex (a BB
cell). Hence every candidate first death lies in the enumerated
union, EXCEPT the named residuals: (i) `u = 1` letters — admitted by
the raw domain law, gap `1/3`, **UNREFUSED** (`r = 8/3`, `den 3 | 3`)
— parked in NF-P/class (c), VISIBLY LOAD-BEARING (if `u = 1` is
ever a legal first death the theorem is false); (ii) beyond-core
descendant strata and the inherited px2 dirty caps — classes
(a)/(f); (iii) the BB menu bounds are the td-11 FC7 proved sups,
CITED not re-proved — class (g). The den-criterion is **NOT
gap-generic**: `g ∈ {1/3, 1/2, 2/3, 5/6}` are unrefused on this
lattice (exhibited in-gate; none but `1/3` occurs in any family).

Load-bearing arithmetic: the menu 5/7-parts; the **neutral lemma**
(`num ≡ 1 (mod u)` so `u | den`, `u` coprime to 6); the cylinder's
`(4ν+1)`-part by direct den computation to `ν = 399`.

## 3. Per-cell stamps

| arrivals | cells | stamp | instrument |
|---|---:|---|---|
| `(1,2)`, `(2,1)` | 6 | SPINE-DEAD-H8 | `6Π₁ = 3Π₂ ⇒ Π₂ = 2Π₁`; odd-letter domain forces `v₂(Π) = 0` both sides: `0 = 1` unsat |
| `(1,1)`, `(2,2)` | 8 | CLASH-DEAD-FIRSTDEATH | co-scaling inhabited (empty stacks pass); every candidate first death den-refused (§2) |

**14/14 dead. 0 LIVE, 0 DEFERRED.**

## 4. Fail-closed classes (SEVEN; KEEP-AS-POSSIBLY-LIVE, Rule 6)

(a) budget-10 beyond-core strata (the fleet FC1 lane is budget-9);
(b) the Q+E5/E5F refile; (c) `ν = 1`/NF-P — **LOAD-BEARING** (the
`u = 1` gap `1/3` is unrefused, gate B1b); (d) current-state
arrivals — **INHABITED** (distinct-state `P/μ` hits exist on the
enlarged core and fall to the sync-agnostic dichotomy at these
constants — sync ⇒ the same refusal lattice, no-sync ⇒ spine at the
current `P/μ`; the `μ = 3` pairs are the class witness); (e)
post-merge strata via FC5-D (the cylinder emits `w = 6` constant —
the identity `κ̄ = 3(2ν+1), d_q = 2ν+1`), joining (a); (f) cap-free
menu completeness at descendant states (the td-11 FC2 analog; the
core's extra gaps are a fragment; the inherited px2 `k<=6/lex<=40`
caps sit here); (g) the BB2/cylinder loop bounds = the td-11 FC7
proved sups, cited not re-proved (the geometric completeness rider
for the five MIXED cells).

Citation hygiene (review finding 7): St 8.4 is cited for `μ | 2`
only; St 8.5 does not apply at the merge; MP6's `M_G | Σμ_e` is used
only at its proved `ε = 0 = k` scope (the skeleton's divisor axis is
the authorized layer; cell-derived root-M rows would carry IDENTICAL
stamps — no instrument reads `M_root`).

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
python3 cases/td12_book.py     # 14 checks, exit 0
```

P1 packet; S1 skeleton (14 = 3+3+3+5, 9/5, 11 orbits); W1 the menu
and no-X structure; F1–F3 the refusal (lattice closure, the neutral
lemma, the 74-candidate sweep); F4 the cylinder by direct den
computation to `ν = 399`; H1a–b the de-tautologized spine checks;
B1 the corrected budget-10 core with the route-maximal criterion;
B1b the not-gap-generic counterexamples and the `u = 1` witness;
H1c the cross-state H8 dichotomy; C1–C2 stamps and the 7-class
certificate structure. No git commit.
