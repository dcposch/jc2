# Hostile different-model review — D73 equality control

| Field | Value |
|---|---|
| Claim under review | Frozen D73-STRICT-OR-EQUALITY local direction-collision gate: exact Jacobian-one germ matching sharp SP-2 x-side data; special-fiber `sum Lambda = pi(G)-1` at direction multiplicity 15; generic `a != 0` cover remains degree 3; Prop 7.3 equality is `if`, not `iff`; local strict upgrade false |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Evidence tier | independent exact algebra over `Q` (chart Jacobian, `df∧dg`, unit cube root, Puiseux characteristics, implicit-function cover); primary-source read of Sigray printed pp. 6, 10–18, 35–38 |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c17bd2542b40f3178ec619ae4a73501550555336` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T08:35:00Z – 2026-08-24T09:15:00Z |
| Python | 3.14.6; stdlib `fractions` / `math` only, used as a second arithmetic check, not as a substitute for the identities |
| Host | Darwin arm64 |

Producer input reread in full before any verdict:

- `xmodel/d73-strict-or-equality-20260824.md` (SHA-256 `90546ffb50b5cf8325195dc04a4e39b550e4075c057049529e29d8d188b698de`, matches the launch prompt)

Cited sources reread on-page against the committed basis `c17bd2542b40f3178ec619ae4a73501550555336`:

- `ladder/SHEET6-LROOT.md` lines 136–153, 184–195, 254–264 (committed wording; the working tree has a later uncommitted rewrite of 5c that already cites this producer — ignored as evidence)
- `ladder/SHEET6-LT-REVIEW.md` lines 90–110
- `refs/sigray_full.pdf` SHA-256 `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae` (matches the producer header): Notation 1.5; Definitions 3.1–3.3; Notations 3.5, 3.8–3.14; Proposition 3.1; Statements 3.9–3.18; Notation 7.1; Statement 7.1; Propositions 7.2–7.4, printed statement and geometric proof of Proposition 7.3 (pp. 36–38)

An internal hostile audit is stated to have passed. It was not opened and is not used. No producer, canonical, ladder, or PDF file was edited.

**Promotion.** Accept as `EQUALITY-CONTROL` of the *local* strictness gate only: direction multiplicity `≥ 2` does not force `sum Lambda ≥ pi(G)` in the analytic/Puiseux category that Proposition 7.3's proof actually uses. Promote nothing else.

**Quarantine.** The germ is not a polynomial Keller pair. It does not kill, realize, or even enter any of the eight terminal classes. It does not prove a global `δ` formula, a global equality case, or JC2, and it does not disprove any of those.

---

## Headline and subclaim table

Write `s = y^{-1}`, `t = xy^4`, `q(t) = t + t^{25}`, `q'(t) = 1 + 25 t^{24}`, and on a small bidisc about `(s,t) = (0,0)`

