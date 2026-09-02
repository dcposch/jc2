# B3-CENSUS-DEG5-DEG6 — exact raw census, spine substitution, and the general-N assembly boundary

**Lane.** `B3-CENSUS-DEG5-DEG6`  
**Date.** 2026-09-02  
**Method.** Frozen inputs only; exact Python/SymPy 1.14.0 integer arithmetic.
No web access, `jc2-lean`, or canonical-ledger edit; this report is the only
repository write.

## 0. Result

The raw census and the affine profile substitution are complete and exactly
reproducible:

```text
Rows(2..7)       = 3, 6, 23, 51, 192, 430
Census(4..7)     = 35, 86, 287, 717
Rows(4), (n=1)   = 23

(B3) charged cells
N=5              = 3
N=6              = 9 = 2 at (a,W)=(3,3) + 7 at (4,2)
```

The ninth `N=6` cell is
`C_1+C_1+M_{2,1}` (two `K=1` cusps and one charged `r=2`
multibranch point), with the review's one-neutral-node `2p_a` cap `3`.
Every affine fibre partition is listed in §3.

There is **no certified EMPTY window at `N=5` or `N=6`**. The review declares
the successor bounded and well-posed (`BR:269–274`), but the requested
endpoint-transition derivation, determinant pruning, and global-graph list
have not been completed from the frozen statements. This is a mathematical
OPEN, not a resource-limit stop. A raw row records contacts without saying
whether each contact ends or continues to another fork. At `N=4` those choices
are settled by the four-sheet identity, Corollary 4, and Lemmas 8–9. No
general-`N` transition table is present. BI-8 caps forks on one spine; it does
not itself give a whole-graph fork bound or attain its cap.

The exact direction-agnostic first-fork row catalogs (the incident `W`-tube
may occur in any labelled direction) have sizes:

```text
N=5,  (a,W)=(3,2):  67
N=6,  (a,W)=(3,3): 181       (the two a=3 profiles)
N=6,  (a,W)=(4,2): 238       (the seven a=4 profiles)
```

If the incident `g`-side is identified with Proposition 3's distinguished
`R` direction at general `N`, the corresponding unmarked row subcatalogs are
`35`, `85`, and `126`. That identification is explicit in the N=4 replay but
is not promoted all-N by the inputs, so these smaller counts are conditional.
Both are unresolved row candidates, not realised graphs; the raw catalogs
remain `86`/`287`.

The `N=4` control does close through the original pipeline: the 35 rows reduce
to the six global graphs 20–25; Lemma 10 kills 24–25, Lemma 11 kills 22–23,
and Lemmas 12–15 kill 20–21. No `(H-∞)` assertion is used in that kill.

Finally, recomputing the charged-profile generating function at `N=7` gives
`32=6+26`, not the stipulated `33`. The raw `717` is correct. The discrepancy
is isolated as one coefficient reconciliation in §3.5; it is not silently
adjusted.

No exit-price assertion is made, so no `charge_basis` declaration is
applicable.

## 1. Custody, scope, and source map

The mandatory hash gate was run before reading. The five results were exactly:

```text
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  b3-boundary-instrument-opus5-20260902.md
048667793c3d34fc568269602fd8c786e9fab09ebbfb9ccd308041bb2cf6bc8f  b3-boundary-instrument-review-grok46-20260902.md
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  do1-mu2-replay-sol56-20260901.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
```

All citations refer to the charged frozen-input directory. Abbreviations are
`BI` (producer), `BR` (review), `DR` (charged DO replay),
`MI` (`MPRIME-ALLN-H2`), and `HF` (`HORN-FLAGSHIP`).

The scope is Keller, noninvertible, `H2`, and case `(B3)`. BI-3 and the
saturation half of BI-5 are used only conditionally under `(H-∞)`; `(H-∞)` is
not promoted at `N=4` or anywhere else (`BR:121–141`). `SCOPE[B3-QH]` is used
only when quoting the local cusp cage, never to create a boundary determinant
constraint. Excluded throughout: `Z(G)=1`, case (A), `A2`, `(B2)`, and every
unfrozen DO source.

The binding degree-free boundary package is exactly:

* `Deg=m n` and `sum Deg=N` over each irreducible target curve;
* repaired Proposition 4 (fork Riemann–Hurwitz);
* Lemma 5's one-/two-contact determinant transfer;
* Proposition 3: `det R_v=1`, `det L_v,det D_v>1`, with the branch
  determinants pairwise coprime, and `det L=-1`;
* Lemmas 2–4, repaired Lemma 7 as a lower bound only, and the edge formula.

This is `BI:131–173` and `BR:177–181`. The N-dependent value occurs in
`sum Deg=N`; it is not permission to reuse Corollary 4 or the six N=4 graph
calculations.

## 2. Raw census: exact enumeration

### 2.1 Definition

For a fork of longitudinal degree `m>=2` and transverse degree `n>=1`, let
`lambda_L,lambda_R,lambda_D` be the three partitions of `m` recording the
longitudinal contact indices. If `ell(lambda)` denotes length, fork
Riemann–Hurwitz is

