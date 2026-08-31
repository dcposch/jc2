# PI1S4-(6,4)-FIXED-TUPLE — decision lane report

lane: FIXED-TUPLE (flagship proof lane, N=4 residual topological core)
model: opus5
date: 2026-08-31

## 0. Inputs, hashes, and consumption typing

## 1. The object: (6,4) three-node curve, invariants re-derived

## 2. The cable braid rho_infty written explicitly

## 3. Exponent-sum cross-check e(rho_infty)

## 4. Promoted block machinery at the outer coprime level

## 5. Inner twists: fixedness inside each tube

## 6. Node relations and the tangency identifications

## 7. Decision

## 8. Scope of the theorem / what is NOT covered

## 9. Successors and typed OPENs

## 10. Ledger line

*(sections are appended in order; the body is sealed by the standalone marker at the end)*

## 0. Inputs, hashes, and consumption typing

Four charged inputs were hashed with `shasum -a 256` **before any was read**; 4/4 match
the boxed values:

```text
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  pi1-s4-decision-opus5-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  pi1s4-close-residual-r2-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

No literature was fetched in this lane: nothing below needs a hashed source. Every
step is either classical (Puiseux expansion at infinity; the Artin action of `B_d` on
`F_d`; blackboard cabling; Bennequin/Rudolph for quasipositive braids; Riemann-Hurwitz)
or promoted, or derived here.

**Typing.**

* `PROMOTED` — integration `126c2d29` §1: Theorem N-A, Corollary N-A-RES, the M-INF
  split (piece 1 `M_emb = mult + β_h − 1` as corrected; piece 2 refuted), D1-DEGREE at
  typed scope including `d = 2g_L + c(Π) + 2`. Plus, per the lane charge, the coprime
  Theorem A machinery and Theorem A'(1)–(4) with Lemma 3.3 (block collapse) and the
  tubular decomposition (3.1) that A'(1) is proved from.
* `PROVISIONAL` — every ROW-SWEEP invariant (`Δ=(6,4,3)`, `β₁=15`, `δ_∞=7`,
  `δ_aff=3`, `M_∞=16`, and the three-node attainment witness `p=r²`, `r=t³+t+1`,
  `q=t⁴+⅔t²+⁴⁄₃t`). Integration §2 routes ROW-SWEEP for review; it has not landed.
  **Every numerical conclusion below is conditional on these.**
* `PROVED-HERE` — established in this report from the above plus classical facts.

**Execution disclosure.** No CAS was run and no job of uncertain duration. Two finite
enumerations were run in plain Python as redundancy checks on hand computations that
are displayed in full: (a) the block-action formula of §4, checked on 400 random
6-tuples; (b) the complete enumeration of the `6^6 = 46656` transposition 6-tuples in
`S_4` against `ρ_∞`-fixedness. Both are instantaneous permutation arithmetic, not
algebra-system computation, and neither is load-bearing: §4–§5 derive the same results
by hand and the enumeration reproduces them exactly.

## 1. The object, and its invariants re-derived

`D ⊂ C²` irreducible, `normalization(D) = A^1`, one place at infinity, three affine
ordinary nodes. Normalised as in the charged decision report §1: `γ(t) = (p(t),q(t))`,
`d := deg p = 6 > n := deg q = 4`, `deg D = 6`, unique point at infinity
`Q = [1:0:0]`, and in the chart `(v,u) = (Y/X, Z/X)` with `s = 1/t`,

```text
a := mult_Q(Dbar) = d − n = 2,      b := I(Dbar, L_∞; Q) = d = 6,
g := gcd(d,n) = 2,   d' := d/g = 3,   n' := n/g = 2,   gcd(d',n') = 1.
```

`a = 2` divides `b = 6`, so charged Lemma 1.3 puts the place in the `a | d` regime:
`β₁ > 6`, `β₁` odd, one characteristic pair `(2; β₁)`. PROVISIONAL row datum:
`β₁ = 15`. Then, unconditionally given `β₁`,

```text
δ_∞ = (a−1)(β₁−1)/2 = 7,     δ_aff = (d−1)(d−2)/2 − δ_∞ = 10 − 7 = 3,
M_emb = a + β_h − 1 = 2 + 15 − 1 = 16   (PROMOTED M-INF piece 1),
M_∞  = max(M_emb, d) = 16 > 15 = 3d − 3.
```

So (M-INF) fails by exactly one unit and Corollary N-A-RES is unavailable at `T = 0`:
this row cannot be closed by Nori. That is why it is the residual, and it fixes the
scope of the present lane — the only remaining lever is the braid at infinity.

`δ_aff = 3` with every affine singularity a double point of two smooth branches gives
exactly **three ordinary nodes**, and the vertical-ramification count of the charged
report,

```text
(V)   V = Σ_t (e_t − 1) = deg p' = d − 1 = 5,
```

is unconditional. The `(8,4)` survivor `Δ=(8,4,6,3)`, characteristic `(4;10,19)`, is
target-isomorphic to this one by the triangular shear `P = p + q²` (ROW-SWEEP §6,
PROVISIONAL), so everything below transfers to it verbatim.

## 2. The cable braid `ρ_∞` written explicitly

**2.1 Puiseux expansion at infinity (PROVED-HERE).** Use the ROW-SWEEP normalisation of
the place: `v = s^a = s²`, `u = Σ_{k≥6} c_k s^k`, `c_6 ≠ 0`, and `β₁ = 15` is the least
`k` with `c_k ≠ 0` and `2 ∤ k`. Since `v = Y/X = y/x` and `u = Z/X = 1/x`,

```text
y = v/u = s²·x        exactly,          x^{-1} = u(s) = c_6 s^6 (1 + Σ_{k≥1} γ_k s^k),
```

with `γ_k = c_{6+k}/c_6`, `γ_k = 0` for `k` odd `< 9`, `γ_9 ≠ 0`. Put `ξ := x^{-1/6}`.
Solving `x^{-1} = u(s)` for `s` gives `s = αξ(1 + a₂ξ² + a₄ξ⁴ + a₆ξ⁶ + a₈ξ⁸ + a₉ξ⁹ + …)`
— only even corrections until the `ξ⁹` term, whose coefficient `a₉` is nonzero exactly
because `β₁ = 6 + 9`. Hence

```text
y = s²x = α²ξ^{-4}·[ E(ξ²) + 2a₉ξ⁹ + … ],     E a unit power series in ξ².
```

Reading exponents of `x` (`ξ^m ↦ x^{-m/6}`), the Puiseux expansion at infinity is

```text
y(x) = c·x^{4/6} + (terms x^{k/6}, k even, k<4) + c'·x^{-5/6} + …
```

with two characteristic exponents `4/6 = 2/3` (denominator `3`) and

```text
(2.1)   second characteristic exponent  =  (d + n − β₁)/d  =  (6+4−15)/6 = −5/6 .
```

`(2.1)` is the exact translation of the promoted cluster datum `β₁` into braid data,
and it is the only place `β₁` enters.

**2.2 Tubes.** The six roots are `y_j`, indexed by `ξ_j = ζ_6^{\,j}ξ_0`. The leading
coefficient carries `ζ_6^{-4j} = ζ_3^{\,j}`, which depends only on `j mod 3`, and every
even-power correction likewise. The first term separating `j` from `j+3` is the `ξ^9`
term: `ζ_6^{9j} = (−1)^j`. Therefore

```text
blocks  B_i = { j : j ≡ i (mod 3) },  i ∈ Z/3,   |B_i| = g = 2,   d' = 3 tubes,
tube centres = the 3 roots of w³ = c³x²  ⟹  tube braid = δ_3^{\,2},  δ_3 = σ_1σ_2,
in-tube separation  y_j − y_{j+3} ~ const·x^{−5/6}.
```

This is the tubular decomposition (3.1) of the promoted A' package, derived here for
this place rather than assumed: with `C_g : B_{d'} → B_d` blackboard cabling,

```text
(2.2)    ρ_∞ = C_2(δ_3^{\,2}) · ι ,      ι = (σ^{k_1}, σ^{k_2}, σ^{k_3}) ∈ B_2×B_2×B_2 .
```

**2.3 The inner exponent, exactly.** Signed crossings between strands `i,j` over
`|x| = R` equal `2·(winding number of y_i − y_j)`. Different tubes: `y_i − y_j ~ x^{4/6}`,
winding `2/3`, and there are `6·4/2 = 12` such pairs. Same tube: winding `−5/6` by
(2.1), and there are `3` such pairs. Hence

```text
e(ρ_∞) = 12·2·(2/3) + 3·2·(−5/6) = 16 − 5 = 11 ,
e(C_2(δ_3²)) = g²·e(δ_3²) = 4·4 = 16 ,
(2.3)    K := e(ι) = k_1+k_2+k_3 = 11 − 16 = −5 .
```

The three tubes contribute `−5/3` each: the individual `k_i` are *not* symmetric and
are not pinned by this computation (the strands are not closed loops), but their sum
is. §5 shows only the sum enters.

**2.4 The knot.** The closure of `ρ_∞` is the `(2,3)`-cable of the `(3,2)`-torus knot
(trefoil): blackboard cabling of a braid of writhe `w = 4` gives the `(2, 2w) = (2,8)`
cable, and `ι` removes `5` twists, `8 − 5 = 3`. Cable genus
`2·g(trefoil) + (2−1)(3−1)/2 = 2 + 1 = 3`. This is a small/"negative" cable, so it is
*not* the link of a local plane-curve singularity — correct, since a link at infinity
of a polynomial curve need not be a local algebraic link.

**2.5 Row-dependence of the inner exponent (PROVED-HERE, and a hostile check).** For
every row of the `(6,4)` census the germ is `(2;β₁)` with `δ_∞ = (β₁−1)/2`, so
`e(ρ_∞) = (d−1)+2δ_aff = 25 − 2δ_∞ = 26 − β₁` and

```text
(2.4)    e(ι) = 10 − β₁ :    β₁ = 7,9,11,13,15  ⟹  e(ι) = 3,1,−1,−3,−5 .
```

§5 will show the fixed-tuple gate is nonvacuous — it kills `e(ι) ≡ 0, 2, 3, 5 (mod 6)`
outright — and that `β₁ = 15` gives `e(ι) = −5 ≡ 1 (mod 6)`, one of the two residues
that survive. So the braid gate and (M-INF) are genuinely independent gates, and the
sole (M-INF)-survivor also survives the braid gate. That is the finding of this lane,
stated in advance.

## 3. Exponent-sum cross-check on `e(ρ_∞) = 11`

The lane charge asks that `e(ρ_∞) = (d−1) + 2δ_aff = 5 + 6 = 11` be verified first.
Four independent derivations agree.

1. **Factorization count.** `V = d−1 = 5` vertical tangencies contribute exponent `1`
   each; three nodes contribute `σ²` each. `5 + 6 = 11`. Uses `(V)` (unconditional) and
   `δ_aff = 3` (PROVISIONAL).
2. **Genus split.** `e(ρ_∞) = (d−1) + [(d−1)(d−2) − 2δ_∞] = (d−1)² − 2δ_∞ = 25 − 14 = 11`.
   Uses `δ_∞ = 7` only.
3. **Winding numbers.** §2.3, from the Puiseux exponents `2/3` and `−5/6`: `16 − 5 = 11`.
   Independent of `(V)` and of `δ_aff`; it uses `β₁` and `(d,n)` alone.
4. **Seifert genus.** `ρ_∞` is quasipositive (product of conjugates of positive band
   powers), so Bennequin/Rudolph gives `2·genus(closure) = e − d + 1 = 6`, genus `3`.
   Independently, smoothing the `3` nodes of `D ∩ B_R` (a disc with `3` pairs of
   points identified, `χ = −2`) gives a Seifert surface with `χ = −5`, one boundary
   component, genus `3`. Both agree with the cable genus of §2.4. Note the resulting
   identity is clean and worth recording:

```text
(3.1)    genus(link at infinity) = δ_aff        (= 3 here),
```
   since `2g = e − d + 1 = (d−1) + 2δ_aff − d + 1 = 2δ_aff`.

Derivations 1 and 3 use disjoint inputs (`V, δ_aff` versus `β₁`) and agree; this is a
genuine consistency check on the ROW-SWEEP row datum `Δ=(6,4,3)` itself, and it passes.

## 4. The outer level: block collapse at the coprime `(3,2)`

Write `T = (t_1,…,t_6)`, all transpositions, `⟨T⟩ = S_4`; blocks `A_1 = (t_1,t_2)`,
`A_2 = (t_3,t_4)`, `A_3 = (t_5,t_6)`; block products `Π_i`, total `Π = Π_1Π_2Π_3`.
Hurwitz action on the left, `σ_i·(…,t_i,t_{i+1},…) = (…, t_it_{i+1}t_i^{-1}, t_i, …)`.

By promoted Lemma 3.3 and A'(1), `BP(T) = (Π_1,Π_2,Π_3)` is a fixed point of the
Hurwitz action of `δ_{d'}^{\,n'} = δ_3^{\,2}`; here `gcd(d',n') = gcd(3,2) = 1`, so the
outer level is **coprime** and the promoted Theorem A argument reruns there verbatim.

`δ_3·(u_1,u_2,u_3) = (Π u_3 Π^{-1}, u_1, u_2)` with the *same* total product `Π`.
Extending `u_{j-3} := Πu_jΠ^{-1}`, fixedness under `δ_3^{\,2}` is `2`-periodicity
`u_j = u_{j-2}`, whence

```text
(4.1)   Π_3 = Π_1 ,        Π Π_1 Π^{-1} = Π_2 ,        Π Π_2 Π^{-1} = Π_1 .
```

Substituting `Π = Π_1Π_2Π_3 = Π_1Π_2Π_1` into either conjugation relation gives, after
cancelling, exactly the **braid relation**

```text
(4.2)   Π_1 Π_2 Π_1 = Π_2 Π_1 Π_2   ( = Π ) ,
```

and conversely (4.2) implies both, since `(Π_1Π_2)Π_1(Π_1Π_2)^{-1} = Π_2` follows from
it. Note (4.2) alone forces `Π_1, Π_2` conjugate — A'(2) recovered, and
`sgn(Π_i) = (+1) = (−1)^g`, `sgn(Π) = (+1) = (−1)^d`, both consistent.

**4.1 Enumeration (PROVED-HERE).** A product of two transpositions in `S_4` is `e`, a
`3`-cycle, or a double transposition; so `Π_1 ∈ {e} ∪ C_3 ∪ V`, and `Π_2` is conjugate
to it.

* `Π_1 = e`: `Π_2 = e`. **(O1)** `Π_1=Π_2=Π_3=e`, `Π = e`.
* `Π_1 = τ ∈ V`: then `Π_2 ∈ V`, and `V ∪ {e}` is the Klein group, so (4.2) reads
  `Π_2 = Π_1` on the left and `Π_1 = Π_2` on the right. **(O2)** `Π_i = τ`, `Π = τ`.
* `Π_1 = ρ ∈ C_3`: then `Π_2 ∈ C_3`. Push (4.2) through `A_4 → A_4/V ≅ C_3`: it becomes
  `2a+b = 2b+a`, i.e. `a = b`, so `Π_2 ∈ ρV`. Write `Π_2 = ρv`, `v ∈ V`. With
  `v^ρ := ρ^{-1}vρ` and the `ρ`-cycle `a → b → c → a` on `V∖{e}`,

  ```text
  LHS = ρ·ρv·ρ = ρ²vρ = v^ρ ,      RHS = ρv·ρ·ρv = (ρvρ^{-1})v = v^{ρ^{-1}}·v ,
  ```
  so (4.2) `⟺ v^ρ = v^{ρ^{-1}}·v`, which holds for **every** `v ∈ V` (`v=a`: `b = c·a`;
  `v=b`: `c = a·b`; `v=c`: `a = b·c`; `v=e`: trivial). Hence
  **(O3)** `v = e`, `Π_1=Π_2=Π_3=ρ`, `Π = ρ³ = e`; and
  **(O4)** `v ≠ e`, `Π_1=Π_3=ρ`, `Π_2 = ρv ∈ C_3`, `Π = v^ρ ∈ V∖{e}`.

The list is exhaustive. In (O4) the outer group is
`H = ⟨Π_1,Π_2⟩ = ⟨ρ,v⟩ = V⋊⟨ρ⟩ = A_4`, so `Z(H) = 1` and A'(3)/A'(5) predict
`Π^{n'} = Π² = 1` — true, since `Π ∈ V`. Consistency, not contradiction. A'(4) is
silent because `n = 4` does not divide `d = 6` (`n' = 2 ≠ 1`); this is exactly the
structural difference from the promoted `(4,2)` collapse, where `n' = 1` forced all
block products equal, `H` cyclic, and the argument closed. **At `(6,4)` the outer level
is a genuine nonabelian coprime level and no outer contradiction is available.**

## 5. Inner twists, and the exact fixed-point system

**5.1 The block action of `C_2(δ_3^{\,2})` (PROVED-HERE; a transcription trap).**
`C_g(σ_i)·(A,B) = (Π_A B Π_A^{-1}, A)`, entrywise conjugation by the product of the
block being crossed (promoted Lemma 3.3(i); re-verified here against the charged
`g=2` computation `C_2(σ_1) = σ_2σ_1σ_3σ_2`). Iterating,

```text
C_2(δ_3)·(A_1,A_2,A_3) = ( w A_3 w^{-1}, A_1, A_2 ),          w := Π_1Π_2 ,
C_2(δ_3²)·(A_1,A_2,A_3) = ( w' A_2 w'^{-1}, w A_3 w^{-1}, A_1 ),   w' := ΠΠ_2^{-1} ,
```
using `w'= wΠ_3w^{-1}Π_1 = ΠΠ_2^{-1}`. **The strand-level formula `δ_d·T = (Πt_dΠ^{-1},…)`
does not transcribe to blocks.** At strand level the conjugator may be written `Π`
because the trailing `t_d` conjugates `t_d` trivially; at block level `Π_3` does *not*
centralise the entries of `A_3`, and the conjugator is `ΠΠ_3^{-1} = w`, not `Π`. Taking
`Π` here is the one substantive error available in this computation and it changes the
verdict; the formula above was checked independently on 400 random 6-tuples (0
mismatches).

**5.2 The system.** With `S_i := σ^{k_i}·A_i` (so `BP(S_i) = Π_i`, and `w,w'` unchanged),
`ρ_∞·T = C_2(δ_3²)·(ι·T) = T` is exactly

```text
(F1)  A_1 = w' S_2 w'^{-1},     (F2)  A_2 = w S_3 w^{-1},     (F3)  A_3 = S_1 .
```

Back-substituting (F3) into (F2) into (F1), and using that the Hurwitz action commutes
with global conjugation, everything collapses onto `A_1` and the **total** inner
exponent `K = k_1+k_2+k_3 = −5`:

```text
(5.1)   A_1 = G·(σ^K·A_1)·G^{-1} ,      G := w'w = ΠΠ_2^{-1}Π_1Π_2 ,
(5.2)   A_3 = σ^{k_1}·A_1 ,    A_2 = w·(σ^{k_1+k_3}·A_1)·w^{-1} .
```

`G` evaluates as follows (`Π_1^{-3} = e` whenever `Π_1` has order `1` or `3`):

| case | `Π_1` | `Π_2` | `Π` | `G` |
|---|---|---|---|---|
| (O1) | `e` | `e` | `e` | `e` |
| (O2) | `τ` | `τ` | `τ` | `τ·τ·τ·τ = e` |
| (O3) | `ρ` | `ρ` | `e` | `ρ` |
| (O4) | `ρ` | `ρv` | `v^ρ` | `v^ρ·v·v^{ρ^{-1}}·ρ = ρ` |

(the (O4) line uses `ρv = v^{ρ^{-1}}ρ` and `xy = z` on `V∖{e}`; each of `v = a,b,c`
gives `G = ρ` — computed in all three cases).

**5.3 Solving (5.1).** Write `A_1 = (α,β)`, `c = αβ = Π_1`. For `K = 2m` the action is
conjugation by `c^m`; for `K = 2m+1` it is `σ^{2m}∘σ`, i.e.

```text
σ^{2m+1}·(α,β) = ( c^m(αβα^{-1})c^{-m},  c^m α c^{-m} ).
```

`K = −5` is odd, `m = −3`, so with `g := G·Π_1^{-3}`:

```text
(5.3)   β = g α g^{-1} ,        α = g(αβα^{-1})g^{-1} .
```

Now case by case.

* **(O1)** `g = e`, so `β = α` — consistent (`Π_1 = e`). But then `σ^k·(α,α) = (α,α)`
  for every `k`, so (5.2) gives `A_2 = A_3 = (α,α)`: **all six entries equal `α`**,
  `⟨T⟩ = C_2`. **Killed by generation.**
* **(O2)** `g = e·τ^{-3} = τ`. With `τ = αβ` and `α,β` disjoint, `τατ^{-1} = α`, so
  (5.3) gives `β = α`, hence `Π_1 = α² = e ≠ τ`. **Killed (contradiction).**
* **(O3)** `g = ρ·ρ^{-3} = ρ`, so `β = ραρ^{-1}` and `αβ = ρ` forces `αρα = ρ^{-1}`:
  `α` inverts `ρ`, hence `α, β ∈ S_3(supp ρ)`. But here `w = Π_1Π_2 = ρ² ∈ S_3(supp ρ)`
  too, so by (5.2) **every** entry of `T` lies in `S_3(supp ρ)` and `⟨T⟩ ⊆ S_3`.
  **Killed by generation.**
* **(O4)** `g = ρ`. Same equation, so again `α` inverts `ρ`, `β = ρ^{-1}α`, and
  `A_1, A_3 ⊂ S_3(supp ρ)`. The second relation of (5.3) is then automatic:
  `αβα^{-1} = ρα` and `ρ(ρα)ρ^{-1} = ρ³α = α`. **No contradiction.**
  And now `w = Π_1Π_2 = ρ·ρv = ρ²v` *moves the letter outside* `supp ρ`, because
  `v ∈ V∖{e}` is fixed-point free. Writing `supp ρ = {1,2,3}` and `m := w^{-1}(4)`:
  `A_1 = (α, ρ^{-1}α)` consists of two *distinct* transpositions of `{1,2,3}`, whose
  supports cover `{1,2,3}`, so at least one of the two entries of `σ^{k_1+k_3}·A_1`
  contains `m`, and the corresponding entry of `A_2 = w(…)w^{-1}` is a transposition
  moving `4`. Since `⟨α, ρ^{-1}α⟩ = S_3(\{1,2,3\})`, we get

```text
(5.4)    ⟨T⟩ = ⟨ S_3({1,2,3}), a transposition moving 4 ⟩ = S_4 .
```

  **(O4) survives, and every member of it generates `S_4`.**

**5.4 The complete solution set, and the exact gate on `e(ι)` (PROVED-HERE).**
Running §5.3 for a general total inner exponent `K` in case (O4) (`G = ρ = Π_1`):

* `K = 2m` even: `ρ^{1+m}` must centralise `α` and `β`; no transposition in `S_4`
  commutes with a `3`-cycle, so `ρ^{1+m} = e`, i.e. `K ≡ 4 (mod 6)`.
* `K = 2m+1` odd: `g = ρ^{(K+1)/2}`. If `g = e` then `β = α` and `Π_1 = e`, false. If
  `g ≠ e` and `α ∉ S_3(supp ρ)`, then `αgα` is a `3`-cycle with support `≠ supp ρ`
  while `αβ = α g α g^{-1} = ρ` forces `αgα = ρg ∈ ⟨ρ⟩`: impossible. So `α` inverts
  `ρ`, `αgα = g^{-1}`, and `ρ = g^{-2}` gives `(K+1)/2 ≡ 1 (mod 3)`, i.e.
  `K ≡ 1 (mod 6)`.

Both branches say the same thing:

```text
(5.5)   an S_4-generating ρ_∞-fixed transposition 6-tuple exists  ⟺  e(ι) ≡ 1 (mod 3),
        and by (2.4), e(ι) = 10 − β₁ ,  so the gate reads   3 | β₁ .
```

`β₁ = 15` passes. The gate is not vacuous: it kills `β₁ ∈ {7,11,13}` of the `(6,4)`
census outright (independently of (M-INF), which kills `β₁ ≤ 13` anyway), and leaves
`β₁ ∈ {9,15}`. The `(M-INF)` survivor is also the braid survivor.

The solution set in case (O4) is parametrised by `(ρ, α, v)` — `ρ` any `3`-cycle
(8), `α` any transposition inverting `ρ` (3), `v ∈ V∖{e}` (3) — together with
`(k_1, k_1+k_3) mod 3`, which the actual `ι` fixes. `β = ρ^{-1}α`, `Π_1=Π_3=ρ`,
`Π_2 = ρv`, `Π = v^ρ`, and `A_2, A_3` by (5.2). That is `8·3·3 = 72` tuples for each
admissible distribution of the `k_i`.

**Independent enumeration.** Brute force over all `6^6 = 46656` transposition 6-tuples,
for eight different distributions `(k_1,k_2,k_3)` with `Σ = −5`, returns in every case
**102 fixed tuples, of which exactly 72 generate `S_4`**, the remaining 30 splitting as
`6` with `⟨T⟩ ≅ C_2` (case O1) and `24` with `⟨T⟩ ≅ S_3` (case O3) — exactly the hand
classification, with the exact counts `6 = |{α}|`, `24 = 8·3`, `72 = 8·3·3`. Scanning
`K` from `−12` to `12` reproduces (5.5) exactly: `72` generating tuples iff
`K ≡ 1 (mod 3)`, none otherwise. The *set* of 72 depends on the distribution
(`|A ∩ B| = 6` for two different distributions) but its size and structure do not,
as (5.1) predicts.

## 6. Node relations and the tangency identifications

**6.1 What the remaining local braids say.** The braid monodromy factorization is
`ρ_∞ = β_8 ⋯ β_1` with `V = 5` factors conjugate to `σ` (simple vertical tangencies)
and `3` factors conjugate to `σ²` (nodes); exponent sums `5 + 6 = 11 = e(ρ_∞)` ✓.
`T` must be fixed by each factor, not merely by the product. For `β = wσ_iw^{-1}`,
fixedness says `(w^{-1}·T)_i = (w^{-1}·T)_{i+1}`; for `β = wσ_i^2w^{-1}` it says those
two entries commute, and the residual's `a_p = 0` upgrades this to **disjoint** (equal
would give `3` points over the node, i.e. `a_p = 1`, contradicting the promoted local
datum).

