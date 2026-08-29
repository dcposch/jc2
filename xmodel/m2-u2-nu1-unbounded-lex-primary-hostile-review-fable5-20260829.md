# Hostile review — Grok 4.6 U2 (`nu_G=1`, unbounded-`lex`) primary (Fable 5, 2026-08-29)

Reviewer: Fable 5, independent lane. Target:
`xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`,
full-file `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613`
(recomputed, exact), body
`49fdda2b84e4a405f6432239546826a943326a5357f10efb26eaa8b2a149a1b6`
(recomputed as the first 24143 bytes, byte-identical to the marker-line
convention stated in the target). Packet
`cases/m2_u2_nu1_unbounded_lex_grok46_20260829/`: all six file hashes
recomputed and byte-exact against the target's §8 list.

## 0. Verdict

**`REPAIR_REQUIRED`** (lead), decomposed as the prompt demands:

| layer | verdict |
|---|---|
| (a) local ODE algebra (U2-ODE, `C'` classification) | **PASS**, theorem-grade; three strengthenings recorded below |
| (b) transport (`dp,dq,E,M,kbar,w_tr,lambda_G`) | **PASS** at recorded pattern scope; one notational conflation, nothing corrupted downstream |
| (c) fixed-terminal finiteness ("Theorem, §4" / `U2_REDUCED_FINITE`) | **REPAIR_REQUIRED**: statement unrefuted and probably true, but the recorded proof is a sketch with real holes; no counterfamily found; repair lemmas supplied |
| (d) low-td controls (td=7 tail, td=8 direct, td=8 post-(A), td=12 cells) | **PASS** at charged scope, with the tier classification of §5 below and one test-suite blind spot |

Because the headline outcome string `U2_REDUCED_FINITE`, the §4 "Theorem",
and §10's "regime U2 … is now finite at the P1-terminal ledger of every
fixed `(td, entry)`" all rest on (c), the packet cannot be promoted as a
finiteness result. The (a), (b), (d) residues are promotable at their
recorded scopes (see §6).

No verdict here authorizes landing, realization, Statement-3.9 gluing, a
global `td` bound, or any JC2 consequence. Nothing here licenses AWS.

## 1. Custody and provenance

