# Hostile review: ZVK-U6 report (Opus)

**Reviewer.** Grok 4.6, different-model gate, default to refutation.
**Date.** 2026-08-31.
**Charged (frozen, hashes verified).**

- `d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a` `pi1s4-64-zvk-u6-opus5-20260831.md`
- `8529de8ec1b11450a95481ffdf19f6e5116129aeef2ea2c27579b4e4fcc93a74` `pi1s4-64-fold-reduction-opus5-20260831.md`
- `a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8` `pi1s4-64-fixed-tuple-opus5-20260831.md`
- `126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286` `block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`

**Constraint.** Desk-scale exact reasoning only. No CAS. Canonical ledgers and `jc2-lean` not inspected.

## 0. Scope, charge, and method

Frozen-input SHA-256 values were recomputed with `shasum -a 256` before any charged file was read; 4/4 match the boxed manifest. No charged file was edited. Canonical ledgers and `jc2-lean` were not inspected. No CAS and no job of uncertain duration were run. Every number below is a hand expansion, a resultant in two variables, or a finite enumeration in `S_4`.

Default is refutation. “CONFIRMED” means the claim reconstructed on a fresh desk pass, not that the producer’s write-up is the shortest or the first derivation. Consumption typing of the charged report is accepted only as a label: Theorem FOLD’s *statement* is used as a hypothesis of ROW-NF, and is not re-proved here beyond a spot-check of the semigroup reduction `p = r^2 +` (linear in `r,q`).

The eight charged items are treated as independent. A later YES does not repair an earlier gap. No `charge_basis` line is declared: this review asserts no new exit price.

**Headline.** Six of eight items reconstruct. The cross-locus correction stands, the counts `1440` and `96` stand, and `Y_{-5} = -8c^3/81` stands. Two slogans do not: “the fold buys exactly three commutations and nothing else,” and “ZVK-U6 is a strictly weaker instance of FACTORIZATION.” Promotion is recommended for the algebraic core (ROW-NF, the closed form, the `(μ)=(3)`-empty correction, the enumeration, ZVK-RESOLVENT) and refused for the slogans.

## 1. Theorem ROW-NF: derivation of the one-parameter family

**Verdict: CONFIRMED**, with one filled gap in the “three singular pairs ⇒ `δ_aff=3`” sentence. The minus-branch collapse `e_1^3=0 ⇒ c=0` reconstructs. The three witness values reconstruct. The Puiseux route to `(1.2)` is correct but unnecessary: the same `q` is the unique choice that makes the minus-branch numerator a pure fourth power of `e_1`.

### 1.1 Setup, accepted

After Theorem FOLD, `D = \{(r(t)^2,q(t))\}` with `deg r=3`, `deg q=4`. Translating `t` kills the `t^2` coefficient of `r`; translating `y` kills `q_0`; scaling `y` sets `q_4=1`. Residual scaling `t ↦ αt` acts by weights `(2,3,1,2,3)` on `(b,c,q_3,q_2,q_1)`. Write `r = t^3+bt+c` and `q = t^4+q_3 t^3+q_2 t^2+q_1 t`. Set `e_1=t+s`, `e_2=ts`.

Plus branch `r(t)=r(s)`, `t≠s`: `r(t)-r(s)=(t-s)(e_1^2-e_2+b)`, so `e_2=e_1^2+b`. Minus branch: `r(t)+r(s)=e_1^3-3e_1 e_2+b e_1+2c=0`. In both cases `q(t)-q(s)=(t-s)[e_1(e_1^2-2e_2)+q_3(e_1^2-e_2)+q_2 e_1+q_1]`.

### 1.2 Why this `q`: resultant form of `(1.2)`, independent of Puiseux

Imposing that the minus-branch system have no solution with `t≠s` is three conditions on `(q_3,q_2,q_1)`. If `e_1≠0`, the minus equation solves as `e_2=(e_1^2+b)/3+2c/(3e_1)`. Substitute into the `q`-equation and clear the denominator `3e_1`:

```text
-e_1^4 - 2 q_3 e_1^3 + (2b-3q_2) e_1^2 + (q_3 b + 4c - 3q_1) e_1 + 2c q_3 = 0.
```

A degree-4 polynomial always has roots in `C` unless the lower coefficients vanish, leaving `-e_1^4`. The four coefficients besides the leading term are three genuine conditions plus one automatic:

- `e_1^3`: `-2q_3=0` ⇒ `q_3=0`;
- `e_1^2`: `2b-3q_2=0` ⇒ `q_2=2b/3`;
- `e_1^1`: `q_3 b+4c-3q_1=0` and `q_3=0` ⇒ `q_1=4c/3`;
- `e_1^0`: `2c q_3=0`, automatic given `q_3=0`.

That is exactly charged `(1.2)`. Under it the numerator is `-e_1^4`, whose only root is `e_1=0`. At `e_1=0` the minus equation reduces to `2c=0`. Hence `c≠0` implies **no minus-branch pairs**. This is the unique `q` making the residual row condition hold, and uniqueness is visible without Newton–Puiseux.

The `e_1=0` case of the minus system, for general `q`, is `2c=0` together with `q_1-q_3 e_2=0`. It is not an extra family: either `c=0` (excluded below) or it is not a minus pair.

### 1.3 Minus-branch collapse after `(1.2)`, re-derived

With `q_3=0`, `q_2=2b/3`, `q_1=4c/3` the two minus equations are

