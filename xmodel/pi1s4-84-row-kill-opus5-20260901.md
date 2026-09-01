# ROW-84 — kill the (8,4) survivor with its own geometry

Lane: `pi1s4-84-row-kill-opus5-20260901`
Model: Opus 5. Started 2026-09-01T00:21Z. Budget 6h hard.
Mode: desk-scale exact reasoning; no CAS; literature fetch permitted with hashes.

## 0. Inputs, hashes, and standing constraints

## 1. Row normal form: the degree-(8,4) one-place family

### 1.1 The gcd/delta tower and the characteristic data

### 1.2 Closed-form family and its modulus

### 1.3 delta_aff by the direct method

### 1.4 The implicit octic and its singularity ledger

## 2. The resolvent target: gamma_inf and psi(gamma_inf)

### 2.1 The tangency census at degree 8

### 2.2 The fold/tower type of the projection

### 2.3 gamma_inf in the tangency generators

### 2.4 psi(gamma_inf) under the meridian-transposition S_4 representation

## 3. The projective classification input

### 3.1 What descends, and to what

### 3.2 Literature: triple planes with branch degree 8

### 3.3 Direct derivation from Miranda binary-cubic data at the (8,4) germ

## 4. Verdict

## 5. Ledger of charged claims, gaps, and successors

---

## 0. Inputs, hashes, and standing constraints

All four frozen inputs were rehashed with `shasum -a 256` **before any was read**;
4/4 match the boxed manifest, so the stop condition never fired.

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe  pi1s4-64-torus-check-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  pi1s4-64-triple-cover-close-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

**Literature fetched and hashed in this lane.**

| tag | source | URL | SHA-256 | used for |
|---|---|---|---|---|
| Sh12 | Shirane, *A note on normal triple covers over `P²` with branch divisors of degree 6*, arXiv:1211.2526v1 | `https://arxiv.org/pdf/1211.2526` | `b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153` | §1.1.3–1.1.7 (Miranda data, splitting inequality, triple-section criterion), Introduction (solved-case list) |

The hash reproduces the value already in custody at `pi1s4-64-torus-check-opus5-20260831.md`
§0 byte-for-byte — an independent third confirmation of that receipt. Sh12 §1.1 is a
statement of Miranda's theory (Miranda, *Triple covers in algebraic geometry*, AJM 107
(1985), Sh12's ref [8]); Miranda itself was **not** fetched and is cited only through
Sh12's displayed statements, which are quoted verbatim in §3.

**Typing.**

* `PROMOTED` — nothing from the coordinator integration is re-audited here.
* `CHARGED-PROVISIONAL` — Theorem ROW-NF and Theorem ROW-KILL of the charged
  TORUS-CHECK report (the latter proved there at ROW-NF scope), and the ROW-SWEEP
  row data `Δ=(8,4,6,3)`, `(4;10,19)`, `(18,3,22)`.
* `PROVED-HERE` — §1 in full (Theorem ROW-NF-84, Lemma FOLD, the germ and the
  singularity ledger), §2 in full (Lemma NO-FOLD, the tangency census, the local
  reformulation of `γ_∞`), §3.1–§3.3 (Theorem OCT-TRIPLE, Corollary OCT-SYZYGY,
  Lemma NO-INNER-NODE-8, the `m_∞` band).
* `SOURCED` — Sh12 §§1.1.3, 1.1.5, 1.1.6, 1.1.7 and Introduction, quoted verbatim.

**Execution disclosure.** No CAS was run; no job of uncertain duration was run. One
`curl` fetch and three `pdftotext` extractions were executed. Every number below is
hand-derived and displayed. No canonical ledger, charged file, or `jc2-lean` artefact
was written or inspected.

**Standing correction to the charge.** The charge writes "gcd tower 8,4 gives g=4 then
the 6,3". The tower is `d_0=8, d_1=4, d_2=2, d_3=1` with quotients `n_1=n_2=n_3=2`; the
`4` is `d_1`, not a terminal gcd, and the last two entries `6,3` reduce it to `1` in two
further steps. The charged characteristic `(4;10,19)` is re-derived independently in
§1.1 and confirmed.

---

## 1. Row normal form: the degree-(8,4) one-place family

Throughout, a *(8,4) row member* is a polynomial map `t ↦ (P(t),Q(t))`, birational onto
its image `D' ⊂ A²`, with `deg P = 8`, `deg Q = 4`, δ-sequence `Δ=(8,4,6,3)`, and affine
singularities exactly three ordinary nodes. `C' := D̄' ⊂ P²`, `L_∞ = \{Z=0\}`.
Scaling `x,y` makes `P,Q` monic; that is assumed from here.

### 1.1 The gcd/delta tower and the characteristic data

`Δ=(8,4,6,3)` is a legitimate Abhyankar–Moh δ-sequence: `d_0=8`, `d_1=4`, `d_2=2`,
`d_3=1`, quotients `n_1=n_2=n_3=2` (all `>1`); `n_1δ_1=8∈⟨8⟩`, `n_2δ_2=12∈⟨8,4⟩`,
`n_3δ_3=6∈⟨8,4,6⟩`; and `δ_2=6<n_1δ_1=8`, `δ_3=3<n_2δ_2=12`. The degree semigroup is
`Γ = ⟨8,4,6,3⟩ = ⟨3,4⟩`, whose gaps are `\{1,2,5\}`; three gaps, matching `δ_aff=3`.

**The germ at infinity, re-derived.** Homogenise `[X:Y:Z]=[P(t):Q(t):1]` and put
`s=1/t`, `\tilde P := s⁸P`, `\tilde Q := s⁴Q` (both units at `s=0`). In the chart `X=1`,
with `v=Y/X`, `w=Z/X`,

```text
   v(s) = s⁴·\tilde Q/\tilde P ,      w(s) = s⁸/\tilde P .                     (1.1)
```

So there is **one place**, at `Q_∞=[1:0:0]`, with `mult_{Q_∞}C' = min(4,8) = 4` and
`I(C',L_∞;Q_∞) = ord_s w = 8`. Bézout `8·1=8` is exhausted at `Q_∞`, so
`C'∩L_∞=\{Q_∞\}` and `L_∞` is the **tangent line** (contact `8 > 4`).

Both `ord v=4` and `ord w=8` lie in `4ℤ`, so the first genuinely new semigroup element
comes from a cancellation. Since `w - cv² = (s⁸/\tilde P²)(\tilde P - c\tilde Q²)` and
`\tilde P - c\tilde Q² = (1-c)+O(s)`, the only useful constant is `c=1`. Writing
`m := deg_t(P-Q²)`, we have `P-Q² = s^{-m}(\text{unit})`, hence
`\tilde P-\tilde Q² = s^{8-m}(\text{unit})` and

```text
   ord_s(w - v²) = 16 - m .                                                     (1.2)
```

Every element of `O_{Q_∞}` is a polynomial in `v` and `u_2 := w-v²`, whose orders are
`4` and `16-m`; so `β̄_1 = 16-m` is the first semigroup generator outside `⟨4⟩`.

