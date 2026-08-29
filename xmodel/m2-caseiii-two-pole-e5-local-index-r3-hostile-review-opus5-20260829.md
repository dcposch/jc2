# Hostile review: Q+E5 two-pole case-III, fibre-finiteness and T1 repair (R3)

Reviewer: Opus 5 (different-model hostile review). Date: 2026-08-29 UTC.
Target: `xmodel/m2-caseiii-two-pole-e5-local-index-r3-repair-fable5-20260829.md`
(full SHA-256 `885e5cc2…7092` **verified byte-exact against the prompt**;
body `a902c94e…a0b6`) and packet
`cases/m2_caseiii_two_pole_e5_local_index_r3_20260829/` (all four file
hashes verified; sealed embedded field `a26d992f…b471` verified; both
suites pass with exactly **1,532,749 checks**, 11.4 s each; the
certificate regenerates **byte-identical** to `certificate_r3.json`).

Sources read literally and re-quoted below: `ladder/BOOK-OFFAXIS.md`
§§6–11a (R1.0 `:227-236`, R1.3 `:283-292`, R2.2 `:341-356`, §11 zero-chain
law, §11a 17-cell book/arrivals/N1 kills/family termination),
`ladder/SHEET6-DEPTH.md` §2 (`:112-134`, DS1(c)) and §§5c–5d (`:278-320`),
`ladder/SHEET6-MULTIPOLE.md` MP1 `:82`, MP2/MP3, MP6(d),
`xmodel/sol-h5a.md` (Prop 1/Prop 2, Q-value ⟹ E5) and
`xmodel/grok-h5a-review.md`, `cases/book_offaxis.py`
(`TDMAX:39`, `census:49-54`, `NUCAP:165`, `cell_check:219-265`,
`solve_arr:273-357`, `expand2`, `node_solve`, `cell_verdict:409-430`),
`cases/td7_census_e5.py` (`e5_cells_C:160-185`), the R2 report and the R2
review in full, and the R2 packet (verified byte-untouched against its own
report hashes). Clean-room scripts built and run under `/tmp/opus_r3/`;
nothing in the packet, `xmodel/`, or any canonical file was modified. No
web, no AWS, no CAS, no `jc2-lean` access of any kind, no git write.

## VERDICT: `PASS_WITH_REPAIR`

Every mathematical claim charged by the prompt is **correct**, and every
published number replicates **exactly** under an independent from-spec
re-implementation that shares no code with the packet. The two R2
blockers are properly repaired: §7.4's "infinite fibre" is withdrawn and
replaced by a true, sharp finiteness theorem; the `{3,4}` T1 encoding is
withdrawn and replaced by a correct general law with a total solver.
Theorem F is genuinely upgraded from the review's empirical claim to a
proof, and I verified the two sub-cases the printed proof silently skips
are vacuous.

The single repair is confined to §8's **proposed, not-executed** engine
migration: the structural scope guard cannot exclude a `nu_G = 1`
(case-I) merge, and I exhibit concrete structurally-in-scope rows that the
DIFFICULT-regime integer-`kbar` loop would kill. This is the same *class*
of hole the R2 review caught in §8.3, but it touches no theorem, no
certificate, and no promoted record — hence `PASS_WITH_REPAIR`, not
`REPAIR_REQUIRED`.

---

## C1 — Preserved Q+E5 theorem layer: CONFIRMED (independently, not by
## deference to the R2 review)

**Census laws are literal source quotes, not paraphrase.** BOOK-OFFAXIS
R2.2 `:341-346` prints `p_red = ⊖η^ε·Π_e(η^ν−c_e^ν)^{μ_e}·Π_j(η^ν−d_j^ν)^{m_j}`
with `ε = μ₀` when a 0-chain arrives, and `dq = (r₀ + k + l)ν + 1`. So
`dp = μ₀ + ν(Σμ_e + Sm)` and `dq = 1 + ν(r₀ + k + l_ex)` verbatim; at
`r₀ = 1` these are the packet's H4 exactly, and Theorem E's
`dq = 1 + ν(1+t)`, `t = r₀ − 1 + σ` is the same identity re-indexed
(`1 + t = r₀ + σ`). (S) `μ_e·dq > dp`, strict NE `m_j·dq < dp`, (R)
`dp ≠ μ★·dq`, `M_G = gcd(dp,dq)` are R2.2 `:348-356` verbatim.
Theorem E's step "`m_j ≤ min(μ_i) − 1`" is not an inference at all — R2.2(S)
prints "every arriving μ_e > every non-chain m_j".

