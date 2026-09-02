# POLAR-CHAIN at N = 4 — the polar tree forks, E_0 is not forced to be a leaf, CH2 cannot empty the cell

**Lane.** `POLAR-CHAIN-N4`. Date 2026-09-02. Desk grok-4.6.
**Charge.** Decide whether `T_+ = supp Z` of the live `N = 4` `(B3)` object is a chain, and whether `E_0` is a leaf; if every admissible tree has `E_0` a leaf, fire `CH2` and type the cell `EMPTY` (conditional); otherwise exhibit a fork. Cross-check Domrina–Orevkov’s six global graphs. `N = 5, 6` if cheap.
**Method.** Exact integer arithmetic, sympy 1.14.0 over `ZZ`. No AWS, no `sat()`, no Groebner, no ledger edit, no `jc2-lean`, no fetch. No new exit price.

**Headline.** `OPEN[POLAR-CHAIN]` at `N = 4` `(B3)` is **NO**: `T_+` forks (`Psi > 0`). Remaining Deg `a = 2` over `v_0` (BI-1 + BI-5-Deg, no `(H-∞)`) must join the dicritical Deg-2 block inside connected `T_+` (FORK-GENUS (iii)), and cannot do so at a valency-2 vertex (DF-3). `CH2` cannot fire: `Psi = 0` and “`E_0` a leaf” are jointly impossible (`7 >= 2n + kappa >= 9`). Cell **not** emptied. DO’s six graphs are the forked candidates of `(mu, corr) = (2,1)`; DO kills them by transfer-determinants, not by `Psi > 0` (SET §§2–7, not reopened). Same join at `N = 5, 6`; graphs remain the Deg-`<=5,6` census.

## 0. Custody, typing, notation

Frozen charged inputs, hashed on this host with `shasum -a 256` **before any reading**. All five match the charge exactly:

```text
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  [frozen]/keller-pencil-genus-opus5-20260902.md
d57d17f8eb6e776013d283e6796bef0db256088011dae2b73d1383c1e40cc56a  [frozen]/keller-pencil-genus-review-grok46-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  [frozen]/horn-flagship-opus5-20260902.md
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  [frozen]/b3-boundary-instrument-opus5-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  [frozen]/sat-mass-opus5-20260902.md
```

Tags `KPG:L`, `KPGR:L`, `HF:L`, `BI:L`, `SM:L` are these copies. `BIR` is the BI review, scopes only. English Fig. 7(a–f) = Russian Figs. 20–25 (BI Control 1 reproduces them; pictures read from `refs/do.pdf` as the instrument’s source). `FALLACY-v2` in force.

**Consumed typing.** FORK-GENUS, ESCAPE-KAPPA Proof 1, CH1/CH2 at KPGR CONFIRMED (conditionals stay conditional). B3-N4 / cage / Props 3.1–3.2 at HR CONFIRMED, `SCOPE[B3-QH]`. BI-1, BI-8, BI-5-Deg at BIR CONFIRMED; BI-3/BI-5 saturation and `(H-∞)` **not** assumed. SAT-MASS only for the extended-cluster `T` definition (`SM:116-126`). No `Z(G)=1`, case (A), A2.

**Naming.** `Lambda`/`Psi` are FORK-GENUS’s (`KPG:257-273`). DO `(m,n,Deg)` is Def. 3 (`BI:110-115`); campaign `a` is sheet count. `T_+ = supp Z = Phi^{-1}(L_infty) = L̃_infty = F^{-1}(L)`. Dicritical `l=g̃` has KPG `m_l=0`, not a `T_+` vertex. `E_0` is the strict transform of source `L_infty` (DO root). Promoted cell: `N=4`, `a=W=2`, `S=1`, dicritical `(s,mu)=(1,2)`, `n>=4`, `kappa<=N`, `rho(G)=S_4`, cusp `(2|p,3|q)` or `(3|p,2|q)`, B3-N4 for `E`, BI-8 cap `#` spine-forks `<=2`. The substitution `n=4 => (g_L,theta_inf)=(0,2)` is MF-EXACT’s *minimum*, not a ceiling. Arithmetic in `ZZ` (sympy `Matrix.det` returned integers). No `sat()`.

## 1. Identities, in force

