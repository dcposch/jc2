# Hostile review: REDUCIBLE-BRANCH REPRICE — is the exact machinery H2-free; does N_min = 6 hold on the reducible branch; the NONPROPER theorems; the measured recovery of the H2 kill

**Reviewer.** grok-4.6 (different-model gate). **Date.** 2026-09-03. **Lane.** `REDUCIBLE-BRANCH-REVIEW`.
Default to refutation. Desk-scale CAS, python 3 / sympy 1.12 over `Q`, `Fraction`s. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis`. No ledger edit; `jc2-lean` not opened; no `ideation-20260903T*` file read. Moh 1983 page images are **not** on this machine: Moh (1)–(13) and Def 5.1 from census-rebase §1 (charged) and OCR `box/depth-drivers-20260902/moh.txt` (display formulas dropped) only.

**Headline.** The ten named items are H2-free in their proofs; H2 is used only as the `[4,16]` clip. `M_s = n−2` is load-bearing for the D1-PIN *coincidence* (algebra confirmed; the printed 5-line numerical table is not a census perturbation). NONPROPER-COUNT / RATE / STRICT-FRONTIER / CAP hold under the hypotheses named below; a non-proper Keller branch cannot sit in a bottom-major disc. The (1)–(7) percentages rerun to the unit, but they are about the **superset**. On the true (1)–(13) space the operative (UNI) `N ≥ 6` numbers are **1 189 groups, 519 killed (43.65%), 670 alive**; `D = 48` **empties**; H2-kill recovery drops from 99.6% to 519/559 = 92.8%. Verdict (c) remains the right typing.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (1) | SCOPE AUDIT: ten items H2-free; H2 only clips `[4,16]`; `M_s = n−2` load-bearing | **CONFIRMED** for the ten proofs and the clip. Perturbation *formula* **CONFIRMED**; printed numerical table **GAP** (repair below). |
| (2) | `N ≤ 5` closure H2-FREE; reducible branch has `N_min = 6` | **CONFIRMED** as literature-typed (Orevkov / Domrina–Orevkov ledger / Żołądek 6.12), with carried `OPEN[ZOLADEK-6.12-ARITHMETIC]`. Campaign-internal fallback `N_min = 4` is correctly priced, not promoted. |
| (3) | Partition PROPER / NON-PROPER; pinned `N` blind to reducibility | **CONFIRMED** under Keller + GEN + Def 5.1 tower with `M_s = n−2` + NU-TWO + DETECTOR-NULL + D1-STAR. A non-proper Keller branch **cannot** occupy a bottom-major disc. |
| (4a) | NONPROPER-COUNT | **CONFIRMED** for `R = D − e Σ V_2 = e(K − Σ V_2)`. Last equality `= D − N(d+e)/((1−δ_1)d)` is **(UNI)/common-`q` only** — GAP off (UNI). |
| (4b) | NONPROPER-RATE | **CONFIRMED**. `(JF)` + `ord_t g_y = −δ^0` (generic `c_2` / FRONTIER-N). Rerun: 113/0. |
| (4c) | STRICT-FRONTIER | **CONFIRMED**. Reproved. Names the no-log/`a_0` step of JAC-FIBRE. |
| (4d) | NONPROPER-CAP | **CONFIRMED** as `n_A^Y ≤ R`. `n_A^Y` is **not** `#` non-proper branches. Cap does **not** consume irreducibility of `A_F`. Chau form stays `GAP[HORIZONTAL-DEGREE]`. |
| (5) | MEASURED (UNI) `D ≤ 120` percentages; no degree emptied; calibration gates | (1)–(7) numbers **CONFIRMED** by rerun. “No degree emptied” **CONFIRMED** on the superset, **REFUTED** on (1)–(13) (`D = 48`). Calibration (10)₁ / MOH_ALL percentages are **not** the true space and **do not survive**. |
| (6) | VERDICT (c) partially subsumed | **CONFIRMED**. Neither (a) nor (b) is forced. |

---

## 0. Custody, method, scope

Frozen copies hashed with `sha256sum` **before any was read**. All eleven match the charge:

```text
fd1f383a2882712ad2a288b2b023b464529570652cbd889778cd665c187c96be  reducible-branch-reprice-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  d1-subtree-review-grok46-20260902.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  moh_skeleton_N.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
b6349f5a76fd56425b47efa009fbbb216f50498a94356cc1ffd62449c54519a5  nmin_reprice.py
c76f5b8e6bd16aca86c50b12259eb3066a25ba71aee8bbe55f6e0e39105d885f  nonproper_count.py
92ded32b61ac5d0fc5902a1982dd792822f8ec1c7fda268b334dbe8946746485  nonproper_rate.py
```

**CH** = D1-SUBTREE producer. **RV** = its grok-4.6 review. **INT17** = integration #17. **RB** = reducible-branch-reprice (the charged producer). **CR** = census-rebase. Moh = T.T. Moh, *J. reine angew. Math.* 340 (1983) 140–212, via CR §1 transcription and OCR `moh.txt`.

