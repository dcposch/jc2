# Moh 1983 source: three questions (Grok 4.6, 2026-09-03)

Source lane. Charged: Opus ideation §0–§1 / §2.4; census-rebase; `box/moh_skeleton_full.py`; drivers `moh4.py`/`battery.py`; Moh 1983 JRAM 340 (journal page N = PDF page N−139). No ledger edit, no `jc2-lean`, no other `ideation-20260903T1015Z-*` submission. No exit-price assertion ⇒ no `charge_basis`.

## 0. Custody

Frozen SHA-256 verified before any page was opened (workspace Python copies match): ideation `b13149ec…22562`, census-rebase `fb137b92…f6948`, `moh_skeleton_full.py` `d20bf084…c506c2`, `moh4.py` `cdf5eeb7…d083d2`, `battery.py` `d6e40234…51685`, Moh PDF `6c8847a8…aa6a51`. PDF 74 pp., rendered `pdftoppm -r 300` and read as images (journal 179–212 = PDF 40–73, plus 187, 190, 193–201). `pdftotext` used only as an index. Firewall: Moh `n = deg_y g` ≠ campaign geometric `N`; `V_i` is Prop 5.3 multiplicity, not a derivative; `A_j` is the increment of (8), not `den δ_j`. Desk CAS: stdlib over `moh_skeleton_full.py`, wall 15 s.

## 1. Q1 — MAJOR-MULT is not Moh's definition of a major disc

**Plain statement.** MAJOR-MULT (`V_j ≥ 2` for every `j = 2..s`) is **not** in Moh and is **not** a consequence of his definitions. Campaign CONJECTURE. The `j = s` slice is already search (7) and is stronger than `≥ 2`. The slice that kills `D = 105` is `V_2 ≥ 2`, which Moh's major/minor split explicitly permits to fail.

### 1.1 Defining sentence (p.179, Definition 5.1)

> **Definition 5.1.** A tower of major discs `D_s ⊇ D_{s-1} ⊇ ⋯ ⊇ D_r` satisfies the following four criteria with a sequence of integers `{V_i : i = (r+1, …, s+1)}`:
>
> (1) In the disc `D_i` the polynomials `g(y)` have precisely `(n/d_{i+1}) V_{i+1}` roots. `T_j^ψ(y)` has precisely `(-μ_j/d_{i+1}) V_{i+1}` roots for `j = 1, …, i`,
>
> (2) the numbers `V_i` satisfy `V_{i+1} d_i / d_{i+1} ≥ V_i > d_i/(n − M_i)` for `i = r+1, …, s`, `V_{s+1} = d_{s+1}`,
>
> (3) logarithmic radius `δ_i` [displayed product],
>
> (4) `σ_i = Σ α_j t^j + π t^{δ_i}` is the unique general point in `D_i`; Prop 4.6 holds with `v = V_{i+1}(d_i/d_{i+1})`.

No `V_i ≥ 2`. No requirement that the selected factor of `p(π)` be non-simple. The unique object in `D_i` is the general point `σ_i`. Criterion (1): `V_2 = 1` still puts `e = n/d_2` roots of `g` in `D_1` (3, not 1, on the `D = 105` trio).

p.179 last paragraph, gloss of Prop 5.2:

> any subdisc can be used as `D_{s-1}` **if it contains more than the average number of roots**.

That is the split: *more than the average*, not *multiplicity ≥ 2*. Introduction p.142: “A major disc is one which contains more than a predetermined number of roots (cf. Definition 4.1). Otherwise it is a minor one.”

### 1.2 `V_r` is a multiplicity; `V_r = 1` is written in (pp.180, 190)

**Proposition 5.3** (p.180):

> Let `π − C_r` be a factor of `p(π)` as in the conclusions of Proposition 4.6 **with multiplicity `V_r`** satisfying `deg p(π) = V_{r+1}(d_r/d_{r+1}) ≥ V_r > d_r/(n − M_r)`. […] Moreover the tower `D_s ⊇ ⋯ ⊇ D_r ⊇ D_{r-1}` is a tower of major discs.

