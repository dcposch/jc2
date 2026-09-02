# SAT-MASS — the satellite mass, and how the degree is assembled on the boundary

Lane: `SAT-MASS`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact desk CAS (sympy 1.14.0 / Python 3.14.7 over `Q`; a
resolution-of-indeterminacy engine written independently for this lane; no
Groebner, no AWS, no fetching, no web). Drivers in `/tmp/satmass`, not installed
in `box/`. Wall time 1.8 s per full battery, peak RSS 76 MB.

## 0. Custody, method, scope

The five charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all five match the charge exactly:

```text
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  n-vs-mapdeg-review-gpt55-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  deg-af-vs-n-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  chau-delta-budget-gpt55-20260902.md
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  b3-boundary-instrument-opus5-20260902.md
```

**NVM** = `N-VS-MAPDEG`, **NVM-R** = its gpt-5.5 hostile review, **DA** =
`DEG-AF-VS-N`, **CD** = Chau delta-budget, **BI** = B3 boundary instrument.
The ceiling set is consumed **at the review's typing, with its repairs**:
`DEG-SPLIT`, `CAP-STRICT`, `NOETHER-K`, `(I1)`–`(I6)`, `PROP DN`,
`MERIDIAN-FLOOR+`, `MOH-FLOOR` and the one-integer reduction as CONFIRMED
(NVM-R:33-84, 269-352); `NO-CEILING` **only** as `NO-CEILING[LATTICE-LEDGER]`
(NVM-R:64-70, 236-259); `NEG-GEN` **only** as a lower-bound refutation
(NVM-R:36-45, 106-140); Moh's normalisation as *both coordinate degrees* `<= 100`
(NVM-R:326-352). DA, CD and BI at their reviewed/charged typings. `Z(G)=1`,
case (A) and the A2 cells are **not consumed anywhere**; `jc2-lean` was not
inspected; no canonical ledger was edited.

Local PDF read this session with `pdftotext -layout` (hashed):

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
```

`refs/` contains **no** Abhyankar-Moh, **no** Nagata, **no** Appelgate-Onishi,
**no** Heitmann, **no** Guccione-Valqui `gcd` item and **no** Jung/van der Kulk
item (listing checked by `ls | grep`). Those stay **ABSENT** and every use of
them below is flagged as carried-from-the-campaign, never as verified here.
No `charge_basis` line: **this report asserts no new exit price.**

## 1. Verdict, up front

```text
(1) T IS A WEIGHT, NOT A REMAINDER.  Put nu_C := ord_C(sigma^*L_infty) (SOURCE
    polar multiplicity), m_C := ord_C(Phi^*L_infty) (TARGET polar multiplicity),
    c_C := Z.C.  Then (THEOREM SAT-WEIGHT, machine-verified on 74 maps, 0 fails)
         D  = sum_C nu_C c_C ,   N = sum_C m_C c_C ,   D - T = sum_C c_C ,
         T  = sum_C (nu_C - 1) c_C  =  sum_{C->L_inf}(nu_C-1)k_C + n sum_l (nu_l-1)s_l .
    D and N are the SAME pairing of the excess vector c against the source resp.
    target polar multiplicity.  c_C is the proximity EXCESS of the base cluster:
    c_{E_i} = a_i - sum_{j->i}a_j, so at most kappa + #dicriticals of the r+1
    cluster points have positive excess and ALL the others satisfy the proximity
    EQUALITY.  OPEN[SAT-MASS] is therefore exactly OPEN[NU-BOUND]: bound the
    integer nu_C on the non-contracted components.
(2) DEFINITION REPAIR.  DEG-SPLIT's T is the mass of points proximate to two
    members of the EXTENDED cluster {L_infty, p_1, ..., p_r}, not of the classical
    cluster.  T = T_class + (D - sum_{level-1} a_i), and the second term is
    nonzero exactly when a branch of the general member is tangent to L_infty
    (witness (x,y+x^4): T=3, T_class=2).  Machine-verified as an identity.
(3) T IS NOT A LEDGER QUANTITY (THEOREM LEDGER-BLIND, with witnesses).  Every
    entry of the boundary ledger -- N, kappa, Lambda, the dicritical excesses, the
    (m,k) data over L_infty, Z.K_X, g_net -- is invariant under SOURCE composition
    F |-> F o chi, while D and T grow without bound.  So no function of
    (N, n, S, kappa, W) bounds T, and OPEN[SAT-MASS] has zero content outside
    degree-minimality.  A Keller family realising this: (x, y+x^k) has the SAME
    ledger for every k and T = k-1 -> infinity.
