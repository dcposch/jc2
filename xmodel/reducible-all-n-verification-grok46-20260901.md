# Verification lane: REDUCIBLE-ALL-N — computation arm

**Lane.** Independent computation arm of the paired review of
`reducible-all-n-opus5-20260901.md`, with coordinator integration
`block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md`
as secondary charged input.

**Scope.** Desk-scale exact reasoning only. No CAS. No `jc2-lean`.
No edits to charged files or canonical ledgers.

**Date.** 2026-09-01
**Agent.** grok-4.6

This report does not declare a `charge_basis`.

## 0. Hash verification of charged inputs

Frozen copies were hashed with `shasum -a 256` **before any was read**. Both reproduce the boxed manifest. The stop condition did not fire.

```text
7c63614eff87640789d4591c67d8f8ce7d48645310d3146e87c44ddfc0dddf89
  .../inputs/reducible-all-n-opus5-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9
  .../inputs/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Primary PDFs in `refs/` were rehashed at execution and agree with the charged report §0:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
```

Palka (arXiv:1405.5391) was not re-fetched: no target below consumes Theorem A/B as a numerical identity. No CAS. No `jc2-lean`. No charged file or canonical ledger edited. One output file only.

**Execution disclosure.** Finite integer arithmetic and set-partition listing of `(μ,s,k)`-ownership profiles; explicit Jacobian expansion of one triangular family; one plane-curve gradient and one Puiseux germ at infinity, all by hand. FALLACY-v2 in force. No `charge_basis` line: this arm asserts no new exit price.

**Constraints used for the census (charged CAGE-N 1–6, applied as filters).** Budget `Σ_i W_i + K_tot = N−1` with `c_l = μ_l s_l + K_l`; RED-N: `m≥2`, at least one trivial `(μ,corr,s)=(1,0,1)`, at least one `μ≥2`; `s_l=1` whenever `μ_l=2` (NO-RAM-2); no ramified carrier (`μ≥3`, `s≥2` costs `≥6`, already over budget at `N≤7` after a trivial and a second owner); Gate SELF: `2W_i ≤ N` on every correction-free component; Gate LZ-KILL: `2W_br ≤ N` when `b=1`; components labelled up to permutation of like dicriticals. A **profile** is an ownership partition of the dicritical multiset (the N=5 grain: P3a ≠ P3b). A **class** is the branched meridian type `[λ^{(k)}]`.

## 1. Target (1): re-enumeration of general-N budget profiles at N=6 and N=7

All `s_l=1` at both degrees: a ramified carrier needs `μ≥3` (NO-RAM-2) and `s≥2`, hence cost `≥6`, plus a trivial and a second owner, total `≥8>N−1`. SELF/LZ at `N=6` is `W_i≤3` on every corr-free component and on the unique branched component; at `N=7` the same bound is `W_i≤3` (`2W≤7`).

### 1.1 N=6, budget 5

Cost-type multisets with a 1 and a part `≥2`. Dead on sight: `(1,0)^5` (Zariski–Nagata, §4.1); `(4,0)+(1,0)` (LZ: `W=4`); `(2,0)+(2,0)` stacked on one component (class `[22]`, `W=4`); anything of cost 5 with no trivial.

Surviving ownership partitions (W written in the order branched then unbranched):

| class | dicriticals | ownership | W | K |
|---|---|---|---|---|
| `[2]` | `(2,0)+B^3` | `A \| BBB` | (2,3) | 0 |
| | | `A \| BB \| B` | (2,2,1) | 0 |
| | | `A \| B \| B \| B` | (2,1,1,1) | 0 |
| | | `AB \| BB` | (3,2) | 0 |
| | | `AB \| B \| B` | (3,1,1) | 0 |
| `[2^(1)]` | `(2,1)+B^2` | `A \| BB` | (2,2) | 1 |
| | | `A \| B \| B` | (2,1,1) | 1 |
| | | `AB \| B` | (3,1) | 1 |
| `[2^(2)]` | `(2,2)+B` | `A \| B` | (2,1) | 2 |
| `[3]` | `(3,0)+B^2` | `A \| BB` | (3,2) | 0 |
| | | `A \| B \| B` | (3,1,1) | 0 |
| `[3^(1)]` | `(3,1)+B` | `A \| B` | (3,1) | 1 |
| `[2+2]` | `(2,0)^2+B` | `A \| A' \| B` | (2,2,1) | 0 |
| | | `AB \| A'` | (3,2) | 0 |