A simple factor (`V_r = 1`) is major precisely when `1 > d_r/(n − M_r)`.

**§6 opening** (p.190), complementary clause:

> If the multiplicity `V_r` satisfies `deg p(π) = V_{r+1} d_r/d_{r+1} ≥ V_r > d_r/(n − M_r)` then we may extend the tower of major discs […]. On the other hand the multiplicity `V_r` may satisfy `d_r/(n − M_r) ≥ V_r`. We shall construct the corresponding disc `D_{r-1}^*` thus denoted a **minor disc**.
>
> **Proposition 6.1.** […] with multiplicity `V_r` satisfying `d_r/(n − M_r) ≥ V_r ≥ 1`.

Moh writes `V_r ≥ 1` on the minor side and does not write `V_r ≥ 2` on the major side. A disc with a single *g*-root is typically minor by the count test (Theorem p.200(5)), but that count is `(n/d_{i+1}) V_{i+1}`, not `V_i`. Equating “simple factor of `p(π)`” = “single root” = “minor” mixes three objects.

### 1.3 Theorem p.200 (4)–(7) and Cor 6.1

**Theorem** (p.200): (4) if the number of roots of `g` in `E_i` is `> n/(n − M_r)` the tower extends; (5) if `≤ n/(n − M_r)`, then `E_i` is a **minor disc**; (7) at least one `E_i` satisfies (4). These reduce to the lower half of search (7). They add no `V_i ≥ 2`. **Corollary 6.1** (p.199): `d_s = 3` and `δ_s = −1` (“more than one point at infinite”) yields a transform `χ` with Jacobian a nonzero constant; p.200 then forces `v_s = 2`, `u_s = 1`, and “we must assume that `d_s > 3`”. Search (6) `d_s ≥ 4` is that corollary, not a multiplicity floor on every `V_j`.

### 1.4 What is in Moh at `j = s`, and what is not

At `r = s`, search (7) is `V_s > d_s/(n − M_s) = d_s/2`. With `d_s ≥ 4` this is `V_s ≥ 3`. MEASURED: `V_s ≥ 3` on **658/658** `(1)–(13)` rows at `n ≤ 100`. So the `j = s` instance of MAJOR-MULT is **DERIVED** from Def 5.1(2) + Cor 6.1, already implemented, and stronger than `≥ 2`.