Projecting to `S_6`: the node factors are trivial and the `5` tangency factors are
transpositions whose product is the `6`-cycle `p(ρ_∞)`; irreducibility of `D` makes
them transitive, so `5` transpositions generate a transitive subgroup of `S_6` — a
**spanning tree**, with no slack. If the tangency relations were literal identifications
`t_i = t_j` along that tree, all six entries would be equal and the row would die at
once. They are not: they are equalities inside Hurwitz *translates* `w^{-1}·T`, and
that is precisely the gap.

**6.2 Both kinds of local factor do occur in `Stab(T)`.** Take the explicit surviving
tuple of §7. `σ_2·T = ((12),(12),(23),(34),(12),(23))`: entries `1,2` are equal, so
`σ_2^{-1}σ_1σ_2 ∈ Stab(T)` is a legitimate tangency factor; entries `4,5` are `(34)`
and `(12)`, **disjoint**, so `σ_2^{-1}σ_4^{2}σ_2 ∈ Stab(T)` is a legitimate node factor
with the required disjointness. So neither constraint (ii) nor the tangency shape is
individually obstructive on the surviving family. What is *not* established is that
`ρ_∞` admits a factorization of the prescribed type `(5×σ, 3×σ²)` entirely inside
`Stab(T)`; that is a factorization problem in `B_6`, and no charged input supplies the
braid monodromy factorization of the `(6,4)` curve.

