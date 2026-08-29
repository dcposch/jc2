# Opus 5 primary — `TD12-GLOBAL-SOURCE-BRIDGE-S/v1` (nu=17 sibling route)

Lane: Opus 5, equal-standing independent primary researcher (not a review).
Date: 2026-08-29 UTC.
Frozen basis, verified at session start and again immediately before sealing:

```text
92ebe92ad5986a47f01af9ed901260595dfed869
```

Owned object: `TD12-GLOBAL-SOURCE-BRIDGE-S/v1`, the `nu=17` sibling route
only. The `nu=25` B route is a separately owned, separately sourced state and
is not identified with this one anywhere below.

Desk algebra only. No AWS, no web, no heavy local CAS; exact `Fraction`
stdlib checks confined to `/tmp` (reproduced in §10). One repository file
written: this report. No commit, no push, no edit to `jc2-lean` or to any
canonical, source, or code file.

## 0. Custody

Recomputed with `shasum -a 256` before any read (identical recomputation
before sealing):

```text
7af80df724d880a47452de96a731ff1c4e17b8244fdbae8fc76eb1461e7bcc22  xmodel/post1224-next-wave-packet-20260829T1335Z.md
9677e2edf9848e81beac51cc9ed091c13cd934f912bc337b6ab8e25a5da86861  xmodel/roundview-20260829T1335Z-92ebe92a.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
79df783a0ed9e370621e750f4e6564dc9871b53e1481898e77dcdd037711ad1c  xmodel/td12-bchild-v1-minimal-source-packet-audit-r1-erratum-sol56-76c-20260829.md
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
d409510a3df418f402a80cc954f646d35a054e9055783fadc0aaa234bb49b242  ladder/REDUCTION.md
```

The wave packet's own seal recomputes: body `6730` bytes, SHA-256
`7a6ce89e9858572b1a7e1cc3c06217145fb7f0e29f2d727b5959c8b0a0abce65`. The
`ROUNDVIEW` slice was read only as generated context and carries no
conclusion below.

**Exact literal perimeter of use** in `refs/sigray_full.pdf` (thesis page
numbers as printed):

- p. 7–8, Notation 2.1 (almost normalized = lexicographically minimal
  `(deg f, deg g)` in the automorphism class), Lemma 2.1(i)–(iv) with proof;
  p. 9, Notation 2.3, Notation 2.4, Statement 2.1.
- p. 9, first line of the page, literally:
  `By [A Lemma 18.2], for any w ∈ R^2, J(f_w^+, g_w^+) = c ∈ C.`
- p. 10, Statement 3.1 with the Puiseux forms (3) and (4).
- p. 12, Notation 3.9 (`η_F := x^{π(F)}(y − Σ_{j∈Q, j<π(F)} c_j x^{−j})`).
- p. 13, Statement 3.7 (5) with the words `except of finitely many j, p_j ≡ 0`;
  Notation 3.10 (`d_{h,F} := j/κ`, `p_{h,F} := p_j`, `j` the **largest**
  index with `p_j ≢ 0`); Notation 3.11 (`D_{h,F} := κ_F d_{h,F}`);
  Statement 3.8.
- p. 13–14, Proposition 3.1 with its clauses (∗), (∗∗) and proof.
- p. 15, Statement 3.9(i)(ii)(iii) **and its proof**, including
  `Since η_G = x^{1/κ}(η_F − c), we obtain h^G(x,η) = Σ_j x^{j/κ} p_j(...)`.
- p. 15–16, Statements 3.10, 3.11, 3.13; Notations 3.13, 3.14.
- p. 18, Proposition 4.1 with hypothesis (7) and display (8), and the line of
  its proof `From the chain rule by induction we have J(f^F(ξ,η),
  (g−b)(ξ,η)^F) = ξ^{−n/κ}`.
- Notation 3.4, 3.5 (`ν_F := e_{j−1}/e_j`, `κ_F := κ/e_j`), p. 12.

Campaign objects consumed **at their recorded scope with their recorded
repairs**, never re-derived: the sibling reduced cell and T1 solve
(`9a9e948c...`, Grok `PASS`), the sibling exact charge tuple
(`52ffafa2...`), the graded convolution `(E_s)` and its landing order
(Fable `1a602643...` §2.3, as audited `PASS` in `876d1717...` §2), the
type-`(2,3)` ratio `D_g/D_F = 3/2` and `r = 3i/2` (`876d1717...` §2), the
weight/vanishing laws `(W)/(V)` and the extraction law `(C)`
(`1a602643...` §2.2, §2.4), and the promoted formal-envelope disposition
`NO_FORMAL_CASCADE_KILL_IN_WINDOW` (`97ba497f...`).

### 0.1 Two literal errata in the proof of Statement 3.9 (p. 15)

Read with `pdftotext -bbox` glyph geometry, not `-layout` (campaign
stacked-fraction hazard). The display in the proof prints

```text
h^G(x, η) = sum_{j=k}^{l} x^{j/κ} p_j( x^{−κ} η + c ),
```

and the sentence after it prints `a_l x^{(n−l)κ} η^l`. Both superscripts are
single glyph tokens with no `1/`; on the same page the paper does render the
genuine fraction `(n−l)/κ` as a stacked `\frac`. The printed `x^{−κ}` and
`x^{(n−l)κ}` must read `x^{−1/κ}` and `x^{(n−l)/κ}`: this is forced by the
same proof's own line `η_G = x^{1/κ}(η_F − c)` and by the immediately
following `s < (n−l)/κ = d − l/κ`. The sum's upper limit printed `l` must
read `n` (the proof has just set `p_n = p_{h,F}`). Everything below uses the
corrected display; this matches the corrected form already carried by the
reviewed `td8` `(C)`/`(V)` machinery.

Also recorded from glyph geometry, because it is load-bearing for the type
ratio: Notation 2.4(i) prints `α/β = k_f/k_g` (numerator glyphs `k`,`f` at
`y≈621.6`, denominator `k`,`g` at `y≈632.0`), while Lemma 2.1(iv) prints
`k_g/k_f ∉ N*` (numerator `k`,`g` at `y≈316.3`). With `k_f < k_g`
(Lemma 2.1(iii)) this gives `α < β`, so type `(2,3)` means
`k_g/k_f = l_g/l_f = 3/2`, independently confirming the ratio the campaign
already carries.

## 1. Disposition (binary)

