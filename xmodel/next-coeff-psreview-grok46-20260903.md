# Hostile review + EXPERIMENT NEXT-COEFF — PS-GROWTH identities, and whether the `n−m−1` global traces are resultant coefficients over `Q`

Lane: different-model gate, Grok 4.6, 2026-09-03. Charged flagship
`xmodel/ps-growth-opus5-20260903.md` (drivers `box/psgrowth-drivers-20260903/`).
This report does not edit a canonical ledger and does not use `jc2-lean`.
No `ideation-20260903T1015Z-*` file was opened; no running lane's report was
opened.

Types: **CONFIRMED** / **GAP** / **REFUTED**; **PROVED-HERE/UNREVIEWED**;
**MEASURED**; **PARTIAL**.

---

## 0. Custody

Frozen SHA-256 of `/tmp/jc2-lane.oOvtyD/inputs` verified **before any input was
read**; 10/10 matched the charge.

```text
9ef022e87f7f0193861e667a6bdaf22df58c4200cafe0d96c73122291e5c3e83  ps-growth-opus5-20260903.md
ecc304f044bfef291b9ec619d342c0b1d6c68cf48cde66667ca5da0dfc906c1b  psgrowth.py
7c3ea309a8e929f4907b52cbaf6818d086adf6fe796a3ad3d8b6c64d7b720f09  leadcheck.py
b08b201ee6d53467ab93732d4702d5544c470f3f26e3f41d2aa519bc5eae82c0  resdeg.py
7800a756991f56cb7cc48831f7629238981b03d3d1c525e12df5d479de424281  existence.py
2d6d7495e33908cf0bd49877384c95581d8254ce471f30324eb2b18a0aa62aad  genfun.py
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  global-interpolation-sol56-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
e639fdbf5cdbdf0756d9d8287b52c0183b07e2bf8ab7d4b293c242ea2c35f37c  exact-n-rigidity-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  bottomode.py
```

Also consumed (tooling, not reports): `box/moh_skeleton_N.py`,
`box/tfe-drivers-20260902/control4.py`,
`box/globalinterp-drivers-20260902/globalinterp.py` (DEG block).
Files written: `box/nextcoeff-drivers-20260903/` and this report.

---

## 1. Verdict, up front

```text
PART A.  The identity family PS-0, LEMMA EJ, PS-1' (no hypothesis on J),
PS-1c, LEMMA DEG, PS-2, PS-3 under (KEL), PS-3+, TRACE-CONSTANT,
TRACE-CONSTANCY, the Newton-polygon certificate for c_max, the RES-DEGREE
correction (RD-1)/(RD-2) with witness (y+1, y^3+xy), the (2,3,2) retraction,
and the D=105 arithmetic correction K1=10, are CONFIRMED.  Driver reruns
reproduce every advertised count (1495/0, 10/0, 32/0, 14/0, 108/0).

         Three load-bearing GAPs, none of which kills the family:
         (G1) PS-3's non-proper step writes "ord_t g_y = -δ^0 < -1"; that
              identity is false as written and is not needed.  Repair: JAC-FIBRE
              on the first non-constant term of f(τ).
         (G2) THEOREM RESIDUE-LEAD's (d/κ)·ptilde_{k+1} is verified only as a
              vanishing/attainment set on the (1,e,1) family, not as a leading
              coefficient.  Φ(δ_1)=1 and the Galois condition ARE confirmed.
         (G3) Two fail-closed holes in the drivers (PS-0 is `cond or True`;
              existence.py asserts "decided", not "GB ≠ {1}"), and genfun.py
              never tests a composition.

         K = d_2 is not "invisible".  It enters as e = n/d_2 and as the
         reduction (d,e) = (m,n)/d_2; on the elementary compositions it also
         equals the Galois orbit size ν.  What is true, and is the reading that
         survives, is that the identity family cannot produce a D-ceiling:
         PS-3 bounds e through c_max = q_max/e, never K, and D = K e.

PART B.  PARTIAL, and the "so that" in the charge splits.

         YES  — every coefficient of R_k and of the coordinator's n-m-1
                moments M_r = Tr(f τ^r / g_y) is a remainder coefficient in
                Q[x,c], computed with no Puiseux, no exponent semigroup, and
                no outer/inner split.  On every charged control, M_r = 0 for
                0 ≤ r ≤ n-m-2 and M_{n-m-1} = 1 exactly.

         NO   — the coefficient at x-order (k+1)c_max − 1 − j is NOT a
                function of the tower data down to level j only.
                First mixing coefficient: B6, k=8, R_8 = −2c  (a constant,
                slack against bound 1/2).  Invisible to the bottom star and
                to chi_N = T^6+x; it is the T^3-term of the level-2
                composition.  The next mixing, B6 k=10, R_10 = −1, is not
                even in the nested-radical truncation (T^3−c)^2+x; it needs
                the −T coming from the "y" in g = y+u^3.

         Re-base globalinterp.py onto remainder arithmetic in
         Q[x,c][y]/(g−c) and, when chi is known, onto [T^{n−1}](T^k mod chi).
         Do not advertise a jet-of-the-tower dictionary, and do not claim a
         g-alone resultant: Res_y(g−c, T−f) still needs f.
```