MF-EXACT (Keller + H2) with `theta_inf = kappa` (ESCAPE-KAPPA Proof 1):

```text
n (W - S)  =  N - 2 + 2 g_L + kappa .
```

At `W - S = 1`, `N = 4`: `n = 2 + 2 g_L + kappa`. Floor `n >= 4` and `1 <= kappa <= 4`, `g_L >= 0` integer, so `2 g_L + kappa >= 2` and `n - kappa` is even and at least 2.

FORK-GENUS (`KPGR:14`, `KPG:263-273`):

```text
2 g_L - 2  =  N - kappa - Lambda + Psi ,
Lambda     =  sum_{deg_{T_+}=1} m_C  +  2 sum_{deg=0} m_C   (>= 2),
Psi        =  sum_{deg>=3} m_C (deg - 2)                    (>= 0).
```

Valency is **inside** `T_+`; the dicritical (`m = 0`) is not a neighbour. POLAR-DEGREE (Keller + H2, `KPGR:119-126`): `n (W - S) = 2 N - Lambda + Psi`. The two identities agree and give the working relation

```text
Lambda - Psi  =  8 - n .
```

SHARP-CHAU (`KPGR:15,157-159`): `D >= n S + kappa = n + kappa`. Combined with `N = sum_C m_C k_C` (`KPG:229`, SAT-WEIGHT’s `N`-row, used here only as the already-CONFIRMED pairing `N = Z^2 = sum m c`): if `E_0` dominated `L_infty` then `D * k_{E_0} <= N = 4`, but `D >= n + kappa >= 5 > 4`, hence `k_{E_0} = 0`. So `E_0` is contracted, `m_{E_0} = D >= n + kappa >= 5`, and `E_0 in T_+`.

SNC at the dicritical (`KPG:245-248` (i)+(ii)): `Z.l = c_l = s n = n` and `m_l = 0`, so `n = sum_{adj} m = m_U` where `U` is the unique `T_+`-neighbour of `l` (Orevkov Lemma 2.1 as MI states it: `p̃` is a single point; SNC forbids a two-component crossing). Thus **`m_U = n >= 4`**. If `k_U >= 1` then `n k_U <= 4` forces `n = 4`, `k_U = 1`, and MF-EXACT gives `4 = 2 + 2 g_L + kappa` with `kappa >= 1`, so `g_L = 1/2`, not an integer. Hence **`U` is contracted**, `k_U = 0`, and `U != E_0` (masses `n < n + kappa <= D`).

BI-1 (`BIR:15,109-113`, no `(H-∞)`): `W + a = N`. BI-5 Deg (`BIR:19,135-137`, no `(H-∞)`): non-dicritical Deg over `v_0` equals `a`. Lemma 6 / Prop. 1: the dicritical-incident block has Deg `= s mu = 2`. Together, Deg over `v_0` is `2 + 2 = 4`. BI-8 (`BIR:22,163-169`): `#` spine-forks `<= a = 2`, a cap.

det `= ±1`: the dual graph of the source compactification `L̃` is unimodal (`do.pdf` p. 1; Russian authority `det L̃ = -1` as in the charged replay). This is the coarse lattice condition, not DO’s transfer identities.

## 2. Every numerical type. CH2 cannot fire

Desk enumeration of MF-EXACT + FORK-GENUS + the floors, `g_L <= 11` (the list is infinite in `g_L` without a bound on `Psi`; that is `OPEN[FORK-MASS]`, not closed here):

```text
 n  kappa  g_L  Lambda-Psi  D>=   Psi>=   Psi if E_0 a leaf
 4    2     0       4        6      0            3
 5    3     0       3        8      0            6
 6    4     0       2       10      0            9
 5    1     1       3        6      0            4
 6    2     1       2        8      0            7
 7    3     1       1       10      1           10
 8    4     1       0       12      2           13
 ...  (g_L >= 2 continues; Psi floor grows; no CH2 row)
```

The primary promoted substitution is the first row: `(n, kappa, g_L) = (4, 2, 0)`, `Lambda - Psi = 4` (`KPG:394`, `KPGR:117,322-323`).

**CH2 arithmetic, all rows with `n >= 4`.** CH2 is `Psi = 0` **and** `E_0` a leaf of `T_+` (`KPGR:16,167-183`; the producer’s CHAIN-CEILING with both hypotheses, `KPG:289-296`). Then `Lambda = 8 - n` and `Lambda >= D + 1 >= n + kappa + 1`, so