**Ambient rings.** The only ring-level inputs are R1.0's q-shape
(`:227-236`: every p-root is a simple q-root, `η ‖ q` when `ν ≥ 2`, hence
`dq ≡ 1 (mod ν)` and `gcd(M_F,ν_F) = 1`) and the R1.3/R2.2 factorisations
in the base `[η]`. Every new statement in R3 (Theorems D/E/F, Lemma T1′)
is pure integer arithmetic on `(dp, dq, ν, μ, μ₀, m_j)`; no step is
ring-sensitive, and the solver's `(dq − 1) % nu_g` gate is exactly R1.0's
`dq ≡ 1 (mod ν)`. Nothing here can be broken by a ring subtlety.

**Lemma A.** `D = μ·dq − dp = ν(μ·s − Sm) − δ = νA − δ` is an exact
identity (recomputed). Bound and equality profile confirmed.

**Theorem B / the 12-of-17.** I reconstructed the §11a book and evaluated
`dq·M = D(2M + 2δ + 1)` on all 17 rows independently: equality holds on
**exactly 12** rows, precisely the `κ̄ = 6` rows, each with the full
profile `D = M`, `ν = δ + M`, `s = 1`, `A = 1`, `M | 2δ+1`; every listed
`M` equals `gcd(dp,dq)`; and the handshake `κ̄ = μ·w·dq/D` at `(μ,w)=(1,2)`
reproduces the book's own `κ̄` on all 17 rows. Lemma A equality holds on
**0** book rows.

**Theorem C.** `μ₀ν_G w_U = δκ̄ + μw` is the correct `(μ,w)`-general form
of the promoted §11a pin (I4) `κ̄ = (μ₀ν_G w_U − 2)/(μ₀ − 1)`: substituting
`μ = 1, w = 2` returns (I4) character-for-character. Its two inputs are
the case-II handshake `κ̄ − X/μ = w` and DEPTH §5c's case-III 0-edge
handshake `κ̄_G − D_G/i = ν_e·w_e` with `ν_e → ν_G` by E5 + the chain-1
freeze — which is what `sol-h5a.md` §2 (Q-value ⟹ E5, eq. (4)) licenses.
Both are engine-literal (`solve_arr:295`, `:307`).

**REVERSE-regime bound is sharper than the engine's and correct.** The
report's `ν_G < w/w_U` (not `μw/(μ₀w_U)`, `book_offaxis.py:328`) follows
because `μ₀ < μ` and `X > 0` give `ν_G w_U = κ̄ − X/μ₀ < κ̄ − X/μ = w`. The
pseudocode's `range(2, ceil(w/w_U) − 1 + 1)` is the correct integer
truncation in both the integral and non-integral case.

**No-incoming-bound proposition.** `ν_U` cancels into `w_U` under E5 and
is free; the "sound replacement" `ν_G ≤ μw(δ(2δ+3)+1)/(μ₀w_U)` follows
from Theorem C plus Lemma A. Opus-clause-4 census: I recomputed
`ν_G ≤ μ₀·num(w_0)` on the book — **16 of 17** rows violate it, the sole
non-violator being `(25,35,17,5)@8` (`μ₀·num(w_U) = 24 ≥ 17`). Matches.

## C2 — Theorem D (finite fixed-pattern fibre): CONFIRMED, proof and
## every census figure

**Proof, recomputed line by line.** `u := μ − 1/r = dp/dq > 0` (the
report's justification via `κ̄ − w = w·dp/D` is valid — that identity does
hold at every `μ`). Strict NE is `m_j < dp/dq = u`, so
`m_j ≤ ceil(u) − 1 =: m_max`; with `k ≤ s`,
`A = μs − Sm ≥ s(μ − m_max)`, and `μ − m_max = (1 + u − ceil(u)) + 1/r`;
inverting `dq = rD = r(νA − δ)` gives `A = s/r + (1+ν)/(rν) + δ/ν`;
subtracting `s/r` yields the display. `1 + u − ceil(u) ∈ (0,1]` strictly,
so `s` is bounded and each member is pinned by its `s`. Part 4: at `μ = 1`
NE forces `m_j < dp/dq < 1`, hence `k = 0`, `Sm = 0`, `A = s`, and
`s ↦ (1+ν+νs)/(νs−δ)` has derivative sign `−ν(δ+1+ν) < 0` — strictly
decreasing, so every `μ = 1` fibre is a singleton. All four parts hold.

**Box census — independent replication, exact.** From-spec enumeration
(box `μ≤7, δ≤8, ν≤30, k≤5, lex≤8`, legality by (S)+(NE)+(R), fibre key
`(μ, μ₀, ν_G, dq/D)`):

    legal cells 93,735 | fibres 92,772 | hist {1:92083, 2:486, 3:136, 4:63, 5:4}
    Theorem-D bound violations 0 | mu=1 fibres 1,815, ALL singletons | mu>=2 keys 90,957

