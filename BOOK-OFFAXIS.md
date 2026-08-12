# BOOK-OFFAXIS.md — Off-axis (b >= 2) sector adjudication

Mission: adjudicate the off-axis sector flagged by both external reviewers and
the BOOK-ENUM.md closing erratum. The book enumerated only all-b=1 entry
configurations; entries with b_i >= 2 propagate M = b_i down their chains and
can meet in MIXED MERGES (all mu_e >= 2, legal at m >= 3). The prime-td
multi-pole exclusion was retracted pending this adjudication.

Status: COMPLETE (2026-08-12). VERDICT: the prime-td (7/11/13) multi-pole
exclusion is NOT restored — off-axis entries survive every printed-tier
filter (23 of 27 pass L6); 2691 merge cells enumerated, 700 mixed; the
erratum's "mixed merges legal only at m ≥ 3" is corrected (false at
m = 2 off-axis). Two named missing lemmas (R1 off-axis w-law, R2
mixed-merge anatomy) would close most of the sector.

## 0. Sources consulted

- BOOK-ENUM.md: erratum (all-b=1 axis only; prime-td retraction), §1 layer-E
  (entries reuse sheet6_campaign.tdu_rows(Λ_i) filtered to global type; MP4
  pin M_i = b_i; any b_i >= 2 => off-axis class, 27 entry multisets, never
  cell-expanded; prime-td panels 100% off-axis), §6 perimeter.
- SHEET6-MULTIPOLE.md MP4 (entry pin: (deg p, deg p_g) = b(α,β), M = b;
  b = 1 forced iff Λ β-minimal or Λ prime), MP5 (M=1 propagation), MP6
  (merge anatomy; k = 0 needs some μ_e = 1), MP7 (l = 0 kill; resonant
  jumps), MP8 (budget transparency proved on the pure M=1 forest ONLY),
  line 120: mixed merges all-μ_e >= 2 obey only MP6(b)/(d) subadditivity,
  legal only m >= 3 downstream of an earlier jump.
- TEMPLATE-ATTACK.md §1a: L6 law + i-sync. SHEET6-DEPTH.md DS1 (§2).
- SHEET6-TDUNIFORM.md §1 menu / tdu_rows b-parameterization.

## 1. Entry census (b >= 2, td <= 14, L6 + MP4 pin)

Engine: cases/book_offaxis.py (reuses book_enum.entries/tdu_rows verbatim;
gate = book_enum.gate() PASS, on-axis td=6 record unchanged; MP4 sanity
PASS: prime/β-minimal Λ force b = 1 arithmetically in tdu_rows).

**27 raw off-axis entry multisets** (matches BOOK-ENUM §5 count) across
td = 6..14, m = 2..⌊td/3⌋; **23 survive the L6 pole filter**
gcd(a(α+β), ν) = 1 (≡ N1 gcd(a,ν) = 1, equivalence asserted per row).
The 4 L6 kills all share the same bad pole (2,3)-L6 a=2, b=1, ν=2
(gcd(2·5, 2) = 2 — the TEMPLATE-ATTACK "a2ν2-(2,3) dies everywhere" row):
td10 m2 L4b2+L6a2; td13 m3 L3+L4b2+L6a2; td14 m2 L6a2+L8a2b2;
td14 m3 L4b2+L4b2+L6a2.
Full surviving table with per-pole M = b and w0 in the engine output;
headline rows (M-vectors): td7 m2: [1,2]; td8 m2: [2,2]; td12 m3:
[2,2,2]; td13 m2: [2,5],[2,3],[2,1],[1,3]; td14 m2: [2,5].
Only types (2,3),(2,5),(3,5),(3,4) occur; b ∈ {2,3,5}.

### 1a. Prime-td check (td = 7, 11, 13)

**NOT emptied at entry level**: L6 survivors 1 / 3 / 6 at td = 7 / 11 / 13.
The prime-td restoration must therefore come from the chain/merge layer
(§2–§3), not the entry layer. Witness at td = 7 (m = 2):
(2,3) with Λ = (3,4), poles (a,b,ν) = (1,1,2) ⊕ (1,2,3), M = (1,2),
w0 = (2, 3/2). NOTE: every td=7/11/13 survivor with m = 2 has at least
one b = 1 pole EXCEPT none — inspect: td7 [1,2]; td11 [1,2],[1,3],[1,2,2];
td13 [1,5],[2,3],[2,1],[1,3],[1,2,1],[1,1,1,2]. Only td13 m2 (2,3)
Λ=(4,9) M=[2,3] has NO b=1 pole; all other prime-td survivors carry a
forced μ = 1 arrival (MP5), so their G* obeys full MP6 anatomy.

