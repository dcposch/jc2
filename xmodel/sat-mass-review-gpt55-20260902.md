# Hostile review: SAT-MASS

Reviewer: gpt-5.5
Date: 2026-09-02
Report: `xmodel/sat-mass-review-gpt55-20260902.md`

No canonical ledger was edited and no `jc2-lean` content was inspected. No
new exit-price assertion is made here; the Moh contradiction price consumes
the reviewed `MOH-CROSS`, so no `charge_basis` line is emitted.

## Custody

The frozen read-only inputs in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.99a82f/inputs`
were hashed before review and all matched the charge:

```text
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  sat-mass-opus5-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  n-vs-mapdeg-review-gpt55-20260902.md
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  integration12-coordinator-fable51-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  chau-delta-budget-gpt55-20260902.md
```

Abbreviations: **SM** = charged `sat-mass-opus5-20260902.md`; **I12** =
`integration12-coordinator-fable51-20260902.md`; **NVM** and **NVM-R** are the
producer/review pair supplied in the frozen input set; **CD** is the supplied
Chau review.

Computational replay used only the preserved desk scripts in
`box/satmass-drivers-20260902`, a verbatim coordinator copy of `/tmp/satmass`
(`README.md:1-3`). Driver hashes used:

```text
8cbd3afd3055ed9ee001188474f659d8b3ffa97df959586fb21b46d9f49a55b1  engine.py
694eddb4c90de1fc382fe91f2f26821980a6470287119fbfb223ed30039a1903  t2.py
5ccaa1e4b06dddf357598141dbc6b4aa19d86fc7bafbb4f5d51f1cf3fc3ff21c  t3.py
5b6ebf3c9d23fae3f0badebfa0fe70fd57ae320b1808f0f035ec789fe7fcac42  t4.py
dc9456546ac402523910bb4f23d523e6fc1f03ca22edefb145d4c31402f7e8b3  t6.py
95fae0c6b0704dad2897eea3c1c20fce9225a640db7294e3864c58a2efa6b42e  t7.py
5295db5b9286b1e3bd945376b4fa535691b75c4c175aafa13c31b05542bac374  count.py
```

## Verdict Matrix

```text
ITEM A  SAT-WEIGHT and excess formulas
        VERDICT: CONFIRMED, with indexing repair.
        SOURCE: SM:90-112, 144-189, 242-278, 680-701.
        REPAIR: the sums are over strict boundary components C.  For an
        exceptional label E_i, c_C means Z.E_i^strict =
        a_i - sum_{j->i}a_j; for E_0 it means
        rho_0 = D - sum_{j->0}a_j.  With that convention,
          D=sum_C nu_C c_C, N=sum_C m_C c_C,
          D-T=sum_C c_C, T=sum_C(nu_C-1)c_C.
        The proof is Picard-intersection algebra, not a machine theorem.

ITEM B  Definition repair for T and Integration #12
        VERDICT: GAP as written; CONFIRMED after correction.
        SOURCE: SM:116-142; I12:24-34.
        REPAIR: DEG-SPLIT requires T_ext, the mass of points proximate to two
        members of K+={L_infty,p_i}.  The relation to classical satellite
        mass is globally
          T_ext - T_class = D - sum_{level-1}a_i - rho_0.
        The charged formula without `-rho_0` is valid only when E_0 is
        contracted, in particular under D>N.  I12 must bind line 27/33's
        "satellite mass" to T_ext, not T_class.

ITEM C  LEDGER-BLIND
        VERDICT: CONFIRMED for the listed banked ledger; REFUTED if "every
        boundary-ledger entry" includes source-cluster data.
        SOURCE: SM:523-562, 719-721.
        REPAIR: state the invariant list explicitly:
          N, A_F data (n, W, s_l, mu_l, S), kappa, Lambda, dicritical
          excesses, the (m,k) multiset over L_infty, Z.K_X, and g_net.
        Exclude a_i, proximity graph, r, nu, T, and T_class.  Those move under
        source composition.