```text
g = q(t),     f = t^{15} + s^3 / (3 q'(t)).
```

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | In this chart `dx∧dy = s^2 ds∧dt` and `df∧dg = s^2 ds∧dt`, hence `J_{x,y}(f,g) = +1` exactly on the bidisc, not merely to leading order | **CONFIRMED** | chart det `s^4 · s^{-2}` without the orientation flip; leftover `dt` terms of `df` failing to wedge to 0 against `dg`; `J = -1` |
| 2 | Height-four leading data: `(k_f,l_f) = (60,15)`, `(k_g,l_g) = (100,25)`, `d_{f,G} = d_{g,G} = 0`, `p_G = t^{15}`, `p_{g,G} = t + t^{25}`, `pi(G) = 4`, `kappa_G = 1`, `mult(p_G,0) = 15`, first characteristic `21/5 > 4` | **CONFIRMED** | leading monomial of `f` not `x^{15} y^{60}`; `deg(t+t^{25})` not contributing at height 4; `e_1 ≠ 1`; `κ_G = 5` from using the pole order in place of `κ/e_0` |
| 3 | Special fiber `f = 0` has exactly three normalized branches, each of `y`-pole order 5, pairwise contact `21/5`, all in `R*_0`, each `Lambda = 1`, hence `sum Lambda = 3 = pi(G)-1` | **CONFIRMED** | `gcd(3,15) ≠ 3`; holomorphic cube root of `-3q'` failing; `z = t` not a uniformizer; contact identifiable under `μ_5` reparametrization; some branch omitted from `R*_0`; `ord_z(q(z)) ≠ 1` |
| 4 | For small generic `a ≠ 0`, all 15 roots `t_i^{15} = a` and their punctures lie in one bidisc; the values `q(t_i)` are pairwise distinct after shrinking; each local `Lambda` is 3; the local cover `g : A_a → B` has degree 3 over any one target; summing the fifteen `Lambda`s is a sum across different `g`-fibers | **CONFIRMED** | some `t_i` forced out of every neighborhood of 0; `q(t_i) = q(t_j)` for arbitrarily small `a`; `C_i = 0`; a second local inverse of `q`; degree 15 over one `b` |
| 5 | Proposition 7.3 gives equality *if* `mult(p_F-a,c) = 1`, not iff. The germ saturates the printed lower bound at multiplicity 15 and therefore locally refutes the proposed strict upgrade `mult ≥ 2, kappa_G = 1 ⇒ sum Lambda ≥ pi(G)` | **CONFIRMED** | a printed converse on p. 37; the germ's `R*_0` sum actually `≥ 4`; the upgrade only claimed for global polynomial pairs and the producer treating the germ as one |
| 6 | Scope: analytic/rational germ in `(x,y)`, not a global polynomial Keller pair; neither kills nor realizes any of the eight terminal classes; the only permitted conclusion is that direction multiplicity alone cannot yield the desired strict *local* defect | **CONFIRMED** | the producer promoting a class kill, a polynomial realization, a global `δ` law, or a JC2 decision |

All remarks below are non-blocking unless marked otherwise. None changes a Jacobian sign, a branch count, a `Lambda`, or a verdict.

---

## 1. Two Jacobians and the sign of `J_{x,y}(f,g)`

Chart and inverse, as written:

```text
s = y^{-1},     t = x y^4,     x = t s^4,     y = s^{-1}.
```

Differentials:

```text
dx = s^4 dt + 4 t s^3 ds,
dy = -s^{-2} ds,
dx ∧ dy = s^4 (-s^{-2}) dt ∧ ds = -s^2 dt ∧ ds = s^2 ds ∧ dt.
```

The inverse Jacobian is `∂(s,t)/∂(x,y) = s^{-2}`, and the product of the two determinants is 1.

Now `g = q(t)`, so `dg = q'(t) dt` with no `ds` term. Write `U = q'(t)` and

```text
f = t^{15} + (1/3) s^3 U^{-1}.
```

Then

```text
df = 15 t^{14} dt + s^2 U^{-1} ds - (1/3) s^3 U^{-2} U' dt.
```

The two `dt` summands wedge to 0 against `dg = U dt`, and

```text
df ∧ dg = (s^2 U^{-1} ds) ∧ (U dt) = s^2 ds ∧ dt = dx ∧ dy.
```

The producer’s compressed line `df∧dg = (s^2/q') ds ∧ q' dt` is exactly this: it discards the `dt` part of `df` because that part is killed by `dg`. Coordinate-free, `J_{x,y}(f,g)` is the coefficient of `dx∧dy` in `df∧dg`, hence `+1`. Equivalently on `{s ≠ 0}`

```text
J_{x,y}(f,g) = J_{s,t}(f,g) / J_{s,t}(x,y) = s^2 / s^2 = 1.
```

The denominator `q'(t)` is a holomorphic unit on a small disk: `q'(0) = 1`, and the nearest zeros lie on `|t| = 25^{-1/24} ≰ 0`. So `f` and `g` are holomorphic on a bidisc about the origin in `(s,t)`, and the identity is exact there, not a leading-form statement.

