# Fable 5 hostile review — Opus td=8 exact separation law and jet freedom

Lane: Fable 5, hostile review. Date: 2026-08-29. Target:
`xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md`
(Opus 5 primary). Prompt:
`xmodel/m2-td8-first-extra-jet-exact-lambda-hostile-review-fable5-prompt-20260829.md`.

Executed from `/Users/dc/code/math/jc2`. No web, no AWS, no commit/push, no
canonical edit, no heavy CAS, no `jc2-lean` access of any kind, no global
`git status`, no workspace-wide search. Scratch in `/tmp` only. The active
Fable coefficient-transport output and all later model output were not read.
Every claimed theorem and every reading of Sigray was treated as an
allegation and re-derived or re-read on-page.

---

## 0. Verdict

**`PASS_WITH_REPAIR`.**

All five headline layers — the exact descent law (Theorem A), the finite
A-step menu (Theorem B), the trunk criterion (Theorem C), the derived
subtop laws (V)/(W) (Theorem D), the jet underdetermination (Theorem E),
and the budget knife-edge (Theorem F) — are **confirmed in substance**, at
the target's own recorded formal scope. The lead verdict
`NOT_DETERMINED_FROM_PRINTED_DATA_WITH_EXACT_SEPARATION_LAW` stands. The
integrality upgrade (INT) is **proved at printed-proof scope** (§2.1
below), and it is accurately described as an upgrade of a pre-existing AF2
perimeter item.