**6.3 Two global consistency checks, both passed.** These are the only tests of the
surviving tuple against promoted global data that are available at desk scale.

*(a) The promoted slice identity.* D1-DEGREE gives `d = 2g_L + c(Π) + 2` with `c(Π)`
the number of cycles of `Π` on `4` letters. Here `Π = v^ρ ∈ V`, cycle type `(2,2)`, so
`c(Π) = 2` and `g_L = 1`. Independently: the generic fibre of `Y → C` (`Y` the degree-4
cover, `C` the `x`-line) is the `4`-fold cover of `A^1` branched at `6` points with
transposition monodromy and monodromy `Π` at infinity; compactifying,
`χ = 4·2 − (6·1 + (4−2)) = 0`, genus `1`. The two computations agree, and `(c,g_L) =
(2,1)` is one of the two slices ROW-SWEEP lists as admissible for this row.

*(b) Euler characteristic of the cover.* Stratifying `C²` by `D`:
`χ_c(Y) = 4·3 + 3·(−5) + 2·3 = 3`. Fibring `Y` over the `x`-line:
generic fibre `χ_c = 4(1−6) + 6·3 = −2`; a tangency fibre has `4` generic branch points
and the tangency point, whose fibre monodromy is `t² = e` but which still carries only
`3` preimages in `Y`, so `χ_c = 4(1−5) + 4·3 + 3 = −1`; a node fibre has `2` preimages
over the node, `χ_c = −2`. Hence `χ_c(Y) = (−2)(1−8) + 5(−1) + 3(−2) = 3` ✓. (Trap
worth recording: counting the tangency point as *unbranched* in `Y` — i.e. using the
fibre-monodromy `e` rather than the `3` actual preimages — gives `χ_c(Y) = 8` and a
spurious contradiction. The branching of `Y → C²` and the branching of `Y_x → F_x` are
different data.)