```text
(A)  e_1^3 - 3 e_1 e_2 + b e_1 + 2c = 0,
(B)  e_1^3 - 2 e_1 e_2 + (2b/3) e_1 + 4c/3 = 0.
```

Subtract: `-e_1 e_2 + (b/3)e_1 + 2c/3 = 0`, so `e_1 e_2 = (b/3)e_1 + 2c/3`. Substitute into `(B)`:

```text
e_1^3 - 2((b/3)e_1 + 2c/3) + (2b/3)e_1 + 4c/3 = e_1^3 = 0.
```

Thus `e_1=0`, hence `2c/3=0`, hence `c=0`. For `c≠0` the minus system is empty (`m=0`). Charged §1.3, second clause, reconstructs.

### 1.4 Plus branch, `t≠s`, and the filled `δ_aff` gap

The same substitution into the plus-branch `q`-equation produces charged `(1.4)`:

```text
h(e_1) := e_1^3 + (4b/3) e_1 - 4c/3 = 0,     e_2 = e_1^2 + b.
```

(The intermediate form is `-e_1^3+(q_2-2b)e_1+(q_1-q_3 b)=0`; inserting `(1.2)` gives `h`.) Three roots. The quadratic `X^2-e_1 X+e_2` has discriminant `-3e_1^2-4b`. This cannot vanish at a root of `h`: `e_1^2=-4b/3` plugged into `h` yields `-4c/3 ≠ 0`. So every plus-pair has `t≠s`, with no extra hypothesis on `j`.

The charged text writes “three roots, i.e. three singular pairs” and stops. That is not yet `δ_aff(D)=3`. Fill: `D'` is a coprime `(4,3)` polynomial curve, so `p_a=3` and `δ_∞(D')=0`, hence `δ_aff(D')=3`. The derivatives never vanish together: `r'=3t^2+b=0` implies `t^2=-b/3`, whence `q'=4t^3+(4b/3)t+4c/3=4c/3≠0`. So every branch of `D'` is smooth. Three singular pairs of two smooth branches on a curve of affine `δ=3` cannot include a tacnode (`δ≥2` plus two further `δ≥1` overshoots `p_a`). Thus `D'` is 3-nodal. The fold `ν:(u,y)↦(u^2,y)` is étale at those nodes (they lie off `u=0` by charged fold Lemma 2.1a, which uses only the nodal class). Image nodes are ordinary. Therefore `D` is 3-nodal and `δ_aff(D)=3`.

An independent numerical path, using fold Lemma 2.3: `m=0` and `Σ μ_τ=3` give `I(D̄',D̄'^-;Q')=16-3=13`, hence `β_1=15`, hence `δ_∞=7`, hence `δ_aff=10-7=3`. Same conclusion; it consumes the fold report’s characteristic-pair lemma rather than the `p_a(D')` argument.

### 1.5 Puiseux coefficients, as a check not a source

The Newton–Puiseux inversion of `r(t)=ζ^3` was re-expanded from `3ζ^2 A+3ζ A^2+A^3+bζ+bA+c=0`. The charged values reconstruct:

```text
a_1=-b/3,  a_2=-c/3,  a_3=0,  a_4=-bc/9,
a_5=-c^2/9+b^3/81,  a_6=0,  a_8=-5c^3/81+5b^3c/243.
```

(`a_7` is nonzero in general and is not needed.) The rewriting `q=ζ^3 t+q_3 ζ^3+β t^2+γ t-q_3 c` with `β:=q_2-b`, `γ:=q_1-c-q_3 b` is an identity from `t^3=ζ^3-bt-c`. The odd part of `Y=q(t(ζ))` has `ζ^3` coefficient `q_3`, `ζ^1` coefficient `a_2+γ`, `ζ^{-1}` coefficient `a_4+γ a_1+2β a_2`. Setting these to zero and using `c≠0` on the last (divide by `c/3`) recovers `(1.2)` a second time. The `ζ^{-3}` coefficient is `a_6+γ a_3+2β(a_4+a_1 a_2)` and vanishes identically because `a_3=a_6=0` and `a_4+a_1 a_2=0`. So `deg_ζ Y_{\mathrm{odd}}≠-3` for every `(b,c,q_i)`, as charged.

Lemma 1.2 (`deg Y_{\mathrm{odd}}=2m-5`) is a resultant-at-infinity count: nine factors `y_i-y'_j`, six off-diagonal of order `ζ^4` with leading `(ω^i-ω^j)ζ^4≠0`, three diagonal of order `deg Y_{\mathrm{odd}}`, divided by `u=ζ^3`; the other side is `deg_u \mathrm{Res}=3+2m`. The leading-coefficient claim is correct. The wording “contradicting `2m-5≥-5`” when `c=0` is garbled (`m≥0` is not a contradiction); the intended fact is that `c=0` forces `Y_{-5}=0` after the earlier conditions, so `deg≤-7` cannot equal `2m-5` for `m∈ℕ`, and the residual degree `-5` is unattainable. With the resultant form of §1.2 this branch is unnecessary: `c=0` makes `e_1=0` a genuine minus solution or makes `D'=D'^-` (if additionally `q` is even).

### 1.6 Three witness values

For `b=c=1`: `r=t^3+t+1`, `q=t^4+(2/3)t^2+(4/3)t`, matching the ROW-SWEEP witness cited in fold §1.1. Reduction `t^3≡-t-1 \pmod{r}` gives `t^4≡-t^2-t`, hence `q≡(-1/3)t^2+(1/3)t=(t-t^2)/3`, matching fold §2.1. Differentiating, `q'=4t^3+(4b/3)t+4c/3 ≡ -(8/3)(bt+c)\pmod{r}`, hence `-(8/3)(t+1)` at the witness, matching fold §2.2. All three checks are identities, not numerics.