The same computation with `x = t s^R`, `f = t^L + s^{R-1}/((R-1) q')` gives both 2-forms equal to `s^{R-2} ds∧dt`. That is the §5 family, used only as a stability check; the numbered claim is the `(R,L) = (4,15)` case.

---

## 2. Height-four leading data

This is the `x`-component chart (Sigray form (4): `y = ∞`, `x` finite). Eggers coordinate at height 4 is `η_G = y^4 x = t`.

**Patterns at `G = I_P(4)`.** In the expansion (6) of Notation 3.10, the highest power of `y` wins.

- `f = t^{15} + y^{-3}/(3 q'(t))`. The second summand is strictly lower in `y`. Thus `d_{f,G} = 0` and `p_G(t) = t^{15}`.
- `g = t + t^{25}` is independent of `y`, so `d_{g,G} = 0` and `p_{g,G}(t) = t + t^{25}`.

Hence `deg p_G = 15 = l_f`, `deg p_{g,G} = 25 = l_g`, and `mult(p_G - 0, 0) = 15`. Both `d` vanish, and `π(G) = 4 > 1`, so Statement 7.1’s numerical content for membership in `T_{0,cv}` holds in this local chart.

**Newton data below height 4.** Substitute `t = x y^4` at bounded `t` and `y → ∞`:

- dominant monomial of `f` is `t^{15} = x^{15} y^{60}`,
- dominant monomial of `g` is `t^{25} = x^{25} y^{100}` (the summand `t = x y^4` is lower in `y`).

At the root `(0,x)` one therefore has `d_f = 60`, `deg p_f = 15` and `d_g = 100`, `deg p_g = 25`. Slope law: both vanish at height `60/15 = 100/25 = 4`. This is exactly the sharp SP-2 numerical row of committed `SHEET6-LROOT.md:184-195` (`k_f,l_f = 60,15`, type `(3,5)`, `(k_g,l_g) = (100,25)`, `R = 4`, `ψ = 3`). It is *local leading data* of an analytic germ, not a global Newton polygon of a polynomial of those degrees. The producer states it as such.

**Puiseux characteristics and `κ_G`.** After the normalization of §3, each branch is `y ∼ C z^{-5}`, `x ∼ C' z^{21} ∼ C'' y^{-21/5}`. So `e_0 = κ = 5`, the first nonzero coefficient is `c_{21}`, `21` is not divisible by 5, `β_1 = 21`, `e_1 = gcd(5,21) = 1`. The only characteristic exponent is `α_1 = 21/5 > 4`. Notation 3.5, printed p. 12: at height `u = 4` one has `α_0 = 0 ≤ 4 < 21/5`, hence `j = 0` and

```text
κ_G = κ / e_0 = 5/5 = 1.
```

No characteristic exponent and no split below 4: the three series share the zero truncation through height 4, and first separate at contact `21/5`. This is the local LR2 pin (`SHEET6-LROOT.md:136-153`): one `x`-cluster, `κ_G = 1`, `π_G = R = 4`.

Non-blocking source alignment: Notation 3.5 is written for `F ∈ V_a`, and `u = 4` need not be a `V_{1,a}` or `V_{2,a}` point (those sit at `21/5`). The decoration `κ/e_j` is constant on the open edge from `(0,x)` to `I_P(21/5)`, and Proposition 7.3 is stated for `F ∈ T_{a,cv}`, not only for `V_a`. The value `κ_G = 1` is unambiguous.

---

## 3. Exact special-fiber normalization

On `f = 0`,

```text
s^3 = -3 q'(t) t^{15}.
```

The right-hand side at `t = 0` is 0; the prefactor `-3 q'(t)` is a holomorphic unit (`-3 q'(0) = -3 ≠ 0`). A small disk is simply connected and omits the zeros of `q'`, so a holomorphic cube root `U(t)` with `U(t)^3 = -3 q'(t)` exists. Setting `S = s/U(t)` yields the exact normal form `S^3 = t^{15}`.