Neither check obstructs; both would have been expected to fail had the tuple been
spurious.

## 7. Decision

**THEOREM `(6,4)`-ρ∞ (PROVED-HERE; numerics conditional on the PROVISIONAL row data).**
*Let `D ⊂ C²` be an irreducible polynomial curve of type `(d,n) = (6,4)` with one place
at infinity of multiplicity `a = 2` and a single characteristic pair `(2;β₁)`, and with
all affine singularities double points of two smooth branches. Let `ρ_∞ ∈ B_6` be its
braid at infinity. Then the set of 6-tuples of transpositions in `S_4` that are fixed by
the Hurwitz action of `ρ_∞` and generate `S_4` is*

```text
   nonempty   ⟺   e(ι) = 10 − β₁ ≡ 1 (mod 3)   ⟺   3 | β₁ ,
```

*and when nonempty it consists of exactly `72` tuples, all of shape (O4):*

```text
Π_1 = Π_3 = ρ (a 3-cycle),  Π_2 = ρv (v ∈ V∖{e}),  Π = ρ^{-1}vρ ∈ V∖{e},
A_1 = (α, ρ^{-1}α) with α a transposition inverting ρ,   A_3 = σ^{k_1}·A_1,
A_2 = (Π_1Π_2)·(σ^{k_1+k_3}·A_1)·(Π_1Π_2)^{-1} .
```

