# NPR dichotomy check (opus5 sealed submission)

Grok 4.6 · 2026-09-06 · lane `npr-dichotomy-grok46-20260906` · receipt basis `cf45b6b4f80196d8bc2236c603ffc62cb0eddaa7`.
Notes: `box/npr-20260906/`. No ledger edit, no `jc2-lean`, no other `ideation-*` input, no fleet.

```text
VERDICT: NPR CONFIRMED (structure).
  Covering (a) OR (b) OR (c) HOLDS for this Newton polytope (Q ≢ 0).
  Exclusive "exactly one" is FALSE (typed gap; does not collapse the covering).
  Corollary arithmetic (n1,m1, semigroup, Newton-genus >=1): 66/66.
  Kill potential: NONE on the 66 rows as a numerical necessary condition.
    OPEN as an unrun leaf-order screen. RH / Abhyankar-Moh do not fire
    without extra geometric hypotheses stated in §4.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Manifest built with `awk` from numbered `charged_input_<i>_sha256=` / `_basename=` of `xmodel/npr-dichotomy-grok46-20260906.run.v2`, prefixed by `lane_inputs_dir=/tmp/jc2-lane.us8BN8/inputs`. `sha256sum -c` returned **OK on 3/3**; independent `sha256sum` of the frozen copies matched. No digest was retyped.

```text
a7ee66808eb8688a568d9da98ec5840e9bb55fe0c76af21e6ac9852fb5cad89f  ideation-20260906T0000Z-opus5.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  roster.jsonl
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

Root free ~2.7G at wake, ~1.7G at write; notes+report << 2 MB.

## 1. Proof, line by line

**Standing object.** `Q = Φ(F,G)` with Moh Prop. 3.1 family (p.157): `Φ(u,v) = v^{n_1} - u^{m_1}` plus monomials `u^i v^j` with `n i + m j < n_1 m` and `j < n_1`. The prompt's Weierstrass form `Φ = v^3 - u^2 + a v^2 + b uv + c u + d v + e_0` is exactly that family at `(n_1,m_1)=(3,2)` (40/66 rows). Principal coefficients are `±1`. Assume `Q ≢ 0` (Prop. 2.2: `deg T_2^ψ = D_2 > 0`).

**Line 1.** `ν(Φ(F,G)) ≥ min_{(i,j)∈supp Φ} (i ν(F) + j ν(G))`. Ultrametric inequality: true for any valuation of `k(x,y)`.

**Line 2.** Equality unless the minimum is attained at two or more support points (possible cancellation). The writeup says "two Newton vertices". For this polygon that is accurate on the unique compact *outer* edge: `gcd(n_1,m_1)=1` ⇒ the hypotenuse `(m_1,0)--(0,n_1)` has no interior lattice points, so a tie there is exactly the two vertices. Axis-adjacent faces can carry extra lattice points; those faces are not minimizing when `ν(F)<0` or `ν(G)<0` (next paragraph). Used to split: unique attaining monomial ⇒ no cancellation ⇒ (c); tie ⇒ (b).

**Line 3.** "`Φ`'s Newton polygon in the weights `(n,m)` has exactly one compact upper edge `(m_1,0)--(0,n_1)`, every other monomial strictly below." **Checked** on the Weierstrass support, weights `(n,m)=(3g,2g)`, `wt(u^i v^j)=g(3i+2j)`:

| monomial | `(i,j)` | `wt/g` |
|---|---|---|
| `v^3` | (0,3) | 6 |
| `-u^2` | (2,0) | 6 |
| `b uv` | (1,1) | 5 |
| `a v^2` | (0,2) | 4 |
| `c u` | (1,0) | 3 |
| `d v` | (0,1) | 2 |
| `e_0` | (0,0) | 0 |

Unique max weight 6g on the two principal vertices. Deleting extra terms (vanishing `a,b,c,d,e_0`) cannot add vertices above the hypotenuse. Same for the general triangle: Prop. 3.1 forbids `j ≥ n_1` and `n i + m j ≥ n_1 m` except the two principals.