```text
BRIDGE_AVAILABLE_AT_MAP_LEVEL / VALUE_LEVEL_STILL_OPEN
```

**The question posed by the packet has a clean answer, and it is not
`PAIRREF_ABSENT`.** A hypothetical normalized counterexample realizing the
named `nu=17` sibling state **does** canonically supply the completion and
every coefficient map. Notation 3.9 supplies the completion; Statement 3.7
supplies the graded coefficient functionals; the (corrected) display inside
the proof of Statement 3.9 supplies the *entire* parent-to-child coefficient
map in closed form, and the first-child vector is literally the child's own
top polynomial. Nothing about these maps is missing, formal, or invented.
What is missing is a finite list of **values**, and this report reduces that
list and pins part of it.

Concretely, the report delivers, unconditionally on any hypothetical
counterexample realizing the cell:

1. **Theorem A** (§3): the whole Sigray vertex descent is one substitution
   `η ↦ c + ξη` on a pair of two-variable polynomials, the Keller identity is
   covariant under it, and `(V)` is exactly a `ξ`-divisibility. The two
   sibling evaluations are two shears of one parent object; this is the exact
   sense in which they are coupled.
2. **Theorem B** (§4): the *floor* of the graded family is a pure Newton
   polygon invariant, computable in closed form and **independent of the
   branch, of the fibre value `a`, and of the entire Puiseux prefix**.
3. **Theorem C** (§5): a floor mirror of Proposition 4.1 that locates the
   distant inhomogeneous row `s*` exactly, from the *other* end, without any
   intermediate jet — packet deliverable 3, in the precise conditional form
   §5.4 states.
4. **Theorem D** (§6): the equality case of Theorem C is completely rigid:
   the floor rows are then *fully determined*, `{c_1, c_2 η}` with
   `c_1 c_2 = 1`. This is a source-provenanced, nonformal, finite jet datum —
   packet deliverable 1/2 at the floor.
5. **Theorem E** (§7): the two sibling evaluations have *identical* floors,
   not merely conjugate ones. This is the genuine simultaneity constraint;
   it also proves why no trace/norm form is available, so none is invented.
6. **Theorem F** (§8): the first genuinely nonformal invariant of the cell,
   pinned: `deg_y f ≥ 68 i`, `deg_x f ≥ 68 i`, `deg f = k_f + l_f ≥ 136 i`,
   `deg g ≥ 204 i`. Fable's charged report lists `deg_y f`, `deg_y g` as
   *unpinned* twice (§3.4(3), §9(a)); this repairs that entry from below.

**Not delivered:** a value of any `v_{S_±,k}` with `k ≥ 1`; an occurrence
proof; a `PairRef`; a kill. The exact fork that blocks further progress is
isolated in §9 as a single named missing source lemma, `FLOOR-COORD`.

## 2. The sibling state, fixed notation

Consumed, not re-derived. `F ∈ V_{1,a} ∩ T_a^+ ∩ T_{y,a}`, `u := π(F)`, `κ`
suitable, `ν_F = 17`, `κ_F` as in Notation 3.5, `Q := κ/κ_F`,
`t := η^{17}`, and

```text
cell (ν,dp,dq,E,k̄,X,l,k,Sm,ε,lex) = (17,68,52,36,13,17,2,2,2,0,0),
p = (t−A)^2 (t−B_+)(t−B_−),  B_± = (9 ± 3√−1) A/8,  A ∈ C*,
p_{f,F} = P_0 = λ_f p^i,  deg_η p_{f,F} = 68 i,  D_F = 17 i,  k̄_F = 13,
type (2,3)  ⟹  D_g/D_F = 3/2,  D_g = 17 r,  r = 3i/2,  i even,
G_0 = c_g p^r,   e_k ≡ 13k (mod 17),   window depth ν_F − 1 = 16,
s* = D_F + D_g − k̄_F = 17i + 51i/2 − 13 = (85i − 26)/2,
c_±^{17} = B_±,   v_{S_±,k} = [(η − c_±)^{i−k}] P_k(η).
```

Two consequences of the printed notations that are used repeatedly and are
worth recording because they pin `u`:

```text
ν_F | κ_F   (Notation 3.4/3.5: κ_F/ν_F = κ/e_{j−1} ∈ N),  so 17 | κ_F;
k̄_F = κ_F(1 − u) = 13   ⟹   u = 1 − 13/κ_F ∈ [4/17, 1),  κ_F ∈ 17N.
```

So `u` is a rational strictly between `0` and `1`, at least `4/17`, and
`κ_F u = κ_F − 13 ∈ N`. In particular `κ_F σ ∈ Z` for every value
`σ = J − u m` with `(J,m) ∈ Z^2`, which is what makes §4 land on the
`κ_F`-lattice of `(E_s)`.

## 3. Theorem A — the canonical bridge is a shear scheme

Write `ξ := x^{−1/κ}` and, for a polynomial `h`, let

```text
h^F(ξ,η) := sum_{j} ξ^{−j} p_{h,j}(η)      (Statement 3.7 (5), rewritten),
```

a **Laurent polynomial in `ξ` with polynomial coefficients in `η`**: finite
in both directions, because Statement 3.7 says `except of finitely many j,
p_j ≡ 0`.

> **Theorem A.** Let `F ∈ T_{y,a}` with `κπ(F) ∈ N` and let `c ∈ C` be such
> that `G := F ∗ c` is defined (Notation 3.8). Then for every polynomial `h`
>
> ```text
> (A1)   h^G(ξ, η) = h^F(ξ, c + ξ η)        (exactly, as Laurent polynomials),
> (A2)   ξ^{l} | h^F(ξ, c + ξη)   with l := mult(p_{h,F}, c),
>        and this divisibility is equivalent to the vanishing ladder
>        ord_c(P_k) ≥ l − k for all k ≥ 0, where P_k := p_{h,n−k}, n := κ d_{h,F},
> (A3)   p_{h,G}(η) = [ξ^{l}] h^F(ξ, c + ξη) · ξ^{n}
>                   = sum_{k=0}^{l} v_{c,k} η^{l−k},   v_{c,k} := [(η−c)^{l−k}] P_k,
> (A4)   the Keller identity is covariant:  J_{ξ,η}(f^G, g^G)(ξ,η)
>        = ξ · [J_{ξ,η}(f^F, g^F)](ξ, c + ξη),   i.e.  u ↦ u + 1/κ.
> ```

