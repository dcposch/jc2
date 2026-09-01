# TORUS-CHECK — the torus-type test and the affine bridge

lane: pi1s4-64-torus-check
model: opus5
date: 20260831
status: IN-PROGRESS

## 0. Input verification and charged registry

## 1. The row sextic F_j: structure and singularities

## 2. Torus-type decision — Oka/Tokunaga conic criterion

## 3. Torus-type decision — the non-tame A^3 - B^2 loophole

## 4. Projective conclusion (R10)

## 5. The affine bridge: escape (a) — branching along L_infty

## 6. The affine bridge: escape (b) — genericity in R10's sense

## 7. Typed status of the branched-at-infinity object

## 8. Assembly: what is killed, what is OPEN

## 9. Dependency chain and source registry

---

## 0. Input verification and charged registry

The four frozen inputs were rehashed with `shasum -a 256` **before any was read**;
4/4 match the boxed manifest, so the stop condition was not triggered.

```text
a130acb580933543a6909753e665c56295bd4ab052469caa8c84e041766c2467  lit-targeted-endgame-grok46-20260831.md
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  pi1s4-64-zvk-u6-opus5-20260831.md
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  pi1s4-64-triple-cover-close-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

**Literature re-fetched and re-hashed in this lane** (not consumed at registry
paraphrase; the two load-bearing statements are quoted verbatim below).

| tag | source | URL | SHA-256 | pp |
|---|---|---|---|---|
| Sh12 | Shirane, *A note on normal triple covers over `P²` with branch divisors of degree 6*, arXiv:1211.2526v1 | `https://arxiv.org/pdf/1211.2526` | `b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153` | 9 |
| Oka05 | Oka, *Zariski pairs on sextics I*, arXiv:math/0507051v1 | `https://arxiv.org/pdf/math/0507051` | `2a864cdd2530533c30f45d2cf9e9435e24f6a53b3788094df26a63e7208213e4` | 12 |

Both hashes reproduce the charged registry byte-for-byte (`lit-targeted-endgame`
§§1.1, 2.1), an independent confirmation of that lane's receipts.

**Ishida–Tokunaga (R10) was *not* fetched** — Euclid `aspm/05610169` returned HTML.
It is not needed: Sh12 Corollary 0.6 is strictly stronger (see §4) and was fetched.
IT09 is therefore cited only as corroboration, at charged-registry scope.

**Typing used throughout.**