No Groebner, no AWS, no web, no `jc2-lean`, no ledger edit. Drivers rerun from `box/reducible-reprice-20260902/` and `box/moh_skeleton_full.py` (`full=True`). Peak RSS of the (1)–(13) pass is desk-scale; wall 0.6 s for the true-space sweep, 51 s for `nmin_reprice.py`, 50 s for `nonproper_count.py`, 0.7 s for `nonproper_rate.py`. No exit price.

Integers kept apart: campaign `N`; Moh `n = deg_y g = D`; `m = deg_y f`; `K = gcd(m,n)`; `n_A = deg Abar_F`; `n_A^Y = #(A_F ∩ {Y = c_2})`. `R` = branches, `Λ` = places, `n_A^Y` = points.

---

## 1. Item (a) — SCOPE AUDIT of the ten named theorems

**CONFIRMED.** For each item the hypothesis line is quoted and H2 is tracked through the *proof*, not only the window clip.

`(H2)` means `A_F` irreducible (RB:99–100, citing the block-descent coordinator). INT17:7–10: “Scope: Keller, noninvertible, degree-minimal, Moh's gauge (GEN, NU-TWO). … H2 only where the window is quoted.” CH:40–41 and CH:720–721: “H2 quoted only where the campaign window `4 <= N <= 16` is used, and marked at every use.” RV:386: “H2 only where the campaign window is quoted.”

### 1.1 The ten items

**JAC-FIBRE.** CH:192–194: “Let `f, g in C[x,y]` be monic in `y`, `F` dominant, `J := [f,g]`. Fix generic `c_2`, let `tau` be any root of `g − c_2`, and let `a_0` be the `t^0`-coefficient of `f(tau)`.” INT17:14–16; RV:60–72. **H2 in the proof: nowhere.** Keller specialises `ord_t J = 0`.

**FRONTIER-EXACT.** CH:232–233: “For a Keller pair in the gauge and generic `c_2`.” INT17:18–21. RV:100–101: no contact may exceed `δ^0` (definition of the frontier). **H2: nowhere.** `N` is a property of `F`, not of `#` components of `A_F`.

**DETECTOR-NULL.** (i) Non-proper ⇒ contribution 0: CH:239–240, Keller only. (ii) Minor ⇒ `δ^0 ≥ 1`: CH:307–315, Prop 6.1(1) “stated for **`r >= 2`** and … the **minor** window `d_r/(n − M_r) >= V_r >= 1`.” INT17:35; RV:328. **H2: nowhere.** Tower/`r ≥ 2`/minor window is (TOW).

**D1-PIN.** CH:328–334: a `g`-root in a bottom-major disc `D_1`. INT17:22–28: “CEILING half uses Moh Def 5.1(1) at level 1; the FLOOR half is Moh-free except Lemma 5.2's evaluation of `λ_g(δ₁)`.” RV:159–163; `Σ_B V_2 ≤ u` is NU-TWO (RV:156). The printed gap `(1−δ_r)(−M_r−m)/(n−M_r)` (CH:342, RV:140–145, INT17:22) is RADIUS-ORDER at `c = n−M_s−1 = 1` (`moh_skeleton_N.py:191–195`). **H2: nowhere in the coincidence.** `M_s = n−2` **is** consumed (§6). CH:531, 546 `[4,16]` clips reported N-sets, not the pin.

**D1-STAR.** CH:365: “Under the hypotheses of D1-PIN.” INT17:29–33; RV:168. **H2: nowhere.** Intra-`f` clustering is free (RV:178).

**PIN-NOT-CEILING (measured).** CH:438–451; INT17:36–40; RV:266–275. Census: `K ≥ 16`, `2 ≤ d < e`, `s ≥ 3`, Def 5.1(2) — (MIN)+(TOW), not H2. Comparing `min L` to 16 is a size check, not irreducibility in the proof that no `D ≤ C(N)` follows.

**Integrality filter.** CH:516–538, 544–560; INT17:41–50; RV:245–257. Arithmetic `N = Σ V_2 q ∈ Z`, `Σ V_2 ≤ u`. **H2 in exactly one column:** “no integer `N` in `[4,16]` (H2)” (CH:546, INT17:43–45, RV:249). Unconditional column is `N ≥ 2` (CH:545). RB:126–127 is right: that clip is the **only** H2 use in the day’s filter.

**Moh condition (15).** CH:594–597: `Σ V_2 q` integral `≥ 2`, `Σ V_2 ≤ u`. INT17:48–50; RV:300–302: `(15) ⇒ (14)`. NOTT (14) had optional `≥ 4` under H2 (RV:298); (15) as printed is `≥ 2`. **H2: not consumed.**