ITEM D  HALF-CAP
        VERDICT: CONFIRMED under the stated mathematical hypotheses; one
        sentence needs a scope repair.
        SOURCE: SM:443-482, 485-521.
        REPAIR: hypotheses are H2, ell=1, and D>N.  The W<=3 implication is:
        if the H2 nonproper cell has S>=1 and 7.B' gives W>=2S, then W<=3
        forces S=1 and ell=1.  W<=3 alone does not force a dicritical in a
        proper or arbitrary dominant map.  Sharpness and the three ambient
        multi-dicritical refutations recompute as charged.

ITEM E  SAT-CROSS price and Moh threshold
        VERDICT: CONFIRMED.
        SOURCE: SM:579-623; NVM-R:382-424; NVM:715-725; I12:70-83.
        REPAIR: for a degree-minimal representative, D=D_min.  If D>N, use
        HALF-CAP; if D<=N, the bound D_min<=2(tau+N) is trivial.  Thus
        T<=tau gives D_min<=2(tau+N) in W<=3 H2 cells.  tau<=50-N gives
        D_min<=100 and contradicts Moh for noninvertible Keller maps.

ITEM F  Degree-minimality and classical citations
        VERDICT: GAP for the claimed cluster translation; CONFIRMED for the
        narrower target-leading-form reduction and Moh floor.
        SOURCE: SM:337-394, 396-435, 742-769; NVM-R:405-420.
        REPAIR: the section proves a level-1 tail diagnostic and target
        elementary degree-reduction criterion for a fixed representative.  It
        does not prove a global source-boundary-tree theorem for a D_min
        Keller pair and does not bound nu_C or T.  The gcd>=16 package is
        non-load-bearing here and should be carried only as an external
        classical input with primary citations.
```

Promotion recommendation: promote Items A and E. Promote Item B only with the
global `-rho_0` correction and the binding phrase `T=T_ext`. Promote Item C
only for the listed banked ledger. Promote Item D with `H2`, `ell=1`, `D>N`,
and the repaired W<=3 implication. Promote Item F only as target-side
minimality plus Moh floor; do not promote it as a source-boundary tree
translation.

## A. SAT-WEIGHT

Setup is the common-degree rational map

```text
[x:y:z] |-> [P_D^h : Q_D^h : z^D]
```

resolved by boundary blowups over `L_infty` (SM:92-107). In the total-transform
basis of `Pic X`,

```text
Z = Phi^*L_infty = D H - sum_i a_i E_i.
```

For a strict exceptional component `C_i=E_i^strict=E_i-sum_{j->i}E_j`,

```text
c_i = Z.C_i = a_i - sum_{j->i} a_j = rho_i.
```

For `C_0=E_0=L_infty^strict=H-sum_{j->0}E_j`,

```text
c_0 = Z.C_0 = D - sum_{j->0} a_j = rho_0.
```

This proves the excess identification in SM:146-161. Since `Z` is nef on the
boundary, `rho_i>=0`; by the NVM trichotomy, positive excess components are
exactly components mapping onto `L_infty` or dicritical components (SM:153-158).
The number of positive-excess points is therefore at most
`#onto-L_infty + ell <= kappa + ell`, because each onto component has positive
integer degree and their degrees sum to `kappa` (SM:163-167).

Now let `nu_C=ord_C(sigma^*L_infty)`. By definition of total transform,

```text
sigma^*L_infty = H = sum_C nu_C C.
```

Pairing with `Z` gives

```text
D = Z.H = sum_C nu_C (Z.C) = sum_C nu_C c_C.
```

Likewise `m_C=ord_C(Phi^*L_infty)` means

```text
Phi^*L_infty = Z = sum_C m_C C,
```

so

```text
N = Z^2 = sum_C m_C (Z.C) = sum_C m_C c_C.
```

Finally,

```text
sum_C c_C = sum_{i>=0} rho_i
          = D + sum_{i>=1}a_i - sum_{i>=1} prox(i)a_i
          = D - sum_{prox(i)=2}a_i
          = D - T_ext.
```

This proves `D-T=sum c_C` directly from the extended satellite definition
SM:116-124. Subtracting this identity from `D=sum nu c` proves
`T=sum(nu-1)c`. No equality or floor is inferred from a lower bound here.

Focused replay of the four SAT-WEIGHT sums:

```text
map                             D   N kap Lam   T  Tc ell sum nu*c sum m*c sum c  sum(nu-1)c ok
auto (x,y+x^2)                  2   1   1   0   1   0   0        2       1     1           1 True
auto (x,y+x^4)                  4   1   1   0   3   2   0        4       1     1           3 True
auto nested                     6   1   1   0   5   2   0        6       1     1           5 True
(x,xy)                          2   1   1   1   0   0   1        2       1     2           0 True
(xy,y)                          2   1   1   1   0   0   1        2       1     2           0 True
(x,x^2y^2)                      4   2   1   2   1   1   1        4       2     3           1 True
(x,x^3y^4)                      7   4   2   1   4   4   1        7       4     3           4 True
(x,x y^4)                       5   4   4   1   0   0   1        5       4     5           0 True
(x,y^2)                         2   2   1   0   1   0   0        2       2     1           1 True
(x^3,y^2)                       3   6   1   0   2   0   0        3       6     1           2 True
psi2 o (x,xy^2)                 6   2   1   2   3   3   1        6       2     3           3 True
(xy^2,xy)                       3   1   1   2   0   0   2        3       1     3           0 True
(x^2y,xy)                       3   1   1   2   0   0   2        3       1     3           0 True
(x,x(x-1)(x-2)y^2)              5   2   2   3   0   0   3        5       2     5           0 True
```

This covers the mandatory automorphisms, `(x,xy)`, `(x,x^2y^2)`,
`(x,x^c y^N)`, and multi-dicritical controls. The full preserved count also
replayed: 76 distinct maps attempted, 74 resolved over `Q`, 2 skipped for
irrational clusters, 0 identity failures.

## B. T Repair

The central repair is right: DEG-SPLIT uses the extended cluster
`K+={p_0=L_infty,p_1,...,p_r}` and counts points proximate to two members of
`K+` (SM:116-128). If "satellite" is read classically, meaning proximate to two
base points `p_j,p_k` with `j,k>=1`, DEG-SPLIT fails on elementary examples.
For `(x,y+x^4)`, replay gives `T_ext=3`, `T_class=2`; using `T_class` would
give `D != Lambda+kappa+T`.

The charged relation to `T_class` is missing one term. Let `L1` be the set of
level-1 points, i.e. `p_i->p_0` and no other parent. Extended-only satellites
are the points proximate to `p_0` and to one exceptional point. Therefore

```text
T_ext - T_class = sum_{i->0, prox(i)=2} a_i.
```

Since

```text
rho_0 = D - sum_{i->0}a_i
      = D - sum_{i in L1}a_i - sum_{i->0, prox(i)=2}a_i,
```

the correct global formula is

```text
T_ext - T_class = D - sum_{i in L1}a_i - rho_0.
```

SM:132-138 states the formula without `-rho_0` and proves it using
`sum_{i->0}a_i=D`, which is only supplied later by Lemma L4 under `D>N`
(SM:230-237). Countercheck:

```text
D<N control (x+y^2,y+x^2):
  D=2, N=4, rho0=2, T=0, T_class=0, sum_level1=0
  T-T_class=0, D-sum_level1=2, repaired value=0

D>N witness (x,y+x^4):
  D=4, N=1, rho0=0, T=3, T_class=2, sum_level1=3
  T-T_class=1, D-sum_level1=1, repaired value=1
```

Binding correction for I12: lines 27 and 33 must be read as
`T=T_ext=sum_{prox_K+(i)=2}a_i`. This preserves I12's DEG-SPLIT line 33 for all
dominant maps. The simplified `T=T_class+(D-sum level1)` may be used only in
the `D>N` downstream scope, which includes the campaign's degree-minimal
noninvertible Keller cells via Moh.

## C. LEDGER-BLIND

Source composition by an automorphism `chi` does not change the target image,
generic fibre cardinality, or nonproperness curve. Hence it fixes `A_F`,
geometric degree `N`, and the H2 data `(n,W,s_l,mu_l,S)`. The components over
target `L_infty`, their polar multiplicities, and their degrees are intrinsic
to the pullback of the target line in the induced function-field extension,
so the listed `(m,k)` multiset, `kappa`, dicritical excess list, and `Lambda`
are preserved. The generic member of the pencil is carried to
`(lambda P+mu Q) o chi`, so `g_net` and `Z.K_X=2g_net-N-2` are preserved
(SM:525-531).

