# Ideation round 20260903T1015Z — blind submission — Fable 5 (claude-fable-5-1)

Lane `ideation-20260903T1015Z-fable5`. Packet `xmodel/ideation-20260903T1015Z-packet.md`
verified: SHA-256 `99c940d1167acfc7796436457a1d87bdd0a1a1a4c673c7bb2e0d3436e3d086b7` (match).
Basis f5aa1caf. Blind: no other `ideation-20260903T1015Z-*` submission read; the three
running lanes' `.md` files not opened; no canonical ledger edited; `jc2-lean` not inspected.

**Sources read.** The packet; AUDIT.md integration #17 and deltas (a)–(h); the two binding
LIVE STATE blocks (08:33Z handoff, 10:02Z acknowledgment); COORDINATION.md (full-spectrum
contract, resolution-first directive, OPEN authoring rule); APPROACHES.md (all 46 rows and
overlays); `census-rebase-opus5-20260902.md` (§0–§7, §10); `integration17-coordinator-
fable51-20260902.md`; the 1608Z synthesis; section maps of `time-function-endgame-*`,
`reducible-branch-reprice-opus5-20260902.md`; `box/moh_skeleton_full.py` (source);
`box/censusrebase-drivers-20260902/survivors-D48-120.txt`. **The Moh 1983 PDF IS present on
this machine** (`refs/moh1983_jram340_configurations_of_roots.pdf`, SHA-256
`6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51`, matches the packet's
prefix); per the packet's licence I read it and say so: pages 148–151, 188–189, 196–202,
207–212 rendered at 110 dpi with `pdftoppm` and read as images. Every Moh citation below is
therefore SOURCE-READ unless marked SOURCE-UNVERIFIED (a page I did not open).

**Computation.** Desk-scale only: three python3 probes importing `box/moh_skeleton_full.py`
(its `census`, `Skel`, `groups_of`, `uni_hits`), one core, < 3 min, < 200 MB. The predicates
are printed in §12 so the numbers are reproducible from the tracked tool.

## 0. Headline — direct answers

1. **Q1 (MOH-PROGRAM).** Moh's printed list (1)–(13) is the program's *skeleton
   sieve*; Appendix II (read in full, pp.207–212) is **not** a uniform filter but
   hand case-work on the six rows: Prop 6.3 descent to a monomial-Jacobian pair of
   degrees (n/d_s, m/d_s), Theorem 1.2 approximate-root expansions with order bounds
   at the major and minor π-roots, and a coefficient count (17, 10, 22, 11
   variables). The **strongest fail-closed numerical discriminator I found is
   `M_2 > m`** (the first characteristic exponent of f in g^{-1/n} beyond −m must
   exceed m): keeps 6/6 printed rows, cuts 658 → 94 rows / 32 classes at n ≤ 100,
   pins (75,50) to M_2 ∈ {55, 60}, and with the pinned-N integrality leaves exactly
   Moh's two (75,50) rows. On the (1)–(13) space at 48 ≤ D ≤ 120 it cuts 1,189 →
   179 groups; with integral N ≥ 6 → **63 groups (59 in [6,16])**, and **D = 105 is
   EMPTIED** (all three trio groups have M_2 ∈ {28, 40} < 70). Twelve degrees empty
   (48, 54, 60, 63, 72, 81, 88, 102, 104, 105, 110, 114); the smallest live
   degree above 100 becomes **108 with two groups in [6,16]**. STATUS: MEASURED
   only. I did not find `M_2 > m` printed on the pages read; typed
   `OPEN[M2-ABOVE-M]` (§11). It is a *candidate* for Moh's hidden restriction, not
   a claim that it is one. The **Abhyankar–Moh semigroup conditions are AUTOMATIC**
   on all 658 rows (MEASURED, §2.4): Q3(d)'s "silently used semigroup condition"
   is refuted as the missing filter.
2. **Q1 all-degree form.** Moh's own mechanism is a **descent**: when u_s = 1
   (509 of the 658 rows; 2 of the 3 trio groups) Prop 6.3 + 6.4 send the pair to
   polynomials in k[γ, π] of π-degrees (n/d_s, m/d_s) with Jacobian −(1/b)γ^{v_s−2}
   and characteristic data {M_i/d_s, d_i/d_s}. That is a **monomial-Jacobian pair
   of degree ≤ n/4** — the GGV "[P,Q] = x^k" world of APPROACHES row 1. This is the
   uniform mechanism the campaign should build: iterate the descent while u_s = 1
   and land in a degree range where monomial-Jacobian pairs are classified.
3. **Q2 (the trio).** Do **not** spend a flagship seat on interpolation. Two desk
   routes kill first: (i) if `M2-ABOVE-M` is a theorem, all three die; (ii) Prop 6.3
   descends group 2 (M = [28,103], V_s = 6, d_3 = 7, u_3 = 1) to a **(15,10) pair
   with [P,Q] ∝ γ^4** and group 3 (M = [40,103], V_s = 4, d_3 = 5, u_3 = 1) to a
   **(21,14) pair with [P,Q] ∝ γ^2** — problems of the size Moh did by hand (his
   (15,10), γ^2 case, pp.210–211, 11 variables). Group 1 (u_3 = 2) needs the
   minor-disc dichotomy Moh used for (99,66). A trio kill buys only D_min ≥ 108;
   the descent buys a *mechanism*.
4. **Q3.** The right all-degree frame is Moh §2: the pair is a **rational curve
   with one place at infinity over k(x)** whose Puiseux characteristic IS the
   skeleton, with Lemma 2.1 (coefficients constant below order n−1, linear in x at
   order n−1) as the *only* place the Jacobian condition enters the expansion.
   (f) is true as stated: (1)–(13) + integrality never empties above D = 100; a
   uniform theorem must use a datum not in the skeleton, and Lemma 2.1 names it:
   the x-dependence at order n−1, equivalently the minor-disc data. Candidates
   (a),(c),(e) LOWER; (b) UNCHANGED; (d) RETYPE (semigroup automatic; keep the AM
   one-place frame).