One genuine repair is required (R1, §2.5): the report's §2b derives the
vanishing ladder (V) and child-pattern formula (C) at the ambient
*suitable* `κ`, and then §8 silently reuses the layer indices `p_{n-1},
p_{n-2}` at `κ_F`-spacing. These are different objects whenever
`Q := κ/κ_F ≥ 2` (which is the generic situation — `κ = κ_F` is not
suitable). At suitable `κ` with `Q ≥ 3`, the target's own Theorem D(i)
forces the literal layers `p_{n-1} ≡ p_{n-2} ≡ 0`, so the literal
statement of Theorem E ("`p_{F*c*} = c_0η² + c_1η + c_2` with the
discriminant a non-constant affine function of `c_2`") is **false as
printed**: the `κ`-microstep child pattern is exactly `c_0η²`. The
repaired statement replaces `p_{n-k}` by the `κ_F`-graded pieces
`P_{k'} := p_{n-(κ/κ_F)k'}` and the vertex `F*c*` by the `κ_F`-level
truncation `I_{P*}(π(F)+1/κ_F)`; the repair is fully available from the
target's own Theorem D(i) plus `Q`-fold iteration of printed St 3.9, I
verified it on an explicit worked example (§2.5), and the packet's actual
computations (weights `e_1, e_2`, the two jets, `s = 3/8`, the
on/off-weight scan) are computations of the **repaired** objects. No
number in the packet is wrong; no verdict-level claim flips.

Also recorded (no repair needed): the `(0,y)` vertex is in `T_a^↗`
(Theorem 6.1: `l_f < k_f`), so it is not a summand of (25); the target's
`λ_{(0,y)} = 0` forcing is correctly obtained through the Prop 7.5
exhaustion, and calling `(0,y)` a "priced vertex" is loose but harmless
(§2.6). The bold "`t`-uniform kill" label is legitimate only in the
reading "any theorem forcing `Δ_A ≥ 3` from the t-free A-data kills all
`t`"; the target itself records `θ`'s t-freeness as open in the same
bullet (§2.6).

Not established by this pass (unchanged): exact `λ`, transport/gluing,
source landing, Keller realization, any panel exclusion, any degree
bound, or JC2. No AWS was or is authorized.

---

## 1. Custody, seals, and replay

Target hashes, recomputed:

```text
full  991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  (matches prompt)
body  f1ae6c2b1dd94ab2dcf26dfb16e149067eab0617b549817d5620c728d6936d11  (bytes through the
      "*Report body ends...*" line inclusive; matches prompt and self-hash)
```

All six custody files of the target's §1 table: full SHA-256 **and** byte
counts reproduced exactly (prompt 2511 B, Grok exact-lambda 21095 B, Sol
D2 5623 B, Grok D2 review 20866 B, Grok Prop 8.1(iv) 18335 B, Fable
Prop 8.1(iv) review 25642 B). The five prior body hashes also reproduce,
including the three prefix-byte conventions (`a53a78db…` at 20342 B,
`cc7035de…` at 17822 B, `9e594a23…` at 25122 B).

Packet `cases/m2_td8_first_extra_jet_exact_lambda_opus5_20260829/`:

```text
e2a4dcbb83ed53c9fd333339a436ee447aeccaf6a2dde7ad6f7b8483b1261cd5  first_extra_jet_td8.py   (615 lines)
c5330c19e7529be8f7cefa21abf8754709d576674e2b0c4a12e4a2dfa35d5d4d  test_first_extra_jet_td8.py (347 lines)
3066d1c25dec8b732e65c7a145b9c0e3b8b281d807de420ccdf5719554b51bc8  README.md
```

Replay (this review):

```sh
python3 test_first_extra_jet_td8.py      # TD8_FIRST_EXTRA_JET_OPUS5_TEST_PASS checks=411
python3 -O test_first_extra_jet_td8.py   # TD8_FIRST_EXTRA_JET_OPUS5_TEST_PASS checks=411
python3 first_extra_jet_td8.py --json | shasum -a 256
#   2c80cf51187822ef16221d44385bfa8e3efad214a55c24999c4f53ffa3754100  (matches seal)
```

The in-stdout certificate `4b20f925a2c5c5344a88a3714f1c5106b1a7f2dda934c3
74cd66cf7fb9c42879` was independently recomputed from the payload (sorted
compact JSON, hash key removed) and matches. The "no `assert` statement"
claim is accurate (the single grep hit is the test docstring); the `-O`
identity was verified by execution, not trusted.

Sigray ground truth re-read on-page this review (fresh pdftotext
extractions to `/tmp`, display-line formulas cross-checked, stacked
fraction hazard respected): pp. 10–13 (Defs 3.1–3.4, Not 3.1–3.11,
St 3.1–3.7), 14–16 (Prop 3.1, St 3.8–3.14), 17–18 (St 3.15–3.18,
Prop 3.2, Prop 4.1), 26–27 ((18), Props 5.5–5.7), 28–33 (Not 6.1,
St 6.1/6.2, Props 6.1–6.7, Cor 6.1, Thm 6.1), 34–39 (Lemma 6.1, Prop 6.8,
Not 7.1, St 7.1–7.3, Props 7.1–7.5, Cor 7.1, Not 8.1, St 8.1), 39–42
(Prop 8.1(i)–(v) with proof, St 8.2–8.5), 48–55 (Not 9.1, St 9.1–9.4,
Props 9.2/9.3, St 9.6–9.8 with proofs). Ladder: SHEET6-AF2 in full;
SHEET6-H3 §§3–4a (H3-psi theorem, exit-set repair); SHEET6-L1 family C;
SHEET6-DEPTH i-normalization; SHEET6-MULTIPOLE MP1/MP2. Charged reports:
Grok exact-lambda and Sol56 D2 in full; the Prop 8.1(iv) pair as
established review context.

---

## 2. Task-by-task audit

### 2.1 Task 1 — printed hypotheses and the integrality decision

Re-read verbatim: St 3.9 (p. 15) — the target's §2a quote is faithful,
including the proof's expansion `η_G = x^{1/κ}(η_F − c)`, so
`f^{F*c} = Σ_j x^{j/κ} p_j(x^{−1/κ}η + c)` is the printed proof's own
line. St 3.10 (p. 16): `ω, ω*` monotone decreasing, `ω` continuous,
locally linear of slope `−ω*` off finitely many rationals — exactly the
convexity package Theorem A(2) needs. St 3.13: unique `u` with
`d_{I(u)} = 0`. St 3.14's proof shows `M_{a,b}` preserves `η_F` itself
(not just `π` and `f⁺`), hence `κ_G = κ_F` — the transport the (INT)
argument needs. Not 7.1: `T_{a,cv} ⊂ T_a^0`, so any cv vertex of the
branch sits at `d = 0`, and by St 3.13 **the cv vertex is the same
`u_0`**; existence from St 7.3 (hypothesis met: `F*c* ∈ T_a^↗`, checked
below); `π(H) > 1` from St 7.1. The `d_f ≥ 0` step: `ω` decreasing with
`ω(u_0) = 0` gives `ω ≥ 0` on `[π(F), u_0]`, so `f − a` and `f` share
patterns there. Direction hypotheses: the northeast test (St 6.2 /
St 8.2) gives `F*c* ∈ T_a^↗ ⟺ D_F/mult > κ̄_F`: `14/2 = 7 > 5` (A),
`17/2 > 7` (trunk) — both hold, and `d` stays positive at the first
microstep (`12 > 0`, resp. `15i_F > 0`).

**(INT) decision: PROVED at printed-proof scope.** Prop 7.3 (pp. 36–38)
contains, inside its geometric proof of the inequality
`Σ_{P∈R_a^*} Λ(P) ≥ κ_F π(F) − κ_F`, the exact equality
`Λ(Q) = κ_G π(G) − κ_G` at the generic-perturbed point `Q`, where
`G = M_{a,a*}(F)` has `π(G) = π(F)`, `κ_G = κ_F` (St 3.14 preserves
`η_F`), `p_G = p_F`, `p_{g,G} = p_{g,F}` (printed lines), and generic
`a*` makes `p_G − a*` simple-rooted so the mult-1 special case applies.
`Λ(Q)` is the local multiplicity of `g − b*` at an actual place — a
positive integer. Hence `κ_H(π(H)−1) = Λ(Q) ∈ N*` for **every**
`H ∈ T_{a,cv}`, strictly positive by St 7.1. Caveats, disclosed: the
proof's "p_G is squarefree" must be read "`p_G − a*` squarefree" (forced
by context — `p_G = p_F` is carried unchanged), and (INT) inherits the
rigor tier of that printed geometric proof (a
degree/continuity argument), the same tier as the thesis's other §7
proofs. The claim that this upgrades "a proof line of St 9.4" is
accurate: SHEET6-AF2 §2/§6 had booked `κ_G(π(G)−1) ∈ N` as a perimeter
item riding the bare St 9.4-proof line; Prop 7.3's proof supplies it.

