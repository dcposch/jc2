# Hostile review: finite reduced P0 chain skeleton R1

Date: 2026-08-29 UTC (session date 2026-08-28 local).  Reviewer: Fable 5,
different-model adversarial referee.  Subject packet:
`xmodel/m2-finite-reduced-chain-skeleton-sol56-20260829.md` +
`cases/m2_finite_reduced_chain_skeleton_r1_20260829/`.

Scope honored: BOOK-OFFAXIS §10 P0–P5, REDUCTION CRITICAL 4–7 + §5.2,
SHEET6-DEPTH §6–§7 (neutral/resonant step laws only), `cases/book_offaxis.py`
(the named legacy engine), and the packet itself.  No other ideation reports,
no `jc2-lean`, no git commands, no web/AWS/CAS.  All replays bounded stdlib
Python; all mutations on private `/tmp` copies; no canonical file edited
except this report.

## VERDICT: `PASS_WITH_NARROWING`

Both theorems are correct as scoped.  I re-derived every bound in the closure
proof independently, found a resolvent identity that upgrades the packet's
key divisor enumeration from "printed P0 fact" to "theorem of the printed
transport," rebuilt the entire closure from scratch in an independent
implementation that reproduces the exact state-table hash, and confirmed the
case-III special-value solve two ways with extended rectangles and an even-`h`
control.  No mathematical error found.  The narrowings: one wording erratum
(a case-II handshake called case III), a precise demotion of what the
69-state legacy match can corroborate (four load-bearing gates are invisible
to the charged instance, and one semantic mutation passes the full 35-check
suite), and a sharpened statement of the neutral-ray modulus for successor
consumers.

## 1. Hash and replay verification (all exact)

| item | claimed | recomputed | match |
|---|---|---|---|
| packet full file | (to recompute) | `239393d7747b6166544342100cfe56b9353860fc7f36cd31620f8fdd04299bad` | n/a |
| packet body (bytes before final `---`) | `8587625b…9bcb` | `8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb` | YES |
| `finite_chain_skeleton_r1.py` | `6e413ff6…8218` | same | YES |
| `test_finite_chain_skeleton_r1.py` | `cd80757d…c38e` | same | YES |
| `td7_caseiii_special_nu_r1.py` | `f064e093…f558` | same | YES |
| `test_td7_caseiii_special_nu_r1.py` | `f4cfa83d…b7a8` | same | YES |
| `README.md` (report omits by design) | — | `f467f3dae75c3e938c5c8abc8c365a1a3b668256cf516bb59499fb23d3911d55` | recorded |
| charged JSON (`--w 3/2 --M 2 --budget 5`) | `74f82b75…cb18` | same | YES |
| `state_table_sha256` | `c2835aaf…f1ad` | same | YES |
| td7 emitted JSON | `1e70f2e3…f3b5` | same | YES |

Replays: `test_finite_chain_skeleton_r1.py` passes 35/35 under `python3` and
`python3 -O`; `test_td7_caseiii_special_nu_r1.py` passes 17/17 under both.
Charged run 0.07 s; all nine observed lines of the packet (69 states, 295
edges, max numerator 3, max `M` 25, `max_k` 2, `max_lex` 0, derived-lex max
27, monotone flag, table hash) reproduce exactly.