```text
ell(lambda_L)+ell(lambda_R)+ell(lambda_D)=m+2.
```

The printed degrees on the incident constant tubes are `n` times the parts.
Thus, with `P(m,r)` the number of partitions of `m` into exactly `r` parts,

```text
f_m(z)   = sum_{r>=1} P(m,r) z^r,
Rows(m)  = [z^(m+2)] f_m(z)^3,
Census(N)= sum_{m=2}^N floor(N/m) Rows(m).
```

Directions `L|R|D` are ordered; parts within one partition are not
(`DR:328–360`; `BR:185–196`).

### 2.2 Compact exhaustive row catalog

Strings such as `321` mean the partition `(3,2,1)`. In the third column, take
every distinct assignment of the displayed length multiset to `L,R,D`, then
every partition from the assigned length classes. This is an exact enumeration
of every row, not merely a count.

| `m` | partitions grouped by length | length multisets and row contributions | `Rows(m)` |
|---:|---|---|---:|
| 2 | `1:{2}; 2:{11}` | `(1,1,2):3` | 3 |
| 3 | `1:{3}; 2:{21}; 3:{111}` | `(1,1,3):3; (1,2,2):3` | 6 |
| 4 | `1:{4}; 2:{31,22}; 3:{211}; 4:{1111}` | `(1,1,4):3; (1,2,3):12; (2,2,2):8` | 23 |
| 5 | `1:{5}; 2:{41,32}; 3:{311,221}; 4:{2111}; 5:{1^5}` | `(1,1,5):3; (1,2,4):12; (1,3,3):12; (2,2,3):24` | 51 |
| 6 | `1:{6}; 2:{51,42,33}; 3:{411,321,222}; 4:{3111,2211}; 5:{21111}; 6:{1^6}` | `(1,1,6):3; (1,2,5):18; (1,3,4):36; (2,2,4):54; (2,3,3):81` | 192 |
| 7 | length counts `1,3,4,3,2,1,1` | `(1,1,7):3; (1,2,6):18; (1,3,5):48; (1,4,4):27; (2,2,5):54; (2,3,4):216; (3,3,3):64` | 430 |

Equivalently, assign the row ID

```text
R(m,n;i,j,k)=(m,n; P_{m,i}|P_{m,j}|P_{m,k})
```

to every ordered triple in the table satisfying the length equation, for every
`1<=n<=floor(N/m)`. This is the complete raw row, with no quotient by direction
permutations.

### 2.3 Degree cells and controls

| `N` | `(m,n): number of rows` | total |
|---:|---|---:|
| 4 | `(2,1):3`, `(2,2):3`, `(3,1):6`, `(4,1):23` | 35 |
| 5 | `(2,1):3`, `(2,2):3`, `(3,1):6`, `(4,1):23`, `(5,1):51` | 86 |
| 6 | `(2,1/2/3):3` each, `(3,1/2):6` each, `(4,1):23`, `(5,1):51`, `(6,1):192` | 287 |
| 7 | all N=6 cells plus `(7,1):430` | 717 |

For `N=4`,

```text
Census(4)=2*Rows(2)+Rows(3)+Rows(4)=2*3+6+23=35.
```

The charged `(m,n)=(4,1)` control is

```text
(1,1,4): 3  +  (1,2,3): 12  +  (2,2,2): 8  = 23,
```

exactly DR (5.1), `DR:342–360`. No affine datum enters this construction.

## 3. The `(B3)` charged profiles and their fibres

### 3.1 Exact finite generator

Put `W=N-a`. At `N=5,6`, `2 sum s_l<=W` with every `mu_l>=2` forces one
dicritical with `s=1`; it is `(s,mu)=(1,W)`. Hence `R=sum(s_l-1)=0`.
For a charged singular point write

```text
P=(r,K,a_p),                  a_p=N-r W-K.
C_K=(1,K,a-K),                a cusp,
M_{r,K}=(r,K,N-r W-K),        a charged multibranch point.
```

The exact rules are `K>=1`, `a_p>=0`, `sum K=a-1`, and at least one cusp.
The `(B3)` cell also contains a multibranch point. Following the charged
producer/review convention, the finite list records only the `K>0` points and
uses one neutral double point

```text
U_2=(2,0,N-2W)
```

as the displayed representative used in every tabulated one-`U_2` cap.
Further `K=0`
multibranch points are not bounded by `(K)` and are not new charged cells. Thus
`3` and `9` count finite **charged skeletons**, not all singular
configurations (`BI:696–699`).

Sources are BI-1/7.B' (`MI:82–88`), laws `(L),(K)` (`MI:222–272`),
localization (`MI:275–294`), THEOREM PROFILE (`MI:413–438`), and the reviewed
lists/caps (`BR:235–265`).

Because `s=1`, each branch over `p` has one dicritical point with local excess
`k_b`, and its escaping fibre part is `mu+k_b`. Therefore the full affine fibre
partition at `p` is