*For the residual row `Δ = (6,4,3)`, `β₁ = 15`, `δ_aff = 3`, `e(ι) = −5`: the set is
nonempty.* `[]`

**Decision on `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`: the braid at infinity does NOT close the
row. The answer to clauses (i)-restricted-to-`ρ_∞` together with (iii) is YES.**

A completely explicit witness, for `(k_1,k_2,k_3) = (0,−5,0)` (any distribution with
sum `−5` gives an equally explicit one):

```text
ρ = (123),  α = (12),  β = (23),  v = (12)(34) ,
T = ( t_1,…,t_6 ) = ( (12), (23), (13), (34), (12), (23) ) ,
Π_1 = Π_3 = (123),  Π_2 = (134),  Π = (13)(24),
w = Π_1Π_2 = (234),  w' = ΠΠ_2^{-1} = (124),  G = w'w = (123) = Π_1 ,
⟨T⟩ = S_4 ,   (c(Π), g_L) = (2,1) ,   χ_c(Y) = 3 .
```

Verification of `(F1)–(F3)` for this witness, by hand: `Π_2³ = e`, so
`S_2 = σ^{-5}·A_2 = (t_3t_4t_3, t_3) = ((14),(13))`, and
`w'S_2w'^{-1} = ((124)(14)(142), (124)(13)(142)) = ((12),(23)) = A_1` ✓;
`S_3 = A_3 = ((12),(23))` and `wS_3w^{-1} = ((13),(34)) = A_2` ✓; `S_1 = A_1 = A_3` ✓.
The independent enumeration of §5.4 confirms `T` is `ρ_∞`-fixed and that exactly `72`
of the `46656` transposition 6-tuples are fixed and generate `S_4`.