Legacy comparison (audit 4): `book_offaxis.close_p(Fraction(3,2),2,5)` on the
current working tree returns **69** states, `capped=False`, max numerator 3,
max `M` 25, and its `{(w,M): λ_min}` map equals the packet's map exactly (no
extra state, no missing state, no cost mismatch).  So P5's prose "70 states"
is stale against its own current engine, as the packet claims.  (The working
tree shows `book_offaxis.py` modified; without git access I cannot date the
69/70 divergence — the claim as worded, "stale relative to its own current
engine," is verified.)

Third, independent implementation: I wrote a from-scratch closure
(`/tmp/fable5_indep_closure.py`,
`813e6b2f708b942fbf53b87a127542f9865d7519a4f3c39fca5a4e6210b981f0`) directly
from the printed P0 laws, with a **different dirty enumeration** (direct
ν-scan testing κ̄∈ℤ at each ν, instead of the divisors-of-`l·a·T` route),
my own partition minimizer, and a pure-ε family computed by a windowed
direct-`N` scan rather than the packet's residue algebra.  It reproduces the
exact `state_table_sha256` `c2835aaf…f1ad`, 69 states, same maxima.  An
overshoot scan (ν pushed until `E > 3·l·a·T + 50`) found **no** legal `E`
beyond `l·a·T` anywhere in the closure.

## 2. Audit 1 — finite reduced closure: PROVED (conditional on P0 as printed)

I re-derived the whole argument.  The load-bearing steps, several of which
the packet uses without writing out, all check:

**Four-family partition is complete and disjoint.**  With `C = l(k+lex)−Sm`
and `Sm ≤ k(l−1)` one gets `C ≥ k ≥ 0` always, and `C = 0 ⟺ k = lex = Sm = 0`
(if `k ≥ 1` then `l·lex ≤ −k < 0`, impossible).  So every P0 step is exactly
one of: neutral (`C=0, ε=0`), pure-ε (`C=0, ε≥1`), clean resonant
(`C≥1, ε=k=0`, i.e. q-extras only), or dirty (`C≥1`, `k≥1` or `ε≥1`).  The
constraint `m_j ≤ l−1` used for the `Sm` range is **derived**, not assumed:
strict NE `m_j·dq < dp` plus own-edge searrow `dp < l·dq` give `m_j < l`.
The dirty ε-range `ε ≤ l−1` is also derived: `T ≥ 1` forces
`ε(1+k) ≤ Sm+l−1 ≤ (k+1)(l−1)`, hence `ε ≤ l−1`.  A mutation extending the
ε-loop to `ε = l` fail-closes on the code's own precondition assert (M5
below), and my independent scan confirms no `ε = l` step can pass `T ≥ 1`.

**Zero-λ menu is exactly {neutral, resonant}.**  The AF2 rule prices every
NE orbit and every ε-root at ≥ 1, so modeled λ = 0 forces `k = ε = 0`.
Because modeled λ is a *lower* bound of true λ, any truly-free step also has
modeled λ = 0, hence lies in the clean family: **no zero-cost family outside
the modeled neutral/resonant moves exists**, conditional on the promoted AF2
rule.  q-extras costing zero opens no hole: q-extras-only steps
(`ε=k=0, lex≥1`) are precisely the resonant family, and I verified the
correspondence exactly — setting `n = lex+1`, `Δ = (n−1)ν+1` one gets
`E = lΔ`, `κ̄ = a·dq/(dΔ)` with `gcd(Δ,dq) = gcd(Δ,ν) = 1`, from which
`Δ | a` and `d | dq` are **necessary** (not just sufficient) for κ̄∈ℤ, using
`gcd(a,d)=1`.  So the coded resonant menu is the complete `ε=k=0, lex≥1`
family.

