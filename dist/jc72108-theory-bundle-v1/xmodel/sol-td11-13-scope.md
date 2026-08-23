# td-11 / td-13 refile + tower-port scope

## Executive summary

1. The refile starts from exactly 3 td-11 and 6 td-13 L6-surviving entries; the old 12/129 cell counts are VOID and are neither lower nor upper bounds.
2. `book_offaxis.py`, P0/`px2`, `px5`, and `td7_census_e5.py` supply useful kernels, but a sound higher-rung census needs a new shared-budget, mixed/nested-merge compiler with current-state multiplicities and vertex-level E5F.
3. TOWER-UNIFORM's conditional algebraic kernels L-A, M=1 absorption, tower-N1, N4, and the base E5F law port; WIN, TERM, N2/N3's numerical cap, AM's `{A,C}` menu, and the A/B/C exhaustion do not port as proved.
4. LOUD ARITHMETIC RESULT: td-11 entry 11-A has a zero-price `5/8` intruder for every N1-legal `nu_X >= 5`, and td-13's all-off-axis entry 13-2b has the exact nonempty menu window `3/10 < 2/5 < 5/2`; these are the first hard objects.
5. CONJECTURE (execution estimate): td-11 needs 6--8 build/replay/review rounds and td-13 a further 9--13; the largest risk is failure to prove a finite, completeness-preserving normal form for priced inter-merge states, not raw runtime.

## 1. REFILE DESIGN

### 1.1 What the census starts from, and how large it is

The governing correction is BOOK-OFFAXIS §10 P5: the stage-R alphabet was
wrong in both directions, so `12` and `129` must disappear from every gate,
fixture, progress denominator, and tower claim.  The exact entry layer is
still usable (`cases/book_offaxis.py:census`, consuming
`book_enum.entries/tdu_rows`):

| rung | L6 entries | labelled hierarchy packets | stale no-chain decorations | corrected direct-inner diagnostic | completed Q+E5/E5F refile |
|---|---:|---:|---:|---:|---|
| td-11 | 3 | 6 (`1+1+4`) | 117, 25 mixed | 159, 34 containing a mixed node | **UNKNOWN** |
| td-13 | 6 | 34 (`1+1+1+1+4+26`) | 686, 86 mixed | 1310, 128 containing a mixed node | **UNKNOWN** |

The hierarchy counts are the exact labelled rooted-tree counts for two,
three, and four leaves: 1, 4, and 26.  The corrected diagnostic repairs the
known `expand` defect (`BOOK-OFFAXIS-REVIEW` finding 2): an inner merge keeps
its emitted `M_child`, while the next edge independently chooses
`mu_e | M_child`; the current code sets `mu_e = M_child`.  Entrywise the
restricted counts are

```
td-11:  [1,2] 6/0, [1,3] 8/0, [1,2,2] 145/34;
td-13:  [1,5] 10/0, [2,3] 14/3, [2,1] 6/0,
        [1,3] 8/0, [1,2,1] 68/5, [1,1,1,2] 1204/120.
```

Here `total/mixed` means decorated skeletons / skeletons containing a mixed
node under the old direct-entry/subadditivity model.  **CONJECTURE (sizing
diagnostic only):** 159 and 1310 are useful workload baselines for engineering,
but are neither mathematical lower nor upper bounds on the final cells.
Post-jump `M` states can add rows; shape, E5F, T1, and budget gates can remove
or identify them.

The breadth increase is already visible before the real budgets are opened.
At budget 5 the current exact P0 closure has 69 states from `(3/2,2)`, but the
td-11/13 `b=3` seeds have 241--360 states, depending on `w`; P5 already warns
that `b=3,5` are worse.  The actual maximum shared budgets are 9 and 11, since
`sum lambda <= td-1-psi` and `psi >= 1`.  No present engine certifies those
multistep closures.

**CONJECTURE (capacity estimate, not a completeness bound):** plan for
`10^3--10^4` canonical merge/arrival records and `10^4--10^5` completion
routes at td-11; plan for `10^4--10^5` records and `10^5--10^6+` routes at
td-13.  The engine should spill/checkpoint at least one decade above these
ranges.  Promotion must depend on a symbolic bound and parity gates, never on
these estimates.