Independently, `δ_2 = \min\{\deg(P-φ(Q)) : \deg φ ≤ 2\}`; subtracting `c_1Q+c_0` only
touches `t`-degrees `4` and `0`, so `δ_2 = m` whenever `m ≥ 5`, and `δ_2 ≤ 4` otherwise.
Therefore, on this row,

```text
   δ_2 = 6  ⟺  m = deg(P-Q²) = 6  ⟺  β̄_1 = 10 .                              (1.3)
```

This is the whole content of the row label, and it is the hinge of §1.2. (The other
`(8,4)` rows of the ROW-SWEEP census fall out of the same formula: `m=7,5,3` give
`β̄_1=9,11,13`, i.e. `gcd(4,β̄_1)=1` and the one-pair germs `(4;9),(4;11),(4;13)`;
`m=2,1` give `β̄_1=14,15`. Every entry of that table is reproduced by `(1.2)`.)

With `e_0=4`, `e_1=\gcd(4,10)=2`, `e_2=1`, the genus split `δ_aff+δ_∞=p_a=\binom{7}{2}=21`
and `δ_aff=3` give `δ_∞=18`, and the charged cluster identity
`2δ_∞ = (e_0-e_1)β_1+(e_1-e_2)β_2-a+1` reads `36 = 20+β_2-3`, so

```text
   (a;β_1,β_2) = (4;10,19) ,   β̄ = (4,10,29) ,   Γ_∞ = ⟨4,10,29⟩ .            (1.4)
```

`β̄_2 = n_1β̄_1+β_2-β_1 = 20+9 = 29`. Sanity: `⟨4,10,29⟩` has gaps `2,6` among the evens
and `1,3,…,27,31,35` among the odds — `2+16 = 18` gaps, so `δ_∞=18` and the conductor is
`36 = 2δ_∞` ✓. Also `M_{emb}=a+β_h-1=4+19-1=22`, `M_∞=\max(8,22)=22`, and `3d-3=21`:
**(M-INF) misses this row by exactly one unit**, which is why it survived.

Two local facts used later.

* **(F1′) Maximal smooth contact is 10.** With `u_1:=v` (order 4) and `u_2:=w-v²`
  (order 10), `O_{Q_∞}=C\{u_1,u_2\}` and `\mathrm{ord}(u_1^iu_2^j)=4i+10j`. A smooth germ
  is `ℓ = αv+βw+(\text{ord}≥2) = αu_1+β u_2+βu_1²+\sum_{i+j≥2}c_{ij}u_1^iu_2^j`. If
  `α≠0`, `ord ℓ=4`. If `α=0`, the term `βu_1²` (order 8) can be cancelled only by
  `c_{20}u_1²`, after which every remaining monomial has order `≥12`; and `4i+10j=10`
  forces `(i,j)=(0,1)`, which is not of order `≥2`. Hence `\max = 10`.
  (Contrast the `(6,4)` germ `A_{14}`, where the maximum is `15`.)
* **(F2′) Link type.** Newton pairs `(p_1,q_1)=(2,5)`, `(p_2,q_2)=(2,9)` — the germ is
  the `(2,9)`-cable of the `(2,5)`-torus knot, `μ=2δ_∞=36`.

### 1.2 Theorem ROW-NF-84: the row is a shear of the (6,4) row

**Theorem A (ROW-NF-84, PROVED-HERE).** *Let `(P,Q)` be an `(8,4)` row member and set
`R := P-Q²`. Then `deg R = 6`, and `(R,Q)` is a `(6,4)` row member: degrees `(6,4)`,
one place at infinity of multiplicity `2` and `δ=7` (germ `A_{14}`, semigroup `⟨2,15⟩`,
`β_1=15`, `Δ=(6,4,3)`, `M_∞=16`), affine singularities exactly three ordinary nodes.
The shear*

```text
   Φ : A² → A² ,   Φ(x,y) = (x - y², y)
```

*is a biregular automorphism of `A²` carrying `D'` onto `D := \mathrm{im}(R,Q)`.
Conversely, for every `(6,4)` row member `(R,Q)` the pair `(R+Q²,Q)` is an `(8,4)` row
member. The two rows are therefore in inverse bijection under `Φ^{±1}`.*

*Proof.* `deg R = 6` is `(1.3)`. `Φ` is polynomial with polynomial inverse
`(x,y)↦(x+y²,y)`, and `Φ∘(P,Q)=(P-Q²,Q)=(R,Q)`, so `Φ(D')=D` and `Φ` restricts to an
isomorphism of pairs `(A²,D') → (A²,D)`. Hence the affine singularities correspond:
`D` has exactly three ordinary nodes and `δ_aff(D)=3`.

`(R,Q)` is a polynomial parametrisation, hence has one place at infinity, and it is
birational onto `D` (it is `Φ` composed with a birational map). So `\deg D̄ = \max(6,4)=6`
and `p_a(D̄)=10`, whence `δ_∞(D̄)=10-3=7`. Repeating `(1.1)` for `(R,Q)` gives
`ord v = 2`, `ord w = 6`: the place is unibranch of multiplicity `2`, so its semigroup is
`⟨2,2δ+1⟩=⟨2,15⟩` and the germ is `A_{14}`, i.e. `β_1=15` and `Δ=(6,4,3)` — the sole
survivor of the `(6,4)` row. Conversely, if `(R,Q)` is a `(6,4)` row member then
`P:=R+Q²` has degree `8`, `P-Q²=R` has degree `6`, so `(1.3)` gives `β̄_1=10` and, with
the three nodes preserved, `Δ=(8,4,6,3)` and `(4;10,19)`. `[]`

**Remark (scope of the equivalence).** Theorem A is *not* the charged "provisional
target-automorphism equivalence" of the ROW-SWEEP witness. ROW-SWEEP exhibited *one*
`(8,4)` curve as `Φ^{-1}` of *one* `(6,4)` curve; Theorem A proves that **every** member
of the `(8,4)` row arises this way, because `deg(P-Q²)=6` *is* the row label `δ_2=6`.
Nothing is inferred by analogy: `(1.2)` is an identity.

### 1.3 Closed form, modulus, and `δ_aff = 3` by the direct method

**Lemma FOLD (PROVED-HERE).** *Let `(R,Q)` be a `(6,4)` row member with `R` monic. Then
there are `r ∈ C[t]` monic of degree `3` and constants `μ,κ` with `R = r² + μQ + κ`.*