Read and hash-verified (byte-exact against the target's §0 pins):
the Opus equal-join report `7ed65bc2…`, its Grok hostile review
`8755bd5d…`, `ladder/BOOK-OFFAXIS.md` `7679db8a…` (§§0–11a in full),
`ladder/SHEET6-MULTIPOLE.md` `93adb7ac…` (MP4–MP9, D9),
`ladder/SHEET6-L1.md` `69e6e4c1…` (§4 L1b), `ladder/SHEET6-DEPTH.md`
`ad9ced6c…` (§1, §5c–5d), `cases/l1_ode_check.py` `e766bfe2…` (header),
`xmodel/sol-td7-law.md` `99bd762a…`, `cases/book_offaxis.py` `c22e3a1f…`.
Also read: the reduced-chain R2 report
(`m2-finite-reduced-chain-skeleton-r2-repair-sol56-20260829.md`, body
`995f310e…`) and its Opus review (`PASS_IMPLEMENTATION_R2`).

**Provenance defect (non-blocking).** The target pins
`ladder/REDUCTION.md` at `0a88db0d…`; disk now reads `007e76de…`, and the
file is an empty blob at every commit touching it, so the pinned bytes are
unrecoverable from history. Impact is low: the target imports no REDUCTION
theorem (CRITICAL 4–7 are cited only as context, and the current disk text
still names U2 as a leak, consistent with the target's mission). Repair
R8: refresh or drop the pin.

Execution: replay + clean-room + mutations all run; this session had a
shell. No web, AWS, CAS, `jc2-lean` access, global `git status`,
workspace-wide search, commit, or canonical edit. Writes: this file only;
scratch under `/tmp/u2rev/`.

## 2. Replay (audit item 6)

From the packet directory, ordinary and `-O`:

    emit_sha256 a6670fa1b2d5dfecbf37ced757fac081b6c74334b88aa7e041fc90f59354b6b6
    t1_identities 8 / r2_parity 11 / td7_inversion_fitting 0 / td8_direct_mp2_alive 0
    U2_EMIT_PASS ; CMP_OK ; U2_NU1_TEST_PASS checks=148 (both modes)

`/tmp/u2.json` file hash `52eafb22…` matches; the `emit_sha256` field
recomputes exactly from the field-stripped canonical JSON. `--cap` exits 2
with `REFUSED cap token` on both executables. No caps, floats, or engine
imports found in the packet source; `polyexact.py` spot-checked
(binomial expansion, differentiation) and independently corroborated by my
own multivariate class (below).

**Test-suite honesty findings.** (i) The check counter includes at least
two free increments with no assertion (`test_u2.py` line ~40 "count it",
and the `n += 1` after the post-(A) loop), so `checks=148` mildly
overcounts. (ii) **The claimed unique `L=1` exact-fit cell is not pinned
by the tests**: the post-(A) loop asserts `n_fitting == 0` only for rows
after the first. Mutation M3 (budget `7-psi -> 8-psi` in
`td8_postA_L_scan`) changes the `L=1` fitting count 1 → 2 while
`test_u2.py` still passes 148/148. The claim *is* sealed by the recorded
emission hash, but a test must assert it (repair R7). Mutations M1
(naive `dq = r+L+1` slot), M2 (recurrence sabotage), M4 (parity flip)
all make the suite fail, as required. The packet's own
`naive_eta_fails` mutation is close to vacuous — it checks a different
shape against the absorbed `rho`, which cannot arbitrate the
normalization (see §3).

## 3. Audit item 1 — normal form and `nu=1` absorption: CONFIRMED

The absorption is grounded where it must be: `SHEET6-MULTIPOLE.md`
MP6(c) ("η-factor absorbed at ν = 1"), `l1_ode_check.py` header ("e0 = 1
iff nu >= 2, forced … nu=1 merged family has q = p*s, no eta factor
forced") and family B `(dp,dq) = (2, 2+l)`, and L1b §4 — all verified on
disk. R1.0's `η ‖ q` clause is explicitly conditional on `ν ≥ 2`, so no
0-root of `q` is forced at `ν = 1`; a 0-root of `p` (`eps ≥ 1`) forces
`e0 = 1` (R1.0's `p(0) = 0` clause), and (NE) `eps·dq < dp` /
`m_j·dq < dp` with `dp` `L`-free and `dq ~ L` empties `eps ≥ 1` and
`k ≥ 1` for all large `L`. The `e0 = 1` variant is exactly `S(0) = 0`;
`dq = r+L` either way. Equal `w` across equal-`mu` non-0 arrivals is
forced by R2.1(i), not assumed. `Rad` squarefree with roots off 0, `S`
simple and coprime — R1.0. No orbit collisions (distinct arrival roots),
no characteristic assumption beyond char 0, scaling `⊖` free. The
Grok review §7.4's naive-slot formula
`w_tr = mu·w·(r+lex)/((mu-eps)+mu·lex)` is numerically identical to the
absorbed law under `lex ↔ L−1`; the real content of absorption is the
**shape space** (`S(0) ≠ 0` allowed). My clean-room check makes this
sharp: with the η-**forced** (naive-copy) constraint `S(0)=0`, the
generic quadratic dies at every odd `L` tested, while the centered one
survives — so the normalization is load-bearing and correctly resolved
by the canonical clauses, not by the packet's identity mutation.

## 4. Audit item 2 — the U2-ODE and the classification of `S`

**Identity.** Re-derived by hand and re-verified with my own independent
sparse multivariate class on a strictly wider symbolic grid than the
packet (`r ∈ {2,3,4} × mu ∈ {1,2,3} × L ∈ {1,2,3}` plus `(5,1,1)`,
`(2,4,2)`; packet: 8 tuples): with `p = Rad^mu`, `q = Rad·S`,
`rho = dp/dq = r·mu/(r+L)`,

    rho·p·q' − p'·q = p · (mu/(r+L)) · (r·Rad·S' − L·Rad'·S),

so Prop. 8.1(iv) ⟺ `r·Rad·S' − L·Rad'·S = C' ≠ 0` and
`C = mu·C'/(r+L)` (also verified on a concrete `(2,3,L=3)` instance
against the full ODE). Exact.

**`r=2` is a genuine iff, now theorem-grade.** The positive-degree
coefficient map on monic degree-`L` `S` is square and injective (a
degree-`d < L` kernel element has top term `(2d−2L)t^{d+1} ≠ 0`), so a
unique monic `S` exists for every squarefree quadratic. The ODE and `C'`
are translation-covariant (verified exactly: `t²+t+1` vs its centered
form `t²+3/4` give equal `C'` at `L = 1,3,5,7`), so WLOG `Rad = t²−A`;
the recurrence `(m−1−L)s_{m−1} = A(m+1)s_{m+1}` seeds only indices
`≡ L (mod 2)`, whence `C' = −2A·s_1 ≠ 0` iff `L` odd — for **all** `L`,
not just the charged window. Clean-room: parity iff confirmed on five
quadratics (two non-centered) for `L = 1..12`. The even-`L` kill is the
D9 residue `(−1)^{n−1}·binom(2n−2,n−1)` in linear-algebra form, exactly
as the target says; the argument is `S(0)`-agnostic, so it covers the
old `l1_ode_check` families B **and** B-η uniformly and lifts
MULTIPOLE §4's `l ≤ 4` engine cap — a strengthening the target earns
but does not claim explicitly.

**Free admissibility lemma (new, gift to the producer).** If `C' ≠ 0`
then `S` is automatically squarefree and coprime to `Rad`: a shared or
double root `ξ` gives `0 − 0 = C'` at `ξ` (using `Rad(ξ)S'(ξ)` and
`Rad'(ξ)S(ξ)` both vanishing termwise), contradiction. So the packet's
charged squarefree/coprime checks are provable outright, and "T1-alive"
= `C' ≠ 0` needs no admissibility rider.

**`r ≥ 3`.** Power family: recurrence re-derived; index chain
`L, L−r, …, 1` at `L ≡ 1 (mod r)` has all factors nonzero, so
`C' = −rA·s_1 ≠ 0` for **all** `k` (theorem, not merely charged;
clean-room `r ≤ 6`, `k ≤ 5`, `A = 3` — a different `A` than the
packet's). `r | L` on the power shape: `s_1 = 0`, dead — confirmed. The
target correctly presents `r ≥ 3` survivals as examples, not an iff
(generic cubic empty at `L ≤ 12` replayed via the linear solve).
**Strengthening:** at `L = r` the death is universal, not just
power-shape: `C' = r·W(S,Rad)` constant forces `∫Rad^{-2}` rational,
whose residue at a root `a_i` is proportional to
`Rad''(a_i)/Rad'(a_i)`; `Rad''` (degree `r−2`) cannot vanish at all `r`
roots. Verified on 10 random squarefree cubics/quartics. **Slip:** the
Dickson constant is `±2rL·alpha^min(r,L)` (verified exactly,
`r = 2..6`), not the target's `2rL·alpha^r` — wrong at `L = r−1`;
`C' ≠ 0` unaffected.

## 5. Audit item 3 — transport: CONFIRMED, one conflation

Independent derivation from R2.1 + Prop 9.3(b): `X = mu(kbar − w)` and
`X/kbar = dp/dq` give `kbar = mu·w·dq/E`, `E = mu·dq − dp = mu·L`,
`kbar = w(r+L)/L`, `w_tr = kbar(dq−1)/dq = w(r+L−1)/L`,
`M = gcd(r·mu, r+L)`, all verified on a 288-cell exact grid, plus
monotonicity `w_tr > w` (strict, `r ≥ 2`), the limit `w`, and the P3
anchor `2 + 1/(t−1)` at `(2,1,2t−2)`. `lambda_G = 0` is exactly P2
(`eps = k = 0`: no priced object; arrivals and `q`-extras price 0).
`(S)` ⟺ `L ≥ 1`; `(R)` `dp ≠ mu·dq` ⟺ `L ≠ 0`; `M ≤ r·mu` is `L`-free —
the load-bearing boundedness. `kbar ∈ Q` is legal at `ν_G = 1` (case I,
N1 off; §8's family-I precedent). Nothing suppressed is consumed later
(`i_G`, `n_e`, `e0` all policy-inert; the trunk consumes only
`(w_tr, M)` and `l | M_G`).

**Conflation (repair R2).** §2's display line
`rho = dp/dq = r·mu/(r+L)` inside the frame table is the *ODE slope*
(§3's `rho`), not the frame `ρ_G = D_G/deg p_G = kbar/dq = w/L`
(DEPTH §1, P1). With the printed line read literally,
`w_tr = kbar − rho` would be false; the stated value
`w(r+L−1)/L` is nonetheless the canonical P2 value and is what every
downstream formula uses. Fix the line; no propagation found.

## 6. Audit item 4 — the finiteness theorem: the proof is not there yet

The §4 "Theorem (U2 reduced-finite at fixed `(td,entry)`)" is the
packet's centre of gravity and its recorded proof is a compressed sketch.
What I verified, what I can repair, and what is genuinely open:

**Verified ingredients (sound).**
- `M_G = gcd(r·mu, r+L) ≤ r·mu`: `L`-free. Clean steps only divide `M`
  down (`M' | l | M`). Resonant steps require `Δ | num(w)`,
  `den(w) | dq`, contract `w` by `n/Δ ≤ 2/3`; neutral steps fix `w`.
  Trunk chain vertices have `ν ≥ 2` (DS1(a)), so `kbar ∈ Z` bites at
  *every* trunk step — the target never says this, and it matters.
- The resolvent identity `E(l·a·s − kbar·d·C) = l·a·T` (P5/R2): I
  re-derived it in two lines from `E = νC + (l−ε)`, `dq = sν+1`. The
  divisor bound `E | l·num(w)·T` is therefore self-contained.
- Direct-terminal case: `j = M(1−w_tr) ∈ N*` forces `L | M·c(r−1)`
  (`w = c/d`), finitely many `L`. Confirmed concretely: on the td=8
  post-(A) AP, `j = (L−2)/L`, never integral — matches the target.

**Repair lemmas I supply (target's versions are absent or ε=0-only).**
- **`M' | T` exactly** (all `ε`): `s·dp − (l+Sm)·dq = εs − (l+Sm) = −T`,
  and `gcd(M', ν) = 1`, so `M' | T` with `1 ≤ T ≤ Sm + l`. This is the
  correct general form of the target's "`M' | (l+Sm)`" (which is the
  `ε = 0` case) and closes the "finite grid of legal `w_t`" step:
  `M ≤ M_G·(B+1)^B` along any trunk with `≤ B` dirty steps.
- **Dirty multiplier bound**: `w'/w = l·s/E ≤ l` (from
  `E ≥ 2C + l − ε` and `C ≥ k + l·lex`); pure-(b) gives
  `l/(l−ε) ≤ l`. With `≤ B` dirty steps and resonant contraction
  `≤ 2/3`, the number of resonant steps on any terminal-reaching trunk
  is bounded by `log_{3/2}(w_max·M_max^B / w_min)` — the missing
  induction skeleton over multi-step paths, cycles, and revisits.
- **Focusing-step kill (single step)**: for a dirty step at `ν ≥ 2`
  consuming `num(w) ~ L` (the `s ∝ L` regime the target waves at),
  `kbar' = l·a·dq/(dE) = ν·τ + m/(dT)` on any family hitting a fixed
  target `τ`; since `1 ≤ m` and `d·T ~ L`, integrality of `kbar'` fails
  for all large `L`. This kills the `ε = 0` unbounded-`lex` reset step
  into a terminal — the specific hole in the target's garbled
  parenthetical.

**Genuinely open (the repair obligation).** The composition of these
lemmas over an arbitrary interleaving of neutral/resonant/dirty steps
(length not budget-bounded in the clean part, `den(w)` tracking through
`den(w') | ν·E·d`-type growth, and the focusing argument made uniform
over `≤ B_res + B` non-neutral steps) is not written, by the target or
by me. Until it is, §4 is a conjecture with strong charged support, not
a theorem. Additional recorded defects: the td=8 dirty display
`E | 6(L+2)T` should be `6(L+1)T` (`num(w_tr) = 2(L+1)`); the
parenthetical "(from `(n−1)nu+1 = Delta` with `n` a multiple of `L`)"
does not describe the actual Diophantine (in the forced families `n`
stays bounded and `ν ~ cL`); "hence `L+1 | 2T`" is not derivable as
written.

**Scope hole (repair R4).** The theorem quantifies over a fixed entry
but its proof fixes the arrival data `(r, mu, w)`. That is complete when
the U2 merge takes *chain* arrivals (finitely many `(mu, w)` by the
chain theorem + St 8.4), but at `m ≥ 3` an arrival can be an inner-merge
child, and an inner **U2** child supplies infinitely many distinct `w`
values — a two-parameter `(L_inner, L_outer)` family the recorded proof
never quantifies over. At `td ≤ 14` I checked this does not materialize
(census: every `m ≥ 3` row has `b ≤ 2` poles, so direct inner U2 dies by
the 2-power-`mu` parity law; post-(A) `mu = 3` inner children feeding an
outer *equal*-`(mu,w)` join are blocked by R2.1(i) exact `w`-matching,
e.g. `w_tr(L') = 3/2` has no integer solution). But the theorem text
must restrict to chain-arrival U2 merges or prove the nested case.

**No counterfamily.** I attacked the td=8 post-(A) AP by hand
(first resonant step forces `Δ = 2(L+1)`, `ν = L−2`, `L−2 | 5`, so
`L ∈ {3,7}`; the `L = 7` continuation dies on `j = 17/7 ∉ N`) and probed
dirty resets; everything died. Zero-cost trunks, cycles, changing
radicals, and family-record collisions are all covered by the repair
lemmas above once the composition is written; a finite capped search was
not used as evidence for anything in this section.

## 7. Audit item 5 — low-td controls: tier classification

All controls replayed and independently reproduced (clean-room menu
written from the P0/P1 text, not from `controls.py`):

- **td=7 `(2,2t)` tail, T1 death: THEOREM-level, all `t`** (even-`L`
  parity, §4 above; the packet charges `t ≤ 15`/`t ≤ 10` but the parity
  argument is complete). Nit: the target twice says "t=2..11 in the test
  suite"; the suite charges `t = 2..10` (`tmax=10`).
- **td=7 tail, budget death: DIAGNOSTIC in-packet.** My menu finds the
  one-step terminal set *raw-empty* (0 hits before the budget filter,
  `t = 2..11`), so at depth 1 this is an arithmetic death and the budget
  filter never fires. One-step inversion alone does not exclude
  zero-cost multi-step trunks; tail closure at budget tier rests on
  canonical P4 (multi-step, hand-proved), and at theorem tier on the
  target's own T1 parity kill — which is the stronger and sufficient one.
- **td=8 direct death: THEOREM-level.** Census row verified on disk
  (unique td=8 row, type `(2,3)`, `Λ=(4,4)`, poles `(1,2,3)²`,
  `M=[2,2]`, `w0=3/2`; the full 23-row L6 census re-extracted and the
  td=7/td=12 rows match the target exactly). `mu | 2` ⟹ even `L`
  T1-dead, odd `L` `M=1` MP2-dead: 32/32 charged, and the underlying
  parity/gcd laws are theorems, so this death is uniform in `L`.
- **td=8 post-(A): CHARGED DIAGNOSTIC cells.** The `(A)`-step data
  `(21,15), λ=2, w→2/3, M→3, mu=3` re-priced by hand from P0 (`kbar=5`,
  gap 2) — matches printed St 9.6. My independent menu reproduces
  exactly 4 hits / 1 fitting at `L=1` and 0 hits at
  `L ∈ {7,13,19,25}`. The fitting route
  (`l=3, eps=0, k=1, Sm=2, lex=0, ν=17, E=20, (dp,dq)=(85,35), kbar=7,
  X=17, λ=2, w'=2/5, M'=5, j=3, ψ=1`) passes every law I can locate
  (resolvent divisor, NE strict, (R)/`T=5`, searrow, integrality) at
  exact budget equality `4+2 = 7−1`. It is a pattern-tier cell under R4
  and the λ-lower-bound rider, correctly not claimed as more. The rows
  `L ≥ 7` are one-step-dead (charged); their *infinite* death is §4's
  theorem and inherits its gap.
- **td=12 cells: VERIFIED.** Direct `(2,5)` `mu=3, L=1`: clean resonant
  `Δ=8, (n,ν)=(2,7)` from `w_tr = 8/3` to `(2/3, 3)`, `ψ=2`, `λ=0`,
  slack 9 — reproduced independently. Nit: the "next equal-w rows"
  sentence skips the partial-equal `m ≥ 3` rows (td=10/11/13/14 carry
  equal-`w` pole pairs); their direct U2 joins die by the same 2-power
  law, but their post-(A) analogues are unscanned and covered only by
  the §4 claim — i.e., conditional on the unproved theorem.

## 8. Audit item 6 — clean-room and mutation record

`/tmp/u2rev/cleanroom.py`: **2038 exact checks**, all pass — independent
poly class, identity grid (29 tuples), `C = mu·C'/(r+L)` concrete,
parity iff on 5 quadratics + translation invariance, η-forced shape
discriminator, power family (`A=3`), `r|L` and universal `L=r` deaths,
Dickson values, 288-cell transport grid, independent one-step menu
(with neutral-step terminals added — no new hits appear), tail
`t=2..11`, post-(A) `L ∈ {1,7,13,19,25}`, td=12 cell. Census extraction:
23 L6 rows, byte-consistent with the target's citations. Mutations: M1
(naive slot) FAIL✓, M2 (recurrence) FAIL✓, M4 (parity flip) FAIL✓, M3
(budget+1) **passes tests while changing the L=1 answer** — the one
blind spot (R7). Cap tokens refused, exit 2. No hardcoded expected rows
found; two formula-restating checks and two free counter increments
noted.

## 9. Maximum safe consequence

Promotable now, at recorded pattern/superset scope, entry-local, no
landing/gluing/JC2:

1. The absorbed U2 normal form (`p = Rad^mu`, `q = Rad·S`,
   `dq = r+L`, `eps = k = 0` for unbounded `L`, `e0` = `S(0)=0`
   subcase) and the transport laws `dp = r·mu`, `dq = r+L`, `E = mu·L`,
   `kbar = w(r+L)/L`, `w_tr = w(r+L−1)/L → w` strictly,
   `M = gcd(r·mu, r+L) ≤ r·mu`, `lambda_G = 0`, merge never terminal at
   `w ≥ 1`.
2. Prop. 8.1(iv) ⟺ `U2-ODE = C' ≠ 0` with `C = mu·C'/(r+L)`; the `r=2`
   parity **iff** for every squarefree quadratic and every `L` (both
   `e0` variants, lifting the B/B-η `l ≤ 4` caps); power-family
   survival on `L ≡ 1 (mod r)` for all `k`; power `r|L` death;
   universal `L = r` death; free admissibility (`C' ≠ 0` ⟹ `S`
   squarefree ∧ coprime).
3. The two uniform deaths: td=7 `(2,2t)` tail T1-dead for every `t`;
   td=8 direct equal-`mu` sector dead for every `L` (2-power `mu`).
4. The td=8 post-(A) `L=1` slack-0 cell and the td=12 `(2,5)` `L=1`
   clean-terminal cell as R4 pattern-tier cells.

**Not safe:** `U2_REDUCED_FINITE` as a theorem or any finite-ledger
claim at fixed `(td, entry)`; any P5 / REDUCTION CRITICAL-5 wording
change implying the U2 leak is closed; the "§4 forbids [an infinite
counterfamily] at any later td ≤ 14 entry" sentence (conditional on the
unproved theorem for all unscanned rows); nested (inner-merge-arrival)
U2 at any tier; the target's "Stop. Do not spend a further desk day on
unbounded lex" — premature while (c) is open.

## 10. Exact repairs

- **R1 (blocking).** Prove §4 as a real composition theorem: fix
  `ν ≥ 2` at trunk vertices; bound resonant steps via multiplier
  `≤ 2/3` and dirty multiplier `≤ l`; replace `M' | (l+Sm)` by the
  exact `M' | T`; then make the focusing-step integrality argument
  (`kbar' = ν·τ + m/(dT) ∉ Z` for large `L`) uniform over all
  `≤ B_res + B`-step interleavings, or exhibit a counterfamily.
- **R2.** Fix §2's `rho = dp/dq` frame line (`ρ_G = kbar/dq = w/L`).
- **R3.** `E | 6(L+2)T` → `E | 6(L+1)T`; rewrite the "(n a multiple of
  L)" parenthetical and the "L+1 | 2T" step to match the actual
  Diophantine.
- **R4.** Restrict the theorem statement to chain-arrival U2 merges, or
  add the nested-arrival case (td ≤ 14 nesting deaths recorded here may
  be cited).
- **R5.** Dickson constant `2rL·alpha^min(r,L)`.
- **R6.** Record the free admissibility lemma; drop the charged
  admissibility riders.
- **R7.** `test_u2.py`: assert `scan[0]` (`n_fitting == 1`, slack 0);
  remove or label the two free `n += 1` increments; fix the two
  "t=2..11" range claims.
- **R8.** Refresh or drop the stale `REDUCTION.md` pin.

## 11. Next research target

Complete R1 (the composition lemma) — that single lemma-complex converts
the whole packet, including the post-(A) and td=12 tables, into the
first genuine finiteness theorem for a proved-infinite reduced regime,
and it is desk-scale: the three supplied lemmas reduce it to one
uniform-integrality induction. After that (not before), the target's own
stop-condition and the hand-off to the U1 coefficient/gluing question
(review §11: realizability of `t^r − A` at infinitely many admissible
`nu ≥ 2`) are the right priorities.

## 12. Commands and counts

    # replay (packet dir): emit ordinary/-O, cmp, tests ordinary/-O, --cap
    #   -> hashes above, 148/148 both modes, cap exit 2 twice
    # /tmp/u2rev/cleanroom.py -> CLEANROOM_PASS checks=2038
    # census extraction -> 23 L6 rows, td7/td8/td12 rows byte-consistent
    # mutations: M1 FAIL, M2 FAIL, M3 PASS(+L=1 1->2), M4 FAIL

Target full `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613`,
body `49fdda2b84e4a405f6432239546826a943326a5357f10efb26eaa8b2a149a1b6`
(both verified). Packet emission body `a6670fa1…`, file `52eafb22…`
(both verified). Lead verdict: **`REPAIR_REQUIRED`** — layers (a), (b),
(d) carry the narrow residues of §9 at their recorded scopes.

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = 2a59c1961b9bf0a1677edc43289670f67ea42442b0f1e1928f4db78cb2645c8b
(sha256 of this file up to and including the line "*Report body ends...*", i.e. of the first 22834 bytes)
