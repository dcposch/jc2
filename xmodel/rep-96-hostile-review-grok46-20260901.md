# Hostile review: REP-96-INNER — THEOREM CABLE-3 and the survives-verdict

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-01.
**Lane.** `REP-96-HOSTILE-REVIEW`.
**Charge.** Default to refutation. Desk-scale exact reasoning plus finite `S_4` / Puiseux / Hurwitz scripts as confirmation of hand computation. No Groebner basis, no resultant, no `sat()`, no `jc2-lean`, no ledger edit. `FALLACY-v2` in force. No `charge_basis` line: this review asserts no new exit price.

A false “survives” here misdirects the campaign’s heaviest resources; a false class list poisons the braid-monodromy successor; a missed §6 kill wastes everything downstream. Load-bearing novelties attacked first: the §2 winding argument, the ordered-product claim, the exponent ledger `e(delta_3^{k_*})=2k_*`, and the §5 class lists (brute enumeration, counts printed verbatim).

**Verdict.** `PROMOTE-WITH-REPAIRS`.

| Claim | Review |
|---|---|
| THEOREM CABLE-3 / GATE-3 | **CONFIRMED** at written scope `(d,n)=(3g,2g)`, one pair at infinity |
| Both live `(9,6)` types SURVIVE GATE-3 | **CONFIRMED** (`k_*=-10,-8` even; both `3 nmid k_*`) |
| Survive every other promoted gate (§6) | **CONFIRMED**; no missed kill found against the rowkill / SHAPE-KILL / N-A / `(M')` theorem list |
| §5 class lists: 6 classes (144 tuples) for `(9,6,2)`, 3 classes (72) for `(9,6,4)` | **CONFIRMED**, exact, no more no fewer |
| §7 fork (BM / source-is-C2 / `M'`-companion) | **CONFIRMED**; `(7.1)`, `a_p∈{0,1,2}`, Pi-tau pin, two-symbols-`b` all hold |

Three repairs are required before the document is a clean successor source. None of them moves a survives-verdict, a class, or the theorem. They are specified in §7.

---

## 0. Hash verification, inputs, method

