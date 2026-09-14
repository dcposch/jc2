# STRUCTURE of the 65-row residual: families, second-generation numerics, and why they all survive

Lane `residual65-structure-fable5-20260905`; adapter claude (Fable 5.1). Drivers and outputs in
`box/residual65-20260905/` (`second_gen.py|.json|.out`, `controls.py|.json|.out`, `classify.py|.out`,
`xu_margins.py|.json`, page renders `moh-pdf*-printed*.png`). Frozen basis `d9f8a8f6eb6cb767a455ad66955612e916193e04`.

## 0. Verdict first

```text
VERDICT: the 65 are NOT a small number of towers over Moh's five; they are 65 distinct
  necessary tower configurations in 39 source degree pairs and 33 child degree pairs,
  organised by ONE shape invariant only: (u_s, s', ell, e:q).  Three coarse families:
    A  u_s = 1, s' = 2            23 rows  (Appendix-II shape; children K' = d_{s-1}/d_s)
    B  u_s = 1, s' >= 3           22 rows  (the depth residue Moh's method never treats)
    C  u_s >= 2 (prefix, D2)      20 rows  (19 at s'=2, 1 at s'=3; radius unlicensed)
  60 rows at n > 100 are neither scalings nor towers of the 5 at n <= 100 (M_s = n-2 does
  not scale; 11 rows share a degree RATIO with a Moh pair, none shares M or V; the only
  shared objects are three child degree pairs (21,14), (15,10), (16,12)).

  SECOND-GENERATION TESTS RUN (exact rationals, box/residual65-20260905/second_gen.py):
    (W)  child Def 5.1(2) windows at every child level          66/66 pass
    (GO) child Galois pattern + ODE at every child level         66/66 pass  (p.201 (8)-(11), Prop 4.6 via p.171 Remark, A.3)
    (B)  child-bottom divisibility (12')/(13')                   66/66 pass  (54 non-vacuous, 12 with A'_1 = 1)
    (SD) second-descent polynomiality, (v'-u'-1) - u'l >= 0      30/30 applicable complete rows pass; 20 prefixes untested
  Moh's five p.207 rows and (99,66) pass every test (control OK).  KILLS: 0 DETERMINED, 0 conditional.
  Residual after the new conditions: 65 (64 complete-or-prefix rows + (99,66)); unchanged.

  THE UNIFORM REASON (Sec. 4).  Every finite numerical necessary condition Moh prints is
  DESCENT-INVARIANT: (i) the child's bottom lattice and ODE degrees are the parent's
  transported: N' = N, M' = M on 46/46 complete rows and A'_1 = the parent's actual-stabilizer
  A_1 (44/46 also equal Moh's (8) A_1), so (B) is the parent's (12)/(13) verbatim; (ii) the child's level patterns are the inversion images of the
  parent's (own-data recipe) with the same P/Q threshold, and Lemma 6.2 preserves
  ramification, so (GO) is inherited; (iii) the only descent-SENSITIVE numeric, the SD
  exponent l'' = (v'-u'-1) - u'l, equals d_{s-1}/d_s - d_s at u_s = 1 and can be negative
  at a minor simple point only when d_{s-1} = d_s(d_s-1), which forces lo_{s-1} = 1 and is
  excluded by the ODE (no multiplicity equals P/Q).  On the 65: l'' < 0 occurs on exactly
  8 rows and on all 8 the SD hypothesis fails (delta'_{s'} != -1 or the second top point is
  MAJOR, lo_top < 1).  20 rows sit at l'' = 0 exactly.
  So the residual is the FIXED-POINT SET of Moh's arithmetic sieve under Prop 6.3 descent.
  A second arithmetic generation cannot move it; only non-arithmetic instruments can:
  the chart (Groebner) receiver, the split window at u_s >= 2, or a sharper Xu Thm 5.1.

  PRICES (Sec. 5): (a) second descent -> 0 kills, vacuous; (b) Xu Thm 5.1 sharpened floor
  V_s/u_s - 1 at u_s > 1 -> 0 kills on the 65 (R001 only, already removed), margins are 0
  on R009 (192,128) and R050 (196,56), 1 on R011; (c) child (12')/(13') -> identity, 0;
  (d) charts: none < 70 unknowns, min 199 (R002/R003 = Moh's (15,10) children), median 883,
  max 4889 (R066); (e) prefixes: completion needs the ES leaves killed (1-6 per row, 38 in
  total) AND the child terminal pair M'_{s'+1} fixed by the x-side p.150 computation.
```

