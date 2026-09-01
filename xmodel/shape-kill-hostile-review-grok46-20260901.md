# Hostile review: SHAPE-KILL report (Opus)

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-01.
**Charge.** Default to refutation. Desk-scale exact reasoning; literature hashed as needed. No CAS. No `jc2-lean`. No `charge_basis` declaration.

## 0. Hash verification, inputs, scope

Frozen inputs were hashed with `shasum -a 256` before they were read. All three SHA-256 values match the charge exactly:

```text
189bc45d83c97df3614c65450a8c6e926938e50f7ccc0b2bacd78a7fd8d11c4d  shape-kill-uniform-opus5-20260901.md
cff4116c19728da875c141133f3b7e739e979ebcb606694272cb14ee6e5130c1  campaign-pin-gpt55-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Below, **SK**, **PIN**, and **Coord** denote those three files in charge order. No canonical ledger or charged file was edited, `jc2-lean` was not inspected, and no CAS was run. The producer’s disclosed `S_4` enumerations in SK §§3.2 and 4.3 were re-derived by hand; they were not re-executed. `FALLACY-v2` is in force. No new exit price is asserted.

Primary sources re-opened (not saved as campaign artifacts):

```text
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
  refs/chau1999_apm71_full.pdf
  Nguyen Van Chau, Non-zero constant Jacobian polynomial maps of C^2,
  Ann. Polon. Math. 71 (1999). Consumed: Theorem B (printed p. 288) and
  the Theorem 4.4 ratio statement quoted on printed p. 288.

b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153
  https://arxiv.org/pdf/1211.2526v1
  Taketo Shirane, A note on normal triple covers over P^2 with branch
  divisors of degree 6, arXiv:1211.2526v1. Consumed: Corollary 0.6
  (deg Δ̄=6), §§1.1.5–1.1.7 (Miranda Tschirnhausen module; branch
  divisor in |(det T_π)^{-2}|; Weierstrass split T_π ≅ L^{-1}⊕L^{-2}),
  Corollary 2.3 (at deg 6, T_π is O(-2)⊕O(-1) or Ω_{P^2}).
  Custody hash as already recorded at
  pi1s4-64-torus-check-hostile-review-sol56-20260901.md:185–188.

Tokunaga, Triple coverings of algebraic surfaces according to the
  Cardano formula, J. Math. Kyoto Univ. 31 (1991) 359–375 (T91),
  inspected via Project Euclid first-page/preview only: Cardano
  discriminant construction, not a general-degree splitting theorem.
```

Standing notation is SK §1: `D=D_1` an escaping `N=4` residual branch curve, birational polynomial parametrisation `(p,q)`, `d=deg p>n=deg q`, `g=gcd(d,n)`, `(d',n')=(d/g,n/g)`, meridional-transposition surjection `φ:π_1(A^2-D)↠S_4`. Promoted inputs actually consumed: Chau trichotomy (PIN:140–146, D1-DEGREE-REVIEW Item 2); target-automorphism invariance of residual data (PIN:81–87); tubular factorisation, Lemma 3.3, Theorem A'(1)–(4) (CONFIRMED at `pi1s4-close-residual-hostile-review-sol56-20260831.md:51–59`); nodal `(M-INF)` at `T=0` only as a side check. Not consumed: A'(5), Shirane Corollary 0.6 off degree 6, any AM converse, any `d_min≤9` bound.

Default-to-refutation concentrated on: (i) SK-1’s attainment and Chau re-run versus the charged block-product collapse; (ii) the `A_4` solution of the deformed braid relation; (iii) the passage from a 3-cycle of block products to `ord(Π)=3`; (iv) whether the four OPENs are forced or are untyped remainder; (v) whether the residual `d_min` cage after the kills is exactly the typed survivors.

**Headline.** SK-1, SK-4, and SK-5 HOLD at their written scopes. The charged collapse mechanism is correctly REFUTED (SK-0). All four OPENs are necessary. The narrowed-cage summary is correct on the residual shapes; Coord’s parenthetical that Tschirnhaus-splitting “would close family 3” is not.

## 1. THEOREM SK-1: the (u,1) family, actual mechanism

**Verdict. CONFIRMED** at the written scope: in any `d_min`-attaining target gauge, `n` does not divide `d`, so the reduced shape is never `(u,1)`. This is a gauge-elimination, not a representation-theoretic prohibition on `(u,1)` presentations. The charged collapse mechanism is not used, and is correctly REFUTED.

### 1.1 What the charge proposed, and SK-0

At `n'=1`, A'(4) gives `Π_1=⋯=Π_{d'}=c` and `Π=c^{d'}`. The charge asked whether this forces `|im φ|≤6` as at `(4,2)`. SK-0: the constant tuple `(c,…,c)∈S_4^{d'}` is a fixed point of the Hurwitz action of `δ_{d'}`, hence of `δ_{d'}^{n'}`, for every `g,d',n'`. The action formula SK cites (`pi1s4-close-residual-r2-opus5-20260831.md:248–250`) is the standard left Hurwitz action of `δ_{d'}=σ_1⋯σ_{d'-1}`:

