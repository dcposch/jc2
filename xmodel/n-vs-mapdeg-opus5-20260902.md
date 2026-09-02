# N-VS-MAPDEG — the all-degree ceiling: what the boundary actually says

Lane: `N-VS-MAPDEG`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact desk CAS (sympy 1.14.0 / Python 3.14.7 over `Q`; an
explicit resolution-of-indeterminacy engine written for this lane; no Groebner,
no AWS, no fetching, no web). Drivers in `/tmp/nvm`, not installed in `box/`.

## 0. Custody, method, scope

The six charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all six match the charge exactly:

```text
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  deg-af-vs-n-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  chau-delta-budget-gpt55-20260902.md
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  companion-curve-alln-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  b3-e-geometry-opus5-20260902.md
12dea79fc65d31dd5ac2dac9fa3faff638cd1d5a12b7c6f72a7f18658b09ba4a  b3-e-geometry-review-grok46-20260902.md
```

**DA** = `DEG-AF-VS-N` (charged; **its review runs in parallel**, so consumed as
PROPOSALS only and re-derived where used), **CD** = Chau delta-budget, **CO** =
COMPANION-CURVE-ALLN, **MI** = MPRIME-ALLN-H2, **B3E** = B3-E-GEOMETRY, **B3E-R**
its grok46 review. MI / CO / B3E(+review) at banked/reviewed typings (`[P3]`,
`7.B'`, sheet gate, Lemma 4.1, `(K)`, `(C1)`-`(C3)`, THEOREM PROFILE, Lemma A,
Chau C6-C8, LEMMA E-ETALE and Prop 3.1/LOC-1, CONFIRMED at B3E-R:51-127).
`Z(G)=1`, case (A) and the A2 cells are **not consumed anywhere**; `jc2-lean` not
inspected; no canonical ledger edited.

Local PDFs read this session with `pdftotext -layout` (hashed):

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7  refs/chau1999_apm71_full.pdf
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
```

Nothing was fetched. `refs/` contains **no** Jelonek and **no** Abhyankar-Moh
item (verified by listing); those stay ABSENT, exactly as DA §7 records.
No `charge_basis` line: **this report asserts no new exit price.**

## 1. Verdict, up front

```text
(1) D_min(F) = min{ max(deg G_1,deg G_2) : G = psi o F o chi } is the invariant.
    BOTH Aut factors are needed: right composition fixes A_F, N, a, W, s_l, mu_l,
    delta_aff, Gamma, and fixes (d,e) and R_0 (Chau 2004 p.2) while moving only
    K = gcd(deg P,deg Q).  So D_min = min_psi [max(d,e)·K_min] and the source half
    is exactly "minimise K".  Is D_min <= C(N) known?  NO -- neither proved nor
    refuted, and nothing in refs/ addresses it.  It IS false for general dominant
    maps (NEG-GEN): (x, x^c y^N) has geometric degree N, n_min = 1, and
    D_min >= (c+N+1)/2.  Those families spend deg Jac, pinned to 0 by Keller.
(2) On the resolution, with Z = Phi^*(L_infty) = sum_C m_C C:  m_{E_0} = D and
    s_l·n = m_{C_l} -- D and n are two values of the SAME polar multiplicity.
    New, machine-verified on 41 maps:
       (DEG-SPLIT)  D = sum_l s_l n_{c(l)} + kappa + T
       (NOETHER-K)  sum_i a_i = 3D - 2N - kappa + n(W-S),  sum_i a_i^2 = D^2 - N.
    DEG-SPLIT sharpens Chau's cap to deg A_F-bar <= D - 1 (never attained).
    "sum Deg a~ = N" is N = sum m_C k_C: it bounds the non-contracted boundary by
    N and nothing on the contracted part.  det(boundary matrix) = +-1 for EVERY
    compactification of A^2 -- an identity, blind to forks and to chain length.
(3) The dicritical parametrisation degree is s_l·n, so the "something" is
    n = m_{C_l}/s_l and the semigroup route returns OPEN[DELTA-AFF-VS-N].  NEW:
    MERIDIAN-FLOOR+, p(W-S) >= N-1 with p = min{deg_t l(a,b)} <= n-1, hence
    n >= ceil((N-1)/(W-S)) + 1 -- one unit sharper than DA at every cell, and at
    N = 4 it re-derives CD Sec 5's n >= 4 from group theory alone.
(4) THEOREM NO-CEILING: no intersection-theoretic boundary instrument can bound D
    at fixed N.  Two machine-verified families realise it ((x, x^c y^N) with
    D -> infinity, all growth in T; psi_k o (x, x y^N) with deg A_F -> infinity).
    Free datum: the SATELLITE MASS T, the boundary avatar of Jung-van der Kulk
    word length.  The one identity that bites is (NOETHER-K) = the Keller
    condition; it reduces the question to one integer,
    Z.K_X = sum a_i - 3D = -2N - kappa + n(W-S), so ANY bound Z.K_X <= f(N)
    closes OPEN[DELTA-AFF-VS-N] -- that is OPEN[ANTICANON-DEFECT].  Honest scope:
    Z.K_X is UNBOUNDED ABOVE for general dominant maps (psi_k o (x,xy^3) reaches
    +7 at fixed N = 3), so any proof must use the Keller condition essentially;
    the only Keller data I have are automorphisms, where Z.K_X = -3 (Noether).
(5) Crossing: (N,W) is EMPTY once D_min <= C with C <= ceil((N-1)/(W-1)) + 1; at
    W = 2, D_min >= N + 1.  Moh 1983 (verified in refs/) gives D_min >= 101, so
    ANY proof of C(N) <= 100 closes that N outright -- the whole (B2) range 5..16
    and (B3) range 4..8 at once, the cheapest crossing in the record.
```

## 2. Part (1): the question, stated invariantly

### 2.1 The group, and why both factors are needed

Let `F = (P,Q) : C^2 -> C^2` be Keller (`Jac F in C^*`) and noninvertible, of
geometric degree `N`. `G := Aut(C^2) x Aut(C^2)` acts by
`(psi,chi)·F := psi ∘ F ∘ chi`. Every member of the orbit is Keller (chain rule)
and noninvertible, and has the same `N`.

* **Left (target).** `A_{psi∘F} = psi(A_F)`; the source curve `E = F^{-1}(A_F)`
  is literally unchanged. This is DA's `n_min` orbit.
* **Right (source).** `A_{F∘chi} = A_F` **on the nose** — the non-properness set
  is a target-side limit condition and does not see the source coordinates.
  Chau 2004 p.2 adds the sharp form: *"the numbers `d, e, B^d/A^e` and the
  polynomial `R_0(u,v)` are invariant of `f` under right actions of automorphisms
  of `C^2`"*. So `N, a, W, s_l, mu_l, K_p, a_p, delta_aff, Gamma, n` are all
  right-invariant while `deg P = Kd`, `deg Q = Ke` are not: right composition
  moves `K` and fixes `(d,e)`. *Control:* `F = (x+y,(x+y)y)` has `(d,e)=(1,2)`,
  `K=1`; `F ∘ (x, y+x^3)` has degrees `(3,6)`, so `K=3` with `(d,e)` unchanged and
  `A_F = {u=0}` in both.

> **DEFINITION.** `D_min(F) := min{ max(deg G_1, deg G_2) : G ∈ G·F }`.

Well defined (least element of a nonempty set of positive integers) and constant
on `G`-orbits. **Any statement "the map degree is bounded by `N`" must be about
`D_min`**: for the raw degree the answer is FALSE and trivially so (right
composition alone), which is the map-side twin of the campaign's banked
`NO-DEG-CAP [D]`.

Because `D = K·max(d,e)` and `(d,e)` is right-invariant,

```text
     D_min(F) = min_{psi ∈ Aut}  [ max(d,e)(psi∘F) · K_min(psi∘F) ],
     K_min(G) := min{ gcd(deg(G∘chi)_1, deg(G∘chi)_2) : chi ∈ Aut } .
