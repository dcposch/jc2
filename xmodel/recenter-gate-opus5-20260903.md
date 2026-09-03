# Hostile gate — OPEN[FULL-TREE-RECENTER]: does the δ_j = 0 recentring close it positive?

Lane `recenter-gate-opus5-20260903` (Opus 5), basis `8a1b2df4`, receipt
`xmodel/recenter-gate-opus5-20260903.run.v2`.

**Hash gate.** Manifest generated mechanically from the receipt
(`awk -F= … charged_input_<i>_sha256 / _basename → sha256sum -c`, no digit
retyped): all **9 charged inputs OK**.

**Moh 1983 pages opened as images** (`pdftoppm -r 130`; PDF = journal − 139):
**pp. 164–166** (PDF 25–27; Prop. 4.1, 4.2, 4.3), **pp. 182–183** (43–44; end
of Prop. 5.3, Prop. 5.4 + the radius formula), **pp. 185–186** (46–47; Lemma
5.3, Prop. 5.5), **pp. 187–188** (48–49; the s = 2 proof, Prop. 5.6 statement),
**pp. 189–190** (50–51; the Prop. 5.6 proof and the recentring). All quotes
below from those pages are `SOURCE-READ`. Blind rule honoured: among this
round's submissions only `ideation-20260903T1200Z-fable5.md` was opened; no
in-progress lane report; no ledger edit; no `jc2-lean`.

---

## 0. Verdict — split, and the split is the whole finding

| claim | type | verdict |
|---|---|---|
| (a) a nonzero label at δ_j = 0 is a **constant**, removable by `y ↦ y − c` = p.190 with a = 0 | SOURCE-READ | **CONFIRMED** |
| (b) `y ↦ y − c` preserves the gauge (monic, deg = deg_y, all `M_i`, `J`) | PROVED-HERE | **CONFIRMED** |
| (c) the tower translates rigidly: radii, `V_i`, `d_i`, `M_i` unchanged | PROVED-HERE | **CONFIRMED** |
| (d) Lemma 5.3's top-chart flag is chart-covariant | SOURCE-READ | **CONFIRMED** for all of `y ↦ y − ax − b`, not just a = 0 |
| (e) p.189's ingredients (i)–(iii) survive the change | SOURCE-READ | **CONFIRMED**; (i) needs no automorphism (§2.3) |
| (f) different killing paths may use different constants | PROVED-HERE | **CONFIRMED** |
| (g) only δ = 0 is integral among intermediate radii; the rule fires only at integral δ | code-read + MEASURED | **CONFIRMED** |
| (h) Fable's MEASURED block (38/52, 0 mismatch, 14-row residue, s = 3 exact) | MEASURED | **CONFIRMED**, replayed exactly |
| **(i) "makes the path zero-typed": all tower labels zero ⇒ σ₁ = π t^{δ₁}** | claimed PROVED-HERE | **GAP** |

**Verdict: GAP.** `OPEN[FULL-TREE-RECENTER]` *as literally posed* — is the
edgewise recentring at an integral radius licensed? — **closes POSITIVE**;
Fable is right against the earlier "must centre every sibling chart" worry, and
right that the frozen rule never touches a non-integral radius. But the
consequence drawn — *"Prop 5.6 kills the path, therefore the POLY column is
promotable with operative numbers 20 / 7 and 1,420 / 686 / 459"* — does **not**
follow. The failing step is (i): the free-coefficient gap already recorded in
charged `whole-tree-review-opus5-20260903.md` §7.3, which the POLY column
inherits unchanged from its own baseline. The rule neither creates nor enlarges
that gap: on the *repaired* (gap-free) screen the δ = 0 rule is worth **19 rows
and 1 class** at n ≤ 100 (234 → 215 rows, 22 → 21 classes), unconditionally.
That is the promotable part.

---

## 1. What Prop. 5.6 actually requires (p.188, verbatim)