Fourteen profiles, six classes. Independent check of (BUD): every row has `Σ W + K = 5`. Independent check of (IND): `Σ ι = N−1−K−Σ s` holds on each class (`[2]`-spine `ι=1`; `[3]` `ι=2`; `[2+2]` `ι=1+1=2`).

Charged SS9: header “14 profiles, 6 classes”; per-class `#` = 4, 3, 1, 2, 1, 2, **sum 13**. Diff: the printed `[2] # 4` omits one of the five rows. The omitted row is `A \| BBB`, `W=(2,3)`: three trivials on one unbranched component, Gate SELF at equality `2W_u=6`. It is allowed by every CAGE-N filter (RC1: `W_i≤4`; `a=(4,3)`; (LOC) at a node of the unbranched component: `a_p+2·3=6` so `a_p=0`, six clusters of size 1, `G_p=1`, TRANS-LOC intact). N=5 P3b already allows two trivials on one unbranched component; the third trivial is the new N=6 budget unit.

**Internal inconsistency of the charged table:** header 14 matches this census; the `#` column sums to 13. The class list itself is complete (no extra class, no missing class). `[4]` and `[22]` are correctly absent.

### 1.2 N=7, budget 6

Same filters, `W≤3`.

| class | # here | charged # | rows (W) |
|---|---|---|---|
| `[2]` | 7 | 6 | (2,3,1), (2,2,2), (2,2,1,1), (2,1^4), (3,3), (3,2,1), (3,1^3) |
| `[2^(1)]` | 5 | 4 | (2,3), (2,2,1), (2,1^3), (3,2), (3,1,1) |
| `[2^(2)]` | 3 | 3 | (2,2), (2,1,1), (3,1) |
| `[2^(3)]` | 1 | 1 | (2,1) |
| `[3]` | 3 | 3 | (3,3), (3,2,1), (3,1^3) |
| `[3^(1)]` | 2 | 2 | (3,2), (3,1,1) |
| `[3^(2)]` | 1 | 1 | (3,1) |
| `[2+2]` | 4 | 4 | (2,2,1,1), (2,2,2), (3,2,1), (3,3) |
| `[2+2^(1)]` | 3 | 2 | (2,2,1); (3,2) trivial on the `k=0` side; (2,3) trivial on the `k=1` side |
| `[2+3]` | 2 | 2 | (2,3,1); (3,3) trivial on the `[2]` side. Trivial on the `[3]` side is `W=(2,4)`, SELF/LZ dead |

Killed and correctly omitted: `[4]`/`[4^(1)]`/`[5]` (`W_br≥4`); `[22]` (`W=4`); `(2,0)^3` (no trivial).

Thirty-one profiles, ten classes. Header “31 profiles, 10 classes” matches. Per-class `#` sums to 28. Three misses, all `W=3` on a corr-free owner at `u≤1` or on the distinguished `k=1` side:

- `[2]`: `(3,3)` — one trivial on `D_br`, three on one unbranched;
- `[2^(1)]`: `(2,3)` — three trivials on one unbranched;
- `[2+2^(1)]`: trivial glued to the `(2,1)`-component, `W=(2,3)`.

(BUD)/(IND) re-checked on every class: `Σ W+K=6`; spine `ι=1` with `Σ s=T+1` and `K=k` gives `6−k−(T+1)=1` since `T=4−k`; `[3]` `ι=2`; `[2+2]` `ι=2`; `[2+3]` `ι=3`.

### 1.3 Diff summary

Classes at N=6 and N=7 match the charged list (6 and 10). Header totals match the independent ownership census (14 and 31). The printed `#` column undercounts four classes by one row each. No class is extra; no class is missing; the ramified and `W≥4` packets are correctly dead.

**Verdict, target (1): BROKEN** on the per-class multiplicities (and on the internal header-vs-`#` arithmetic). The class list and the header totals HOLD. The four missing rows are listed above and satisfy every charged filter.

## 2. Target (2): N=4 / N=5 instance recovery against the promoted cages

Same filters, now at the closed degrees. SELF/LZ is `2W≤N`.

### 2.1 N=4, budget 3. Bound `W_i≤2`

Only cost multiset with a 1 and a part `≥2`: `(2,0)+(1,0)`. Ownership: two components, `W=(2,1)`, `K=0`, class `[2]`. LZ: `2W_br=4≤4`. The `t_br=1` attempt stacks both dicriticals on one component and leaves `m=1`, excluded. `(3,0)` has no trivial. `(1,0)^3` is Zariski–Nagata. `(2,1)` has no trivial.