### 1.2 The object that must be re-enumerated

The refile is a DAG dynamic program, not a replay of the old grid:

1. **Entry census.**  Freeze `(td,m,alpha,beta)` and, for every pole,
   `(Lambda,a,b,nu)`, `M=b`, `w0`, `D_P=a*alpha`, and the full pole-pattern
   degree `pdeg_P=b*alpha`.  Apply L6/BOOK-N1 here.  These are exact and small.

2. **Priced chain graphs.**  Starting at each `(w0,M,pdeg_P)`, enumerate P0
   transitions with a state rich enough for later consumers:

   ```
   (w, M, lambda, pdeg multiplier, nu, rho, kbar,
    last cell, direct-arrival vertices, zero-cost family tag).
   ```

   Keep Pareto fronts, not just minimum `lambda`: E5F and H8 can distinguish
   two paths to the same `(w,M)`.  Represent neutral padding and zero-cost
   resonances symbolically.  Prove the budget-dependent `k`, multiplicity-
   partition, and `l_ex` bounds; do not inherit `px2`'s td-7 loop caps.

3. **Merge cells, recursively.**  For every hierarchy node enumerate all
   zero-slot placements, current-state arrivals `mu_e | M_U`, emitted
   `M_G | sum mu_e` where applicable, case-I/II/III/IV handshakes, orbit-
   multiplicity partitions, `epsilon`, `(dp,dq,nu_G)`, `(kbar_G,X_G)`, and
   the emitted trunk frame.  Feed an inner merge's emitted frame into a new
   priced inter-merge chain graph before attaching it to its parent.  This
   is where multi-orbit, all-`mu>=2` mixed, simultaneous, and nested merges
   enter.

4. **Local Prop. 8.1(iv) filter.**  For each fixed cell solve the exact linear
   ODE with the cell's actual multi-factor `p`, rather than importing td-7's
   one-nonzero-orbit law `dp | dq`.  Record a proof certificate or an explicit
   admissible solution.  This is the branch-7' caution in
   `xmodel/sol-probability.md`: a fixed equation is promising, but the normal
   forms are genuinely broader.

5. **Q+E5 arrivals, then E5F.**  The H5a issue is resolved (`AUDIT.md`, H5a
   resolution), so use the Q/jump convention everywhere.  On every leaf or
   inner arrival retain the full vertex data and require

   ```
   n = nu_U*kbar_G - nu_G*kbar_U >= 1.                 (E5F)
   ```

   Test direct vertices, entry vertices, clean pads, and legal reroutes.  The
   td-7 shortcut
   `kbar_E5=(mu0*nu_G*w_U-2)/(mu0-1)` is valid only when another handshake
   has already proved `X=kbar-2`; in a mixed/nested cell `X` must be recomputed
   from all incoming handshakes.  A rejected direct vertex does not reject a
   state or cell until every budget-legal pad/reroute has been checked.

6. **Shared lambda budget and completion routes.**  Add chain, merge-NE,
   free-zero, inter-merge, and trunk prices over all pairwise-distinct
   searrow vertices in the whole configuration.  Finish with P1's exact
   `psi=ceil(1/(1-w_t))-1` and terminal laws.  Deduplicate only after retaining
   equality/slack, multiplicity partitions, charged predecessor strata, and
   E5F witness vertices; those decorations are part of the tower perimeter.

Required output per canonical row is therefore

```
entry + hierarchy + node cells + chain paths + arrivals/E5 offsets
+ local-ODE verdict + lambda ledger + terminal + raw/dedup route key.
```

### 1.3 What can be reused