> **Proposition 5.6.** *Suppose that s ≥ 2 and that a tower of major discs*
> `D_s ⊋ D_{s−1} ⊋ ⋯ ⊋ D_1` *has been constructed. If the corresponding
> π-root* `σ_1`*, which is the unique one in* `D_1`*, is of the following form*
> `σ_1 = π t^{δ_1}` *then either* `k[x,y] = k[T_1^ψ, g] = k[f,g]` *or there
> exists an automorphism* `k[x,y] → k[x,y]` *which will reduce the degrees of*
> `f(x,y)`, `g(x,y)` *and* `T_1^ψ(f(x,y), g(x,y))` *simultaneously.*

The hypothesis is a statement about the **series** `σ_1`, not about the tower
labels: every coefficient below `δ_1` must vanish. Compare Prop. 4.1 (p.164):

> **Proposition 4.1.** *Let* `x = t^{−1}` *and* `σ = Σ a_j t^j + π t^δ` *be a
> π-root of* `g(y) = g(x,y)`. … `J_{t,π}(h(σ), g(σ)) = [λ_h h_σ(π) g'_σ(π) −
> λ_g g_σ(π) h'_σ(π)] t^{λ_g+λ_h−1} = −h_f(σ) t^{−2+δ}`.

Moh's notation carries an unrestricted `Σ a_j t^j`; Prop. 5.6 is the case where
that sum is empty. **As printed it requires zero-typing in the chart in which
the tower was constructed** — but hypothesis and both alternatives of the
conclusion are preserved by any degree-preserving automorphism (§2.4), so it
may equivalently be applied in *any* admissible chart. That much of Fable's
framing is right.

## 2. The covariance checks, against the print

### 2.1 Gauge and tower (pp.183, 185, 187)

p.185 prints `deg T_1^ψ(f,g) = deg_y T_1^ψ = −M_1 ∉ (n)`; p.187 prints
`M_1 = μ_1 = −deg_y T_1^ψ(y)`. Under `ỹ = y − c` (c ∈ k) the coefficient of
`y^d` in `h(x, y+c)` equals that of `y^d` in `h(x,y)`, so `deg_y` is preserved
*exactly* — for `g`, `f` and every `T_i^ψ` (which transform as
`T_i^ψ(f∘α, g∘α) = (T_i^ψ(f,g))∘α`). Hence every `M_i` and `d_i = gcd` is
unchanged; monicity persists; the degree-n homogeneous form is unchanged (a
constant shift is a degree-0 perturbation), so `deg g = deg_y g = n`; and
`J(f∘α, g∘α) = J(f,g)∘α` since `det dα = 1`.

p.183 prints the radius formula
`δ_i = 1 − (n−M_i)Π_{j>i}[V_j(n−M_j) − d_j] / {(n−M_s−1)Π_{j>i}[V_j(n−M_{j−1}) − d_j]}`
— byte-for-byte `TreePartition.radius` (`full_tree_partition.py:63–70`), a
function of `(n, M_i, V_j, d_j)` only. Def. 5.1's radii and labels are stated
**relative to a chart**, but the configuration translates rigidly: the roots of
`g(x, y+c)` are `{τ_j − c}`, so every disc, radius, `V_i` and multiplicity
carries across unchanged (discs of radius ≤ 0 are unchanged even as sets,
`ord c = 0 ≥ δ`). **CONFIRMED — chart-relative in definition, covariant in
fact.**

### 2.2 Lemma 5.3's top-chart flag (p.185, verbatim)

> **Lemma 5.3.** *Suppose that* `g(x,y)` *is monic in y with*
> `deg g = deg_y g = n > 1`*. Then the smallest disc which contains all roots
> of* `g(y)T_1^ψ(y)` *is of logarithmic radius −1 iff* `M_s = n−2` *and the
> highest homogeneous form of* `g(x,y)` *has two roots with one root having a
> multiplicity* `(n/d_s) v_s` *where* `v_s` *satisfies* `d_s > v_s > d_s/2`.

The flag is about the **root multiplicities of the leading form** plus
`M_s = n−2`. Both are invariant under `y ↦ y − ax − b`: the substitution sends
`G_n(x,y)` to `G_n(x, y+ax)`, a linear reparametrisation of its roots
preserving their number and multiplicities, and `M_s` is a `deg_y`. The flag is
therefore covariant for the **whole** affine family, not just `a = 0` — which
also licenses the driver's `dangerous=True` start
(`full_tree_partition.py:365–371`), encoding the p.190 removal at δ_s = −1.
**CONFIRMED.**

