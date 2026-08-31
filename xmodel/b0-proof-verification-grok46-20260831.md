# B0 proof verification (countermodel / computation arm)

- Lane: independent of the line-by-line gate
- Date: 2026-08-31
- Reviewer: grok-4.6
- Scope: exact arithmetic, explicit configurations, group-theoretic enumerations
- Inputs (frozen, hashed):
  - `b0-trivial-dicritical-proof-opus5-20260831.md`
    SHA-256 `b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55` — MATCH
  - `block-descent-a1-mprime-coordinator-integration-fable5-20260831.md`
    SHA-256 `69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9` — MATCH

## 0. Hash check and reading plan

Both frozen inputs match the charged SHA-256 values. Primary PDFs in `refs/` were rehashed before any formula was used; all five agree with the B0 report §0 table (see §8). No CAS. All arithmetic below is integer or Laurent-monomial, by hand.

Standing rearrangement used throughout §1. Promoted (E) `1 = N(1-χ_c(D))+χ_c(F^{-1}(D))` with `χ_c(D)=(2-c)-ν`, `χ_c(D_0)=(2-c)-ν-s`, covering `χ_c(F^{-1}(D_0))=a·χ_c(D_0)`, and `χ_c(F^{-1}(D))=a·χ_c(D_0)+Σ_p a_p`, yields exactly

```text
(N-a)(2-c) - (N-a)·ν + a·s  =  N-1 + Σ_p a_p .     (3.2)
```

Under `c≥1` and `ν≥s` this implies

```text
(a-1) + (N-2a)·s + Σ_p a_p  ≤  0 .                 (3.3)
```

If also `2a≤N` and `a≥1`, every summand of (3.3) is `≥0`, so `a=1`, `s=0`, `Σ a_p=0`, and feeding back into (3.2) forces `c=1`, `ν=0`.

## 1. Lemma 3.4 / (3.2): five non-Keller control configurations

Five integer tuples `(N,a,c,ν,s,Σa_p)` of the author's design. Geometric side-constraints used as filters only: `N≥3`, `1≤a≤N-1`, `c≥1`, `ν,s,a_p∈Z_{≥0}`. No Keller map is asserted to realize them.

**C1. Hypothesis (i) met (D smooth).** `N=4`, `a=1`, `c=1`, `ν=0`, `s=0`, `Σ=0`.
LHS `(4-1)(2-1)=3`, RHS `4-1=3`. Identity holds. The only integer solution of `(N-a)(2-c)=N-1` with `c≥1` is `c=1`, `a=1`: already `c=2` gives `0=N-1`, and `c≥3` makes LHS negative. Forces `a=1` and `D≅A^1` as claimed.

**C2. Hypothesis (ii) met (Orevkov N=3 shape).** `N=3`, `a=1`, `c=1`, `ν=0`, `s=0`, `Σ=0`; here `2a=2≤3` and `ν≥s`.
LHS `(3-1)(1)=2`, RHS `2`. Identity holds. (3.3) is `0+1·0+0=0`, and the back-substitution `c+ν=1` with `c≥1`, `ν≥0` forces `c=1`, `ν=0`. Matches the report's sanity gate (i) at `jc86.pdf` p. 10.

**C3. Hypothesis (ii) as a filter, but `s>0`.** `N=4`, `a=1`, `c=1`, `ν=1`, `s=1`, `Σ=0` (`2a=2≤4`, `ν=s`).
LHS `(4-1)(1)-(4-1)·1+1·1=1`, RHS `3`. Identity fails. Equivalently (3.3) reads `0+(4-2)·1+0=2≰0`. There is no integer point in the (ii)-region with `s>0`. The identity refuses exactly the data Lemma 3.4 claims to kill.