**Resonance strictly decreases the reduced numerator.**  `w′ = w·n/Δ` with
`n < Δ` (since `Δ = (n−1)ν+1 ≥ 2n−1 > n`), and moreover `gcd(n,d) = 1`
(because `d | dq = nν+1` and `gcd(n, nν+1) = 1`), so the reduced numerator
is exactly `(a/Δ)·n < a`.  The packet's claim holds even without the gcd
refinement, since further cancellation only shrinks it.  Neutral steps send
`M` to `gcd(l, ν+1) | l | M` and fix `w`; every divisor of `M` is realized
(`l = M₂`, `ν+1 ≡ 0 (mod lcm(M₂,d))`, the `d`-factor coming from the neutral
step's own κ̄ = `w(ν+1)` ∈ ℤ).  Hence the zero-cost graph is nonincreasing
in `(num(w), M)` and well-founded; combined with λ ≥ 1 off the clean family
and finite one-step menus, the budget induction in the packet's item 5 is
sound.  Finiteness of the *modeled* superset transfers to the true reachable
set because modeled λ never overprices.

## 3. Audit 2 — dirty `lex` bounds and divisor enumeration: COMPLETE, with a new identity

Both bounds re-derive exactly as printed.  `ν·T = dp − ε·dq`, so `T ≥ 1` is
the strict ε-NE law and for `ε > 0` gives
`lex ≤ ⌊(Sm+l−ε(1+k)−1)/ε⌋`.  For `ε = 0`, `E = l+νC ≥ l+2C` with
`E ≤ l·a·T`, `T = Sm+l` fixed, gives `C ≤ ⌊(l·a·T−l)/2⌋` and the coded lex
bound.  `k ≤` remaining budget is legitimate because λ ≥ `k + [ε≥1]`; it is
a derived shortcut, not a cap (steps it skips are exactly those the budget
filter would delete).

**New result (closes the one real gap risk).**  The packet enumerates `E`
over divisors of `l·a·T`, citing P0's printed `E | l·num(w)·T`.  That
divisibility does *not* follow from κ̄∈ℤ by naive manipulation (one only
gets `E | l·a·ν·T`, and `gcd(E,ν) = gcd(l−ε,ν)` can exceed 1).  It does
follow exactly, by the resolvent identity I derived and machine-checked on
every legal candidate in the closure:

```text
E · ( l·a·(1+k+lex) − κ̄·d·C ) = l·a·T,        w = a/d in lowest terms,
```

valid whenever `dp = ε+ν(l+Sm)`, `dq = (1+k+lex)ν+1`, `E = l·dq−dp`,
`κ̄ = l·w·dq/E`.  Since the parenthesis is an integer exactly when κ̄∈ℤ (`d`,
`C`, `a`, `l` integers), κ̄∈ℤ ⟹ `E | l·a·T`, with the quotient determining
κ̄ and conversely.  So the divisor enumeration is **complete**: no legal
ε/k/lex/E family is omitted, and the degenerate infinite family one might
fear (`C = (l−ε)(1+k+lex)`, which would admit unboundedly many `E`) is
exactly the `T = 0` locus excluded by the root-mult law (R).  The empirical
overshoot scan (§1) corroborates.  No hidden global cap exists in the
source: I read all 412 lines; the only truncations are budget-derived, and
cap-free runs at budgets 6 and 7 complete in 0.12 s / 0.55 s with 162 / 349
states (max `M` 49 / 97), where the legacy engine would return `capped=True`.
A separate charged run from `(w,M) = (2,4)` at budget 4 exercises `lex = 2`,
`k = 4`, and numerator growth 2 → 8, confirming the cap-free machinery on a
state family the td-7 instance never touches.

Remaining conditionality (correctly inside the packet's trust statement, not
defects): ν ≥ 2 at chain vertices and κ̄∈ℤ are premises of P0's printed
transport; `l | M` is St 8.4; R1.0 pattern completeness and the AF2 price
rule are review-confirmed priors.  The theorem is exactly as conditional as
it says it is.

## 4. Audit 3 — pure-ε congruence quotient: CORRECT, and provably map-equivalent to legacy

For pure-ε (`k=lex=Sm=0`): `dq = ν+1 = N`, `E = l−ε`, and κ̄ = `l·a·N/(d·E)`
∈ ℤ ⟺ `P | N` with `P = d·E/gcd(d·E, l·a)` — the code's
`required_multiple`.  `M′ = gcd(E,N)`.  Both the divisibility and `M′`
depend only on `N mod lcm(E,P)` (the code's modulus; the packet's stated
modulus matches), each accepted class is an infinite arithmetic progression
and so contains `N ≥ 3` (ν ≥ 2 exists), the ε-NE law `ε·dq < dp` is
automatic (⟺ `ε < l`), and the price `⌈l·w/ε⌉` is ν-free (it equals the AF2
ε-term because `T = E` here).  `kbar ≥ 1` is automatic from positivity.  The
census can never be empty: residue 0 always qualifies, giving `M′ = E`.
Verified against the suite's brute check and my independent windowed scan.

**Divergence census vs legacy.**  The legacy engine emits *all* divisors of
`E` as pure-ε `M′`; the packet engine emits only the congruence-achievable
ones.  These genuinely differ **in reach** at the charged instance: 41
divergent `(state, l, ε)` menus at 13 of the 69 states, e.g. at
`(2/13, 13)` with `l=13, ε=2` only `M′ = 11` is legal but legacy adds
`M′ = 1`; at `(3/10, 10)`, `l=10, ε=6` legal `M′ = 4` vs legacy `{1,2,4}`.
Hand check of the exemplar `(3/5,5), l=5, ε=1`: κ̄ = `3N/4` ∈ ℤ forces
`4 | N`, so `M′ = 4` only — the packet engine's reading of P0 is the
faithful one; legacy over-emits P0-illegal children.

**Why the reduced maps still agree — an equivalence lemma, not luck.**  The
residue-0 class always makes `M′ = E` achievable at the same price, and any
phantom `g | E` is then a zero-cost neutral drop from `(w′, E)`.  So every
legacy phantom edge is simulated by two legal steps at equal total cost, and
the two engines produce **identical reduced `(w,M)`/min-λ maps for every
input**, even though their edge sets differ.  Mutation M1 (below) confirms:
forcing the packet engine to legacy's all-divisors semantics changes the
edge count (295 → 347) but leaves the state table hash identical.
Consequence for consumers: the congruence classes are invisible at the
reduced-map tier and load-bearing only for transition-level data (which ν
live at a vertex — exactly what the arrival law and merge handshakes
consume).  This simultaneously upgrades the packet's legacy-match from
corroboration to a two-sided structural equivalence *for the map*, and
demotes it to zero evidence *for the congruence data*.

## 5. Audit 4 — mutation battery (private `/tmp` copies; harness `f3412208fc4c12be1b6a0fcf5a78c6c9316b357d302ca5e0ebfe9e0a8eb394af`)

| mutant | effect on charged closure | reading |
|---|---|---|
| M1 pure-ε → all divisors of `E` | 69 states, edges 347, **hash same** | equivalence lemma confirmed; suite's edge pin catches it |
| M2 allow ν = 1 in dirty | 69 states, edges 305, hash same | ν≥2 gate is state-invisible here; caught only by the edge pin |
| M3 drop κ̄∈ℤ | **635 states**, max numerator 27 | κ̄-integrality is the finiteness engine at instance scale |
| M4 tighten k-max by 1 | **52 states**, max `M` 13 | budget-derived k-bound is binding and sharp (k = remaining fires) |
| M5 ε-loop to `ε = l` | fail-closed exception | derived ε ≤ l−1 enforced by precondition assert |
| M6 semantic lex cap at 0 | 69/295, **byte-identical payload** | see blind-spot finding below |
| M7 drop `d | dq` in resonant | 69 states, hash **differs** | illegal resonances perturb min-costs; gate load-bearing |
| M8 neutral self-only | **45 states** | neutral divisor drops load-bearing |
| M9 delete pure-ε family | **48 states** | legal steps disappear; caught |
| M10 price resonance at 1 | 69, edges 292, hash same | no resonant step is min-cost-critical at this instance |

**Blind-spot finding (the main narrowing).**  The full 35-check suite
**passes** under M6: a semantic `lex ≤ 0` cap that binds nowhere in the
charged instance is undetectable by construction (`max_lex_observed = 0`;
no legal `lex ≥ 1` step exists anywhere in this closure, which M6's
identical edge count proves).  Cap-token refusal is a substring firewall
and cannot see it.  Likewise ν=1 admission, the congruence refinement, and
resonant pricing are state-invisible at this instance (M2/M1/M10).  None of
this breaks the theorem — the general-case support is the analytic bounds,
which I verified independently, plus the suite's function-level boundary
checks (`test_derived_lex_bounds`, which are sharpness mini-proofs, though
the report's phrase "bound-stop mutations" oversells them slightly).  But
the packet's sentence "matching a capped legacy engine is corroboration"
should be read narrowly: the charged instance corroborates the κ̄ gate, the
k-bound, neutral drops, pure-ε presence, and `d | dq`; it corroborates
nothing about lex bounds, ν≥2, congruence classes, or resonance pricing.
Legal `lex ≥ 1` dirty steps do exist elsewhere (612 found on a small grid;
first at `(w,M) = (2,4)`: `l=4, ε=0, k=2, Sm=2, lex=1, ν=2`, price 2,
child `(4/3,3)`), so the lex machinery is globally non-vacuous.
**Recommendation for R2:** pin the `(2, 4, budget 4)` run (152 states,
`max_lex 2`, `max_k 4`, max numerator 8, plus its table hash) as a second
charged regression; it makes M2/M6-style mutations hash-visible.

## 6. Audit 5 — case-III special-ν theorem: CONFIRMED (one wording erratum)

Derivation re-done from P0/P2/P3 only.  Chain-1 frozen `(μ,w,M) = (1,2,1)`
gives the **case-II** handshake `X = κ̄−2` (P3 verbatim).  Chain-2 μ₀ = 2
arrivals at the `(3/2,2)` segment: arrival law `μ₀ | M_H = gcd(l, ν_H+1)`,
`l | 2` forces `l = 2` and ν_H odd; ν ≥ 2 makes the ray odd `h ≥ 3`.  Here
the neutral κ̄∈ℤ condition `d | ν_H+1` (`d = 2`) coincides with the μ₀
parity condition, so "odd `h ≥ 3`" is exactly right.  P3 class-C pin:
κ̄ = `(μ₀ν_H w₂ − 2)/(μ₀−1)` = `3h−2`; `X = 3h−4`.  Shape: `dp = μ₀+ν_G =
g+2` (printed); `ν_G | (μ₀+c−1)` ⟺ `dq ≡ 1 (mod g)` (since `dp ≡ μ₀ + g`);
`X < κ̄` forces `dq > dp`, which **excludes** `dq = g+1`, i.e. `l = 0` — so
`dq = (l+1)g+1, l ≥ 1` is the complete parametrization, and `ν_G = 1` is
excluded by P3's printed case-I argument.  Substituting into the ratio
`dq(κ̄−2) = κ̄·dp` gives exactly `g((3h−4)l−2) = 3h`.  The inequality step
(`l ≥ 2 ⟹ D ≥ 6h−10 > 3h/2 ⟹ g < 2`) and the `l = 1` divisibility
(`(h−2) | 2`, odd `h` ⟹ `h = 3, g = 3`) both check.  Independent brute of
**both** formulations (packet equation, and P3's literal
ratio-integrality + mod-`g` law) over `h ≤ 5001`, `l ≤ 500` / `g ≤ 3999`:
unique solution `(3,1,3) → (dp,dq,M_G) = (5,7,1)`, w_tr = 2, MP2-dead
interior.  Even-`h` control: the excluded ray would contain `(h,l,g) =
(4,1,2) → (4,5)`, so the oddness (arrival law) is load-bearing, not
decorative.  Every odd `h ≥ 5` is case-III-ZCH empty for this partner and
shape.  Scope firewalls in the JSON (other partners, other shapes, entry and
landing-cell special vertices, full book, landing, JC2) are accurate.

**Erratum (wording only):** the packet body says "The two case-III
handshakes give kbar=3h−2, X=3h−4."  Chain-1's handshake is case II (P3:
"X = κ̄ − 2 from chain-1's case-II handshake"); only chain-2's is case III.
The formulas used are correct.  Fix the sentence in any successor rev.

## 7. Audit 6 — exactly what part of P5/CRITICAL 5 is corrected

**Corrected (conditional on P0 as printed):** CRITICAL 5's sentence "At a
fixed budget, reachable states can have unbounded numerator and `M`," P5's
"post-jump states of unbounded numerator and `M`" at fixed entry/budget, and
REDUCTION §5.2's "state numerator and `M` are unbounded under the current
description" — all three, **at the reduced `(w,M)` chain-state tier only**.
The reduced per-pole closure is finite, cap-free, and effectively computable
at every fixed entry and budget; zero/low-cost escapes cannot grow the
reduced state.  Also corrected: P5's "70 states" prose figure (engine says
69).

