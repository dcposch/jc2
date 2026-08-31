# NORI-BC: extending Nori 3.27 past nodality, or equisingular nodalization

Lane: NORI-BC (wave-10). Target: OPEN[PI1S4-TANGENTIAL-NONCOPRIME], item (ii)
of the N=4 residual decision report.

## Contents

- 0. Provenance and hash ledger
- 1. What Nori actually proves (§3, verbatim consumption)
- 2. The transversality consumption, located exactly
- 3. Route (a): one blow-up at each tacnode — bookkeeping and verdict
- 4. Route (b): local replacement of transversality at a tangency
- 5. Route (c): can 3.26 (B(C)>0, C ∩ R = ∅) substitute?
- 6. (ii-a) Equisingular-at-infinity nodalization
- 7. Verdicts, typed OPENs, and what is proved unconditionally
- 8. Successor packet

<!-- SECTION 0 -->

## 0. Provenance and hash ledger


**Verdict in one line.** (ii-b) *as literally stated is refuted twice* (§4); a
strictly weaker but **sharp** unconditional extension of Prop. 3.27 to nodes +
`A_{2k-1}` tangencies is **proved** (§3, Theorem N-A), and specialises to the
residual as the single scalar gate `M_infty + 2T <= 3d-3` (§3.5). (ii-a)'s
`pi_1`-transport is **refuted as a general principle** by an explicit witness
(§6); only a cover-level transport can survive, and that is typed OPEN.

### 0.1 Hashes

Three charged inputs verified with `shasum -a 256` **before any reading**; 3/3 match
the boxed values:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  pi1s4-close-residual-r2-opus5-20260831.md
aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0  pi1s4-close-residual-hostile-review-sol56-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Nori re-fetched **in this lane** from Numdam
(`http://www.numdam.org/article/ASENS_1983_4_16_2_305_0.pdf`, 4 546 575 bytes,
41 PDF pages, journal pp. 305-344), hashed:

```text
1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45  nori_refetch_20260831.pdf
```

matching the boxed value. Page map: journal page `p` = PDF page `p - 303`. The
NUMDAM text layer is 1983 OCR and is unreliable on formulas; **every statement
quoted below was re-read from a 200-dpi raster of the page**, not from the text
layer. Two OCR corrections are recorded in §1.4. No CAS was run; no other
literature was fetched.

### 0.2 Typing

`PROMOTED` = coordinator integration `bafe5e89` §1. `PROMOTED-CONSUMED` = a
statement the hostile review `aa41551f` re-typed as promoted (notably charged
Lemma 4.3 and the Nori reduction `C'^2 - 2 delta_aff = 3d-2-M_infty`, review
item D.1 "CONFIRMED"). `NORI` = quoted verbatim from the hashed PDF with page
number. `PROVED-HERE` = established in this report from those plus classical
facts. `REFUTED` = a counterexample is exhibited. `OPEN` = typed residual.

**Binding stop respected**: the hostile review REFUTED the claimed `d<=7` nodal
closure and deleted the `(6,4)` semigroup step; I do not consume it. Any
survivor has `d>=6`, `n>=2`, `gcd(d,n)>=2` (review D.2).

<!-- SECTION 0 END -->
<!-- SECTION 1 -->

## 1. What Nori actually proves (§3, verbatim consumption)


All quotations are from the hashed PDF, read off the 200-dpi raster.

**1.1 WLT (journal pp. 305-306).**

> *WLT. Let* `H` *be a connected compact complex-analytic subspace (not necessarily
> reduced) of a connected complex manifold* `U`, *defined by a locally principal sheaf
> of ideals. Assume that* `O_U(H)|H` *is ample and* `dim U >= 2`. *Let* `q : U -> X`
> *be a holomorphic, locally invertible, map, with* `X` *a smooth projective variety.
> Let* `R ⊂ X` *be an arbitrary Zariski-closed subset. Put* `h = q o i` ... *Finally
> let* `G` *be the image of* `pi_1(U - q^{-1}(R)) -> pi_1(X - R)`. *Then:*
> **A** : `G` *is a subgroup of finite index.*
> **B** : *If* `q(H) ∩ R = 0`, *then the image of* `pi_1(H) -> pi_1(X-R)` *is a
> subgroup of finite index.*
> **C** : *If* `dim X = dim U = 2`, *then* `[pi_1(X-R) : G]` *is bounded above by*
> `(Div h)^2 / H^2`.

Note what WLT does **not** require: `H` is *not* assumed smooth, and in part **A**
it is *not* assumed disjoint from `R`. The only numerical input is
`O_U(H)|H` ample, i.e. (for `H` a curve in a surface) `H^2 > 0`.

**1.2 Fact 1.4 B (journal p. 310)** — the centrality engine.

> *Fact 1.4 B. — With* `M, N, S` *as above, assume that* `S` *is smooth and that*
> `N` *is a divisor with normal crossings in a neighbourhood of* `S`. *Then for a
> suitable tubular neighbourhood* `U` *of* `S`, `gamma(S) ⊂ pi_1(U-N)` *is central,
> and is therefore a singleton.*

Here `M` is a complex manifold, `N ⊂ M` a closed subvariety, `S ⊂ N` an irreducible
codimension-one component, and `gamma(S)` the meridian conjugacy class (Definition
1.1, journal p. 310).

**1.3 Definition 3.25 and Proposition 3.26 (journal p. 330).**

> *DEFINITION 3.25. — If the curve* `C` *on* `X` *is defined in a neighbourhood of*
> `P ∈ C` *by* `f = 0`, *let* `f = f_1 f_2 f_3 ... f_r` *be its prime factorisation in*
> `A = Ô_{X,P}` *and let* `A(C;P) = 2 ( sum_{i<j} l(A/(f_i,f_j)) )` *and*
> `B(C) = C^2 - sum_P A(C;P)`.
>
> *PROPOSITION 3.26. — If* `C` *is an irreducible curve with* `B(C) > 0` *and*
> `C ∩ R = ∅`, *then the image of* `pi_1(C̄) -> pi_1(X-R)` *has index* `<= C^2/B(C)`,
> *where* `C̄ -> C` *is the normalisation of* `C`.
>
> *Remark. — For a nodal curve* `C`, `B(C) = C^2 - 2 r(C)`.

Its proof (journal p. 331) is the load-bearing computation of this whole report:

> *Proof. — There is a unique diagram* `C̄ -> H -> C` *such that* `C̄ -> H` *is
> set-theoretically injective and* `H -> C` *induces an injection of Zariski
> tangent-spaces. In fact, if* `P ∈ C`, *with the notation of 3.25, there are exactly*
> `r` *points of* `H` *lying above* `P` *and the complete local rings of* `H` *at these
> points are* `A/(f_i)`, `1 <= i <= r`. *Let* `(U, i, q)` *be a neighbourhood of*
> `h : H -> X` ... *and consider the divisor* `q^{-1}(C) = H + F`. *We see that*
> `(F.H) = C^2 - B(C)`, *and also* `H.q^{-1}(C) = C^2` *because* `H -> C` *is
> birational. It follows that* `H^2 = B(C) > 0` *and the proposition is proved by
> appealing to WLT and noting that* `C̄ -> H` *is a homeomorphism.*

So `H` in 3.26 is the **branch separation** of `C` (branches pulled apart, each kept
with its own singularities), and `B(C)` is *defined to be its self-intersection in a
tubular neighbourhood*.

**1.4 Proposition 3.27 and its proof (journal p. 331).**

> *PROPOSITION 3.27. — Let* `D` *and* `E` *be curves in* `X` *that intersect
> transversally. Assume that* `D` *is nodal and* `C^2 > 2 r(C)` *for every irreducible
> curve* `C` *lying in* `D`. *Then the kernel* `N` *of*
> `pi_1(X - (D u E)) -> pi_1(X - E)` *is abelian and its centraliser is a subgroup of
> finite index.*
>
> *Proof. — Fix an irreducible curve* `C` *contained in* `D`. *Let* `H = C̄` *the
> normalisation of* `C` *and let* `h` *be the composite* `H -> C -> X`. *For a
> sufficiently small tubular neighbourhood* `(U, i, q)` *of* `h`, *let*
> `U' = q^{-1}(X')`, `X' = X - R`, `R = D u E`, *and then* `gamma(H)` *is central in*
> `pi_1(U')` **by 1.4 because** `H` *is smooth and intersects the closure of*
> `q^{-1}(R) - H` **transversally**. *The image of* `gamma(H)` *in*
> `pi_1(U') -> pi_1(X')` *is* `delta ∈ gamma(C) ⊂ pi_1(X')` *and the centraliser*
> `C(delta)` *of* `delta` *contains the image of* `pi_1(U')` *and is therefore a
> subgroup of finite index* **by WLT**. ... *From 3.24, there is a commutative diagram
> ... with* `Y` *a normal surface,* `phi` *a finite morphism unramified outside* `R`
> ..., `pi_1(U') -> pi_1(Y')` *a surjection. Let* `Z = { y ∈ Y | phi is not etale at
> y }`. *Then* `Z ∩ s(H) = ∅`, *and* **by Lemma 5.2**, `Z` *does not contain any
> irreducible component of* `phi^{-1}(D)`. ...

`r(C)` is defined in the introduction (journal p. 306) as "*the number of singular
points of a curve* `C`" — singular points **of `C` itself**, not of `D`. Lemma 5.2
(journal p. 333) says: any two irreducible curves in `phi^{-1}(D)` intersect each
other, for `phi` finite tamely ramified unramified outside `D u E`, with `D`, `E`
as in 3.27.

**1.5 The general-singularity proposition Nori already has (journal p. 336).**
This is decisive for route (a) and the lane prompt does not name it.

> *We now discuss other singularities. Let* `A = C[[a,b]]`, `T = Spec A`, *and*
> `f ∈ A` *is square-free and in the square of the maximal ideal. By a sequence of
> blowing-up transformations we get a proper birational* `psi : S -> T` *with*
> `div psi*(f) = F + G` *where* `F` *is the proper transform of* `f = 0` *and* `F`
> *meets* `G_red` *transversally. Let* `s = G.(G + 2F)`. ... *Put* `s = s(C;P)`.
> *Let* `F(C) = sum_P s(C;P)`.
>
> *PROPOSITION 6.5. — With the above notation, if* `C^2 > F(C)`, *then*
> `pi_1(X-C) -> pi_1(X)` *is a central extension.*
>
> *Proof. — After a series of blowing-ups, we get* `phi : Y -> X` *with*
> `phi^{-1}(C) = C' + G`, *where* `C'` *is the proper transform of* `C`, `C'` *meets*
> `G_red` *transversally, and* `G.(G+2C') = F(C)`. *Thus* `(C')^2 > 0`. *Putting*
> `(Y, C', G)` *in place of* `(X, D, E)` *in 2.5, we see that* `gamma(C')` *is central
> in* `pi_1(Y - phi^{-1}(C))` *and therefore* `gamma(C)` *is central in* `pi_1(X-C)`.
>
> *Remark 6.6. — ... For a node,* `s(C;P) = 2` *and therefore if* `C^2 > 4 r(C)` *for
> an irreducible nodal curve* `C`, `pi_1(X-C) -> pi_1(X)` *is a central extension.*
> *However example 3.19 (C) shows that this is false when* `C^2 = 4 r(C)`.
>
> *Example 6.7. — For an ordinary cusp* `(a^2 - b^3 = 0)`, `s(C,P) = 6`.

Corollary 2.5 (journal p. 315), the engine of 6.5, requires `D` nodal **and every
irreducible `C ⊂ D` smooth with `C^2 > 0`**; its proof is one line from Fact 1.4 B
plus surjectivity 2.4.

**1.6 Two errata in the printed text (PROVED-HERE, raster-verified).**
*(E1)* The lane prompt's gloss "`A(C;P)` = sum of pairwise branch intersection
multiplicities and `B(C) = C^2 - 2 sum_P A(C;P)`" **double-counts the factor 2**.
Nori puts the `2` *inside* `A`. Net value is the same,
`B(C) = C^2 - 2 sum_P sum_{i<j} l(A/(f_i,f_j))`, but `A(C;P) = 2` at a node, not `1`.
*(E2)* Remark 6.6's "`s(C;P) = 2`" **for a node is a misprint for `4`**; the
inequality `C^2 > 4 r(C)` printed in the same sentence is correct. Proof: from
`phi^{-1}(C) = C' + G` and `(C'+G)^2 = C^2` one gets the identity
`(C')^2 = C^2 - G.(G+2C') = C^2 - F(C)`; at a node one blow-up gives `G = 2E`,
`F.E = 2`, `E^2 = -1`, so `s = 2E.(2E+2F) = -4+8 = 4`, and `(C')^2 = C^2 - 4` as it
must be (one blow-up at a point of multiplicity 2). The cusp value `s = 6` of
Example 6.7 is `2^2+1^2+1^2`, confirming the general rule below. The `s = 2` reading
was re-checked on the raster and is genuinely what the 1983 print says.