```

So the source-minimisation is *exactly* the minimisation of `K = gcd(deg P,deg Q)`.

### 2.2 `n_min <= D_min`, and the gap

Chau's cap (CD §1/§4, CONFIRMED there; Chau 2004 Thm 1 + Cor 1 read directly)
gives `sum_i deg D_i <= max(deg P, deg Q)` for the actual components of `A_F`.
Applying it to a `D_min`-attaining representative `G = psi∘F∘chi`:
`n_min <= deg closure(psi(A_F)) <= D(G) = D_min`. So

> **`n_min(F) <= D_min(F)`**, unconditionally.

Is it ever strict at the minimum? **Always**, by §3.3 below (`D >= n + 1` in
every gauge, hence `D_min >= n_min + 1`). In the Chau parameters this reads
`K >= S·m + 1 >= m + 1`: **Chau's `m <= K` is never an equality.**

### 2.3 The classical dictionary, made exact

Homogenise `P, Q` to the common degree `D := max(deg P, deg Q)`; the forms
`P^h_D, Q^h_D, Z^D` have no common factor. Let `sigma : X -> P^2` resolve the
base locus (all base points lie on `L_infty`, since `F` is a morphism on `A^2`),
`Phi := F-bar ∘ sigma`, `a_1,...,a_r` the base multiplicities. From the classes
in `Pic X = <H := sigma^*L, E_1,...,E_r>`:

```text
  (D1)  Z := Phi^*(L_infty) = D·H - sum_i a_i E_i ,     Z^2 = N ,
        i.e.   sum_i a_i^2 = D^2 - N .
  (D2)  deg P · deg Q = N + I_infty ,   I_infty := sum_{z ∈ L_infty}
        I_z( {P=u}-bar , {Q=v}-bar )   for generic (u,v)          [Bezout]
  (D3)  the leading forms satisfy  P^~ = c H_0^d , Q^~ = c' H_0^e  (Jac(P^~,Q^~)=0),
        deg P = K d, deg Q = K e, gcd(d,e) = 1;  minimality forces d ∤ e, e ∤ d.
  (D4)  Newton/AM data of A_F:  Gamma (semigroup at infinity), n ∈ Gamma,
        p := min{deg_t l(a,b)} ∈ Gamma,  mult at infinity = n - p     [DA (R4)]
  (D5)  Jung-van der Kulk: Aut(C^2) = Aff *_{Aff∩J} J.  The de Jonquières
        length of chi is what right composition spends; §5.3 identifies its
        boundary avatar as the satellite mass T.
```

`(D1)` and `(D2)` are two readings of one deficiency: `(D2)` says "bound `D` by
`N`" *is* "bound the contact at infinity of the two level pencils"; `(D1)` puts
it on the resolution, where §3 can act on it.

### 2.4 THEOREM NEG-GEN: for general dominant maps the answer is NO

> **THEOREM NEG-GEN.** For every `N >= 1` the family
> `F_{N,c}(x,y) := (x, x^c y^N)`, `c >= 1`, consists of dominant polynomial maps
> `C^2 -> C^2` of geometric degree exactly `N`, with `A_F = {u = 0}` (so
> `n = n_min = 1`, one place at infinity), and
> ```text
>          D_min(F_{N,c})  >=  (c + N + 1)/2  ->  infinity .
> ```
>
> *Proof.* For `u ≠ 0` the fibre is `{x=u, y^N = v/u^c}`: `N` points, so
> `deg_geo = N`; the escaping values are exactly `{u=0}`. For any
> `G = psi∘F∘chi`, the chain rule gives
> `Jac G = c_0 · (Jac F)(chi) = c_0 N · chi_1^{c} · chi_2^{N-1}`, whose degree is
> `c·deg chi_1 + (N-1)·deg chi_2 >= c + N - 1` (coordinates of an automorphism are
> nonconstant). On the other hand `deg Jac G <= deg G_1 + deg G_2 - 2 <= 2 deg G - 2`.
> Hence `2 deg G - 2 >= c + N - 1`. ∎

Two readings, both load-bearing.

* **The general-dominant version of `OPEN[N-VS-MAPDEG]` is FALSE**, with an
  explicit family, at every fixed `N` and even at fixed `n_min = 1`. So no proof
  can go through finiteness/properness/geometric-degree arguments alone.
* **The datum the family spends is `deg Jac`.** The Keller hypothesis is
  `deg Jac = 0`, the extreme value; §3.4 shows its exact boundary shadow is the
  Noether-type identity `(NOETHER-K)`, and §5 shows that this is the *only*
  banked constraint the unbounded families violate.

`NEG-GEN` also shows `n_min <= D_min` can be arbitrarily strict for general maps.

### 2.5 Literature custody — what is actually in `refs/`

```text
 (M) MOH 1983, Crelle 340 [hashed above; read with pdftotext -layout].
     Introduction p.143 and Appendix II, verbatim: "There is no counter-example
     of polynomials of degrees less than or equal to 100 for the Jacobian
     conjecture."  His standing normalisations are deg f = deg_y f (a generic
     linear RIGHT change) and "the degrees of f and g can not be reduced
     simultaneously" -- Moh's theorem is natively about a DEGREE-MINIMAL
     representative.  Residual rows (64,68),(84,56),(75,50),(99,66) settled there.
     >> MOH-FLOOR:  a Keller counterexample has  D_min >= 101.  <<
     (If D_min <= 100 some psi∘F∘chi is Keller of degree <= 100, hence an
     automorphism by (M), hence F is.)
 (C99) CHAU 1999, Ann. Polon. Math. 71 [hashed].  Verified:
       Thm B (p.288):  deg P = kd >= deg Q = ke, gcd(d,e)=1  ==>  e = 1, or
              deg_geo f = r d + s e >= min{2e,d},  r,s >= 0, r+s >= 1;
       Thm 4.1(ii) (p.301): deg_geo f = sum_{[phi]} gcd(a,b)·gcd(deg P_phi,
              deg Q_phi)·d e / i_phi,  i_phi | d or i_phi | e;
       Thm C (p.288):  deg P (chi_Q - N) = deg Q (chi_P - N).
     SUBSTANCE: Thm B constrains only the REDUCED SHAPE -- N lies in the
     numerical semigroup <d,e> and (d>e>1) forces e <= N -- and says nothing
     about K; Thm C is homogeneous in K (d(chi_Q-N) = e(chi_P-N)).  Since
     D = K·max(d,e) and §2.1 shows K is the right-Aut coordinate, the literature
     has bounded the half of the degree that is NOT the obstruction.
 (C04) CHAU 2004 (arXiv math/0305088): Thm 1, Cor 1, Cor 2 read directly, agreeing
     with CD §1 including CD's M_R notation repair, plus the right-invariance
     sentence quoted in §2.1.
 (J)  JELONEK: ABSENT from refs/ (listing checked); used for nothing.  Its bound
     is in (deg f, deg g), an instance of the open question -- DA §7 (L1)
     CONFIRMED, not re-litigated.
 (AM) ABHYANKAR-MOH: ABSENT from refs/; DA's (AM-SG) consumed at the campaign's
     banked typing (AM-CHECK.md:50-63), only in §4.3, flagged there.