### 2.2 Task 2 — Theorem A re-derived

All five clauses re-derived independently; **confirmed**.

1. `N(0⁺) = m` is St 3.9(i) at every suitable refinement plus `ω*`
   monotone; `N ≥ 1` since the branch counts itself; step function from
   St 3.10(i)/(iii).
2. `D_F = ∫_0^{τ_0} N dτ` is St 3.10(ii)+(iii) integrated from
   `ω(π(F)) = d_F` to `ω(u_0) = 0`, rescaled by `κ_F`. Note `N` counts
   with multiplicity if `f − a` is non-reduced; every inequality used
   holds a fortiori in that degenerate case.
3. Pure algebra given `π(H) = u_0` (§2.1).
4. Re-derived from Not 3.4/3.5 plus standard Puiseux conjugacy. The
   load-bearing convention check: Not 3.5 sets `κ_F = κ_P/e_j` with
   `α_j ≤ u` — the **post-jump** convention — so at a `V_{1,a}` vertex
   `κ_F` already includes `π(F)`'s denominator, and
   `κ_{I(u)} = κ_{P*}/E(u)` with `E(u) = e_j(P*)` the number of
   conjugates agreeing through `u` (contacts between conjugates sit
   exactly at characteristic exponents; `gcd`-chain `e_j` standard).
   Hence `κ_H/κ_F = E_+/E_0 ∈ N*`, dividing `E_+`. `E_+ ≤ m`: the `E_+`
   conjugates agree through `π(F)`, so each carries the coefficient `c*`
   there and is counted by `deg(p_{F*c*}) = m` (Prop 3.1(∗)/(∗∗));
   distinct conjugates are distinct series, so the bound survives even
   non-squarefree fibers. Also verified: `ν_F | κ_F`
   (`κ_F = (κ_P/e_{j−1})·ν_F`), used once in §8b.