| component | reuse | required change |
|---|---|---|
| `book_offaxis.py` entry layer | `entries`, `tdu_rows`, L6, `w0`, pole packets | none beyond new parity fixtures |
| `book_offaxis.py` hierarchy/merge layer | rooted hierarchy generator, R2 handshake/shape-solver architecture, P0/P1 formulas | fix inner `mu`; carry full child frame; add priced inter-merge chains; remove `PCAP_BUDGET=5` and verdict-by-cap behavior |
| `px2` / `chain_steps_p` | P0 Diophantine identities, exact `Fraction`, lambda minimization over NE partitions | parameterize budget; derive `k/l_ex` bounds; enumerate all multiplicity partitions; expose degree/frame transitions |
| `px5` | Dijkstra pattern, arrival cellmap, terminal `psi`, shared-feasibility and route-dedup patterns | remove td-7 `ENTRY`, class A/B/C, one-merge, and budget-5 assumptions; compose an arbitrary hierarchy |
| `td7_census_e5.py` | cap-free inversion style, Q+E5-vs-cell double pin, positive/negative/parity gates | its formulas assume one `mu=1,w=2` edge and one-orbit class C; add general merge frames and the promoted vertex-level `n>=1` filter |
| `tower_rollout_arith.py` / `tower_check.py` | exact degree transport, gap calculation, mutation gates, witness-ledger format | consume the new refile; remove hardcoded degrees `2/4`, seed `(3/2,2)`, `{A,C}`, budget 5, and cap `k|2` |

The td-13 one-step audit already proves why simple parameterization is
mandatory: at budget 11 the `b=5,w=8/5` seed has six legal `k=7` rows omitted
by `px2`'s current `k<=6` loop.  Their gaps add no new maximum, but their cells
and descendants belong to the census.

### 1.4 Genuinely new machinery

The new core is one **canonical priced hierarchy compiler** with four proof
obligations:

- a cap-free multistep state bound at budgets 9/11;
- correct current-state arrival divisibility across inner edges;
- generalized multi-orbit/mixed Prop. 8.1(iv) certificates;
- Q+E5/E5F transport on every nested edge, including pads and reroutes.

No combination of the present `stage_rp_census`, td-7 class-C inversion, or
old merge skeleton proves those four items.  Until they are discharged, a
finite run may report candidates but may not report an empty panel.

## 2. TOWER PORT

### 2.1 Lemma classification: td-agnostic as proved versus td-7 data

The named theorem in TOWER-UNIFORM is scoped to the 17-cell td-7 filed book.
The table separates already-proved conditional kernels from the hypotheses
that made them panel-constant.  “tower-N1” below is not BOOK-N1/L6.

| item | td-agnostic kernel already proved | td-7-specific part that does not port |
|---|---|---|
| **L-A** | On any merge-free `M=1` branch, `l=1`; charged directions are shape-impossible and `M=1` propagates, budget-independently. | “Frozen at `(w,M)=(2,1)`,” absence of clean state-changing resonances, degree-2 anchor, and the `n=1` X-gap.  L-A proves uncharged, not constant `w`. |
| **AM** | `M=1` is absorbing on a merge-free chain. | The first charged menu `{(21,15),(20,16)}`, `lambda=2`, `i=2`, and pruning of other steps use seed `(3/2,2)` and a single class-C target.  An `M=1` branch may legally enter a higher mixed/nested merge. |
| **WIN** | Degree-growth and ratio estimates are reusable techniques. | The lemma uses pole top `5/2`, degrees `2/4`, budget 5, the 69-state closure, and competing maximum `2/5`.  It is not a td-uniform theorem. |
| **TERM** | The strategy “bound every rootward gap below X” is reusable. | The proof uses the 16 td-7 cells and `deg p_{f,G}>=42`; an inner merge plus later sibling is not a td-7 terminal. |
| **tower-N1** | A state-preserving zero-cost insertion has `n=1`, clean form `(l*nu,nu+1)`, and the gcd identity. | It does not classify state-changing clean resonances or eligible states. |
| **tower-N2** | Only `gcd(l*nu,nu+1)=gcd(l,nu+1)` is generic. | Odd `nu`/odd `P_pre` uses the td-7 pre-charge state `M=2`.  States `M=3,5` require new congruence classes. |
| **tower-N3** | Simultaneously alive vertices impose the intersection of their exponent caps. | `k|2` uses pole exponent 4, first-charge exponent `2P_pre`, and N2 oddness.  The new cap is entry/state dependent, typically `k | gcd(pdeg_P,i_first*P_pre)`. |
| **tower-N4** | A neutral inserted above full degree `Dprev` has gap `(nu+1)/(Dprev*nu)`, independent of `l`; if `Dprev>=4`, it is `<=3/8`. | Its comparison with an X-gap `>1/2`, and shrinkage of the A/C gaps, are td-7 numerical inputs. |
| **E5F** | Under resolved Q+E5, `n=nu_U*kbar_G-nu_G*kbar_U>=1`; the intermediate `rho` identity is general. | `X=kbar-2`, minimal-pad `n=-2`, and the filed `n=-1` family are td-7 frame corollaries. |
| **A/B/C exhaustion** | The displayed divisibility calculations are identities once the td-7 packet is assumed. | The packet is `(k0,l0)=(2,3)`, `alpha1=3/2`, cap `k|2`, X-gap `(nu+1)/(2nu)`, empty top `5/2` window, and prefix menu `{1,3/2,2}`.  Type `(2,5)`, type `(3,4)`, resonant X, or another cap needs a new exhaustion. |

