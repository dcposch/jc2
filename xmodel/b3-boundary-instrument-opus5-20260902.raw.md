# B3-BOUNDARY-INSTRUMENT — the Domrina–Orevkov package at general `N`, fed by the affine cage

Lane: `B3-BOUNDARY-INSTRUMENT`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact integer/symbolic algebra (python 3, sympy 1.14, rationals
only). No Groebner, no AWS, no literature fetched, no web, no `jc2-lean`, no
canonical-ledger edit. Drivers in `/tmp/b3bi`, not installed in `box/`.

## 0. Custody, scope, method, and a notation warning

The six charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all six match the charge exactly:

```text
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  b3-e-geometry-opus5-20260902.md
12dea79fc65d31dd5ac2dac9fa3faff638cd1d5a12b7c6f72a7f18658b09ba4a  b3-e-geometry-review-grok46-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
717134c733adc17b3b70409b018858fb1311c37608a24f0eebe65ae79aec8b11  ideation-20260902T0741Z-sol56.md
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  do1-mu2-replay-sol56-20260901.md
```

Below: **BE** = B3-E-GEOMETRY, **BR** = its grok-4.6 hostile review, **HF** =
HORN-FLAGSHIP, **MI** = MPRIME-ALLN-H2, **DR** = the charged DO I `mu=2` replay,
**SOL** = Sol's 0741Z ideation (cited as PROPOSAL only; Card 2 is consumed as a
*task*, not as a result).

**Consumed at BR's CONFIRMED typing, with BR's binding repairs in force:**
`E-ETALE`; `E-BMY-VACUITY` (log-smooth repair); `PROP 3.1`/`LOC-1`; `COR 3.2`
(with `g = p_a(E~-bar)`); `E-CHARGE` (with the **contracted-model** repair and
the place/branch dictionary explicit); `B3-E-GENUS`; `B3-E-NOCROSS`; BE §6's
identification of the `N=4` object as `(mu,corr) = (2,1)` and its
non-uniformity. **At HR's CONFIRMED typing:** HF `B3-DEGREE`, `B3-CAGE`,
`B3-LOC`, `B3-PUSHOFF`, `B3-COMPONENT`, Props 3.1/3.2, `B3-N4`, `SCOPE[B3-QH]`.
**As MI states them:** Lemma A, Lemma 4.1 and `(L)`, `(K)`, `(C1)`–`(C3)`,
control 2, 7.B', `N4-PIN`, `THEOREM PROFILE`, `j <= a`, MI's statement of
Orevkov Lemmas 2.1 and 3.1. **From DR only through the charged replay's
assembly, its repairs binding:** Definition 3, formula (9), `(4.3)`, Prop 3,
Lemmas 1–5, the edge formula `(4.7)`, Prop 4 (§4.1), Lemma 7 (§4.2), Lemma 6,
Lemmas 8–9, Corollaries 4–5 (§6), Lemmas 10–15 (§7).

**Not consumed:** `Z(G) = 1`; case (A) and `CUSP-A-VOID`; any `A2` cell; the
`E_0` quintic (never used below); any value of `deg E-bar`, `deg A_F-bar` or
`kappa-bar`; `(B2)` beta-forced rows.

**No `charge_basis` line: this report asserts no new exit price.**

**Notation warning (FALLACY-v2, variable/ring map).** DO I writes `a` for a
*target boundary vertex* and `a~` for a source component over it; the campaign
writes `a` for `deg(E° -> A_F°)`. These are different objects and the collision
is fatal if left standing. **Throughout this report the DO target vertex is `v`,
its fibre set `v'`, a source component over it `v~`, and its three branch
directions `L_v, R_v, D_v`.** The letter `a` always means the campaign's affine
sheet count. `l` (or `g~`) is a dicritical, `l' = l ∩ Phi^{-1}(A^2)`;
`p̃_l := l \ l'`; `p := Phi(p̃_l) = A_F-bar ∩ L` (MI Lemma A: a single point);
`v_0` is the component of `L` through `p`. `Ē_X` is the closure of `E` in the
source model. `E~-bar` is the smooth model of `E`; **places of `E` at infinity**
are points of `E~-bar \ E~` and are kept apart from points of `Ē_X ∩ L̃` until
the dictionary of §2.1 is invoked.

## 1. Verdict, up front

```text
INSTRUMENT BUILT.  NO KILL.  No EMPTY window in N.  Three new degree-free
bridges, two controls PASSED, one route closed NEGATIVE, one GAP-CANDIDATE.

(1) EXTRACTION (§2).  The whole DO determinant/transfer apparatus (Lemmas 1-5,
    Prop 3, edge formula, Prop 4, Lemma 7) is degree-free, and its one profile
    hypothesis -- A_F-bar meets L in a SINGLE point -- is supplied at EVERY N by
    MI Lemma A under H2.  sum Deg v~ = N stays an EQUALITY at every N and,
    applied to the target CURVE g = A_F-bar rather than to a boundary vertex, it
    IS the campaign's [P3]: N = a + W, dicriticals the n>=2 part, Ē_X the n=1
    part (THEOREM BI-1).  First contact between the two ledgers.

(2) SUBSTITUTION (§3).  BI-2: n(v~_y) = e_y at each mark over p -- the
    transverse degree of the carrying vertex IS the ramification index of that
    place of E over ∞_{A_F}.  BI-3: the local-degree ledger of F over p is
    exactly (s_l mu_l)_l and (e_y)_y, summing to W + a = N.  BI-5: the marks
    SATURATE the non-dicritical Deg over v_0.  BI-4 places the affine excess:
    the branches of Ē_X at the t in l' over p total r_p[(r_p-1)W + K_p], at most
    K_p of it charged to the k_t.

(3) CONTROL 1, N=4 (§4).  PASSES.  Reproduces (mu,corr) = (2,1); with Cor 4 pins
    v_0 to Deg 2+1+1, IDENTIFYING DO's "the other two sheets" (DR:534) as the
    two places of E at infinity over ∞_{A_F}; replaces DO's entry seam by
    N4-PIN; re-derives the assembly depth.  Does NOT shorten the census: 35 rows
    and six graphs untouched, the kill still the SET §§2-7.  Reason: the census
    is indexed by target vertices, the ledger by g and Sing A_F; they share
    only v_0.

(4) CONTROL 2, Sol's Gamma (§5.1-5.2).  PASSES on every requested item, and
    imports neither smoothness of E nor chi(E) = 1.

(5) N=5, N=6 (§5.3).  All (B3) profiles run.  NO EMPTY WINDOW.  Sole
    non-generic cell (N=6, a=4, three cusps + node) is forced to p_a <= -1,
    hence j >= 2 -- a constraint, not a kill; BI-7 proves the route can never
    kill.  Residual: two named data plus one GAP-CANDIDATE.

(6) UNIFORMITY (§6).  Census(N) = sum_m floor(N/m) Rows(m),
    Rows(m) = [z^{m+2}] f_m(z)^3;  Census(4) = 35, reproducing DO exactly, then
    86, 287, 717, ..., 405434 at N = 14.  The affine data does NOT bound it.  It
    DOES bound the assembly depth: #forks on a spine <= N - s_l mu_l = a for one
    dicritical -- exactly the two merges DO needs at N = 4.  K_p and the fibre
    partitions bound neither.
```