### 1.7 Modulus

Scaling acts with weights `(2,3)` on `(b,c)`, so `j=b^3/c^2` is the residual invariant, and `c≠0` makes the `(b,c)`-space a `G_m`-bundle over `𝔸^1`. “Irreducible one-parameter family” is correct as a moduli statement. It is not “one target-isomorphism class”: `j` is not killed by triangular `Aut(𝔸^2)`. The integration report’s phrasing is the one that should be corrected; the charged ZVK-U6 correction on this point is right.

**Promotion of Theorem ROW-NF: yes**, at the statement in charged §1.3, with the `δ_aff` gap filled as in §1.4 of this review and with `(1.2)` permitted to cite either the resultant or the Puiseux route.

## 2. Closed-form β₁ and the claimed identity Y_{-5} = -8c³/81

**Verdict: CONFIRMED** for the identity `Y_{-5}=-8c^3/81`. **CONFIRMED as a re-derivation, not as a first proof**, for `β_1=15`.

After `(1.2)` one has `γ=c/3` and `β=-b/3`. The coefficient of `ζ^{-5}` in `Y_{\mathrm{odd}}` is

```text
Y_{-5} = a_8 + γ a_5 + 2β(a_6 + a_1 a_4 + a_2 a_3).
```

(The odd part of `t^2` is `2 t_{\mathrm{odd}} t_{\mathrm{even}}`; there is no further contribution at this weight.) Substitute the coefficients of §1.5, using `a_3=a_6=0`:

```text
a_8 = -5c^3/81 + 5 b^3 c/243,
γ a_5 = (c/3)(-c^2/9 + b^3/81) = -c^3/27 + b^3 c/243,
2β a_1 a_4 = 2(-b/3)(b^2 c/27) = -2 b^3 c/81.
```

Cubic terms: `-5/81 - 1/27 = -5/81-3/81=-8/81`. The `b^3 c` terms: `5/243+1/243-2/81=6/243-6/243=0`. Hence `Y_{-5}=-8c^3/81`. For `c≠0` this is nonzero, so `deg_ζ Y_{\mathrm{odd}}=-5` exactly, and Lemma 1.2 with `m=0` gives `deg_u \mathrm{Res}=3`, matching the affine intersection forced by `Σμ=deg r=3`. Bézout on two quartics then gives `I(Q')=13`. Fold Lemma 2.3 converts this into `β_1=15`.

The same number is already in the fold report, by a shorter path that does not use the explicit `q`: fold Lemma 2.1b (row condition ⇒ no minus pairs) plus `Σμ=3` plus Bézout plus Lemma 2.3. What is new here is the uniform closed form and the fact that `c≠0` is forced by the row rather than assumed. The comparison to the witness coefficient `c_{13}=-8/27` is structural (`≠0`), not numerical: the two series live in different charts (`U=u/y` versus `ζ` with `r(t)=ζ^3`).

Per FALLACY-v2 (floor/attainment, raw remainder degree): the identity is an exact leading-odd-term computation after vanished leaders `ζ^3,ζ,ζ^{-1},ζ^{-3}` have been imposed, and the `c=0` branch is handled. No omitted term can cancel `-8c^3/81` at this weight.

**Promotion of the closed form: yes. Promotion of “`β_1=15` proved here” as a priority claim: no** — record it as an independent check of fold §2.3.

## 3. Cross-locus correction versus the fold report

**Verdict: the charged ZVK-U6 report is right; fold §2.2 is wrong to carry `(μ)=(3)` as a live sub-case of the residual row.** The identification `(μ)=(2,1) ⇔ j=-27/4` is confirmed. Both reports agree that `(1,1,1)` is the open stratum.

Fold §2.2 lists three sub-cases of the cross-locus `D'∩D'^-`, indexed by the root pattern of `r`: `(1,1,1)`, `(2,1)`, `(3)`. That is the correct list of *cubic* root patterns. It is not the correct list for the *row*. The row condition forces `c≠0` (§1.3). A perfect cube, after the translation that kills the `t^2` term, is `r=t^3`, hence `b=c=0`, contradicting `c≠0`. So `(μ)=(3)` is empty on `Δ=(6,4,3)`.

If one nevertheless sets `b=c=0` and tries to stay in type `(4,3)`, the minus system becomes `e_1(e_1^2-3e_2)=0`. The branch `e_1=0` is `s=-t`, and `q(t)=q(-t)` has solutions unless the odd part of `q` vanishes identically; if it does, `D'=D'^-` and the intersection is a curve, not a finite scheme. In all cases `δ_aff(D)>3` or the union is degenerate. The residual class never sees `(μ)=(3)`. Fold §2.2’s excuse — “a double root of `r` is consistent with the nodal class of `D`” — applies to `(2,1)`, not to a triple root.

The pattern `(2,1)` is the vanishing of `disc(r)=-4b^3-27c^2`, i.e. `j=-27/4`. At that modulus `r` and `r'` share a root `τ`, so a vertical tangency of `D'` collides with the cross-locus and the union has an `A_3` plus a node over `u=0`. This is a genuine (non-generic) member of the row: `h` has discriminant `-256b^3/27-48c^2`, vanishing at `j=-81/16≠-27/4`, so the three plus-pairs of `D` remain distinct. Fold §2.2 was right to keep `(2,1)` and wrong only in not pinning the modulus.

