# Hostile review: SHAPE-3-FINISH (Opus) — Theorem TB and the family-3 ledger

**Reviewer.** Grok 4.6, different-model gate.
**Charge date.** 2026-09-01.
**Stance.** Default refutation; promotion only if the charged proof and ledger survive line-by-line attack.
**Scope.** THEOREM TB (total-branch congruence for normal triple covers); mixed-branching analysis; m=0 case; family-3 ledger; adjudication of the OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT] reversal versus SHAPE-KILL.

## 0. Hash verification and charged corpus

Frozen inputs were hashed with `shasum -a 256` before they were read. All three SHA-256 values match the charge exactly:

```text
963be6af1b87115508e0db5dda3f8212fb3116c9c1c1cc20701267b0be2829ec  shape-3-finish-opus5-20260901.md
0213fcae67bbde4d426a50f2d5d17c71db907d78718860459f14ff50e2ce4a01  shape-kill-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Below, **S3F**, **REV**, and **Coord** denote those three files in charge order. SK denotes the SHAPE-KILL report as quoted by REV (and, for the one sentence REV repeats from SK §4.2, as that quote). No canonical ledger or charged file was edited, `jc2-lean` was not inspected, and no CAS was run. `FALLACY-v2` is in force. No new exit price is asserted, so there is no `charge_basis` line.

Primary source re-opened (not saved as a campaign artifact):

```text
b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153
  https://arxiv.org/pdf/1211.2526v1   (fetched 2026-09-01, 174308 bytes)
  Taketo Shirane, A note on normal triple covers over P^2 with branch
  divisors of degree 6, arXiv:1211.2526v1.
  Consumed: Notation (reduced branch Δ_π = S_π + T_π; weighted
  Δ̄_π = S_π + 2 T_π; total branched point); Remark 0.2 (finite
  surjective from a normal surface to a smooth surface is a normal
  cover, via Cohen–Macaulayness); §§1.1.1–1.1.7 (Tschirnhausen
  module; Miranda Φ; local a,b,c,d and A,B,C; X ⊂ V(E) Cohen–Macaulay;
  branch divisor B^2−4AC, associated bundle (det T)^{-2}; Weierstrass
  split T ≅ L^{-1}⊕L^{-2}); Remark 0.5 / Introduction (nonempty
  (deg S, deg T)=(4,1) of Tokunaga/Yasumura).
  This hash reproduces S3F §7 and REV §0.
```

Miranda, *Triple covers in algebraic geometry*, Amer. J. Math. **107** (1985), was consumed only through Shirane’s §1.1 restatement, as in S3F. Theorem A was checked at `xmodel/pi1-s4-decision-opus5-20260831.md:214–219` (the citation S3F names). Infinity-chart orders `(ord v, ord u)=(d−n,d)` were checked at `xmodel/d1-degree-bound-sol56-20260831.md:60–64` and SK:102–105 (the row-sweep lines S3F cites are the general `(a,d)` form, specialised to family 3 by `a=g`, `d=4g`). Ciliberto–Miranda arXiv:2512.07965v1 was **not** consumed as a kill; see §10.

Default-to-refutation concentrated on: (i) existence of the mixed cover versus REV’s “no triple cover of `P^2`”; (ii) the trace-kernel step `n = T|_{T_0}` and the identification `m'=m` in TB; (iii) the Puiseux no-cancellation in (2.8) and the finite computation TB-2; (iv) whether Weierstrass splitting is actually a lever on the non-constant stratum; (v) the family-3 ledger against REV §8.

## 1. Verdict

**Headline.** THEOREM TB HOLDS, as do the mixed-cover existence, the weighted degree `4g+2`, the congruence `m ≡ g+2 (mod 3)` with `0 ≤ m ≤ 2g`, and Proposition TB-2 (`m=4` at `g=2`). The charged parity horn (reduced branch degree `4g+1` odd) is correctly REFUTED. Family 3 is not killed uniformly. The advertised reversal of REV on `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` is a **scope split, not a refutation**: REV’s *conclusion* about the then-typed OPEN is right; REV’s *supporting sentence* “there is no triple cover of `P^2` to apply it to” is false. Coord:49–50 remains too strong on every reading.