*Proof.* (A1) is the corrected display in the proof of Statement 3.9, p. 15,
rewritten in `ξ`. (A2): expanding, `[ξ^s η^m] h^F(ξ,c+ξη) = P_{s−m}^{(m)}(c)/m!`;
Statement 3.9(iii) says `d_{h,G} = d_{h,F} − l/κ`, i.e. the top `ξ`-index of
`h^G` is `−n + l`, i.e. all coefficients with `s < l` vanish, i.e.
`P_k^{(m)}(c) = 0` for every `m ≤ l − k − 1`. (A3) is then the `ξ^l`
coefficient, and Statement 3.9(i) `deg p_{h,G} = l` confirms the degree.
(A4) is the chain rule for the substitution `(ξ,η) ↦ (ξ, c+ξη)`, whose
Jacobian determinant is `ξ`. ∎

Three consequences that settle the packet's framing question.

- **The coefficient maps are not missing.** `(A3)` says the "first-child
  coefficient vector" is not an auxiliary construct at all: it **is**
  `p_{f,F∗c}`, the child's own top polynomial, in the sense of Notation 3.10.
  Every entry is a printed functional of the parent family.
- **`(V)` is a genuine source input, not a formal identity.** `(A2)` is an
  equivalence with Statement 3.9(iii), which requires `F ∗ c` to be a real
  tree vertex. A desk control confirms this is not vacuous: for
  `h = x^3(y−1)^2(y−2)(y+3) + (lower)` and `c = 1` a double root of the top
  row, `(A2)` **fails** (§10, TEST 3b) — the divisibility stops at `ξ^1`.
  For the genuine double branch `f = x^2(y−1)^2 − 1` (branches
  `y = 1 ± 1/x`) it holds exactly, together with 3.9(i)(ii)(iii) (§10, TEST 3c).
  So no descendant may assume `(V)` for a root that is not a tree direction.
- **The sibling coupling has a normal form.** The two sibling children are
  `f^{G_±}(ξ,η) = f^F(ξ, c_± + ξη)`, two shears of *one* `f^F`. This is the
  exact content of the R1 erratum's sentence "the `+` and `−` vectors are
  evaluations of the same `P_k` family"; Theorem E below extracts from it a
  constraint that the top-side data cannot see.

## 4. Theorem B — the floor of the graded family is a Newton polygon invariant

For `0 ≠ h ∈ C[x,y]` and `u ∈ Q_{≥0}` define the support function and the
minimal form in direction `(1,−u)`:

```text
σ_h(u) := min{ J − u m : (J,m) ∈ supp(h) },
h_u^↓   := sum_{ (J,m) ∈ supp(h),  J − u m = σ_h(u) }  h_{Jm} x^J y^m .
```

> **Theorem B.** Let `F ∈ T_{y,a}`, `u = π(F)`, `κ` suitable with `κu ∈ N`,
> and let `h^F(x,η) = Σ_j x^{j/κ} p_{h,j}(η)` be its Statement 3.7 expansion.
> Then the **least** `x`-exponent occurring in `h^F` is exactly `σ_h(u)`, and
> the corresponding coefficient polynomial is
>
> ```text
> p_{h,min}(η) = h_u^↓(1, η) = sum_{J − u m = σ_h(u)} h_{Jm} η^m  ≠ 0,
> equivalently   h_u^↓(x, x^{−u} η) = x^{σ_h(u)} p_{h,min}(η).
> ```
>
> In particular `p_{h,min}` **does not depend on the branch `P`, on the fibre
> value `a`, or on any coefficient of the Puiseux prefix `φ`** — only on
> `supp(h)` and on the single rational number `u = π(F)`.

*Proof.* Notation 3.9 gives `y = φ(x) + η x^{−u}` with
`φ(x) = Σ_{0 ≤ j < u} c_j x^{−j}` (form (3) has `j ≥ 0`; the sum in Notation
3.9 is over `j < π(F)`), so every exponent of `φ` lies in `(−u, 0]`. A
monomial `x^J y^m` of `h` contributes
`x^J(φ + η x^{−u})^m = Σ_{m' ≤ m} \binom{m}{m'} x^{J − u m'} φ^{m−m'} η^{m'}`,
whose exponents are `J − u m' − Σ_{i=1}^{m−m'} j_i` with `j_i ∈ [0, u)`.
For `m' < m` this exceeds `J − u m` by
`u(m−m') − Σ j_i ≥ (m−m')(u − max j_i) > 0`. Hence the least exponent
contributed is `J − u m`, attained only by the pure `η^m` term with
coefficient `h_{Jm}`. Summing over `supp(h)`, the least exponent is
`σ_h(u)`, and the coefficient at that exponent is `Σ_{J−um=σ_h(u)} h_{Jm} η^m`,
which is nonzero because distinct support points on the minimal face have
distinct `m` (they lie on a line of slope `1/u ≠ 0` in the `(J,m)`-plane, so
`m` determines `J`). ∎

Machine-checked exactly on three independent `(h, u, κ, φ)` tuples with
`u ∈ {3/2, 5/3, 7/4}` and nontrivial prefixes (§10, TEST 1).

**Remark (sharpness under constant shifts).** `σ_{h−a}(u) = min(σ_h(u), 0)`
for `a ≠ 0`. Proposition 4.1 carries the matching hypothesis (7) and the
`b`-shift on the `g` side at the *top*; at the floor the sharpest reading is
obtained with the unshifted `f, g` and is the one used below. Using `f − a`
instead only inserts extra rows on which the floor equation is vacuous
(`P` constant and `σ = 0` kill both terms), so nothing is lost.

## 5. Theorem C — the floor form of Proposition 4.1, and the exact location of `s*`

Proposition 4.1 (p. 18) is the **ceiling** dichotomy:
`d_F + d_{g−b,F} ≥ 1 − u`, with `J(f_F^+,(g−b)_F^+) = ξ^{−u}` in the equality
case and `= 0` otherwise. In `κ_F`-graded language it says `s* ≥ 0` and that
the inhomogeneous Keller row is the top row exactly when `s* = 0`. The
following is its exact mirror, and it is *computable*.