### 2.2 Why entry uniqueness was load-bearing

The unique td-7 entry forced, for every cell and route:

```
type (2,3), pole top 5/2, pole full degrees 2/4,
chain seeds (2,1) and (3/2,2), first charge {A,C}, cap k|2.
```

Only arrival state, cell frame, and terminal varied.  That is exactly why
the clash apparatus became panel-constant.  At td-11/13, a refile can at
best make it **entry-constant**, and nested hierarchies can change even that
by inserting an inner merge before the candidate clash.

The td-11 three-pole entry and td-13 three-/four-pole entries contain an
exact td-7 local pair `(1@2;pdeg2) + (2@3/2;pdeg4)`.  **CONJECTURE
(local-to-global inheritance):** if that pair forms a genuine two-child
submerge and every attached sibling/inner vertex has gap at most the selected
X, the td-7 local obstruction survives later attachment.  No current lemma
proves this; TERM covers a rootward terminal continuation, not another merge.

Thus the answer to “does the level-1 clash survive per entry?” is **NO AS
PROVED**.  Section 3 shows which entries nevertheless have the same local
gap ordering and which already fail it.

### 2.3 Exact port obligations

1. **Entry ladder packet:** prove the common pole collapse, `(k0,l0)`,
   `alpha1`, pole top, and every full pole exponent for each of the nine
   entries; do not infer them from `td` or from type `(2,3)` alone.

2. **Route-level clash carrier:** for every hierarchy/orientation identify a
   real X branch and opponent.  The all-off-axis entry 13-2b has no L-A
   carrier.

3. **Freeze plus resonance:** apply L-A to each `M=1` segment, then classify
   all state-changing clean resonances and the actual pole-adjacent X gap.
   The seeds `w=3,4,6` are not td-7-frozen.

4. **H8 synchronization:** prove every incoming degree quotient and stack
   product is integral and nonempty.  Record nonintegrality as spine-death;
   `P=1` means the proposed X does not exist.  Nested merges require a ledger
   at every node, not the single td-7 identity `P=i_G/2`.

5. **First-charge menu and cap:** rerun the cap-free priced menu for every
   seed/state, prove the simple reduced factors, and derive the actual joint
   cap and residue classes.  Empty gap windows are insufficient without this
   cap.

6. **Global window theorem:** bound every budget-admissible pole descendant,
   state-changing resonance, charged predecessor stratum, neutral insertion,
   sibling, inner merge, trunk, and terminal.  Include multiplicity
   partitions and self-returns, as TOWER-UNIFORM's perimeter requires.

7. **Prefix exhaustion:** recompute the non-killing prefix grid from the new
   `alpha1`, cap, and window, and prove every prefix length.  In particular,
   build a `k|3` analogue for type `(3,4)` and separate the resonant-X cases.

8. **Multi-pole composition:** prove restriction of a global ladder to a
   forbidden two-branch subtree, or enumerate all global first-death orders.
   A routewise “choose maximum X” normalization must handle ties and prove
   compatibility with H8 and the fixed global ladder.

9. **Insertion closure:** retain tower-N1/N4, but regenerate eligible-state
   tables and N2/N3 congruence/cap data at every state.  Prove closure under
   arbitrary finite neutral insertion, not a depth sample.

10. **E5F closure:** apply the base law at every direct/inner/pad arrival and
    prove that every E5-refuted vertex either has a legal in-budget reroute or
    removes the route.  Never import td-7's specialized offset formula into
    a different handshake.