| Claim | Scope | Verdict |
|---|---|---|
| Mixed cover `Z→P^2` branched at `D̄ ∪ L_∞`, inertia `(2,3)` | non-constant family 3, every `g≥2` | **ESTABLISHED** |
| Charged parity horn (`4g+1` odd vs Cardano) | — | **REFUTED**; weighted `deg Δ̄=4g+2` even |
| `k = −deg det T = 2g+1` | every `g` | **ESTABLISHED** |
| THEOREM TB: `k_0+m ≡ 0 (mod 3)` | normal triple cover, smooth rational `T_0 ⊂ T_π` meeting the rest of `Δ̄` at one point | **ESTABLISHED** |
| `m=0` ⇔ curvilinear fibre ⇔ Gorenstein over `P` | same | **ESTABLISHED** |
| `m ≡ g+2 (mod 3)`, `0≤m≤2g` | non-constant family 3 | **ESTABLISHED** |
| `m=0 ⇒ g≡1 (mod 3)` | every `g≥2` | **ESTABLISHED**, conditional on `m=0` |
| Prop. TB-2: `(8,6)` non-constant has `m=4` | `g=2` | **ESTABLISHED** |
| Uniform kill of family 3 non-constant | every `g` | **NOT OBTAINED** (correctly not claimed as a theorem) |
| Route 2 (A-side fork) new constraint at `(4,3)` | every `g` | **VACUOUS**; fork entered, not exited |
| A(3) sharpened to `d≡4 (mod 6)` | coprime and not, `ord(Π)=3` | **ESTABLISHED**, conditional on `m=0` |
| Mixed cover exists, so REV “no triple cover of `P^2`” is false as written | — | **CONFIRMED** as a wording correction |
| Then-typed OPEN (descended, payoff `6∣d`) closes non-constant family 3 | — | **FALSE**; REV §7’s *conclusion* STANDS |
| Retyped Weierstrass-split on the mixed cover is a sufficient lever for `m=0` / `g≡1 (mod 3)` | — | **HOLDS as a hypothetical**; does not close family 3; already answered **NO** on `g≢1 (mod 3)` by `k=2g+1` |
| Coord:49–50 “would close family 3 if resolved” | — | **FALSE** on every typing |
| Existence of a residual curve in any surviving row | — | **NOT ASSERTED** (correctly) |

## 2. Charge reconstruction (what was claimed)

S3F takes as given REV’s promotion of SK-5: in the non-constant stratum of family 3, `(d,n)=(4g,3g)`, the block products `A,B,C` are pairwise distinct, `conj_Π` cycles them, and `Π` is a 3-cycle at every `g≥2`. Consequently the resolvent `ψ∘φ: π_1(A^2−D)↠S_3` does not factor through `π_1(P^2−D̄)`. REV and SK stop there, and infer that there is no triple cover of `P^2` to which `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` could apply.

S3F’s increment is Route 1. The same homomorphism is a representation of `π_1(P^2−(D̄∪L_∞))`. Normalising `P^2` in the degree-3 subextension attached to a point stabiliser `S_2<S_3` produces a normal triple cover `π: Z→P^2` with simple inertia along `D̄` and total inertia along `L_∞`, so (S3F (2.1)) `S_π=D̄`, `T_π=L_∞`, weighted branch `Δ̄=D̄+2L_∞` of degree `4g+2`. The charged parity horn (reduced degree `4g+1` odd) is declared dead; the exploitable arithmetic is `k:=−deg det T=2g+1` together with a local defect `m=ord_{P_∞}(Φ|_{L_∞})`.

THEOREM TB is the general statement: a smooth rational curve in the total branch, meeting the rest of `Δ̄` at one point, forces `k_0+m≡0 (mod 3)`, with `m=0` iff the fibre over that point is curvilinear iff `Z` is Gorenstein there. Specialised, `3∣(2g+1+m)` i.e. `m≡g+2 (mod 3)`, and a local expansion gives `0≤m≤2g`. The `m=0` branch kills every row with `g≢1 (mod 3)`. At `g=2`, TB-2 pins `m=4` exactly, so `(8,6)` is not in the `m=0` branch. Route 2 (the Theorem A order fork at outer coprime `(4,3)`) is declared structurally vacuous. Successors: `OPEN[S3-RESOLVENT-GORENSTEIN-AT-P-INF]` / `OPEN[S3-TB-M0]`, `OPEN[S3-TB-G2]`, and a retyped Tschirnhaus-split with payoff `6∣d+2` rather than `6∣d`.

Three explicit corrections are charged against REV/SK: (1) “no triple cover of `P^2`” is false as written; (2) REV’s rejection of Coord:49–50 for the non-constant stratum is itself false, because splitting *does* bear; (3) SK’s payoff `6∣d` is the descent-stratum form, and applying it to a 3-cycle stratum would conflate reduced and weighted branch.

What is *not* claimed: a uniform kill; existence of any residual curve; a desk-scale contradiction at `g≥3` from the leading `σ`-jets.

## 3. THEOREM TB — statement, hypotheses, and attack surface

**Statement** (S3F:154–164). Let `π: Z→Y` be a normal triple cover of a smooth surface, `T_0⊂T_π` a smooth rational curve in the total branch locus, meeting the rest of `Δ̄_π` in a single point `P`. Set `k_0:=−deg(det T|_{T_0})` and `m:=ord_P(Φ|_{T_0})≥0`. Then `k_0+m≡0 (mod 3)`. Moreover `m=0` iff the fibre of `π` over `P` is curvilinear, iff `Z` is Gorenstein over `P`.

Notation collision, inherited from Shirane: `T_π` is both the reduced total-branch divisor and (script `𝒯_π`) the Tschirnhausen module. Parseable. S3F’s `Δ_π` is Shirane’s *weighted* `Δ̄_π=S_π+2T_π`, not the reduced branch. Also parseable.

Hypotheses actually used, and whether family 3 supplies them:

- `Y` smooth, `π` a normal triple cover in Shirane’s sense (finite flat, `Z` normal). For family 3 this is the mixed cover of §5, not an extra axiom.
- `T_0` smooth rational, lying in the total-branch divisor. `L_∞≅P^1`.
- `T_0` meets the rest of `Δ̄` at one point. `D̄` is irreducible of degree `4g` with a single place at `P_∞=[1:0:0]` (row-nf-exhaustiveness review:55–60, REV §1.2(ii)); `(D̄·L_∞)_{P_∞}=4g`.
- Char 0 (trace of nilpotents; finite bijective ⇒ birational; `g≠0` in (2.8); the `3` in the polarised cubic). Present.
- `Φ|_{T_0}` not identically zero, so that `n^2` is generically rank 1 and `m<∞`. Ordinary total ramification along a reduced component of `T_π` (cyclic sanity check (i); local form `t^3=unit·σ`). If this failed, Miranda’s algebra would be degenerate along a curve and `Z` would fail to be a genuine triple cover.

Attack surface, in the order the proof uses it: (A) unique point of `Z` over every point of `T_0`, and `Γ:=(π^{-1}(T_0))_{\mathrm{red}}≅T_0`; (B) nilradical `n` of `A|_{T_0}` equals `T|_{T_0}` (the trace-kernel step S3F itself flags); (C) saturation `N` of `n^2`, quotient `Q`, and `Q^{⊗2}→N` of cokernel length `m'`; (D) `A=B=C=0` on `T_0`, so `Φ|_{T_0}` is a cube, and a primitive linear form can be completed to a holomorphic frame at `P`; (E) Miranda multiplication in that frame, identifying `m'=m`; (F) Gorenstein / curvilinear dictionary; (G) specialisation `k_0=2g+1` and the local expansion (2.8)–(2.12) for the bound and for TB-2.

Identity (2.3) is an input, not a consequence of TB. Polarised cubic `(α_0,…,α_3)=(−b, 3a, −3d, c)` versus Miranda’s `Φ=(−b, a, −d, c)`: the `3`’s are units in char 0. Hand expansion of the classical discriminant against `B^2−4AC` confirms (2.3) as written. Shirane 1.1.3 gives exactly that `Φ`. The `2A,2C` in Shirane’s multiplication `φ(z^2)=2A+az+bw` vanish on `T_0` once `A=B=C=0`, so they do not pollute the restricted algebra.

## 4. Line-by-line verification of the TB proof

**(A) Unique geometric fibre; `Γ≅T_0`.** Finite morphisms have 0-dimensional fibres, so no component of `π^{-1}(T_0)` can contract to a point. Each irreducible component therefore maps onto `T_0`. Over a generic point of `T_0` there is one geometric point of `Z` (total ramification), so there is one component. `Z` is a normal surface, hence Cohen–Macaulay; `T_0` is Cartier on the smooth surface `Y`; finite flat pullback `π^*T_0` is Cartier on `Z`, hence without embedded points. Every point of `Z` over `P` therefore lies on `Γ`. Finite bijective in char 0 is birational; a finite birational map onto a normal curve is an isomorphism. **HOLDS.**

**(B) `n=T|_{T_0}`.** `A=π_*O_Z` is a rank-3 bundle (`π` finite flat). Restrict to `T_0`. The map `A_0→π_*O_Γ≅O_{T_0}` is surjective on fibres (quotient by the maximal ideal of a local length-3 algebra). Kernel `n` is a rank-2 subbundle. The two local length-3 algebras over `C` are `C[t]/(t^3)` and `C[u,v]/(u,v)^2`; both have 2-dimensional maximal ideal with cube zero, so `n^3=0`. Multiplication by a nilpotent algebra element is a nilpotent endomorphism, hence has trace zero. Thus `n⊆ker(tr)=T|_{T_0}`. Two rank-2 subbundles, inclusion: the quotient is a torsion sheaf on a smooth curve, and is a subsheaf of `A_0/n≅O_{T_0}`, which is torsion-free, hence the quotient is zero. **HOLDS.** This is the step S3F asked to have attacked; the missing word is “torsion-free”, not a missing argument.

**(C) Filtration.** Generically along `T_0` the fibre is Gorenstein (`Φ|_{T_0}≢0`), so `n^2` is generically rank 1. Saturation `N` of `n^2` in `n` is a line subbundle; `Q=n/N` is a line bundle. The product `n·N` vanishes generically (`n·n^2=n^3=0` and `N` agrees with `n^2` off a finite set) and sits in the torsion-free sheaf `n`, hence is zero. Multiplication therefore factors as a nonzero map of line bundles `Q^{⊗2}→n^2⊆N`, injective, cokernel of finite length `m'`. Degrees: `deg N=2 deg Q+m'`, `deg det n=3 deg Q+m'`. With `det n=O(−k_0)` one has `−k_0=3 deg Q+m'`, i.e. `k_0+m'≡0 (mod 3)`. **HOLDS.** Completing note (S3F §6): if `Φ(p)=0` at `p∈T_0\setminus S_π` then `a,b,c,d∈m_p`, so `A,B,C∈m_p^2` and `mult_p(B^2−4AC)≥4`, contradicting multiplicity 2 along `T_π\setminus S_π`. Thus `m'` is supported in `T_0∩S_π={P}`, and `m'=m` once the local identification is made. **HOLDS.**

