# Hostile review: ROW-SWEEP report (Sol)

Different-model gate. Default to refutation. Desk-scale exact
reasoning only. No `charge_basis` declaration.

Charged inputs (frozen, hashes verified below):

- `xmodel/row-sweep-sol56-20260831.md`
- `xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`
- `xmodel/pi1s4-close-residual-r2-opus5-20260831.md`

Reviewer: grok-4.6, 2026-08-31.

## 0. Hash verification and scope

Verified with `shasum -a 256` before any mathematical use. All three frozen copies match the charge:

```text
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb
  .../inputs/row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286
  .../inputs/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696
  .../inputs/pi1s4-close-residual-r2-opus5-20260831.md
```

Primary source re-fetched, not saved as a campaign artifact:

```text
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9
  241372 bytes, https://arxiv.org/pdf/0910.2613v2
  C. Galindo--F. Monserrat, The Abhyankar--Moh theorem for plane
  valuations at infinity, arXiv:0910.2613v2.
  Consumed: Theorem 2.1 (δ-sequence axioms) and Proposition 2.1
  (conversion to maximal-contact values).
```

This is the custody hash already recorded in the M-INF hostile review. No CAS. No `jc2-lean`. No charged file or canonical ledger edited. Default is refutation: a kill is recorded only after the reduction, the cluster identity, and the consumed theorem are re-derived at the written scope.

Typing. `KILLED` / `SURVIVES-AS` / `OPEN` are used as in the charged sweep. Promoted inputs actually consumed: PI1-S4 Main Theorem at coprime + tangency-allowed scope (N≤19 integration §1.1); target-automorphism invariance of residual data (D1-DEGREE review Item 1, argument not restricted to one elementary family); `M_emb = a+β_h-1` as corrected; N-A-RES at `T=0` (nodal (M-INF)); A'(1)--(4) only as a negative control, never as a kill; Galindo Theorem 2.1 and Proposition 2.1 as above. Not consumed: (M-INF-T), A'(5), the coprime order-three/order-four fork off the coprime stratum, any AM converse, Nori's `B(C)>0` form.

## 1. (6,3) tangential kills: triangular reduction to coprime (5,3) / (4,3)

**Verdict: HOLDS.** Both charged labels are killed by a triangular target automorphism landing in the promoted coprime Main Theorem. (M-INF-T) is correctly not consumed.

Setup. Residual normalisation `d=6>n=3`, so `a=3`. Lemma 1.3 of the residual-r2 report (charged) forces the dichotomy `a|d` or `d=β_1`. Here `3|6`, hence one transverse pair `(3;β_1)` with `β_1>6` and `3∤β_1`. The plane-branch delta formula `2δ_∞=(a-1)(β_1-1)` gives `δ_∞=β_1-1`. Genus `10` and `δ_aff≥1` restrict to `β_1∈{7,8,10}`. The two charged labels are `β_1=7` and `β_1=8`; the third value is not charged.

Galindo–Monserrat Theorem 2.1 for `Δ=(6,3,c)`: `d_1=6`, `d_2=3`, `n_1=2`, and `d_3=1` forces `3∤c`; axiom (2) is `6∈⟨6⟩` and `3c∈⟨6,3⟩=⟨3⟩`; axiom (3) is `c<6`. Thus `c∈{1,2,4,5}`. Proposition 2.1 in the `ν(u)|ν(v)` case converts `β̄_0=a=3` and `β_1=12-c`. Matching the charged labels:

- `(β_1,T)=(7,4)` is `Δ=(6,3,5)`, cluster `M(3,7)=(3,3,1,1,1)`, `δ_∞=6`, `δ_aff=4`, `M_∞=max(6,3+7-1)=9`.
- `(β_1,T)=(8,3)` is `Δ=(6,3,4)`, cluster `M(3,8)=(3,3,2,1,1)`, `δ_∞=7`, `δ_aff=3`, `M_∞=10`.

`T` is undefined in the three charged files (as the sweep itself records). No partition of `δ_aff` is inferred from the frozen labels. Conditionally, `M_∞+2T` is `17` resp. `16`, both `>15`, so a tangential Nori gate would not fire even if `T` were licensed. That is a non-issue: the kill below does not use it.