**Not corrected, and correctly kept outside any promotion:** last-vertex ν
(the neutral ray is genuinely unbounded; only its congruence shadow is
finite at the chain tier), κ̄ along consumers (e.g. `κ̄ = 3h−2` is unbounded
on the ray), full pattern degree, merge q-extra families, complete
partner-dependent merge legality (the arrival law's "direct" list is a
superset), any full-configuration landing (CRITICAL 4), the §9 grid solve's
completeness (its loop bounds concern cells and merges, not reduced states),
`G2-BD`/ceiling/topological-degree (CRITICAL 7), realizability, Keller
counterexample, JC2.  The packet's own Result and Scope-firewall sections
state exactly this list; no overshoot found.  P5's operational conclusion
"0 DEAD / 0 ALIVE / 2691 OPEN" is *not* invalidated: budget-priced kills
still need per-route covers; what changes is that the per-pole state layer
is no longer the obstruction.

## 8. Exact statement safe to promote

> **Theorem (finite reduced P0 chain closure; conditional).**  Assume the P0
> chain grammar of BOOK-OFFAXIS §10 exactly as printed: the R1.0 pattern; `l
> | M` (St 8.4); transport `κ̄ = l·w·dq/E ∈ ℤ` with `ν ≥ 2`, `E = l·dq−dp ≥
> 1`, `w′ = l·w(dq−1)/(νE)`, `M′ = gcd(dp,dq)`; strict NE laws `ε·dq < dp`,
> `m_j·dq < dp`; and the AF2 price lower bound.  Then for every initial
> reduced state `(w₀,M₀)` and every λ-budget `B`, the set of reachable
> reduced chain states `(w,M)`, with minimal modeled λ, is finite and
> effectively computable with no cap on `k`, `lex`, `num(w)`, `M`, or `ν`:
> the modeled-zero-cost menu is exactly neutral (`w` fixed, `M′ | M`) plus
> resonant (`Δ | num(w)`, `d | dq`, reduced numerator strictly decreases);
> every other step costs ≥ 1; and per state the one-step menu is finite via
> `ε ≤ l−1` (from `T ≥ 1`), `Sm ≤ k(l−1)` (from NE + `E > 0`), `k ≤`
> remaining budget, the two printed lex bounds, and `E | l·num(w)·T` — the
> last being equivalent to κ̄∈ℤ through
> `E·(l·num(w)(1+k+lex) − κ̄·den(w)·C) = l·num(w)·T`.  Pure-ε steps realize
> exactly the `M′ = gcd(l−ε, ν+1)` with `ν+1 ≡ 0 (mod d(l−ε)/gcd(d(l−ε),
> l·num(w)))`, classified by `ν+1` modulo `lcm(l−ε, ·)`, and always include
> `M′ = l−ε`.  Charged instance `(3/2, 2, B=5)`: 69 states, max numerator 3,
> max `M` 25, state-table SHA-256 `c2835aaf…f1ad`, equal (provably, via the
> phantom-absorption lemma of §4 above, not only empirically) to the legacy
> reduced map.