```text
8 - n  >=  n + kappa + 1     =>     7  >=  2 n + kappa  >=  8 + 1  =  9.
```

Contradiction for every integer `n >= 4`, `kappa >= 1`. **CH2’s two hypotheses are jointly impossible.** The implication “`E_0` a leaf `=> n W <= 2N-2`” uses `Psi=0`; it does not fire on a fork, and a chain with `E_0` a leaf is the same empty pair. A false conjunction does not empty the cell. The same obstruction holds at `N=5` (`2n+kappa <= 9` vs `>=11`) and both `N=6` profiles (`3n+kappa <=11` vs `>=13`; `2n+kappa <=11` vs `>=13`). Not a `(B3)` kill.

**Chain arithmetic, independently.** On a chain, `Psi = 0`, `Lambda = 8 - n <= 4`. If `E_0` is a leaf, `Lambda >= D + 1 >= n + 2`, so `8 - n >= n + 2`, `n <= 3`, contradicting the floor. If `U` is a leaf, `Lambda >= n + 1`, same contradiction. So **every chain has both `E_0` and `U` interior** (valency 2). That is the only remaining chain shape; it is excluded in §3 by connectedness, not by this mass count.

## 3. `T_+` is not a chain

**THEOREM (POLAR-CHAIN at `N = 4` `(B3)`).** For a noninvertible Keller map under `H2` in the live `N = 4` `(B3)` cell, `T_+` is not a chain: `Psi > 0`.

*Proof, consumed statements only.*