Every published figure reproduces to the digit, including the
`92,772 − 1,815 = 90,957` bookkeeping.

**Cap-free complete census — independent replication, exact.**

    histogram {1:79267,2:5261,3:2462,4:1461,5:950,6:642,7:481,8:251,9:144,10:25,11:8,12:5}
    max fibre 12 at (7,15,2,15/74) | max member s = 1202 at (7,15,13,170/1019)
    keys attaining the bound with EXACT equality: 29,444 of 90,957

I also verified the `s = 1202` witness by hand end to end: `dq = 15640`,
`D = 93748`, `dp = 15732`, `u = 171/170`, `m_max = 1`, `Sm = k = 1202`,
`lex = 0`, and the bound evaluates to `15626/13 = 1202` exactly — (S),
strict (NE) (`15640 < 15732`) and (R) all hold. Theorem D part 3's
sharpness claim is real, not a rounding artefact.

**§7.4 refuted pattern-by-pattern — replicated.** At `(μ,w,μ₀)=(4,1,5)`,
`κ̄=2`, `ν_G=3`: `r = 1/2`, `u = 2`, slack `= 1`, bound `s ≤ 3`, fibre
exactly `{(20,10) [s=2], (26,13) [s=3]}`. Enumerating every candidate
`(k, mults, lex)` with `Σmults = 2s−3`, mults in `[1,3]`, I get candidate
counts **4, 6, 15, 57, 213** for `s = 4, 5, 9, 21, 45` — matching the
report digit for digit — and `legal_patterns = 0` for all five.

**Canonical-engine cross-check — replicated.** Importing
`book_offaxis` read-only, `cell_check(2, 4, [4], 5, gcd(dp,dq))` returns
`True` for `s = 2, 3` and `False` for `s = 4,5,6,7,8,9,21,45`; `NUCAP` is
`500` and `TDMAX` is `14` in the working tree. The cross-check is not
vacuous: `M_G = gcd(dp,dq)` varies with `s`, so each call reconstructs a
different `(dp,dq)`.

**Non-replication of the R2 review's deep search — I confirm the
non-replication, and the R2 review is the defective side.** Under
"keys-from-the-box with `μ ≥ 2, r < 1`" I get exactly **75,808** keys —
the packet's stated figure — with max fibre 12 and members reaching the
`s ≤ 400` cap, not 57,960 / 9 / 27. I probed eight further readings
(no-legality seeding 264,300; `r ≤ 1` 75,892; all `r` 90,957; `μ ≥ 1`
75,808; `ν ≤ 20` 50,417; `lex ≤ 5` 69,295; `μ ≤ 6` 50,590; `δ ≤ 6`
56,503) — **none** yields 57,960. R3's disposition (document, do not
incorporate) is the correct one, and the direction is conservative: the
cap-free census dominates the review's figures on both statistics.

## C3 — Theorems E and F (arity-graded countercells): CONFIRMED, and
## Theorem F's printed proof is complete once two skipped cases are checked

**Theorem E proof, recomputed.** With `mu = max μ_i`,
`A' = μ(1+t) − Σμ_i − Sm`, `D = νA' − δ` is exact;
`A' ≥ μσ − Sm ≥ σ` (using `mu` maximal, `k ≤ σ`, `m_j ≤ μ−1`) and
`A' ≥ 1` from `νA' = D + δ ≥ 2`; hence
`dq = 1 + νr₀ + νσ ≤ 1 + (r₀+1)νA' = 1 + (r₀+1)(D+δ)` and
`dq/D ≤ (r₀+1) + ((r₀+1)δ+1)/M` via `M | D`. Equality forces
`r₀ + σ = (r₀+1)A'`, hence `A' = 1`, `σ = 1`, `ν = δ + M`, `D = M`,
`M | (r₀+1)δ + 1`. At `r₀ = 1` this is Theorem B; at `r₀ = 2, M = 1` it
is `3δ + 4`. Correct as printed.

**The six §7.1 countercells.** Recomputed each from `(μ,δ)`:
`(13,7), (19,10), (20,7), (38,13), (109,22), (195,28)` — all `D = 1`
hence `M = 1` (MP2-dead as interior merges), all break `2δ+3`, and all
attain Theorem E with equality. The disclosure is accurate.

**Theorem F proof.** `r₀ = 2`: a violator needs
`M < (3δ+1)/(2δ) ≤ 2`, so `M = 1`. Correct. `r₀ = 3`: the case analysis
(`D(2δ−1) < 4δ+1`, `D ≥ M ≥ 2`) is correct in every branch I checked —
`δ ≥ 2` forces `D = M = 2`, `ν = δ+2`, `A' = 1`, `t ∈ {2,3}`, both killed
(parity for `t = 3`); `δ = 1` splits `D ∈ {2,3,4}` and each dies on
integrality/parity/divisibility. **The printed proof silently drops the
`ν = 1` factorisations** `(ν,A') = (1,3), (1,4), (1,5)` of `y`. I checked
all three: they give `dq ≤ 7, 8, 9` against violation thresholds
`10, 16, 21` respectively, so they are vacuous. The proof is therefore
complete; the omission costs nothing but should be one line.