> **Theorem C.** Let `(f,g)` be any Jacobian pair (`J(f,g) = 1`), `F ∈ T_{y,a}`,
> `u = π(F) ∈ Q_{≥0}`. Put `Γ(u) := (1−u) − σ_f(u) − σ_g(u)`. Then
>
> ```text
> (C1)  σ_f(u) + σ_g(u) ≤ 1 − u,   i.e.  Γ(u) ≥ 0;
> (C2)  J_{x,y}( f_u^↓ , g_u^↓ ) = 1   if Γ(u) = 0,
>                                = 0   if Γ(u) > 0;
> (C3)  in the graded system (E_s) the floor row sits at
>          K_P + K_G = ( D_F − κ_F σ_f(u) ) + ( D_g − κ_F σ_g(u) )
>                    = s* + κ_F Γ(u),
>       so the distant inhomogeneous row s* is exactly κ_F Γ(u) rows above the
>       floor and s* rows below the ceiling, and the two ends coincide with the
>       Keller row exactly when Γ(u) = 0 resp. s* = 0;
> (C4)  if Γ(u) > 0 and σ_f(u) σ_g(u) ≠ 0 the floor row is homogeneous and
>          ( p_{g,min} )^{σ_f(u)} = c ( p_{f,min} )^{σ_g(u)},  c ∈ C*,
>       equivalently  ( g_u^↓ )^{σ_f(u)} = c ( f_u^↓ )^{σ_g(u)}:
>       the two minimal faces are homothetic with ratio ρ(u) := σ_g(u)/σ_f(u);
> (C5)  Γ is a nonnegative, convex, piecewise-linear function of u with
>       Γ(0) = 1 − ord_x f − ord_x g ∈ {0,1} and Γ(u) → ∞;
>       hence {Γ = 0} is a closed interval containing 0 whenever it is nonempty.
> ```

*Proof.* The charged graded convolution (Fable §2.3, audited `PASS`) reads,
at `κ`-index `m`,

```text
sum_{j+k=m} ( j p_{f,j} p_{g,k}' − k p_{f,j}' p_{g,k} ) = κ · [ m = κ(1−u) ],
```

and is an exact rewriting of the printed proof line of Proposition 4.1,
`J_{x,η}(f^F, g^F) = x^{−u}`. By Theorem B the least index on the left is
`m_f + m_g` with `m_h := κ σ_h(u)`. If `m_f + m_g > κ(1−u)` the left side
vanishes identically at index `κ(1−u)` while the right side is `κ ≠ 0`; this
proves (C1). The row at the least index is

```text
κ ( σ_f p_{f,min} p_{g,min}' − σ_g p_{f,min}' p_{g,min} ) = κ · [ Γ(u) = 0 ].
```

Substituting `y = x^{−u} η` in Theorem B's identity and using
`dx ∧ dy = x^{−u} dx ∧ dη` gives

```text
J_{x,y}( f_u^↓ , g_u^↓ ) = x^{ (1−u) − σ_f − σ_g − ... }
                          · ( σ_f p_{f,min} p_{g,min}' − σ_g p_{f,min}' p_{g,min} ) · x^{σ_f+σ_g+u−1},
```

i.e. the displayed row is `J(f_u^↓, g_u^↓)` up to the factor `κ` and the
monomial `x^{1−u−σ_f−σ_g}`; this is (C2). (C3) is arithmetic:
`D_F + D_g − κ_F(σ_f+σ_g) = D_F + D_g − k̄_F + κ_F Γ = s* + κ_F Γ`. (C4): from
`σ_f P G' = σ_g P' G` one gets `σ_f (log G)' = σ_g (log P)'`, hence
`G^{σ_f} = c P^{σ_g}` after clearing denominators; transporting through
Theorem B's identity gives the face form. (C5): each `σ_h` is a minimum of
finitely many affine functions of `u`, hence concave piecewise-linear, so
`Γ` is convex piecewise-linear; `Γ ≥ 0` is (C1); `σ_h(0) = ord_x h` and
`ord_x f + ord_x g ≤ 1` because `J = f_x g_y − f_y g_x` has
`ord_x ≥ ord_x f + ord_x g − 1` and equals `1`; for large `u`,
`σ_f(u) = J_f^* − u l_f` and `σ_g(u) = J_g^* − u l_g` so
`Γ(u) = 1 − J_f^* − J_g^* + u(l_f + l_g − 1) → ∞` since `l_f, l_g ≥ 1`
(Lemma 2.1(i)). ∎

(C1) is the exact analogue of Sigray's own quotation on p. 9,
`By [A Lemma 18.2], for any w ∈ R^2, J(f_w^+, g_w^+) = c ∈ C`, applied to
`w = (−1, u)`; the proof above does **not** use Abhyankar, so no uncited
hypothesis is imported. Both (C1)–(C4) were machine-checked exactly on seven
genuine Jacobian pairs at eight values of `u` each (§10, TESTS 2 and 6).

### 5.4 What this does for the packet's deliverable 3

The packet asks for "a nonzero compatibility at `s* = D_F + D_g − k̄_F` that
cannot be absorbed by the `J = 0` binomial response". (C3) gives its exact
address, and (C2) gives the compatibility **whenever `Γ(u) = 0`**: the row at
`s*` is then the floor row and equals `J(f_u^↓, g_u^↓) = 1`, a finite,
explicit, jet-free identity on the two Newton polygon faces. It is not
absorbable by the reviewed own-order response of Theorem B of `1a602643...`:
that response `G_s = c_g p^{r−i}((r/i) P_s + Z)` is a *homogeneous* solution
operator and cannot produce the nonzero constant `κ_F`. The obstruction to
cashing this in unconditionally is precisely `Γ(u) = 0` versus `> 0`, which
§6 turns into an exact, finite fork and §9 turns into one named lemma.

## 6. Theorem D — floor rigidity: the equality case is completely determined

> **Theorem D.** Let `(f,g)` be a Jacobian pair and `u ∈ Q_{>0}`. Then
> `Γ(u) = 0` **iff**, up to interchanging the roles of `f` and `g`,
>
> ```text
> f_u^↓ = c_1 x ,   g_u^↓ = c_2 y ,   c_1 c_2 = 1,
> equivalently   σ_f(u) = 1,  p_{f,min} = c_1  (a nonzero constant),
>                σ_g(u) = −u, p_{g,min} = c_2 η .
> ```
>
> Consequently, if `Γ(u) = 0` for some `u > 0` then `x | f` (resp. `x | g` in
> the swapped case), `Γ(0) = 0`, and `{Γ = 0} = [0, u_max]` with
> `u_max ≤ min( (k_f − 1)/l_f , k_g/(l_g − 1) )`.
> Contrapositive: **if `x ∤ f` and `x ∤ g` then `Γ(u) > 0` for every `u ≥ 0`,
> at every vertex of every tree**, and the floor row is always the homothety
> (C4).

