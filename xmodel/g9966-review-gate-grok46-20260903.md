# Hostile gate: three DERIVED-SOURCE facts of the `(99,66)` source review

Lane `g9966-review-gate-grok46-20260903`.  Charged:
`g9966-source-review-opus5-20260903.md` §1–§5, §7 (N1–N15).  FALLACY-v2.
No ledger, `jc2-lean`, `ideation-*`, or in-progress lane reports were edited.

## Verdict first

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/g9966-review-gate-grok46-20260903.run.v2`, checked with `sha256sum -c`.
All nine frozen inputs `OK`.  No digest was retyped.
Manifest: `box/g9966revgate-20260903/inputs.sha256`.

| fact | charged claim | verdict | scope |
|---|---|---|---|
| (1) Prop 6.1 order identity | `ord g(σ)=(n/d_s)(u_s δ−v_s)=9(3δ−8)`, ceiling `δ<8/3` | **CONFIRMED** | identity and five Xu orders; ceiling is derived, not a printed Prop 6.1 line |
| (2) split-order classification | `δ∈{2,5/2}`, `[2,1]`/`(25,14)` forced at 2, Galois `[1,1,1]`/`p=π(π²−c)` at `5/2` | **CONFIRMED** | as a *split* classification; `den(δ)≤3` is SOURCE-ASSERTED; survives by Galois |
| (3) tree-blind identity + Im/IM | difference 30; `Im=6,7`; `IM=16`; Cor 5.3 passes | **CONFIRMED** for (4.3) vs Thm 3.4 principal and for Im/IM; **GAP[IDENTIFICATION]** of that identity with 4.7(i) | 4.7(i) extra is `(|D|−1)(δ−1)`, not tree-blind; inequality still does not kill |

Decider consequence: the branch-B face point `p=π²(π+3a)`, `q=π^{25}(π+3a)^{14}(π−2a)` and the `δ=5/2` cubic `p=π(π²−c)` are **not slices** of the face ODE after Galois.  Dropping Galois would reopen the ODE-admissible `[2,1]` vectors at `δ=5/2`.

`(99,66)` remains `OPEN`.  Nothing here is a Keller witness.  No exit-price assertion.

## 0. Pages opened

Printed Moh page `p` is PDF page `p−139`.  Xu printed page `p` is PDF page `p`.
`pdftoppm -png -r 200` from the frozen PDFs, named under
`box/g9966revgate-20260903/pages/`:

```text
moh_p190_pdf51.png .. moh_p196_pdf57.png   Prop 6.1, dichotomy, Prop 6.2
moh_p202_pdf63.png                         table (n,m,M,V,δ)=(99,66,77,97,8,8,1/3,4/9)
xu_p10_pdf10.png .. xu_p13_pdf13.png       §7.3, Prop 7.3, Cor 7.5, §8
xu_support_p-04.png .. -09.png             Thm 3.4, (4.3)/(4.4), Thm 4.7, Cor 5.3
```

Supporting Xu pp.4–9 are in the charged PDF and in the charged
`xu9966-read-gpt55` SOURCE-READ; they were re-opened because fact (3) cites them.

## 1. Fact (1): the order identity

`SOURCE-READ`, Moh p.190.  After a major tower `D_s ⊇ ⋯ ⊇ D_r`, a factor
`(π−C_r)` of the Prop 4.6 polynomial `p(π)` of multiplicity `V_r` is **major**
if `V_r > d_r/(n−M_r)` and **minor** if `d_r/(n−M_r) ≥ V_r ≥ 1`.  At `(99,66)`
the threshold is `d_3/(n−M_3)=11/2`.  Table `V_3=8` is major; the complementary
factor `u_s=d_s−v_s=3` is minor.  Prop 6.1 applied to the principal packet must
use `V_r=u_s=3`, not the p.202 major `V_3=8`.

`SOURCE-READ`, Moh p.191, for the unique `π`-root `σ*` in `D*_{r−1}`:

```text
ord g(σ*) = n δ_s + Σ_{i=r+1}^s V_i (n/d_i)(δ_{i−1}−δ_i) + V_r (n/d_r)(δ*_{r−1}−δ_r)
          = n/(n−M_r) (−1+δ_r) + V_r (n/d_r)(δ*_{r−1}−δ_r).