Exactly one row: core `(2,1,0)`, `W=(2,1)`. Charged SS8: “exactly one row (core `(2,1,0)`, `W=(1,2)`)”. Same unordered pair. This is the unique N=4 reducible-with-trivial profile (corr=0 on both dicriticals, branched meridian a transposition, unbranched meridian trivial) that the N=5 report records as the N=4 residual at ALLN §5.2 / C19 §1. The coordinator’s “six AM-numerical candidate types” are infinity-types of this one profile, not extra dicritical rows.

### 2.2 N=5, budget 4. Bound `W_i≤2`

| profile | W | K | charged N5 | gate |
|---|---|---|---|---|
| `(2,0)+B^2`, `A \| B \| B` | (2,1,1) | 0 | S2 / P3a | lives |
| `(2,0)+B^2`, `A \| BB` | (2,2) | 0 | S2 / P3b | lives |
| `(2,0)+B^2`, `AB \| B` | (3,1) | 0 | P3c | SELF/LZ `2W=6>5` **dead** |
| `(2,1)+B`, `A \| B` | (2,1) | 1 | S1 / P1 | lives (`k=1`, SELF does not apply to `D_br`; LZ `4≤5`) |
| `(3,0)+B`, `A \| B` | (3,1) | 0 | P2 | LZ `6>5` **dead** |

No `b=2` row: two nontrivial carriers cost `≥4` and leave no trivial. No ramified row: Lemma B already forces `s=1` at this budget (N5 §2.2), recovered here from NO-RAM-2 plus the cost floor.

Charged SS8: “S2 (core `(2,1,0)`, `W=(1,1,2)` or `(2,2)`) and S1 (core `(2,1,1)`, `W=(1,2)`), with P2 and P3c killed by Gate SELF/LZ-KILL. No row of the closed degrees is lost and none is added.” Row-for-row match against N5 §2.3 / §4.5 / §5.1–5.2.

### 2.3 Control on the counting grain

N=5 S2 is two ownership rows, not one. The independent grain used in §1 is the same grain: if `[2]` at N=6 were counted only by `(t_br, u)`, N=5 would still show two S2 rows (the two `u` values), and the N=6 miss `W=(2,3)` is a genuine extra ownership, not a double-count of `(t_br,u)`.

**Verdict, target (2): HOLDS.**

## 3. Target (3): NO-DEG-CAP family

Charged statement: `deg A_F` admits no bound in terms of `N`, via `T(x,y)=(x, y+x^k)` acting on the target. Re-derived.

### 3.1 The family

For `k≥1` let `T_k: C^2 → C^2` by `T_k(x,y)=(x, y+x^k)`. Inverse `T_k^{-1}(x,y)=(x, y−x^k)`, polynomial. Jacobian matrix `[[1,0],[k x^{k−1}, 1]]`, determinant 1. So `T_k ∈ Aut(C^2)` with constant Jacobian. Coefficient field `C`, generator order `(x,y)`, image of generators as written.

Let `F=(P,Q)` be Keller of geometric degree `N`. Then `T_k ∘ F = (P, Q+P^k)`. Expanding the Jacobian:

```text
P_x (Q_y + k P^{k-1} P_y) − P_y (Q_x + k P^{k-1} P_x)
  = P_x Q_y − P_y Q_x
  = Jac(F).
```

So `T_k ∘ F` is Keller. Geometric degree: for generic `(a,b)`, the fibre of `T_k ∘ F` over `(a,b)` is the fibre of `F` over `(a, b−a^k)`; `T_k` is bijective, so the two generic fibre-cardinalities agree. Non-proper value set: `q` is a non-proper value of `T_k ∘ F` iff some `p_n→∞` has `T_k(F(p_n))→q` iff `F(p_n)→T_k^{-1}(q)` (homeomorphism of `C^2`) iff `T_k^{-1}(q) ∈ A_F`. Thus `A_{T_k ∘ F} = T_k(A_F)`.

Dicritical numbers: `μ` is the local degree of `F` on a source-transversal to a dicritical, equivalently the sheet-count of a small target-transversal to `D` about a generic point. `T_k` carries a small transversal to `D` to a small transversal to `T_k(D)` (local biholomorphism of the affine target), and source fibres match, so `μ` and the jump divisor `corr` are unchanged. The map `l' → T_k(D)` is `T_k|_D ∘ (l' → D)`; `T_k|_D: D → T_k(D)` is an isomorphism of affine curves, so `s_l` is unchanged. Ownership is unchanged.

