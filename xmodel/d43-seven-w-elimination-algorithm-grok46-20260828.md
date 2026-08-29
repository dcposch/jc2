# D43 seven-condition elimination: independent hostile design memo

**UTC:** 2026-08-28  
**Role:** Grok 4.6, equal-standing co-researcher  
**Verdict:** **REPAIR THE STORY, THEN SOLVE BY FITTING-STRATIFIED BLOCK ELIMINATION.**  
A generic 24-variable Groebner basis is the wrong first algorithm. The phrase “seven residual conditions on `W1,W2`” is a local expected-codimension count on one Jacobian chart, not a presentation of an elimination ideal, not a proof of zero-dimensionality, and not a license to discard rank-drop or coefficient-algebra components.

No CAS, no AWS job, no repository edit, and no `jc2-lean` access were used. Sampled modular ranks and packet verdict banners are treated as shape evidence only.

---

## Custody of inputs (read, not trusted as theorems)

| file | SHA-256 |
|---|---|
| `xmodel/d43-exact-sparse-source-opus5-hostile-audit-20260828.md` | `456edb3ad982da10c13ebe6f41e9ebdf7e7124e1ae4ef76363f253626ad5fea0` |
| `xmodel/d43-exact-sparse-rows-hostile-review-gpt56-20260828.md` | `283d47df4f55a0e83fbf1758cc8ac71fbe5ee8549dcdb1c3a6838c8ccc42b21e` |
| `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md` | `e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863` |
| `cases/d43_exact_sparse_source_preflight.py` | `504341d6a26dccf18ee83db21bc02d36cd5e58651e251043ec76ecbdb34aa4f5` |
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` |
| `cases/d43_exact_sparse_rows_20260828/selected_rows.py` | `05c244b6bf19334d61bdd79835b56f6e1f8cf8f4e3556e6eea51330c4d705755` |
| `cases/d43_exact_sparse_rows_20260828/PILOT_MANIFEST.json` | `d18e03f989043fc3c7b1b79442107831602559db79781cc8d89e3109b800f435` |

The current `cases/d43_exact_sparse_rows_20260828/` packet is the uncollapsed selector-algebra emitter (independent `HW1,HW2`, advertised rank 6048 before component choice). It is **not** the `a00pp` rank-432 algebra this solve is charged to use. A concurrent replacement may be in flight. **Neither directory is a sealed 184-row `a00pp` inventory.** The algorithm below starts only after a different-agent PASS on a hash-frozen packet that emits all 184 rows over

```text
K0 = Q[zeta42, r3, A1, A2, h] /
     (Phi_42(zeta42), r3^2-3, A1^3-(3+r3), A2^3-(3-r3), 2*h^2-3),
```

with literal `HW_i = h*W_i`, refused surviving `EB`, and polynomial unknowns `W1,W2`. Vector-space rank of this presentation is 432. That is not `[K0:Q]` for a field.

Assumed **after** that PASS, and not before: 155 rows are the zero polynomial, 29 live rows live in bands 20/30/40, total tail degree at most 2, support is the registered 22 names, and the 29×22 tail Jacobian has rank 22 at both registered frames `p=105337` and `p=105673`. Rank 22 at two fibers is the **maximum** possible, so those two points lie on a full-rank chart. It does not empty the degeneracy locus, and it does not bound the residual ideal in `W`.

---

## 0. Objects, in the order they actually exist

Work in the affine chart ring

```text
R = K0[W1, W2, L, M, H],
```

where the 22 tails are the filtration blocks

```text
L (band-20 / D21 support, 10):
  tf1_47, tf1_52, tf2_47, tf2_52, tg1_47, tg1_52, tg2_47, tg2_52, tg01_52, tg02_52
M (band-30 new, 8):
  tf1_57, tf2_57, tg1_57, tg2_57, tf1_62, tf2_62, tg01_62, tg02_62
H (band-40 new, 4):
  tf1_67, tf2_67, tf1_72, tf2_72.