```

At `r=s=3` the sum is empty, `δ_s=−1`, `n−M_3=2`, `V_r=3`, `n/d_s=9`.
P.193 eq. (3) is the same formula with `δ*` replaced by the order `δ` of a
general such `π`-root:

```text
ord g(σ) = n [ 1/(n−M_r)(−1+δ_r) + (V_r/d_r)(δ−δ_r) ] = −99 + 27(δ+1) = 9(3δ−8).
```

Four exact forms agree on a grid of `δ` (driver): the p.191 truncation, p.193
eq. (3), the closed form `(n/d_s)(u_s δ−v_s)`, and the contact count
`72·(−1)+27·δ` (72 major `g`-roots at contact `−1`, 27 principal at contact `δ`).
Specialisations:

```text
δ=1   : −45     = Prop 6.2 p.195 display (u_s−v_s)n/d_s
δ=2   : −18     = Moh p.209 printed t^{-18}
δ=5/2 : −9/2
```

Using the *major* `V_r=8` at `δ=2` yields `117`, which contradicts the printed
`t^{-18}`.  The minor reading is forced by the source, not a convention.

Xu §8's five orders follow from the same skeleton (Cor 7.5 exponents; `p'=d/dπ`):

```text
f: 6(−8+3δ),  g: 9(−8+3δ),  T_2: 5(−8+3δ),
(T_3)_f: 22(−8+3δ)   with 22=(−μ_3+n−2)/d_s,
T_3: 13(−8+3δ)−1+δ   with 13=(−μ_3−2)/d_s,  deg q=13·3+1=40.
```

Both `δ=2` and `δ=5/2` match Xu p.13 exactly, including `T_3(5/2)=−5`.

**Hypotheses of the general formula.**  `g` monic in `y`, `deg_y=n>1`; `r=s≥2`
with major disc `D_s` of radius `δ_s=−1`; `(π−c_s)` a Prop 4.6 factor of
multiplicity `V_r=u_s` satisfying the p.190 minor test; `σ` a `π`-root of
`g ∏_{i<s} T_i^ψ` with `ord(σ−τ)>δ_s`; two points at infinity,
`[(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}`, `a≠b` (p.194).  The contact-count form
uses only the last of these plus `ord(σ_{\mathrm{minor}},σ_{\mathrm{major}})=−1`.

**Ceiling.**  Prop 6.1(1) *prints* only `δ<1 ⇒ ord g<0`.  The identity gives
the sharp sign `ord g<0 ⇔ δ<v_s/u_s=8/3`.  Prop 6.1(2) is `ord g<0 ⇒`
distribution detector; its `δ≥1` half (Prop 4.2, p.193) covers the window
`1≤δ<8/3`.  So `δ<8/3` is the detector ceiling.  It is the same number as
`Im_{\min}` and as Prop 6.3's unproved premise, but those are different objects
(split order of a principal `π`-root vs combined `δ*` vs a final-root floor).
`FALLACY-v2 / flag-place-series`: not identified.

Verdict (1): **CONFIRMED**.  N3 stands.

## 2. Fact (2): exhaustive split-order classification

Window: `1<δ<8/3` (Xu Prop 7.3, proof exhibited pp.10–11; ceiling of §1).
Integers: only `δ=2` lies in the window; `δ=1` is Prop 7.3 (no split);
`δ≥3` has `ord g≥9>0`.  `δ=8/3` has `ord g=0`, ODE degenerates (`b=0`).

Xu p.13 asserts `den(δ)≤u_s=3` as a tool.  **No proof is exhibited** in
§7.3, Prop 7.3, Cor 7.5, or §8.  N5 is correctly `SOURCE-ASSERTED`.

The missing reason: a `π`-root of order `δ=p/e` in lowest terms is ramified of
index `e` over `k((t))`.  Galois `τ↦ζ_e τ` (`t=τ^e`) acts by `π↦ζ_e^{p} π`
with `gcd(p,e)=1`, so nonzero orbits have size `e`.  A cubic split cannot host
an orbit of size `e>3` except all-at-`0` (not a split).  Thus `den(δ)∈{1,2,3}`
for any split of `deg p=u_s=3`.  The classification **survives without Xu's
assertion**.

ODE-only (no Galois, no den bound) is *not* exhaustive: the driver finds
further ODE-admissible split rows in `(1,8/3)` with `den≤30`
(`9/4,13/5,17/7,…`).  All have `den>3` and are Galois-killed.  `9/4=(v_s+1)/(u_s+1)`
is the Cor 7.5 threshold (strict inequality); Galois `e=4` kills it.

Face ODE, from Xu (7.1) with the §8 leading terms.  Exponents match for every
`δ`.  Monic leading coefficients give `c=27a−40b=45`, `δ`-independent:

```text
9 a q p' − b q' p = 45 p^{14},   a=ord T_3=40δ−105,  b=ord g=27δ−72,
deg p=3, deg q=40,   p'=d/dπ, q'=d/dπ.
```