## 2. Task (1): the degree-free DO package at general `N`

### 2.1 The dictionary, stated once

DO I Definition 3 attaches to a source component `c~` dominating an irreducible
target curve `C`:

```text
  n(c~) = ord_{c~} F^*(C)   (transverse degree),
  m(c~) = deg( F|_{c~} : c~ -> C ),      Deg c~ = m(c~) n(c~).
```

`DR:48-60` fixes the dictionary against the campaign: for a dicritical `l`,
`n(l) = mu_l` and `m(l) = s_l`, so `Deg l = s_l mu_l`. Two further entries are
forced and are used throughout:

```text
 (D1)  Ē_X-components.  E = F^*(A_F) is REDUCED (F etale, Keller), so every
       component of Ē_X has n = 1 and m = its degree over A_F-bar; the m's sum
       to a = deg(E -> A_F).
 (D2)  p̃_l.  l \ l' = (F|_l)^{-1}(p) is a SINGLE point (Orevkov Lemma 2.1 as
       MI states it: l' ≅ A^1), so F|_l is totally ramified there and the
       local index of F|_l at p̃_l is exactly s_l.
```

### 2.2 What stays true at every `N`

The following are the ingredients DR uses, each with its exact hypothesis and
its `N`-loading marked. `[DF]` = degree-free, `[N]` = carries `N`.

```text
 DF-1 [DF]  Definition 3 and Deg = m n.                          DR:44-52
 DF-2 [N ]  Generic-sheet identity  sum_{c~ over C} Deg c~ = N, for EVERY
            irreducible target curve C, boundary or not.  An EQUALITY at every
            N; only the VALUE is N.                              DR:205-211
 DF-3 [DF]  Fork RH.  For a fork c~ ≅ P^1 over a vertex v of valence r, with
            k_i points over the i-th direction: sum_i k_i = (r-2)m + 2; and
            source valence = target valence <=> m = 1 <=> every incident chain
            has Deg = m n.  At r = 3 this is DR (4.3): sum_j e_{X,j} = m per
            direction, sum_{X,j}(e_{X,j}-1) = 2(m-1), r_L+r_R+r_D = m+2.
                                                                 DR:213-229, 277-289
 DF-4 [DF]  Lemma 5 transfer.  det Q/det B = n(c~)/Deg Q = 1/e (one contact,
            far endpoint an end); = n(c~)n(b~)/Deg Q (two).      DR:231-243
 DF-5 [DF]  Lemma 7 conservation  sum_{c~ ∈ c' ∩ br_{a~}(b~)} Deg c~ >= q.
            A LOWER bound, never an attainment.                  DR:291-306
 DF-6 [DF]  Prop 3: det R_v = 1, det D_v > 1, det L_v > 1, det L = -1, target
            branch determinants pairwise coprime.                DR:245-259
 DF-7 [DF]  Lemmas 2-4: branch determinants at a vertex are coprime; away from
            the root all non-root branches but at most one are unit; a subgraph
            excluding the root has positive determinant.         DR:266-270
 DF-8 [DF]  Edge formula (4.7) and K~ = F^*K + B, B boundary-supported BECAUSE
            F is etale on A^2 (Keller), coefficient mu_l - 1 at a dicritical.
                                                                 DR:261-264, 623-631
```

**The one profile hypothesis, and why it is available at every `N`.** DF-6 is
not general position: Prop 3's configuration presupposes that `g = A_F-bar`
meets `L` in a **single** point `p`, on a single vertex `v_0` with a
distinguished terminal (`R_v`) direction — i.e. *"`A_F` has one place at
infinity"*. DO has it at `N = 4` from the low-degree analysis; the campaign has
it **at every `N` under `H2`**, as MI **Lemma A** (`A_F~ ≅ A^1`), which BE and
BR both consume at CONFIRMED typing.

```text
 EXTRACTION-1.  Under H2 the ENTIRE target-side determinant package DF-4/6/7/8
 is available at every N.  The N-dependence of the Domrina-Orevkov argument is
 concentrated in DF-2 alone.
```

**The census identity in the form that stays true.** DF-2 is an equality for
*any* irreducible target curve: over a generic point of `C` the `N` sheets
distribute as `sum m(c~) n(c~)`, contracted components contributing nothing.
DO applies it at boundary vertices; the new move is to apply it at `g`.

> **THEOREM BI-1 (the census identity at `g`; all `N`, `H2`).** Apply DF-2 to
> the target curve `C = g = A_F-bar`. The components of `F^{-1}(g)` dominating
> `g` split by `n`:
> ```text
>    n >= 2 :  the dicriticals l,  Deg l = s_l mu_l ;
>    n  = 1 :  the components of Ē_X,  Deg = m = degree over A_F-bar.
> ```
> Hence
> ```text
>     sum_l s_l mu_l  +  a   =   N ,        i.e.   W + a = N .
> ```
> *Proof.* `n(c~) >= 2` iff `c~` is a component of `Phi^*(A_F-bar)` with
> multiplicity `>= 2`; `E = F^*A_F` is reduced (D1), so the multiplicity-one
> part is exactly `Ē_X` and the rest are the dicriticals, whose `n` is `mu_l`
> and whose `mu_l >= 2` by 7.B'. Summing `m` over `Ē_X` gives `a` by
> definition of `a`. DF-2 gives the total `N`. ∎

