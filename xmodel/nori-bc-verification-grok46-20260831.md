# NORI-BC verification — computation and countermodel arm

Date: 2026-08-31
Lane: computation/countermodel (independent of the gate)
Charged inputs (frozen, hashed):

- `nori-bc-extension-opus5-20260831.md` SHA-256 `64bcabd1e14d69026cc86e101ff266a92009c7f15e9dfc00dce88fb607e7560f`
- `block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md` SHA-256 `bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270`

Hash verification: MATCH (both files).

## 0. Hash check and scope

Both charged SHA-256 values were recomputed with `shasum -a 256` on the frozen copies **before any mathematical work** and match the boxed hashes exactly.

Scope of this arm: desk-scale exact arithmetic and topology only. No CAS. Primary literature was fetched and hashed as recorded below; Nori was re-fetched from Numdam and hashed to `1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45` (4 546 575 bytes), matching the charged report. No canonical ledger, charged file, or `jc2-lean` was edited or inspected.

**Literature hashed in this arm.**

| Source | bytes | SHA-256 |
|---|---|---|
| Nori, *ASENS* 1983, Numdam PDF | 4546575 | `1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45` |
| Amram–Garber–Teicher, arXiv:math/0305418v4 | 478905 | `33febe81567201d577d4a1b473be50adc18b95ff9d8a5b266b14aeb06d82c1b0` |
| Amram–Garber–Teicher, arXiv:math/0612346v2 | 435196 | `7287c49c82b1c592245d866aa6e8adaebedfe180af1df092280fa1ccfd5a44cc` |
| Akyol–Degtyarev, arXiv:1406.1491v2 | 501157 | `724fccc5a0a192585420e484f56da4c6238b32d0dc506bc4e39606526779d70f` |
| Artal Bartolo, arXiv:alg-geom/9505007 | 94267 | `70e97ea99753489fb7db1784a33dd9de4b59122405a7ec3115a01ab5f82b8af7` |

Zariski, *Amer. J. Math.* **51** (1929), 305–328, was not obtained as a byte-stable PDF (JSTOR). The π₁ claim for the six-cuspidal torus sextic is consumed from Nori's raster-quoted Example 6.7 (journal p. 336) and from the independently hashed secondary sources above. Yang, *Tohoku Math. J.* **48** (1996), 203–227, is the complete ADE-sextic existence list; the Project Euclid copy returned an HTML paywall stub, not a PDF, so it is **not** hashed.

Lemma 4.3 of the PI1-S4 decision report is used only as the charged identity `C'^2 - 2 delta_aff = 3d-2-M_infty`; the identity is re-derived in §5 from adjunction plus `sum m_j(m_j-1)=2 delta_infty`, without reading `jc2-lean`.


## 1. Lemma 3.1 blow-up bookkeeping at k=1,2,3

Local model: two smooth branches `b1 = {y=0}`, `b2 = {y=x^k}` in a smooth surface. Centres of the minimal embedded resolution of the pair are free (each lies on exactly one exceptional), by the coordinate computation of charged Lemma 3.1(1): in the chart `y = x y_1` the pair becomes `y_1=0`, `y_1=x^{k-1}`, with `E={x=0}`, and the previous exceptional lives in the other chart.