Reduction. Because `n_1=δ_0/δ_1=2` is an integer, the last approximate root of Galindo Definition 2.3 is Tschirnhausen in the coordinates: `r=p-φ(q)` with `deg φ=2` and `deg_t r=δ_2`. (If `δ_1` did not divide `δ_0` the approximate root would be a genuine degree-`δ_0/d_2` polynomial in two variables, and the claimed elementary automorphism would be false. That does not occur on this row.) The map `T(u,v)=(u-φ(v),v)` is an elementary automorphism of `A^2`, Jacobian `1`. It sends the parametrisation to `(r,q)` of coprime degree pair `(5,3)` resp. `(4,3)`.

Invariance. The D1-DEGREE hostile review Item 1 is written for the opposite elementary family `(u,v)↦(u,v+u^k)`, but its argument never uses that shape: `det dT=1` preserves the Keller property; `A_{T∘F}=T(A_F)`; the finite cover, branch locus, fibre cardinalities, `a_D`, `a_p`, meridian classes, and the two-smooth-branch local type are pulled back through a biregular map of the target. The same sentences apply to `(u,v)↦(u-φ(v),v)`. Affine double points (nodes or `A_{2k-1}`) map to affine double points of the same type. The residual class is therefore preserved, and the image is a polynomial curve with `gcd=1`.

Landing. The promoted PI1-S4 Main Theorem (N≤19 integration §1.1) forbids a transposition-valued `S_4` quotient on every irreducible polynomial curve with `gcd(d,n)=1` and affine singularities double points of two smooth branches, tangency allowed. Both `(5,3)` and `(4,3)` meet that scope. The intermediate `(C1)+A(3)` survivor table still contains `(4,3)`; that table is not the Main Theorem. Theorem C is the ingredient that kills tangential coprime pairs, and it is inside the promoted Main Theorem, not an off-stratum use of the order-three/order-four fork. The fork is a coprime-stratum subtheorem and is not invoked here as a noncoprime constraint.

No alternative kill is needed, and none is claimed. The two degree-six tangential rows close.

## 2. (8,2) and (9,3) M-INF kills: infinity types and M_∞ bounds

**Verdict: HOLDS**, as nodal-row statements. Every admissible infinity type satisfies `M_∞≤3d-3` after the corrected cluster identity. The N-A-RES package at `T=0` then gives `π_1=Z`.

Corrected identities used throughout. Euclidean blocks `M(e_{i-1},Δ_i)` with `Δ_1=β_1`, `Δ_i=β_i-β_{i-1}` sum to `M_emb=a+β_h-1` (M-INF review §2; residual-r2 (4.2) as repaired). With terminal multiplicity-one centres included, `M_∞=max(d,M_emb)` exactly. Nodal Nori is `C'^2>2δ_aff`, and `C'^2-2δ_aff=3d-2-M_∞`, hence the integral gate `M_∞≤3d-3`. Promoted N-A-RES at `T=0` is this gate.

**(8,2).** Here `a=6`, `6∤8`, so Lemma 1.3 forces `β_1=8` and `e_1=2`. A second odd characteristic `β_2` is required. Galindo for `Δ=(8,2,c)`: `n_1=4`, `n_2=2`, `c` odd, `c<8`. Axiom (2) holds for every such `c` (`8∈⟨8⟩`, `2c∈⟨8,2⟩=2ℕ`). Thus `c∈{1,3,5,7}`. The non-dividing conversion of Proposition 2.1 gives `β̄_0=6`, `β̄_1=8`, `β̄_2=32-c`. Matching characteristics via `β̄_2=n_1^{char}β_1+β_2-β_1` with `n_1^{char}=3` yields `β_2=16-c`. The delta formula is `2δ_∞=β_2+27`, genus `21`:

| `c` | `(a;β_1,β_2)` | cluster | `δ_∞` | `δ_aff` | `M_∞` |
|---:|---|---|---:|---:|---:|
| 7 | `(6;8,9)` | `(6,2^3,1,1)` | 18 | 3 | 14 |
| 5 | `(6;8,11)` | `(6,2^4,1,1)` | 19 | 2 | 16 |
| 3 | `(6;8,13)` | `(6,2^5,1,1)` | 20 | 1 | 18 |
| 1 | `(6;8,15)` | `(6,2^6,1,1)` | 21 | 0 | 20 |

The last row is outside the residual (`δ_aff=0`). No four-term sequence exists: an even third term would force `n_2=1`. Each listed cluster sums to `a+β_2-1` and to `max(8,M_emb)`. All three residual types have `M_∞≤18<21=3·8-3`. Nodal (M-INF) kills the row. Tangential realisations of the same `δ_aff` (one `A_{2k-1}`) are not claimed killed; the ledger says nodal, correctly.