```

Let `F = (F20, F30, F40)` be the 29 live rows, ten plus nine plus ten. Let `Z` be the 155 rows certified as the zero polynomial. The raw-J scheme on this support is

```text
X_J = V(F) ⊂ Spec(R).
```

The two displayed E5 rows, E6, and a product-unit are **not** generators of `(F)`. After the reviewed bridge `e1b99600...`, their existential projection to the localized `W`-plane is exactly

```text
E := (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4 = 0,     W1*W2 ≠ 0,
```

with reconstructed

```text
HM  = -C * a1^2 * A1 * W1^4 / (4*(a1-4)),
s1F = (2^8 / 7^16) * HM,     tSAT = s1F^{-1},
C   = 243 * S_M^3 * (a1-a2)^4,   S_M = 7^12/2^6,
a1=3+r3, a2=3-r3, b=4.
```

All displayed denominators are units on `W1*W2 ≠ 0` in characteristic zero: `a1*a2=6`, `(a1-4)*(a2-4)=-2`, `a1-a2=2*r3`. The other two E6 cube-root branches are `ω * s1F` with `ω^3=1`, `ω ≠ 1`. Since `zeta42 ∈ K0`, one has `ζ3 = zeta42^14 ∈ K0`, so those branches do not enlarge the coefficient algebra. They **are** distinct template embeddings of `s1F`.

`+42` at `(eta,slot)=(0,20)` is the only constant inhomogeneity in the Euler rows. It is what can pin a common `W`-scale. Without it the band-20 linear block is compatible with a scaling degeneration that the two modular fibers do not test.

---

## 1. Filtration-aware elimination that beats a generic Groebner basis

Do **not** compute a grevlex or lex basis of 29 quadratics in 24 unknowns over a rank-432 algebra. The input is block-triangular of a much smaller type, once the certified shape is parsed as polynomial identities rather than as two modular fibres.

### 1.1 Parse the exact blocks before any solve

From the frozen 29 live rows, extract (this is a parse, not a solve):

- `F20(W,L)`: the 10 band-20 rows. After a passing collapsed-D21 band-20 equality these **are** the exact D21 affine block, so they have the form

  ```text
  A(W) · L  =  b(W),     A ∈ Mat_{10×10}(K0[W1,W2]),  b ∈ K0[W1,W2]^{10}.
  ```

  Linearity in `L` is then a theorem of the D21 bank plus the equality gate, not a modular rumour.

- `F30(W,L,M)`: 9 rows, degree ≤ 2. **Read** whether they are affine in `M`:

  ```text
  Q30(W,L) + B(W,L) · M  =  0.
  ```

  If any monomial `M_i M_j` or `M_i H_k` occurs, the predicted triangularity is false and the DAG must refuse the cheap path (fallback in §1.6). Modular “affine after substituting earlier **values**” is not this identity.

- `F40(W,L,M,H)`: 10 rows, likewise parsed as

  ```text
  Q40(W,L,M) + C(W,L,M) · H  =  0
  ```

  only if the exact polynomials say so.

The 4/4/4 ranks in the preflight are ranks of these affine maps **after substituting the banked numerical earlier coordinates**. They are not the ranks of `A(W)`, `B(W,L)`, `C(W,L,M)` as polynomial matrices, and they are not the rank of `dF/d(L,M,H)`. Mixing those three linearizations is how the “seven conditions” slogan was born. Keep them separate.

### 1.2 Band 20 is a parametric linear system in two unknowns `W1,W2`

This is the whole speed win.

`A(W)` and the augmented matrix `(A|b)` live in `K0[W1,W2]` alone. Their Fitting ideals / determinantal ideals are residual conditions **before any tail is eliminated**.

Let `I_{k+1}(A)` be the ideal of `(k+1)×(k+1)` minors. The rank stratification of the `W`-plane is the chain of closed sets

```text
Z_k(A)  =  V(I_{k+1}(A))  =  { rank A ≤ k } ⊂ Spec(K0[W1,W2]).
```

On the locally closed stratum `U_k(A) = Z_k(A) \ Z_{k-1}(A)` one has `rank A = k`. Consistency of `A L = b` on that stratum is

```text
rank(A|b) = k,     i.e.  W ∈ Z_k(A|b).
```

Those conditions do not involve `L,M,H`. They are the first exact residual ideal in `W`.

**Forbidden inference:** both registered fibers have `rank A = rank(A|b) = 4`. That proves only that those two points of `Spec(K0) × A^2` lie in `U_4(A) ∩ Z_4(A|b)`. It does **not** prove `I_5(A) = (0)`, i.e. it does not prove generic rank ≤ 4. If any 5×5 minor of `A` is a nonzero element of `K0[W1,W2]`, generic rank is at least 5 and the folklore 4/4/4 picture is a special-fiber accident. That identity is the first cheap exact discriminator of the whole solve (§DAG.D3).

Computationally, 10×10 sparse polynomial matrices are handled by fraction-free / Bareiss elimination over `K0[W1,W2]`, or by searching for a single nonzero `k×k` minor (lower bound on generic rank) and, separately, by proving that the `(k+1)`st Fitting ideal is zero (upper bound). Do not enumerate `C(10,5)^2 = 63504` minors as the primary method; produce a pivot sequence and the corresponding maximal-minor generator, then saturate the remaining Fitting generators only as needed.

On each exact-rank-`k` chart, a chosen nonzero `k×k` minor `Δ_L` gives Cramer / adjugate formulae

```text
L_pivot  =  (1/Δ_L) · adj · (b − A_free L_free),
```

an affine `(10-k)`-plane of `L` over the chart ring `K0[W1,W2, L_free][Δ_L^{-1}]`. If `k=10`, `L` is unique on that chart. If `k=4`, there are six free `L` coordinates. Either way this is linear algebra, not a Groebner basis.

### 1.3 Bands 30 and 40 are linear in their highest variables, quadratic in the already-parametrized ones

Substitute the chart parametrization of `L` into `F30`. If affine in `M`, one obtains a 9×8 matrix `B^♥(W, L_free)` over a localization of `K0[W, L_free]`. Repeat Fitting:

- strata `U_ℓ(B^♥)`,
- consistency `Z_ℓ(B^♥ | Q30^♥)`,
- charts by `ℓ×ℓ` minors `Δ_M`,
- `M` parametrized by free `M` (if any).

Then substitute `(L,M)` into `F40` and repeat for the 10×4 matrix `C^♥`. Four highest variables means at most `C(10,4)=210` minors of size 4; that block is cheaper than band 20’s 5×5 Fitting, but its coefficients depend on earlier free tails, so it is **not** the first discriminator.

The leftover rows on a full-rank highest chart are polynomial conditions on `(W, free tails)`. If the 29×22 tail Jacobian is invertible on that chart, implicit-function says there are no remaining free tails: the leftover system must cut the free-tail fibre to length finite (or empty). That is a theorem **on the chart**, after the leftover ideal is computed, not a premise.

### 1.4 What the Jacobian rank-22 fact actually buys

Let `J_T = ∂F/∂(L,M,H)`, a 29×22 matrix over `R`. At two modular points it has rank 22, so some 22×22 minor `Δ_*` is a unit at those points. On `D(Δ_*)` the 22 tails are a finite étale function of `W` after base change to an algebraic closure of the residue field of `W`, **provided** the leftover 7 rows vanish. The elimination ideal of the chart is generated by those 7 substituted leftover rows (plus the inverted minor in the denominator, cleared). That is the only honest meaning of “seven residual conditions.”

It is not:

- seven independent equations,
- a regular sequence,
- a proof that `V(F)` is 0-dimensional in `W`,
- a proof that `V(F) = V(F) ∩ D(Δ_*)`.

The complementary closed set `V(I_{22}(J_T))` is a different scheme, typically harder, and is part of the answer. A passing computation on `D(Δ_*)` that reports “empty” or “here are the points” has said nothing about that closed set.

### 1.5 Why this is faster than a 24-variable GB

| object | variables after a full-rank triangular chart | degree |
|---|---|---|
| generic grevlex on `F` | 24 | 2 |
| band-20 Fitting | 2 (`W`) | det degrees of a 10×10 |
| leftover on a rank-`A`=4 chart, before later bands | 8 (`W` + 6 free `L`) | 1 in `L` |
| same, after imposing `E` and `W2 ≠ 0` | 7 (scale + 6 free `L`) or less | as above |
| leftover after also solving `M,H` at full block rank | 2 (`W` only) | whatever the Schur complement produces |

The Macaulay matrix of 22 quadratics in 22 tails already has unusable size. The block method never builds it. The only Groebner/univariate job that should run on the generic chart is the residual ideal in **two** (or, after `E`, essentially one) `W` coordinates, possibly after a short elimination of leftover free tails that later bands failed to kill.

### 1.6 Fallback, only if the parse fails

If band 30 or 40 is not affine in its new variables, refuse the triangular DAG and use a bilinear/Dixon or hidden-variable resultant **per block**, still not a 24-variable grevlex. If even that fails, a lex GB with elimination order `H > M > L > W` and block-graded lex inside each band is the last resort, with hard memory/time caps. It is not the design.

---

## 2. Retain every determinantal chart and every rank-drop stratum

A computation that inverts one minor and proceeds is a computation on a principal open. The vanishing locus of that minor is not “measure zero.” It is an algebraic set that may carry the only characteristic-zero points, or extra points, or embedded components.

### 2.1 Mandatory cover, for every linear block

For a polynomial matrix `X` of size `p×q` (so `A` is 10×10, `B^♥` is 9×8, `C^♥` is 10×4, and `J_T` is 29×22), the cover is

```text
Spec(base)  =  ⊔_k  ⊔_{Δ ∈ Minors_k(X)}  D(Δ) ∩ U_k(X)     ⊔     Z_{k_min-1}(X).
```

Operationally:

1. Record `I_{k+1}(X)` by a generating set (Bareiss diagonals plus enough minors to generate, with a membership certificate).
2. For each `k` that is not proved empty, cover `U_k` by the `k×k` minors that are nonzero as polynomials. One generating set of the Fitting ideal is enough if every generator is used as a chart; a proper subset of minors is a **partial** cover and must be labelled as such.
3. On `D(Δ)`, invert `Δ`, solve, substitute, continue.
4. Recurse on `V(Δ)` inside `U_k` using the remaining minors; do not claim `U_k` is done until the closed complement is either solved or proved empty by a Nullstellensatz certificate in the chart ring.
5. The total drop `Z_{k_min}` where `k_min` is the proved lower bound on rank (e.g. from a nonzero minor, or from 0) is a separate job.

Never use “the two modular witnesses have rank 22 / 4 / 4 / 4” to skip (4)–(5). Those witnesses may all lie on a single open `D(Δ_*)`. That is evidence that `D(Δ_*)` is the interesting chart for **comparison** with the banked points. It is not evidence that other charts are empty.

### 2.2 What must not be discarded

- `V(Δ_L)` for every band-20 pivot minor actually inverted.
- `V(all 5×5 minors of A)` if generic rank ≥ 5 is proved; this is then the modular-rank-4 locus, and it is exactly where the two fibers live if that proof succeeds.
- `V(Δ_M)`, `V(Δ_H)` after substitution.
- `V(I_{22}(J_T))`, the tail-Jacobian drop. On this locus the implicit-function count “seven conditions in `W`” is false: tails need not be finite over `W`. Positive-dimensional tail fibres, multiple roots, and embedded components are all legal here.
- `W1=0` and `W2=0`, which are excluded by localization, not by pretending they are not zeros of `F`.
- Every primitive idempotent factor of `K0` (§3). Inverting a zero-divisor in `K0` is the same crime as inverting a minor: it throws away components.

### 2.3 Bookkeeping contract

Every worker receipt names:

- the `K0`-factor,
- the list of inverted minors `(Δ_L, Δ_M, Δ_H, Δ_T, …)`,
- the Fitting ideal hashes of the complementary closed sets,
- whether those complements have a terminal receipt (`EMPTY` with Nullstellensatz, `FINITE` with a point list, `OPEN` = incomplete, `TIMEOUT`).

A parent “`PASS` / finite list / empty” is illegal if any complementary receipt is `OPEN` or missing. That is the only mechanism that prevents a passing generic-chart run from silently discarding candidates.

### 2.4 Do not confuse stratum dimension with emptiness

`I_5(A) ≠ 0` does not make `Z_4(A)` empty. `Δ_* ≠ 0` at two primes does not make `V(Δ_*)` empty over `K0`. A degree-6 scale polynomial observed modulo 105337 on the E-ratio slice is not the characteristic-zero residual, and it is not a generating set of any Fitting ideal.

---

## 3. The coefficient algebra is a reduced étale `Q`-algebra of rank 432, not a field

### 3.1 What is proved without CAS

The five defining polynomials are a complete-intersection monomial-rewrite system with leading terms `zeta42^{12}`, `r3^2`, `A1^3`, `A2^3`, `h^2`. As a `Q`-vector space the quotient therefore has dimension 432, independently of irreducibility.

Separability of each generator in the tower, after inverting `2,3,7`:

- `Phi_42` is the 42nd cyclotomic polynomial (coefficients `(1,1,0,-1,-1,0,1,0,-1,-1,0,1,1)` in `d43_common_integral_emitter.py`). Discriminant supported at `2,3,7`.
- `r3^2-3`: derivative `2 r3`. If `r3=0` then `-3=0`. After inverting 2, `r3` is a unit on the spectrum (`r3^2=3`).
- `A1^3-(3+r3)`: derivative `3 A1^2`. `A1=0` forces `3+r3=0`, so `r3=-3`, `r3^2=9 ≠ 3`. Thus `A1` never vanishes on `Spec(K0)`, and `3 A1^2` is a unit after inverting 3. Same for `A2`.
- `2 h^2-3`: derivative `4h`. `h=0` forces `-3=0`. After inverting 2, `h` is a unit.

So `K0 ⊗ Q` is finite étale, hence **reduced**: a product of number fields whose degrees sum to 432. The class name `RadicalCoefficient` does not prove this; the resultant/gcd check of each generator against its derivative in the tower is a required cheap job. There are no nilpotents over `Q` once that check passes. (Nilpotents in the **row ideal** `(F)` are a different issue: non-reduced points of `X_J`. Those are retained as multiplicities, not as coefficient-algebra nilpotents.)

The two registered frames are two `F_p`-points of `Spec(K0)` at which the derivatives are units. They certify two étale specializations, not transitivity of `Gal(Q-bar/Q)` on the 432 geometric points, and not that `K0` is a domain.

Heuristic (not a theorem, not to be used as a gate): `Q(zeta42)` is a field of degree 12; `r3^2-3` is irreducible over it because `Q(zeta42) ∩ Q(√3) = Q`; `2h^2-3` adjoins a form of `√2` and is likely irreducible over `Q(zeta42,r3)`; the two Kummer cubics may or may not be irreducible or linearly disjoint. Degrees 48, 144, 432, or a product, are all still legal. **Factor the tower. Do not guess.**

### 3.2 Required decomposition

Job `K0-SPLIT` produces a certified isomorphism

```text
K0  ≅  ∏_{i=1}^c  K_i,     K_i = Q[t]/(m_i(t))  or an explicit tower,
```

by successive factorization:

1. `Q[zeta42]/(Phi_42)` is already a field.
2. Factor `T^2-3` over that field (expected irreducible).
3. Factor `2 T^2-3` over the quadratic.
4. Factor `T^3-(3+r3)` over the result.
5. Factor `T^3-(3-r3)` over each factor from (4).

Output for each `K_i`: minimal polynomial (or tower), `Q`-basis, discriminant, inverted primes, and which of the two registered frames (if any) factor through `K_i`. Components that miss both frames are **not** optional: they are part of the `a00pp` algebra. A solver that only works in the residue field of the `p=105337` frame has solved a different problem.

If some `m_i` remains unfactored, keep that `K_i` as a domain candidate and run D5/dynamic evaluation inside it: every pivot `a ∈ K_i` splits the computation into `D(a)` and `V(a)`. Inverting a zero-divisor without this split is a silent component deletion.

### 3.3 Arithmetic rules while `K0` is still unsplit

If a worker is forced to start before `K0-SPLIT` returns (it should not, on the critical path):

- `K0` arithmetic is the 432-term normal form already implemented.
- A pivot is legal only after a Bézout identity `a b = 1` in `K0`, or after splitting at the annihilator `Ann(a)`.
- “Divide by this coefficient because it is nonzero at both registered frames” is illegal. Nonzero at two points does not prove a unit.
- Denominator primes of `RadicalCoefficient` are presently asserted in `{2,3,5}` for source coefficients; E5/E6 reconstruction also uses `7`. The inverted set is `{2,3,5,7}`. A new prime in a denominator is a halt.

### 3.4 What “componentwise” means for `W1,W2`

`W1,W2` stay polynomial. One does **not** adjoin fourth roots of `W` to `K0` in order to make a “degree-16 field.” That bound was false even as a field-degree estimate, and it is the wrong object: the residue field of a point is an **output** of elimination. After `K0 ≅ ∏ K_i`, the ring of the raw-J problem is `∏ K_i[W1,W2,L,M,H]`. Solve on each factor. Report a product of schemes. Never glue them into a single “degree-432 field of `W`.”

---

## 4. Where `E`, units, `HM`, E5, `s1F`, E6, and the 184-row replay enter

Two rails. They are not interchangeable, and the claim tier must name which rail ran.

### Rail J (raw finite-J existence)

1. Do **not** impose `E`.
2. Run the Fitting-stratified block elimination of §1–§2 over each `K_i`.
3. Localize at `W1*W2` **or** work affinely with Rabinowitsch `W1 W2 u − 1` (one product-unit is enough for this rail).
4. Output: a certified empty residual, or a finite list of `(W,L,M,H)` over finite `K_i`-algebras, or a positive-dimensional residual with an explicit Hilbert polynomial / triangular set.
5. **Then** post-filter: evaluate `E` at each finite candidate. Survivors are raw-J points that happen to lie on `E=0`. Failures are raw-J points that are **not** displayed-E5/E6 extendable.
6. Replay all 184 exact rows, including the 155 zeros, at every candidate. This is a membership check, not a construction.

Rail J is the only rail that may claim “raw finite-J existence on this support.”

### Rail E (displayed E5/E6/unit search; smaller, not stronger)

This is the bridge’s recommended 22-support form.

1. Impose `E=0` and `W1 W2 u = 1` at the **start**.
2. On `W2 ≠ 0` set `ρ = W1/W2`. Then `E` becomes the **constant** (in `K_i`) condition

   ```text
   (9+5*r3)*A1 * ρ^4 + (9-5*r3)*A2  =  0,
   ```

   so `ρ^4 ∈ K_i` is fixed. This is a degree-≤4 cover of each `K_i`, not a degree-16 adjunction of two independent fourth roots, and not a replacement of `W` by constants. The remaining `W`-unknown is the scale `σ = W2`.
3. Band 20 becomes a univariate-in-`σ` linear system over that cover. The `+42` inhomogeneity is what can make `rank(A|b)` depend on `σ`. The modular degree-6 scale polynomial is a **prediction** for this univariate, not a certificate.
4. Continue block elimination in `(σ, L, M, H)`.
5. **Mandatory reconstruction, not optional sugar.** For every surviving point set

   ```text
   HM  := −C a1^2 A1 W1^4 / (4(a1-4)),
   s1F := (2^8/7^16) HM,     tSAT := s1F^{-1},
   ```

   and also the two other cube-root branches `ω s1F`. Evaluate the **literal** polynomials

   ```text
   4(a1-4) HM + C a1^2 A1 W1^4,
   4(a2-4) HM + C a2^2 A2 W2^4,
   2^{24} HM^3 − 7^{48} s1F^3,
   s1F tSAT − 1,
   W1 W2 u − 1.
   ```

   A reconstruction that is not replayed is not a displayed-E5/E6/unit claim.
6. Replay all 184 rows exactly.

Rail E may claim at most “displayed E5/E6/unit extension of a raw-J point on this support.” It may not claim Q0, `H_F` identification, any other tower/quotient/tie, NF equivalence, or JC2.

### Order on the critical path

For **speed of finding displayed-template points**, start Rail E as soon as band-20 matrices exist. For **soundness of claim tiers**, Rail J must still run, because:

- Rail E empty does not imply Rail J empty (`E` may be the obstruction);
- Rail J points that fail `E` are still raw-J points;
- whether `E ∈ (F)` after elimination is an exact membership question, presently open.

Do **not** insert `E` as a generator of the row emitter. Do **not** insert `HM,s1F` as coordinates of `X_J`. Do **not** treat `E=0` as one of the “seven residual J-conditions.”

### What reconstruction does **not** identify

The reconstructed `s1F` is an existential witness for the displayed cube tie. It is **not** automatically the quotient lead `H_F` of the actual `f`-jet at that point. The reconstructed `HM` is **not** automatically the `G_m` `h1`-lead of the jets. If later template rows (Q0: `W_F(n,60) − s1F c_n`, and anything else using `H_F`) are claimed, those rows must be evaluated at the jet-derived `s1F`, and the cube-root branch that matches the jet (if any) must be named. That check is **full template**, not displayed E5/E6/unit.

---

## 5. Independently checkable certificates, by claim tier

A certificate is a byte object with a SHA-256, an evaluator that does not re-run elimination, and a mutation battery. “We ran Singular and it printed 0” is not a certificate.

### Tier 0 — exact `a00pp` row inventory (prerequisite, not a solve)

Already required by the row reviews. The solve DAG consumes, and hash-pins:

- coefficient-algebra descriptor with `field_claim: null`,
- 184-row semantic digest (registry-id monomial order, normalized `Fraction` pairs, 432-term exponents),
- identity proofs of the 155 zeros (support/weight, not sampled evaluation),
- live-row parse: bands, tail degree, affine-in-new-variable flags,
- collapsed-D21 band-20 equality plus HW-sign and `+42`-omission mutations,
- support, registry, `PIN42`, `alpha=beta=0`, `+42` once at `(0,20)`.

Maximum promotion: exact support-specialized `a00pp` raw-source rows. No point.

### Tier 1 — raw finite-J existence on this 22-support cell

**Emptiness of a chart.** For each `(K_i, determinantal chart, unit chart)` a Nullstellensatz record

```text
∑_ν  a_ν F_ν  +  (Δ g − 1) + (W1 W2 u − 1) h   =   1
```

in the chart ring, or a Groebner basis containing a unit of `K_i` together with the S-polynomial reduction log (signature GB or recorded pair reductions). Independently checkable by expanding the combination and reducing to the 432-term normal form.

**Emptiness of the whole `X_J`.** The above for **every** chart and every `K_i`, including Jacobian-drop and `W=0` if those were not localized out of the claim. Missing stratum ⇒ the emptiness claim is incomplete, not true.

**Finite nonempty.** A triangular decomposition / regular chain / rational univariate representation over each `K_i`:

- primitive-element minpoly, or a lex GB of the residual that is 0-dimensional,
- each coordinate as an element of that artinian algebra,
- multiplicity (length of the local ring, not just geometric points),
- chart id, inverted minors, `K_i` id,
- a residual that the independent checker evaluates to zero on all 29 live rows and all 155 zero rows.

Independent checker: `RadicalCoefficient` arithmetic, no GB engine. Must accept a mutation that perturbs one coordinate by 1 and fails.

**Positive-dimensional residual.** Dimension, Hilbert polynomial or a triangular set with a free variable, and an explicit statement that Tier 1 is **not** finite. This is a legal outcome. It is not a point list.

**Not in this tier:** `E`, `HM`, `s1F`, NF, Keller, JC2.

Specialization to `p=105337` and `p=105673` is a **regression**, not a construction. A char-0 point whose `K_i` maps to a registered frame must reduce to a zero of the specialized rows; mismatch is a halt. A char-0 point on a `K_i` that does not map to those frames will not match the banked points; that is not a failure of Tier 1.

### Tier 2 — displayed E5/E6/unit extension

Tier 1 object (or a Rail-E residual) plus:

- `E=0` as an exact identity at the point,
- `W1 W2 u = 1`,
- reconstructed `HM, s1F, tSAT` (all three cube-root branches listed; the branch used for the claim named),
- literal E5 pair, literal E6, literal `s1F tSAT-1` all exactly zero,
- `HM` and `s1F` units.

The bridge `e1b99600...` makes this equivalent, on `W1 W2 ≠ 0`, to `E=0` plus reconstruction replay. The replay is still mandatory: the equivalence is a lemma about polynomials, the certificate is about a specific point.

### Tier 3 — full residue-A / template-conform locus

Tier 2 plus **every other** applicable exact equation of the intended template: Q0 rows with jet-derived `H_F`, remaining quotient/tower/ties, separate `uW1,uW2` if claimed, any `H_F ≟ s1F` identification, and a written list of those equations with hashes. This list is **not** in the present 184-row packet. **Refuse Tier 3 until that list exists and is reviewed.** Relation `E` is not a substitute.

### Tier 4 — NF-presentation equivalence

509 reducer-to-parked identities and 184 source-to-NF identities, plus the parked package the common-integral emitter already refuses to seal. Independent of Tiers 1–3. A finite raw-J point does not identify the banked NF component.

### Tier 5 — all-depth compatibility

Inverse-limit / compatibility across depths. Finite `D=43`, `B=84`, `PIN42`, `alpha=beta=0`, and a 22-name support specialization are all depth-local. **Refuse.**

### Tier 6 — a Keller map

A convergent/algebraic global Keller pair. **Refuse.** A finite D43 point is not a Keller map.

### Tier 7 — JC2

**Refuse.** Campaign policy is unchanged: a finite D43 characteristic-zero point advances only the finite algebraization ladder.

### Cross-tier fraud to reject on sight

- CRT / rational reconstruction of coordinates from the two modular points.
- Treating a linear modular GB as proof that source rows are affine (except band 20, which is exact after D21 equality).
- Treating `K0` as `Q(zeta42,r3,A1,A2,h)` a field because the two frames exist.
- Adjoining two pinned fourth roots and quoting `[K:K0] ≤ 16`.
- Promoting Rail E emptiness to Rail J emptiness.
- Promoting reconstructed `s1F` to jet `H_F`.
- Using the rejected 89-variable graph witness as a source point.
- Consuming incomplete `jet_g_03_G0p2.pkl` as final `g`.

---

## 6. Hidden gaps in the current seven-condition story

The overlay “eliminating the 22 tails leaves seven residual conditions in `W1,W2`; E5/E6 fix the fourth-power ratio; the J rows pin the common scale” is useful as a **search heuristic**. As mathematics it has the following holes. The first three are fatal if ignored.

### G1. `29 − 22 = 7` is not an elimination ideal

On a full-rank tail-Jacobian chart, seven leftover polynomials in `W1,W2` generate the residual **on that chart**. They need not be independent. They need not be a regular sequence. Their common zero scheme may be empty, finite, or a curve. Seven “conditions” in two variables are overdetermined; either they are dependent (actual codimension 0, 1, or 2) or they cut to empty. The slogan assumes the convenient middle case: dependent enough not to be `(1)`, independent enough to be 0-dimensional after intersecting `E`. That is exactly what the computation is for, and it is not known.

### G2. Rank 22 at two points does not control other components of `V(F)`

Full tail rank at two modular points proves those two local branches are étale over their `W`-bases. It does not prove:

- `I_{22}(J_T) = (1)`,
- there is no component with positive-dimensional tail fibre,
- there is no non-reduced tail fibre,
- generic rank of `A(W)` is 4.

If a worker solves only `D(Δ_*)` and reports a finite list, the list is the list on that open. The rank-drop closed set is unsolved. The current story mentions “retain alternatives if the chosen minor vanishes” and then talks as if the seven-condition residual **is** the problem. Those are different schemes.

### G3. Sequential 4/4/4 is a different linearization than `J_T`

After substituting **numerical** earlier tails, the new-variable maps have ranks 4, 4, 4 at the witnesses (sum 12). The tail Jacobian has rank 22. The extra 10 come from derivatives of later rows with respect to earlier tails, i.e. from the bilinear coupling. A solver that treats each band as an underdetermined affine map in new variables and expects six plus four free tails will miscount, and a solver that treats 4/4/4 as “generic exact rank of `A,B,C`” will invert the wrong minors. The 4/4/4 table is evidence about special fibers of a substitution, not a block rank over `K0[W]`.

### G4. `E` is not one of the seven, and reconstructed `s1F` is not `H_F`

The seven leftovers are J-row conditions. `E` is the existential projection of displayed E5. Whether `E` already lies in the elimination ideal of `F` is open. Modular points satisfy both because they are banked template-conform points, not because of an ideal membership.

Worse: Rail E’s reconstruction produces **some** `HM,s1F` satisfying displayed E5/E6. The jets at a raw-J point already determine (or fail to determine) an `H_F`. These can disagree. The bridge is honest (“nothing about template equations other than E5/E6 and units”). The seven-condition overlay’s phrase that the bridge “belongs to source existence” is easy to misread as closing template existence. It does not.

### G5. `K0` components that miss the registered frames are invisible to every modular check in the packet

Both etale gates and both rank-22 witnesses live on two `F_p`-points of `Spec(K0)`. A factor `K_i` through which neither frame factors can carry its own `W`-scheme. No modular replay in the current preflight sees it. Treating “the” seven conditions as objects over “the” radical field silently drops those factors.

### G6. Modular vanishing does not lift, but it does constrain emptiness slogans

`d43_char0_lift.source_rows` vanishing at the two banked `F_p` points shows that the **mod-`p` source formulae** have a common zero. If the exact `a00pp` polynomials reduce to those formulae, a Nullstellensatz certificate of char-0 emptiness with denominators in `{2,3,5,7}` would reduce to `1=0` at `p=105337` and `p=105673`, which is a contradiction. So **global** emptiness of Rail J over every `K_i` is in tension with a genuine exact-source modular zero. This is **not** a char-0 point. It is also not nothing. A claimed Rail-J emptiness must therefore either (i) exhibit a new denominator prime, (ii) live on a `K_i` that does not specialize to those frames, or (iii) prove that the evaluator and the emitter are not the same polynomials (v1 uncollapsed vs `a00pp` is exactly this escape, and is why v1 must not be solved).

### G7. The 22-support is a coordinate subspace, not “the” D43 scheme

Zeros of the specialized rows are zeros of the full 184-row system. The converse is false. A finite D43 point with extra support is outside this solve. The seven-condition core is the 22-cell, `alpha=beta=0`, `PIN42`, `B=84`, residue A. Honest specialization; dishonest if promoted to existence for the unspecialized source.

### G8. `+42` and scale

Opus’s scratch (generic `λ`-scale of an E-ratio slice: `rank A = 4`, `rank(A|b) = 5`; banked scale: both 4; degree-6 univariate at one prime) is the only quantitative hint that J pins scale. It is modular, it already imposes `E`, and it is band-20 only. The leftover bands can kill those six roots or add more. Do not write “the scale is degree 6” as a theorem.

### G9. 155 zeros by evaluation are not identities

The shape assumption of this charge includes identity proofs. If a future emitter reports 155 zeros because they vanished at two primes or at a random `W`, those rows are extra conditions and the count “seven” moves. The certificate for identical vanishing is a 432-term sparse-zero check of each of the 155 polynomials, or a weight/support identity.

### G10. Non-reduced structure

Even on a full-rank chart, the residual in `W` may be non-radical (`σ^2` factors, etc.). Geometric point lists without lengths are incomplete. Multiplicity is not a JC2 issue; it is a scheme-theoretic honesty issue at Tier 1.

---

## AWS job DAG and decision tree

**Do not launch this DAG until** a different-agent PASS exists on an immutable `a00pp` 184-row packet: literal `HW_i=h W_i`, rank-432 output, collapsed-D21 band-20 equality with HW-sign and `+42` mutations, identity of 155 zeros, live-shape parse, coherent hashes, live EC2 identity, zero swap, atomic terminal receipts. Current v1 is not that packet. The concurrent replacement, if any, is not that packet until reviewed.

**Host:** idle isolated EC2, not box01 (monolith still owns `GB42`). ≥512 GiB RAM, ≥100 GiB disk, zero swap, pinned tag/instance/CPU, no competing `singular`/`msolve`/`magma`/`build_tails43`. The AWS wrapper is the only authorized entry.

**This DAG is the solve.** Concurrent sparse `f/g` jet builds belong to the **emitter**, already specified by the row review, and must be finished before anything below.

### Parallelism

```text
                         [frozen 184-row a00pp packet]
                                    |
            +-----------------------+-----------------------+
            |                       |                       |
        K0-SPLIT              PARSE-BLOCKS              E-POLY
        (tower factor,        (A,b, affine flags,       (E, HM, s1F
         reducedness,          live/zero hashes)         as K0[W] objects)
         idempotents)
            |                       |                       |
            +-----------+-----------+-----------+-----------+
                        |                       |
                   D3 FITTING-A            (Rail E wait)
                   (minors of A(W),        (needs K0-SPLIT
                    I_5(A), I_*(A|b))       and PARSE)
                        |
         +--------------+------------------+
         |              |                  |
      Rail J         Rail E            Rail DROP
      (no E)         (E first,         (V(I_22(J_T))
                      univariate        and other
                      scale)            closed strata)
         |              |                  |
         +------+-------+--------+---------+
                |                |
           RECONSTRUCT        INDEPENDENT
           + 184 REPLAY       CHECKER
                |
           MOD-p REGRESSION (non-constructive)
```

`K0-SPLIT`, `PARSE-BLOCKS`, and `E-POLY` run in parallel immediately. `FITTING-A` starts as soon as `PARSE-BLOCKS` has `A,b` and can run over the 432-term ring even before the tower split; it must be **reissued per `K_i`** once the split exists. Rail E and Rail J may run in parallel after `FITTING-A`; they share charts but must not share claim language. Rail DROP is independent and may consume the same row packet on a second cap.

### First cheap discriminators (in this order; halt or branch on each)

**D0. Packet algebra.** Refuse if `EB` survives, if `HW1` and `HW2` remain independent generators, if basis rank is not 432, if `W1,W2` were specialized, or if 155-zero identities are missing. This discriminator already kills current v1 as a solve input.

**D1. `K0` reducedness.** Gcd/resultant of each tower generator with its derivative. Expected: reduced after inverting `{2,3,7}`. If a nilpotent is found, stop and repair the coefficient theory; do not continue under the name `RadicalCoefficient`.

**D2. Tower factorization.** Output `∏ K_i` and the frame-to-factor map. Cheap number-field work (PARI/Magma). If this times out, D5-split on pivots; do not declare a field.

**D3. One exact minor of `A(W)`.** Search for a nonzero `k×k` minor in `K0[W1,W2]`, starting at `k=5`.  

- If a 5×5 minor is a nonzero polynomial: generic rank `A` ≥ 5. The 4/4/4 folklore is a special-fiber statement. The two modular witnesses lie in `Z_4(A)` if their rank-4 reports survive exact specialization of this same `A`. **This is the most important cheap exact fact the campaign does not have.**
- If all 5×5 minors are the zero polynomial: generic rank ≤ 4, consistent with the fibers. Then hunt a nonzero 4×4 minor to open `U_4`.

**D4. Consistency Fitting of `(A|b)` on each `U_k`.** An ideal in `K0[W1,W2]` only. If this ideal is `(1)` on every `K_i` and every `k`, Rail J is empty in the band-20 projection (still check that this is the same `A` as the emitter). If it is 0-dimensional already, later bands only filter a finite `W`-list.

**D5. Rail E univariate.** On each `K_i`, each 4th-root branch of `ρ`, the scale polynomial coming from D4 after substituting `W1=ρ σ`, `W2=σ`. Factor it. This is the exact object the degree-6 mod-`p` scratch was guessing.

**D6. Affine-in-`M` / affine-in-`H` parse.** Boolean. If false, refuse triangular Rails J/E and open the fallback resultant path. Do not “try GB anyway” on the same host without a new manifest.

### Artifacts and hashes (each atomic, written after the mathematics, never hashed while still open)

Every job writes a receipt with schema, input digest, code digest, `K_i` id, chart id, and output digest.

| artifact | required content |
|---|---|
| `ROWPACK.sha256` | 184-row semantic digest, algebra descriptor, support, registry, D21 gate, 155-zero identity digest |
| `K0SPLIT.json` + `.sha256` | factors `K_i`, minpolys, frame homomorphisms, reducedness proof |
| `PARSE.json` + `.sha256` | `A,b` semantic digest, affine flags for `B,C`, term counts, max degrees |
| `EHM.json` + `.sha256` | `E`, reconstruction formulae, unit factor of E5₂/`E` as in the bridge, cube-root branches |
| `FIT_A.json` | Fitting generators of `A` and `(A|b)`, generic rank bounds, chart list |
| `CHART/<id>/gb_or_ns.cert` | Nullstellensatz or 0-dim triangular set, inverted minors |
| `DROP/fitting_JT.cert` | generators of `I_{22}(J_T)` and a terminal receipt for that locus |
| `POINTS/<tier>/<id>.json` | coordinates in a number-field basis, multiplicity, branch of `s1F` |
| `REPLAY/<id>.json` | exact 184 residuals (must be the 0 polynomial), literal E5/E6/unit residuals |
| `REGRESS/p105337.json`, `p105673.json` | specialization of each point that maps to that frame; non-mapping `K_i` explicitly skipped |
| `CHECKER.sha256` | independent evaluator source; must differ from the producer |
| `ARTIFACTS.sha256` | written last, excludes itself, binds terminal verdict |

Terminal markers only after `ARTIFACTS.sha256`. No self-hashing of an open directory.

### Decision tree (promotion / refusal)

```text
D0 fail                          → REFUSE solve; emitter repair
D1 nilpotent                     → REFUSE; coefficient theory repair
D2 incomplete                    → continue only under D5 splitting; no field language
D3 generic rank ≥ 5              → keep U_k for k≥5 as the generic Rail J/E;
                                   open Z_4(A) as a FIRST-CLASS stratum
                                   (this is where the modular witnesses live)
D3 generic rank ≤ 4, some 4×4 ≠0 → generic chart is U_4; still solve Z_3, Z_2, …
D6 affine flags false            → REFUSE triangular path; new fallback manifest
any chart receipt OPEN/TIMEOUT   → parent may not claim EMPTY or COMPLETE FINITE
Rail J EMPTY on all charts       → Tier 1 empty on this support; still run Rail DROP;
                                   do not promote to “no D43 point”
Rail J FINITE                    → Tier 1 list; then E-filter for Tier 2 candidates
Rail E FINITE + reconstruction
  + literal E5/E6/unit replay
  + 184 replay                   → at most Tier 2
H_F / Q0 / other ties missing    → REFUSE Tier 3
509+184 NF traces missing        → REFUSE Tier 4
finite D=43 support cell         → REFUSE Tiers 5–7 always
CRT from two primes              → REFUSE the point
K0 called a field w/o K0SPLIT    → REFUSE the packet
v1 uncollapsed rows              → REFUSE the packet
```

**Maximum promotion this DAG may ever emit:** a hash-pinned, independently replayed finite list (or emptiness) of raw-J points on the 22-support `a00pp` cell, and a sublist that passes displayed E5/E6/unit reconstruction. Nothing else.

**First AWS minutes that are actually worth the host:** `K0-SPLIT` plus `FITTING-A` of the 10×10 matrix `A(W)`. If those two jobs are not sealed, no 22-tail elimination, no msolve, and no language of seven conditions, should run.
