# SHEET6-TDU-REVIEW.md — Adversarial review of the TD-UNIFORM entry theorem (08fbbda)

Reviewer: Claude (adversarial pass, 2026-08-10). Status: COMPLETE.

**2026-08-28 correction.**  This dated review remains valid for the prime
entry theorem because every `M=1` kill occurs at a nonroot pole.  Its root
compatibility sentence is superseded: repaired Statement 8.5 gives only
`M_(0,y)|3`, so root `M` may be `1` or `3`; corrected Proposition 8.4 has no
root clause.  The two zero-charge survivors therefore remain unexcluded.
The chain budgets are now licensed by the reviewed actual-weight Corollary
7.1 and disjoint first-separation exit sets, not by printed equation (22).
Root/SF1 numerical completeness still awaits the root-aware AWS rerun.
Scope: SHEET6-TDUNIFORM.md + the `tduniform` stage of cases/sheet6_campaign.py
— headline claim: single-pole exclusion at ENTRY for every PRIME td (Theorem
TDU), plus the composite-residual negative (TDU-neg) and the td≤9 salvage
corollary (TDU-c). Ground truth: refs/sigray_full.pdf re-read on-page this
review (pp. 9, 19, 23-31, 39, 44-51). Engines re-run: gate PASS, tdu gate
PASS, full census td≤40, chain runs td ∈ {4,6,8,9,10,12,14,15,16} both via
the committed CLI and via an independent harness (this review, in-session,
correct namespace — see front 4).

Verdicts:
- Front 1 (b-parameterization of the leaf table): **CONFIRMED** — complete
  and exactly the printed §5 constraint set; both baselines (11 rows Λ≤6 =
  table (23) cell-by-cell, 14 at Λ≤7) reproduce; td = abαβ/ν re-derived
  from (19)/(20).
- Front 2 (pinned M = b, td-uniform): **CONFIRMED** — all four pin
  ingredients re-read on-page; NOTHING before §9 (p. 45) mentions td or Λ;
  gcd(bα,bβ) = b exact; Prop 8.4 applicability td-free.
- Front 3 (prime-td menu completeness): **CONFIRMED** — divisibility
  argument re-derived from scratch; case (B) empty, ν=1 impossible, α=1
  illegal by St 2.1 (p. 9) AND moot (would still be b=1 → M=1 → dead).
- Front 4 (scan td≤40 + hand rows): math **CONFIRMED** (census identical,
  all 11 primes live=0, 6 rows hand-verified) — but the committed
  reproduction path is **REFUTED**: an IIB_DERIVED namespace bug silently
  disables the promoted AF2-IIb pricing in the `tduniform` CLI, so
  `--td N` prints 31/41/60 at td=8/9/10 instead of the sheet's 16/16/23.
  Every printed chain number (0/4/16/16/23/71/48/87/212 + frontier) DOES
  reproduce once the flag is set in the module hiii_compose actually reads.
- Front 5 (td=9 slack-6 chain): **CONFIRMED** — re-derived by hand end to
  end; no missed kill in the promoted arsenal; Σλ=0 is untouchable by any
  budget-side sharpening. Correction: the td=9 book has TWO Σλ=0 survivor
  classes, not "one" (§4) — the negative is slightly STRONGER than stated.
- Front 6 (perimeter honesty): **CONFIRMED, list incomplete** — no hidden
  H5/E5/AF2/H3 in the entry-death argument (H5a correctly quarantined to
  item 4); but the §6 statement list omits three H1-tier ingredients it
  actually uses (p. 9 type facts; the Not 6.1/St 6.1 searrow glue;
  St 3.16 for deg p_F ≥ 2).

**NET: Theorem TDU SURVIVES adversarial review** — single-pole
configurations at every prime td die at entry, on the AF3/H1-tier
perimeter (with the §6 list enlarged per front 6; same trust tier, no new
hypotheses). TDU-neg also survives: the composite residual is real,
growing, and budget-immune (the Σλ=0 exhibit is engine-independent). The
one genuine defect is an ENGINE bug (front 4): the committed CLI does not
apply the promoted kill set, so the repo's reproduction commands print
weaker-kill numbers at td ≥ 8; the printed tables are the correct
promoted-set values (independently reproduced this review). Since the
buggy path only UNDER-kills, no printed positive claim is inflated by it.