### 3.2 Degree growth, explicit

If `D` has equation `f(x,y)=0` of degree `d` and `r = deg_y f ≥ 1`, then `T_k(D)` has equation `f(x, y−x^k)=0` of degree `max(d, k r)`, unbounded in `k`. The case `r=0` is a union of vertical lines, excluded by Lemma NL (no component is a line). Sample: `D = {y=x^2}` (degree 2), `T_k(D) = {y = x^2 − x^k}`, degree `k` for `k>2`. Sample with a node: `D = {y^2 = x^2(x+1)}` (nodal cubic), `T_k(D)` has equation `(y−x^k)^2 = x^2(x+1)`, degree `max(3,2k)`.

This is a family of target automorphisms, not a family of Keller maps constructed from scratch. Operationally: there is no function `B(N)` such that every noninvertible Keller map of geometric degree `N` has `deg A_F ≤ B(N)`, because any one such `F` with `A_F ≠ ∅` (and noninvertible Keller maps are not proper, so `A_F ≠ ∅`) produces `T_k ∘ F` of the same `N` and unbounded degree. Floor/attainment: this is the absence of a ceiling, not an exact degree formula. It does not realise any SS9 class; it only says raw `deg A_F` is not a gate. The `d_min` restatement in charged SS6 is the surviving form.

**Verdict, target (3): HOLDS.** The exhibited family is `T_k(x,y)=(x,y+x^k)`, `k≥1`, with the identities above.

## 4. Target (4): three N=6 gate applications (Zariski–Nagata, eta/cover, per-component M-INF)

Three numerical applications at `N=6`, one per named gate. No profile is claimed realised.

### 4.1 Zariski–Nagata / branch-locus nonemptiness

Packet `(1,0)^5`. Budget: five trivials, `Σ W = 5 = N−1`, `K=0`. Every meridian has cycle type `1^6` (all `μ=1`, `s=1`), so `ρ` is trivial. The covering `C^2 \ F^{-1}(A_F) → C^2 \ A_F` would be 6 disjoint copies. Both total space and base are complements of curves in `C^2`, hence connected. Contradiction. The packet is dead. (IND) is consistent rather than obstructive: `Σ ι = 5−0−5 = 0`. The kill is transitivity, not the budget.

Control in the other direction: `[2+2]` at `N=6` is the first `b=2` packet (`W=(2,2,1)` or `(3,2)`). Two transposition meridians, image contains a transitive subgroup generated by transpositions, so `G=S_6`. Zariski–Nagata does **not** kill it. Charged SS2’s claim that `b=2` first appears at `N=6` is the matching numerical statement (`2b ≤ N−2` becomes `b≤2`).

### 4.2 eta/cover (Gate SELF) at three N=6 rows

corr=0 and `s=1` ⇒ `h_l` iso and `dφ ≠ 0` ⇒ `η` immersive. Gate EMB forbids a smoothly embedded `A^1`, so some point has `r≥2`, and (LOC) gives `2W_i ≤ 6`.

| row | corr-free W | `2W` vs 6 | r-cap `⌊6/W⌋` | verdict |
|---|---|---|---|---|
| `(4,0)+(1,0)`, `W=(4,1)` | 4 | 8>6 | `⌊6/4⌋=1` so r=1, immersive+injective | **dead** (embedded `A^1`) |
| `[3]` `W=(3,2)` | 3 and 2 | 6=6, 4<6 | r≤2 on `D_br` | **lives** (equality; N=5 P2 was `2W=6>5`) |
| `[2]` `W=(2,3)` | 2 and 3 | 4<6, 6=6 | r≤2 on the unbranched | **lives** at equality |

The N=5 Gate AMS (`W≥3` and corr=0 ⇒ `5/W<2` ⇒ embedding ⇒ line) is strictly stronger than SELF, and it is the reason P2/P3c die at N=5. At N=6 the same numerical test leaves `W=3` alive. That is the eta/cover mechanism applied per component, and it is what admits the extra `[2]` row of §1.1.

### 4.3 Per-component M-INF

Two numerical layers: the local `M_t` / (LOC) identity on three N=6 profiles, and N-A-RES (`M_∞+2T ≤ 3d−3 ⇒ π_1=Z`) on an explicit polynomial quintic in the `[2]` hypothesis class.