**HARMONIC-BOUND.** Not restated in CH/RV/INT17. CH:609: “HARMONIC-BOUND (NOTT) is unaffected and remains `1/N > 1/deg P + 1/deg Q`.” Statement (NOTT:335–341, the named source CH points to): Lemma 6.1 ⇒ `δ_1 ≥ 0`; `v ≥ 1` ⇒ `u ≤ K−1`; `N < mn/(m+n)` and `N < D/2`, at a degree-minimal pair in Moh’s gauge with NU-TWO and `2 ≤ d < e`. False of automorphisms. **H2: nowhere.** “Unconditional” there means “no H2”.

**N-CEILING.** CH:353–354: `N ≤ u q = U`, attained when bottom discs exhaust `D_{s−1}`. RV:155; `moh_skeleton_N.py:19–20, 197–205`. Unique major child is NU-TWO. **H2: nowhere** in `N ≤ uq`. Old `U ≥ 4` was an H2 size clip, not the theorem.

### 1.2 Load-bearing, not H2

RB:44–50 is right on the mechanism: what the pin uses is (GEN), (KEL), (MIN) via NU-TWO, and Moh’s tower **with** `M_s = n−2`. Off that normalisation the printed CH/RV/INT17 gap identity is not the actual floor–ceiling difference (§6). H2 does not repair or replace that.

---

## 2. Item (b) — NONPROPER-COUNT, NONPROPER-RATE, the partition

### 2.1 Exact hypothesis for “non-proper branches lie in minor discs”

Covering CH:685–688 (reviewed RV:370–371) plus Moh §5–§6 as transcribed: every factor of `p(π)` at `r ≥ 2` is **major** (`V_r > d_r/(n−M_r)`, Prop 5.3 / Def 5.1(2), CR:86, OCR `moh.txt:2154–2177`) or **minor** (`V_r ≤ d_r/(n−M_r)`, Prop 6.1, OCR `moh.txt:2708–2757`). The two windows partition `V_r ∈ Z_{>0}`. Root ball `D_s` has a unique major child `D_{s−1}` (NU-TWO; Prop 5.2); other children are minor. A tower stopping above level 1 leaves its roots in minor discs. At `r = 1`, D1-STAR: `a_1 = e V_2` roots separate at `δ_1` with common `δ^0 = δ_1 + n(1−δ_1)/(n+m)`.

Every generic-fibre branch is therefore in a **bottom-major disc** or a **minor disc**. Hypotheses: Keller + GEN + Def 5.1 with `M_s = n−2` + NU-TWO + Prop 6.1(1) + D1-STAR. Not H2. Prop 6.1 displays were not re-read from page images; the window split is OCR + reviewed CH/RV.

### 2.2 A non-proper branch cannot sit in a bottom-major disc

**Proof.** D1-STAR (c), CH:372: `δ^0 = δ_1 + n(1−δ_1)/(n+m) = (n + m δ_1)/(n+m)`. Then `δ^0 < 1` iff `n + m δ_1 < n + m` iff `δ_1 < 1`. Lemma 5.2 / RADIUS-ORDER at `r = 1` with `c = 1` gives `λ_g(δ_1) = −n(1−δ_1)/(n+m) < 0`, hence `δ_1 < 1`. For a Keller pair FRONTIER-EXACT / JAC-FIBRE give `ord_t f = δ^0 − 1 < 0` on that branch: it is **proper**.

Algebra check (exact `Fraction`s): for `(n,m) = (48,32)` and `δ_1 ∈ {−1/2, 0, 1/6, 1/3, 9/16, 2/3, 5/6}`, one has `δ^0 < 1`; at `δ_1 = 1` one has `δ^0 = 1`, excluded for major discs.

Off Keller the implication fails: CONTROL R, `f = y`, `g = y^3 + x y^2`, place `s → 0`, has `δ^0 = 1/2 < 1` and `ord_t f = 1/2 > 0` (non-proper). RB:294–296 is right: the dichotomy `proper ⇔ δ^0 < 1` is Keller-specific.

A proper Keller branch cannot sit in a minor disc either: Prop 6.1(1) ⇒ `δ^0 ≥ 1`, and STRICT-FRONTIER (§3) upgrades to `δ^0 > 1`, hence non-proper. The partition is therefore a **bijection** of blocks, not merely a covering:

```text
proper branches   =  roots of bottom-major discs   (e Σ_B V_2(B) of them)
non-proper        =  roots in minor discs          (the rest)
```

That is the exact hypothesis under which RB:206–207 holds. Breaking it would require a non-proper root inside a bottom-major disc; D1-STAR forbids that for Keller.

### 2.3 NONPROPER-COUNT, reproved

Def 5.1(1) (CR:128, OCR `moh.txt:2118–2121`): a bottom-major disc holds `(n/d_2) V_2 = e V_2` roots of `g`. Summing over disjoint bottom-major discs inside `D_{s−1}`: `#` proper branches `= e Σ_B V_2(B)`. The fibre has `D = n = K e` branches. Hence

```text
R  :=  # non-proper branches  =  D − e Σ_B V_2(B)  =  e (K − Σ_B V_2(B)).
```

