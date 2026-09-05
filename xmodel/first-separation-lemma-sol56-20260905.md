# First separation and route-to-state for Moh data

**Lane:** `first-separation-lemma-sol56-20260905`  
**Date:** 2026-09-05  
**Disposition:** `FIRST-SEPARATION = PROVED` after the hypotheses below are made explicit; `RADIUS-ROUTE-TO-STATE = PROVED` for a *realized, first-separation-decorated* datum; `ROUTE-TO-KILL-INSTRUMENT = OPEN` as a universal claim.

## 0. Custody and verdict

The seven charged inputs were read only from `/tmp/jc2-lane.QHjsXx/inputs`. A checksum manifest generated mechanically from the receipt's `charged_input_<i>_sha256=` and `_basename=` fields was checked with `sha256sum -c`; all seven entries returned `OK`. The manifest is `/tmp/first-separation-lemma.manifest`. No ledger, `jc2-lean`, or `ideation-*` file was edited.

There are two source corrections which prevent promotion of the requested statement verbatim.

1. Moh's theorem on printed p. 200 has hypotheses/conclusions numbered **(1)–(7)**. After its proof, Moh starts a different list for his degree-`≤100` search, numbered **(1)–(13)** across pp. 200–201. Item (1) literally contains `n≤100`, and item (6) contains `s≤5`. Consequently Moh does not prove that an all-degree minimal counterexample satisfies the literal p. 200–201 list (1)–(13).
2. The frozen evidence proves a three-way *state* classifier, not a universal map to three proved kill instruments. In particular, Xu's Corollary 7.5 excludes only a full `u_s`-distinct-root split below a strict cutoff; the receiver atlas explicitly leaves 296 complementary split obligations `UNASSIGNED`, and a general licensed descendant need not have the special `k=4`-ray shape.

The safe result is therefore:

```text
minimal non-coordinate Keller pair
        |
        |  First-Separation Lemma
        v
Moh p.194 two-point datum, M_s=n-2, u_s>=1
        |
        |  realized minor first-separation radius rho
        +-- u_s=1 --------------------> D1: licensed monomial descent
        +-- u_s>=2, rho<v_s/u_s ------> ES: typed early-split obligation
        `-- u_s>=2, rho>=v_s/u_s -----> D2: licensed monomial descent