### 2.3 The three ingredients of p.189

The printed proof is:

> *It follows from Proposition 5.4 and Lemma 5.3 that we shall only consider
> the case* `δ_s = −1`, `M_s = n−2` *and* `d_s > v_s`. … `δ_1 ≥ δ_{s−1} ≥ 0`. …
> *the polynomials* `g(x,y)` *and* `T_1^ψ(f,g)` *have no common polynomial
> factor* … *Especially y is not a factor of either* `T_1^ψ + c_1` *or*
> `g + c_2`*, say* `g + c_2`*, for all possible constants* `c_1` *and* `c_2`*.
> We conclude at once that there must be a term of the form* `x^l` *in*
> `g(x,y)` *for* `l ≥ 1`*. Then we have* `ord g(σ_1) = nλ ≤ −l`. …
> `nλ + (−M_1)λ − 1 = −2 + δ_1 ≥ −2` … `l = 1, nλ ≤ −1` …
> `δ_1 = nλ + (−M_1)λ + 1 ≤ (−M_1)λ < 0. A contradiction.`

* **(ii) the balance.** `nλ + (−M_1)λ − 1 = −2 + δ_1` is the exponent identity
  of Prop. 4.1(1) with `λ_g = nλ`, `λ_h = (−M_1)λ` (printed at p.187 and again
  at p.165, Prop. 4.2(1)–(2)). Prop. 4.1 is stated for a π-root with
  **arbitrary** `Σ a_j t^j`, and its right-hand side `−h_f(σ)t^{−2+δ}` comes
  from `J_{t,π}(x,σ) = −t^{−2+δ}`, which depends only on `δ`. **Covariant.**
* **(iii) `δ_1 ≥ δ_{s−1} ≥ 0`.** Pure arithmetic in `n, M_i, V_s, d_s` (top of
  p.189); those are gauge data, preserved by §2.1. **Covariant.**
* **(i) the pure `x^l` term.** Coprimality of `g` and `T_1^ψ(f,g)` is
  automorphism-invariant, and `J ∈ (h)` for a common factor `h` rules out
  `h = y − c` for every `c ∈ k`; so `g(x,c)` is non-constant for every `c`.
  **Covariant — and stronger than Fable claims: no automorphism is needed.**
  With `σ_1 = c + π t^{δ_1}`, `c ∈ k`, expand
  `g(t^{−1}, σ_1) = Σ_b g_b(t^{−1})(c + πt^{δ_1})^b`: the `π^0` coefficient is
  exactly `g(t^{−1}, c)`, of order `−l` with `l = deg_x g(x,c) ≥ 1`. Powers of
  `π` cannot cancel, so `ord g(σ_1) ≤ −l` and the rest of p.189 runs verbatim.
  (Moh's "say `g + c_2`" is a genuine WLOG: with the pure term in `T_1^ψ`
  instead, the same chain with `nλ < 0` for `(−M_1)λ < 0` gives `δ_1 ≤ nλ < 0`.)

### 2.4 One centred path suffices (f)

Prop. 5.6's hypothesis quantifies over **one** tower and **one** π-root, and
its conclusion is global. Translating by `c_B` to centre branch `B` leaves that
branch a valid tower with the same radii and multiplicities; sibling labels
become `C − c_B`, irrelevant to the hypothesis. Degrees are preserved exactly,
so a degree-reducing `β` for `(f∘α, g∘α)` gives `α∘β` reducing degrees of
`(f,g)`. Requiring *every* dangerous branch to die is therefore correct, not
over-strong — reaffirming charged §7.2 against the earlier worry. **CONFIRMED.**

---

## 3. The step that fails: "the path is zero-typed"