**(D) Cube and frame.** Total ramification ⇔ local algebra ⇔ Hessian vanishing ⇔ `A=B=C=0` on `T_0`. By (2.3) the polarised cubic is a perfect cube over the function field: `Φ|_{T_0}=ρ·ℓ^3`. Over the DVR at `P`, “primitive” means the two coefficients of `ℓ` generate the unit ideal, so `ℓ(P)≠0` and `ℓ` completes to a holomorphic frame of `T` at `P`. After that change, Miranda coefficients satisfy `a=c=d=0`, `b=−ρ`, with `ord_P ρ=m`. The polarised cubic and the Miranda 4-tuple *agree* on `T_0` (middle coefficients already zero); off `T_0` they differ by units `3` on the middle slots. Vanishing orders in §2.4 are insensitive to that. **HOLDS**, with that notation repair.

**(E) Restricted multiplication.** Shirane 1.1.3, `A=B=C=0`, `a=c=d=0`, `b=−ρ`: `z^2=−ρ w`, `zw=0`, `w^2=0`. Then `n=⟨z,w⟩`, `n^2=⟨ρ w⟩`, `N=⟨w⟩`, `Q=⟨z̄⟩`, and `Q^{⊗2}→N` is multiplication by `−ρ`, cokernel length `ord ρ=m`. So `m'=m`. **HOLDS.**

**(F) Gorenstein dictionary.** `ρ(P)≠0`: `w=−z^2/ρ`, algebra `C[z]/(z^3)`, curvilinear, Gorenstein. `ρ(P)=0`: `C[z,w]/(z,w)^2`, socle 2-dimensional, not Gorenstein. For finite flat `A→B` with `A` regular of dimension 2, `B` is Gorenstein iff the fibre algebra is. The witness `z^2=yw`, `zw=yt`, `w^2=tz` is the cone over the twisted cubic, the standard normal non-Gorenstein triple point. **HOLDS.**

**(G) Specialisation and (2.8)–(2.11).** On `P^2`, `det T≅O(−k)` with `2k=deg Δ̄=4g+2`, so `k=2g+1`. Restriction to a line does not see jumping: `k_0=k`. Thus `3∣(2g+1+m)`, equivalently `m≡g+2 (mod 3)`. **HOLDS.**

Infinity chart: SK:102–105 and d1-degree-bound:60–64 give `(ord v, ord u)=(a,d)=(g,4g)` at the unique place. In `(y,σ)=(Y/X,Z/X)` this is `(s^g u_1, s^{4g} u_2)` with units, tangent `L_∞={σ=0}`. The `g` Puiseux series `σ_j(y)` all have `ord_y=4` and the *same* leading coefficient (`s↦ζs` multiplies `σ` by `ζ^{4g}=1`). Weierstrass `f=unit·∏(σ−σ_j)` then gives S3F (2.8): `ord_σ f(0,σ)=g`, `ord_y f(y,0)=4g`, and `ord_y(∂f/∂σ)|_{σ=0}=4(g−1)` because `∑_{k}∏_{i≠k}σ_i` has leading coefficient `g·(lc)^{g−1}` with `g≠0`. The `∂unit` term against `f(y,0)` has order `≥4g>4(g−1)` and does not cancel. **HOLDS.** This is the other step S3F flagged.

Write `Φ=ρ(y) X^3+σ·η'` in the adapted frame, `η'=∑ α_i X^{3−i}Y^i`, `α_i∈C{y,σ}`, `ord_y ρ=m`. Classical disc expansion along the triple-root locus is the polynomial identity

```text
disc = −27 ρ^2 σ^2 α_3^2 + ρ σ^3 t(η') + σ^4 disc(η'),
t(η') = −4α_2^3 − 54 α_0 α_3^2 + 18 α_1 α_2 α_3.
```

Hand substitution of `(ρ+σ α_0, σ α_1, σ α_2, σ α_3)` into the classical discriminant confirms (2.9). Miranda’s local equation is `B^2−4AC`; (2.3) identifies its disc with `−27` times that, so `disc=unit·f·σ^2`. Divide: (2.10). Reading (a) at `σ=0`: `2m+2γ=4g` with `γ:=ord_y α_3(y,0)`. Neither `ρ` nor `α_3(y,0)` can vanish identically (`f(y,0)` has finite order `4g`), so `0≤m≤2g`. **HOLDS.**

**(H) Proposition TB-2.** From (2.7) and (2.11) at `g=2`: `m≡1 (mod 3)` and `m∈{0,1,2,3,4}`, hence `m∈{1,4}`. Assume `m≤3`, so `m=1` and `γ=3≥1`. Reading (c): left side `ord_y=4`; first right-hand term `≥m+4≥5`; no cancellation, so `ord_y(ρ t_0)=4`, hence `ord t_0=γ≥1`, so `t(η')(0,0)=0`. Then `α_3(0,0)=0` reduces `t` to `−4α_2(0,0)^3`, so `α_2(0,0)=0`. Every monomial of `disc(η')` contains `α_2` or `α_3`, so `disc(η')(0,0)=0`. Reading (b) at `g=2` (uses `m≥1`) says `ord_σ disc(η')(0,σ)=0`, i.e. that value is nonzero. Contradiction. Thus `m=4`. **HOLDS.**