**C4. Drop `corr_l=0`, keep `2a≤N`: the N=4 survivor `(μ,corr)=(2,1)`.** Take `N=4`, `a=2`, `c=1`, `ν=0`, `s=1`, `Σ=1` (one unibranch non-immersive point, so `ν=0<s`).
LHS `(4-2)(1)+2·1=4`, RHS `3+1=4`. Identity holds. (3.3) reads `(2-1)+(4-4)·1+1=2≰0`, so there is no forcing. This is the report's sanity gate (ii): the profile satisfies neither (i) nor (ii) of Lemma 3.4, and (3.2) admits it.

**C5. Drop `2a≤N`, keep `ν≥s`.** `N=5`, `a=3`, `c=1`, `ν=2`, `s=2`, `Σ=0` (`2a=6>5`).
LHS `(5-3)(1)-(5-3)·2+3·2=2-4+6=4`, RHS `4`. Identity holds. (3.3) reads `(3-1)+(5-6)·2=0≤0`, but the middle term is negative, so `a=1` is not forced. Dropping `2a≤N` admits solutions exactly as the T3.5-SHARPEN residual says.

Bonus on the N=5 H2 survivors (drop `corr_l=0` only). Profile `(2,0)+(1,1)` with `s_1=s_0=1` gives `a+2+1=5`, so `a=2`. Tuple `N=5`, `a=2`, `c=1`, `ν=0`, `s=1`, `Σ=1`:
LHS `(5-2)(1)+2·1=5`, RHS `4+1=5`. Holds, and `2a=4≤5` so only the missing `ν≥s` saves it. The one-correction relaxation quoted in OPEN[B0-GENERAL-N],

```text
2a - N - 1 + (N-2a)s + Σ a_p  ≤  0,
```

evaluates to `4-5-1+(5-4)·1+1=0`, satisfiable, as claimed.

**Verdict.** HOLDS. Identity (3.2) is the advertised rearrangement of (E); it forces `a=1`, `D≅A^1` on every integer point of (i) or (ii); dropping `corr_l=0` realises the N=4 `(2,1)` and N=5 `(2,0)+(1,1)` survivors; dropping `2a≤N` realises a genuine extra solution.

## 2. N=4 profile table completeness; N=5 surviving profiles

Budget `[O-4.2]`: `Σ_ℓ (μ_ℓ+corr_ℓ)=N-1`, each `μ≥1`, `corr≥0`, hence each summand `μ+corr≥1`.

**N=4, sum=3.** Let `k=#` dicriticals. Then `1≤k≤3`.

- `k=1`: `μ+corr=3` gives `(3,0)`, `(2,1)`, `(1,2)`.
- `k=2`: the only composition of 3 into two parts `≥1` is `1+2`. The part 1 is `(1,0)` only; the part 2 is `(2,0)` or `(1,1)`. Multisets: `(2,0)+(1,0)` and `(1,1)+(1,0)`.
- `k=3`: only `(1,0)+(1,0)+(1,0)`.

These are exactly the six rows of the §4.1 table. No `(0,3)` (`μ≥1` forbids it), no `k=4` (min sum `4>3`). **Table complete.**

**N=5, sum=4, under the report's own exclusions, with a trivial dicritical.** All multisets:

| k | profiles |
|---|---|
| 1 | `(4,0)`, `(3,1)`, `(2,2)`, `(1,3)` |
| 2 | `(3,0)+(1,0)`, `(2,1)+(1,0)`, `(1,2)+(1,0)`, `(2,0)+(2,0)`, `(2,0)+(1,1)`, `(1,1)+(1,1)` |
| 3 | `(2,0)+(1,0)+(1,0)`, `(1,1)+(1,0)+(1,0)` |
| 4 | `(1,0)^4` |

Exclusions used by the report, under H2: Cor. 3.8 kills `μ=N-1=4`, i.e. `(4,0)`; Lemma 3.1 kills every all-`μ=1` row (`Br=∅`), i.e. `(1,3)`, `(1,2)+(1,0)`, `(1,1)+(1,1)`, `(1,1)+(1,0)+(1,0)`, `(1,0)^4`; Cor. 3.7 kills every all-`corr=0` row (equivalently `Σ μ=N-1`), i.e. `(3,0)+(1,0)`, `(2,0)+(2,0)`, `(2,0)+(1,0)+(1,0)`. Rows with no `μ=1` are not "carrying a trivial dicritical". The two remaining profiles that both carry a `μ=1` dicritical and survive the exclusions are exactly `(2,0)+(1,1)` and `(2,1)+(1,0)`.

