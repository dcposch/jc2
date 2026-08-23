# SHEET6-DEPTH-REVIEW.md — Adversarial review of SHEET6-DEPTH.md (2c81954), the Chain-Depth Closure Lemma

Reviewer: Claude (adversarial deep-dive, 2026-08-12). Status: COMPLETE.
Scope: the keystone conservation law w := (κ̄ − ρ)/ν and everything hung on
it — DS1 (characteristic rigidity), DS2 (step law), DS3 (resonance budget),
DS4 (menu factorization), the Lemma (§6), the restored finite book (§8) —
re-derived from the printed record independently, case branch by case
branch, plus the SIGRAY-AUDIT interaction and adversarial machine
extension. Ground truth: refs/sigray_full.pdf re-read on-page this session:
pp. 10–18 (Defs 3.1–3.4, Not 3.3–3.5/3.10/3.13, St 3.16–3.18, Props
3.1–3.2), pp. 39–42 (Not 8.1, Prop 8.1, St 8.2–8.4), pp. 48–52 (Not 9.1,
St 9.1–9.2, Props 9.2–9.3(a)–(m), St 9.6 + proof). Engines re-run:
cases/depth_closure_check.py (13/13 PASS, exit 0), cases/twopole_check.py
l1only (byte-match: 26 pre-merge shapes, 18427/17199/601/276 merge ledger,
RESIDUE child (1/2, 3, 2, 5) at **351 parent pairs** — the 351/351 claim
reproduces). Independent adversarial checker: /tmp/depth_adv.py + inline
sweeps (entries to w₀ = 720 and gen(W) = 4, fractional w to denominator 12,
boundary w = 1, w < 1, w < 0, depth ≤ 12, caps ν ≤ 30, n ≤ 10; full menus
including the I-family cells the doc's `jumps()` filter excludes).

Verdicts:
- Front 1 (conservation law): **CONFIRMED** — re-derived from printed
  Prop 9.3(a)–(h),(i)–(m); every case branch classified; the ONLY
  w-drifting branch is case (III), and the lemma quarantines exactly it
  (§1 below); i-normalization consistent with MP/engines (§1c).
- Front 2 (characteristic-vertex claim vs SIGRAY-AUDIT): **CONFIRMED under
  the audit's forced readings** — DS1 uses precisely the jump/max κ_F that
  St 3.8 forces, Not 3.4's audit-proved P-independence, and the p_{f−a}
  reading of St 3.16 (§2).
- Front 3 (menu-through-w factorization): **CONFIRMED** — handshake and
  join re-derived; no book datum escapes (w, cell); the per-edge (l, n_e)
  reach data are state-dependent existence certificates, not book data,
  and the doc says so (§3).
- Front 4 (d₀ = gen(W)+2): **STATEMENT VERIFIED THROUGH gen 4 WITHIN CAPS;
  PRINTED PROOF INCOMPLETE** — the §6(⊆) replay sketch supports only
  d₀ ≤ 2·gen+2; the sharper gen+2 is empirically tight at gen 3 and never
  violated (§4). One substantive fix owed; finiteness and td = 6 unaffected.
- Front 5 (mechanical): **CONFIRMED + EXTENDED, no violation found** (§5).
- Front 6 (final book spec): **DELIVERED** (§6).

Net: **the lemma STANDS** (claims 1, 2, 3, 5, 6 at their stated tiers;
claim 4's constant stands machine-verified with its proof owing one
repair, safe fallback 2·gen+2). The finite-book restoration (§8) stands.

---

## 1. Front 1 — the conservation law, re-derived branch by branch

### 1a. The step arithmetic (case II), independent re-derivation

Printed Prop 9.3 (p. 50), edge G = F + c with G the upper vertex (chain
parent), F = G° the child; case (II) equations, i-normalized with
deg(p_G) = i_F (transport, §1c):

    (b)  dp_F/dq_F = (ρ_G + n)/(κ̄_G + n)     [LHS reduced, in lowest terms]
    (c)  D_F = (D_G + n·deg p_G)/ν_G  ⟹  ρ_F = (ρ_G + n)/(ν_G ν_F)
    (d)  κ̄_F = (κ̄_G + n)/ν_G

With (dp, dq) = (ν_F, n_Fν_F + 1) coprime, (b) forces ρ_G + n = tν_F,
κ̄_G + n = t·dq_F, t = (κ̄_G − ρ_G)/Δ_F = ν_G w_G/Δ_F (no integrality of t
needed — re-checked). Then κ̄_F = t·dq_F/ν_G, ρ_F = t/ν_G, and

    w_F = (κ̄_F − ρ_F)/ν_F = t(dq_F − 1)/(ν_G ν_F) = t·n_F/ν_G
        = w_G · n_F/Δ_F.        ∎  (matches §3 of the doc exactly)

n_F = 1 ⟹ Δ = 1 ⟹ w fixed; n_F, ν_F ≥ 2 ⟹ Δ ≥ 2n_F − 1 ⟹
n_F/Δ_F ≤ n_F/(2n_F−1) ≤ 2/3, maximum at (n,ν) = (2,2). Contraction
constant CONFIRMED. DS3's divisibility: κ̄_F = a·dq_F/(bΔ_F) ∈ ℤ
(DS1(c)), gcd(Δ_F, dq_F) = gcd(Δ_F, ν_F) = 1, hence Δ_F | a — re-derived,
correct (Δ | a needs only gcd(Δ, dq) = 1, independent of b). Ranges
ν ≤ a−1, n ≤ (a+1)/2, num contraction ≤ 2/3, resonant-count
< log_{3/2}a₀ + 1: all re-checked.

### 1b. Case coverage: where each printed branch can occur, and its w-law

The Prop 9.3 case split classifies the LOWER vertex F of the edge (the
upper vertex sits at α_j of the proposition's P). Complete table, each
w-law re-derived here from the printed equations:

| case | equations | w-law (i-normalized, μ = 1) | where it occurs in the lemma |
|---|---|---|---|
| (I) F ∈ V₂ₐ\V₁ₐ | (a)–(d) | handshake κ̄_m − D/i = w_e | I-family (ν = 1) merges only — a segment CHILD has ν_F ≥ 2 ⟹ V₁ₐ (DS1b), so (I) cannot occur inside a segment |
| (II) F ∈ V₁ₐ, u = α_{j−1} | (a)–(d) | w_F = w_G·n/Δ (chain); handshake w_e (merge) | every within-segment edge (DS1d); every non-0 merge edge |
| (III) F ∈ V₁ₐ, u > α_{j−1} | (e)–(h), ν := ν_F | **w drifts: κ̄_m − D/i = ν_e·w_e** (equivalently a chain-shaped (III) step would give w_F = ν_G·w_G·n/Δ — re-derived here from (g),(h)) | ONLY the ZCH 0-edge (§5c): the 0-direction pole has coefficient 0 at π(G_m), so π(G_m) is off its support, hence not characteristic — (III) forced. Inside a segment (III) is excluded by DS1(d) |
| (IV) F = (0,y) | (i)–(m) | n* = ν_e − κ̄_e forced; handshake w_e = 1 − l_f/i₀ < 1 | root merges only (§5d) |

So the single case whose step law breaks conservation is (III), and the
lemma's §5c is precisely the correction that moves the engine's 0-edge
from (a)–(d) to (e)–(h). The exclusion of (III) from segments is DS1(d),
whose lattice argument I re-derived independently: exponent lattices below
u are generated-subgroup objects, hence branch-independent as rationals;
all exponents of P_i strictly below u = π(F_j) lie in L = (e′_{j′−1}/κ′)ℤ
while u ∉ L; c_u(P_i) ≠ 0 (orbit has no 0 root + Prop 3.1(**)); so u is
exactly P_i's next characteristic exponent; consecutiveness from Not 3.3
(F° skips no V_a vertex) + Def 3.4 (characteristic values are V_a
vertices). Moreover the argument is P-robust: whichever P Prop 9.3
supplies with v = α_j(P), P agrees with P_i strictly below v, so u is
characteristic and consecutive for THAT P too — the (II)-classification
does not depend on the proposition's unstated choice of P. DS1(d) is
correct and stronger than it advertises.

DS1(a)'s orbit-parameter identification (MP5's ν IS ν_F) is grounded:
St 9.6's printed proof (p. 52, re-read) says "p(η) = ⊖(η^ν − c^ν) for
some ν = ν_F" — the identification is the thesis's own, carried by
promoted MP5/D5(d). DS1(b): Not 3.4's contrapositive, sound. DS1(c):
κ_F π(F) = β′_{j′}/e′_{j′} ∈ ℤ by Def 3.1(ii) — re-checked (e_j | β_j and
e_j | κ both from Def 3.1). Entry edges from ν = 1 pole vertices (Prop
5.5(i), V₂ₐ) are honestly quarantined to bare H1 in §9 — correctly so:
DS1(d) does not cover them (the pole vertex need not be characteristic);
the engine's promoted entry-step model is what is used, and every entry
edge in the promoted record conserves w (check 6).

### 1c. Normalization audit vs MP5/MP6 and the engines

- ρ := D/deg(p_full) = (D/i)/deg(p_red) (Prop 8.1(i): p_full = ⊖(ξ^δ
  p_red)^i, deg p_full = i·deg p_red — on-page). The engine's residue
  child (ρ, ν, M, κ̄) = (1/2, 3, 2, 5) has D/i = 3, dp_red = 6, ρ = 1/2:
  SAME convention. MP-REVIEW §5c's layer-J equation dp/dq =
  μ_e(ρ_e+n_e)/(κ̄_e+n_e) restricts at μ_e = 1 to the (b) form used here:
  no DEPTH↔MULTIPOLE mismatch. Check 5's ρ = (6s+3)/(4s+2) reads St
  9.6(v)'s printed Q with full degrees: consistent.
- Transport deg(p_parent) = i_child·μ_e: St 3.17(i) (deg p_{G+c} =
  mult(p_G, c), upper-from-lower) + Prop 8.1(i) + St 8.4 (μ_e | M_upper,
  = 1 on M≡1 ancestry) — all three re-read on-page; this is MP6(b) at
  chain edges, exactly as claimed. It is what closes (b) in ρ, and it is
  the only place the "conservation" could have been faked by a
  normalization slip — it is not: St 9.6's proof itself computes
  i = deg(p_G)/M_G = j in the μ = M_G case, confirming the reading.
- Cosmetic: §1 of the doc writes edges as "F = G + c (F above G)"
  (Prop 3.2/St 3.17's naming) while §3 and Prop 9.3 use G = F + c with G
  above. Each is faithful to its cited source; a one-line convention note
  would prevent misreads. No error.

## 2. Front 2 — survival under SIGRAY-AUDIT's forced readings

| audit item | audit verdict | what the lemma uses | survives? |
|---|---|---|---|
| Not 3.4 (ν_F) | VERIFIED; P-independence PROVED by audit | DS1(b): ν_F ≥ 2 ⟹ F ∈ V₁ₐ needs only well-definedness of the decoration | YES — the audit result is exactly sufficient |
| Not 3.5 (κ_F) | GAP = H5a; jump/max reading FORCED (via St 3.8) | DS1(c) evaluates κ_F at F = I_{P′}(α′_{j′}) as κ′/e′_{j′} — the JUMP value | YES — at a V₁ₐ vertex the max-over-branches equals the jump value: branches realizing u characteristically share e′_{j′}/κ′ = gcd-lattice of (e′_{j′−1}/κ′, u) (rational, branch-free); non-jumping branches give the coarser (smaller) κ/e_{j−1}. Re-derived here. Prop 9.3's proof-internal κ_F = κ_G/ν_G is the same-branch jump-value relation — H5a-consistent |
| St 3.8 (D ∈ ℤ) | ERRATUM; corrected version proved by audit under forced reading | not cited by the doc; NEEDED implicitly for κ̄_m ∈ ℤ at case-(I) merges (§5b window) via St 9.1 (κ̄ = D_f + D_g on T_{a,pole}) | YES with a filing fix (§7 item 2); at V₁ₐ vertices DS1(c) re-derives integrality independently |
| St 3.16 | VERIFIED_WITH_NIT (p_{f−a} reading) | DS1(a) iff + orbit shape; Prop 3.1(**) root/continuation dictionary | YES — the lemma computes with the corrected p_{f−a} reading throughout (campaign standard; patterns are the f−a fiber patterns) |

Additional check: the audit's Def 3.4 nit ("u = α_{j,P}, j ≥ 1 forced")
does not touch DS1 (all uses have j′ ≥ 1 since ν = e_{j′−1}/e_{j′} ≥ 2
presupposes a genuine characteristic index). No use of the audited-GAP
St 6.2 "in particular" clause anywhere in the doc. Front 2 is clean.

## 3. Front 3 — the factorization, hunted for leaks

- Handshake: from (c)+(d) i-normalized, κ̄_m − D_m/i = (κ̄_e − ρ_e)/ν_e =
  w_e in one line — re-derived; cell-independent as claimed. Join =
  common (κ̄_m, D_m/i) ⟹ common w (subtraction); conversely same (w,
  cell) ⟹ same child datum w·(dq_c, dp_c, 1)/Δ_c (two linear equations).
- §5b windows re-derived: dq_c ≤ (r+1)Δ_c holds in all three families for
  l ≥ 1 (IIa: r(lν+1−ν) ≥ 0; ZCH: rν(l−1)+ν−1 ≥ 0; I: r(l−1) ≥ 0), so
  κ̄_m ∈ (w, (r+1)w] ∩ ℤ; the three ν-determination identities re-derived
  (IIa: ν(wr − Di·l) = Di; ZCH: ν(l·Di − w(r−1)) = w; I: l = wr/Di).
  Finite per (w, r) as claimed. Cascade map w ↦ w(r+l)/(lν+1)
  (ν-independent = r·w at l = 0) re-derived; composed ≤ m−1 times by MP1.
- The hunt: MP-REVIEW §5a's per-edge bounds (n_e ≤ (rκ̄_e −(r+l)ρ_e −1)/l
  etc.) are NOT functions of w alone — they depend on (κ̄_e, ρ_e), i.e.
  the frame state. Verdict: these are existence certificates for
  reachability, not book data; every datum the book records — (family,
  ν_c, l, M, κ̄_m, D_m/i, child frame) — is (w, cell)-determined, and the
  doc's §5a parenthesis flags the state-dependence explicitly, deferring
  it to §6. l's range per (w, r, κ̄_m) is w-determined by the window +
  determination equations; l's realizability per frame is not, and need
  not be. M = gcd(dp_c, dq_c): cell-determined. r ≤ m: layer T. μ_e = 1:
  forced. i, l_f, coefficient solves: instance/coefficient layer, outside
  the pattern book by design. NO LEAK FOUND. Machine cross-check: closed
  form Menu(w) ⊇ every swept frame menu at every reached frame, all
  entries incl. adversarial (§5).
- ZCH correction (§5c): re-derived from (e)–(h); the corrected handshake
  ν_e·w_e and the join filter "w's in integer ratio ν_e ≥ 2" are exact
  consequences; the case-(III) classification of the 0-edge is proved,
  not assumed (0-coefficient at π(G_m) ⟹ off-support ⟹ non-
  characteristic; V₁ₐ membership from ν_m ≥ 2; u > α_{j−1} strict by
  descent-consecutiveness). Check 7's model matches (n = n′ν_m ∈ ℕ*).
- Root (§5d): (k) is (c) with n forced to ν_e − κ̄_e; (j) ⟺ n* ≥ 1;
  handshake 1 − D/i = w_e re-derived; w < 1 NECESSARY for root merges —
  confirmed, with one directionality nit in §8(iii) (see §7 item 3).

## 4. Front 4 — d₀ = gen(W)+2: the one real flaw

gen(W) = number of BFS generations of the arithmetic closure W(w₀) under
w ↦ w·n/Δ, Δ | num(w), Δ ≥ 3. The 2/3 constant: confirmed (§1a). W
finite: confirmed (numerator strictly divides-and-contracts). Claim 1
(finite alphabet) and claim 2 (menu ⊆ Menu(W), finite) are PROVED at the
stated tier. Claim 3's (⊆) direction — every deep menu item realized by
depth d₀ = gen+2 — has an incomplete printed proof:

- The replay argument compresses a deep path to its resonant steps plus
  "one l = 0 step". But resonant-step admissibility from a resonant child
  (w′, ν_F, n_F) — and even l = 0 admissibility from it — requires
  n_F | w′ (for integer w′: n_e = ...− w′/n_F ∈ ℤ). When n_F ∤ w′ the
  state is a dead end (fine); when n_F | w′ an interposed l = 0 step may
  still be needed before the next resonant step (positivity
  n_Fν_Fν′ > Δ′ can fail from the raw resonant child). The argument as
  written therefore proves realization by depth ≤ 2·gen+2, not gen+2.
- Adversarial machine hunt (this review): entries at w₀ = 8, 12, 16, 24,
  27, 30, 36, 60, 64, 105, 128, 147, 149, 173, 203, 210, 405, 512, 720
  (gen up to 4), fractional w₀ ∈ {3/2, 4/3, 7/4, 25/12, 19/9}, depth
  ≤ 10, caps ν ≤ 30, n_pat ≤ 10, first-appearance depth recorded for
  EVERY cell (jump cells, I-family, M = 1 cascade cells — the doc's
  checker only tracks `jumps()`): **maximum first-appearance depth never
  exceeded gen+2, and attains it** (maxFirst = 5 = gen+2 at w₀ = 405 and
  512, gen 3; maxFirst = 4 = gen+2 at w₀ = 128, gen 2). Step laws held on
  every edge (0 violations across ~10⁴ edges); reached w-sets ⊆ W(w₀)
  always.

Verdict: the CONSTANT gen+2 is true in every instance examined and tight;
its proof is not complete as printed. Required fix (§7 item 1): either
restate d₀ ≤ 2·gen(W)+2 (which the doc's own argument proves, and which
changes nothing downstream — finiteness, menu content, W, and td = 6
(gen 0, both give 2) are d₀-insensitive) — or supply the missing chaining
lemma. Caveat inherited from the doc's §9 (correctly flagged there): the
empirical d₀ verification is cap-limited; the menu CONTENT conclusions
are cap-free via §5b.

## 5. Front 5 — mechanical verification and extension

- depth_closure_check.py: 13/13 PASS re-run, exit 0. The checks verify
  what they claim: (1) per-edge law W/D/contraction on every BFS edge;
  (2) the td = 6 record incl. menu constancy 1–12 and the exact two-cell
  pre-suffix menu; (3+4) 10 real (m=2, b=1, td ≤ 12) entries, closure
  containment, stabilization at gen+2 vs depth 8, closed-form superset;
  (5) St 9.6(v) w ≡ 3/2 (re-derived by hand here as well: w =
  3(2s+1)²/(2(2s+1)²) = 3/2 identically); (6) all 26 promoted phase-4
  shapes have w = 2 at every instance; (7) the corrected case-(III) ZCH
  solve: 403 cells, none joinable at W = {2}.
- Entry-list note: check 3's entry generator imposes (α ≡ 0, β ≡ 1) or
  (β ≡ 0, α ≡ 1) mod ν — this is the pole q-shape pin dq ≡ 1 (mod ν) at
  b = 1, and it forces w₀ ∈ ℤ on the whole M=1 axis; fractional w enters
  only through m ≥ 3 cascade children. Consistent, worth a comment line.
- 351/351: twopole_check.py l1only re-run — 26 shapes, RESIDUE child
  (1/2, 3, 2, 5) at 351 parent pairs, ZCH suffix-DEAD ×276, ν=1 ODE-dead
  601 — and the w-formula PREDICTS the child: 2·(10, 6, 1)/4 =
  (κ̄, D/i, ρ) = (5, 3, 1/2). The "explains 351/351" claim is exact.
- Boundary adversarial (this review): w = 1 entry — no κ̄_m = 1 root
  cell anywhere (strictness of w < 1 confirmed); w = 2/3 and 3/4
  entries — root cells appear (9 and 6 resp.); w = −1/2 entry — no
  admissible children at all (inert); no frame with w ≥ 1 ever admitted
  a κ̄_m = 1 cell across all entries. §5d's picture is exact.

## 6. Front 6 — the FINAL book spec (deliverable)

Merge of SHEET6-MP-REVIEW §5c with this lemma's w-index; hand to the
enumeration workflow as-is. All layers finite per (m, td).

    BOOK(m, td), m ≥ 2, 3m ≤ mβ ≤ td:
    E. Entry layer (printed): type (α,β), 2 ≤ α < β, gcd = 1, mβ ≤ td;
       partition td = ΣΛ_i, Λ_i ≥ β; per pole (a_i, b_i, ν_i) with
       Λ_i = a_i b_i αβ/ν_i, ν_i | α or ν_i | β, plus the q-shape pin
       (b_iβ ≡ 1 mod ν_i when ν_i | α, symmetrically); Q(P_i) =
       (a_iα, b_iα, ν_i, b_i, a_i(α+β)); b_i = 1 forced at Λ_i = β or
       Λ_i prime. Each M=1 entry carries w₀ = a_i(b_i(α+β)−1)/(b_iν_i)
       (∈ ℤ at b_i = 1); num(w₀) ≤ td²/2.
    T. Tree layer (printed): rooted trees, m leaves, Σ(r−1) = m−1,
       r(G) ≤ m, no merge below G*.
    C′. Chain layer (CLOSED by the lemma; H1): an M=1 segment is coded
       by w alone. Alphabet: W = closure of the entry w₀'s under
       (i) resonant steps w ↦ w·n/Δ, Δ = (n−1)ν+1 ≥ 3, Δ | num(w),
       n ≥ 2, ν ≥ 2 (< log_{3/2}num(w₀)+1 per segment; all other steps
       fix w), and (ii) M=1-emitting merges w ↦ w·(r+l)/(lν+1), composed
       ≤ m−1 times. Segments of arbitrary depth realize no cell data
       beyond depth d₀ (≤ 2·gen(W)+2 proved; gen(W)+2 machine-verified
       through gen 4).
    J′. Jump layer, indexed by (w, cell), w ∈ W: cells (family, ν, l)
       with κ̄_m ∈ (w, (r+1)w] ∩ ℤ (integrality via St 9.1 + corrected
       St 3.8), Di := κ̄_m − w, ν DETERMINED per (κ̄_m, l): IIa
       ν(wr − Di·l) = Di; I l = wr/Di (ν = 1); M = gcd(dp_c, dq_c) ≥ 2,
       gcd(M, ν) = 1, M | r ≤ m outside ZCH; child datum (κ̄, D/i, ρ) =
       w·(dq_c, dp_c, 1)/Δ_c. Filters: all non-0 edges are case (II) with
       handshake κ̄_m − D_m/i = w (joins force equal w); ZCH 0-edge is
       case (III): solve with n′ ∈ (1/ν_m)ℕ*, handshake ν_e·w_e — ZCH
       reachable only if arriving w's stand in integer ratio ν_e ≥ 2.
       Coefficient layer per cell (out of pattern book): Prop 8.1(iv)
       rigid solve + the MP §8-item-3 coefficient-vs-ratio match.
    R. Root layer (printed + H1): case (IV), n* = ν_e − κ̄_e ≥ 1 forced
       ((j): κ̄_e < ν_e — keep as the engine filter; w_e = 1 − l_f/i₀ ∈
       (0,1) is the implied frame-free necessary form: root merges dead
       whenever W ∩ (0,1) = ∅), plus (l) d < deg p_G, (m) M-divisibility,
       l odd, l ≤ td−2, k_f = (r+l)l_f, ψ = r+l−1.
    S. Suffix layer (printed): MP2 restored kill below G*, single-pole
       engine, St 9.4 budget Σλ ≤ td−1−ψ. (Check 5's w ≡ 3/2 on St
       9.6(v) suggests the closure extends to M ≥ 2 suffixes — unproved,
       correctly out of scope.)

    Instance td = 6, m = 2: W = {2}, d₀ = 2; J′ = {IIa (2,3,1), M = 2,
    child (5, 3, 1/2)} exactly (corrected model removes ZCH pre-suffix);
    R empty (w = 2 ≥ 1); matches the promoted record cell-for-cell.

## 7. Required fixes (none demote the lemma)

1. **§6 claim 3 (the one substantive fix)**: the (⊆) replay proof
   supports d₀ ≤ 2·gen(W)+2, not gen(W)+2 — restate with the safe
   constant (nothing downstream changes), or add the missing chaining
   lemma (resonant-from-resonant needs n_F | w′; n_F ∤ w′ states are
   dead ends — half the lemma is already in this review). Keep gen+2 as
   the machine-verified sharp value (tight at gen 3).
2. **§5b κ̄_m ∈ ℤ at case-(I)/I-family merges**: DS1(c) covers only V₁ₐ
   vertices; cite St 9.1 (κ̄ = D_f + D_g on T_{a,pole}) + the
   audit-corrected St 3.8, or the equivalent lattice argument (at a
   strict V₂ₐ meet the contact exponent is in the common lattice, else
   some branch jumps and the vertex is V₁ₐ). One line.
3. **§8 engine fix (iii) directionality**: "root filter strengthened to
   w < 1 ... subsumes the κ̄ < ν pin" is backwards — (j) κ̄ < ν IMPLIES
   w < 1, not conversely (reachable hairline witness: (ρ, ν, κ̄) =
   (ν/(ν+1), ν, ν), w = ν/(ν+1) < 1, (j) fails). w < 1 is the correct
   frame-free necessary filter (and the right one-line td = 6 kill); the
   per-edge engine should keep (j)+(k)+(l)+(m). At td = 6 both kill
   everything — no promoted conclusion touched.
4. Cosmetic: §1 vs §3 edge-naming conventions (F = G + c vs G = F + c,
   both printed-faithful) deserve a one-line note; check 3's entry
   congruence (q-shape pin) deserves a code comment; the doc's `jumps()`
   stabilization filter excludes I-family cells — this review verified
   they stabilize within the same d₀ (record it, e.g. as check 8).

## 8. Reproduction

    cd cases && python3 depth_closure_check.py     # 13/13, exit 0
    python3 twopole_check.py l1only                # 26 shapes / 351 pairs
    python3 /tmp/depth_adv.py                      # this review: adversarial
                                                   # entries, boundary w,
                                                   # first-depth audit
    # gen-3/4 stress + full-menu (I-family) stabilization: inline sweeps
    # recorded in §4/§5 (w0 ≤ 720, gen ≤ 4, depth ≤ 12, nu ≤ 30, npat ≤ 10).
    # PDF: pp. 10-18, 39-42, 48-52 re-read on-page for §§1-3.