1. BI-1 (`BIR` CONFIRMED, hypotheses Keller, `H2`, 7.B'; no `(H-∞)`): `W + a = N`, so `a = 2`.
2. Dicritical block Deg `= s mu = 2` (DR Lemma 6 / Prop. 1, extracted as BI’s spine start, `BI:357-358,666-674`; BIR CONFIRMED for BI-8’s hypotheses DF-2, DF-3, Lemma 6).
3. BI-5 Deg (`BIR` CONFIRMED, no `(H-∞)`): non-dicritical components over `v_0` carry Deg `= N - W = a = 2`. F-constant components are already absent from that sum.
4. Those non-dicritical components dominate `v_0`, a component of target `L`, hence lie in `F^{-1}(L) = L̃_infty = T_+`. The Deg-2 dicritical-incident block likewise lies in `T_+` (it meets `g̃` at `p̃ in L̃_infty`).
5. FORK-GENUS (iii) (`KPG:249-251`, `KPGR` CONFIRMED): `T_+` is a subtree. Keller’s generic pencil member is irreducible, so after blowing up the `theta_inf` base points the fibre `pi^{-1}(infty)` is connected and its image is `T_+`.
6. Let `Delta` be the maximal constant-Deg block of `T_+` incident at `g̃`; it has Deg 2. The remaining Deg 2 over `v_0` is *not* in `Delta` (maximality). If it formed a separate component of `T_+`, step 5 would fail. If it joined `Delta` at a valency-2 vertex, that vertex would merge two distinct maximal blocks while remaining a tube: forbidden by DO Prop. 4 / DF-3 (`BI:141-145`, `BIR` CONFIRMED as BI-8’s DF-3: source valency equals target valency iff `m = 1` iff every incident chain has Deg `= m n`; a valency-2 vertex has two arms, not a merge).
7. Therefore the remaining Deg 2 joins `Delta` at a vertex of `T_+`-valency `>= 3`. That vertex contributes positively to `Psi`. ∎

**Scope of the theorem.** No `(H-∞)`. No Corollary 4 (the join is a fork whether or not it is Deg 2; Cor. 4 only names its Deg, and is the mark-side use BIR flagged as exposed to BI-ATTACH). No B3-N4 puncture signs. No `SCOPE[B3-QH]`. Conditional on the extracted DF-3 / Prop. 4 tube statement as BIR promoted it for BI-8, and on FORK-GENUS (iii). If DF-3 were withdrawn, the join argument would stop and the chain shape of §2 (interior `E_0`, interior `U`) would return as OPEN, bounded by the number of vertices of `T_+` in `[4, #L̃]`.

**Corollary.** CH1 (`Psi = 0 => n(W-S) <= 2N-2`) does not apply. Combined with §2, **neither CH1 nor CH2 constrains this cell.** No EMPTY window is produced. This is not a disagreement with the KPG control `Lambda - Psi = 4`; it is the determination that the mass `4` is carried with `Psi > 0`, `Lambda >= 5`.

**Desk check (not used in the theorem).** Interior-`E_0`/`U` chains, `r<=6`, masses `<=10`, `E_0^2=-1`, other `C^2<=-1`, no contracted `(-1)` except `E_0`: SNC examples exist, **zero** have `det A` or `det(-A)` in `{±1}`. A `Y` at `(n,kappa,g,Lambda,Psi)=(4,2,0,8,4)` with `(m,k,C^2)` equal to `L0(2,0,-3)--E_0(6,0,-1)--F(4,0,-3)--U(4,0,-1)` and a side leaf `V(2,2,-1)` is SNC-integral; `det A=-(ell2+1)` never `±1`. The six DO graphs are the shapes that pass coarse det and fail transfer (§5).

## 4. Solutions by `(n, kappa, g_L, Lambda, Psi, shape)`

The identities plus §3 give the complete numerical-and-shape list at `N = 4`. `Psi > 0` is forced; `Lambda = Psi + (8 - n)`; `n = 2 + 2 g_L + kappa >= 4`; BI-8 caps spine-forks by 2. `E_0` is in `T_+`, contracted, not forced to be a leaf (a leaf would force `Psi >= 2 n + kappa - 7 >= 3` at the primary row, consistent with §3 but not implied by it).

**Primary row** `(n, kappa, g_L) = (4, 2, 0)`, `Lambda - Psi = 4`, `D >= 6`:

| shape | spine forks | first-fork Deg | `Psi > 0` | `E_0` a leaf of `T_+` | source |
|---|---:|---:|---|---|---|
| chain | 0 | — | no | impossible (§2) | excluded, §3 |
| English 7(a) = Ru 20 | 1 | 4 | yes | not forced | DO Cor. 5 |
| English 7(b) = Ru 21 | 1 | 4 | yes | not forced | DO Cor. 5 |
| English 7(c) = Ru 22 | 2 | 3 then 4 (`3+1`) | yes | not forced | DO Cor. 5 |
| English 7(d) = Ru 23 | 2 | 3 then 4 (`3+1`) | yes | not forced | DO Cor. 5 |
| English 7(e) = Ru 24 | 2 | 3 then 3 | yes | not forced | DO Cor. 5 |
| English 7(f) = Ru 25 | 2 | 3 then 3 | yes | not forced | DO Cor. 5 |

The six are the complete `L̃` types for `(m,n)(g̃)=(1,2)` under DO’s assembly (BI Control 1; BIR: SET not reopened). Tubes are valency-2 (free in `Lambda`/`Psi`); the black vertex is `g̃`; the Deg-2 tube ends at `U`, a `T_+`-leaf of mass `n`. `E_0` is the root, in `T_+`, outside `Delta` on Figs. 20–21 (Lemmas 13–14), not thereby a leaf: OPEN per graph, bounded `{0,1}`.

KPG `(m_C,k_C)` is not DO `(n,m)` on every vertex: identifying them on Fig. 7(a) yields `Lambda-Psi=n+1=8-n` for no integer `n`. Dominating multisets for `kappa=2` are `{(2,2)}`, `{(1,1),(3,1)}`, `{(2,1),(2,1)}`. Other MF-EXACT rows (`n>=5`) have the same six shapes, `Psi>0`, `Lambda=Psi+(8-n)`. Unbounded `g_L` is `OPEN[FORK-MASS]`. Dicritical: DO `(1,2)`, KPG `m_l=0`, `c_l=n`, neighbour `U` with `m_U=n`, `k_U=0`.

## 5. Cross-check: which of the six, and how DO kills them

The live `(B3)` `N = 4` object *is* Orevkov’s one-dicritical profile `(mu, corr) = (2, 1)` (BI Control 1(a), BIR CONFIRMED, N4-PIN, no Orevkov Lemma 4.2). Its polar tree is **one of the six**, not a seventh shape: Cor. 5’s assembly from the maximal Deg-2 block, with Cor. 4 excluding a Deg-2 *first* fork, produces exactly Figs. 20–25 (`BI:479-481`, `BIR:68,208-210`). This lane does not pick a single one; the affine ledger meets the census only at `v_0` and does not shorten the six (`BI:472-491`).

DO’s own kill of all six is a **determinant obstruction**, not `Psi > 0`:

```text
Figs 24-25 = 7(e,f): Lemma 10, (7.3)   -2 d_2 = 18 delta^2 - 2 d_2 - 6 y delta^2
                                       vs  y > 4,  so y = 3 contradiction.
Figs 22-23 = 7(c,d): Lemma 11, (7.6)   odd  -1  =  even
                                       (det L̃_infty = -2, det L = -1).
Figs 20-21 = 7(a,b): Lemmas 12-15, (7.10)  -1 = -B - alpha C  <= -4.
```

None of (7.3), (7.6), (7.10) is a fork-mass identity. All six already have `Psi>0`; DO kills the transferred branch determinants, not the forks. SET §§2–7, **not reopened**. Not a CH2 EMPTY. Withdrawing Cor. 4 still leaves a fork; a chain would need DF-3 or connectedness to fail (§3).

## 6. `N = 5` and `N = 6`, cheap

BI’s profile lists (`BI:554-616`; BIR: no empty window, `N = 6` charged types 9 not 8) are:

```text
N=5: a=3, W=2, dicritical (1,2), meridian 1^3·2; three charged-point profiles.
N=6: a=3, W=3, dicritical (1,3), meridian 1^3·3; two charged profiles.
     a=4, W=2, dicritical (1,2), meridian 1^4·2; six charged profiles
     (BIR: nine types, one missed cell at cap 3).
```

The join of §3 uses `N` only through `a=N-W`. At every one-dicritical `(B3)` profile, remaining Deg over `v_0` is `a>=2`, so **`Psi>0` at `N=5` and both `N=6` cells**. CH1/CH2 do not apply; CH2 is instance-free (§2). No EMPTY (agrees with BI/BIR). Graphs at Deg `<=5,6` are `OPEN[BI-CENSUS-DEG5-DEG6]`: `Census(5)=86`, `Census(6)=287`. Spine data: start Deg `2` or `3`, depth `<=a in {3,4}`, `Psi>0`. The `v_0` list `{(1,1,1),(1,2),(3)}` is not licensed (BIR: unramified infinity fibre is an `N=4` B3-N4/`(H-∞)` input).

## 7. FALLACY-v2

Flag/place/series: `n`, `D`, `N`, `kappa`, `g_L`, `Lambda`, NVM-`Lam`, `Psi`, `T`, DO-`(m,n,Deg)` never identified; `T_+`, `L̃_infty`, dicritical, `E_0`, `U` kept apart. Per-ray: each `T_+` edge once (FORK-GENUS). Carrier: six graphs `REPRESENTATIVE`, not a realisation. Floors: MERIDIAN-FLOOR+, SHARP-CHAU, `n=4` minimal not attained; BI-8 a cap; CH2 unused. SNC at `l` only after the dicritical vertex class; `(H-∞)` not assumed. `sat()` unused. DO `(m,n)` vs KPG `(m_C,k_C)` declared in §0. No EMPTY by vacuous CH2; Cor. 4 not used to exclude chains; DO kill not re-derived. No `charge_basis`.

## 8. Typed verdict block

```text
LANE     POLAR-CHAIN-N4
SCOPE    Keller, noninvertible, H2, case (B3), N=4 primary; N=5,6 by the
         same join. SCOPE[B3-QH] unused. (H-∞) not assumed. No Z(G)=1,
         no case (A), no A2, no jc2-lean, no ledger edit. No exit price.

ANSWER   OPEN[POLAR-CHAIN] at N=4 (B3): NO.  T_+ is not a chain; Psi > 0.
         Bounded quantity was # of valency>=3 vertices of T_+, in
         [0, #L~ - 2]; the answer is an integer >= 1 (exactly 1 or 2
         spine-forks on the six graphs, BI-8 cap 2).
         E_0 is in T_+, contracted, not forced to be a leaf.
         CH2 cannot fire (Psi=0 and E_0 a leaf jointly impossible:
         7 >= 2n+kappa >= 9). CH1 does not apply. Cell NOT EMPTY
         by this lane.

CHAIN OF CONSUMED STATEMENTS (T_+ not a chain)
         BI-1 (BIR CONFIRMED; Keller, H2, 7.B'; no (H-∞))
         BI-5 Deg (BIR CONFIRMED; no (H-∞)): non-dicritical Deg over
           v_0 equals a = 2
         DR Lemma 6 / Prop. 1: dicritical block Deg = s mu = 2
         FORK-GENUS (iii) (KPGR CONFIRMED): T_+ a subtree, connected
         DF-3 / Prop. 4 (BIR CONFIRMED as BI-8 hypothesis): a valency-2
           vertex is a tube, not a merge of distinct maximal blocks.
         Not used: (H-∞), Cor. 4, B3-N4 puncture signs, SAT-MASS
           except the T definition, Z(G)=1.

FORK WITNESS
         Any of English Fig. 7(a-f) = Russian Figs. 20-25.  Concrete
         identity-level Y at (n,kappa,g,Lambda,Psi)=(4,2,0,8,4) with
         vertices (m,k,C^2)
           L0(2,0,-3)--E_0(6,0,-1)--F(4,0,-3)--U(4,0,-1)
                                      |
                                      V(2,2,-1)
         and dicritical at U; SNC holds; coarse det A = -(ell2+1)
         never ±1 (so it is not a compactification). The six graphs
         are the ones that pass coarse det. Datum that excludes a
         given six-graph: the matching identity (7.3)/(7.6)/(7.10).

DO CROSS-CHECK
         The polar tree of (mu,corr)=(2,1) is one of the six; the
         affine ledger does not select among them. DO kills all six
         by transfer-determinant identities, not by Psi>0. SET §§2-7,
         N=4-CHECKED-CLOSED, not reopened. Not a CH2 EMPTY, not the
         first (B3) EMPTY window.

N=5,6    Same join: Psi>0, CH1/CH2 do not apply, CH2 instance-free
         arithmetically. No EMPTY (agrees with BI/BIR). Exact graphs
         = OPEN[BI-CENSUS-DEG5-DEG6], bounded Census(5)=86 and
         Census(6)=287 raw rows; do not use the n=1 v_0 list.

NOT CLAIMED  any (B3) EMPTY; any unconditional ceiling; Psi=0;
             E_0 a leaf; (H-∞) at any N; KPG (m,k) = DO (n,m) on
             every vertex; a bound on Psi (OPEN[FORK-MASS] stands);
             reopening of the DO (2,1) kill.

MEASURED  sympy 1.14.0, ZZ. MF-EXACT x FORK-GENUS grid g<=11 (47
          rows); CH2 obstruction 7>=2n+kappa>=9 at N=4 and the N=5,6
          analogues; dominating (m,k) partitions of N=4 for kappa=1..4;
          chain SNC r<=6 m<=10 (0 minimal unimodular); Y and deg-4
          fork SNC solutions and det A never ±1.

OPENS    OPEN[FORK-MASS] restated, not closed: integer Psi-Lambda
           = 2g_L-2-N+kappa, Lambda>=2, 1<=kappa<=N, Psi>=0.
           POLAR-CHAIN at N=4 is answered, so CH1 is unavailable;
           the ceiling still sits on this integer.
         OPEN[E0-LEAF-ON-SIX] per graph, bounded {0,1}: is the root
           a T_+-leaf on English 7(a-f)? Not needed for CH2.
         OPEN[BI-CENSUS-DEG5-DEG6] carried, sizes 86 and 287.
         OPEN[BI-TAIL-AT-INFINITY] carried, now including N=4;
           bounded one yes/no per dicritical. Unused here.

SUCCESSOR  OPEN[FORK-MASS] (a bound on Psi, not a chain theorem),
           in parallel with OPEN[SING-WITNESS] as KPGR directed,
           and the Deg<=5 census if a graph-level (B3) kill is
           wanted at N=5. Do not attempt CH2 at N=2W: the
           hypotheses are jointly empty there.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19464`.
- Body SHA-256:
  `514149c5a7cacf30a390b19865593437cc9ef936a7ed8e992a05ec0e3ce5c71c`.
- Frozen basis: `f604fdda6f851fee6423822c54cdd8c2894ccebd`.