The further exclusion `j≠-81/16` (`disc h=0`) is the collision of two nodes of `D`, not a cross-locus phenomenon. The charged open stratum `j∉\{-27/4,-81/16\}` is the right set for equisingularity of `U_6` and for the nodal class of `D` simultaneously. The family over that stratum is connected, so row-level `π_1` statements are licensed; witness-level `j=1` is interior (`disc r=-31≠0`).

**Binding correction.** Future work that consumes fold §2.2 must drop `(μ)=(3)` for the residual row. The charged “`(3)` EMPTY; `(2,1)` iff `j=-27/4`” is the replacement statement.

**Promotion of the correction: yes.**

## 4. Strand count and discriminant census

**Verdict: CONFIRMED** for 6 strands, for `V=5=3+2` with three vertical tangencies simultaneous at `x=0`, and for the relation `|Σ_u|=2|Σ_x|-1`. **CONFIRMED on a slightly thinner open set** for the census `|Σ_x|=6`, `|Σ_u|=11`.

### 4.1 Six strands

`deg_y g=3` for each component, so a vertical line `u=c` meets `U_6` in `3+3=6` points. Equivalently the vertical pencil is based at `Q'=[0:1:0]`, each quartic passes through `Q'` smoothly (`a=deg q-deg r=1`), and `8-1-1=6`. A generic pencil would see degree 8 and would destroy the pullback of §5. Both derivations are elementary. Fold §4.3(b) already used 6 strands; there is no conflict.

### 4.2 Split of `V` and the two discriminant sets

`p=r^2` gives `p'=2r r'`, degree 5, matching the promoted `V=d-1=5`. The five roots split as: three roots of `r`, all with the same critical value `x=0`; two roots of `r'=3t^2+b`, with critical values `x=r(t_j)^2`. Off `j=-27/4` one has `gcd(r,r')=1`, so the latter values are nonzero. This split is not in FIXED-TUPLE, which treated five tangency fibres as distinct, and it is the source of the fibre-count correction in charged §4.4 / §7.

Nodes of `D` sit at `x=u_i^2` with `u_i=r(t)` along the three plus-pairs `(1.4)`. Thus

```text
Σ_x = {0} ∪ {r(t_1)^2, r(t_2)^2} ∪ {u_1^2, u_2^2, u_3^2}.
```

The map `π:u↦u^2` satisfies `Σ_u=π^{-1}(Σ_x)` because `ν` identifies the fibre configurations for `c≠0`. Since `0∈Σ_x`, one has `|Σ_u|=2|Σ_x|-1` whenever the five nonzero elements of `Σ_x` are distinct.

They are distinct off a finite set of `j`. The two excluded moduli already in charged §1.5 kill `r(t_j)^2=0` and a node collision. In addition: `r(t_1)^2=r(t_2)^2` would require `c=0` or `b=0` with `t_1=0` (the two critical parameters are opposites, and `r(t)^2-r(-t)^2=4t(t^2+b)c` with `t^2=-b/3` is `8bt c/3≠0` for `b,c≠0`); `u_i^2=0` is fold Lemma 2.1a. Remaining collisions are node-versus-tangency equalities `u_i=±r(t_j)`, algebraic in `(b,c)` and not identities (the fold witness has 11 distinct upstairs values, fold §4.3(b)). So `|Σ_x|=6` and `|Σ_u|=11` hold on a Zariski-open of the `j`-line containing `j=1`, possibly properly smaller than `ℂ∖\{-27/4,-81/16\}`. Charged §2.2 already conditions on “the five nonzero values distinct”; the open-stratum sentence in §1.5 should cite that same proviso when it claims 11 values at row level.

### 4.3 Local types, exponent sums, cable

- Four simple vertical tangencies of `U_6` at `u=±r(t_j)`: `r'(t_j)=0` implies `q'(t_j)=4c/3≠0`, so each is a genuine simple branch point, local braid a half-twist. Two downstairs values times two sheets.
- Six self-nodes at `u=±u_i`, local braid `σ^2`.
- Fibre `u=0`: three pairs `q(τ_i)±(q'/r')u+O(u^2)`, single-valued, three distinct `y`-levels. Circling `u=0` once circles `x=u^2` twice, so the local braid is `β_0^2`, three disjoint full twists. Downstairs, `β_0` is three disjoint half-twists.

Exponent sum upstairs: `4·1+6·2+3·2=22`. Independently, `Disc_y(G_U)=Disc(g)\,Disc(g^-)\,Res(g,g^-)^2` has `u`-degree `8+8+2·3=22`, using `deg Disc_y(g)=2·3·(4/3)=8` from `y_i∼ω^i u^{4/3}` and `deg Res=3` from Lemma 1.2 with `m=0`. Downstairs: `e(ρ_∞^D)=3+2+6=11`, matching FIXED-TUPLE four ways. The identity `e(ρ_∞^U)=2\,e(ρ_∞^D)` is the double winding of `x=u^2`.

The cable description from `Y(η)-Y(-η)∼Y_{-5} η^{-5}` and `η↦e^{iπ/3}η` as `x` circles once reconstructs `Σ k_i=-5` and `e=16-5=11`. The upstairs slogan `ρ_∞^U=(ρ_∞^D)^2` is the same double winding; the further claim that this equals the 2-cable of `(σ_1σ_2)^4` with `-10` internal half-twists is an exponent-sum check (`32-10=22`) and not a commutation relation in `B_6`. It is not used later.

### 4.4 Correction to FIXED-TUPLE §6.3(b)