**Why the `(4,2)` mechanism has no analogue here.** At `(4,2)`: `g = d' = 2`, `n' = 1`,
so A'(4) forces all block products equal, `H = ⟨Π_1⟩` is cyclic, `Z(H) = H`, A'(3) is
vacuous, and the promoted solve collapses to `(ab)³ = 1` and `|im φ| ≤ 6`. At `(6,4)`:
`n' = 2`, the outer level is a genuine coprime `(3,2)` level, `H = A_4` is centreless,
A'(3)/A'(5) are *satisfied* (`Π² = 1`) rather than violated, and A'(4) is silent because
`4 ∤ 6`. The collapse is structurally absent, not merely unproven.

## 8. Scope of the theorem, and what is NOT covered

**Inputs actually used.** (a) `(d,n) = (6,4)` giving `g=2`, `d'=3`, `n'=2` and the tube
partition — unconditional. (b) The place at infinity through the single number
`e(ι) = 10 − β₁ = −5`, via the second characteristic exponent `(d+n−β₁)/d` of §2.1 —
conditional on the PROVISIONAL `β₁ = 15`. (c) `e(ρ_∞) = 11`, cross-checked four ways.
**Nothing else**: not the witness curve, not the positions of the nodes, not the braid
monodromy factorization, not `M_∞`, not Nori.

