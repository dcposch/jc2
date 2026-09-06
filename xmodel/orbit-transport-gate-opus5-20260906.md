# HOSTILE GATE — orbit transport, `I'_M = u_s I_M` — Opus 5 — 2026-09-06

```text
VERDICT.  CONFIRMED-WITH-FIX.
  The local rule and the identity are correct and re-derived here from the print.
  Moh p.197(3) prints the POSITIVE monomial -(u_s/b)*gamma^{v_s-u_s-1} in the
  STATEMENT; only the p.198 proof display is corrupt (twice), so the "corrected
  Jacobian monomial" is a correction to a proof line, not to the theorem.
  FIX 1: the transportable invariant is the PRODUCT N'*rho' = eps*N*rho, not the
  pair (N'=eps*N, rho'=rho); the pair fails at the eps=delta endpoint, the product
  does not, and inverse_top already computes the product form.
  FIX 2: N is the orbit size of the ACTUAL centre; zero-route levels contribute a
  factor 1.  With Moh's coarse L_i the prerequisite eps*N in Z fails outright.
  REFUTED, and already declined by the producer: the gate's promotion consequence
  "child integrality is not a new condition at u_s=1".  Transport equates VALUES on
  mapped data; the child supplies necessary conditions with no parent counterpart.
  NUMERICS: 46/46 complete u_s=1 rows give ratio exactly u_s=1 and N'rho'=eps*N*rho;
  20 u_s>=2 rows are rule-internal only (no licensed child Def 5.1).
```

## 0. Custody

Manifest built with `awk` from the receipt's numbered `charged_input_<i>_sha256=`/
`_basename=` fields, piped to `sha256sum -c` before any mathematical read: **8/8 OK**
(`box/orbit-transport-gate-20260906/charged-inputs.sha256`); all reads were the frozen
copies in `/tmp/jc2-lane.cgofWX/inputs`. Moh displays were read as **page images**
(`pdftoppm` pp.188, 194, 197, 198); the OCR layer drops every display. Declared
uncharged repo reads: `box/lib/own_v_routes.py` (import dependency of the charged
`descend_own.py`) and `box/lib/__init__.py`; the repo `descend_own.py` is byte-identical
to the charged one (`3fbb5bb8…`). No fleet, ledger edit, `jc2-lean`, or `ideation-*`
input. Writes: this report and `box/orbit-transport-gate-20260906/` (288 KB).
Key: **M** = Moh (journal pages), **X** = Xu; `'` marks the child, never a derivative;
Xu's `f` is the smaller member (`deg_y f = m`), the roster's `g`.

## 1. The print, re-derived (gate item 1)

**The ring map is verbatim M p.197.** Prop 6.3 fixes `y^{-1} = θ`, the π-root
`σ = Σ a_j θ^j + π θ^{v_s/u_s}`, and `γ = θ^{1/u_s}`; eq. (10) on p.198 is `z = y-bx-e`
and `σ` is substituted for `z`. Hence, with `c(γ) := Σ a_j γ^{u_s j}`,

```
   y = gamma^{-u_s},     x = (gamma^{-u_s} - e - c(gamma) - gamma^{v_s} pi)/b,
   x_pi = -gamma^{v_s}/b,   y_gamma = -u_s gamma^{-u_s-1},
   J_{gamma,pi}(x,y) = -x_pi*y_gamma = -(u_s/b) gamma^{v_s-u_s-1}.
```

This **is** the printed conclusion (3), `J_{γ,π}(ḡ(σ),T_1^{ψ}(σ)) = -(u_s/b)γ^{v_s-u_s-1}`,
given the p.198 chain rule `= J_{γ,π}(x,y)·J_{x,y}(g,T_1^ψ)` with the printed normalisation
`J_{x,y}(g,T_1^ψ)=1`. Conclusion (2) prints the π-degrees `u_s n/d_s` and `u_s(-μ_i)/d_s`,
i.e. `(n',m') = (u_s n/d_s, u_s m/d_s)` at `μ_1 = M_1 = -m`. **All confirmed.**