*Proof.* Write `u = q/p` in lowest terms, `p, q ≥ 1`. The minimal face of a
support in direction `(1,−u)` is a set of lattice points in arithmetic
progression with step `(q,p)`, so

```text
f_u^↓ = x^A y^B Φ(τ),   g_u^↓ = x^C y^D Ψ(τ),   τ := x^q y^p,
A,B,C,D ∈ N,  Φ(0) ≠ 0 ≠ Ψ(0).
```

A direct expansion (verified symbolically on 40 random parameter tuples,
§10 TEST 4b) gives

```text
J(f_u^↓, g_u^↓) = x^{A+C−1} y^{B+D−1}
   [ (AD − BC) ΦΨ + (Ap − Bq) τ Φ Ψ' + (qD − pC) τ Φ' Ψ ].
```

By (C2), `Γ(u) = 0` forces this to equal `1`. The bracket is a polynomial in
`τ = x^q y^p`, so the whole right side is a sum of monomials
`x^{A+C−1+qn} y^{B+D−1+pn}`. Exactly one of them may survive, with exponents
`(0,0)`. If the surviving `n` is `0`, then `A + C = 1`, `B + D = 1`, and the
`τ^0` coefficient `(AD−BC)Φ(0)Ψ(0)` must be nonzero, so `AD ≠ BC`. With
`A,C ≥ 0` and `A + C = 1` we get `{A,C} = {0,1}`, likewise `{B,D} = {0,1}`,
and `AD − BC ≠ 0` leaves exactly `(A,B,C,D) ∈ {(1,0,0,1),(0,1,1,0)}`. In the
first case the bracket is `ΦΨ + pτΦΨ' + qτΦ'Ψ`, whose coefficient of
`τ^{a+b}` (`a = deg Φ`, `b = deg Ψ`) is `(1 + pb + qa) φ_a ψ_b`; since
`p,q ≥ 1` and `a,b ≥ 0`, the factor `1 + pb + qa` is **strictly positive**,
so `a + b = 0`, i.e. `Φ, Ψ` are constants. In the second case the analogous
factor is `−(1 + qb + pa) < 0`, same conclusion. If instead the surviving `n`
were `≥ 1`, then `qn = 1 − A − C ≤ 1` and `pn = 1 − B − D ≤ 1` force
`p = q = n = 1` and `A = B = C = D = 0`; but then `AD−BC = Ap−Bq = qD−pC = 0`
and the bracket vanishes identically, contradiction. Hence `Φ, Ψ` constant
and `{f_u^↓, g_u^↓} = {c_1 x, c_2 y}` with `J(c_1x, c_2y) = c_1c_2 = 1` (resp.
`−c_1c_2 = 1` after the swap).

Conversely `J(c_1x,c_2y) = 1 ≠ 0`, so (C2) gives `Γ(u) = 0`.

For the consequences: `f_u^↓ = c_1 x` means `σ_f(u) = 1` with the minimal
face the single point `(1,0)`, hence `J − u m ≥ 1` for every `(J,m) ∈ supp f`;
taking `m = 0` shows `(0,m) ∉ supp f` for all `m`, i.e. `x | f`. Then
`σ_f(0) = ord_x f = 1` and `σ_g(0) = ord_x g = 0` by (C1) at `u = 0`, so
`Γ(0) = 0`; convexity of `Γ` (C5) then makes `{Γ = 0}` an interval containing
`0`. The bound on `u_max` is `J − u m > 1` at `(k_f,l_f) ∈ supp f`
(Lemma 2.1(i)) and `J − um > −u` at `(k_g,l_g) ∈ supp g`. ∎

Exhaustive small search over `(p,q) ∈ {(1,1),(1,2),(2,1),(2,3),(3,2),(4,17),
(13,17)}` and `deg Φ, deg Ψ ≤ 3` confirms no admissible tuple lets the top
bracket coefficient vanish (§10, TEST 4c).

**This is the packet's deliverable 1/2 at the floor.** In the equality case
the floor rows of *both* sides are pinned to the last constant:
`p_{f,min} = c_1`, `p_{g,min} = c_2 η`, `c_1 c_2 = 1`. They are
source-provenanced (Theorem B reads them off `supp f`, `supp g`), finite, and
not formal jets. In the other case (C4) pins the floor pair up to one scalar
and one exponent `ρ(u) = σ_g(u)/σ_f(u)` — also a global-support invariant.

## 7. Theorem E — the two sibling evaluations have identical floors

> **Theorem E.** Let `F` be the sibling vertex and `c_+, c_-` the two
> `nu=17` directions (`c_±^{17} = B_±`). Then for `h ∈ {f, g}`:
>
> ```text
> σ_h at F∗c_+  =  σ_h at F∗c_-  =  σ_h( u + 1/κ ),
> p_{h,min}(F∗c_+) = p_{h,min}(F∗c_-) = h_{u+1/κ}^↓(1, ·)   (identical polynomials),
> Γ(F∗c_+) = Γ(F∗c_-),   ρ(F∗c_+) = ρ(F∗c_-),
> ```
>
> and the same identities hold at every common depth `ℓ ≤ 16` of the two
> sibling towers, and equally for the `A`-direction child. In particular the
> two sibling towers are in the **same** case of Theorem C/D at every level,
> and the numbers of graded rows separating `s*` from the floor agree exactly.

*Proof.* Immediate from Theorem B: the floor data depend only on `supp(h)`
and on `π(·)`, and `π(F∗c) = π(F) + 1/κ` for every admissible `c`. Directly
from Theorem A: `[ξ^{max}] h^F(ξ, c + ξη) = Σ_{a+b = max} (coeff)_{a,b} η^b`
carries **no `c`** — the top `ξ`-degree part of a shear is `c`-free. ∎

Verified exactly: three distinct children of one parent chart share floor
index and floor polynomial, which further equals the `(1,−u')`-minimal form
(§10, TESTS 3b/3d).

**Consequences for the brief's explicit search directions.**

- *Symmetric / trace / norm constraints.* There is a genuine simultaneity
  law coupling the two evaluations, and Theorem E is it. It is an
  **equality**, not a symmetric function: the two floors coincide on the
  nose. Therefore no norm or trace form arises there, and this report
  constructs none.