* `PROMOTED` — nothing from the coordinator is re-audited here.
* `PROVISIONAL` — Theorem ROW-NF and the row data `Δ=(6,4,3)`, `δ_aff=3`,
  `δ_∞=7`, three ordinary nodes (charged `pi1s4-64-zvk-u6` §1, itself consuming
  Theorem FOLD's statement); the node datum `a_p=0`; the count `72` and shape
  `(O4)` (**not used**: their definitions are not in any charged input).
* `PROVED-HERE` — §1.3–1.5 (infinity germ re-derivation), §2 (Theorem NO-TORUS,
  four proofs), §3 (the scope finding on the charged cancellation lemma),
  §5 (Theorem INF-TRIVIAL), §7 (assembly).
* `SOURCED` — Sh12 Cor 0.6, Oka05 Prop 2 / Lemma 3, quoted verbatim.

**Execution disclosure.** No CAS was run; no job of uncertain duration was run.
Two `curl` fetches and two `pdftotext` extractions were executed; every
mathematical number below is hand-derived and displayed in full.

---

## 1. The row sextic `F_j`: structure and singularities

### 1.1 The family

Theorem ROW-NF (charged `zvk-u6` §1.3) gives every row member in closed form:

```text
   D_j :  x = r(t)² ,  y = q(t) ,   r = t³+bt+c ,  q = t⁴+(2b/3)t²+(4c/3)t ,  c ≠ 0 ,
```

with modulus `j = b³/c² ∈ C` and the three-ordinary-node stratum
`j ∉ {−27/4, −81/16}`. Everything below is stated on that stratum
(the ROW-SWEEP witness `b=c=1`, `j=1`, lies in it).

### 1.2 The implicit sextic

Write `F_j := Res_t(x − r(t)², y − q(t)) / (leading unit) ∈ C[x,y]`, `F̄_j` its
degree-6 homogenization in `P²`, `C := V(F̄_j)`, `L_∞ := {Z=0}`.

*Degree 6, irreducible.* A generic line `αx+βy+γ` pulls back to a `t`-polynomial of
degree `6` (the `x`-term dominates: `deg r² = 6 > 4 = deg q`), and the parametrisation is
generically injective (ROW-NF: exactly three identified parameter pairs), so
`t ↦ (r(t)²,q(t))` is birational onto its image and `deg C = 6`. The image of an
irreducible variety is irreducible, so `F̄_j` is **irreducible and reduced**.

I do **not** need the expanded coefficients of `F_j` anywhere below. Every step uses
the parametrisation, which is the honest content of the resultant.

### 1.3 The point at infinity (re-derived)

Homogenise: `[X:Y:Z] = [r(t)² : q(t) : 1]`. With `s := 1/t`,

```text
   [r²:q:1] = [ s^{-6}(1+bs²+cs³)² : s^{-4}(1+(2b/3)s²+(4c/3)s³) : 1 ] .
```

Divide by the first entry and pass to the chart `X=1`, `(v,w) := (Y/X, Z/X)`:

```text
   v(s) = s²·U(s) ,  U = (1+(2b/3)s²+(4c/3)s³)(1+bs²+cs³)^{-2} = 1 − (4b/3)s² − (2c/3)s³ + … ,
   w(s) = s⁶·V(s) ,  V = (1+bs²+cs³)^{-2} = 1 − 2bs² − 2cs³ + … .                       (1.1)
```

So `s ↦ 0` gives the single point `Q_∞ = [1:0:0]`, and:

* **one place at infinity**, unibranch (it is the image of one Puiseux branch, and the
  parametrisation is birational);
* `mult_{Q_∞}(C) = min(ord v, ord w) = min(2,6) = **2**`;
* `I(C, L_∞; Q_∞) = ord_s w(s) = **6**`. Bézout `6·1 = 6` is exhausted at `Q_∞`, so
  **`C ∩ L_∞ = {Q_∞}`** and `L_∞` is the *tangent line* of the germ (contact `6 > 2`).

### 1.4 The germ is `A_14` (derived, not consumed)

`C` is rational (parametrised by `A¹`) of degree 6, so `Σ_P δ_P = p_a = (6−1)(6−2)/2 = 10`.
The affine part carries three ordinary nodes (ROW-NF §1.3: the minus-branch system
collapses to `e₁³=0`, forcing `m=0`; the plus branch has the three roots of
`h(e₁)=e₁³+(4b/3)e₁−4c/3`), so `δ_aff = 3` and

```text
   δ_{Q_∞} = 10 − 3 = 7 .
```

A **unibranch germ of multiplicity 2** has semigroup `⟨2, 2k+1⟩` and `δ = k`. Hence
`k = 7`, semigroup `Γ = ⟨2,15⟩`, and the germ is `A_14`. This reproduces the charged
`δ_∞ = 7` and the charge's `3A_1 + A_14`, **from ROW-NF alone**.

### 1.5 The two facts about `A_14` that do the work

Fix the local analytic normal form of the germ: `(ξ,η) = (s^{15}, s²)` (equation
`ξ² = η^{15}`), tangent line `{ξ=0}`.

**(F1) Maximal smooth contact is 15.** Let `S` be any smooth germ at `Q_∞`, `ℓ` its
equation, `ord ℓ = 1`. Write `ℓ = αξ + βη + Σ_{i+j≥2} c_{ij}ξ^iη^j`. On the branch the
monomial `ξ^iη^j` has order `15i + 2j`, so

```text
   ord_s ℓ(γ(s)) ∈ { 2 }  ∪  { 4,6,8,10,12,14 }  ∪  { 15 } ,      max = 15 ,
```

the value `15` occurring only when `β = 0` and `c_{0j} = 0` for `j ≤ 7`. No cancellation
can raise it: the only monomial of order `15` is `αξ` itself (`15i+2j=15 ⟹ (i,j)=(1,0)`).

**(F2) The six conic monomials have distinct orders.** In the chart `X=1` a conic
`G_2/X²` is a combination of `1, v, v², w, vw, w²`, of orders on the branch

```text
   0 , 2 , 4 , 6 , 8 , 12       (all distinct;  10 is absent) .                (1.2)
```

Distinctness means **no cancellation between basis terms**, so for any conic
`a = c_1 + c_2v + c_3v² + c_4w + c_5vw + c_6w²`,

```text
   ord_s a(γ(s)) = min{ order of a term with nonzero coefficient } .           (1.3)
```

`(F1)` and `(1.3)` are the only local input to §2.

---

## 2. Torus-type decision — Oka/Tokunaga conic criterion

**Definition.** `C` is of *(2,3)-torus type* if `F̄_j = G_2³ + G_3²` for homogeneous
`G_i` of degree `i`. Scaling is free: replacing `(G_2,G_3)` by `(λG_2, μG_3)` with
`λ³=μ²=κ` turns the identity into `κF̄_j`, so "up to `C^*`" costs nothing. Over `C`,
`G_2³ + G_3² = G_2³ − (iG_3)²`, so the `±` convention costs nothing either.

Two preliminary facts, both `PROVED-HERE`.

**Lemma 2.1 (coprimality).** `G_2 ≠ 0`, `G_3 ≠ 0`, and `gcd(G_2,G_3)=1`.
*Proof.* `G_2=0` gives `F̄=G_3²`, `G_3=0` gives `F̄=G_2³`, both non-reduced. If `h`
is a common factor then `h³ | G_2³` and `h² | G_3²`, so `h² | F̄` — non-reduced. `[]`

**Lemma 2.2 (no node is inner).** If `G_2(P)=G_3(P)=0` then `P` is *not* an ordinary
node of `C`. *Proof.* Locally `f = a³+b²` with `a(P)=b(P)=0`. Then `ord_P f ≥ min(3,2)=2`,
and the degree-2 part of `f` is the degree-2 part of `b²`, i.e. `b_1²` where `b_1` is the
linear part of `b`. If `b_1 ≠ 0` the tangent cone is a *double line* (rank ≤ 1), not two
distinct lines. If `b_1 = 0` then `ord_P b ≥ 2` and `ord_P f ≥ 3`. Either way `P` is not an
`A_1`. `[]`

Lemma 2.2 already **corrects the framing in the charge**: the charge budgets "passing
through 3 nodes = 3 conditions". For this curve the conic must *avoid* the nodes; they
cannot lie on it at all.

### 2.1 First proof — the conic space is one-dimensional and its member is excluded

Tokunaga's criterion, verbatim from Oka05 p. 3 (fetched, hashed above):

> **Lemma 3.** *(Tokunaga Criterion [14])* The sextic `C` is of torus type if and only
> if there exists a conic `C_2 : g_2(x,y)=0` such that `C_2 ∩ C ⊂ Σ(C)` and
> `I(C,C_2;P) = 2ρ(P,5)` for any `P ∈ C ∩ C_2`.

Only the **"only if"** direction is used, and in the concrete form supplied by the
identity itself: for a torus sextic, `C_2 := V(G_2)` satisfies
`C ∩ C_2 = V(G_2) ∩ V(G_3)` (if `G_2(P)=0` and `F̄(P)=0` then `G_3(P)²=0`) and
`I(C,C_2;P) = I(G_3², G_2; P) = 2·I(G_2,G_3;P)`, whence `Σ_P I(C,C_2;P) = 12` by Bézout.

By Lemma 2.2, `C ∩ C_2 ⊆ Σ(C) ∖ {3 nodes} = {Q_∞}`. So a torus structure forces a conic
with

```text
   I(C, C_2; Q_∞) = 12 .                                                       (2.1)
```

Now compute the space of such conics **exactly**, using `(1.2)`/`(1.3)`. The orders of
the six basis conics on the branch are `0,2,4,6,8,12`; since they are pairwise distinct,
`(2.1)` is equivalent to killing every coefficient whose monomial has order `< 12`:

```text
   coeff(X²)=0  (order 0) ,  coeff(XY)=0  (2) ,  coeff(Y²)=0  (4) ,
   coeff(XZ)=0  (6) ,        coeff(YZ)=0  (8) .
```

That is **five** conditions, not six: order `10` is *absent* from the list `(1.2)`, so no
condition is imposed there. The solution space is therefore exactly

```text
   { G_2 : I(C,G_2;Q_∞) ≥ 12 } = C·Z²  ,   one-dimensional.                    (2.2)
```

The unique candidate is the **double line at infinity**, `C_2 = 2L_∞`. It is excluded:
`G_2 = Z²` gives

```text
   F̄_j = Z⁶ + G_3² = (G_3 + iZ³)(G_3 − iZ³) ,
```

a product of two cubics, contradicting irreducibility of `F̄_j` (§1.2). Hence no
admissible conic exists.

**Theorem NO-TORUS (PROVED-HERE).** *For every `j` on the three-ordinary-node stratum,
the row sextic `F̄_j` is **not** of (2,3)-torus type.*

The computation is worth restating because it is the whole content: the row's `A_14`
place has value semigroup `⟨2,15⟩`, and the six conic monomials realise the orders
`0,2,4,6,8,12` on it. Contact `12` at a single point is *just* attainable — by `Z²`
alone — and `Z²` is exactly the degenerate solution that makes the sextic split.

### 2.2 Second proof — Oka's `ρ`-count, i.e. the tame list turned into an argument

Oka05 p. 2 (verbatim, same fetch): if `C_3` is non-singular at an inner `P`, the germ is
`A_{3ι−1}` with `ι = I(C_2,C_3;P)`; if `C_3` is singular at `P`, the germ is simple only
when `C_2` is smooth at `P` and `ι = 2`, in which case it is `E_6`. And:

> **Proposition 2.** Assume that `T` is a sextic of torus type and `P` be an inner simple
> singularity. Then `ρ(P,5) = ι(C_3,C_2;P)`. Thus `Σ_{P:inner} ρ(P,5) = 6` for a sextics
> of torus type with only simple singularities.

All singularities of `C` are simple (`3A_1 + A_14`), and every inner point is a
singularity of `C`, so every inner point is an *inner simple* singularity. The admissible
inner types are therefore `{A_2, A_5, A_8, A_11, A_14, A_17, …} ∪ {E_6}`. A node is
`A_1`, and `A_1 = A_{3ι−1}` would need `ι = 2/3`; `A_1 ≠ E_6`. So the three nodes are
**outer** (independent confirmation of Lemma 2.2), and the only possible inner point is
`Q_∞`, of type `A_14 = A_{3·5−1}`, contributing `ρ = ι = 5`. Then

```text
   Σ_{P inner} ρ(P,5)  ∈  {0, 5}  ≠  6 ,
```

contradicting Proposition 2. `[]`

The residue `6 − 5 = 1` is the sharp statement of what is missing: a torus sextic with an
inner `A_14` needs one further inner point of `ι = 1`, i.e. a **cusp** `A_2`. The row has
no cusp — its three extra singularities are nodes. This is precisely the registry's
observation (R12) that the tame list's `(5,1)` slot is `[A_14, A_2]` and that `[A_14,3A_1]`
appears nowhere; §2.1 and §2.2 upgrade that observation from "absent from a list" to a
proof, by showing the nodes must be outer and the Bézout residue then cannot be paid.

---

## 3. Torus-type decision — the non-tame `A³ − B²` loophole

### 3.1 Scope finding: the charged cancellation kill does **not** cover this identity

The charge asks whether the charged `triple-cover-close` cancellation kill "covers
exactly the `A³−B² = c·F` identity needed here, all scaling conventions matched".
**It does not, and the mismatch is directional, not a matter of conventions.**

*Conventions do match.* Dehomogenising a torus identity at `Z=1` gives
`F = A³ + B²` with `A = G_2|_{Z=1}` of degree `≤ 2` and `B = G_3|_{Z=1}` of degree `≤ 3`;
replacing `B` by `iB` gives `A³ − B² = F`. Conversely, homogenising `A³ − B² = F` to
degree `6` returns `(A^h)³ − (B^h)² = F̄` because `deg F = 6` exactly. So

```text
   C is of torus type  ⟺  ∃ A,B ∈ C[x,y] :  A³ − B² = F ,  deg A ≤ 2 , deg B ≤ 3 .   (3.1)
```

*But the charged lemma runs the other way.* Charged `triple-cover-close` §4 opens the
numerical bands `(deg A, deg B) = (2k,3k)`, `k ≥ 2`, i.e. `(4,6),(6,9),(8,12),(10,15)`
(display (4.4)), and §5 eliminates all four, concluding display (5.6):

```text
   deg A ≤ 2   and   deg B ≤ 3 .
```

That is the **conclusion** `(3.1)` needs as a **hypothesis**. The charged lemma
therefore *delivers the torus band*; it does not exclude it. The kill of the low band in
charged §6 is outsourced to the *uncharged* `triple-cover-r2` report (its "leading-form
classification, lines 167–222" and "infinity calculation, lines 224–270"), which is not
among my inputs and which I cannot audit. Per FALLACY-v2 (carrier/attainment; no filling
a gap by analogy) I do not consume it.

§3.2 supplies the missing low-band kill directly, in four lines, from ROW-NF alone.

### 3.2 Third proof — the parametrisation forces `A` constant

Assume `(3.1)`. Set `a(t) := A(r(t)²,q(t))`, `b(t) := B(r(t)²,q(t)) ∈ C[t]`. Since
`F` vanishes on the image, `a³ = b²`.

*Step 1: `a` has no root.* If `a(t_0)=0` then `b(t_0)²=0`, so the point
`p_0 := (r(t_0)², q(t_0))` lies in `V(A,B) ∩ C²`. But `A(p_0)=B(p_0)=0` forces
`F(p_0)=0` and, by Lemma 2.2, `p_0` is a singular point of `C` that is not an ordinary
node. The affine singularities of `C` are exactly three ordinary nodes, so no such `p_0`
exists. Hence `a = α ∈ C^*`.

*Step 2: `A` is constant.* Substituting `x = r(t)²` (degree `6`, monic) and `y = q(t)`
(degree `4`, monic), the six monomials of a degree-`≤2` polynomial acquire the **pairwise
distinct** `t`-degrees

```text
   x² ↦ 12 ,   xy ↦ 10 ,   y² ↦ 8 ,   x ↦ 6 ,   y ↦ 4 ,   1 ↦ 0 .              (3.2)
```

Reading `a(t) = α` in descending degree gives, in order,
`a_{20}=0`, then `a_{11}=0`, then `a_{02}=0`, then `a_{10}=0`, then `a_{01}=0`
(each coefficient is the unique new contributor at its degree, the previous ones having
already been set to zero). So `A ≡ α ∈ C^*`.

*Step 3: contradiction.* Then `F = A³ − B² = α³ − B²`, of degree `6`, so `deg B = 3` and

```text
   F = (α^{3/2} − B)(α^{3/2} + B) ,
```

a product of two cubics — contradicting irreducibility of `F`. `[]`

### 3.3 Fourth proof — projective Bézout against maximal contact

Independent of §3.2, and degree-free in `A`:

Assume `F̄ = G_2³ + G_3²`. As in §2, `C ∩ V(G_3) = V(G_2) ∩ V(G_3) ⊆ Σ(C)`, and by
Lemma 2.2 no node qualifies, so

```text
   C ∩ V(G_3) = V(G_2) ∩ V(G_3) = { Q_∞ }     (nonempty by Bézout on the conic/cubic).
```

*`G_3` is smooth at `Q_∞`.* `mult_{Q_∞} F̄ = 2` (§1.3), while
`mult(G_2³+G_3²) ≥ min(3·mult G_2, 2·mult G_3) ≥ min(3, 2·mult G_3)`. If
`mult_{Q_∞} G_3 ≥ 2` the right side is `≥ 3`, forcing `mult F̄ ≥ 3`. So
`mult_{Q_∞} G_3 = 1`.

*Bézout.* `F̄` (degree 6, irreducible) and `G_3` (degree 3) share no component, so
`Σ_P I(F̄,G_3;P) = 18`, all of it at `Q_∞`. The germ of `F̄` at `Q_∞` is unibranch, so
`I(F̄,G_3;Q_∞) = ord_s G_3(γ(s))`, and `G_3` is locally a unit times a **smooth** germ.
By `(F1)` of §1.5 that order is at most `15`. Then `18 ≤ 15`. `[]`

The consistency of the two Bézout ledgers is worth recording, because it shows where the
obstruction actually lives. On the branch, `α := G_2|_γ`, `β := G_3|_γ` satisfy
`α³ = −β²`, so `3·ord α = 2·ord β`; the two Bézout totals `I(F̄,G_2)=12` and
`I(F̄,G_3)=18` give `ord α = 12`, `ord β = 18`, and `3·12 = 2·18` ✓. **Both values lie in
the semigroup `Γ = ⟨2,15⟩`** — so the semigroup imposes no obstruction whatever. The
obstruction is the *multiplicity-one* constraint: `18 ∈ Γ` is realisable only by a germ of
multiplicity `≥ 2`, and `mult_{Q_∞}G_3 = 1` is forced.

### 3.4 Status of the four proofs

| route | input used | independent of |
|---|---|---|
| §2.1 conic space `= C·Z²` | `(1.2)`, irreducibility | any literature theorem |
| §2.2 `Σρ = 6` vs `5` | Oka05 Prop 2 (fetched, hashed) | §2.1, §3 |
| §3.2 parametrisation | ROW-NF, 3 nodes, irreducibility | all projective input |
| §3.3 Bézout vs max contact | `(F1)`, `mult=2`, 3 nodes | §2, §3.2 |

Each is a complete proof of Theorem NO-TORUS on its own; §2.1 and §3.2 use no fetched
source at all. The `A_1`-vs-`A_{3ι−1}` fact (Lemma 2.2) is common to three of them and
is elementary. I therefore treat Theorem NO-TORUS as settled at the scope of its
hypotheses: `F̄_j` irreducible of degree 6, affine singularities exactly three ordinary
nodes, germ at infinity `A_14`.

**Scope caveat (recorded, not waived).** Lemma 2.2 fails for germs of type `A_{3ι−1}`.
On the two excluded moduli `j ∈ {−27/4, −81/16}` the affine singular configuration
degenerates (`δ_aff = 3` still, but the type is not `3A_1`); if such a member carried an
affine `A_2` or `A_5`, that point *could* be inner and §2/§3 would not close it. Those
members are outside the campaign's residual, which is the explicit three-node curve.

---

## 4. Projective conclusion

### 4.1 The theorem consumed, verbatim

Sh12 (fetched and hashed in §0), Corollary 0.6, p. 2:

> **Corollary 0.6.** Let `Δ` be a divisor of degree 6 on `P²`. Then there is a normal
> triple cover `π` with `Δ_π = Δ` if and only if there are homogeneous polynomials
> `G_i(x_0,x_1,x_2)` of degree `i` for `i = 1,2` [read `i = 2,3`; the displayed identity
> is `G_2³+G_3²`] with the following three conditions:
> (1) `G_2³ + G_3² = 0` defines `Δ`;
> (2) `G_2 ∉ m_E` or `G_3 ∉ m_E²` for any prime divisor `E`; and
> (3) `G_2 ∈ m_E` or `G_2³ + G_3² ∉ m_E²` for any prime divisor `E`.

Notation, from Sh12 p. 2: a *cover* is a finite flat morphism; a *normal triple cover* is
a degree-3 cover of normal varieties; `Δ_π = S_π + 2T_π` is the **branch divisor**, `π`
being ramified with index 2 along `S_π` and index 3 along `T_π`; `Δ_π := S_π + T_π` is the
reduced branch locus. Remark 0.2 records that a finite surjective morphism from a normal
surface to a smooth surface is automatically a normal cover — so no flatness hypothesis
has to be checked by hand.

**Why this and not R10 (IT09 Thm 1.1).** Sh12 Cor 0.6 is strictly stronger for my
purposes on three counts: it needs **no simple-singularity hypothesis**, it needs **no
genericity hypothesis** (no "finitely many total branch points"), and it is an **iff for
arbitrary normal triple covers**, not only non-Galois generic ones. Sh12 Rem 0.7(iv)
states explicitly that it generalises the Ishida–Tokunaga result. Escape (b) of the
charge — "the extension is not generic in R10's sense" — is therefore closed by
*replacing the theorem*, not by verifying genericity; see §6.

### 4.2 What dies

**Proposition 4.1 (PROVED-HERE).** *Let `ψ : π₁(C²−D_j) → S_3` be any homomorphism with
all meridians of `D_j` mapping to transpositions and with `ψ` surjective, and suppose
`ψ(γ_∞) = 1` for a meridian `γ_∞` of `L_∞`. Then a contradiction follows.*

*Proof.* `π₁(P²−F̄_j)` is the quotient of `π₁(P²−(F̄_j∪L_∞)) = π₁(C²−D_j)` by the normal
closure of `γ_∞`, so `ψ` descends to a surjection `ψ̄ : π₁(P²−F̄_j) ↠ S_3`. Let
`X` be the normalisation of `P²` in the degree-3 field extension attached to the
`S_3`-action on 3 points; `X` is normal, irreducible (`S_3` is transitive), and
`X → P²` is finite surjective, hence a normal triple cover (Sh12 Rem 0.2).

Its branch divisor: over a generic point of `F̄_j` the local monodromy is a transposition,
so `F̄_j ⊆ S_π` with index 2 and multiplicity 1 in `Δ_π`. Nothing else is in the branch
locus: `ψ̄` is defined on `π₁(P²−F̄_j)`, so `X → P²` is étale over `P² ∖ F̄_j`. Hence

```text
   S_π = F̄_j ,   T_π = 0 ,   Δ_π = F̄_j ,   deg Δ_π = 6 .
```

Corollary 0.6 now applies and its "only if" direction gives condition (1): `F̄_j` is
defined by `G_2³+G_3²`, i.e. `F̄_j` is of `(2,3)`-torus type. This contradicts Theorem
NO-TORUS. `[]`

The object that dies, stated exactly as the charge asks: **the `S_3` resolvent cover of
the campaign's hypothetical `φ`, extended to `P²` with branch divisor of degree 6 — i.e.
with ramification only along `F̄_j`, and none along `L_∞`.** Two escapes remain, and are
the subject of §§5–6:

```text
 (a)  ψ(γ_∞) ≠ 1 : the projective extension also ramifies along L_∞ ;
 (b)  the extension fails some hypothesis of the consumed theorem.
```

Nothing in Proposition 4.1 has yet been said about `S_4`: the passage from `φ : π₁ ↠ S_4`
to `ψ` is `φ` followed by `S_4 ↠ S_4/V = S_3`, which sends transpositions to
transpositions and preserves surjectivity. That is Theorem ZVK-RESOLVENT of the charged
`zvk-u6` §5.4 in its downstairs form; here it is a one-line composition and needs no
braid data.

---

## 5. The affine bridge: escape (a) — branching along `L_∞`

This is the new work. The campaign's `φ` lives on `C²−D_j`; the theorems of §4 live on
`P²`. The gap is one element: `ψ(γ_∞)`, the image of the meridian of the line at
infinity. I compute it exactly, with no braid-monodromy data.

### 5.1 What is a priori available

`H_1(C²−D_j) = Z⟨g⟩` (`D_j` irreducible), and `γ_∞ = 6g` there (a generic line meets
`D_j` in 6 points). The sign character `S_3 → Z/2` kills `γ_∞` because `6` is even, so

```text
   ψ(γ_∞) ∈ A_3 ≅ Z/3   —   and, S_4-side,  φ(γ_∞) ∈ A_4 .                    (5.1)
```

`Z/3` is abelian, so `ψ(γ_∞)` is a **well-defined element**, independent of the choice of
meridian (all meridians of `L_∞` are conjugate). Abelianisation gives nothing further: the
dichotomy `ψ(γ_∞) ∈ {e, 3-cycle}` is genuine at this level. This is exactly the charge's
"is the `L_∞` meridian image trivial or a 3-cycle" question.

### 5.2 The three identifications at `x = 0`

Project along `x`. `D_j → C_x` is a 6-section (`r(t)² = x` has six roots). Over `x = 0`
the six points collide **in three disjoint pairs**: `r(t)² = 0 ⟺ r(t) = 0`, whose roots
`τ_1,τ_2,τ_3` are simple and distinct on the stratum `j ≠ −27/4`. Near `x=0`,
`r(t) = ±√x` gives `t = τ_i ± √x/r'(τ_i) + O(x)` and

```text
   y = q(τ_i) ± ( q'(τ_i)/r'(τ_i) ) √x + O(x) ,   i = 1,2,3 ,                   (5.2)
```

with `q'(τ_i) ≠ 0` (`q' ≡ −(8/3)(bt+c) mod r`, and `bt+c` shares no root with `r` unless
`c=0`, excluded). So each pair is a two-valued branch swapping under `x ↦ e^{2πi}x`: the
local braid at `x=0` is a product of **three simultaneous, pairwise disjoint half-twists**.
In a geometric basis of the base fibre `{x = x_*}` (`|x_*|` small) adapted to the three
clusters — indices `{1,2}`, `{3,4}`, `{5,6}` in cluster order — this is
`β_0 = σ_1σ_3σ_5`. This is the charged `zvk-u6` §3.2 datum, re-derived here.

The Zariski–van Kampen relation `β_0·T = T` for a half-twist on adjacent strands is the
**identification** of the two meridians, so in `G := π₁(C²−D_j)`:

```text
   g_1 = g_2 ,   g_3 = g_4 ,   g_5 = g_6 .                                      (5.3)
```

*Exponent cross-check.* `e(ρ_∞) = 3·1 (the three σ's at x=0) + 2·1 (the two simple
vertical tangencies at the roots of r′) + 3·2 (the three nodes) = 11`, matching the
independent Puiseux computation `16 − 5 = 11` of charged `zvk-u6` §2.4. The three
half-twists at `x=0` are counted once each, so `(5.3)` is three relations, not six.

### 5.3 The product of a geometric basis

For a geometric basis `(g_1,…,g_6)` of `π₁(ℓ ∖ (ℓ∩D_j))` on a fibre line
`ℓ = {x=x_*}`, the ordered product `g_6g_5g_4g_3g_2g_1` is the class of a large circle,
i.e. the boundary of a disc around the point at infinity of `ℓ`. That point is
`Q' = [0:1:0]`, the base point of the pencil, and **`Q' ∉ D̄_j`**: by §1.3 the only point
of `D̄_j` on `L_∞` is `Q_∞ = [1:0:0] ≠ Q'`. Hence the large circle is a genuine meridian
of `L_∞` in `P² ∖ (F̄_j ∪ L_∞)`:

```text
   γ_∞ = g_6 g_5 g_4 g_3 g_2 g_1     (in the adapted geometric basis).           (5.4)
```

Combining `(5.3)` and `(5.4)`, **in `G` itself**:

```text
   γ_∞ = g_5² g_3² g_1²  .                                                       (5.5)
```

The bracketing works because the adapted basis has the two members of each cluster at
*adjacent* indices — the same adjacency that makes `β_0 = σ_1σ_3σ_5` a product of the
*standard* generators. Under the opposite ordering convention one gets
`γ_∞ = g_1²g_3²g_5²`; the conclusion below is identical.

### 5.4 The theorem

**Theorem INF-TRIVIAL (PROVED-HERE).** *Let `H` be any group and `χ : G → H` a
homomorphism sending every meridian of `D_j` to an **involution** (in particular: to a
transposition of `S_3` or of `S_4`). Then `χ(γ_∞) = 1`.*

*Proof.* By `(5.5)`, `χ(γ_∞) = χ(g_5)²χ(g_3)²χ(g_1)²`, and each factor is the square of
an involution. `[]`

Three consequences, in increasing strength.

1. `ψ(γ_∞) = 1` for the `S_3` resolvent. **Escape (a) closes**: the projective
   extension of the resolvent triple cover does **not** ramify along `L_∞`, and
   Proposition 4.1 applies verbatim.
2. `φ(γ_∞) = 1` already at the `S_4` level: the hypothetical quadruple cover also
   extends to `P²` unramified along `L_∞`, with branch divisor `F̄_j` of degree 6.
3. The result is **tuple-independent**. It is a relation in `G`, not a property of a
   particular admissible tuple, so it holds for *every* candidate simultaneously and
   needs no enumeration, no `(O4)` shape, and no count `72`. The charge's plan — compute
   the `L_∞`-meridian image "under the `S_3` resolvent of the `(O4)`-shape tuples" — is
   answered without having to know what those tuples are; and that is fortunate, since
   the definitions of `(O4)` and of the `72` count are in no charged input.

### 5.5 A conflict to adjudicate, stated plainly

Charged `zvk-u6` §4.2 quotes, as promoted-from-`FIXED-TUPLE` and `PROVISIONAL`, a
downstairs slice value `(c(Π), g_L) = (2,1)`, where `Π` is the product of the six
transpositions in a generic fibre. Theorem INF-TRIVIAL gives `Π = e`, hence `c(Π) = 4`
and (Riemann–Hurwitz on the fibre line, `2g−2 = 4(−2)+6+(4−c(Π))`) `g_L = 0`.
**These disagree.**

I flag rather than reconcile, and record what each rests on. My value rests on `(5.3)`
(charged `zvk-u6` §3.2, `PROVED-HERE` there, re-derived in §5.2 above) plus the
elementary identity `(5.4)`. The `(2,1)` value comes from `FIXED-TUPLE`, which is *not*
a charged input here, so I cannot see its derivation. One observation may locate the
error: `zvk-u6` §4.2 justifies the downstairs value by "the line `x = c` … meets `D̄` at
`Q_D` where the place is unibranch of multiplicity 2". That justification cannot be
right for the `x`-pencil: the lines `x = c` all pass through `Q' = [0:1:0]`, whereas
`D̄_j ∩ L_∞ = {[1:0:0]}` (§1.3). The description fits the **upstairs** pencil, where
`D̄'` (a quartic) does pass through `Q'`. A slice datum computed for `U_6` and
transcribed downstairs would produce exactly this symptom.

Note also that even the *weaker*, tuple-free consequence `(5.1)` already narrows sharply:
if `φ(γ_∞)` were of `(2,2)` type it lies in `V`, so `ψ(γ_∞) = 1` and Proposition 4.1
fires anyway. Under the promoted `c(Π) = 2` the only surviving case would be
`φ(γ_∞) =` a 3-cycle. Theorem INF-TRIVIAL removes even that.

---

## 6. The affine bridge: escape (b) — genericity in `R10`'s sense

**Primary answer: the escape is void because the consumed theorem has no such
hypothesis.** Sh12 Cor 0.6 quantifies over *all* normal triple covers with
`deg Δ_π = 6`; it assumes neither "generic" (finitely many total branch points), nor
non-Galois, nor simple singularities, nor smoothness of `X`. The only typing to check is
`Δ_π = F̄_j` with `deg = 6`, done in Proposition 4.1, plus normality of `X`, which holds
by construction (normalisation) and is not even a hypothesis by Sh12 Rem 0.2.

**Redundant answer: the genericity hypothesis of R10 holds anyway.** Should a successor
prefer to route through IT09 Thm 1.1, all of its hypotheses are met:

* `F̄_j` is reduced with at worst simple singularities (`3A_1 + A_14`; `A_n` is ADE) ✓;
* the branch locus is exactly `F̄_j` ✓ (Proposition 4.1);
* *finitely many total branch points* ✓. A total branch point needs local monodromy
  containing a 3-cycle. At a generic point of `F̄_j` the monodromy is a transposition, so
  the total-branch locus is a proper closed subset of `F̄_j`, hence finite. Concretely it
  is contained in `Sing(F̄_j) = {N_1,N_2,N_3,Q_∞}`, and at the three nodes it is empty:
  the two branch meridians commute in `S_4` (charged `a_p=0`: they are disjoint), and `S_3`
  has no pair of disjoint transpositions, so their `S_3`-images are **equal** and the local
  group is `Z/2` — no 3-cycle;
* *non-Galois* ✓: the Galois group of the closure is `S_3` (`ψ̄` is onto), so the degree-3
  cover is not Galois.

Both escapes named in the charge are therefore closed, (a) by Theorem INF-TRIVIAL and (b)
twice over.

---

## 7. Typed status of the branched-at-infinity object

By §5 this object **does not arise** for the `(6,4)` row. It is typed here anyway,
because it is the correct successor target if `(5.3)` is ever disputed, and because the
`(8,4)` and `(8,6)/(9,6)` rows may present it.

```text
OBJ[BRANCHED-AT-INFTY-TRIPLE-PLANE]:
  π : X → P² normal triple cover, X normal irreducible,
  S_π = F̄  (index 2, transposition monodromy, deg 6) ,
  T_π = L_∞ (index 3, total ramification along a line) ,
  Δ_π  = F̄ + 2 L_∞ ,  deg Δ_π = 8 ,  reduced branch locus F̄ ∪ L_∞ of degree 7 ,
  Tschirnhausen: π_*O_X = O ⊕ E with deg(det E^∨) = 4 ,
                 so E^∨ ∈ { O(1)⊕O(3), O(2)⊕O(2), non-split with c_1 = 4 } .
```

**Literature status.** The charged registry's `R8` (CM25 §5, Prop 19–20) and `R9`/`R11`
(Sh12 Thm 0.3, Cor 0.6) are stated for `deg Δ_π = 6` and do not reach `deg Δ_π = 8`.
Sh12's introduction lists the solved cases as
`(deg S_π, deg T_π) ∈ {(2,1),(2,2),(4,0),(4,1)}` (Tokunaga, Yasumura) plus `T_π = 0`,
`deg S_π = 6` (Ishida–Tokunaga) — the case `(6,1)` needed here is **not** among them.
CM25's title covers branch curves of degree at most 10 and is the single acquisition
target; the charged registry extracted only its degree-6 section, so this is a genuine
`SOURCE-OPEN`, not a refutation.

**Equivalent form, for a successor.** With `sign∘ψ` unchanged, such a cover has Galois
closure `W → Z → P²` where `Z` is the double plane `z² = F̄` (a `K3` after resolving its
`3A_1 + A_14`), `L_∞` splits in `Z` into two rational curves `L̃_1, L̃_2` meeting over
`Q_∞` (because `F̄|_{L_∞} = c·ℓ^6` is a perfect square), and `W → Z` is a cyclic `Z/3`-cover
totally branched along `L̃_1 + L̃_2` and étale over the preimage of `F̄` (the inertia
`⟨τ⟩ ≅ Z/2` at `F̄` meets `A_3` trivially). Existence is then a **3-divisibility question
in `NS` of the resolved `K3`**: `∃ L` with `3L ≡ L̃_1' + 2L̃_2' + (exceptional correction
along the `A_14` chain)`, the two coefficients being `1` and `2` because the covering
involution of `Z/P²` swaps `L̃_1, L̃_2` and inverts the `Z/3`. That is the Tokunaga
`D_{2n}`-cover machinery (registry `R15`/`R18`) in the one configuration those papers do
**not** cover: `ACT08`'s hypothesis `C_2 ∩ Sing(C_1) = ∅` fails here, since
`L_∞ ∋ Q_∞ ∈ Sing(F̄)`.

```text
OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW]  (typed, not on the (6,4) critical path):
  classify normal triple covers of P² with Δ_π = S + 2T, deg S = 6, deg T = 1,
  S of type 3A_1+A_14 and T its tangent line at the A_14 place;
  equivalently decide the NS-3-divisibility above.
  Acquisition: CM25 (arXiv:2512.07965) degree-7/8 sections; Yasumura (deg S,deg T)=(4,1).
```

---

## 8. Assembly: what is killed, what is OPEN

**Theorem ROW-KILL (PROVED-HERE, at PROVISIONAL row-geometry scope).**
*Let `D_j` be a row member on the three-ordinary-node stratum `j ∉ {−27/4, −81/16}` of
Theorem ROW-NF. There is **no** surjection*

```text
   φ : π₁(C² − D_j)  ↠  S_4      with every meridian of D_j a transposition.
```

*Proof (full chain).*

1. **Geometry.** `F̄_j` is an irreducible plane sextic; its affine singularities are three
   ordinary nodes; `F̄_j ∩ L_∞ = {Q_∞}` with `I = 6`; the germ at `Q_∞` is unibranch of
   multiplicity 2 with `δ = 7`, i.e. `A_14`, semigroup `⟨2,15⟩` (§1, from ROW-NF).
2. **Not torus type.** `F̄_j ≠ G_2³+G_3²` for any `G_2,G_3` (Theorem NO-TORUS, §2–§3;
   four independent proofs, two of them using no external source).
3. **Resolvent.** `ψ := (S_4 ↠ S_4/V = S_3) ∘ φ` is onto `S_3` and sends every meridian
   to a transposition.
4. **No branching at infinity.** In `G = π₁(C²−D_j)`, `γ_∞ = g_5²g_3²g_1²`, so
   `ψ(γ_∞) = 1` (Theorem INF-TRIVIAL, §5). The two identifications feeding this are the
   three simultaneous disjoint half-twists over `x=0` and the geometric-basis product
   identity.
5. **Contradiction.** `ψ` descends to `π₁(P²−F̄_j) ↠ S_3`, whose normalised triple cover
   is a normal triple cover of `P²` with `Δ_π = F̄_j`, `deg Δ_π = 6`. Sh12 Cor 0.6 (fetched,
   hashed, quoted verbatim) forces `F̄_j` to be of `(2,3)`-torus type, contradicting 2. `[]`

**Campaign consequences.**

| item | before | after |
|---|---|---|
| `OPEN[PI1S4-(6,4)-FIXED-TUPLE]` | OPEN | **resolved NO** |
| `OPEN[PI1S4-(6,4)-TRIPLE-COVER]` | OPEN, priority raised | **resolved NO** (step 5 alone) |
| `OPEN[PI1S4-(6,4)-TRIPLE-COVER-GLOBAL-MONOGENICITY-ROW]` | OPEN | **vacuous**: the charged class `C_F` is empty, hence `R_{F,S4}^{nm}` of display (7.1) is empty |
| `OPEN[PI1S4-(6,4)-FACTORIZATION]` / the queued AWS braid job | the deciding computation | **not needed**; the row is decided by algebra + one sourced classification, as the charge anticipated |
| `OPEN[PI1S4-(6,4)-FOLD-ZVK-U6]` / `-FOLD-EQUIVARIANT` | retired into FACTORIZATION | **dead**: by `zvk-u6` Thm ZVK-RESOLVENT, `Γ ↠ S_4` implies `G ↠ S_3`, refuted in step 5 |
| row `(8,4)` | provisionally target-equivalent | **not transferred**. Charged `triple-cover-close` §6 records that the shear does not transport a fixed `B_6` tuple to a fixed `B_8` tuple, and that the fold is only a pullback-surjectivity statement. A `(8,4)` kill needs its own §1-style geometry. |

**Residuals and caveats, none of them repairable by cap or analogy.**

* `R1 — ROW-NF is PROVISIONAL.` The whole chain is conditional on Theorem FOLD's
  statement and the ROW-SWEEP row data. Nothing here upgrades them.
* `R2 — stratum.` The two excluded moduli `j ∈ {−27/4,−81/16}` are outside the theorem
  (§3.4). If a successor needs them, the missing input is the affine singularity type
  there: only an `A_2` or `A_5` (or multiplicity `≥3`) could be inner and reopen §2.
* `R3 — the c(Π) conflict (§5.5)` must be adjudicated by the coordinator, since
  `FIXED-TUPLE` is not a charged input here. If `(5.3)` were wrong, §5 falls, §4 becomes
  conditional, and `OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW]` (§7) becomes the live residual.
  **Theorem NO-TORUS is unaffected either way.**
* `R4 — Sh12 Cor 0.6 is consumed as a published theorem`, quoted verbatim from the fetched
  PDF. Its proof was not re-verified. The `i = 1,2` in its statement is a typo for
  `i = 2,3`, resolved by the displayed identity `G_2³+G_3²`.

---

## 9. Dependency chain and source registry

### 9.1 What each result consumes

```text
 §1  geometry of F̄_j            ← ROW-NF (PROVISIONAL) + classical Puiseux/genus. Nothing else.
 §2.1 conic space = C·Z²        ← §1 orders (1.2) + irreducibility. NO literature.
 §2.2 Σρ = 6 vs 5               ← Oka05 Prop 2 (fetched, hashed, verbatim) + §1 types.
 §3.2 parametrisation proof     ← ROW-NF + three ordinary nodes + irreducibility. NO literature.
 §3.3 Bézout vs max contact     ← §1.5 (F1) + mult 2 + three ordinary nodes.
 §4  Proposition 4.1            ← Sh12 Cor 0.6 (fetched, hashed, verbatim) + Theorem NO-TORUS.
 §5  Theorem INF-TRIVIAL        ← the x=0 collision (5.2), re-derived here; charged
                                  zvk-u6 §3.2 agrees. + geometric-basis product (5.4).
 §8  Theorem ROW-KILL           ← §1 + §2/§3 + §5 + §4.
```

**Not consumed anywhere:** the shape `(O4)`, the count `72`, `e(ρ_∞)=11` (used only as a
cross-check), `M_∞ = 16`, `β₁ = 15`, the promoted `(c(Π),g_L)=(2,1)`, the charged
cancellation lemma (5.6), the `triple-cover-r2` leading-form/infinity analysis, and any
braid-monodromy factorisation. The node datum `a_p = 0` is used only in the redundant
genericity check of §6, never in the kill.

### 9.2 Sources

```text
 Sh12   arXiv:1211.2526v1, 9 pp,  b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153
        Corollary 0.6 (p. 2), Theorem 0.3 (p. 2), Remarks 0.2, 0.5, 0.7 — quoted §4.1, §7.
 Oka05  arXiv:math/0507051v1, 12 pp, 2a864cdd2530533c30f45d2cf9e9435e24f6a53b3788094df26a63e7208213e4
        p. 2 inner-singularity calculus, Proposition 2, Lemma 3 — quoted §2.
 IT09   NOT FETCHED (Euclid aspm/05610169 served HTML). Cited only as corroboration at
        charged-registry scope; superseded for this lane by Sh12 Cor 0.6.
 CM25   arXiv:2512.07965 — acquisition target for §7 only; not fetched, not consumed.
```

Both fetched hashes reproduce the charged `lit-targeted-endgame` registry byte-for-byte.

### 9.3 Corrections and promotion candidates

**Corrections to carry.**

1. The charge's condition count for Oka's criterion ("passing through 3 nodes = 3
   conditions") is **inverted**: by Lemma 2.2 the conic must *miss* the nodes. The correct
   count is 5 conditions concentrated at `Q_∞` on the 6-dimensional space of conics,
   leaving the 1-dimensional space `C·Z²` (§2.1).
2. The charged `triple-cover-close` cancellation lemma (5.6) does **not** cover the torus
   identity; it produces the torus band `deg A ≤ 2, deg B ≤ 3` rather than excluding it
   (§3.1). Composed with §3.2 it does yield the unconditional statement that
   `A³ − B² = F` has **no** solution at any degree — i.e. the affine resolvent is never
   monogenic — but the low band is supplied here, not there.
3. `(c(Π), g_L) = (2,1)` downstairs conflicts with `Π = e`, `(c,g_L) = (4,0)` (§5.5).

**Promotion candidates** (row-level, stated with their hypotheses):
Theorem NO-TORUS (§2, four proofs); Lemma 2.2 (`A_1` and, more generally, any germ not of
type `A_{3ι−1}`/`E_6`, is never an inner singularity of a torus sextic); the exact conic
space `(2.2)`; Theorem INF-TRIVIAL (§5.4) — note it is stated for *any* involution-valued
target and so is reusable on other rows; Proposition 4.1; Theorem ROW-KILL (§8).

### 9.4 Non-claims

No exit price is asserted and no `charge_basis` line is declared. Nothing here upgrades
ROW-NF or Theorem FOLD from `PROVISIONAL`; Theorem ROW-KILL inherits that scope. Nothing
here bears on `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`, `OPEN[NA-AGGREGATE-REDUCIBLE]`,
`OPEN[ROW-(8,6)-NODAL-REALIZATION]`, `OPEN[ROW-(9,6)-NODAL-REALIZATION]`,
`OPEN[NORI-BC-SELF-TANGENT-COEFF]`, `OPEN[PI1S4-D1-DEGREE]`, or on rows `(8,4)`, `(8,6)`,
`(9,6)`. No canonical ledger, charged file, or `jc2-lean` artefact was read or written.

<!-- BODY-END -->