**1.7 The rule for `s` (PROVED-HERE).** For any singular germ,
`s(C;P) = sum_i m_i^2` over the multiplicities `m_i` of `C` at the centres of the
minimal embedded resolution of the germ, because each blow-up at a point of
multiplicity `m` drops the self-intersection by `m^2` and `(C')^2 = C^2 - F(C)`.
Values used below: node `4`; ordinary cusp `6`; and (§3.1) `A_{2k-1}` gives `4k`.

<!-- SECTION 1 END -->
<!-- SECTION 2 -->

## 2. The transversality consumption, located exactly


**2.1 The numerical hypothesis of 3.27 is a normal-bundle degree (PROVED-HERE).**
In 3.27 Nori takes `H = C̄` (the normalisation) and applies WLT to a tubular
neighbourhood `(U,i,q)` of `h : C̄ -> X`. WLT's only numerical input is
`O_U(H)|H` ample, i.e. `H^2 > 0`. Run the 3.26 computation with this `H`:
`q^{-1}(C) = H + F`, `H.q^{-1}(C) = C^2` (birationality), so

```text
(2.1)   H^2  =  deg N_h  =  C^2 - 2 delta(C),        delta(C) = sum_P delta_P .
```

For `C` **nodal** this is `C^2 - 2r(C)`, which is Nori's printed hypothesis; and it
also equals `B(C)` (Remark after 3.26). In general the two differ:

```text
(2.2)   B(C) = C^2 - 2 sum_P sum_{i<j} (f_i . f_j)_P ,    delta_P = sum_{i<j}(f_i.f_j)_P + sum_i delta(f_i),
        hence   B(C) = deg N_h + 2 sum_P sum_i delta(f_i)  >=  deg N_h ,
```
**with equality iff every branch of `C` is smooth.** So `B(C)` is *blind to
unibranch singularities*: for a cuspidal curve `B(C) = C^2` however bad the cusps.
This is the first structural reason (ii-b) as stated cannot be right (§4.1).

For `C` with only **double points of two smooth branches** (`A_{2k_p-1}`,
contact `k_p`), `delta_P = k_p` and
`B(C) = deg N_h = C^2 - 2 sum_P k_p` — exactly the residual's class.

**2.2 Transversality is consumed at exactly two places (PROVED-HERE).**

**(N1) Fact 1.4 B.** In 3.27's proof, `M = U`, `N = q^{-1}(R)`, `S = H`. Fact 1.4 B
requires `S` smooth **and `N` a normal-crossings divisor in a neighbourhood of `S`**.
Nori discharges this with "`H` is smooth and intersects the closure of
`q^{-1}(R) - H` transversally". `H` smooth is free (normalisation). The second half
is where nodality of `D` and transversality of `D, E` are spent: over a node of `C`,
`F = closure(q^{-1}(C)-H)` is the *other* branch, and it crosses `H` transversally
precisely because the node is transverse.

**(N2) Lemma 5.1(a), via Lemma 5.2.** 3.27's second half invokes Lemma 5.2 to show
`phi` is unramified outside `E`. Lemma 5.1 (journal p. 332) *hypothesises*
"`A -> phi(A) = B` birational, and `B` **a nodal curve**, with `B^2 > 2r(B)`", and
its proof (journal p. 333) reads

> *(b) assures us that* `Y` *is smooth at every point of* `A`, *and that the only
> singular points of* `phi^{-1}(B)` *lying on* `A` *are nodes. Consequently if*
> `phi^{-1}(B) = A + R` *as divisors,* `A` *intersects* `R` **transversally** *in*
> `{P ∈ A | A is smooth at P and B is singular at phi(P)}`. *Therefore*
> `(A.R) = 2r(B) - 2r(A)`.

So the identity `A^2 - 2r(A) = B^2 - 2r(B)` that drives 5.1 is *the same*
transversality bookkeeping. **Any repair of (N1) alone leaves (N2) open**; this
is a correction to the lane prompt's framing, which names only the `H`/`1.4`
consumption.

**2.3 (N1) fails at a tangency — not a gap, a falsehood (PROVED-HERE).**
Local model at an `A_{2k-1}`: in a bidisc `U_0`, `H = {y=0}`, `F = {y = x^k}`,
`N = H u F`. Then `U_0 - N` is the complement of the `(2,2k)`-torus link and

```text
G_k := pi_1(U_0 - N) = < a, b | (ab)^k = (ba)^k >,      a = gamma(H).
```

`z := (ab)^k` is central (`a^{-1}(ab)^k a = (ba)^k = (ab)^k`, likewise for `b`), and
`G_k/<z> = <a,c | c^k = 1> = Z * Z/k` with `c = ab`. For `k >= 2` this free product
has trivial centre and the image of `a` is a free generator of infinite order; hence
**no nonzero power of `a` is central in `G_k`**. For `k = 1` (a node) `G_1 = Z^2` and
`a` is central. So Fact 1.4 B's conclusion is *false* at a tangency, and the failure
is already visible in the local model that `U` restricts to. Route (b) in the sense
of "replace transversality by a local computation at the tangency" is therefore
**dead**: there is nothing true to compute. What survives locally is only that
`(ab)^k` — the class of the *boundary of the Milnor fibre*, not a meridian — is
central; that is not `gamma(H)` and does not generate `N`.

**2.4 Consequence for the shape of any extension.** Since (N1) and (N2) both
demand a normal-crossings/nodal picture, an extension of 3.27 must *produce* one.
Nori's own answer is Prop. 6.5: resolve completely and pay `F(C) = sum_i m_i^2`.
Route (a) below resolves **only the tangencies**, keeps `D` nodal, and pays strictly
less.

<!-- SECTION 2 END -->
<!-- SECTION 3 -->

## 3. Route (a): one blow-up at each tacnode — bookkeeping and verdict


**3.1 LEMMA (local resolution of `A_{2k-1}`; PROVED-HERE).** *Let* `p` *be a point of
a smooth surface at which two smooth branches* `b_1, b_2` *meet with contact*
`k = (b_1.b_2)_p >= 1`. *Let* `sigma` *be the composite of the* `k` *point blow-ups
defined inductively: blow up* `p`, *then the unique point at which the strict
transforms still meet, etc. Then:*

1. *In the chart* `y = x y_1` *the branches* `y=0`, `y=x^k` *become* `y_1=0`,
   `y_1 = x^{k-1}`, *and* `E_1 = {x=0}`; *the strict transform of the previous
   exceptional lies in the other chart, so* **every centre is a free point** *lying on
   exactly one exceptional curve.*
2. *After the* `(k-1)`*-st step the picture is* `y_{k-1}=0`, `y_{k-1}=x`, `E_{k-1}={x=0}`:
   *three pairwise transverse smooth germs (an ordinary triple point). The* `k`*-th
   blow-up separates all three:* `E_k` *meets* `b̃_1, b̃_2, E_{k-1}'` *at three distinct
   points, transversally, and* `b̃_1 ∩ b̃_2 = ∅`.
