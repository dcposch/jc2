# Prop 6.3 radius gate: is the descent hypothesis discharged on the u_s ≥ 2 kills?

Lane `prop63-radius-gate-opus5-20260905`; basis `d7ff4cea`; adapter opus.
Drivers and logs: `box/prop63gate-20260905/`.

## 0. Verdict first

`MECHANICAL-CHECK`: PASS. The manifest was generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/prop63-radius-gate-opus5-20260905.run.v2` and checked with
`sha256sum -c`; all 8 frozen inputs under `/tmp/jc2-lane.I8LOUD/inputs`
returned `OK`. No digest was retyped. Manifest banked at
`box/prop63gate-20260905/inputs.sha256`.

```text
FLAG CLEARED — conditionally, and the condition is already banked elsewhere.

k=4 ray K=7  (21,14;15;6;4)   SAFE  UNCONDITIONAL.  Every admissible ancestor
                              is (147,98) with u_s = 1; Prop 6.4 discharges the
                              radius outright.  The one u_s ≥ 2 arithmetic
                              candidate, (57,38), is not (1)-(13)-admissible.
k=4 ray K=8/K=9 u_s=1 arms    SAFE  UNCONDITIONAL.  (168,112) 277 rows and
                              (189,126) 78 rows, all u_s = 1.
D=108 no-split  (24,16;18;7;4) DISCHARGED, not assumed.  The chain is explicit
                              in 17(fffff) §2.3 and 17(ssss); the residual
                              window (1,7/2) den ≤ 2 = {3/2,2,5/2,3} is proved
                              empty, the last member by the δ=3 split kill.
                              Standing dependency: 17(ddddd).
(99,66) case (A) (27,18;21;8;4) DISCHARGED by the same architecture.  Window
                              (1,8/3) den ≤ 3 = {4/3,3/2,5/3,2,7/3,5/2}; the
                              charged C2 replay returns exactly {2 [2,1],
                              5/2 [1,1,1]} after Galois, and those two ARE
                              branches B and C.  Standing dependency: the B/C
                              joint-chart kills.
SPLIT kills                   UNAFFECTED.  Confirmed structurally: Prop 6.3 is
                              needed only to descend.  No circularity — the
                              split kills are what discharge the radius, and
                              they consume no descent.