```

These leaves are exclusive and exhaustive for an actual realization. The further arrows to `(T)`, a joint chart, and a `k=4` ray are not universal theorems in the frozen record. First Separation closes the one-point-at-infinity leak, but the claimed all-degree reduction is not yet complete.

## 1. Notation and source discipline

Work over an algebraically closed field `k` of characteristic zero, as Moh does throughout [Moh83, p. 140 (PDF p. 1)](../refs/moh1983_jram340_configurations_of_roots.pdf). A **Keller pair** is `(f,g)∈k[x,y]^2` with `J(f,g)∈k*`. It is **non-coordinate** when `k[f,g]⊊k[x,y]`. A minimal counterexample means a non-coordinate Keller pair minimizing `deg f+deg g`; such a pair cannot be carried by a source automorphism to another pair having both degrees strictly smaller, because source automorphisms preserve the Keller property and preserve properness of the generated subalgebra.

After a generic linear source change, orient the pair so that

```text
deg g = deg_y g = n > 1,       deg f = deg_y f = m,
```

with both polynomials monic in `y`. Use Moh's characteristic data `(M_i,d_i)`, the effective terminal index `s`, and a major-disc tower with integers `V_i`. Put

```text
d_s = gcd(n,M_1,...,M_{s-1}),   v_s=V_s,   u_s=d_s-v_s.
```

The first approximate root is `T_1^ψ`. Moh's Proposition 2.2 gives `T_1^ψ=f+` a polynomial in `g`; replacing `f` by it preserves `k[f,g]` and the Jacobian. See `prop54-minimality-opus5-20260905.md:152–176`.

Two radii must remain distinct.

- `δ`, below, is the logarithmic radius of the smallest disc containing all roots of `g(y)T_1^ψ(y)`. This is the p. 183/Lemma 5.3 radius which detects the first separation into points at infinity.
- `ρ:=δ^*_{s-1}` is the logarithmic radius of the *minor disc inside the terminal major disc*. Moh defines it as a minimum of pairwise root-contact orders on p. 191. It is the later, minor-cluster first-separation radius used by Propositions 6.3 and 6.4.

Neither is a physical place, and neither is identified with a probe merely because two orders agree (`FALLACY-v2.md:5–6`).

## 2. Lemma A — First Separation

### Citable statement

**Lemma A (First Separation).** Let `(f,g)` be a normalized, non-coordinate plane Keller pair with `deg g=deg_y g=n>1`. Assume no automorphism of `k[x,y]` simultaneously lowers `deg f` and `deg g`. In particular, the assumption holds for a counterexample of minimal `deg f+deg g`. Then the smallest disc containing all roots of `g(y)T_1^ψ(y)` has logarithmic radius `−1`, and Moh's characteristic data satisfy

\[
M_s=n-2,
\qquad d_s>v_s>\frac{d_s}{2},
\qquad u_s=d_s-v_s\in\mathbb Z_{>0}.
\]

For two distinct constants `a≠b`, the top homogeneous form of `g` is

\[
g_n(x,y)=
\left[(y-ax)^{v_s}(y-bx)^{u_s}\right]^{n/d_s}.
\tag{FS}
\]

Thus `g=0` has exactly two distinct points—not necessarily two places—on the line at infinity, and `v_s>u_s≥1`. The pair is in Moh's p. 194 setup and under his general tower theorem on p. 200.

If, in addition, `n≤100` and one adopts all the bounded-search normalizations Moh states after that theorem, the datum is subject to Moh's separate p. 200–201 restrictions (1)–(13). Without `n≤100`, Lemma A does **not** assert the literal list (1)–(13), nor membership in a particular computed campaign census.

### Proof

**Step 1: the radius cannot be below `−1`.** For either normalized monic polynomial `g` or `T_1^ψ` (whose total degree equals its `y`-degree in this setup), write

\[
g(x,y)=y^n+a_1(x)y^{n-1}+\cdots+a_n(x),
\qquad \deg a_j\le j,
\]

and put `x=t^{-1}`. If a Puiseux root `τ` had `ord_t τ=α<−1`, then `y^n` evaluated at `τ` would have order `nα`, while every other term would have order at least

\[
-j+(n-j)\alpha=n\alpha-j(1+\alpha)>n\alpha.
\]

The unique lowest-order term could not cancel. Hence every root of `gT_1^ψ` has order at least `−1`; every root difference has order at least `−1`, so `δ≥−1`. This index-free Newton-polygon delta is promoted at `prop54-minimality-opus5-20260905.md:138–148`.

The same conclusion is visible in Moh's tower notation. Proposition 5.4 identifies the relevant index

\[
i=\max\{r:V_{r+1}d_r/d_{r+1}>V_r\}
\]

and its proof computes

\[
\delta_i=-\frac1{n-M_i-1}.
\]

Since `M_i≤M_s≤n−2`, this is at least `−1`; see [Moh83, p. 183](../refs/moh1983_jram340_configurations_of_roots.pdf) and `prop54-minimality-opus5-20260905.md:120–136`. The elementary proof avoids the empty-maximum presentation seam.

**Step 2: the radius cannot be above `−1`.** Proposition 5.4 says that if this smallest-disc radius is greater than `−1`, then either

\[
k[x,y]=k[T_1^\psi,g]=k[f,g],
\]

or an automorphism simultaneously reduces the degrees of `T_1^ψ(f,g)`, `g`, and `f`; this is printed on [Moh83, p. 183](../refs/moh1983_jram340_configurations_of_roots.pdf), with the degree-reducing automorphism completed on p. 185. The first alternative contradicts the non-coordinate hypothesis; the second contradicts non-simultaneous reducibility. Hence `δ≤−1`. Together with Step 1, `δ=−1`.

**Step 3: convert radius to characteristic and projective data.** Lemma 5.3 states that the smallest-disc radius is `−1` if and only if `M_s=n−2` and the highest homogeneous form of `g` has two roots, one having multiplicity `(n/d_s)v_s`, with

\[
d_s>v_s>d_s/2.
\]

This is printed on [Moh83, pp. 185–186](../refs/moh1983_jram340_configurations_of_roots.pdf). Since `u_s=d_s-v_s`, `0<u_s<v_s`. Moh writes (FS), with exponent `n/d_s` and `a≠b`, on [p. 194](../refs/moh1983_jram340_configurations_of_roots.pdf). Its linear factors give exactly two projective points. ∎

### Why minimality is enough

If a counterexample exists, choose one minimizing `deg f+deg g`. For a source automorphism `φ`,

\[
J(f\circ\phi,g\circ\phi)
=(J(f,g)\circ\phi)\det J(\phi)\in k^*,
\]

and `k[f∘φ,g∘φ]=φ^*(k[f,g])` stays proper. A simultaneous degree drop gives a smaller counterexample. See `prop54-minimality-opus5-20260905.md:154–184`. An arbitrary Keller pair is insufficient because Proposition 5.4 retains the coordinate alternative.

## 3. What “(1)–(13)” can safely mean

There are two lists on p. 200, and they must not be merged.

**Moh's general theorem.** Hypotheses (1)–(3) give degrees, characteristic data, and `M_s` largest `≤n−2`. Conclusions (4)–(7) construct towers for every `r≥2`, classify the subdiscs by root count, bound their number, and guarantee a major continuation. See [Moh83, p. 200](../refs/moh1983_jram340_configurations_of_roots.pdf). Lemma A supplies `M_s=n−2`.

**Moh's bounded search.** After the theorem's proof, the numbering restarts. In compact notation, pp. 200–201 require or derive:

1. `m=−M_1<n≤100`;
2. `m∤n` and `M_s=n−2`;
3. `J(f,g)=1` and no simultaneous degree reduction;
4. the displayed `M` sequence is the indicated initial part of the characteristic data (the printed phrase “less than `n−2`” sits uneasily beside item 2 and is not repaired here);
5. `d_r=gcd(n,M_1,...,M_{r-1})`;
6. `3≤s≤5` and `d_s≥4`;
7. `V_{r+1}d_r/d_{r+1}≥V_r>d_r/(n−M_r)`;
8. radii are computed by Definition 5.1 and denominator increments `A_{r-1}` are defined;
9. the Euclidean division `V_r(d_{r-1}/d_r)=Δ_{r-1}A_{r-1}+R_{r-1}`;
10. the stated bound `V_{r-1}≤Δ_{r-1}` for a nonzero linear factor;
11. alternatively `V_{r-1}=jA_{r-1}+R_{r-1}` for the zero factor;
12. at `r=2`, `A_1 | (n/d_2)V_2` and `A_1 | (m/d_2)V_2−1`; or
13. the symmetric divisibilities with `m,n` exchanged.

See [Moh83, pp. 200–201](../refs/moh1983_jram340_configurations_of_roots.pdf). These are bounded-search restrictions, not an all-degree theorem; `s≤5` appears only after the `n≤100` search begins.

Accordingly:

> **OPEN[CENSUS-COVERAGE-ALL-DEGREE].** A cap-free analogue still needs a proof that it enumerates every datum admitted by Moh's general theorem. Lemma A and the “historical selected” 296-row atlas do not prove compiler coverage (`receiver-atlas-k1-astra-20260905.md:397–400`).

This is a citation-scope correction, not a defect in Lemma A.

## 4. Lemma B — the exhaustive pair-level radius route

### Citable statement

**Lemma B (Radius Route to State).** Let an *actual realization* of a p. 194 datum be given, and let `ρ=δ^*_{s-1}` be Moh's minor-disc first-separation radius. Define `R` by

\[
R:\quad \rho\ge \frac{v_s}{u_s}.
\]

Exactly one of the following states occurs:

| state | defining predicate | source-level consequence |
|---|---|---|
| `D1` | `u_s=1` | `R` holds by Proposition 6.4; Proposition 6.3 gives polynomial monomial-Jacobian descendants. |
| `ES` | `u_s≥2` and `ρ<v_s/u_s` | the minor cluster has a typed first separation in the early window; its common leading polynomial has `q≥2` distinct roots, `2≤q≤deg p≤u_s`, `deg p|u_s`, and `den(ρ)≤u_s`. |
| `D2` | `u_s≥2` and `ρ≥v_s/u_s` | `R` holds; Proposition 6.3 gives polynomial monomial-Jacobian descendants. |

For either descent state, put `θ=y^{-1}` and `γ=θ^{1/u_s}`. Proposition 6.3 supplies a truncation

\[
\sigma=\sum a_j\theta^j+\pi\theta^{v_s/u_s}
\]

such that `\bar g(σ),\bar T_1^ψ(σ),...,\bar T_{s-1}^ψ(σ)∈k[γ,π]`, are monic in `π`, and have `π`-degrees

\[
\frac{u_sn}{d_s},\quad
\frac{u_s(-\mu_1)}{d_s},\ldots,
\frac{u_s(-\mu_{s-1})}{d_s},
\]

with

\[
J_{\gamma,\pi}(\bar g(\sigma),\bar T_1^\psi(\sigma))
=-\frac{u_s}{b}\gamma^{\ell},
\qquad \ell=v_s-u_s-1.
\tag{MJ}
\]

The route is a function of the realized decorated datum `(M,d,V,s,u_s,v_s;ρ,p,partition)`. A bare integer skeleton `(M,d,V,s,u_s,v_s)` does not determine `ρ`, `p`, or the partition and therefore routes only to a finite set of obligations, not necessarily to one leaf.

### Proof and completeness

Lemma A gives `u_s≥1`, so exactly one of `u_s=1` and `u_s≥2` holds. In the first case Proposition 6.4 gives `ρ≥v_s`; Proposition 6.3 yields (MJ) and the degree conclusions. See [Moh83, pp. 197–199](../refs/moh1983_jram340_configurations_of_roots.pdf). This proves `D1`.

Now suppose `u_s≥2`. Trichotomy of the ordered rationals gives exactly one of `ρ<v_s/u_s` and `ρ≥v_s/u_s`. The latter is precisely Proposition 6.3's hypothesis and gives `D2`.

In the former case, Proposition 6.1 gives `ρ≥1` [Moh83, p. 191](../refs/moh1983_jram340_configurations_of_roots.pdf). The p. 194 leading form gives `ord g(σ)=(n/d_s)(u_sρ−v_s)<0`; Proposition 6.1 then makes `σ` a distribution detector. At the minimal radius, the leading polynomials are powers of a common `p`. The generalized Proposition 6.4 gcd is `u_s`, so `deg p|u_s`. Minimality of `ρ` forces at least two roots of `p`. Thus

\[
2\le q\le\deg p\le u_s.
\]

See the derived-source proof at `prop63-radius-gate-opus5-20260905.md:113–176`.

For the promoted denominator delta, the Galois-stable cluster shares its truncation below `ρ`. A Puiseux Galois generator multiplies each nonzero first-separation center by a root of unity of order `den(ρ)`. Its orbit has that size (remove a possible zero center), so `den(ρ)≤q≤u_s`. See `prop63-radius-gate-opus5-20260905.md:153–169`; Xu does not prove this general bound.

The three predicates are disjoint, and the two dichotomies used to form them are exhaustive. Equality `ρ=v_s/u_s` belongs to `D2`, exactly as the `≥` in Proposition 6.3 requires. The `ES` label means **first separation strictly below the descent threshold**; it does not mean that a cluster in `D1` or `D2` never splits later. This typed meaning prevents the strict-below/at-level conflation prohibited by FALLACY-v2. ∎

### Exact role of Xu Corollary 7.5

Xu defines split by more than one distinct leading root [Xu16, p. 1](../refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf). Under §7.3's extra hypotheses, Proposition 7.3 excludes order `1`. Corollary 7.5 proves only

\[
\text{a split into all }u_s\text{ distinct roots}
\quad\Longrightarrow\quad
\rho\ge\frac{v_s+1}{u_s+1},
\]

with a strict excluded side [Xu16, pp. 11–12](../refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf). It does not cover `2≤q<u_s` or equality. Xu leaves a possible `u_s=3`, `ρ=5/2` split open on p. 13 and only mentions, rather than proves, the denominator bound there.

Xu filters some `ES` obligations; it does not exhaust every window. Finiteness follows from the interval and denominator bound, while emptiness needs row-specific classification and kills. The frozen audit establishes exhaustion only for `D=108` and `(99,66)` S8/case A (`prop63-radius-gate-opus5-20260905.md:221–295`).

## 5. Why the requested instrument map is not yet a lemma

The source-level output of Lemma B is enough to define obligation states. It is not enough to identify the following target charts.

| desired adapter | status in the frozen record | exact issue |
|---|---|---|
| `D1 → descended order chart (T)` | `OPEN[DESCENDANT-RECEIVER-COVERAGE]` | Moh proves polynomial monomial-Jacobian descent, but not the campaign's coefficient-support chart. The round synthesis says the current `≤100` order chart still lacks an `h`-support lemma and omits 76 allowed coordinates in 8 of 12 fibres (`ideation-20260905T1200Z-synthesis.md:5–6`). |
| `ES → joint two-point chart` | `OPEN[SPLIT-TO-JOINT-MAP]` | A label is not a map. The frozen inputs relay joint-chart kills only for selected `(99,66)` B/C and `D=108,δ=3` branches (`prop63-radius-gate-opus5-20260905.md:322–349`); they do not give a chart, localization, or pullback certificate for every `(ρ,partition)`. |
| `D2 → k=4-ray unsplit chart` | false without extra predicates | Proposition 6.3 yields exponent `ℓ=v_s-u_s-1`, arbitrary descended degrees, and inherited depth. The selected atlas already contains `ℓ=0,...,8` (`receiver-atlas-k1-astra-20260905.md:397–415`), so licensed descendants are not all `ℓ=4`. “No early split” also does not force the `3:2`, two-level `k=4` ray. |

The `k=4` adapter is valid only after separately proving the special descendant shape—conventionally the two-level slice

\[
(n',m';M_2';V_2';\ell)
=(3K,2K;3K-6;K-1;4),
\]

plus every support/localization hypothesis of its unsplit-configuration lemma. The frozen radius report discusses only the finite `K=7,8,9` arms and warns that sixteen `(108,72)` ancestors descend to three-level charts rather than the killed two-level chart (`prop63-radius-gate-opus5-20260905.md:187–219, 432–436`). It cannot be used as a universal shape theorem.

Consequently the phrase “no split ⇒ radius discharged ⇒ descent” is safe only when “no split” means “the complete typed `ES` window for this row has been exhausted.” The further phrase “⇒ k=4 ray” needs an independent arithmetic shape theorem. Neither finiteness of the window nor absence of a split selected by Xu supplies those results.

## 6. Receiver-atlas reconciliation: the 296 obligations

The answer is **no**: the atlas's 296 `UNASSIGNED` split obligations are not already assigned joint charts by construction.

The frozen atlas distinguishes 296 source records from 132 coarse receiver keys. For every one of those 296 `u_s≥2` records it constructs a valid map to a *larger monomial receiver only on the licensed-descent branch*. The complementary branch is stored as `UNASSIGNED_SPLIT_OBLIGATION`; the atlas explicitly says these dispositions neither assert that all branches are realized nor kill any source (`receiver-atlas-k1-astra-20260905.md:13–20, 397–415, 435–465`). Its larger receivers have explicit rational points and are nonempty (`:286–297`), and its final discharged count is `0/1110`, including `0/671` advertised exponent-one clients (`:467–481`).

Set-theoretically, the 296 complements are the per-source slots which Lemma B labels `ES` if realized. Algebraically, they remain unassigned because no universal homomorphism from each typed split source chart to a necessary joint chart, and no certificate pullback, is supplied. Moreover, one source record may give several obligations indexed by `ρ` and the partition of the roots of `p`; `296` is not a count of realized splits or of joint charts. Retyping those rows as “assigned by construction” would contradict the atlas's proved interface statement.

The same atlas also rejects a proposed shortcut on the descent side. The literal forward-wedge receiver is empty, but the K16 source map fails because `[γπ^0]P=−g` is a scalar unit; therefore that receiver's unit certificate proves neither K16 nor `(T)` (`receiver-atlas-k1-astra-20260905.md:5–20, 299–395`). A valid state label cannot substitute for a necessary ring map.

## 7. Named “third configurations” and exact residual

The following are residual receiver/interface configurations *after* first separation; they are not third alternatives to the two points at infinity proved by Lemma A.

1. **U-NEGATIVE:** a descended row with `V'_2>d'_2`. The frozen minimality report preserves an unresolved internal disagreement over whether this is outside the earlier stratum or merely a per-row chart condition (`prop54-minimality-opus5-20260905.md:196–215, 295–298`). The safe classification is `OPEN[U-NEGATIVE-CHART]`; no geometric “third point” claim is made.
2. **Depth:** descended characteristic depth `s'>2`, which lies outside the two-level receiver/ray charts. In the current twelve-row residual, eleven rows have `s'=3` and one has `s'=4`, correcting the earlier shorthand “all `s'=3`” (`ideation-20260905T1200Z-synthesis.md:5–9`). This is `OPEN[DESCENT-STATE-S>2]`.

They must be named, but they are not the whole residual. The exact outstanding obligations are:

- `OPEN[CENSUS-COVERAGE-ALL-DEGREE]`: prove the cap-free census covers every Moh-admissible all-degree datum; literal p. 200–201 (1)–(13) cannot do this because it includes `n≤100` and `s≤5`.
- `OPEN[SKELETON-DECORATION]`: attach or enumerate the realized first-separation order, common leading polynomial, and root partition. A bare `(M,d,V,s,u_s,v_s)` is not a single-valued input to Lemma B.
- `OPEN[SPLIT-WINDOW-CLASSIFICATION]`: for every `u_s≥2` row, classify all rational first separations in the finite window, including partial partitions not covered by Xu Corollary 7.5.
- `OPEN[SPLIT-TO-JOINT-MAP]`: provide a declared source ring, target ring, localization branches, generator images, and pullback certificates for every surviving typed split state. This includes the atlas's 296 per-source complements.
- `OPEN[DESCENDANT-RECEIVER-COVERAGE]`: prove a complete necessary support/order chart for every licensed descendant, including the current `h`-support gap.
- `OPEN[U-NEGATIVE-CHART]` and `OPEN[DESCENT-STATE-S>2]`, as just specified.
- `OPEN[K4-SHAPE-AND-UNIFORM-KILL]`: prove which licensed descendants actually have the `k=4`-ray shape and then prove the applicable unsplit-configuration lemma for them; finite `K=7,8,9` data are not an all-degree theorem.
- **Per-branch kills:** after valid maps exist, every joint, order, receiver, U-negative, depth, and ray chart still needs its own elimination theorem. The current larger receiver atlas kills zero sources.

No new exit-price assertion is made in this report, so no `charge_basis` declaration is applicable.

## 8. Final citable verdict

**Promote Lemma A.** Every normalized non-coordinate plane Keller pair whose degrees cannot be simultaneously reduced—and therefore every minimal-total-degree plane Keller counterexample—has `M_s=n−2` and the exact two-point top form (FS). This closes the one-point-at-infinity leak for minimal counterexamples.

**Promote Lemma B only as a realized-data state classifier.** Its leaves `D1`, `ES`, and `D2` are mutually exclusive and exhaustive. `D1` and `D2` carry Moh's polynomial monomial-Jacobian descent; `ES` carries a typed finite early-split obligation. Do not rename `D2` “globally unsplit,” and do not claim a bare integer skeleton chooses one leaf.

**Do not promote the requested route-to-instrument conclusion.** The frozen evidence does not prove that every `D1` state reaches the complete order chart `(T)`, every `ES` state reaches a certified joint chart, or every `D2` state has `k=4`-ray shape. The 296 atlas complements remain genuinely `UNASSIGNED`.

Hence First Separation plus the radius dichotomy gives a rigorous reduction architecture, but `(H1)∧(H2)` is complete only after the all-degree census-coverage theorem, the missing source-to-chart adapters, U-NEGATIVE and `s'>2` coverage, and all per-chart kills are supplied. It is not presently complete modulo only the two named third configurations and the kills.

## References actually consumed

- T. T. Moh, *On the Jacobian conjecture and the configurations of roots*, J. Reine Angew. Math. **340** (1983), 140–212: printed pp. 140, 183, 185–186, 191, 194, 197–201. In this scan, printed page `N` is PDF page `N−139`.
- Y. Xu, *Intersection Numbers and Split of Minor Roots*, arXiv:1604.07683v4: pp. 1, 4, 10–13.
- `prop54-minimality-opus5-20260905.md`, especially lines 35–90, 114–176, 194–215, 246–269.
- `prop63-radius-gate-opus5-20260905.md`, especially lines 51–176, 180–349, 351–436.
- `receiver-atlas-k1-astra-20260905.md`, especially lines 5–20, 130–183, 185–297, 397–481.
- `ideation-20260905T1200Z-synthesis.md`, lines 5–19.
- `FALLACY-v2.md`, all guardrails; in particular lines 5–6, 20–29.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23570`.
- Body SHA-256:
  `1d3f6fe24abcb6f3e99674eca7f7cc8b47d8574ee2369238bec556506563b6ac`.
- Frozen basis: `b478879ba7180c3829a5fcc863ea2c25552d3460`.