## 2. Off-axis chain calculus (M = b >= 2 segments)

Thesis pp. 41-45 read verbatim (sigray_full.pdf):

(a) **M-divisibility needs no M=1** (St 8.5, p. 42): F ∈ T_a^↘ ∩ V_a,
G = F°, G ∉ V_{2,a} ⟹ M_G | M_F. So down every merge-free segment the
M-value divides b_i non-increasingly, and arrivals obey μ_e | M (St 8.4,
p. 42, mult(p,c) | M_G — verbatim, no M=1 hypothesis). A b ≥ 2 chain MAY
still arrive with μ_e = 1 (any divisor).

(b) **Pattern shape** (St 3.18, used in St 8.5's proof): at a non-merge
chain vertex G ∉ V_{2,a}, p_G = ⊖(η^ν − c^ν)^l, c ≠ 0 — the l-fold
thickened ν-orbit; Prop 8.3(ii) is its l = 1 (M = 1) specialization.
DS1(a)-(d) (SHEET6-DEPTH §2) generalizes VERBATIM to l ≥ 2: the proof
uses only the root SET {ζc} (≥ 2 roots ⟹ ν ≥ 2, c ≠ 0), Not 3.4/3.5
integrality, and the characteristic-exponent descent — never simplicity.
So off-axis segment vertices ∉ V_{2,a} are still consecutive
characteristic vertices of their own pole with case-(II) edges.

(c) **The two genuine breaks**:
  (c1) V_{2,a} escape: MP5's exclusion of separating rays used M = 1
  (Cor 8.1 ⟹ G ∉ V_{2,a}; Cor 8.1 needs M_F = 1). For M ≥ 2 the printed
  record does NOT exclude segment vertices in V_{2,a} (Prop 8.2 gives
  only the conditional d_F ≤ deg(p_F)((1−v)/M + v − u) descent). Hence
  the MP8 zero-row itemization does not extend: off-axis chains can
  carry Y(F) ≠ ∅ / λ > 0 — but a POSITIVE lower bound is not printed
  either (transparency fails in both directions; see §3 budget).
  (c2) DS2 w-conservation FAILS as printed: its proof takes Prop 9.3(b)
  dp_F/dq_F = (ρ_G+n_e)/(κ̄_G+n_e) "both sides in lowest terms" via
  gcd(ν, nν+1) = 1 — for M ≥ 2 gcd(dp,dq) = M ≥ 2, the lowest-terms
  step breaks, t is determined only up to the M-fold ambiguity, and the
  M ≥ 2 chain q-shape is not printed. NO w-alphabet, NO equal-w join
  law, NO root w<1 window on off-axis chains at printed tier.

## 3. Mixed-merge cells

Engine: merge_cells/merge_census in cases/book_offaxis.py — for each L6
entry: all merge hierarchies (MP1: Σ(r−1) = m−1 automatic), all
μ-assignments (leaf μ_e | b_i by St 8.4/8.5; inner μ_e | emitted M), all
emitted M_G | Σμ_e (subadditivity — the ONLY (d)-law valid at mixed
merges, MP-REVIEW l.120), MP2 (interior G* emits M ≥ 2; G* = (0,y)
root-merge cells kept, tagged). Conservative superset: no l/ν expansion,
no non-ZCH M | r cap, no root-merge St 9.2 arithmetic.

**2691 merge cells over the 23 entries: 700 contain a MIXED (all-μ_e ≥ 2)
merge, 1991 are pure MP6-anatomy** (some μ_e = 1 at every merge — full
MP6(a)-(e) applies there). Highlights:
- **ERRATUM CORRECTION (sharpening)**: mixed merges are structurally
  available already at **m = 2** (both b_i ≥ 2, both μ_e = 2: td8 [2,2]
  5 cells; td12 [2,2],[3,3],[2,2]; td13 [2,3] 3 cells; td14 [2,5]).
  The BOOK-ENUM erratum's parenthetical "legal at m ≥ 3" is an all-b=1
  relic (there μ ≥ 2 needs an upstream jump, consuming a merge); off-axis
  it is FALSE — the gap is wider than stated, not narrower.
- Prime td: td7: 6 cells, ALL MP6-anatomy (the b=1 pole forces a μ=1
  edge at G*); td11: m=2 rows all MP6 (14 cells), m=3 row 103 cells of
  which 25 mixed; td13: m=2: 38 cells (3 mixed, all in the all-b≥2 row
  Λ=(4,9) M=[2,3]), m=3: 50 (5 mixed), m=4: 598 (78 mixed).
- Kills actually firing at this tier: MP2 (M=1 interior emission) only.
  L6 fired at entry layer (§1). No MP7-analogue exists for mixed merges
  (the l ≥ 1 forcing needs a μ=1 edge); no λ-charge is printed (§2(c1)),
  and MP8 transparency is equally unavailable — budget status of every
  off-axis cell is UNKNOWN, in both directions.

## 4. Per-td verdicts

- **td 6, 9 (all m); m=4 td 12**: off-axis sector EMPTY (0 raw entries).
  The book's panels there are COMPLETE as printed; at td = 6 the
  multi-pole story remains exactly Theorem O's residue-A cell.
- **td 7 (m=2)**: PRIME-TD EXCLUSION NOT RESTORED. One off-axis entry
  survives L6: (2,3), Λ=(3,4), M=(1,2), 6 merge cells, all with full
  MP6 anatomy (μ=1 edge forced). Closing needs the off-axis w-law
  (rider R1) — with it, the b=2 chain would carry w0 = 3/2 against the
  b=1 chain's w = 2, and the equal-w join law would kill every interior
  cell at once; the retraction stands until R1 is proved.
- **td 11**: not restored. 3 entries; m=2 cells (14) all MP6-anatomy —
  same single missing lemma R1; m=3 row adds 25 genuinely mixed cells
  (rider R2 also needed).
- **td 13**: not restored; the worst prime panel. 6 entries incl. the
  only all-b≥2 prime-td row (2,3) Λ=(4,9) M=[2,3] (its 3 mixed cells
  need R2); plus b=5 chains (Λ=10 rows) — largest per-pole M in sweep.
- **td 8, 10, 12, 14 (composite)**: off-axis cells exist and are open
  (same riders); they sit BESIDE the book's on-axis survivors, so these
  panels were open anyway — the off-axis sector adds breadth, not a
  first counterexample-channel.
- **Global**: no (m, td) panel in 6..14 is closed by the off-axis sweep
  alone; conversely NO printed-tier statement kills any of the 2691
  cells beyond MP2/L6. The sector is a true frontier, exactly as the
  reviewers flagged.

## 5. Riders / honest caveats

- **R1 (off-axis w-law)** — the single highest-value missing lemma: the
  DS2 orbit map for l-fold patterns ⊖(η^ν − c^ν)^l (M ≥ 2). Needs the
  M ≥ 2 chain q-shape (not printed; Prop 8.1(iii)-(iv) gives gcd data
  only). If w-conservation (or any computable w-evolution) holds, the
  equal-w join + κ̄-window machinery closes ALL pure-MP6 off-axis cells,
  restoring td=7 and most of td=11/13 immediately.
- **R2 (mixed-merge anatomy)**: no analogue of MP6(a)/(c)/(e) or MP7's
  l ≥ 1 forcing when every μ_e ≥ 2; only subadditivity M_G | Σμ_e is
  proved (and it kills nothing). A k=0-type root-count argument for
  μ_min ≥ 2 merges is the natural target.
- **R3 (budget silence)**: MP8 transparency does NOT extend off-axis
  (Cor 8.1's M=1 hypothesis; V_{2,a} escape §2(c1)) — but neither is a
  λ ≥ 1 charge proved. Either resolution is progress: transparency ⟹
  suffix budgets stay td−2; a charge ⟹ new kills at small td.
- **R4 (conservative superset)**: the merge census imposes no l/ν
  window, no i-sync (always solvable: segment ν-products are free
  integers ≥ 1, DS1-R1 gives no (m,td) bound), no root-merge St 9.2
  arithmetic, no P-realizability. Counts are upper-bound structure, not
  existence claims.
- **R5 (inherited)**: Prop 5.8 td = ΣΛ generic-a rider (SIGRAY-AUDIT)
  carries through the entry layer; everything here consumes it.

## Reproducibility

    cd cases && python3 book_offaxis.py    # ~1 s, exit 0

Script: cases/book_offaxis.py (additive over book_enum.py, imports its
entries/tdu_rows/set_partitions verbatim; exact integer arithmetic; no
floats). Gates, all mandatory before output: (1) book_enum.gate() —
on-axis td=6 record reproduced unchanged (PASS); (2) MP4 sanity — prime
and β-minimal Λ force b = 1 in tdu_rows (PASS); (3) L6 ≡ N1 equivalence
asserted per entry row.