5. Follows from 2–4 plus (INT); equality case `N ≡ m` exact.

The "where the two printed inequalities lose" decomposition (ratio
`E_+/E_0` vs area `∫(m−N)`) is exact, and the corrected St 9.3(24) — E6
sign repair re-verified against the proof's own chain
(`κ_F(w−1) = κ_F(w−u) − κ_F(1−u)`) and all three p. 53 usages
(`7−5 = 2`, `9−6 = 3`, `5−4 = 1`) — is precisely the `N ≡ m`,
`κ_H = κ_F` case.

### 2.3 Task 3 — A-step menu reconstructed from scratch

**Confirmed, including both endpoint subtleties.** Route data reproduced
independently: frame `(21,15,E=9)`, `(κ̄,X,ρ,w,M) = (5,7,1/3,2/3,3)`;
`i_A = 2` from St 3.17(i) (`deg p_pole = 4 = i_A·2`); `m = i_A·1 = 2`
(Prop 8.1(i), extra orbit simple in the reduced pattern);
`D = 14, κ̄ = 5`. The extra-orbit ratio `B = (3/2)A` was **re-derived by
hand from Prop 8.1(iv)** via Cor 6.1 (T²-coefficient
`ρ(1+2ν) = 3ν ⟹ ρ = 21/15`; T¹-coefficient `−21A + 14B = 0`), and
likewise the trunk's `D = (4/3)C` (T¹-coefficient `−68C + 51D = 0`) —
both match Grok and the packet gauge `BVAL = 3/2`.

With `m = 2`, `N` drops at most once. Two exclusive regimes, keyed to
`E_+ ∈ {1,2}` (exhaustive since `E_+ ≤ m`):

- **Contact** (`E_+ = 1`): then `κ_{I(u)} = κ_{P*} = κ_F` for all
  `u > π(F)` — no jump is even possible — so `Δ = 9 − θ`, and (INT)
  *excludes* non-integral `θ` (a fine-lattice companion contact would
  make `Δ ∉ N`; the kill is integrality, not lattice geometry). Hence
  `θ ∈ {1,…,6}` or `θ ≥ 7`, giving `{8,…,3} ∪ {2}`.
- **Conjugate** (`E_+ = 2`): the companion is `σP*`; conjugates agree at
  every `κ_F`-lattice exponent (the order-2 twist fixes even-numerator
  exponents), so separation sits at a characteristic exponent
  `b/(2κ_F)`, `b` odd, and `κ_F π(F) = β_j/2 ∈ Z` (`e_j = 2 | β_j`),
  giving `θ ∈ 1/2 + N` exactly as claimed; `Δ = 2(9−θ) ∈
  {17,15,…,5}` for `θ < 7`, and for `θ > 7`, `u_0 < O` gives `E_0 = E_+`
  and ratio 1, so `Δ = 2`. `θ = 7` is impossible in this family (parity),
  so the code's ratio-independent collapse at `θ ≥ 7` is justified.

Multiple coincident drops are impossible (`N ≥ 1` and after a
characteristic jump `e = 1` terminates the chain). The equivalence
`Δ_A = 2 ⟺ θ ≥ 7 ⟺ deg(p_H) = 2` holds including the boundary
`θ = 7 = τ_0` (Prop 3.1(∗) counts series agreeing *strictly below*
`u_0`, so both are still counted at the cv vertex). Menu
`{2,…,8} ∪ {5,7,9,11,13,15,17}` **confirmed** as a proved containment.

### 2.4 Task 4 — trunk criterion reconstructed