**(9,3).** Here `a=6`, `6∤9`, so `β_1=9`, `e_1=3`, and `3∤β_2`. For `Δ=(9,3,c)`: `n_1=n_2=3`, `3∤c`, `c<9`, axiom (2) holds, and a third term divisible by 3 would force `n_2=1`. Thus `c∈{1,2,4,5,7,8}`. Conversion: `β̄_2=27-c`, `n_1^{char}=2`, hence `β_2=18-c`. Then `δ_∞=β_2+11`, genus `28`, `M_∞=β_2+5`:

| `c` | `(a;β_1,β_2)` | cluster | `δ_∞` | `δ_aff` | `M_∞` |
|---:|---|---|---:|---:|---:|
| 8 | `(6;9,10)` | `(6,3^2,1^3)` | 21 | 7 | 15 |
| 7 | `(6;9,11)` | `(6,3^2,2,1^2)` | 22 | 6 | 16 |
| 5 | `(6;9,13)` | `(6,3^3,1^3)` | 24 | 4 | 18 |
| 4 | `(6;9,14)` | `(6,3^3,2,1^2)` | 25 | 3 | 19 |
| 2 | `(6;9,16)` | `(6,3^4,1^3)` | 27 | 1 | 21 |
| 1 | `(6;9,17)` | `(6,3^4,2,1^2)` | 28 | 0 | 22 |

Exclude `c=1`. The five residual types satisfy `M_∞≤21<24=3·9-3`. Nodal (M-INF) kills the row. The independent approximate-root shears to coprime `(8,3)`, `(7,3)`, `(5,3)`, `(4,3)`, `(3,2)` are valid on this row because `δ_1|δ_0`, so they also land in the Main Theorem even without nodality; they are a check, not the gate used.

No off-stratum order fork is used. The cluster identity is the corrected one (terminal `1`-centres included). The two M-INF kills stand.

## 3. (6,4) survivor: Δ-census, invariants (7,3,16), three-node attainment

**Verdict: HOLDS.** `Δ=(6,4,3)` is the unique numerical (M-INF) survivor; the displayed parametrisation is an in-class three-node curve of that type; the missing lemma is the noncoprime fixed tuple.

Census. `a=2`, `2|6`, so one odd `β_1>6`. For `Δ=(6,4,c)`: `n_1=3`, `n_2=2`, and `d_3=1` forces `c` odd (an even third term yields `n_2=1`, so there is no four-term sequence). Axiom (2): `12∈⟨6⟩` always; `2c∈⟨6,4⟩` fails only at `c=1` (`2∉⟨6,4⟩`). Axiom (3): `c<12`. Hence `c∈{3,5,7,9,11}`. Proposition 2.1 (dividing case) gives `β_1=18-c`. The `(2,β_1)` formulae are `δ_∞=(β_1-1)/2`, `M_∞=β_1+1`, genus `10`, cluster `(2^{δ_∞},1,1)`:

| `c` | `β_1` | `δ_∞` | `δ_aff` | `M_∞` |
|---:|---:|---:|---:|---:|
| 11 | 7 | 3 | 7 | 8 |
| 9 | 9 | 4 | 6 | 10 |
| 7 | 11 | 5 | 5 | 12 |
| 5 | 13 | 6 | 4 | 14 |
| 3 | 15 | 7 | 3 | 16 |

Threshold `3d-3=15` kills the first four. The unique threat is `Δ=(6,4,3)`, invariants `(β_1,δ_∞,δ_aff,M_∞)=(15,7,3,16)`. The banked triple-point curve of the M-INF review realises the same semigroup and is out of class; it does not decide nodality.

Attainment. Put `r=t^3+t+1`, `q=t^4+(2/3)t^2+(4/3)t`, `p=r^2`. The identity

```text
8r/27 = p^2-q^3-2pq+(2/3)q^2-(16/27)p+(1/9)q-1/9
```

is a polynomial identity in `t`: expanding and cancelling, the degree-12 and then degree-8 through degree-4 terms drop, and the remainder is exactly `(8/27)(t^3+t+1)`. Thus `r∈C[p,q]`, so `C[p,q]=C[r,q]`. Coprime degrees `3,4` give fraction field `C(t)` and ordinary degree `6`. The identity is load-bearing for degree six: without `r∈C(p,q)` the map `t↦(r^2,q)` could be 2-to-1 onto a cubic.