## 1. Front 1 — the leaf-table parameterization, re-derived on-page

- **(R1) completeness of the (a,b) split.** St 5.2(i) (p. 26, verbatim):
  deg(p_F)/deg(p_g,F) = D_F/D_g,F = α/β. With gcd(α,β) = 1 (Not 2.4(ii),
  p. 9): D_F·β = D_g,F·α ⟹ α | D_F ⟹ (D,Dg) = a(α,β); identically
  (P,Pg) = b(α,β). No pair with ratio α/β escapes: the factorization is
  COMPLETE, and a,b are independent (table (23) rows 3 vs 4 realize (2,1)
  and (1,2)).
- **(R2)** = St 5.2(ii) verbatim (proof from Prop 5.4 + Prop 5.3, p. 26).
  Derived gcds check: ν | bβ−1 ⟹ gcd(ν,b) = gcd(ν,β) = 1 (case A), dual
  in case B. ν ≤ β since ν | α or ν | β and α < β.
- **(R3)** Prop 5.6 (19) p. 27: Λ = D_g,F·deg(p_F)/ν = aβ·bα/ν; Prop 5.8
  (20) p. 28: td = Σ_{T_a,pole} Λ ⟹ single pole: td = abαβ/ν exactly.
  Integrality automatic (ν | α or ν | β). **(R4)** Prop 5.7 p. 27: Λ ≥ β
  (proof re-read: both ν-cases).
- **No missing constraint**: pp. 25-28 re-read; Prop 5.3(v)/(vi) and
  Prop 5.4 constrain PATTERNS (squarefree, no common roots, ν-orbit
  forms), not the multiplicity data. The sheet's "no other constraint
  printed in §5" is accurate.
- **Sweep exactness** (tdu_rows): β ≤ td (R4), b ≤ td/α (Λ ≥ abα ≥ bα
  since ν ≤ β, a ≥ 1), ν ≤ β, a = td/(bαβ/ν) forced — enumeration
  complete, not just a sample. Gate re-run: tdu_rows == prop91 slices
  td = 3..7 (so 11 rows at Λ≤6 = table (23), 14 at Λ≤7 — the +3 are the
  prime menu {(2,7),(3,7),(6,7)} = divisors of 6, matching CAMPAIGN §1).
  All 11 rows of (23) hand-checked against (a,b,ν): a-values
  (1,1,2,1,1,1,1,1,1,1,1), b-values (1,1,1,2,1,1,1,3,2,1,1), every
  ν-congruence and Λ = abαβ/ν verified by hand this review.
- Citation nit: §1 credits "Not 2.4 + Lemma 2.1" for 2 ≤ α < β; the
  direct print for α,β ≠ 1 is **St 2.1 (p. 9)** (from Lemma 2.1(iv));
  α < β is Lemma 2.1(ii)+(iv) (k_f ≤ k_g, k_g/k_f ∉ ℕ*).

## 2. Front 2 — the pin at every td: no hidden td-dependence

All four ingredients re-read on-page hunting for Λ/td restrictions:
- Not 8.1 (p. 39): M_F := gcd(deg p_F, deg p_{h_0,F},…,deg p_{h_m,F}) —
  pure definition, any F ∈ T_a. No td.
- Prop 4.2 (p. 19): stated for arbitrary F ∈ T_a^+; h_0 = g by fiat;
  m_F ∈ ℕ intrinsic. No td.
- Prop 5.1 (pp. 23-24): stated for arbitrary P ∈ R̄_a \ R_a of an
  arbitrary normalized counterexample; proof (monotone ρ, St 3.10/3.11/
  3.18 + Prop 4.1 "(8)" — E8 cite-slip stands as filed) is degree-free.
  No td.
- Prop 8.4 (p. 44): arbitrary normalized counterexample + T_a,pole = {G};
  proof (characteristic sequence to (0,y), Prop 8.3 induction, k=1
  Bezout, Thm 6.1) — no td. The FIRST Λ-bound in the thesis is Prop 9.1
  (p. 45).