11. **Nested TERM:** replace TERM by a bound that covers arbitrary rootward
    merge continuation and attached siblings.

12. **Perimeter certificate:** each surviving refile row must carry entry,
    hierarchy, all arrivals/`M_U` classes, E5 offsets, H8 products, cap,
    maximum competing gap, prefix deltas, charged strata, terminal gaps, and
    raw/dedup census parity.  This is the higher-rung version of
    TOWER-UNIFORM §3's frozen witness table.

## 3. CLASH-WINDOW ARITHMETIC NOW

### 3.1 Common formulas and entry packets

For type `(alpha,beta)`, both pole collapses have

```
g_top = (alpha+beta)/alpha = 1 + beta/alpha.
```

Write `[M@w;p]` for entry `M`, entry weight `w`, and full pole-pattern
degree `p=b*alpha`.  A child `(dp,dq)` entered with multiplicity `l` has

```
pdeg_child = p*dp/l,          gap = l*dq/(p*dp).
```

On an `M=1` clean child `(nu,n*nu+1)`, this is
`(n*nu+1)/(alpha*nu)`.  After local BOOK-N1/L6:

- `w=2`: no resonance; neutral `nu` is odd.  X lies in the exact discrete
  family `(nu+1)/(2nu) in (1/2,2/3]`, or for type `(3,4)`,
  `(nu+1)/(3nu) in (1/3,4/9]`.
- `w=3`: neutral `3` does not divide `nu`; the maximum is `3/4` at `nu=2`.
  The legal pole-adjacent resonance `(n,nu)=(2,2)` has gap `5/4` and sends
  `w:3 -> 2`.
- `w=4`: neutral `nu` is odd, giving `(1/2,2/3]`; the legal resonance
  `(2,3)` has gap `7/6` and sends `4 -> 2`.
- `w=6`: neutral `gcd(nu,6)=1`, giving `(1/2,3/5]`.  The apparent `(2,2)`
  resonance fails N1; the legal `(2,5)` resonance has gap `11/10` and sends
  `6 -> 2`.

The exact surviving entries are:

| ID | type and entry | `[M@w;p]` packet | pole top | M=1 status |
|---|---|---|---:|---|
| 11-A | `(2,3): L3a1b1n2 + L8a2b2n3` | `[1@2;2] + [2@3;4]` | `5/2` | strict `w=2` freeze |
| 11-B | `(2,5): L5a1b1n2 + L6a1b3n5` | `[1@3;2] + [3@4/3;6]` | `7/2` | uncharged, but `3 -> 2` |
| 11-C | `(2,3): L3a1b1n2 + 2 L4a1b2n3` | `[1@2;2] + 2[2@3/2;4]` | `5/2` | strict; two opponents |
| 13-2a | `(2,3): L3a1b1n2 + L10a1b5n3` | `[1@2;2] + [5@8/5;10]` | `5/2` | strict |
| 13-2b | `(2,3): L4a1b2n3 + L9a1b3n2` | `[2@3/2;4] + [3@7/3;6]` | `5/2` | **none; all off-axis** |
| 13-2c | `(2,3): L4a1b2n3 + L9a3b1n2` | `[2@3/2;4] + [1@6;2]` | `5/2` | uncharged; legal `6 -> 2` gap `11/10` |
| 13-2d | `(3,4): L4a1b1n3 + L9a1b3n4` | `[1@2;3] + [3@5/3;9]` | `7/3` | strict, degree-3 X |
| 13-3 | `(2,3): L3a1b1n2 + L4a1b2n3 + L6a1b1n1` | `[1@2;2]+[2@3/2;4]+[1@4;2]` | `5/2` | one strict plus one `4 -> 2` branch |
| 13-4 | `(2,3): 3 L3a1b1n2 + L4a1b2n3` | `3[1@2;2]+[2@3/2;4]` | `5/2` | three strict branches |

All X statements below are conditional on a nonempty H8 synchronization
stack.  Proving that condition is a refile/tower obligation, not entry
arithmetic.

### 3.2 Cap-free first-step menu gaps

The following are exact local-N1-legal one-step results at the gross budgets
9/11.  “Fixed” means dirty/charged finite cells; “pure” is the parametric
pure-(b) family.  E5F is not yet applicable because no merge arrival frame
has been chosen.

