# Blind whole-portfolio ideation — Opus 5 — round `20260830T1015Z`

Researcher: Opus 5, equal-standing whole-portfolio lane.
Declared basis: `4decd33d5caf8553bcbaa199b93a900ecabeee18`.
Lifecycle: **BLIND SUBMISSION / EXACT DESK RESULTS PROVISIONAL / DIFFERENT-MODEL
REVIEW REQUIRED BEFORE ANY PROMOTION.**
This report asserts no new exit price; expect receipt `charge_basis_status=ABSENT`.

## 0. Custody, execution, and one disclosed basis drift

I recomputed and matched all ten charged hashes in the state packet before use:

```text
ce5b9564a8f5cab7eea146e0408bc32950ff8a168a678f340d682fba4e621c58  state packet
90df4ac0... APPROACHES.md      ab1865c8... AUDIT.md
1c0c20fa... COORDINATION.md    046dbe4d... PROGRESS.md
7f901db6... ladder/REDUCTION.md  2dc015cf... notes.md
0db1bd7d... xmodel/ideation-20260829T2254Z-synthesis.md
bb55f9a5... xmodel/websweep-20260830T0340Z.md
6a7dc7be... xmodel/bd-a2-singular-f5-unbalanced-local-polar-sol56-20260830.md
5a31a2ab... xmodel/bd-a2-q8-f5-global-lattice-elimination-b5-b6-u5-u6-sol56-20260830.md
```

**Disclosed defect in my own custody discipline.** The working tree advanced
from the declared basis to `026099e3` *during* this session (other lanes
committed). All ten hashes matched at first read, but a later read of
`AUDIT.md` returned post-basis content, because I verified once rather than
per read. Consequences, stated exactly:

- Every mathematically load-bearing input I actually computed on is
  byte-pinned and **unchanged** across the drift, re-verified at the end:
  `6a7dc7be...`, `5a31a2ab...`, `fdf8f476...`
  (`bd-a2-singular-f5-local-polar-and-a6-a7-elimination-coordinator-integration`,
  charged inside §1 of `5a31a2ab...`), and `2739f638...`
  (`bd-a2-normal-f5-decorated-carrier-effectivity-reduction-different-model-review-gpt55-r2-20260830.md`,
  a secondary input I pinned myself; it is *not* in the packet's charged list).
- I did consume one post-basis fact: the current `AUDIT.md` head records that
  the GPT-5.5 q=8 hostile review returned `CONFIRM_WITH_CORRECTIONS` and that
  the singular-F5 q=8 rows are now **promoted** empty, with binding repairs.
  The packet's §1.1 language ("review is active … treat as provisional") is
  therefore stale relative to its own charged `AUDIT.md`. I flag this rather
  than hide it; §8 turns it into an `UPGRADE` card.
- I read **no** sibling blind submission, prompt, log, or run receipt from this
  round, and no file under `jc2-lean`. I did not read the GPT-5.5 q=8 review
  report itself, only the ledger sentence above.

Execution: desk-scale exact integer arithmetic in Python, no CAS, no network.
Every claimed run is a separate process under the 60 CPU-second / 1 GiB budget
(measured: 41.5 s, 33.9 s, 2.7 s, 0.9 s; max RSS 12 MiB). Scratch lives in
`/tmp/jc2op`; no canonical file, Git object, or `ops/` artifact was touched.
The scripts contain **zero** Python `assert` statements — all gates are
explicit `if`/`RuntimeError` — and the control suite emits the identical digest
`77dab2ff5974d64f53a9432e40275d3c5e549036555cf61ff1e81e3bee07ae03`
in ordinary, `-O`, and `-OO` modes, with a live mutation that is rejected in
all three.

---

## 1. Disposition over all 46 avenues

Three raises, one execution-priority lower, no reopen, no lower of tier. All
changes share one driver: the Miyanishi–Sugie `A1`-ruling/Euler instrument has
gone from decorative to load-bearing, and it is transplantable off the
quadratic client.

| # | Disposition | Reason |
|--:|---|---|
| 1 | unchanged | No new degree/td ceiling; the GGV transcription bridge is untouched this round. |
| 2 | unchanged (principal) | `G2-PSC`, universal landing/coverage, and the absent td ceiling are all exactly as in `ladder/REDUCTION.md`. Nothing this round bears on them. |
| 3 | unchanged | Scope still strips/`d1=1`/depth two. |
| 4 | **lower (execution priority of the row-extension sub-lane only; tier unchanged)** | Each further ramified calendar grade costs more and buys a strictly weaker finite-jet statement. §6 argues a jet-**codimension** law and a transition-image theorem dominate more rows on information gain. The avenue itself is not demoted. |
| 5–6 | unchanged | — |
| 7 | unchanged | Still no component-labelled `A(F)` packet; it is now the single highest-value *missing object* (§2, §3.2). |
| 8–25 | unchanged | No new evidence; 11, 18, 41, 44 stay closed/refuted. |
| 26 | **raise** | The block-descent structure theorem gives a forced non-`A^2` étale sandwich; §3.2 supplies a *promoted* instrument that applies to that surface without any quadratic frame. Index `d2=2` gains a concrete first test rather than a slogan. |
| 27 | unchanged | The decisive gate in the F5 funnel is a boundary dual-graph forest condition, i.e. plumbing-style reasoning — but on the incidence surface, not on the link of the map. Methodological transfer noted; the avenue's own object is untouched. |
| 28 | **raise** | Promoted at 08:33Z and now doing real elimination: `r+k<=8` kills every `A8` row, and in my q=6 computation (§5) it is what bounds the affine ADE decoration to `r_aff<=3`. This is the first time a log-surface/Euler argument has emptied cells rather than "passing identically". |
| 29 | unchanged | The `kappa(P)` quotient is still an exact reformulation with no receiver. |
| 30 | **raise** | Same driver as 26: the forced non-`A^2` surface `Y` is now a target for a promoted instrument, not only a recognition problem. |
| 31 | unchanged | Rees/normal-filtration tool with a K00 client; no integrality proof. |
| 32–46 | unchanged | No new evidence; 46 stays rigor-only. |

Nothing in this round justifies raising 25, 33, 34, 35, or 39: the F5 result is
lattice/graph combinatorics, not monodromy, symplectic, sweep, or cohomological
content.

---

## 2. Reranked gaps

### 2.1 Global proof gaps

1. **Selector arrow** — from an arbitrary minimal Keller counterexample to one
   bounded boundary/block client. Unchanged and still first. The fixed-quadratic
   funnel is now nearly closed and still buys nothing without this.
2. **`G2-PSC`** — GGV packet → decorated Sigray pole tree with fidelity.
3. **Quadratic-basis existence / intrinsic degree ceiling** — rises above the
   remaining quadratic strata. Closing every quadratic presentation is
   worthless if no counterexample admits one; §5.4.
4. **Universal full-configuration landing/coverage** (CRITICAL 4).
5. **Absolute or cofinal td ceiling** (CRITICAL 7).
6. **`G2-BD`** — bounded delay, route-specific.
7. **Component-labelled `A(F)`** — promoted from "nice to have": it is the only
   named object that could give a *lower* bound on the ramification-prime count
   `k` to meet the Euler cap's *upper* bound (§3.2).
8. Remaining quadratic strata: nonreduced infinity, projective basepoints/
   nonfiniteness, degree drops, higher/primitive blocks.

### 2.2 Counterexample / falsification gaps

1. **Source completeness** of the K00 normalized supports — an unnoticed failure
   retroactively voids the whole ramified calendar, so it dominates.
2. **Transition-image theorem** — turn finite-jet emptiness into a statement
   about actual transitions; without it no number of rows converts.
3. **Compatible all-order lifting** — the arc, not the jet.
4. **Occurrence / reachability** — which cells a real minimal pair can occupy.
5. **Algebraization** — last, and only after 3.
6. Row extension in a fixed calendar — now *below* all of the above (§6).

---

## 3. One new mechanism and one new connection

### 3.1 `MARK-EPS` — the marking-corrected intersection identity (`NEW`)

The promoted q=8 identity is

```text
sum_(j<k) C_j.C_k = 2*sum_(j<k) a_j a_k - (sum_l c_l^2 - Q)/2,   Q >= sum_l c_l,
```

and it silently uses `C_j.S_0 = 0`, i.e. `b_j = 2a_j`, which holds **only** at
`h_S = 3`. Repository search finds `C_j.S_0=0` exactly once, in `5a31a2ab...`
line 281, and no epsilon-corrected form anywhere. The correct general form,
with `eps_j := C_j.S_0 >= 0` and `sum_j eps_j = C.S_0 = 3 - h_S`, is

```text
b_j = 2 a_j + eps_j,
sum_(j<k) C_j.C_k
   = 2*sum_(j<k) a_j a_k
     + [ (sum_j a_j)(sum_j eps_j) - sum_j a_j eps_j ]
     - (sum_l c_l^2 - Q)/2,                                        (MARK-EPS)
```

and, equivalently and more usefully, pairwise disjointness is the **exact
forced-overlap system**

```text
sum_l x_(jl) x_(kl) = 2 a_j a_k + a_j eps_k + a_k eps_j    for every pair,
```

which turns a blind split enumeration into a two-sided-pruned column search.
`MARK-EPS` reduces to the promoted identity at `eps = 0`. It is what makes q=6
computable at desk scale at all (§5), and it is the reason the q=8 argument
does not transfer verbatim: at `h_S = 2` the marking contributes a *positive*
`sum_j a_j - a_(j0)` term that partly cancels the negative square-sum term.

Positive control: an independent implementation of the ambient lattice plus
`MARK-EPS` reproduces **all twelve** rows of the `5a31a2ab...` §5 replay table,
including the intermediate linear and adjunction counts
(`648/270/0`, `59/37/0`, `504/90/0`, `67/21/0`, `33/15/0`, `8/5/0`,
`504/90/0`, `513/162/0`, `49/19/0`, `52/30/0`, `234/18/0`, `33/9/0`),
0 mismatches. Mutating one Gram entry (`S_0^2 = -1`) makes the same control
fail closed in all three optimized modes.

### 3.2 `RULE-ON-Y` — transplant the promoted `A1`-ruling instrument onto the block-descent surface (`NEW` composition; components `KNOWN`)

The 08:33Z promotion applies Miyanishi–Sugie plus Gurjar–Miyanishi Lemma 2.2 to
`U = X \ Supp(H+R_X)` for the *quadratic incidence* surface. The hypotheses it
actually consumes are: `U` normal affine, and dominated by `A^2`. The
block-descent structure theorem (2254Z §4.2, promoted) gives, for **any** proper
intermediate field of **any** hypothetical non-invertible Keller map,

```text
A^2 --g1 etale, quasi-finite--> Y --g2 finite flat--> A^2,
Y normal affine, Y not isomorphic to A^2, branch(g2) nonempty and missed by g1.
```

Since `g1` is dominant and its image misses `B = branch(g2)` pointwise,
`A^2 -> Y \ B` is dominant, so `Y \ B` is a normal affine surface dominated by
`A^2`. The same theorem therefore applies: `Y \ B` carries an `A1`-fibration
over `A1` or `P1`, and every reduced degenerate fibre is a disjoint union of
`A1`s. This is **selector-side**: it needs no quadratic trace-zero frame, no
fixed presentation, and no F5 infinity type.

Explicit scope, stated because it is the obvious way to get this wrong: the
*numerical* cap `e(U) = 12 - r - c` does **not** transfer. The `12` is the Euler
characteristic of one specific completion of the rank-eleven quadratic
incidence; `Y` has no charged completion or Picard rank. What transfers is the
qualitative ruling and the fibre-component structure. Converting that into a
number requires an independent completion/Picard bound for `Y` — which is
exactly where a component-labelled `A(F)` packet would enter, since
`disc(g2) subset A(F)` gives an independent handle on the boundary components.

Novelty check: `Miyanishi` occurs in the repository only in `COORDINATION.md`
policy lines and in the `bd-a2-a1-ruling-*` quadratic packets; there is no
application to `Y` or to any block-descent object.

---

## 4. Selector, QCS, `G2-PSC`, `G2-BD`: prove / falsify / bypass

| target | prove | falsify | bypass |
|---|---|---|---|
| **global selector** | Build the arrow *from the client side*: show that any minimal counterexample with a proper block yields a `Y` satisfying the `RULE-ON-Y` hypotheses, then bound `Y`'s boundary. This replaces "every counterexample has a quadratic presentation" (unproved) with "every counterexample with a block has an `A1`-ruled `Y \ B`" (proved modulo §3.2 review). | Exhibit an abstract normal affine `Y`, not `A^2`, with an étale quasi-finite `A^2 -> Y`, a finite flat `Y -> A^2`, and a branch divisor whose complement is `A1`-ruled — i.e. a consistent sandwich model. That would show the sandwich cannot be excluded by these instruments and would *lower* avenues 26/30. | Attack primitivity directly (avenue 26): if minimal-degree Keller maps are primitive, the whole intermediate-surface programme is vacuous, and no selector through blocks is needed. |
| **QCS** | Construct the map from a reduced pole module to a quotient-collision event module (`PAIR-SQUARE-QCS/v1`); still needs compactification invariance and the event-module dimension. Name where `J(F)=1` enters through the boundary. | Show the off-diagonal étale cover depends only on monodromy and boundary data with no `J=1` slot — then no rank inequality can be derived from it, and the object is `COSTUME`. | Route the rank inequality through the block discriminant instead of the fibre square, using `disc(g2) subset A(F)`. |
| **`G2-PSC`** | Unchanged: a fidelity functor from GGV packets to decorated pole trees. | Exhibit two GGV packets with identical Sigray-normalized pole trees but different downstream book behaviour. | Pure-Sigray architecture (already documented): pay your own source theorem instead. |
| **`G2-BD`** | Unchanged. | Unchanged. | Do not import `td=12` laboratory results into an untyped map; keep the conditional tier explicit. |

I do **not** propose retrying the refuted codimension-one-image bridge or the
`Y isomorphic to A^2` alternative in any of these lanes.

---

## 5. The q=6 attack, executed

This is the item with the most content, so I state the endpoint first, then the
mechanism, then exactly which conclusions depend on which lemma.

### 5.0 Endpoint

Working in the promoted `S`-adapted nine-blowup basis of `F_2`, with the
promoted q=6 marking, and charging only the `6a7dc7be.../fdf8f476...` local
polar rows:

```text
U_3/A_3  (partition 4+4)     : EMPTY, using only promoted instruments.
B_3/A_2  (partition 4+2+2)   : reduces to exactly ONE integral configuration,
                               which dies under a new affine-root forest
                               lemma (5.5) that itself needs review.
```

Everything below is exact integer arithmetic, replayed, controlled, and
provisional.

### 5.1 Why the q=8 mechanism fails at q=6 — the precise reason

Take `A = 2S_0+5F-sum E_i`, `B = F`, `r^*R_X = 2A+B`, and the promoted q=6
marking `h_S = 2`, `L = E_l`, `T = S_0+3F-sum_(i in I_6) E_i` with `|I_6| = 6`,
`Z_H = 2F-2E_l-E_j-E_k`. I verified `A = L+S+T+Z_H` and `T^2 = -2`,
`S.T = 1` exactly. The charged local rows have `m = h` in both q=6 rows —
`m=(2,1) = h` for `A_2` (from `n = 3e_1`) and `m=(2,2,1) = h` for `A_3` (from
`n = 2e_1+e_2`) — so the exceptional polar block is `Z_H` and

```text
C = r^*R_X - Z_H = 4S_0 + 9F - sum_i c_i E_i,
c_l = 0,   c_j = c_k = 1,   c_i = 2  (i in I_6),
sum c = 14,   sum c^2 = 26.
```

The decisive difference is the **residual boundary contact**:

```text
q=8:  C.S_0 = 0,  C.T = 0,  C.L = 0,  sum c = 12, sum c^2 = 20;
q=6:  C.S_0 = 1,  C.T = 1,  C.L = 0,  sum c = 14, sum c^2 = 26.
```

So `b_j = 2a_j` fails for exactly one prime, and the promoted identity is not
applicable as written. `MARK-EPS` (§3.1) supplies the corrected form.

This is not a bookkeeping artefact. It is the same fact as `S.T = 1`: at q=6 the
two sections meet `E_1` at one common point, and the local data say which germ
passes through it. For `A_3`, the smooth polar germ (2.5) meets `E_1` at `Z=1`,
which §2.3 of `6a7dc7be...` identifies as the point carrying "the two section
directions"; its `ord(u)` is then `h_1 + 1 + 1 = 4`, and the cusp through the
node `E_1 cap E_2` has `h_1+h_2 = 4`, recovering `4+4`. For `A_2`,
`ord(u) = h_1 + (H'-contact)`, so the degree-4 germ is the one through the
common section point and the two degree-2 germs are disjoint from `S,T`. I call
this the **sharp marking** (`eps` and `eta` on the same prime); the scan below
also runs without it.

### 5.2 What is enumerated

For strict primes `C_j = a_j S_0 + b_j F - sum_l x_(jl) E_l`:

```text
a_j >= 1 (horizontal),                b_j = 2 a_j + eps_j,
sum_l x_(jl) = 5 a_j + 2 eps_j - d_j,
sum_(l in I_6) x_(jl) = 3 a_j + eps_j - eta_j,     x_(j,l) = 0,
eps_j, eta_j >= 0 with sum eps = C.S_0 = 1, sum eta = C.T = 1,
p_a(C_j) >= 0,        pairwise:  sum_l x_(jl) x_(kl) = 2 a_j a_k + a_j eps_k + a_k eps_j.
```

Two lattice facts remove the need for any decoration guesswork:

- **At most one contracted carrier, unconditionally.** Solving
  `S_0.Z = L.Z = T.Z = A.Z = 0`, `p_a(Z) >= 0` gives `beta = 2 alpha`,
  `sum z = 5 alpha`, `sum z^2 <= 2 alpha^2 + alpha + 2`; the minimum sum of
  squares over the eight available coordinates already exceeds the bound for
  `alpha >= 2`. So `alpha = 1` and `Z = S_0+2F-E_j-E_k-sum_(K) E_i`,
  `K in binom(I_6,3)` — the 20 charged candidates, each containing **both**
  outside indices. Since `c_j + c_k = 2` is a lattice invariant, a second
  carrier or a carrier of multiplicity two would need `c_j + c_k >= 4`.
- **The affine root system is `A_5 + A_1`.** A square-`(-2)` class with
  `p_a = 0` orthogonal to `S_0, F, A, K, T, L` forces `alpha = 0` and hence
  `Q = E_p - E_q` with `p,q` both in `I_6` or both in `O`. (The numerical
  classes `F - E_p - E_r` are excluded because they meet `S_0` — the same
  repair the q=8 review required.) In particular no `D` or `E` affine tree can
  occur, since `A_n` has only type-`A` subsystems.

The scan therefore covers **every** total class reachable by *any* number of
affine roots of *any* multiplicity, with or without the single carrier:

```text
type N: 4S_0+9F,  c_l=0, c_j+c_k=2, sum_(I_6) c = 12,  sum_j a_j = 4;
type Z: 3S_0+7F,  c_l=0, c_j=c_k=0, sum_(I_6) c =  9,  sum_j a_j = 3.
```

Up to the `S_6 x S_2` symmetry that is exactly 142 canonical classes. Because
`sum_j a_j <= 4` and `a_j >= 1`, the number of strict primes is `n <= 4`; I
enumerate every composition `d` of 8 into `n` positive parts, so **every**
`B_3/A_2` modulus subcell (the `Delta = 0` tangent cell and the `tau = 0`
endpoint cell, where only `k >= 2` is safe) is covered without needing its
unpinned local table.

### 5.3 Results

| level | filter | pairwise-disjoint survivors | distinct total classes |
|---|---|---:|---:|
| L0 | any `n<=4`, any `d`, `eps/eta` free, **no** Euler cap, **no** root-forest | 156 | 16 |
| L1 | + sharp marking | 116 | 15 |
| L2 | charged rows `{4+4, 4+2+2}` only, `eps/eta` free | 18 | 3 |
| L3 | charged rows + sharp marking | **6** | **1** |
| L3 restricted to `U_3/A_3` (`d = 4+4`) alone | | **0** | 0 |
| L0–L3 + Euler cap + affine-root forest lemma (5.5) | | **0** | 0 |

**L0 is the honest headline for the transferred mechanism: the promoted q=8
argument does not close q=6.** The uniform bound leaves 156 labelled survivors
once the decoration lattice is opened up.

The six L3 survivors are one unordered configuration up to labelling, on the
single class `c = (0,1,1,4,4,2,2,0,0)`:

```text
C_a = 2S_0 + 5F - (0,1,1,2,2,1,1,0,0)   A.C=4  B.C=2  C.S_0=1  C.T=1  p_a=0
C_b = 1S_0 + 2F - (0,0,0,1,1,0,1,0,0)   A.C=2  B.C=1  C.S_0=0  C.T=0  p_a=0
C_c = 1S_0 + 2F - (0,0,0,1,1,1,0,0,0)   A.C=2  B.C=1  C.S_0=0  C.T=0  p_a=0
```

It lives only in the `B_3/A_2` row and requires the shift
`D = c - c_base = (0,0,0,+2,+2,0,0,-2,-2)`: an affine ADE decoration of
exceptional ramification multiplicity **two**.

### 5.4 What is already closed, and by what

- `U_3/A_3` is empty using **only promoted instruments**: the charged `4+4`
  vector with `m = (2,2,1)`, the sharp marking read off `6a7dc7be...` §2.3, the
  promoted Euler cap, and the promoted forest condition on strict primes. No
  new lemma. Directly verified: restricting to `d = (4,4)` with the Euler cap
  on and the forest lemma off returns 0 survivors at the sharp marking **and**
  at the relaxed marking.
- `B_3/A_2` needs one further step.

### 5.5 `AFF-FOREST` — the affine-root forest lemma (`NEW`, review-critical)

Let `Sigma_0 = Supp(H)` union the infinity exceptional tree. It is connected
(the three F5 branches meet at `p_0`). Every strict prime meets `Sigma_0`,
because `A.C_j = d_j >= 1`. Every affine ADE curve `Q` in `R_X` is **disjoint**
from `Sigma_0`: `A.Q = 0` with `A = S+T+L+Z_H` effective, `Q` not a component,
and every `h_i >= 1`, so each term vanishes. Hence if a connected affine tree
`T` meets two distinct strict primes, the path through `T` and the path through
`Sigma_0` close a cycle in the dual graph after a common embedded SNC
resolution — precisely the promoted second-path argument. Therefore

```text
#{ j : sum_(Q in T) C_j.Q > 0 } <= 1   for every connected affine tree T,
with   C_j.Q = x_(jp) - x_(jq) >= 0.                        (AFF-FOREST)
```

I deliberately do **not** claim the stronger `sum_j C_j.Q <= 1`: a single
tangential contact of multiplicity two resolves to a chain, not a cycle, so
that stronger form is false and I do not use it.

Applying `AFF-FOREST` to the six survivors: `c` takes values `{4,2,0}` on
`I_6`, and the columns with `c = 4` have splits `x_(.,3) = x_(.,4) = (2,1,1)` —
all three primes positive. Every decomposition of `D` into `<= 3` roots (the
Euler bound for `rho_0 = 2`, `k = 3`) — two disjoint `A_1`s with `mu = 2`, an
`A_1+A_2`, or an `A_3` chain with `mu = (2,4,2)` — has a connected component
whose telescoped root sum is `E_p - E_q` with the `c=4` column at `p`, hence is
met by all three primes. Four or more roots exceed the Euler cap. So no
admissible decoration exists and the class dies.

The exhaustive machine check enumerates every ADE forest of at most
`8 - rho_0 - n - #Z` roots in `A_5 + A_1` (pairwise intersection in `{0,1}`,
acyclic), solves exactly for the multiplicities by rational elimination, and
tests `AFF-FOREST` per connected component. Result: 0 survivors at every level
L0–L3.

### 5.6 Controls

- Positive: 12/12 rows of the charged q=8 replay table reproduced exactly,
  including intermediate counts.
- Mutation (fail-closed): corrupting `S_0^2` makes the positive control raise
  in ordinary, `-O`, and `-OO`.
- Forgery: a hand-built pair with the *same* `A`- and `B`-degrees as two true
  survivors is rejected by the disjointness test; a self-pair is rejected.
- Old-pass/new-fail: relaxing `AFF-FOREST` from `hits <= 1` to `hits <= 3`
  revives the six survivors; tightening the Euler bound from `r_aff <= 3` to
  `r_aff <= 1` also kills them. Both knobs are demonstrably load-bearing, so
  the zero is not vacuous.
- Zero AST `Assert`; identical JSON digest in all three modes.

### 5.7 Exact scope and what is *not* claimed

Charged and unchanged: `6a7dc7be...`, `5a31a2ab...`, `fdf8f476...`,
`2739f638...`. Mine and unreviewed: `MARK-EPS`; the identification `M = Z_H`
for q=6 from `m = h`; the sharp marking; `AFF-FOREST`; the at-most-one-carrier
and `A_5 + A_1` lattice classifications. `U_3/A_3` is the local packet's
provisional row.

This proves no effectivity, no proximity, no analytic realization, no incidence
surface, no polynomial map, no counterexample, and no JC2 result. Together with
the promoted q=8 closure it would empty the reduced finite normal-singular F5
stratum — **and that is still not JC2**, because the presentation and selector
arrows (§2.1 items 1 and 3) are absent.

### 5.8 A non-quadratic alternative, ranked above finishing the funnel

`RULE-ON-Y` (§3.2). The quadratic funnel is one fixed-basis cubic-block horn;
closing it fully returns a theorem about presentations that may not exist. The
`A1`-ruling instrument is the transferable asset the funnel produced, and it
applies to the block-descent surface with no presentation hypothesis. If I had
one lane, I would spend it there, not on the last quadratic strata.

---

## 6. K00: the strongest next attack

Ranked by information gain per unit compute, against the packet's five options.

1. **Source-completeness falsification (highest).** A single missed normalized
   support voids every ramified calendar row retroactively. Enumerate the next
   partition rather than extrapolating from three closed calendars. Failure is
   as valuable as success here, which is what makes it dominant.
2. **`JET-CODIM` — a stopping law, not another row (new; adjacent precedent
   only).** Every closed cell reports *emptiness* of a jet scheme at grade `G`.
   Nobody has recorded the **codimension** of the surviving scheme grade by
   grade. Two outcomes, both decisive:
   - if the codimension increment is eventually `0` on some branch, that branch
     has a formal arc and further row extension on it is provably futile — an
     immediate, honest stop for avenue 4's most expensive sub-lane;
   - if the increment is `>= 1` per grade against a bounded ambient dimension,
     emptiness is *forced* at a computable grade, converting an open-ended row
     grind into a finite theorem.
   The measurement is nearly free: the existing solvers already build the
   ideals; only the dimension call is added. Novelty: the one repository hit
   for "stopping theorem" (`sol-ucda.md:340`) is about Puiseux coefficients in
   the residue-A pole calculus, a different object.
3. **Transition-image theorem.** Without it, no number of finite-jet rows
   becomes a statement about maps. This is the arrow, and it is worth more than
   any row — but it is also the least tractable of the three, so it ranks below
   the two cheap discriminators.
4. All-order lifting — needs 3 first.
5. Reachability / occurrence — needs 1 and 3.
6. Algebraization — last.
7. **More truncation rows — explicitly last.** Cost rises per grade, the
   statement stays finite-jet, and `JET-CODIM` can tell us in one pass whether
   the grind terminates at all.

Do not extrapolate one load calendar across ramification indices; the `e=2,m=2`
cell already proved it is not the substitution shadow of `e=2,m=1`.

---

## 7. Software acceleration / decisive experiment

**`LATTICE-REPLAY` — a portable exact ruled-lattice replay library.** Every F5
lattice packet so far has shipped a bespoke script. I wrote an independent one
in this round and it reproduced all twelve charged q=8 cells in 0.06 seconds
and then decided q=6 in four processes, each under the desk budget. Generalizing it
to arbitrary `(q, marking, row, decoration)` gives every future packet a cheap
*independent* cross-check instead of a producer-authored one — directly
addressing the recorded "generated `.sing` unconditional flags" failure mode.

- Acceptance test: reproduce the twelve charged q=8 counts exactly; reproduce
  the q=6 table of §5.3; fail closed on a planted Gram mutation in ordinary,
  `-O`, and `-OO`; zero AST `Assert`; identical digest across modes.
- Compute class: desk. Not AWS.

Not proposed: the 2254Z transition compiler (`KNOWN`, already selected) or any
new heavy CAS.

---

## 8. Campaign-systems card

### `UPGRADE / BASIS-PINNED-READ-ROOT`

**Defect, observed live this round (§0).** Charged-hash verification happens
once, at lane start, but the working tree keeps advancing. A blind lane that
verifies at `T0` and reads the same path at `T1` can silently receive
post-basis content — as I did with `AUDIT.md`, whose head now records a review
verdict the packet describes as pending. Nothing warned me; I caught it only
because I re-hashed at the end. In a blind round this is also a leak channel:
the drifting tree carried sibling submissions into the same directory I was
reading.

**Change.** For any blind or basis-frozen lane, materialize the declared basis
into a read-only worktree (`git worktree add --detach <path> <basis>`), point
the lane's read root there, and make every canonical read resolve inside it.
Cheapest partial version if a worktree is too heavy: require re-verification of
a charged hash immediately before any quotation, and have the round harness
record `basis_drift_detected` in the receipt.

**Smallest measurable acceptance test.** Start a lane at basis `X`; have the
coordinator commit any change to a charged file; the lane re-reads that file.
Pass = the lane's read returns the `X` bytes (worktree version) or the harness
raises `BASIS_DRIFT` (re-verify version). Fail = the lane silently receives
post-`X` bytes. One lane, one commit, one re-read; runs in under a minute.

**Why not `NO_CHANGE`.** I have a live instance, in a round whose entire value
depends on independence, on a file that materially changed its lifecycle
language. This is not hypothetical.

---

## 9. Research cards

### Card A — `Q6-FOREST-CLOSE`

- **Novelty:** `NEW`. No repository text contains `MARK-EPS`, `AFF-FOREST`, or
  any q=6 global lattice computation.
- **Dependencies:** charged `6a7dc7be...`, `5a31a2ab...`, `fdf8f476...`;
  promoted Euler cap and rational-forest theorem; the q=6 marking in
  `2739f638...`.
- **Exact statement to review:** §5.0 endpoint, with §5.1–§5.5 as the argument.
  The three review-critical steps are (i) `M = Z_H` at q=6 from `m = h`;
  (ii) the sharp marking, i.e. that the degree-4 germ passes through the common
  `S/T` attachment point on `E_1`; (iii) `AFF-FOREST`.
- **Cheapest discriminator:** re-run L3 restricted to `d = (4,4)` with the
  forest lemma **off**. It returns 0 in under a second. If a reviewer confirms
  that single number, `U_3/A_3` is closed on promoted instruments alone,
  independent of everything new in this report.
- **Outcome meanings:** all three steps confirmed → the singular F5 stratum is
  empty (a presentation theorem, not JC2). (iii) refuted → `B_3/A_2` survives
  on exactly one integral cell and the successor is proximity/effectivity on
  that cell. (i) or (ii) refuted → the q=6 total class changes and the scan must
  be rerun; the machinery still applies.
- **Stop condition:** any refuted step, or a survivor that also passes
  proximity.
- **Information gain:** high. Closes or precisely localizes the last open cell
  of a stratum that has consumed most of the last day.
- **Compute class:** desk, four processes, each under 45 CPU seconds.
- **Ownership:** prove — the q=6 lane; falsify — a different model attacking
  `AFF-FOREST` with an explicit tangential-contact model; bypass — Card B,
  which does not care whether this closes.

### Card B — `RULE-ON-Y`

- **Novelty:** `NEW` as a composition; both inputs `KNOWN` and promoted.
- **Dependencies:** the block-descent structure theorem; the Miyanishi–Sugie /
  Gurjar–Miyanishi statements as cited in `bd-a2-a1-ruling-euler-boundary-cap-hostile-review-gpt55-20260830.md`.
- **Exact theorem to attempt:** for every proper intermediate `Y` of a
  hypothetical minimal non-invertible Keller map, `Y \ branch(g2)` is a normal
  affine surface dominated by `A^2`, hence carries an `A1`-fibration over `A1`
  or `P1` whose reduced degenerate fibres are disjoint unions of `A1`s.
- **Cheapest discriminator:** verify the two hypotheses only — normality of
  `Y \ B` and dominance of `A^2 -> Y \ B`. Both are one-paragraph checks
  against the charged block-descent theorem. No computation.
- **Outcome meanings:** hypotheses hold → a promoted instrument now acts on a
  selector-side object, and avenues 26/30 have a real programme. Dominance
  fails → the block-descent image statement is weaker than recorded, which is
  itself a correction worth having. Normality fails → restrict to the smooth
  locus and re-price.
- **Stop condition:** a proof that no numerical invariant of `Y` is accessible
  without a completion — then the card yields structure but no elimination, and
  should be parked pending an `A(F)` packet.
- **Information gain:** highest in the report, because it is the only item that
  crosses the presentation firewall.
- **Compute class:** desk / pen-and-paper.
- **Ownership:** prove — a surface-geometry lane; falsify — a lane building an
  explicit consistent sandwich model; bypass — primitivity (avenue 26).

### Card C — `JET-CODIM`

- **Novelty:** `NEW` for K00; adjacent precedent in `sol-ucda.md:340` for a
  different object.
- **Dependencies:** the existing ramified-calendar solvers and their frozen
  fixtures.
- **Exact experiment:** for one already-closed calendar (`e=2,m=2,h10=1`,
  closed through G13), recompute each grade recording the **dimension and
  codimension** of the surviving scheme, not only emptiness. Fit the increment.
- **Cheapest discriminator:** three consecutive grades of one branch. If the
  increment is constant and positive, extrapolate to the forced-emptiness grade
  and check that it matches the observed one — a free retrodiction test.
- **Outcome meanings:** increment `>= 1` with bounded ambient dimension → a
  stopping theorem, and row extension becomes finite and schedulable. Increment
  `-> 0` → that branch has a formal arc; stop extending it and move the whole
  K00 budget to source completeness. Erratic increment → no law; report `OPEN`
  and do not fill the gap by analogy.
- **Stop condition:** no law after two calendars.
- **Information gain:** high and cheap; it is the only proposal that can
  *terminate* avenue 4's most expensive sub-lane rather than feed it.
- **Compute class:** desk if the frozen fixtures suffice; AWS-only and
  preregistered if a dimension call exceeds the desk budget. Nothing is
  launched by this report.
- **Ownership:** prove — the K00 lane; falsify — a reviewer checking that the
  dimension is computed in the declared quotient/localization and not from a
  raw remainder; bypass — source-completeness work, which is ranked above it.

## 10. Ranked launch portfolio

1. **Card A discriminator** (one second): re-run `d = (4,4)` with the forest
   lemma off. Closes `U_3/A_3` on promoted instruments alone. Provisional
   descendants may start immediately; promotion needs review.
2. **Card B hypothesis check** (no compute): the highest-value item, and the
   only one that leaves the quadratic horn.
3. **Card A full review** (`MARK-EPS`, sharp marking, `AFF-FOREST`) by a
   different model. Note that `AFF-FOREST` also applies to the promoted q=8
   affine-root cells and would show they were vacuous — a strengthening, not a
   correction, since those cells returned zero anyway.
4. **`UPGRADE / BASIS-PINNED-READ-ROOT`** acceptance test (one minute). Nothing
   mathematical waits on it, but this round produced a live failure instance.
5. **Card C retrodiction** on the `e=2,m=2,h10=1` calendar.
6. **`LATTICE-REPLAY`** generalization, in the background.
7. K00 source-completeness partition enumeration — the standing top
   counterexample-side item, unchanged in rank by this round.

I did not launch, preregister, or license any AWS work, and no broad web sweep
is due before `2026-08-31T03:40Z`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `34538`.
- Body SHA-256:
  `16cf3e290d423ba084dab92c105ab50882532d87f086552d561d34cff3b51092`.
- Frozen basis: `dcd6cf9ccce35e7deee956245ca46d2dfd00d5d2`.
