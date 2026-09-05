# HOSTILE GATE: census COVERAGE THEOREM (Astra, 17(zzzzzzz))

**VERDICT: CONFIRMED-WITH-FIX.** Every numerical claim reproduces from my own frozen inputs;
the Guccione–Valqui citation is exact; items (2), (7), (10)–(11), (12)–(13) are A-class as
classified; the centre argument and all three operative flags check against printed lines;
Xu Cor. 5.3 is used in the safe direction. No coverage leak was found — **REFUTED is not
returned.** Two load-bearing premises the frozen report *asserts but does not carry* are
supplied below (§1.1, §3.2), and one downstream label changes (§5: the 66-row residual is
**65** under the full conjunction). Promotion may proceed with those three additions.

**Custody, mechanical.** `awk -F=` join of `charged_input_<i>_basename`/`_sha256` from the
receipt under `lane_inputs_dir`, then `sha256sum -c`: **8/8 OK**, no content mismatch. The
five auxiliary operative implementations Astra snapshotted are **byte-identical** to live
repo files (`opus5_probe`, `full_tree_partition`, `xu_screen`, `scope_enum`,
`split_window`), so the aux chain is not a private fork. No ledger, `jc2-lean` or
`ideation-*` file was touched. Moh printed page = PDF ordinal + 139; Moh was read as page
images, GGV/Xu have native text layers.

**Independent replay** (`gate_replay.py`, frozen inputs):

| n ≤ 200 | Astra | gate |
|---|---:|---:|
| core `Kmin=2` | 24,063 | **24,063** |
| core `Kmin=16` | 23,720 | **23,720** |
| `C_FULL_TREE_POLYNOMIAL_ODE` (either `Kmin`) | 1,420 | **1,420** |
| … AND Xu Cor. 5.3 | 1,377 | **1,377** (43 cut) |
| `full_tree_partition` vs `opus5_probe` mismatch | 0 | **0** |
| n ≤ 100: operative / Xu | 20 / 17 | **20 / 17** |

1,400 of the 1,420 have n > 100 and 166 have s = 6, so the content lies almost entirely
outside Moh's printed bounded search — which is what makes the two B clauses decisive.

---

## 1. Re-derivation of the A classification

### 1.1 Item (2), `m ∤ n`: does the degree-reduction automorphism move the row?

The gate's worry is correct in form and does not bite. Restated:

If `m | n`, `n = km`, then `J(f,g) ∈ k^×` kills the degree-`(m+n−2)` part, so
`J(f_m,g_n) = 0`; for binary forms this forces `g_n^m = c f_m^n`, hence `g_n = c′f_m^k` over
`k = k̄`. Put `g′ = g − c′f^k`: `J(f,g′) = J(f,g)`, `k[f,g′] = k[f,g]`, degree sum strictly
drops. So `(f,g′)` is again a non-coordinate Keller pair. **`k=1` is included, so the map
also forces `m ≠ n`** — item (1)'s "cancel equal leading degrees" is the same A necessity,
not an extra C choice.