5. **Q4.** Build the **skeleton descent engine** (recursive Prop 6.3 on census
   groups + the `M_2 > m` flag + a monomial-Jacobian receiver) before any order-k
   interpolation engine. It runs in seconds to D = 200 and its negative control is
   Moh's p.207 table.
6. **First lane (frontier seat):** `M2-DESCENT` (Opus): prove or refute
   `M_2 > m` from Moh §2–§5, and run the Prop 6.3 descent on the two u_s = 1 trio
   groups to explicit (15,10; γ^4) and (21,14; γ^2) monomial-Jacobian problems.

## 1. What Appendix II actually is (SOURCE-READ, pp.207–212)

* p.207: "A simple computer program shows that the only possible counter-examples
  ... are of degrees (64,68) [erratum for (64,48)], (84,56), (75,50) and (99,66)
  with some special data attached. ... the number of coefficients ... 3370, 5308,
  4352 and 7348." So the *program* already output the four classes; Appendix II
  starts after the program. The 658-vs-6 gap (delta (h)) is therefore inside the
  program, i.e. inside "the above discussion" of pp.178–201, not in Appendix II.
* Prop 6.4 (p.198): with δ_s = −1 and u_s = 1, the minor disc D*_{s−1} has
  δ*_{s−1} ≥ v_s. Prop 6.3 (p.197): with δ*_{s−1} ≥ v_s/u_s there is a π-root
  σ = Σ a_j θ^j + π θ^{v_s/u_s}, γ = θ^{1/u_s}, such that ḡ(σ), T̄_i^ψ(σ) ∈ k[γ,π],
  monic in π of π-degrees u_s n/d_s, u_s(−μ_i)/d_s, and
  J_{γ,π}(ḡ(σ), T̄_1^ψ(σ)) = −(u_s/b) γ^{v_s−u_s−1}. Check against the p.207 table:
  (64,48) → (16,12), γ^{3−2} = X; (84,56) → (21,14), X; (75,50) → (15,10),
  γ^{4−2} = X²; all match, including M_2/d_s = 13, 16[18], 11.
* p.208: (16,12) case — Theorem 1.2 with h the common quasi-approximate root
  (ḡ = h⁴ + α_1h³ + … + α_4, f̄ = h³ + β_2h + β_3), order bounds
  ord α_i(σ), ord α_i(σ̄) ≥ i(−1/4) at the major root σ = πt^{1/4} and the minor
  root σ̄ = t^{-1} + a_0 + a_1t + a_2t² + πt^{11/4}; 17 coefficients. "Similar
  arguments ... show the impossibility directly" for (21,14); 22 [15 or 13] for
  (15,10). p.208–209: the η-expansion trick (f = η^{-12}, g = η^{-16} + …,
  replace (f,g) by (f − ¾a_3, g − a_1f − a_4)) reduces to 10 coefficients.
* p.209: (99,66), u_3 = 3, no Prop 6.3: the unique π-root in the minor disc D*_2
  has g_σ(π) either a power of a linear polynomial (→ data (27,18,21; V_2 = 8,
  δ_2 = −1, δ_1 = 0, Jacobian X⁴), 10 coefficients) or the 9th power of a cubic
  with two roots (→ Ω: x → x^{-1}, y → a_0 + a_1x + a_2x² + yx³ with
  J(Ωf, Ωg) = x, 11 variables).
* pp.210–211: the (15,10, X²) case in full: g = h³ + 3βh + … must cancel its
  y^{-1} power series; equations (2)–(4); the minor disc forces h and β into the
  shapes (5)–(6) (h = (y² − x² + a_1y + a_2x + a_3)³ + …); deg_y γ ≤ 2 gives three
  quadratic equations in the a_i; both cases contradict. "All other cases can be
  computed directly as above."

**Reading.** Every kill in Appendix II is *polynomiality of the expansion of g in
the quasi-approximate root h at both the major and the minor π-root*, after a
descent that makes the Jacobian a monomial. That is the campaign's interpolation
identity (item 6 of the packet) in Moh's coordinates — but applied to a pair of
degree ≤ n/4 with a monomial Jacobian, where the coefficient count is 10–20, not
thousands. The lesson for Q2/Q4 is: **descend first, interpolate second.**

## 2. Q1 — the missing elimination

### 2.1 What the characteristic data are (SOURCE-READ, p.150–151)

g = η^{-n}, η = g^{-1/n} = y^{-1} + α_2(x)y^{-2} + … ∈ k[x]((y^{-1})), and
f = η^{-m} + Σ_{j>−m} f_j(x) η^j ∈ k[x]((η)). d_1 = n, d_{j+1} = gcd(n, M_1..M_j),
M_j = min{i : f_i(x) ≠ 0, d_j ∤ i}. So {M_j; d_j} is the Abhyankar–Moh Puiseux
characteristic at infinity of the rational curve F(f,g) = 0 over k(x), "cf.
[A-M.1] p.68". Lemma 2.1: J = c ≠ 0 iff f_i(x) is constant for all i < n−1 and
deg_x f_{n−1} = 1. Hence all M_i ≤ n−1 and the data below n−1 are those of a
*constant-coefficient* Laurent series P(η): the skeleton sees only the k-part
of the branch; the x-dependence starts at order n−1 (this is the datum Q3(f)
asks for).

### 2.2 MEASURED: candidate filters on the 658 rows (Moh's own space, n ≤ 100)

Predicates run on `census(n, Kmin=2, full=True)` of `box/moh_skeleton_full.py`
(code in §12). "printed" = the six p.202 rows (fail-closed).

```text
filter                                   rows  classes  printed kept
(1)-(13) baseline                         658     63       6/6
Abhyankar-Moh semigroup (ii)+(iii)        658     63       6/6   <- AUTOMATIC
M_2 > m                                    94     32       6/6   <- the cut
all M_i > m (i >= 2)                       94     32       6/6   (same set)
M_2 - m = d_3                              61     22       4/6   REJECTED
u_s = 1                                   509     55       5/6   REJECTED
s = 3                                     212     62       6/6   (weak)
V_2 <= V_3                                152     45       5/6   REJECTED
e - d = 1                                 578     40       6/6   (weak)
q <= 1                                    514     42       6/6   (weak)
delta_2 > 0 ; delta_1 > delta_2           658     63       6/6   automatic
M_2 > m AND integral pinned N >= 6 (UNI)   33     17       5/6   ((84,56) M2=64 dies at N>=6, as in #17 A.8)
```