No new exit-price assertion is made, so no `charge_basis` line is licensed.

## 1. Custody and population

Manifest built with `awk` from the paired `charged_input_<i>_basename=`/`_sha256=` lines of the
`.run.v2` receipt, then `sha256sum -c`: **9/9 OK** (`box/residual65-20260905/manifest.sha256`). Moh
pages were rendered fresh from the charged PDF at 130 dpi (printed page = PDF ordinal + 139):
170, 171, 185, 188–202, 205–208; every quotation below is read off an image. Xu was read from
its native text layer.

Population: the 66 rows of `roster.jsonl` (schema `jc2.residual66.roster/v1`, every row typed
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`). R001 `(84,56) M=(64,82) V=(2,3)` is
removed by Xu Cor 5.3 under the full conjunction (17(ccccccccc)); it is kept here as a
positive control (Moh's second p.207 row) and excluded from the counts, giving **65**.
Roster child radii were replayed from `delta'_i = (l+1)·Def 5.1(3)(n',M',d',V',s',i)` on all
46 complete rows: **46/46 equal** (assertion in `second_gen.analyse_row`).

## 2. Classification of the 65

### 2.1 Coarse invariants

| invariant | distribution on the 65 |
|---|---|
| `u_s` | 1: 45, 2: 11, 3: 6, 4: 2, 5: 1 |
| route | D1 complete (Prop 6.4 radius): 45; D2 prefix (radius unlicensed): 20 |
| source height `s` / child `s'` | s 3: 42, 4: 22, 5: 1 ; s' 2: 42, 3: 22, 4: 1 |
| `l = v_s - u_s - 1` | 1: 27, 2: 13, 3: 9, 4: 8, 5: 2, 6: 4, 7: 1, 8: 1 |
| `d_s` | 4: 26, 5: 9, 6: 8, 7: 5, 8: 2, 9: 5, 10: 1, 11: 4, 12: 1, 14: 1, 15: 2, 19: 1 |
| `n/m` | 3/2: 39, 4/3: 9, 5/3: 4, 7/4: 3, 5/4: 2, 7/5: 2, 5/2: 2, 7/2: 2, 10/7: 1, 7/3: 1 |
| child `(e,q) = (n'/K', m'/K')` | (3,2): 39, (4,3): 9, (5,3): 4, (7,4): 3, (5,2),(5,4),(7,2),(7,5): 2 each, (7,3),(10,7): 1 each |
| `delta'_{s'}` | −1: 45, −1/2: 9, −2: 5, −1/4: 2, −1/3, −1/5, −3, −5: 1 each |
| `d = -delta'_{s'}` (source-support constant) | 1: 45, 1/2: 9, 2: 5, 1/4: 2, others 1 each — `d > 1` on 7 rows (R018, R057, R058, R063, R064, R065, R066) |
| chart size (unknowns without T) | min 199, median 883, max 4889; buckets <300: 3, <700: 13, <1500: 35, ≥1500: 14; **none < 70** |

39 distinct source pairs, 33 distinct child pairs, 51 distinct receiver keys `(n',m',M'_last,l)`.
The finest natural family key is `(u_s, s', l, e:q)`: **41 families**, the largest being
`u=1, s'=3, l=1, (3,2)` with 11 members (R019 R020 R021 R039 R040 R041 R042 R056 R060 R063 R064)
and `u=1, s'=2, l=1, (3,2)` with 4 (R006 R007 R009 R031). Full listing: `classify.out` §E.

### 2.2 Are the 60 rows at n > 100 scalings or towers over the five at n ≤ 100? No.

