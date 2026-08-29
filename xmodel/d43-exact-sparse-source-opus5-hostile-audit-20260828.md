# D43 exact sparse source route — Opus 5 hostile audit

UTC: 2026-08-28T19:50Z  
Role: independent read-only audit through the authenticated `claude --model opus` CLI  
Verdict: **REPAIR** — the route is meaningful and smaller than stated, but its coefficient-field and checkpoint claims need correction.

## Independently confirmed

Setting the support complement to zero is an honest specialization: any exact
solution of the restricted system is an exact solution of the full 184-row
raw-J system.  The modular support is therefore a search heuristic, not a
circular proof premise.

The committed `d43_char0_lift.source_rows` evaluator already gives an
independent source-first route to all 184 canonical values.  A light scratch
replay found:

| check | result |
|---|---:|
| nonzero rows at either registered banked point | 0 / 184 |
| live rows on the common 22-tail support | 29 / 184 |
| live bands | 20: 10, 30: 9, 40: 10 |
| maximum total tail degree | 2 |
| Jacobian rank in the 22 tail columns at either witness | 22 |

Thus the restricted system is locally zero-dimensional in the tails.  After
eliminating those 22 tails, its mathematical core is seven residual
conditions on `W1,W2`.

The `+42` inhomogeneity at `(eta,slot)=(0,20)` agrees across the source
evaluator, `eplus43`, and the preflight checker.  The parked/NF distinction,
the rejection of the old 89-variable witness, and the scoped
`alpha=beta=0`/`P4P1` caveat are also correct.

## Required repairs

### R1 — E5/E6 leave the common W scale free

The two E5 rows have three unknowns `(HM,W1,W2)`.  Eliminating `HM` gives the
single relation

```text
(9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4 = 0,
```

equivalently

```text
W1^4/W2^4 = (15*r3-26)*A2/A1.
```

E6 introduces `s1F`; with the unit conditions it does not fix the remaining
common W scale.  The preflight's bounds obtained by adjoining two separately
pinned fourth roots (`[K:K0] <= 16` and `432 -> 6912`) are therefore wrong.
`W1,W2` must remain solve unknowns; their eventual residue field is an output
of elimination.

The J rows supply the missing scale condition.  Holding the E5 ratio fixed
and scaling both W values by a generic `lambda` makes the band-20 coefficient
system inconsistent: rank 4 but augmented rank 5.  At the banked scale the
augmented rank drops to 4.  In a mod-105337 scratch check the allowed scales
were roots of a degree-six polynomial.  All four fourth-root ratio branches
had the same rank-4/augmented-rank-4 behavior at their corresponding banked
scale, so there is no observed branch-selection defect.

Computationally, solve the raw J system first and use E5/E6 as a filter on its
finite candidates.  Algebraically, a proved elimination-equivalent E/unit
form may instead be intersected with the raw-J ideal; the claim tier must say
which formulation is used.

### R2 — the full-checkpoint sharder is not launchable

`FORB` has three orbits and `GORB` has six.  Seven of nine checkpoints exist,
and the final cumulative g checkpoint `jet_g_05_GB21.pkl` is absent.  The
monolith is still inside g-orbit construction, not the final two `jmul`
calls.  Therefore no worker that requires complete `jf,jg` may launch.  The
19-band target partition itself is correct but remains inert until checkpoint
9/9 and a fresh compatibility seal.

The support-specialized source-first producer does not depend on those full
checkpoints and remains the preferred route.

### R3 — make every zero specialization literal

The producer contract must explicitly set to zero:

- every tail outside the 22-name support;
- `uf18,uf24,uf30,vf1_34,vf1_36,vf2_34,vf2_36`;
- all six PIN42 level-74 tails; and
- `Xf_alpha,Xg_beta`.

It must retain the fixed B-orbit constants and impose `HW_i=h*W_i` in the
`a00pp` frame.  The 155 exact-zero rows need a support/weight identity proof,
not only sampled evaluations.

### R4 — interpret the 4/4/4 ranks correctly

Rank four at the banked point is not six freely selectable lower directions:
the generic augmented rank is five.  The lower block already imposes a
nontrivial condition on the coefficient algebra.  The modular ranks are shape
evidence only and do not reconstruct an exact lift.

### R5 — coefficient-ring wording

The rank-432 `RadicalCoefficient` object is initially a quotient algebra, not
automatically a field.  The two etale specialization gates certify the
registered fibers, not global irreducibility.  A solver must either work
componentwise or prove the selected component is a field.

## Corrected minimal artifact contract

1. Emit the 184 symbolic raw-J rows over the exact radical quotient algebra
   with polynomial unknowns `W1,W2` and the 22 retained tails.  The existing
   `source_rows` formulas provide an independent semantic reference for the
   new sparse-jet emitter.
2. Bind the complete literal zero-specialization manifest above, retain the
   B-orbit constants, append `+42` once, and keep `alpha=beta=0`.
3. Prove exactly 155 rows vanish identically and retain them in the manifest;
   expect 29 live rows in bands 20/30/40 of tail degree at most two.
4. Eliminate the 22 tails using a mechanically certified full-column-rank
   chart, retaining all chart alternatives if its minor vanishes.  Produce
   the seven-condition residual ideal in `W1,W2`.
5. Intersect or post-filter with the exact E relation and `W1*W2 != 0`.
   Replay the literal E5 pair with `HM`, E6 with nonzero `s1F`, and the unit
   equations before making a template-conform claim.
6. Replay all 184 raw rows exactly at every candidate.  Only afterward reduce
   under the two registered prime embeddings as regression evidence.
7. Keep raw finite-J existence, full template-conform existence,
   NF-presentation equivalence, all-depth compatibility, a Keller map, and
   JC2 as separate claim tiers.

## Ranking

Promote the support-specialized exact lane within the D43 program: it is now a
small zero-dimensional elimination problem rather than a speculative large
solve.  Under campaign policy, even this bounded exact computation belongs on
AWS after hostile packet review; the audit's scratch checks were diagnostic
only.  Defer the general 19-shard lane until the final g checkpoint exists.
Nothing here changes the global warning that a finite D43 point is not an
all-depth object or a JC2 counterexample.