With m_F = 0 at pole vertices (Prop 5.1(i) via Not 5.1/5.2), the family
is {g} and M_F = gcd(bα, bβ) = b·gcd(α,β) = **b** — exact, every td.
Applicability of the kill AT the pole vertex (G ∈ T_a^↘ ∩ V_a) rides the
A3L1-REVIEW glue (d_F + d_g,F = 1−u, d_g,F > 0, deg p_F ≥ 2 by
5.3(iv)+St 3.16, vs Not 6.1 p. 29) — re-checked: also td-free. The
engine asserts gcd(P,Pg) = b on every row (tdu_entry_nodes line 648);
ran clean over all td ≤ 40 (605 rows).

## 3. Front 3 — prime-td menu: the divisibility argument, independently

Let td = p prime, Λ = abαβ/ν = p.
- Case (A) ν | α: write α = να′; then a·b·α′·β = p with all factors in
  ℕ*. β ≥ 3 (α ≥ 2 by St 2.1, α < β, coprime) divides a product equal to
  a prime ⟹ β = p and a = b = α′ = 1, i.e. ν = α; remaining congruence
  ν | bβ−1 = p−1. Menu: {(α,p) : α | p−1, 2 ≤ α < p, ν = α, a = b = 1}. ✓
- Case (B) ν | β: β = νβ′, a·b·α·β′ = p; α ≥ 2 ⟹ α = p, a = b = β′ = 1,
  ν = β > α = p; but ν | bα−1 = p−1 with 0 < p−1 < ν — impossible. EMPTY. ✓