No new exit price is asserted. No `charge_basis` line is due.

---

## 2. Driver reruns (MEASURED)

All six charged drivers were re-run from the frozen copies in
`box/nextcoeff-drivers-20260903/` (import path pointed at that directory).
Whole battery: 71 s wall, one core, well under 1 GB.

| driver | advertised | this rerun | match |
|---|---|---|---|
| `psgrowth.py 20` | 1495 / 0 | **1495 / 0** | yes |
| `leadcheck.py` | 10 / 0 | **10 / 0** | yes |
| `resdeg.py` | 32 / 0 | **32 / 0** | yes |
| `existence.py` | 14 / 0 | **14 / 0** | yes (see G3) |
| `genfun.py` | 108 / 0 | **108 / 0** | yes |
| `trio105.py` | trio K0=4, K1=10; census max K0 = 14, 62, 62 at D=48, 108, 120, median 2–3 | same table | yes |

`nextcoeff.py`: 8.90 s, 59 MB, 214 named checks. The 22 `FAIL` lines are
the dictionary mismatches of §5.3, not CAS errors.

Fail-closed holes, recorded because they nearly became findings:

- `psgrowth.py:174`: `check("PS-0 ...", Poly(...).is_multivariate or True)` is
  identically true. PS-0 itself is still true by construction (`chi ∈ Q[x,c][T]`,
  Newton stays in `Q[x,c]`), and the independent trace route matches for
  `k ≤ 8` on every `n ≤ 6` control.
- `existence.py:38`: `check("star %s existence decided", exists(*t) is not None)`
  never asserts `GB ≠ {1}`. The **print** says `EXISTS: True` for all twelve
  census types, including `(2,3,2)` in 0.11 s. That is the evidence; the
  counter is not fail-closed.
- `resdeg.py:57-59`: the per-Keller "charged form agrees/disagrees" check
  passes `True` unconditionally. The actual refutation is the separate NP1
  check, which does fire.
- `genfun.py:27`: `controls()[:6]` is A1–A6 only. Compositions untested there.
  This lane's B6 gate checks `GF-R == remainder` for `k ≤ 20`, 21/21.

---

## 3. PART A — item by item

Citations are `xmodel/ps-growth-opus5-20260903.md:LINE`.

### 3.1 PS-0 (ll.119–127) — CONFIRMED, with G3

Under (MON), `A = R[y]/(g−c)` is free of rank `n`, `chi` is monic in `R[T]`,
and `P_k = tr(μ_f^k) ∈ R`. Under (SEP), `chi(T) = ∏(T − f(x,τ_i))` with no
lc correction. Repair the driver: drop `or True`. The theorem does not
depend on the broken check.

### 3.2 LEMMA EJ (ll.129–138) — CONFIRMED

`g−c` monic with simple roots ⇒ `g_y(τ_i) = ∏_{j≠i}(τ_i−τ_j)`. Lagrange
interpolation of the normal form `h̄` (deg_y `< n`) at the `τ_i` and comparison
of `[y^{n-1}]` gives
`∑ h(τ_i)/g_y(τ_i) = [y^{n-1}] h̄`. Both sides are `R`-linear; `h` and `h̄`
agree at every `τ_i`. Scope: `Tr(h/g_y)` is a priori over `Frac(R)` after
inverting `disc_y(g−c)`; (SEP) supplies that, and the right-hand side shows
the trace lands in `R`. No repair.

### 3.3 PS-1' / PS-1 / mixed partials of `log chi` (ll.144–167) — CONFIRMED

JAC-FIBRE `(★)` is `d/dx f(x,τ_i) = J(x,τ_i)/g_y(x,τ_i)`, obtained from
`τ_i' = −g_x/g_y` with **no** hypothesis on `J`. Then
`dP_{k+1}/dx = (k+1) Tr(J f^k / g_y)`, and EJ finishes. Under (KEL), `J`
comes out. The generating-function form (GF-P)/(GF-R) is the equality of
mixed partials of `log chi`; `genfun.log` confirms it on A1–A6 to `T^{-9}`
(108/0), and this lane confirms (GF-R) against the remainder on B6 for
`k ≤ 20`. PS-1 with constant `J` is refuted at `k=0` on all four charged
non-Keller rows (MEASURED, `psgrowth.log`).

### 3.4 PS-1c (l.173) — CONFIRMED

At fixed `x`, `dτ_i/dc = 1/g_y`, so `dP_k/dc = k ∑ f^{k-1} f_y / g_y =
[y^{n-1}]((f^k)_y)`. No hypothesis on `J`. Checked in the driver for
`k ≤ 6` on every positive control.