The V-packet determines `R` the same way it determines `N`. No H2.

If every bottom disc shares the same `q` — (UNI), or one Galois orbit — then `N = (Σ V_2) q` with `q = (1−δ_1) d e/(d+e)`, so `Σ V_2 = N/q` and `R = D − N(d+e)/((1−δ_1)d)`. **Off (UNI)** different discs may carry different `q(B)`; the last equality is then false while the first three remain. RB:222 writes all four as equal without naming (UNI). **Repair:** keep `R = e(K − Σ V_2)` unconditionally (given the partition); tag the `N`-form as (UNI).

PLACE-LEDGER: RB:232–236 correctly refuses `Λ = R` (INT17:72–74 GAP) and uses `R ≥ Λ` in the safe direction.

### 2.4 NONPROPER-RATE, reproved

JAC-FIBRE, CH:192–196: `ord_t(f(τ)−a_0) + ord_t g_y(τ) = −1 + ord_t J(τ)`, monic in `y`, `F` dominant, generic `c_2`. Monicity: `g_y(τ_i) = ∏_{j≠i}(τ_i−τ_j)`, so `ord_t g_y = Σ_{j≠i} ord_t(τ_i−τ_j)`. Along `τ_i`’s path, `Λ(δ) = δ + Σ_{j≠i} min(δ, ord_j)`. For `δ < δ^0` one has `λ_g < 0`, so `Λ(δ) = λ_g(δ)`; continuity gives `Λ(δ^0) = 0`. Generic `c_2` (FRONTIER-N, INT16 promoted / RV:93): no contact exceeds `δ^0`, hence `min(δ^0, ord_j) = ord_j` and `ord_t g_y = −δ^0`. This step does **not** need `δ^0 < 1`. Substitute into `(JF)`:

```text
ord_t(f(τ) − a_0)  =  δ^0 − 1 + ord_t J(τ).
```

Keller: last term 0. At a non-proper place of ramification `ν_γ`, `ord_γ(f−a_0) = ν_γ(δ^0−1)`.

**Hypothesis repair:** RB:262–264 says “only that `δ^0` is the frontier.” The identification `ord g_y = −δ^0` also uses generic `c_2` / no contact `> δ^0`. Not a hole on the stated scope (generic fibre).

Rerun of charged `nonproper_rate.py`: **113 checks, 0 failures**, 19 non-Keller rows, 38 places. The four displayed rows (RB:287–290) match the stdout, including `f = y`, `g = y^3 + x y^2`, `δ^0 = 1/2`, non-proper.

---

## 3. Item (c) — STRICT-FRONTIER

**CONFIRMED.** For a Keller pair in the gauge, no branch of a generic fibre has `δ^0 = 1`. Proper `⇔ δ^0 < 1`, non-proper `⇔ δ^0 > 1`, strictly.

**Proof.** Keller ⇒ `ord_t J = 0` on every branch, so NONPROPER-RATE gives `ord_t(f−a_0) = δ^0 − 1`. By definition of `a_0` as the `t^0`-coefficient, `f(τ)−a_0` has vanishing constant term, hence `ord_t(f−a_0) ≠ 0` unless `f−a_0 ≡ 0`. The vanishing case: `f` is constant on a formal neighbourhood of a place at infinity of `{g = c_2}`; by the identity theorem `f` is constant on that component, so `F` contracts a curve to a point, contradicting that a Keller map is étale (hence quasi-finite). Thus `δ^0 ≠ 1`. Combined with FRONTIER-EXACT’s `δ^0 ≥ 1` ⇔ non-proper (CH:239–240), the value 1 is a gap.

This is the named form of RV:74–75 (“After `a_0` is stripped, `k ≠ 0` … It is exactly `delta^0 = 1`”). Promotion is of the *name and the Keller dichotomy*, not of a new identity.

CONTROL R tests the **local** content `ord_t(f−a_0) > 0` on non-proper branches, not `δ^0 ≠ 1`: off Keller, `δ^0 = 1` occurs (first row: `f = y`, `g = y^2 + x y`, `s → 0`, `δ^0 = 1`, `ord J = 1`). RB:283’s slogan “STRICT-FRONTIER’s local content” is right if read as `oa > 0`; it is not a check that `δ^0 = 1` is empty off Keller.

---

## 4. Item (d) — NONPROPER-CAP and `n_A^Y`

**CONFIRMED** as an upper bound on the horizontal degree. **Not** an identification with the number of non-proper branches. **Does not consume irreducibility of `A_F`.**