```

> **VERDICT on the charge's question (1).** `D_min <= C(N)` is **open**: not a
> theorem, not refuted, and not stated in any source in `refs/`. What *is* in the
> literature is (i) a **floor**, `D_min >= 101` (Moh), and (ii) a bound on the
> reduced shape `(d,e)` by `N` (Chau 1999 Thm B). Both run the same way as
> MERIDIAN-FLOOR: **every verifiable statement in the record bounds the map degree
> from below.** The upper half has no literature at all.

## 3. Part (2): the boundary — the polar ledger, and what it proves

Notation as in §2.3. Write `E_0` for the strict transform of `L_infty` and, for a
boundary component `C`, `m_C := ord_C Phi^*(L_infty) >= 0` and `c_C := Z·C`.
`L~` is SNC (blowing up a point of an SNC configuration preserves SNC), its dual
graph is a tree with `r+1` vertices, and `X ∖ L~ = A^2`.

### 3.1 The trichotomy and the six identities

`Phi(C)` is a point, or `L_infty`, or an irreducible curve meeting `A^2`; in the
last case `Phi(C) ∩ A^2` is a component of `A_F` (the affine part of `Phi(L~)`
*is* the non-properness set) and `C` is a **dicritical**. Correspondingly
`m_C > 0` iff `Phi(C) ⊆ L_infty`, and by the projection formula

```text
   c_C = Z·C = (Phi_*C)·L_infty =
        0                                    C contracted (to a point of L_infty
                                             OR of A^2 -- both occur),
        k_C := deg(Phi|_C) >= 1              Phi(C) = L_infty,
        lambda_l := s_l · n_{c(l)}           C = l dicritical, m_l = 0.
```

> **(I1)** `m_{E_0} = D`.  *Proof.* `Z·sigma^*L = D` from the class; and
> `sigma^*L·C = 0` for exceptional `C`, `= 1` for `E_0`. ∎
> **(I2)** `N = Z^2 = sum_C m_C c_C = sum_{C -> L_infty} m_C k_C`.
> In particular `#{C : Phi(C) = L_infty} <= kappa := sum k_C <= N`.
> **(I3)** contracted `C`: `m_C(-C^2) = sum_{C' adj C} m_{C'}`.
> **(I4)** `C -> L_infty`: `m_C(-C^2) = sum_{C' adj C} m_{C'} - k_C`; and
> `e_C = m_C` (the ramification index of `Phi` along `C` is its multiplicity in
> `Phi^*L_infty`).
> **(I5)** dicritical `l`: `m_l = 0` and `sum_{C' adj l} m_{C'} = s_l n_{c(l)}`.
> **(I6)** the boundary components form a **`Z`-basis of `Pic X`** (they are
> `r+1` classes spanning the rank-`r+1` lattice because `X ∖ L~ = A^2` has
> trivial `Pic` and `H^2`), so the boundary intersection matrix has
> `det = (-1)^r`.

Two working rules follow, and they are what the drivers use:

```text
   m_{new}  =  (sum of m over the components through the blown-up point)  -  a_i ,
   c_{Ctilde}  =  a_C  -  sum{ a_i : p_i lies on Ctilde } ,   with a_{E_0} := D .
```

**`(I6)` is an identity, not a constraint.** It holds for *every* SNC
compactification of `A^2` whatsoever, by the same argument. That settles one
half of the charge's question (2): the degree-free determinant package
(`det L = -1` and its relatives) cannot bound the number of forks, the chain
length, or the degree, because it is satisfied by every candidate. What the
Domrina-Orevkov apparatus adds beyond `(I6)` is the *sub-chain* conditions
(`det R_a = 1`, `det L_a > 1`, pairwise-coprime branch determinants), and those
are conditions on which chains can occur, not on how long they are: the
Hirzebruch-Jung chains of `1/q` for `q -> infinity` have unimodular sub-blocks of
unbounded length.

### 3.2 DICRITICAL-NEIGHBOUR

> **PROPOSITION DN.** Under `H2` (so `A_F` is irreducible of degree `n` with one
> place at infinity) and Orevkov's `l' := l ∩ Phi^{-1}(A^2) ≅ A^1`
> (MI Lemma 4.1's structural input, also B3E §3.2), the dicritical `l` has
> **exactly one** boundary neighbour `C_l` with `m_{C_l} > 0`, and
> ```text
>                 s_l · n  =  m_{C_l} .
> ```
> *Proof.* `l ∖ l' = l ∩ Phi^{-1}(L_infty)` is a single point `t_infty` because
> `l' ≅ A^1` and `l ≅ P^1`. Neighbours with `m > 0` lie in `Phi^{-1}(L_infty)`,
> hence meet `l` inside `{t_infty}`; SNC allows at most one component besides `l`
> through a point. Now `(I5)`: `s_l n = sum_{C' adj l} m_{C'} = m_{C_l}`. ∎

So `D = m_{E_0}` and `s_l n = m_{C_l}`: **`D` and `n` are two values of one
function `m` on the boundary tree**, read at the root and at the dicritical's
neighbour. That is the sharpest form of the question the charge asked for.

### 3.3 THEOREM DEG-SPLIT — the exact decomposition of the map degree

Call a base point `p_i` **satellite** if it lies on two boundary components
(`prox(i) = 2`) and **free** if on one. Put `T := sum_{satellite i} a_i`.

> **THEOREM DEG-SPLIT.** For every dominant `F = (P,Q)` (Keller not needed),
> ```text
>        D  =  sum_{l dicritical} s_l · deg(closure Phi(l))  +  kappa  +  T ,
>        kappa = sum_{C -> L_infty} k_C >= 1 ,   T >= 0 .
> ```
> *Proof.* Summing `c_C` over the reduced boundary, the §3.1 trichotomy gives
> `sum_C c_C = kappa + sum_l s_l n_{c(l)}`. The class of `L~_red` is
> `H - sum_{prox(j)=2} E_j`: the coefficient of `E_j` in
> `(H - sum_{I_0}E_i) + sum_i (E_i - sum_{j prox i}E_j)` is `1 - prox(j)`, and
> `prox(j) ∈ {1,2}` by SNC. Hence `Z·L~_red = D - T`. Finally `kappa >= 1` because
> `Phi` is surjective with `Phi^{-1}(L_infty) ⊆ L~`. ∎

> **COROLLARY CAP-STRICT.** For a noninvertible Keller map (`A_F ≠ ∅`, and every
> component of `A_F` is the image of at least one dicritical),
> ```text
>       deg A_F-bar  =  sum_c n_c  <=  sum_l s_l n_{c(l)}  =  D - kappa - T  <=  D - 1 .
> ```
> In Chau's parameters, with `H2` and `n = m·max(d,e)`:
> `(K - S m)·max(d,e) = kappa + T >= 1`, i.e. **`K >= S m + 1 >= m + 1`.**

> **COROLLARY.** `D >= n·S + kappa >= n + 1`, in every gauge; hence
> `D_min >= n_min + 1`.

**Correction to a charged input (typed).** CD item 4 and CO §5 run the `(9,6)`
row with a realised component `D_1` of degree `9 = max(deg P, deg Q)`, i.e. with
Chau's cap *saturated*, and conclude that no companion can be added.
`CAP-STRICT` says more: at `(9,6)` one has `deg A_F-bar <= 8`, so **no `A_F` with
a degree-9 component occurs at that row at all**, companion or not. This
*strengthens* CD's CLAIM [D] and is consistent with CO's own typing of the
`(9,6,2)` curve as REPRESENTATIVE (it is a genuine one-place rational curve; it
is not a component of the non-properness set of a Keller pair of degrees `(9,6)`).
It also removes the row from the ledger independently of Moh, who kills it too.

### 3.4 NOETHER-KELLER — the boundary shadow of `Jac F ∈ C^*`