The divergence is also real. For the Keller automorphisms `(x,y+x^k)`, all
listed ledger data stay

```text
N=1, kappa=1, S=0, Lambda=0, Z.K_X=-3, g_net=0,
```

while `D=k` and `T=k-1` (SM:553-562). The right-composition replay in SM:537-546
was reproduced on four non-Keller bases plus an automorphism base; for example
`(x,xy^2)` under five source automorphisms had constant
`N=2, kappa=2, Lambda=1, ZK=-4, g_net=0, (m,k)=[(1,2)]`, while
`D=3,5,7,4,10` and `T=0,2,4,1,7`.

Repair: do not say "every boundary-ledger entry" without a list. The source
cluster entries `a_i`, proximity graph, `r`, `nu`, `T`, and `T_class` are not
invariant; they are exactly where the divergence lives.

## D. HALF-CAP

Assume H2, `D>N`, and exactly one dicritical component `l`. Then
`Lambda=c_l=s_l n` and DEG-SPLIT gives

```text
D = Lambda + kappa + T.
```

The depth lemma in SM:443-457 is sound after unpacking the `m` formula. If
`nu_l=1`, every ancestor of `l` lies on a single free chain to `p_0`, and

```text
0=m_l=D*nu_l - sum_k pi(l,k)a_k
```

forces the sum of the chain multiplicities to be `D`. Proximity inequalities
make those multiplicities nondecreasing toward `p_0`, so `D>=h a_l>=h c_l`.
The case `h=1` would force `a_l=D` at level 1, contradicting Lemma L4's
`rho_0=0` plus at least two points over `p_0` (SM:230-237). Hence `h>=2` and
`2c_l<=D`.

If `nu_l>=2`, SAT-WEIGHT gives `T>=c_l=Lambda`, so

```text
D = Lambda+kappa+T <= 2T+kappa <= 2(T+kappa).
```

If `nu_l=1`, the depth lemma gives `2Lambda<=D`, hence

```text
2(D-T-kappa)<=D,  so  D<=2T+2kappa.
```

Therefore always

```text
Lambda=S n <= D/2,   D<=2(T+kappa),   T>=D/2-kappa.
```

The one-dicritical hypothesis is load-bearing. Replay of `t7.py` gave 21
single-dicritical rows with `D>N` and 0 failures of both `D<=2(T+kappa)` and
`2Lambda<=D`. The sharp rows recompute:

```text
(x,xy):       D=2, T=0, kappa=1, ell=1, D=2(T+kappa)
(xy,y):       D=2, T=0, kappa=1, ell=1, D=2(T+kappa)
(x,x^2y^2):   D=4, T=1, kappa=1, ell=1, D=2(T+kappa)
```

The ambient multi-dicritical refutations also recompute:

```text
(xy^2,xy):                  ell=2, D=3, T=0, kappa=1, 2(T+kappa)=2, 2Lambda=4
(x^2y,xy):                  ell=2, D=3, T=0, kappa=1, 2(T+kappa)=2, 2Lambda=4
(x,x(x-1)(x-2)y^2):         ell=3, D=5, T=0, kappa=2, 2(T+kappa)=4, 2Lambda=6
```

These are not Keller counterexamples. They refute dropping `ell=1` in the
ambient dominant category. Whether Keller+H2 forbids the bad multi-dicritical
configuration is not proved here; see `OPEN[TWO-DICRITICAL-KELLER]` below.

The W<=3 sentence in SM:459-460 needs a qualifier. From 7.B' one has
`W>=sum_l s_l mu_l>=2S` with `mu_l>=2`, and `ell<=S`. Thus W<=3 implies
`S<=1`. In a nonproper H2 cell, `S>=1`, so `S=1` and `ell=1`. Without
nonproperness or `S>=1`, W<=3 does not force any dicritical.

## E. Price

For a degree-minimal representative in a W<=3 H2 nonproper cell, the repaired
W<=3 implication gives `ell=1`. If `D>N`, HALF-CAP gives

```text
D_min = D <= 2(T+kappa) <= 2(tau+N)
```

from `T<=tau` and `kappa<=N`. If `D<=N`, the same inequality is trivial because
`tau>=0`. Therefore the charged translation is confirmed:

```text
T<=tau on a degree-minimal representative  =>  D_min<=2(tau+N).
```

Moh was already reviewed in NVM-R:405-420: a noninvertible Keller map has
`D_min>=101`. Consequently

```text
2(tau+N)<=100  <=>  tau<=50-N
```

empties the cell outright through `MOH-CROSS` (NVM:719-721; I12:70-83). The
named thresholds are exact:

```text
N=4:   tau<=46 gives D_min<=100.
N=16:  tau<=34 gives D_min<=100.
```

This is conditional. HALF-CAP is a floor on `T` in terms of `D`; it does not
prove that such a `tau` exists.

## F. Degree-Minimality

The target-side leading-form reduction is basically correct. For a Keller pair,
the top homogeneous Jacobian vanishes, so the leading forms are algebraically
dependent. In `C[x,y]` this gives

```text
P_tilde = alpha H_0^d,  Q_tilde = beta H_0^e,
deg P=Kd, deg Q=Ke, gcd(d,e)=1.
```

If `d=1`, a target elementary map subtracts a scalar multiple of `P^e` from
`Q` and lowers degree; similarly for `e=1`. If `deg P=deg Q`, a target linear
combination lowers degree. Conversely, for a fixed representative with
`d,e>=2` and unequal degrees, this elementary leading-term move is absent
(SM:362-377). Calling this "Abhyankar-Moh" is imprecise: the common-power
leading-form statement and the elementary reduction used here are elementary
plus the standard plane automorphism reduction, not the one-place
Abhyankar-Moh semigroup theorem recorded in `ladder/AM-CHECK.md:50-73`.

Moh is correctly consumed at the reviewed scope. The local OCR copy records
the simultaneous-degree-minimal hypothesis and the `<=100` conclusion
(`box/satmass-drivers-20260902/moh.txt:3259-3262, 3838-3839`), matching
NVM-R:405-420. Thus `MOH-FLOOR: noninvertible Keller => D_min>=101` is
confirmed.

The gcd citation bundle is not proved by SM. Lines SM:391-394 mark
Nagata/Appelgate-Onishi/Heitmann/GGV absent from `refs/` and non-load-bearing.
Local campaign context separately records a primary-source-checked
GGV/Heitmann frontier `gcd(deg_total P,deg_total Q)>=16`
(`COORDINATION.md:350-358`, `history/APPROACHES-overlays-20260824-30.md:4629-4631`),
but SAT-MASS does not need it. Promotion should state it, if at all, as an
external classical input with primary citations, not as a theorem established
in this lane.

What the boundary-tree section proves is narrower than its rhetoric. Lemma L5
computes the level-1 multiplicity from a Newton-polygon reading and identifies
the `L_infty` tail mass over a level-1 point in the `rho_0=0` scope
(SM:398-413). In examples such as `(x,y+x^k)`, the target elementary
subtraction is exactly the operation that removes that visible tail. This is a
correct diagnostic for a non-minimal representative.

What it does not prove:

```text
* no theorem that a D_min Keller pair has no source satellite chain;
* no theorem that non-contracted source components have nu_C=1;
* no bound on nu_C or T in terms of N;
* no functor translating the target valuation w=ord_{E0} o Phi^*
  into the source proximity tree with enough control to bound nu.
```

Thus the exact proved statement about a degree-minimal Keller pair is only:
after both automorphism factors have been minimized, no target affine/elementary
coordinate change can lower `max(deg P,deg Q)`; equivalently, in every
degree-minimal target coordinate system the leading forms pass the
`d,e>=2`, unequal-degree test. The source boundary tree may still contain
satellite tails and high `nu`; bounding them is precisely the remaining open.

## Typed Verdict Block