**Verdict.** HOLDS.

## 3. Theorem 4.3(5): aggregate identity on concrete shapes

Stand on the report's own ingredients: (E) in aggregate form

```text
Σ_i (4-a_i) χ_i  =  3 - 4s + Σ_p a_p ,     (†)
```

with `χ_i=χ_c(D̃_i)-n_i`, `a_1=2`, `a_0=4-s_0` so `4-a_1=2` and `4-a_0=s_0`, `χ_c(D̃_1)=2-r_1`, `χ_c(D̃_0)=2-c_0`, `n_1=Σ β_p`, `n_2=Σ k_p`, and the Y-fibre

```text
2 β_p + t_p + a_p + ε_p  =  4
```

(`ε_p≥0` residual L_C multiplicity). Summing fibres: `Σ a_p = 4s - 2 n_1 - Σ t_p - Σ ε_p`. Substituting into (†) and cancelling `-2n_1` produces

```text
2 r_1 + s_0 c_0 + Σ_p (s_0 k_p - t_p)  =  1 + 2 s_0 + Σ_p ε_p .     (5')
```

The printed display of Thm 4.3(5) is the same formula with `Σ ε_p` moved to the left. That is an algebra error: `a_p=4-2β_p-t_p-ε_p` puts `ε` on the right of (5'). When every `ε_p=0` the two displays agree, and the positivity argument the report runs by inspection of `s_0∈{1,2,3}` does force `c_0=1` and the stated `r_1` dichotomy. The error matters as soon as some `ε_p>0` is admitted — and the report explicitly admits L_C points on `Sing A_F`.

**Shape `s_0=1` (`a_0=3`), ε=0 slice.** (5') reads `2 r_1 + c_0 + NN = 3` with `NN:=Σ(k_p-t_p)≥0`. Min `r_1≥1`, `c_0≥1` is 3, so `r_1=c_0=1`, `NN=0`. Concrete witness: one node `q∈Sing D_1\setminus D_0` (`β=2,t=0,k=0,a=0,ε=0`) and D_0≅A^1 disjoint from D_1. Then `s=1`, `n_1=2`, `n_2=0`, `χ_1=2-1-2=-1`, `χ_0=1`, LHS of (†) `2(-1)+1(1)=-1`, RHS `3-4+0=-1`. Printed (5) also holds because `ε=0`. Here `c_0=1` is forced.

**Shape `s_0=1` with ε>0: `c_0=1` is not forced.** Take `r_1=1`, `c_0=2`, `NN=0`, `Σε=1`, and two points of `Sing A_F`:

- `q∈Sing D_1\setminus D_0`: `β_q=2`, `t_q=0`, `k_q=0`, `a_q=0`, `ε_q=0` (fibre `4=4`);
- `p∈D_1∩D_0`: `β_p=1`, `t_p=1`, `k_p=1`, `a_p=0`, `ε_p=1` (fibre `2+1+0+1=4`).

Then `s=2`, `n_1=3`, `n_2=1`, `χ_1=2-1-3=-2`, `χ_0=2-2-1=-1`. LHS of (†): `2(-2)+1(-1)=-5`. RHS: `3-8+0=-5`. So (E) holds, fibres hold, `NN=(0-0)+(1-1)=0`. Corrected (5') is `2(1)+1(2)+0=4` against `1+2+1=4`. Printed (5) reads `5=3` and fails. And `c_0=2`, so `D̃_0≅C^*`, contradicting "hence `c_0=1`".

**Shape `s_0=2` (`a_0=2`), ε=0 slice.** (5') reads `2 r_1 + 2 c_0 + NN = 5`. The left is even plus `NN`, so `NN` is odd and at least 1; the only nonnegative solution with `r_1,c_0≥1` is `r_1=c_0=1`, `NN=1`. Concrete witness: node `q` as above, plus an intersection `p` with `β=1`, `t=1`, `k=1`, `a=1`, `ε=0` (fibre `2+1+1+0=4`). Then `s=2`, `n_1=3`, `n_2=1`, `χ_1=-2`, `χ_0=0`, LHS of (†) `2(-2)+2(0)=-4`, RHS `3-8+1=-4`. Printed (5) holds (`ε=0`). On this slice `c_0=1` and `r_1=1` are forced.

**Shape `s_0=3`, r_1 dichotomy.** With `ε=0`, (5') is `2 r_1 + 3 c_0 + NN = 7`. Solutions with `r_1,c_0≥1`, `NN≥0`: `(r_1,c_0,NN)=(1,1,2)` and `(2,1,0)` only. That is the advertised dichotomy. With `ε>0` extra solutions appear (`c_0=2` with `ε≥1`, `r_1=3` with `ε≥2`), so the dichotomy is not forced once L_C multiplicity is allowed.

**Verdict.** BROKEN. The printed identity has the wrong sign on `Σ ε_p`. The claim "`c_0=1`" (and the `s_0=3` dichotomy as an exhaustive list) is a theorem only on the slice `ε≡0`; the explicit `(s_0,r_1,c_0,NN,ε)=(1,1,2,0,1)` configuration satisfies (E) and every fibre relation the proof invokes, with `c_0=2`.

## 4. Group theory: S_4 transpositions, (2,2) orbits, cyclic S_N, OPEN[B0-N4-REDUCIBLE-PI1]

**Cyclic transitive subgroup of `S_N`.** If `G=⟨g⟩≤S_N` is transitive, the orbits of `⟨g⟩` are the supports of the cycles of `g` (fixed points as 1-cycles). Transitivity forces a single N-cycle. Used in Thm 3.5: `π_1(C^2-D)≅Z` cyclic transitive on N letters ⇒ N-cycle ⇒ no fixed point, contradicting `a≥1`. HOLDS.

**Transitive subgroup of `S_4` generated by conjugates of one transposition.** Let `τ` be a transposition and let `G=⟨ σ τ σ^{-1} : σ∈G ⟩` act transitively on 4 letters. The generating set is a G-conjugacy class of transpositions; the associated graph `Γ` (vertices `{1,2,3,4}`, edges the transposed pairs) is G-invariant. The subgroup generated by those transpositions preserves the connected components of `Γ`, so transitivity of G forces `Γ` connected. A connected graph of transpositions contains a spanning tree of transpositions, which generates all of `S_4`. Thus G=`S_4`.

Controls: `A_4` has no transpositions; `C_4` and `V_4` have none of type `(2,1^2)`; the Sylow `D_4=⟨(1234),(24)⟩` contains the two disjoint transpositions `(24)` and `(13)`, which are conjugate in `D_4`, but the subgroup they generate is `⟨(13),(24)⟩≅C_2×C_2 ≠ D_4`, so `D_4` is not generated by that class. No other transitive subgroup of `S_4` is generated by transpositions. Thm 4.3(3) HOLDS.

**Two transpositions, orbit sizes `(2,2)`, are disjoint.** Let `σ,τ` be transpositions.

- Equal: orbits `2+1+1`, not `(2,2)`.
- Share one letter, e.g. `(12),(13)`: generate `S_3`, orbits `3+1`.
- Disjoint, e.g. `(12),(34)`: group `C_2×C_2`, orbits `(2,2)`.

These are the only incidence patterns of two 2-subsets of a 4-set. Thm 4.3(4) HOLDS. (Commuting is equivalent to equal-or-disjoint, so the local `π_1≅Z^2` at a node of two smooth branches plus orbit type `(2,2)` already forces disjointness.)

**Weaker sufficient form in OPEN[B0-N4-REDUCIBLE-PI1].** A YES on abelianness of `π_1(C^2-D)` implies there is no surjection onto `S_4` at all. The weaker form ("no surjection `π_1(C^2-D)→S_4` sending every meridian to a transposition and the two local meridians at each double point to disjoint transpositions") is strictly weaker, and it is sufficient to kill Thm 4.3(3)–(4): meridians of the single irreducible `D_1` generate `π_1` up to conjugacy, so any such surjection would realise a transitive transposition-generated subgroup of `S_4`, hence `S_4`, with the node constraint of (4). The form is correctly weaker and correctly sufficient. Whether it is true is the OPEN, not tested here (Deligne–Fulton / Nori were not acquired, matching the report's own refusal to quote them).

**Verdict.** HOLDS on the three group claims and on the logical status of the weaker form. The geometric lemma remains OPEN.

## 5. Prop 2.1/2.2 charts and Prop 2.3 unobstructedness

Take `k=2`, `l=3`, so `μ_D=l-k=1` and `γ=l/k=3/2`. Dictionary: `(k,l,v,u)=(m_φ, n_φ-m_φ, t, ξ)` gives `m_φ=2`, `n_φ=5`.

**Żołądek chart.** Simplest alteration with one free term, plus a lower term to exercise the general Jacobian: `θ˜(u,v)=(v + u v^3, v^{-2})` (so `l_1=1`, `l=3`, `k=2`, `gcd(1,3,2)=1`).

```text
∂θ1/∂u = v^3 ,   ∂θ1/∂v = 1 + 3u v^2 ,
∂θ2/∂u = 0   ,   ∂θ2/∂v = -2 v^{-3} .
det Dθ˜ = v^3 · (-2 v^{-3}) - 0 = -2 .
```

Żołądek's printed `v^{l-k-1}` is `v^{0}=1`, up to the unit `-k=-2`. Matches `[Z-6.7]` (`zoladek2008_official.pdf` local p. 28 / journal p. 458): `Jac θ˜ = v^{l-k-1}`, `μ_D=l-k=1`.

**Chau chart.** π-series (2.5) with `m=2`, `n=5`: `φ(x,ξ)= x^{0} + ξ x^{1-5/2} = 1 + ξ x^{-3/2}` (constant term `a_2=1`). Then `Φ(t,ξ)=(t^{-2}, φ(t^{-2},ξ))=(t^{-2}, 1 + ξ t^{3})`.

```text
∂x/∂t = -2 t^{-3} ,  ∂x/∂ξ = 0 ,
∂y/∂t = 3 ξ t^2  ,  ∂y/∂ξ = t^3 ,
det DΦ = (-2 t^{-3})(t^3) = -2 .
```

Chau's printed formula (`chau1999_apm71_full.pdf` journal p. 294): `-m_φ t^{n_φ-2m_φ-1} = -2 t^{5-4-1}=-2`. Same monomial. Coordinates are exchanged (`Φ` has `x=t^{-m}`, `θ˜` has `y=v^{-k}`), as Prop. 2.1 states. Both Jacobians equal `-2`.

The ξ-derivative is always `x^{1-n/m}` independently of the `a_k`, so `det DΦ=-m t^{n-2m-1}` is an identity, not an estimate. For a Keller map the chain rule gives `det DF_φ=J·det DΦ=-m J t^{μ_l-1}` with `μ_l=n-2m=l-k`, which is Prop. 2.2.

**`μ_l≥1` forcing.** Holomorphy of `F_φ` across `{t=0}` forces `ord_t det DF_φ≥0`, i.e. `μ_l≥1`. Negative control: `l=k=2` (so `μ=0`). `θ˜(u,v)=(u v^2, v^{-2})` has `det=-2 v^{-1}`, a simple pole; Chau `n=4`, `m=2` gives `-2 t^{4-4-1}=-2 t^{-1}`. The order-`-1` chart is not holomorphic, so `μ=0` is excluded by holomorphy alone.

**Prop. 2.3, `l=k+1` unobstructed.** The single integral condition `μ_l=1` is `l=k+1`. Then `gcd(k+1,k)=1` for every `k≥1`, so the normalisation `gcd(l_1,…,l,k)=1` of `[Z-6.7]` never rules the chart out. The worked pair `(k,l)=(2,3)` is one such chart, and both Jacobians are units (order 0). No further inequality `l` vs `k` is present in the Jacobian, which is an exact monomial.

**Verdict.** HOLDS.

## 6. Countermodel hunt for Cor 3.6 (Keller hypothesis)

Cor. 3.6: a noninvertible Keller map cannot have `A_F` irreducible and smooth. The hunt is among non-Keller quasi-finite maps, to see whether Keller is doing work.

**Witness.** `F=(x, y + x y^3) : C^2→C^2`. Jacobian `1+3x y^2`, not constant. Geometric degree 3: `C(x,y)/C(x, y+x y^3)` is generated by a root of `u T^3 + T - v =0`. Quasi-finite: the fibre over `(a,b)` is `x=a` and `y+a y^3=b`; one root if `a=0`, three if `a≠0`.

Non-proper values: if `y_n→∞` and `F` stays bounded then necessarily `x_n ∼ -1/y_n^2`. Precisely, `x=-y^{-2} + c y^{-3}` gives `P→0` and `Q= y + (-y^{-2}+c y^{-3}) y^3 = c`. Every `(0,c)` is a non-proper value, and every other end (`y` bounded and `x→∞`; both `→∞` off that Puiseux ray) sends `F→∞`. Thus `A_F={P=0}≅A^1`, irreducible and smooth.

This is a degree-3 quasi-finite polynomial map with irreducible smooth `A_F`. Cor. 3.6 without the Keller hypothesis is false; the hypothesis is load-bearing. The N=2 member of the same family, `(x, y+x y^2)`, likewise has `A_F={P=0}≅A^1` (Jacobian `1+2xy`). No Keller countermodel was found at desk (and none is claimed).

**Verdict.** HOLDS as a Keller-specific statement, with an explicit non-Keller witness that the hypothesis is necessary. No countermodel among Keller maps was produced.

## 7. Verdict table

| Target | Verdict |
|---|---|
| 1. Lemma 3.4 / (3.2), five controls | **HOLDS** |
| 2. N=4 table complete; N=5 survivors `(2,0)+(1,1)` and `(2,1)+(1,0)` | **HOLDS** |
| 3. Thm 4.3(5), shapes `s_0=1,2` and `r_1` at `s_0=3` | **BROKEN** (sign of `ε`; `c_0=1` not forced) |
| 4. Group claims in 4.3(3)–(4) and the weaker OPEN form | **HOLDS** (geometric lemma itself remains OPEN) |
| 5. Prop 2.1/2.2 dictionary, `μ≥1`, Prop 2.3 `l=k+1` | **HOLDS** |
| 6. Cor 3.6 among non-Keller maps | **HOLDS** (Keller necessary; witness `F=(x,y+x y^3)`) |

Load-bearing break is Target 3 only. Targets 1–2, 4–6 survive desk-scale exact checks. The N=4 residual configuration of Thm 4.3 is therefore not as rigidly a polynomial curve on the trivial-dicritical side as printed: L_C multiplicity at `Sing A_F` numerically permits `D̃_0≅C^*`.

## 8. Sources fetched

Rehashed at execution; all five match the B0 report §0 table.

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7  refs/chau1999_apm71_full.pdf
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3  refs/do.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

Pages used: Chau 1999 journal pp. 293–294 (Lemma 3.1 / `det DΦ`); Żołądek 2008 journal pp. 457–459 (Prop. 6.5(b), Prop. 6.7); Orevkov `jc86.pdf` local pp. 7–10 (Lemma 4.2, Cor. 4.3, Lemma 5.2, Lemma 5.3, closing Remark). Deligne–Fulton and Nori were not acquired.

<!-- BODY-END -->