*Proof.* The degree semigroup is `Γ=⟨3,4⟩` (§1.1), so some `f∈C[x,y]` has
`\deg_t f(R,Q)=3`; put `r_0:=f(R,Q)`. Then `\deg r_0² = 6 = \deg R`, so after scaling
`r_0` we may assume `\deg(R-r_0²)<6`. Every element of `C[R,Q]` has `t`-degree in `Γ`,
and `Γ∩[0,5]=\{0,3,4\}`. If `\deg(R-r_0²)=4`, subtract `μQ`; the remainder lies in
`Γ∩[0,3]=\{0,3\}`. If it is `3`, it equals `νr_0+(\text{lower})` — replace `r_0` by
`r:=r_0+ν/2`, which changes `r_0²` by `νr_0+ν²/4` and leaves the degree-3 part cancelled.
What remains has `t`-degree in `Γ∩[0,2]=\{0\}`, i.e. is a constant `κ`. `[]`

Applying the `(6,4)`-preserving target shear `x ↦ x-μy-κ` and the charged ROW-NF
coefficient normalisation (`t`-translation kills `t²` in `r`; `y`-translation kills the
constant of `q`) gives the closed form of the row:

```text
   D'_j :  x = ρ·r(t)² + q(t)² ,  y = q(t) ,
           r = t³+bt+c ,   q = t⁴+(2b/3)t²+(4c/3)t ,   c ≠ 0 ,  ρ ∈ C^* ,      (1.5)
```

with modulus `j = b³/c² ∈ C` and three-ordinary-node stratum `j ∉ \{-27/4,-81/16\}`.
The scaling `t↦αt`, `x↦α^{-8}x`, `y↦α^{-4}y` sends `ρ↦ρα^{-2}` and fixes `j`, so `ρ=1`
is a normalisation, at the cost of pinning `(b,c)` within its `j`-orbit. The ROW-SWEEP
witness is `b=c=1`, `ρ=1`, `j=1`.

**`δ_aff = 3` by the direct method.** Let `Q^{[1]}(t,u) := (Q(t)-Q(u))/(t-u)` and
likewise `P^{[1]}`, `R^{[1]}`. From `P=R+Q²`,

```text
   P^{[1]} = R^{[1]} + (Q(t)+Q(u))·Q^{[1]} ,
```

so on `V(Q^{[1]})` one has `P^{[1]} = R^{[1]}`: **the off-diagonal double-point schemes of
`(P,Q)` and `(R,Q)` are the same scheme**, `V(Q^{[1]},R^{[1]})`. This is the divided-
difference form of Theorem A and needs no CAS. For the witness `b=c=1`, in the symmetric
coordinates `σ=t+u`, `π=tu`, that ideal is `(π-σ²-1,\;3σ³+4σ-4)` (charged ROW-SWEEP §2,
re-used, not re-derived): the cubic has nonzero discriminant, its three roots give
pairwise-distinct images and distinct tangent directions, so the scheme is three reduced
unordered pairs. Hence `δ_aff = 3`, realised by three ordinary nodes, and no diagonal or
triple fibre occurs. Together with `p_a=21` this gives `δ_∞=18` and closes `(1.4)`.

### 1.4 The implicit octic and its singularity ledger

`F' := \mathrm{Res}_t(x-P(t),\,y-Q(t))` up to a unit; `C'=V(\bar F')`. A generic line
pulls back to a `t`-polynomial of degree `8` (the `x`-term dominates) and the
parametrisation is generically injective, so `\deg C' = 8` and `C'` is **irreducible and
reduced** (image of an irreducible variety). Ledger:

| locus | type | `mult` | `δ` | local invariants |
|---|---|---:|---:|---|
| `N_1,N_2,N_3` (affine) | ordinary nodes `3A_1` | 2 | `1` each | two smooth branches, distinct tangents |
| `Q_∞=[1:0:0]` | unibranch, `(2,9)`-cable of `(2,5)`-torus knot | 4 | `18` | `Γ_∞=⟨4,10,29⟩`, `(4;10,19)`, conductor `36`, `μ=36` |

Totals: `δ_aff+δ_∞ = 3+18 = 21 = p_a(\deg 8)` ✓. Intersection with the line at infinity:
`C'∩L_∞=\{Q_∞\}`, `I=8`, `L_∞` tangent. `M_∞ = 22 = 3d-3+1`.

The charge asks "three nodes + what at infinity? mult 4 germ, semigroup from `(4;10,19)`".
Answer: the semigroup is `⟨4,10,29⟩` — **not** `⟨4,10,19⟩`; the second characteristic
*exponent* `19` and the second semigroup *generator* `29` differ by
`β̄_2-β_2 = (n_1-1)β̄_1 = 10`. The two must not be identified (FALLACY-v2, flag/place).

---

## 2. The resolvent target: `γ_∞` and `ψ(γ_∞)`

Write `G := π_1(C²-D'_j)`. The hypothetical object is a surjection
`φ : G ↠ S_4` sending every meridian of `D'_j` to a transposition; its **resolvent** is
`ψ := q∘φ` with `q : S_4 ↠ S_4/V ≅ S_3`, which is onto and sends transpositions to
transpositions. The projective step of the `(6,4)` chain needed `ψ(γ_∞)=1`, supplied
there by Theorem INF-TRIVIAL. This section determines what survives at degree 8.

### 2.1 The tangency census at degree 8

Project along `x`. The pencil is the lines `\{x=c\}`, whose base point is `[0:1:0]`;
by §1.4 `C'∩L_∞=\{Q_∞\}=\{[1:0:0\}]`, so `[0:1:0]∉C'` and the pencil is admissible:
in a geometric basis `(g_1,…,g_8)` of a generic fibre,

```text
   γ_∞ = g_8g_7g_6g_5g_4g_3g_2g_1 .                                            (2.1)
```

`D'_j → C_x` is an `8`-section (`P(t)=x` has `8` roots). Its vertical tangencies are the
zeros of

```text
   P' = 2(ρ r r' + q q') ,     deg P' = 7 = d-1 ,                               (2.2)
```

confirming the charge's `V=7`. Riemann–Hurwitz on the normalisation cross-checks this:
`P : P¹→P¹` has degree `8` and `-2 = 8(-2)+\sum(e_i-1)` gives `\sum(e_i-1)=14`, of which
`7` sits at `t=∞` (`P` has a pole of order `8`), leaving `7` in the affine part ✓.

For generic `j` the seven zeros of `P'` are simple with pairwise distinct critical values,
so the braid factorisation has seven simple half-twists plus three node squares:

```text
   e(ρ_∞) = 7·1 + 3·2 = 13 .                                                    (2.3)
```

The same count on the `(6,4)` sextic gives `p'=2rr'` with three zeros of `r` and two of
`r'`, i.e. `5·1+3·2 = 11`, reproducing the charged `e(ρ_∞)=11` — so `(2.3)` is computed
by a method already validated on the adjacent row.

### 2.2 The fold structure: there is none

The `(6,4)` mechanism is not the tangency count but a *collision*: `p=r²` forces the
three zeros of `r` into the **single** fibre `x=0`, where the local braid is
`β_0=σ_1σ_3σ_5`, three simultaneous disjoint half-twists, giving `g_1=g_2`, `g_3=g_4`,
`g_5=g_6` and hence `γ_∞=g_5²g_3²g_1²`. The charge asks whether the analogue
`x=s(t)²` (`\deg s=4`) or `x=u(t)^4` (`\deg u=2`) holds here. It does not.