`W + a = N` is MI `[P3]`. So **DO's generic-sheet identity, evaluated on
`A_F-bar` instead of on a boundary vertex, IS `[P3]`** — a three-route agreement
(DO formula (9), MI Lemma 4.1 at a smooth point, Orevkov's budget) and a
positive control on the dictionary. It also makes `E` a participant in DO's
bookkeeping, which it was not before: `E` is the `n = 1` half of `F^{-1}(g)`.

*Sanity control (MEASURED).* In the explicit resolved model of §3.4 (a `(1,2)`
dicritical, `N = 2`), `W = 1*2 = 2`, `a = 0` because `E = {x=0}` is contracted
and does not dominate `A_F`; `W + a = 2 = N` ✓.

### 2.3 Where `N` actually enters

DF-2 gives the fork list `{(m,n) : m >= 2, n >= 1, mn <= N}` and thence the
local census. Its exact size is computable (§6). At `N = 4` the list is
`(2;2,1), (3;3,1), (4;4,1), (4;2,2)` — DR (4.2) — and the raw row count is 35 —
DR (5.1). Both are reproduced by the closed form of §6, which is the positive
control on the growth analysis.

## 3. Task (2): feeding the package the affine ledger

### 3.1 The marks, and the transverse-degree dictionary

BE Prop 3.1 (BR CONFIRMED): over the puncture at infinity of `A_F` the whole
degree `a` of `E~-bar -> P^1` is carried by places of `E` at infinity. In the
contracted model those places converge to points of `L̃`: the **marks over `p`**.
Standing local resolution conventions: `(R1)` `p` is a smooth point of `L` and
`g` is transverse to `L` there; `(R2)` `Ē_X + L̃` is SNC, so a mark is a
transverse crossing of `Ē_X` with one boundary component at a smooth point.

> **THEOREM BI-2 (mark dictionary; all `N`).** Let `y` be a mark over `p`, on
> the boundary component `v~_y`. Then `F(v~_y) = v_0` and
> ```text
>            n(v~_y)  =  e_y ,
> ```
> where `e_y` is the ramification index of `E~-bar -> A_F~-bar = P^1` at the
> place `y` over the infinity puncture. In particular
> `sum_{marks over p} e_y = a`, and a mark can lie only on a boundary component
> whose transverse degree equals its own index.
>
> *Proof.* Local coordinates `(u,w)` at `y` with `v~_y = {u=0}`, `Ē_X = {w=0}`;
> coordinates `(U,W)` at `p` with `v_0 = {U=0}`, `g = {W=0}`. `F(Ē_X) = g` gives
> `F^*U|_{w=0} ≢ 0`, and near `y` the only curves in `F^{-1}(v_0)` are boundary
> components (a curve of the source `A^2` cannot map into `L`), so by `(R2)`
> `F^*U = u^{a_1}·unit` with `a_1 = ord_{v~_y}F^*(v_0) = n(v~_y)`. Restricting
> to `Ē_X = {w=0}`, `F|_{Ē_X}` reads `u |-> U = u^{a_1}·unit` in the coordinate
> `U` along `g`, so its local index at `y` is `a_1`. Since `g` is smooth at `p`
> by `(R1)`, that index is the ramification index of the normalised map, i.e.
> `e_y`. Summing over marks gives `a` by BE Prop 3.1. ∎

This is the dictionary BR asked for and BE did not state: it converts a
curve-side invariant of `E` (a ramification index over `∞_{A_F}`) into a
graph-side label (a transverse degree), and is why the marks are consumable.

### 3.2 The fibre-at-`p` budget

> **THEOREM BI-3 (fibre-at-`p` budget; all `N`, under `(H-∞)`).** Write
> `(H-∞)` for: *no contracted component of `L̃` maps to `p`*. Under `(H-∞)`,
> `F^{-1}(p)` is finite and its local-degree ledger is
> ```text
>    at p̃_l  (one per dicritical) :  deg_{p̃_l} F  =  s_l mu_l ,
>    at each mark y over p        :  deg_y F      =  e_y ,
>    total                        :  W + a = N   (BI-1).
> ```
> Hence the points of `L̃` over `p` are exactly the `m` attaching points and the
> marks, and nothing else.
>
> *Proof.* Under `(H-∞)` every point of `F^{-1}(p)` is an isolated point of the
> fibre and `sum_{z ∈ F^{-1}(p)} deg_z F = N`. At `p̃_l`, `(R1)`+`(D2)` make `F`
> monomial: `F^*U = u^{a_1}·unit` with `a_1` the index of `F|_l` at `p̃_l`,
> which is `s_l` by `(D2)`; `F^*W = w^{b_2}·unit` with
> `b_2 = ord_l F^*(g) = mu_l`. Local degree `= a_1 b_2 = s_l mu_l`. At a mark,
> the same computation with `b_2 = ord_{Ē_X}F^*(g) = 1` and `a_1 = e_y` (BI-2)
> gives `e_y`. The two families already sum to `N` by BI-1, so there is no
> room for a third. ∎

*MEASURED positive control on the local degree.* Resolve
`F(x,y) = (x, x y^2)` (degree 2, one dicritical) by three blowups at `[0:1:0]`.
In the chart `(X_2, Z')` one gets, in target coordinates `U' = u/v`, `V' = 1/v`
at `p`,
```text
  U' = X_2^2 Z'^2 ,   V' = Z' ;   g~ = {X_2 = 0} dominates g = {U'=0} ;
  exponent matrix [[2,2],[0,1]], det = 2 = s*mu = 1*2 = deg_{p̃} F .
```
(driver `/tmp/b3bi/attach.py`). The local degree at `p̃` is exactly `s_l mu_l`,
as BI-3 asserts. **The same computation also shows the component the dicritical
physically meets is CONTRACTED there** — see the GAP-CANDIDATE in §3.5.

`(H-∞)` **holds at `N = 4`**: `N4-PIN` gives `K_tot = 1`, concentrated at the
cusp, so the unique contracted tail of the unique chain (Orevkov Lemma 2.1 as MI
states it, one tail per dicritical) sits at the affine point `t` over the cusp,
where `mu_t = e_t mu_l + k_t = 3 > mu_l`, and not at `p̃`. For `N >= 5` it is
**not** derived here:

```text
 OPEN[BI-TAIL-AT-INFINITY].  Whether a contracted component of L̃ can map to
 p = A_F-bar ∩ L at N >= 5.  If it can, BI-3 and BI-5 degrade from equalities
 to inequalities (the marks then account for at most a, not exactly a, of the
 non-dicritical Deg over v_0) and every §5 conclusion weakens accordingly.
 This is one of the two data the boundary side still lacks.
```

### 3.3 Where the affine excess sits: `E-CHARGE` transported

`E-CHARGE` (BE §3.2, BR CONFIRMED **with the contracted-model repair**, binding
here: `Phi` is finite of degree `mu_t` at `t ∈ l'` only after contraction)
places the affine half. With BE Prop 3.1 it gives the per-point statement.

> **PROPOSITION BI-4 (charged vs branch-exchanged, all `N`).** Fix
> `p ∈ Sing A_F` with `r_p` branches, and let `T_p := ∪_l h_l^{-1}(eta^{-1}(p))`
> be the points of the dicriticals over `p`. Then, in the contracted model:
> ```text
>   sum_{t ∈ T_p}  sum_{branches Gamma of Ē_X at t}  deg(Phi|_Gamma)
>          =  r_p ( a - a_p )  =  r_p [ (r_p-1) W + K_p ] ,
>   of which  <=  K_p = sum_{t ∈ T_p} k_t  is SAME-BRANCH (Phi(Gamma) = b(t)),
>   the remainder being BRANCH-EXCHANGED.
> ```
> At a unibranch `p` (`r_p = 1`) there is no exchange and the inequality is an
> equality: `K_p = a - a_p` is carried entirely, and only, by the same-branch
> branches. At a `p` with `K_p = 0` every branch of `Ē_X` at every `t ∈ T_p` is
> exchanged.
>
> *Proof.* Each of the `r_p` punctures `P_b` of `A_F~-bar` over `p` carries, by
> BE Prop 3.1, places of `E` at infinity of total degree `a - a_p`; the `r_p`
> puncture-fibres are disjoint, giving `r_p(a - a_p)` in total; in the
> contracted model each such place converges to a point of `T_p` and is a branch
> `Gamma` of `Ē_X` there with `deg(Phi|_Gamma)` its degree over `A_F-bar`. The
> same-branch bound is `E-CHARGE` summed over `t ∈ T_p`. ∎

So the answer to *"which vertices of the graph carry which excess"* is:

```text
  the boundary vertex v_0             carries the a marks, with transverse
                                      degrees n(v~_y) = e_y  (BI-2, BI-3);
  the dicritical vertex l itself      carries, at its AFFINE points t, all the
                                      other places of E at infinity, as MARKS
                                      ON AN EXISTING VERTEX, split by BI-4 into
                                      K_p charged and r_p(a-a_p) - K_p exchanged.
```

BR's objection to BE's successor — *"a curve meeting the boundary at points of
`l` adds marked points on an existing vertex; no identity consumes them"* — is
answered for the marks over `p` and **only** for those: the consuming identity
is BI-3 (`N = W + a` read as a fibre budget) and the consuming label is
`n(v~_y) = e_y`. The marks on `l'` remain marks on an existing vertex; BI-4
gives them a **budget**, not a determinant identity.

### 3.4 Saturation, and the determinants of the resulting branches

> **THEOREM BI-5 (mark saturation; all `N`, under `(H-∞)` and `(R1)`,`(R2)`).**
> Let `v~ ∈ v_0'` be a component of `L̃_∞` over `v_0` which is not a
> dicritical-incident block. Then **every** one of the `m(v~)` points of `v~`
> over `p` is a mark, `F|_{v~}` is unramified over `p`, and each of those marks
> has index `e_y = n(v~)`. Consequently the ramification profile of
> `E~-bar -> P^1` over the infinity puncture is exactly the multiset
> ```text
>          { n(v~) repeated m(v~) times :  v~ ∈ v_0' non-dicritical } ,
> ```
> a partition of `a`.
>
> *Proof.* By DF-2 at `v_0`, `sum_{v~ ∈ v_0'} Deg v~ = N`; the dicritical blocks
> contribute `sum_l s_l mu_l = W` (DF-2 at `g` is BI-1; the block incident to
> `l` carries `Deg = s_l mu_l`, DR Lemma 6 / Prop 1), so the non-dicritical
> components carry `sum Deg v~ = N - W = a`. Each `v~` has at most `m(v~)`
> points over `p`; writing `c_{v~}` for the number that are marks and using
> BI-2, `sum_{v~} c_{v~} n(v~) = a` by BI-3 and `(H-∞)`. Since
> `c_{v~} <= m(v~)` and `sum_{v~} m(v~) n(v~) = a`, every inequality is an
> equality: `c_{v~} = m(v~)` for all `v~`. ∎

**Determinants of the resulting branches.** Feed BI-5 into DF-4 and DF-7.

> **COROLLARY BI-6 (the coprimality load carried by `E`).** A mark-carrying
> component with `Deg = 1` (a *unit lift*, `m = n = 1`) has transfer factor
> `n/Deg = 1`, so by DF-4 its source branch determinants **equal** the
> corresponding target branch determinants. Hence two unit lifts of `E` may
> merge at a source fork only over a target branch of determinant `1`: over a
> branch with `det B > 1` they would present two equal non-unit branch
> determinants at one source vertex, contradicting DF-7 (Lemma 2). With DF-6
> (`det R_{v_0} = 1`, `det D_{v_0} > 1`, `det L_{v_0} > 1`) the merges of
> `E`-unit-lifts are confined to the `R`-side.

This is the mechanism DR uses over and over ("*repeats a non-unit determinant
and fails coprimality*", DR:379, 391, 448) — and BI-6 says what it is *about*:
**the coprimality kills in DO I are kills of the multiplicity of `E`'s sheets.**
That is the first structural statement linking the two halves BE §6 called
disjoint.

### 3.5 A GAP-CANDIDATE raised against the block the campaign would lean on

The instrument uses only `Deg B_l = s_l mu_l`. The `(m,n)` **split** of that
block is *not* determined by the frozen replay, and my independent local
computation disagrees with the reading DR's §6 assembly presupposes:

```text
 Local computation at p̃_l (coordinates as in BI-3, assuming p̃_l is a
 transverse crossing of l with a single component B_l of L̃_∞ and F is monomial
 there):   n(B_l) = ord_{B_l} F^*(v_0) = a_1 = index of F|_l at p̃_l = s_l ,
           m(B_l) >= b_2 = mu_l ,     so   (m,n)(B_l) = (mu_l, s_l).
 DR's §6 assembly instead treats the object incident to g~ at N=4 as a
 CONSTANT block, i.e. m = 1, n = 2, i.e. (m,n) = (s_l, mu_l): the TRANSPOSE.
 Both give Deg = s_l mu_l = 2.  They differ on whether that object is a FORK.
```

If `(m,n)(B_l) = (mu_l, s_l)` and `mu_l >= 2` (always, 7.B'), then `B_l` is a
fork of degree `s_l mu_l`; at `N = 4` that is a **degree-two fork**, which DR's
Corollary 4 excludes — a one-line kill, which the length of DO I refutes. The
resolution is visible in the MEASURED model of §3.2: **there, the component the
dicritical meets at `p̃` is CONTRACTED**, so `B_l` is not the physically adjacent
component and DR's Prop 1 transfers across a contracted tail. Hence:

```text
 GAP-CANDIDATE[BI-ATTACH].  The (m,n) split at the dicritical-incident vertex
 is not fixed by the frozen replay, and the naive identification "B_l = the
 L̃_∞-component that l meets" is NOT licensed: an explicit resolved model has l
 meeting a contracted component at p̃.  ONLY Deg B_l = s_l mu_l is safely
 consumable.  Any general-N successor that wants to invoke Corollary 4 ("no
 degree-two fork") must settle the split first.
 Consequence for this lane: NONE of BI-1..BI-6 uses the split; §4 flags the one
 place (the Cor-4 step) where it would matter.
```

## 4. Control 1 (mandatory): `N = 4`, the `(mu, corr) = (2,1)` kill

BE §6 and BR §8 (both CONFIRMED) place the `(B3)` `N = 4` object at Orevkov's
one-dicritical profile `(mu,corr) = (2,1)`, DO I's `n(g~) = 2, m(g~) = 1`.
Substituting the affine data:

**(a) The entry seam is replaced.** DR §3 obtains `(m,n) = (1,2)` from Orevkov
`[3, Lemma 4.2]` plus an RH argument that `m = 1` (`DR:171-181`). The campaign
gets the same tuple from `(C1)`+`(K)`+7.B' alone: `2a >= N`, `a <= N-2` force
`a = W = 2`, and `W = 2 = sum s_l mu_l` with `mu_l >= 2` forces the single
dicritical `(1,2)` — `N4-PIN`. Two independent routes, one answer; **the affine
data supplies DO's entry without DO's Lemma-4.2 citation.**

**(b) Which lemma fires — the answer is unchanged, and it is a SET.** With the
affine data in place the elimination is still DR §§5–7: local census Lemmas 8–9
→ six global graphs (DR §6, REPAIRED) → Lemmas 10–15, terminating at exactly
three displays,
```text
   Figs 24-25 : (7.3)   -2 d_2 = 18 delta^2 - 2 d_2 - 6 y delta^2  vs  y > 4 ;
   Figs 22-23 : (7.6)   odd  -1 = even ;
   Figs 20-21 : (7.10)  -1 = -B - alpha C <= -4 .
```
None of the three consumes an affine quantity. **No single lemma fires, and the
affine data changes which one fires nowhere.**

**(c) What the affine data does add at `v_0`.** Apply BI-1, BI-3, BI-5 at
`N = 4`, `k_odd >= 1` or `k_odd = 0`:

```text
  Deg over v_0 :  2 (dicritical block)  +  2 (non-dicritical) = 4 .
  Marks over p :  by B3-N4 the branch locus of E~-bar -> P^1 is the 2 k_odd
                  odd-contact node punctures and eps_infty = 0, so the fibre
                  over the infinity puncture is UNRAMIFIED: two marks, e_y = 1.
                  (k_odd = 0: E = E_1 ⊔ E_2, each mapping isomorphically -- two
                  marks, e_y = 1, again.)
  BI-2/BI-5    :  each non-dicritical v~ ∈ v_0' has n(v~) = 1 and c_{v~} = m(v~).
                  Total Deg 2 with n = 1 leaves  m = 2 (one Deg-2 fork)  or
                  m = 1, 1 (two unit lifts).  DR Corollary 4 excludes the
                  degree-two fork.  Hence exactly TWO UNIT LIFTS.
```

> **CONTROL-1 RESULT.** *The two `Deg = 1` components over `v_0` that DR's
> assembly calls "the other two sheets" (`DR:534`) are exactly the two places of
> `E` at infinity over `∞_{A_F}`.* DR's opening move — "*if its other end were
> terminal, the other two sheets would form a separate component*" — is, read
> through BI-1/BI-5, a statement about `E`. The connectivity of `L̃_∞` that
> forces the first merge is the statement that those two places of `E` must join
> the dicritical's spine.

This step uses Cor 4, hence is exposed to `GAP-CANDIDATE[BI-ATTACH]`; the
alternative reading would put a `Deg-2` fork at `v_0` and the identification
would read "one component with `m = 2` carrying both marks" instead. Both
readings agree that **the non-dicritical `Deg` over `v_0` is `a` and is entirely
mark-bearing**, which is the part §5 uses.

**(d) Does the affine data shorten the census? NO — and here is the reason.**

```text
  35 raw local rows  :  UNCHANGED.  They enumerate the local neighbourhoods of a
        fork at an ARBITRARY target vertex v, for every (m,n) with mn <= 4.  The
        campaign ledger constrains the fibre over the CURVE g (BI-1) and over
        Sing A_F (BI-4); on the boundary it constrains ONE vertex, v_0.
  six global graphs  :  UNCHANGED.  Figs 20-25 differ by the type of the first
        fork (Deg 3 vs Deg 4) and by which of local Figs 13-16 sits there --
        pure boundary data, invisible to the affine ledger.
  ASSEMBLY DEPTH     :  REPRODUCED, not shortened.  §6.2's cap gives <= a = 2
        merges, which is exactly the two (A, then B) DR's §6 uses.
  ENTRY              :  SHORTENED (item (a)).
  OPENING MOVE       :  IDENTIFIED (item (c)).
```

The structural reason, which is the answer to the charge's question: **the DO
census is indexed by target boundary vertices; the campaign ledger is indexed by
`g` and by `Sing A_F`; the two index sets meet in the single vertex `v_0`.** One
vertex cannot shorten a census over all of them.

## 5. Control 2 (Sol's `Gamma` regression) and the `N = 5, 6` runs

### 5.1 `Gamma : y^2 = x^3 (x-1)^2`, parametrised `(t^2, t^3(t^2-1))`

MEASURED (sympy 1.14 over `Q`, driver `/tmp/b3bi/gamma.py`):

```text
  parametrisation satisfies the equation identically ;  irreducible over Q ;
  total degree 5 ;  affine singular locus EXACTLY {(0,0), (1,0)} ;
  (0,0): orders (2,3) in t at t = 0  -> ordinary (2,3) CUSP, delta = 1 ;
  (1,0): branches t = +1, -1 with tangents dy/dx = +1, -1 -> transverse NODE,
         contact t_1 = 1 (ODD), delta = 1 ;
  the parametrisation has NO affine pole -> exactly ONE place at infinity ;
  p_a = 6, delta_aff = 2, so delta_infty = 4 .
```

So `Gamma` is rational with one place at infinity (MI Lemma A's shape), one
cusp and one node with odd contact: the `N = 4`, `k = k_odd = 1` `(B3)` datum.

### 5.2 The instrument run on `Gamma` — PASSES on every requested item

Driver `/tmp/b3bi/ledger.py`; inputs `N=4`, `a=2`, dicritical `(1,2)`, points
`(r,K) = (1,1)` [cusp], `(2,0)` [node]:

```text
  Deg over g              :  [2] (dicritical) + 2 (Ē_X) = 4 = N              BI-1
  fibre-at-p ledger       :  2 (at p̃) + marks summing to 2 ; total 4 = N     BI-3
  marks over p            :  2, each e_y = 1, so n(v~_y) = 1                 BI-2
  spine-depth cap         :  <= N - s mu = 2                                 §6.2
  cusp p_0 (r=1,K=1)      :  a_p = 1  -> FORCED CUSP PREIMAGE y_0, and F etale
                             makes E singular there with the same (2,3) germ;
                             E-places at infinity over the cusp puncture: deg 1,
                             SAME-BRANCH, saturating K = 1                    BI-4
  node p_1 (r=2,K=0)      :  a_p = 0 -> the node has NO affine preimage;
                             Ē_X-branch degree at the two t's: 4, ALL
                             branch-exchanged (K = 0)                         BI-4
  chi_c(E) = a(1-R) + sum a_p , R = 3   ->   -3   =  1 - 4k  at k = 1        ✓
  n_infty  = (R-1)a + 2 - 2 p_a - sum a_p r_p  =  5                          ✓
  g(E) = k_odd - 1 = 0 , covering cap 2g <= 1  ->  g = 0                     ✓
  place split 2 (over ∞_Gamma) + 1 (cusp) + 2 (node)  =  5                   ✓
```

> **CONTROL-2 RESULT: PASS.** The instrument reproduces the forced cusp
> preimage `y_0`, `chi_c(E) = 1 - 4k = -3`, and the predicted genus `0` and
> `5` ends. It imports neither smoothness of `E` nor `chi(E) = 1` — the two
> steps SOL warns (`SOL:250-268`) must not be transferred from case (A): `E` is
> singular at `y_0` by construction here, and `chi_c(E) = -3 ≠ 1`.
> **It also makes a prediction `Gamma` did not previously carry:** two marks of
> index `1` over `∞_Gamma` sitting on boundary components of transverse degree
> `1`, and exactly three branches of `Ē_X` on `l'`, of degrees `(1; 2, 2)`, at
> the three points of `l'` over `Sing Gamma` (three because `s_l = 1` makes
> `h_l` an isomorphism, so `#T_p = r_p`).

### 5.3 `N = 5` and `N = 6`: the `(B3)` profiles, run

Admissible `(B3)` data, enumerated from `THEOREM PROFILE` + `(L)`,`(K)`,
`(C1)`,`(C2)`, Lemmas 4.2/4.3, 7.B' (driver `/tmp/b3bi/profiles.py`; `(B2)` rows
excluded by requiring a cusp, per the charge). At both degrees `sum_l s_l mu_l
= W` with `mu_l >= 2` forces a **single** dicritical with `s_l = 1`, hence
`R = 0`, hence `{p : K_p > 0}` = `{p` carrying a singular branch`}`:

```text
  N=5 : a=3, W=2, D_gap=1, dicritical (1,2), generic meridian 1^3·2 = (2,1,1,1);
        rho(G) = S_5 (transitive, generated by conjugate transpositions);
        B3-DEGREE eps = (-1)^{W - sum s_l} = -1  ✓ consistent with S_5.
        charged-point profiles:  {cusp K=2}, {cusp K=1, cusp K=1},
                                 {cusp K=1, multibranch-with-singular-branch K=1};
        plus k >= 1 uncharged double points (r=2, K=0, a_p=1).
  N=6 : a=3, W=3, D_gap=0, dicritical (1,3), meridian 1^3·3 = (3,1,1,1);
        eps = +1, so rho(G) ⊆ A_6  ✓ (B3-DEGREE positive control);
        charged profiles {cusp K=2}, {cusp K=1, cusp K=1}; nodes have a_p = 0.
        a=4, W=2, D_gap=2, dicritical (1,2), meridian 1^4·2 = (2,1,1,1,1);
        eps = -1, rho(G) = S_6 ; six charged profiles, and multibranch points
        may have r_p ∈ {2,3} (r=3 forces K=0, a_p=0).
```

The **generic meridian cycle type** used above is a degree-free reading of MI
Lemma 4.1 worth recording, since `N4-PIN`'s `(2,1,1)` was previously an input:
at a smooth `p` the fibre is `a` affine points plus, per dicritical and per each
of its `s_l` points over `p`, one block of `mu_l` sheets cyclically permuted by
the normal form `u = x'`, `v = y'^{mu_l}`. So

```text
   generic meridian cycle type  =  1^a · prod_l (mu_l)^{s_l} .      [BI-MERIDIAN]
   N=4:  1^2 · 2  =  (2,1,1)  ✓ reproduces N4-PIN.
```

Running the substituted package on every profile (driver `/tmp/b3bi/ledger.py`)
gives, for each, a complete boundary ledger. Representative rows:

```text
 profile                          Deg over g   marks over p   Ē_X-load at the t's        2 p_a(E) <=
 N=5 cusp K=2 + node              2 + 3 = 5    sum e_y = 3    cusp 2 (all charged),          1
                                                              node 4 (all exchanged)
 N=5 two cusps + node             2 + 3 = 5    sum e_y = 3    1 + 1 charged, 4 exchanged     0
 N=5 cusp + charged dp + node     2 + 3 = 5    sum e_y = 3    1 charged; 6 and 4 at the      4
                                                              two multibranch points
 N=6 a=3 cusp K=2 + node          3 + 3 = 6    sum e_y = 3    cusp 2 charged, node 6 exch.   3
 N=6 a=3 two cusps + node         3 + 3 = 6    sum e_y = 3    1+1 charged, 6 exchanged       2
 N=6 a=4 cusp K=3 + node          2 + 4 = 6    sum e_y = 4    3 charged, 4 exchanged         1
 N=6 a=4 cusps K=1,2 + node       2 + 4 = 6    sum e_y = 4    1+2 charged, 4 exchanged       0
 N=6 a=4 cusp + charged dp + node 2 + 4 = 6    sum e_y = 4    1 + (8, of which 2 charged)    5
 N=6 a=4 THREE cusps + node       2 + 4 = 6    sum e_y = 4    1+1+1 charged, 4 exchanged    -1
```

**The one interesting cell, and why it is not a kill.** The last row has
covering cap `2 p_a(E~-bar) <= -1`. With BR's binding repair `g = p_a(E~-bar)`
and `p_a = sum_i g_i - j + 1` for `j` components, this reads
`sum_i g_i <= j - 2`, i.e. **`E` is disconnected with `j >= 2`**. That is a
genuine new constraint on that cell (`B3-COMPONENT` must return `j >= 2` there),
but it is not emptiness. And the route can never produce emptiness:

> **PROPOSITION BI-7 (the disconnected reading never empties `(B3)`).** For any
> `(B3)` profile, `B3-E-GENUS` reads
> `2 p_a <= 1 - a + sum_p r_p max(0,(r_p-1)W + K_p - 1) >= 1 - a`. Emptiness by
> MI's `j <= a` would require `1 - p_a > a`, i.e. `2 p_a < 2 - 2a`. Since
> `2 - 2a < 1 - a` for every `a >= 2`, and `a >= ceil(N/2) >= 2` in `(B3)`, the
> required inequality is **never** attainable. `ROUTE CLOSED NEGATIVE.`

```text
  N = 5 and N = 6 RESULT:  NO EMPTY WINDOW.  Every (B3) profile at both degrees
  admits a consistent boundary ledger; the only cell forced off the generic
  branch is N=6 / a=4 / three cusps, which is forced to j >= 2, not to nothing.
```

**The exact residual — the two data the boundary side still lacks.**

```text
 OPEN[BI-CENSUS-DEG5-DEG6].  DO's Lemmas 8-9 census local fork neighbourhoods
   for Deg <= 4 only.  Running §§5-7 at N = 5 or 6 needs the same census for
   Deg <= 5 and <= 6 -- 86 and 287 raw rows (§6.1) -- with the determinant
   pruning of DR §5.2-5.3 redone.  The affine ledger supplies the SPINE DATA
   (starting Deg = s_l mu_l, depth <= a, mark saturation at v_0) and nothing
   about the rows.  Bounded, purely combinatorial-plus-determinant; the cheapest
   decisive next step for (B3) at N = 5.
 OPEN[BI-TAIL-AT-INFINITY] (§3.2) and GAP-CANDIDATE[BI-ATTACH] (§3.5).  Without
   the first, BI-3 and BI-5 are inequalities and v_0 is not pinned; the second
   blocks any general-N use of Corollary 4.
```

## 6. Task (6): the uniformity obstruction, named exactly

### 6.1 What grows, in closed form

The finiteness of DO's census is `sum_{v~ ∈ v'} Deg v~ = N` (DF-2). At general
`N` the fork list is `{(m,n) : m >= 2, mn <= N}` and, by `(4.3)`, a fork of
longitudinal degree `m` at a valence-3 target vertex admits one triple of
partitions of `m`, one per direction, with `m + 2` parts in total. Hence

```text
  Rows(m) = [z^{m+2}] f_m(z)^3 ,   f_m(z) = sum_{r>=1} P(m,r) z^r ,
  Census(N) = sum_{m>=2} floor(N/m) · Rows(m) .
```

MEASURED (driver `/tmp/b3bi/census.py`, exact integer arithmetic):

```text
 m     :   2    3    4    5     6     7     8     9     10     11     12
 Rows  :   3    6   23   51   192   430  1308  3105   8169  18348  46017

 N     :   4    5    6    7     8     9    10    11     12     13      14
 types :   4    5    8    9    12    14    17    18     23     24      27
 Census:  35   86  287  717  2051  5162 13385 31733  77974 177172  405434
```

`Census(4) = 35` **reproduces DO's own raw count exactly** (`DR:329-345`, and
its `(4,1)` sub-count `3 + 12 + 8 = 23` is `Rows(4) = 23`). That is the positive
control on the growth analysis. The growth is roughly geometric with ratio
`~2.3-2.9` at these degrees and is driven by `Rows(m) <= p(m)^3`; it is not
polynomial. **The affine ledger does not touch it.**

### 6.2 What the affine data *does* bound: the assembly depth

> **PROPOSITION BI-8 (spine-depth cap; all `N`).** Along the spine of maximal
> constant blocks and forks running outward from a dicritical `l`, the values of
> `Deg` are strictly increasing (a fork merges `>= 2` incoming packets) and are
> bounded above by `N` (DF-2). Starting from `Deg = s_l mu_l` (DR Lemma 6), the
> number of forks on that spine is at most `N - s_l mu_l`; when there is a
> single dicritical this is
> ```text
>          # forks on the spine   <=   N - W   =   a .
> ```
>
> *Control at `N = 4`.* `a = 2`, and DR's assembly (`DR:501-546`) uses exactly
> two: the first fork `A` (`Deg 3` or `4`) and, in the `Deg 3` case, the second
> fork `B` (`Deg 4`), after which "*every continuation cycles; the list stops*".
> The cap is tight. At `N = 5`: `<= 3`. At `N = 6`: `<= 3` (`a = 3`) or `<= 4`.

So the answer to the charge's question is split:

```text
 Does K_p cap the number of forks?          NO.  K_p is an AFFINE invariant
      (an excess on l', BI-4); it never appears in DF-2/DF-3 and constrains no
      target vertex.  Its only boundary shadow is the same-branch part of the
      Ē_X-load at the t's, which are marks on the vertex l, not vertices.
 Does the fibre partition cap them?         NO, for the same reason: the fibre
      partition over p ∈ Sing A_F is a partition of N into affine parts (a_p of
      size 1) and escaping parts (one of size mu_t per t); it is an invariant of
      the AFFINE fibre and of l', not of L̃_∞.
 What DOES the affine data cap?             (i) the spine DEPTH, by a = N - W
      (BI-8); (ii) the starting Deg of every spine, = s_l mu_l (BI-1 + Lemma 6);
      (iii) the whole non-dicritical Deg over v_0, = a, together with its
      mark structure (BI-5).  Nothing else.
 What is genuinely unbounded?               Census(N) above, and the number of
      double points of A_F (each has K_p = 0, so (K) never limits it) -- which
      is MI's OPEN[DEG-AF-VS-N] again, now seen to gate the BOUNDARY side too,
      through the number R = sum r_p of punctures that BI-4's ledger runs over.
```

## 7. FALLACY-v2 audit

* **Variable/ring map.** The fatal collision `a` (DO target vertex) vs `a`
  (campaign affine sheet count) is renamed once, in §0; the DO vertex is `v`
  throughout. `m`/`n`/`Deg` are declared against `s_l`/`mu_l` in §2.1 with the
  source line (`DR:48-60`).
* **Flag/place/series.** Six objects kept apart: `A_F`; `A_F~ ≅ A^1` with its
  punctures; `E`; `E~-bar` and its **places at infinity**; **marks**
  (`Ē_X ∩ L̃`); boundary **vertices** `v~`. The place↔mark dictionary is stated
  (BI-2) and used only in the contracted model, per BR's binding repair. `l`,
  `l'`, `p̃_l` are distinguished at every use.
* **Carrier / floor / attainment.** `Gamma` is a `REPRESENTATIVE` curve-level
  datum, never `A_F` for a Keller map; `E_0` is unused. BI-8 is a cap, its
  `N=4` tightness exhibited against DR's assembly, not assumed. `Census(N)`
  counts RAW rows. DF-5 (Lemma 7) is a lower bound and is never promoted.
  `E-CHARGE` is an inequality except at unibranch points; BI-4's
  "same-branch `<= K_p`" is **not** upgraded at multibranch points, and the
  complementary count comes from BE Prop 3.1's arithmetic.
* **Per-ray / exit-set charge.** Each branch of `Ē_X` at `t` is charged once, to
  `k_t`, only when `Phi(Gamma) = b(t)`; exchanged branches are declared
  uncharged. The `r_p` puncture-fibres are disjoint, so `r_p(a-a_p)` counts no
  place twice. BI-5's saturation comes from two equal sums, not a bijection.
* **Pole/interior.** Local degrees, monomial normal forms and the projection
  formula are used only where `F` is a finite map germ: at `p̃_l` and at marks
  under `(R1)`,`(R2)`, and at `t ∈ l'` only in the **contracted** model. `(H-∞)`
  is stated wherever the fibre at `p` must be finite, verified at `N = 4`, typed
  `OPEN` otherwise.
* **Prime label/derivative.** `l'`, `v'`, `R_v`, `b'`, `U'`, `V'`, `Z'`, `X'`
  are labels; the only derivatives are `f_X`, `f_Y`, `dy/dx` in §5.1.
* **`sat()` / raw remainder / merge-free / arrival index.** Not in play.
  `sympy.solve` on `(f, f_X, f_Y)` for `Gamma` returns a complete finite set.
* **Not filled by cap or analogy.** `(m,n)` split → `GAP-CANDIDATE[BI-ATTACH]`;
  census at `Deg <= 5, 6` → `OPEN[BI-CENSUS-DEG5-DEG6]`; the fibre at `p` →
  `OPEN[BI-TAIL-AT-INFINITY]`. No emptiness is manufactured.

## 8. Typed verdict block

```text
LANE     B3-BOUNDARY-INSTRUMENT
SCOPE    Keller, noninvertible, H2, case (B3).  Quasi-homogeneity only where HF
         local theory is consumed (SCOPE[B3-QH], charged); §§2,3,6 use none.
         No Z(G)=1, no case (A), no A2 cells, no (B2) beta-forced rows, no
         jc2-lean, no canonical-ledger edit.

PROVED HERE (all UNREVIEWED)
  BI-1        DO formula (9) at g = A_F-bar:  W + a = N, dicriticals the n>=2
              part, Ē_X the n=1 part.  DO's census identity IS [P3].
  BI-2        n(v~_y) = e_y at every mark over p.  All N.
  BI-3        fibre-at-p local-degree ledger (s_l mu_l)_l ∪ (e_y)_y summing to
              N; under (H-∞), which is verified at N=4.  Local degree value
              MEASURED in an explicit resolved (1,2)-dicritical model.
  BI-4        charged/exchanged split at p: total r_p(a-a_p), same-branch <= K_p,
              equality at unibranch p.  (E-CHARGE, contracted model.)
  BI-5        mark saturation at v_0 under (H-∞): c_{v~} = m(v~), so the
              ramification profile of E~-bar -> P^1 over ∞ is { n(v~)^{m(v~)} }.
  BI-6        unit lifts of E transport target determinants unchanged; DO's
              coprimality kills are kills of the multiplicity of E's sheets.
  BI-7        the disconnected reading of B3-E-GENUS can NEVER contradict
              j <= a.  ROUTE CLOSED NEGATIVE.
  BI-8        spine-depth cap #forks <= N - s_l mu_l (= a for one dicritical);
              tight at N = 4.
  BI-MERIDIAN generic meridian cycle type = 1^a · prod_l (mu_l)^{s_l};
              reproduces N4-PIN's (2,1,1).
  EXTRACTION-1 DF-4/6/7/8 available at every N under H2, via MI Lemma A.
  CENSUS      Census(N) = sum_m floor(N/m) Rows(m), Rows(m) = [z^{m+2}]f_m(z)^3;
              Census(4) = 35, matching DO.

CONTROLS  CONTROL 1 (N=4) PASS -- §4, incl. the identification of DR:534's
            "the other two sheets"; census NOT shortened, and why.
          CONTROL 2 (Gamma) PASS -- §5.2, every requested item, plus a new
            prediction (two index-1 marks; three Ē_X-branches of degrees 1;2,2).

N=5, N=6  NO EMPTY WINDOW.  Sole non-generic cell: N=6, a=4, three cusps + node,
          forced to p_a <= -1 hence j >= 2.  BI-7 closes the route.

NOT CLAIMED  any kill of (B3) at any N; any EMPTY window; that Gamma is A_F for
          any Keller map; the (m,n) split at the dicritical block; (H-∞) at
          N >= 5; a general-N analogue of Corollary 4; any value of deg A_F-bar,
          deg E-bar, or kappa-bar.

OPENS     OPEN[BI-CENSUS-DEG5-DEG6] (§5.3), OPEN[BI-TAIL-AT-INFINITY] (§3.2),
          GAP-CANDIDATE[BI-ATTACH] (§3.5) -- stated in full there.
          RE-RANKED: OPEN[DEG-AF-VS-N] gates the BOUNDARY side too (BI-4 runs
          over R punctures).  OPEN[E-INFINITY-SPLICE-DEGREE] is NOT needed here:
          BI-2/3/5 use indices e_y, never multiplicities Ē_X·L_infty.

SUCCESSOR Run OPEN[BI-CENSUS-DEG5-DEG6] at Deg <= 5 with BI-1/BI-5/BI-8
          substituted from the start (spine starts at Deg 2, depth <= 3, the
          non-dicritical Deg 3 over v_0 entirely mark-bearing with profile in
          {(1,1,1),(1,2),(3)}).  Settle GAP-CANDIDATE[BI-ATTACH] first, since
          Corollary 4's analogue is the pruning step.

MEASURED  §6.1 (Rows(2..12), Census(4..14); Census(4)=35 and the (4,1)
          sub-count 23 match DR exactly); §5.1 (Gamma, full singularity data);
          §3.2 (toy resolution: exponent det 2 = s·mu, neighbour CONTRACTED);
          (B3) profiles 3 / 8 / 33 at N = 5 / 6 / 7 with boundary ledgers
          computed for every N = 5, 6 row.

COMPUTATION python 3 + sympy 1.14.0 over Q; exact integer arithmetic for the
          census, profiles and ledgers.  No Groebner, no AWS, no msolve, no
          literature fetch, no web.

DEVIATIONS (1) The charge asked for "the determinants of the resulting
             branches".  Only BI-6 is derived; the rest need the (m,n) split,
             which GAP-CANDIDATE[BI-ATTACH] blocks.  Stated, not filled.
           (2) Drivers left in /tmp/b3bi, not installed in box/.
           (3) Body is ~44.9 KB against the charged 25-40 KB target.  The
             overage is content, not prose: nine PROVED-HERE items with proofs,
             two controls, the N=5/6 runs and the closed-form census.  Two
             compression passes were made; further cuts would have deleted
             either a proof or a control.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `45202`.
- Body SHA-256:
  `e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f`.
- Frozen basis: `665adaf1`.