The producer's "printing conflict" is real but should be stated more precisely: the
p.198 display is corrupt **twice**. Its matrix entry for `x_π` is `-1/(bγ^{v_s})`
(reciprocal; the substitution gives `-γ^{v_s}/b`), and its final line
`-u_s/(bγ^{v_s-u_s-1})` is not even the determinant of its own matrix
(that would be `-(u_s/b)γ^{-v_s-u_s-1}`). The **statement** on p.197 is right, so the
producer's `C γ^ℓ` is not a repair of Prop 6.3 but a rejection of one garbled proof
line — and the producer's independent reason is decisive: conclusion (1) puts
`ḡ(σ), T̄_1^ψ(σ)` in `k[γ,π]`, whose Jacobian cannot be `γ^{-ℓ}` for `ℓ>0`.

**Signs and the f/g swap.** `I_M := -Σ_{P_M}|D^f_σ|λ^g_σ` (X:344, verbatim), with
`λ^g<0`, so every term is positive; transport multiplies `λ'_g` by `u/ε>0` and the
root count by `ε`, so no sign can flip. Counting the other member gives
`|D^g|=(n/m)|D^f|`, `λ^f=(m/n)λ^g`; both ratios are descent-invariant because
`n'/m' = n/m`, so the swap commutes with transport. Moh's (3) orders the pair
`(ḡ(σ),T_1^{-ψ}(σ))`, Xu's Lemma 4.1 orders it `(f,g)`; the swap changes only the sign
of the nonzero constant, and only `ord J = ℓ` enters the calculus. **The `u_s` in the
Jacobian constant `-(u_s/b)` is not the `u_s` of the identity** — the identity's factor
comes from `λ' = (u_s/ε)λ` and `N' = εN` and would be unchanged if that constant were 1.
The producer does not conflate them; neither does this gate.

**The radius rule, derived independently.** With `w := π - h(T) = -b T^v x`, `T=γ^{-1}`,
`t=1/x`: a parent centre of order `ε>0` gives `ord_T t = u/ε`; two branches with
`ord_t(α-α̃)=δ` satisfy `ord_t(t̃-t)=δ-ε+1`, hence `ord_t(x̃-x)=δ-ε-1`, hence

```
   ord_T(w~ - w) = v + (u/eps)(delta-eps-1) = (v-u) + (u/eps)(delta-1) = H + (u/eps)(delta-1),
```