Double-point scheme. For `σ=t+s`, `π=ts`, divided differences yield `q(t)=q(s)` (`t≠s`) iff `σ^3-2σπ+(2/3)σ+4/3=0`. Then `p(t)=p(s)` splits as `r(t)=±r(s)`. The plus case is `π=σ^2+1`; substituted, it is the cubic `3σ^3+4σ-4=0`. Discriminant of `3σ^3+4σ-4` is `-4656≠0`, so three distinct roots in `C`. The minus case, equated to the `q`-condition, forces `σ^2/3=σ^2/2`, hence `σ=0`, which does not satisfy the cubic. So only the plus component occurs.

Pair discriminant `σ^2-4π=-3σ^2-4` vanishes at `σ^2=-4/3`, and `3σ(-4/3)+4σ-4=-4≠0`, so never on the cubic: six parameters, three genuine pairs. Distinct images: `r=(σ-1)/3` and `q=(σ^2+1)/3` on the cubic (the displayed `-σ^3/4` equals `(σ-1)/3` via `3σ^3=4-4σ`). Equal `q` for two roots of the cubic would force the second to be plus or minus the first; equal `r` then forces `σ=0`, not a root. No shared parameter across pairs: a common `t` would require `σ_i^2+σ_j^2+σ_iσ_j+1=0`, which reduces by `σ_1+σ_2+σ_3=0` and `σ_iσ_j=4/3+σ_k^2` to `-1/3≠0`. No triple fibre.

Immersion and nodes. `q'=(4/3)r`, so `r'=0` (`t^2=-1/3`) gives `q'=4/3≠0`. Tangent vectors at a plus-pair are `r(t)(2r'(t),4/3)` and likewise at `s`; they are parallel iff `t^2=s^2`, iff `σ=0`, not a root. Also `r=(σ-1)/3≠0` on the cubic (`σ=1` gives `3≠0`). Three ordinary nodes, not tangencies, no diagonal. Hence `δ_aff=3`. The unique numerical semigroup containing `⟨6,4⟩` of genus `3` is `⟨3,4⟩`, so `δ_∞=7` and `β_1=15` as required. The triple-point member is a specialisation, not a forced feature.

Structural tests do not kill. Reduced Chau shape `(3,2)`; scale only `gcd(deg P,deg Q)≥4`; slice alternatives `(c(Π),g_L)=(4,0)` or `(2,1)`; A'(1)--(4) at `(g;d',n')=(2;3,2)` give one conjugacy orbit and `P^2` central, with no equal-product clause (`4∤6`). The three disjoint-transposition matchings of `S_4` are a local negative control, not a route-to-tuple. OPEN[PI1S4-(6,4)-FIXED-TUPLE] is the correct residual.

## 4. (8,4) survivor and claimed target-equivalence to (6,4)

**Verdict: HOLDS.** The unique (M-INF) survivor is `Δ=(8,4,6,3)`, characteristic `(4;10,19)`, invariants `(18,3,22)`, and it is the image of the §3 curve under an elementary automorphism.

Census. `a=4`, `4|8`. Galindo on prefixes `(8,4,·)`:

- Three-term `Δ=(8,4,c)`: `n_1=2`, `n_2=4`, `c` odd, `c<8`. Even `c` with `4|c` forces `n_2=1`. Thus `c∈{1,3,5,7}`. Conversion: `β_1=16-c`. Then `c=1` has `δ_aff=0`. Remaining: `(8,4,7)`, `(8,4,5)`, `(8,4,3)` with `(M_∞,δ_aff)=(12,9)`, `(14,6)`, `(16,3)` and clusters `(4^2,1^4)`, `(4^2,3,1^3)`, `(4^3,1^4)`.
- Four-term with third term `c≡2 (mod 4)` (so `gcd(4,c)=2`, `n_2=2`). Axiom (3) forces `c∈{2,6}`.
  - `(8,4,2,e)`: `e` odd, `e<4`, and `2e∈⟨8,4,2⟩`. This leaves `(8,4,2,3)` (`e=1` has `δ_aff=0`). Characteristic `(4;14,15)`, cluster `(4^3,2^2,1^2)`, `(δ_∞,δ_aff,M_∞)=(20,1,18)`.
  - `(8,4,6,e)`: `e` odd, `e<12`, `2e∈⟨8,4,6⟩` excludes `e=1`. Conversion: `β_1=10`, `β_2=22-e`. The five types are