3. *Hence* `b̃_1 u b̃_2 u E_1' u ... u E_{k-1}' u E_k` *has normal crossings, the
   exceptionals forming a chain, with* `b̃_i` *meeting* `E_k` *only.*
4. *If both branches lie on one irreducible* `C`, *then* `C` *has multiplicity* `2`
   *at every centre and* `C̃^2 = C^2 - 4k`. *If they lie on distinct components*
   `C, C_2`, *then* `C` *has multiplicity* `1` *at every centre and* `C̃^2 = C^2 - k`.

*Proof.* (1)-(2) are the displayed coordinate computation together with the fact that
`{x=0}`'s strict transform meets the new exceptional at the point of the `y_1`-axis
direction, which is not the next centre. (3) follows: each `b̃_i` met `E_j` at the
centre of step `j+1`, which was blown up. (4) each centre carries both branches
(multiplicity 2) resp. one branch (multiplicity 1), and a blow-up at a point of
multiplicity `m` drops the self-intersection by `m^2`. `[]`

Consistency with §1.7: `s(A_{2k-1}) = sum m_i^2 = 4k`, matching the lane prompt's
`4k_p`, and `s(A_1) = 4` matching erratum (E2).

**3.2 LEMMA (the group does not move; PROVED-HERE).** *Let* `sigma : X̃ -> X` *be a
blow-up at* `p ∈ D`, `D̃, Ẽ` *the strict transforms and* `Ẽ_tot = Ẽ u (exceptional)`.
*Then* `X̃ - (D̃ u Ẽ_tot) ≅ X - (D u E)` *and* `pi_1(X̃ - Ẽ_tot) ≅ pi_1(X - E)`,
*compatibly; hence the two kernels* `N` *agree.*
*Proof.* `sigma` is an isomorphism off the exceptional locus, and
`sigma^{-1}(D u E)` as a **set** is `D̃ u Ẽ u (exceptional)`, giving the first
isomorphism. For the second, `X̃ - Ẽ_tot ≅ (X - E) - {p}` if `p ∉ E`, and `≅ X - E`
if `p ∈ E`; removing a point from a complex surface (real codimension 4) does not
change `pi_1`. Naturality of the square gives the identification of kernels. `[]`

**3.3 THEOREM N-A (PROVED-HERE; the (ii-b) extension that is true).**
*Let* `X` *be a smooth projective surface and* `D, E ⊂ X` *curves with:*

* **(A1)** *every singular point of* `D` *is a double point of two smooth branches,
  with contact* `k_p >= 1` *(type* `A_{2k_p-1}`*);*
* **(A2)** `D u E` *has normal crossings at every point of* `D - Sing(D)`, *and*
  `E ∩ Sing(D) = ∅`.

*For a component* `C` *of* `D` *put* `r_1(C) = #{p ∈ Sing C : k_p = 1}`,
`T(C) = sum_{p ∈ Sing C, k_p>=2} k_p`, `T_x(C) = sum_{p ∈ C ∩ (D-C), k_p>=2} k_p`.
*If for every irreducible component* `C ⊂ D`

```text
(3.1)   C^2 > 2 r_1(C) + 4 T(C) + T_x(C)     <==>     B(C) > 2 T(C) + T_x(C) ,
```

*then* `N = ker( pi_1(X - (D u E)) -> pi_1(X - E) )` *is finitely generated abelian
and its centraliser has finite index.*

*Proof.* Let `sigma : X̃ -> X` be the composite of the resolutions of Lemma 3.1 at
the finitely many `p ∈ Sing D` with `k_p >= 2` (pairwise disjoint, so they commute).
Put `D̃` = strict transform of `D`, `Ẽ` = strict transform of `E` together with all
exceptional curves.

*`D̃` is nodal.* At a resolved point the branches are separated (3.1(2)); the points
with `k_p = 1` were untouched and stay nodes; elsewhere `D̃ ≅ D` is smooth.

*`D̃` and `Ẽ` intersect transversally.* At a resolved point this is 3.1(3); at a node
of `D̃` nothing was blown up and `E` does not pass there by (A2); at a smooth point of
`D̃` it is (A2). No exceptional curve meets `D̃` outside the `E_k`'s of 3.1(3).

*Numerics.* By 3.1(4), `C̃^2 = C^2 - 4T(C) - T_x(C)`, and `r(C̃) = r_1(C)` because the
tangential self-points have been resolved, cross-points were never singular points of
`C`, and no new singular point of `C̃` is created. Hence
`C̃^2 - 2 r(C̃) = C^2 - 2r_1(C) - 4T(C) - T_x(C) > 0`, which is Nori's hypothesis
`C̃^2 > 2 r(C̃)` on `X̃`.

Nori Prop. 3.27 applied to `(X̃, D̃, Ẽ)` gives the conclusion for the corresponding
kernel; Lemma 3.2, iterated, identifies that kernel with `N`. `[]`

*Note.* `B(C) = C^2 - 2r_1(C) - 2T(C)` here (2.2), so (3.1) is literally "`B(C) > 0`
with the tangential weight charged twice more". For nodal `D` (`T = T_x = 0`) (3.1)
**is** 3.27. Both consumptions (N1) and (N2) of §2.2 are discharged, because `D̃` is
genuinely nodal and `D̃ u Ẽ` genuinely normal-crossing along `D̃`.