```text
LANE       SAT-MASS hostile review
SCOPE      Dominant polynomial maps for SAT-WEIGHT/DEG-SPLIT/LEDGER-BLIND;
           Keller + H2 + nonproper cell for W<=3 consequences; D>N wherever
           Lemma L4 or the simplified T_class formula is used.

CONFIRMED
  SAT-WEIGHT       D=sum nu_C c_C, N=sum m_C c_C, D-T=sum c_C,
                   T=sum(nu_C-1)c_C, with C strict boundary components and
                   c_C=Z.C=rho_C.  Positive excess count <= kappa+ell.
  DEG-SPLIT T      T is the extended-cluster satellite mass T_ext.  With this
                   definition D=Lambda+kappa+T for all dominant maps.
  LEDGER-BLIND     Source composition fixes the listed target/nonproperness
                   ledger and lets D,T diverge; (x,y+x^k) gives a Keller
                   invertible/non-minimal family with T=k-1.
  HALF-CAP         H2 + ell=1 + D>N gives S n=Lambda<=D/2,
                   D<=2(T+kappa), T>=D/2-kappa.  Sharp witnesses confirmed.
  SAT-CROSS        T<=tau on a degree-minimal W<=3 H2 representative gives
                   D_min<=2(tau+N); tau<=50-N closes by Moh.
  MOH-FLOOR        Noninvertible Keller => D_min>=101, as already reviewed.

GAP / REPAIR
  T_class formula  SM:132 omits rho_0.  Correct global identity:
                   T_ext-T_class = D-sum_level1 a_i-rho_0.  The charged
                   version is valid in the D>N/E_0-contracted scope.
  I12 wording      I12:27 and I12:33 say "satellite mass" without the extended
                   definition.  Binding correction: read as T_ext.
  W<=3 forcing     W<=3 forces ell=1 only in an H2 nonproper cell with S>=1.
  Ledger phrase    "every boundary-ledger entry" must exclude source-cluster
                   entries a_i, prox, r, nu, T, and T_class.
  Minimality       Target leading-form minimality is proved; source boundary
                   tree control is not.
  Classical refs   Moh is checked; the gcd>=16 package is external and
                   non-load-bearing here.

REFUTED
  Global formula   T_ext=T_class+D-sum_level1 a_i for all dominant maps.
                   Counterexample: (x+y^2,y+x^2), D=2,N=4,rho_0=2,T=T_class=0.
  Multi-dicritic   HALF-CAP without ell=1 in the ambient dominant category.
                   Refuted by (xy^2,xy), (x^2y,xy), and
                   (x,x(x-1)(x-2)y^2).
  Broad ledger     LEDGER-BLIND read as invariance of the source cluster.

MEASURED
  14-row focused SAT-WEIGHT table above: all four identities true.
  Full preserved count: 76 attempted, 74 resolved over Q, 2 irrational-cluster
  skips, 0 failures.
  T repair control: (x+y^2,y+x^2) detects the missing rho_0 term.
  HALF-CAP replay: 21 single-dicritical D>N rows, 0 violations; three
  multi-dicritical ambient refutations reproduced.
  Right-composition replay: four dominant bases plus one automorphism base,
  ledger invariant and D,T moving as charged.

OPENS
  OPEN[NU-BOUND-MINIMAL]
    Question: for a degree-minimal noninvertible Keller pair, is
    nu_C=ord_C(sigma^*L_infty) bounded above on non-contracted boundary
    components by a function of N?
    Bounded quantity: the integer nu_C in Z_{>=1}.  Equivalent to bounding
    T through T=sum_C(nu_C-1)c_C and sum_C c_C=kappa+S n.
    False without minimality: (x,y+x^k) has fixed ledger and nu=k.

  OPEN[TWO-DICRITICAL-KELLER]
    Question: under Keller+H2, can the ambient multi-dicritical failures of
    HALF-CAP occur, or can one prove |A|<=1 for
    A={dicritical l with nu_l=1}?
    Bounded quantity: |A| in {0,...,ell}.  |A|<=1 gives the weaker
    D<=4T+2kappa; the first campaign cell where ell>=2 can occur is (N,W)=(8,4).

PROMOTION
  Promote SAT-WEIGHT, DEG-SPLIT with T_ext, LEDGER-BLIND scoped to the listed
  banked ledger, HALF-CAP under H2+ell=1+D>N, and SAT-CROSS's Moh price.
  Do not promote the unqualified T_class formula, the overbroad ledger phrase,
  or any source-boundary-tree theorem from degree-minimality.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21937`.
- Body SHA-256:
  `0d6b801f66cfe9ea1f5171d1245bd3ca63e9abd242349f452425c35c57955ff9`.
- Frozen basis: `75ed98d6e6e418bd49f10a2fc29a3f592f2ee6d5`.