- *Descent from the Kummer field.* The floor data lie in the field generated
  by `supp(f), supp(g)` and are fixed by every automorphism of
  `Q(A)(√−1, B_±^{1/17}, μ_{17})` over the coefficient field of `f, g`,
  because they do not involve `A`, `B_±`, `c_±`, or `μ_{17}` at all. So the
  *floor* descends unconditionally, while the *top* does not: the reviewed
  level-1 exhibit of `1a602643...` §8.4, with `v_{S_+,1} ≠ 0 = v_{S_-,1}`,
  remains admissible. Galois conjugacy of the two vectors is therefore still
  **not** forced, and is not assumed anywhere here; Theorem E explains why
  the coupling that does exist cannot produce it.
- *Approximate-root tower.* Theorems B–E use none of Proposition 4.2; the
  filed Proposition-4.2 trust boundary is therefore not on the critical path
  of any statement in this report.
- *Universal coefficient scheme of exact polynomial pairs.* Theorem A is
  that scheme in normal form: a hypothetical pair is carried by
  `(f^F, g^F) ∈ C[ξ^{±1}, η]^2` with `J_{ξ,η}(f^F,g^F) = −κ ξ^{κ u − κ − 1}`,
  and every vertex of `T_a` is one word in the shears `η ↦ c + ξη`. The
  coefficient variables are the coefficients of `f, g` themselves; the route
  incidence conditions are `(A2)` at each step. No formal independent jet is
  introduced, and none is called a source coefficient.

## 8. Theorem F — the first nonformal invariant, pinned

> **Theorem F.** Suppose a normalized counterexample `(f,g)` (Notation 2.3)
> has a vertex `F ∈ T_{y,a}` realizing the sibling cell with full index `i ≥ 1`.
> Then, in the Lemma 2.1 coordinates,
>
> ```text
> l_f = deg_y f ≥ 68 i,        k_f = deg_x f ≥ l_f ≥ 68 i,
> deg f = k_f + l_f ≥ 136 i,
> and if the counterexample is of type (2,3):
> l_g = deg_y g ≥ 102 i,       k_g = deg_x g ≥ 102 i,     deg g = (3/2) deg f ≥ 204 i.
> ```
>
> If instead `F ∈ T_{x,a}`, the transposed argument gives `k_f ≥ 68 i` and
> `deg f ≥ 68 i`, `deg g ≥ 102 i`.

*Proof.* `deg_η f^F = deg_y f`: substituting `y = φ(x) + η x^{−u}` in
`f = Σ_{β ≤ l_f} f_β(x) y^β` produces the `η^{l_f}` coefficient
`f_{l_f}(x) x^{−l_f u} ≠ 0` and nothing higher. Every `p_{f,j}` is a
coefficient of a power of `x` in `f^F`, hence `deg_η p_{f,j} ≤ deg_y f`. In
particular `deg_y f ≥ deg_η p_{f,F} = deg_η(λ_f p^i) = 68 i`, the reduced
degree `dp = 68` being the printed cell datum (`9a9e948c...` §2,
`deg p = 17(2+1+1) = 68`). Lemma 2.1(iii) prints `l_f ≤ k_f`, and Lemma
2.1's proof prints `f^+_{(1,1)}(x,y) = x^{k_f} y^{l_f}`, a single monomial,
so `deg f = k_f + l_f`. For the `g` side, Lemma 2.1(ii) prints
`k_g/k_f = l_g/l_f`, so `deg g/deg f = k_g/k_f`, which is `3/2` for type
`(2,3)` by Notation 2.4 as resolved in §0.1. ∎

Three remarks.

1. **This repairs a declared gap.** The charged Fable report lists the caps
   `(deg_y f, deg_y g)` as *unpinned* — "the degree caps `(deg_y f, deg_y g)`
   are unpinned (§3.4)", and again in the `TD12-BCHILD/v1` input list §9(a).
   Theorem F supplies the missing side of that pin (a floor, not a ceiling):
   `deg_y f ≥ 68 i` and `deg_y g ≥ 102 i`. It does not supply a ceiling, so
   the per-order dimension counts of `1a602643...` §8.3 stay quarantined
   exactly as `876d1717...` §5 left them.
2. **Only the `deg f ≥ 136 i` half needs the type.** The bounds
   `l_f ≥ 68i`, `k_f ≥ 68i`, `deg f ≥ 136i` use *no* type hypothesis and no
   `r = 3i/2`; only the `g`-side numbers do.
3. **Comparison, not consumption.** `ladder/REDUCTION.md` records GGV22's
   dichotomy "`max(deg P, deg Q) ≥ 125` or degree pair `(72,108)` or its
   transpose", and records GGV22 as a preprint that is "**not** load-bearing
   in the sheet/book reduction and cannot be used globally". Theorem F is
   independent of it and strictly stronger for this cell, and it is *not*
   consistent with `(72,108)`: `deg f ≥ 136 > 72`. Since GGV22 is not
   load-bearing here, this is recorded as an observation, **not** as an
   exclusion of anything, and no branch of the reduction is touched.

Numerically, under the reviewed direct-entry rider `i = 6n` the floor reads
`deg f ≥ 816 n`, `deg g ≥ 1224 n`; under the promoted formal-window
transparency rider `i ≥ 12` it reads `deg f ≥ 1632`, `deg g ≥ 2448`. Both
riders are consumed at their own recorded scopes and neither is asserted
here.

### 8.1 A second, elementary global relation (recorded, not claimed novel)

Comparing the coefficient of `y^{l_f + l_g − 1}` on both sides of
`J(f,g) = 1` (which is legitimate whenever `l_f + l_g ≥ 2`) gives
`l_g f'_{l_f} g_{l_g} = l_f f_{l_f} g'_{l_g}`, hence

```text
f_{l_f}^{\,l_g} = c · g_{l_g}^{\,l_f},   c ∈ C*,
so for type (2,3):  f_{l_f} = c_1 W^2 ,  g_{l_g} = c_2 W^3  for one W ∈ C[x].
```

This is the `u → ∞` end of the same family of relations as (C4). It is
elementary and probably folklore; it is recorded because it is the only
`x`-side datum of the floor family that is available with no hypotheses at
all. Verified exactly (§10, TEST 7).

## 9. Exact blockers, and the first missing source lemma

The bridge is built to the map level and, at the floor, to the value level in
one of two cases. Exactly one lemma separates the two cases.