```text
1^(a_p)  +  (mu+k_1,...,mu+k_r),       sum k_b=K.
```

This is the pointwise fibre law, not a boundary `v_0` profile.

The displayed right-hand-side cap on `2p_a(E~-bar)` is recomputed from

```text
2 p_a(E~-bar) <= 1-a
  + sum_p r_p max(0,(r_p-1)W+K_p-1),
```

using the charged skeleton after adjoining exactly one neutral `U_2`, exactly
as in the review. That extra node is a display convention, not a
THEOREM-PROFILE consequence when the charged skeleton already contains an
`M_{2,K}`.

### 3.2 `N=5`: three cells

Here `(a,W)=(3,2)`, the dicritical is `(1,2)`, the generic meridian is
`1^3*2`, the incident constant block has Deg `2`, and BI-8 permits at most
`3` forks on its dicritical spine.

| ID | charged skeleton | charged-point fibres | neutral `U_2` fibre | reviewed one-`U_2` cap on `2p_a` |
|---|---|---|---|---:|
| `5.1` | `C_2` | cusp `(4,1)` | `(2,2,1)` | 1 |
| `5.2` | `C_1+C_1` | each cusp `(3,1,1)` | `(2,2,1)` | 0 |
| `5.3` | `C_1+M_{2,1}` | cusp `(3,1,1)`; charged `r=2` multibranch fibre `(3,2)` | `(2,2,1)` | 4 |

At a cusp the total `Ē_X` load on `l'` is `K` and is all same-branch. At the
neutral node it is `2W=4`, all exchanged; at `M_{2,1}` it is
`2(W+1)=6`, of which at most one is same-branch. These are BI-4 budgets, not
attained branch-by-branch determinant values.

### 3.3 `N=6`, `a=3`: two cells

Here `W=3`, dicritical `(1,3)`, generic meridian `1^3*3`, incident constant
block Deg `3`, and at most `3` forks on its dicritical spine.

| ID | charged skeleton | charged-point fibres | neutral `U_2` fibre | one-`U_2` cap on `2p_a` |
|---|---|---|---|---:|
| `6.1` | `C_2` | cusp `(5,1)` | `(3,3)` | 3 |
| `6.2` | `C_1+C_1` | each cusp `(4,1,1)` | `(3,3)` | 2 |

The neutral-node `Ē_X` load is `2W=6`, all exchanged. The canonical
coefficient at the dicritical in a putative Lemma-13 analogue is now
`mu-1=2`, not the N=4 value `1`; this change is load-bearing in §5.

### 3.4 `N=6`, `a=4`: seven cells

Here `W=2`, dicritical `(1,2)`, generic meridian `1^4*2`, incident block Deg
`2`, and at most `4` forks on its dicritical spine. A neutral double point has fibre `(2,2,1,1)`;
a neutral triple point `U_3=(3,0,0)` is also numerically allowed and has fibre
`(2,2,2)`. It is a neutral parameter, not an additional charged cell.

| ID | charged skeleton | charged-point fibres | one-`U_2` cap on `2p_a` |
|---|---|---|---:|
| `6.3` | `C_3` | `(5,1)` | 1 |
| `6.4` | `C_1+C_2` | `(3,1,1,1)` and `(4,1,1)` | 0 |
| `6.5` | `C_1+C_1+C_1` | three copies of `(3,1,1,1)` | -1 |
| `6.6` | `C_2+M_{2,1}` | `(4,1,1)`; `(3,2,1)` | 4 |
| `6.7` | `C_1+M_{2,2}` | `(3,1,1,1)`; `(4,2)` **or** `(3,3)` | 5 |
| `6.8` | `C_1+M_{2,1}+M_{2,1}` | `(3,1,1,1)`; two copies of `(3,2,1)` | 7 |
| `6.9` | `C_1+C_1+M_{2,1}` | two copies of `(3,1,1,1)`; `(3,2,1)` | 3 |

Cell `6.9` is the review's missed cell (`BR:251–263`). For `M_{2,2}`, total
`K=2` does not determine the branchwise split: `(k_1,k_2)=(2,0)` gives
`(4,2)`, while `(1,1)` gives `(3,3)`. Neither BI-4 nor B3-CAGE selects one,
so the displayed two-element set is exact.

For the displayed realization of cell `6.5`—three cusps, exactly one `U_2`,
and no other neutral point—the cap `2p_a(E)<=-1` forces `p_a(E)<=-1` and hence
`j>=2`; it does not make the charged skeleton empty (`BR:149–161`). Replacing
or adding neutral structure (for example `U_3` rather than `U_2`) changes the
right-hand side, so this conclusion is not a property of skeleton `6.5`
alone and the table is not an equality.

### 3.5 `N=7`: the stipulated `33` does not reproduce

Here `(B3)` gives `2a>=N` and `a<=N-2`, so only `a=4,5`; `W=3,2` again
forces the sole dicritical `(s,mu)=(1,W)`.

For fixed `(N,a)`, the charged-cell generator implied by the preceding rules is