**Line 4 (the jump).** "If `ν(F)<0` or `ν(G)<0` and the minimum is attained twice, the attaining monomials are the two endpoints, giving `m_1 ν(F)=n_1 ν(G)`; otherwise attained once, no cancellation, case (c)." This does **not** follow from the `(n,m)`-weighted polygon alone: that polygon is the supporting face for *one* functional (the standard weights). An arbitrary divisorial `ν` uses `L(i,j)=i ν(F)+j ν(G)`, whose min-face can a priori be any face of `conv(supp)`. **Missing dual-cone step, filled from this polytope (not by analogy):** `supp Φ ⊂ T := conv{(m_1,0),(0,n_1),(0,0)}`, and the hypotenuse is always a face (principal coeffs `±1`). In the closed third quadrant `ν(F)≤0`, `ν(G)≤0` not both zero, `L` decreases away from the origin, so the min-face is that unique outer edge: tie iff `(ν(F),ν(G))=-t(n_1,m_1)`, `t>0` (case (b)); otherwise unique min at one outer vertex. Mixed signs: extra terms have `i < m_1` or `j < n_1`, so unique min at `(m_1,0)` if `ν(F)<0≤ν(G)` and at `(0,n_1)` if `ν(G)<0≤ν(F)`. Axis scan: `ν(F)<0=ν(G)` unique at max `i`; `ν(G)<0=ν(F)` unique at max `j`. Integer dual-cone scan on the Weierstrass support (`ν(F),ν(G) ∈ [-6,6] ∩ Z`, not both `≥0`) and on the full triangle for every roster pair: **0 covering failures** (`box/npr-20260906/newton-check.txt`).

**Tie handling.** A tie is assigned to (b). The proof does *not* claim (c) on the ray. After possible cancellation of `v^{n_1}` against `-u^{m_1}`, one may have `ν(Q) > min`. That is compatible with covering. **Exclusivity is not.** If the two principal initial forms do *not* cancel, then (b) and (c) both hold. Exhibit (Newton combinatorics; the proof never used `J=1`): `Φ=v^3-u^2`, `F=x^3`, `G=y^2`, `Q=y^6-x^6`, `ν=-deg`. Then `(ν(F),ν(G))=(-3,-2)` is (b) with `t=1`, and `ν(Q)=-6=min(2(-3),3(-2))<0` is (c). For a Keller pair along the *standard* degree valuation the approximate-root construction typically *does* cancel, putting that one valuation in (b) not (c); the statement claims every divisorial `ν` at infinity, and exclusivity is not a Newton identity.

**Correct theorem.** For every divisorial valuation of `k(x,y)` centred at infinity: (a) or (b) or (c). Equivalently: if not (a) and not (b), then (c). The OPEN in the charged file already writes inclusive `or`; §2.2's "exactly one" is the overclaim.

**Corollary geometry (apart from the 66-row arithmetic).** Leading form `v^{n_1}-u^{m_1}` with `gcd=1` is unibranch at infinity in the toric compactification of `T`; lower-weight terms do not split that place. One place ⇒ irreducible. Pole orders of `(u,v)` along that place are `(n_1,m_1)`, semigroup `⟨n_1,m_1⟩`. The number `(n_1-1)(m_1-1)/2` is the number of interior lattice points of `T` (Pick), hence the Kouchnirenko geometric genus of a *Newton-nondegenerate* compactification / generic fibre — not a smoothness witness for every special `s` (discriminant fibres of the 40 elliptic rows can drop to geometric genus 0). FALLACY-v2 floor/attainment: equality of geometric genus to the Newton number needs non-degeneracy, not stated per row. One place and the Newton number `≥1` still stand.

Moh p.150's "one place at `y=∞`" is a *different* curve: the `(f,g)`-parametrization over `k(x)` with parameter `y`, which is rational. FALLACY-v2 flag/place/series: not identified with `Γ_s = {Φ=-s}` and not identified with a source branch. The charged file already separates them.

## 2. Corollary census (mechanical, 66/66)

From `roster.jsonl` fields `source.{n,m}` and `own_child.{n_prime,m_prime}` only: `g=gcd(n,m)`, `n_1=n/g`, `m_1=m/g`, semigroup `⟨n_1,m_1⟩`, genus `(n_1-1)(m_1-1)/2`. Per-row table: `box/npr-20260906/census.tsv`.

| check | count |
|---|---|
| `gcd(n_1,m_1)=1` | **66/66** |
| Newton-genus `≥ 1` | **66/66** |
| parent `(n_1,m_1)` = child | **66/66** |
| `(n_1,m_1)=(3,2)` (Weierstrass `Φ`) | 40/66 |

Genus histogram: `1:40, 2:2, 3:11, 4:4, 6:3, 9:3, 12:2, 27:1` — matches the charged file. Pair histogram: `(3,2):40, (4,3):9, (5,3):4, (7,4):3, (5,2):2, (5,4):2, (7,2):2, (7,5):2, (7,3):1, (10,7):1`. No row has `n_1=1` or `m_1=1` (the Newton-genus-0 locus). The 26 non-Weierstrass rows use the same triangle with a longer hypotenuse; still one compact outer edge.