**Confirmed.** `i_F = 28(4+3t)` re-derived through the St 3.17(i) chain
(`42 = 3i_G ⟹ i_G = 14`; `14·(24+18t) = 3i_T`); `m = 2i_F`,
`D = 17i_F`, gap `17/2 − 7 = 3/2`. From Theorem A:
`Δ = r(τ_0 − 7)`, `r ∈ N*`, `τ_0 ≥ 17/2`. `Δ = 2` forces
`r·(3/2) ≤ 2 ⟹ r = 1 ⟹ τ_0 = 9`; any jump `r ≥ 2` gives `Δ ≥ 3`
(exactly Theorem C). The area identity `∫_0^9 (2i_F − N) = i_F` is
arithmetic from `∫N = 17i_F`. The half-drop-at-`τ=8` profile realizes
`τ_0 = 9` (checked for `t ∈ {0,1,4,33}` in the suite and by hand at
`t=0`); it is correctly presented as a formal `N`-profile, not a
source-realized one. The lower bound `Δ ≥ 2` is (INT) + gap, matching
AF2's `⌈3/2⌉` floor with the strictly-positive-defect refinement.

### 2.5 Task 5 — (V), (W), Theorem E: confirmed content, one repair

**(W)/Theorem D: CONFIRMED, re-derived by hand.** The stabilizer of the
truncation is `μ_{Qν_F}` (`Q := κ/κ_F`), `ω = ζ^{κπ(F)}` restricts to
`ξ^{N_1}` with `N_1 = κ_F π(F) mod ν_F`; `gcd(N_1, ν_F) = 1` is forced
by Def 3.1 (`e_j = gcd(e_{j−1}, β_j)`), so the code's unit guard is the
right check; the kernel has order `Q` and yields (i); the support law
`e ≡ (k' − D_F)N_1^{−1} (mod ν_F)` follows on survivors; `ν_F | κ_F`
gives `N_1 = (−κ̄_F) mod ν_F`. Pinned weights independently recomputed:
A-step `(N_1, e_0, e_1, e_2) = (2, 0, 4, 1)`, trunk `(10, 0, 12, 7)`;
`e_0 = 0 ⟺ ν_F | D_F` reproduces St 3.16's printed `l = 0` at both
vertices; `e_2 = 2e_1 (mod ν)` both times.