```text
[x^(a-1)] (C(x)-1) M(x),
C(x)=prod_{K=1}^{a-1} (1-x^K)^(-1),
M(x)=prod_{r>=2,K>=1,N-rW-K>=0} (1-x^K)^(-1).
```

Each admissible pair `(r,K)` is a separate multibranch colour; `C-1` enforces
at least one cusp. Exact expansion gives:

```text
N=7, a=4, W=3: M-types {(2,1)}
                    x + 3x^2 + 6x^3 + O(x^4),  coefficient = 6;
N=7, a=5, W=2: M-types {(2,1),(2,2),(2,3),(3,1)}
                    x + 4x^2 + 11x^3 + 26x^4 + O(x^5), coefficient = 26.
```

Thus the stated rules give `6+26=32`, while `BI:794–798` prints `33` and the
charge repeats it. The hostile review confirms the `N=6` correction but does
not audit this `N=7` number. Adding arbitrary `K=0` points cannot repair a
finite charged-cell count. A concrete one-count reconciliation would split
`C_1+M_{2,3}` by branch excess: `(3,0)` has fibre `(5,2)`, while `(2,1)` has
fibre `(4,3)`, raising `26` to `27`. But `M_{2,2}`'s two fibre splits at N=6
are one cell here, so a convention explaining that asymmetry is still owed.
Safe status:

```text
OPEN[PROFILE-N7-33]
bounded quantity: one reconciliation of the coefficient 32 with the
                  stipulated 33 by an omitted typing/equivalence rule.
```

The `717` raw-row count is independent and verified.

## 4. What spine substitution actually prunes

### 4.1 Licensed data and the index-set separation

The unconditional substitution is:

```text
BI-1:  W+a=N; dicriticals are the n>=2 part over g; Ē_X is the n=1 part.
BI-5-Deg: over v_0, the incident dicritical block contributes W and all
          non-dicritical dominating components contribute total Deg a.
BI-8:  first block Deg W; number of forks on a dicritical spine <=a.
```

BI-1's hypotheses and lack of `(H-∞)` are `BR:109–114`; BI-5's unconditional
and conditional halves are separated at `BR:135–141`; BI-8 is only a cap at
`BR:163–169`.

The cusp/node partitions of §3 live over affine singular points and on points
of `l'`. They do not identify a row at a target boundary vertex. BI itself
states that neither `K_p` nor these fibre partitions bounds the number or type
of boundary forks (`BI:683–695`). Consequently all profiles with the same
`(N,W)` have the same boundary seed catalog. This is a theorem-interface fact,
not a failure to substitute the profiles.

### 4.2 The degree-only `v_0` alternatives

Without `(H-∞)`, it is forbidden to substitute the all-`n=1` list
`{(1,1,1),(1,2),(3)}` (`BR:275–280`). The unconditional replacement is the
finite multiset of factor pairs `(m,n)` whose products sum to `a`.

For `a=3` the five alternatives are `1+1+1`, `(2,1)+1`, `(1,2)+1`,
`(3,1)`, `(1,3)`, where `1=(1,1)`. For `a=4` the eleven are `1^4`;
one of `(2,1),(1,2)` plus `1+1` (2); two such components as `AA,AB,BB`
(3); one of `(3,1),(1,3)` plus `1` (2); or one of
`(4,1),(2,2),(1,4)` (3).

These are degree allocations, not mark-saturation profiles and not claims of
realisability. Contracted components contribute no `Deg` and remain invisible
to this list.

### 4.3 Exact first-fork incidence catalogs

For a raw row

```text
r=(m,n; lambda_L|lambda_R|lambda_D),
```

the first fork must satisfy `mn>W`, and the physical incident block must be
one actual contact tube. Without identifying its labelled direction, the
necessary incidence test is

```text
mn>W,
W in {n e : e in lambda_L or lambda_R or lambda_D}.
```

The N=4 figure convention takes the incident `g`-side to be Proposition 3's
distinguished `R` direction. The frozen all-N package does not explicitly
make that identification. I therefore report both the unconditional union and
the conditional `R` subcatalog:

| window | only `mn>W` | any labelled direction | `R` only, conditional |
|---|---:|---:|---:|
| `N=4,W=2` control | 32 | 25 | 13 |
| `N=5,W=2` | 83 | **67** | **35** |
| `N=6,W=3` | 278 | **181** | **85** |
| `N=6,W=2` | 284 | **238** | **126** |

The any-direction breakdowns by `(m,n)` are

```text
N4/W2: (2,2):3, (3,1):3, (4,1):19;
N5/W2: (2,2):3, (3,1):3, (4,1):19, (5,1):42;
N6/W3: (2,3):3, (4,1):13, (5,1):36, (6,1):129;
N6/W2: (2,2):3, (3,1):3, (3,2):6, (4,1):19, (5,1):42, (6,1):165.
```

All counts are unmarked row types: repeated equal `W`-parts do not multiply a
row. In the N=4 replay the fixed `R` convention is available, and the
determinant/endpoint analysis reduces its 13 types to legal first-fork Figs.
10, 11, 13, 14.