| seed `(w,M;p)` | zero-cost clean / neutral | fixed charged gaps | pure maxima | overall maximum |
|---|---|---|---|---:|
| `(3,2;4)` | resonance `5/8`; neutral `<=3/8` | `{7/16,2/5,3/8,5/14,11/32}` | `3/11` | **`5/8`** |
| `(4/3,3;6)` | no resonance; neutral `<=1/5` | `{5/22,3/14,7/34}` | `1/5,2/11` | **`5/22`** |
| `(3/2,2;4)` | no resonance; neutral `<=3/10` | `{2/5,5/14}` | `3/10` | **`2/5`** |
| `(8/5,5;10)` | resonance `3/14`; neutral `<=3/20` | `{15/134,7/62,13/114,3/26,11/94,5/42,9/74,7/54,5/34,1/6,3/14}` | `1/8,1/9,1/9,2/19` | **`3/14`** |
| `(7/3,3;6)` | resonance `3/4`; neutral `<=1/4` | `{13/64,11/52,5/23,9/40,4/17,5/16,2/5}` | `1/5,3/16` | **`3/4`** |
| `(5/3,3;9)` | resonance `1/4`; neutral `<=1/6` | `{3/22,7/48,2/13,1/4}` | `2/15,1/8` | **`1/4`** |

For td-11, `lambda>=k` makes `k<=9`; the exact P0 divisor bound produces
no rows beyond `k=5`.  For td-13, `k<=11`; the derived
`E=C*nu+(l-epsilon) | l*num(w)*T` bound finds six additional `k=7` rows for
`(8/5,5)`, but no new gap value.  This proves the table only for one step.
**CONJECTURE:** no full-route maximum may be inferred until the multistep
budget-9/11 closure, inner merges, trunks, and E5F reroutes are complete.

### 3.3 Entry verdicts

#### td-11

**LOUD RESULT: td-11 IS NOT AN EMPTY-WINDOW PANEL.**

- **11-A is the next hard td-11 object.**  Its off-axis branch has the
  zero-cost clean resonance

  ```
  Delta=3, n=2, nu=2,  w:3 -> 2, M:2 -> 1,
  pdeg=8, dq=5, gap=5/8, lambda=0.
  ```

  For the strict chain-1 branch
  `g_X=(nu_X+1)/(2*nu_X)`.  Exactly

  ```
  5/8 > g_X  <=>  nu_X > 4.
  ```

  N1 makes `nu_X` odd, so the attainable in-window cases are precisely odd
  `nu_X>=5`; `nu_X=3` clears the intruder.  Budget pricing cannot remove a
  zero-price step.  **CONJECTURE:** whether a completed Q+E5/E5F route
  realizes this X/resonance pair is the first refile question.

- **11-B has an empty one-step opponent window.**  The off-axis maximum is
  `5/22`, below every neutral chain-1 X.  If the `w=3` resonance itself is
  pole-adjacent, X is `5/4`; if neutral pads precede it, its later rescaled
  gap lies below the pole-adjacent X.  The type `(2,5)` prefix exhaustion is
  nevertheless new.

- **11-C has empty leaf one-step windows:** both off-axis maxima are `2/5`,
  while the selected strict X is `>1/2`.  It contains exact td-7 local pairs,
  but the 145-row corrected skeleton includes direct and nested three-pole
  orders.  **CONJECTURE:** its global window remains empty after inner-merge
  and terminal gaps are added.

#### td-13

Let `X_*` be the largest actual pole-adjacent `M=1` gap on a route.  At the
entry/one-step tier, conditional on a nonempty stack:

| entry | exact comparison | entry-local result |
|---|---|---|
| 13-2a | `3/14 < 1/2 < X_*` | empty |
| 13-2c | `2/5 < 1/2 < X_*`, or resonant `X_*=11/10` | empty |
| 13-2d | `1/4 < 1/3 < X_*` | empty; requires a new `k|3` exhaustion |
| 13-3 | `2/5 < 1/2 < X_*` | max-X window empty |
| 13-4 | `2/5 < 1/2 < X_*` | max-X window empty |