**(LOC) / cluster sizes.** `a_p + Σ_i r_{i,p} W_i + K_p = 6`.

- `[2]` `W=(2,1,1,1)`, `K=0`. Generic on `D_br`: `4+2=6`. Node of `D_br` (`r=2`): `a+4=6`, `a=2`. Generic on an unbranched: `5+1=6`.
- `[3]` `W=(3,2)`, `K=0`. Generic on `D_br`: `3+3=6`. Node of `D_br` at equality: `a+6=6`, `a=0`. Generic on the unbranched: `4+2=6`. Node of the unbranched: `a+4=6`, `a=2`.
- `[2+2]` `W=(2,2,1)`, `K=0`. Generic on a branched: `4+2=6`. Node of one branched, off the other: `a+4=6`, `a=2`. Two branched components meeting, `r=1` each: `a+4=6`, `a=2`.

All values are nonnegative integers. For a trivial dicritical, `M_t = e_t·1 + k_t = 1`. For the `(2,0)` carrier, generic `M_t=2`; at a node of `D_br` the two places are two clusters of size 2. For `[2^(1)]`, `K=1` sits at one `t_0` with `M_{t_0}=3` (CUSP-2: `k=ν−1=1` ⇒ ordinary cusp `(2,3)`), and (LOC) at that point with `r=1` reads `a+2+1=6`, `a=3` if the unbranched miss it.

**(N-A-RES on an explicit quintic).** `[2]` at N=6 has `ι=1`, so DEG-PER / (TG-N) give `d_br ≥ 5`. Take

```text
φ(t) = (t^2, t^5 − t),     F(x,y) = y^2 − x(x^2−1)^2.
```

Degree 5. Gradient: `F_y=2y`, `F_x=−(x^2−1)(5x^2−1)`. Singularities require `y=0` and `F_x=0` and `F=0`, hence `x∈{0,±1}` from `F=0`; at `x=0`, `F_x=−1≠0` (smooth); at `(±1,0)` both partials vanish. Parametrization: `φ(1)=φ(−1)=(1,0)`, `φ(i)=φ(−i)=(−1,0)`, and `φ'(t)=(2t, 5t^4−1)` is never zero (at `t=0`, `φ'=(0,−1)`). Two ordinary nodes, immersive, not injective. One point at infinity: homogenise `Y^2 Z^3 = X(X^2−Z^2)^2`; at `Z=0` one gets `X^5=0`, the single point `[0:1:0]`. Chart `Y=1` with `s=1/t`: `(X/Y, Z/Y) ∼ (s^3, s^5)`, one place, characteristic `(3,5)`. Then `M_emb = 3+5−1 = 7 = M_∞`. Ordinary nodes, `T=0`. Threshold `3d−3=12`. So `M_∞+2T=7≤12`: N-A-RES fires, `π_1(C^2−D)=Z`, and this curve cannot carry a transitive `S_6`-image generated by transpositions.

Control: the graph `y=x^5` is a smoothly embedded `A^1` (Gate EMB). Homogenised `YZ^4=X^5`, germ `z^4=x^5` at `[0:1:0]`, `M_emb=4+5−1=8≤12`, N-A-RES fires, consistent with `π_1=Z` after `T(x,y)=(x,y−x^5)`.

Coprime-bidegree family at `d=5`: `φ(t)=(p_m, q_5)` with `gcd(m,5)=1`, `m∈{1,2,3,4}`. Leading terms send `∞` to `[0:1:0]` in the `Y=1` chart as `(s^{5−m}, s^5)`, so `M_∞=(5−m)+5−1=9−m`. The case `m=1` is a graph (EMB). For `m=2,3,4` one has `M_∞∈{7,6,5}`, all `≤12`. The explicit quintic is `m=2`. This is a T=0 slice kill inside `[2]` at the DEG-PER floor, not a class kill: `d≥6` or `T≥1` can violate `M_∞+2T≤3d−3` (at `d=6` the threshold is 15). Charged SS9’s “N-A-RES applies row-by-row to the `k=0`, `b=1` classes only” is the right scope; the quintic is the numerical content of that row-by-row at `d=5`.

**Verdict, target (4): HOLDS.** All three gates fire on the packets above as claimed; SELF at equality is sharp and is what lets `W=3` live; N-A-RES kills every T=0 one-place polynomial quintic (all have `M_∞≤8≤12`) and does not kill class `[2]`.