Number of branches: `d = gcd(3,15) = 3`. Parametrizing each by the uniformizer `z = t`,

```text
S = ω z^5,     s = U(z) ω z^5,     ω^3 = 1.
```

The map `z ↦ (s,t)` is an embedding of a disk onto each branch, so `z` is a uniformizer at each puncture. Then

```text
y = s^{-1} ∼ C_ω z^{-5},     x = t s^4 = U(z)^4 ω^4 z^{21} ∼ C'_ω z^{21}.
```

`y`-pole order 5; first Puiseux term of `x` at exponent `21/5`. Leading coefficients scale as `ω^{-1/5}`. A `μ_5` reparametrization of `y^{-1/5}` multiplies the `j = 21` coefficient by a 5th root of unity; the ratio of leading coefficients of distinct cube-root branches is a nontrivial 15th root of unity, hence not in `μ_5`. Pairwise contact is exactly `21/5`, not higher. All three truncations below height 4 are zero, so they form one cluster through `G`.

**Membership in `R*_0`.** Proposition 7.3, printed p. 36: for `F ∈ T_{a,cv}` and a direction `c` with `F * c` defined,

```text
R*_a = { P ∈ R̄_a \ R_a : I_P(π(F) + 1/κ) = F * c }.
```

Suitable denominator `κ = 5`, `π(G) = 4`, so `π(G) + 1/5 = 21/5`. The coefficient of `y^{-4} = y^{-20/5}` vanishes, so the direction is `c = 0` and `G * 0 = I_P(21/5)`. Definition 3.3’s clause `u ≤ O(P,P')` at `u = 21/5 = O(P,P')` identifies all three points at this height. Locally these are all the punctures in that direction. Producer table “all three normalized ends are in `R*_0`” is correct.

**`Lambda`.** Notation 1.5, printed p. 6: `Λ(P)` is the multiplicity of `g` at `P`. On each branch `g = q(z) = z(1 + z^{24})` has a simple zero, so `Λ(P) = 1`. Therefore

```text
∑_{P ∈ R*_0} Λ(P) = 1+1+1 = 3 = κ_G(π(G)-1) = π(G)-1,
```

while `mult(p_G,0) = 15 ≥ 2`. This is equality in the printed lower bound of Proposition 7.3, at a multiple direction.

Pole-order check (not used as a proof, only as a conservation sanity): generic fiber in this chart has 15 punctures of `y`-pole order 1; special fiber has 3 punctures of pole order 5; `15 · 1 = 3 · 5 = l_f`.

---

## 4. Generic `a ≠ 0`: neighborhood, distinctness, multiplicity 3, cover degree 3

Fix a bidisc `A` small enough that `q'` is a unit and `q` is injective (possible since `q'(0) = 1`). For `0 < |a|` small, the equation `f = a` on `s = 0` is `t^{15} = a`, hence fifteen distinct roots `t_i` with `|t_i| = |a|^{1/15} → 0`. All fifteen points `Q_i = (0, t_i)` lie in `A`.

**Distinct `g`-values.** `q(t_i) = q(t_j)` with `t_i ≠ t_j` would require `1 + ∑_{k=0}^{24} t_i^k t_j^{24-k} = 0`. The extra sum is `O(|a|^{24/15}) → 0`, so after shrinking it cannot equal `-1`. The values `b_i = q(t_i)` are pairwise distinct.

**Local multiplicity 3.** Implicit function: `Φ(s,t) = t^{15} - a + s^3/(3 q'(t))`, and `∂Φ/∂t(0,t_i) = 15 t_i^{14} ≠ 0`. Thus `t - t_i = C_i s^3 + O(s^6)` with

```text
C_i = -1 / (45 q'(t_i) t_i^{14}) ≠ 0
```

(`q'(t_i) ≠ 0` by the same shrinking). Then