At (75,50): `M_2 > m` leaves M_2 ∈ {55, 60}; the two M_2 = 60 rows (V_2 = 9, 20;
q = 9/11, 10/11; u = 20) have no integral N, so **(1)–(13) + M_2 > m + N ∈ ℤ
reproduces Moh's (75,50) output exactly** (55; V_2 = 2, 3). The 28 residual rows
beyond the printed table (33 minus 5) are listed in §12; they are concentrated at
(100,40) (10 rows), (96,64) (5), (80,·) (4). This sharpens OPEN[MOH-PROGRAM]'s
bounded quantity from 652 rows to **28 rows** *conditional on `M_2 > m`*.

### 2.3 MEASURED: the same filter on the (1)–(13) space, 48 ≤ D ≤ 120

```text
   D   groups  M2>m  alive N>=6 (UNI)  alive mixed [6,16]
  48       2     0        0     0
  54       2     0        0     0
  60      15     1        0     0
  63       2     0        0     0
  64       9     1        1     1     (Moh's row; Appendix II)
  72      46     4        0     0
  75       5     2        1     1     (Moh's rows)
  80      40     6        4     4
  81       2     1        0     0
  84      38     7        2     2
  88       1     0        0     0
  90      62    11        1     1
  96     157    17        6     6
  99       7     2        1     1     (Moh's row)
 100      57    15        9     9
 102       3     0        0     0
 104       3     0        0     0
 105      14     5        0     0     <- EMPTIED (trio dead: M_2 = 28, 40 < 70)
 108     125    18        5     2     N in [6,16]: m=72 M=[84,88,106] V_s=3 (N=9);
                                                   m=72 M=[84,104,106] V_s=3 (N=16)
 110       3     0        0     0
 112      71    14        5     5
 114       3     0        0     0
 117       7     3        1     1     m=78 M=[91,115] V_s=11 (N=8)
 120     515    72       27    26
 TOTAL  1189   179       63    59
```

Twelve degrees empty; the pinned-N programme on the filtered space has **63 live
groups at D ≤ 120** instead of 670. The live D = 108 pair is the new first target
if the filter is a theorem. (Knapsack: `uni_hits`/`mixed_hit` from the tool,
N_min = 6 read from the frontier line, never re-derived.)

### 2.4 The Abhyankar–Moh semigroup is not the filter (MEASURED; refutes Q3(d) as posed)

With r_0 = n, r_1 = m, n_j = d_j/d_{j+1}, r_{j+1} = n_j r_j − (M_{j+1} − M_j)
(chain extended by M_{s+1} = n−1 when d_{s+1} > 1), both planar-semigroup
conditions — n_j r_j ∈ ⟨r_0..r_{j−1}⟩ in standard form (0 ≤ c_i < n_i) and
r_{j+1} < n_j r_j — hold on all 658 rows. The inequality is automatic from
M_{j+1} > M_j; the membership is automatic in range because the Frobenius bound
of ⟨e,d⟩ is tiny against (e−1)d(K/d_3). (The exact statement of the AM theorem
over the ground field k(x) is SOURCE-UNVERIFIED here — [A-M.1] p.68 not opened —
but the test is unconditional: whatever the theorem says, it removes nothing.)
Conductor/genus: c(Γ) ≤ (n−1)(n−2) is likewise far from binding ((64,48):
c = 1430 vs 3906). So the semigroup route (Bresinsky/approximate roots) is
**closed as the missing filter**; the AM *frame* (one-place curve over k(x))
stays and is the right frame (§4).

### 2.5 Where `M_2 > m` could come from (three hypotheses, each with a test)