`H = ℓ+1 = v_s-u_s`. This is the producer's `δ'`. **Confirmed.** Polynomial values are
unchanged by the substitution, so `λ'_f=(u/ε)λ_f`, `λ'_g=(u/ε)λ_g`. **Confirmed.**

**Completeness of the major transport.** Three printed ingredients, only the first of
which the producer cites explicitly:

1. **M p.194 (8)–(10) (image read).** After Moh's normalisation `a=0`, every root of
   `g` and `T_i^ψ` in the *major* disc `D_{s-1}` has the form `y = 0·t^{-1}+c_j+…`, i.e.
   `ord_t ≥ 0`; the roots at `y = bt^{-1}+e+…` lie in the *minor* disc `D*_{s-1}`.
   **X Def 4.3** (X:217) then declares exactly that group — the smaller multiplicity
   `u_s < v_s` of the leading form `[(y-ax)^{v_s}(y-bx)^{u_s}]^{n/d_s}`, and
   `u_s<v_s ⟺ ℓ≥0` — the **principal minor**. So no major sits at `ε<0`.
2. `ε=0` is impossible: `y→c≠0` with `x→∞` sends the branch to finite `γ_0≠0` with
   `π→∞` while `F` is monic in `π` (Prop 6.3(1),(2)). This is not new prose — it is
   already the charged instrument's `PROP6.3_FINITE_POLE` obstruction
   (`descend_own.py:196-208`), raised on the `δ_{s-1}=0` rows.
3. `ε<δ` for a final major: `ε=δ` means `σ_1 = πt^{δ_1}`, which is precisely the
   hypothesis of **M Prop 5.6 p.188** (image read), excluded in the minimal-counterexample
   setting. Its proof p.189 is explicitly restricted to `δ_s=-1, M_s=n-2, d_s>v_s`,
   i.e. the campaign's reduced source with `u_s≥1`.

Conversely no child major is new: `ord_T G<0` forces `g→∞` with `y=T^u→0`, hence
`x→∞`, so the branch is the image of a parent branch with `ε>0`, major because
`ord_T G = (u/ε)·ord_t g`. **Both directions confirmed.** The producer's second, global
proof (over `γ≠0` the chart is the degree-`u_s` cover `γ^{u_s}=y^{-1}` of `y≠0`) is also
correct and *stronger* than stated: for generic `ξ` the boundary term `B` vanishes
because `f(x,0)=ξ` and `g(x,0)=0` share no solution, so no "generic `g`-translation" is
needed. It needs an actual pair (§2).

## 2. The quantifier (gate item 2)

**Both readings are needed, and neither gives the gate's promotion consequence.**

The *cover* proof is a statement about a realised pair and its image; it cannot be
read on configurations at all. The *local-rule* proof is combinatorial and does apply
to necessary data — but only where the data determine `ε` per packet, and its output is
a *child configuration* only if it happens to satisfy the child's own necessary
constraints. Three facts settle the question:

* `ε` is **not** a function of the coarse configuration. A zero-route sibling
  (the `π^z` factor) has no determined first-nonzero exponent, so transport is a
  **partial** map on necessary configurations. This is exactly where R063's parent
  and child values diverge (§5).
* The child carries constraints with **no parent counterpart**: the finite-line
  packet `r_0 = deg_x f(x,0)` must have non-negative integral multiplicity `z'` in the
  child's level-`j` pattern; the child's own Galois law `ρ' ≡ 0,1 (mod A')` and its own
  thresholds apply. §3 exhibits `D ≥ 0, D ∈ Z` as a live test with no parent analogue.
* Conversely the transported major **value** is the parent's. So a child test at
  `u_s=1` can never kill a mapped configuration *by its value*; whatever kill power it
  has lies in configuration **existence**.

Hence: **"child integrality is not a new condition at `u_s=1`" is REFUTED** as a
promotion consequence. What survives is the weaker and correct pair of statements the
producer's report itself makes: (a) for a realised pair the child's major sum is
`u_s` times the parent's, so a child-integrality kill of *every* enumerated child
configuration remains a valid kill of the row (it says no realised pair exists), and
(b) the theorem never licenses replacing an unverified child's computed value by its
parent's. The producer states (a)'s converse-free form and (b) explicitly; the gate
prompt's parenthetical is stronger than the report it cites.

## 3. Numerics (gate item 3)

Driver `box/orbit-transport-gate-20260906/transport.py`, exact `Fraction`
throughout, results in `row_transport.json` / `finite_line.json`. For every roster row
it runs the charged `descend_own`, rebuilds the parent's selected chain from
`(n,m,M,V)` by Def 5.1 and Moh's Prop 4.6 level parameters, and compares the parent's
final-major term `(n/(n+m))Nρ(1-δ_1)` with the child's `(n'/(n'+m'))N'ρ'((1+ℓ)-δ'_1)`
computed **from the child datum only** (`M'`, `d'`, `V'`, `δ'` as returned by the
instrument), never from the transport rule.

| test | scope | result |
|---|---|---|
| `I'_M(sel)/I_M(sel) = u_s` | 46 complete `u_s=1` rows | **46/46** |
| `N'ρ' = ε N ρ` | 46 complete `u_s=1` rows | **46/46** |
| radius rule `=` child Def 5.1 (instrument assert) | 46 rows | **46/46** |
| child `A'_j = εN`, child `P'_j =` `inverse_top` pattern | 59 rows reachable | **59/59** |
| finite-line remainder `D` a non-negative integer | 54 rows with `z=0` at level `j` | **54/54** |
| `D` fractional | 12 rows with `z>0` at level `j` | **12/12**, all endpoint rows |
| ratio `= u_s` rule-internal only | 20 `u_s≥2` rows | 2,3,4,5 as `u_s` |

Named rows beyond the producer's two controls (`R009`, `R050` reproduce its tables
exactly, including `λ'_g=-2/5` and `-1`):