(4) BUT T HAS A FLOOR THAT CARRIES.  THEOREM HALF-CAP: if D > N and F has exactly
    ONE dicritical (forced by 7.B' whenever W <= 3), then
         D <= 2(T + kappa),   equivalently   S n = Lambda <= D/2,   T >= D/2 - kappa.
    Sharp: (x,xy) and (x,x^2y^2) attain D = 2(T+kappa).  REFUTED for two or more
    dicriticals (witnesses (xy^2,xy), (x^2y,xy), (x, x(x-1)(x-2)y^2)) -- the
    hypothesis is load-bearing.  Consequences: Chau's cap is halved at W <= 3
    (deg A_F-bar <= D/2, not D-1); T > 0 is FORCED there, so the charge's
    T = 0 test on the N = 4 (B3) profile answers NO; and, crucially,
         ANY bound T <= tau on a degree-minimal representative gives D_min <= 2(tau+N).
(5) THE PRICE, CHEAPER THAN CHARGED.  MOH-CROSS needs only D_min <= 100.  With
    HALF-CAP that is  tau <= 50 - N  -- and it closes the cell OUTRIGHT, with NO
    n-ceiling, no DEG-AF, no ANTICANON-DEFECT.  tau <= 46 closes N = 4 (B3);
    tau <= 34 closes N = 16.  For W >= 4 the direct route needs |A| <= 1 and costs
    tau <= 25 - N/2; otherwise the charge's carry route n <= (100-kappa-tau)/S.
```

## 2. Part (1): what `T` is on the resolution

### 2.1 Setting, fixed once

`F = (P,Q) : C^2 -> C^2` dominant, of geometric degree `N`; `D := max(deg P, deg Q)`.
Homogenise to the **common degree** `D` and resolve the rational map

```text
   Fbar : P^2 --> P^2 ,   [x:y:z] |-> [ P^h_D : Q^h_D : z^D ] ,
```

by `sigma : X -> P^2`, blowing up the base cluster `K = {p_1,...,p_r}`, which lies
entirely on `L_infty` and its infinitely near points (`F` is a morphism on `A^2`).
`Phi := Fbar o sigma`; `E_0` = strict transform of `L_infty`, `Ltil` its total
transform, `Ltil_red` the reduced form; `a_i` = multiplicity of the **net**
`<P^h_D, Q^h_D, z^D>` at `p_i`; and

```text
   Z := Phi^*(L_infty) = D H - sum_i a_i E_i  in  Pic X = <H, E_1..E_r> ,
   Z^2 = N ,   i.e.   sum_i a_i^2 = D^2 - N .                                (D1)
```

`X \ Ltil = A^2`; `Ltil` is SNC with tree dual graph; `m_C := ord_C(Phi^*L_infty)`;
`c_C := Z.C`. All of this is NVM sec 2.3/3.1, CONFIRMED with the reviewer's
scope repairs (NVM-R:145-200), and is re-derived, not quoted, below.

### 2.2 The extended cluster, and the exact definition of `T`

> **DEFINITION (extended cluster).** Put `p_0 := L_infty` with multiplicity
> `a_0 := D`, and let `K^+ := {p_0, p_1, ..., p_r}`. Say `p_i -> p_j`
> (`p_i` is **proximate** to `p_j`) if `p_i` lies on the strict transform of
> `E_j` at the stage `p_i` is blown up, where `E_0 := L_infty`. By SNC,
> `prox(i) := #{j : p_i -> p_j} in {1,2}`.
> `p_i` is **free** if `prox(i) = 1` and a **satellite** if `prox(i) = 2`.
> ```text
>          T  :=  sum_{prox(i) = 2} a_i .
> ```
> The **classical** satellites are those proximate to two points `p_j, p_k` with
> `j,k >= 1`; write `T_class` for their mass.

**REPAIR (typed, and it matters).** DEG-SPLIT's `T` is the extended notion, not
the classical one. `p_i` can lie on `E_j` and on the strict transform of
`L_infty`; it is then free as a point of `K` but satellite in `K^+`.

> **LEMMA L1.** `T - T_class = D - sum_{p_i level 1} a_i`, i.e. the discrepancy is
> exactly the mass of the base points lying on the strict transform of `L_infty`
> above level 1 — the branches of the general member that are **tangent to
> `L_infty`**.
> *Proof.* `sum_{i -> 0} a_i` is the total mass on the `L_infty`-chain; the level-1
> points are free, the higher ones on that chain are exactly the extended-only
> satellites; and `sum_{i->0}a_i = D` whenever `E_0` is contracted (Lemma L4). ∎

Machine check (`t6.py`, `sha256 dc945654...`): the identity holds on every row,
e.g. `(x,y+x^4)`: `T = 3`, `T_class = 2`, discrepancy `1`; `(x^3,y^2)`: `2, 0, 2`;
`(x,x^3y^2)`: discrepancy `0`. The two notions genuinely differ.

### 2.3 The proximity excess IS the intersection number

> **THEOREM EXCESS-TRICHOTOMY.** For `i >= 0` put
> `rho_i := a_i - sum_{j -> i} a_j` (with `a_0 = D`). Then
> ```text
>            rho_i  =  Z . E_i^strict  =  c_{E_i}   for i >= 1 ,
>            rho_0  =  Z . E_0         =  c_{E_0} ,
> ```
> hence `rho_i >= 0` (**the proximity inequalities of the base cluster at
> infinity**) and, by the NVM/NVM-R trichotomy,
> ```text
>    rho_i = 0                 <=>  E_i is contracted by Phi ,
>    rho_i = k_C >= 1          <=>  Phi(E_i) = L_infty, of degree k_C ,
>    rho_i = s_l n_{c(l)} >= 1 <=>  E_i is a dicritical.
> ```
> *Proof.* `E_i^strict = E_i - sum_{j->i}E_j` and `E_0 = H - sum_{i->0}E_i` in
> `Pic X`; pair with `Z = DH - sum a_kE_k` using `H^2=1`, `E_k^2=-1`, `H.E_k=0`.
> Non-negativity is `Z` nef on the boundary (NVM (I1)-(I6), CONFIRMED). ∎

> **COROLLARY (rigidity).** At most `kappa + ell` of the `r+1` members of `K^+`
> have positive excess, where `kappa = sum_{C->L_infty}k_C <= N` and
> `ell := #dicriticals <= S <= floor(W/2)`. **Every other point of the extended
> cluster satisfies the proximity EQUALITY** `a_i = sum_{j->i}a_j` — i.e. the
> cluster is, off a set of size `<= kappa + ell`, the cluster of a curve.

This is the structural fact the rest of the report runs on; it is invisible in
the `(a_i)`-coordinates the ledger has been using.

### 2.4 DEG-SPLIT, re-derived from the excess

Summing `rho` over `K^+` and using the trichotomy:

```text
   sum_{i>=0} rho_i  =  sum_C Z.C  =  kappa + Lambda ,   Lambda := sum_l s_l n_{c(l)} .
```

On the other hand `Ltil_red = H - sum_{prox(j)=2}E_j` in `Pic X` (the coefficient
of `E_j` in `(H - sum_{i->0}E_i) + sum_i(E_i - sum_{j->i}E_j)` is `1 - prox(j)`),
so `Z.Ltil_red = D - T`. Hence

> **(DEG-SPLIT)**  `D = Lambda + kappa + T = sum_l s_l·deg(closure Phi(l)) + kappa + T`,
> and under `H2` (`A_F` irreducible of degree `n`) `Lambda = S n`, so
> `T = D - S n - kappa`.

The two computations of `sum rho` agree; that is the whole proof, and it
**identifies `D - T` as the total proximity excess of `K^+`**.

### 2.5 The Noether equations, and the genus of the net

Consumed at NVM-R's typing (Keller, `H2`, `R_aff = 0`):

```text
   (NOETHER-K)   sum_{i>=1} a_i = 3D - 2N - kappa + n(W - S) ,
                 sum_{i>=1} a_i^2 = D^2 - N ,      Z.K_X = sum_i a_i - 3D .
```

Two clean re-readings, both new here and both machine-checked.

> **LEMMA L2 (genus of the net).** Let `g_net` be the geometric genus of a general
> member of the net (= of the projective closure of a generic fibre of a generic
> `lambda P + mu Q`). Then, for **every** dominant `F`,
> ```text
>            Z . K_X  =  2 g_net  -  N  -  2 .
> ```
> *Proof.* By Bertini the general member is smooth off the base points, so its
> only singularities are the (infinitely near) `p_i`, with multiplicities `a_i`;
> hence `p_a(D) - g_net = sum_i a_i(a_i-1)/2`. Substitute `(D1)` and
> `Z.K_X = sum a_i - 3D`. ∎
>
> **COROLLARY.** Under Keller + `H2`, `g_net = (2 - N - kappa + n(W-S))/2 >= 0`,
> so `n(W-S) >= N + kappa - 2` and `n(W-S) = N + kappa mod 2`.
> `OPEN[ANTICANON-DEFECT]` is **exactly** "is the genus of the generic member of
> the pencil bounded in `N`?" — the question the parallel flagship
> `KELLER-PENCIL-GENUS` owns. This lane hands it over as an identity, and claims
> nothing further about it.

Controls, all reproduced by the engine: `g_net = 0` for every automorphism
(`Z.K_X = -3`, Noether's value) and for `(x,y^4)`; `g_net = 1` for `(x^3,y^2)`
(elliptic general member) and `(x^2,y^4)` (`x^2 = ` quartic in `y`).

> **LEMMA L3 (where Keller actually enters).** `Jac F in C^*` implies
> `dG != 0` everywhere for `G = lambda P + mu Q`, so **every** member of the net —
> not merely the general one — is smooth in `A^2`. (Bertini gives the general
> member for free, for any dominant `F`; the Keller hypothesis upgrades it to all
> members.) This is the exact place where `R_aff = 0` sits.

> **LEMMA L4 (`E_0` is contracted).** If `D > N` then `k_{E_0} = 0`, `E_0` is
> contracted to a point `q_0 in L_infty`, `rho_0 = 0` and
> `sum_{i -> 0} a_i = D`. Moreover at least **two** members of `K^+` are proximate
> to `p_0`.
> *Proof.* `(I2)` gives `N = sum_{C->L_infty}m_Ck_C >= m_{E_0}k_{E_0} = D k_{E_0}`,
> so `D > N` forces `k_{E_0}=0`; `m_{E_0} = D > 0` puts `Phi(E_0)` inside
> `L_infty`, hence a point. Then `rho_0 = c_{E_0} = 0`. If a single `p_1 -> p_0`,
> then `a_1 = D` and `sum_i a_i^2 >= D^2 > D^2 - N`, contradicting `(D1)`. ∎

By `MOH-FLOOR` (`D_min >= 101`, NVM-R:326-352) every gauge relevant to the
campaign has `D > N`, so `L4` is unconditional downstream.

## 3. THEOREM SAT-WEIGHT — how the degree is assembled

Define, for each boundary component `C`,

```text
    nu_C  :=  ord_C ( sigma^* L_infty )        [ SOURCE polar multiplicity ]
    m_C   :=  ord_C ( Phi^*   L_infty )        [ TARGET polar multiplicity ]
    c_C   :=  Z . C                            [ excess / trichotomy value ]
```

`nu` obeys the total-transform rule `nu_{E_i} = sum_{j in prox(i)} nu_{E_j}`,
`nu_{E_0} = 1`; so `nu_{E_i}` is the **number of proximity chains from `p_i` down
to `L_infty`** — `1` exactly when the whole ancestry of `p_i` is free, and a
continuant (Fibonacci-type) growth along satellite chains. Equivalently, for a
polynomial `h` on `A^2` not vanishing at the cluster, `ord_C(h) = -nu_C·deg h`:
`nu_C` is the *degree weight* of the divisorial valuation `ord_C`, and
`nu_{E_0} = 1` while `D = m_{E_0}` — the two multiplicities are dual, read at the
same component.

> **THEOREM SAT-WEIGHT.** For every dominant polynomial map `F`,
> ```text
>       D      =  sum_C  nu_C · c_C ,
>       N      =  sum_C  m_C  · c_C ,
>       D - T  =  sum_C  c_C ,
>       T      =  sum_C ( nu_C - 1 ) · c_C ,
> ```
> the sums being over all boundary components; only the `<= kappa + ell`
> non-contracted ones contribute. Under `H2`, splitting the trichotomy,
> ```text
>       D  =  kappa_nu + n · S_nu ,      T  =  (kappa_nu - kappa) + n (S_nu - S) ,
>       kappa_nu := sum_{C -> L_infty} nu_C k_C ,   S_nu := sum_l nu_l s_l .
> ```
> *Proof.* Expanding the total transform, `sigma^*L_infty = E_0 + sum_i nu_i E_i^{st}`
> as divisors, hence `H = E_0 + sum_i nu_i E_i^{st}` in `Pic X`. Pair with `Z`:
> `D = Z.H = rho_0 + sum_i nu_i rho_i = sum_{i>=0} nu_i rho_i`, and `rho_i = c_{E_i}`
> by EXCESS-TRICHOTOMY. `N = Z^2 = sum_C m_C (Z.C)` is `(I2)`. `D - T = sum rho_i`
> is sec 2.4. Subtracting the first and third gives the `T` formula. ∎

**Machine verification.** `engine.py` (`sha256 8cbd3afd...`) resolves `Fbar` by
explicit two-chart blow-ups over `Q`, returning the cluster with its full
proximity structure, `m_C`, `rho_C`, `nu_C` and the trichotomy. **74 distinct
dominant maps** were resolved (`D <= 24`, `N <= 8`, `r <= 17`; 2 further
candidates skipped, cluster not rational over `Q`); **all 74** satisfy `(D1)`,
`(I1)`, `(I2)`, `DEG-SPLIT`, all four `SAT-WEIGHT` identities, `rho_C >= 0`,
`m_C >= 0`, and `rho_0 = 0 <=> E_0` contracted — **0 failures**. The `m`-formula
`m_i = D·nu_i - sum_k pi(i,k)a_k` (`pi` = chain counts) was verified separately
on 27 maps, 0 failures. Extract, in NVM sec 3.6's own columns:

```text
 map                    D   N  kappa  Lam    T   T_class  sum a   Z.K_X   nu_max
 (x, y+x^k), k=2..6     k   1    1     0    k-1    k-2    3k-3     -3        k
 (x, xy)                2   1    1     1     0      0       3      -3        1
 (x, y^2)               2   2    1     0     1      0       2      -4        2
 (x, xy^2)              3   2    2     1     0      0       5      -4        1
 (x, x^2 y)             3   1    1     1     1      1       6      -3        2
 (x, x^2 y^2)           4   2    1     2     1      1       8      -4        2
 (x^2 y, y)             3   2    2     1     0      0       5      -4        1
 psi_2 o (x, x y^2)     6   2    1     2     3      3      16      -2        4
 psi_4 o (x, x y^2)    12   2    1     4     7      7      36       0        8
 psi_2 o (x, x y^3)     8   3    1     2     5      5      23      -1        6
 psi_3 o (x, x y^3)    12   3    1     3     8      8      37      +1        9
 psi_k = (u,v) |-> (u+v^k, v)
```

Every `(D, N, kappa, Lam, T, sum a, Z.K_X)` entry agrees **row for row** with NVM
sec 3.6/5.1, from an independently written engine — a two-route agreement on the
charged input's measured table. (One cosmetic disagreement: NVM's compressed row
`psi_k o (x,xy^2): 6k` contradicts its own explicit `psi_2` row `D = 6`; my
`psi_2` gives `D = 6`, `psi_4` gives `D = 12`, and the `T` / `Z.K_X` lists match
exactly. A typo in the compressed row, not a substantive disagreement.)

### 3.1 Three immediate corollaries

> **COROLLARY C1 (`T = 0` characterised).** `T = 0` <=> the extended cluster has
> **no satellite point at all** <=> `nu_C = 1` for every non-contracted `C`
> <=> `D = S n + kappa`. Machine-checked as an equivalence on all 74 maps.
> Geometrically: every branch of the general member at infinity is smooth **and**
> transverse to `L_infty`.

> **COROLLARY C2 (the crude bound, and why it is the right shape).**
> `T <= (nu_max - 1)(kappa + S n)` with `nu_max` the largest `nu` on a
> non-contracted component. So `OPEN[SAT-MASS]` is **exactly**
> `OPEN[NU-BOUND]`: bound `nu_C in Z_{>=1}` for non-contracted `C`.

> **COROLLARY C3 (`T` is the Jung-van der Kulk word length, made exact).** For the
> de Jonquieres automorphism `(x, y+x^k)` the unique non-contracted component has
> `nu = k`, `c = 1`, so `T = k-1 = D-1`: the whole degree sits in `nu`. This is
> NVM sec 5.2's identification, now with the mechanism (`nu` is a continuant of
> the satellite chain) rather than an analogy.