The residual content — `V_2 ≥ 2`, and `V_j ≥ 2` for `3 ≤ j ≤ s−1` — is **NOT-IN-SOURCE**. It keeps the six p.202 rows and kills every `D = 105` group that survives INCREMENT ∧ NOT-ALL-(11): those groups have `V_2 = 1` *and* `1 > d_2/(n − M_2)` (major by Moh's own test):

`m=70 M=[28,103] V_s=5 or 6`, `m=70 M=[40,103] V_s=4`: all `V_2=1`, `d_2/(n-M_2)<1`, `windows_ok`. If MAJOR-MULT were a consequence of the definitions, these would not be windows-admissible. They are.

**Typing.** MAJOR-MULT as charged: **NOT-IN-SOURCE**, campaign CONJECTURE. `OPEN[MAJOR-MULT]`, bounded **161 rows** at `n ≤ 100` (247 → 86 under `V_2 ≥ 2`; a further 35 under all `V_j ≥ 2`, 34 of them `V_3 = 1`) and **744 groups** at `48 ≤ D ≤ 200` (2,652 → 1,908), including the `D = 105` trio.

## 2. Q2 — (12)/(13) and `A_1 ≥ 2`

**Plain statement.** Moh's *derived* condition on p.188 **is** the exclusive disjunction, and under that disjunction `A = 1` is inadmissible. The printed search pair (12)/(13) on p.201 is **not** written as that exclusive disjunction; both branches hold when `A_1 = 1`. Identifying p.188's `A` with the increment `A_1` of (8) is licensed by “cf. the proof of Proposition 5.5”, and on the census it is exactly `(12)∨(13) ∧ A_1 ≥ 2`. That strengthening is **DERIVED**, not printed. Extending it to every level is **NOT-IN-SOURCE**. `A_{r-1} = 1` is not a missing characteristic exponent.

### 2.1 p.187–188: exclusive or, and `A > 1`

Prop 5.5 (p.186) is the two-characteristic-pair reduction (`s = 2`). Moh writes `δ_1 = B/A` in lowest terms and (p.187, after “Clearly we have `0 < δ_1 < 1`”):

> i.e. the rational number `δ_1` is a true fraction and **`A > 1`**.

Then p.188 l.1–13:

> The conjugations of `k((t^{1/A}))` over `k((t))` show us that if the reduced denominator `A` of `δ_1` is not a factor of `deg g_σ(π) = n* V_2` then `π` is a factor of `g_σ(π)`. Moreover if `A` is a factor of `n* V_2` then `g_σ(π) ∈ k[π^A]` and `π` is a factor of `(d/dπ) g_σ(π)`. In view of the two co-prime conditions above we must have `A | n* V_2` and `A ∤ m* V_2` or `A ∤ n* V_2` and `A | m* V_2`. Moreover we always have from the very definition of `A` the following `A | (n* + m*) V_2 − 1`.

This **is** exclusive: if `A` divides both `n* V_2` and `m* V_2` then, with the identity, `A | 1`. When `A = 1` both “does not divide” clauses are false. Independently p.187 has `A > 1`. **PROVED-IN-SOURCE** for the `A` of Prop 5.5.

### 2.2 p.201 (12)/(13) is not that exclusive or, as printed

p.201, after defining the *increment* `A_{r-1}` in (8):

> Finally, when `r = 2` we must have the following (cf. the proof of Proposition 5.5):
>
> (12) `A_1 | (n/d_2) V_2`, `A_1 | (m/d_2) V_2 − 1`
>
> or
>
> (13) `A_1 | (m/d_2) V_2`, `A_1 | (n/d_2) V_2 − 1`.

Each branch is a conjunction; the connective is “or”. When `A_1 = 1` both hold. The printed pair does **not** force `A_1 ≥ 2`. That is why `cond1213` admits the 200 rows with `A_1 = 1`.

### 2.3 The increment `A_1` is not `den δ_1`

p.188's `A` is “the reduced denominator `A` of `δ_1`”. p.201's `A_1` is the increment of (8): reduced denominator of `L_1 δ_1`. These coincide in Prop 5.5 (`s = 2`, `δ_2 = −1`, `L_1 = 1`) and on the two `(75,50)` printed rows. They do not coincide in general:

```text
MEASURED n<=100 (1)-(13): 0<delta_1<1 on 658/658; A_1=1 on 200
  (all 200 have den(delta_1)>1); identity A_1|(n*+m*)V_2-1 on 658/658;
  xor on A_1 458/658 (fails exactly on A_1=1); xor on den(delta_1)
  77/658 (fails on 4 of 6 printed rows).
```

Fail-closed: xor on `den δ_1` **kills four of Moh's six rows**. The `A` that keeps the table is the increment `A_1`. Given the identity, printed `(12)∨(13) ⇔ e V_2 ≡ 0 or 1 (mod A_1)`; adding the xor is adding `A_1 ≥ 2`.

The exclusive disjunction is **PROVED-IN-SOURCE** (p.188). `A_1 ≥ 2` as a search predicate is **DERIVED** by reading (12)/(13) against the derivation they cite. The parenthetical “so `A_1 = 1` is inadmissible” is true of that derived reading and false of (12)/(13) as typeset.

### 2.4 Higher levels: `A_{r-1} = 1` is not “not a characteristic exponent”

(8)–(11) never say `A_{r-1} ≥ 2`. When `A_{r-1} = 1` the automorphism `t̄ ↦ ω t̄` of (8) is the identity, (9) has remainder 0, (10) collapses to the upper half of (7), and (11) is automatic. Vacuous, not excluded.

Characteristic data are the `M_i` (p.201(4)), with `d_r = gcd{n, M_1, …, M_{r-1}}` strictly dropping. MEASURED: `A_j = 1` at `j ≥ 2` on 92 `(1)–(13)` rows at `n ≤ 100`; in the samples the gcd still drops, and several have `δ_j = 0` (integer radius ⇒ increment 1) with a genuine new `M_j`. Those levels **are** characteristic in Moh's sense. The alternative reading is **NOT-IN-SOURCE** and false of the printed definitions.

| claim | type | citation |
|---|---|---|
| xor on p.188 | PROVED-IN-SOURCE | p.188 l.1–13 |
| `A > 1` in Prop 5.5 | PROVED-IN-SOURCE | p.187 |
| printed (12)/(13) exclusive as typeset | NOT-IN-SOURCE | both hold at `A_1=1` |
| `A_1 ≥ 2` as search predicate | DERIVED | xor + “cf. Prop 5.5” + identity |
| `A_j ≥ 2` for `j ≥ 2` | NOT-IN-SOURCE | (8)–(11) impose no such bound |
| `A=1` ⇒ not a characteristic exponent | NOT-IN-SOURCE | p.201(4)–(5); gcd still drops |

`OPEN[MOH-INCREMENT-j≥2]`, bounded 11+56+25 rows at `n ≤ 100` with `A_2, A_3, A_4 = 1`. The `j = 1` clause is DERIVED: the 200-row cut `658 → 458` of the xor, equivalently `658 → 391` of `A_j ≥ 2` for all `j`.

## 3. Q3 — Appendix II, per row, and the second point at infinity

**Location.** Appendix I occupies p.202 (after the table) through p.207 (Prop A.5). **Appendix II. Some special cases** is p.207–211; p.212 is References. p.202: “The treatment of these four exceptional cases will be presented in Appendix II.” p.207 reprints them as degrees `(64, 68), (84, 56), (75, 50) and (99, 66)` — the known `(64,68)→(64,48)` erratum; the Prop 6.3 image is `(16,12) = (64,48)/4`, which pins `m = 48`.

### 3.1 Extra datum per p.202 row (one line each)

Never in `{n, m, M_*, V_*}`.

| p.202 row | extra datum used in Appendix II |
|---|---|
| `(64,48)` `V_2=3` | Prop 6.4 (`u_3 = d_3−v_3 = 1`) + Prop 6.3 monomial-Jacobian transform to `(16,12)`; 4th approximate root `h` of `f̃`; π-root `σ^*` in the **minor** disc `D_1^*`; remainder-degree identities on the `α_i, β_i`; then an `η`-adic expansion cutting coefficients 244 → 17 → 10 (pp.207–209). |
| `(84,56)` `M_2=64` `V_2=2` | same Prop 6.3/6.4 transform to `(21,14)`; “similar arguments” (approximate roots + minor-disc `σ^*`); coefficients 5308 → 373 → 22 [15 or 13] → 12 [10 or 7] (pp.207–209). |
| `(84,56)` `M_2=72` `V_2=5` | same transform, bracketed alternate `(21,18)`; same method as the previous row. |
| `(75,50)` `V_2=3` | Prop 6.3/6.4 to `(15,10)`, Jacobian `X^2`; then **direct computation**: approximate-root identities `β^2 = α h + γ` with remainder `deg_y γ < 5`, and the inverse Prop 6.3 transform forcing a minor disc, hence a `2+2+6` split of roots of `f` in major `D_2`; coefficient cases `a_9 = 0` / `≠ 0` (pp.210–211). |
| `(75,50)` `V_2=2` | bracketed alternate of the same transformed row; p.211 finishes `V_2 = 3` explicitly and sends “all other cases” to the same remainder-degree / approximate-root computation. |
| `(99,66)` `V_2=8` | **not** Prop 6.3 (`u_3 = 11−8 = 3 ≠ 1`). Extra datum: the factor type of `g_σ(π)` from the distribution of `g`-roots in the minor disc `D_2^*` — either a power of a linear polynomial (transforms to `(27,18)`, Jacobian `X^4`) or the 9th power of a cubic with two roots, then an inversion `Ω: x ↦ x^{-1}`, `y ↦ a_0 + a_1 x + a_2 x^2 + y x^3`, analysed in `k⟪x^{-1}⟫` and `k⟪y^{-1}⟫` (pp.209–210). |

p.211 last two sentences: “All other cases can be computed directly as above. There is no counter-example of polynomials of degrees less than or equal to 100 for the Jacobian conjecture.” The endgame is coefficient identities after a transform, not a further arithmetic filter on `{M_*, V_*}`.

### 3.2 Second point at infinity / second tower

**Yes, §6 analyses the other point at infinity locally. No, there is no second Def 5.1 tower.**

Lemma 5.3 (p.185): smallest disc of all roots has radius `−1` iff `M_s = n−2` **and the highest homogeneous form of `g` has two roots**, one of multiplicity `(n/d_s) v_s`. Prop 4.5 (p.169): “at most two points at infinite.” Cor 6.1(3) (p.199): `δ_s = −1` “i.e., more than one point at infinite.” p.194: `g = [(y−ax)^{v_s} (y−bx)^{u_s}]^{n/d_s}`, `u_s = d_s − v_s`; “The major disc `D_s` […] contains a major disc `D_{s-1}` and a minor disc `D_{s-1}^*`.”

What §6 builds for the other point: Prop 6.1, a minor disc with only `δ^* ≥ 1` (no assigned `V`-sequence); Prop 6.2, after `z = y − bx − e`, **`deg_z g̃ = u_s n/d_s`**; Lemma 6.2, inversion; Prop 6.3, Jacobian a monomial `−(u_s/b) γ^{v_s−u_s−1}` (the Appendix II transform when `u_s = 1`); Prop 6.4, `u_s = 1 ⇒ δ_{s-1}^* ≥ v_s`. No second `{n, M_i, V_i}` and no second search (1)–(13). Appendix II consumes the minor-disc π-root and, for `(99,66)`, inversion `Ω` into `k⟪x^{-1}⟫` and `k⟪y^{-1}⟫`.

Uniform-theorem shape: every Appendix II extra datum is an approximate root plus a remainder-degree identity, a monomial-Jacobian transform, a minor-disc factor type, or an inversion. None of those live in `{n, m, M_*, V_*}`.

## 4. Reproduction (fail-closed)

Predicates as in charged `moh4.py` / `battery.py`, unmodified `box/moh_skeleton_full.py`. Driver rerun this session (wall 8 s) plus independent cascade (wall 15 s). Every charged number matches to the unit.

| claim | result | detail |
|---|---|---|
| 6/6 p.202 rows kept under MOH-4 | **CONFIRMED** | all six `full_ok` ∧ `incr` ∧ `any10` ∧ `V_j≥2` |
| `(75,50)` residue `{M=(55,73), V_2 ∈ {2,3}}` | **CONFIRMED** | `(1)–(13)`: 9 rows, `M_2 ∈ {5,10,40,55,60}`; three clauses leave exactly the two printed rows |
| `658 → 391 → 247 → 86 → 51` | **CONFIRMED** | 658/63 classes; +INCREMENT 391/62; +NOT-ALL-(11) 247/42; MOH-3 86/15; MOH-4 51/13 |
| `D = 105` empties | **CONFIRMED** | 14 → 8 → 4 → **0** groups. The three pinned-N groups all have `V_2=1`; a fourth `any10∧incr` group `m=84 M=[70,103] V_s=5` also has `V_2=1` |
| emptied degrees `{48,60,63,81,88,104,105,110,152,154}` | **CONFIRMED** | MOH-3 empties all but 48; MOH-4 adds 48 |
| groups `14,016 → 2,652 → 1,908` | **CONFIRMED** | `48≤D≤200`, `K≥16` |

Incidence CONFIRMED: `A_1=1` on 200/658; `A_2=1` on 11; `A_3=1` on 56; `A_4=1` on 25. **Discrepancy, uncharged.** Ideation §1.3 “MOH-4” per-degree counts 28, 127, 273, 538, 540 are this lane's **MOH-3** numbers; MOH-4 is 25, 82, 168, 430, 357. Charged cascade and emptied-degree list are not affected. `(75,50)` after the three clauses: `M=[55,73] V={2:2,3:4} A=[3,5]` (12); `V={2:3,3:4} A=[2,5]` (13).

## 5. FALLACY-v2 / OPEN

Flag/place/series not used. No exit claim, no `charge_basis`. Census counts are exact enumerations. Analogy gaps not filled: `A_j ≥ 2` for `j ≥ 2` is NOT-IN-SOURCE, not inferred from `j = 1`; `V_i = 1 ⇒` minor is NOT-IN-SOURCE.

```text
OPEN[MAJOR-MULT]         NOT-IN-SOURCE / CONJECTURE. 161 rows n<=100;
                         744 groups 48<=D<=200; the D=105 trio.
                         If rejected, D=105 does not empty here.
OPEN[MOH-INCREMENT-j>=2] NOT-IN-SOURCE. 11+56+25 rows with A_2,A_3,A_4=1.
                         j=1 is DERIVED, not OPEN.
OPEN[MOH-PROGRAM]        45 excess rows / 9 classes under the three
                         clauses (51 vs Moh's 6); 652 under (1)-(13).
                         Appendix II uses non-skeleton data.
```

## 6. Typed block

```text
LANE          moh-source-three-questions (Grok 4.6), 2026-09-03
SOURCE        Moh 1983 JRAM 340, 300-dpi images, 6c8847a8d8374f7d
Q1            NOT-IN-SOURCE (CONJECTURE). Def 5.1(2) V_i > d_i/(n-M_i);
              Prop 5.3 V_r = multiplicity; Prop 6.1 minor if
              d_r/(n-M_r) >= V_r >= 1; Thm p.200(4)-(5) major =
              more than n/(n-M_r) g-roots. j=s slice V_s>=3 is
              DERIVED from (7)+Cor 6.1.
Q2            xor p.188 PROVED-IN-SOURCE; A>1 p.187 PROVED-IN-SOURCE.
              Printed (12)/(13) NOT exclusive (both hold at A_1=1).
              A_1>=2 as search predicate DERIVED. A_j>=2 for j>=2
              NOT-IN-SOURCE. "A=1 => not a characteristic exponent"
              NOT-IN-SOURCE (false).
Q3            App II p.207-211. Extra datum: Prop 6.3/6.4 + approx
              roots + minor-disc pi-root (first five rows); (99,66)
              minor-disc factor type or inversion Omega. Section 6
              analyses the other point at infinity locally; no
              second Def 5.1 tower.
REPRODUCTION  6/6 KEPT CONFIRMED; (75,50) residue CONFIRMED;
              658>391>247>86>51 CONFIRMED; D=105 empties CONFIRMED;
              emptied {48,60,63,81,88,104,105,110,152,154} CONFIRMED;
              groups 14016>2652>1908 CONFIRMED.
              Discrepancy: ideation §1.3 "MOH-4" per-D counts are MOH-3.
OPEN          MAJOR-MULT (161 rows / 744 groups / D=105 trio);
              INCREMENT j>=2 (92 rows); MOH-PROGRAM (45 excess rows).
ARTIFACTS     this report. No ledger edit. One core, 15 s.
```

<!-- BODY-END -->