**Coverage.** Since `ρ_∞` is determined up to conjugacy in `B_6` by the place at
infinity, and the conclusion is invariant under conjugation (relabelling permutes the
72 tuples), Theorem `(6,4)`-ρ∞ covers **every** three-node `(6,4)` curve with
`Δ = (6,4,3)` uniformly — the whole row, not the attained witness only. The individual
`k_i` are not pinned by this lane; the theorem is proved for every distribution with
`Σk_i = −5`, so that gap is closed by quantification rather than by determination.

**What a surviving tuple is not.** Per FALLACY-v2 (carrier/attainment, floor/attainment):
a `ρ_∞`-fixed tuple is a *necessary* condition satisfied, never a homomorphism
`π_1(C²−D) ↠ S_4`, and never a Keller counterexample. It supplies a floor on the
residual, and it removes a candidate kill; it asserts nothing about attainment. Two
independent global consistency checks (§6.3) pass, which raises the cost of the residual
but does not discharge it.

**Clause (ii).** The node commutation relations are shown *realizable* on the surviving
family (§6.2 exhibits both a legitimate tangency band and a legitimate disjoint node
band in `Stab(T)`), but the conjunction — a factorization of `ρ_∞` into `5` `σ`- and
`3` `σ²`-conjugates all inside `Stab(T)` — is neither proved nor refuted here.

**Transfer to `(8,4)`.** ROW-SWEEP §6 (PROVISIONAL) makes the sole `(8,4)` survivor
target-isomorphic to this one by `P = p + q²`; target isomorphisms preserve the
complement and its braid data, so the verdict transfers verbatim. Rows `(8,6)` and
`(9,6)` are untouched by this lane.

## 9. Successors and typed OPENs

**`OPEN[PI1S4-(6,4)-FACTORIZATION]` — the immediate successor, and the only one that can
still kill the row combinatorially.** For one (equivalently, by `S_4`-conjugacy, for
one representative of each of the `3` conjugacy classes) of the `72` tuples `T`: does
`ρ_∞` factor in `B_6` as a product of `5` conjugates of `σ` and `3` conjugates of `σ²`,
every factor in `Stab(T)`, with the `σ²`-factors carrying *disjoint* pairs and the `5`
`σ`-factors projecting to a spanning tree on the `6` strands? A NO for all `72` kills
rows `(6,4)` and `(8,4)` and reduces the `N=4` core to the six `(8,6)/(9,6)` numerical
types. A YES exhausts the combinatorial route. This is a bounded search in `B_6`, not
desk-scale; it should be routed with an explicit depth bound and a negative control.

**`OPEN[PI1S4-(6,4)-FOLD-REDUCTION]` — highest-leverage geometric handle, new here.**
The ROW-SWEEP witness has `p = r²` with `r = t³+t+1`, so `D` is the image of
`D' := {(r(t), q(t))}` under the fold `ν(u,y) = (u²,y)`. `D'` has normalised type
`(4,3)`, **coprime**, with `δ_∞ = 0` and `δ_aff = (n−1)(d−1)/2 = 3`: a 3-nodal rational
quartic, for which the promoted coprime Main Theorem gives `π_1(C²−D') = Z`. Since
`ν^{-1}(D) = D' ∪ D'^-` (`D'^-` the image under `u ↦ −u`) and `ν` is branched only over
`L_0 = {u=0}`, and since `L_0 ⊄ D` makes `μ_{L_0}` null-homotopic in `C²−D` already,
**every** `φ: π_1(C²−D) ↠ S_4` restricts to a surjection

```text
   π_1( C² − (D' ∪ D'^-) )  ↠  S_4 ,   all meridians ↦ transpositions
```