FIXED-TUPLE stratified the quadruple cover by eight special fibres (5 tangencies + 3 nodes) and obtained `χ_c(Y)=(-2)(1-8)+5(-1)+3(-2)=3`. The correct downstairs count is six special fibres, with the three `r=0` tangencies stacked at `x=0`:

```text
generic χ_c=-2 over χ(C_x∖Σ_x)=-5;
node fibre χ_c=-2 (a_p=0), ×3;
simple-tangency fibre χ_c=-1, ×2;
x=0 fibre: 3 points of D, each a smooth vertical tangency, χ_c=4(1-3)+3·3=+1.
Total: 10-6-2+1=3.
```

Totals agree; the route is the one that must be carried. The `x=0` formula uses the geometry of `D`, not the upstairs commutations.

**Promotion of the split `V=3+2` and of `|Σ_u|=2|Σ_x|-1`: yes**, with the distinctness proviso. **Promotion of “11 values for every row member off two moduli”: no**, without the extra collision check.

## 5. Theorem ZVK-PULLBACK: index-2 and “exactly three commutations”

**Verdict: CONFIRMED** for the pullback identity `bm_U=bm_D∘π_*` and for `B_D=⟨B_U,β_0⟩` with `[B_D:B_U]≤2`. **REFUSED** as stated for the slogan “the fold buys exactly three commutations in place of three identifications, and nothing else.”

### 5.1 The cover and the image subgroup

`0∈Σ_x`, so `π:C_u∖Σ_u→C_x∖Σ_x`, `u↦u^2`, is an unbranched connected double cover. The fibre configurations of `U_6` at `u=c≠0` are the `y`-coordinates of `D` at `x=c^2` (`ν` is the identity on `y`). Monodromy of a pulled-back configuration family is the pullback of the monodromy. That is Theorem ZVK-PULLBACK.

`π_1(C_x∖Σ_x)` is free of rank `|Σ_x|=6`. The homomorphism to `ℤ/2` is winding number about `x=0` mod 2. Its kernel has Schreier rank `2(6-1)+1=11`, generated by `γ_0^2`, `γ_k`, and `γ_0 γ_k γ_0^{-1}` for `k=1,…,5`. These are geometrically the loops about the 11 points of `Σ_u`. Zariski–van Kampen depends only on the image of braid monodromy, so

```text
G = F_6 / ⟨⟨ β_0·T=T,  β_k·T=T ⟩⟩,
Γ = F_6 / ⟨⟨ β_0^2·T=T, β_k·T=T, β_0 β_k β_0^{-1}·T=T ⟩⟩,
```

and `B_U=bm_D(\ker)⊆B_D=⟨B_U,β_0⟩`. Index is 2 iff `β_0∉B_U`. The charged summary correctly writes `≤2`; the slogan in §6 item 5 that treats the index as a structural 2 is slightly looser than §3.1.

`β_0` is three disjoint half-twists pairing each `D'`-strand with a `D'^-`-strand (local expansion `y≈q(τ_i)±(q'/r')√x`). In a basis adapted to those three clusters, `β_0=σ_1σ_3σ_5`, downstairs identifications `g_1=g_2`, `g_3=g_4`, `g_5=g_6`, upstairs commutations `[g_1,g_2]=[g_3,g_4]=[g_5,g_6]=1`. That local comparison is correct, and it is the content of `(D0)` versus `(U0)`. The second derivation of `(D0)` via `ν_*(μ_1)=ν_*(μ_2)` at a cross-point (ball minus a smooth disc) agrees.

### 5.2 What the slogan drops

Fixing `T` by `B_U` is not the same as taking the downstairs presentation and replacing three identifications by three commutations.

1. Upstairs the conjugate factors `β_0 β_k β_0^{-1}` are independent relations. They become automatic only when `β_0·T=T`. For a non-descending tuple (some pair complementary rather than equal) they are extra equations, not free consequences of “three commutations.” The charged Reduction Theorem in §5.1 is the precise statement and does not need the slogan: `{G\text{-admissible}}=\{Γ\text{-admissible with the three pairs equal}\}`.
2. “Nothing else” is false as a description of the two presentations: `Γ` has the conjugate relations and does *not* have `β_0·T=T`. The fold therefore both relaxes three relations and adjoins five conjugate relations. Net, `B_U` is a subgroup of index at most 2, not a modification of `B_D` at a single local braid.
3. The four upstairs identification relations (two tangencies and their `β_0`-mirrors) forming two spanning trees, one per component, reconstruct from the `S_6`-images and match fold §4.3(b). That is a correct re-derivation, independent of the slogan.

The trap in charged §3.5 — `β_0` is not the tube-diagonal of the cable — is a legitimate GAP. For `r=t^3+1` the roots of `r` are not closed under `t↦-t`, so the `x=0` matching (same `τ_i`) is not the `∞`-matching (`η↔-η`). Path-dependence of the transport is exactly a Hurwitz-move datum. The argument is geometric and not fully expanded (one path, one member), but it is enough to forbid writing `β_0=σ_1σ_3σ_5` in the FIXED-TUPLE cable basis. The charged report consumes this nowhere, correctly.

**Promotion of Theorem ZVK-PULLBACK (the identity `bm_U=bm_D∘π_*`, the Schreier generators, the Reduction Theorem): yes. Promotion of the slogan as a theorem: no.**

## 6. Enumeration counts 1440 and 96

**Verdict: CONFIRMED**, by an independent partition of the `(E0)`-set. The counts are of tuples satisfying only `(E0)+(E3)` and `(E0')+(E3)`; they are not a count of homomorphisms.