At `g≥3`, (2.12) *requires* `disc(η')(0,0)=0`, and the first term of (c) is no longer strictly heavier than the left side. S3F’s scope statement is honest: the leading `σ`-jets do not kill `g≥3`, and the next layer needs characteristic exponents `β_i≥d`, which the row gauge does not pin. Not a hole in a claimed theorem.

Sanity (i)–(iv) are consistency checks, not load-bearing. Cyclic covers and the split Weierstrass family `(deg S, deg T)=(6e−2,1)` (nonempty at `e=1` by Tokunaga/Yasumura, Shirane Remark 0.5) confirm that `m=0` is realised and that `m≢0` is realised (cone over the twisted cubic). The naive identity `k=3Γ^2` is correctly refused: `π^*L_∞=3Γ` would give `Γ^2=1/3`, so `Γ` is not Cartier and the correction *is* `m`. Floor/attainment, not a competing proof.

## 5. Mixed-branching analysis (branch degree 4g+1 and the Z/3 component at L_inf)

**Existence of `Z→P^2`.** SK-5 (CONFIRMED at REV §3.2) puts `Π` a 3-cycle. Identify `Π` with the `φ`-image of a meridian of `L_∞`: a generic compactified line `{x=c}` meets `L_∞` transversely at `[0:1:0]` (not at `P_∞`), and the large circle in that affine line is a small circle about that point, hence a meridian of the divisor `L_∞`. On that `P^1` the product of all meridians is 1, so the infinity meridian is `Π^{±1}` up to conjugacy. Cycle type is insensitive to the inverse. This is the same identification REV already uses when it equates `Π∈V_4` with descent. Then `ρ:=ψ∘φ: π_1(P^2−(D̄∪L_∞))↠S_3` is surjective (`φ` onto `S_4`, `ψ: S_4↠S_4/V_4≅S_3` onto). Riemann existence / Grauert–Remmert supplies a finite étale cover of the complement; normalisation in the degree-3 subextension attached to a point stabiliser `S_2<S_3` (equivalently `D_8<S_4`) yields a connected normal surface `Z` finite over `P^2`. Shirane Remark 0.2: normal surface singularities are Cohen–Macaulay, and a finite surjective morphism from a normal surface to a smooth surface is a normal cover (finite flat). Transitivity of `S_3` on three letters gives irreducibility. Purity of the branch locus puts all ramification in `D̄∪L_∞`.

**Inertia.** A transposition of `S_4` acts on the three pairings as a transposition, cycle type `(2,1)` on the sheets of `Z`: simple branch, index 2, so `D̄≤S_π`. A 3-cycle of `S_4` maps to a 3-cycle of `S_3`, acting as a 3-cycle on the three cosets of `S_2`: total branch, index 3, so `L_∞≤T_π`. `D̄` is irreducible and distinct from `L_∞`, so equality in S3F (2.1): `S_π=D̄`, `T_π=L_∞`, `Δ̄=D̄+2L_∞`. The `Z/3` component at `L_∞` is exactly SK-5, rewritten geometrically. **ESTABLISHED.**

**Parity horn.** The *reduced* branch `D̄∪L_∞` has degree `4g+1`, which is odd. The divisor that carries Miranda’s class is the weighted one. Shirane 1.1.5, quoting Miranda Lemma 4.5 and Prop. 4.7: `Δ̄` is locally `B^2−4AC=0` and lies in `|(det T)^{-2}|`. Local discriminants: simple branch `(t^2−u)(t−c)` has `disc` of order 1 in `u`; total branch `t^3−u` has `disc=−27u^2`, order 2. Hence `deg Δ̄=4g+2=2k` with `k=−deg det T=2g+1`. Even, as it must be. The odd number `4g+1` is not the invariant the structure theory constrains. **Parity horn REFUTED.**

The same arithmetic recovers the sign rule `sgn(Π)=(−1)^d` (Theorem A(2), not used as input): `Π∈V_4` gives `Δ̄=D̄` and `d` even; `Π` a transposition or 4-cycle gives `Δ̄=D̄+L_∞` and `d` odd; `Π` a 3-cycle gives `Δ̄=D̄+2L_∞` and `d` even. Route 1 does not contradict A(2). For family 3, `d=4g` is even and `Π` is a 3-cycle, consistent.

**What SK-5 actually forbids.** A triple cover of `P^2` branched *only* in `D̄`. That object does not exist on the non-constant stratum, and the original NO-TORUS/Shirane-at-degree-6 attack remains closed, for the reason REV gave. The mixed cover is a different object. Conflating the two is the wording error in SK §4.2 / REV §3.2 / REV §7.

## 6. The m=0 case

TB specialised: `m=0` iff `Φ(P_∞)≠0` iff the resolvent cover is Gorenstein over `P_∞`. Then `3∣(2g+1)`, so `g≡1 (mod 3)`, i.e. `d≡4 (mod 6)`. Dead under this hypothesis: `(8,6)`, `(12,9)`, `(20,15)`, `(24,18)`, `(32,24)`, … Survivors: `(16,12)`, `(28,21)`, `(40,30)`, …. **The implication HOLDS. The hypothesis is not proved in general, and at `g=2` it is disproved:** TB-2 forces `m=4≠0`, so the `m=0` kill does not fire on `(8,6)`. Listing `(8,6)` among the `m=0`-dead rows (S3F §2.5) is the conditional list, not an unconditional kill. The table at S3F §5 is the accurate one.