```text
OPEN[DO-GSIDE-R]
bounded quantity: one yes/no identification, in the N=5,6 successor scope,
                  of the physical g-side with Proposition 3's R branch.
```

### 4.4 Why no further row count is licensed

DR explicitly warns that a partition part records a **contact, not a vertex**:
it may end, continue to a fork, or reach the dicritical, and these alternatives
are resolved only after determinant transfer, coprimality, and `sum Deg=N`
(`DR:328–340`). A concrete control is the row `11|2|2`: repeated left
determinants kill it only if both contacts end; DR instead forces at least one
to continue and holds the row for the degree-three census (`DR:366–381`).
Therefore a screen that kills every repeated `1` before assigning endpoint
classes is false.

At `N=4`, the subsequent pruning repeatedly uses consequences of the value
four: a forced endpoint has total degree `4`, a parallel packet makes a Lemma-7
lower bound exceed `4`, or Corollary 4 removes a Deg-2 fork
(`DR:364–482`). At `N=5,6` those conclusions change. In particular, BR forbids
a general-`N` Corollary 4 (`BR:269–280`). The repaired attachment says the
dicritical is incident to Lemma 6's constant block; it does not turn Corollary
4 into an all-degree fork theorem (`BR:60–86`).

Thus there are four honest stages:

```text
raw local rows:                         86 / 287;
direction-agnostic incidence rows:      67 / 181 or 238;
conditional R-oriented row types:       35 / 85 or 126;
fully determinant-pruned global rows:   OPEN / OPEN.
```

Neither incidence catalog is a realised survivor count. A repeated-unit
screen giving `25`, `44`, or `75` silently assumes terminal endpoints and
fails the `11|2|2` control.

## 5. Assembly and Lemmas 10–15

### 5.1 The N=4 control through the same pipeline

The `(B3)` affine entry gives `a=W=2`, one dicritical `(s,mu)=(1,2)`, hence the
DO entry `(m,n)(g~)=(1,2)` and the maximal constant Deg-2 block. This is the
`(mu,corr)=(2,1)` branch (`BR:202–210`). No `(H-∞)` equality is needed.

Local determinant pruning gives:

```text
Fig. 10 = 21|21|3,       Fig. 11 = 3|21|21,
Fig. 13 = 4|211|31,      Fig. 14 = 31|211|4,
Fig. 15 = 31|31|22,      Fig. 16 = 22|31|31.
```

These are exactly `DR:383–389,446–473`. The repaired Corollary-5 assembly is
(`DR:484–529`):

| global graph | assembly |
|---|---|
| Fig. 20 | first fork local Fig. 13 |
| Fig. 21 | first fork local Fig. 14 |
| Fig. 22 | local Fig. 11, then the `3+1` join of local Fig. 15 |
| Fig. 23 | local Fig. 11, then the `3+1` join of local Fig. 16 |
| Fig. 24 | local Fig. 10; the next degree-three fork has local Fig. 11 |
| Fig. 25 | local Fig. 10; the next degree-three fork has local Fig. 10 |

The final eliminations are:

```text
Figs. 24–25: Lemma 10, (7.3) forces y=3 but (7.2) gives y>4.
Figs. 22–23: Lemma 11, (7.6) is odd -1 = an even integer.
Figs. 20–21: Lemmas 12–15, (7.10) says -1=-B-alpha*C<=-4.
```

This reproduces the six graphs and the kill set, rather than replacing it by a
one-line Corollary 4 argument.

### 5.2 Hypotheses and degree status of Lemmas 10–15

Every entry below retains the replay's common ambient scope: a four-sheeted
Keller map with one dicritical, `(m,n)(g~)=(1,2)`, resolved compactifications,
conditions A–E, the Proposition-3 package, and the stricter Russian meaning of
“linear” (every subgraph vertex has ambient valence at most two;
`DR:105–112,145–155`). Each row adds its graph and root facts.