`(u_1,…,u_{d'}) ↦ (Π u_{d'} Π^{-1}, u_1, …, u_{d'-1})`, `Π=u_1⋯u_{d'}`.

Checked at `d'=2` and `d'=3`: the first slot is `Π u_{d'} Π^{-1}`, and on a constant tuple `Π=c^{d'}` centralises `c`. So A'(1)–(4) are satisfiable at every noncoprime shape. The outer level alone cannot kill. This is the uniform form of the promoted `(6,2)` counterexample (blocks `((12),(12)), ((23),(23)), ((34),(34))`, products `1`, entries generating `S_4`; residual-review item 5). The `(4,2)` accident — two blocks of two transpositions with equal products cannot generate `S_4` — fails as soon as `d'≥3`. **SK-0 CONFIRMED. Charged mechanism REFUTED.**

### 1.2 The actual instrument

SK-1 uses four ingredients, none of them outer-braid collapse.

**(i) Attainment.** `{deg T(D): T∈Aut(A^2)}` is a nonempty subset of the positive integers, so it has a least element `d_min`. Over `C`, Jung–van der Kulk says every automorphism is tame, but tameness is not required: the elementary maps used below already lie in `Aut(A^2)`. This is well-ordering of `ℕ`, not compactness. No floor/attainment fallacy.

**(ii) Normalisation in an attaining gauge.** Fix `T_0` attaining, `D_0=T_0(D)`, birational polynomial parametrisation `(P,Q)`. Promoted target-automorphism invariance (PIN:81–87) puts `D_0` back in the residual class. If `deg P=deg Q`, the linear map `(x,y)↦(x−λ y,y)` extends to an automorphism of `P^2` (so preserves projective degree) and strictly drops `deg P`. If `deg P<deg Q`, swap. One may take `d:=deg P>n:=deg Q` with `d=d_min`.

Projective degree equals `d`: the map `P^1→P^2`, `[T:S]↦[P_d(T,S): S^{d-n} Q_n(T,S): S^d]`, has no base points (`S=0` gives `[lc(P):0:0]≠0`; `S≠0` cannot kill the third coordinate together with the first two). Birationality of the affine parametrisation makes the map birational onto its image, so `deg D̄_0=d`.

**(iii) Strict drop when `n∣d`.** Escape forces `g≥2`, hence `n≥2`. If `d=un` with `u≥2`, set `λ=lc(P)/lc(Q)^u` and `T_1(x,y)=(x−λ y^u,y)∈Aut(A^2)`. Then `T_1(D_0)` is parametrised by `(P−λ Q^u, Q)`. The identity `d=u n` puts `δ_0∈⟨δ_1⟩`, so `deg(P−λ Q^u)=d_1<d` (SK (2.2)). Constancy of `P−λ Q^u` would give `C(P,Q)=C(Q)`, a proper subfield of `C(t)` because `n≥2`, contradicting birationality. The projective degree of `T_1(D_0)` is at most `max(d_1,n)<d` (`u≥2` gives `n<d`; if the map `P^1→` image has degree `>1` the projective degree is even smaller). This contradicts minimality.

**(iv) Chau re-run.** In the attaining gauge, `n` does not divide `d`. Chau 1999 Theorem B (hashed PDF, printed p. 288): after arranging `deg P=kd≥deg Q=ke` with `gcd(d,e)=1`, either `e=1` or `deg_{geo} f=rd+se≥min{2e,d}`. Combined with Theorem 4.4 (dicritical-image degree ratio equals the map’s ratio) this is the promoted trichotomy (PIN:140–146). The only source change Chau uses is a generic linear change making coordinates monic in `y` (Newton–Puiseux in `y`, printed p. 289). Target postcomposition produces a new Keller map to which the same pair of theorems apply, so the trichotomy is valid in every target gauge, including a `d_min` gauge. With `n∤d` the reduced shape is `(odd u,2)` or `(4,3)`.

### 1.3 Scope, not overclaim

SK §2.3 explicitly refuses the statement “no residual curve admits a `(u,1)` presentation”: the maps `T_k(u,v)=(u,v+u^k)` produce infinitely many such presentations (PIN:126–135). The property being excluded — a meridional-transposition surjection onto `S_4` — is gauge-invariant in both directions, so a sweep that clears `(odd u,2)` and `(4,3)` in a `d_min` gauge clears every residual curve. That is the precise sense in which family 1 dies, and it is the sense PIN needs.

PIN:250–260 already recorded the triangular drop and that a `(u,1)` shape cannot be a `d_min` representative; D1-DEGREE recorded the Jung-reduced remark. SK-1’s increment is the packaging: attainment plus re-running Chau in the attaining gauge, converting a normalisation remark into an elimination of one of the three cage columns. The mathematics is not new, but it is correct, and the fallacies the producer flags (floor/attainment, representative vs actual) are avoided.

### 1.4 Independent corroborations, not load-bearing for SK-1

**Lemma SK-2 / Corollary SK-2'.** At `g=2`, a block with product `1` is `(τ,τ)`, and every power of `σ∈B_2` fixes it, so `ι` acts trivially. The cabled-crossing formula (Lemma 3.3, CONFIRMED) then makes `C_2` of any braid act through `B_{d'}↠S_{d'}`. The image of `δ_{d'}^{n'}` is a `d'`-cycle because `gcd(n',d')=1`, whose fixed tuples are the constant ones, giving `im=ℤ/2`. Combined with the two nontrivial values of a product of two transpositions: a 3-cycle confines every entry to three letters (`im≤S_3`); a double transposition pins each block to its two disjoint factors (`im≤V_4`). This kills the whole `n=2` column `(2u,2)` by inner-plus-realisability, independently of SK-1, and it kills the promoted `(6,2)` product-tuple that A'(4) cannot. Honest scope is `g=2`; for `g≥3` a trivial-product block is not `B_g`-fixed. **CONFIRMED**, used below in SK-4’s `ord W=1` case and in the `(8,6)` constant stratum.