**R1 — the required repair (index normalization κ vs κ_F).** §2b's (V)
and (C) are derived at ambient suitable `κ` and are correct there — but
at that spacing, Theorem D(i) itself forces `p_{n−k} ≡ 0 for Q ∤ k`, so
for `Q ≥ 3` the literal `p_{n−1}, p_{n−2}` vanish identically, (V) at
`k = 1` is vacuous, and the `κ`-microstep child pattern is exactly
`c_0η^m`. The literal Theorem E statement is then false (`disc ≡ 0`
constant), and §8's weight assignments (`e_1` to `p_{n−1}`) only make
sense if `n−1` means the first `κ_F`-graded piece. `κ = κ_F` cannot be
assumed: suitability (Not 3.7 / Prop 3.1) must cover every branch of the
fiber, not just those through `F`. **Repair** (available entirely from
the target's own results plus print): (a) Theorem D(i) says `f^F`'s
nonzero layers live on `d_F − (1/κ_F)N`, so
`f^F = Σ_{k'} x^{d_F − k'/κ_F} P_{k'}(η)` with
`P_{k'} := p_{n−Qk'}` is well defined; (b) iterating printed St 3.9
through the `Q` suitable-`κ` microsteps from `π(F)` to `π(F)+1/κ_F`
(all intermediate coefficients forced to 0 because the intermediate
patterns are `c·η^m`) telescopes to the `κ_F`-level child pattern
`Σ_{k=0}^m c_k η^{m−k}` with `c_k = [(η−c*)^{m−k}]P_k`, and to the
ladder `ord_{c*}(P_{k'}) ≥ m − k'`. I verified the mechanism on the
explicit example `f = x(xy²−1)² − y` (branch pair
`y = ±x^{−1/2} ± ½x^{−5/4}`, `ν_F = 2`, `κ_F = 2`, suitable `κ = 4`):
the `κ`-microstep child pattern is the forced square `4η²`, the layers
of `f^F` sit at `k ∈ {0, 6} ⊂ 2N` exactly as D(i) predicts, the
`κ_F`-level pattern reproduces `c_1 = c_2 = 0` correctly, and the pair
separates at the characteristic `5/4`, i.e. `θ = 3/2 ∈ 1/2 + N` — the
conjugate menu's parity in the wild. With R1 applied, everything in §8
reads correctly with `P_1, P_2` in place of `p_{n−1}, p_{n−2}`, and the
packet already computes the repaired objects. The "minimal missing
source datum" clause needs the same relabel (`P_2(c*)`); its intrinsic
form (the contact level `O(P*, P**)`) is unaffected and is the better
statement.

**Theorem E under the repaired reading: CONFIRMED.**
- Both fillings satisfy (V) at both orbits (`ord_{c*} = 1` needs
  `≥ 1`; `ord_{c_A} = 3, 2` need `≥ 3, 2`) and lie exactly on the pinned
  weights; no printed degree/support constraint is violated (subtop
  degrees 32 and 15 ≤ deg_y f; per-orbit (V) is imposed orbit-uniformly,
  which is stronger than St 3.18's one-direction-per-orbit requirement,
  hence admissible). Prop 8.1(i)–(v) constrain only `f_F⁺, h_F⁺`
  (re-read pp. 39–40) — no subtop constraint was missed.
- `c_0 ≠ 0` is St 3.9(ii) (transported unchanged through the `Q`
  microsteps: the `c = 0` steps preserve the leading coefficient);
  `c_1 ≠ 0` from the simple `(η^7−B)` factor.
- **`s = 3/8` recomputed by hand** in `K = Q[η]/(η^7 − 3/2)` (a field —
  `2x^7−3` irreducible): `c_0 = (147/32)c*^5`, `c_1 = (21/16)c*^3`,
  `c_2 = s·c*/4`, and `c_1² = 4c_0c_2 ⟹ s = 3/8`. Exact match.
- The on/off-weight scan's mechanism verified structurally: weight-`e`
  values lie on the line `c*^e·Q ⊂ K`, so `c_1² ∈ c*^{2e_1−2}Q` and
  `4c_0c_2 ∈ c*^{5+e_2}Q` are proportional iff `e_2 ≡ 2e_1 (mod 7)` —
  (W) is load-bearing exactly as claimed, and still insufficient.
- Jet E (`disc ≠ 0`) forces contact-type separation at `θ = 1`
  (conjugates cannot part at a lattice level), hence `Δ = 8`; jet L
  (`disc = 0`) removes the first-level separation and the same freedom
  recurs one `κ_F`-step deeper where Prop 8.1 no longer applies
  (`F*c* ∈ T_a^↗`, and Prop 8.1 is stated on `T_a^↘`) — so `θ ≥ 7`
  stays unrefuted. Correctly, jet L is only claimed *compatible with*
  `Δ = 2` (full charge 2 needs tuning at every deeper level, which the
  target discloses). The freedom proved is at-least-one free scalar;
  the theorem claims no more.
- Scope hygiene §8c (top-pattern identity vs source realizability) is
  clean; neither jet is claimed realized by any `(f,g)`.

### 2.6 Task 6 — Theorem F, exit set and accounting

**Confirmed, two phrasing notes, no repair.** Ceiling: `ψ = 1` is
printed-derivable (`ψ l_f < k_f` at `ψ = 1` is Theorem 6.1; H3-psi's
`ψ = ⌈M/j⌉ − 1 = ⌈5/3⌉ − 1 = 1` with `j = M(1−w) = 3` agrees), so
(25) gives `Σ λ^exit ≤ 8 − 1 − 1 = 6` over the pairwise-distinct
↘-vertices `{A_1, A_2, G, trunk}` under the promoted exit-set repair
(AF2 header + H3 §4a, charged prior). Exit census: each A-copy has
exactly one extra orbit (`B`-orbit; the arrival/continuation is the
`A`-orbit) and no 0-root; the merge pattern `(η^{2ν_G} − a²)^3` has
both orbits chain arrivals and no 0-root, so by St 3.18 there is **no**
`G*c*` exit and `λ_G = 0` is an identity (verified against St 9.6's
grammar and the reviewed Prop 8.1(iv) merge pattern); the trunk has
exactly one extra orbit (`D`-orbit, reduced mult 2). No omitted
vertex or charge: the x-side cv is netted into `ψ`, and the floors are
exact corrected-(24) gaps plus (INT), not confused with charges. Floors
`2+2+0+2 = 6` meet the ceiling, so all three priced charges are exactly
2. The final clause is correctly proved through Prop 7.5's *identity*
(not (25)): `td − 1 = 7 = Σ_{T_{a,cv}} κ(π−1) + Σ_a δ_a ≥ 2+2+2+ψ = 7`
with Prop 7.4's `δ_a ≥ 0`, forcing `δ_a = 0` for all `a`,
`T_{a,cv} = {H_1, H_2, H_tr, H_x}` with weights `2,2,2,1` — this
exhaustion is also what legitimately forces `λ_{(0,y)} = 0`, since
`(0,y) ∈ T_a^↗` (Thm 6.1) and cannot itself sit in (25)'s sum. Notes:
(i) listing `(0,y)` among "priced vertices" is loose — harmless, the
proof routes around it; (ii) the "`t`-uniform kill" consequence is valid
in the reading "a proof of `Δ_A ≥ 3` from the t-free A-step data kills
every `t` at once"; the target itself records openness of `θ`'s
t-freeness in the same bullet, so no overclaim survives into the
firewall table.

### 2.7 Task 7 — replay, independent arithmetic, hostile mutations

Replay: 411/411 ordinary and `-O`, stdout and certificate seals match
(§1). Independent arithmetic re-derived by hand this review (not by
rerunning producer formulas): both frames and the merge frame at `t=0`,
the pole data `(2,4,3,2,5)`/`w_0 = 3/2`, the full i-chain
`(2, 42, 14, 336, 112)`, both gaps, `τ_lin ∈ {7, 17/2}`, the menu
closed forms and collapse, Theorem C's `r = 1` forcing, `ψ = 1`, the
budget sums `6` and `7`, the pinned weight quadruples at both vertices,
the Prop 8.1(iv) `T²`/`T¹` coefficient laws with **both** unique ratios
`B = (3/2)A` and `D = (4/3)C`, and the jet-L scalar `s = 3/8`.

Hostile mutations, producer copy in `/tmp/fable_mut`, packet untouched,
**5/5 rejected**:

| mutation | outcome |
|---|---|
| `N_1 := (+κ̄) mod ν` (producer row replicated) | 3 fails; first: pinned weights `(5,0,3,6) ≠ (2,0,4,1)` |
| late-separation collapse removed (producer row) | 8 fails; first: `θ=7` gives `4 ≠ 2` |
| gap sign flipped to printed (24) (producer row) | 9 fails; first: A gap `12 ≠ 2` |
| **new:** conjugate parity broken (`θ ∈ Z` not `1/2+Z`) | 4 fails; first: "conjugate charges are odd" |
| **new:** `ψ := 0` | 21 fails; first: `ψ = 0 ≠ 1` (budget layer collapses) |

The three replicated rows reproduce the producer table's stated
rejection signatures, so that table is honest as spot-checked. Suite
character, disclosed: the route/menu/budget tests largely restate
producer formulas (the prompt's warning applies); the semantics
validation here is the in-suite independent integrator, the exact
`K`-arithmetic of the jet layer, and this review's hand re-derivations.
Minor packet notes (no repair): `ord_at_A` evaluates in the non-field
ring `Q[η]/(η^7−1)` — sound for these orbit-uniform inputs since ring
vanishing is simultaneous vanishing at all orbit roots; one dead `psi`
line in `route()`.

---

## 3. Clause-level scorecard

| layer | verdict |
|---|---|
| Exact descent law (Thm A, 5 clauses; loss decomposition; corrected (24) as constant-profile case) | **CONFIRMED** |
| (INT) `κ_H(π(H)−1) ∈ N*` via Prop 7.3 geometric proof; upgrade-of-perimeter claim | **CONFIRMED** at printed-proof scope |
| Finite A-menu (Thm B): `{2..8} ∪ {5,7,…,17}`; `Δ_A = 2 ⟺ deg(p_H) = 2`; contact/conjugate dichotomy, parity, endpoints | **CONFIRMED** |
| Trunk criterion (Thm C): `Δ = 2 ⟺ κ_H = κ_F ∧ τ_0 = 9`; one-`i_F`-unit defect; jump fatal | **CONFIRMED** |
| Merge `λ_G = 0` exact (St 3.18 identity) | **CONFIRMED** |
| Subtop laws: (V) ladder and (W)/Thm D pinned weights `(2,0,4,1)`, `(10,0,12,7)`; `e_0 = 0` ↔ St 3.16 | **CONFIRMED** (weights re-derived) |
| Jet underdetermination (Thm E): two admissible fillings, `Δ ∈ {8, 2}`-compatible; (W) load-bearing and insufficient; `s = 3/8` | **CONFIRMED WITH REPAIR R1** — statement/derivation must be re-indexed to the `κ_F`-graded pieces `P_{k'}`; literal `κ`-layer reading is false for `Q ≥ 3`; packet computes the repaired objects; no number wrong |
| Minimal missing datum (`P_2(c*)` / contact level `O(P*,P**)`) | **CONFIRMED** under R1 relabel; intrinsic form untouched |
| Budget knife-edge (Thm F): ceiling 6, floors `2,2,0,2`, all three forced to 2; `δ_a = 0`; four-element `T_{a,cv}` weights `2,2,2,1` | **CONFIRMED** ((0,y) note; kill-uniformity reading note) |
| Firewall table / not-claimed ledger (no route kill, no exact λ, no landing, no realization, no JC2, no AWS) | **ACCURATE** |
| Custody, seals, `-O` identity, mutation table | **VERIFIED** (5/5 review mutations, 3 producer rows replicated) |

Valid narrow residues preserved even where phrasing was loose: the
per-`t` budget arithmetic, the θ-menu containment, the contact-lane
reduction of the gate to one `V_{2,a}` bit per A-copy, and the trunk's
strictly-positive-defect refinement of the AF2 floor all stand
independently of R1.

---

## 4. Maximum safe consequence and next lemma

**Maximum safe consequence.** On the reviewed td=8 equal-join affine
route, the first-separation charge at each priced vertex obeys the exact
law `Δ = (κ_H/κ_F)(τ_0 − κ̄_F)` with `Δ ∈ N*`; the A-copies' charges lie
in `{2,…,8} ∪ {9,11,13,15,17}` with `Δ_A = 2` iff `deg(p_H) = 2`; the
trunk's charge is 2 iff `κ_H = κ_F` and exactly one `i_F` unit of
branch-area is shed; and the route survives the exact-λ gate iff all
three charges equal 2, forcing `δ_a = 0` and the four-element cv set.
The first extra-branch jet is not determined by St 3.9 + the
characteristic jump + the rigid tops + the derived subtop laws: the
`κ_F`-graded second subtop value `P_2(c*)` (equivalently the pair's
contact level) is genuinely free in the printed data. Nothing here
kills or promotes the route, computes exact λ, lands a source, or
bounds `td`.

**Best next lemma** (unchanged from the target, endorsed, with R1
folded in): the Prop 7.1 integrality ladder at a `deg(p_H) = 2` cv
vertex — `deg(r_j) = (l_j/k_j)·2` for `0 ≤ j ≤ m_H − 1` against every
`(K,L,S)` compatible with `td = 8` and `Λ(P) = 2` — since an
unsatisfiable ladder gives `Δ_A ≥ 3` from t-free data and kills the
whole family; secondarily the Prop 7.5 closed-configuration census
(`T_{a,cv}` of weights `2,2,2,1` against (19)/(20) with two `Λ = 4`
poles). Both are desk-scale; neither needs the subtop values; no AWS.

---

## 5. Review reproduction

```sh
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md').read_bytes()).hexdigest())"
cd cases/m2_td8_first_extra_jet_exact_lambda_opus5_20260829
python3 test_first_extra_jet_td8.py && python3 -O test_first_extra_jet_td8.py
python3 first_extra_jet_td8.py --json | shasum -a 256
# mutations: copy the two .py files to /tmp, apply the 5 edits of §2.7, rerun the suite
```

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = 463a8f4860f950445a9ff784b1c1b41729762bbebd530477b2e1b53717d564a7