| `Δ` | `(4;β_1,β_2)` | cluster | `δ_∞` | `δ_aff` | `M_∞` |
|---|---|---|---:|---:|---:|
| `(8,4,6,11)` | `(4;10,11)` | `(4^2,2^2,1^2)` | 14 | 7 | 14 |
| `(8,4,6,9)` | `(4;10,13)` | `(4^2,2^3,1^2)` | 15 | 6 | 16 |
| `(8,4,6,7)` | `(4;10,15)` | `(4^2,2^4,1^2)` | 16 | 5 | 18 |
| `(8,4,6,5)` | `(4;10,17)` | `(4^2,2^5,1^2)` | 17 | 4 | 20 |
| `(8,4,6,3)` | `(4;10,19)` | `(4^2,2^6,1^2)` | 18 | 3 | 22 |

No five-term sequence: a further even generator would force `n_3=1`. Genus `21` and `M_∞=max(8,4+β_h-1)` check on every row. Threshold `21` kills the first eight residual types. The unique survivor is `(8,4,6,3)` with `(18,3,22)`.

Equivalence. Let `(p,q)` be the §3 parametrisation. Set `P=p+q^2`. Then `T(u,v)=(u+v^2,v)` is elementary, Jacobian `1`, and `deg P=8` (leading term of `q^2` is `t^8`, no cancellation with `p`). Affine singularities, complement, and cover data are preserved. Approximate-root degrees are `deg P=8`, `deg q=4`, `deg(P-q^2)=6`, `deg r=3`, i.e. `Δ=(8,4,6,3)`, converting to `(4;10,19)` as above. Three ordinary nodes are the images of the three nodes of §3.

Structural tests again fail to kill: reduced shape `(2,1)`; `4|8` triggers A'(4) (common block product `c` with `P=c^2`) but not an internal-transposition collapse; A'(5) is withheld. The OPEN is the same missing tuple, now on a target-isomorphic curve. There is one geometric class, not two.

## 5. (8,6) / (9,6) numerical-type lists

**Verdict: HOLDS as numerical censuses.** Four resp. two types survive (M-INF). Nodal realisation is not proved and is not claimed.

**(8,6).** `a=2`, `2|8`, one odd `β_1>8`. For `Δ=(8,6,c)`: `n_1=4`, `n_2=2`, `c` odd, `c<24`. Axiom (2) is `24∈⟨8⟩` and `2c∈⟨8,6⟩=2⟨4,3⟩`. The even semigroup `2⟨4,3⟩` omits `{2,4,10}`, so odd `c` is excluded at `c=1,5`. No four-term sequence (`n_2=1` if `c` even). Thus `c∈{3,7,9,11,13,15,17,19,21,23}`. Conversion `β_1=32-c`, cluster `(2^{δ_∞},1,1)`, `δ_∞=(β_1-1)/2`, `M_∞=β_1+1`, genus `21`:

| `c` | `β_1` | `δ_∞` | `δ_aff` | `M_∞` |
|---:|---:|---:|---:|---:|
| 23 | 9 | 4 | 17 | 10 |
| 21 | 11 | 5 | 16 | 12 |
| 19 | 13 | 6 | 15 | 14 |
| 17 | 15 | 7 | 14 | 16 |
| 15 | 17 | 8 | 13 | 18 |
| 13 | 19 | 9 | 12 | 20 |
| 11 | 21 | 10 | 11 | 22 |
| 9 | 23 | 11 | 10 | 24 |
| 7 | 25 | 12 | 9 | 26 |
| 3 | 29 | 14 | 7 | 30 |

Threshold `21` kills the first six. Survivors exactly `(β_1;δ_∞,δ_aff;M_∞)=(21;10,11;22)`, `(23;11,10;24)`, `(25;12,9;26)`, `(29;14,7;30)`. The largest threat is `β_1=29`, not `31`: `(8,2,31)` would require affine `Δ=(8,6,1)`, which fails axiom (2). Galindo's converse realises a one-place degree-8 curve of type `(8,6,3)`; it does not realise an `A^1`-normalisation with seven reduced off-diagonal nodes. That distinction is correctly kept.