### 3.5 LEMMA DEG, quantifier order (ll.198–212) — CONFIRMED (attack (a))

Write `Q = ∑_j a_j(c) x^j`, `d = max{j : a_j ≠ 0}`. For `c_2` outside the
finite set `{a_d = 0}` one has `deg_x Q(·,c_2) = d = deg_x Q`. The three
finite sets avoided per `k` — (i) `disc_y(g−c)=0`, (ii) vanishing of the top
coefficient of `P_{k+1}` or `R_k`, (iii) jumps of the branch profile
`{δ^0_i}` — are the zeros of nonzero polynomials in `c` (leading coefficients
of `chi`'s `a_j`, of `R_k`, and the discriminant). Their intersection is
cofinite, hence nonempty. The bound `B = (k+1)c_max − 1` uses the **generic**
`c_max` (Newton polygon of `chi` at generic `c`); specialisation can only
drop `deg_x`, so an upper bound at a generic `c_2` is an upper bound on the
bivariate `deg_x`. Avoiding (ii) is load-bearing: without it one would bound
a specialised degree that may be strictly smaller than `deg_x Q`. The
quantifier order (choose `c_2` after `k`) is stated and is correct. The bound
does **not** depend on the auxiliary `c_2`.

### 3.6 PS-2 (ll.218–223) — CONFIRMED

`−ord_t ∑ f(τ_i)^{k+1} ≤ (k+1) max γ_f`; LEMMA DEG converts this to
`deg_x P_{k+1}`. No (KEL). No attainment of `N` is claimed. The inequality
`c_max ≤ N` is the trivial `max ≤ sum` of nonnegative terms.

### 3.7 PS-3 / PS-3+, proper branches (ll.225–240) — CONFIRMED under (KEL)

Under (KEL), `d/dx f(τ) = J/g_y` with `J ∈ k_0^*`. If `f(τ) ∼ a t^{-c}` with
`c ≠ 0`, then `d/dx = −t^2 d/dt` gives `ord_t(d/dx f) = 1−c`, hence
`ord_t g_y = c−1` and
`−ord_t(f^k/g_y) = (k+1)c − 1`. Summing and LEMMA DEG give PS-3; integrality
gives PS-3+. The route through `dP_{k+1}/dx` is equivalent up to the constant
case, which the direct proof avoids.

### 3.8 PS-3, non-proper case — GAP in the writeup, conclusion OK (attack (b))

The text (ll.235–236) says: at a non-proper branch,
`ord_t g_y(τ) = −δ^0 < −1` and `γ_f ≤ 0`, so the same expression is `< −1`.

That identity is not a theorem of (MON)+(SEP)+(KEL), and it is false on the
paper's own non-Keller witness: `g = y^3+xy`, `τ_0 ∼ c/x` has `δ^0 = 2` but
`g_y ∼ x`, so `ord_t g_y = −1 ≠ −2`. (Not a counterexample to PS-3, which
needs (KEL); a counterexample to the cited identity.)

**Repair.** Under (KEL), JAC-FIBRE still holds. Non-proper means `ord_t f ≥ 0`.
`J ≠ 0` forbids `f` constant on the branch, so `f = a_0 + b t^λ + ⋯` with
`λ > 0`, `ord_t(d/dx f) = λ+1 > 1`, `ord_t g_y = −(λ+1) < −1`, and
`−ord_t(f^k/g_y) < −1`. No `δ^0` required. If every branch is non-proper then
`c_max = 0` and the same estimate gives `R_k ≡ 0`. The automorphism library
has no non-proper Keller fibre (`resdeg.log`: `shed_0 = 0` on all ten).

### 3.9 TRACE-CONSTANT / TRACE-CONSTANCY / PS-3-SHARP (ll.176–178, 246–268)

- TRACE-CONSTANT: `R_0 = 0` for `n ≥ 2`, so under (KEL) `P_1` is
  `x`-independent. **CONFIRMED**; it is the `k=0` case of PS-1.
- TRACE-CONSTANCY: if `km ≤ n−2` then `f^k` is already reduced.
  **CONFIRMED**, trivial, needs (GAU) for `deg_y f = m`.
- PS-3-SHARP: `c_max = q_max/e` from D1-PIN + FRONTIER-EXACT + DETECTOR-NULL.
  **CONFIRMED as a deduction** from promoted D1-PIN (integration #17 A.3–A.4).
  The extra `δ_1 ≥ 0 ⇒ c_max ≤ d/(d+e)` is correctly marked SOURCE-UNVERIFIED
  and is **false** on `(y, x+y^3)` (`δ_1 = −1/3`, `c_max = 1/3 > 1/4`). Quote
  `c_max = q_max/e`. Trio arithmetic: `q=1/2`, `e=3`, `c_max=1/6`,
  `K0=4`, `K1=10`, so `R_11` may have `deg_x 1`. **CONFIRMED**,
  `trio105.log`.

### 3.10 Newton-polygon certificate for `c_max` (ll.298–309) — CONFIRMED

`chi = T^n + a_1 T^{n-1} + ⋯ + a_n`, `ord_t a_j = −deg_x a_j` at generic `c`,
slopes of the lower hull of `{(j, ord_t a_j)}` are `{ord_t f(τ_i)}`, and
`c_max = max(0, max_j deg_x a_j / j)`. This is Newton–Puiseux on `chi`, no
tree. Reproduced: D15 gives `c_max = 1/15` and `{γ_f} = {1/15}^{15}`, matching
exact-n-rigidity §6(c) row 4. On every charged control the polygon agrees with
the composition description (one slope, `n` equal parts).

### 3.11 THEOREM RESIDUE-LEAD (ll.369–414) — CONFIRMED as an attainment theorem; GAP as a coefficient formula (attack (c))

**The Φ step is correct.** Exact-n-rigidity defines
`Φ(δ) := δ − λ_f(δ) − λ_g(δ)`. Phi-TOWER gives `Φ(δ_1) = 1` under the Moh
tower hypotheses (`M_1 = −m`). At the general point of a bottom-major disc,
`g(σ_1(π)) = t^{λ_g}(p_g(π)+O(t^ε))` and `∂y/∂π = t^{δ_1}`, so
`g_y = t^{λ_g − δ_1}(p_g'+⋯)` and
`ord_t g_y = λ_g − δ_1`. Then `Φ(δ_1)=1` is exactly
`δ_1 − λ_f − λ_g = 1`, i.e. `λ_g − δ_1 = −λ_f − 1 = c − 1`. The parenthetical
"this IS `Φ(δ_1)=1`" is the right identification. It consumes promoted
D1-PIN / Phi-TOWER, which the paper flags.

**BOTTOM-ODE ⇒ `S_k = (d/κ) ptilde_{k+1}`.** Evaluating
`d p_f p_g' − e p_g p_f' = κ ∈ C^*` at a simple root of `p_g` gives
`p_g'(π_i) = κ/(d p_f(π_i))` (neither factor vanishes: `κ ≠ 0` and D1-STAR).
Then `S_k = ∑ p_f^k / p_g' = (d/κ) ∑ p_f^{k+1}`. Algebra CONFIRMED given
BOTTOM-ODE and simple roots.

**Galois survival `1−(k+1)c_max ∈ Z`.** If the bottom discs form one orbit
of size `ν` under `Gal(C⟨t⟩/C((t)))`, the leading term is
`t^θ · (∑ κ_i)` with `θ = 1−(k+1)c_max`. Invariance forces `θ ∈ Z` or the
sum vanishes. **CONFIRMED.** This is PS-3+ on the leading term. Multiple
orbits with the same `c_max` could cancel even when `θ ∈ Z`; the paper does
not claim otherwise, and the controls are one-orbit.

**What was actually checked.** `leadcheck.py` predicts
`{k : (e ν) | (k+1)}` against `{k : deg_x R_k = (k+1)c_max − 1}` on five
`(1,e,1)` pairs, 5/5, including D15 (`e=3`, `ν=5`, attained only at `k=14`;
`R_17, R_20, R_23` nonzero at a strictly lower order). That confirms the
**support** of the leading term, not the value `(d/κ) ptilde_{k+1}` times a
tower constant. On the A-series the leading coefficient is `±1`, consistent
with a tower constant of 1, but the prefactor is not isolated. **GAP** in the
coefficient claim; **CONFIRMED** as an attainment theorem on `(1,e,1)`.

D15's slack survivors are exactly the caveat the paper states (l.435–437):
RESIDUE-LEAD governs the top term only.

### 3.12 Negative reading / no D-ceiling (ll.484–521, 608–612) — CONFIRMED as a reading; K is not invisible (attack (d))

PS-3 is attained on a positive-density set of `k` on every `(1,e,1)` control
and at `k=14` on D15. A bound that is attained cannot be contradicted by a
lower bound of the shape `deg_x R_k ≥ φ(k,m,n)` with
`φ > (k+1)c_max − 1`. The `Θ(km)` expectation is **REFUTED** by D15
(`deg_x R_20 = 0` against `km = 100`). Route (P-b) is dead. **CONFIRMED.**

**Explicit dependence of `(m, n, q_max, e)` on the tower**
(`box/moh_skeleton_N.py:148-163`, exact-n-rigidity ll.31–35, 297–298):

```text
d_1 = n
d_2 = K = gcd(m,n)            ← this is the d_2 of the charge
d_{j+1} = gcd(d_j, M_j)
e = n/K = n/d_2
d = m/K = m/d_2
a_1 = n V_2 / d_2 = e V_2
b_1 = m V_2 / d_2 = d V_2
q(B) = (1−δ_1) d e / (d+e)    (δ_1 from Def 5.1(3), sees M_j, V_j, the whole chain)
c_max = q_max / e = q_max · d_2 / n
```

PS-0..PS-3 are functions of `(m, n, q_max, e)` plus, on a composition, `ν`.
So `d_2` **is** seen, as `e = n/d_2` and as `(d,e) = (m,n)/d_2`. On the
elementary compositions it is seen a third time: B6 has `(d,e)=(1,3)`,
`K=d_2=2=ν`, `c_max=1/(eν)=1/6`; A3 has the same `(d,e)` with `K=ν=1`,
`c_max=1/3`. `K` scales `c_max` through `ν` when the parent is a `K`-sheeted
cover.

What **is** invisible is `d_3,…,d_s`, the top-form `(u,v)`, and `A_bot` as a
free integer. A residue floor still yields `e ≤ C(N)`, never `D = Ke ≤ C(N)`,
because `K` is not bounded by `N`. That is the reading that survives (D=105
already has `e=3`). Repair: "K is not bounded; the family sees it through
`e=n/K` and, on a composition, through `ν`". PIN-NOT-CEILING is not
over-applied. **CONFIRMED** as a reading.

### 3.13 RES-DEGREE (ll.533–564) — CONFIRMED, witness holds (attack (e))

`Res_y(g−c, h) = ∏ h(x,τ_i)` for `g−c` monic, so
`deg_x Res = ∑ γ_h(τ_i)`. (RD-1) `h = f−c_1` generic: `γ = (1−δ^0)^+`,
degree `N`. (RD-2) `h = f`: degree `N − shed_0` with `shed_0` the vanishing
order of `f` on non-proper places, **not** `∑(1−δ^0)^-`.

Witness, re-measured (`resdeg.log` and this lane):

```text
g = y^3 + x y.  Branches of {g=c}: τ_± ∼ ±√(−x)  (proper, 1−δ^0 = 1/2),
                                  τ_0 ∼ c/x      (non-proper, 1−δ^0 = −1).
sum_i (1−δ^0_i) = 0.
f = y    (a_0=0): deg_x Res_y(g−c, f) = 0   charged form holds here
f = y+1  (a_0=1): deg_x Res_y(g−c, f) = 1   charged form REFUTED (0 ≠ 1)
          Res = c + x + 1.
```

On the ten Keller controls every branch is proper, `shed_0=0`,
`deg_x Res(g−c,f) = N = 1`. Charged form true and vacuous on the Keller
locus. ORTHO-DEFECT minus RES-DEGREE is `N−N=0`. **CONFIRMED.** Trap:
`branch_orders` of `chi` returns `γ_f`, which is `0` not `−1` on NP1's
non-proper branch; summing those recovers `1`, accidentally equal to
`deg_x Res`. The paper's comparison is to `1−δ^0 = −ord_t(f−a_0)`, not to
`γ_f`. That distinction is the content of the correction.

### 3.14 Twelve census stars (ll.690–705) — CONFIRMED as a measurement; G3 on the check

Saturated Gröbner of
`I = (coeffs_{π^1..π^{a+b−1}} of d p_f p_g' − e p_g p_f',  z κ − 1)`
is not `{1}` for all twelve types
`(1,2,1),(1,3,1),(1,4,1),(1,6,1),(2,3,1),(2,3,2),(2,3,3),(2,5,1),(2,5,2),(3,4,1),(3,5,1),(4,5,1)`,
with `γ = V(de−d−e)+1` as advertised. `(2,3,2)` exists (0.11 s). The
`sympy.solve` "no (2,3,2) star" is a retracted artefact of `starres.py`.
Repair: `existence.py` should `check(..., exists is True)`, not
`is not None`. MAJOR-MULT is not implied by star-realisability at `V_2=1`.
**CONFIRMED** as stated.

### 3.15 OPEN[PS3-NEG] (ll.332–336, 667–671) — ANSWERED for (MON)+(SEP); still open for `J ≠ 0` (attack (f))

PS-3 as charged uses (KEL). The four non-Keller rows of `psgrowth.py` do not
violate it (`c_max ∈ {1, 3/2, 3}`, bound slack). This lane searched the
charged space (two-tower row 1 plus monic pairs with `c_max < 1`) and a
bounded monomial perturbation of `(y, x+y^n)`.

**Witness, letter of the statement.** `g = y^2+1` (monic, independent of `x`),
`f = y`. Then `J = 0` (not in `k_0^*`), `chi = T^2+1−c` has `c_max = 0`,
`R_1 = [y](y) = 1`, `deg_x R_1 = 0 > (1+1)·0 − 1 = −1`. (SEP) holds for
generic `c` (`disc = −4(1−c)`). So (MON)+(SEP) do **not** imply PS-3:
(KEL) cannot be dropped as written.

The witness is degenerate (`g` ignores `x`, the map is not dominant). Every
`J ≠ 0` candidate in the search satisfied PS-3. The order identity without
(KEL) is
`−ord_t(f^k/g_y) = (k+1)c − 1 + ord_t J`
along a max-growth branch (`d/dx f ∼ t^{c−1}` still, now `g_y = J / (d/dx f)`).
A violation needs `ord_t J > 0`, i.e. `J → 0` at infinity along that branch.
For `f = y`, `J = −g_x`, and a polynomial `g_x` does not tend to 0 along
`y → ∞`. For `J` a nonzero constant one is back in (KEL).

**Typed remainder of the OPEN:** exhibit a pair with `J` a **nonzero
nonconstant** polynomial and `deg_x R_k > (k+1)c_max − 1`, or prove PS-3
under (MON)+(SEP)+`J ≠ 0`. Desk search in the charged space found none.
PS-3 needs (KEL) at least to exclude `J = 0`; whether it needs `J` constant
is not settled by the automorphism-perturbation battery.

---

## 4. FALLACY-v2

Flag/place (`c_max` vs `N`), at-level vs frontier (`δ_1` vs `δ^0`), and
pole/interior (`γ_f` vs `−ord_t(f−a_0)` on NP1) are kept distinct. No new
exit price, so no `charge_basis` line. RESIDUE-LEAD claims attainment only
on `(k+1)c_max ∈ Z` and `ptilde ≠ 0`; D15 separates `R_k ≠ 0` from tightness.
`sat()` wrapping is of `zκ−1` in grevlex; the hole in G3 is the *check*, not
the ideal. Remainders are in the free quotient with zero branched. `p_g'` is
`d/dπ`. Merge-free / target index untouched. The one FALLACY-adjacent
overclaim is "K is invisible" (§3.12).

---

## 5. PART B — EXPERIMENT NEXT-COEFF

### 5.1 Setup

`R_k` expanded completely in `x` over `Q[c]`, `k ≤ 20`. Weighted residues
for `w = e_r(τ̂)` and for the DEG block `w = y^r`. Towers:

| pair | `n` | `m` | `c_max` | tower | bottom star | `ν` |
|---|---|---|---|---|---|---|
| `(y, x+y^k)`, `k=2..6` | `k` | 1 | `1/k` | 1-level | `(1,k,1)` | 1 |
| B6 `(x+y^2, y+(x+y^2)^3)` | 6 | 2 | `1/6` | 2-level: cube under square | `(1,3,1)` | 2 |
| C6 `(x+y^3, y+(x+y^3)^2)` | 6 | 3 | `1/6` | 2-level: square under cube | `(1,2,1)` | 3 |
| D15 `(x+y^5, y+(x+y^5)^3)` | 15 | 5 | `1/15` | 2-level: cube under fifth | `(1,3,1)` | 5 |

B6 `chi = T^6 − 2c T^3 − T + x + c^2` (verified). Level-2 prediction:

```text
chi_flat = T^6 + x                 # Newton leading; flattened (1,6,1)
chi_comp = (T^3 − c)^2 + x         # nested radicals, drop −T
chi_full = chi_comp − T            # the pair
```

(GF-R) on each truncation vs the remainder. Same filtration on C6 and D15.

### 5.2 The `n−m−1` identities ARE remainder coefficients — YES

Global-interpolation (1.7)/(DEG): `M_r := ∑_i f(τ_i) τ_i^r / g_y(τ_i) = 0`
for `0 ≤ r ≤ n−m−2`, and `M_{n−m−1} = 1` in the monic gauge. By EJ this is

```text
M_r = [y^{n−1}]( y^r f  mod (g−c) ) ∈ Q[x,c].
```

Measured `== 0` (resp. `== 1`) on every charged control, including D15's
nine identities (`n−m−1 = 9`). These are the coordinator's traces
`Tr(f s_r / g_y)` after the triangular change of basis (1.6) from
`e_r(τ̂)` to `τ^r`. They do not require Puiseux, an exponent semigroup, or
an outer/inner split. They also do not require the deficit=level dictionary.

Closed form on the 1-level family, checked `k ≤ 20`:
`R_k = (c−x)^{(k+1)/n − 1}` if `n | (k+1)`, else `0`.

### 5.3 The dictionary "x-order `(k+1)c_max−1−j` ↔ level `j`" — NO

**1-level A-series.** The entire polynomial `R_k` is the binomial expansion
of `(c−x)^q`. Every deficit `j = 0,1,...,q` is a function of the **same**
single disc (star `(1,n,1)` plus the fibre constant `c` sitting in `chi_L = −c`,
the lower `x`-degree part of the unique Newton vertex `a_n = x−c`). There is
no level `j` for `j ≥ 2`. A strict "deficit `j` sees only level `j`" reading
is already meaningless here; the honest reading is "all coefficients see
level 1", which is vacuous for `s=1`.

**B6 gate (the charged check).** Remainder vs the three truncations,
exact, `k ≤ 20`:

| `k` | bound | `R_k` | source of each `[x^d]` |
|---|---|---|---|
| 5 | 0 | `−1` | flat (deficit 0) |
| 8 | 1/2 | `−2c` | **comp / level-2**, not flat |
| 10 | 5/6 | `−1` | **full `−T`**, not even `chi_comp` |
| 11 | 1 | `x − 3c^2` | `[x^1]` flat; `[x^0]` comp |
| 13 | 4/3 | `−4c` | full `−T` |
| 14 | 3/2 | `4c x − 4c^3` | both from comp |
| 15 | 5/3 | `−1` | full `−T` |
| 16 | 11/6 | `2x − 10c^2` | full `−T` |
| 17 | 2 | `−x^2 + 10c^2 x − 5c^4` | `[x^2]` flat; `[x^1]` and `[x^0]` comp |
| 20 | 5/2 | `−6c x^2 + 20c^3 x − (6c^5+1)` | leading two from comp; constant needs `−T` |

Tight leading terms (`k ∈ 5+6Z`) match `chi_flat`, i.e. RESIDUE-LEAD /
Newton leading / flattened `(1, n, 1)`. That is deficit 0 ↔ bottom×Galois,
as charged. The **next** integer coefficient on those `k` matches `chi_comp`
(level-2 nested radicals) at `k=11,17`, but already at `k=20` the constant
term needs the `−T`. Independently, the first **nonzero slack** coefficient
is `k=8`, `R_8=−2c`: bound `1/2` (Galois-cancelled half-integer), surviving
constant from the `T^3` term, invisible to the bottom star
(`ptilde_{9} ≠ 0` since `3|9`, but `ν=2` kills `t^{1/2}`).

**First coefficient that mixes levels:** B6, `k=8`, `R_8 = −2c`.
**First coefficient that mixes beyond the nested-radical level-2
prediction:** B6, `k=10`, `R_10 = −1`.

C6 and D15 repeat the pattern. D15: `R_14 = 1` (tight, Newton),
`R_17 = 5c`, `R_20 = 15c^2` (slack, from `chi_L`, the parent fifth). The
first slack nonzero on D15 is `k=17`, a level-2 (parent) number, not a
"deficit 1 of the bottom star".

A 3-fold square (`n=8`, `c_max=1/8`) repeats it: `R_7=1` tight Newton, then
`R_9=4c`, `R_10=2`, `R_11=10c^2` all from `chi_L`. No window where deficit
`j` sees only level `j`.

### 5.4 Why the "so that" fails, and what still re-bases

The charge glues two claims: (i) deficit `j` is a function of levels
`≤ j`; (ii) **so that** the `n−m−1` identities are resultant coefficients
over `Q`. (ii) is true and does not use (i). (i) is false. The identities
are remainders because `f` is a polynomial and EJ is an identity in the
quotient `Q[x,c][y]/(g−c)`, not because the tower is filtered by
`x`-degree.

When `f` is **unknown** (the g-alone interpolation engine), those remainders
are not available: `Res_y(g−c, T−f)` still names `f`. NEXT-COEFF does not
produce a resultant in `g` alone. What it does produce is a cheaper
representation of the **known-pair** (or ansatz-for-`f`) block of
`globalinterp.py`.

### 5.5 Proposal: re-base `globalinterp.py` onto `Res_y` / remainders

1. **DEG block, known `f` (or an ansatz).** Replace the Puiseux construction
   of `H_i` and the truncated Laurent arithmetic for
   `A_{m+1}=⋯=A_{n-1}=0` by the `n−m−1` remainder identities
   `[y^{n-1}](y^r f mod (g−c)) = 0`, `r = 0,...,n−m−2`, plus the monic
   `[y^{n-1}](y^{n−m−1} f) = 1`. Exact over `Q`, no tails, no uniformizer.
2. **When `chi` is known.** LEMMA EJ in the `T`-variable:
   `∑ α^k / chi'(α) = [T^{n-1}](T^k mod chi)`. JAC-FIBRE gives
   `g_y = J · chi_T / (−chi_x)` along `α = f(τ)`, hence
   `R_k = −(chi_x / J) · [T^{n-1}](T^k mod chi)` when `chi_x` is constant
   (B6: `chi_x=1`, `J=1`, checked `k ≤ 20`), and a weighted remainder when
   it is not. Input: the coefficients of `chi`, which **are**
   `Res_y(g−c, T−f)`. This eliminates the `y`-tree Puiseux from the
   `R_k` / moment engine. It does not eliminate `f`.
3. **Do not** filter `chi` by Newton-hull plus `j` lower terms: B6 `k=8`
   and `k=10` are the obstruction. Polynomiality of `A_0..A_m` mixes the
   whole of `chi` at the first slack `x`-degree. **Do not** charge a
   g-alone resultant: this instrument cannot test it.

Payoff of (1)–(2): Puiseux / semigroup / outer-inner split are avoided for
the DEG block and for `R_k` of an explicit pair. The polynomiality block
stays a global computation on `chi`. The full `R_k ∈ Q[x,c]` is cheap; it
is not a level-by-level interpolation engine.

---

## 6. Typed OPENs (this lane)

```text
OPEN[PS3-NEG]     ANSWERED for (MON)+(SEP): J=0, g=y^2+1, f=y, R_1=1,
                  deg_x=0 > −1.  REMAINS OPEN for J nonzero nonconstant.
                  Search space of the charge (two-tower + c_max<1 monomials)
                  produced no J≠0 witness; the order identity is
                  (k+1)c−1+ord_t J with ord_t J ≤ 0 on every pair tried.
OPEN[RESIDUE-LEAD-LC]  NEW, bounded: match the actual leading coefficient
                  of R_k to (d/κ)·ptilde_{k+1} times an explicit tower
                  constant, on one (2,3,1) star (not just (1,e,1) support).
                  One CAS hour; the (1,e,1) battery cannot see the prefactor.
OPEN[STAR-PTILDE] inherited, untouched: ptilde rows (2,3,2),(2,3,3),
                  (2,5,1),(2,5,2),(3,4,1),(3,5,1),(4,5,1).
```

PS-VACUITY, RES-SHED, DELTA1-SIGN: not re-opened. The first is answered in
the charged paper and the vanishing table reproduced; the second is a retype;
the third is correctly SOURCE-UNVERIFIED.

---

## 7. Typed verdict block

```text
LANE         hostile review + NEXT-COEFF (different-model gate), Grok 4.6, 2026-09-03
CONFIRMED    PS-0 (construction); LEMMA EJ; PS-1' (no J hypothesis); PS-1c;
             LEMMA DEG (quantifier order and c_2-independence); PS-2;
             PS-3 under (KEL), proper branches; PS-3+; TRACE-CONSTANT;
             TRACE-CONSTANCY; PS-3-SHARP from D1-PIN with the δ_1≥0
             correction; Newton-polygon c_max; RESIDUE-LEAD as an
             attainment theorem on (1,e,1) including D15; Φ(δ_1)=1 as the
             g_y-order step; Galois survival 1−(k+1)c_max ∈ Z;
             RES-DEGREE (RD-1)/(RD-2) and the NP1 witness;
             all 12 census stars exist (saturated GB); (2,3,2) retraction;
             trio K1=10; driver counts 1495/0, 10/0, 32/0, 14/0, 108/0.
GAP          PS-3 non-proper writeup (ord_t g_y = −δ^0), repair via JAC-FIBRE;
             RESIDUE-LEAD leading-coefficient prefactor not numerically matched;
             PS-0 `or True`; existence.py checks "decided" not "exists";
             genfun.py skips compositions (B6 GF-R filled in here, 21/21);
             "K invisible" overstated (e=n/d_2 and ν on compositions).
REFUTED      the strict dictionary "coeff of x^{(k+1)c_max−1−j} is a function
             of tower data down to level j only"  (witness B6, k=8, R_8=−2c;
             second witness B6, k=10, R_10=−1);
             "PS-3 needs no (KEL)" in the form (MON)+(SEP) ⇒ PS-3
             (witness (y, y^2+1)).
PARTIAL      NEXT-COEFF: the n−m−1 identities ARE remainder coefficients
             over Q (YES); the level dictionary is NO.  Re-base the DEG
             block of globalinterp.py onto remainders; do not claim a
             g-alone resultant and do not filter chi by deficit.
MEASURED     nextcoeff.py 8.9 s; B6/C6/D15 full R_k tables k≤20; DEG block
             on all charged controls; 3-fold square n=8 probe.
NOT CLAIMED  a D-ceiling; a J≠0 PS-3 counterexample; a g-alone resultant
             form of the interpolation identities.
NEXT         OPEN[RESIDUE-LEAD-LC] if a coefficient formula is needed;
             do not re-charge the deficit=level dictionary.
```

## 8. Reproduction

```text
box/nextcoeff-drivers-20260903/
   python3 psgrowth.py 20      -> psgrowth.log     1495 checks, 0 fail
   python3 leadcheck.py        -> leadcheck.log    10 / 0
   python3 resdeg.py           -> resdeg.log       32 / 0
   python3 existence.py        -> existence.log    14 / 0  (print: 12/12 exist)
   python3 genfun.py           -> genfun.log       108 / 0
   python3 trio105.py          -> trio105.log
   python3 nextcoeff.py        -> nextcoeff.log    8.9 s, dictionary = NO
sympy 1.12, python3, one core.  No ledger edited.  No network.
```

<!-- BODY-END -->