```text
MISSING SOURCE LEMMA  FLOOR-COORD.
  For a normalized counterexample (Notation 2.3), is  ord_x f = ord_x g = 0 ?
  Equivalently: is  Γ(0) = 1 ?   Equivalently (Theorem D): is  Γ(u) > 0
  for every u ≥ 0, at every vertex of every T_a ?
```

Status on the frozen basis: **not derivable**. Lemma 2.1 places `N_f` inside
the rectangle `[0,k_f] × [0,l_f]` and prints `(k_f,l_f) ∈ N_f`, but never
asserts `(0,m) ∈ N_f`. `x | f` is not obviously absurd: writing `f = x f̃`,
the identity `J(f,g) = 1` gives at `x = 0` that `f̃(0,y) g_y(0,y) ≡ 1`, so
both are nonzero constants and `g(0,y)` is affine in `y` — consistent, and
consistent with smoothness of the fibre `f = 0` (the two components
`{x = 0}` and `{f̃ = 0}` are then disjoint). Nothing in the charged perimeter
decides it. What is decided: if `FLOOR-COORD` holds, Theorem D forces case
(C4) everywhere, so the floor row is *never* the Keller row and §5.4's
compatibility is never cashable at any vertex; if it fails, Theorem D pins
the floor pair completely and the Keller row is the floor row on the whole
interval `[0, u_max]`.

Other exact blockers, stated so no descendant re-derives them:

- **B1. Ceiling caps.** Theorem F is a floor. `deg_η P_k ≤ deg_y f` is the
  only printed ceiling, and `deg_y f` has no upper bound on the basis; so
  the `1a602643...` §8.3 dimension counts and the "exactly one infinity
  cokernel" claim stay quarantined (`876d1717...` §5). Nothing here
  unquarantines them.
- **B2. `u` is pinned only to `1 − 13/κ_F` with `17 | κ_F`.** `κ_F` itself is
  not pinned, so `u` ranges over `{4/17, 21/34, 38/51, …}` and neither
  `σ_f(u)` nor `Γ(u)` can be evaluated numerically.
- **B3. `(V)` needs a real tree direction.** Theorem A(A2) is an equivalence
  with Statement 3.9(iii), and the desk control of §10 TEST 3b exhibits a
  concrete failure at a double root that is not a branch coefficient. Any
  descendant that applies `(V)` to a root of `p_{f,F}` must first say why
  `F ∗ c` is defined.
- **B4. `[A, Prop 17.4]` is not reproduced in Sigray.** Sigray applies it
  only for `w` in the open positive quadrant. This report deliberately avoids
  it: the pure-power law (C4) is derived from the printed chart identity
  alone. No descendant should upgrade (C4) to a full Newton polygon homothety
  `N_g = (3/2) N_f` by invoking Prop 17.4 at general `w` without first
  obtaining its hypotheses.
- **B5. Occurrence.** Nothing here proves the sibling cell occurs. Every
  statement of §§2, 8 is conditional on a hypothetical realization.
- **B6. `s*` remains distant in the generic case.** If `Γ(u) > 0`, (C3) says
  the Keller row sits `κ_F Γ(u)` rows above the floor and `s* = (85i−26)/2`
  rows below the ceiling, and neither end reaches it. Closing that gap needs
  the intermediate rows, which remain unavailable; the homogeneous cascade
  is stopped through `s ≤ r` and is not reopened here.

## 10. Machine checks (exact, stdlib `Fraction`, scratch only)

```text
/tmp/bridge_s_check.py, /tmp/bridge_s_check3.py, /tmp/bridge_s_check4.py
TEST 1   Theorem B on (h,u,κ,φ) with u ∈ {3/2, 5/3, 7/4} and nontrivial
         prefixes: least x-exponent = σ_h(u) and floor polynomial = the
         (1,−u)-minimal form                                            PASS
TEST 2   (C1),(C2) on 7 genuine Jacobian pairs × 8 values of u: the
         inequality always holds, and equality ⇔ J(f↓,g↓) is a nonzero
         constant ⇔ {f↓,g↓} = {c1 x, c2 y}                              PASS
TEST 3b  negative control: for a non-tree root c the shear divisibility
         (A2) FAILS at a double root — (V) is a source input          FAILS,
                                                       as it must
TEST 3c  f = x^2(y−1)^2 − 1 (genuine double branch y = 1 ± 1/x):
         (A1),(A2),(A3), St 3.9(i)(ii)(iii) all hold                    PASS
TEST 3d  Theorem E: three distinct children of one parent share floor
         index and floor polynomial, equal to the (1,−u′)-minimal form   PASS
TEST 4b  the quasi-homogeneous bracket formula, 40 random tuples         PASS
TEST 4c  exhaustive: no admissible (p,q,A,B,deg Φ,deg Ψ) makes the top
         bracket coefficient vanish ⇒ Φ,Ψ constant                      PASS
TEST 6   (C4) pure-power floor law on 3 Jacobian pairs × 5 values of u   PASS
TEST 7   f_{l_f}^{l_g} = c g_{l_g}^{l_f} (§8.1), degenerate l_f = 0
         case correctly excluded                                        PASS
```

No software is promoted; these are desk controls for identities proved above,
and no conclusion rests on them alone.

## 11. Hostile attacks on this report's own results

1. *"Theorem B is Proposition 4.1 with a sign flipped, hence already known."*
   No. Proposition 4.1 is about `d_{h,F}` (Notation 3.10 explicitly takes the
   **largest** index) and its leading form depends on the whole branch.
   Theorem B is about the **least** index and is branch-free. The two are
   different data; (C3) shows they bound `s*` from opposite sides, and their
   sum is the total row count. A grep of the campaign (`xmodel`, `ladder`,
   `cases`) finds `d_F + d_{g,F} = 1−u` consumed at pole flags
   (`m2-td12-pole-entry-price-r1-hostile-review-fable5-20260829.md:81`) and
   no occurrence of a minimal-index, minimal-face, or `σ_h(u)` construction.
2. *"The floor of the chart could be created by cancellation, so `p_{h,min}`
   might vanish."* Ruled out inside the proof of Theorem B: distinct points
   of the minimal face carry distinct `η`-powers, so no cancellation is
   possible. Checked numerically in TEST 1 with prefixes chosen to create
   collisions.
3. *"Theorem D's classification forgets faces that are single points."*
   A single point is `deg Φ = 0`, which is the surviving case; the argument
   excludes only `a + b > 0`.