RB:32–33 defines `n_A^Y := #(A_F ∩ {Y = c_2})` at generic `c_2`. In the gauge `F = (f,g)`, a point of `A_F ∩ {Y = c_2}` is a finite limit of `f` along a sequence in `{g = c_2}` escaping to infinity — i.e. a limit of a non-proper branch. The map from non-proper *places* to those points is therefore surjective by the definition of the nonproper value set relative to the second coordinate. Cardinality of the image is `≤ Λ ≤ R`. Lemma NL (no component of `A_F` is a line; imported from the reducible cage / Chau Thm 1, not re-proved here) excludes a horizontal component `{Y = const}`, so a generic slice is finite and `n_A^Y` is the horizontal degree `deg_X` of the affine equation of `A_F`. Then `c := #` components satisfies `c ≤ n_A^Y` (each component meets a generic `Y`-line at least once). **None of this uses that `A_F` is irreducible.** H2 is the special case `c = 1`, equivalently (RB:308) transitivity of `c_2`-monodromy on the limit points — a translation, not a hypothesis of the cap.

RB:312–315: `n_A^Y ≤ e(K − Σ_B V_2(B))`. Correct. The parenthetical in the charge, “identified with the number of non-proper branches”, would be **false**; RB does **not** make that identification. `R` is the branch count; `n_A^Y` is the point count; the cap is the inequality.

The Chau clause “if `e | deg A_i` transfers to the horizontal degree, `c ≤ K − Σ V_2`” is correctly tagged `GAP[HORIZONTAL-DEGREE]`, bounded quantity `mult_{[1:0:0]} Abar_F ∈ [0, n_A]` (RB:317–318). Unconditionally the cap is on `n_A^Y`, not on `n_A` (RB DISCLOSURE (2), RB:628–629).

---

## 5. Item (e) — reruns, and the true (1)–(13) space

### 5.1 Charged drivers, rerun

`nmin_reprice.py` `D ∈ [48,120]`, (UNI), one core, 51 s. **Unit match** to RB:397–411 and INT17:45–47 / RV:247–256: `N≥6` 893340/902893 (98.94%) assign, 6360/10637 (59.79%) groups; `[4,16]` 893706 (98.98%) / 6386 (60.04%); per-degree H2 group-kills 209, 419, 795, 47, 2390; no degree emptied in any of five windows.

`nonproper_count.py`: 9 553 / 902 893 V-assignments survive `N ≥ 6`; 4 277 / 10 637 groups; FREE and CHAU both 9 553 / 4 277; **0** groups killed by the reducible tests; `min R = 6 = 2e` at `(48, 32, M=(−8,46), V_2=2, V_3=7, k=7, ΣV_2=14, N=14)`. Unit match to RB:491–498.

`nonproper_rate.py`: 113 / 0, as §2.4.

These numbers are about `moh_skeleton_N.py`’s census: Moh (1)–(7) + Def 5.1(2), **not** (8)–(13). CR:29–31 / INT17 delta (h): the true space at `48 ≤ D ≤ 120` is 1 189 groups, 1 692 V-assignments.

### 5.2 True (1)–(13) space, `box/moh_skeleton_full.py`, (UNI), `D ≤ 120`

Rerun with `census(n, full=True)` and the same `N = k V_2 q`, `k V_2 ≤ u` arithmetic. Wall 0.6 s. **Unit match to CR §6** on groups / `uni≥6` alive / `uni[6,16]` alive / V-assignments:

```text
window          assign       kill        %    groups  grpkill        %    alive
N>=2              1692        781   46.16%      1189      457   38.44%      732
N>=4              1692        804   47.52%      1189      478   40.20%      711
N>=6              1692        852   50.35%      1189      519   43.65%      670
N>=4 <=16         1692        928   54.85%      1189      559   47.01%      630
N>=6 <=16         1692        976   57.68%      1189      600   50.46%      589
```

Per-degree `uni≥6` alive matches CR:412–438 to the unit (105:7, 108:87, 112:33, 117:4, 120:271). `D = 66` and `D = 78` carry no (1)–(13) skeleton (CR:444–445) but exist in (1)–(7).

**Degrees emptied (every group killed):**

- `N ≥ 6` and `N ∈ [6,16]`: **`D = 48` only.**
- `N ≥ 2`, `N ≥ 4`, `N ∈ [4,16]`: **NONE.**

`D = 48` has two (1)–(13) groups: `(m,M,V) = (32,(24,46),{2:3,3:5,4:2})` with `q = 3/7`, no integer `N`; and `(32,(−8,36,46),{2:2,3:1,4:3,5:2})` with `q = 1/3`, achievable `{2,4}` only. Both die at the frontier; the second survives `N ≥ 2`. Emptying is a **frontier** effect, not an unconditional-integrality effect. **No `D > 100` empties**, matching CR:446.

H2-kill recovery on this space: group-kill `N ≥ 6` over `[4,16]` is `519/559 = 92.8%`, not `6360/6386 = 99.6%`. Assignment recovery `852/928 = 91.8%`. The upper clip 16 still kills 81 extra groups at `N ≥ 6` (`600 − 519`).

Distinct achievable `N ≥ 6` on (1)–(13): **31 values, max 36** (superset claim 33 / max 40 was not in the charged driver’s stdout).