- ν = 1 (the A∩B overlap): abαβ = p with α ≥ 2, β ≥ 3 — impossible. ✓
- **α = 1 edge** (the front's danger case): NOT a legal row — St 2.1
  (p. 9): "the type (α,β) satisfies α ≠ 1 and β ≠ 1". Robustness bonus
  (this review): even admitting α = 1, case (A) forces (1,p) ν=1 b=1 and
  case (B) forces (1,νp) b=1 — all with M = b = 1, still entry-dead. The
  prime THEOREM does not hinge on the α ≥ 2 convention; only the exact
  menu statement does.
- Every menu row has b = 1 ⟹ M = 1 ⟹ Prop 8.4 contradiction. Engine
  gate asserts the closed form for the 11 primes ≤ 40; hand-counted
  divisor menus at p = 11,13,17,23,29,31,37 ({2,5,10}, {2,3,4,6,12},
  {2,4,8,16}, {2,11,22}, {2,4,7,14,28}, {2,3,5,6,10,15,30},
  {2,3,4,6,9,12,18,36}) match the census row counts 3/5/4/3/5/7/8 exactly.

## 4. Front 4 — the scan: census CONFIRMED, reproduction path REFUTED

- **Census** (`tduniform --tdmax 40`, re-run): the §3 table reproduces
  IDENTICALLY — rows/pin-dead/N1-dead/live for all td ∈ [3,40]; every
  prime live = 0; every composite ≥ 4 live ≥ 1. The §2 β = bα−1
  construction re-derived (gcd(α,bα−1) = 1, β > α, ν = β trivially
  satisfies (B), a = 1 passes N1) and matched to concrete rows
  ((2,3)a1b2nu3@4, (2,13)a1b7nu13@14).
- **Hand rows** (independent of engine): primes as in §3 above; composite
  (3,4)a1b3nu4@9: ν=4|β, 4|bα−1=8, Λ=9, M=gcd(9,12)=3=b, Q=(3,9,4,3,7),
  ρ=1/3 ✓; (2,13)a1b7nu13@14: 13|13, Λ=14, M=7, κ̄=15 ✓; (2,3)a1b2nu1@12:
  ν=1, Λ=12, M=2, κ̄=5 ✓ — all exactly the engine's entries.
- **THE BUG.** tdu_scan/tdu_bash set `globals()['IIB_DERIVED'] = True`
  (sheet6_campaign.py lines 664, 702). Under `python3 sheet6_campaign.py
  tduniform …` the script runs as `__main__`, while hiii_compose does
  `import sheet6_campaign as sc` — a SECOND module object. `sc.step`
  (line 249) reads the module copy's IIB_DERIVED = False: the promoted
  AF2-derived IIb pricing is OFF in the committed CLI path. Measured:
  CLI gives td=8: **31**, td=9: **41**, td=10: **60** survivor classes
  vs the sheet's 16/16/23. Setting the flag on the imported module
  (`import sheet6_campaign as m; m.IIB_DERIVED = True` before importing
  hiii_compose) reproduces the ENTIRE printed table: 0/4/16/16/23/71/48/
  87/**212** at td = 4/6/8/9/10/12/14/15/16, with frontier 0/0/0/0/0/1/
  0/2/**6** — byte-for-byte the sheet's §4 numbers, td=16 included.
  One-line fix: replace the globals() calls with
  `sys.modules.setdefault…`-style assignment on the module hiii_compose
  reads (or set `hcmp.sc.IIB_DERIVED = True`). Legacy paths
  (`hiii_compose.py pin`/`iib`) are UNAFFECTED (there hiii_compose is
  `__main__` and sets `sc.IIB_DERIVED` on the unique imported copy) —
  the sheet's "existing stages untouched" is true; the NEW stage is the
  broken one, so §9's "chain counts re-run … all IDENTICAL" can only
  refer to in-session runs, not the committed commands.
  Direction of error: the bug only under-kills (prices drop), so no
  printed survivor count was deflated; the residual-growth conclusion
  holds under either pricing.
- **Step-1 claim re-verified with pricing ON** (this matters: with IIb
  priced, free steps could vanish): 298 live entries at td ≤ 40, every
  one retains a λ = 0 first step (all IIa_0 cells, M_F ≥ 2). CONFIRMED.
- Aggregation note: the §4 "opens" column counts per-entry open KINDS
  summed over entries (td=12: 4, td=15: 6); globally deduplicated kinds
  are 3 resp. 3 — no contradiction, just a definition to keep in mind.

## 5. Front 5 — the td=9 Σλ=0 chain: no missed kill

Re-derived by hand, then confirmed against the fixed-namespace engine:
- Entry legality: type (3,4) (gcd 1, 2≤3<4), case (B) ν=4|β=4 with
  4 | bα−1 = 8; Λ = 1·3·3·4/4 = 9; pin M = gcd(9,12) = 3 = b; N1
  gcd(a,ν) = gcd(1,4) = 1; Q = (D,P,ν,M,κ̄) = (3,9,4,3,7), ρ = 1/3.
- The step (μ=3 | M ✓ St 8.4; IIa_0, l=1): dp = μν_F = 12, dq =
  (l+1)ν_F+1 = 9; n0 = (−7) mod 4 = 1, m = 1 ⟹ n = 5; ratio check
  12/9 = 3(1/3+5)/(7+5) = 4/3 exact; κ_F = (7+5)/4 = 3 ∈ ℕ; M_F =
  gcd(12,9) = 3 ≠ 1 (pin at child ✓); child N1: gcd(3,4) = 1 ✓; λ = 0
  (k = 0: all p-roots in the descending orbit; the extra q-orbit is
  priced by NOTHING in AF2 — p-directions only, St 3.18 — and is the
  thesis's own printed λ=0 move 9.6(v)).
- Terminal IV at (1/3, 4, 3, 3): (j) 3 < 4; (k) den = ρ+ν−κ = 4/3 > 0,
  d_F = P/R = 12/3 = 4 ∈ ℕ; (l) R = ν/den = 3 > 1; (m) M/R = 1 ∈ ℕ*;
  ψ = ⌈R⌉−1 = 2; (25): Σλ = 0 ≤ 9−1−2 = 6. SLACK 6. Engine
  (iv_dispositions) agrees: SURVIVOR, R = 3.
- Kill-hunt (all promoted weapons tried): pin ✓ passed, μ|M ✓, N1 ✓ at
  both vertices, AF2-IIb inapplicable (no IIb step), E5-III inapplicable
  (no III step), ψ-upgrade to any ψ ≤ R = 3 still leaves 0 ≤ 5, and repaired
  St 8.5 gives `M_(0,y) in {1,3}` — both satisfiable; corrected Prop 8.4 is
  unavailable at the root. A Σλ = 0 chain is
  immune to EVERY budget-side refinement; the sheet's "budgets are a
  small-td weapon" mechanism (κ̄ = a(α+β) independent of b, IIa_0
  κ-collapse free) is correctly diagnosed.
- CORRECTION: the fixed td=9 book contains **two** Σλ=0 survivor
  classes — (1/3,4,3,3)@0 and the s-family (2/3,3s+2,3,2s+2)@0 (the
  AF3-class-3 shape, here reached spend-free) — §4's "one at Σλ=0"
  undercounts its own exhibit. Strengthens TDU-neg.
- TDU-c's mechanical basis re-verified: td ∈ {4,6,8,9} runs (pricing ON)
  give opens = 0, frontier = 0, all survivors ψ-consistent IV terminals
  (0/4/16/16) — so an H3-strong root lemma would indeed close td ≤ 9;
  td = 10 already has 1 open kind (parametric III-E5), td = 12 adds
  frontier — the "fails at td ≥ 10 even conditionally" line is right.
  SF1 caveat correctly inherited.

## 6. Front 6 — perimeter audit of Theorem TDU

- The §6 list (Prop 4.2, 5.1, 5.3-5.8, St 5.2, Not 5.2/5.3/8.1, Prop
  8.4) covers the pin + table + kill. It OMITS three things the argument
  uses, all H1-tier prints or promoted review-glue:
  (i) Not 2.3/2.4 + Lemma 2.1 + St 2.1 (p. 9) — type well-defined,
  gcd(α,β)=1, 2 ≤ α < β: load-bearing for the exact prime menu (§3);
  (ii) Not 6.1/St 6.1 (p. 29) + the pole-vertex-searrow glue (A3L1
  §1) — needed for Prop 8.4's hypothesis F ∈ T_a^↘ ∩ V_a;
  (iii) St 3.16 (deg p_F ≥ 2 inside that glue). Recommend adding these
  to the theorem's stated perimeter. Same trust tier — no downgrade.
- No hidden H5/E5: mechanically, n1_dead = 0 at every prime td ≤ 40 (the
  census column) — the prime kill NEVER consults N1; item 4 is the only
  H5a use and is flagged. AF2/E5/H3/budgets appear only in TDU-neg and
  TDU-c, which carry the heavier standing-hypothesis stack explicitly.
  The "NO H2" claim: St 9.1/Prop 9.2 (the E9-afflicted Y(F)/entry
  neighborhood) are NOT needed for items 1-3 (the kill fires at the pole
  vertex directly) — correctly excluded, though §1's Q-datum exposition
  cites them (expository only).

## 7. Corrections banked

- **C1 (engine, must-fix)**: IIB_DERIVED namespace split in
  tdu_scan/tdu_bash (sheet6_campaign.py:664,702) — the `tduniform` CLI
  runs the chain layer WITHOUT AF2-IIb pricing; committed reproduction
  commands print 31/41/60/… at td ≥ 8 instead of the sheet's numbers.
  One-line fix; all printed numbers verified correct for the PROMOTED
  set via fixed-namespace reruns (this review).
- **C2 (sheet §4)**: "16 (one at Σλ = 0)" → two Σλ=0 classes at td=9.
- **C3 (sheet §9)**: "chain counts re-run … all IDENTICAL" — true only
  in-session; the committed CLI cannot have produced them (C1).
- **C4 (sheet §6)**: perimeter list += St 2.1/Not 2.4/Lemma 2.1 (p. 9),
  Not 6.1/St 6.1 (p. 29), St 3.16 (p. 17) — front 6.
- **C5 (sheet §1, cosmetic)**: "Lemma 2.1 ⟹ 2 ≤ α" — the print is
  St 2.1; Lemma 2.1(iv) is its proof.
- E8/E9 (thesis errata) re-confirmed as filed in AF3; no new thesis
  errata found on the pages re-read.

## 8. Reproduction

    cd cases && python3 sheet6_campaign.py gate            # PASS
    python3 sheet6_campaign.py tduniform --tdmax 40        # census: OK (bug-free layer)
    python3 sheet6_campaign.py tduniform --td 9            # WRONG (41): C1 bug
    # correct chain layer until C1 is fixed:
    python3 -c "import sheet6_campaign as m; m.IIB_DERIVED=True; \
                # ... BFS as in tdu_bash (see /tmp harness, this review): td9 -> 16"

Exact arithmetic throughout; pdf pages cited = printed pages.