Two transpositions in `S_4` commute iff they are equal or complementary. There are 6 transpositions and 3 perfect matchings of `K_4`. Each of the three `β_0`-pairs is one of 12 options (6 equal, 6 complementary), so `12^3=1728` tuples satisfy `(E0)`. A set of transpositions generates `S_4` iff the associated graph on 4 vertices is connected. Let `k` be the number of complementary pairs.

- **`k=3`.** `6^3=216` ordered complementary triples. Disconnected iff all three matchings coincide: `3·2^3=24`. Connected: `192`. (Two distinct matchings already give a 4-cycle.)
- **`k=2`.** Three choices for which pair is equal. Complementary-with-distinct-matchings: `6×4=24`, times 6 for the equal pair gives 144 connected (a 4-cycle plus an edge). Complementary-with-equal-matchings: `6×2=12`, times 4 edges outside that matching gives 48 connected; the 2 edges inside the matching disconnect. Per position `192`, total `576`. Raw `(E0)` count `3×6×36=648`, of which `3×24=72` disconnect.
- **`k=1`.** Three positions. Complementary 6, two equal `6×6=36`. Disconnects iff both equal transpositions lie in the matching (`2×2=4` pairs). Per position `6·(36-4)=192`, total `576`.
- **`k=0`.** Ordered triples of transpositions, i.e. `(E0')`. Cayley: `K_4` has `4^{2}=16` spanning trees, each with 3 distinct edges, `3!=6` orders: `96`. Raw `6^3=216`, so 120 disconnect (a triangle on 3 of 4 vertices, a matching, a star of one edge, etc.).

Sum of connected classes: `192+576+576+96=1440`. Complement `1728-1440=288=24+72+72+120` closes. The `k=0` line is exactly `(E0')+(E3)`, so `96`. Ratio `1440/96=15`.

The enumeration is exhaustive: every `(E0)` tuple has a unique `k`, and each class is counted by listing matchings and edges of `K_4`. No orbit-stabiliser is required; the charged “16 trees × 3!” is the Cayley count, not an orbit count of a group action on tuples.

**What the counts are not.** They ignore `(E1)`–`(E2')`. The charged claim that no subset of those equations constrains `T` until the conjugating words are known is correct *equationwise* (all transpositions are conjugate in `S_4`), and the words are not in any charged input. Jointly the words are words in the `g_i`, hence in the `t_i`, so the system is not “1440 independent of braids”; it is 1440 candidates. Calling 15 “the full quantitative content of what the fold buys” is a slogan about this floor, not about the solved system. Per FALLACY-v2 (floor/attainment, carrier/attainment): 1440 and 96 are floors on a residual, never attainment, and the charged report says so in §7.

The 96 downstairs tuples are in the `β_0`-adapted indexing. They are not the 72 cable-fixed tuples of FIXED-TUPLE §7. Comparing the two numbers without `GAP[BETA0-TUBE-POSITION]` is a type error; the charged report does not make that comparison, and this review does not either.

**Promotion of Enumeration E1 (1440 / 96): yes**, as a count of `(E0)+(E3)` / `(E0')+(E3)` tuples.

## 7. Theorem ZVK-RESOLVENT

**Verdict: CONFIRMED.** The two corollaries are correctly scoped.

`S_4` has a unique normal Klein four-group `V`, and `S_4/V≅S_3`. A transposition in `S_4` acts on the three nontrivial elements of `V` as a transposition, so meridians that are transpositions remain transpositions in the quotient. Surjectivity of `⟨t_1,…,t_6⟩=S_4` passes to the quotient.

`S_3` contains no pair of disjoint transpositions (its three transpositions are the edges of a triangle). Therefore `(E0)` forces `\bar t_1=\bar t_2`, `\bar t_3=\bar t_4`, `\bar t_5=\bar t_6`: the reduced tuple satisfies `(E0')` and is fixed by `β_0`. Hurwitz action commutes with post-composition by a homomorphism, so the reduced tuple is fixed by `B_U` and hence by `B_D=⟨B_U,β_0⟩`. It therefore defines `G=F_6/N_D→S_3` with transposition meridians.

The argument uses only `(E0)` and the subgroup relation of §5.1. It does not use conjugating words, `a_p=0`, row numerics, or the enumeration. That is the advertised independence of braid data, and it holds.

**Corollary (i).** A negative answer to `OPEN[PI1S4-(6,4)-TRIPLE-COVER]` — no simply-branched `S_3`-cover of `C^2` with branch curve `D` — kills both `G↠S_4` and `Γ↠S_4` with transposition meridians. The charged caveat on writing a triple cover as a monic `z^3+az+b` over `A^2` (freeness of bundles does not make the leading coefficient a unit) is a caveat on one attack, not on the implication.

**Corollary (ii).** Every `Γ↠S_4` with transposition meridians either has all three `β_0`-pairs equal, in which case it is `G`-admissible by the Reduction Theorem, or has some complementary pair, in which case it is invisible as an `S_4`-representation of `G` but still yields `G↠S_3`. There is no third commuting type in `S_4`. Correct.

A minor wording point: the theorem as stated produces a homomorphism from `G`, not a geometric triple cover; the translation “simply-branched `S_3`-cover with branch curve `D`” additionally needs the meridians of all components of the branch locus to be transpositions and the cover to be connected, both of which are in the hypotheses. No gap.

**Promotion of Theorem ZVK-RESOLVENT: yes.**