**Lemma NO-FOLD (PROVED-HERE).** *On the `(8,4)` row in normal form `(1.5)`, `P` is not a
perfect square in `C[t]`. A fortiori `P ≠ u^4`.*

*Proof.* Suppose `P=s²`; `P` is monic, so take `s` monic of degree `4`. Then
`(s-q)(s+q)=P-q²=ρr²` has degree `6` and `\deg(s+q)=4`, so `h:=s-q` has degree exactly
`2` and `h·(h+2q)=ρr²`. On the three-node stratum `\mathrm{disc}(r)=-4b³-27c²=-c²(4j+27)≠0`,
so `r=\prod_{i=1}^3(t-ρ_i)` has distinct roots and `h=\mu h_0` with `h_0` monic dividing `r²`.

*Case `h_0=(t-ρ_i)(t-ρ_j)`, `i≠j`.* Then
`h+2q = ρr²/h = (ρ/\mu)(t-ρ_i)(t-ρ_j)(t-ρ_k)²`, so
`2q=(t-ρ_i)(t-ρ_j)\big[(ρ/\mu)(t-ρ_k)²-\mu\big]`, i.e. `\deg\gcd(q,r)≥2`. But reducing
`t⁴≡-bt²-ct \bmod r` gives `q ≡ \tfrac{t}{3}(c-bt) \bmod r`, and `r(0)=c≠0`, so
`\gcd(q,r)=\gcd(t(c-bt),r)` has degree `≤1`. Contradiction.

*Case `h_0=(t-ρ_1)²`.* Then `h+2q=(ρ/\mu)(t-ρ_2)²(t-ρ_3)²`; comparing leading coefficients
gives `ρ/\mu=2`, and comparing coefficients of `t³` (which vanishes in `2q`) gives
`2·(-2)(ρ_2+ρ_3)=0`, i.e. `ρ_2+ρ_3=0`. Since `r` has no `t²` term, `\sum ρ_i=0`, so
`ρ_1=0`; but `r(0)=c≠0`. Contradiction. `[]`

So the eight points of the fibre `\{x=0\}` are `P(t)=ρr²+q²=0`, which for `ρ=1` factors as
`(q+ir)(q-ir)=0` — **two coprime quartics** (their gcd divides `\gcd(2q,2ir)`, of degree
`≤1`, and a degree-1 common factor would be a common root of `q` and `r`, forcing
`\deg\gcd(q,r)=1` and still leaving eight roots in two groups). Generic fibres carry eight
distinct points, and no identity forces two vertical tangencies into one fibre. The
`(6,4)` degeneration is an artefact of the *sextic* coordinate `p=r²`, which the shear
destroys.

### 2.3 `γ_∞` in the tangency generators

Consequently `(2.1)` does **not** collapse. What is available unconditionally:

1. `D'_j` is irreducible, so `H_1(G)=Z⟨g⟩` and `[γ_∞]=8g`.
2. `\mathrm{sign}∘ψ : G → Z/2` factors through `H_1`, sending `g↦1`; as `8` is even,
   `\mathrm{sign}(ψ(γ_∞))=0`, i.e. `ψ(γ_∞) ∈ A_3 ≅ Z/3`, a well-defined element
   (all meridians of `L_∞` are conjugate and `A_3` is abelian). Likewise `φ(γ_∞) ∈ A_4`.
3. The dichotomy `ψ(γ_∞) ∈ \{e,\text{3-cycle}\}` is **not** resolved by abelian data.

There is, however, an exact transport identity, and it locates the difficulty precisely.
Under `Φ` of Theorem A, the line `\{x=x_*\}` pulls back to the **parabola**
`Λ_{x_*}=\{\tilde x = x_*-y²\}` in the `(6,4)` coordinates, whose projective closure is the
conic `\bar Λ : \tilde XZ+Y²-x_*Z²=0`. On the `A_{14}` branch (`\mathrm{ord}\,v=2`,
`\mathrm{ord}\,w=6`) one has `\mathrm{ord}(w+v²-x_*w²)=\min(6,4)=4`, so

```text
   I(\barΛ, \bar C ; Q_∞) = 4 ,   I(\barΛ, L_∞ ; Q_∞) = 2 ,
   #(\barΛ ∩ D) = 2·6 - 4 = 8  affine points ,                                  (2.4)
```

matching the eight points of the octic's fibre. Hence

```text
   Φ_*(γ_∞^{(8,4)}) = the large circle of the parabola Λ_{x_*} ∖ D ,
                    = ∂ of the disc cut by \barΛ at Q_∞ , class ±(4-2·6)g = ∓8g . (2.5)
```

The homology check `4·[m_C] + 2·[m_L] = 4g - 12g = -8g` (using `[m_L]=-6[m_C]` in
`H_1(P²∖(\bar C∪L_∞))`) confirms `(2.5)`. So `γ_∞^{(8,4)}` and `γ_∞^{(6,4)}` are **genuinely
different elements of the same group `G`** — `8g` and `6g` in `H_1` — and INF-TRIVIAL,
which is the statement `χ(g_5²g_3²g_1²)=1`, says nothing about the former. The charged
non-transfer note is correct on exactly this point.

Computing `(2.5)` as a word would require a Zariski–van Kampen calculus for a **pencil of
conics** (base locus `Q_∞` with multiplicity 4, all members tangent to `L_∞` there), or
equivalently the image of the local link group of the germ `\bar C·L_∞` at `Q_∞` — the
`(2,15)` torus knot together with an unknot of linking number 6. Neither is a desk-scale
line-pencil ZvK, and neither is attempted here.

### 2.4 `ψ(γ_∞)`: the typed answer

```text
OPEN[PI1S4-(8,4)-INF-TRIVIAL]:
  decide ψ(γ_∞^{(8,4)}) ∈ A_3 for an involution-valued ψ on G, equivalently decide
  whether the class ∂(\barΛ ∩ B(Q_∞)) lies in the kernel of every such ψ.
  Missing input: a ZvK (or local-link) calculus for the conic pencil |O(2)| through
  Q_∞ tangent to L_∞, or a braid factorisation of the octic's x-pencil.
  Status: NOT on the critical path (see §4); needed only for a projective-only chain.
```

Two things must be said plainly. First, `ψ(γ_∞^{(8,4)})=1` is *not* obtainable by analogy
from INF-TRIVIAL, and asserting it would be exactly the flag/place identification that
FALLACY-v2 forbids. Second, the question is **vacuous on this row**: Theorem B of §4
proves that no `φ` — hence no `ψ` — exists at all, so there is nothing whose value at
`γ_∞` could be asked. The `OPEN` above is retained only because a successor wanting a
self-contained *projective* argument at degree 8 (for instance for rows `(8,6)` or
`(9,6)`, where no shear reduction is available) will need it.

---

## 3. The projective classification input