**Census confirmation — independent replication, exact.**

    r0=2  cells 357,260  ThmE violations 0  equality hits 312  violators 96, all M=1
    r0=3  cells 439,730  ThmE violations 0  equality hits 272  violators 248, all M=1
    unequal-mult spot box  cells 75,713  violations 0  violator M-values {1}

The full equality profile (`A'=1, σ=1, D=M, ν=δ+M, M | (r₀+1)δ+1`) holds
on every one of the 584 equality hits.

**The `(44,46)` `r₀ = 4` witness.** Verified legal and extremal:
four `μ=1` arrivals, `μ₀=8`, `δ=7`, `ν=9`, `σ=1`, `t=4` give `dq=46`,
`dp=44`, `D=M=2`, `dq/D = 23 > 17 = 2δ+3`, and `5 + 36/2 = 23` is graded
equality. Theorem F is genuinely false at `r₀ = 4`.

**Campaign-scope argument.** MP1 (`SHEET6-MULTIPOLE.md:82`) prints
"each with `r(G) ≤ m`"; `book_offaxis.py:39` is `TDMAX = 14` and
`:53-54` loops `for m in range(2, td // 3 + 1)`, so `m ≤ 4` and
`r₀ = r(G) − 1 ≤ 3`. Both citations are exact and the inference is sound
(`r(G)` counts the 0-arrival, which is a pole-chain edge in `Va ∩ Ta&`).

**Scope precision the report should carry (not an error).** The `r₀ = 4`
failure is *generic*, not a single knife-edge accident. In a modest box
(`μ≤6, δ≤10, ν≤40, k≤2, lex≤5`) I find **186** MP2-alive two-pole-constant
violators at `r₀ = 4` with `M ∈ {2,3,6}`, and much smaller witnesses than
`(44,46)` — e.g. `(14,16)`: four `μ=1` arrivals, `μ₀=2`, `ν=3`, `σ=1`,
`D = M = 2`, `dq/D = 8 > 5`, also at graded equality. The firewall clause
("`r₀ = 4` MP2 behaviour beyond the single sealed witness") is correctly
worded, but a downstream `TDMAX ≥ 15` reader could mis-read §4's framing
as "one extremal cell". State that the witness is illustrative, not
minimal or isolated.

**Definitional note.** Theorem E's `D := max_i(μ_i)·dq − dp`. For
`r₀ ≥ 2` this is a choice (a different edge gives a different ratio); it
is the choice that makes `r₀ = 1` reduce to Theorem B, and it is what the
countercells and G-e′ fixtures use. Consistent throughout — worth one
explicit sentence.

## C4 — Lemma T1′ (general zero-chain identification): CONFIRMED, and the
## `μ = 1` restriction is *necessary*, not merely cautious

**The identity holds at every `μ`.** `κ̄ = μw·dq/D` and `dp = μ·dq − D`
give `κ̄ − w = w(μ·dq − D)/D = w·dp/D`, hence `w/(κ̄ − w) = D/dp`
universally. At `μ = 1`, `dq = dp + D`, so
`dp | dq ⟺ dp | D ⟺ D/dp ∈ Z≥1`. `M = dp ⟺ dp | dq` is a gcd tautology.

**Integer normalisation.** With `n = D/dp`, `κ̄ = w + w/n`; for `w, κ̄ ∈ Z`
(DS1(c)) this needs `n | w`, giving `κ̄ ∈ {w + d : d | w}`. Menus verified:
`w=1→{2}`, `w=2→{3,4}`, `w=3→{4,6}`, `w=4→{5,6,8}`, `w=6→{7,8,9,12}`.

**The `{3,4}` encoding really is the `w = 2` specialisation.**
BOOK-OFFAXIS §11 prints `κ̄ = 2d_q/(d_q − d_p)`, i.e. `μ=1, w=2`; and I
confirmed by handshake that **all 17** §11a book cells sit at
`(μ,w) = (1,2)`. §11's middle leg is also an identity: with
`T = (d_q−1)/ν`, `(d_p−ν)T − 1 = d_p T − d_q`, so
`d_p | (μ(l+1)−1) ⟺ d_p | d_q`.