> **Theorem (td=7 μ₀=2 odd-ray case-III quotient; conditional on P0/P2/P3).**
> Against chain-1 frozen at `(μ,w,M) = (1,2,1)` (case-II handshake `X =
> κ̄−2`), the μ₀ = 2 arrivals at the 0-direction from neutral vertices of the
> `(w,M) = (3/2,2)` segment form the ray `ν_H = h` odd, `h ≥ 3`, and carry
> `κ̄ = 3h−2`.  The class-C (case III, `ν_G ≥ 2`) cell laws `dp = 2+ν_G`,
> `dq ≡ 1 (mod ν_G)`, `dq > dp`, `dq(κ̄−2) = κ̄·dp` reduce to
> `ν_G((3h−4)l−2) = 3h` and have the unique solution `(h,l,ν_G) = (3,1,3)`,
> giving `(dp,dq,M_G) = (5,7,1)`, an MP2-dead interior cell; for every odd
> `h ≥ 5` the cell set is empty.  Entry-vertex and landing-cell arrivals and
> all other partners/shapes are outside this statement.

Neither statement asserts merge completeness, landing, realizability, degree
bounds, or JC2.

## 9. Repairs / errata (none blocking)

1. **Wording:** "two case-III handshakes" → chain-1's is case II (§6).
2. **Corroboration scope:** state explicitly in a successor rev that the
   charged 69-map is blind to lex bounds, ν≥2, congruence classes, and
   resonance pricing (M1/M2/M6/M10), and that the 35-check suite passes
   under a semantic `lex ≤ 0` cap.  Add the `(2,4,B=4)` pinned regression
   (§5) to close M2/M6 visibility.