NONPROPER tests on the 670 groups alive at `N ≥ 6`: FREE and CHAU both **670 / 670**; **0** killed by the reducible tests. `min R = 6` moves to `(84, 56, M=(−14,82), V_2=1, k=26, ΣV_2=26, K=28, e=3, N=26)` — the superset witness at `D = 48` is dead on (1)–(13). Tightness `R = 2e` survives; the witness does not.

### 5.3 Calibration (10)₁ / reconstructed full gate

RB §4.3 (not a charged driver) measured a STAR-CONGRUENCE / (10)₁ gate (9 630 groups) and a MOH_ALL gate **without branch (11)** (287 groups). CR:27–31: omitting (11) under-counts groups by 4.1× (287 vs 1 189). Those percentages (63.40% vs 63.69%; 9.41% vs 13.94%; “unconditional filter kills nothing”) are **not** numbers on the true space. On (1)–(13), unconditional `N ≥ 2` kills **38.44%** of groups. The slogan “the whole kill is the frontier” is **REFUTED** on (1)–(13).

---

## 6. Item (f) — perturbation of `M_s = n−2`

**Formula CONFIRMED. Printed table GAP.**

RADIUS-ORDER, `moh_skeleton_N.py:191–195`: `λ_g(δ_r) = −n(1−δ_r)(n−M_s−1)/(n−M_r)`. Put `c := n−M_s−1`. Floor from JAC-FIBRE + slope `≥ 1`: `(1−δ_r) + λ_g`. Ceiling from Def 5.1(1) proportionality: `−(m/n) λ_g`. Difference:

```text
floor − ceiling  =  (1−δ_r) [ 1 − (n+m) c / (n−M_r) ].
```

At `r = 1`, `n−M_1 = n+m`, this is `(1−δ_1)(1−c)`. Identity checked on five `(n,m,δ_1)` pairs, `Fraction`s, both expressions equal. For `c = 1` (`M_s = n−2`) the gap vanishes at `r = 1` (and CH’s printed formula is recovered). For `c ≠ 1` the gap is `(1−δ_1)(1−c) ≠ 0` (`δ_1 = 1` excluded: it forces `λ_g(δ_1) = 0` and `N = 0`). Off `M_s = n−2`, D1-PIN **brackets** `N`, it does not pin it. That is the load-bearing claim (RB:49–50, 174–191).

**Live census perturbation**, Def 5.1(3) recomputed. Skeleton `(n,m,M,V) = (48,32,(−8,46),{2:1,3:5})`, windows OK:

```text
M_s=46  c=1  δ_1=43/68  floor=ceil=5/34     gap=0        PINNED
M_s=45  c=2  δ_1=97/272 floor=-35/272 ceil=35/68  gap=-175/272  BRACKETED (windows still OK)
M_s=44  c=3  δ_1=9/34   floor=-10/17  ceil=15/17  gap=-25/17    BRACKETED
```

The closed gap equals `(1−δ_1)(1−c)` after the delta recomputation.

**The printed 5-line table (RB:180–185) is not this perturbation.**

- `(n,m,M_s) = (48,32,46)` with `floor = 1/3` forces `δ_1 = 1/6`, which is **not** the `δ_1` of any of the 36 live V-assignments at `M = (−8,46)` (first: `43/68`, floor `5/34`). Holding `δ_1 = 1/6` fixed while lowering `M_s` gives `c=2` gap `−5/6`, not the printed `−65/72`. The printed `c=2` row is a *different* `δ_1` (`7/72`).
- `(64,48, M=(16,62))` has **zero** V-assignments in the (1)–(7) census: `M_2 = 16` does not drop `d_2 = 16`. The printed `floor = ceiling = −72/25` inverts to `δ_1 = 193/25 > 1`, not a major-disc radius.

**Repair:** replace the table by the live `(48,32,(−8,46),{2:1,3:5})` row above. Keep the formula. The qualitative conclusion — off `M_s = n−2` the pin is lost — stands.

---

## 7. Item (g) — verdict typing

RB:470–483 types **(c) PARTIALLY SUBSUMED**, boundary at proper / non-proper.

- **Not (a) fully subsumed.** NONPROPER-CAP is an *upper* bound in the same direction as the companion razor; the FREE/CHAU tests kill **zero** groups on both the superset and the true space. `OPEN[COMPANION-R0-REALISATION]` / degree-cap, the razor stack, the reducible cage, `NO-DEG-CAP` remain statements about the zero-contributing block. A lower bound on `n_A^Y` is still missing (`OPEN[COMPANION-DEGREE-FLOOR]`, carried).
- **Not (b) not subsumed.** JAC-FIBRE, FRONTIER-EXACT, D1-PIN, D1-STAR, the integrality filter, (15), PIN-NOT-CEILING, HARMONIC-BOUND, N-CEILING, and literature `N_min = 6` do not use H2 and apply verbatim to a reducible-`A_F` counterexample. The census-plus-pinned-`N` filter is one program. On (1)–(13) it additionally **empties `D = 48`**, still H2-free, still for both branches.