**The `μ ≥ 2` restriction is necessary.** Over 25,284 legal `μ ∈ {2,3,4}`
samples at four `w` values I find **260** cells where `w/(κ̄−w) ∈ Z≥1` but
`dp ∤ dq` — e.g. `μ=2, μ₀=4, ν=3, (dp,dq) = (10,25), w=1, κ̄=5/4`. (The
other direction, `dp|dq ⟹ D/dp ∈ Z≥1`, does survive at every `μ`, since
`dp|dq ⟹ dp | μ·dq − dp`; the report could claim that half generally.)

**Solver totality and the sealed menus.** I re-derived all six sealed
rows by hand from `κ̄ = w·dq/D` and `dq % dp`:

    (8,16,5,8)  D=8  kbar=2w  -> 2 / 4 / 6 at w = 1 / 2 / 3, T1-DEAD (M=dp=8)
    (10,15,7,5) D=5  kbar=3w  -> 3 / 6 / 9,                    alive (M=5)
    (7,21,4,7)  D=14 kbar=3w/2 -> 3 at w=2, DEAD (M=dp=7)
    (29,145,24,29) D=116 kbar=5w/4 -> 5 at w=4, DEAD (M=dp=29)
    (45,81,40,9)   D=36  kbar=9w/4 -> 9 at w=4, alive (M=9)
    (15,105,13,15) D=90  kbar=7w/6 -> 7 at w=6, DEAD (M=dp=15)
    (21,39,19,3)   D=18  kbar=13w/6 -> 13 at w=6, alive (M=3)

All agree with the divisor menus. The "slice-stable dead cell, unstable
`κ̄` menu" observation is right and is exactly why `{3,4}` is unsafe.

**The R2 crash and the `e5_cells_C` withdrawal both check out.** Running
R2's module: `e5_solve_mu1` raises
`ValueError: T1 encodings dp|dq and kbar in {3,4} disagree` at `w = 1` and
`w = 3`, and returns `[(7,21,κ̄3,dead),(8,16,κ̄4,dead),(10,15,κ̄6,alive)]` at
`w = 2` — R3's `w=2` row is a byte-match as claimed.
`td7_census_e5.e5_cells_C:167-185` hard-codes the constant 2 in `g*r > 2`,
`den = c*m*r − 2(m−1)` and `kb = Fr(2*dq, c)`: that is `μw = 2`, a td-7
instrument. Withdrawing it as "the general model" is correct.

## C5 — Source migrations: every line reference verified exact

| Claim | Verified |
|---|---|
| `cell_check:219-265` | `def` at 219, `return False` at 265 ✔ |
| `solve_arr:273-357` | `def` at 273, final `return` at 357 ✔ |
| pinned-branch incoming check `:305-309` | `if zero is not None:` … `return 'DEAD'` ✔ |
| `mu0 == mu` branch `:320-323` | ✔ (no `cell_check` on that branch — confirmed) |
| `mu0 < mu` cap `:325-328` | ✔ |
| `mu == 1` doc-9 cap `:329-336` | ✔ (includes the 2-line `ncap` expression) |
| NUCAP loop `:337-357`, `NUCAP:165`, loop pin `:343` | ✔ |
| `TDMAX:39`, census `m <= td//3` at `:49-54` | ✔ |
| MP1 `r(G) ≤ m` at `SHEET6-MULTIPOLE.md:82` | ✔ verbatim |
| DS1(c) `κ̄ ∈ ℤ` at `SHEET6-DEPTH.md:116` | ✔ (proof at `:133-134` uses only `F ∈ V_{1,a}`, i.e. `ν ≥ 2` — the extrapolation from "segment vertex" to "any `ν_G ≥ 2` vertex" is licensed by the proof, not just the statement) |
| `ν_G = 1` merges are case I, DEPTH §5c | ✔ `:301` verbatim |
| `:305-309` unreachable under the guard | ✔ `len(non0)==1` leaves `pin = None` |
| `expand2` emits every divisor as `M_G` | ✔ `for MG in divisors(sum(mus))`, so `M_G = 1` rows reach `solve_arr`; MP3 exempts strict ancestors of `G*` ✔ |
| `cell_check` builds `dp = M_G d0, dq = M_G q0`, `gcd(d0,q0)=1` ⟹ `gcd(dp,dq) = M_G` | ✔ — licenses the `M_G`-graded menu in the pseudocode |
| R2 review's F4 figures (2,158,158 cells; 29,518,848 handshake samples) | ✔ present in the R2 review at `:27`, `:219`, `:274` |
| "R1 and R2 byte-untouched" | ✔ R2's four packet hashes still match its own report |

## C6 — Packet integrity and adversarial controls: CONFIRMED

* Four file hashes match §9 exactly; sealed embedded field `a26d992f…b471`
  matches; the certificate regenerates byte-identical.