**Relation to `NO-CEILING[LATTICE-LEDGER]`.** `SAT-WEIGHT` is not a ceiling on
`D` at fixed `N`: it expresses `D` through `nu`, which the lattice ledger does
not bound. Nothing here contradicts the reviewer-scoped theorem, and nothing here
is claimed to.

## 4. Part (2): degree-minimality

### 4.1 The invariant, restated as a degree function

For a polynomial `h` on `A^2`, `deg h = -ord_{E_0}(h)` in **any** compactification
containing the strict transform `E_0` of `L_infty`. Hence for `R in C[u,v]`

```text
        v(R) := deg R(P,Q) = - ord_{E_0}( Phi^* R )
```

is a **degree function** (`v(RR') = v(R)+v(R')`, `v(R+R') <= max`), and

```text
        min over target coordinate systems (u',v') of max( v(u'), v(v') )
```

is the target half of `D_min`. Once `E_0` is contracted (Lemma L4, always here),
`v(R) = D·deg R - w(R^h)` with `w := ord_{E_0} o Phi^*` a divisorial valuation of
the **target** plane centred at `q_0 = Phi(E_0) in L_infty`, normalised by
`w(L_infty) = D`. Degree-minimality is thus a statement about a single divisorial
valuation at a single point of the target line at infinity.