```
R001 (84,56)  s=3 j=2 eps=2/7  parent 7x4  d1=16/21 I_M=4   child 2x4  d'1=7/6  I'_M=4
R022 (150,100) s=4 j=3 eps=1/5 parent 10x6 d1=3/4   I_M=9   child 2x6  d'1=7/4  I'_M=9
R059 (192,128) s=5 j=4 eps=1/4 parent 8x22 d1=7/12  I_M=44  child 2x22 d'1=1/3  I'_M=44
R061 (200,120) s=3 j=2 eps=1/4 parent 4x21 d1=3/5   I_M=21  child 1x21 d'1=2/5  I'_M=21   (z=2)
R015 (99,66)  s=3 j=2 eps=1/3 u_s=3 ell=4  parent 3x16 d1=4/9 I_M=16 -> rule-only 48 = 3*16
```

`R001`'s `I_M = 4` is **X §6.2(i)**'s printed number, and `R002`'s is **X §6.1(ii)**'s:
a printed-source calibration of the parent side of the ratio.

**FIX 1 (the count rule).** The producer's pair `N'=εN, ρ'=ρ` fails at its own R050
endpoint, where it reports `ρ'=ερ=4` with `N'=N=1`. The invariant that holds in
**both** regimes is the product `N'ρ' = εNρ`, and this is what the identity actually
consumes: `-N'ρ'λ'_g = -(εNρ)(u/ε)λ_g = u(-Nρλ_g)`, and equally
`N'ρ'(H-δ') = εNρ·(u/ε)(1-δ) = uNρ(1-δ)`. The charged `inverse_top` already emits the
product form (`W0 = u_s d_{j+1}/d_s - a·Σr`; on R050 `W0=2`, giving the doubled
endpoint count `4` with no special case). Recommend promoting the product form and
demoting the split to a remark.

**FIX 2 (which `N`).** `N` is the orbit size of the **actual** centre. My first driver
took `N = ∏_{i≥2} A_i` with `A_i = den(L_iδ_i)`; that failed on seven `u_s=1` rows
(`R026 R028 R042 R056 R058 R063 R064`, ratios `1/6 … 1/7`). The correction — a
zero-route level contributes the single `π^z` disc, factor `1`, and only levels with a
nonzero centre coefficient enlarge the denominator lattice — restores `46/46`. This is
exactly the producer's caveat "inserting denominators from earlier zero coefficients
does not increase `N`" and `descend_own.py:151-152`; it is load-bearing, not decorative,
and it is why `εN ∈ Z` (§5).

**`u_s ≥ 2` (the requested prefix).** `descend_own` returns
`top_license=OPEN_CHILD_TERMINAL_IDENTIFICATION` and a retained prefix on all 20 rows,
so there is **no licensed child Def 5.1 radius** and the `u_s≥2` ratio test is
rule-internal, i.e. tautological. Two things can still be said. (i) Applying
`def51_radii` to the retained prefix with multiplier `ℓ+1` reproduces the transport
metric on **20/20** rows — the rule and Def 5.1 agree algebraically at `u_s≥2` too, but
the prefix-terminal reading is the rejected C-TOP convention, so this is consistency,
not confirmation. (ii) The producer's cover argument does give the factor `u_s` at
`u_s≥2` for a realised pair, independently of any child radius. The producer's
"the `u`-cover may split an image into several Galois orbits" predicts child orbit size
`a/gcd(a,u_s)` at `ε=a/b`; on this roster `gcd(a,u_s)=1` on all 20 rows, so the
prediction is untested. `R015`'s and two other rows' transported `δ'_1 = 0` is inside
the shifted major window `δ' < 1+ℓ` and is not an obstruction.

## 4. Prop 5.6 at the child (gate item 4)