| lemma | hypotheses actually consumed in the replay | conclusion | degree status |
|---|---|---|---|
| 10 | Exact global Figs. 24/25; their root/nonroot placements; target root strictly outside `delta(ab)`; transferred coefficients `18,4,6`; whole-tree determinant identity | root-unit gives `d_1=d_3=1`; Lemma 4 gives `delta:=det delta(ab)>0`; then `y>4` while (7.3) forces `y=3` | **Not degree-free as a graph kill.** Edge formula, root-unit lemma, and positivity are degree-free; the coefficients and graph determinant are N=4 outputs. |
| 11 | Exact Figs. 22/23; degree-four target determinants `(3,2,1)`; degree-three terminal determinants; `det L=-1`; graph calculation `det L~_infty=-2` | (7.6): odd `-1` equals even | **Not degree-free as a graph kill.** Transfer algebra is degree-free; `-2` and parity coefficients are graph-specific. |
| 12 | The replay does not isolate the printed statement. Its proof input is that the generic point of the original source line at infinity maps to target infinity in polynomial coordinates, persisting under blowups; separately, `K~=F^*K+B` has boundary-supported Jacobian divisor | certified common payload for Lemmas 12–14: root lies in `L~_infty`; coefficient at `g~` is `n(g~)-1` | These root/canonical identities are degree-free under the Keller compactification hypotheses. The value `1` uses `n(g~)=2`; at `mu=3` it is `2`. No broader conclusion is attributed to Lemma 12. |
| 13 | Maximal Deg-2 block `Delta`; first nodal vertex on `[v~,g~]`; transfer value `det(v_1 g)=2`; root placement; strict Russian linearity | `Delta ∩ [v~,g~]` is linear in the published ambient-valence sense | **Conditional degree-free schema once Deg `Delta=2`, `n(g)=2`, and the graph/root hypotheses hold; not an arbitrary-N/`mu` kill.** In the `d>1` branch unity comes from root-unit Lemma 3, not positivity Lemma 4. |
| 14 | Lemma 13 plus the supposition that the root lies in `Delta`; canonical decomposition; exact alternatives `det L~_infty=-2` for Figs. 22/23 and `-1` for Figs. 20/21 | root is outside `Delta` | **Conditional ambient-degree-free implication** once the Deg-2/`n(g)=2` Lemma-13 hypotheses and `det L~_infty>=-2` hold. That determinant bound is graph-specific; no arbitrary-`mu` version is promoted. |
| 15 | Exact Figs. 20/21; Proposition-2 calculation `det L~_infty=-1`; Lemmas 13–14; `B>=1`, omitted branch product `C>=3`, `alpha>=1` | (7.10), `-1<=-4`, contradiction | **Not degree-free as a graph kill.** The floors are degree-free; `det=-1`, `C>=3`, and the closed graph are specific. |

Locations are `DR:533–590` (Lemma 10), `DR:592–634` (Lemma 11), and
`DR:636–705` (Lemmas 12–15). Every binding repair is retained:

* Proposition 4's RH equivalence (`DR:284–300`);
* Lemma 7 only as `sum Deg>=q`, never equality (`DR:302–319`);
* explicit Corollary-5 tree assembly (`DR:484–529`);
* `det(delta(ab))>0` before cancellation (`DR:545–548`);
* the three companions: Fig. 25 (`DR:582–590`), Fig. 23
  (`DR:631–634`), and Fig. 21 (`DR:684–687`);
* Lemma 13's corrected citation to Lemma 3 (`DR:657–660`).

### 5.3 What survives at N=5 and N=6

No lemma in the preceding table fires on an `N=5` or `N=6` seed merely from
its row. There is no identified analogue graph on which to substitute the
numeric calculation. The review labels the successor bounded and well-posed
(`BR:269–274`), but it does not supply a whole-tree fork theorem. The
prospective extension classes are:

```text
G_5(P)      = extensions of 67 any-direction row types
              (35 in the conditional R subcatalog), P in {5.1,5.2,5.3};
G_6,3(P)    = extensions of 181 types (conditional R: 85),
              P in {6.1,6.2};
G_6,4(P)    = extensions of 238 types (conditional R: 126),
              P in {6.3,...,6.9}.
```

“Extension” here means assigning each contact an endpoint class, gluing equal
tube degrees without a cycle, adding the companion components required by
`sum Deg=N` at every target vertex, locating the source root, and then imposing
Lemma-5 transfer, determinant coprimality, repaired Lemma 7, and the edge and
canonical formulas. This definition states the remaining task; it does not
pretend that the extensions have been enumerated. BI-8 gives per-spine fork
caps `3`, `3`, and `4`; these do not bound total forks in the whole tree.

The missing derivation can be typed precisely. Across the raw catalogs there
are `549` contact-port occurrences at `N=5` and `2127` at `N=6`. Grouping by
printed tube degree gives:

```text
N=5: q=1..5 port counts   228,156,81,54,30;
N=6: q=1..6 port counts   810,612,336,195,99,75.
```

Including diagonal reuse (needed already by N=4 Fig. 25), the equal-degree
projection contains `sum_q c_q^2 = 86,697` and `1,196,991` ordered pairs.
These are reproducible diagnostics only. Endpoint compatibility also depends
on downstream branch state and root placement, so they are not bounds on
transition cases or global graphs.

If `F` bounds total fork vertices, a coarse bound on compressed labelled
endpoint assignments (including a root-location factor) is

```text
E(N,F)=sum_(k=1)^F Census(N)^k (k(N+2)+2)^(k(N+2)) (k(N+2)+1).
```