**(9,6).** `a=3`, `3|9`, `3∤β_1`, `β_1>9`. For `Δ=(9,6,c)`: `n_1=n_2=3`, `3∤c`, `c<18`, and `3c∈⟨9,6⟩=3⟨3,2⟩` iff `c∈⟨3,2⟩` (automatically excluding `c=1`). No four-term sequence. Thus `c∈{2,4,5,7,8,10,11,13,14,16,17}`. Conversion `β_1=27-c`. One-pair formulae: `δ_∞=β_1-1`, `M_∞=β_1+2`, cluster `M(3,β_1)` which is `(3^k,1^3)` for `β_1=3k+1` and `(3^k,2,1^2)` for `β_1=3k+2`. Genus `28`:

| `c` | `β_1` | `δ_∞` | `δ_aff` | `M_∞` |
|---:|---:|---:|---:|---:|
| 17 | 10 | 9 | 19 | 12 |
| 16 | 11 | 10 | 18 | 13 |
| 14 | 13 | 12 | 16 | 15 |
| 13 | 14 | 13 | 15 | 16 |
| 11 | 16 | 15 | 13 | 18 |
| 10 | 17 | 16 | 12 | 19 |
| 8 | 19 | 18 | 10 | 21 |
| 7 | 20 | 19 | 9 | 22 |
| 5 | 22 | 21 | 7 | 24 |
| 4 | 23 | 22 | 6 | 25 |
| 2 | 25 | 24 | 4 | 27 |

Integer equivalence `M_∞≤3d-3` ⇔ `M_∞<3d-2` makes equality at `24` still fire (`C'^2-2δ_aff=1>0`). First nine types die; survivors `(Δ;β_1;δ_∞,δ_aff;M_∞)=((9,6,4);23;22,6;25)` and `((9,6,2);25;24,4;27)`. Class demand is six resp. four reduced double fibres of an immersive parametrisation. AM supplies neither existence nor exclusion.