**Not printed for the child, and not needed by this theorem.** M Prop 5.6 p.188 is
stated for a tower of major discs of a pair whose Jacobian is a unit, and its p.189
proof opens with "`g(x,y)` and `T_1^ψ(f,g)` have no common polynomial factor. Otherwise
… `J_{x,y}(T_1^ψ,g) ∈ (h(x,y))`. A contradiction." For the child `J = cγ^ℓ`, so
`h | γ^ℓ` is not contradictory and the step fails verbatim; the reductions it invokes
(Prop 5.4, Lemma 5.3) are likewise unit-Jacobian statements. The producer's use is
correct because it is **at the parent**: Prop 5.6 excludes `ε=δ` for the parent's final
majors, which is what confines the endpoint anomaly to *minor* packets — and minors
contribute `0` to both sides of the identity. `descend_own`'s use is also parent-side:
the route loop `range(s-1,1,-1)` never admits a bottom-level first support, the all-zero
branch is explicitly *not* exposed as a child `V` (`descend_own.py:239-241`), and
`reduced_source=False` raises a typed `OPEN` rather than a filled value. Any future
argument that transports Prop 5.6 *to* the child would be unlicensed and must be typed.

## 5. `εN ∈ Z`, and the provenance of R063's `19`

The charged roster settles the input the producer could not obtain: `R063` is
`(168,112)`, `M=[-112,140,160,166]`, `V=[3,21,3]` — **exactly** its reconstruction
(`4·M'_3 = 160`, `V_3=21`, `V_2=V_4=3`). So there is no missing or wrong roster row.

Recomputing from that row: `δ = (3/4, 3/10, 1/5, -1)`; `P_3 = 21 = V_3`, so the whole
level-3 factor is the selected zero part and the route is zero to level 2, `ε=δ_2=3/10`.

* With the **actual** stabilizer (`L_2=1`, `A_2 = den(3/10) = 10`) the level-2 pattern
  is **unique**: `z=12`, orbit `(3)`; `I_M = 9 + 504/59 = 1035/59`. This reproduces the
  producer's number exactly, including its selected-orbit term `9`, which my §3 driver
  transports to the child's `9` (`10×6 → 3×6`, `δ 3/4 → 7/6`).
* With Moh's **coarse** `L_2 = lcm(den δ_3, den δ_4) = 5`, so `A_2 = den(5·3/10) = 2`,
  the row has **509** level-2 configurations — the census count — and exactly one has an
  integral major sum: **`I_M = 19`**, at `z=0`, orbits `(11,3,3,1,1,1,1)`.

So `19` and `1035/59` are the same row under two stabilizer conventions, not a
descriptor error. Transport adjudicates: the coarse configuration's selected packet has
actual orbit size `N = A_2 = 2`, so `εN = 3/5 ∉ Z` — a centre coefficient at exponent
`3/10` cannot live in a degree-2 disc orbit. `εN ∈ Z` is thus a **necessary condition
the coarse enumeration violates on zero routes**, and the actual-stabilizer reading is
the one under which transport holds 46/46. I promote no consequence for R063 or the
residual: the census convention is outside this charge and the exact-contact gate's
`924/1,080` are coarse counts. Raised as OPEN 3/4.

## 6. FALLACY-v2 ledger

*Floor/attainment.* `I_M` is Xu's defined major sum; the identity is between two
defined sums and claims no attainment (`= deg_x Res` only via Thm 5.1/5.1^ℓ). `I_m`
never enters. *Carrier/attainment.* Every row is a necessary configuration; no pair is
asserted, and the cover proof is flagged pair-only. *Flag/place/series.* Roots, discs,
Galois orbits, and the two "infinities" (`γ=0` finite chart vs `T=0` child infinity)
are kept apart in §1. *Prime label/derivative.* `'` is the child generation; the only
derivatives are `d/dt`, `d/dπ`, `x_π`, `y_γ`. *Variable/ring map.* `Φ*`, its generator
order and the `(f,g)`/`(g,T_1^ψ)` orientation are declared, `M_1=-m` re-checked per row.
*Pole/interior.* Major/minor is decided by `sign(λ^g)` after the vertex class; the
principal group comes from M p.194 (8)–(10) plus X Def 4.3, not by analogy.
*Merge-free/M-descent.* Child `M'`,`d'`,`V'`,`δ'` come from `descend_own`, never copied.
*Target/arrival index.* Coarse `A_i` and the actual orbit size `N` are kept distinct —
FIX 2 is the consequence of confusing them. No new exit-price assertion is made, so no
`charge_basis=` line applies.