> **THEOREM NOETHER-K.** With `R` the ramification divisor of `Phi`
> (`K_X = Phi^*K_{P^2} + R`), for every dominant `F`
> ```text
>   sum_i a_i  =  3D - 3N + Z·R ,
>   Z·R  =  Z·R_aff  +  sum_{C -> L_infty}(m_C - 1) k_C  +  sum_l (mu_l - 1) s_l n_{c(l)} ,
> ```
> where `R_aff` is the part of `R` supported on the strict transform of
> `{Jac F = 0}`. If `F` is **Keller** then `R_aff = 0` and, under `H2`,
> ```text
>   (NOETHER-K)     sum_i a_i  =  3D - 2N - kappa + n (W - S) ,
>                   sum_i a_i^2 = D^2 - N ,
> ```
> with `W = sum_l s_l mu_l = N - a` (`[P3]`), `S = sum_l s_l`.
> *Proof.* `Z·K_X = -3D + sum a_i` from the classes; `Z·K_X = -3N + Z·R` from
> `K_X = -3Z + R`; contracted components have `Z·C = 0` so drop out of `Z·R`;
> along a component onto `L_infty` the ramification index is `m_C` (`I4`), along
> a dicritical it is `mu_l = ord_l Phi^*(A_F-bar)` (`E = F^*A_F` reduced since `F`
> is étale). Substituting `sum_{C→L_infty} m_C k_C = N` gives the Keller form. ∎

At `S = 0` (`A_F = ∅`, i.e. an automorphism) `(NOETHER-K)` reads
`sum a_i = 3D - 3`, which is **Noether's equation for a plane Cremona map** — so
`(NOETHER-K)` is exactly the Keller generalisation of Noether's equations, with
`N`, `kappa` and the dicritical ramification as the correction terms. Machine
control: `(x, y+x^k)` for `k = 2..5` and `(x+y^k, y)` for `k = 2,3` all return
`sum a_i - 3D = -3` on the nose (§3.6 table).

Two consequences used later:

```text
   sum_{satellite} a_i  =  T  =  D - S n - kappa ,
   sum_{free}      a_i  =  2(D - N) + n W .
```

### 3.5 Where `sum Deg a~ = N` enters, and what it bounds

B3E §6 locates the literature's `N = 4` kill on Domrina-Orevkov's generic-sheet
identity `sum_{a~ over a} Deg a~ = 4`, and asks what it becomes at general `N`.
In the present ledger it is `(I2)`:

```text
       N  =  sum_{C : Phi(C) = L_infty}  m_C · k_C .
```

That is a genuinely finite statement and it is the *only* finiteness in the
boundary package:

* the number of components **over `L_infty`** is at most `kappa <= N`, and each
  has `m_C <= N`;
* the number of **dicriticals** is at most `S <= W/2 <= N/4` (`7.B'`: `mu_l >= 2`);
* so the non-contracted boundary components number at most `N + N/4`;
* and it bounds **nothing** on the contracted part. `E_0` itself is contracted as
  soon as `D > N` (else `(I2)` gives `N >= m_{E_0}k_{E_0} = D k_{E_0} >= D`), so
  the very component carrying the map degree is invisible to `(I2)`.

**Forks and chain length.** Nothing in `(I1)-(I6)` bounds `r`: `(D1)` gives only
`r <= D^2 - N`, a bound in `D`, and the ladders of §5.1 have `r` growing linearly
in `D` at fixed `N` with **one** fork throughout. The shortcut "every leaf is a
dicritical or lies over `L_infty`" is also false — a leaf created free and then hit
only by satellite blow-ups keeps tree-degree 1 while its self-intersection drops
arbitrarily. **The determinant + degree package bounds the non-contracted part of
the boundary by `N` and leaves the contracted part entirely free.**

### 3.6 Machine verification

Driver `/tmp/nvm/blowup.py` (`sha256 206e0f4d…`) resolves `F-bar` by explicit
two-chart blow-ups over `Q`, returning the cluster with its proximity structure;
`/tmp/nvm/ident.py` (`67d72fd2…`) and `/tmp/nvm/synth.py` (`0f76688f…`) do the
Picard-lattice bookkeeping. **41 distinct dominant maps** were resolved (`D <= 24`, `N <= 50`, `r <= 15`);
**all 41** satisfy `(I1)`, `(I2)`, `Z^2 = D^2 - sum a_i^2`, `m_C >= 0`,
`c_C >= 0` and `DEG-SPLIT` — **0 failures**. A representative extract:

```text
 map                     D   N  kappa  Lam=sum s_l n_c   T   sum a_i   sum a-3D
 (x, xy)                 2   1    1        1             0     3         -3
 (x, y^2)                2   2    1        0             1     2         -4
 (x, xy^2)               3   2    2        1             0     5         -4
 (x, y+x^k), k=2..5     k   1    1        0            k-1   3k-3       -3   Keller
 (x+y^k, y), k=2,3       k   1    1        0            k-1   3k-3       -3   Keller
 (x, x^2 y)              3   1    1        1             1     6         -3
 (x, x^2 y^2)            4   2    1        2             1     8         -4
 (x^2 y, y)              3   2    2        1             0     5         -4
 (x^5, y^10)            10  50    5        0             5    10        -20
 psi_k ∘ (x,xy), k=2..5 2k   1    1        k            k-1   6k-3       -3
 psi_2 ∘ (x,xy^2)        6   2    1        2             3    16         -2
 psi_3 ∘ (x,xy^2)        9   2    2        3             4    25         -2
 psi_k ∘ (x,xy^2), k=2..6  6k  2   1,2,1,2,1  k        3,4,7,8,11   -2,-2,0,0,+2
 psi_k ∘ (x,xy^3), k=2..6  4k  3   1,1,3,1,1  k        5,8,9,14,17  -1,+1,+1,+5,+7
 psi_k = (u,v) |-> (u+v^k, v)
```

The last two rows are the ones that matter for §5.4: at **fixed `N`** they have
`n = deg A_F = k -> infinity`, `T -> infinity`, and the anticanonical defect
`sum a_i - 3D` **turns positive**. They are of course not Keller.

Positive controls: `(x, xy)`, `(x, y+x^3)`, `psi_2∘(x,xy)` were also computed by
hand and by an independent synthetic-cluster evaluator; all three agree on
`(a_i, prox, D, m, c, N)`. Negative control: the predicate "every `m_C = 0`
component is a dicritical" FAILS on `(x, x^2 y)`, exposing a component contracted
to an **affine** point — a case my first reading of `Phi^{-1}(A^2)` had wrongly
excluded. `DEG-SPLIT` is unaffected (`c_C = 0` either way); §3.1 is repaired.

### 3.7 THEOREM NO-CEILING — why this package can only give floors

> **THEOREM NO-CEILING.** Let `L_r = <H, E_1..E_r>` with `H^2 = 1`,
> `E_i·E_j = -delta_ij`, `H·E_i = 0`. The constraints that the boundary ledger
> imposes on `Z` — `Z` nef, `Z^2 = N > 0`, `Z·C >= 0` for the boundary classes,
> `Z = D H - sum a_i E_i` with `a_i >= 1` and the proximity inequalities — do not
> bound `D = Z·H` at fixed `N`.
>
> *Proof.* Hodge index on a lattice of signature `(1,r)` gives, for `Z, H` in the
> positive cone, `(Z·H)^2 >= Z^2 H^2 = N` — a **lower** bound `D >= sqrt(N)`, and
> that is the only inequality available in this direction. For unboundedness:
> `Z = D H - sum_{i=1}^{r} y_i E_i` has `Z^2 = D^2 - sum y_i^2`, and for every
> `D` with `D^2 >= N` the value `D^2 - N` is a sum of four squares, so `r = 4`
> already realises `Z^2 = N` with `Z·H = D` arbitrary. Every constraint in
> `(I1)-(I6)`, `(D1)`, `DEG-SPLIT` is of the form `Z·(effective) >= 0` or an
> equality between such pairings; none is a negativity. ∎