**3.4 Comparison (PROVED-HERE).** For the same class of curves Nori's own Prop. 6.5
needs `C^2 > F(C) = 4 r_1(C) + 4 T(C)` (by §1.7 and 3.1(4)), with `E = ∅`. Theorem
N-A weakens the hypothesis by `2 r_1(C)` — nodes are not resolved — and allows
`E != ∅`, at the price of "abelian" in place of "central". Against the promoted
(B')-style bookkeeping, N-A charges each `A_{2k-1}` a **self-intersection cost `4k`**
and leaves nodes at cost `2`; the target `B(C)>0` would charge `2k`. The gap is
exactly `2T(C) + T_x(C)`.

**Sharpness of the `T_x` coefficient.** §4.2 exhibits two bitangent conics:
`C_i^2 = 4`, `r_1 = T = 0`, `T_x = 4`, so (3.1) reads `4 > 4` and fails by exactly one
unit — and the conclusion of 3.27 is **false** there (`N = Z * Z/2`). So the
coefficient `1` on `T_x` cannot be lowered, and `B(C) > 0` alone is not enough.

**3.5 COROLLARY N-A-RES (PROVED-HERE) — the residual gate.**
In the PI1-S4 residual setting (`D_1` irreducible polynomial curve of degree `d`, all
affine singularities double points of two smooth branches — PROMOTED; `X'` the
infinity resolution with `C'` smooth and transverse to `B_infty` at a smooth point;
`E = B_infty`; `X' - B_infty = C^2`), write `delta_aff = sum_p k_p = r_1 + T`. The
charged Lemma 4.3, `C'^2 - 2 delta_aff = 3d - 2 - M_infty` (PROMOTED-CONSUMED,
review item D.1 CONFIRMED), gives

```text
C'^2 - 2 r_1 - 4T = (3d-2-M_infty) + 2(r_1+T) - 2r_1 - 4T = 3d - 2 - M_infty - 2T ,
```

so (3.1) (with `T_x = 0`, `D` irreducible) is exactly

```text
(M-INF-T)      M_infty + 2 T  <=  3d - 3 ,        T = sum over tangential double points of k_p .
```

Then `X̃ - Ẽ ≅ C^2` minus finitely many points, so `pi_1(X̃ - Ẽ) = 1` and
`N = pi_1(C^2 - D_1)` is abelian, hence `= H_1 = Z`; the residual answers **NO**.
At `T = 0` this is verbatim `(M-INF)`, so N-A-RES **strictly extends** the promoted
nodal closure: the price of tangency is exactly two units of `(M-INF)` slack per unit
of tangential weight.

*Concrete gain at `(d,n) = (6,3)`* (the one non-coprime row the hostile review left
standing, review D.1: "`(6,3)` is a one-pair calculation"). There `a=3`, `3|6`, so the
germ at infinity is the `(3,beta_1)`-cusp with `3 ∤ beta_1 > 6`, `delta_infty = beta_1-1`,
`M_infty = beta_1+2`, `delta_aff = 11-beta_1`, and `3d-3 = 15`:

| `beta_1` | `M_infty` | `delta_aff` | gate `2T <= 15-M_infty` | closed configurations |
|---|---|---|---|---|
| 7 | 9 | 4 | `T <= 3` | `T ∈ {0,2,3}`; open only `T = 4` |
| 8 | 10 | 3 | `T <= 2` | `T ∈ {0,2}`; open only `T = 3` |
| 10 | 12 | 1 | `T <= 1` | `T = 0` forced by `delta_aff = 1` — closed |

So at `(6,3)` every tangential configuration is closed except `(beta_1,T) = (7,4)` and
`(8,3)`. `(4,2)` is unaffected (`delta_aff = 1` forces `T = 0`).

<!-- SECTION 3 END -->
<!-- SECTION 4 -->

## 4. Route (b): local replacement of transversality at a tangency


**4.1 Verdict on route (b): DEAD, and not for want of effort.** §2.3 shows the
statement one would have to prove — "`gamma(H)` is central in `pi_1(U - q^{-1}(R))`
when `H` is smooth and the rest of `q^{-1}(R)` is tangent to it" — is **false in the
local model**, so no etale-local computation can replace transversality in Fact
1.4 B. Moreover §2.2 (N2) shows a *second* transversality consumption in Lemma 5.1,
which route (b) never even addresses. The honest statement of what is available
locally is: at an `A_{2k-1}` the only central element of the local group is
`(ab)^k`, the class of the boundary of the Milnor fibre; it is not a meridian and
the meridians do not generate a subgroup in which it is a proper power of one of
them. Typed: `REFUTED[NORI-BC-ROUTE-B]`.

The two refutations below explain *why* no local fix can exist: the target
statement itself is false.

**4.2 REFUTATION 1 — `B(C) > 0` for general singularities (PROVED-HERE, using
Nori's own example).** Nori, journal p. 336, Example 6.7 (raster-verified):

> *The general curve* `C` *in* `P^2` *of degree 6 given by* `f^2 - g^3 = 0`, *where*
> `f` *and* `g` *are homogeneous of degrees 3 and 2 respectively, is smooth outside*
> `f = g = 0` *where its singularities are ordinary cusps. Therefore*
> `C^2 = F(C) = 36` *in this case. This example is due to Zariski [Z]. He shows that*
> `pi_1(P^2 - C) ≅ Z/(2) * Z/(3)`.

Take `X = P^2`, `D = C`, `E = ∅`. Each of the 6 cusps is **unibranch**, so in
Definition 3.25 `r = 1` at each `P` and the sum over `i<j` is empty:
`A(C;P) = 0`, hence `B(C) = C^2 = 36 > 0`. But
`N = ker(pi_1(P^2-C) -> pi_1(P^2)) = pi_1(P^2 - C) = Z/2 * Z/3` is **non-abelian**.
So *"3.27 with `D` nodal replaced by `B(C) > 0`" is false*. Note the corrected
invariant of (2.1) does not save it either: `delta(C) = 6`, so
`C^2 - 2 delta(C) = 24 > 0` as well. Typed: `REFUTED[NORI-BC-GENERAL]`.

**4.3 REFUTATION 2 — `B(C) > 0` even for curves with only `A_3` double points of
smooth branches (PROVED-HERE).** Let `lambda ∈ C - {0,1}` and

```text
C_1 = { z y = x^2 },     C_2 = { z y = lambda x^2 },     D = C_1 u C_2 ⊂ P^2 .
```

`C_1 ∩ C_2 = {x = 0, zy = 0} = { P=[0:1:0], Q=[0:0:1] }` with local intersection 2 at
each (total 4 = Bezout). Both conics are smooth, so each of `P, Q` is a double point
of two smooth branches with contact 2, i.e. an `A_3` tacnode. Hypothesis (A1) of
Theorem N-A holds; `B(C_i) = C_i^2 - 0 = 4 > 0` for both components, because
Definition 3.25 only sees branches of `C_i` **itself**.

*Computation of `pi_1(P^2 - D)`.* In the chart `x = 1`, with `(Y,Z) = (y/x, z/x)`,
`C_1 = {YZ = 1}` and `C_2 = {YZ = lambda}` — two disjoint smooth affine curves. Put
`W = P^2 - D - L_x = C^2_{Y,Z} - {YZ=1} - {YZ=lambda}` and `f = YZ : C^2 -> C`.

* Over `C - {0,1,lambda}`, `f` is a `C^*`-bundle; the base is homotopy equivalent to a
  wedge of three circles and `H^2 = 0`, so the bundle is trivial and
  `pi_1 = F_3 x Z = <t_0,t_1,t_lambda> x <mu>`.
* `f^{-1}(D_eps) = {|YZ| < eps}` deformation-retracts to `{Z=0} ≅ C` by
  `(Y,Z) |-> (Y, sZ)`, `s: 1 -> 0` (which stays inside), so it is **contractible**;
  and `f^{-1}(D_eps - 0)` is a `C^*`-bundle over an annulus, `pi_1 = Z^2 = <t_0, mu>`.
* Van Kampen: `pi_1(W) = (F_3 x Z)/<<t_0, mu>> = F_2 = <t_1, t_lambda>`, the
  meridians of `C_1` and `C_2`.

By Nori's Fact 1.2 (journal p. 310), `pi_1(P^2 - D) = pi_1(W)/<<gamma(L_x)>>`. A
meridian of `L_x` is the boundary of a transverse disc at a generic point of `L_x`;
taking the line `Z = cY` (`c` generic), that disc is its neighbourhood of infinity,
with boundary `Y = R e^{i theta}`, `Z = cR e^{i theta}`. Its image under `f` is
`W = cR^2 e^{2 i theta}`, a large circle traversed **twice**, whose class in
`pi_1(C - {0,1,lambda})` is `(t_0 t_1 t_lambda)^{-2}`; since `mu = 1` the lift is
well defined and, using `t_0 = 1`,

```text
gamma(L_x) = (t_1 t_lambda)^{-2} ,        pi_1(P^2 - D) = < t_1, t_lambda | (t_1 t_lambda)^2 = 1 > .
```

Setting `c = t_1 t_lambda` this is `Z * Z/2`, **non-abelian**. Consistency check:
`H_1 = Z^2/<2(t_1+t_lambda)> ≅ Z ⊕ Z/2`, which is the standard `H_1(P^2 - D)` for two
components of degree 2. Here `N = pi_1(P^2 - D)` is non-abelian while `B(C_i) > 0`
for both components. Typed: `REFUTED[NORI-BC-DOUBLEPOINT]`.

**4.4 What this locates.** `B(C)` is blind to exactly two things: (i) singularities
of the individual branches (§4.2), and (ii) contact between **distinct components**
(§4.3). Theorem N-A repairs both — (i) by hypothesis (A1), (ii) by the term
`T_x(C)` — and §3.4 shows the repair of (ii) is **sharp to one unit** on the
example of §4.3. The remaining question, the coefficient `4` versus `2` on the
*self*-tangential weight `T(C)`, is not touched by either counterexample and is
typed OPEN in §7 with a named candidate.

<!-- SECTION 4 END -->
<!-- SECTION 5 -->

## 5. Route (c): can 3.26 (B(C)>0, C ∩ R = ∅) substitute?


**5.1 What `R` is.** In WLT, `R ⊂ X` is an **arbitrary Zariski-closed subset** and
the conclusion concerns `pi_1(X - R)`. Part **B** — the part 3.26 rests on —
carries the extra hypothesis `q(H) ∩ R = ∅`, which is inherited by 3.26 as
`C ∩ R = ∅`. In 3.27, by contrast, `R = D u E` and `C ⊂ D ⊂ R`; only WLT **A** is
used there, and A has no disjointness hypothesis.

**5.2 3.26 cannot substitute (PROVED-HERE).** In the residual application the object
whose fundamental group we want is `C^2 - D_1 = X' - (C' u B_infty)`, so
`R = C' u B_infty` **necessarily contains `C'`**. The hypothesis `C ∩ R = ∅` is not a
convenience: without it `pi_1(C̄) -> pi_1(X-R)` is not even defined by the
inclusion, since `C̄` does not map into `X - R`. Arranging `E = B_infty` disjoint
from `C'` is beside the point and in any case impossible (the infinity resolution
requires `C'` to meet `B_infty`); and taking `R = B_infty` alone makes
`pi_1(X' - R) = pi_1(C^2) = 1`, so 3.26's index bound `<= C'^2/B(C')` is vacuous. The
conclusion of 3.26 is a "big image" statement about a curve *away* from the removed
locus; it can never see the meridians of `C'` itself, which are exactly what
generates `N`. Typed: `REFUTED[NORI-BC-ROUTE-C]`.

**5.3 What does transfer from 3.26 (PROVED-HERE).** Two things, both used above.

1. *The identity* `H^2 = B(C)` for `H` the branch separation, which is what lets one
   read 3.27's hypothesis `C^2 > 2r(C)` as the normal-bundle statement `H^2 > 0`
   (§2.1). This is the correct typing of the numerical side of (ii-b): **the
   numerics were never the obstruction.**
2. *The branch-separation construction itself.* It is worth recording that the
   obvious hybrid — run 3.27's proof with `H` = branch separation instead of `H = C̄`,
   to buy `H^2 = B(C)` — **fails, and for the same reason as everything else**: (i)
   the branch separation is smooth only when every branch of `C` is smooth, so Fact
   1.4 B's first hypothesis is not free; and (ii) even when it is smooth, over an
   `A_{2k-1}` the divisor `F = closure(q^{-1}(C) - H)` is the *other* branch, still
   tangent to `H` with contact `k`, so Fact 1.4 B's normal-crossings hypothesis fails
   exactly as in §2.3. Swapping `H` changes the numerics but not the topology.

<!-- SECTION 5 END -->
<!-- SECTION 6 -->

## 6. (ii-a) Equisingular-at-infinity nodalization


**6.1 A simplification of the stratum problem (PROVED-HERE).** Every member of
`P_{d,n}` is a **rational** curve (parametrised by `A^1`), of degree exactly `d` on
the open locus `deg p = d`, with a single point `Q` at infinity. Hence

```text
(6.1)   delta_aff + delta_infty = (d-1)(d-2)/2   is CONSTANT on { deg p = d, deg q = n } .
```

Consequently **`delta_infty` is constant on a subfamily if and only if `delta_aff`
is**. This removes the awkwardness the r2 report flags at its §6.4 ("`delta_infty`
jumps on `P_{d,n}` when `g >= 2`"): one never has to control the place at infinity
directly; controlling the *affine* `delta` controls it. And a nodalization of an
`A_{2k-1}` into `k` nodes is by definition `delta`-constant, `delta_aff = sum_p k_p`
being unchanged. So the object to construct is precisely

> `Sigma := { gamma ∈ P_{d,n} : delta_aff(gamma) = delta_aff(gamma_0) }` near `gamma_0`,
> and one needs the generic point of the component of `Sigma` through `gamma_0` to be
> nodal.

**6.2 The local half is classical.** In the semiuniversal deformation of a plane
curve singularity, the `delta`-constant stratum is irreducible and its **generic
member has exactly `delta` nodes** (Teissier). For `A_{2k-1}` this is the splitting
into `k` nodes used in §3.1 in blown-up form. So the required nodalization exists in
the versal deformation of each affine singularity of `D_1`.

**6.3 The global half is the gap, and it is not the one the report names.** What is
missing is that the *parametrised* family `P_{d,n}` maps onto (a neighbourhood of the
origin in) the product of the versal deformations of the affine singularities — the
"affine double-point scheme still spreads" clause. Nothing promoted supplies this;
`P_{d,n}` has dimension `d + n + 2` while the product of versal bases has dimension
`sum_p tau_p = sum_p (2k_p - 1)`, so the count is favourable in low degree and says
nothing about surjectivity. Typed `OPEN[PI1S4-ES-SPREAD]`.

**6.4 REFUTATION — the `pi_1`-transport itself is false, even `delta`-constantly
(PROVED-HERE).** Suppose 6.1-6.3 were all supplied. The transport step as the r2
report states it — "the generic member is nodal, so by Nori its complement has
abelian `pi_1`; transport back to `gamma_0`" — **does not exist as a principle.**
Witness, with `delta` constant:

* `D_0 = C_1 u C_2` = the two bitangent conics of §4.3; `delta(D_0) = 2 + 2 = 4`
  (two `A_3`'s), `pi_1(P^2 - D_0) = Z * Z/2`, **non-abelian**.
* Fix `C_1 = {zy = x^2}` and let `C_2^{(s)}` be a generic small deformation of
  `C_2 = {zy = lambda x^2}` inside `P^5`. The conics tangent to `C_1` form a proper
  closed subvariety of `P^5` (one equation), so for generic small `s` the two conics
  meet in **4 distinct transverse points**: `D_s` is nodal with `r = 4`, hence
  `delta(D_s) = 4 = delta(D_0)` — the family is `delta`-constant.
* For `s != 0`, Nori 3.27 applies verbatim (`C_i^2 = 4 > 0 = 2 r(C_i)`, `E = ∅`), so
  `pi_1(P^2 - D_s)` is **abelian**, `= H_1 = Z ⊕ Z/2`.

So a `delta`-constant family whose generic member is nodal with abelian `pi_1` can
have a special member with non-abelian `pi_1`. Typed:
`REFUTED[PI1S4-NODALIZATION-PI1-TRANSPORT]`. (This is the expected direction of
semicontinuity — degenerating adds relations to the *nearby* group, not to the
special one — but the point here is the explicit witness, which needs no
semicontinuity theorem.)

**6.5 What is left of (ii-a).** Only a transport at the level of the **cover**, not of
`pi_1`: "if `pi_1(C^2 - D_1)` admits a surjection to `S_4` with every meridian a
transposition and the promoted local data, then so does a nearby nodal member,
contradicting the nodal closure". Its local half is clean and I prove it:

> **LEMMA 6.6 (PROVED-HERE).** *Let* `p` *be an* `A_{2k-1}` *point of* `D_1` *with
> local group* `G_k = <a,b | (ab)^k = (ba)^k>` (§2.3) *and promoted local monodromy
> generated by two* **disjoint** *transpositions,* `a |-> (12)`, `b |-> (34)`. *This
> is a well-defined homomorphism* `G_k -> S_4` *for every* `k`, *because disjoint
> transpositions commute and therefore* `(ab)^k = (ba)^k` *holds in the image.
> Under the* `delta`*-constant splitting of* `p` *into* `k` *nodes, each node has local
> group* `Z^2 = <a_i, b_i>` *and the assignment* `a_i |-> (12)`, `b_i |-> (34)`
> *is again well defined and agrees with the restriction of the original
> representation to the meridians of the two branches. So the local monodromy data
> imposes no obstruction to deforming the cover.*

What is **not** available is the global statement that the branched cover deforms
with the curve — an equisingular-deformation-of-covers theorem, which is what the
gate's "local intersection-number conservation" was meant to replace charged
Lemma 5.5 with. Typed `OPEN[PI1S4-COVER-DEFORMATION]`.

**6.7 Priority.** Theorem N-A (§3) closes every tangential case satisfying
`(M-INF-T)` **unconditionally and with no deformation theory at all**, so (ii-a) is
now only needed in the complementary regime `3d-3 < M_infty + 2T`. Given 6.4, I
recommend (ii-a) be retyped as a *cover*-deformation lane, not a nodalization lane.

<!-- SECTION 6 END -->
<!-- SECTION 7 -->

## 7. Verdicts, typed OPENs, and what is proved unconditionally


**7.1 Verdict table.**

| Item | Verdict | Where |
|---|---|---|
| (ii-b) verbatim: "3.27 with `D` nodal replaced by `B(C)>0`" | **REFUTED** (Zariski sextic; `B=36>0`, `pi_1 = Z/2 * Z/3`) | §4.2 |
| (ii-b) restricted to double points of smooth branches | **REFUTED** (two bitangent conics; `B(C_i)=4>0`, `pi_1 = Z*Z/2`) | §4.3 |
| (ii-b) route (a): blow up `k_p` times at each `A_{2k_p-1}` | **PROVED** — Theorem N-A, and **sharp** in `T_x` | §3.1-3.4 |
| (ii-b) route (b): local replacement of transversality | **REFUTED** (Fact 1.4 B is false at a tangency; and a second consumption in Lemma 5.1 is unaddressed) | §2.2-2.3, §4.1 |
| (ii-b) route (c): substitute 3.26 | **REFUTED** (`C ∩ R = ∅` is structural; `C' ⊂ R` always) | §5.2 |
| Residual gate | **PROVED**: `M_infty + 2T <= 3d-3` `=>` `pi_1(C^2-D_1) = Z` | §3.5 |
| (ii-a) `pi_1`-transport after `delta`-constant nodalization | **REFUTED** (explicit `delta`-constant witness) | §6.4 |
| (ii-a) equisingular-at-infinity stratum | reduced to `delta_aff`-constancy (PROVED); construction OPEN | §6.1-6.3 |
| (ii-a) cover-level transport | local half PROVED (Lemma 6.6); global half OPEN | §6.5 |

**7.2 Proved unconditionally in this lane.** (2.1)-(2.2) the normal-bundle reading of
3.27's hypothesis and `B(C) >= deg N_h` with equality iff all branches are smooth;
§2.3 the local non-centrality at `A_{2k-1}`; Lemma 3.1 (`s(A_{2k-1}) = 4k` and the
normal-crossings resolution); Lemma 3.2 (`N` is a blow-up invariant); **Theorem N-A**
and **Corollary N-A-RES**; the two refutations of §4 and their `pi_1` computations
(each cross-checked against the standard `H_1`); §5.3 that the branch-separation
hybrid fails; (6.1) `delta_infty` constant `<=>` `delta_aff` constant on `P_{d,n}`;
Lemma 6.6; §6.4's refutation. Errata (E1), (E2) of §1.6.

**7.3 Typed OPENs.**

**`OPEN[NORI-BC-SELF-TANGENT-COEFF]`** — *the one place the two conditions still
differ.* For `D` **irreducible** with only nodes and self-tangencies, N-A requires
`C^2 > 2r_1 + 4T` while `B(C)>0` reads `C^2 > 2r_1 + 2T`. Neither §4.2 nor §4.3
touches this. The two conditions first differ at **degree 6**. For a plane curve of
degree `d`, `B(C) = d^2 - 2 delta` and N-A reads `d^2 > 2 r_1 + 4T = 2 delta + 2T`,
so the gap is `delta + T >= d^2/2`. At `d = 4,5` the maximum of `delta + T` is
`2 delta <= 6, 12` against thresholds `8, 12.5` — no gap. At `d = 6`,
`delta <= 10` gives `B(C) >= 16 > 0` always, while N-A fails exactly on
`(delta,T) ∈ {(9,9), (10,8), (10,9), (10,10)}`. The extremal candidate is a
**rational sextic with 5 tacnodes** (`delta = T = 10`, `B(C) = 16 > 0`, N-A needs
`36 > 40`). Deciding existence of such a sextic
and its `pi_1` is the sharp test; no CAS was run and nothing here settles it. Until
settled, `4T` is the honest coefficient.

**`OPEN[M-INF-T]`** — verify `M_infty + 2T <= 3d-3` on the surviving rows
(`d >= 6`, `n >= 2`, `gcd(d,n) >= 2`, per review D.2). §3.5 discharges `(6,3)` except
`(beta_1,T) ∈ {(7,4),(8,3)}`. `(6,2)` inherits the review's condition that charged
(4.2) be proved with the review's induction inserted; `(6,4)` remains a GAP (review
D.1) and is untouched here.

**`OPEN[PI1S4-ES-SPREAD]`** (§6.3) and **`OPEN[PI1S4-COVER-DEFORMATION]`** (§6.5) —
the two named halves of what remains of (ii-a).

**`OPEN[PI1S4-D1-DEGREE]`** — carried unchanged; still the highest-leverage external
gap (review D.2 target `d <= 5`). Nothing here bounds `deg D_1`.

**7.4 Corrections carried forward.**
1. The lane prompt's (and any downstream) reading of Definition 3.25 must place the
   factor `2` **inside** `A(C;P)`: `A(C;P) = 2 sum_{i<j} l(A/(f_i,f_j))`,
   `B(C) = C^2 - sum_P A(C;P)` (§1.6 E1).
2. Nori's Remark 6.6 misprints `s(node) = 2`; the correct value forced by his own
   identity `(C')^2 = C^2 - F(C)` is `4`, and the inequality `C^2 > 4r(C)` printed
   alongside is correct (§1.6 E2).
3. The r2 report's §6.4 names only the `H`/Lemma-1.4 transversality as the
   obstruction. There is a **second** consumption, in Lemma 5.1(a) via Lemma 5.2
   (§2.2 N2); both are discharged by Theorem N-A's blow-up but neither by any purely
   local fix.
4. `B(C)` is *not* the right invariant outside "all branches smooth"; the
   normal-bundle degree `C^2 - 2 delta(C)` is (§2.1), and even that is insufficient
   without the smooth-branch hypothesis (§4.2).

<!-- SECTION 7 END -->
<!-- SECTION 8 -->

## 8. Successor packet


**8.1 What to promote.** Theorem N-A (§3.3), Corollary N-A-RES (§3.5) and the
three refutations (§4.2, §4.3, §6.4) are self-contained given hashed Nori 3.27 and
(for N-A-RES only) charged Lemma 4.3, which the hostile review already typed
CONFIRMED. Promoting N-A-RES replaces the nodality hypothesis in the residual's
row 4 by the single arithmetic gate `M_infty + 2T <= 3d - 3`, which is checkable
from the place at infinity plus the affine singularity type — no deformation theory,
no equisingular strata, no new literature.

**8.2 Named successors, in leverage order.**

1. **`NORI-BC-SEXTIC-5TAC`** — decide `OPEN[NORI-BC-SELF-TANGENT-COEFF]` at its
   extremal point: does an irreducible rational sextic with five tacnodes exist, and
   if so is `pi_1(P^2 - C)` abelian? A negative answer to abelianness would prove
   Theorem N-A's coefficient `4T` optimal and *close* (ii-b) definitively; a positive
   answer would motivate hunting a `2T` proof. Desk-scale entry: the `5`-tacnode
   sextic would be rational with `delta = 10`; parametrise and test.
2. **`M-INF-T`** — extend the existing `(M-INF)` verifications to the `+2T` form on
   `d >= 6`, `gcd(d,n) >= 2`. The `(6,3)` row is done here modulo two configurations;
   `(6,2)` needs charged (4.2) with the review's induction; `(6,4)` needs a
   replacement for the deleted semigroup step.
3. **`PI1S4-D1-DEGREE`** — unchanged, and now with a *lower* payoff threshold: with
   N-A-RES in hand, a degree bound closes the residual without any nodality
   hypothesis wherever the gate holds.
4. **`PI1S4-COVER-DEFORMATION`** — retype the old (ii-a) lane as a cover-deformation
   lane (§6.7). Its `pi_1` formulation is refuted and should not be re-attempted.

**8.3 Execution record.** Desk-scale only; no CAS, no numerical computation. Nori
re-fetched from Numdam in this lane (`curl`, 4 546 575 bytes) and hashed to
`1b848c19...`, matching the boxed value; a byte-identical copy was already present at
`/tmp/nori_ens1983.pdf` and both hash the same. All Nori statements were read from
200-dpi rasters produced with `mutool draw` (§0.1) because the NUMDAM OCR text layer
mangles formulas — this is what surfaced errata (E1) and (E2); the text layer was
used only for locating statements. Journal pages consumed: 305-306 (WLT, `r(C)`),
310 (Definition 1.1, Facts 1.2, 1.4 A, 1.4 B), 315 (Corollary 2.5), 322 (Lemma 3.17),
330 (Definition 3.25, Proposition 3.26, Remark), 331 (proof of 3.26, Proposition 3.27
and its proof), 332-333 (Lemmas 5.1, 5.2), 336 (Proposition 6.5, Remark 6.6, Example
6.7). No other literature was fetched; Teissier's `delta`-constant fact (§6.2) is
cited as classical and is **not** hashed — it is used only inside the OPEN discussion
of (ii-a), never in Theorem N-A or its corollary. The two `pi_1` computations of
§4.3 and §6.4 are hand Zariski-van Kampen arguments; each was cross-checked against
the independently known `H_1(P^2 - D)`. No canonical ledger, charged file, or
`jc2-lean` was touched.

<!-- SECTION 8 END -->

<!-- BODY-END -->