```text
g - b_i = q'(t_i)(t-t_i) + O((t-t_i)^2) = C'_i s^3 + O(s^6),   C'_i ≠ 0.
```

On the generic compactified fiber, `s` itself is a uniformizer at `Q_i` (the graph `t = t(s)` is an embedding). Hence `Λ(Q_i) = 3 = κ_G(π(G)-1)`, which is the simple-direction equality case of Proposition 7.3. Each of the fifteen simple roots of `p_G - a` may be followed inside `A`. Local tree transport does not fail.

**Cover degree over one target.** For small `b`, local invertibility of `q` produces exactly one `t = q^{-1}(b)` in the disk. Then

```text
s^3 = 3 q'(t) (a - t^{15})
```

has three solutions counted with multiplicity. Degree of `g : A_a → B` is therefore 3, not 15. At `b = b_i` the three `s`-roots coalesce at `Q_i` (local degree 3) without raising the degree of the cover. At `(a,b) = (0,0)` the same total 3 is carried by three points of degree 1.

**Hidden summation.** The fifteen generic punctures lie over fifteen different values `b_i`. Adding their `Lambda`s is a sum across different fibers of `g`, not a computation of `∑_{P ∈ R*_c} Λ(P)` for one collided direction of one fiber of `f`. Proposition 7.3’s geometric proof (printed pp. 37–38) picks *one* nearby simple `Q ∈ A_ã` and uses `∑_{R*_a} Λ ≥ Λ(Q) = κπ - κ`. It does not add the other fourteen simple roots sitting over other `b`’s. A theorem equating that illegal sum `15 · 3` with the multiplicity at the collided value is false for this exact Jacobian-one germ: the collided sum is 3.

The same count is visible in the Euler grouping of Proposition 7.5’s proof: each pair `(a, b_i)` is a distinct point of the value-curve `(p_G(c), p_{g,G}(c)) ≅ C`, and the vertex is charged once, not fifteen times.

---

## 5. Source wording versus the proposed strict upgrade

Proposition 7.3, printed p. 37, after the inequality `∑_{P ∈ R*_a} Λ(P) ≥ κ_F π(F) - κ_F`:

> In the special case `mult(p_F − a, c) = 1`, we have `R*_a = {P}`, and `Λ(P) = κ_F π(F) − κ_F`.

That is a sufficient condition for equality, not a necessary one. There is no converse on pp. 36–38. The geometric half of the proof (preimage count in a small bidisk) yields only `≥`. Committed `SHEET6-LT-REVIEW.md:90-94` records this accurately. Committed `SHEET6-LROOT.md:45` and `:254-259` twice write “equality iff `mult = 1`”; that “iff” is not in the primary source. The producer’s wording correction is right.

The proposed local upgrade was

```text
mult(p_G - a_*, c) ≥ 2,     κ_G = 1
    ⟹    ∑_{P ∈ R*_{a_*}} Λ(P) ≥ π(G).
```

For this germ the hypotheses hold (`mult = 15`, `κ_G = 1`) and the conclusion fails (`sum = 3 < 4`). The germ therefore locally refutes the upgrade in the analytic/Puiseux category that the printed proof actually uses. It does not refute a *global polynomial* statement that the producer never claims; see §6.

The mechanism (producer §5) is the same identity that makes the SP-2 numbers work: after a unit change the special fiber is `S^{R-1} = t^L`, with `d = gcd(R-1, L)` branches and `g`-multiplicity `(R-1)/d` on each, totaling `R-1` independently of the collision multiplicity `L`. Multiplicity of `p_G` records tangency of the boundary value map; normalization can absorb it into fewer branches with compensating ramification. It need not create another sheet of `g`.

---

## 6. Scope and explicit exclusions

As a function of `(x,y)` on the affine plane,

```text
g = xy^4 + (xy^4)^{25}          (polynomial),
f = (xy^4)^{15} + y^{-3} / (3 (1 + 25 (xy^4)^{24}))
```