**Lemma SK-3.** The conversion identity with `β_i≥d` (row-gauge lower bound, SK:102–105) and `E=e_{h-1}≥2` produces `β_h≤Φ(E)=(C+Ed)/(E-1)`. `Φ` is decreasing in `E` precisely when `2δ_∞>(a-1)(d-1)`; the complementary regime has `E=a` and `β_1≤d≤2d+n-2`, so `(M-INF)` fires. In the decreasing regime the worst case is `E=p(a)`, and clearing `Φ(p)≤2d+n-2` is exactly SK (2.3) (re-expanded: `C−RHS=d(n-p)−p(n-2)−2δ_aff−1`). Sufficient, nodal, not sharp. For `n=2` one has `n≤p(a)`, so (2.3) holds and every *nodal* `n=2` row dies by `(M-INF)` alone. Tangential `n=2` is not covered by SK-3; SK-2' covers it. SK-3 is not used in SK-1, SK-4, or SK-5.

**Promotion recommendation for SK-1: PROMOTE**, with the gauge-elimination wording of SK:227–236, not “no `(u,1)` residual exists”. Promote SK-0 with it.

## 2. THEOREM SK-4: the g=2 slice of (odd u, 2)

**Verdict. CONFIRMED.** For `g=2` and `(d,n)=(2u,4)` with `u` odd, the row is dead unless `u≡3 (mod 6)`. In every surviving outer configuration `Π` is a double transposition, hence lies in `V_4`.

### 2.1 Outer equation

A'(2) at `(d',n')=(u,2)`: the block-product sequence is 2-periodic, values `X=Π_1=Π_3=⋯` and `Y=Π_2=Π_4=⋯`, and `r=d' mod n'=1` makes conjugation by `Π` the shift by `-1`. With `u=2m+1` and `W:=XY` one has `Π=W^m X`, and `Π X Π^{-1}=Y` rearranges to the single equation

```text
(3.1)     X W^m X = W^{m+1}.
```

Conversely (3.1) implies both conjugation relations (the second via `W^{m+1} X^{-1}=X W^m`). At `m=1` (`u=3`, reduced shape of `(6,4)`) this is the braid relation `XYX=YXY`. Identities (3.2): `Π=W^m X=X^{-1} W^{m+1}` and `Π^2=W^u` follow by substitution. Composition is right-to-left as declared; all conclusions below are about orders, cycle types, supports, and generated subgroups, which are anti-isomorphism invariant.

### 2.2 Complete solution in A_4