H1 (Moh §2–§3, SOURCE-UNVERIFIED): a statement that the tree data of the n
conjugates Ω_i f — which are determined by {M_j, d_j} — must be compatible with
Lemma 2.1's constant coefficients *and* the Ω-symmetry in a way that forbids a
non-K-divisible exponent in (−m, m]. Test: read pp.152–160 (the tree-data
section) for an inequality on M_2; one hour of a second reader on the PDF.
H2 (Prop 5.6 route, p.189): the "trivial observation" that g and T_1^ψ have no
common factor forces a term x^l in g and ord g(σ_1) ≤ −l; a similar argument at
the level of the top disc D_s with the π-root σ_s may force M_2 > m. Test: desk
derivation, half a day.
H3 (it is *not* a theorem but a consequence of (1)–(13) + something else that
Moh's program had): falsify by finding, at D ≤ 200, a (1)–(13) skeleton with
M_2 ≤ m that survives every other known necessary condition and constructing a
Keller-like object to some order for it. Weakest.

**Outcome map.** If `M_2 > m` is a theorem: D_min ≥ 108 unconditionally on the
frontier, 12 degrees empty, and the census-rebase residual is 28 rows at
n ≤ 100 (Moh killed those by Appendix-II-type case work, so they are the
calibration set for the descent engine). If it is refuted: the 94-row cut is an
artefact and OPEN[MOH-PROGRAM] stays at 652; the descent mechanism (§3) is
unaffected. Either way the cheapest test on the census is already run (above).

### 2.6 Is Moh's program a theorem, a sieve, or case-by-case? (direct)

A **sieve followed by descent**. The printed sieve leaves an infinite family (no
D > 100 empties, delta (h)); `M_2 > m` — if a theorem — still leaves an infinite
family (179 groups at D ≤ 120 before N, 63 after). Moh's finishing move at every
class is the descent to a monomial-Jacobian pair plus polynomiality at two
π-roots; that *is* uniform in form (Prop 6.3/6.4 for u_s = 1, the minor-disc
dichotomy otherwise) even though he executed it by hand. So the answer to "what
should the all-degree program be" is: **make the descent recursive and typed,
and let the interpolation identity act on the descended pair, where the
coefficient count is O(10)–O(20).**

## 3. Q2 — the D = 105 trio: cheapest exact discriminators

Groups (packet item 6; K = 35, (d,e) = (2,3), m = 70):

```text
G1  M=[28,103] V_s=5  d_3=7  u_3=2  q=1/2   N in 6..12
G2  M=[28,103] V_s=6  d_3=7  u_3=1  q=9/13  N=9    -> Prop 6.3: (15,10), [P,Q] ∝ γ^4, M_2' = 4
G3  M=[40,103] V_s=4  d_3=5  u_3=1  q=9/17  N=9    -> Prop 6.3: (21,14), [P,Q] ∝ γ^2, M_2' = 8
```

1. **Route A (numerical, free):** all three have M_2 < m. If `OPEN[M2-ABOVE-M]`
   closes positive, the trio is dead with no further computation.
2. **Route B (descent, desk):** G2 and G3 satisfy u_3 = 1, so Prop 6.4 gives
   δ*_2 ≥ v_3 and Prop 6.3 applies verbatim (hypotheses: g monic in y,
   deg g = deg_y g, δ_s = −1 — all in Moh's gauge). The descended objects are
   polynomials P = ḡ(σ), Q = T̄_1^ψ(σ) ∈ k[γ,π], monic in π of π-degrees (15,10)
   resp. (21,14), with [P,Q] = −(1/b)γ^{4} resp. γ^{2}. Discriminator: does such a
   pair exist with the inherited data (M_2' = 4, d_2' = 5) resp. (M_2' = 8,
   d_2' = 7)? Moh's own (15,10; γ²) run (pp.210–211) is the template: write
   P = h³ + 3βh + …, impose cancellation of the θ^{-1}-series, count. Expected
   size: 10–25 unknowns, a handful of quadratic equations — **desk sympy, hours**.
   GAP to close first: Prop 6.3 fixes π-degrees, not γ-degrees; the Newton
   polygon of (P,Q) in (γ,π) must be read off the tower (δ_3 = −1, δ_2, δ_1 and
   the V's) — `OPEN[DESCENT-POLYGON]` (§11). A kill of G2 and G3 by Route B leaves
   G1 alone at D = 105.
3. **Route C (G1, u_3 = 2):** Prop 6.3's hypothesis δ*_2 ≥ v_3/u_3 = 5/2 is not
   automatic; use Moh's (99,66) dichotomy: the unique π-root of the minor disc
   D*_2 has g_σ(π) either a power of a linear form or a d-th power of a polynomial
   with exactly two roots, and each alternative descends (to a monomial Jacobian
   γ^k with a different k, or through the Ω-transformation). This is the one
   genuinely new piece of uniformisation needed and it is the content of
   `OPEN[MINOR-DICHOTOMY]`.
4. **Route D (global interpolation, the packet's item 6):** unknown/condition
   count per order at the *undescended* skeleton: n = 105 values F_i, y-degree
   m = 70 interpolant, n − m = 35 degree-killing relations at each x-order plus
   polynomiality of 71 coefficients; the Sol lane owns the exact counting. My
   expectation from Appendix II's numbers (3370–7348 raw coefficients versus
   10–22 after descent): a counting kill at the undescended level needs orders
   in the tens, while the descended problem kills at order ≤ 3. Route D is the
   last resort, not the first.

**Verdict on the flagship seat:** NO for the trio as posed. A trio kill buys
D_min ≥ 108 (next live: the two D = 108 groups above under the filter, or 76
groups without it). The seat is better spent on the *mechanism* (§8, first lane),
which kills the trio as a by-product if it works.

## 4. Q3 — the all-degree frame

**Answer: skeleton realisability is the right *object* but the wrong *level*.**
The right frame is Moh §2 itself: (f,g) is a rational curve with one place at
infinity over k(x); its Puiseux characteristic is the skeleton; the Jacobian
condition enters the expansion exactly once (Lemma 2.1: constant coefficients
below n−1, a linear coefficient at n−1). Everything the campaign proved on the
boundary (JAC-FIBRE, D1-PIN, STAR-ABC, NO-RESIDUE) lives in the constant part;
the datum a uniform theorem must use is the x-linear coefficient f_{n−1}(x) and
the minor-disc data it generates. The descent (Prop 6.3) is the operation that
*moves* that datum into the constant part of a smaller pair (Jacobian γ^{v_s−2}
is the shadow of f_{n−1} being linear in x) — which is why Moh could finish by
hand.

Dispositions of the coordinator's candidates:
* (a) D-module/Picard–Fuchs: **LOWER.** The interpolant's differential
  operator has regular singularities only at the roots of g − c_2 and at ∞ with
  exponents read from the skeleton; the irregularity at ∞ is bounded by the
  pole orders, all O(1) by PIN-NOT-CEILING. No cofinal invariant grows with D.
* (b) Dessin tower rigidity: **UNCHANGED** (receiver only). STAR-ABC is promoted
  and always realisable; rigidity of a Galois orbit of Davenport–Stothers pairs
  is a real question but bounds V_2, not D.
* (c) Characteristic p / Cartier: **LOWER.** Row 20 was run (1608Z synthesis §2:
  p-curvature of the inverse-Jacobian connection vanishes identically); the
  Cartier form of NO-RESIDUE is a diagnostic, not a bound.
* (d) Semigroup at infinity: **RETYPE.** Refuted as the missing filter (§2.4);
  RAISE the AM one-place frame (this section) as the organising frame.
* (e) Numerical realisation of a survivor: **LOWER** until Routes A–C have run;
  if any descended small pair (15,10; γ⁴) or (21,14; γ²) *exists*, that is the
  first positive signal and it costs hours, not a seat.
* (f) "The census never empties": **ANSWERED YES** for (1)–(13) + integrality
  (delta (h)) and, MEASURED here, still yes with `M_2 > m` (63 groups at D ≤ 120,
  growing). Consequence stated: the proof side must use f_{n−1}(x) (Lemma 2.1),
  i.e. the descent, not more skeleton arithmetic.

## 5. Q4 — software: the skeleton descent engine (build this week)

Smallest useful version (one file beside `moh_skeleton_full.py`, stdlib + fractions):
1. Input: a (1)–(13) group (n, m, M_*, V_*) from `groups_of`. Flags: `M2>m`,
   `u_s` (= d_s − V_s), N-set (from `uni_hits`/`mixed_hit`).
2. If u_s = 1: emit the descended datum (n' = n/d_s, m' = m/d_s,
   M_i' = M_i/d_s for i ≤ s−1, d_i' = d_i/d_s, k = v_s − 2, Jacobian γ^k) and
   recurse: re-run the (1)–(7)-type gcd/window checks on the descended data
   (they are Puiseux-characteristic facts, Jacobian-independent) and re-check
   `M_2' > m'`. Type the recursion `MEASURED` until `OPEN[DESCENT-CLOSURE]`
   (§11) says which of (8)–(13) survive a monomial Jacobian.
3. Terminal receiver: a table of (n', m', k) with a status from row 1's GGV
   corner-family engine (`EMPTY-CERTIFIED` / `OPEN`) — the campaign already owns
   [P,Q] = x^k certificates in this degree range; wire them, do not recompute.
4. Gates: (G1) Moh's six rows reproduce the p.207 transformed table to the unit
   ((16,12,13; X), (21,14,16[18]; X), (15,10,11; X²)) — fail-closed; (G2) every
   descended datum has integral M_i'/d_s (a transcription check); (G3) the
   engine must NOT empty D = 64, 75, 84, 99 by itself (Moh needed Appendix II).
5. Negative control against a vacuous pass: feed the (1)–(7) superset; the
   engine must flag > 90 % of its groups as `M2<=m` or `u_s>1`, and must keep the
   six printed rows through every stage. If a stage kills a printed row, the
   stage is wrong, not Moh.
Cost: a day of one Grok seat; runs to D = 200 in seconds.

The order-by-order interpolation engine the packet asks for should be built
**on the descended pair** (unknowns O(10)), not on the degree-105 pair; its
counting bound per skeleton is then Moh's own coefficient count (17/10/22/11).

## 6. Disposition vector — APPROACHES.md (changes only)

* Row 1 (GGV corner families, [P,Q] = x^k): **RAISE.** Prop 6.3 lands every
  u_s = 1 skeleton in this world at degree n/d_s ≤ n/4 with k = v_s − 2. The
  farm's certificates become kill conditions for Moh skeletons.
* Row 5 (JvdK degree descent): **RETYPE → "monomial-Jacobian descent".** The
  objection ("amalgam rigidity never bites on non-automorphisms") does not apply
  to Moh's descent, which is an inversion-lemma change of variables plus a
  specialisation, and it *does* bite on non-automorphisms (Appendix II).
* Row 6 (Abhyankar–Moh one-place): **REOPEN / RAISE.** The two surveys said it
  was tried "on the wrong object (fibres are multi-place)". The right one-place
  object is Moh's curve F(f,g) = 0 over k(x) (p.150): its semigroup is
  ⟨n, m, r_2, …⟩ with r_j = n_{j−1}r_{j−1} − (M_j − M_{j−1}); the AM conditions are
  automatic (§2.4) but the frame is the one in which Lemma 2.1 lives.
* Row 16 (D-module index) and row 45 (differential Galois): **LOWER** (Q3(a)).
* Row 20 (char p): **UNCHANGED** (already run; diagnostic only).
* Row 25 (dessins/passports): **UNCHANGED**; STAR-ABC closed it positively.
* Row 36 (guided CE search): **RAISE slightly** as the receiver for descended
  small pairs — a (15,10; γ⁴) search is desk-scale and structured.
* All other rows: unchanged.

Queued fronts: census-rebase second reader — **CONTINUE, RAISE**, with §2 as
input (two reads of pp.152–160 for H1); branch-orbits v2 — **LOWER** behind the
descent engine; DISC-COUPLING relaunch on a D = 105 survivor — **STOP** until
Routes A–B have run (its target set may be empty); reducible-branch review —
continue; web sweep — continue with two named queries (§8).

## 7. Reranked bottlenecks

Proof side: (P1) `OPEN[M2-ABOVE-M]` — a theorem or a refutation; (P2)
`OPEN[DESCENT-CLOSURE]` — which numerical conditions survive the descent so the
recursion is typed; (P3) `OPEN[MINOR-DICHOTOMY]` — the u_s > 1 branch in uniform
form; (P4) the interpolation engine on descended pairs; (P5, demoted) the global
interpolation counting at the undescended degree.
Disproof side: (C1) existence of a descended small pair (15,10; γ⁴) or
(21,14; γ²) with the inherited characteristic data — the first *cheap* positive
signal possible; (C2) the 28 residual rows at n ≤ 100 (§12) — if one of them
descends to an existing monomial-Jacobian pair, Moh's completeness claim is
wrong and the campaign has a target list below 100; (C3) the two D = 108 groups
with N ∈ {9, 16}.

## 8. New avenue, new cross-connection, attacks, experiment

**NEW avenue — `DESCENT-RECURSION`.** Iterate Moh's Prop 6.3: a degree-n Keller
skeleton with u_s = 1 becomes a degree-(n/d_s) skeleton with Jacobian γ^{v_s−2};
if the descended pair again has u_{s'} = 1 descend again; each step divides the
degree by ≥ 4. The recursion terminates in a degree range where monomial-Jacobian
pairs are classifiable (row 1's certificates, or Moh's own hand method). The
proof-side theorem to aim at: *every u_s = 1 skeleton descends to a pair that
the boundary theory (JAC-FIBRE etc., which is Jacobian-monomial-tolerant since
ord J enters additively) kills or classifies*. The counterexample-side use: a
descended pair that exists lifts only if the inversion lemma is inverted — a
separate, explicit question (`OPEN[DESCENT-LIFT]`).

**NEW cross-connection.** Moh's Prop 6.3 (1983) and the GGV–Horruitiner
reduction to [P,Q] = x^k (row 1) are two reductions of a Keller pair to a
monomial-Jacobian pair; the campaign's (72,108) certificate machinery is the
receiver Moh lacked. Cheapest test: descend Moh's (75,50) row to (15,10; γ²) and
ask row 1's engine whether it empties (15,10; γ²) — Moh says it does (pp.210–211).
Agreement calibrates the bridge; disagreement is a bug on one side. Second
connection: Lemma 2.1 (f_{n−1}(x) linear in x) is the same fact as the
campaign's NO-RESIDUE/JAC-FIBRE at the top disc, read in the η-expansion; the
descent's exponent k = v_s − 2 is its shadow.

**Strongest proof attack.** Prove `M_2 > m` (H2 route: g and T_1^ψ coprime ⇒
a term x^l in g ⇒ an order inequality at the top π-root σ_s that forces the
first non-K-divisible exponent above m), then prove the descent preserves
(1)–(7) + `M_2 > m`; the recursion then bounds every skeleton by a finite
terminal table, and the terminal table is finite case-work of Appendix-II size.

**Strongest counterexample attack.** Take G2 (D = 105): build the (15,10; γ⁴)
pair ansatz in k[γ,π] from the tower (δ_3 = −1, δ_2, δ_1 = 11/26, V = (1,6)),
impose cancellation of the θ^{-1} series to all orders (a finite polynomial
system, Moh-sized), and solve exactly. A solution is the first positive signal
above D = 100 at desk cost; lifting it is `OPEN[DESCENT-LIFT]`.

**Decisive experiment / software acceleration.** §5's engine, gated by the
p.207 table. One day. It decides at once whether the frontier is D ≥ 108
(conditional on `M2-ABOVE-M`) and hands the trio's two u_s = 1 groups to a
desk lane as explicit small problems.

## 9. Campaign-systems check — UPGRADE (state freshness / retrieval cost)

Evidence: the packet was frozen with "Moh page images NOT on this machine";
`refs/` was synced at 10:08Z, so every blind submitter *may* be reading a source
the packet says is absent, and the coordinator cannot tell who did. Smallest
useful fix: `ops/lane.sh` writes into the `.run.v2` receipt the SHA-256 of every
file under `refs/` that the lane opened (bind `refs/` read-only through a logging
shim, or simply hash `refs/*` at launch and at seal and diff). Test: relaunch the
fg smoke lane with one `refs/` read and confirm the receipt lists it. Cost: an
hour; benefit: source-read claims become auditable instead of self-declared.

## 10. Idea cards (three)

**CARD 1 — M2-ABOVE-M.** Target: OPEN[MOH-PROGRAM]. Mechanism: prove/refute
`M_2 > m` from Moh §2–§5 (H1/H2). Dependencies: the PDF (present), Lemma 2.1,
Prop 5.6's coprimality remark. Cheapest discriminator: a second reader hunts the
statement on pp.152–160 and pp.178–187 (2 h); in parallel a desk derivation via
the top π-root (half a day). Outcomes: theorem → D = 105 empty, 12 degrees empty,
OPEN[MOH-PROGRAM] bounded 28 rows; refuted → discard the 94-row cut, keep §3
routes B–C. Stop: 1 day. Information gain: highest of the round (it is the
frontier).

**CARD 2 — DESCENT-TRIO.** Target: the D = 105 trio and the descent mechanism.
Mechanism: Prop 6.3/6.4 on G2, G3 → explicit (15,10; γ⁴), (21,14; γ²) problems;
solve by Moh's pp.210–211 method in sympy. Dependencies: OPEN[DESCENT-POLYGON]
(γ-degrees from the tower) — must be closed first, desk. Discriminator: the
polynomial system's consistency. Outcomes: inconsistent → G2, G3 dead, and the
method is validated on two fresh cases; consistent → first positive signal;
lift question opens. Stop: 2 days. Gain: high on both sides.

**CARD 3 — DESCENT-ENGINE (software).** §5. Dependencies: none beyond the
tool. Discriminator: gates G1–G3. Outcomes: per-degree terminal table to
D = 200 with typed status; a machine-checkable version of "Moh's program".
Stop: 1 day of Grok. Gain: turns OPEN[MOH-PROGRAM] into a per-row ledger.

## 11. OPENs raised (each with its bounded quantity; ops/open_collision.py contract)

OPENS RAISED

* `OPEN[M2-ABOVE-M]` — decide whether every Keller skeleton in Moh's gauge has
  M_2 > m (bound: the number of (1)–(13) rows with M_2 ≤ m that are realisable;
  MEASURED cut 658 → 94 at n ≤ 100, 1,189 → 179 groups at D ≤ 120, keeps 6/6
  printed rows).
* `OPEN[DESCENT-CLOSURE]` — determine which of Moh's conditions (1)–(13) and
  `M_2 > m` hold for the Prop 6.3-descended pair with Jacobian γ^{v_s−2} (bound:
  the list of surviving conditions; at least (1)–(5) are Puiseux facts).
* `OPEN[DESCENT-POLYGON]` — compute the γ-degree / Newton polygon of the
  descended pair from the tower data (bound: deg_γ P and deg_γ Q as functions
  of (δ_j, V_j, d_j)).
* `OPEN[MINOR-DICHOTOMY]` — state Moh's p.209 dichotomy for the minor-disc
  π-root (g_σ(π) a power of a linear form, or a d-th power of a polynomial with
  two roots) as a theorem for every u_s > 1 skeleton (bound: the number of
  alternatives, conjecturally two).
* `OPEN[DESCENT-LIFT]` — decide whether a monomial-Jacobian pair with the
  descended data lifts to a Keller pair of degree (n, m) (bound: the dimension
  of the lifting fibre; 0 or empty expected).
* `OPEN[MOH-PROGRAM]` SHARPENED, not re-raised — bound: at most 28 excess rows
  at n ≤ 100 conditional on `OPEN[M2-ABOVE-M]` (was 652 unconditionally), §12.

FALLACY-v2 check: no exit price asserted (no `charge_basis` line needed); no
flag/place/series identification; every count is a floor on the kill (the
filters are necessary conditions or MEASURED candidates, never attainment);
`sat()`/quotient rules not exercised (no ideal computation here); N_min = 6 read
from the frontier line; the AM semigroup conventions are declared (§2.4) and the
theorem's exact scope typed SOURCE-UNVERIFIED; no D ≤ C(N) inferred anywhere.

## 12. Reproducibility — the predicates, and the 28 residual rows

```python
# on Skel S from box/moh_skeleton_full.py (census(n, Kmin=2, full=True) for n<=100)
M2_above_m = lambda S: S.M[2] > S.m
u_s        = lambda S: S.d[S.s] - S.V[S.s]
def am_semigroup(S):                       # r_0=n, r_1=m, r_{j+1}=n_j r_j-(M_{j+1}-M_j)
    Ms=[S.M[i] for i in range(1,S.s+1)]; ds=[S.d[i] for i in range(1,S.s+2)]
    if ds[-1]>1: Ms.append(S.n-1); ds.append(1)
    nn=[ds[i]//ds[i+1] for i in range(len(Ms))]; r=[S.n,-Ms[0]]
    for j in range(2,len(Ms)+1): r.append(nn[j-2]*r[j-1]-(Ms[j-1]-Ms[j-2]))
    def rec(i,rem): return rem>=0 and rem%r[0]==0 if i==0 else \
        any(rec(i-1,rem-c*r[i]) for c in range(nn[i-1]) if rem-c*r[i]>=0)
    return all(rec(j-1,nn[j-1]*r[j]) and (j==len(Ms) or r[j+1]<nn[j-1]*r[j]) for j in range(1,len(Ms)+1))
# integral pinned N (UNI): uni_hits([(S.V[2], S.q(), S.u)], 6, None)
```

Residual at n ≤ 100 after (1)–(13) + M_2 > m + integral N ≥ 6 (UNI), printed
rows excluded (28; `n m M V u_s q N`):
```text
75 45 [55,73] {2:2,3:4} 1 1 [6,8,10,12] | 80 32 [52,78] {2:1,3:3} 1 1/2 [6]
80 48 [52,78] {2:2,3:3} 1 1 [6,8,10,12]  | 80 32 [56,78] {2:1,3:7} 1 1/2 [6,7]
80 60 [68,78] {2:7,3:3} 1 1 [7,14]       | 84 36 [54,82] {2:1,3:5} 1 7/6 [7]
84 60 [66,82] {2:3,3:5} 1 2 [6,12,18]    | 84 56 [70,77,82] {2:5,3:10,4:5} 2 1/2 [10]
90 36 [60,88] {2:3,3:5} 1 1 [6,9,12,15]  | 96 60 [66,94] {2:1,3:5} 1 5/3 [10,15]
96 72 [80,84,94] {2:7,3:6,4:3} 1 1 [7,14]| 96 64 [68,94] {2:2,3:3} 1 2/5 [8]
96 64 [76,94] {2:3,3:3} 1 3/7 [9]        | 96 64 [72,94] {2:2,3:7} 1 2/5 [8]
96 64 [80,84,94] {2:5,3:4,4:3} 1 1/2 [10]| 96 64 [80,88,92,94] {2:5,3:10,4:5,5:3} 1 1/2 [10]
98 42 [63,96] {2:1,3:5} 2 7/8 [7]        | 100 40 [88,98] {2:3,3:3} 1 1/2 [6]
100 40 [50,98] {2:1,3:8} 2 10/13 [10]    | 100 40 [50,98] {2:1,3:9} 1 10/11 [10]
100 40 [50,55,98] {2:1,3:8,4:4} 1 10/13 [10] | 100 40 [50,55,98] {2:3,3:8,4:4} 1 1 [6,9,12,15]
100 40 [50,65,98] {2:1,3:8,4:4} 1 10/13 [10] | 100 40 [50,75,98] {2:1,3:8,4:4} 1 10/13 [10]
100 40 [50,85,98] {2:1,3:8,4:4} 1 10/13 [10] | 100 40 [50,95,98] {2:1,3:5,4:4} 1 5/8 [10]
100 40 [50,95,98] {2:1,3:8,4:4} 1 10/13 [10] | 100 75 [85,98] {2:7,3:3} 2 1/2 [7]
```
Note 24 of the 28 have u_s = 1 and therefore descend by Prop 6.3 to pairs of
degree ≤ 25 with a monomial Jacobian — exactly the objects §5's engine
classifies. If Moh's completeness claim is right, all 28 die there.

## 13. Lanes — continue / redesign / stop; the single first lane

* `global-interpolation-sol56-20260902`: **REDESIGN** — keep the exact global
  conditions, but state them for a pair with Jacobian γ^k and apply first to the
  descended (15,10; γ⁴) and (21,14; γ²) objects of §3; the D = 105 undescended
  targets go last.
* `reducible-branch-review-grok46-20260903`: **CONTINUE** unchanged.
* `websweep-20260903T1010Z-grok46`: **CONTINUE**, add two queries: (i) any
  published uniformisation of Moh's Appendix II / Prop 6.3 descent (Moh's later
  papers, Abhyankar's "Expansion techniques"); (ii) Sathaye–Stenerson / Abhyankar
  planar-semigroup theorems over function fields k(x) (to type §2.4).
* Queued census-rebase second reader: **CONTINUE, RAISE**, charged with H1.
* Queued branch-orbits v2: **LOWER** (after the engine).
* Queued DISC-COUPLING relaunch: **STOP** pending Routes A–B.
* Box01: keep idle/stop (auxiliary census done); no AWS needed for anything here.

**The single first lane:** `M2-DESCENT` on an Opus frontier seat, 6 hours, with
the PDF: (1) prove or refute `M_2 > m` (CARD 1); (2) close OPEN[DESCENT-POLYGON]
and write the two descended trio problems explicitly (CARD 2, first half). Why
this one: it is the only lane whose *positive* outcome closes D = 105 and twelve
other degrees by theorem rather than by computation, whose *negative* outcome
costs nothing downstream, and whose by-product (two Moh-sized polynomial
systems) is the cheapest counterexample-side signal available above D = 100.

## 14. Typed block

```text
SUBMISSION   ideation-20260903T1015Z-fable5 (Fable 5), basis f5aa1caf
SOURCE       Moh 1983 PDF present and read (pp.148-151, 188-189, 196-202, 207-212)
MEASURED     AM semigroup automatic on 658/658; M_2 > m keeps 6/6, 658 -> 94 rows;
             D<=120: 1189 -> 179 groups -> 63 alive (N>=6), 59 in [6,16];
             D = 105 EMPTIED under M_2 > m; twelve degrees empty; D = 108: 2 groups
             in [6,16]; n<=100 residual beyond Moh's table: 28 rows (24 with u_s = 1)
NOT CLAIMED  that M_2 > m is a theorem; that Prop 6.3 descent preserves (8)-(13);
             any realisation; any D <= C(N)
READING      Moh's program = sieve + descent; the all-degree program is the
             typed descent recursion with interpolation on the descended pair
FIRST LANE   M2-DESCENT (Opus, desk, 6 h)
```

## 15. OPEN collision check (ops/open_collision.py, run before sealing; rc=0)

Blind-rule note: the tool is lexical and scans the whole banked corpus, so its hit
list below cites lines from other `ideation-20260903T1015Z-*` submissions and from
running lanes' partial reports. Those files were NOT opened by this lane and nothing
in this submission derives from them; the hits are review candidates for the
coordinator, never closures. The only banked hit on `OPEN[M2-ABOVE-M]` is the
n-on-the-tree review's p.202 legibility remark (unrelated to M_2 > m).

## COLLISIONS

status: CANDIDATES

### OPEN[M2-ABOVE-M]

- `xmodel/n-on-the-tree-review-grok46-20260902.md:228` — **`n=75` "OCR illegible" — REFUTED.** p.202, row `n=75`: `delta_2=1/5`, `delta_1=1/2 [1/3]`, perfectly legible (DR already read this crop; INT15 left `OPEN[DELTA75-BRACKET]` unpromoted). Def 5.1(3) gives `delta_1=1/2` at `V_2=3` (matches...

- `OPEN[DESCENT-CLOSURE]` (report:480): NONE

- `OPEN[DESCENT-POLYGON]` (report:483): NONE

- `OPEN[MINOR-DICHOTOMY]` (report:486): NONE

- `OPEN[DESCENT-LIFT]` (report:490): NONE

### OPEN[MOH-PROGRAM]

- `xmodel/branch-orbits-v2-grok46-20260903.md:341` — OPEN[MOH-PROGRAM] (census-rebase; untouched). 652 excess rows at n<=100.
- `xmodel/census-rebase-opus5-20260902.md:385` — > **`OPEN[MOH-PROGRAM]` (bounded quantity: 652 excess rows, 59 excess `(n,m)`
- `xmodel/census-rebase-opus5-20260902.md:960` — program encoded. Bounded quantity: **652 excess rows / 59 excess `(n,m)` classes
- `xmodel/census-rebase-opus5-20260902.raw.md:385` — > **`OPEN[MOH-PROGRAM]` (bounded quantity: 652 excess rows, 59 excess `(n,m)`
- `xmodel/census-rebase-opus5-20260902.raw.md:960` — program encoded. Bounded quantity: **652 excess rows / 59 excess `(n,m)` classes
- `xmodel/ideation-20260903T1015Z-gpt55.md:210` — best candidate for `OPEN[MOH-PROGRAM]` (bounded 652 excess rows at `n<=100`).
- `xmodel/ideation-20260903T1015Z-gpt55.md:297` — | 6 | raise | Abhyankar-Moh approximate roots and semigroups are now central to `OPEN[MOH-PROGRAM]` (bounded 652 excess rows). |
- `xmodel/ideation-20260903T1015Z-gpt55.md:352` — | census-rebase second reader on Moh PDF | raise/continue | Highest-value review debt for `OPEN[MOH-PROGRAM]` (bounded 652 excess rows). |
- `xmodel/ideation-20260903T1015Z-gpt55.md:584` — - `xmodel/census-rebase-opus5-20260902.md:385` -- > **`OPEN[MOH-PROGRAM]` (bounded quantity: 652 excess rows, 59 excess `(n,m)`
- `xmodel/ideation-20260903T1015Z-gpt55.md:586` — - `xmodel/census-rebase-opus5-20260902.md:960` -- program encoded. Bounded quantity: **652 excess rows / 59 excess `(n,m)` classes
- `xmodel/ideation-20260903T1015Z-gpt55.md:590` — - `xmodel/census-rebase-opus5-20260902.raw.md:385` -- > **`OPEN[MOH-PROGRAM]` (bounded quantity: 652 excess rows, 59 excess `(n,m)`
- `xmodel/ideation-20260903T1015Z-gpt55.md:592` — - `xmodel/census-rebase-opus5-20260902.raw.md:960` -- program encoded. Bounded quantity: **652 excess rows / 59 excess `(n,m)` classes
- `xmodel/ideation-20260903T1015Z-gpt55.md:595` — - `xmodel/ideation-20260903T1015Z-packet.md:74` -- 5. DECISIVE NEGATIVE -- OPEN[MOH-PROGRAM] (bounded: 652 excess rows, 59
- `xmodel/ideation-20260903T1015Z-grok46.md:672` — OPEN[MOH-PROGRAM] bounded quantity: 652 excess (1)–(13) rows and 59
- `xmodel/ideation-20260903T1015Z-opus5.md:761` — | `OPEN[MOH-PROGRAM]` (existing, bounded 652 excess rows) | **REPRICE: 80 excess rows / 11 excess classes at `n ≤ 100`** under MOH-4 (51 rows / 13 classes vs Moh's 6 / 4), if MOH-INCREMENT and MAJOR-MULT are accepted; 241 excess rows if ...
- `xmodel/ideation-20260903T1015Z-packet.md:74` — 5. DECISIVE NEGATIVE — OPEN[MOH-PROGRAM] (bounded: 652 excess rows, 59
- `xmodel/reducible-branch-review-grok46-20260903.md:280` — **CARRIED (not re-opened here).** `OPEN[COMPANION-DEGREE-FLOOR]`: bound `n_A^Y` from below at a degree-minimal counterexample; the integer lies in `[c, e(K − Σ_B V_2(B))]` with `c ≥ 2`. `GAP[HORIZONTAL-DEGREE]`: bound `mult_{[1:0:0]} Aba...

<!-- BODY-END -->