Degree-general form, not using the `(4,3)` shape: if `Π` is a 3-cycle and the resolvent is Gorenstein over `P_∞`, then `deg Δ̄=d+2=2k` and `3∣k`, so `d≡4 (mod 6)`. This sharpens Theorem A(3)’s first horn (`ord(Π)=3`, `3∣n`, `d` even) by one more modulus. Coprime `(4,3)` itself has `d=4≡4 (mod 6)`, so the sharpening does not kill it — correctly, since that row dies by the `B`/`C` half of the coprime theorem, not by A. **COROLLARY ESTABLISHED, still conditional on `m=0`.**

Weierstrass split `T≅L^{-1}⊕L^{-2}`, `L=O(e)`, forces `k=3e` and, in Weierstrass form, leading coefficient 1, so `Φ|_{any\ line}` has a nonvanishing `X^3` term and `m=0`. Thus splitting is *sufficient* for the `m=0` branch (S3F sanity (ii)–(iii)). It is not necessary: TB applies to non-split Tschirnhausen modules (Shirane Cor. 2.3 already exhibits `Ω_{P^2}` at weighted degree 6). Arbitrary split `O(a)⊕O(b)` with `a+b=−k` only recovers the already-known `deg Δ̄=2k`; it does not give divisibility by 6 (REV §7, still right).

Constant stratum, recorded for the ledger not as a new kill: `Π=c^4`. For `g` odd, `c` is odd in `S_4`, hence a transposition or a 4-cycle, and `c^4=1∈V_4`. (S3F’s reason “`c` odd so `c^4=1`” is the classification of odd elements, not a general fact about odd permutations.) For `g` even, `c∈A_4`, and `c^4` is a 3-cycle iff `c` is a 3-cycle (`c=1` also satisfies `c^4=c`, but then `Π=1∈V_4`). On those 3-cycle configurations TB applies; `m=0` would kill even `g≢1 (mod 3)`. Residual constant configurations have `Π∈V_4`, TB is silent, and the *original* (descended) Tschirnhaus OPEN is the lever — as REV said for that case.

Route 2 remains vacuous at `(4,3)`: SK-5, `3∣n'=3`, and `d'` even are identities of the shape; `A'(3)` is `Π^3∈Z(H)`, empty once `ord(Π)=3`. Inner-cable `e(ι)=4g−1+2δ_{\mathrm{aff}}−9g^2` is one linear condition, not a census. Filling it by analogy with `(4,2)` would be a FALLACY-v2 cap. S3F correctly refuses.

## 7. Adjudication: OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT] as a sufficient lever

Three objects have been named by the same OPEN. They must be kept apart. `FALLACY-v2` flag/place: do not identify a cv flag, a physical place, and a cover series.

**Typing A (as in SK, REV §7, Coord:49–50, and the web-sweep target).** The *descended* `S_3`-resolvent of `P^2` branched only along `D̄`, and the question whether its Tschirnhausen module is Weierstrass `O(−e)⊕O(−2e)`. Payoff, if yes: `6∣d`.

On the non-constant stratum this object does not exist (SK-5: `Π` is a 3-cycle, not in `V_4`). A yes-answer cannot fire. Coord:49–50 (“which would close family 3 if resolved”) is false at this typing. REV §7’s *conclusion* — the then-typed OPEN does not close family 3’s non-constant stratum — is **right**. REV’s *reason* — “there is no triple cover of `P^2` to apply it to” — is **wrong as a blanket existence claim**. The correct restriction, which S3F supplies, is: no triple cover branched **only** in `D̄`.

**Typing B (S3F’s retarget).** The *mixed* cover of §5, same Weierstrass question. Payoff, if yes: `k=3e=2g+1`, hence `g≡1 (mod 3)`, i.e. `6∣d+2` not `6∣d`. Applying the Typing-A payoff `6∣d` to a 3-cycle stratum would be a flag/place conflation of reduced and weighted branch, as S3F says.

This is a sufficient condition for the `m=0` branch of TB, never a competing one. It does **not** close family 3: the rows with `g≡1 (mod 3)` survive a yes-answer. It is already answered **NO** on every non-constant row with `g≢1 (mod 3)`, because `k=2g+1` is not divisible by 3; Weierstrass is arithmetically impossible there (e.g. `g=2`, `k=5`). A yes-answer can therefore kill only rows on which a yes-answer is already impossible. As a *hypothetical extra geometric theorem* (“every mixed `(deg S, deg T)=(4g,1)` cover is Weierstrass”), it would kill `g≢1 (mod 3)` and nothing else — the same arithmetic TB’s `m=0` branch already names, without proving `m=0`. That is a sufficient lever in the sense of a research programme, not a present kill, and not a reversal of REV’s conclusion about Typing A.

**Typing C (Coord as written).** “Tschirnhaus-splitting would close family 3.” False on A (wrong object on the non-constant stratum; on the constant/`Π∈V_4` stratum a yes-answer gives `6∣4g` i.e. `3∣g`, not a uniform close). False on B (the `g≡1 (mod 3)` non-constant rows survive, as does every constant `Π∈V_4` configuration to which B does not apply). Coord is not “nearer right than REV”. Coord overclaimed; REV caught the overclaim at Typing A and then overspoke the supporting geometry.