## 5. Verdict table

| # | target | verdict | note |
|---|---|---|---|
| 1 | N=6 / N=7 budget census vs charged SS9 | **BROKEN** | Class lists HOLD (6 and 10). Header totals HOLD (14 and 31). Per-class `#` undercounts four classes by one row each; `#` sums (13, 28) disagree with the headers. Missing rows: N=6 `[2]` `W=(2,3)`; N=7 `[2]` `W=(3,3)`, `[2^(1)]` `W=(2,3)`, `[2+2^(1)]` trivial on the `k=1` side. All four pass CAGE-N 1–6. |
| 2 | N=4 / N=5 instance recovery vs promoted cages | **HOLDS** | N=4: unique row core `(2,1,0)`, `W=(2,1)`. N=5: S1 = `(2,1)+(1,0)` `W=(2,1)`; S2 = P3a `W=(2,1,1)` and P3b `W=(2,2)`; P2 and P3c killed by SELF/LZ. No row lost, none added. |
| 3 | NO-DEG-CAP family | **HOLDS** | `T_k(x,y)=(x,y+x^k)`: Jac=1, inverse polynomial; `Jac(T_k∘F)=Jac(F)`; geometric degree preserved by fibre translation `(a,b)↦(a,b−a^k)`; `A_{T_k∘F}=T_k(A_F)`; `(μ,corr,s)` preserved; `deg T_k(D)` unbounded once `deg_y f ≥1`. Absence of a ceiling, not an attainment. |
| 4 | N=6 Zariski–Nagata, eta/cover, per-component M-INF | **HOLDS** | `(1,0)^5` dead by transitivity. SELF kills `W=4`, keeps `W=3` at equality (the N=5 AMS embedding test does not fire). (LOC) integer-exact on three profiles. N-A-RES kills the explicit nodal quintic `y^2=x(x^2−1)^2` (`M_∞=7≤12`) and every T=0 one-place polynomial quintic (`M_∞≤8`); class `[2]` remains open at `d≥6` or `T≥1`. |

No target is UNTESTABLE. No `charge_basis` line.

## 6. Notes, OPEN items, and FALLACY-v2 flags

**What this arm does not touch.** Lemma CUSP-2 / NO-RAM-2 as local analytic statements (only their numerical consequence `s=1` at `μ=2` was used as a filter); Gate LZ-KILL’s appeal to Palka Theorem A; the Zariski generic-line surjection in Gate TG-N (charged `OPEN[ZARISKI-GENERIC-LINE-CUSTODY]`); N=8 header 104, which was not re-enumerated. The four missing rows of §1 are ownership profiles, not Keller witnesses.

**Coordinator file.** Used only as the lineage marker that Theorem 7.B has closed the irreducible side at every degree, so RED-N is the surviving front, and that the N=4 residual is one dicritical profile whose remaining content is AM-numerical / PI1-S4, matching §2.1.

**FALLACY-v2.** Flag/place/series: `t ∈ l'`, `π(t)`, `z=h_l(t)`, `η(z)` kept distinct in the (LOC) counts (`M_t` vs `W_i` vs `r_{i,p}`). Carrier/attainment: no SS9 class is realised; `T_k` is a target automorphism acting on a hypothetical `F`, not a constructed Keller map. Floor/attainment: (TG-N) `d_br≥5`, SELF `2W≤N`, N-A-RES `M_∞+2T≤3d−3` are used only as filters or slice-kills; NO-DEG-CAP is the absence of a ceiling. Variable/ring map: `T_k` declared with images of generators, Jacobian, inverse, and coefficient field. Pole/interior, `sat()`, prime-label, merge-free, target/arrival: not in play. No gap filled by cap or analogy: the N=8 table and CUSP-2 are left unread as proofs.

**OPEN.** The four missing rows of §1 should be restored in any promotion of SS9. Whether `a_p=0` at an unbranched node with `2W=N` is geometrically realisable by three distinct trivial dicriticals (rather than merely budget-legal) is a geometric question this arm does not close; numerically it satisfies every charged filter, including the N=5 precedent of two trivials on one unbranched component.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20589`.
- Body SHA-256:
  `89e157560cbc360f277ee8b050ed605273490086931615d6da781e81e5eda0b4`.
- Frozen basis: `27b3a801aafd69c9860f51f9f4ea1cc89f638270`.