A blow-up at a point of multiplicity `m` drops self-intersection by `m^2`. If both branches lie on one irreducible `C`, every centre has `m=2`. Nori's `s = G.(G+2F)` equals that total drop, because `(C')^2 = C^2 - F(C)` and `F(C)=s`.

**k=1 (node `A_1`).** One blow-up. Chart `y=x y_1`: strict transforms `y_1=0` and `y_1=1`, meeting `E={x=0}` at two distinct points, transversely. Multiplicity sequence of `C`: `(2)`. Drop `4`. Total transform `C' + 2E`, so `G=2E`, `G.(G+2C') = 4E.(E+C') = 4(-1+2)=4`. Thus `s=4=4·1`. After this single step the pair is already nodal (no residual triple point).

**k=2 (tacnode `A_3`).** Step 1 as above yields `y_1=0`, `y_1=x`, `E_1={x=0}`: three pairwise transverse smooth germs at one point (ordinary triple point). Multiplicity `(2)`. Drop `4`. Step 2 blows that point: chart `y_1 = x y_2` separates `b1`, `b2` from each other and from `E_2` at three distinct points; the strict transform of `E_1` lives in the other chart. Multiplicity `(2,2)`. Total drop `8`.

Pullback bookkeeping: `σ^*C = C' + 2E_1' + 4E_2` (the second exceptional inherits multiplicity 2 from `C` and 2 from `E_1`). Then `G=2E_1'+4E_2`, with `E_1'^2=-2`, `E_2^2=-1`, `E_1'·E_2=1`, `E_1'·C'=0`, `E_2·C'=2`. Hence `G^2=-8` and `G·C'=8`, so `s=G^2+2G·C'=8=4·2`.

**k=3 (`A_5`).** After two steps the picture is again an ordinary triple point (`y_2=0`, `y_2=x`, `E_2={x=0}`). The third blow-up separates all three. Multiplicity sequence `(2,2,2)`, total drop `12`. The first exceptional is *not* blown at step 3 (it meets `E_2` at a different point). Pullback: `σ^*C = C' + 2E_1' + 4E_2' + 6E_3`. The rule `s=sum m_i^2` gives `4+4+4=12=4·3`, matching `(C')^2=C^2-12`.

| `k` | type | multiplicity sequence of `C` | self-intersection drops | `s=sum m_i^2` | `4k` |
|---|---|---|---|---|---|
| 1 | `A_1` | `(2)` | 4 | 4 | 4 |
| 2 | `A_3` | `(2,2)` | 4+4 | 8 | 8 |
| 3 | `A_5` | `(2,2,2)` | 4+4+4 | 12 | 12 |

In each case the `(k-1)`-st step is an ordinary triple point (vacuously for `k=1`), and the `k`-th blow-up separates. Distinct components (one branch each) have multiplicity `1` at every centre and drop `k`, not `4k`.

**Verdict: HOLDS.** The identity `s(A_{2k-1})=4k` is the multiplicity-square sum, verified by direct pullback at `k=1,2,3`. Charged erratum (E2) (`s(node)=4`, not the printed `2`) is the `k=1` row.


## 2. Theorem N-A numerics: three synthetic configurations

Inequality (3.1): `C^2 > 2 r_1 + 4 T + T_x`, equivalently `B(C) > 2T + T_x`, with `B(C)=C^2-2 r_1-2T` on this class (smooth branches, so `B=deg N_h`). Configurations are numerical, not existence claims unless noted.

**SYN-A (strict interior).** Irreducible nodal plane quartic, three nodes: `C^2=16`, `r_1=3`, `T=T_x=0`. Right-hand side `6`. `16>6`. `B=16-6=10>0`. Nori 3.27 applies verbatim. (Existence classical: generic rational quartic.)

**SYN-B (equality, self-tangential).** Irreducible plane sextic with three `A_5` points and no other singularities: `C^2=36`, `r_1=0`, `T=9`, `T_x=0`. RHS `36`. Strict inequality `36>36` **fails** (equality). `B=36-18=18`, and `2T+T_x=18`, so `B>2T` also fails at equality. Geometric genus `(5)(4)/2-9=1`; not the extremal rational object of §7. Existence of this configuration is not used.

**SYN-C (fails on `T_x`).** Two smooth plane quartics whose 16 intersection units are four contacts of order 4 (`A_7` cross-points): for either component, `C^2=16`, `r_1=T=0`, `T_x=16`. Then `16>16` fails, `B=16`, `2T+T_x=16`. Same numerical shape as the bitangent conics of §3, scaled: the coefficient `1` on `T_x` is again tight. (Existence not claimed; Bézout is saturated.)

Summary:

| config | `C^2` | `r_1` | `T` | `T_x` | RHS of (3.1) | (3.1) | `B` | `B>2T+T_x` |
|---|---|---|---|---|---|---|---|---|
| SYN-A nodal quartic | 16 | 3 | 0 | 0 | 6 | holds | 10 | holds |
| SYN-B three `A_5` | 36 | 0 | 9 | 0 | 36 | fails (=) | 18 | fails (=) |
| SYN-C four `A_7` cross | 16 | 0 | 0 | 16 | 16 | fails (=) | 16 | fails (=) |

The two sides of (3.1) are both represented. Interior cases pay the node cost `2` only; equality cases show that neither the `4T` nor the `T_x` coefficient can be lowered on numerical grounds alone. The charged bitangent-conic pair (next section) is the unique *existing* sharpness witness for `T_x`.

**Verdict: HOLDS** as numerics of (3.1). SYN-B and SYN-C are not asserted to exist.


## 3. Two bitangent conics: B, the unit failure, and π₁

Let `λ ∈ C \ {0,1}` and `C_1={zy=x^2}`, `C_2={zy=λ x^2}`, `D=C_1 ∪ C_2 ⊂ P^2`.

**Bézout and type.** `C_1 ∩ C_2 = {x=0, zy=0} = {P=[0:1:0], Q=[0:0:1]}`, local intersection 2 at each, total 4. Both conics are smooth (the affine `YZ=1` is a smooth hyperbola; the points at infinity on each conic are smooth). Each of `P,Q` is an `A_3` of two smooth branches, contact `2`. For each component: `r_1(C_i)=0`, `T(C_i)=0`, `T_x(C_i)=2+2=4`, `C_i^2=4`. Definition 3.25 sees only branches of `C_i` itself, so `A(C_i;P)=0` and `B(C_i)=C_i^2=4>0`.

**(3.1) fails by one unit.** `4 > 2·0 + 4·0 + 4` is `4>4`, false. Equivalently `B=4 > 2T+T_x=4` is false. The gap is exactly one unit of `T_x`.

**Independent computation of π₁.** Charged §4.3 gives a Zariski–van Kampen computation yielding `⟨ t_1, t_λ | (t_1 t_λ)^2 = 1 ⟩`. Independently:

1. *Algebraic identification.* Set `c=t_1 t_λ`. The presentation is `⟨ t_λ, c | c^2=1 ⟩ ≅ Z * Z/2`. The two-relation form `⟨ a,b | (ab)^2=(ba)^2=1 ⟩` is the same group: `(ba)^2 = b(ab)^2 b^{-1}`, so the second relation is redundant once `(ab)^2=1`. Kurosh: the group is nonabelian. Abelianization: `H_1 ≅ Z ⊕ Z/2`, matching the standard `H_1(P^2-D)` for a two-component degree-`(2,2)` curve (`c_1(O(D_i))` generate with the relation `2[C_1]+2[C_2]=0` in `H_2(P^2)`, i.e. `2(t_1+t_λ)=0`).

2. *Literature (hashed).* Amram–Garber–Teicher, arXiv:math/0305418v4, Proposition 1.1 (SHA-256 `33febe81…`): for a curve `S` of two tangent conics,
   `π_1(CP^2-S) ≅ ⟨ x_1, x_2 | (x_1 x_2)^2 = (x_2 x_1)^2 = e ⟩`.
   The same isomorphism to `Z * Z/2` is recorded in arXiv:math/0612346v2, Corollary 3.10 and the discussion after Corollary 2.9 (SHA-256 `7287c49c…`): `⟨ a,b | (ab)^2=(ba)^2=e ⟩ ≅ ⟨ x,y | x^2=e ⟩ ≅ Z * Z/2`. Their route is braid monodromy of the real arrangement, not the fibration `YZ` used in the charged report.

Thus `N = π_1(P^2-D) ≅ Z * Z/2` is nonabelian, while `B(C_i)>0`. Theorem N-A's `T_x` coefficient cannot drop; `B>0` alone is false for this class.

**Verdict: HOLDS** (numerics, the unit failure, and `π_1 ≅ Z * Z/2` by an independent hashed source).


## 4. Zariski-sextic data

Let `f`, `g` be general homogeneous forms of degrees 3 and 2, and `C = {f^2 - g^3 = 0} ⊂ P^2`. Degree 6, so `C^2=36`.

**Singularities.** At `f=g=0` one has 6 points (Bézout: `3·2=6`); generically they are distinct. Locally this is `u^2=v^3`, an ordinary cusp `A_2`, unibranch. No other singularities for general `f,g`. Each cusp has `r=1` in Definition 3.25, so the pairwise sum is empty: `A(C;P)=0` and `B(C)=C^2=36>0`. Delta: `δ(A_2)=1`, total `δ=6`, geometric genus `10-6=4`. The “normal-bundle” quantity `C^2-2δ=24` is also positive.

**`F(C)` and Nori 6.5.** Each ordinary cusp has `s=6` (Example 6.7, and `2^2+1^2+1^2=6`). Thus `F(C)=36=C^2`, so 6.5's hypothesis `C^2>F(C)` fails (equality). This is Nori's own sharpness example for 6.5.

**π₁.** Nori Example 6.7, journal p. 336, raster-quoted in the charged report, attributes to Zariski: `π_1(P^2-C) ≅ Z/(2)*Z/(3)`. Primary: Zariski, *Amer. J. Math.* **51** (1929), 305–328 (not hashed: no open PDF obtained). Independently hashed confirmations:

- Artal Bartolo, arXiv:alg-geom/9505007, p. 1 (SHA-256 `70e97ea9…`): “Let `C_1` be a sextic … `f^2+g^3=0` … 6 cusps lying on a conic … `π_1(P^2\C_1) ≅ Z/(2)*Z/(3)`,” citing Zariski [9] = the 1929 paper.
- Akyol–Degtyarev, arXiv:1406.1491v2 (SHA-256 `724fccc5…`), and the standard survey statement of Eyral–Oka (*J. Math. Soc. Japan* **57**, 2005): six cusps on a conic ⇒ `π_1 ≅ (Z/2)*(Z/3)`; six cusps not on a conic ⇒ `Z/6`.

The group `Z/2 * Z/3 ≅ PSL_2(Z)` is nonabelian. Hence `N=ker(π_1(P^2-C)→π_1(P^2))` is nonabelian while `B(C)=36>0`. This kills any “replace nodality in 3.27 by `B(C)>0`” for general singularities. It does *not* touch Theorem N-A, whose hypothesis (A1) forbids unibranch points.

**Verdict: HOLDS** (`B=36>0`, `π_1 ≅ Z/2 * Z/3`, sourced). The 1929 original is cited but not byte-hashed.


## 5. Corollary N-A-RES algebra and the (6,3) table

**Re-derivation of the scalar identity.** On the infinity resolution `X'→P^2` one has `C'^2 = d^2 - sum m_j^2` and `sum m_j(m_j-1) = 2 δ_infty` (unibranch germ at `Q`). Writing `M_infty = sum m_j` and `N_infty = sum m_j^2` gives `N_infty = 2δ_infty + M_infty`, hence `C'^2 = d^2 - 2δ_infty - M_infty`. For a rational plane curve of degree `d`, `2(δ_aff+δ_infty)=(d-1)(d-2)`. Therefore

```text
C'^2 - 2 δ_aff = d^2 - 2δ_infty - M_infty - 2δ_aff
                = d^2 - (d-1)(d-2) - M_infty
                = 3d - 2 - M_infty.
```

This is charged Lemma 4.3. In the residual class every affine singularity is an `A_{2k_p-1}` of two smooth branches, so `δ_aff = r_1 + T`. Substitute:

```text
C'^2 - 2 r_1 - 4T
  = (C'^2 - 2 δ_aff) + 2(r_1+T) - 2 r_1 - 4T
  = (3d-2-M_infty) - 2T.
```

The N-A inequality on `X'` is `C'^2 - 2 r(C') > 0` with `r(C')=r_1` and `T_x=0` (irreducible `D_1`, no cross-component tangency). For integers this is `M_infty + 2T ≤ 3d-3`, i.e. (M-INF-T). **Algebra HOLDS.**

**Germ constraints at `(d,n)=(6,3)`.** Here `a=d-n=3` and `a | d`. Lemma 1.3 of the residual report (re-used as a contact constraint, not as a π₁ statement): `I(C, L_infty)=d` is either a multiple of `a` strictly less than `β_1`, or equals `β_1`. Since `d=2a`, necessarily `β_1 > 6` and `3 ∤ β_1` (else the first characteristic exponent would not yet have appeared). The germ is the one-pair `(3,β_1)`-cusp. Then `2δ_infty=(3-1)(β_1-1)`, so `δ_infty=β_1-1`. Genus: `δ_aff+δ_infty=10`, hence `δ_aff=11-β_1`. `M_emb=a+β_1-1=β_1+2` (one-pair Euclidean sequence; equivalently (4.2) at `h=1`). Since `β_1≥7`, `M_infty=max(M_emb,6)=β_1+2`. Gate: `β_1+2 + 2T ≤ 15`, i.e. `T ≤ (13-β_1)/2`. Residual singularity: `δ_aff≥1` forces `β_1≤10`. The integers `7≤β_1≤10` with `3 ∤ β_1` are exactly `{7,8,10}` (`9` is excluded).

`T=sum_{k_p≥2} k_p` with `r_1+T=δ_aff` and each `k_p∈Z_{≥1}`, so `T=1` is impossible, and `T≤δ_aff`.

| `β_1` | `δ_infty` | `M_infty` | `δ_aff` | gate `2T≤15-M` | admissible `T` | N-A-RES closes | survives |
|---|---|---|---|---|---|---|---|
| 7 | 6 | 9 | 4 | `T≤3` | `{0,2,3,4}` | `{0,2,3}` | `{4}` |
| 8 | 7 | 10 | 3 | `T≤2` | `{0,2,3}` | `{0,2}` | `{3}` |
| 10 | 9 | 12 | 1 | `T≤1` | `{0}` | `{0}` | none |

The charged table omitted the `δ_infty` column but the displayed `M_infty`, `δ_aff`, gates, and survivor list match. At `β_1=10`, `δ_aff=1` forces a single node (`T=0`); the gate `T≤1` is then automatic. Survivors of N-A-RES at `(6,3)` are exactly `(β_1,T)∈{(7,4),(8,3)}`.

**Verdict: HOLDS** (algebra and the complete `(6,3)` table).


## 6. Same analysis at (6,2) and (6,4); banked (6,4) triple-point curve

Throughout, `3d-3=15` and `δ_aff+δ_infty=10`. `M_emb=mult+β_h-1` is used as the one-pair Euclidean evaluation at `(6,4)` and as the two-pair evaluation at `(6,2)` (induction of the residual hostile review; checked on the multiplicity sequences below).

### (6,2): `a=4`, `4 ∤ 6`

Lemma 1.3 forces `β_1=d=6`. Then `e_1=gcd(4,6)=2`, so a second characteristic exponent `β_2` is required, odd and `>6`. Standard bars: `n_1=n_2=2`, `β̄_2=β_2+6`, and `2δ_infty=β_2+9`. Thus `δ_infty=(β_2+9)/2`. Singularity `δ_aff≥1` gives `β_2≤9`, so `β_2∈{7,9}`. `M_emb=4+β_2-1=β_2+3`, and `M_infty=β_2+3` (already `>6`).

| `β_2` | `δ_infty` | `M_infty` | `δ_aff` | gate `T≤(15-M)/2` | admissible `T` | closes | survives |
|---|---|---|---|---|---|---|---|
| 7 | 8 | 10 | 2 | `T≤2` | `{0,2}` | both | none |
| 9 | 9 | 12 | 1 | `T≤1` | `{0}` | `{0}` | none |

**Verdict for (6,2): HOLDS, and N-A-RES closes the whole row.** (No residual configuration of double points survives.)

### (6,4): `a=2`, `2 | 6`

Lemma 1.3: `β_1>6` and `β_1` odd (so `e_1=1`, one pair, germ `(2,β_1)`). Then `δ_infty=(β_1-1)/2`, `δ_aff=(21-β_1)/2`, `M_emb=2+β_1-1=β_1+1=M_infty`. Naive genus `δ_aff≥1` allows `β_1∈{7,9,11,13,15,17,19}`.

| `β_1` | `δ_infty` | `M_infty` | `δ_aff` | gate `T≤(15-M)/2` | admissible `T` | closes | survives |
|---|---|---|---|---|---|---|---|
| 7 | 3 | 8 | 7 | `T≤3` | `{0,2,3,4,5,6,7}` | `{0,2,3}` | `{4,5,6,7}` |
| 9 | 4 | 10 | 6 | `T≤2` | `{0,2,3,4,5,6}` | `{0,2}` | `{3,4,5,6}` |
| 11 | 5 | 12 | 5 | `T≤1` | `{0,2,3,4,5}` | `{0}` | `{2,3,4,5}` |
| 13 | 6 | 14 | 4 | `T≤0` | `{0,2,3,4}` | `{0}` | `{2,3,4}` |
| 15 | 7 | 16 | 3 | `T≤-1` (impossible) | `{0,2,3}` | none | all |
| 17 | 8 | 18 | 2 | impossible | `{0,2}` | none | all |
| 19 | 9 | 20 | 1 | impossible | `{0}` | none | `{0}` |

The residual r2 claim `δ_aff≥5` (hence `β_1≤11`, `M≤12≤15`) is **false** as a semigroup inference from `S⊇⟨4,6⟩` alone: that containment only *upper*-bounds the gap set. Sharp floor from a numerical semigroup of genus 3 containing `{4,6}` is `δ_aff≥3`, attained.

### Banked `(6,4)` curve with `β_h=15`

The M-INF review example
```text
p(t)=t^6+(3/2)t^3+3/8,    q(t)=t^4+t,
```
satisfies `p^2-q^3=(1/8)t^3+9/64`, so `z:=t^3 ∈ C[p,q]` and `C[p,q] ≅ C[z,y]/(y^3-z(z+1)^3)` with `y=q`. Birational: `t=y/(z+1)` and `t^3=z`. Type `(6,4)`. Semigroup `S_aff=⟨3,4⟩`, gaps `{1,2,5}`, `δ_aff=3`, hence `δ_infty=7` and `β_1=15` for the one-pair germ of multiplicity 2. Then `M_emb=16>15`.

Affine singularities, by hand: `F=y^3-z(z+1)^3`, `F_y=3y^2`, `F_z=-(z+1)^2(4z+1)`. The only common zero on `F=0` is `(z,y)=(-1,0)`. Tangent cone: set `w=z+1`, lowest terms `y^3+w^3=(y+w)(y+ωw)(y+ω^2 w)`, three distinct lines. Ordinary triple point of three smooth branches; local `δ=3`. This is **not** a double point of two smooth branches.

**Compatibility with the residual class.** Numerically, `δ_aff=3` *can* be partitioned as three nodes (`T=0`), a tacnode plus a node (`T=2`), or one `A_5` (`T=3`). So the infinity type `β_h=15` is not numerically forbidden for double-points-only. Intrinsically, however, any affine ring with `S=⟨3,4⟩` is (after Aut(`A^1`)) `C[t^3,t^4]` (unibranch `(3,4)`-cusp, type `(4,3)`, not birational of type `(6,4)`) or a deformation such as `C[t^3,t^4+t]`, whose unique plane model is the triple-point curve above. Thus *this* semigroup does not yield a residual `D_1`. Whether some other genus-3 semigroup containing `{4,6}` (e.g. `⟨2,7⟩` or `⟨4,5,6,7⟩`) is realized by a `(6,4)` polynomial curve with only `A_{2k-1}` points is not settled at desk. If such a curve exists, (M-INF-T) **fails for every** `T` at `β_1≥15`.

**Verdict.** `(6,2)` table HOLDS and is closed by N-A-RES. `(6,4)` germ constraints and gate numbers HOLD as displayed; the charged residual's `δ_aff≥5` bound is BROKEN. The banked curve is a genuine `(6,4)` polynomial curve of type `β_h=15` with an ordinary triple point, hence **out of the residual class**. Compatibility of that infinity type with double-points-only: numerically possible, geometrically **UNTESTABLE-AT-DESK**.


## 7. Rational sextic with 5 tacnodes

**Would-be invariants (independent of existence).** Five `A_3` points, no other singularities, irreducible plane sextic:

- `δ(A_3)=2`, so `δ=T=10` and `r_1=T_x=0`.
- Arithmetic genus `(d-1)(d-2)/2 = 5·4/2 = 10`. Geometric genus `10-10=0`. The curve would be rational, as charged.
- `C^2=36`, `B(C)=36-2·10=16>0`.
- N-A: `36 > 4·10 = 40` fails (by four units). Equivalently `B=16 > 2T=20` fails.
- This is the first degree at which `B>0` and N-A diverge for irreducible curves with only nodes and self-tangencies (charged §7.3). Class `m = d(d-1)-4·(# tacnodes)=30-20=10>0`: no Plücker obstruction.

**Existence survey (fetched/hashed).** `5A_3` is ADE of total Milnor number `15≤19`, hence in the range of Urabe (`μ≤16`) and of Yang's complete list of simple sextics (*Tohoku Math. J.* **48** (1996); PDF not obtained, Project Euclid paywall). Akyol–Degtyarev, arXiv:1406.1491v2 (hashed `724fccc5…`) complete the *deformation* classification of irreducible simple sextics and record 2996 non-maximizing non-special sets, but do not print the list; a search of that PDF found no isolated `5A_3` (or `A_3^5`) row. Orevkov, arXiv:1504.06615, parametrizes only the *maximizing* (`μ=19`) double-point sextics; `5A_3` is not among them. No primary source obtained in this arm exhibits an irreducible plane sextic whose only singularities are five tacnodes, and none proves impossibility. A weaker object is classical: rational sextics with three tacnodes and four nodes exist (e.g. Dolgachev, *Rational Coble surfaces*, the tetrahedral example with three tacnodes and four nodes, `δ=3·2+4=10`). Replacing the four nodes by two further tacnodes is one condition per tacnode on the 9-dimensional moduli of rational plane sextics, expected dimension 4, which is not a proof.

**π₁.** Even given existence, abelianness of `π_1(P^2-C)` is not a desk computation (the curve is irreducible of degree 6, so `H_1≅Z/6`; nonabelianness would have to be a nonabelian extension).

**Verdict.** Invariants HOLDS. Existence (and π₁) **UNTESTABLE-AT-DESK**. The coefficient `4T` remains the honest N-A charge until this object is constructed or ruled out.


## 8. Verdict table and open items

| Target | Verdict | Note |
|---|---|---|
| (1) Lemma 3.1 at `k=1,2,3` | **HOLDS** | multiplicity sequences `(2)`, `(2,2)`, `(2,2,2)`; `s=4k` |
| (2) Theorem N-A, three synthetics | **HOLDS** | SYN-A interior; SYN-B/C equality (not existence claims) |
| (2+) bitangent conics: `B`, unit failure | **HOLDS** | `B(C_i)=4`, (3.1) is `4>4` |
| (2+) `π_1(P^2-two bitangent conics)≅Z*Z/2` | **HOLDS** | independent: Amram–Garber–Teicher Prop. 1.1, hashed |
| (3) Zariski sextic `B=36>0`, `π_1=Z/2*Z/3` | **HOLDS** | Nori Ex. 6.7 + hashed Artal 1995; 1929 original not hashed |
| (4) N-A-RES algebra | **HOLDS** | re-derived from Lemma 4.3 + `δ_aff=r_1+T` |
| (4) `(6,3)` table, all `β_1∈{7,8,10}` | **HOLDS** | survivors exactly `(7,4)` and `(8,3)` |
| (4) `(6,2)` N-A-RES table | **HOLDS** | whole row closed |
| (4) `(6,4)` germs and gates | **HOLDS** as numbers; residual `δ_aff≥5` **BROKEN** | naive `β_1` up to 19; floor `δ_aff=3` |
| (4) banked `(6,4)` `β_h=15` curve | **HOLDS** as a triple-point example; **out of class** | ordinary triple point, tangent cone `y^3+w^3` |
| (4) `β_h=15` vs double-points-only | **UNTESTABLE-AT-DESK** | numerically compatible (`δ_aff=3`); no residual witness |
| (5) 5-tacnode sextic invariants | **HOLDS** | `δ=T=10`, `g=0`, `B=16>0`, N-A fails `36>40` |
| (5) existence of that sextic | **UNTESTABLE-AT-DESK** | Yang list not obtained; Akyol–Degtyarev do not display `5A_3` |

Nothing in this arm is a new exit-price assertion. Typed OPENs left on the computation side: existence of a residual `(6,4)` curve with `β_1≥15`; existence and `π_1` of an irreducible rational sextic with five tacnodes and no other singularities.

No `charge_basis` line: this report consumes charged numerics and does not declare a new exit price.

<!-- BODY-END -->