**(c) is the right typing.** The true-space remeasurement changes the *numbers* inside the subsumed block, not the block diagram.

RB K1: “`N ≤ 5` closed” is H2-free as literature. Żołądek 6.12 as printed (n5-soundness:96): “Any Jacobian map `P` with `degtop P ≤ 5` is invertible” — no `A_F` hypothesis. N=4 ledger (notes.md:17564–17571) likewise. Orevkov `N ≤ 3` is classical; RB’s `notes.md:15648` is a B0-nearest-miss line, not the closure ledger — repair the citation. n5-soundness:6 “residual after H2 is reducible `A_F`” is the **cage leftover** (that report:370–371), not a restriction of 6.12. Carry `OPEN[ZOLADEK-6.12-ARITHMETIC]`. Campaign-internal H2-bound N=4/N=5 kills (Thm 4.2, 7.B) are correctly separated; RB’s fallback `N_min = 4` is priced, not promoted here.

---

## 8. What survives unchanged on the true (1)–(13) space

| Claim | On (1)–(7) SUPERSET (RB) | On true (1)–(13) (this review / CR §6) |
|---|---|---|
| Scope audit; `M_s = n−2` load-bearing | unchanged (not a census claim) | unchanged |
| `N_min = 6` H2-free (literature) | unchanged | unchanged |
| Partition; NONPROPER-* theorems | unchanged | unchanged |
| Verdict (c) | unchanged | unchanged |
| (UNI) `N ≥ 6` assignment kill | 893 340 / 902 893 = 98.94% | **852 / 1 692 = 50.35%** — re-measured |
| (UNI) `N ≥ 6` group kill | 6 360 / 10 637 = 59.79% | **519 / 1 189 = 43.65%**; **670 alive** — re-measured, matches CR |
| H2 `[4,16]` group kill | 6 386 / 10 637 = 60.04% | **559 / 1 189 = 47.01%** — re-measured |
| Recovery of H2 group kill by `N ≥ 6` | 6 360 / 6 386 = 99.6% | **519 / 559 = 92.8%** — re-measured |
| Unconditional `N ≥ 2` group kill | 55.13% | **38.44%** — re-measured; **not** “nothing” |
| No degree emptied | NONE in five windows | **`D = 48` emptied at `N ≥ 6`** — REFUTED as a (1)–(13) statement |
| Calibration 63.40% / 9.41% | wrong space already | **discard**; not (1)–(13) |
| FREE/CHAU zero kills | 0 / 4 277 | **0 / 670** — survives |
| `min R = 2e` | 6 at `D = 48`, `N = 14` | 6 at `D = 84`, `N = 26`; `D = 48` witness **dead** |
| Distinct `N ≥ 6` | claimed 33, max 40 (not in driver stdout) | **31 values, max 36** |

Operative H2-free filter number for both branches, `D ≤ 120`, (UNI), no upper window: **670 groups alive of 1 189**.

---

## 9. OPEN(S) RAISED

None new. The producer’s residue is confirmed, not enlarged.

**CARRIED (not re-opened here).** `OPEN[COMPANION-DEGREE-FLOOR]`: bound `n_A^Y` from below at a degree-minimal counterexample; the integer lies in `[c, e(K − Σ_B V_2(B))]` with `c ≥ 2`. `GAP[HORIZONTAL-DEGREE]`: bound `mult_{[1:0:0]} Abar_F ∈ [0, n_A]`. `OPEN[MINOR-INTEGRALITY]`: per surviving skeleton, the multiset of `(ν_γ, δ^0_γ)` over minor discs. `OPEN[ZOLADEK-6.12-ARITHMETIC]`: line-replay of 6.12 A–M. `OPEN[MOH-PROGRAM]`: (1)–(13) is a strict superset of Moh’s table (CR:385–391, 652 excess rows at `n ≤ 100`). `OPEN[BRANCH-ORBITS]`, `OPEN[V-FLOOR]`, `OPEN[STAR-REALISABILITY]`, `OPEN[COMPANION-R0-REALISATION]`, `OPEN[NONPROPER-DEGREE]`, PLACE-LEDGER identification (GAP).

---

## 10. FALLACY-v2 audit

Flag/place/series: `D`, `N`, `K`, Moh `n,m`, `n_A`, `n_A^Y` apart; `R`/`Λ`/`n_A^Y` never identified; rank-four “reducible” ≠ reducible `A_F` (RB K5); `{g=c_2}` places ≠ PLACE-LEDGER (INT17:72–74, not consumed). Per-ray: no exit price, no `charge_basis`; each `g`-root in one block. Automorphism controls are not `FULL_ACTUAL_EXIT`; CONTROL R is non-Keller. Floor/attainment: CAP used only as an upper bound; D1-PIN attains only at `c=1`; filter numbers are finite-set (UNI) measurements. `(star)` via CH; `g_y` a partial; CONTROL R orders from cancelled rationals. No `sat()`, no Groebner. Missing companion floor stays OPEN; Chau divisibility is not transferred; (1)–(13) is not “Moh’s program”.