**Who is right, at exactly what scope.**

| Claim | Who | Scope |
|---|---|---|
| Mixed cover `Z→P^2` branched at `D̄∪L_∞` exists | **S3F** | non-constant family 3, every `g≥2` |
| “There is no triple cover of `P^2` to apply it to” | **REV/SK, false as written** | correct repair: no cover branched *only* in `D̄` |
| Typing-A OPEN does not close non-constant family 3 | **REV** | the OPEN as then typed |
| Typing-A payoff `6∣d` is the wrong modulus on a 3-cycle stratum | **S3F** | use `6∣d+2` for mixed covers |
| Typing B is sufficient for `m=0` / `g≡1 (mod 3)` | **S3F**, as a hypothetical | does not prove splitting; already NO when `g≢1 (mod 3)` |
| Coord:49–50 closes family 3 | **neither**; claim false | all typings |
| S3F “REV §7 Refuted” | **overclaim** | wording of REV is repaired; REV’s conclusion on Typing A stands |

The honest correction is a *retarget*, not a reversal. Keep `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` OPEN, with the object named: descended (Typing A: family-2 `g=2` survivors and family-3 constant `Π∈V_4`) versus mixed (Typing B: sufficient for TB’s `m=0` branch, payoff `d≡4 (mod 6)`). Do not consume it. Do not promote “splitting closes family 3”.

## 8. Family-3 ledger audit

REV §8 residual shapes in a `d_min` gauge, family-3 rows only:

3. `(4,3)`, `g=2` non-constant — `(8,6)` AM-numerical types; one `φ`-orbit of outer data.
4. `(4,3)`, `g≥3` — both strata, including `(12,9)`, `(16,12)`, …. Name: `OPEN[SHAPE-3-ALL-g]`.