* Both suites: **1,532,749 checks**, 11.36 s and 11.36 s.
* Field `pattern_fibre_infinite_at_fixed_kbar_nu_G` is **absent**;
  `firewall.r2_fibre_infinitude_reinstated` and
  `firewall.t1_w2_encoding_reinstated` are both `False`;
  `nucap_removal_authorized: False`.
* The mutation harness is real (unique-target assertion, `/tmp` copy,
  subprocess, control must pass). I re-ran the four permanent mutations
  outside the suite and got the exact claimed deaths:
  `MUT_G → "strict NE law failed"`,
  `MUT_H → "Lemma T1' closed form disagrees with dq % dp"`,
  `MUT_I → "Theorem F refuted: an MP2-alive (M >= 2) cell exceeds the
  two-pole constant at r0 <= 3"`,
  `MUT_J → "r0=2 countercell must be M = 1 (D = 1 forces it)"`.
* The `t1_regression` sweep is non-vacuous: 17,610 cases over
  `μ ∈ {1,2,3}` and five `w` including `7/2` and `5/3`; the universal
  identity and `M = dp` leg are checked at every `μ`, the iff only at
  `μ = 1` — correctly scoped.

**"Preserved verbatim" is true at the executable level, not literally.**
`gap_pattern_certificate` and `charged_slice` differ from R2 by docstring
lines plus two deleted comments in `charged_slice`; `kbar_bound`,
`e5_eliminate_nu_g`, `BOOK`, `FORCED_SUBBOOK`, `DEAD56_SPOT` are
byte-identical. No executable statement changed. §10's "preserved
verbatim" should read "preserved with docstring-only edits".

## C7 — Corrected glosses (§6): CONFIRMED

* **`ν_U = 13`.** §11a's arrival row for `(18,27,13,9)@5` is
  "direct (2,5),(7,5),(12,5); neutral ν≡4(5)". `13 ∉ {2,7,12}` and
  `13 mod 5 = 3 ≠ 4` (equivalently `5 ∤ 14`), so `13` is not
  arrival-legal; the mixed pin `κ̄ = (ν_U − 1)/2 = 6` matches only at
  `ν_U = 13`, so the mixed pin kills the cell. I further checked the
  mixed-pin `ν_U = ν_G` value against the arrival row for
  `(15,25,12,5)@3` (12 vs `ν≡2 mod 3`), `(21,35,17,7)@4` (17 vs
  `ν≡3 mod 4`), `(25,35,17,5)@8` (17 vs `{5}` / `ν≡7 mod 8`) and
  `(26,39,19,13)@7` (19 vs `{3,10,17}` / `ν≡6 mod 7`) — all illegal —
  while `(9,15,7,3)@2` (`ν_U = 7`, neutral `ν≡1 mod 2`) and
  `(10,15,7,5)@3` (`ν_U = 7`, direct `(7,3)`) survive. The 2-cell
  forced-ν sub-book is exactly right.
* **`(4m−2, 6m−3)`.** Verified against all 12 `κ̄ = 6` book rows:
  `ν_G = 3m−2`, `M = 2m−1`, `κ̄ = 2(6m−3)/(2m−1) = 6` identically,
  `w_U^req = 2/m`. `gcd(6, 3m−2) = 2` for even `m` (so N1 fails) and
  `= 1` for odd `m`; the four even-`m` members
  `(14,21,10,7)@4, (22,33,16,11)@6, (30,45,22,15)@8, (38,57,28,19)@10`
  are §11a's four recorded N1 kills verbatim. Termination at `m = 25` is
  §11a's closure exhaustion (`no priced state with w ≤ 2/27 at budget 5`),
  correctly attributed to the closure and not to any theorem here.
* **Charged slice.** `(μ,μ₀,w,w_U) = (1,2,2,3/2)`: Theorem C gives
  `ν_G = (κ̄+2)/3`, `κ̄ ≤ 10`, menu `{4,7,10} → ν_G ∈ {2,3,4}`; cells
  `(4,8)` (`M=4`, T1-dead, `κ̄=4 ∈ {3,4}`), `(5,7)` (`M=1`, MP2-dead),
  and `κ̄=10` non-integral `dq` ⟹ DEAD. Kill is reading-stable.

## R1 — REPAIR REQUIRED (§8 migration only): the scope guard does not
## exclude a `ν_G = 1` (case-I) merge, and the gap is non-vacuous

The DIFFICULT-regime loop enumerates **integer** `κ̄` only. That is
licensed by DS1(c) — but DS1(c) needs `ν_G ≥ 2`, which is hypothesis (H2)
of case III, *not* something the structural guard tests:

    if not (zero is a pole-chain leaf and len(non0) == 1
            and inner_mus == [] and inner0_mu is None):