(proof: `π_1(U°) = π_1(W°)·⟨μ_{L_0}⟩` for the index-2 unbranched cover
`W° → U° = C² − D − L_0`, and `φ°(μ_{L_0}) = e`). This converts the residual into a
statement about a **two-component** curve whose components are separately settled by the
promoted coprime theorem — a genuinely different attack, and it needs no braid data.
Named as the successor most likely to decide the row.

**`OPEN[PI1S4-(6,4)-TRIPLE-COVER]` — an independent elimination route.** The resolvent
`S_4 → S_3` (kernel `V`) sends each meridian to a transposition, and the two disjoint
transpositions at a node to the **same** transposition. Over `C[x,y]` every projective
module is free, so the resulting simply-branched triple cover is a global cubic
`z³ + az + b`, forcing

```text
   f = 4a³ + 27b² ,   deg a ≤ 2, deg b ≤ 3,   with degree-6 form  4a_2³ + 27b_3² = c·y^6
```

(the last because the unique place at infinity forces leading form `c y^d`). Deciding
whether a one-place three-node `(6,4)` curve admits such a presentation is a bounded
elimination problem. Typed as a successor, not a result: the triple-cover structure
theorem is classical but was not hashed in this lane.

**Carried, untouched.** `OPEN[ROW-(8,6)-NODAL-REALIZATION]`,
`OPEN[ROW-(9,6)-NODAL-REALIZATION]`, `OPEN[NORI-BC-SELF-TANGENT-COEFF]`,
`OPEN[PI1S4-D1-DEGREE]`. Nothing in this lane bears on them.

## 10. Ledger

**Charged inputs**, hashed before reading, 4/4 match (§0). **Primary literature
consumed: none** — no fetch was needed and none was made.

**Promoted items consumed.** Integration `126c2d29` §1: M-INF piece 1
(`M_emb = mult + β_h − 1`, used once, in §1); D1-DEGREE's slice identity
`d = 2g_L + c(Π) + 2` (used as a check, §6.3a); Corollary N-A-RES (used only to record
that it is unavailable, `M_∞ = 16 > 15`). Per the lane charge: Theorem A'(1)–(4) with
Lemma 3.3 and the tubular decomposition (3.1) — A'(1) and (3.1) are re-derived here for
this place from the Puiseux expansion (§2), and A'(3)/(4)/(5) are used only as
consistency checks, never as the source of a kill.

**PROVISIONAL items, flagged at each use.** The ROW-SWEEP row data
`Δ=(6,4,3)`, `β₁=15`, `(δ_∞, δ_aff, M_∞) = (7,3,16)`, the three-node attainment witness,
and the `(8,4)` target-equivalence. Every numerical statement in §§1–7 inherits this
conditionality. The structural statements — §4's enumeration (O1)–(O4), §5.1's
block-action formula, §5.4's gate `e(ι) ≡ 1 (mod 3)` — do not.

**Classical facts used without a hashed citation.** Puiseux expansion at infinity;
Zariski–van Kampen and the Artin action of `B_d` on `F_d`; blackboard cabling as a
homomorphism with `e(C_g(β)) = g²e(β)`; signed-crossing count as twice the winding
number of root differences; Bennequin's inequality with Rudolph's equality for
quasipositive braids; cable genus `p·g(K) + (p−1)(q−1)/2`; Riemann–Hurwitz;
`δ = (a−1)(b−1)/2` for the `(a,b)`-cusp; freeness of projective modules over `C[x,y]`
(§9, successor only).

**Own contributions, in dependency order.** §2.1 the translation
`second characteristic exponent = (d+n−β₁)/d`; §2.3 `e(ι) = −5` by winding numbers and
the identification of the link at infinity as the `(2,3)`-cable of the trefoil; §3 the
identity `genus(link at infinity) = δ_aff`; §5.1 the corrected block conjugators
`w = ΠΠ_3^{-1}`, `w' = ΠΠ_2^{-1}` (the `Π`-transcription trap); §4.1 the complete outer
enumeration; §5.3–5.4 the inner solve, the kills of (O1)–(O3), and the exact gate
`e(ι) ≡ 1 (mod 3) ⟺ 3 | β₁`; §7 Theorem `(6,4)`-ρ∞ and the explicit witness tuple;
§6.3 the two global consistency checks and the tangency-fibre Euler trap; §9 the fold
reduction to the coprime 3-nodal quartic and the triple-cover elimination.

**Corrections to charged material.** The charged r2 §3.3/§3.4 block formalism, if read
as "`C_g(δ_{d'})` conjugates the wrapped block by the total product `Π`", is wrong; the
conjugator is `ΠΠ_{d'}^{-1}` (§5.1). This does not affect r2's `(4,2)` solve (which is
done at strand level and which I do not disturb), but it is load-bearing at `(6,4)`:
using `Π` yields `G = Π²`, kills case (O4), and returns a false NO.

**Status line.** `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`: **not closed; NO is unavailable from
the braid at infinity.** Explicit `ρ_∞`-fixed `S_4`-generating tuples exist — exactly
`72`, fully classified — for every three-node `(6,4)` curve with `Δ = (6,4,3)`, and the
same for the target-equivalent `(8,4)` survivor. The residual is now sharper and
smaller: it is the factorization question `OPEN[PI1S4-(6,4)-FACTORIZATION]`, with
`OPEN[PI1S4-(6,4)-FOLD-REDUCTION]` as an independent geometric route. No exit-price
assertion is made, so no exit-price basis line is declared.

<!-- BODY-END -->