## 7. Verdict

```text
(1)  LOCAL RULE + IDENTITY: CONFIRMED, re-derived from M pp.194,197,198 (images),
     M Prop 5.6 p.188, X Def 4.3 / Lemma 4.1 / Lemma 4.4 / Thm 5.1.
     Jacobian: p.197(3) already prints -(u_s/b)gamma^{v_s-u_s-1}; the p.198 display
     is corrupt in BOTH its x_pi entry and its final line.  Sign conventions and the
     f/g swap are transport-invariant; the u_s of the constant is NOT the u_s of the
     identity.  FIX 1: promote N'*rho' = eps*N*rho (product), not the split pair.
     FIX 2: N is the ACTUAL centre orbit size (zero-route levels contribute 1).
(2)  QUANTIFIER: the cover proof needs a realised pair; the local-rule proof is a
     PARTIAL map on necessary configurations (eps is undetermined on zero routes) and
     lands in the child's constraint set only contingently.  The gate's consequence
     "child integrality is not a new condition at u_s=1" is REFUTED; the producer's
     own weaker statements stand.
(3)  46/46 complete u_s=1 rows: ratio = u_s and N'rho' = eps*N*rho, exact.
     54/54 z=0 rows: finite-line remainder D a non-negative integer; the 12 z>0 rows
     are exactly the endpoint class.  20 u_s>=2 rows: rule-internal only.
(4)  PROP 5.6 AT THE CHILD: NOT PRINTED (p.189 needs a unit Jacobian).  Not needed:
     the theorem and descend_own use it at the PARENT only.
(5)  PROMOTE: the declared ring map; the p.197 Jacobian monomial C*gamma^ell with the
     p.198 display marked erratum; the strict-sector rule with the product count;
     major-orbit transport I'_M = u_s*I_M on actual reduced licensed images at
     u_s=1, and at u_s>=2 for a realised pair via the cover argument only.
     DO NOT PROMOTE: a packet bijection; transport as a total map on enumerated
     configurations; "child integrality is vacuous at u_s=1"; any R063 verdict here.

OPENS RAISED
  1. Transport is stated only for a first-nonzero centre at a CHARACTERISTIC level;
     descend_own enumerates eps in {delta_i} only.  A first nonzero coefficient at a
     non-characteristic exponent is neither enumerated nor excluded.
     QUANTITY: decide whether a non-characteristic eps can occur on the 66 rows; <= 2 h.
  2. u_s >= 2 has no licensed child Def 5.1 radius, so the factor u_s rests on the
     cover argument (pairs only).  The predicted multi-orbit split a/gcd(a,u_s) is
     untested: gcd(a,u_s) = 1 on all 20 roster rows.
     QUANTITY: supply the Prop 6.3 terminal identification for u_s >= 2; <= 4 h.
  3. Coarse vs actual centre stabilizer.  eps*N in Z FAILS on coarse zero-route
     configurations, and the 1,080/924 census is coarse.
     QUANTITY: re-enumerate the 66 rows with actual stabilizers; <= 3 h.
  4. R063's parent value is 19 (coarse, unique integer of 509) or 1035/59 (actual,
     unique configuration).  The source row is confirmed; only the convention is open.
     QUANTITY: adjudicate OPEN 3 and re-decide R063 at the PARENT level; <= 2 h.
  5. No configuration here is a witness pair.  Unchanged.
```

Replay: `sha256sum -c box/orbit-transport-gate-20260906/charged-inputs.sha256`, then
run `box/orbit-transport-gate-20260906/transport.py`'s `row_transport` over
`T.rows()`; `row_transport.json` and `finite_line.json` hold every exact rational.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20462`.
- Body SHA-256:
  `d4071d60a4682921cb6d9d95e64446cc49761d47fec892936f0a935978f68a37`.
- Frozen basis: `cf5892d088023b651886ea9c16c3fd8d9b50f12c`.