Nothing there distinguishes a `ν_G = 1` (I-family, DEPTH §5c) merge. And
the legacy `cell_check:239-241` deliberately admits `ν = 1` patterns at
**fractional** `κ̄` (`if nu >= 2 and kbar.denominator != 1: continue`).

**Non-vacuous.** Searching structurally in-scope states `(μ, μ₀, w, w_U)`
with `μ ∈ [2,4]` and small rational `w, w_U`, I find **1,290** rows where
the `ν_G = 1` branch of Theorem C yields a fractional `κ̄` on which the
canonical `cell_check` returns `True` — e.g. `μ=2, μ₀=3, w=1, w_U=3/2`
gives `κ̄ = 5/2`, `X = 3`, `(dp,dq) = (6,5)` with `M_G = 1`, alive. The
legacy path reaches that row (mixed pin `ν_H = 1` with a depth-0 arrival,
`nu_ok(1,3,1)` true) and returns `ALIVE`; the proposed E5 branch would
scan `κ̄ ∈ Z ∩ (w, …]`, find nothing, and return `DEAD`. On a case-III row
the E5/legacy divergence is intended; on an I-family row the case-III
handshake does not apply at all, so the kill would be unlicensed.

The R2 review called the guard "sufficient", but only in the routing
sense it stated ("with `len(non0) == 1` the R2.1(ii) pin is unreachable").
R3 re-cites that as "review-confirmed sufficient", which over-reads it.

**Required repair (three lines, no theorem changes).**
1. §8: state that the E5 branch is licensed only where `ν_G ≥ 2` is
   established, and make the guard fall through to `solve_arr` whenever a
   `ν = 1` pattern realises the row (i.e. whenever `cell_check` restricted
   to `ν = 1` succeeds at any `κ̄` permitted by Theorem C at `ν_G = 1`).
2. Add gate **(G-g): case-I negative control** — in-scope-by-structure
   rows that are I-family merges must retain the legacy verdict, with the
   `μ=2, μ₀=3, w=1, w_U=3/2 → (6,5)` row as a sealed fixture.
3. Soften "review-confirmed sufficient" to "review-confirmed sufficient
   for routing".

## Nits (no verdict impact)

* **N1.** §5's regression block prints `w=3/2 … empty menu` immediately
  under the T1 divisor menus. That "empty" is the *Theorem-C* `κ̄` menu at
  `(μ₀,w_U) = (2,1/2)` (there `ν_G = κ̄ + 3/2 ∉ Z` for every integer `κ̄`),
  **not** the T1-dead set: at `w = 3/2` the T1-dead integer `κ̄` are
  `{2,3}` (`n = 3` and `n = 1`). The report is not wrong — the closed form
  is explicitly conditioned on `w ∈ Z` — but the juxtaposition invites
  "non-integer `w` ⟹ no T1-dead cells". One clarifying clause.
* **N2.** §8's EQUAL-regime comment says "mirror it exactly for verdict
  parity", but the mirrored predicate is not `nu_ok` — legacy tests
  `ν_H = ν_i or (ν_H ≥ 2 and gcd(ν_H, μ₀) = 1)` on the *arrival* index,
  while the E5 line tests `ν_G ≥ 2` plus `μ₀ | M_U`. That substitution is
  right under E5 (the arrival law applies to the free `ν_U`), but "mirror
  it exactly" is true only of the *absence of `cell_check`*.
* **N3.** Theorem F's printed `r₀ = 3` proof should add the one line
  disposing of `ν = 1` (see C3).
* **N4.** §10's "preserved verbatim" → "docstring-only edits" (see C6).
* **N5.** §4/§11 should say the `r₀ = 4` witness is illustrative, not
  minimal or isolated (see C3).

## Maximum safe consequence

At the promoted-record tier (H5a Q-value + E5; `U_7C` recorded, not
adjudicated), the following are now established and may be cited:

1. **Merge-local finiteness is complete for two-pole case III.** Finite
   priced-state closure × finite `κ̄` menu (Lemma A / Theorem B) × finite
   pattern fibre (Theorem D) ⟹ the two-pole case-III cell book over any
   fixed state `(μ, w, μ₀, w_U)` is a **finite, effectively enumerable
   object**, with the per-entry member count bounded by
   `[(1+ν)/(rν) + δ/ν] / (1 + u − ceil(u))` and that bound attained on
   32.4% of the census keys. At `μ = 1` each menu entry has exactly one
   cell.
2. **The two-pole ratio constant is arity-graded, not universal.**
   `dq/D ≤ (r₀+1) + ((r₀+1)δ+1)/M` at every interior merge, with an
   exact equality profile; `2δ+3` is its `r₀ = 1, M = 1` corner.