3. **Precision available for free:** the report can cite the resolvent
   identity (§3) to upgrade "P0 gives `E | l·a·T`" to "κ̄∈ℤ forces
   `E | l·a·T`," removing any doubt about the enumeration's completeness,
   and the phantom-absorption lemma (§4) to upgrade the legacy match from
   empirical to structural.
4. **Successor-proofing note:** the neutral-ray modulus for a μ₀ consumer is
   `lcm(μ₀-condition, den(w))` because the neutral vertex's own κ̄ =
   `w(ν+1)` ∈ ℤ imposes `den(w) | ν+1`.  At both charged rays (`d = μ₀ = 2`
   and `d = μ₀ = 3`) the two conditions coincide, so nothing is wrong in
   the packet, but a partner with `d ≠ μ₀` needs the lcm.

## 10. Cheapest next generic-AP discriminator (worked far enough to certify cheapness)

Do the same solve for the **μ₀ = 3 ray on the `(2/3,3)` segment** (the
feeder of P4's post-jump class-C book).  I executed it during this review:
κ̄ = `(3·h·(2/3)−2)/2 = h−1`, `X = h−3`, `dp = 3+ν_G`, `dq = (l+1)ν_G+1`,
ratio ⟹ `ν_G((h−3)l−2) = 2h`, ray `h ≡ 2 (mod 3)`, `h ≥ 5` (here again
`d = 3` makes the κ̄ and μ₀ conditions coincide).  Solution table
(brute-confirmed to `h ≤ 3001`, `l ≤ 399`): specials
`h=5 → (8,16), M_G=8` (P4's surviving `(8,16)` cell) and
`h=8 → (5,7), M_G=1` (MP2-dead); every other ray value empty; the
landing-cell special vertex `ν_H = 7` off the ray gives exactly `(10,15),
M_G=5` — P4's exact-fit route.  So one page of hand algebra plus a 30-line
script reproduces and *quotients* the two sharpest P4 cells: this is the
discriminator pattern to run for every `(partner, state, μ₀)` in the finite
charged skeleton, with landing-cell vertices as explicit finite side tables.
Failure mode to watch: a consumer whose special table is not finite —
that would falsify the packet's generic-AP program.

## 11. Artifacts

- `/tmp/m2-skeleton-r1-replay.json` (`74f82b75…`), `/tmp/skel-b6.json`,
  `/tmp/skel-b7.json`, `/tmp/skel-w2m4.json`, `/tmp/td7-caseiii-replay.json`
  (`1e70f2e3…`);
- `/tmp/fable5_indep_closure.py` (`813e6b2f…`), independent third
  implementation, reproduces `c2835aaf…`;
- `/tmp/mutate_harness.py` (`f3412208…`), ten mutants M1–M10 with results as
  tabled in §5.

No canonical file was modified; nothing was committed; `jc2-lean` was not
touched.

---
Report-body SHA-256 (bytes before the separator line above): `28fc400c6879a288f3f09a85668d3cd8e56ea88e518dfcdaaa41f26692651320`