**The automorphism is therefore never applied.** It is a reductio against minimality: no
second row is produced, and coverage never needs the image pair's row. Astra's cell ("A for
a minimal representative after C") is right.

**Fix F1 — the premise Astra does not carry.** The reductio is valid only if the minimum is
over a class *closed* under `(U,V) ↦ (U, V − cU^k)`, i.e. over **all** non-coordinate Keller
pairs, and only if the preceding C-chain preserves the degree sum. Astra asserts the latter
(line 34) without proof, and the preface `f = T_1^ψ` is the one C op not obviously
degree-preserving. It is: p.185 gives verbatim `T_1^ψ = f + polynomial in g` and
`deg T_1^ψ(f,g) = deg_y T_1^ψ = −M_1 ∉ (n)`; `deg H(g) ∈ nZ` for non-constant `H`, with no
cancellation possible against `deg f = m < n`, so `m = −M_1 < n` forces `deg H(g) = 0`,
i.e. **`H` constant and `deg T_1^ψ = deg f`**.

Hence the preface preserves the degree sum and minimality transfers to the FS presentation.
All other C ops (generic linear source change; output scalings; `(x,y) ↦ (x/c,y)` for
`J=1`; target swap; `(x,y) ↦ (x,y−ax−b)`) preserve `deg f`, `deg g` exactly. **Add F1.**

### 1.2 Item (7): necessity at every level, or only for major successors?

Read off Prop. 5.3 p.180. Its *hypothesis* is "Let `π − C_r` be a factor of `p(π)` … with
multiplicity `V_r` satisfying `deg p(π) = V_{r+1}(d_r/d_{r+1}) ≥ V_r > d_r/(n−M_r)`", and
its *conclusion* ends "Moreover the tower `D_s ⊋ … ⊋ D_r ⊋ D_{r−1}` is a tower of major
discs." So **the strict right-hand inequality is exactly the major-successor selector, not a
universal constraint on discs.** p.200 Theorem(4)/(5) agrees in root counts:
`#{roots of g in E_i} > n/(n−M_r)` ⟺ major, `≤` ⟺ *minor*, and
`v·n/d_r > n/(n−M_r)` ⟺ `v > d_r/(n−M_r) = lo`.

So imposing it at **every recorded level** `i = s,…,2` (code 189–191: `w0 = floor(lo)+1`,
exact `Fraction`, hence strict) is correct: the census row *is* the major tower `V_s,…,V_2`
and nothing else. Imposing it on unselected siblings would over-restrict; the code does
**not** — `coin_options` splits `value > lo` (major, recurse) from `value ≤ lo` (minor,
contributes to `Im`) and keeps both.

**Sharpening.** Astra derives `d_s/2 < V_s` from (7) at `r=s` and cites Lemma 5.3 separately
for `V_s < d_s`. Both are one printed line — Lemma 5.3 p.185: the highest homogeneous form of
`g` has **two roots**, one of multiplicity `(n/d_s)v_s` "where `v_s` satisfies
**`d_s > v_s > d_s/2`**" (repeated in p.200's Cor. 6.1 proof). So the top window has one
source and does not rest on the `V_{s+1} = d_{s+1}` convention, which is inert anyway: at
`i=s` it only yields `hiQ = d_s`, weaker than line 198.

### 1.3 Items (10)–(11): the Puiseux action over the old 1/L lattice

p.201 (`moh-p201-62.png`), verbatim: "Let `(t̄)^{LA_{r−1}} = t`. Due to the existence of the
following automorphism of `k⟪t̄⟫` **over `k⟪t̄^{A_{r−1}}⟫`**: `t̄ → ω t̄`, where `ω` is an
`A_{r−1}`-th root of unity…". Since `t̄^{A_{r−1}} = t^{1/L}`, the fixed field is exactly
`k((t^{1/L}))` — **Astra's "old 1/L lattice" reading is the printed one**, and the field
statement is not decorative.

*Orbit size.* By (8), `A_{r−1}` is the **reduced** denominator of `Lδ_{r−1}`, so
`Lδ_{r−1} = a/A_{r−1}` with `gcd(a,A_{r−1}) = 1` and `t^{δ_{r−1}} = t̄^{a}`. The action
multiplies that coefficient by `ω^{a}`, again a *primitive* `A_{r−1}`-th root of unity, so a
nonzero root has orbit **exactly** `A_{r−1}` and zero is fixed. The claim is automatic from
"reduced" — no extra hypothesis needed. Then `deg p = △A + □` (eq. 9) splits as (nonzero
mass, a multiple of `A`) + (zero multiplicity), giving (10) and (11) as printed.

*Worked examples.* Moh p.202 row `(75,50)`, `M=(55,73)`, `V=(2,4)`, `d=(75,25,5,1)`,
`δ=(2/3,1/5,−1)` — Xu's §6 case with his printed correction `δ_1 = 2/3`:

```
r−1 = 2 :  L = 1,  A_2 = den(1·1/5) = 5,  deg p = V_3 d_2/d_3 = 20 = 4·5 + 0  (△=4, □=0)
           t̄^{LA}=t̄^5=t ;  t̄^{A}=t^{1/1}=t^{1/L}  ;  t^{δ_2}=t̄^1, gcd(1,5)=1 → orbit 5
           (10): V_2 = 2 ≤ △ = 4  ✓   nonzero budget A·V_2 = 10 ≤ △A = 20 ≤ deg p = 20 ✓
bottom  :  L_c = 5,  A_1 = den(5·2/3) = 3,  (n/d_2)V_2 = 6,  (m/d_2)V_2 − 1 = 3
           (12) 3|6 ∧ 3|3 → TRUE ;  (13) 3|4 ∧ 3|5 → FALSE
```

`L = 1` there, so it does not exercise the lattice claim. The first `L > 1` internal level
in the census does: `n=48, m=32, M=(−8,36,46), V=(2,1,3)` has `L = lcm(1,4) = 4`,
`δ_2 = 17/24`, `A_2 = den(4·17/24) = 6`. Then `t̄^{24} = t`, `t̄^{6} = t^{1/4} = t^{1/L}` ✓,
`t^{δ_2} = t̄^{17}` with `gcd(17,6)=1` (orbit exactly 6) ✓, and the *previous* centre term
`t^{δ_3} = t^{1/4} = t̄^{6}` is `A`-divisible, hence **pointwise fixed** by `t̄ → ωt̄` ✓ —
precisely Moh's "over `k⟪t̄^{A_{r−1}}⟫`", and precisely the gap the increment action alone
leaves at `L>1` (§3.1).

*One permissiveness.* Line 196's `(w − sq) % A == 0` admits `j < 0`; Moh's (11) has `j ≥ 0`.
This **adds** rows, so it is safe. Astra states the positivity, not that the code drops it.

### 1.4 Items (12)–(13): does the code retain both?

Yes, and the disjunction is load-bearing, not decorative. Code 205–208:

```python
b12 = (ns*w % A1 == 0) and ((ms_*w - 1) % A1 == 0)   #  A_1 | (n/d_2)V_2 ,  A_1 | (m/d_2)V_2 − 1
b13 = (ms_*w % A1 == 0) and ((ns*w - 1) % A1 == 0)   #  A_1 | (m/d_2)V_2 ,  A_1 | (n/d_2)V_2 − 1
if not (b12 or b13): continue
```

character-for-character p.201 (12)/(13), with `A_1 = den(L_c δ_1)`,
`L_c = lcm{den δ_s,…,den δ_2}` — the LCM does include `δ_2`, as (8) requires. Over the
23,720 core rows:

| bottom condition | rows |
|---|---:|
| (12) only | 7,001 |
| **(13) only** | **6,759** |
| both | 9,960 |

So **6,759 rows exist only because (13) is retained**; discarding it after fixing `m<n`
would delete 28% of the core. Confirmed with a quantified witness, not a code read. A
(13)-only row: `n=48, m=32, M=(24,46), V=(3,5)`, `L_c=7`, `δ_1=9/14`, `A_1=2`.

---

## 2. The Guccione–Valqui citation

Rendered p.2, p.34, p.35; the PDF has a native LaTeX text layer and image and text agree.
All three of the gate's sub-questions are **YES**:

* **Statement.** p.34, last line: "**Corollary 6.6.** *We have* `B ≥ 16`." Proof at the top
  of p.35: `B = gcd(v_{1,1}(P),v_{1,1}(Q)) = (1/m)v_{1,1}(P) ≥ (1/m)v_{1,1}(en_{ρ,σ}(P)) =
  v_{1,1}(A_0) ≥ 16`, closing on Prop. 6.5 (p.34).
* **Quantifier.** p.2 defines `B := ∞` if JC is true, else `min gcd(v_{1,1}(P),v_{1,1}(Q))`
  "**where `(P,Q)` runs on the counterexamples**" — over *all* counterexamples, **not** a
  normalized subclass. Cor. 5.21 (p.29) enters only inside the proof ("if `B < ∞` … then
  *there exists* a Jacobian pair … standard … and minimal, i.e. `gcd = B`"): it picks a
  witness attaining the already-global minimum, so no subclass leaks into the statement.
  The abstract is flat: "`gcd(deg(P),deg(Q)) ≥ 16` **for any counterexample**".
* **Same object.** p.1: `K` of characteristic zero, `L := K[x,y]`, Jacobian pair `[P,Q] ∈ K^×`,
  counterexample = a Jacobian pair that is not an automorphism — a plane Keller non-coordinate
  pair over char 0. `v_{1,1}` is total degree, so `B = gcd(deg P, deg Q)` = the census's
  `K = gcd(n,m)` in the FS presentation.

Astra's careful phrasing survives: `B` being a *minimum over all* counterexamples, `B ≥ 16`
gives `K ≥ 16` for **every** counterexample, so no claim that the minimal-degree-sum pair
also minimizes the gcd is needed. `Kmin=16` is A with auxiliary GGV; the `Kmin=2` relaxation
is a correct safety net, adding 343 core rows and **0** operative rows.

---

## 3. The centre argument and the three operative flags

`C_FULL_TREE_POLYNOMIAL_ODE` = `evaluator(S, polynomial_recenter=True,
ode_nondegenerate=True)`, mirrored by `Tree(gate=False, ode=True, recenter=True,
capacity=False, passport=False)`. Each flag is *restrictive*, so each needs a necessity.
Ablation over the 23,720 core rows, baseline = 1,420:

| variant | rows | vs baseline |
|---|---:|---|
| `gate=F, ode=T, rec=T` (operative) | 1,420 | — |
| `ode` OFF | 1,691 | **+271 / −0** |
| `recenter` OFF | 2,824 | **+1,404 / −0** |
| `gate` ON | 10,606 | **+9,186/−0** |

Every variant is a strict superset — the flags only remove. The full-Galois `gate=False`
step is by far the largest single necessity in the screen (**9,186 rows**), ahead of
`recenter` (1,404) and the ODE (271).

### 3.1 `recenter=True` and `gate=False`: the centre argument

Code: `removable_nonzero = polynomial_recenter and δ_j.denominator == 1 and δ_j <= 0`;
`newdanger = dangerous and (is_zero or removable_nonzero)`; at `j == 2` a still-dangerous
path is rejected. The claim: a path whose every recorded centre coefficient is zero or
removable can be affinely transported to the all-zero-centre configuration that Prop. 5.6
pp.188–190 excludes.

*Condition check.* Mechanically over all 23,720 rows: `δ_s = −1`, `0 ≤ δ_j < 1` for `j < s`,
and the **only** integral `δ_j` with `j < s` anywhere in the census is `δ_j = 0` (never at
`j = 1`) — all three **23,720/23,720**. So the integral centre exponents in the live range
are exactly `{−1, 0}`, the top slope and the constant, which is exactly what p.190's
`(x,y) ↦ (x, y − ax − b)` removes; the `den == 1 ∧ δ ≤ 0` test fires on that set alone.

*Full-Galois step (`gate=False`).* `gate=True` would spare a dangerous path owning a
`free_exponent` (a non-integral lattice point strictly between consecutive radii);
`gate=False` rejects regardless. Astra's argument, re-derived step by step: take the
**first** nonzero non-integral centre term `a t^e`; everything below `e` is then integral,
so in `k((t))`. The packet is Galois-stable over `k((t))` (ultrametrically, if `σ` fixes
`k((t))` then `ord(τ − στ) = e > δ_{i+1}`, so `στ` stays in the packet, and likewise against
every other member), and `στ ≠ τ` because `e ∉ Z`. Prop. 5.3's own definition —
`δ_i = min{ord(τ_a − τ_b)}` over the packet, "the logarithmic radius of `D_i` which is the
minimal disc containing all roots …" — then forces radius `≤ e < δ_i`. Contradiction. It is genuinely
stronger than the increment action `t̄ → ωt̄`, which fixes `k((t^{1/L}))` pointwise and cannot
move an old-lattice exponent (§1.3's `L=4` case): it repairs the `L>1` gap without a cap.
`gate=False` is licensed — and at 9,186 rows it is the step most worth a second reader.

### 3.2 `ode=True` — Fix F2

Code rejects a root multiplicity `v` with `P = Qv`. The derivation is right, and I
reproduced it from the page: from `P·p·q′ − Q·p′·q = c·p`, `c ≠ 0` (Prop. A.3 p.205 rewrites
it `n q p′ = (m q′ − c)p`, `m = deg p`, `n = deg q`), at a `p`-root `a` of multiplicity `v`,
using A.3(1) `q(a) = 0` and A.3(2) `q` squarefree, the coefficient of `(π−a)^v` gives
`(P − Qv)·q′(a) = c ≠ 0`, so `P ≠ Qv`.

**But Astra's citation "Prop. 4.6 / Prop. A.3" is under-specified in exactly the place a
hostile reader will push.** Prop. 4.6 p.170 states its differential equation only under
"*Moreover if `r = 1` then* …". Imposing `P ≠ Qv` at **every** level therefore looks like an
r=1 result promoted to all `r` — and it costs 271 rows. It is not: p.171
(`moh-p171-32.png`) carries the `r ≥ 2` case explicitly —

> `D(v(−μ_r/d_r), v, p(π), T^ψ_{r,σ}(π)) = C* p(π)^{((−μ_r+M_r−n)/d_r)+1}` …
> "**Then the conclusions (2), (3), (4) and (5) follow at once from Propositions A.3 and A.4
> of Appendix 1.**"

so A.3's hypothesis `D(deg p, deg q, p, q) = c·p` holds at all `r ≥ 2`, with
`deg p = v = V_{r+1}d_r/d_{r+1} = P` (Prop. 5.3) and `deg q = v(n−M_r)/d_r =
V_{r+1}(n−M_r)/d_{r+1} = Q` — the code's `P`, `Q` exactly. **Cite p.171, not Prop. 4.6's
`r=1` sentence.** The same page yields A.3(4) at every level ("at least one root of `p(π)`
with multiplicity `> m/n` = `lo`"), independently of p.200 Theorem(7). **Add F2.**

### 3.3 The remaining operative conditions

Checked against p.200's Theorem, read in full: (4) the major/minor threshold `n/(n−M_r)` in
`g`-root counts ⟺ `v > d_r/(n−M_r)`; (6) "the number of subdiscs `E_i` is bounded by
`(n−M_r)·V_{r+1}/d_{r+1}`" `= Q`, the orbit-count cap, agreeing with the `deg q = Q`,
`q` squarefree route; (7) "there must be at least one `E_i` satisfying the requirement in
(4)" — stated for any `r ≥ 2`, so "one factor `v > lo`" is A at every level.
Theorem(3), "the number `M_s` is the largest one `≤ n−2`", is printed verbatim and soundly
replaces the self-contradictory literal item (4) (data "less than `n−2`" while item (2) sets
`M_s = n−2`); Astra's diagnosis stands.

Both B clauses are mechanically absent: no literal `100` in lines 147–215, no cap on
`len(ch)`/`s`. Materiality — the census holds **1,833 height-six rows, all at `n = 192`**
(e.g. `(192,128)`, `M_2..M_6 = (−96,−80,−72,−36,190)`, `V_2..V_6 = (1,24,12,6,3)`), of which
**166 survive the operative screen**; a printed `s ≤ 5` cap would delete them. `any10` is
defined and never called.

---

## 4. Xu Cor. 5.3 as a bound

`row_bound` returns `Im_min = 1 + principal_minor_floor + tree.im_min`,
`IM_max = tree.im_max`, rejecting only on `IM_max < Im_min`. Confirmed p.8:
`Im(f,g) = 1 + Σ_{σ∈P_m}(δ_σ − 1)` and **Cor. 5.3** `IM(f,g) ≥ Im(f,g)`. The screen is
sound for containment iff `IM_max ≥ IM` and `Im_min ≤ Im`; then
`IM_max ≥ IM ≥ Im ≥ Im_min` and **a realized pair can never violate it** — a structural
guarantee, not an empirical one (no realized non-coordinate pair exists to test against;
I record that rather than claim a witness). Each direction:

* **Minor terms.** Xu **Lemma 4.4(ii) p.5**: "If `α` is a minor root, then `δ > 1`" (from
  `λ^f = λ^g = 0`, `ε − 1 ≤ δ − 2`). Every summand `δ_σ − 1` is thus strictly positive, so
  the code's `max(0, ρ_0 − 1)` per packet is a valid *lower* bound, with
  `ρ_0 = δ_j + [d_j/(n−M_j)](1−δ_j)/v` and `δ_σ ≥ ρ_0`. Xu **Cor. 4.5 p.5** supplies that
  these packets *are* minor roots, for Moh Prop. 6.1 minor-disc centres.
* **Principal floor — the gate's question.** `principal_im_floor` returns `V_s/u_s − 1` at
  `u_s = 1` and **`0` at `u_s > 1`**. This is not a permissive taste; it is *forced by the
  hypothesis of the cited proposition*. Moh **Prop. 6.4 p.198**: "Suppose that `g(x,y)` is
  monic in `y` with `deg g = deg_y g = n > 1`, **`δ_s = −1` and `u_s = 1`**. Then the
  logarithmic radius `δ*_{s−1}` of the minor disc `D*_{s−1} ≥ v_s/u_s = v_s`." No `u_s > 1`
  statement is printed, so `0` is the only licensed value, and it is a valid lower bound
  because the term it replaces is `> 0` by Lemma 4.4(ii). **Answer: yes.** (Prop. 6.4's
  other hypothesis `δ_s = −1` holds 23,720/23,720 — §3.1.) The sharper `V_s/u_s − 1` at
  `u_s > 1` is unprinted; Astra rightly holds it back as a diagnostic (48 kills, not 43).
* **Not closed.** I did not independently re-derive Xu Thm 5.1's major-leaf expression
  `(v·m/d_2)·(n/(m+n))·(1−δ_1)` as an upper bound over refinements. Astra states it as a
  bound, not attainment; it is the one link taken on the frozen report's word.

Sensitivity: **18 of the 43 Xu removals depend on the `u_s = 1` principal floor**; 25 do
not. Kill profile by `u_s`: `{1: 34, 2: 7, 3: 1, 4: 1}`.

---

## 5. CROSS: the 66-row residual against the 1,377

All 66 rows of `box/residual66-20260905/roster.jsonl`, keyed on `source`
`(n, m, M_2..M_s, V_2..V_s)`, were looked up in my independently computed 1,420-row
operative set. **66/66 matched; 0 missing.** Of those:

* **65 survive Xu Cor. 5.3** — they lie in the 1,377.
* **1 is removed:**

| row | (n,m) | `M_2..M_s` | `V_2..V_s` | `d_s` | `v_s` | `u_s` | `IM_max` | `Im_min` |
|---|---|---|---|---:|---:|---:|---:|---:|
| **R001** | (84, 56) | 64, 82 | 2, 3 | 4 | 3 | 1 | **4** | **5** |

`Im_min = 1` (global) `+ 2` (principal floor `v_s/u_s − 1`) `+ 2` (tree minor minimum) `= 5`
against `IM_max = 4`. **The kill is entirely floor-dependent**: drop the `u_s = 1` floor and
`Im_min = 3 ≤ 4`, so R001 survives. Its removal stands or falls with Moh Prop. 6.4 p.198 —
printed, and R001 meets both hypotheses (`δ_s = −1`, `u_s = 1`). The removal is licensed.

**Label consequence.** The 17(vvvvvvv) residual is stated against the pre-Xu 1,420; under
the *full* conjunction it is **65**. The residual66 record for R001 is not wrong — it is a
source-side descent/receiver record, `split_window` correctly `NOT_APPLICABLE_U_S_EQ_1` —
but the two lanes must not both be quoted as "the residual" without naming the population.

---

## 6. VERDICT

**COVERAGE THEOREM CONFIRMED-WITH-FIX ⇒ promote with three added sentences.** No normalized
minimal-counterexample datum was exhibited that the enumerator would miss. I probed the four
places a leak could hide — the preface's degree change (§1.1), the ODE's `r=1` scope (§3.2),
the `L>1` increment-action gap (§3.1), the Xu floors (§4) — and each closed against a printed
line.

Required additions before promotion:

1. **F1 (§1.1).** Minimality is over *all* non-coordinate Keller pairs, and the preface
   `f = T_1^ψ` is degree-preserving because `deg T_1^ψ = −M_1 = m < n` forces the `H` of
   `T_1^ψ = f + H(g)` to be constant. Without it item (2)'s "A after C" is asserted, not proved.
2. **F2 (§3.2).** Cite **p.171** ("the conclusions (2),(3),(4),(5) follow at once from
   Propositions A.3 and A.4") for the `r ≥ 2` ODE, not Prop. 4.6's `r = 1` sentence. 271
   operative rows depend on it.
3. **Label (§5).** The 17(vvvvvvv) residual is 66 against 1,420 and **65** against 1,377;
   R001 `(84,56)` is removed, and that removal is `u_s = 1` principal-floor dependent.

Recommended, not required: record §1.3's `j ≥ 0` permissiveness and §1.2's single-line
source for `d_s/2 < V_s < d_s`.

Independently reproduced and unchanged: all five counts, 0 tree-set mismatches, 0 coverage
leaks, both B clauses absent, `Kmin = 16` sound on GGV Cor. 6.6. Out of scope here as there:
larger `Kmin`, an `s ≤ 5` cap, UNI/H2, realization, elimination. Still **containment**.

**FALLACY-v2.** Flag/place/series kept apart: label-zero, old-lattice exponent and physical
packet are separated in §3.1, and the increment action is never identified with full Puiseux
Galois. Floors never imply attainment (§4); rows never imply realization (§5's
`semantic_type` is `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`). Every
normalization in §1.1 names its group element. The one unclosed link (Xu Thm 5.1's major
upper bound) is typed as such, not filled by analogy. No new exit-price assertion is made,
so no `charge_basis` line applies.

**Replay** (repository root):

```text
sha256sum -c /tmp/manifest.sha256                  # 8/8 OK (awk join of the receipt)
python3 box/census-coverage-gate-20260905/gate_replay.py 2    # 24063 / 1420 / 1377
python3 box/census-coverage-gate-20260905/gate_replay.py 16   # 23720 / 1420 / 1377
```

Renders (GGV 2/34/35; Moh 170–171, 179–182, 185–190, 194, 198–201, 205; Xu 5/7/8),
`cross-66-vs-1377.json`, the ablation logs and both replay JSONs are in
`box/census-coverage-gate-20260905/`. No ledger promotion is performed here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22000`.
- Body SHA-256:
  `719d5a5e72e6f9fc2519e2ae15e41834a303c1cc30e1595591f29b5221c8d463`.
- Frozen basis: `bb054cb758bc50404eb664422ffec9b638cfccce`.