3. **No MP2-alive violator exists in the campaign's arity range.** At
   `r₀ ∈ {2,3}` — the whole range reachable at `TDMAX = 14` via MP1 —
   every two-pole-constant violator has `M = 1`, hence is MP2-dead as an
   interior merge. This is now a theorem, not a census observation.
   It is false from `r₀ = 4` on.
4. **The zero-chain T1 verdict has a correct general form.** At the
   `μ = 1` pinned solve, `dp | dq ⟺ M = dp ⟺ w/(κ̄−w) ∈ Z≥1`, and
   `κ̄ ∈ {w + d : d | w}` for integer `w, κ̄`. `κ̄ ∈ {3,4}` is a `w = 2`
   encoding and must never be hard-coded.
5. **No incoming-index bound exists, follows, or is required** under E5;
   the mixed pin, where imposed, *kills* `(18,27,13,9)@5` and leaves
   exactly the 2-cell forced-ν sub-book.
6. **`NUCAP = 500` stays.** Wholesale replacement remains certified
   UNSOUND; Theorem D does not rescue it (the failure is arity/inner
   scope), and Theorem F confines the `r₀ ∈ {2,3}` phenomenon to
   `M_G = 1` rows.

## Exact exclusions

Nothing here licenses: any canonical engine edit (the §8 plan is
unexecuted and now carries the R1 gate debt); removing, raising or
replacing `NUCAP`; `U_7C` adjudication or the mixed reading; equal-nonzero
join `κ̄` bounds (the `κ̄ = w(2ν+1)`, `M = 3` family is still
affine-unbounded); inner-merge or multipole trees (unknown `w` at solve
time); `r₀ ≥ 4` MP2 behaviour (Theorem F is false there, and the failure
is generic); realizability of any cell (i-sync/`n_e` untracked; the
priced-closure layer is cited, not re-proved); the legacy `cell_check`
grammar beyond its conservative-existence role; source landing; full
configuration cover; topological-degree bounds; Keller counterexamples;
JC2; any AWS or fleet action. Theorem D is a statement about *pattern*
fibres, not about routes, budgets, or transport.

## Best next lemma

**The EQUAL-regime (`δ = 0`) kill lemma.** `μ₀ = μ` is now the only
regime with zero kill power: Theorem C degenerates to `ν_G = w/w_U`, `κ̄`
is genuinely unpinned, and both legacy and the proposed E5 branch return
`ALIVE` without any existence solve. But the Theorem E machinery closes it
at `δ = 0` in two lines: `D = νA'`, `σ ≤ A'`, `1 ≤ A'` give
`dq = 1 + ν(1+σ) ≤ 1 + 2νA' = 1 + 2D`, hence

    dq/D <= 2 + 1/D <= 2 + 1/M,   so   kbar in Z cap (w, mu*w*(2 + 1/M_G)].

That is a **finite, explicitly bounded `κ̄` menu at `μ₀ = μ`**, so the
EQUAL regime becomes decidable: ALIVE iff `cell_check` succeeds for some
`κ̄` in that menu. Proving it (and certifying that the existence solve is
complete on that menu, which is the only real work) converts an
unconditional `ALIVE` into a real verdict and is the largest remaining
merge-local gain available without touching `U_7C` or the arity/inner
frontier. Second choice: promote Theorem D to a *state-level* count —
`Σ_{menu entries} |fibre|` in closed form — which is what a
`fibre_solve`-based engine would actually consume.

## Reproduction

    /tmp/opus_r3/box.py        # 93,735 / 92,772 / hist / 0 violations / 1,815 mu=1
    /tmp/opus_r3/complete.py   # 90,957 keys, cap-free: hist, max 12, s=1202, 29,444 equalities
    /tmp/opus_r3/deep.py       # 75,808 keys under the review's stated regime
    /tmp/opus_r3/readings.py   # eight readings, none gives 57,960
    /tmp/opus_r3/seven4.py     # candidate counts 4/6/15/57/213, legal 0, canonical cell_check
    /tmp/opus_r3/arity.py      # 357,260 / 439,730 / 75,713, 0 violations, violator M = {1}
    /tmp/opus_r3/r04.py        # r0 = 4 failure is generic (186 MP2-alive violators)
    /tmp/opus_r3/nug1.py       # 1,290 in-scope rows alive only via nu_G = 1 fractional kbar

The report body hash is over the bytes preceding the final `---`
separator line (recompute with
`python3 -c "import hashlib,sys; b=open(sys.argv[1],'rb').read();
print(hashlib.sha256(b[:b.rfind(b'---\n')]).hexdigest())" <file>`).

---
Review-body SHA-256 (bytes before the separator line above): `45ec4167440c2e17ed3929b1e225df50e738a55f16b6cecce560f127cf0767df`