## 8. Retirement logic: OPEN into FACTORIZATION

**Verdict: ACCEPT the allocation, REFUSE the slogan “strictly weaker instance.”** The lane `OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]` should not be maintained as an independent desk-scale kill. It is not strictly weaker than `OPEN[PI1S4-(6,4)-FACTORIZATION]`.

### 8.1 What is true

`B_U⊆B_D` with the difference localised at `β_0`. The conjugating words of `β_1,…,β_5` are the same geometric paths downstairs and upstairs (upstairs they appear twice, once conjugated by `β_0`). No charged input supplies those words; charged §3.4 correctly explains why `π_1(C^2-D')=Z` does not (the 6-point fibre inserts `D'^-` letters). The one natural guess that would have supplied them is the cable identification of `β_0`, and charged §3.5 refutes it. Therefore a completed ZvK on `U_6` is not cheaper than a completed factorization of `D`, and the right computational object is the explicit family of Theorem ROW-NF. As campaign routing, retirement of the *decision item* FOLD-ZVK-U6 into FACTORIZATION is correct.

The charged verdict OPEN (neither KILLED nor EXISTS) is also correct: 1440 and 96 are unfiltered by `(E1)`–`(E2')`.

### 8.2 Why “strictly weaker” is the wrong comparison

1. **Kill-power runs the other way.** A complete NO on the upstairs system (`Γ`-admissible set empty after `(E1)`–`(E2')`) kills `Γ↠S_4` *and* `G↠S_4`, because `G`-admissible tuples are a subset. A downstairs-only NO leaves possible non-descending `Γ↠S_4`. Upstairs-NO is the stronger kill, obtained from a weaker constraint system on a larger finite set. “Weaker instance” mixes those two orders.
2. **The two named OPENs are not the same problem.** FIXED-TUPLE’s FACTORIZATION asks whether `ρ_∞` factors in `Stab(T)` for the 72 cable-fixed tuples of shape (O4). ZVK-U6’s downstairs 96 are `(E0')+(E3)` tuples in the `β_0`-basis. Without `GAP[BETA0-TUBE-POSITION]` these are incommensurable finite sets. Computing the actual braid monodromy of `D` (the strong reading of FACTORIZATION, charged ZVK-U6 §7) does decide both; the 72-tuple search as specified in FIXED-TUPLE §9 does not automatically decide the 1440.
3. **A parallel cheaper-if-NO route exists.** Theorem ZVK-RESOLVENT raises `OPEN[PI1S4-(6,4)-TRIPLE-COVER]` to a braid-free kill of *both* questions. Retiring FOLD-ZVK-U6 into FACTORIZATION must not bury that successor. The charged §7 already keeps it; the §6 sentence “the union route cannot be cheaper than the direct route and can only be weaker” is then false of the TRIPLE-COVER branch.

### 8.3 Corrected retirement statement

Replace the charged verdict sentence with: *The decision item `OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]` is not independently cheaper than computing the braid monodromy factorization of a ROW-NF member, and should be read off that computation (96 tuples downstairs, 1440 upstairs). A separate braid-free kill remains `OPEN[PI1S4-(6,4)-TRIPLE-COVER]`, now implied by ZVK-RESOLVENT. Lemmas proved in the ZVK-U6 lane are not retired.*

The last clause is load-bearing. ROW-NF, the closed form, the `(μ)=(3)` correction, the `V=3+2` split, the Reduction Theorem, Enumeration E1, and ZVK-RESOLVENT are not instances of FACTORIZATION and must survive as statements.

**Promotion of the retirement as campaign routing: yes, with the wording repair above. Promotion of “strictly weaker”: no.**

## 9. FALLACY-v2 and campaign-safety flags

The charged report is unusually clean against FALLACY-v2. The remaining flags are on slogans, not on hidden exits.

- **Carrier / attainment.** No homomorphism `π_1(C^2-D)↠S_4` is asserted. The 1440 / 96 counts are labelled floors. The Euler check is labelled a cost-raiser. Compliant.
- **Floor / attainment.** `e(ρ_∞)=11` is obtained four ways (factor count, genus split, winding, Seifert) and the upstairs 22 two ways; equality is not a one-sided bound. The identity `Y_{-5}=-8c^3/81` is an exact coefficient, not a floor. The slogan “ratio 15 is the full quantitative content of what the fold buys” *is* a floor dressed as exactness of the solved system; refused in §6.
- **Raw remainder degree.** The Puiseux odd part is expanded in the chart `r(t)=ζ^3`; vanished leaders `ζ^3,ζ,ζ^{-1}` are imposed; the identically vanished `ζ^{-3}` is identified; the `c=0` branch is handled (and, independently, excluded by the resultant form). Compliant.
- **Variable / ring map.** The fold `ν(u,y)=(u^2,y)`, the residual scaling weights, and the identification of fibres by `ν` are declared. Matching names are not used as proofs. Compliant.
- **Pole / interior.** Puiseux at `Q'` / `Q_D` is used after the place is identified (`a=1` upstairs, unibranch of multiplicity 2 downstairs). Fold Lemma 2.3 is consumed by name for `β_1=I(Q')+2`. Compliant for the closed-form check; the first proof of `β_1=15` remains the fold report’s.
- **Prime label / derivative.** `r'`, `q'` are derivatives of polynomials in `t`. No ambiguous prime marks.
- **Target / arrival index.** Triangular `Aut(A^2)` is distinguished from source reparametrisation; `j` is correctly not claimed to be a target invariant. The integration report’s “one target-isomorphism class” is the statement that fails this test; ZVK-U6 corrects it.
- **Flag / place / series, per-ray charge, `sat()` wrapping, merge-free / M-descent.** Not in play. No computer algebra, no exit-price assertion, no `V_{2,a}` step.