At `g=2` each block product is a product of two transpositions, so `X,Y∈A_4`. Elements of `A_4` have order 1, 2 (double transpositions), or 3 (3-cycles). No square in `A_4` is a double transposition (4-cycles square to double transpositions, but 4-cycles are odd).

- **`ord W=1`.** Then `Y=X^{-1}` and (3.1) gives `X^2=1`. If `X=1` then SK-2 gives `im=ℤ/2`. If `X` is a double transposition then `Y=X` and every block is the ordered pair of the two disjoint factors of `X`, so `im≤V_4`. Dead.
- **`ord W=2`.** `m` even: `X^2=W`; `m` odd: `X W X=1` rearranges to `X^2=W^{-1}=W`. Both require a square equal to a double transposition. No solutions.
- **`ord W=3`, `m≡0 (mod 3)`.** (3.1) reads `X^2=W`, so `X=W^2` (the unique 3-cycle square-root of `W` in `⟨W⟩`), hence `Y=X`. Constant 3-cycle: every entry lives in `supp(c)`, `im≤S_3`. Dead.
- **`ord W=3`, `m≡2 (mod 3)`.** `X W^2 X=1` rearranges to `X^2=W`, same constant solution. Dead.
- **`ord W=3`, `m≡1 (mod 3)`.** (3.1) reads `X W X=W^2`. Fix `W=(123)`, so `W^2=(132)`. The twelve elements of `A_4` were checked by hand (not by the producer’s script):

  Identity: `W≠W^2`. The three double transpositions are involutions, so `XWX` is conjugation of `W`: `(12)(34)` gives `(142)`, `(13)(24)` gives `(134)`, `(14)(23)` gives `(243)`, none equal to `(132)`. The eight 3-cycles: `X=(123)` gives `1`; `X=(132)` gives `(132)` (constant solution); `X=(124)` gives `(132)`; `X=(142)` gives `(243)`; `X=(134)` gives `(13)(24)`; `X=(143)` gives `(132)`; `X=(234)` gives `(132)`; `X=(243)` gives `(14)`. Exactly four solutions, `X∈{(132),(124),(143),(234)}`, matching SK.

  Non-constant pairs, with `Y=X^{-1}W` under right-to-left composition:

  ```text
  (X,Y) ∈ { ((124),(234)), ((143),(124)), ((234),(143)) },   W=XY=(123).
  ```

  Direct products: `(124)(234)=(123)`, `(143)(124)=(123)`, `(234)(143)=(123)`. Supports `{1,2,4}∪{2,3,4}={1,2,3,4}` (and cyclic analogues), so the available transpositions include `(12),(23),(34)` and generate `S_4`. These outer data are realisable as block-product tuples.

Fixing `W=(123)` is without loss of image: all 3-cycles are conjugate in `S_4`. The other `A_4`-class `W=(132)` yields the inverse equation, the same cycle types, and again `Π` a double transposition.

### 2.3 Formula (3.3) and the modulus

`u=2m+1` with `m≡1 (mod 3)` is `u≡3 (mod 6)`. Then `W^3=1` gives `Π=W^m X=WX`, and

```text
(123)(124)=(13)(24),   (123)(143)=(14)(23),   (123)(234)=(12)(34).
```

All double transpositions, so `Π∈V_4`. Also `Π^2=W^u=1` because `u` is divisible by 3, consistent with order 2.

Diction: “exactly one `⟨Π⟩`-orbit” is loose. For fixed `W`, `⟨Π⟩` has order 2 and the three pairs are not a single size-2 orbit. Up to `S_4`-conjugacy there is one class of non-constant configurations, and that is what SK-4 uses. Not a hole in the kill.

### 2.4 What is killed, what is only classified

If `u≢3 (mod 6)`, every solution of (3.1) in `A_4` has image at most `S_3` or `V_4`. No `ρ_∞`-fixed tuple can have image `S_4`. This is a complete row kill: A'(1) forces the outer equation, and the inner braid cannot relax it. Rows `(10,4),(14,4),(22,4),(26,4),…` die with no delta-sequence census. PIN:286–290 listed `(10,4)` as having no promoted general kill; SK-4 supplies one.

If `u≡3 (mod 6)`, the outer data survive. SK-4 does **not** claim the geometric row is realised; the table correctly marks `u≥9` OPEN. The `u=3` row `(6,4)` is outside SK-4’s kill and is dead only by the promoted explicit-family ROW-KILL after ROW-NF, conditional on that identification (PIN:110–121). SK does not smuggle it into SK-4.