This is the structural reason the campaign has only ever produced floors on the
degree — MERIDIAN-FLOOR, Chau's cap, `DEG-SPLIT`, `MOH-FLOOR` — and it says a
ceiling must come from outside the intersection theory of the resolution. §5.4
names the one place where such an input can enter.

## 4. Part (3): the semigroup, and a sharper meridian floor

### 4.1 The dicritical parametrisation returns `n`

`phi_l = eta ∘ h_l : l' ≅ A^1 -> A_F ⊂ A^2` with `deg h_l = s_l`, so its
coordinate degrees are `s_l·(deg a, deg b)` and the parametrisation degree is
`s_l·n`. The charge asks whether "the something" is bounded by semigroup data
plus `N`. It is `n = deg A_F-bar` itself, and by `PROP DN` it equals
`m_{C_l}/s_l`. Since `n ∈ Gamma` with the `(R1)-(R4)` window of DA §3.3 and
`#gaps(Gamma) = delta_aff`, bounding `n` from `Gamma` is exactly bounding
`delta_aff`: the semigroup route is **not** independent of
`OPEN[DELTA-AFF-VS-N]`. This confirms DA §5.3 by a second, boundary-side,
computation. The conductor `c(Gamma) = 2 delta_aff` enters only through the AM
ceiling, §4.3.

### 4.2 THEOREM MERIDIAN-FLOOR+ — the generator count is `p`, not `n`

DA's MERIDIAN-FLOOR generates `pi_1(A^2 ∖ A_F)` by the `n` meridians of a
**generic** line (Zariski). The pencil through the *point at infinity of `A_F`*
does better.