4. *"Theorem D might miss `u` irrational."* `u = π(F) ∈ Q` by Notation 3.6
   (`T_a := T_a^* ∩ π^{−1}(Q)`), and §2 pins `u = 1 − 13/κ_F` for this cell.
5. *"Theorem F confuses the reduced pattern degree with the full top."*
   No: `dp = 68` is the reduced `η`-degree, and the full top is `λ_f p^i` of
   `η`-degree `68 i`; the inequality then goes through `deg_η p_{f,j} ≤
   deg_η f^F = deg_y f`, which is an equality on the top `η`-power only.
6. *"Theorem F secretly uses `f − a` rather than `f`."* Notation 3.13 sets
   `p_F := p_{f,F}`, and for `F ∈ T_a^+` (`d_F > 0`) the tops of `f` and
   `f − a` coincide, so the bound is insensitive to the shift. The floor is
   sensitive to it; §4's Remark states which reading is used and why nothing
   is lost.
7. *"Theorem E proves the two sibling vectors are equal."* It does not. It
   proves the two **floors** are equal. The top-side freedom recorded by
   `1a602643...` §8.4 and audited in `876d1717...` §4 is untouched; the
   level-1 asymmetric exhibit survives Theorem E verbatim.
8. *"§5.4 is a kill."* It is not. It is a compatibility that is available
   only in the `Γ(u) = 0` branch, and §9 shows that branch is undecided. No
   kill, exclusion, or landing is claimed anywhere.
9. *"The bbox reading of Notation 2.4 could be wrong."* It is cross-checked
   twice: `k_g/k_f ∉ N*` in Lemma 2.1(iv) is content-bearing only in that
   direction (its proof forms `g − c f^{α}`, which needs `deg g = α deg f`),
   and `k_f < k_g` in (iii) forces `α < β`. Both agree with the campaign's
   already-reviewed `D_g/D_F = 3/2`.
10. *"The graded convolution is re-derived, so a fresh error could enter."*
    It is not re-derived: §5 consumes it verbatim from `1a602643...` §2.3
    as audited `PASS` in `876d1717...` §2, and only reads its least-index
    row, which was not previously read.

## 12. Smallest nonduplicate descendant

```text
TD12-S17-FLOOR-COORD/v1        (desk, source-local, one output file)
  input   : refs/sigray_full.pdf §§2–4 at the perimeter of §0 above;
            this report's Theorems B, C, D as the exact statement of the fork;
            no route data, no PairRef, no cell, no i.
  question: for a normalized counterexample of Notation 2.3, decide
            ord_x f + ord_x g ∈ {0,1}, i.e. decide Γ(0).
  outputs : (a) FLOOR-COORD proved  ⇒ Γ(u) > 0 at every vertex of every tree,
                the floor row is always the homothety (C4), the exponent
                ρ(u) = σ_g(u)/σ_f(u) is promoted as a new global invariant of
                the source pair, and §5.4 is closed as never cashable;
            (b) FLOOR-COORD refuted or shown independent ⇒ the interval
                [0, u_max] is the exact set of vertices at which the Keller
                row is the floor row, with the completely pinned floor pair
                {c_1, c_2 η}, c_1 c_2 = 1 (Theorem D), and the first jet-free
                Keller compatibility of the campaign becomes available at
                every vertex of that interval;
            (c) typed OPEN with the exact obstruction, if neither.
  fail-closed states: NORMALIZATION_SCOPE_UNCLEAR, ORD_X_UNDECIDED,
            AUT_CLASS_INSUFFICIENT.
  cost    : desk. No CAS, no AWS, no PairRef, no occurrence input.
```

This is strictly smaller than any packet in the frozen basis: it needs no
route, no cell, no `PairRef`, no completion, and no index `i`. It is not a
homogeneous-window cascade descendant, and it does not target `s = i+1` or
`s = r+1`. The route-separated `TD12-S17-SIBLING-PARENT-PAIRPACK/v1` of
`876d1717...` §6.2 remains the correct *next source* deliverable and is
unaffected; `FLOOR-COORD` is a prerequisite that can run in parallel and
needs none of that packet's absent inputs.

A second, independent, also-desk descendant, if a second lane is available:
apply Theorem F's argument at the separately owned `nu=25` B cell. This
report deliberately computes **no** B numbers, to keep the two source states
separated as the R1 erratum requires.

## 13. Nonclaims and scope firewall

Not claimed, not implied, and not to be read into anything above:

- any value of `v_{S_+,k}` or `v_{S_-,k}` for `k ≥ 1`; any emitted child
  vector; any gate verdict at any level; any `gcd`, binomial, or
  catalecticant test result;
- a `PairRef`, an exact pair, a fibre tag, a completion instance, an
  occurrence witness, a landing, a germ, or a counterexample;
- Galois conjugacy of the two sibling evaluations; any trace, norm, or
  symmetric-function relation between them; any shared pair, fibre,
  completion, source ladder, `c_g`, or exact pair with the `nu=25` B route;
- any new exit price, charge, flag, exit set, or first-separation claim; the
  reviewed charges `4+4` and `8` are neither used nor re-derived, and
  `charge_basis` is correctly absent because this task asserts no exit price;
- an upper cap on `deg_y f`, `deg_y g`, `deg_η P_k`, or `deg_η G_k`; any
  unquarantining of the `1a602643...` §8.3 cokernel/cascade dimensions;
- a reopening of the homogeneous window cascade, of `EN`/splice, or of
  Avenue 27; a `td` exclusion; a degree *upper* bound; a JC2 conclusion in
  either direction;
- any claim about `refs/`-external preprints: GGV22 is cited only as recorded
  in `ladder/REDUCTION.md`, is not load-bearing here, and no branch of the
  reduction is opened or closed by §8's remark 3;
- any software promotion. The `/tmp` scripts are desk controls for identities
  proved by hand; nothing is licensed to run on AWS, and no heavy successor
  is preregistered by this report.

`jc2-lean` was not read, opened, or touched. No canonical, source, or code
file was modified. No commit and no push was made. Exactly one repository
file was written: this report.

## Seal

Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`, verified at session
start and re-verified immediately before this seal. All charged hashes in §0
recomputed identically before reading and before sealing.

Body = all bytes of this file before the literal `## Seal` heading.

- Body byte count: `42816`.
- Body SHA-256:
  `c0c03d4edb1838f27ed0f1b86c8041568d41366a94f678209458ca3909831ac0`.
- Frozen Git basis:
  `92ebe92ad5986a47f01af9ed901260595dfed869`.