**Promotion recommendation for SK-4: PROMOTE** the kill `u≢3 (mod 6)` and the identity (3.3) on surviving outer data. Do not promote existence of a residual curve with `u≡3 (mod 6)`, `u≥9`.

## 3. THEOREM SK-5: non-constant (4,3)-scalings, `Π` of order 3

**Verdict. CONFIRMED.** The charge’s gloss “constant-stratum constraint” is the wrong stratum: SK-5 is the *non-constant* stratum, at every `g`. In that stratum `Π` is a 3-cycle, so the `S_3`-resolvent does not descend to `π_1(P^2-D̄)`. The constant stratum is a separate `g=2` kill, not SK-5.

### 3.1 Outer datum and Lemma 4.2

Here `d'=4`, `n'=3`, `(d,n)=(4g,3g)`. A'(2) gives a 3-periodic block-product sequence: `A=Π_1=Π_4`, `B=Π_2`, `C=Π_3`, `Π=ABCA`, and conjugation by `Π` is the shift by `-1`:

```text
(4.1)     Π A Π^{-1}=C,   Π C Π^{-1}=B,   Π B Π^{-1}=A.
```

A'(3) puts `Π^{n'}=Π^3∈Z(H)` with `H=⟨A,Π⟩`, so `φ:=conj_Π` satisfies `φ^3=id` on `H`. Lemma 4.2: if any two of `A,B,C` agree then all three agree. If `A=C` then `φ(A)=A` so `B=φ^2(A)=A`. If `A=B` then `φ^2(A)=A`; applying `φ` and `φ^3=id` gives `φ(A)=A`. If `B=C` then `φ^2(A)=φ(A)`, so `φ(A)=A`. **Lemma 4.2 CONFIRMED.** The non-constant stratum is exactly the case of three pairwise distinct block products, on which `φ` acts as a 3-cycle.

### 3.2 Order of `Π`

The set `{A,B,C}⊂S_4` is `conj_Π`-invariant, and the restriction of `conj_Π` to that set has order 3. The order of a restriction of a bijection to an invariant subset divides the order of the bijection. Hence 3 divides the order of `conj_Π` as an automorphism of `S_4`. Since `Z(S_4)=1`, that order equals `ord(Π)∈{1,2,3,4}`. The only multiple of 3 in that list is 3, so `Π` is a 3-cycle. A 3-cycle is not in `V_4`, so the loop at infinity has nontrivial image in `S_3=S_4/V_4` and the composite `π_1(A^2-D)↠S_4↠S_3` does not factor through `π_1(P^2-D̄)`.

(Alternatively: if `ord(Π)=4` then `Π^3=Π^{-1}∈Z(H)` forces `Π∈Z(H)`, so `φ` is id on `H` and `A=B=C`, contradicting non-constancy. If `ord(Π)∣2` the action on `{A,B,C}` cannot have order 3. Same conclusion, and this is the “`Π` central” content of A'(3) that the charge named.)

Sign check, not used but consistent: `sgn(Π_i)=(-1)^g` and `Π=ABCA` has `sgn(Π)=sgn(B)sgn(C)`, even in both parities of `g`, matching a 3-cycle.

SK-5 is uniform in `g` because (4.1) and A'(3) are outer. It does **not** kill family 3. It permanently closes the NO-TORUS/Shirane route on the non-constant stratum, which is why the campaign never had a Shirane attack on `(8,6)` of the same shape as on `(6,4)`. Family 2 at `g=2` is the opposite: (3.3) *forces* `Π∈V_4` and descent is automatic.

Closing `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` would not touch this stratum: there is no triple cover of `P^2` to apply it to. It could still bite the constant stratum, where `Π=c^4` may lie in `V_4`.

### 3.3 The `g=2` split, not part of SK-5

At `g=2`, `(d,n)=(8,6)`, block products lie in `A_4` and `sgn(Π)=(-1)^8=+1`.

*Constant stratum.* `c=1` is SK-2 (`gcd(3,4)=1`). A 3-cycle confines entries to three letters. A double transposition pins each block to its two disjoint factors. Dead, by the same realisability filters as SK-2'. **CONFIRMED as a `g=2` lemma**, not as SK-5.

*Non-constant stratum.* SK-5 gives `Π` a 3-cycle; take `Π=(123)`. Then `C=φ(A)`, `B=φ^2(A)`, and `ABCA=Π` is checked on `A_4`. The `φ`-fixed points in `A_4` are `{1,(123),(132)}`; among them only `A=Π` solves `A^4=Π`. If `A` is a double transposition then `{A,φ(A),φ^2(A)}=V_4\setminus\{1\}` and the product in the abelian group `V_4` collapses to `A≠Π`. The six 3-cycles moving 4 form two `φ`-orbits of size 3:

```text
{(134),(142),(243)}     and     {(124),(234),(143)}.
```

(The conjugation formula `σ(abc)σ^{-1}=(σ(a) σ(b) σ(c))` must not be rewritten `(314)=(134)`; `(314)=(143)`.) Direct tracking of `A=(134)`, `B=(243)`, `C=(142)` gives `ABCA=(123)=Π`. For `A=(124)`, `B=(143)`, `C=(234)` one gets `ABCA=A≠Π`. So the non-constant solutions are exactly one `φ`-orbit, supports `{1,3,4},{2,3,4},{1,2,4}`, whose transpositions exhaust `S_4`. The `(8,6)` row survives the outer battery, matching PIN’s AM-numerical types. This is an outer classification, not an existence theorem for a residual curve.

For `g≥3` the same filters are vacuous. SK’s explicit odd-permutation solutions at `g=3` (`A=(12)` and `A=(14)` with `Π=(123)`) satisfy `ABCA=Π`, and a block of three transpositions with a prescribed transposition product can generate `S_4`. The construction runs at every `g`. Family 3 is not killed uniformly.

**Promotion recommendation for SK-5: PROMOTE** as a non-constant-stratum theorem at every `g`, together with the `g=2` constant-stratum kill. Do not promote a uniform kill of family 3, and do not promote existence of the `(8,6)` non-constant orbit as a residual curve.

## 4. OPEN SHAPE-2-INNER-g>=3

**Verdict. NECESSARY.** Not a gap in a claimed theorem.

The three ingredients of SK-4 are `g=2` phenomena. (1) `X,Y∈A_4` uses that `g` is even; for `g` odd both are odd (transpositions or 4-cycles), and (3.1) has a different solution set. (2) Support confinement and factor-pinning use that a product of *two* transpositions determines its factors up to order; for `g≥3` a prescribed product can have factors generating `S_4`. (3) SK-2 needs the block `(τ,τ)`; for `g≥3` a trivial-product block is not `B_g`-fixed.

SK-0 still supplies the constant tuple as an outer fixed point at every `g`. The outer level therefore cannot kill. The missing ingredient is the inner braid `ι`, pinned numerically by (1.1) to `e(ι)=gu-1+2δ_aff-2g(gu-g)` but not otherwise constrained without a `δ_aff` census. Filling this by analogy with `(4,2)` (where `ι` ranged over `ℤ^2` with one condition) would be a FALLACY-v2 cap. Typed OPEN is the only safe remainder.

A sharpening the producer did not record, and which does **not** close the OPEN: for *even* `g≥4`, `X,Y` still lie in `A_4`, so the solution list of §2.2 still classifies outer data. Constants with `c` a 3-cycle, which die at `g=2` by support confinement, may generate `S_4` at `g≥4`. Odd `g` is untouched. The OPEN remains necessary on both parities.

## 5. OPEN SHAPE-2-INFINITY-Z3

**Verdict. NECESSARY** as a successor on the `g=2`, `u≡3 (mod 6)` survivors. Claim (3.4) HOLDS for affine *nodes*; it is not checked for tangential `A_{2k-1}`.

Shirane, hashed arXiv:1211.2526v1, Corollary 0.6 is literally `deg Δ̄=6`. Family 2 has branch `D̄` of degree `d=gu`, equal to 6 only at `(6,4)`. There is no promoted degree-`2k` analogue; for `deg B≥8` the double plane is of general type. The classification half of the `(6,4)` kill does not travel. CONFIRMED.

The descent half *is* degree-free, and at `g=2` it is automatic: (3.3) puts `Π∈V_4`. It also forces `sgn Π=+1`, hence `d` even, hence (with `u` odd) `g` even: no odd-`g` family-2 row admits the `S_3` descent. Those rows are not killed; they lose the route.

Given descent, let `W_2→P^2` be the double cover branched along `D̄` and `Y→P^2` the Galois `S_3`-cover, so `Y→W_2` is cyclic of degree 3. At an affine node the two meridians map to disjoint transpositions (promoted residual local type, row-sweep:108–110). Disjoint transpositions lie in the same `V_4`-coset (`(12)(34)∈V_4`), so they have the same image in `S_3`. Local inertia in `S_3` is a single order-2 subgroup, meeting `A_3` trivially. Hence `Y→W_2` is étale there. The point of `W_2` over a node is an `A_1` singularity, whose link has `π_1=ℤ/2` and admits no `ℤ/3` quotient. Smooth points of `D` have transposition inertia, already used by the double cover, so they contribute no `A_3` inertia either. That is (3.4) in the nodal case.

The residual class also allows tangential double points `A_{2k-1}`. SK writes “affine node”. The Kleinian `A_1` argument does not automatically copy to the double cover of a tacnode. Scope of (3.4): nodal. Converting even the nodal statement into a contradiction requires Tokunaga’s divisor-class criterion at the infinity singularity, which SK correctly refuses to consume from a first-page inspection of T91. Typed OPEN is forced. It applies only where descent holds — the SK-4 survivors — not to odd `g` or to family 3’s non-constant stratum.

## 6. OPEN SHAPE-3-ALL-g

**Verdict. NECESSARY.** Family 3 is not killed uniformly. SK-5 removes a route; it does not remove the family.

What SK adds, and which may be promoted as outer structure rather than as a kill: the normal form (4.1); SK-5; the complete `g=2` split (constant dead, non-constant a single explicit `φ`-orbit). The residual mechanism is again `ι`, with

```text
(4.2)     e(ι)=4g-1+2δ_aff-9g^2
```

(`g=2`: `2δ_aff-29`; `g=3`: `2δ_aff-70`). At `g=2`, `ι∈B_2^4≅ℤ^4` with one linear condition, a three-parameter family; at `g≥3` the factors are nonabelian and (4.2) constrains only the total exponent. That is why the `(4,2)` template (`e(ι)=1` on two parameters) does not repeat. No desk-scale inner analysis is supplied, and none is claimed. OPEN is the correct remainder for `g=2` non-constant and for all `g≥3` (both strata).

## 7. OPEN TRIPLE-COVER-TSCHIRNHAUS-SPLIT

**Verdict. NECESSARY**, and correctly not consumed. Highest-value successor only on strata where descent holds.

Miranda (as quoted by Shirane §§1.1.1–1.1.5): `π_*O_X=O⊕T_π` with `T_π` locally free of rank 2; the weighted branch divisor lies in `|(det T_π)^{-2}|`, so `deg B` is even and nothing more. Shirane 1.1.7: the cover is a triple section of a line bundle `L` if and only if `T_π≅L^{-1}⊕L^{-2}`. That is the Cardano/Weierstrass split `E^∨=L^{-1}⊕L^{-2}`, `L=O(k)`, giving `deg B=6k`. An arbitrary split `T_π≅O(a)⊕O(b)` only yields `deg B=2(a+b)`, not divisibility by 6. Rank-2 bundles on `P^2` need not split (`T_{P^2}`, and Horrocks is a vanishing criterion, not a splitting theorem). Shirane Corollary 2.3 is a counterexample even at degree 6: `T_π` is `O(-2)⊕O(-1)` *or* `Ω_{P^2}`. T91 studies non-Galois triple covers via the Cardano discriminant; it does not prove that the resolvent of a residual `S_4` cover has Weierstrass Tschirnhausen module.

A positive answer would give `6∣d` on every stratum with `Π∈V_4`: family-2 `g=2` survivors, and family-3 *constant* stratum. It would kill `(8,6)` only if that curve lay in the constant stratum, which §3.3 already kills by SK-2' filters, or if a non-constant `(8,6)` somehow descended, which SK-5 forbids. Coord:49–50 (“which would close family 3 if resolved”) is false for the non-constant stratum. `FALLACY-v2` forbids filling the splitting gap by cap or analogy. Typed OPEN.

## 8. Narrowed-cage summary and remaining d_min obligation

**Verdict. CONFIRMED** on the residual shapes. The remaining `d_min` obligation is scoped over exactly the typed survivors of SK-1 and SK-4, plus family 3, plus the finite `d≤9` AM-numerical types that sit inside those families. It is not scoped over the four OPEN *names* as if they were four families: two of those names are attack routes.

PIN’s unconditional layer (PIN:220–237) is the Chau cage at `g≥2`:

```text
(u,1):   (d,n)=(gu,g),     g≥2, u≥2
(odd u,2): (d,n)=(gu,2g),  g≥2, u≥3 odd
(4,3):   (d,n)=(4g,3g),    g≥2
```

SK-1 deletes the first column in every `d_min` gauge. SK-4 cuts the second column, at `g=2` only, to `u≡3 (mod 6)`. Family 3 is untouched as a family (constant `g=2` dead; non-constant outer-open). For `d∈{10,12,14,15,16}` PIN lists twenty pairs. Thirteen are `(u,1)` and die by SK-1; `(10,4)` and `(14,4)` die by SK-4 (`u=5,7≢3 (mod 6)`). Five remain, matching SK:593–600:

```text
d=10:  none
d=12:  (12,8)  [g=4, (3,2)] ,  (12,9)  [g=3, (4,3)]
d=14:  none
d=15:  (15,6)  [g=3, (5,2)] ,  (15,10) [g=5, (3,2)]
d=16:  (16,12) [g=4, (4,3)]
```

The same two rules at every degree. First new `g=2` family-2 survivor beyond `(6,4)` is `(18,4)` (`u=9`). Prime degrees contribute no noncoprime Chau escape, as PIN already had.

`OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` is therefore still required, over a strictly smaller cage: one of three columns deleted rather than bounded. Coord:44–51 records this as provisional; the present review confirms the narrowing and rejects Coord’s claim that Tschirnhaus-splitting would close family 3.

Exact remaining residual shapes in a `d_min` gauge:

1. `(odd u,2)`, `g=2`, `u≡3 (mod 6)`, `u≥9` — i.e. `d=18,30,42,…`. (The `u=3` row `(6,4)` is in the finite sweep and is dead only after ROW-NF+ROW-KILL.) Attack name: `OPEN[SHAPE-2-INFINITY-Z3]`.
2. `(odd u,2)`, `g≥3` — including `(9,6),(12,8),(15,6),(15,10),(18,12),…`. Name: `OPEN[SHAPE-2-INNER-g>=3]`.
3. `(4,3)`, `g=2` non-constant — `(8,6)` AM-numerical types. Outer data: one `φ`-orbit.
4. `(4,3)`, `g≥3` — both strata, including `(12,9),(16,12),…`. Name: `OPEN[SHAPE-3-ALL-g]`.

The finite conditional layer of PIN:193–218 (two reviewed delta rows, already target-equivalent, plus six AM-numerical `(8,6)/(9,6)` types) sits inside (3) and (2) and is not enlarged. `(u,1)` appearances such as `(8,4)` and `(10,2)` are non-minimal gauges, not extra residual shapes.

`OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` is not a residual family. A positive answer would constrain only descent strata (`Π∈V_4`), i.e. item 1 and family-3 constants, and would not replace a `d_min` bound on items 2–4.

## 9. Promotion recommendations

| Item | Recommendation | Scope |
|---|---|---|
| SK-0 | **PROMOTE** | Constant BP-tuple is always outer-fixed; charged collapse REFUTED |
| SK-1 | **PROMOTE** | `d_min`-gauge elimination of `(u,1)`; not “no `(u,1)` presentation” |
| SK-2 / SK-2' | **PROMOTE** | `g=2` only; kills trivial products and the `n=2` column |
| SK-3 | **PROMOTE as sufficient** | Nodal `(M-INF)` criterion (2.3); not a tangential kill |
| SK-4 | **PROMOTE** | Kill `g=2`, `u≢3 (mod 6)`; classify surviving outer data, including (3.3) |
| SK-5 | **PROMOTE** | Non-constant family 3, every `g`: `Π` a 3-cycle, no `S_3` descent |
| `(8,6)` constant | **PROMOTE** | Dead by SK-2' filters |
| `(8,6)` non-constant outer orbit | **PROMOTE as outer data** | Not an existence theorem |
| SHAPE-2-INNER-g>=3 | **KEEP OPEN** | Necessary |
| SHAPE-2-INFINITY-Z3 | **KEEP OPEN** | Necessary; (3.4) nodal only |
| SHAPE-3-ALL-g | **KEEP OPEN** | Necessary; family 3 not killed |
| TRIPLE-COVER-TSCHIRNHAUS-SPLIT | **KEEP OPEN** | Necessary; do not consume; does not close family 3 non-constant |
| Narrowed cage / `d_min` | **PROMOTE the narrowing** | Obligation remains, over items 1–4 of §8; not over `(u,1)` |

Do not promote: a uniform kill of families 2 or 3; existence of any `u≡3 (mod 6)`, `u≥9` residual curve; Shirane off degree 6; `6∣d` from Cardano without splitting; Coord’s “Tschirnhaus closes family 3”; any `d_min≤9` bound; A'(5).

Campaign-pin replacement statement PIN:308–315 (`d_min≤9`) is not supplied. After this review the safe ledger is: conditional `d≤9` ledger, plus the four residual shapes of §8, subject only to the promoted coprime theorem on landing, SK-1, SK-4, SK-5, the `g=2` constant kills, and the explicit-family ROW-KILL on `(6,4)` after ROW-NF.

<!-- BODY-END -->