### 3.1 What descends, and to what

Suppose `ψ(γ_∞)=1`. Then `ψ` descends to `\barψ : π_1(P²-C') ↠ S_3`; let `X` be the
normalisation of `P²` in the degree-3 field extension attached to the `S_3`-action on
three points. `X` is normal and irreducible (`S_3` is transitive), and `X→P²` is finite
surjective, hence a **normal triple cover** (Sh12 Remark 0.2, quoted in the charged
TORUS-CHECK §4.1). Over a generic point of `C'` the local monodromy is a transposition,
and `\barψ` is defined on `π_1(P²-C')`, so `π` is étale outside `C'`:

```text
   S_π = C' ,  T_π = 0 ,  Δ_π = C' ,   deg Δ_π = 8 .                            (3.1)
```

If instead `ψ(γ_∞)` is a 3-cycle, `π` is totally ramified along `L_∞` and
`Δ_π = C' + 2L_∞`, `\deg Δ_π = 10`. Both branches are treated below.

### 3.2 Literature: triple planes with branch degree 8

Sh12, Introduction (fetched, hashed §0), lists the cases of Problem 0.1 that are solved,
verbatim:

> If `S = 0`, then a normal triple cover `π : X → P²` with branch divisor `∆` must be a
> Galois cover … In the cases where `(deg S, deg T ) = (2, 1), (2, 2), (4, 0)` and `(4, 1)`,
> Tokunaga solved Problem 0.1 … Moreover, Yasumura showed that, if … `(deg S, deg T ) = (4, 1)`,
> then `X` is a cubic surface in `P³` … In the case where `T = 0` and `S` is a sextic curve
> with at most simple singularities, Ishida and Tokunaga showed …

and Sh12 itself settles `\deg Δ_π = 6` in full (Theorem 0.3, Corollary 0.6). The two cases
this lane needs, `(\deg S_π,\deg T_π) = (8,0)` and `(8,1)`, are **not** in that list and are
not covered by Sh12. This is a genuine `SOURCE-OPEN`, not a refutation; the charged
acquisition target CM25 (arXiv:2512.07965, branch curves of degree at most 10) was not
fetched and is not consumed. Tokunaga's dihedral-cover papers reach `\deg Δ_π ≤ 6` only.

The *structure* theory, however, is degree-free, so §3.3 derives the degree-8 normal form
directly rather than citing a classification.

### 3.3 Direct derivation from the Miranda binary-cubic data