```text
OPEN[DO-GLOBAL-FORK-CARDINALITY]
bounded quantity: three integers F_(5,3),F_(6,3),F_(6,4) bounding total fork
                  vertices, compatible with BI-8's per-spine caps 3,3,4.

OPEN[DO-ENDPOINT-N5]
bounded quantity: one endpoint/continuation/root-state theorem on 86 row
                  types and 549 raw ports; at most E(5,F_(5,3)) compressed
                  assignments once F_(5,3) is supplied.

OPEN[DO-ENDPOINT-N6]
bounded quantity: one endpoint/continuation/root-state theorem on 287 row
                  types and 2,127 raw ports; at most E(6,F_(6,3)) or
                  E(6,F_(6,4)) assignments once those bounds are supplied.

OPEN[DO-DET-CANONICAL-N5-N6]
bounded quantity: one exact integer determinant/canonical audit per graph
                  in the finite list, conditional on the preceding two
                  derivations producing that list.

OPEN[DO-MU3-CANONICAL-BLOCK]
bounded quantity: one rederivation of Lemmas 13–14 with incident Deg 3 and
                  canonical coefficient mu-1=2, for profiles 6.1–6.2.
```

No numerical `F` is inferred: multiplying BI-8's per-spine cap by a local port
count would silently turn “on a spine” into “in the tree.” Determinant values
are likewise not capped by analogy; the audit is binary only after a graph is
fixed.

```text
OPEN[BI-TAIL-AT-INFINITY]
bounded quantity: one yes/no assertion whether an F-constant component of
                  L~_infty maps to p, applied to the sole dicritical.
```

It gates BI-3/BI-5 saturation only; it does not weaken BI-1, BI-5-Deg, the
incidence catalogs, or BI-8 (`BR:121–141,275–280`). BI-ATTACH itself is
repaired and is not reopened.

## 6. Outcome and growth

The requested either/or outcome is the second branch, with an important
qualification: the frozen data determine exact **seed catalogs**, not exact
completed global graphs.

| degree/profile | raw rows | incidence row types: any direction / conditional `R` | lemma firing now | boundary datum still needed |
|---|---:|---:|---|---|
| N=5, each of 3 cells | 86 | **67 / 35** | none | `GSIDE-R`; `GLOBAL-FORK-CARDINALITY`; `ENDPOINT-N5`; `DET-CANONICAL` |
| N=6, cells 6.1–6.2 | 287 | **181 / 85** | none | `GSIDE-R`; `GLOBAL-FORK`; `ENDPOINT-N6`; `DET-CANONICAL`; `MU3-BLOCK` |
| N=6, cells 6.3–6.9 | 287 | **238 / 126** | none | `GSIDE-R`; `GLOBAL-FORK-CARDINALITY`; `ENDPOINT-N6`; `DET-CANONICAL` |
| N=4 control | 35 | 25 / 13; then 4 legal first-fork rows | Lemma 10 on 24/25; Lemma 11 on 22/23; Lemmas 12–15 on 20/21 | none for the `(mu,corr)=(2,1)` kill |

Accordingly:

```text
FIRST EMPTY WINDOW IN N FOR (B3):  NOT ESTABLISHED.
N=5: no Lemma-10–15 analogue has a graph on which it legally fires.
N=6: same; the a=3 branch additionally changes the canonical coefficient.
```

The growth statement must retain all stages:

```text
N=5: 86 raw rows; 67 incidence candidates (conditional R: 35);
     final determinant-pruned survivor count OPEN.
N=6: 287 raw rows; 181 candidates at W=3 and 238 at W=2
     (conditional R: 85 and 126); final survivor count OPEN.
N=7: 717 raw rows; the stated profile rules give 32 charged cells, not 33.
```

Across profiles, raw workloads are `258` and `2,583`; incidence candidates are
`3*67=201` and `2*181+7*238=2,028` (conditional `R`: `105` and `1,052`).

If the coordinator elects to retain `33` as an external convention pending
repair, the advertised work face is `33 x 717 = 23,661` profile-row incidences
before any assembly. Under the rules actually reproduced here it is
`32 x 717 = 22,944`. Both numbers are bookkeeping products, not independent
graph counts; profiles with the same `W` reuse one boundary row catalog.

## 7. Sol's `Gamma` and FALLACY-v2 audit

Sol's

```text
Gamma: y^2=x^3(x-1)^2,   (x,y)=(t^2,t^3(t^2-1))
```

is only `REPRESENTATIVE`. The charged computation gives one cusp, one
transverse node, genus zero, and the N=4 affine fibre ledgers (`BR:212–231`).
No boundary graph is attached to `Gamma` in this report: the map-level raw
census, incidence sieve, and B3-CAGE are not applied to this standalone curve.
No step here kills it. The N=4 DO contradictions use Keller-only
resolution/étale/canonical hypotheses—especially the boundary-supported
Jacobian divisor—so they are not statements that this curve cannot exist. HF
records the analogous **profile-level** representative survivor; it is not an
independent boundary test of this particular `Gamma` (`HF:353–375`).

FALLACY-v2 checks:

* **Flag/place/series.** An affine branch, its point on `l'`, an escaping fibre
  part, a boundary contact, and a global source branch are never identified.
  The `M_{2,2}` two-way fibre split is retained.
* **Carrier/attainment.** Raw rows and first-fork seeds are candidate encodings,
  not realised maps. BI-8 is never asserted tight outside the N=4 control.
* **Floor/attainment.** Lemma 7 remains `>=q`; no companion degree or fork count
  is promoted to equality.