is rational in `(x,y)`, holomorphic only for large `|y|` and small `|xy^4|`, and is not a polynomial. Jacobian one on that bidisc does not produce a global Keller pair, does not pin any opposite-side (`y`-component) template, and does not meet Lemma 2.1 as a normalized polynomial counterexample.

Consequences, all required:

- none of the eight terminal classes of committed `SHEET6-LROOT.md:172-181` is realized;
- none of them is killed;
- the eight-class book is not altered;
- no global equality case of (22) is proved;
- JC2 is neither proved nor disproved;
- the remaining named surface is exactly committed `SHEET6-LROOT.md:260-264` as written on the charged basis: `x`-side realizability versus the pinned opposite-side templates, or a global balance law on a compactified polynomial fiber.

The only permitted conclusion is the local one: direction multiplicity alone cannot yield the extra local `δ` unit.

---

## Source caveats (none load-bearing)

1. Proposition 7.3 is stated for polynomial Jacobian pairs. The refutation is of a *local* strengthening of its inequality, in the bidisk category of its geometric proof. That is the producer’s stated scope; it is not a hidden swap of categories.
2. Notation 3.5 defines `κ_F` on `V_a`. The cv point `I_P(4)` may lie on an open edge. The edgewise value is still `κ/e_0 = 1`, and Proposition 7.3 applies to `T_{a,cv}`.
3. Printed Statement 3.15 has the campaign’s standing label swap (E10). Direct multiplicity of `g` on a uniformizer is used here, so the swap is not load-bearing for any numbered claim.
4. Notation 7.3’s printed per-puncture display, read naively as `∑_P (Λ(P) − κ(π−1))` without grouping by direction/`b`, would go negative on this special fiber and contradict Proposition 7.4. The proof of Propositions 7.3 and 7.5 groups by the value-curve and charges the vertex once per `(F,b)`. The producer uses that grouped `R*` sum, which is the quantity the upgrade was about. This is a source-display caution, not a hole in the germ.
5. Committed LROOT’s “iff” is a wording error in the *campaign*, correctly isolated by the producer; this review does not edit LROOT.
6. The `t^{25}` term is required to match `deg p_{g,G} = l_g = 25`. Dropping it would preserve `J = 1` and the `Lambda` sum, but would miss the SP-2 `g`-pattern degree. It does not disturb local invertibility of `q` near 0.

---

## Promotion advice

**Accept** the report as a local `EQUALITY-CONTROL` closing the named D73 strictness gate: one cannot extract an extra local `δ` unit from `mult(p_G − a_*, c) ≥ 2` with `κ_G = 1` by any argument that lives in Proposition 7.3’s local analytic category.

**Do not accept** as any of the following:

- a polynomial realization of SP-2 or of any other terminal class;
- a kill of any slack-0 class, or a cut of the book 8 → 4;
- a global equality case of identity (22);
- a theorem that every polynomial Keller pair with this x-side data has `δ = 0` at the collision fiber;
- a JC2 decision.

Successor work, if any, has to be global: polynomial realizability of the unit-corrected germ together with the pinned opposite-side data, or an additional `g`-zero/branch on the same compactified polynomial fiber. That is outside this freeze.

---

## Explicit exclusions

This review does not:

- edit the producer file, `ladder/SHEET6-LROOT.md`, `ladder/SHEET6-LT-REVIEW.md`, `AUDIT.md`, `APPROACHES.md`, or `refs/sigray_full.pdf`;
- treat the internal hostile audit as evidence;
- assert that a holomorphic cube root of a unit extends beyond a disk;
- assert that `f` is polynomial, entire, or a finite map `C^2 → C`;
- assert anything about y-side orbits, pole clusters, or the (22) ledger of a global pair;
- invent a local excess formula that *would* force `δ > 0` for polynomial pairs.

Frozen producer SHA-256, recomputed on disk at review time:

```text
90546ffb50b5cf8325195dc04a4e39b550e4075c057049529e29d8d188b698de  xmodel/d73-strict-or-equality-20260824.md
```