Frozen copies were hashed with `shasum -a 256` **before any reading**. All three match the charge exactly:

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  encoding-faithfulness-audit-r2-sol56-20260901.md
```

Below: **REP** = the charged inner report, **RK** = the rowkill coordinator integration, **AUD** = the encoding-faithfulness audit. Campaign documents consumed on disk and cited by file and section, not re-hashed as primary: `shape-kill-uniform-opus5-20260901.md` §§3.1–3.4; `pi1s4-close-residual-r2-opus5-20260831.md` §3.1–3.2 (tubular factorisation, Lemma 3.3); `pi1-s4-decision-opus5-20260831.md` §§1–2; `nori-bc-extension-opus5-20260831.md` §3.5; `round1033-sheet-gate-opus5-20260831.md` §7 (`(M')`/`(M'-def)`/block-free form); `row-86-prebuild-opus5-20260901.md` §5 Control 2; `reducible-all-n-opus5-20260901.md` `:130-134`, `:459`. No charged file was edited.

**Method.** Independent re-computation of: Galindo census; truncated Puiseux over `Q` of both `(9,6)` curves and the ROW-NF sextic at `b=c=1`; family-2 block algebra at `d'=3` (conjugator `Pi Pi_{d'}^{-1}`, ordered product `beta=iota_2 iota_3 iota_1`, `h=Y X^2 Y`); exhaustive `S_4` enumeration (`60` outer, `1080` pairs, `delta_3^k c_h` for every residue, conjugacy classes at `k=-10,-8`); the same at `g=2` including `E=-3`; block-free `(M')` and the Pi-tau pin. Permutation words compose right-to-left; Hurwitz is the promoted left action, `(beta gamma)·T=beta·(gamma·T)`. Charge paced 20–30 KB; the overrun is the verbatim GATE-3 table (`k=0..-12`) and the from-scratch CABLE-3 algebra the charge required kept.

---

## 1. Task (1): census, winding, ordered product, exponent ledger

### 1.1 Galindo conversion and the §1 census — CONFIRMED

`(d,n)=(9,6)`, `a=d-n=3`, `g=gcd(d,n)=3`, `d'=3`, `n'=2`, `p_a=(d-1)(d-2)/2=28`. AUD §3 (quoting NODAL-REALIZATION) gives `beta_1=d^2/g-c=27-c` and, for one place with a single characteristic pair `(a;beta_1)`, `gcd(a,beta_1)=1`,

```text
delta_inf = (a-1)(beta_1-1)/2 = beta_1-1 ,
delta_aff = 28 - delta_inf = 29 - beta_1 ,
M_inf = a + beta_1 - 1 = beta_1 + 2 .
```

| type | `c` | `beta_1` | `delta_inf` | `delta_aff` | `M_inf` | `S_aff` gaps | Frobenius |
|---|---:|---:|---:|---:|---:|---|---:|
| `(9,6,2)` | 2 | 25 | 24 | 4 | 27 | `{1,3,5,7}` of `<2,9>` | `7=2*4-1` |
| `(9,6,4)` | 4 | 23 | 22 | 6 | 25 | `{1,2,3,5,7,11}` of `<4,6,9>` | `11=2*6-1` |

Both semigroups were enumerated from the generators, independently of REP: four gaps and six gaps respectively, both symmetric, and `delta_aff+delta_inf=28` on both rows. `gcd(3,25)=gcd(3,23)=1`. This is REP’s table, recomputed from the conversion and from the affine semigroups, not copied.

### 1.2 `k_*` from the curves — CONFIRMED, including the vanished `k=±2` on `(9,6,2)`

Affine coordinates `x=p(t)`, `y=q(t)`. Chart at infinity: `z=1/t`, `P(z)=z^d p(1/z)`, `Q(z)=z^n q(1/z)`, `xi=x^{1/d}`, invert `z=xi^{-1}P(z)^{1/d}` as a series in `u=xi^{-1}`, then `y=sum_k c_k x^{k/d}`. Truncated polynomial inversion over `Q` (Newton for `P^{1/d}` and `P^{-n/d}`, no floating point) returns:

```text
(9,6,2)  p=t^9+12t^5+24t, q=t^6+8t^2
         nonzero k = 6, -6, -10, -14, ...     k_* = -10
         (k=2 and k=-2 vanish)

(9,6,4)  p=t^9+3t^7+(21/4)t^5+(35/8)t^3+(63/32)t ,
         q=t^6+2t^4+(5/2)t^2
         nonzero k = 6, 0, -8, -10, ...       k_* = -8

(6,4)    ROW-NF at b=c=1:  k_* = -5
```

`k_*` is the largest `k` with `a nmid k`. REP’s initial segments match, including the Abhyankar–Moh vanishing of `k=±2` on `(9,6,2)`. The relation `k_*=2d-a-beta_1` then gives `beta_1=15-k_*∈{25,23}`, matching §1.1 with no conversion in the loop.

Realized curve, re-checked exactly: `p^2-q^3-64q-64t^2=0`, `deg(p,q)=(9,6)`, `gcd(p',q')=gcd(p,p')=1`. Four nodes: `p` odd, `q` even, so `{t,-t}` collide iff `p(t)=0`, `t≠0`, i.e. `w=t^4` a root of `w^2+12w+24`, `w=-6±2sqrt(3)`; the two families have distinct `q^2=w(w+8)^2=-48∓16sqrt(3)` (numerically `q∈{±8.70131 i, ±4.50413 i}`), `p'≠0`, exhausting `delta_aff=4`. All eight node parameters are the nonzero roots of `p`, so all four nodes lie on `x=0`; residual smooth point `t=0`; fibre multiplicity `2·4+1=9=d`. Eight simple vertical tangencies: `p'=3(3t^8+20t^4+8)` has two distinct nonzero `t^4`-roots (disc `304/9`), none a node, eight distinct `p`-values (the two families have distinct `p^4`). Ledger `8·1+4·2=16=2 delta_aff+d-1`. Plücker `m=72-(8+50)=14` on `(9,6,2)` and `72-(12+46)=14` on `(9,6,4)`: a check, not an obstruction.

### 1.3 Family-2 block structure at `g=3`, re-derived — CONFIRMED (not family 3)

`(9,6)=(3·3,2·3)` is family 2 with reduced shape `(d',n')=(3,2)`, `u=3` odd, **not** family 3. PB’s `3`-periodic products, `e(C_2(delta_4^3))=36` at `d'=4`, and gate `3|e(iota)` are `(4,3)`-shape statements and are not used. Promoted tubular factorisation (`pi1s4-close-residual-r2` (3.1)–(3.2)):

```text
rho_inf = C_3(delta_3^2) · iota ,    iota in B_{3,1}×B_{3,2}×B_{3,3} ,
e(C_3(delta_3^2)) = g^2 n'(d'-1) = 9·2·2 = 36 ,
e(rho_inf) = 2 delta_aff + d - 1 ,
e(iota) = (d-1)+2 delta_aff - n(d-g) = 2 delta_aff - 28 .
```

`(9,6,2)`: `e(iota)=-20`. `(9,6,4)`: `e(iota)=-16`.

**Outer datum / parity.** `A'(2)`: `BP` is `2`-periodic, `X:=Pi_1=Pi_3`, `Y:=Pi_2`; `r=d' mod n'=1` so conjugation by `Pi` shifts by `-1`. Total product `Pi=XYX` and the first conjugation yield `XYX=YXY` — SHAPE-KILL (3.1) at `m=1`, an identity at `u=3` not a transplant. Each block product is `g=3` transpositions, hence odd; `sgn(Pi)=(-1)^9=-1`, so `Pi` is never in `V_4` (SHAPE-KILL §3.3 item 1 / §3.4: no surviving odd-`g` family-2 row admits the `S_3` descent). Confirmed on all `60` outer solutions.

**Block-level cable action.** Left Hurwitz: `delta_3=sigma_1 sigma_2` acts by

```text
delta_3 · (u1,u2,u3) = ((u1 u2) u3 (u1 u2)^{-1}, u1, u2) .
```

The conjugator is `u1 u2 = Pi Pi_{d'}^{-1}`, **not** `Pi`. Lemma 3.3 cabling then gives REP’s (2.4):

```text
C_3(delta_3) · (B1,B2,B3) = (c_{P1 P2}(B3), B1, B2) .
```

Internal check, re-run: on block products `(X,Y,X)`, one application yields `(XYX(XY)^{-1}, X, Y)=(Y,X,Y)` by the braid relation; a second returns `(X,Y,X)`. `C_3(delta_3^2)` preserves the block-product sequence. A mis-assigned conjugator (`Pi` in place of `Pi Pi_3^{-1}`) would send the first slot to `c_{XYX}(B3)=c_{Pi}(B3)` and break the round trip.

### 1.4 Ordered-product claim — CONFIRMED (the algebraic novelty holds)

Write `T=(T1,T2,T3)` in blocks, `S=iota·T` so `S_i=iota_i·T_i` with the same block products. `rho_inf·T=T` reads `C_3(delta_3^2)·S=T`. Applying (2.4) twice, with block products `(X,Y,X)` before the first application and `(Y,X,Y)` before the second:

```text
C_3(delta_3) · S = (c_{XY}(S3), S1, S2) ,
C_3(delta_3^2) · S = (c_{YX}(S2), c_{XY}(S3), S1) = (T1, T2, T3) .
```

Hence `T1=c_{YX}(S2)`, `T2=c_{XY}(S3)`, `T3=S1`. Conjugation commutes with Hurwitz (the action is by words in the entries), so composing around the cycle `T1←T2←T3←T1` gives

```text
T3 = iota_1 · T1 ,
T2 = (iota_3 iota_1) · c_{XY}(T1) ,
T1 = (iota_2 iota_3 iota_1) · c_{(YX)(XY)}(T1) ,
```

i.e. `T1=beta·c_h(T1)` with `beta:=iota_2 iota_3 iota_1∈B_3` and `h=(YX)(XY)=Y X^2 Y`. **Only the ordered product `beta` survives; the distribution of `iota` among the three tubes is invisible to (3.1).** Its exponent sum is `e(beta)=e(iota)`.

Finite check of the two-fold cabling word against the braid relation; no Puiseux data. Attack: the three copies of `B_g` act on different strand sets. Reply: after `c_{XY}`, `c_{YX}` identify the `S_4`-labels, Hurwitz is the abstract action of `B_3` on `3`-tuples; the remaining strand-identification ambiguity is conjugacy in `B_3`, which (3.1) absorbs by replacing `T1` with a `B_g`-orbit point. CONFIRMED.

### 1.5 Winding argument — CONFIRMED, with the exponent pinning the sign

This is the other load-bearing novelty. Attack points, in order.

**(i) Formula `k_*=2d-a-beta_1`.** In the chart `(v,u)=(y/x, 1/x)` at `P_inf`, the place is `v=s^a`, `u=sum_{k≥d} c_k s^k` with first non-`a`-divisible exponent `beta_1` (AUD’s local `y` is this `u`; AUD’s local `x` is this `v`). Then affine `y=v/u=s^{a-d}U^{-1}`, `U=sum c_k s^{k-d}`, and the first non-`a`-divisible power `s^{beta_1-d}` survives inversion. With `s∼x^{-1/d}` the corresponding affine exponent is `k=2d-a-beta_1`. Every later non-`a`-divisible exponent `m>beta_1` in `u` produces a strictly smaller `k`. So `k_*` is exactly that value. At `(9,6)`, `k_*=15-beta_1`. This keeps four objects at `P_inf` apart (FALLACY flag/place/series): contact `d=9`, multiplicity `a=3`, characteristic numerator `beta_1∈{25,23}`, affine second exponent `k_*∈{-10,-8}`.

**(ii) Rigid rotation.** Over `|x|=R` the `9` roots fall into `d'=3` blocks of size `g=3` by leading term `x^{2/3}`. Within a tube the mean retains the `3|k` terms; the deviations at the largest `3 nmid k`, namely `k_*`, are the vertices of an equilateral triangle (`zeta_3^{k_*}` primitive iff `3 nmid k_*`, the one-place condition). Dominance as `R→∞` makes the tube an asymptotically regular `3`-gon. As `x` traverses one loop, `x^{k/9}↦x^{k/9}zeta_9^k`; after **three** loops a tube returns and the leading deviation is multiplied by `zeta_3^{k_*}`, i.e. the triangle turns through `k_*/3` full turns.

**(iii) Dual Garside.** `delta_g:=sigma_1…sigma_{g-1}`, `e(delta_g)=g-1`, and `delta_g^g` is the full twist (dual Garside: `δ^n` is the full twist in `B_n`). Rotation of a regular `g`-gon by `1/g` turn is `delta_g`; `k_*/g` full turns is `delta_g^{k_*}`. Blackboard cabling is already factored off as `C_3(delta_3^2)`, so it adds no inner twist. The three-loop accumulated inner braid of a tube — which is the Hurwitz word `beta`, up to conjugacy in `B_g` from the choice of basepoint tube and strand labelling — is therefore conjugate to `delta_g^{k_*}`.

**(iv) Sign and extra twists.** `e(delta_g^{k_*})=k_*(g-1)=2k_*` at `g=3`. Independently `e(iota)=2k_*` by (2.2) plus (i). An identification `beta∼delta_g^{-k_*}` would have the opposite exponent and is excluded unless `k_*=0`. An extra full twist `delta_g^{k_*+mg}` would shift the exponent by `m g(g-1)=6m`, contradicting `e(beta)=2k_*` unless `m=0`. So conjugacy class in the Hurwitz action is pinned to `delta_g^{k_*}` once rigidity supplies “a power of `delta_g`” rather than “some braid of that exponent.”

**(v) Individual `iota_i` are not pinned** — a feature, not a gap. `e(iota_i)` need not be `2k_*/3` (and cannot be: `3 nmid k_*` makes that non-integral). Only the ordered product is a geometric rotation. At `g=2` the tube group is abelian and the distinction collapses; at `g=3` it is why SHAPE-KILL §3.3 predicted an exponent-sum gate would be vacuous.

**(vi) Controls.** Two `(9,6)` Puiseux expansions give `k_*=-10,-8`; the ROW-NF sextic at `b=c=1` gives `k_*=-5`; Route 1 gives `e(iota)=-20,-16,-5`, matching `e(delta_g^{k_*})`. The identity `(d-1)^2-(a-1)(beta_1-1)-n(d-g)=(2d-a-beta_1)(g-1)` holds identically on family 2 at `u=3`. CONFIRMED.

### 1.6 Outer solution set — CONFIRMED, with one table-cell error (repair R1)

Solving `XYX=YXY` over the `12` odd elements of `S_4` gives exactly **`60` pairs**, no mixed transposition/`4`-cycle solutions, in four strata of sizes `6, 6, 24, 24`. `A'(4)` (`Pi^{n'}=Pi^2∈Z(<Pi_1,Pi>)`) holds on all `60` (information-free at this shape). Independent cycle types:

| stratum | count | `W=XY` | `Pi=XYX` | `h=Y X^2 Y` |
|---|---:|---|---|---|
| `const-T` | 6 | `e` | transposition | `e` |
| `const-4c` | 6 | double transposition (`X^2`) | `4`-cycle (`X^{-1}`) | `e` |
| `noncst-T` | 24 | `3`-cycle | transposition | `e` |
| `noncst-4c` | 24 | **`3`-cycle** | transposition | double transposition |

REP’s table matches except the `W` column of `noncst-4c`: REP writes “double transposition”; the actual value, on all `24` pairs and on the displayed representative `X=(1234)`, `Y=(1243)`, is the `3`-cycle `XY=(132)` (and `YX=(142)`). The `h` column on that row is correctly a double transposition (`h=(13)(24)` for the displayed pair). GATE-3 and §5 do not consume `W`’s cycle type on this stratum — they consume `h` and the enumeration — but a successor reading the table as data would be poisoned. Repair R1.

`const-T` is dead at every `k` for full image: here `W=e`, so (3.2) gives `im(phi)=<T1>`, and three transpositions with product a transposition generate a subgroup of order in `{2,4,6}` (independent census: `6+18+96` such triples, **zero** of image `S_4`). The parenthetical “order at most `6`” is true, not merely “not `S_4`”. The chain `(12)(23)(34)` generates `S_4` but has product a `4`-cycle, so it is not a `const-T` triple. This is the `g=3` replacement for Lemma SK-2, proved on its merits; SHAPE-KILL §3.3 item 3 correctly forbids transporting SK-2 (the block `(tau,tau)` is not `B_g`-fixed for `g≥3`).

---

## 2. Task (2): three routes, four controls — CONFIRMED, including the `E=-3` kill

**Route 1 (discriminant).** `e(rho_inf)=2 delta_aff+d-1` unconditionally (each affine singularity contributes `2 delta_p+(m_p-r_p)`, and `sum(m_p-r_p)` plus smooth vertical tangencies is the ramification `d-1` of `p:P^1→P^1`). Subtract `36` to get (2.2). `(9,6,2)`: `-20`. `(9,6,4)`: `-16`.

**Route 2 (Puiseux winding).** `(2.3)` gives `e(iota)=k_*(g-1)=2k_*` with `k_*=15-beta_1`. Same two values. The identity behind the agreement is the polynomial of §1.5(vi).

**Route 3 (from the curves).** §1.2: `k_*=-10,-8` by exact series, no conversion in the loop.

**Control 1 (one place at infinity).** Permutation of `C_3(delta_3^2)` is three disjoint `3`-cycles (blackboard cabling preserves within-block order; tube permutation is a `3`-cycle). Composite with `iota` is a `9`-cycle iff `3 nmid k_*`. Holds on both rows (`k_*=-10,-8`). Equivalent to `gcd(k_*,3)=1`, which is the definition of `k_*` together with `a=3`.

**Control 2 (promoted `(6,4)` row, positive and negative).** Independent enumeration, same conventions:

- Outer solutions of `XYX=YXY` in `A_4`: **`36`**, of which **`24`** are the SK-4 non-constant `3`-cycle pairs.
- On every one of those `24`, `h=Y X^2 Y=X` and `Pi=WX` is a double transposition, reproducing SK-4 (3.3). Hand check of the displayed word: `(234)(124)^2(234)=(124)=X`. (REP’s parenthetical “`=(234)`” is a local arithmetic slip: the product is `X`, not `Y`. The surrounding claim `h=X` is correct on all `24`. Repair R3.)
- SK-4 pairs `(outer, T1)` with `T1` two transpositions of product `X`: **`72`**.
- Fixed-tuple counts as a function of `E=k_*`, full-image / total, restricted to those `72`:

```text
E ≡ 1 (mod 3)  i.e.  3 | (E+2) :  72/72   (E=...,-11,-8,-5,-2,1,4,...)
E ≡ 0,2 (mod 3) :                  0/0
```

REP’s displayed window `E=-8,-5,-2` is three consecutive representatives of the passing class; “`0` at every other residue” is correct in that window and in general. Realized `(6,4,3)`: `delta_aff=3`, `e(iota)=(d-1)+2·3-n(d-g)=5+6-16=-5`, **passes**. Hypothetical `delta_aff=4`: `e=5+8-16=-3`, `3|(-1)` false, **killed**. Both match PB §5 Control 2, including the negative half that the charge named. CABLE-3 specialises to the promoted `g=2` statement: `delta_2=sigma`, `h=X`, `sigma^2=c_X`, so (3.1) is `T1=sigma^{k_*+2}·T1`, solvable iff `3|(k_*+2)`. Not a new convention.

**Control 3 (`(6,4)` through Route 3).** Exact Puiseux of the ROW-NF sextic `x=r(t)^2`, `r=t^3+t+1`, `y=t^4+(2/3)t^2+(4/3)t` returns `k_*=-5`, `beta_1=2d-a-k_*=15`. PB’s Control-2 value, from the curve.

**Control 4.** `A'(4)` holds identically on all `60` odd outer solutions; the braid relation was checked as equivalent to the two conjugations, not assumed.

**Where CABLE-3 stops.** Rigidity uses a **single** characteristic pair. Both `(9,6)` rows have one pair (`gcd(a,beta_1)=1`). `OPEN[SHAPE-2-INNER-MULTIPAIR]` is correctly typed. `OPEN[SHAPE-2-INNER-g≥3]` is **narrowed, not closed**: GATE-3 settles `d'=3` with one pair (and both `(9,6)` types); `d'≥5` odd and `g≥4` remain. The general family-2 statement at `g≥3` is not claimed.

---

## 3. Task (3): class lists by brute enumeration — EXACT

Universe: `S_4` as permutations of `{0,1,2,3}`, `6` transpositions, `12` odd elements, `216=6^3` transposition triples. Hurwitz `delta_3` and `delta_3^{-1}` implemented from the explicit formulae of §1.3 and checked inverse to each other on a sample of triples. Image size: subgroup generated by the six entries of `T1` and `c_{XY}(T1)`, by the orbit algorithm in a set of `24`. Simultaneous `S_4`-conjugacy on `(X,Y,T1)`.

**Outer and pairs, verbatim:**

```text
|S4| = 24 ,  |odd| = 12 ,  |transpositions| = 6
outer solutions of XYX=YXY over odd elements:  60
  const-T 6 , const-4c 6 , noncst-T 24 , noncst-4c 24 , mixed 0
A'(4) holds on 60 of 60
pairs (outer, T1) with prod(T1)=X:  1080
  const-T 120 , const-4c 96 , noncst-T 480 , noncst-4c 384
```

**GATE-3 table, independent, `(full-image / total fixed)`:**

```text
   k   |  const-4c   const-T    noncst-4c   noncst-T
  -----+---------------------------------------------
    0  |    96/96      0/120        0/0      264/480
   -1  |     0/0        0/6         0/0        0/24
   -2  |     0/0        0/30       96/96      48/120
   -3  |     0/0        0/24        0/0       72/96
   -4  |    24/24       0/30        0/0       48/120
   -5  |     0/0        0/6         0/0        0/24
   -6  |     0/0        0/120     384/384    264/480
   -7  |     0/0        0/6         0/0        0/24
   -8  |    24/24       0/30        0/0       48/120
   -9  |     0/0        0/24        0/0       72/96
  -10  |     0/0        0/30       96/96      48/120
  -11  |     0/0        0/6         0/0        0/24
  -12  |    96/96      0/120        0/0      264/480
```

REP’s displayed `k=0..-6` matches **entry for entry**. The table is `12`-periodic (`k` and `k+12` identical; also `k` and `-k` have identical counts — an extra evenness not claimed by REP). It is **not** `6`-periodic on the `4`-cycle strata: `const-4c` at `k=0` is `96/96` and at `k=-6` is `0/0`; `noncst-4c` swaps those two. REP’s caption “`k=-7,...,-12` repeat `k=-1,...,-6`” asserts global `6`-periodicity and is **false**. The body of §3 already states the correct modulus: the fixed set of `delta_3^k c_h` depends only on `k` modulo `3·ord(X)∈{6,12}`. Period `6` holds on the transposition strata (`ord(X)=2`) and fails on the `4`-cycle strata (`ord(X)=4`, period `12`). Repair R2. GATE-3’s pinned-stratum sentence uses `k mod 4`, which is the correct extraction from the period-`12` table, and §5 was computed at the actual `k_*`, not from the caption.

Reading the table, given `3 nmid k_*` (Control 1, automatic):

- `const-T` is dead at every `k` for full image.
- `const-4c` requires `4|k_*`.
- `noncst-4c` requires `k_*=2 (mod 4)`.
- `noncst-T` requires `k_*` even (at `k=-3`, which has `3|k_*`, there **are** `72` full-image tuples; the parenthetical “given `3 nmid k_*`” is necessary and correct).
- Residues with `gcd(k_*,6)=1` (i.e. `k≡±1,±5 (mod 12)`) admit **no** full-image fixed tuple. Half the admissible residues die. GATE-3 is not vacuous.

**GATE-3 equivalences**, re-derived: `k_*=15-beta_1`, `e(iota)=2k_*` so `4|e(iota)⇔k_*` even; `delta_aff=29-beta_1` so `delta_aff-k_*=14` even, hence `2|delta_aff⇔2|k_*`; `beta_1=27-c` so `k_*=c-12`, hence `2|k_*⇔2|c`. Combining the live strata: a full-image `rho_inf`-fixed tuple exists only if `k_*` is even, and then `k_*=2 (mod 4)` allows only `noncst-4c` and `noncst-T`, while `k_*=0 (mod 4)` allows only `const-4c` and `noncst-T`. CONFIRMED as a necessary condition.

**The exponent sum alone is vacuous at `g=3`.** Independent BFS of the Hurwitz graph on the `216` triples, generators `sigma_1^{±1},sigma_2^{±1}`, tracking exponent modulo `24`: **every one of the `1080` pairs** admits a `beta` of exponent `≡-20 (mod 24)` and of exponent `≡-16 (mod 24)`; **`744`** of them have full image. Exact match to REP. Every bit of GATE-3 comes from rigidity.

**Surviving classes, verbatim.**

At `k=-10` (`(9,6,2)`, `k_*=2 (mod 4)`):

```text
full-image fixed tuples: 144
S4-conjugacy classes:    6 , each of size 24
  noncst-T  : X=(34)  Y=(23)  Pi=(24) , T1 = ((13),(14),(13))
            : X=(34)  Y=(23)  Pi=(24) , T1 = ((14),(13),(14))
  noncst-4c : X=(1234) Y=(1243) Pi=(34) , T1 = ((12),(23),(34))
            :                         T1 = ((23),(34),(14))
            :                         T1 = ((34),(14),(12))
            :                         T1 = ((14),(12),(23))
```

At `k=-8` (`(9,6,4)`, `k_*=0 (mod 4)`):

```text
full-image fixed tuples: 72
S4-conjugacy classes:    3 , each of size 24
  noncst-T  : the same two classes as above
  const-4c  : X=Y=(1234) , Pi=(1432) , T1 = ((34),(14),(12))
```

REP’s displayed representatives were checked individually: braid relation, `prod(T1)=X`, fixed at the relevant `k`, `|im|=24`, `Pi∉V_4`, `sgn(Pi)=-1`. No further class exists. No listed class dies. **Exactly 6 (144) and 3 (72).** `T2,T3` are then determined by `T1` and `iota` through the displayed relations of §1.4; (3.2) was the image test used.

**Survives-verdicts.** `(9,6,2)`: `k_*=-10≡2 (mod 4)`, PASSES GATE-3. `(9,6,4)`: `k_*=-8≡0 (mod 4)`, PASSES GATE-3. Both `c∈{2,4}` even, so GATE-3 is non-binding on this row while remaining binding in general (`gcd(k_*,6)=1` is fatal). REP reports this as found rather than strengthening the gate to fit the charge’s hoped-for kill. Correct.

Scope, stated exactly and respected: GATE-3 is a necessary condition for a `rho_inf`-fixed tuple with image `S_4`. Passing it is not existence of `phi`. `rho_inf`-fixedness is the product of the local relations only (§7 R1). Nothing here asserts a Keller map, and nothing here asserts a curve is non-realizable.

---

## 4. Task (4): all-gates sweep and the N-A boundary

### 4.1 Promoted theorem list, every item run or scoped out

Against RK §1–§2, SHAPE-KILL’s theorem list, N-A-RES, sheet-gate `(M')`, and PI1-S4 Theorem A:

| Gate | Scope | `(9,6,2)` | `(9,6,4)` |
|---|---|---|---|
| THEOREM CABLE-3 / GATE-3 | family 2, `u=3`, one pair | PASSES | PASSES |
| (M-INF) `M_inf≤3d-3=24` | one-place polynomial curve | silent (`27>24`, miss by 3) | silent (`25>24`, miss by 1) |
| (M-INF-T) `M_inf+2T≤24` | N-A-RES, `T≥0` | silent (slack `-3-2T`) | silent (slack `-1-2T`) |
| N-A / Lemma 4.3, `C'^2>2r_1` at `T=0` | irreducible, nodes | fails by 2 (`6>8`) | **boundary** (`12>12`) |
| Shirane Cor 0.6 + `S_3` resolvent | explicit degree-6 families; needs `Pi∈V_4` | N/A (odd `Pi`, `deg=9`) | N/A |
| INF-TRIVIAL (even-word) | even `d`, or a fibre of even meridian-word | **refuted by parity** (`d=9`) | same |
| Theorem A (coprime) | `gcd(d,n)=1` | N/A (`gcd=3`) | N/A |
| SK-1 | family `(u,1)` | N/A | N/A |
| SK-4 | family 2 at `g=2` | N/A (`g=3`); used only as Control 2 | N/A |
| SK-5 | family `(4,3)` | N/A | N/A |
| THEOREM TB / TB-2 | family 3, chart orders `(g,4g)` | N/A (charts `(3,9)`); typed `OPEN[TB-FAMILY-2]` | N/A |
| RK S4 row-kill | explicit `D_{b,c}` / `D'_{b,c}` | N/A (degree 9 is not in the reviewed gauge) | N/A |
| THEOREM[S5-COPRIME-KILL] | `N=5`, `S_5` | N/A | N/A |
| D1-DEGREE / NO-DEG-CAP | degree as a cage-closer | OPEN; no-deg-cap forbids a degree kill | same |
| `(M')` under (H2)+(H3) | irreducible `A_F` | N/A (H2 closed at `N=4`) | N/A |
| `(M')` block-free | reducible `A_F` | constraint on `D_2` only, §5 below | same |
| FIXED-TUPLE / TRIPLE-COVER / FOLD / ZVK-U6 / NONMONOGENIC / EDGE-MODULI / TORUS-CHECK | `(6,4)` explicit family | N/A | N/A |
| HF-TWIN | `(9,6,4)` as a construction target | n/a | PASS_NECESSARY_ONLY on the twin; not a kill; six-node question remains OPEN per AUD |

No promoted gate was skipped. Family-3’s `3|e(iota)` was **not** transported. Where a tool does not reach, the verdict is `not applicable` with the reason typed, and an `OPEN` is raised rather than an analogue being assumed.

### 4.2 N-A boundary arithmetic — CONFIRMED

Charged Lemma 4.3 (N-A-RES, review item D.1 CONFIRMED): `C'^2-2 delta_aff=3d-2-M_inf=25-M_inf`. With `r_1=delta_aff`, `T=T_x=0`:

```text
(9,6,2):  C'^2 - 2 r_1 = 25-27 = -2  ,  C'^2=6 ,  N-A reads 6>8  (false by two)
(9,6,4):  C'^2 - 2 r_1 = 25-25 =  0  ,  C'^2=12 ,  N-A reads 12>12 (false by equality)
```

`(9,6,4)` sits exactly on the N-A boundary, with `(8,6,11)`, `(6,4)` and `(8,4)`. A YES on `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` would kill it and leave `(9,6,2)` untouched (deficit 2). REP records the coincidence and does **not** relax `>` to `≥`; the promoted sharpness datum concerns the `T_x` coefficient on a reducible configuration and settles nothing for irreducible `C`. Correct, and a FALLACY floor/attainment pass.

Equivalent `(M-INF)` form: `beta_h≤2d+n-2=22`; `beta_1=25,23` both miss. Tangential refinement is monotone the wrong way. Silence is not `pi_1≠Z`.

### 4.3 Shirane / INF-TRIVIAL / odd `d` — CONFIRMED not a kill

Two independent reasons Shirane does not reach `(9,6)`: (i) descent needs `Pi∈V_4`, but `sgn(Pi)=(-1)^9=-1`, confirmed on all `60` outer solutions and all `9` surviving classes; (ii) Cor 0.6 is degree-6-specific (`deg Dbar=9`, weighted `Dbar+2L_infty` has degree `11`). RK §3’s stop is respected.

INF-TRIVIAL is **refuted** at odd `d`, not merely unavailable: every `x`-fibre meets `D` with multiplicities summing to `9`, so the meridian word has odd length and `sgn(phi(gamma_inf))=-1`. On the realized curve, `x=0` carries four nodes plus one smooth point; node meridians go to disjoint transpositions, giving `Pi∈V_4·tau` — odd, consistent. PB §7’s four-node line criterion fails by one unit of degree (`9=4·2+1`). Recorded, not stretched.

---

## 5. Task (5): §7 fork — `(M')`, `a_p` clusters, Pi-tau pin

### 5.1 `(M')` under (H2) — CONFIRMED as a control, not a kill of `(9,6,2)`

Sheet-gate `(M'-def)`: `sum_p(a-a_p)=(a-1)+nu(d-a)`, with `1≤a≤d-2=2`, `0≤a_p≤a`. Hypotheses Keller+(H2)+(H3). For nodal `A_F`, `nu=s`, LHS `≤s a`. At `a=2`: `2s≥1+2s`, i.e. `0≥1`, false for every `s`. At `a=1`: `s≥3s`, false for every `s≥1`. No nodal `N=4` residual survives `(M')` under (H2). This reproduces the promoted “B0 holds at `N=4` under H2” and is a control on the identity, not a new theorem.

The `(9,6,2)` candidate does **not** live under (H2): the `N=4` residual is the reducible-`A_F` case.

### 5.2 Block-free instantiation — CONFIRMED; `s_1` cancels; `(7.1)` is `chi_2+sigma_2=1`

Sheet-gate without (H2): `sum_i a^{(i)} chi_c(D_i\Sing D)+sum_p a_p=1-d chi_c(V)`, and (E) gives `chi_c(V)=1-chi_c(D)`, `d=N=4`. Profile (`reducible-all-n`:459): core `(2,1,0)`, `W=(1,2)` — one branched component `D_1` of weight `2` and one trivial-dicritical component `D_2` of weight `1`. Thus `a^{(1)}=N-W_1=2`, `a^{(2)}=N-W_2=3`. Independently `a^{(1)}=#Fix(transposition)=2`. `D_1` has `s_1` nodes and normalization `A^1`; `D_2` has `sigma_2` nodes and `chi_c(D_2)=chi_2`; they meet transversally in `j` points.

`a_p=#F^{-1}(p)` (sheet-gate, not the PI1-S4 sheet count). Cluster values against that definition:

- Node of `D_1`: two size-2 clusters (two disjoint transpositions) exhaust the four letters of the geometric fibre of `F` ⇒ `a_p=0`. Independently, `H_p≅Z/2×Z/2` generated by those transpositions has `s_p=#Fix(H_p)=0`, so `a_p=s_p-b_p=0`.
- Transverse `D_1∪D_2` point: clusters `2+1` ⇒ leftover `1` ⇒ `a_p=1`.
- Node of `D_2`: clusters `1+1` ⇒ leftover `2` ⇒ `a_p=2`.

These sit in the ranges `0≤a_p` and are compatible with the generic values `a^{(1)}=2`, `a^{(2)}=3`.

Euler, independently assembled. `chi_c(D_1)=1-s_1` (norm `A^1`, `s_1` nodes). `chi_c(D)=chi_c(D_1)+chi_c(D_2)-j=1-s_1+chi_2-j`. Hence `chi_c(V)=s_1-chi_2+j` and

```text
RHS = 1 - 4 chi_c(V) = 1 - 4 s_1 + 4 chi_2 - 4 j .
```

On the left: `D_1\Sing D` is `A^1` minus `2s_1` node-preimages minus `j` intersections, `chi_c=1-2s_1-j`; `D_2\Sing D` has `chi_c=chi_2-sigma_2-j` (remove `sigma_2` node-points and `j` intersections from the space `D_2`); `sum a_p=0·s_1+1·j+2·sigma_2`. So

```text
LHS = 2(1-2s_1-j) + 3(chi_2-sigma_2-j) + j + 2 sigma_2
    = 2 - 4 s_1 + 3 chi_2 - sigma_2 - 4 j .
```

`LHS-RHS=1-chi_2-sigma_2`. The identity therefore collapses to

```text
(7.1)     chi_2 + sigma_2 = 1 ,
```

**with `s_1` cancelling identically** (both sides carry `-4s_1`) **and `j` cancelling identically**. `chi_2+sigma_2=chi_c(normalization of D_2)`, so (7.1) is exactly “`D_2` also has normalization `A^1`”. `(M')` is blind to `delta_aff(D_1)`. It neither kills nor supports `(9,6,2)`. Typed `OPEN[REP-96-MPRIME-COMPANION]` is the right residue.

### 5.3 Pi-tau pin — CONFIRMED, two of six

On the realized curve the fibre `x=0` contributes four commuting `sigma_i^2` (nodes: local relation `(N_1)`, disjoint transpositions, product in `V_4`) and one smooth meridian `tau=phi(g_9)` at `t=0`. Grouping, `Pi∈V_4·tau`. Every surviving `(9,6,2)` class has `Pi` a transposition (§3). Two transpositions have product in `V_4` iff they are equal (product `e`) or disjoint (product a double transposition); if they share one letter the product is a `3`-cycle, not in `V_4`. Hence `tau=Pi` or `tau` disjoint from `Pi`.

Independent check on the two `Pi`-types that appear: `Pi=(24)` forces `tau∈{(24),(13)}`; `Pi=(34)` forces `tau∈{(34),(12)}`. **Two of the six transpositions**, not six. A genuine additional pin, obtained from the curve, available without transports.

The eight tangencies forming a tree on nine sheets is graph Euler (`v-e=9-8=1` for a connected graph with `8` edges on `9` vertices), not a mis-applied curve Riemann–Hurwitz (`R=2d-2=16` is separately accounted: `8` affine simple critical points plus ramification index `9` at infinity). It collapses meridians in `H_1` (giving `H_1=Z`, as it must) and does not force equality of `phi`-images, because each ZvK relation is conjugacy by a transport word. No cheap kill, and none is claimed. `OPEN[REP-96-BM-FACTORISATION]` is correctly the cheapest decisive next step.

`OPEN[REP-96-SOURCE-IS-C2]` is correctly named as the largest single gap: a `phi` fixed by the whole factorisation gives a degree-4 branched cover `Y→C^2`, and Keller requires `Y≅C^2` plus the normality / miracle-flatness step RK inserts into the `(6,4)` descent. Riemann existence does not supply the isomorphism type.

---

## 6. Task (6): two-symbols-`b`, FALLACY-v2

### 6.1 Two symbols `b` — CONFIRMED, no conflation

REP §7 R3 keeps them apart explicitly:

- THEOREM 7.B (all-degree H2 integration): `b=0` is the count of dicriticals with affine image and `mu=1`, a **consequence of H2**.
- Reducible cage (`reducible-all-n`:130-134): `b` is the number of **branched components** of `A_F`, and (RC2) forces `b=1` at `N=4,5`.

Only the second is used. The `N=4` residual is one branched component of weight `2` plus one trivial-dicritical component of weight `1`; `corr=0` on both dicriticals, so the branched component carries only double points of smooth branches. The realized curve’s four ordinary nodes of two smooth branches are consistent. The budget does not obstruct `(9,6,2)`; it does demand a companion component of degree at least `2` (Lemma NL), about which the numerical type is silent.

### 6.2 FALLACY-v2 — no violation found

Flag/place/series: contact `d=9`, multiplicity `a=3`, `beta_1∈{25,23}`, affine `k_*∈{-10,-8}` kept apart; `k_*` derived twice, not table-read; the `a` conjugate series are one place. Floor/attainment: `e(iota)` exact; (M-INF) silence is not `pi_1≠Z`; N-A equality is not consumed as `≥`. Carrier: §5 is group data, not a witness; passing GATE-3 is a necessary condition met, not a representation exhibited. No exit price, no `charge_basis`. Pole/interior: winding on `|x|=R` in the tube regime, rigidity by dominance of `k_*` as `R→∞`. Prime labels: `p',q'` are derivatives; `Pi`, `Pi_i`, `X`, `Y` distinct; two symbols `b` separated. Variable/ring: chart orders `(a,d)=(3,9)`; Hurwitz convention declared; conjugator derived as `Pi Pi_{d'}^{-1}` and round-trip checked. No `sat()`, no raw remainder degree, no `M`-descent. Family-3’s `3|e(iota)` was not transported; TB, Shirane, INF-TRIVIAL, and `(M')` under (H2) are typed `not applicable` with reasons.

---

## 7. Repairs (required) and non-repairs

Load-bearing claims do not move. Three errors in supporting text would poison a successor who consumes a table or an example instead of the theorem and the §5 list.

**R1 (must fix).** §2 outer-solution table, `noncst-4c` row, `W=XY` column: write **`3`-cycle**, not “double transposition”. Witness: on all `24` such pairs `W` has cycle type `(3,1)`; on the displayed `X=(1234)`, `Y=(1243)`, `XY=(132)`, `YX=(142)`, while `h=Y X^2 Y=(13)(24)` is the double transposition (that column is already correct). Do not swap `W` with `X^2`.

**R2 (must fix).** §3 table caption “the table is `12`-periodic in `k`; `k=-7,...,-12` repeat `k=-1,...,-6`”: delete the second clause. The table is `12`-periodic, and the body already states the correct modulus `3·ord(X)∈{6,12}`. Global `6`-periodicity holds on the transposition strata and **fails** on the `4`-cycle strata — which is exactly where using the caption to read `k=-10` as `k=-4` (and `k=-8` as `k=-2`) would **swap the `4`-cycle content of the two types**. The GATE-3 pinned-stratum sentence (`k mod 4`) and the §5 class lists are computed from the true residues and are not themselves wrong. A successor must take §5 and (3.3), not the caption.

**R3 (must fix).** §3 / §4 Control 2 example: `(234)(124)^2(234)=(124)=X`, not `(234)`. The claim `h=X` on all `24` SK-4 pairs is correct; only the displayed evaluation is wrong.

Non-repairs, recorded so they are not re-opened: the parenthetical “order at most `6`” on `const-T` is true (independent census); Control 2’s window `E=-8,-5,-2` is a complete set of consecutive representatives of the passing class `E≡1 (mod 3)`, not an incomplete list of passing integers; “false by one unit” at the N-A boundary is informal language for equality failing a strict inequality, and the displayed `C'^2-2r_1=0` is the precise statement; `(9,6,4)` is not promoted to a six-node realization (AUD leaves that OPEN; REP treats it as a numerical type surviving the representation gate).

---

## 8. Typed verdict

```text
LANE              REP-96-HOSTILE-REVIEW  (gate CABLE-3 and the survives-verdict)
REVIEWER          grok-4.6
CHARGED           rep-96-inner-opus5-20260901.md
                  SHA-256 a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401

THEOREM CABLE-3   CONFIRMED at written scope (family 2, u=3, one pair at infinity).
                  Ordered-product claim CONFIRMED (algebra of two-fold cabling).
                  Winding argument CONFIRMED (k_*=2d-a-beta_1 re-derived; three
                  independent Puiseux checks; sign pinned by exponent; g=2
                  specialisation recovers 3|(E+2) on both halves).
GATE-3            CONFIRMED. k_* even <=> 4|e(iota) <=> 2|delta_aff <=> 2|c.
                  Non-vacuous: gcd(k_*,6)=1 admits no full-image fixed tuple.
                  Exponent-sum gate at g=3 is vacuous (1080/1080 admit e=-20
                  and e=-16; 744 with full image).

(9,6,2)           delta_aff 4, beta_1 25, delta_inf 24, M_inf 27, k_*=-10,
                  e(iota)=-20. GATE-3 PASSES (k_*=2 mod 4).
                  SURVIVES every other promoted gate run in §4.
                  Residual: 6 classes, 144 tuples, exactly the listed set.
                  OPEN at OPEN[REP-96-BM-FACTORISATION].
(9,6,4)           delta_aff 6, beta_1 23, delta_inf 22, M_inf 25, k_*=-8,
                  e(iota)=-16. GATE-3 PASSES (k_*=0 mod 4).
                  SURVIVES every other promoted gate; exactly on the N-A
                  boundary (12>12). Residual: 3 classes, 72 tuples, exact.
                  A YES on OPEN[NA-R1-SHARPNESS-IRREDUCIBLE] would kill it.

§7 FORK           CONFIRMED. (7.1) chi_2+sigma_2=1 with s_1 cancelling;
                  a_p in {0,1,2} matches sheet-gate #F^{-1}(p) and the
                  cluster definitions; Pi-tau pin is two of six
                  transpositions; two symbols b are not conflated.
                  OPENs BM-FACTORISATION, SOURCE-IS-C2, MPRIME-COMPANION
                  stand, in that cost order.

ROW VERDICT       The (9,6) row is NOT killed at the S_4 representation
                  level. Given AUD's realization of (9,6,2), the row is
                  alive on the merits.

OVERALL           PROMOTE-WITH-REPAIRS
                  (R1 W-column of noncst-4c; R2 period-6 caption; R3
                  Control-2 example arithmetic). No survives-verdict, no
                  class, and no theorem statement moves under these repairs.
```

**What this review does not do.** It does not compute the eight tangency transports. It does not assert that a representation exists, that a Keller map exists, or that `(9,6,4)` is a six-node curve. It does not promote GATE-3 from a necessary condition to a sufficient one.

No `charge_basis` line: no new exit price is asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `39245`.
- Body SHA-256:
  `ab8ee8fd0d769aca7be30872134b8c7cc7ee4621673314f570a3c85320db5ac7`.
- Frozen basis: `3fc735f958b806e33a75227bcc9da697291e4c34`.