The GAP `BETA0-TUBE-POSITION` is the right typed OPEN: no analogy (`β_0=σ_1σ_3σ_5` in the cable basis) is used to close it. The conjugating-word gap is likewise returned typed rather than filled.

No `charge_basis` line is applicable (no new exit-price assertion; no consumption of a promoted exit price in a way that would require one).

## 10. Verdicts by item and promotion recommendation

| # | Charge | Verdict |
|--:|---|---|
| 1 | Theorem ROW-NF: the family `r=t^3+bt+c`, `q=t^4+(2b/3)t^2+(4c/3)t`, `c≠0`, modulus `j=b^3/c^2`; `δ_aff=3` by `e_1^3=0` | **CONFIRMED.** `(1.2)` re-derived by a minus-branch resultant (unique `q` making the numerator `-e_1^4`). Collapse `e_1^3=0⇒c=0` reconstructs. Three witness values reconstruct. Gap “3 pairs ⇒ `δ_aff=3`” filled: `D'` has `p_a=3` and no cusp, so the pairs are ordinary nodes and `ν` is étale there. |
| 2 | `Y_{-5}=-8c^3/81` and closed-form `β_1=15` | **CONFIRMED** for the identity. **CONFIRMED as a check** for `β_1=15` (first proof remains fold Bézout + Lemma 2.3). |
| 3 | Cross-locus: `(3)` EMPTY; `(2,1)` iff `j=-27/4` | **ZVK-U6 right, fold §2.2 wrong** to carry `(μ)=(3)` on the row. `(2,1)` pinned at `j=-27/4` is correct. |
| 4 | 6 strands; 11 values; `\|Σ_u\|=2\|Σ_x\|-1`; `V=5=3+2` with three simultaneous at `x=0` | **CONFIRMED** for 6 strands, the split, and the double-cover relation. **CONFIRMED on a thinner open set** for the census 6 / 11 (node–tangency collisions are finite extra `j`). FIXED-TUPLE’s 8-fibre stratification is a genuine route correction; totals agree at `χ_c=3`. |
| 5 | ZVK-PULLBACK, index 2, “exactly three commutations” | **CONFIRMED** for `bm_U=bm_D∘π_*`, Schreier rank 11, `[B_D:B_U]≤2`, Reduction Theorem. **REFUSED** for the slogan: upstairs also adjoins the five `β_0`-conjugate relations, automatic only on descending tuples. |
| 6 | Enumeration 1440 and 96 | **CONFIRMED** by an independent `k`-partition and Cayley (`16×3!=96`). Floors, not homomorphisms. Not comparable to FIXED-TUPLE’s 72. |
| 7 | Theorem ZVK-RESOLVENT | **CONFIRMED**, including both corollaries. Independent of braid words. |
| 8 | Retire OPEN into FACTORIZATION as a strictly weaker instance | **ACCEPT the allocation, REFUSE the slogan.** Same deciding data as a full factorization of a ROW-NF member; upstairs-NO is the *stronger* kill; TRIPLE-COVER is a parallel cheaper-if-NO; the 72-search as named in FIXED-TUPLE §9 is not automatically the 1440. Lemmas of this lane are not retired. |

**Promote (row-level, independent of PROVISIONAL witness numerics).**

- Theorem ROW-NF, with the `δ_aff` gap filled as in §1.4.
- The identity `Y_{-5}=-8c^3/81` (and, as a check, `deg Y_{\mathrm{odd}}=-5` for every row member).
- The correction: `(μ)=(3)` is empty on the row; `(μ)=(2,1)` iff `j=-27/4`.
- The split `V=3+2` and the relation `|Σ_u|=2|Σ_x|-1` under distinctness of the five nonzero values.
- Theorem ZVK-PULLBACK as the identity `bm_U=bm_D∘π_*`, together with the Reduction Theorem of charged §5.1.
- Enumeration E1: 1440 tuples for `(E0)+(E3)`, 96 for `(E0')+(E3)`.
- Theorem ZVK-RESOLVENT.

**Do not promote.**

- “The fold buys exactly three commutations and nothing else.”
- “ZVK-U6 is a strictly weaker instance of FACTORIZATION.”
- Unconditional `|Σ_x|=6` / `|Σ_u|=11` off only the two moduli `-27/4` and `-81/16`.
- `β_1=15` as a new theorem of this lane (already fold §2.3).
- Any attainment, existence of `π_1↠S_4`, or Keller claim. None is made, and none is licensed.

**Binding on consumers.** Drop fold §2.2’s live sub-case `(μ)=(3)`. Carry six downstairs discriminant values, not eight, in any reuse of FIXED-TUPLE §6.3(b). Treat the residual as a one-parameter family `j=b^3/c^2`, one topological class off the two moduli, not one target-isomorphism class. Do not put `β_0=σ_1σ_3σ_5` in the cable basis. Route the decision through FACTORIZATION on a ROW-NF member (read 96 and 1440 off the same words) and through TRIPLE-COVER as a braid-free kill.

**Lane status.** The algebraic core of the charged report survives a different-model hostile pass. The two slogans do not. The decision item remains OPEN, correctly, and should be closed only by factorization or by a triple-cover NO. This is not a Keller counterexample and not a proof that the residual dies.

<!-- BODY-END -->