Chau/A' non-kills on both rows are correctly negative: `(8,6)` is reduced `(4,3)`, `(9,6)` is reduced `(3,2)`; equal-product is unavailable (`n'≠1` at `(8,6)`, and `6∤9` at `(9,6)`). OPEN[ROW-(8,6)-NODAL-REALIZATION+S4-TUPLE] and OPEN[ROW-(9,6)-NODAL-REALIZATION+S4-TUPLE] are the safe remainders. Six numerical types in all.

## 6. Ledger consumption discipline

**Verdict: HOLDS.** The final table matches the re-derived row statuses, and the four forbidden consumptions are absent.

No A'(5). The only uses of Theorem A' are (i) to record that A'(1)--(4) do not kill the surviving types and (ii) to invoke A'(4) at `(8,4)` as a non-controlling equal-product constraint. Both cite the residual hostile review's promotion of A'(1)--(4) and its withhold of A'(5). A kill never depends on A'.

No coprime order fork off-stratum. The sweep's §0 states that the order-three/order-four fork is a coprime-Main-Theorem subtheorem and that off the coprime stratum only A'(1)--(4) are available, with `c(Π)` the cycle count (an order-three element of `S_4` has two cycles). The two `(6,3)` kills apply the full Main Theorem only after an automorphism has made `gcd=1`; that is on-stratum, not an off-stratum fork. The `(9,3)` shear to coprime pairs is an independent check of the same kind.

No AM converse. Sections 7--9 of the sweep treat Galindo's converse as producing a one-place curve of the stated δ-sequence, and explicitly refuse to upgrade that to an `A^1` normalisation with the displayed number of reduced double fibres. The six numerical types remain OPEN on realisation.

No attainment overclaim. The only in-class attainments proved are the target-equivalent three-node curves in rows `(6,4)` and `(8,4)`. Neither is asserted to carry a global residual `S_4` representation. Numerical admissibility is not called existence. `T` is not defined into a theorem. (M-INF-T) is not consumed.

Nori scope. The two M-INF kills use N-A-RES at `T=0` on the nodal subclass, which is the promoted package. They do not use the refuted `B(C)>0` extension, the reversed factor-2 erratum, or a self-tangent coefficient. The coordinator's instruction to charge `4T` rather than `2T` until the tacnode test is settled is respected by simply not running a tangential Nori gate.

Coordinator alignment. The NA integration's provisional table (four KILLED, one geometric class, six numerical types, missing lemma `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`) is exactly the sweep ledger. It remains provisional until this review; the mathematics of the ledger is not the defect.

## 7. Verdict per row and promotion recommendation

| row | sweep claim | this gate | note |
|---|---|---|---|
| `(6,3)`--`(7,4)` | KILLED, triangular to `(5,3)` | **CONFIRMED** | Main Theorem after `T(u,v)=(u-φ(v),v)`; `δ_1\|δ_0` makes `φ` univariate |
| `(6,3)`--`(8,3)` | KILLED, triangular to `(4,3)` | **CONFIRMED** | same; `(4,3)` is an A(3) survivor but not a Main-Theorem survivor |
| nodal `(8,2)` | KILLED, (M-INF) | **CONFIRMED** | three types, `M_∞≤18<21`; tangential realisations unclaimed |
| nodal `(9,3)` | KILLED, (M-INF) | **CONFIRMED** | five types, `M_∞≤21<24`; coprime shears are a check |
| nodal `(6,4)` | OPEN, sole `Δ=(6,4,3)`, `(7,3,16)`, three-node attained | **CONFIRMED** | identity and double-point scheme re-derived; nodes, not tangencies |
| nodal `(8,4)` | OPEN, sole `(8,4,6,3)`, target-equivalent | **CONFIRMED** | `P=p+q^2` is elementary; one geometric class |
| nodal `(8,6)` | OPEN, four numerical types | **CONFIRMED** | `β_1∈{21,23,25,29}`; AM ⇏ nodal matching |
| nodal `(9,6)` | OPEN, two numerical types | **CONFIRMED** | `(23;22,6;25)`, `(25;24,4;27)`; equality at `M=24` still fires |

**Promotion recommendation: PROMOTE the four kills and the exact residual ledger, at the typed scopes above.** Promote also: the `(6,4)` three-node witness as an in-class attainment of `Δ=(6,4,3)`; the elementary equivalence of that witness with the unique `(8,4)` survivor; the two numerical lists as complete Galindo censuses, not as existence theorems.

Do not promote: a tangential kill of `(8,2)` or `(9,3)`; any (M-INF-T) statement; an AM-converse realisation of the six higher types; A'(5); an off-stratum order fork; a claim that the three-node curve carries the residual `S_4` representation.

The topological core after this sweep is one target-isomorphism class of an explicit three-node sextic, plus six AM-numerical types whose nodal matching schemes are themselves unproved. A safe successor is either a noncoprime braid fixed-tuple theorem with route-to-node data for the `(6,4)` cable, or an exact divided-difference obstruction for each of the six types. FALLACY-v2 does not change a verdict: no flag/place/series identification, no `FULL_ACTUAL_EXIT` from a representative, no pole identity, no `sat()` wrap, and no floor promoted to attainment.

No `charge_basis` line: this review consumes promoted prices and does not assert a new exit.

## 8. Sources consulted

Charged frozen inputs, hashes in §0.

Primary literature, re-fetched in this lane:

```text
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9
  C. Galindo--F. Monserrat, arXiv:0910.2613v2, Theorem 2.1 and
  Proposition 2.1. 241372 bytes.
```

Promoted campaign statements used at their written scopes, not re-proved here: PI1-S4 Main Theorem as corrected (N≤19 integration §1.1); D1-DEGREE target-automorphism invariance (hostile review Item 1, applied to both elementary families); `M_emb=a+β_h-1` as corrected; Corollary N-A-RES at `T=0`; A'(1)--(4) as negative controls only.

Classical facts used without a hashed citation: Euclidean multiplicity blocks for a plane branch; `δ=Σ m(m-1)/2`; genus `(d-1)(d-2)/2`; elementary automorphisms of `A^2` have Jacobian `1`; the numerical semigroup `⟨3,4⟩` has genus `3` and is the unique oversemigroup of `⟨4,6⟩` of that genus; cubic discriminant `18abcd-4b^3d+b^2c^2-4ac^3-27a^2d^2`.

Not consumed: Orevkov 1990; Abhyankar--Moh 1975 original PDF (not obtained); GB--P Theorem 6.4 as a scalar cap; Nori's `B(C)>0` form; AM converse as nodal realisation; (M-INF-T); A'(5).

Execution. Desk-scale arithmetic only. The §3 polynomial identity was expanded by hand through degree 12; the minus-sign double-point branch was reduced to `σ=0`; pair/image/tangent determinants were evaluated on the cubic. No CAS, no computation of uncertain duration, no second output file.

<!-- BODY-END -->