Sh12 §1.1 (Miranda's theory), quoted verbatim from the fetched PDF:

> **1.1.3** … `φ(z²) = 2A + az + bw`, `φ(zw) = −B − dz − aw`, `φ(w²) = 2C + cz + dw`, where
> `a, b, c` and `d` are in `O_Y`, and `A = a² − bd`, `B = ad − bc` and `C = d² − ac`. In
> particular, `b ≠ 0` and `c ≠ 0` if `A` is an integral domain.
> **1.1.5** … the branch divisor `∆_π` is locally given by `D := B² − 4AC = 0` … Moreover,
> the line bundle associated to `∆_π` is `(\det T_π)^{−2}`.
> **1.1.6** … If `T_π ≅ L^{−1} ⊕ M^{−1}` … then `a ∈ H⁰(L)`, `b ∈ H⁰(L² ⊗ M^{−1})`,
> `c ∈ H⁰(L^{−1} ⊗ M²)` and `d ∈ H⁰(M)`. Hence `L² ≥ M` and `M² ≥ L`.
> **1.1.7** … `X` is a triple section in the total space of a line bundle `L` over `Y` if and
> only if `T_π ≅ L^{−1} ⊕ L^{−2}`.

**Theorem OCT-TRIPLE (PROVED-HERE).** *Let `π : X → P²` be a normal triple cover with `X`
irreducible and `\deg Δ_π = 8`. Then:*

1. *For a general line `ℓ`, `T_π|_ℓ ≅ O_ℓ(-2) ⊕ O_ℓ(-2)`; equivalently `T_π(2)` has
   generic splitting type `(0,0)`.*
2. *If `T_π` splits, then `T_π ≅ O(-2)⊕O(-2)` and `a,b,c,d ∈ H⁰(O(2))` are **conics**,
   `A,B,C ∈ H⁰(O(4))` are quartics, and `Δ_π = V(B²-4AC)`.*
3. *`X` is **never** a triple section in the total space of a line bundle; there is no
   global depressed-cubic ("Cardano") form and hence no `\bar F = G^3 + H^2` torus
   statement at branch degree 8.*

*Proof.* By 1.1.5, `(\det T_π)^{-2} = O(8)`, so writing `T_π ≅ L^{-1}⊕M^{-1}` (locally, or
on a line) with `L = O(l)`, `M = O(m)` gives `l+m = 4`. 1.1.6's `L² ≥ M` and `M² ≥ L` read
`2l ≥ m` and `2m ≥ l`, so `l ∈ [4/3, 8/3]`, i.e. `l = m = 2`. This proves (2), and then
`a ∈ H⁰(O(2))`, `b ∈ H⁰(O(4-2))`, `c ∈ H⁰(O(-2+4))`, `d ∈ H⁰(O(2))` are all conics, and
`A,B,C` are quartics with `B²-4AC` of degree 8 ✓.

For (1): restrict everything to a general line `ℓ`. By the Zariski hyperplane-section
theorem `π_1(ℓ - Δ_π) ↠ π_1(P² - Δ_π)`, so the monodromy of `X_ℓ → ℓ` is still `S_3`,
hence `X_ℓ` is irreducible and its algebra is a domain; by 1.1.3, `b|_ℓ ≠ 0 ≠ c|_ℓ`, so
the same two inequalities hold on `ℓ` and `T_π|_ℓ ≅ O_ℓ(-2)^{⊕2}`.

For (3): 1.1.7 requires `T_π ≅ L^{-1}⊕L^{-2}`, i.e. `m = 2l`, so `3l = l+m = 4` — not an
integer. `[]`

Part (3) is the structural reason the `(6,4)` route cannot be transplanted. At branch
degree `6` one has `l+m=3`, `l=1`, `m=2=2l`, so `T_π = O(-1)⊕O(-2)`, `b ∈ H⁰(O(0))` is a
nonzero **constant**, the cube can be completed by the unipotent automorphism
`z ↦ z + λw` with `λ ∈ H⁰(ML^{-1}) = H⁰(O(1))`, and one lands on `G_2³+G_3²`. At branch
degree `8`, `6 ∤ 8` and `b` is a conic: **no unit, no depression, no torus form.**

**Corollary OCT-SYZYGY (PROVED-HERE).** *In the split case of Theorem OCT-TRIPLE put*

```text
   f  := -bS³ + 3aS²T - 3dST² + cT³      (coefficients in H⁰(O(2)))
   H_M := AS² - BST + CT²                 (coefficients in H⁰(O(4)))
   K  := (f_S (H_M)_T - f_T (H_M)_S)/3    (coefficients in H⁰(O(6)))
```

*Then `\mathrm{Hess}(f) = 9H_M` and `\mathrm{Disc}(f) = -27(B²-4AC) = -27κ^{-1}\bar F'`
for some `κ ∈ C^*`, and the classical binary-cubic syzygy `J² = 4\mathrm{Hess}³ - 27\mathrm{Disc}·f²`
becomes, for every **constant** `(S_0:T_0) ∈ P¹` (legitimate because `T_π^∨ = O(2)⊗_C C²`
has constant transition functions, so `S,T` are honest coordinates),*

```text
   K_0² = 4H_0³ + κ^{-1}·\bar F'·f_0² ,
   H_0 ∈ H⁰(O(4)) , K_0 ∈ H⁰(O(6)) , f_0 ∈ H⁰(O(2)) .                          (★)
```

Verification of the constants: `\mathrm{Hess}(f)` for `f = αS³+βS²T+γST²+δT³` is
`(β²-3αγ)S²+(βγ-9αδ)ST+(γ²-3βδ)T²`; with `(α,β,γ,δ)=(-b,3a,-3d,c)` this is
`9(a²-bd)S² - 9(ad-bc)ST + 9(d²-ac)T² = 9H_M` ✓. And
`\mathrm{Disc}(f) = β²γ²-4αγ³-4β³δ-27α²δ²+18αβγδ = a²d²-4bd³-4a³c-27b²c²+18abcd`
`= -27(-3a²d²-6abcd+b²c²+4a³c+4bd³)/(-27)`; expanding `B²-4AC = (ad-bc)²-4(a²-bd)(d²-ac)`
gives exactly `-3a²d²-6abcd+b²c²+4a³c+4bd³`, so `\mathrm{Disc}(f) = -27(B²-4AC)` ✓. The
syzygy constants `J² = 4\mathrm{Hess}³-27\mathrm{Disc}\,f²` were fixed by evaluating the
`S^6` and `T^6` coefficients on `f = S³+pST²+qT³` (`\mathrm{Hess} = -3pS²-9qST+p²T²`,
`\mathrm{Disc} = -4p³-27q²`), where both check identically.

**Degree-6 sanity.** There `A ∈ H⁰(O(2))`, `B ∈ H⁰(O(3))`, `C ∈ H⁰(O(4))`, and taking
`(S_0:T_0)=(1:0)` gives `f_0 = -b ∈ C^*`, `H_0 = A`, `K_0 = bB - 2aA ∈ H⁰(O(3))`, so `(★)`
reads `\bar F = κ b^{-2}(K_0² - 4A³)` — **the `(2,3)`-torus identity, recovered exactly.**
So `(★)` is the honest degree-8 analogue of torus type, and the *only* difference is that
`f_0` is a conic rather than a unit.

**Lemma NO-INNER-NODE-8 (PROVED-HERE).** *For all but finitely many `(S_0:T_0)`, `H_0` does
not vanish at any of the three nodes of `C'`.*

*Proof.* First, `(a,b,c,d)` do not all vanish at a node `N`: if they did, `A,B,C` would
vanish to order `≥2` at `N`, so `\bar F' = κ(B²-4AC)` would vanish to order `≥4`, whereas
`\mathrm{ord}_N \bar F' = 2`. Hence `f|_N` is a nonzero binary cubic and `f_0(N)=0` for at
most three values of `(S_0:T_0)`; discard the (at most nine) bad values. Now suppose
`H_0(N)=0`. Restricting `(★)` to `C'` gives `K_0² = 4H_0³` there, so `K_0(N)=0` too. Then
`\mathrm{ord}_N(K_0²-4H_0³) ≥ \min(2,3) = 2` with degree-2 part equal to `(K_0)_1²`
(the square of the linear part of `K_0`), while `\mathrm{ord}_N(κ^{-1}\bar F'f_0²) = 2`
with degree-2 part `κ^{-1}f_0(N)²·(\text{tangent cone of a node})` — two **distinct**
lines, never a perfect square. If `(K_0)_1 = 0` the left order is `≥3 ≠ 2`. `[]`

**The obstruction divisor and how far it goes.** Fix a good `(S_0:T_0)`. On the
normalisation `P¹` of `C'`, `K_0² = 4H_0³` gives `3\,\mathrm{ord}_P H_0 = 2\,\mathrm{ord}_P K_0`
at every point; write `\mathrm{ord}_PH_0 = 2m_P`, `\mathrm{ord}_PK_0 = 3m_P`, `E := \sum m_PP`.
Then `\deg(H_0|) = 4·8 = 32 = 2\deg E`, so `\deg E = 16`, and `\deg(K_0|)=48=3·16` ✓.

* *Nodes are outside `\mathrm{Supp}\,E`* (Lemma NO-INNER-NODE-8).
* *Smooth points of `C'` in `\mathrm{Supp}\,E` lie on `V(f_0)`.* If `H_0(P)=0` at a smooth
  `P ∈ C'` then `K_0(P)=0`, so `\mathrm{ord}_P(K_0²-4H_0³) ≥ 2`, while
  `\mathrm{ord}_P(κ^{-1}\bar F'f_0²) = 1 + 2\,\mathrm{ord}_Pf_0`; hence `f_0(P)=0`.
* *Local order bound.* With `η` a local equation of `C'` at such a `P`,
  `(K_0²-4H_0³)/η|_{η=0} = 2\bar K_0K_{0,η} - 12\bar H_0²H_{0,η}` has order `≥ 3m_P` in the
  branch parameter, and equals a unit times `\bar f_0²`, whose order is even. So
  `\mathrm{ord}^{br}_P(f_0) ≥ ⌈3m_P/2⌉`.
* *Bézout.* `\sum_P \mathrm{ord}^{br}_P(f_0) = 2·8 = 16`, so
  `16 ≥ \tfrac32(16-m_∞)`, i.e. **`m_∞ ≥ 6`**.
* *No total concentration.* `m_∞ = 16` would force `\mathrm{ord}_{Q_∞}H_0 = 32` and
  `\mathrm{ord}_{Q_∞}K_0 = 48`, the Bézout maxima. The order filtration of `H⁰(O(4))`
  (15 distinct values on the branch) has 1-dimensional top step `C·ℓ_∞^4`, and likewise
  `H⁰(O(6))` has top step `C·ℓ_∞^6`. Then `K_0²-4H_0³ = \text{const}·ℓ_∞^{12}` must equal
  `κ^{-1}\bar F'f_0²` with `\bar F'` irreducible of degree 8, forcing the constant to be `0`
  and `f_0 ≡ 0` — possible for at most three `(S_0:T_0)`. So **`m_∞ ≤ 15`**.
* *Semigroup filter.* `2m_∞` and `3m_∞` lie in `Γ_∞ = ⟨4,10,29⟩`. Even `m_∞` always passes;
  odd `m_∞ ∈ \{7,9,11,13,15\}` gives `3m_∞ ∈ \{21,27,33,39,45\}` and `21,27 ∉ Γ_∞`. Hence

```text
   m_∞ ∈ { 6, 8, 10, 11, 12, 13, 14, 15 } .                                     (3.2)
```

At branch degree 6 the same argument closes in one line: `f_0` is a *unit*, so
`\mathrm{Supp}\,E ⊆ \{Q_∞\}` immediately, `m_∞ = \deg E = 6`, `\mathrm{ord}_{Q_∞}K_0 = 18`,
and `K_0` is smooth at `Q_∞` (because `\mathrm{mult}\,\bar F = 2`), contradicting maximal
smooth contact `15`. At degree 8 the conic `f_0` opens a 16-unit reservoir of intersection
outside `Q_∞`, and `(3.2)` is as far as the desk-scale argument reaches.

```text
OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW-84]:
  exclude (or realise) a normal triple cover π: X→P² with X irreducible, Δ_π = C'
  (deg 8, 3A_1 + the (4;10,19) place at Q_∞ with L_∞ tangent, I=8).
  Reduced to: for every binary cubic f with conic coefficients and every good (S_0:T_0),
  exclude the syzygy (★) with m_∞ in the band (3.2); plus the non-split case
  c_2(T_π(2)) > 0. Acquisition: CM25 (arXiv:2512.07965) degree-8 section.
  The ψ(γ_∞) ≠ 1 branch is the same problem at deg Δ_π = 10, where l+m=5 and the same
  inequalities force T_π|_ℓ = O(-2)⊕O(-3) — again with 3 ∤ 5, so again no Cardano form.
```

This `OPEN` is **not** on the critical path: §4 kills the row without it.

---

## 4. Verdict

**Theorem B (ROW-KILL-84, PROVED-HERE at the scope of Theorem ROW-KILL).**
*Let `D'_j` be any `(8,4)` row member — `\deg P = 8`, `\deg Q = 4`, `Δ=(8,4,6,3)`
(equivalently `(4;10,19)`, `(δ_∞,δ_{aff},M_∞)=(18,3,22)`), affine singularities exactly
three ordinary nodes. Then there is **no** surjection*

```text
   φ : π_1(C² - D'_j) ↠ S_4    with every meridian of D'_j a transposition.
```

*Proof.* By Theorem A, `Φ(x,y) = (x-y²,y)` is a biregular automorphism of `A²` with
`Φ(D'_j) = D_j`, where `D_j := \mathrm{im}(P-Q²,\,Q)` is a `(6,4)` row member with exactly
three ordinary nodes — i.e. a member of the three-ordinary-node stratum on which Theorem
ROW-KILL is stated. `Φ` restricts to a biregular isomorphism of complements

```text
   Φ : C² - D'_j  \xrightarrow{\ \sim\ }  C² - D_j ,
```

hence `Φ_* : π_1(C²-D'_j) → π_1(C²-D_j)` is an isomorphism. Because `Φ` is an isomorphism
of *pairs*, it carries smooth points of `D'_j` to smooth points of `D_j` and small
transverse discs to small transverse discs; so `Φ_*` maps the conjugacy class of meridians
of `D'_j` **onto** that of `D_j`. Therefore `φ` exists iff `φ∘Φ_*^{-1} : π_1(C²-D_j) ↠ S_4`
exists with all meridians of `D_j` transpositions. Theorem ROW-KILL (charged TORUS-CHECK
§8) says the latter does not. `[]`

**Row `(8,4)`: KILLED.** The chain, end to end:

```text
 1. (1.2)-(1.3):  Δ=(8,4,6,3) ⟺ deg(P - Q²) = 6.                      [PROVED-HERE §1.1]
 2. Theorem A:    Φ = (x-y², y) carries the whole (8,4) row bijectively
                  onto the whole (6,4) row, nodes and all.            [PROVED-HERE §1.2]
 3. Φ ∈ Aut(A²) ⟹ isomorphism of pairs ⟹ meridian-preserving
                  isomorphism of π_1(C² - ·).                          [PROVED-HERE §4]
 4. Theorem ROW-KILL: no meridian-transposition S_4 quotient on the
                  (6,4) row.                             [CHARGED, TORUS-CHECK §8]
 ⟹ no such quotient on the (8,4) row.
```

Steps 1–3 are unconditional and use no literature. Step 4 is `CHARGED-PROVISIONAL`:
Theorem ROW-KILL is proved in the charged report but inherits ROW-NF's provisional status
and consumes Sh12 Corollary 0.6 as a published theorem. **Theorem B inherits exactly that
scope and nothing weaker or stronger.** No `charge_basis` line is declared; no exit price
is asserted.

**Adjudication of the charged non-transfer note.** TORUS-CHECK's table records row `(8,4)`
as "**not transferred**", citing TRIPLE-COVER-CLOSE §6: the shear does not transport a
fixed `B_6` braid tuple to a fixed `B_8` tuple, and the fold is only a
pullback-surjectivity statement. Every one of those observations is **correct**, and none
of them is used above. What genuinely fails to transport is exactly the projection-
dependent and compactification-dependent data:

| object | `(6,4)` | `(8,4)` | transports? |
|---|---|---|---|
| projective closure | sextic | octic | **no** |
| germ at infinity | `A_{14}`, `⟨2,15⟩`, `I=6` | `(4;10,19)`, `⟨4,10,29⟩`, `I=8` | **no** |
| `M_∞` vs `3d-3` | `16 ≤ 15`? no | `22 ≤ 21`? no | (both miss) |
| braid tuple | `B_6`, `e(ρ_∞)=11` | `B_8`, `e(ρ_∞)=13` | **no** |
| `γ_∞` in `H_1` | `6g` | `8g` | **no** (§2.3) |
| fold at `x=0` | `p=r²`, `σ_1σ_3σ_5` | none (Lemma NO-FOLD) | **no** |
| torus type / `Δ_π` degree | `6` | `8` (no Cardano form) | **no** |
| the pair `(A², D)` up to `\mathrm{Aut}(A²)` | — | — | **yes** |
| `π_1(C²-D)` **with its meridian class** | — | — | **yes** |

The last two lines are the whole kill. TRIPLE-COVER-CLOSE §6 already stated the principle
("if an actual target automorphism carries both the curve and representation, it preserves
the complement"); two caveats blocked its use then, and both are now removed:
*(i)* the `(6,4)` statement available at that time was conditional on global monogenicity,
whereas Theorem ROW-KILL is unconditional at row-geometry scope; *(ii)* the target
equivalence was recorded only for the single ROW-SWEEP witness, whereas Theorem A proves
it for **every** member of the row, because `\deg(P-Q²)=6` *is* the row label `δ_2=6`.
No braid tuple, no fold, and no degree-8 classification is consumed.

**What the direct octic route would still need**, if a successor wants a chain that never
leaves degree 8: `OPEN[PI1S4-(8,4)-INF-TRIVIAL]` (§2.4) **and**
`OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW-84]` (§3.3). Both are typed at their exact missing
lemma. Neither is needed for Theorem B.

---

## 5. Ledger of charged claims, gaps, and successors

### 5.1 What each result consumes

```text
 §1.1  germ (4;10,19), Γ_∞=⟨4,10,29⟩, δ_∞=18, M_∞=22   ← identity (1.2) + genus split. No literature.
 §1.2  Theorem A (row = shear of the (6,4) row)         ← (1.3) + Φ ∈ Aut(A²). No literature.
 §1.3  Lemma FOLD (R = r² + μQ + κ)                     ← Γ = ⟨3,4⟩ only.
 §2.2  Lemma NO-FOLD (P is never a square)              ← normal form (1.5) + disc(r) ≠ 0. No literature.
 §2.3  γ_∞^{(8,4)} = ∂(conic disc), class ±8g           ← (2.4) Bézout at Q_∞.
 §3.3  Theorem OCT-TRIPLE, Corollary OCT-SYZYGY,
       Lemma NO-INNER-NODE-8, band (3.2)                ← Sh12 §1.1.3/1.1.5/1.1.6/1.1.7 (fetched,
                                                          hashed, quoted verbatim) + Zariski–Lefschetz.
 §4    Theorem B (ROW-KILL-84)                          ← Theorem A + Theorem ROW-KILL (charged).
```

**Not consumed anywhere:** any braid-monodromy factorisation, any `B_6`/`B_8` tuple, the
fold/pullback-surjectivity statement, `A'(1)–(4)`, `A'(5)`, the coprime order fork,
`(M-INF)` or `(M-INF-T)`, global monogenicity, the exact class `(7.1)` of
TRIPLE-COVER-CLOSE, `CM25`, `IT09`, or any degree-8 triple-plane classification.

### 5.2 Status table

| claim | typing |
|---|---|
| `Δ=(8,4,6,3) ⟺ \deg(P-Q²)=6`; germ `(4;10,19)`, `Γ_∞=⟨4,10,29⟩`, `δ_∞=18`, `M_∞=22=3d-3+1` | **PROVED-HERE**, unconditional |
| Theorem A: the `(8,4)` row is `Φ^{-1}` of the `(6,4)` row, bijectively | **PROVED-HERE**, unconditional |
| Lemma FOLD, Lemma NO-FOLD, `V=7` tangencies with no forced simultaneity | **PROVED-HERE**, unconditional |
| `γ_∞^{(8,4)} ≠ γ_∞^{(6,4)}` in `G`; INF-TRIVIAL does not redo | **PROVED-HERE**, unconditional |
| `ψ(γ_∞^{(8,4)}) ∈ A_3` | **PROVED-HERE** (abelianisation) |
| `ψ(γ_∞^{(8,4)}) = 1` | **OPEN** — `OPEN[PI1S4-(8,4)-INF-TRIVIAL]`; **vacuous** on this row |
| `T_π ≅ O(-2)^{⊕2}` (split case) / generic splitting `(-2,-2)`; no Cardano form at `\deg Δ_π = 8` | **PROVED-HERE** from Sh12 §1.1 |
| syzygy `(★)`; nodes not inner; `m_∞ ∈ \{6,8,10,\dots,15\}` | **PROVED-HERE** |
| degree-8 triple-plane classification | **SOURCE-OPEN** — `OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW-84]` |
| **Row `(8,4)` killed** | **PROVED-HERE at charged ROW-KILL scope** (Theorem B) |

### 5.3 Corrections to carry

1. The charge's "gcd tower `8,4` gives `g=4`": `4` is `d_1`, not a terminal gcd; the tower
   is `8,4,2,1` with three quotients `2` (§0, §1.1).
2. The semigroup of the infinity place is `⟨4,10,29⟩`, **not** `⟨4,10,19⟩`. The
   characteristic exponent `β_2=19` and the semigroup generator `β̄_2=29` differ by
   `(n_1-1)β̄_1 = 10` and must not be identified (§1.4).
3. The charge's fold hypothesis ("`x=s(t)²` with `\deg s=4` — is there one? — or
   `x=u(t)^4`") is answered **negatively and unconditionally** (Lemma NO-FOLD, §2.2).
   The `(6,4)` collision at `x=0` is an artefact of the sextic coordinate `p=r²` and is
   destroyed by the shear.
4. The charge's "TORUS-CHECK's non-transfer note is binding" is correct for every
   projection- or compactification-dependent object, and **not** for `π_1(C²-D)` with its
   meridian class (§4 table). The note blocked the braid route, not the complement route.
5. `M_∞ = 22` exceeds `3d-3 = 21` by exactly one unit — the row survived (M-INF) by the
   minimum possible margin.

### 5.4 A structural remark for the remaining rows

The reduction of Theorem A exists precisely when a triangular target shear can drop the
degree, i.e. when `\deg Q \mid \deg P` (so that `φ(y)=y^{d/n}` matches the top degree).
Among the residual rows:

```text
   (8,4):  4 | 8   → reduces to (6,4).      [this lane]
   (6,4):  4 ∤ 6   → no shear reduction.    [killed by TORUS-CHECK on its own geometry]
   (8,6):  6 ∤ 8   → no shear reduction.
   (9,6):  6 ∤ 9   → no shear reduction.
```

So rows `(8,6)` and `(9,6)` are **not** reachable by this argument and genuinely need
either their own `§1`-style geometry or the nodal-realisation obstruction already typed
in ROW-SWEEP §§7, 9. Nothing here bears on them, nor on
`OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`, `OPEN[NORI-BC-SELF-TANGENT-COEFF]`, or
`OPEN[PI1S4-D1-DEGREE]`.

### 5.5 Campaign consequence

`OPEN[PI1S4-(8,4)-FIXED-TUPLE]` (ROW-SWEEP §6; coordinator integration §2) is **resolved
NO**, at the scope of Theorem ROW-KILL. Combined with TORUS-CHECK's `(6,4)` kill, the
coordinator's "one target-isomorphism class" residual core is closed in both of its
presentations, and the `N=4` residual cage reduces to the two AM-numerical rows `(8,6)`
and `(9,6)`, whose nodal attainment is itself unproved. If Theorem ROW-NF or Theorem
ROW-KILL is later downgraded, Theorem B falls with it and the live residual becomes
`OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW-84]` together with
`OPEN[PI1S4-(8,4)-INF-TRIVIAL]`; Theorems A, OCT-TRIPLE, OCT-SYZYGY and the lemmas of
§§1–3 are unaffected either way.

### 5.6 Non-claims

No exit price is asserted and no `charge_basis` line is declared. Nothing here upgrades
ROW-NF, Theorem FOLD, or Theorem ROW-KILL from their charged status. Sh12 §1.1 is consumed
as published statements of Miranda's theory; Miranda's paper was not fetched and its
proofs were not re-verified. No CAS was run. No canonical ledger, charged file, or
`jc2-lean` artefact was written or inspected.

<!-- BODY-END -->