---

## 11. Typed verdict block

```text
LANE       REDUCIBLE-BRANCH-REVIEW (hostile, grok-4.6), 2026-09-03
SCOPE      Keller, noninvertible. Degree-minimality and Moh's gauge where
           D1-PIN / D1-STAR / the census require them. H2 nowhere in the
           ten proofs; H2 = the [4,16] clip only. Page images of Moh 1983
           not on this machine; (1)-(13) and Def 5.1 from CR §1 + OCR.
           No charge_basis.

PROMOTE    SCOPE-AUDIT CONFIRMED.  Ten named items H2-free in the proof.
             Integrality [4,16] column is the only H2 use.
           M_s = n-2 LOAD-BEARING CONFIRMED (formula).  r=1 gap
             = (1-delta_1)(1-(n-M_s-1)).  Printed 5-line table GAP;
             replace by live (48,32,M=(-8,46),V={2:1,3:5}).
           N_min = 6 on the reducible branch CONFIRMED as literature-
             typed (Orevkov / N=4 ledger / Zoladek 6.12 as printed).
             Carry OPEN[ZOLADEK-6.12-ARITHMETIC].  Do not promote a
             campaign-internal N_min = 6.
           NONPROPER-COUNT CONFIRMED: R = D - e sum V_2 = e(K-sum V_2).
             Last N-form is (UNI) only.
           NONPROPER-RATE CONFIRMED.  113/0 rerun.
           STRICT-FRONTIER CONFIRMED.  Keller => delta^0 != 1.
           NONPROPER-CAP CONFIRMED as n_A^Y <= R.  Does not equal R;
             does not consume H2.  Chau form stays GAP[HORIZONTAL-DEGREE].
           PARTITION CONFIRMED.  Non-proper Keller branch cannot sit in
             a bottom-major disc (D1-STAR: delta^0 < 1 there).
           VERDICT (c) CONFIRMED.  Not (a), not (b).
           (1)-(7) FILTER NUMBERS CONFIRMED by rerun (unit match).
           (1)-(13) OPERATIVE NUMBERS: 1189 groups, 519 killed at
             N>=6 (43.65%), 670 alive; D=48 emptied; recovery of the
             [4,16] group kill is 519/559 = 92.8%, not 99.6%.
             Matches CR §6 to the unit.  FREE/CHAU still zero kills.

DO NOT PROMOTE
           RB's 98.94% / 59.79% / "no degree emptied" / "99.6% recovery"
             as numbers on Moh's space.  They are the (1)-(7) SUPERSET.
           Calibration 63.40% / 9.41% / "unconditional kills nothing".
             Wrong space (no (11)); false on (1)-(13) (N>=2 kills 38.44%).
           NONPROPER-COUNT's four-way equality off (UNI).
           The printed M_s-perturbation numerical table.

REPAIR     CH/RV/INT17 D1-PIN gap identity is the c=1 specialisation;
             state M_s = n-2 as a hypothesis of the coincidence.
           CH:239-240 "delta^0 >= 1 iff non-proper": carry STRICT-FRONTIER
             (the value 1 is a gap for Keller).
           RB:15648 as the N<=3 citation: replace by the Orevkov theorem,
             not a B0 nearest-miss line.
           n5-soundness "residual after H2 is reducible A_F": cage leftover,
             not a restriction of 6.12.

CONFIRMED  INT17:7-10 / CH:40-41,720-721 / RV:386: H2 only at the window.
           CR §6 (1)-(13) counts, independently rerun.

DISCLOSURE (1) No noninvertible Keller pair to test on; CONTROL R is
               non-Keller.  (2) Prop 6.1 displays not re-read from page
               images; window split from OCR + reviewed CH/RV import.
           (3) (UNI) throughout; hypothesis-free knapsack not re-run.
           (4) Lemma NL / Chau Thm 1 imported, not re-proved.
           (5) Distinct N>=6 on (1)-(7) (claimed 33/max 40) not in the
               charged driver's stdout and not re-enumerated here.
```

**Per-item promotion:** (1) H2-free audit + `M_s = n−2` formula, not the printed table. (2) literature `N_min = 6`, carry Żołądek arithmetic. (3) partition. (4) COUNT (first three equalities), RATE, STRICT-FRONTIER, CAP-as-inequality; not the Chau form. (5) (1)–(7) rerun as record calibration; (1)–(13) as the operative census; not “no degree emptied” / 99.6% off the superset. (6) verdict (c).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31581`.
- Body SHA-256:
  `23797572cc23112eddb7f5beefb5e20f41df024032c1089f84a3d0271fb6676b`.
- Frozen basis: `f5aa1cafd1d848b1b3ccb6b3370972b737f98628`.