At a root of `p` of multiplicity `mm` with `ord_q=r`, either `r=13mm+1`
(non-resonant: LHS order `=14 mm`) or `9a mm=b r`, i.e. `r=ρ mm` with
`ρ=5(8δ−21)/(3δ−8)`.  Budget `Σ r ≤ 40`.  Non-resonant totals: `[1,1,1]→42`,
`[2,1]→41`, both over budget at every `δ`.

| `δ` | `ρ` | split survivors |
|---|---|---|
| `4/3,3/2,5/3,7/3` | non-integral | none (`[3]` with `r=40` is unsplit, not charged) |
| `2` | `25/2` | only `[2,1]` vector `(25,14)` (sum 39) |
| `5/2` | `10` | `[1,1,1]`: `(10,10,10)` and mixed `10/14`; `[2,1]`: `(20,10),(20,14),(27,10)` |

**`δ=2`, `(25,14)` forced — by what?**  Not by Xu's generic `q=p^{13}(π−c)`
(that is the all-simple iterate, already over budget / Cor 7.5).  By the local
order analysis: `[1,1,1]` has `ρ` non-integral and non-resonant `42>40`;
`[2,1]` non-resonant `41>40`; the only feasible pair is resonant `r(2)=25` plus
non-resonant `r(1)=14`.  Leftover degree 1 is one extra linear factor.  Solving
`p=π²(π−s)`, `q=π^{25}(π−s)^{14}(π−w)` in the ODE yields the unique relation
`w=−2s/3`.  The charged family is the gauge `s=−3a`, `w=2a`.  Residual `0`.
Xu (8.2) holds identically (driver); it exhibits the family, it does not prove
uniqueness — the budget plus the extra-root solve do.  Gauge `π↦λπ` eats `a`.
Face = a point.  **Not a slice.**

Cor 7.5 (proof exhibited p.12) independently kills `[1,1,1]` at `δ=2`
(`2<9/4`).

**`δ=5/2`, `μ_2`.**  The place is `σ=⋯+π t^{5/2}`.  Clearing `s²=t` gives a
term `π s^5`; Galois `s↦−s` of `k((s))/k((t))` sends `π↦−π`.  Unique
`μ_2`-stable cubic split: `{0,γ,−γ}`, i.e. `p=π(π²−c)`, `c≠0`.  A `[2,1]`
multiset of distinct roots would need both the double and the simple fixed at
`0`: impossible.  This excludes the ODE-admissible `[2,1]` vectors.  Xu p.13
writes “possible `p=π(π²−c)`” as a suggestion, not as this Galois argument;
the forcing is `DERIVED-SOURCE`.