Fable's §2.1 asserts that with all tower labels zero except `c` at δ_j = 0,
`σ_1 = c + π t^{δ_1}`, so `α` produces Prop. 5.6's hypothesis. That equates
**the centre of `D_1`** with **the sum of the tower labels**. Def. 1.3 (p.146,
quoted in charged §7.3) writes the centre as `Σ_{j<δ} a_j t^j` over *all*
exponents below δ, and nothing in Def. 5.1 pins the `a_e` at non-radius
exponents. p.183 indexes the tower by the `M_i` (exactly `s` levels,
`δ_i = δ(M_i)`), and p.182's use of Prop. 4.4 gives only
`ord(τ_i − τ_j) > δ_{r−1}` — *no splitting* inside `(δ_r, δ_{r−1})`. It does
**not** give `a_e = 0` there: a nonsplitting shrink whose leading coefficient
has a single **nonzero** root re-centres the disc (p.164, "the δ-disc has to be
shrunk to determine the tree data") and contributes `a_e t^e` invisibly to
every order datum.

The failure is located precisely in ingredient (i). With `σ_1 = c(t) + πt^{δ_1}`
and `c(t)` non-constant, the `π^0` coefficient of `g(t^{−1}, σ_1)` is
`g(t^{−1}, c(t)) = Π_j (c(t) − τ_j)`, a sum of contact orders and in general
`≫ −l`. **`ord g(σ_1) ≤ −l` is exactly what breaks, and it breaks precisely
when the removed coefficient is not a constant** — which is why δ = 0 (and
δ = −1 via `ax`) is licensed and nothing else is.

Moh's own s = 2 display survives because there `L_1 = den(δ_2) = 1`, so the
centre's support is integral and `(−1, δ_1) ∩ ℤ = {−1, 0}`:
`σ_1 = a t^{−1} + b + π t^{δ_1}` (p.190). For `s ≥ 3` the lattice is finer.
Replaying the charged §7.3 free-set construction (`replay4.py`; control on
Moh's six reproduces the charged table row-for-row, `(99,66)` free = ∅):

```
 38 POLY-killed rows   : free set EMPTY on 14, NON-EMPTY on 24
 14 POLY+ODE survivors : free set EMPTY on  4, NON-EMPTY on 10
```

`GAP` — named step: **"all tower labels zero ⇒ σ₁ = π t^{δ₁}"**. Cheapest
test: already executed here (§5); it is a recount, not a new theorem.

---

## 4. The integrality claims (task item 2) — CONFIRMED

**Code.** `full_tree_partition.py:194–203`, `:205–214`:

```python
removable_nonzero = self.polynomial_recenter and delta_j.denominator == 1 and delta_j <= 0
newdanger = dangerous and (is_zero or removable_nonzero)
```

The rule fires only at an **integral, non-positive** radius — exactly Fable's
guard ("a nonzero label at a NON-integral radius is NOT removable").
**CONFIRMED by code-read.**

**Only δ = 0 is available.** From the p.183 formula, for `i < s` every
numerator factor `V_j(n−M_j) − d_j` is positive (window (10)/(11)) and is
strictly smaller than its denominator partner `V_j(n−M_{j−1}) − d_j` because
`M_{j−1} < M_j`; with `M_s = n−2` the outer denominator is `1`. Hence
`0 < N/D` and `δ_i < 1` **always**; `δ_i ≥ 0` is Moh's p.189 inequality
`δ_1 ≥ δ_{s−1} ≥ 0`. So the only integer an intermediate radius can be is 0,
and δ = −1 only at the top. Instrumenting the frozen DP over the whole n ≤ 100
census (`replay2.py`, both the global and the embed recursions):

```
 POLY rule FIRED at radii        : {'0': 2262}
 all radii <= 0 seen at DP levels: {'0': 5578}
 integral radii seen at DP levels: {'0': 5578}
```

**MEASURED: the rule never fires anywhere but δ = 0, over 5 578 level-visits.**

---

## 5. Replay of the charged numbers, and the operative counts

**Fable's MEASURED block replays exactly** (`replay1.py`, `replay2.py`):

```
 52 excess C_FULL_TREE_ODE rows; POLY+ODE excess 14
 δ=0 NONZERO selected edge: 38    killed by the POLY rule: 38    mismatch: 0
 integral non-zero radii on the 52 selected chains: 0; on the 14 chains: 0
 intermediate radius multiset: {'0':38,'1/7':5,'1/5':4,'17/44':3,'3/10':3,
   '8/35':2,'17/35':2,'5/11':2,'1/4':2,'3/11':2,'9/28':1,'25/77':1,'5/17':1,'9/29':1}
 52 excess: s {4:37, 5:15}, u_s = 1 on 52/52 → no s = 3 excess, i.e. at s = 3
   the screen is EXACT (Moh's six)
 14 residue: (90,60)×4, (96,64)×4, (96,72)×6; s {4:13, 5:1}; u_s = 1 on 14/14
```

Screen counts re-derived in-process from the frozen driver, and matching the
charged `full-tree-polynomial-ode-n100-audit.json`
(`survivors 20`, `excess 14`, `printed_rows_killed 0`):

| screen | n ≤ 100 rows / classes | printed killed | 48 ≤ D ≤ 200 V / groups / UNI |
|---|---|---:|---|
| `C_FULL_TREE_ODE` | 58 / 12 | 0 | 2,824 / 1,384 / 865 |
| `C_FULL_TREE_POLYNOMIAL_ODE` (charged) | 20 / 7 | 0 | 1,420 / 686 / 459 |
| **gated ODE** (§7.3 repair, no recentring) | **234 / 22** | 0 | not computed this lane |
| **gated POLY+ODE** (repair + δ = 0 rule) | **215 / 21** | 0 | not computed this lane |

(D ≤ 200 columns quoted from charged `whole-tree-review-opus5-20260903.md`
§8.1; its triple is `candidate-results.md`'s "D48-200 V/groups/UNI".) My gate
is validated by agreeing to the row with the sealed charged §7.4 line
"gated + ODE = **215 / 21**".

**The exact operative numbers.** *If* the free coefficients are assumed to
vanish (the convention `C_FULL_TREE` already runs on), the recentring is worth
38 rows, 58 → 20, 5 classes, and D ≤ 200 becomes 1,420 / 686 / 459 — **not
promotable, because the baseline is not**. *Gap-free*, the δ = 0 rule is worth
**19 rows and 1 class**, 234 → 215 / 22 → 21 at n ≤ 100, spread over
(72,48)×1, (80,32)×1, (84,56)×2, (90,60)×4, (96,64)×5, (96,72)×2, (96,80)×1,
(100,40)×1, (100,80)×2. **That is the promotable content of
`OPEN[FULL-TREE-RECENTER]`.** 19 ≠ §3's 14 because the gate is applied
per-branch inside the DP: a row can be killed gap-free on a sibling branch;
14 is the selected-chain-only count.

---

## 6. K = 16 ray and Moh's six (task item 4) — UNTOUCHED

`replay3.py`, frozen driver:

```
 K=16 ray (n=48t+16, m=32t+16, M=(n−12,n−2), V2=V3=3), t = 1..12:
   δ2 = 1/4 for every t;  ODE = True and POLY+ODE = True for every t;
   selected_mode at j = 2 is "nonzero";  POLY rule fired: 0 times.
 Moh's six: ODE = POLY+ODE = True; selected chains carry δ2 ∈ {1/4, 2/7, 1/5, 1/3};
   POLY rule fired: 0 times on any of them.  printed_killed = 0 on every screen.
```

`δ_2 = 1/4` has denominator 4, so `delta_j.denominator == 1` is false and the
rule is structurally incapable of touching the ray — consistent with delta
17(v)'s "danger clears on the nonzero label, no Prop 5.6 step is involved". The
ray's cofinality argument and the six printed rows are independent of this
lane's verdict in either direction. **CONFIRMED.**

---

## 7. Typed block and FALLACY-v2

```text
GATE         recenter-gate-opus5-20260903 (Opus 5), basis 8a1b2df4; 9/9 charged hashes MATCH
SOURCE-READ  Moh pp.164,165,166 (Prop 4.1/4.2/4.3), 182,183 (Prop 5.3 end, Prop 5.4 + radius
             formula), 185,186 (Lemma 5.3, Prop 5.5), 187,188 (s=2 proof, Prop 5.6 statement),
             189,190 (Prop 5.6 proof; y -> y - ax - b).  PDF pages 25-27,43-44,46-51
CONFIRMED    items (a)-(h) of the section-0 table, in full.  In particular: the delta_j = 0
             label is a CONSTANT and its removal is Moh p.190 with a = 0; gauge and tower
             are preserved exactly; Lemma 5.3's flag is covariant under all of
             y -> y - ax - b; p.189 (i) needs no automorphism (pi^0 argument); the frozen
             rule fires only at integral delta (code) and only at 0 (5578 level-visits);
             38/52 = 38 POLY kills, mismatch 0; residue 14 rows, u_s = 1, s >= 4
GAP          "all tower labels zero => sigma_1 = pi t^{delta_1}".  Prop 5.6 as printed needs
             the series, not the labels; the p.189 step that breaks is ord g(sigma_1) <= -l,
             whose pi^0 coefficient g(t^-1, c(t)) is uncontrolled for non-constant c.
             Same gap as charged whole-tree-review 7.3; INHERITED, not created, by POLY.
MEASURED     gap-free increment of the delta = 0 rule: 234/22 -> 215/21 at n <= 100 (19 rows,
             1 class); charged ungated increment 58/12 -> 20/7 (38 rows).  Gate implementation
             validated against the sealed charged 7.4 line "gated + ODE = 215 / 21".
             free set EMPTY on 14 of the 38 POLY-killed selected chains, on 4 of the 14 survivors
NOT PROMOTED the POLY column (20/7; 1,420/686/459).  Those numbers remain SOURCE-ASSERTED, GAPPED
NOT CLAIMED  any kill or survival of a realised Keller pair; anything about D = 108; cofinality;
             any change to the K = 16 ray or to Moh's six; any D <= C(N)
```

**FALLACY-v2.** No exit price asserted, so no `charge_basis` line is due.
*Flag/place/series:* radii, labels and the tower index `i` are kept distinct
from the disc exponent `e`; strict-below (`Σ_{j<δ}`) is kept apart from
at-level (`π t^δ`) throughout §3. *Carrier/attainment:* every §5 count is of
PATH-ARITH/tree survivor rows, never of pairs; "kill" = screen rejection.
*Floor/attainment:* 234 → 215 is an exact recount of the same DP, not a bound;
38 vs 19 compares two baselines and is stated as such. *Variable/ring map:*
`x = t^{−1}`, `ord` = t-adic valuation with `ord t = 1`, as printed in Prop. 4.1
(p.164); `λ_g = nλ`, `λ_h = (−M_1)λ`, `λ < 0` as in Prop. 4.2 (p.165). *Prime
label:* `'` is `d/dπ`, defined in Def. 4.1 (p.164). *Pole/interior*,
*`sat()`/remainder*: no ideal or pole computation here.

## 8. Drivers

`box/recenter-gate-20260903/` — `replay1.py` (witness-chain replay,
38/52/0-mismatch), `replay2.py` + `.json` (instrumented firing radii),
`replay3.py` (K = 16 ray t = 1..12; Moh's six), `replay4.py` (free sets;
control reproduces charged §7.3), `replay5.py` (gated screens, 234/22, 215/21),
their `.log` files, ten page images, and `work/` (frozen driver + skeleton,
hashes unchanged `875c098a…`, `d20bf084…`). Every script < 30 s, one core.

## OPENS RAISED

* `OPEN[CENTRE-SUPPORT]` — is the centre of `D_i` confined to `(1/L_i)ℤ`,
  `L_i = lcm(den δ_s, …, den δ_{i+1})` (the p.188 conjugation argument, which
  Moh runs only for `s = 2`, where `L_1 = 1`)? Bounded: p.188 top plus p.201;
  cheapest test one page image, different model. Fixes the free set, hence the
  exact size of §3's gap.
* `OPEN[NONSPLIT-RECENTRE]` — can a nonsplitting shrink inside
  `(δ_r, δ_{r−1})` have a **nonzero** single root, i.e. does the label list
  really omit centre data? Bounded: Prop. 4.4, pp.166–170; cheapest test one
  page image. A negative answer closes §3's gap outright and promotes the whole
  POLY column.
* `OPEN[GATED-D200]` — the D ≤ 200 column for the gated and gated+POLY screens
  (only n ≤ 100 computed here). Bounded: one rerun of `tree-independent.py`
  with the §5 gate; ~2 min desk.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20079`.
- Body SHA-256:
  `2bf0aff0760c2b48b2bb40ba0b4e1b96be224d8948ec2f2ae7191fc55ef1ddd9`.
- Frozen basis: `8a1b2df43e554512eecf58099ba116b2d408327c`.