**LOUD QUALIFIED RESULT: FIVE OF SIX td-13 ENTRIES HAVE AN ENTRY-LOCAL
MAX-X EMPTY WINDOW.  THIS IS NOT YET A GLOBAL TOWER THEOREM.**

The qualification matters.  In 13-3, the `w=4` resonance `7/6` lies in a
labelled `w=2` branch's window; with two neutral branches,
`x(nu_Y)>x(nu_X)` exactly when `nu_Y<nu_X`.  In 13-4,
`X_*=x(min_i nu_i)`; every nonmaximal labelled branch sees a sibling in its
own window, and ties give simultaneous X vertices.  A routewise max-X choice
removes the leaf intruder arithmetically.  **CONJECTURE:** this relabelling is
compatible with H8 and the single global ladder through every nested merge.

**13-2b is the next hard td-13 object.**  It is the sole all-off-axis entry,
so no L-A X exists.  It has the following exact N1-valid menu pair:

```
b=2 branch: M-preserving neutral (l,n,nu)=(2,1,5),
            (dp,dq,M,kbar)=(10,6,2,9), gap=3/10;
b=3 branch: charged (dp,dq,nu,l,kbar,M,lambda)
            =(20,16,5,3,4,4,1), gap=2/5.
```

Therefore its menu window is genuinely nonempty:

```
                         3/10 < 2/5 < 5/2.
```

The same `b=3` branch also has a zero-cost clean resonance of gap `3/4`; if
synchronization forces that branch shape and makes it the carrier, its local
top window is empty.  **CONJECTURE:** a completed Q+E5 route realizes the
displayed `3/10,2/5` pair.  E5F cannot decide it before the refile supplies
`(nu_G,kbar_G)` and both arrival vertices.

For every row marked “empty,” the proved statement stops at entry/one-step
arithmetic.  A full-route empty window remains **CONJECTURE** until charged
predecessor strata, state-changing descendants, inner merges, pads/E5F
reroutes, trunks, terminal gaps, and H8 stack existence are closed.

## 4. EXECUTION ESTIMATE

Define one round as one frozen artifact with machine gates, an independent
exact replay, one hostile review, and its errata fold.  A large enumeration
run without a completeness proof is not a round.

| rung | refile rounds | tower/closure rounds | expected total |
|---|---:|---:|---:|
| td-11 | 3--4: parameterized P0/shared-budget core; two two-pole books; corrected three-pole mixed/nested book plus ODE/E5F gates | 2--3: resolve 11-A's `5/8` order, port the empty-window entries, prove composition; 1 promotion review | **CONJECTURE: 6--8** |
| td-13, after td-11 core promotion | 5--7: budget-11 `b=3,5` closure; four two-pole books; all-off-axis mixed book; three-pole book; 26-hierarchy four-pole book plus generalized ODE/E5F | 3--4: five max-X ports, new `k|3` block, 13-2b first-death analysis, multipole composition; 1--2 promotion reviews | **CONJECTURE: 9--13 additional** |

Recommended order is deliberately not increasing cell count:

1. Build the cap-free shared-budget kernel and run **11-A first**.  If E5F or
   the generalized ODE removes every `5/8` route, the td-11 tower returns to
   the empty-window track.
2. Close 11-B, then use 11-C as the first nested/local-to-global test.  Do not
   promote td-11 from the two two-pole entries alone.
3. At td-13 run **13-2b before the 1204-row four-pole skeleton**.  It is the
   smallest object that tests whether a tower theorem exists without an
   `M=1` carrier.  A failure there changes the architecture for the whole
   rung.
4. Only after that decision run the `b=5` and m=4 breadth campaigns, with the
   five max-X entries batched by type/cap.

These totals are conditional closure estimates.  **CONJECTURE:** if 11-A or
13-2b survives the generalized first-death analysis, coefficient gluing or a
new ODE invariant is needed and the round count is unbounded by present
evidence.

The single biggest risk is **finite completeness of the priced nested state
space**.  Post-jump numerator and `M` grow, an inner arrival uses the current
state rather than the entry `b`, and every inner merge seeds another chain.
Without a cap-free normal form, a capped run can miss exactly the route needed
to defeat an E5 kill or a tower window; no amount of review can promote an
empty census built on that omission.