* **Pole/interior.** BI-3 and mark saturation are not used without `(H-∞)`.
  The unconditional degree split is kept separate.
* **Variable map.** DO's `m,n,Deg` are distinct from campaign `s,mu,a,W`.
  The incident block has Deg `s mu`; the repaired review does not identify it
  with the excluded transpose fork.
* **Per-ray/exit-set.** BI-4 same-branch load is `<=K` at a multibranch point;
  only a cusp gives equality. No exit price is asserted.
* **Prime labels.** No prime notation is used for differentiation.
* **No analogy fill.** Corollary 4 remains N=4-only; Lemmas 10–15 are separated
  into degree-free primitives and graph-specific conclusions.

## 8. Reproducibility core

The following pure-Python generator produced `35,86,287,717` and the `23`
control. SymPy 1.14.0 was used only for the exact profile-series expansions;
all coefficients are integers.

```python
from itertools import product

def parts(t, hi=None):
    if t == 0:
        yield ()
        return
    hi = min(t, t if hi is None else hi)
    for q in range(hi, 0, -1):
        for tail in parts(t-q, q):
            yield (q,) + tail

def census(N):
    for m in range(2, N+1):
        P = tuple(parts(m))
        for n in range(1, N//m + 1):
            for L, R, D in product(P, repeat=3):
                if len(L)+len(R)+len(D) == m+2:
                    yield (m, n, L, R, D)

def r_seed_rows(N, W):
    for m, n, L, R, D in census(N):
        if m*n > W and W in tuple(n*e for e in R):
            yield (m, n, L, R, D)

def any_direction_seed_rows(N, W):
    for m, n, L, R, D in census(N):
        contacts = L + R + D
        if m*n > W and W in tuple(n*e for e in contacts):
            yield (m, n, L, R, D)

assert [sum(1 for _ in census(N)) for N in (4,5,6,7)] == [35,86,287,717]
assert sum(r[:2] == (4,1) for r in census(4)) == 23
assert [sum(1 for _ in r_seed_rows(N,W))
        for N,W in ((4,2),(5,2),(6,3),(6,2))] == [13,35,85,126]
assert [sum(1 for _ in any_direction_seed_rows(N,W))
        for N,W in ((4,2),(5,2),(6,3),(6,2))] == [25,67,181,238]
```

The charged-profile coefficient was computed as

```python
import sympy as sp
x = sp.symbols('x')

def trunc_prod(weights, d):
    out = sp.Integer(1)
    for k in weights:
        out = sp.series(out/(1-x**k), x, 0, d+1).removeO().expand()
    return out

def charged_count(N, a):
    W, d = N-a, a-1
    C = trunc_prod(range(1,d+1), d)
    types = [(r,K) for r in range(2,N+1) for K in range(1,d+1)
             if N-r*W-K >= 0]
    M = trunc_prod([K for r,K in types], d)
    return int(sp.expand((C-1)*M).coeff(x,d))

assert charged_count(5,3) == 3
assert charged_count(6,3) + charged_count(6,4) == 9
assert charged_count(7,4) + charged_count(7,5) == 32
```

## 9. Typed verdict

```text
LANE       B3-CENSUS-DEG5-DEG6
SCOPE      Keller, noninvertible, H2, (B3); no case A/A2/B2/Z(G)=1.

MEASURED   Rows(2..7)=3,6,23,51,192,430.
           Census(4..7)=35,86,287,717; (4,1) subcount=23.
           Profiles N5/N6=3/9; missed N6 cell C1+C1+M21,
           reviewed one-U2 cap on 2p_a = 3.
           Incidence rows N5=67; N6=181 (W3),238 (W2).
           Conditional R subcatalogs: 35; 85,126.

CONTROL    N4 raw 35 -> six global graphs -> EMPTY for (mu,corr)=(2,1):
           L10 kills 24/25, L11 kills 22/23, L12-15 kill 20/21.
           H-infinity not used; all replay repairs binding.

RESULT     No EMPTY N=5 or N=6 window is certified.
           No L10-15 analogue legally fires before general-N assembly.

OPEN       DO-GSIDE-R: one binary N5/N6 direction identification.
           DO-GLOBAL-FORK-CARDINALITY: three total-fork integer bounds.
           DO-ENDPOINT-N5/N6: state theorems over 86/287 rows and
           549/2,127 ports, conditionally bounded by E(N,F).
           DO-DET-CANONICAL-N5-N6: one binary audit per fixed emitted graph.
           DO-MU3-CANONICAL-BLOCK: one coefficient-2 rederivation.
           BI-TAIL-AT-INFINITY: one yes/no per unique dicritical; saturation only.
           PROFILE-N7-33: one typing/equivalence reconciliation; count here 32.

GROWTH     N7 has 717 raw rows. Stipulated 33 profiles would mean 23,661
           profile-row incidences; reproduced 32 means 22,944.

GUARDRAIL  Gamma retained as REPRESENTATIVE; no non-Keller step kills it.
           No general-N Corollary 4, no unpromoted v0 partition, no attainment.
```

<!-- BODY-END -->