* **Scalings.** `M_s = n − 2` is not homogeneous, so no census row is a scalar multiple of
  another. Eleven rows share a degree *ratio* with a Moh pair — (168,112) = 2·(84,56) ×7,
  (150,100) = 2·(75,50), (128,96) = 2·(64,48), (192,144) = 3·(64,48) ×2 — but their `M`, `V`,
  `s` differ (e.g. R019 `(168,112) M=(−112,−28,148,166) V=(1,3,3)` has s = 4, Moh's (84,56) has s = 3).
* **Towers.** No child `(n',m')` of any row is itself a source pair of another row; the children
  have `n' ≤ 63`. What *is* shared with Moh: three child degree pairs — `(21,14)` on R007 (Moh's
  `M'=18, V'=5`), R008 `(147,98) → M'=15, V'=6, l=4` and R018 `(126,84) → M'=18, V'=5, l=3`;
  `(15,10)` on R002/R003 (Moh's two); `(16,12)` on R004 (Moh's first). R018's child has the same
  `(n',m',M',V')` as Moh's `(21,14;18;5)` but `l = 3` instead of `1`, so it lives on a *different*
  receiver (`d = 2` instead of `1`): same degrees, different chart.
* **Descended-height structure.** All 45 `u_s = 1` rows descend by Prop 6.4 to a complete child chain
  with `d'_{s'+1} = 1`; 23 have `s' = 2` (Moh's Appendix-II shape), 22 have `s' ≥ 3` (the depth
  residue). The `u_s ≥ 2` block is prefix-only (`d'_{s'+1} = u_s > 1`); 19 of 20 have `s' = 2`.

### 2.3 The three coarse families and what each is

**A. `u_s = 1, s' = 2` (23 rows).** Children `(n',m')` with `K' = gcd = d_{s−1}/d_s`; 13 with
`l = 1`, 6 with `l = 2`, two with `l = 3` (R018, R030), one each at `l = 4, 5` (R008, R013). All have
`delta'_1`, `delta'_2` of the p.207 kind; 15 have `delta'_2 = −1` (Prop 6.3 hypothesis for a second descent).
Smallest charts live here (199–1819 unknowns).

**B. `u_s = 1, s' ≥ 3` (22 rows).** 21 at `s' = 3`, one at `s' = 4` (R059, `(192,128) → (48,32)
M'=(−32,40,44,45)`). Thirteen have `l = 1`. Six of them (R025–R028, R057, R058) have a child top
form `p'` of degree `d'_{s'} = 2` with **two simple MAJOR points** (`lo_top = 2/5`, `2/3 < 1`): the
child carries two major towers, so the sibling tower must also extend (p.200 Thm (4) for the child,
Jacobian-free through Prop 5.3). Checked by hand on R025: the sibling can copy the selected tower
(`V''_2 = 2`, `A = 3`, `(12')` holds), so it does not kill.

**C. `u_s ≥ 2` prefixes (20 rows).** Split-window status from the roster: every row still carries
1–6 typed `ES_NECESSARY_LEAF` orders (38 leaves in total; R055 `(171,114) u=5` has 6 of 18 orders
alive, R038/R062 4 of 10, R043 3 of 10), so Prop 6.3's radius hypothesis is *not* forced and the D2
branch remains as the alternative. Four prefix children have `u' = d'_{s'} − V'_{s'} = 1` and
`delta'_{s'} = −1` (R012, R015, R045, R062) — the shape on which a second descent would be
polynomial if the terminal pair were known.

## 3. The second-generation tests: statement, licence, result

All tests act on the child tower `(n', m', M'_1..M'_{s'}, d', V'_2..V'_{s'}, delta', l)` of the
roster, with `V'_{s'+1} := 1` on complete chains (`d'_{s'+1} = 1`: "all `n'` roots lie in `D'_{s'}`"
is a tautology, not the p.201(4) convention). On prefixes the top level is untested.

**(W) Child window.** `P'_j = V'_{j+1} d'_j/d'_{j+1} ≥ V'_j > d'_j/(n'−M'_j)` — Def 5.1(2) p.179,
p.201 (7). Already 65/65 in the own-data gate; re-confirmed 66/66.

**(GO) Child Galois pattern and ODE at level `j`.** With `L'_j = lcm{den delta'_i : i > j}` and
`A'_j = den(L'_j delta'_j)` (p.201 (8), verbatim "let the l.c.m. of the reduced denominators of
`delta_s, …, delta_r` be `L`; `A_{r−1}` is the reduced denominator of `L delta_{r−1}`"), a pattern
`p'(xi) = xi^z ∏(xi^{A'} − c_nu)^{r_nu}`, `z + A'Σr = P'_j`, must exist with `V'_j ∈ {z} ∪ {r_nu}`
(p.201 (10),(11)), `[z>0] + A'·#orbits ≤ Q'_j` (Prop 4.6(3),(4): `q` squarefree, roots of `p` are
roots of `q`), no multiplicity equal to `P'_j/Q'_j` (from A.3's identity `P p q' − Q p' q = c p`
at a root of multiplicity `v`: `(P − Qv) q'(a) = c ≠ 0`; this also excludes `p = q^w`, 4.6(5)),
and some multiplicity `> P'_j/Q'_j` (A.3(4)). **Licence for the child:** the p.171 Remark,
verbatim "*With a verbatim proof, for a slightly general Jacobian condition … `J_{x,y}(f,g) = x^l`
Proposition 4.6 is still valid with the condition (3) replaced by (3)*: `λ = (−1−l+δ)/(n−m_r)`*",
and the child is exactly such a pair by Prop 6.3(3) (`J_{γ,π} = −(u_s/b) γ^{v_s−u_s−1}`). The
Galois orbit statement is field theory over `k((t'))` and needs no Jacobian.
Result: 66/66 alive at every level (pattern counts 1–36 per level, `second_gen.out`).

**(B) Child-bottom divisibility.** p.188, verbatim: "*if the reduced denominator `A` of `δ_1` is
not a factor of `deg g_σ(π) = n*V_2` then `π` is a factor of `g_σ(π)`. Moreover if `A` is a factor
of `n*V_2` then `g_σ(π) ∈ k[π^A]` and `π` is a factor of `(d/dπ) g_σ(π)`. In view of the two co-prime
conditions above we must have `A | n*V_2 and A ∤ m*V_2 or A ∤ n*V_2 and A | m*V_2`. Moreover we
always have from the very definition of `A` the following `A | (n*+m*)V_2 − 1`*" — the last line
is the `π → ζπ` covariance of the r = 1 ODE `D(n, −M_1, g_σ, T_{1,σ}) = c ≠ 0` (Prop 4.6, last
sentence), which is `l`-valid by the same Remark; so (12)/(13) hold at the child's bottom with
`A'_1 = den(L'_1 delta'_1)`, `N' = (n'/d'_2)V'_2`, `M' = (m'/d'_2)V'_2`, independently of `l`.
Result: 66/66 — 54 non-vacuous (`A'_1 ∈ {2,…,10}`), 12 vacuous (`A'_1 = 1`, all with
`delta'_1 ∈ {0, 1}` or `L'delta'_1 ∈ Z`).

**(SD) Second-descent polynomiality.** If `delta'_{s'} = −1` and the child's top form has a MINOR
point of multiplicity `u` (p.190: minor iff `u ≤ d'_{s'}/(n'−M'_{s'})`) whose minor-disc radius is
`≥ v'/u`, `v' = d'_{s'} − u`, then Prop 6.3(1) — whose proof (p.197–198) is Jacobian-free — makes
the grandchild `(P'', Q'')` POLYNOMIAL in `k[γ', π']`, and the p.198 chain rule with
`J_{γ,π}(P,Q) = c γ^l` and `γ = (γ'^{−u} − e' − A'(γ') − π'γ'^{v'})/b'` gives

```text
J_{γ',π'}(P'', Q'') = c' · γ'^{(v'-u-1) - u·l} · (1 - e'γ'^u - A'(γ')γ'^u - π'γ'^{u+v'})^l .
```

The last factor is a polynomial with constant term 1, so polynomiality forces
`l'' := (v'−u−1) − u·l ≥ 0`. (The earlier reading "`l'' = 0` gives a Keller grandchild" is FALSE:
the last factor is non-constant for `l ≥ 1`; only the exponent condition survives. Moh's own
category is not closed under descent, as `depth-residual` already recorded.) Licence at `u = 1`:
Prop 6.4 p.198 under `J = x^l`. Its proof reduces to Prop 6.1(2) (p.190–192), which verifies
Prop 4.4's conditions; under the p.169 Remark's (6)* and the (3)^l shift the `−1−l` terms cancel
identically and the condition again reads `V_r ≤ d_r/(n−M_r)` (p.192 display), so the reduction is
verbatim; and Moh himself applies the bound to the `l = 1` child `(16,12)` on p.207–208
(`σ* = t^{−1} + a_0 + a_1 t + a_2 t^2 + π t^3`, i.e. `δ* = 3 = v'/u'`). At `u ≥ 2` the radius is the
child's split-window question (conditional). Result: applicable on 30 complete rows; **30/30
survive** — on 24 of them a pattern with all non-selected points simple and `l'' ≥ 0` exists, on
the 6 rows of family B with `d'_{s'} = 2` the second point is MAJOR and (SD) does not apply.

**Controls.** Moh's five p.207 children (R001–R004, R007) pass (W), (GO), (B), (SD) — as they must,
since Moh kills them by the Appendix-II coefficient computation, not by numerics. (99,66) (R015,
prefix) passes (W), (GO) at the tested levels and (B) vacuously (`A'_1 = 1`). Parent replay and
census-wide controls: Sec. 4.3.

## 4. Why a second arithmetic generation cannot move the residual

### 4.1 (B) is the parent's (12)/(13), verbatim

With the roster's metric radii (own-data recipe, `pi <-> y`, `gamma <-> x`): for `i ≥ j` (first
nonzero source index) `delta'_i = v − u/delta_i`, for `i < j` `delta'_i = v − u − (u/e)(1 − delta_i)`,
`e = delta_j`. At `s = 3`, `u = 1`, `j = 2`: `L' = den(v − 1/delta_2) = num(delta_2)` and
`L' delta'_1 = num(delta_2)(v−1) − den(delta_2)(1 − delta_1)`, so
`A'_1 = den(den(delta_2)·delta_1) = A_1`; and `n'/d'_2 = n/d_2`, `m'/d'_2 = m/d_2`, `V'_2 = V_2`
(D1 identity), so `N' = N`, `M' = M`. At `s ≥ 4` a zero-selected level `i` has `delta'_i = v − u/delta_i`
integral whenever `u/delta_i ∈ Z`, so the child's `L'` omits that level's denominator — exactly the
own-data lane's rule "a zero coefficient adds no denominator": `A'_1` is the parent's *actual*
centre-stabilizer `A_1`, not Moh's (8) value. Numerically on the roster: **44 of 46 complete rows have `A'_1 = A_1` with Moh's (8) lattice and all 46 have `N' = N`, `M' = M`; the two exceptions R026, R028 (`s = 4`, zero-selected levels 3,4 whose child radii `−1, 0` are integral) have `A'_1 = 3, 2` against Moh-(8) `A_1 = 1`, which is exactly the own-data lane's *actual centre stabilizer* `A_1` (a zero coefficient adds no denominator) — the lattice `own_v_routes` already imposes at the parent's bottom; on the 20 prefixes 10 are equal and 10 have `A'_1 | A_1`**. For `u ≥ 2` the
same computation gives `A'_1 | A_1`, so the child condition is *implied* by the parent's. (B) is
therefore not a new condition anywhere in the census — it is the parent's bottom test transported,
which is exactly what Lemma 6.2 (p.196, "*`x(θ) mod θ^q ∈ k((θ^{1/p})) ⟺ y(t) mod t^q ∈ k((t^{1/p}))`*")
predicts: inversion preserves ramification.

### 4.2 (GO) is inherited, (SD) is vacuous on ODE-screened rows

*Inheritance.* The child's top pattern is the inversion image of the parent's level-`(s−1)`
pattern (own-data `inverse_top`: the zero root goes to `W_0 = u·d_{s−1}/d_s − a·Σr`, each nonzero
`b`-orbit of multiplicity `r` to `a` child roots of multiplicity `r`, `delta_{s−1} = a/b`), with the
same threshold `lo' = d'_{s'}/(n'−M'_{s'}) = d_{s−1}/(n−M_{s−1})`. The orbit multiplicities `r ≠ lo`
and "some `r > lo`" are literally the parent's ODE conditions; the child's new constraints are
`W_0 ≠ lo` and `[W_0>0] + (a/gcd(a,u))·k ≤ Q'`, and every one of the 46 complete rows has an
admissible image pattern (e.g. R019: parent `P=21,Q=15,A=7` with orbit `(3)` maps to child
`z'=1`, orbit `(3)` at `A'=2`, distinct `3 ≤ 5`). Lower child levels have `P'_j = P_j`, `Q'_j = Q_j`
exactly (`n'−M'_j` and `d'_{j+1}` both scale by `u/d_s`).

*Vacuity of (SD).* At `u_s = 1`, `d'_{s'} = d_{s−1}/d_s` and `l = d_s − 3`, so at a simple minor
point `l'' = d_{s−1}/d_s − d_s`. A kill needs `l'' < 0`, i.e. `d_{s−1} < d_s^2`, together with the
SD hypothesis `delta'_{s'} = −1 ⟺ M_{s−1} = n − d_s(d_s−1)` and minority `1 ≤ lo_{s−1} =
d_{s−1}/(n−M_{s−1}) = d_{s−1}/(d_s(d_s−1))`. Since `d_s | d_{s−1}`, the window is the single value
`d_{s−1} = d_s(d_s−1)`, where `lo_{s−1} = 1` exactly — and then the parent's level-`(s−1)` ODE
forbids any simple root (multiplicity `1 = P/Q` is excluded). So on every ODE-screened row (SD)
at a simple point is empty, and (SD) at a heavy point (`u ≥ 2`) is conditional on the child's
split window. On the 65 the boundary is populated: **20 rows have `l'' = 0`** (`d_{s−1} = d_s^2`:
R002 R003 R004 R008 R013 R014 R017 R022 R030 R034 R036 R037 R039 R040 R041 R042 R046 R047 R048 R059),
and the 8 rows with `l'' < 0` (R025–R028, R057, R058: `d_{s−1} = 12, d_s = 6`; R064; R066) all have
the SD hypothesis failing (`delta'_{s'} ∈ {−2,−5}` or both top points major, `lo_top ∈ {2/5, 2/3}`).

### 4.3 Controls (`controls.py`, `controls.out`)

* **Parent replay, l = 0.** The same level-local engine (W + GO at every level + B) run on the 66
  parents: **0 of 66 parents rejected**. On the whole (1)–(13) census at `Kmin = 2`, `16 ≤ n ≤ 200`:
  **24,063 rows; all 1,420 operative rows accepted, 35 of the 22,643 non-operative rows rejected (so my rejections ⊂ the Tree's)** — operative rows rejected by my engine: **0** (must be 0;
  my conditions are a sub-conjunction of the operative `C_FULL_TREE_POLYNOMIAL_ODE`).
* **SD reach on the census** (`u_s = 1`, `s ≥ 3`): rows in the kill window
  (`delta'_{s'} = −1`, `l'' < 0`, simple point minor): ****0 of 24,063 census rows and 0 of 1,420 operative rows** — the cell `top = −1 ∧ l'' < 0 ∧ simple point minor` is empty on the whole census, as Sec. 4.2 predicts; 41 operative rows sit at `l'' = 0` with `top = −1` (46 s)**.
* **Outer-set probe.** `descend_own` on all operative rows reproduces **the own-data partition exactly (NONEMPTY 66, EMPTY_NECESSARY_FIRST_SUPPORT 1,051, EMPTY_NECESSARY_WHOLE_SOURCE_TREE 213, EMPTY_PROP6.3_FINITE_POLE 90)**; on the
  rows whose first-support outer set is non-empty but whose full necessary set is empty, the child
  tests on the outer vectors give **215 outer vectors on the 213 tree-empty rows: 192 pass both, **21 fail (B)** (11 at `u_s = 1`, 10 at `u_s > 1`) and **2 fail (GO)** at child level 2 (both `(180,120) M=(−120,90,160,165,178)`) — the child tests are not tautologies; they bite exactly on the near-misses the whole-tree screen already kills, which is what the identity of Sec. 4.1 predicts** — this measures the independent killing power
  of (GO)/(B) on near-miss child data.

## 5. Pricing the not-yet-applied necessary conditions, per family

| condition | family A (u=1, s'=2; 23) | family B (u=1, s'≥3; 22) | family C (u≥2; 20) |
|---|---|---|---|
| (a) child's own source-support consistency / second descent | numerics inherited (Sec. 4); (SD) applies to 15 rows, 0 kills; the chart-level content of (a) IS the receiver chart | (SD) applies to 15 rows, 0 kills; 6 rows carry a compulsory sibling major tower (no kill on R025 by hand) | top level untested (`V'_{s'+1}` unknown); (SD) would apply to 15 rows with `delta'_{s'} = −1` once the terminal pair is fixed |
| (b) Xu Thm 5.1 sharpened (floor `V_s/u_s − 1` at `u_s > 1`) | no change (floor already used) | no change | **0 kills** on all 20 (`Im_sharp ≤ IM_max` everywhere, `xu_margins.out`) |
| (b') margin `IM_max − Im_min` | 0 on R009 (192,128) and R050 (196,56); 1 on R011; else ≥ 3 | ≥ 4 (min R022 = 4) | ≥ 2 (min R016 = 2) |
| (c) child (12')/(13') | identity with the parent's, 0 kills | identity, 0 kills | implied by the parent's (`A'_1 | A_1`), 0 kills |
| (d) chart size (unknowns without T) | 199 (R002, R003), 241 (R004), 307, 322, 370 (R007, R008), …, 1819 (R061) | 706 (R019–R021) … 3074 (R064) | 475 (R012), 593 (R015), 620 (R016) … 4889 (R066) |
| (e) what licenses completion | n/a (complete) | n/a (complete) | kill the 38 ES leaves (Xu (7.1) face-ODE per `(ρ, partition)`), then fix `M'_{s'+1}` by the x-side p.150 computation (three cases: ∞ / `n'−1` / `< n'−1`) |

Reading of (b): the coverage gate's one unclosed link is Xu Thm 5.1's *major* leaf expression
`(n/(m+n))Σ|D_σ^f|(1−δ_σ)`; the Xu-screen gate showed it is an identity of Def 5.1(3), so no
sharpening of `IM_max` is available from the skeleton alone. The two margin-0 rows R009 and R050 are
the only ones any refinement of Xu could reach at n ≤ 200; both are family A, `l = 1`, children
`(48,32; M'=37)` and `(49,14; M'=46)`.

Reading of (d): Moh's own counts for the three p.207 children are 244/373/202 total coefficients
before his 17/22-coefficient reduction; the roster's `G_i`-only receivers for the same children
are 241/370/199 — the source-support theorem recovers Moh's total-degree bound almost exactly, and
nothing on the 65 is below it. The 78-unknown chart quoted in `depth-residual` belongs to a row
(parent `(96,64) V=(1,1,6,3)`) that the own-data reduction has since emptied; it is not among the 65.

## 6. VERDICT

```text
FAMILIES:  A  u_s=1, s'=2   23 rows    B  u_s=1, s'>=3   22 rows    C  u_s>=2 prefix   20 rows
           finest natural key (u_s, s', l, e:q): 41 families; no towers, no scalings over Moh's five.

NEW NECESSARY CONDITIONS APPLIED (all exact, all 66 rows):
  (W)  child windows            kills 0   DETERMINED (Def 5.1(2) for the child's own tower)
  (GO) child Galois + ODE       kills 0   DETERMINED at u_s=1 (p.171 Remark); conditional at u_s>1 (radius)
  (B)  child bottom (12')/(13') kills 0   DETERMINED, and IDENTICAL to the parent's actual-stabilizer test (Sec. 4.1)
  (SD) second-descent l'' >= 0  kills 0   applicable 30/30 survive; typed DETERMINED-mod-[P6.4 under J=x^l]
                                          at simple minor points; vacuous on ODE-screened rows (Sec. 4.2)
  Xu sharpened floor            kills 0   (diagnostic; unprinted at u_s>1)
EXACT RESIDUAL AFTER THEM: 65  (unchanged; R001 remains the sole Xu removal).

INSTRUMENT EACH FAMILY NEEDS:
  A  the G_i receiver chart (199-1819 unknowns), exact-Q std; the two Xu-tight rows R009/R050 first.
  B  the s'>=3 receiver (706-3074 unknowns), band-wise elimination; the six two-major-tower rows
     (R025-R028, R057, R058) additionally admit a sibling-tower joint chart.
  C  the split-window leaves (38 typed ES leaves) via Xu (7.1)/(F) per leaf, then the child terminal
     pair (x-side p.150), then the same chart as A.
```

**FALLACY-v2 ledger.** *Flag/place/series:* the child's `pi`-roots are the minor cluster's branches
re-expanded at `y = ∞`; the child's top disc is NOT the parent's `D_{s−1}` (different clusters), and
Sec. 4.2 uses only the inversion image, never an identification of discs. *Floor/attainment:* every
pattern existence is a survival, never a witness pair; `l'' ≥ 0` is necessary, `l'' = 0` proves
nothing (the Keller-grandchild reading was caught and withdrawn in Sec. 3). *Pole/interior:* (SD)
is applied only after checking the vertex class (minor vs major point, p.190 threshold) and Prop
6.3's `delta_s = −1`. *Variable/ring map:* the second-descent substitution is declared with its
direction (`π = γ'^{−u}`, `γ = (π − e' − A' − π'γ'^{v'})/b'`) and its Jacobian is computed, not
matched by name. *Prime label:* `'` and `''` are generation labels; no differentiation is meant
except in `q'(a)`, which is Moh's own `d/dπ`. *Merge-free/M-descent:* prefixes keep their terminal
index open; no `M'_{s'+1}` is invented. *Target/arrival index:* child level `j` is compared with
parent level `j` for `P, Q` and with parent level `s−1` for the top pattern, and these are stated
separately. No `sat()`, no Groebner run in this lane.

## OPENS RAISED

```text
OPEN[SECOND-GEN-NUMERICS-DESCENT-INVARIANT]
  QUANTITY: for a licensed Prop 6.3 descendant, the child-level necessary numerics satisfy
    A'_1 = A_1^{act} (actual centre stabilizer), N' = N, M' = M (u_s = 1) and A'_1 | A_1 (u_s >= 2);
    P'_j = P_j, Q'_j = Q_j at every common level; and the SD exponent l'' = d_{s-1}/d_s - d_s at u_s = 1.
  STATUS: derived from the metric radii and the descent law; verified on 46/46 complete rows and
    20/20 prefixes (controls.out (b)); SD window empty on 24,063/24,063 census rows (controls.out (d)).
    Not yet promoted as a theorem in the ledger.
  CHEAPEST TEST: replay controls.py on the full 1,420 operative set with own V' (descend_own),
    ~3 minutes; a single row with A'_1 not dividing A_1 refutes it.
  BLAST RADIUS: none on counts; it retires "second arithmetic generation" as an avenue for all
    1,420 rows, and re-prices avenue (a) to the chart receiver alone.

OPEN[SD-HEAVY-POINT-CONDITIONAL]
  QUANTITY: at a MINOR top point of multiplicity u >= 2 of a child with delta'_{s'} = -1,
    (SD) requires l'' = d'_{s'} - 2u - 1 - u*l >= 0 given the child's minor radius >= v'/u.
  STATUS: the inequality is necessary given the radius; the radius is the child's split-window
    question (analogue of OPEN[PROP6.3-RADIUS-US>1]).  On the 65 no admissible top pattern is
    forced to carry such a point (every row has an all-simple alternative), so it kills 0 here.
  CHEAPEST TEST: for each of the 30 applicable rows list patterns whose non-selected points are
    all heavy (u >= 2) and check whether the (GO) constraints could force one; ~1 minute.
  BLAST RADIUS: 0 on the 65; possibly nonzero on rows outside the operative set.
```

## OPENS RETAINED

```text
OPEN[CTOP-EXTRA-CONDITION-E], OPEN[PROP6.3-RADIUS-US>1], OPEN[CHILD-TERMINAL-SUPPORT-US>1]
  -- unchanged; they are exactly what family C's completion needs (Sec. 5 (e)).
OPEN[PROP42-ELL-CONDITION3] -- unchanged; consumed by the (SD) licence at u = 1 and by every
  child radius, in the same way the source-support closeout consumes it.
OPEN[MINOR-RADIUS-BOUNDARY-ONE], OPEN[RESONANCE-FILTER-EXACT-FORM], OPEN[SIBLING-EXTENSION-DEPTH]
  -- unchanged; none touches the 65.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26930`.
- Body SHA-256:
  `164c9377db02a992e28930cbed474bac1d9132f0e48957ea2c8a065fc181ac8c`.
- Frozen basis: `d9f8a8f6eb6cb767a455ad66955612e916193e04`.