Xu's reduced form `q=p^{10} q_1`, `q_1' = −2 p^3` (constant `e_0` invisible to
the reduced Jacobian) is the full `[1,1,1]` face.  With `e_0=0`, Xu's printed
integral vanishes at `π=0` and takes the value `c^5/20` at `±√c`, so the
multiplicity vector is `(14,10,10)`, not `(10,10,10)`.  Generic `e_0` gives
`(10,10,10)`; one even choice of `e_0` zeros both `±√c` and gives `(10,14,14)`.
All three Galois-allowed vectors live in **one** family.  After `π↦λπ`
(`c↦c/λ²`) the face is 1-parameter (`e_0`), as the review states.  Residual `0`
at `k=10`.  **Not a slice** of Galois-allowed cubics.

Verdict (2): **CONFIRMED**, with N5 typed `SOURCE-ASSERTED` and supplied with
the Galois proof Xu does not print.  N6, N8, N9 stand.  Partition `[3]`
(linear-power, Moh's first p.209 alternative) is unsplit and outside this
classification.

## 3. Fact (3): (4.3) vs Theorem 3.4, Im, IM

`SOURCE-READ`, Xu p.4 Thm 3.4 (no Jacobian):
`I(f_ξ,f_y)=−Σ_σ (e(f_σ)−1) λ_σ` over splitting `π`-roots of `f_ξ`.
On the principal side only the split order contributes (finals have `λ=0`):
`−(k−1)·(m/d_s)(u_s δ−v_s)=(k−1)·6·(8−3δ)`.

`SOURCE-READ`, Xu p.6 eq. (4.3) is an **equality**:
`I(f_ξ, f_y g)=deg_y f + Σ_{P_m} |D_σ^{f_ξ}|(δ_σ−1)`.

Thm 4.7(i) is an **inequality**, from (4.4) and `ord g_y(β)≥−δ_σ`, with extra
term `Σ (|D_σ|−1)(δ_σ−1)`.  These are not the same quantity.

Trees (two derivations of the finals agree: `ord g=0` and Xu's
`δ_σ=48−Σ` contacts):

| tree | `Σ |D|(δ−1)` | Thm 3.4 principal | difference | 4.7(i) extra | Im |
|---|---:|---:|---:|---:|---:|
| `δ=2`, `[2,1]` | 42 | 12 | **30** | 37 | 6 |
| `δ=5/2`, `[1,1,1]` | 36 | 6 | **30** | 30 | 7 |
| `δ=2`, `[1,1,1]` (dead) | 54 | 24 | **30** | 45 | 10 |

Closed form, any `k`-way split of the 18 principal `f`-roots at order `δ`,
using `n_i δ_i=48−δ(18−n_i)`:

```text
Σ n_i(δ_i−1) = 48k − 18δ(k−1) − 18,
Thm 3.4 principal = (k−1)(48−18δ),
difference = 30   for every k and every δ.
```

`30=(v_s−u_s)m/d_s=48−18`.  **CONFIRMED** as an identity of (4.3)'s extra term
against the principal Thm 3.4 summand.

**GAP[IDENTIFICATION].**  The review's prose treats this as “Theorem 4.7(i) at
equality”.  4.7(i)'s extra is `(|D|−1)(δ−1)`; its difference from Thm 3.4
principal is `25 / 24 / 21`, not constant.  Scope: this does **not** revive a
separating constraint.  4.7(i) remains an inequality whose slack is (4.4);
Cor 5.3 is the equality-adjacent test and it passes (next paragraph).
`SATURATED-EMPTY[THM-34-EQUALITY-SEPARATION]` still holds for the charged
comparison.

`Im=1+Σ_{P_m}(δ_σ−1)`: branch B finals `(3,4)` give `1+2+3=6`; `δ=5/2` finals
`(3,3,3)` give `1+6=7`.  `IM` from Xu Thm 5.1 on the printed major tower,
single final major place at `δ_1=4/9` over 48 major `f`-roots:
`λ^g=−1/3`, `IM=−48·(−1/3)=16`, matching `n/(m+n)·48·(1−4/9)=16`.
Cor 5.3: `16≥6`, `16≥7`.  **CONFIRMED** under that major-tower reading.
`FALLACY-v2 / floor-attainment`: `IM=16` is used only to make N12 pass, never
as a kill.  If the major tree split into several finals of different order,
`IM` could move; that is outside this desk (`OPEN` on the p.202 major tree,
already so in the charged review).

Verdict (3): identity and Im/IM **CONFIRMED**; 4.7(i) labelling **GAP** of
identification, not of the numbers.  N12, N13 stand with that scope.

## 4. N-list (charged §7) against this gate

N1, N2, N4, N7, N14: `PRINTED`, re-read, not in dispute.
N3: **CONFIRMED** (§1).
N5: **SOURCE-ASSERTED**; classification survives by Galois (§2).
N6, N8, N9: **CONFIRMED** as split-face facts (§2).  N8 “forced” = ODE budget
+ extra-root uniqueness, not `q=p^{13}(π−c)`.
N10, N11: tree finals `(3,4)` / `(3,3,3)` clear `8/3`; not re-litigated as a
new source fact.
N12: **CONFIRMED** (`16≥6,7`).
N13: **CONFIRMED** as (4.3) vs Thm 3.4 principal; not as 4.7(i).
N15: `OPEN` for `u_s=3`, untouched.

## 5. FALLACY-v2

Flag/place/series: major radii `(4/9,1/3,−1)`, split order `δ`, and combined
`δ*` are not identified; the shared value `8/3` is derived in §1 for `δ` only.
Carrier/attainment: face solutions are `REPRESENTATIVE[FACE-ODE]`, not
`FULL_ACTUAL_EXIT`.  Floor/attainment: `IM=16` is not used as equality in a
kill.  `sat()`: none.  Prime mark: `p',q'` are `d/dπ`.  Variable/ring map:
`(y,z)` is Moh p.194 (10) with `b≠0`; `π`-gauge of §2 is stated with its
action on `a` and `c`.  Raw remainder degree: the `deg q=40` budget keeps both
resonant and non-resonant branches and the leftover degree.  No new
exit-price assertion, so no `charge_basis` line.

## 6. Reproduction

```text
python3 box/g9966revgate-20260903/g9966revgate_driver.py \
  > box/g9966revgate-20260903/results.json
```

Python 3, SymPy 1.12; under 5 s; no Singular.  Artifacts:
`box/g9966revgate-20260903/{g9966revgate_driver.py,results.json,inputs.sha256,artifacts.sha256,pages/}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13748`.
- Body SHA-256:
  `0d989e7bf6d6e076b97e379c54a59bfa711721993b0efd0f4d9ddf72fa052e4d`.
- Frozen basis: `ce9d48de4ef44a6dcc6061a51dfe5c8068e15683`.