Constant `g=2` was already dead (SK-2' filters, REV §3.3). Family 2 is untouched by TB (`Π∈V_4` at `g=2` by SK (3.3); `T_π=0`; TB vacuous). That structural split between `OPEN[SHAPE-2-INFINITY-Z3]` and the present lane is correct.

S3F’s increment, all established in §§4–6:

| Row class | Unconditional | Conditional on `m=0` | Status |
|---|---|---|---|
| Non-constant, every `g≥2` | `Π` a 3-cycle (SK-5); mixed cover exists; `m≡g+2 (mod 3)`, `0≤m≤2g` | `g≡1 (mod 3)` | family thinned, not killed |
| `g=2` non-constant `(8,6)` | `m=4` exactly (TB-2) | hypothesis `m=0` is false | outer orbit still lives; residual is `OPEN[S3-TB-G2]` |
| `g=3` `(12,9)` | `m∈{2,5}` | would die | OPEN |
| `g=4` `(16,12)` | `m∈{0,3,6}` | survives (`4≡1 (mod 3)`) | OPEN; the first `m=0`-compatible row |
| Constant, `g` odd | `Π=1∈V_4`; TB silent | Typing-A split would give `3∣g` | original OPEN only |
| Constant, `g` even, `c` a 3-cycle | TB applies | would die unless `g≡1 (mod 3)` | `g=2` already dead by SK-2' |
| Constant, `g` even, `c` not a 3-cycle | `Π∈V_4`; TB silent | Typing A | original OPEN only |

`OPEN[SHAPE-3-ALL-g]` remains **NECESSARY**. It is no longer “the whole family with no inner arithmetic”. It is: the congruence plus a single integer `m` at `P_∞`, pinned at `g=2`, unpinned at `g≥3`, with Gorenstein-ness the named switch. Not a finite list. The `d_min` obligation of `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` still stands over REV’s items 1–4; S3F does not shrink the cage to a bound, and correctly does not claim to.

S3F’s named successors, retyped:

1. `OPEN[S3-TB-M0]` / `OPEN[S3-RESOLVENT-GORENSTEIN-AT-P-INF]`: is `m=0`? Highest value; also makes the A(3) sharpening unconditional. **KEEP OPEN.**
2. `OPEN[S3-TB-G2]`: kill `m=4` at `g=2`. Local data fully named (`ord_y ρ=4`, `γ=0`, germ of type `A_8` in the stated gauge). Leading jets exhausted. **KEEP OPEN.**
3. `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]`, two objects (§7). **KEEP OPEN**; do not consume; do not promote as a family-3 closer.
4. Unchanged: `OPEN[SHAPE-2-INNER-g>=3]`, `OPEN[SHAPE-2-INFINITY-Z3]`, `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`.

Dead ends S3F records (RH genera `2g−1`, `2g−2`, `24g−15` integral; `Γ^2=1/3`; Tokunaga class on the double plane already divisible by 3) are correctly refused. Not re-run.

Ciliberto–Miranda arXiv:2512.07965v1 classifies normal *non-cyclic* triple planes with weighted branch degree `≤10`, hence includes `g=2` (`deg Δ̄=10`), with completeness failing at one `p_g=0,q=1` slot. Not consumed by S3F, not consumed here, not a safe close of `OPEN[S3-TB-G2]`. Pointer only.

## 9. FALLACY-v2 flags

- **Flag/place/series.** S3F itself flags the reduced-versus-weighted conflation in SK’s `6∣d` payoff. The reversal overclaim in S3F §4 correction 2 is the dual error: identifying Typing A (descended cover, the flag REV ruled on) with Typing B (mixed cover, a different series). §7 separates them.
- **Floor/attainment.** `k=3Γ^2` is refused (`Γ^2=1/3`). The bound `0≤m≤2g` is not treated as pinning `m`. TB-2 is an exact computation, not a floor. Conditional `m=0 ⇒ g≡1 (mod 3)` is not sold as an unconditional kill. Clean.
- **Carrier/attainment.** No residual curve is asserted. Outer `(8,6)` orbit remains outer data, as in REV. Clean.
- **Pole/interior.** Infinity-chart orders are the row-gauge place `(a,d)=(g,4g)`, not a polar identity used off its vertex class. The meridian of `L_∞` is taken at `[0:1:0]`, the generic point of the line, not at `P_∞`. Clean.
- **`sat()` / raw remainder / variable-ring map.** No computer algebra. Disc identities (2.3) and (2.9) were re-expanded by hand.
- **Prime label/derivative.** `∂/∂σ` is an actual derivative of a local equation. The unit-product expansion of `∂(unit·f)/∂σ` at `σ=0` is dominated by `unit·∂f/∂σ` (order `4(g−1)` versus `≥4g`). S3F skipped writing that comparison; it holds.
- **Merge-free / target-arrival.** Not in play.
- **Per-ray/exit-set.** No exit price is asserted. No `charge_basis` line, as required.

No gap was filled by cap or analogy. Route 2, `g≥3` jets, and Ciliberto–Miranda at degree 10 are left OPEN.

## 10. Promotion recommendation and residual OPEN items

| Item | Recommendation | Scope |
|---|---|---|
| Mixed cover `Z→P^2`, `S_π=D̄`, `T_π=L_∞` | **PROMOTE** | non-constant family 3, every `g≥2` |
| Parity horn `4g+1` odd | **PROMOTE the refutation** | weighted degree `4g+2` even; `k=2g+1` |
| THEOREM TB | **PROMOTE** | as stated: one rational total-branch curve, one meeting point |
| `m≡g+2 (mod 3)`, `0≤m≤2g` | **PROMOTE** | non-constant family 3 |
| `m=0 ⇒ g≡1 (mod 3)` / `d≡4 (mod 6)` | **PROMOTE as conditional** | not `m=0` itself |
| Prop. TB-2, `m=4` at `g=2` | **PROMOTE** | `(8,6)` non-constant; not a row kill |
| A(3) sharpened to `d≡4 (mod 6)` | **PROMOTE as conditional** | `ord(Π)=3` and Gorenstein over `P_∞` |
| Route 2 at `(4,3)` | **PROMOTE as vacuous** | fork entered, not exited |
| REV/SK wording “no triple cover of `P^2`” | **PROMOTE the repair** | “no cover branched only in `D̄`” |
| Typing-B split as sufficient for `m=0` | **PROMOTE as a hypothetical** | already NO when `g≢1 (mod 3)` |
| Uniform kill of family 3 | **DO NOT PROMOTE** | not obtained |
| Existence of any surviving residual curve | **DO NOT PROMOTE** | not asserted |
| “REV §7 Refuted” / “Coord nearer right” | **DO NOT PROMOTE** | §7 scope split; Coord:49–50 still false |
| “Tschirnhaus closes family 3” | **DO NOT PROMOTE** | false on every typing |
| `6∣d` from Cardano/split without Weierstrass and without naming the cover | **DO NOT PROMOTE** | REV §7 still right on that |
| `OPEN[SHAPE-3-ALL-g]` | **KEEP OPEN** | necessary; thinned, not finite |
| `OPEN[S3-TB-M0]` | **KEEP OPEN** | named local integer |
| `OPEN[S3-TB-G2]` | **KEEP OPEN** | finish `(8,6)` |
| `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` | **KEEP OPEN** | two objects, §7; do not consume |
| `OPEN[SHAPE-2-INNER-g>=3]`, `OPEN[SHAPE-2-INFINITY-Z3]`, `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` | **KEEP OPEN** | untouched |

Default refutation did not break TB, TB-2, the mixed cover, or the congruence. It broke the advertised reversal as a *refutation of REV’s conclusion*, and it broke Coord:49–50 on every reading. Promote the theorems; keep the OPENs; do not promote a family-3 close.

Ciliberto–Miranda 2512.07965v1 remains an unconsumed pointer at weighted degree 10 (`g=2`), completeness failing at one slot. Using it to close `OPEN[S3-TB-G2]` would be a new lane, not a repair of S3F.

Nothing above is an exit-price assertion. SK-1, SK-4, SK-5, the `g=2` constant kills, and the narrowed cage of REV §8 stand as previously reviewed. Family 2 is not touched. The `(8,6)` non-constant outer orbit remains outer data with a pinned local integer `m=4`, not a residual curve.

<!-- BODY-END -->