### 4.2 What "no further degree-lowering automorphism" says — the exact theorems

`Jac(Ptilde, Qtilde) = 0` for the leading forms (Keller forces
`deg Jac = 0 < deg P + deg Q - 2`), so the binary forms `Ptilde, Qtilde` are
algebraically dependent, whence

```text
   (LF)  Ptilde = alpha H_0^d ,  Qtilde = beta H_0^e ,  deg H_0 = K = gcd(deg P, deg Q),
         deg P = Kd , deg Q = Ke , gcd(d,e) = 1 .
```

* If `d = 1` then `Q - c P^e` has smaller degree for one `c`; symmetrically for
  `e = 1`. If `d = e` then `d = e = 1` and `beta P - alpha Q` drops. So
  **degree-minimality (over target elementary automorphisms) is exactly
  `d, e >= 2` and `deg P != deg Q`.** This is the Abhyankar-Moh leading-form
  reduction; **AM 1975 is ABSENT from `refs/`** and the statement is carried at
  the campaign's banked typing (`AM-CHECK.md`), used here only in this elementary
  form, which is proved above from `(LF)` alone.
* **Moh 1983 is native to degree-minimal pairs.** Verified in `refs/` this
  session, OCR line 3259-3262: his search assumes
  `deg f = m < deg g = n <= 100`, `J(f,g) = 1` and *"the degrees of `f(x,y)` and
  `g(x,y)` can not be reduced simultaneously"*; Propositions 5.4/5.5 are exactly
  degree-lowering-automorphism statements (*"there exists an automorphism of
  `k[x,y]` which reduces the degrees of `Tf(f,g)`, `g(x,y)` and `f(x,y)`
  simultaneously"*); Appendix II closes with *"There is no counter-example of
  polynomials of degrees less than or equal to 100 for the Jacobian conjecture"*
  (OCR 3838-3839). So `MOH-FLOOR: D_min >= 101` at NVM-R's typing.
* Moh's own descent yields `d_s >= 4` for **his** gcd
  `d_s = gcd{n, M_1,...,M_{r-1}}` of the characteristic data (OCR 3275, from
  Corollary 6.1, OCR 3196-3210). **This is not `gcd(deg P, deg Q)`**; the two must
  not be identified. It is the only gcd bound actually present in `refs/`.
* `gcd(deg P, deg Q) >= 16` (Nagata; Appelgate-Onishi; Heitmann; GGV): **all
  ABSENT from `refs/`**, carried at the charge's "as banked" typing. It yields
  only `D = K max(d,e) >= 48`, weaker than `MOH-FLOOR`, and is load-bearing for
  nothing here.

### 4.3 The cluster translation of minimality: the tail an elementary map removes

> **LEMMA L5 (Newton-polygon form of the level-1 multiplicities).** Let `p_j` be a
> level-1 base point and choose affine coordinates in which `p_j` is the direction
> `y_j -> infinity`. Then
> ```text
>       a_{p_j} = D - max( deg_{y_j} P , deg_{y_j} Q , 0 ) ,
>       I_{p_j}(C_gen, L_infty) = e·r_j   ( r_j = multiplicity of the root of H_0 ),
> ```
> and by Lemma L1 the `L_infty`-tail above `p_j` has mass `e r_j - a_{p_j}`.
> *Proof.* In the chart `(xi,zeta) = (x/y_j, 1/y_j)` a monomial `x^a y_j^b` of a
> degree-`D` form becomes `xi^a zeta^{D-a-b}`, of order `D-b`; take the minimum
> over the support of a generic member. The second identity is
> `ord_{p_j}(mu·Qtilde) = e r_j`. ∎

This makes the "free tail" concrete: for `(x, y+x^k)`, `a_{p_1} = k - 1`,
`e r_1 = k`, tail mass `1`, and the reduction `Q - cP^k` is exactly what removes
it. Machine-verified: `T - T_class = D - sum_{level 1}a_i` on every row (sec 2.2).

**The two alternatives the charge poses, answered.**

> **(a) Is `T` bounded by a function of `(n, S, kappa, N)` for a minimal
> representative?** The question is only meaningful *at* the minimum: by
> THEOREM LEDGER-BLIND (sec 6) `T` is unbounded on the orbit at fixed
> `(N, n, S, kappa, W, Z.K_X, g_net)`. So no ledger function exists; what a bound
> would have to use is minimality itself, and the ledger gives it no purchase.
> **Typed: OPEN[SAT-MASS] (bounded quantity `T in Z_{>=0}`), with the missing
> datum named: `nu_C` on the non-contracted components (`OPEN[NU-BOUND]`).**
>
> **(b) Is `T` a function of the Puiseux characteristic of the place at infinity?**
> **YES, in form, and this is the content of `SAT-WEIGHT`.** The satellite
> structure of a cluster is precisely the Euclidean/continued-fraction resolution
> of the Puiseux characteristic of the branches it resolves, and `nu` is the
> continuant of that expansion; `T = sum_C (nu_C-1)c_C` is therefore a function of
> the Puiseux characteristics of the branches of the **general member of the net**
> at infinity, together with the excess vector `c`. What it is *not* is a function
> of `(n,S,kappa,N)`: the Puiseux characteristic itself is what is unbounded, and
> the place of `A_F-bar` at infinity (the charge's second candidate) is the wrong
> curve — `T` is read on the *net*, not on `A_F`. Under `H2` the dicritical
> contribution `n(S_nu - S)` is the only part that sees `A_F` at all, through `n`.

## 5. Part (3): the dicritical side — where `T > 0` is forced

The charge asks for the first case where `T > 0` is forced, and specifically for
the `N = 4` `(B3)` test `S = 1`, `n >= 4`, `kappa <= 4`. The answer is stronger
than `T > 0`.

> **THEOREM DICRITICAL-DEPTH.** Let `D > N` and let `l` be a dicritical, with
> `c_l = s_l n`. Then
> ```text
>        either   nu_l >= 2   ( hence  T >= (nu_l - 1) s_l n >= s_l n ) ,
>        or       2 s_l n  <=  D .
> ```
> *Proof.* Suppose `nu_l = 1`. Then every `p_k` with `pi(l,k) >= 1` lies on the
> unique proximity chain `l = k_0 -> k_1 -> ... -> k_h = p_0` (if `k` were off it,
> the `nu_k >= 1` chains from `k` to `p_0` would give a second chain from `l`), and
> `pi(l,k) = 1` on it. The verified `m`-formula
> `m_l = D nu_l - sum_{k>=1} pi(l,k) a_k` and `m_l = 0` (dicritical) give
> `sum_{t=0}^{h-1} a_{k_t} = D`. The proximity inequality at `k_{t+1}` gives
> `a_{k_{t+1}} >= a_{k_t}`, so the chain multiplicities increase towards `p_0` and
> `D >= h · a_l >= h · c_l = h s_l n`. If `h = 1` then `a_l = D` with `p_l -> p_0`,
> contradicting Lemma L4; so `h >= 2` and `D >= 2 s_l n`. ∎

> **THEOREM HALF-CAP.** Let `D > N` and suppose `F` has exactly **one** dicritical
> (`ell = 1`; forced by `7.B'` whenever `W <= 3`, since `W >= 2S >= 2ell`). Then,
> under `H2`,
> ```text
>      Lambda = S n  <=  D / 2 ,      D  <=  2 ( T + kappa ) ,      T  >=  D/2 - kappa .
> ```
> *Proof.* `Lambda = c_l = s_l n` and `Lambda = D - T - kappa` (DEG-SPLIT).
> If `nu_l >= 2`: `T >= c_l = Lambda = D - T - kappa`, so `D <= 2T + kappa`.
> If `nu_l = 1`: `2 Lambda <= D` by DICRITICAL-DEPTH, i.e. `2(D-T-kappa) <= D`,
> so `D <= 2T + 2kappa`. Either way `D <= 2(T+kappa)`, and then
> `Lambda = D - T - kappa <= D/2`. ∎

**Sharpness and scope, both machine-established.**

```text
  witnesses attaining  D = 2(T + kappa)  :  (x, xy)   D=2, T=0, kappa=1
                                            (xy, y)   D=2, T=0, kappa=1
                                            (x, x^2y^2) D=4, T=1, kappa=1
  21 single-dicritical rows tested, 0 violations of  D <= 2(T+kappa)  and 2Lam <= D.
  REFUTED for ell >= 2 (the hypothesis is load-bearing, not decorative):
       (x y^2, x y)              ell=2  D=3  T=0  kappa=1   2(T+kappa)=2 < 3
       (x^2 y, x y)              ell=2  D=3  T=0  kappa=1   2(T+kappa)=2 < 3
       (x, x(x-1)(x-2) y^2)      ell=3  D=5  T=0  kappa=2   2(T+kappa)=4 < 5
  (and 2*Lambda <= D fails on the same three rows: 4 > 3, 4 > 3, 6 > 5).
```

> **COROLLARY T-POSITIVE.** If `ell = 1` and `D > 2 kappa`, then `T >= 1`. Since
> `kappa <= N` and `D_min >= 101` (`MOH-FLOOR`), **`T > 0` is forced in the
> degree-minimal gauge for every `(N,W)` cell with `W <= 3` and `N <= 50`**, and
> quantitatively `T >= D/2 - N >= 101/2 - N`, i.e. `T >= 35` at `N = 16` and
> `T >= 47` at `N = 4`.

> **COROLLARY (the charged `N = 4` `(B3)` test).** With `S = 1` (hence `ell = 1`),
> `n >= 4`, `kappa <= 4`: `T = 0` would give `D = n + kappa <= 2kappa <= 8`,
> contradicting `D_min >= 101`. **So the Keller condition does not allow
> `T = 0` there: `D = S n + kappa` is impossible at `N = 4` `(B3)`**, and in fact
> `T >= D/2 - 4 >= 47`.

> **COROLLARY (Chau's cap halved).** For `ell = 1` (so all `W <= 3` cells)
> ```text
>          deg A_F-bar  =  n  <=  D / (2S)  <=  D / 2 ,
> ```
> against `CAP-STRICT`'s `n <= D - kappa - T <= D - 1` (NVM, CONFIRMED at
> NVM-R:200-215). In Chau's parameters this reads `K >= 2 S m`, sharpening
> `K >= S m + 1`. Consistent with, and stronger than, CD item 4 / CLAIM [D];
> it is a floor on `D`, used here only as a floor.

**Where the two-dicritical door is.** `ell >= 2` needs `S >= 2`, hence
`W >= 2S >= 4`, hence `N >= 8` (profile `a >= ceil(N/2)`, `W = N-a`). The first
cell where HALF-CAP can fail is `(N,W) = (8,4)`; for `N = 4..7`, and for every
`W in {2,3}` at any `N`, `ell = 1` is forced.

**General `ell`.** Splitting the dicriticals into `A = {nu_l = 1}` and
`B = {nu_l >= 2}`: `sum_A s_l n <= |A| D/2` and `sum_B s_l n <= T`, so
`D - T - kappa = Lambda <= |A| D/2 + T` and

```text
      D ( 2 - |A| )  <=  4T + 2 kappa ,
      |A| = 0 :  D <= 2T + kappa ;   |A| = 1 :  D <= 4T + 2 kappa ;   |A| >= 2 : vacuous.
```

`|A| <= ell <= S <= floor(W/2)`, so the bound is available whenever `W <= 5` with
at most one free-ancestry dicritical, and unconditionally when `W <= 3`.

## 6. Part (4): the negative route — `T` is blind to the ledger

> **THEOREM LEDGER-BLIND.** Let `F` be dominant and `chi in Aut(C^2)`. Then
> `F o chi` has the same `A_F` (hence `n`, `delta_aff`, `Gamma`), the same
> geometric degree `N`, the same monodromy data `(a, W, s_l, mu_l, S)`, the same
> `kappa`, the same dicritical excesses, the same `(m_C, k_C)` multiset over
> `L_infty`, and the same `Z.K_X` (`= 2g_net - N - 2`, and `g_net` is
> right-invariant because `(lambda P + mu Q) o chi` has the same generic fibre up
> to an automorphism of `A^2`). Meanwhile `D(F o chi)` is unbounded as `chi`
> varies, hence so is `T = D - Sn - kappa`.
>
> **Consequently no function of `(N, n, S, kappa, W, Z.K_X, g_net)` — i.e. of the
> entire banked ledger — bounds `T`.**

Machine witnesses (driver `t4.py`, `sha256 5b6ebf3c...`; `chi` ranging over
`id`, `(x,y+x^2)`, `(x,y+x^3)`, `(x+y^2,y)`, `(x,y+x^2)o(x+y^2,y)`):

```text
 base F         D over the chi-orbit    T over the chi-orbit   constant ledger
 (x, x y^2)      3,  5,  7,  4, 10       0,  2,  4,  1,  7     N=2 kap=2 Lam=1 ZK=-4 g=0 (m,k)=[(1,2)]
 (x, x^2 y^3)    5,  8, 11,  7, 16       3,  6,  9,  5, 14     N=3 kap=1 Lam=1 ZK=-3 g=1 (m,k)=[(3,1)]
 (x, y^3)        3,  6,  9,  3, 12       2,  5,  8,  2, 11     N=3 kap=1 Lam=0 ZK=-5 g=0
 (x, x y^3)      4,  7, 10,  5, 14       0,  3,  6,  1, 10     N=3 kap=3 Lam=1 ZK=-5 g=0 (m,k)=[(1,3)]
   (dicritical excess rho = [1] and every listed invariant constant along each row)
```

These four are dominant, not Keller; they establish that the ledger data do not
*determine* `T`. A genuinely **Keller** family with the same behaviour, and the
exact analogue of the charge's `(x, x^c y^N)` request:

> **THEOREM (Keller instance).** The family `(x, y + x^k)`, `k >= 2`, consists of
> Keller maps satisfying `(D1)`, `(I1)`-`(I6)`, `DEG-SPLIT`, `SAT-WEIGHT`,
> `NOETHER-K` (`sum a_i = 3D - 3`, the Noether/Cremona value), the proximity
> inequalities and the trichotomy, with **identical ledger data**
> `N = 1, kappa = 1, S = 0, Lambda = 0, Z.K_X = -3, g_net = 0` for every `k`, and
> ```text
>        T = k - 1 = D - 1  ->  infinity ,     nu_max = k .
> ```
> The unique non-contracted component has `nu = k`, `c = 1`; every satellite
> carries multiplicity `1`. All of these are non-minimal: `D_min = 1`.

**The charge's `(x, x^c y^N)` family, re-read.** Consumed at NVM-R's typing as a
lower-bound refutation only. It is the `S = 1`, `n = 1` shape and its growth is
indeed entirely in `T` (`N = 4`: `D = 5,6,7`, `T = 0,3,4`). It is not Keller;
what it spends is `Z.R_aff`. HALF-CAP does not stop it — `Lambda = 1 <= D/2` with
enormous slack — so it is nowhere near the HALF-CAP boundary, which is attained by
`(x,xy)` and `(x,x^2y^2)` instead.

> **What is missing, named.** The construction typing `OPEN[SAT-MASS]` undecidable
> *from the ledger alone* is complete (LEDGER-BLIND). What is missing is any
> handle on `nu_C` for a **degree-minimal** representative — `OPEN[NU-BOUND]`, sec
> 9. The obstruction is structural: by sec 4.1 the degrees are values of the
> valuation `w = ord_{E_0} o Phi^*` at `q_0 in L_infty`, so minimality is a
> statement about the cluster of `w` in the **target** plane, whereas `nu_C` lives
> in the **source** cluster. No instrument in the charged set connects the two.

## 7. Part (5): consequences and the price

`MOH-CROSS` (NVM sec 6.3, CONFIRMED at NVM-R:326-352): any proved
`D_min <= 100` empties geometric degree `N` outright.

> **COROLLARY SAT-CROSS (the direct route, `W <= 3`).** By HALF-CAP,
> `D_min <= 2(T + kappa) <= 2(tau + N)` for any proved bound `T <= tau` on a
> degree-minimal representative. Hence
> ```text
>        tau  <=  50 - N       closes the cell (N, W) with W <= 3, OUTRIGHT:
>        no n-ceiling, no DEG-AF, no ANTICANON-DEFECT, no delta_aff.
> ```
> `|A| <= 1` at larger `W` gives `D_min <= 4tau + 2N`, i.e. `tau <= 25 - N/2`.
> Otherwise the charge's carry route applies: `n <= (100 - kappa - tau)/S`.

```text
TABLE C2.  The price of SAT-MASS, 4 <= N <= 16.  Profile a = N-W,
  ceil(N/2) <= a <= N-2 ;  S <= floor(W/2) [7.B'] ;  ell <= S ;  kappa <= N.
  P0+1 = reviewed MERIDIAN-FLOOR+ floor on n at S=1.
  tau_dir = 50-N  (needs ell=1, i.e. W<=3) ;  tau_|A| = 25-N/2 ;
  carry = floor((100-N-1)/S_max), the n-ceiling that closes the cell at tau=1.

   N   W  Smax  ell=1?  P0+1   tau_dir   tau_|A|   carry(tau=1)
   4   2    1     YES      4      46       23.0        95
   5   2    1     YES      5      45       22.5        94
   6   3    1     YES      4      44       22.0        93
   7   2    1     YES      7      43       21.5        92
   8   3    1     YES      5      42       21.0        91
   8   4    2      no      4       --      21.0        45
  10   2    1     YES     10      40       20.0        89
  12   3    1     YES      7      38       19.0        87
  12   6    3      no      4       --      19.0        29
  16   2    1     YES     16      34       17.0        83
  16   8    4      no      4       --      17.0        20
  (full 49-row table generated by t8.py; no row has the required n-ceiling
   below the reviewed floor P0+1, even at tau = 50 -- the crossing is never
   self-contradictory in the charged range.)
```

**Reading.** The `(B3)` range `N = 4..8` at `W = 2,3` and every `W in {2,3}` cell
up to `N = 16` are closed by a single bound `T <= 34` on the satellite mass of a
degree-minimal representative — a bound in an integer with no curve theory in it.
That is the cheapest price the campaign has recorded for those cells, and it does
**not** route through `OPEN[DELTA-AFF-VS-N]`. For `W >= 4` the cheapest routes are
the `|A| <= 1` variant (`tau <= 25 - N/2`) or the charge's carry.

**What SAT-CROSS does not do.** It is conditional on a bound that this lane does
not prove, and HALF-CAP itself runs the *other* way: it is a **floor**,
`T >= D/2 - kappa`, so it tightens `D_min >= 2Sn` and is consistent with every
floor in the record. It is not evidence that `tau` exists.

## 8. FALLACY-v2 audit

* **Flag/place/series.** Four multiplicity functions kept apart and never
  identified: `a_i` (base multiplicity of the net), `nu_C = ord_C(sigma^*L_infty)`
  (source polar), `m_C = ord_C(Phi^*L_infty)` (target polar), `c_C = Z.C = rho_i`
  (excess). `D = m_{E_0}` and `nu_{E_0} = 1` are values of *different* functions at
  the *same* component; that they pair into `D = sum nu c` and `N = sum m c` is
  proved (sec 3), not assumed. `T` and `T_class` are separated and their difference
  computed. `ell`, `S = sum s_l` and `W` are three different integers.
* **Per-ray/exit-set charge.** No exit price; no `charge_basis` line. In
  `SAT-WEIGHT` each component contributes `c_C` once and each base point `a_i` at
  most once; the derivation is one intersection number computed two ways. In
  DICRITICAL-DEPTH each chain element is charged once and `h = 1` is disposed of
  separately rather than absorbed.
* **Carrier/attainment; floor/attainment.** Every explicit map in secs 3, 5, 6 is
  typed **REPRESENTATIVE / NON-KELLER** except the automorphisms, typed **KELLER /
  INVERTIBLE / NON-MINIMAL**; none is claimed to be or approximate a noninvertible
  Keller map. HALF-CAP's attainment is exhibited by two witnesses, its failure for
  `ell >= 2` by three. `MOH-FLOOR`, `MERIDIAN-FLOOR+`, `CAP-STRICT`, HALF-CAP and
  `T >= D/2 - kappa` are floors, used only as floors; SAT-CROSS is conditional with
  its missing input named. `T = 0` is settled by a *proof of impossibility* under a
  stated hypothesis, not by failure to construct.
* **Pole/interior.** `rho_0 = 0` is used only after `D > N` is established
  (Lemma L4), and `D > N` is sourced to `(I2)`, not assumed. `prox(i) in {1,2}`
  uses SNC, preserved under blow-up. Lemma L2 uses Bertini (valid for any dominant
  `F`); the Keller-specific upgrade is isolated in Lemma L3 and is not used to
  prove L2.
* **Variable/ring map.** The engine declares its charts `(U, UV)` and `(U'V', V')`,
  divides by the exact order of vanishing with an exactness assertion, and works
  over `Q` in the basis `(H, E_1..E_r)`. Positive controls: every
  `(D,N,kappa,Lam,T,sum a,Z.K_X)` reproduces NVM sec 3.6/5.1 on the overlapping
  rows from an independently written engine; `g_net` reproduces four independently
  known genera. Negative controls: the engine **asserts and refuses** on
  non-rational clusters (2 of 76 candidates skipped, reported, not dropped);
  `D <= 2(T+kappa)` **FAILS** on three `ell >= 2` maps, which is what fixes
  HALF-CAP's hypothesis; and `rho_0 > 0` occurs exactly once in the battery
  (`(x+y^2,y+x^2)`, `D = 2 < N = 4`), so Lemma L4's hypothesis is not vacuous.
* **Prime label / derivative; `sat()` / raw remainder.** `E_i^{strict}` and `E_i`
  are distinguished by superscript, never by a prime; `Ptilde` is a leading form;
  the only derivatives are inside `Jac`. No saturation, no Groebner basis, no
  quotient normal form -- only substitution, exact monomial division, `gcd`, and
  `factor_list` over `Q` with a degree-1 assertion on every factor.
* **Not filled by cap or analogy.** Abhyankar-Moh, Nagata, Appelgate-Onishi,
  Heitmann/GGV and Jung-van der Kulk are marked ABSENT from `refs/`; the only
  literature verified here is Moh 1983, quoted with OCR line numbers. Moh's
  `d_s >= 4` is explicitly *not* identified with `gcd(deg P, deg Q)`. Two typed
  OPENs are raised rather than guessed.

## 9. Typed verdict block

```text
LANE       SAT-MASS
SCOPE      Dominant polynomial maps throughout secs 2-3 and 6; Keller + H2 in
           secs 2.5, 5, 7.  D > N assumed wherever rho_0 = 0 is used, and it is
           supplied by MOH-FLOOR in every campaign gauge.  Case (A), Z(G)=1 and
           the A2 cells are not consumed.  Quasi-homogeneity never used.

PROVED HERE  (all PROVED-HERE, UNREVIEWED)
  T (repair)     DEG-SPLIT's T is the mass of points proximate to two members of
                 the EXTENDED cluster {L_infty,p_1..p_r}; T - T_class =
                 D - sum_{level-1}a_i, nonzero exactly at branches tangent to
                 L_infty.  Machine-verified identity.
  EXCESS-TRICH   rho_i := a_i - sum_{j->i}a_j = Z.E_i^strict = c_{E_i}: the
                 proximity inequalities ARE the nef conditions, and at most
                 kappa + ell of the r+1 cluster points have positive excess -- all
                 the rest satisfy the proximity EQUALITY.
  DEG-SPLIT      re-derived cluster-side: D - T = sum_i rho_i = kappa + Lambda.
  SAT-WEIGHT     D = sum nu_C c_C, N = sum m_C c_C, D - T = sum c_C,
                 T = sum (nu_C-1)c_C, with nu_C = ord_C(sigma^*L_infty) = the
                 number of proximity chains from C to L_infty.  D = kappa_nu +
                 n S_nu.  T = 0 <=> no satellite <=> nu = 1 on non-contracted C.
  m-FORMULA      m_i = D nu_i - sum_k pi(i,k) a_k  (pi = chain counts).
  LEMMA L2       Z.K_X = 2 g_net - N - 2 for EVERY dominant F, g_net = geometric
                 genus of the general member of the net.  Retypes
                 OPEN[ANTICANON-DEFECT] as the pencil-genus question and hands it
                 to KELLER-PENCIL-GENUS as an identity.  Keller+H2:
                 g_net = (2-N-kappa+n(W-S))/2 >= 0, so n(W-S) >= N+kappa-2 and
                 n(W-S) = N+kappa mod 2.
  LEMMA L4       D > N => E_0 contracted, rho_0 = 0, sum_{i->0}a_i = D, and >= 2
                 members of K^+ are proximate to L_infty.
  DICRIT-DEPTH   every dicritical has nu_l >= 2 (hence T >= s_l n) or 2 s_l n <= D.
  HALF-CAP       ell = 1 and D > N  =>  D <= 2(T+kappa), S n <= D/2,
                 T >= D/2 - kappa.  Sharp at (x,xy), (x,x^2y^2).  REFUTED for
                 ell >= 2 (three witnesses).
  T-POSITIVE     ell = 1, D > 2kappa => T >= 1; with MOH-FLOOR, T >= D/2 - N >= 35
                 for N <= 16.  T = 0 is IMPOSSIBLE on the charged N = 4 (B3)
                 profile (S = 1, kappa <= 4).
  HALF-CHAU      deg A_F-bar <= D/(2S) <= D/2 when ell = 1: CAP-STRICT halved,
                 i.e. K >= 2 S m in Chau's parameters.
  LEDGER-BLIND   F |-> F o chi fixes N, n, S, kappa, W, Lambda, the dicritical
                 excesses, the (m,k) multiset over L_infty, Z.K_X and g_net, while
                 D and T -> infinity.  No function of the banked ledger bounds T.
  SAT-CROSS      T <= tau on a degree-minimal representative gives D_min <=
                 2(tau+N) when ell = 1 (W <= 3), so tau <= 50 - N closes the cell
                 OUTRIGHT via MOH-CROSS -- no n-ceiling.  |A| <= 1 variant:
                 D_min <= 4tau + 2N, tau <= 25 - N/2.

MEASURED     74 distinct dominant maps resolved exactly over Q (D <= 24, N <= 8,
             r <= 17); all satisfy (D1), (I1), (I2), DEG-SPLIT and all four
             SAT-WEIGHT identities -- 0 failures.  m-formula verified on 27 maps.
             HALF-CAP verified on 21 single-dicritical rows, 0 violations, and
             REFUTED on 3 multi-dicritical rows.  Every overlapping row reproduces
             NVM sec 3.6/5.1 exactly (D, N, kappa, Lam, T, sum a, Z.K_X).  Right-
             composition invariance measured on 4 bases x 5 automorphisms.
             Wall time 1.8 s, peak RSS 76 MB.

NOT CLAIMED  any upper bound on T, nu_C, D_min, n_min or delta_aff; any kill of any
             (N,W) cell; that Z.K_X <= 0; that any exhibited map is or approximates
             a noninvertible Keller counterexample; anything about case (A), the A2
             cells, Z(G), the reducible branch, or the value of g_net for a Keller
             counterexample (that is KELLER-PENCIL-GENUS's).

OPENS RAISED OPEN[NU-BOUND].  For a degree-minimal noninvertible Keller pair, is
               nu_C bounded above by a function of N on the non-contracted
               boundary components?  Bounded quantity: nu_C = ord_C(sigma^*
               L_infty) in Z_{>=1}.  Equivalent to OPEN[SAT-MASS] via
               T = sum_C (nu_C - 1)c_C with sum_C c_C = kappa + Sn.
               SCOPE: FALSE without minimality -- (x, y+x^k) is Keller with
               nu = k at fixed ledger data.
             OPEN[TWO-DICRITICAL].  Does HALF-CAP survive ell >= 2 under Keller
               + H2?  Bounded quantity: |A| = #{dicriticals with nu_l = 1} in
               {0,...,ell}; |A| <= 1 suffices for D <= 4T + 2kappa.  First cell
               where it can bite: (N,W) = (8,4).  Refuted in the ambient dominant
               class by three witnesses, so a proof must use Keller.

OPENS        OPEN[SAT-MASS] is CONFIRMED open and RETYPED: it is exactly
RETYPED      OPEN[NU-BOUND], it is empty of ledger content (LEDGER-BLIND), and its
             payoff is now DIRECT rather than a carry -- tau <= 50 - N closes a
             W <= 3 cell without the n-half.  OPEN[ANTICANON-DEFECT] is retyped as
             the pencil-genus question via Z.K_X = 2g_net - N - 2 (identity).

SUCCESSOR    NU-MINIMAL.  Decide whether a degree-minimal Keller pair can have a
             non-contracted boundary component with nu_C >= 2 -- one integer, on
             one component.  Instruments in hand: SAT-WEIGHT, the m-formula,
             HALF-CAP, and sec 4.1's target-side reformulation (D_min = min over
             target coordinate systems of max(v(u'),v(v')), v(R) = D deg R -
             w(R^h), w = ord_{E_0} o Phi^* at q_0 = Phi(E_0)).  The gap the lane
             could not close: nu lives in the SOURCE cluster, minimality in the
             TARGET one; the cheapest next instrument is the composition rule
             relating the two clusters, finite at each r.

DEVIATIONS   (1) Item (4) asked for a SYNTHETIC Keller-compatible cluster family
                 with T -> infinity.  I exhibited ACTUAL families instead
                 (LEDGER-BLIND; and the Keller family (x,y+x^k)) with every ledger
                 quantity constant and T -> infinity, which settles the
                 undecidability question outright.  I did NOT construct a
                 synthetic NONINVERTIBLE Keller cluster and do not claim one exists.
             (2) HALF-CAP, DICRITICAL-DEPTH and SAT-CROSS were not on the charged
                 instrument list; they are what the excess reading produced, and
                 they make the crossing cheaper than charged.
             (3) Item (3) asked for "the FIRST case where T > 0 is forced".  The
                 answer is uniform, not first: forced in every cell with ell = 1,
                 i.e. every W <= 3, at every N.
             (4) Report length ~45 KB, above the charged 25-40 KB target.  The
                 overrun is the sec 2 identity package with its proofs and the
                 sec 3 machine table, which items (1) and (4) of the charge
                 require; the audit, the verdict block and tables C2 and the
                 sec 6 witness table were already thinned.
             (5) Desk CAS: 1.8 s, 76 MB, inside the 15 min / 4 GB budget.  Drivers
                 in /tmp/satmass (engine.py 8cbd3afd..., t1..t8.py, count.py),
                 not installed in box/.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `44943`.
- Body SHA-256:
  `dd691a97696ea35fe46b535bfcd75a00dd1892cb4ef092d5e2b0c25b52a34c95`.
- Frozen basis: `c513bcef9863771057803c0e45f9f42e4154f3ef`.