> **THEOREM MERIDIAN-FLOOR+ (all `N`, `H2`).** Let `p := min{ deg_t l(a(t),b(t)) :
> l affine-linear }` (DA's `p`; `1 <= p <= n-1` for `n >= 2`). Then
> ```text
>        p · (W - S)  >=  N - 1 ,       hence      n  >=  ceil((N-1)/(W-S)) + 1 ,
> ```
> and at `W = 2` (where `S = 1` is forced by `mu_l >= 2`): `p >= N-1`, `n >= N`.
>
> *Proof.* (i) Choose affine coordinates realising the minimum, so
> `z_A := ` the unique point at infinity of `A_F-bar` is the vertical direction
> and `deg_y f = p` for the defining polynomial `f` of `A_F` (the vertical line
> `x = c` meets `A_F` in the `deg a = p` points `(c, b(t_i))`, `a(t_i) = c`, for
> **every** `c`, so `f` has constant leading `y`-coefficient: no vertical
> asymptote). (ii) Zariski-van Kampen for a curve monic in `y`: `pi_1(A^2 ∖ A_F)`
> is generated by the `p` meridians of a generic fibre `{x = c} ∖ A_F`.
> (iii) `A_F` irreducible (`H2`), so those `p` generators are all conjugate to a
> single meridian, whose monodromy image has cycle type
> `1^a · prod_l mu_l^{s_l}` (MI:694-695): support `W`, with `S` nontrivial cycles.
> (iv) `F : A^2 ∖ E -> A^2 ∖ A_F` is finite étale of degree `N` with connected
> total space (LEMMA E-ETALE, B3E-R:51-67 CONFIRMED), so the monodromy is
> transitive. Starting from `N` singleton blocks, one generator merges at most
> `sum_{cycles}(len - 1) = W - S` blocks; reaching one block needs `N-1` merges. ∎

Comparison and controls.

* Strictly sharper than DA's floor: `p <= n-1`, so `n >= p+1` improves
  `n >= ceil((N-1)/(W-S))` by one unit at every cell.
* At `N = 4`, `W = 2` it returns `n >= 4`. CD §5 obtained `n >= 4` for `(B3)`
  independently, from the delta budget (and DA flagged CD's as the sharper one).
  **MERIDIAN-FLOOR+ re-derives CD's bound from group theory alone**, with no
  budget and no `delta_infty` — a two-route agreement on a number the campaign
  uses.
* At `N = 5`, `W = 2`: `p >= 4`, `n >= 5`; the record's Gate TG value
  (`d_min >= 4`) is now the value of `p`, not of `n`.
* The hypothesis `mu_l >= 2` is `7.B'`, banked; `S <= W/2` is its consequence.

### 4.3 What the semigroup then gives

Combining with DA's `(AM-SG)`-based ceiling `n <= 2 delta_aff + b_1 - 1
<= 3 delta_aff` (DA Theorem DEG-DELTA(b), typed there with the residual
`OPEN[MIN-EMBED-DEGREE]`; consumed here as a PROPOSAL and flagged):

```text
   delta_aff  >=  n/3  >=  ( ceil((N-1)/(W-S)) + 1 ) / 3        [conditional on (AM-SG)]
   delta_aff  <=  p_a(n) - (n-p)(n-p-1)/2                        [DA (R4), a ceiling]
```

The first is a **floor** on the affine singularity content that grows with `N` —
the wrong direction for the gates, as DA already noted, but now one unit better.
The second is a ceiling only once `n` is known. Nothing in the semigroup produces
a ceiling in `N`; §5.4 says where one could.

## 5. Part (4): the negative route

### 5.1 Two machine-verified families at fixed `N`

Both are dominant polynomial maps, so every boundary identity of §3 holds
automatically; both were run through the resolution engine.

```text
 (A)  F = (x, x^c y^N):  N fixed, D = c+N -> infinity, n = deg A_F = 1 fixed;
      growth is ENTIRELY in T.   [c = 1..5, N = 1..8, 40 maps, all identities OK]
      N=1: D=2,3,4,5     kappa=1        Lam=1          T=0,1,2,3
      N=8: D=9,..,13     kappa=8,1,2,1,4  Lam=1,2,1,4,1  T=0,7,8,7,8
 (B)  F = psi_k ∘ (x, x y^N),  psi_k = (u,v) |-> (u+v^k, v):  N fixed,
      D -> infinity AND deg A_F = Lam = k -> infinity.
      N=1: k=1..5  D=2,4,6,8,10     T=0,1,2,3,4     Z·K_X = -3 throughout
      N=2: k=2..6  D=6,9,12,15,18   T=3,4,7,8,11    Z·K_X = -2,-2,0,0,+2
      N=3: k=2..6  D=8,12,16,20,24  T=5,8,9,14,17   Z·K_X = -1,+1,+1,+5,+7
```

So the **intersection-theoretic boundary ledger together with the affine data
does not decide the ceiling**, in the strongest sense: `(A)` and `(B)` satisfy
`(I1)-(I6)`, `DEG-SPLIT`, `(D1)`, `PROP DN`, the one-place-at-infinity structure
and Chau's cap, at fixed `N`, with `D -> infinity` and (in `(B)`) `n -> infinity`.
Combined with THEOREM NO-CEILING this is not merely "I could not derive it": no
instrument of that kind exists. The `Z·K_X` column of `(B)` is the datum §5.4
turns on: at fixed `N` and growing `n` the anticanonical defect grows too, and in
this ambient class it is unbounded.

### 5.2 The free datum, named

> The single quantity that is free in every candidate family is the
> **satellite mass** `T = sum_{satellite base points} a_i`. `DEG-SPLIT` says
> `T = D - S n - kappa` with `kappa <= N` and `S <= W/2`; and `T` is precisely
> the **Jung-van der Kulk word length seen on the boundary**: for the de
> Jonquières automorphism `(x, y+x^k)` the engine returns `kappa = 1`, `S = 0`,
> `T = k - 1 = D - 1`, i.e. all of the degree sits in `T`.

Hence the exact decomposition of the open problem:

```text
   OPEN[N-VS-MAPDEG] (upper half)   <==>   OPEN[DELTA-AFF-VS-N]  AND  OPEN[SAT-MASS] ,
   OPEN[SAT-MASS]:  is  T = D - S n - kappa  bounded in terms of N for a
                    DEGREE-MINIMAL Keller representative?
                    bounded quantity: T ∈ Z_{>=0};  T = 0 iff every base point of
                    the linear system at infinity is free.
```

`kappa <= N` is proved (§3.5), and `S <= W/2 <= N/4` is banked, so those two of
the three terms are already controlled by `N`; the open content is exactly `n`
and `T`.

### 5.3 The one identity that does bite: `(NOETHER-K)`

No family member satisfies `(NOETHER-K)` together with the campaign profile —
checked one by one for all 14 listed above, `none` in every case — and none can:
all are far from Keller. This is not an accident. Searching the *synthetic*
cluster model (driver `/tmp/nvm/forest.py`, `113544a0…`, which enumerates genuine
blow-up forests with exact adjacency and solves the whole ledger from the
non-negative integers `c_C`) over all forests with `r <= 5` and `c_C <= 4`, at
`N = 8`, returned **no** assignment satisfying `(I1)`, `(I2)`, `DEG-SPLIT`,
`(NOETHER-K)` and the campaign profile (`ceil(N/2) <= a <= N-2`, `W = N - a`,
`W >= 2S`, `mu_l >= 2`) simultaneously. Running the 40 monomial maps
`(x, x^c y^N)`, `N <= 8`, `c <= 5` through the same test: `(NOETHER-K)` + profile
is satisfiable for **none** of them.

This is a bounded negative result and I state its scope exactly: it certifies
that the easy families do not survive `(NOETHER-K)`, and that the reachable part
of the forest model (small `r`, hence small `D`) contains no solution; it does
**not** certify that no solution exists at large `D`. The obstruction to pushing
the search is structural — large `D` at fixed `N` needs `r ~ D` blow-ups (the
ladders of §5.1), which is outside exhaustive enumeration.

### 5.4 Where a ceiling can come from: one integer

`(NOETHER-K)` is the statement `sum_i a_i = 3D + Z·K_X` with

```text
        Z · K_X   =   sum_i a_i - 3D   =   -2N - kappa + n (W - S)        [Keller, H2] .
```

> **Reformulation.** `OPEN[DELTA-AFF-VS-N]` is **equivalent** to a bound on the
> single integer `Z·K_X`, the *anticanonical defect of the base cluster at
> infinity*:
> ```text
>       n  =  ( 2N + kappa + Z·K_X ) / (W - S) ,      kappa <= N ,  W - S >= 1 .
> ```
> `Z·K_X <= 0` would give `n <= 3N`, hence `delta_aff <= (3N-1)(3N-2)/2` and a
> finite `(B3)` list at every `N` — the finiteness CD §3 and DA §6.2 both want.
> The equivalence is unconditional; the *hypothesis* `Z·K_X <= 0` is not
> (see the OPEN below): it is false in the ambient class of dominant maps.

```text
 OPEN[ANTICANON-DEFECT].  For a noninvertible Keller map, is  sum_i a_i - 3D
   bounded above by a function of N (in particular, is it <= 0)?
   Bounded quantity: the integer Z·K_X = sum_i a_i - 3D, equivalently
   deg(branch divisor of Phi, with multiplicity) - 3N.
   SCOPE, stated honestly.  For GENERAL dominant maps the answer is NO: the
     engine returns  Z·K_X = -2, -2, 0, 0, +2  for psi_k o (x, x y^2), k = 2..6
     (N = 2 throughout), and  -1, +1, +1, +5, +7  for psi_k o (x, x y^3),
     k = 2..6 (N = 3 throughout).  So the defect is unbounded above at fixed N,
     and any proof of a Keller bound must use  Jac F ∈ C^*  essentially -- these
     families are exactly the n -> infinity shape, and what makes them work is
     the affine ramification term Z·R_aff, which Keller kills.
   POSITIVE data, and its limits: Z·K_X = -3 for every Keller instance computed
     -- but all of those are automorphisms, where -3 = -2N - kappa with
     N = kappa = 1 is FORCED by Noether's equation, so they are not independent
     evidence for N >= 2.  Every birational map returns -3 for the same reason.
   ALSO REFUTED, bounding the method: the neighbouring statement
     Z·(K_X + L~_red) <= 0 -- which would give the stronger n W <= 2N -- is FALSE
     even before the above: psi_4 ∘ (x,xy) gives +2, psi_3 ∘ (x,xy^2) gives +3.
   WHAT REMAINS: the question is not whether Z·K_X <= 0 in general (it is not),
     but whether the Keller hypothesis bounds it.  Any bound Z·K_X <= f(N) gives
     n <= (3N + f(N))/(W - S).
```

A consistency check worth recording. Applying the log ramification formula to
`Phi : (X, L~_red + E-bar_X) -> (P^2, L_infty + A_F-bar)` and pairing with `Z`
(which annihilates every contracted component) gives
`Z·K_X + (D - T) + a n = N(n-2)`; substituting `DEG-SPLIT` and `(NOETHER-K)`
reduces it identically to `W + a = N`, i.e. to `[P3]`. So the log route adds no
new equation — it *is* `[P3]` — which is an independent verification of both new
identities against a banked one.

## 6. Part (5): consequences

### 6.1 The floors, assembled

```text
   D_min  >=  n_min + 1                                    [CAP-STRICT]
   D_min  >=  S·n + kappa  >=  S·( ceil((N-1)/(W-S)) + 1 ) + 1     [+ MERIDIAN-FLOOR+]
   guaranteed form (S = 1, kappa = 1):   D_min >= ceil((N-1)/(W-1)) + 2
   at W = 2 (S = 1 forced):              p >= N-1,  n >= N,  D_min >= N + 1
   D_min  >=  101                                          [MOH-FLOOR, refs/ verified]
```

```text
TABLE T1.  P0 := ceil((N-1)/(W-1))  is the guaranteed floor on p; n_min >= P0+1;
           D_min >= P0+2.  Cells with a ∉ [ceil(N/2), N-2] are void.
  N |   W=2     W=3     W=4     W=5     W=6            entries:  P0 / D-floor
  4 |  3/5      --      --      --      --
  5 |  4/6      --      --      --      --
  6 |  5/7     3/5      --      --      --
  8 |  7/9     4/6     3/5      --      --
 10 |  9/11    5/7     3/5     3/5      --
 12 | 11/13    6/8     4/6     3/5     3/5
 14 | 13/15    7/9     5/7     4/6     3/5
 16 | 15/17    8/10    5/7     4/6     3/5
 20 | 19/21   10/12    7/9     5/7     4/6
```

### 6.2 The crossing, priced three ways

> **CROSSING (this lane).** The cell `(N,W)` is EMPTY as soon as one proves any
> one of
> ```text
>     p     <= C   with  C < ceil((N-1)/(W-S))          (weakest hypothesis),
>     n_min <= C   with  C < ceil((N-1)/(W-S)) + 1      (one unit weaker than DA),
>     D_min <= C   with  C < S·(ceil((N-1)/(W-S))+1) + kappa ;
>                  guaranteed:  C <= ceil((N-1)/(W-1)) + 1 .
> ```

```text
TABLE T2.  Guaranteed (S=1, kappa=1) crossing prices.
  N  W |  DA crossing (n)     this lane (n)      this lane (D_min)
   4  2 |  n_min <= 2          n_min <= 3         D_min <= 4
   5  2 |  n_min <= 3          n_min <= 4         D_min <= 5
   6  2 |  n_min <= 4          n_min <= 5         D_min <= 6
   8  2 |  n_min <= 6          n_min <= 7         D_min <= 8
   8  4 |  n_min <= 2          n_min <= 3         D_min <= 4
  11  2 |  n_min <= 9          n_min <= 10        D_min <= 11
  12  3 |  n_min <= 5          n_min <= 6         D_min <= 7
  16  2 |  n_min <= 14         n_min <= 15        D_min <= 16
  16  4 |  n_min <= 4          n_min <= 5         D_min <= 6
```

### 6.3 The cheapest crossing in the record: Moh

`MOH-FLOOR` is far above every entry of T2. Therefore:

> **COROLLARY (MOH-CROSS).** If `C(N)` is any proved bound `D_min <= C(N)` with
> `C(N) <= 100`, then geometric degree `N` is **EMPTY** — every case, `(A)`,
> `(B1)`, `(B2)`, `(B3)`, every `W`, no profile analysis needed.

Consequently a ceiling of the crude shape `C(N) = 3N` (which is what
`OPEN[ANTICANON-DEFECT]` yields for `n`, §5.4) would, if it could be carried from
`n` to `D`, close **all** of `4 <= N <= 33` outright, covering the whole `(B2)`
range `5..16` and the whole `(B3)` range `4..8` with room to spare. Carrying it
from `n` to `D` is exactly `OPEN[SAT-MASS]`. This is the single sharpest
statement of the campaign's remaining price:

```text
      (B2) at 5 <= N <= 16 and (B3) at 4 <= N <= 8 are BOTH closed by
      [ OPEN[ANTICANON-DEFECT] with any bound Z·K_X <= f(N), f(N) <= (W-S)*100 - 2N ]
      +  [ OPEN[SAT-MASS] with any bound T <= 100 - S n - kappa ] .
```

### 6.4 The `(B2)`/`(B3)` ranges under the conditional ceiling alone

Without `OPEN[SAT-MASS]`, `OPEN[ANTICANON-DEFECT]` still bounds `n`, hence
`delta_aff`, hence the `(B3)` enumeration. The `n`-window
`[ ceil((N-1)/(W-1)) + 1 , 3N/(W-1) ]` (`S = 1`, `kappa <= N`) reads

```text
  N |     W=2         W=3         W=4         W=5
  4 |  [ 4, 12]      --          --          --
  8 |  [ 8, 24]   [ 5, 12]   [ 4,  8]      --
 12 |  [12, 36]   [ 7, 18]   [ 5, 12]   [ 4,  9]
 16 |  [16, 48]   [ 9, 24]   [ 6, 16]   [ 5, 12]
```

Every window is non-empty, so the conditional ceiling alone kills no cell; what it
does is make `delta_aff <= p_a(n_max)` finite at each `(N,W)` — the input DA §6.2
needs to turn the `(B3)` list into a terminating enumeration, and the one CD §5
flagged as missing. It does **not** reach the `(B2)` thresholds (`delta_aff <= 3`,
resp. `<= 1`): those need `n <= 4`, i.e. `2N + kappa <= 4(W-S)`, impossible since
`W <= floor(N/2)`. So `(B2)` and the crossing remain different consumers, and only
the crossing (or `MOH-CROSS`) reaches `(B3)`.

## 7. FALLACY-v2 audit

* **Flag/place/series.** Six quantities kept apart: `D` (gauge), `D_min`
  (double-coset invariant), `n` (gauge), `n_min`, `p = min linear-form degree`
  (gauge, `<= n-1`), `N`. Three multiplicity functions never identified:
  `m_C = ord_C Phi^*(L_infty)` (polar, on the boundary), `a_i` (base
  multiplicities, on the cluster), `mu_l` (ramification along a dicritical).
  `D = m_{E_0}` and `s_l n = m_{C_l}` are two values of the *same* `m`, and that
  is proved (§3.2), not assumed. `kappa`, `Lambda`, `T` are three disjoint parts
  of one sum; contracted components are charged to none (`c_C = 0`).
* **Per-ray/exit-set charge.** No exit price; no `charge_basis` line. In
  `DEG-SPLIT` each component contributes `c_C` once and each base point `a_i` at
  most once (to `T`, only if `prox = 2`); the derivation is one intersection
  number computed two ways. In MERIDIAN-FLOOR+ each generator is charged once to
  `W - S = sum_{cycles}(len-1)`, not `W`; fixed points contribute nothing.
* **Carrier/attainment.** Every map in §3.6 and §5.1 is typed **REPRESENTATIVE /
  NON-KELLER**: they establish that the identities hold and that the intersection
  ledger does not bound `D`; none is claimed to be or approximate a Keller
  counterexample. CO's `(9,6,2)` curve is consumed only at CO's own REPRESENTATIVE
  typing. `MOH-FLOOR`, `CAP-STRICT`, `MERIDIAN-FLOOR+` are floors and used only
  as floors.
* **Floor/attainment.** Every kill in §6 is conditional ("EMPTY as soon as one
  proves ..."), with the missing input named and typed. `Z·K_X <= 0` is typed OPEN, never
  asserted, and §5.4 records that it is outright FALSE in the ambient dominant
  class (defect up to +7) and that the only Keller data confirming it are
  automorphisms, where the value `-3` is forced by Noether and is therefore not
  independent evidence; its log cousin is REFUTED with two witnesses.
* **Pole/interior.** `m_{E_0} = D` uses that all base points lie on `L_infty`
  (`F` is a morphism on `A^2`); `prox(j) ∈ {1,2}` uses SNC, preserved under
  blow-up. `PROP DN` uses `l' ≅ A^1`, an Orevkov input, stated with that
  hypothesis visible. The Zariski-van Kampen step of §4.2 uses monicity in `y`,
  which is *derived* from the parametrisation, not assumed.
* **Variable/ring map.** The engine declares its charts `(s,t) -> (s, st)` and
  `(s,t) -> (s't', t')`, divides by the exact order of vanishing at the origin,
  works over `Q`, and de-duplicates the chart overlap by an explicit `1/t`
  identification; the Picard basis is `(H, E_1..E_r)` with the declared form.
  Controls: `D^2 - sum a_i^2` reproduced the known geometric degree of all 41
  maps; three clusters were reproduced by hand; the independent synthetic
  evaluator reproduces the engine on all three. A negative control — the predicate
  "every `m_C = 0` component is a dicritical" — FAILED on `(x, x^2 y)`, exposing a
  component contracted to an **affine** point, which my first reading of
  `Phi^{-1}(A^2)` had wrongly excluded; §3.1 is the repaired statement and
  `DEG-SPLIT` is unaffected.
* **Prime label / derivative; `sat()` / raw remainder.** `l'` is a label (the
  affine part of `l`), never a derivative; `P^~, Q^~` are leading forms; the only
  derivatives are inside `Jac`. No saturation, no Groebner basis, no quotient
  normal form — only substitution, exact monomial division, and `gcd`.
* **Merge-free / target index.** In MERIDIAN-FLOOR+ the merge count is per
  generator and per cycle, and the transitivity target (`N` blocks to `1`) is kept
  distinct from the support size `W` and the cycle count `S`.
* **Not filled by cap or analogy.** Three typed OPENs are raised rather than
  guessed; Jelonek and Abhyankar-Moh are marked ABSENT; DA's theorems are flagged
  as PROPOSALS wherever consumed, and its MERIDIAN-FLOOR is re-derived, not quoted.

## 8. Typed verdict block

```text
LANE       N-VS-MAPDEG
SCOPE      Keller, noninvertible.  §§2-3, §5 use no case split and no H2 except
           where marked; §3.2, §4, §6 use H2.  Quasi-homogeneity never used.
           Case (A), Z(G)=1 and the A2 cells not consumed.

PROVED HERE  (all PROVED-HERE, UNREVIEWED)
  D_min          both Aut factors required; right composition fixes A_F, (d,e),
                 R_0 (Chau 2004) and moves only K:  D_min = min_psi[max(d,e)K_min].
  NEG-GEN        (x, x^c y^N) is dominant of geometric degree N with n_min = 1 and
                 D_min >= (c+N+1)/2: the general-dominant form of the question is
                 FALSE, and the datum spent is deg Jac.
  (I1)-(I6)      m_{E_0} = D;  N = sum_{C->L_inf} m_C k_C (so kappa <= N); the
                 harmonic relations; e_C = m_C; the boundary components are a
                 Z-basis of Pic X, so det = (-1)^r for EVERY compactification of
                 A^2 -- an identity, blind to forks and to chain length.
  PROP DN        a dicritical has exactly one boundary neighbour with m > 0, and
                 s_l n = m_{C_l}: D and n are two values of one function.
  DEG-SPLIT      D = sum_l s_l·deg(closure Phi(l)) + kappa + T  (all dominant F).
  CAP-STRICT     deg A_F-bar <= D - kappa - T <= D - 1; D_min >= n_min + 1;
                 in Chau parameters K >= S m + 1 >= m + 1.
  NOETHER-K      sum a_i = 3D - 2N - kappa + n(W-S), sum a_i^2 = D^2 - N; at S = 0
                 this is Noether's equation sum a_i = 3D - 3.
  NO-CEILING     no intersection-theoretic boundary instrument can bound D at
                 fixed N (Hodge index gives only D >= sqrt(N); the nef hyperboloid
                 Z^2 = N is unbounded in Z·H).
  MERIDIAN-FLOOR+  p(W-S) >= N-1 with p <= n-1, so n >= ceil((N-1)/(W-S)) + 1;
                 at W = 2:  p >= N-1, n >= N, D_min >= N+1.
  MOH-FLOOR      D_min >= 101   [Moh 1983, verified in refs/ this session].
  Z·K_X          n(W-S) = 2N + kappa + Z·K_X, Z·K_X = sum a_i - 3D: the upper half
                 of the question is ONE integer.
  log-check      the log ramification formula on (X, L~+E-bar) reduces identically
                 to [P3], N = a + W  (independent control).

CORRECTED /  * DA's MERIDIAN-FLOOR sharpened by one unit (p, not n); the sharpened
SHARPENED      form re-derives CD §5's independent n >= 4 at N = 4.
             * Chau's cap is never attained: deg A_F-bar <= D - 1.  The (9,6) row
               therefore admits no degree-9 component at all -- CD item 4 /
               CLAIM [D] strengthened, not contradicted, and consistent with CO's
               REPRESENTATIVE typing of (9,6,2).
             * Chau 1999 Thm B bounds only the reduced shape (d,e); Thm C is
               homogeneous in K.  The literature bounds the half of the degree
               that is not the obstruction.
             * Z·(K_X + L~_red) <= 0 is FALSE (two witnesses), and Z·K_X <= 0 is
               FALSE for general dominant maps (two families, defect up to +7):
               the log version of the anticanonical route is refuted outright and
               the canonical one survives only as a Keller-specific question.
             * A boundary component CAN be contracted to an affine point (witness
               (x, x^2 y)); repaired in §3.1.

MEASURED     41 distinct dominant maps resolved exactly over Q (D <= 24, N <= 50,
             r <= 15): all satisfy (I1),(I2),(D1),DEG-SPLIT, m_C >= 0, c_C >= 0
             -- 0 failures.  6 Keller instances satisfy NOETHER-K with
             sum a_i - 3D = -3 exactly.  Families at fixed N with D -> infinity
             and with n -> infinity, including two in which the anticanonical
             defect sum a_i - 3D turns POSITIVE (up to +7 at N = 3).  Forest
             model: all blow-up forests r <= 5, c_C <= 4 at N = 8 -- no solution
             of the FULL Keller ledger; 40 monomial maps -- none satisfies
             NOETHER-K + profile.

NOT CLAIMED  any kill of any (N,W) cell; any upper bound on D_min, n_min,
             delta_aff or T; that Z·K_X <= 0; that any exhibited map is or
             approximates a Keller counterexample; anything about case (A), the A2
             cells, Z(G), or the reducible branch.

OPENS RAISED OPEN[ANTICANON-DEFECT]  is sum_i a_i - 3D = Z·K_X bounded above in
               N for a noninvertible Keller map (in particular <= 0)?  Bounded
               quantity: the integer Z·K_X = deg(branch divisor of Phi, with
               multiplicity) - 3N.  Payoff, exact: n = (2N + kappa + Z·K_X)/(W-S),
               so any bound Z·K_X <= f(N) closes OPEN[DELTA-AFF-VS-N].
               SCOPE: FALSE in the ambient dominant class (psi_k o (x,xy^3)
               reaches +7 at N = 3), so a proof must use Jac F ∈ C^* essentially;
               the only Keller data are automorphisms, where -3 is forced by
               Noether and is therefore not independent evidence for N >= 2.
             OPEN[SAT-MASS]  is T = D - S n - kappa bounded in N for a
               degree-minimal representative?  Bounded quantity: T ∈ Z_{>=0}; it is
               the Jung-van der Kulk word length seen on the boundary.
OPENS        OPEN[N-VS-MAPDEG] (upper half) = OPEN[DELTA-AFF-VS-N] ∧
RETYPED      OPEN[SAT-MASS]; its raw form stays FALSE and its general-dominant
             form is now FALSE WITH A WITNESS (NEG-GEN).  Lower half strengthened
             from DA's max(deg P,deg Q) >= ceil((N-1)/(W-1)) to
             D_min >= ceil((N-1)/(W-1)) + 2, and to D_min >= 101 from Moh.

SUCCESSOR    ANTICANON.  Decide sum_i a_i <= 3D for Keller maps: one inequality
             about the base cluster at infinity, exactly equivalent to the
             campaign's missing ceiling on delta_aff.  The lane has mapped its
             boundary: FALSE without Keller, FALSE in its log form, and the only
             Keller data (automorphisms) are degenerate.  No new machinery:
             (NOETHER-K), (D1), DEG-SPLIT and the proximity inequalities are in
             hand.  Cheapest instruments: (i) run the engine along a family of
             non-Keller pairs whose Jacobian degree is driven down to 0 and watch
             where Z·K_X crosses; (ii) ask whether Z·R_aff = 0 alone forces
             Z·K_X <= f(N), which is a question about the base cluster of a pencil
             with no affine critical points -- finite at each r.

DEVIATIONS   (1) Item (4) asked for a family satisfying EVERY banked constraint.  I
                 built families satisfying the whole intersection ledger and PROVED
                 (NO-CEILING) that no instrument of that kind can bound D, but none
                 satisfying (NOETHER-K); §5.3 states the scope of that negative
                 exactly and §5.4 converts it into the successor.
             (2) MERIDIAN-FLOOR+ and MOH-FLOOR were not on the charged instrument
                 list; the first sharpens a charged theorem, the second is the
                 cheapest crossing in the record.
             (3) Report length ~52 KB, above the charged 25-40 KB target.  The
                 overrun is the §3 identity package with its proofs and the §3.6
                 machine table, both of which the charge's items (2) and (4)
                 require; tables T1-T3 were already thinned.
             (4) Desk CAS: wall time under 11 minutes, peak memory under 300 MB.
                 Drivers in /tmp/nvm (blowup.py, ident.py, synth.py, forest.py,
                 family.py, ram.py, zk.py, noether.py, tables.py), not installed
                 in box/.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `52339`.
- Body SHA-256:
  `c86d144fbe7a8af88ab263e060723d28d2213154576880158dbb548f7557870f`.
- Frozen basis: `c463a7cf7d51ae514ced606c3de5049b3d8d07f7`.