```

**The one sentence to carry away.** The audit's premise is right — for
`u_s ≥ 2` the radius is a real hypothesis and Moh proves nothing about it —
but on the two banked `u_s ≥ 2` rows it was *not* assumed: both lanes
discharged it as the complement of an exhausted split window, and this lane
re-derives the window bound (`N5`) from Moh's own Prop 6.4 proof rather than
relaying it. The audit's separate claim that the `k=4`-ray `K=7` row is a
`u_s ≥ 2` kill is **wrong**: `K=7` has no admissible `u_s ≥ 2` ancestor at all.

No new exit-price assertion is made, so no `charge_basis` line is licensed.

## 1. The hypothesis, exactly as printed

`SOURCE-READ`. Journal page `N` = PDF page `N−139`; images at 200 dpi in
`box/prop63gate-20260905/moh_p197-58.png`, `moh_p198-59.png`,
`moh_p199-60.png`, `moh_p207-68.png`. The PDF text layer garbles the
displayed fractions on p.197–198, so every quantity below was read off the
rendered page, not the text layer.

> **Proposition 6.3** (p.197). *Suppose that* `g(x,y)` *is monic in* `y` *with*
> `deg g(x,y) = deg_y g(x,y) = n > 1`, `δ_s = −1` *and the logarithmic radius
> of* `δ*_{s−1}` *of the minor disc* `D*_{s−1} ≥ v_s/u_s`. *Let* `z` *be
> defined by equation (10),* `y^{−1} = θ`… *Then there is a π-root*
> `σ = Σ a_j θ^j + π θ^{v_s/u_s}` *such that with* `γ = θ^{1/u_s}` *we have*
> (1) `ḡ(σ), T̄^ψ_1(σ),…,T̄^ψ_{s−1}(σ) ∈ k[γ,π]`, (2) *monic in* `π` *with
> π-degrees* `u_s n/d_s, u_s(−μ_1)/d_s, …, u_s(−μ_{s−1})/d_s`, (3)
> `J_{γ,π}(ḡ(σ), T_1^{−ψ}(σ)) = −(u_s/b) γ^{v_s−u_s−1}`.

So the radius condition is exactly

```text
(R)      delta*_{s-1}  >=  v_s / u_s ,      v_s = V_s ,  u_s = d_s - V_s .
```

Three things fix its meaning and none may be conflated (`FALLACY-v2 /
flag-place-series`):

* `δ*_{s−1}` is the **logarithmic radius of the minor disc** — by Prop 6.1
  (p.191), `δ*_{s−1} = min{ord(τ_i − τ_j)}` over the roots of
  `g(y)∏T_i^ψ(y)` lying at distance `> δ_r` from `τ`. It is therefore the
  **first-separation order of the minor cluster**, not a probe order and not a
  major radius `δ_i`.
* `v_s/u_s` is the **detector ceiling**: the p.194 top form
  `[(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}` puts `v_s n/d_s` roots in the major disc
  at contact `−1` and `u_s n/d_s` roots in the minor cluster, so
  `ord g(σ) = (n/d_s)(u_s δ − v_s)`, negative exactly for `δ < v_s/u_s`. The
  two objects coincide *numerically* in (R); they are not the same object.
* Prop 6.3's proof uses (R) once and concretely: it needs *all* coefficients
  `e_i` at exponents `1 ≤ i < v_s/u_s` in `y = bt^{−1} + e + Σ e_i t^i + …`
  to be **common** to the whole minor cluster (p.198, first line). That is
  precisely `δ*_{s−1} ≥ v_s/u_s`.

Moh's `≥ 1` estimate (p.194, from Prop 6.1) buys only the `t^0` coefficient
`e`, which is why the hypothesis is not vacuous whenever `v_s/u_s > 1`.

## 2. Why `u_s = 1` discharges it, and where the proof stops

### 2.1 The source discharge

`SOURCE-READ`, p.198, immediately after Prop 6.3's proof:

> **Proposition 6.4.** *Suppose that* `g(x,y)` *is monic in* `y` *with*
> `deg g = deg_y g = n > 1`, `δ_s = −1` **and** `u_s = 1`. *Then the
> logarithmic radius* `δ*_{s−1}` *of the minor disc* `D*_{s−1} ≥ v_s/u_s = v_s`.

Prop 6.4 is nothing but (R) under `u_s = 1`. Moh's own usage confirms the
reading: p.207, Appendix II — *"We shall apply Proposition 6.4 to the first
three cases. Note that in these cases we always have `u_3 = d_3 − v_3 = 1`.
Thus it follows from Proposition 6.3 that our table can be transformed…"* He
descends `(64,68), (84,56), (75,50)` and **not** `(99,66)`, the fourth case.
`(99,66)` is the one entry of Appendix II with `u_s ≥ 2`. The gap the audit
names is Moh's gap, and he respected it.

### 2.2 Where `u_s = 1` is load-bearing (p.199 proof, re-run at general `u_s`)

Moh's proof of 6.4: suppose `δ*_{s−1} < v_s`, let `σ` be the π-root at radius
`δ*_{s−1}`. Then `ord g(σ) = −v_s n/d_s + δ*_{s−1} u_s n/d_s < 0`; by
Prop 6.1(2) `σ` is a distribution detector; write `g(σ) = g_σ(π)t^{nλ} + ⋯`,
`T_i^ψ(σ) = T^ψ_{i,σ}(π)t^{−μ_i λ} + ⋯`. Then

> *"Note that* `g.c.d.(n/d_s, −μ_1/d_s, …, −μ_{s−1}/d_s) = 1`. *Thus the
> polynomials* `g_σ(π), T^ψ_{1,σ}(π), …` *are powers of a common linear
> polynomial. It contradicts the very definition of* `δ*_{s−1}`."

Two steps must be separated. The "powers of a common polynomial `p(π)`" is
Prop 4.6(1) (p.170) and is `u_s`-free. The word **linear** comes only from the
gcd. At general `u_s` the π-degrees are the ones Prop 6.3(2) prints —
`u_s n/d_s` and `u_s(−μ_i)/d_s`, and independently the count of minor roots —
so

```text
deg p  |  gcd(u_s n/d_s, u_s(-mu_1)/d_s, ...)  =  u_s * 1  =  u_s .
```

`u_s = 1` forces `deg p = 1`, one common centre, the whole cluster inside a
strictly smaller disc, contradicting minimality of `δ*_{s−1}`. **For
`u_s ≥ 2` the gcd is `u_s` and the contradiction simply does not close.**
Prop 6.4 is sharp, not merely stated conservatively.

### 2.3 RADIUS DICHOTOMY (`DERIVED-SOURCE`, this lane)

Running the same proof at general `u_s` yields a usable statement rather than
a failure:

> **Lemma R.** Let `g` be monic in `y`, `deg g = deg_y g = n > 1`, `δ_s = −1`.
> Then **either** `δ*_{s−1} ≥ v_s/u_s` (Prop 6.3 licensed), **or** the minor
> cluster genuinely splits at `δ = δ*_{s−1} ∈ [1, v_s/u_s)`, with leading
> polynomial `p(π)` satisfying `deg p | u_s`, and with `q ≥ 2` distinct
> centres, `2 ≤ q ≤ deg p ≤ u_s`; the split is proportional across `g` and all
> `T_i^ψ`.

Corollary (`u_s = 1`): the second alternative is empty — Prop 6.4.

> **Lemma R2 (denominator).** In the second alternative,
> `den(δ*_{s−1}) ≤ u_s`.
>
> *Proof.* All minor roots lie in `k((t^{1/N}))`; the cluster is Galois-stable
> because its centre `b ∈ k` (p.194 top form). The common truncation
> `σ_0 = Σ_{j<δ*} a_j t^j` is therefore Galois-invariant, so it has integer
> exponents and coefficients in `k`. For `τ = σ_0 + c_τ t^{δ*} + ⋯`, the
> generator `t^{1/N} ↦ ζ_N t^{1/N}` sends `c_τ ↦ ω c_τ` with
> `ω = ζ_N^{Nδ*}` of exact order `den(δ*)`. The set of `q` centres — the
> distinct roots of `p` — is `⟨ω⟩`-stable, so its nonzero part is a union of
> orbits of size `den(δ*)`; hence `den(δ*) | q` (no zero centre) or
> `den(δ*) | q−1`. Either way `den(δ*) ≤ q ≤ u_s`. ∎

Lemma R2 **is** the charged `N5` (`den(δ) ≤ u_s`, banked `PROVED` as
`n5-denominator` and relayed by 17(ssss)). Deriving it here from Moh's own
Prop 6.4 proof rather than relaying it is the two-instrument agreement the
gate wanted: the two routes give the same bound on both audited rows.

The practical consequence, and the shape of the whole residual:

```text
(R) fails  <=>  the minor cluster splits at some
                delta in [1, v_s/u_s) with den(delta) <= u_s .
```

That is a **finite, cheap, per-row** check, not an open analytic condition.

## 3. Per-row audit

Descent arithmetic (`box/prop63gate-20260905/descent_radius_audit.py`, on the
frozen `moh_skeleton_full.py`): `v_s = V_s`, `u_s = d_s − V_s`,
`ell = v_s − u_s − 1`, `(n',m') = ((n/d_s)u_s, (m/d_s)u_s)`,
`prop63_automatic ⇔ u_s = 1`.

### 3.1 The `k=4` ray, `ℓ = 4`: which ancestors exist at all

For a descended `(3K, 2K)` at `ell = 4` one has `v_s = u_s+5`, `d_s = 2u_s+5`,
and integrality of `n/d_s = 3K/u_s`, `m/d_s = 2K/u_s` forces `u_s | K`. The
full arithmetic candidate list and its `(1)-(13)` admissibility
(`ray_ancestors_K789.log`):

| `K` | `u_s` | ancestor `(n,m)` | `v_s/u_s` | admissible rows | Prop 6.4 |
|---:|---:|---|---:|---:|---|
| 7 | 1 | (147, 98) | 6 | **6** | AUTOMATIC |
| 7 | 7 | (57, 38) | 12/7 | **0** | — |
| 8 | 1 | (168, 112) | 6 | **277** | AUTOMATIC |
| 8 | 2 | **(108, 72)** | **7/2** | **17** | N/A |
| 8 | 4 | (78, 52) | 9/4 | **0** | — |
| 8 | 8 | (63, 42) | 13/8 | **0** | — |
| 9 | 1 | (189, 126) | 6 | **78** | AUTOMATIC |
| 9 | 3 | **(99, 66)** | **8/3** | **2** | N/A |
| 9 | 9 | (69, 46) | 14/9 | **0** | — |

**Finding, and it corrects the gate's premise.** `K = 7` carries **no**
`u_s ≥ 2` client. Its only admissible ancestors are the six `(147,98)` rows
`d = (147,49,7,1)`, `V_s = 6`, `u_s = 1`, all discharged by Prop 6.4. The
`K = 7` ray kill needs no radius argument and is **unconditional**. The same
holds for the `u_s = 1` arms at `K = 8` and `K = 9`.

Of the 17 `u_s = 2` rows at `(108,72)`: exactly one, `M = (−72,81,106)`,
`d = (108,36,9,1)`, `V = (7,7)`, `s = 3`, descends to a two-level chart with
`M_2' = 18` — the charged `(24,16;18;7;4)`. The other sixteen are `s = 4`
rows with `d = (108,36,18,9,1)`, whose descended `M' = (−16,−12,−10)` is a
**three-level** chart; they are not clients of the ray kill and are not in
scope here. `FALLACY-v2 / target-arrival-index`: the ray charts' own
`u' = K' − V_2'` (e.g. `u' = 1` for case (A)) is a *descended* index and is
never the `u_s` of (R).

### 3.2 `D = 108` no-split, `(108,72) V=(7,7)` → `(24,16;18;7;4)`

`d_s = 9`, `v_s = 7`, `u_s = 2`, so (R) reads `δ*_{2} ≥ 7/2`. **Not**
automatic. Was it assumed?

**No — 17(fffff) §2.3 states the chain and 17(ssss) supplies it.** By
Lemma R the failure of (R) means a split with `deg p = 2` at
`δ* ∈ [1, 7/2)`, `den ≤ 2`. 17(ssss) opens the window at `1` by Xu Prop 7.3
(order-1 probe ⇒ powers of a common **linear** polynomial ⇒ `δ* > 1`) and
closes it at `7/2` by the Prop 6.1 order identity
`ord g(σ) = 12(2δ − 7) < 0`. Candidates, recomputed here independently
(`radius_window.log`):

```text
window (1, 7/2), den <= 2 :   3/2,  2,  5/2,  3     -- exactly 4, agreeing
                                                       with 17(ssss) verbatim
```

* `3/2, 2, 5/2` — `EXCLUDED` **by two independent routes** (charged 17(ssss)
  §2, Verdict block): Xu Cor. 7.5, which applies below
  `(v_s+1)/(u_s+1) = 8/3` because at `u_s = 2` a genuine split *is* a split to
  `u_s` distinct roots; and the face-ODE budget, where a `[1,1]` split needs
  `ρ = (51δ−176)/(2δ−7)` integral and only `δ = 3` has it.
* `3` — `SURVIVES` the classification (`p = π²−c`, `q = p²³u`), and is killed
  separately as `DEAD[D108/delta3/DECLARED-NECESSARY-JOINT-CHART]` in
  17(ddddd), relayed by 17(fffff) §0 and §2.3.

Window empty ⇒ (R) holds ⇒ Prop 6.3 licensed ⇒ the `(24,16;18;7;4)` chart is
the correct descended object ⇒ the `UNIT_IDEAL_CHAR0` kill of 17(bbbbbb)
closes the row. **Radius DISCHARGED**, with one standing dependency:
17(ddddd). Not circular: §4.

The residual language in 17(fffff) — *"the premise is the complementary
alternative to a now-empty split window, not a proof that every pair with this
skeleton has `δ* ≥ 7/2`"* — was written while `δ = 3` was still alive. Once
the window is **empty**, the complement is everything and the conditional
becomes a proof. That upgrade is the substance of this gate.

### 3.3 `(99,66)` case (A), `(27,18;21;8;4)`

Case (A) is `S8`: `M = (−66,77,97)`, `d = (99,33,11,1)`, `V = (8,8)`, so
`d_s = 11`, `v_s = 8`, **`u_s = 3`**, `v_s/u_s = 8/3`, `ell = 4`,
`(n',m') = (27,18)`. Answering the gate's question directly: case (A) is
`u_s = 3`, **not** `u_s = 1`; the `u' = 1` that appears in the descended
4-tuple is the arrival index `K'−V_2' = 9−8`, a different object.

Only 2 of the 8 admissible `(99,66)` rows are `u_s = 1` (`V=(1,10)` and
`V=(2,10)`, both descending to `(9,6)` at `ell = 8`) — reproducing the
`prop63_automatic` reading quoted in the round's ideation, and confirming that
the flag tracks `u_s = 1` exactly.

Window by Lemma R/R2, `deg p | 3` and `deg p ≥ 2` so `deg p = 3` with
`q ∈ {2,3}` (partitions `[2,1]`, `[1,1,1]`), `den ≤ 3`:

```text
window (1, 8/3), den <= 3 :   4/3,  3/2,  5/3,  2,  7/3,  5/2     -- exactly 6
```

Charged 17(ssss) control **C2** is a replay of the `(99,66)` screen and its
`[ok]` line reads: *"the screen returns exactly `{2 [2,1], 5/2 [1,1,1]}` at
`(99,66)` after Galois, with `(25,14)` forced at `δ = 2` and
`{(10,10,10),(14,10,10),(14,14,10)}` at `5/2` — Xu's printed vectors."* So
four of the six candidates (`4/3, 3/2, 5/3, 7/3`) are excluded and the
survivors are exactly two — **and those two survivors are branches B and C**,
which the campaign killed by the joint chart. Hence:

```text
delta* < 8/3  =>  split at 2 [2,1] or 5/2 [1,1,1]  =  branch B or C  =  dead
             =>  delta* >= 8/3  =>  Prop 6.3 licensed on case (A).
```

**Radius DISCHARGED** for case (A), with standing dependency on the B/C
joint-chart kills. The `A / B / C` trichotomy is not a convenience: it is
*exactly* the Lemma R dichotomy with the second alternative enumerated, so
completeness of the trichotomy and discharge of (R) are the same statement.

Sibling row `S4` (`M = (−66,22,97)`, `V = (1,8)`) has identical
`(d_s, v_s, u_s)` and therefore the identical window, but a different `μ_2`
and hence a different face-ODE. The charged C2 line says "at `(99,66)`"
without naming the row; if `S4` is to be closed through the same descended
chart, its screen must be replayed on its own data. Typed below.

### 3.4 The `u_s = 1` population, and the `≤ 100` claim

`u_s = 1` ⇒ SAFE is now a theorem with a one-line test, so any row list can be
cleared by inspection. Measured on the frozen census (`sweep_48_100.log`,
`Kmin = 16`, full `(1)-(13)`): at `48 ≤ n ≤ 100` there are 592 admissible
rows, of which **457 are `u_s = 1` (SAFE) and 135 are `u_s ≥ 2` (live)**; no
row has `u_s ≤ 0`.

The gate's "14 excess `≤ 100` rows, which are `u_s = 1`" could **not** be
reproduced from the charged inputs. The unscreened `(1)-(13)` census at
`n ≤ 100` has 28 distinct degree pairs — Moh's four plus **24** excess, not
14 — and of those 24 only seven are entirely `u_s = 1`: `(72,54)`, `(80,32)`,
`(80,48)`, `(80,64)`, `(90,36)`, `(90,72)`, `(96,80)`. The other seventeen
contain `u_s ≥ 2` rows. So the 14-row list must be a *screened* subset (the
whole-tree screen 17(r)/(hh)/(ll) is not in this lane's inputs). The claim
"all 14 are `u_s = 1`" is therefore neither confirmed nor refuted here; it is
a one-line check against the flag, and it is listed as an OPEN rather than
assumed.

## 4. The split kills are unaffected — and there is no circularity

`CONFIRMED`, structurally and from the charged text. Prop 6.3 is a
*change of variables*: it exists to trade `deg` for monicity and produce
`k[γ,π]`. A kill carried out on the **original** `(x,y)` data consumes
nothing from §6. The two split families are exactly that:

* `(99,66)` branches B (`δ = 2`, `[2,1]`) and C (`δ = 5/2`, `[1,1,1]`) — the
  joint chart is built in the tower coordinates of the un-descended row
  (17(ssss) §4 tower blocks `77/198/319/1683/2772/594/1683 = 7326`).
* `D = 108` `δ = 3` incidence — 17(ssss) `SURVIVES[108-DELTA-3]` face
  `p = π²−c`, killed in 17(ddddd) on the declared-necessary joint chart.

Neither invokes (R), neither invokes Prop 6.3, and neither is reachable only
through the descended chart. The dependency graph is a tree, not a cycle:

```text
split classification (17(ssss), N5, Xu 7.3, Cor 7.5, ODE budget)
   |-- split branches killed  ---------------> [independent of Prop 6.3]
   `-- window empty => (R) holds => Prop 6.3 => descended chart
                                                 |-- 17(bbbbbb) UNIT_IDEAL
```

The corollary worth stating: the split kills are **doubly load-bearing**. They
kill their own branch *and* license the descent on the complementary branch.
Withdrawing 17(ddddd) would not merely re-open `δ = 3`; it would re-open the
`D = 108` no-split descent as well. That coupling should be recorded wherever
those kills are banked.

## 5. Verdict, per row

| row | `u_s` | (R) | status | residual |
|---|---:|---|---|---|
| `k=4` K=7 `(21,14;15;6;4)` ← (147,98) ×6 | 1 | `δ*≥6` | **UNCONDITIONAL** | none (Prop 6.4) |
| `k=4` K=8 arm ← (168,112) ×277 | 1 | `δ*≥6` | **UNCONDITIONAL** | none (Prop 6.4) |
| `k=4` K=9 arm ← (189,126) ×78 | 1 | `δ*≥6` | **UNCONDITIONAL** | none (Prop 6.4) |
| D=108 no-split `(24,16;18;7;4)` ← (108,72) V=(7,7) | 2 | `δ*≥7/2` | **DISCHARGED** | 17(ddddd) δ=3 kill must stand |
| (99,66) case (A) `(27,18;21;8;4)` ← S8 V=(8,8) | 3 | `δ*≥8/3` | **DISCHARGED** | B/C joint-chart kills must stand |
| (99,66) S4 V=(1,8) → same chart | 3 | `δ*≥8/3` | **CONDITIONAL** | own C2 replay not exhibited |
| (99,66) branches B, C | 3 | n/a | **UNAFFECTED** | Prop 6.3 not used |
| D=108 δ=3 incidence | 2 | n/a | **UNAFFECTED** | Prop 6.3 not used |

No verdict is downgraded to `CONDITIONAL[PROP63-RADIUS]`, because on every
audited row the radius was computed and compared to `v_s/u_s` rather than
assumed — which is what FALLACY-v2 demands. The honest qualifier is that two
rows' discharges are *inherited from split kills banked in other lanes*
(17(ddddd); the B/C joint charts), neither of which is charged here; they are
relays, and they are typed as such.

## 6. FALLACY-v2 audit

*Flag/place/series*: `δ*_{s−1}` (first-separation order of the minor cluster),
the probe order `δ` in Lemma R, the detector ceiling `v_s/u_s`, and the major
radii `δ_i` are four objects; the coincidence `7/2 = v_s/u_s` at `D = 108` is
numerical and is never used as an identification.
*Floor/attainment*: Prop 6.1's `δ* ≥ 1` is a floor and buys only the `t^0`
coefficient; the descent needs the strictly stronger (R), and this is stated,
not elided. "Empty window ⇒ (R)" is a proof by exhaustion of a finite list,
not a floor promoted to equality.
*Carrier/attainment*: 17(ssss)'s "SURVIVES" is a screen result; this lane
consumes it only in the direction *excluded ⇒ absent*, never *survives ⇒
exists*.
*Prime label/derivative*: `n', m', M', V', u', K'` are labels for descended
data throughout; `p'` in the relayed ODE is `d/dπ`, as declared in 17(ssss).
*Variable/ring map*: Lemma R2's Galois action is on `k((t^{1/N}))` with
`t = x^{−1}`, generator `t^{1/N} ↦ ζ_N t^{1/N}`; `θ = y^{−1}` and
`γ = θ^{1/u_s}` are Prop 6.3's variables and are not identified with `t`.
*Target/arrival index*: `u_s = d_s − V_s` (ancestor, in (R)) and
`u' = K' − V_2'` (descended) are kept strictly apart; §3.3 flags the case (A)
instance where they are 3 and 1.
*`sat()`*: not used. *Raw remainder degree*: no normal form taken here.
*Merge-free/M-descent*: not touched.
No exit-price assertion is made, so no `charge_basis` line is emitted.

## 7. Reproduction

All in `box/prop63gate-20260905/`, foreground, single-threaded, < 20 min total:

```text
inputs.sha256                 awk-generated manifest; sha256sum -c => 8/8 OK
descent_radius_audit.py       descent map + Prop 6.4 flag on the frozen census
  descent_9966_10872.log        (99,66) 8 rows; (108,72) 199 rows
  sweep_48_100.log              592 admissible rows, 48<=n<=100: 457 / 135
  ray_ancestors_K789.log        ell=4 ray ancestors, K=7,8,9, with admissibility
radius_window.py              Lemma R/R2 window per row
  radius_window.log             {3/2,2,5/2,3} at D=108; {4/3,3/2,5/3,2,7/3,5/2}
                                at (99,66); empty at every u_s=1 row
moh_p197-58.png .. moh_p207-68.png    the four pages actually read
```

## OPENS RAISED

- `OPEN[PROP63-RADIUS-DISCHARGE]` — **closable as written; recommend
  reclassifying to `DISCHARGED-BY-COMPLEMENT`**. The number of banked
  `u_s ≥ 2` descent kills whose radius is undischarged is `= 0`; the number
  whose discharge is inherited from an uncharged split kill is `= 2`
  (D=108 via 17(ddddd); (99,66) case (A) via the B/C joint charts).
- `OPEN[PROP63-RADIUS-S4]` — the `(99,66)` sibling `S4` (`V = (1,8)`) shares
  the descended chart `(27,18)` with case (A) but not its `μ_2`. The number of
  window candidates needing its own C2 replay is `= 6`
  (`4/3, 3/2, 5/3, 2, 7/3, 5/2`); the number replayed in the charged record
  is `<= 2`. Cheap: one screen run on `S4` data.
- `OPEN[PROP63-RADIUS-14-ROWS]` — the gate's "14 excess `≤ 100` rows, all
  `u_s = 1`" is not reproducible from the charged inputs: the unscreened
  `(1)-(13)` census at `n ≤ 100` has `= 24` excess degree pairs, of which
  `= 7` are entirely `u_s = 1`, so `>= 17` contain `u_s ≥ 2` rows. Re-derive
  the 14-row list under its screen and read the flag; cost `<= 1` command.
- `OPEN[SPLIT-KILL-COUPLING]` — the split kills license the complementary
  descent. The number of banked descent kills that would re-open if a split
  kill were withdrawn is `>= 2`. Record the coupling at both banking sites.
- `OPEN[D108-MULTIROW-DESCENT]` — the `(24,16)` descended degree at
  `(108,72)` has `= 17` admissible `u_s = 2` ancestors, of which `= 1`
  descends to the two-level `(24,16;18;7;4)` chart killed in 17(bbbbbb); the
  remaining `= 16` descend to three-level charts and are `>= 16` rows that
  "D = 108 closed at skeleton level" must dispose of by other means.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23334`.
- Body SHA-256:
  `25ad811f497d974946a7a991a5c3c2fa9bda9f9ab4d06a14080d44fdf3fbae69`.
- Frozen basis: `d7ff4ceaaeaa508deec3f1bd7a906a8364fbaba7`.