This confirms the *arithmetic* corollary on all 66 rows. It does not promote geometric genus of every fibre.

## 3. What NPR adds (and does not)

**Not a new necessary numerical condition on any of the 65/66.** The quantities `(n_1,m_1)`, `gcd=1`, and Newton-genus `≥1` are functions of `(n,m)` already on the roster; all 66 pass. Parent=child on 66/66 is the charged file's own observation that the Newton datum is descent-invariant, hence useless as a Q2 discriminator.

**It is a structural fact about the pencil `{Φ=-s}` in the `(u,v)`-plane:** one place at infinity, semigroup `⟨n_1,m_1⟩`, Newton-genus `(n_1-1)(m_1-1)/2 ≥ 1` (generic fibre). And a covering constraint on divisorial valuations of `k(x,y)` at infinity: off the `n_1:m_1` ray, a negative order of `F` or `G` forces `Q` to have a pole of exact Newton order `min(m_1 ν(F), n_1 ν(G))`.

Case (a) is the campaign's finite-pole typing (`EMPTY_PROP6.3_FINITE_POLE`). Case (b) is the standard characteristic ray. The operative new alternative is (c) as a *leaf-order* constraint: a typed `(ord F, ord G)` that is negative in at least one slot and off the ray is forbidden unless `Q` attains that min. The charged file did not apply this to family C's `ES_NECESSARY_LEAF` orders; those orders were not a charged input of this lane, and the screen was not run. Charge it only if it fires on a leaf the whole-tree screen does not already kill.

## 4. Could genus / one-place kill a row?

**Abhyankar–Moh — exact statement needed to kill.** If a row forced that `Γ_s ⊂ A^2` is a closed polynomial embedding of `A^1` (i.e. `k[u,v]/(Φ+s) ≅ k[t]`, an embedded line), then AM says the smaller pole order divides the larger. Here the pole orders are `n_1,m_1` with `gcd=1` and both `≥2`, so neither divides the other: contradiction. The residual rows do *not* assert `Γ_s ≅ A^1`; NPR claims Newton-genus `≥1`, which is the opposite. AM does not fire. (Source AM-type arithmetic is already a census filter; the 66 are typed `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.)

**Riemann–Hurwitz — exact statement needed to kill.** Let `C` be a smooth complete curve with a morphism `φ: C → \overline{Γ}_s` of degree `d ≥ 1`. Then `2g(C)-2 = d(2g(Γ_s)-2) + deg R`. A kill requires: (i) a source curve `C` whose existence is forced by the row (e.g. a compactification of a component of `{Q=-s}`); (ii) geometric genera of `C` and of the normalization of `Γ_s`; (iii) `deg φ`; (iv) a bound on `deg R` from the row, making the equality impossible. The 66 rows are not polynomial pairs: there is no map `(F,G)` and no such `C` in the row data. For an actual Keller automorphism, `(F,G)` identifies `{Q=-s}` with `Γ_s` and RH is tautological.

Using Newton-genus as if it were geometric genus of a special fibre would be a floor/attainment error (FALLACY-v2) and could only *weaken* a target-genus lower bound.

## 5. FALLACY-v2

*Flag/place/series.* `ν` is a divisorial valuation of `k(x,y)` at infinity; `Γ_s`'s unique infinite place is not a source branch and is not Moh p.150's place at `y=∞`. *Floor/attainment.* Covering uses equality only at a unique support point (one monomial, coeff `±1`); genus equality to the Newton number is not promoted per special fibre. *Pole/interior.* Vertex class of the outer edge checked on the explicit support before any pole-order identity; the missing dual-cone step is filled from that support. *Prime label.* `n',m',s'` are generation labels. *Variable/ring map.* `Φ` is in `(u,v)` with `u ↔ F`, `v ↔ G`, weights `wt u = n`, `wt v = m`. *Per-ray charge.* No exit claim. *`sat()` / remainder / merge-free / target index.* Not used.

## 6. Kill potential (typed)

```text
arithmetic on the 66:           NONE (0 rows fail n1,m1,gcd,Newton-genus)
leaf-order screen (c) vs (a)|(b): OPEN, not executed (leaf orders uncharged)
RH kill:                        does not fire; needs the §4 morphism package
AM kill:                        does not fire; would need Gamma_s isomorphic to A^1
exclusive-or as stated:         FALSE; replace by covering OR
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11672`.
- Body SHA-256:
  `df2abea7f85dccf4e53ddf2cc2413741da04bdc563774382202dfef1b3603ce8`.
- Frozen basis: `cf45b6b4f80196d8bc2236c603ffc62cb0eddaa7`.
