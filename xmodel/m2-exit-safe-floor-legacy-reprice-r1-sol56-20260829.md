# M2 legacy exit-floor repricing after the full-exit arity audit

Date: 2026-08-29  
Producer: Sol 5.6 (Ultra)  
Status: sealed producer report; no canonical ledger is edited here

## 0. Verdict

The safe full-exit floor changes **none** of the thirteen `td=12` U1
first-trunk menu rows.  All ten dirty rows have simple nonzero root
multiplicities and positive **integral** defects; the other three rows have no
charged nonzero direction.  The four P1-shaped dirty rows therefore retain
charges `8,8,8,8`, budgets `9,8,6,2`, and exactly the first two still fit.

The reviewed LL-1 residue book does change.  Across all 72 frozen transition
records, representing 16 unique dirty cells, exactly four cells have a
nonintegral nonzero-direction defect whose floor rises:

```text
(dp,dq,nu) = (17,5,2), (51,15,7), (85,25,12), (119,35,17).
```

In every case `l=4`, `X=17`, `kbar=5`, the one nonzero root has multiplicity
`3`, and

```text
delta = 17/3 - 5 = 2/3,       ceil(delta)=1,
L_safe(delta)=ceil(2 delta)=2.
```

Keeping each epsilon/zero-direction charge separate, the first three total
cell floors rise `2 -> 3`, and the epsilon-free `(119,35)` floor rises
`1 -> 2`.  Reweighting the already frozen LL-1 graph reduces its
`ALIVE`/`ALIVE_FRAGILE` inventory from 13 rows to 7.  Six legacy alive rows
are no longer in-budget.  The base `(2/7,7)` survives only at accumulated
charge `4` (equality-fragile), not at the former slack row of charge `3`.

The sampled reviewed td7 route is unchanged: its nonintegral full-direction
defects are `1/2` and `1/3`, both of which still have safe floor `1`.

This repricing is licensed only when the consumer charges the **full actual
exit set** of a direction.  A generic MFE selected representative, or one
arbitrary raywise flag, remains priced by its original one-witness floor and
is **UNTYPED for this upgrade**.  The safe floor is a lower bound, not an
attainment formula.

## 1. Exact perimeter

The load-bearing corrected floor and its type boundary are in:

```text
05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84
  xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md
```

The exact `td=12` pre-cutoff frames and independent menu review are:

```text
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271
  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f
  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
6f214a755e1d589bacf155195e687799b8f793706a5ca2fa7cb508c00a038d7e
  cases/m2_td12_u1_trunk_consumer_grok46_20260829/trunk_consumer.py
```

The reviewed LL-1 report, hostile arithmetic review, and frozen R3 book are:

```text
f501bf91815aa7862fe36f665ea7ec7d379bc4c5f26502c4a0273bf97eff9aa6
  xmodel/landing-ledger-ll1-r3-provenance-repair-fable5-20260829.md
8f56d1e4f2b159bbddf170010d9ac85337639e00e3b4ea537e0cc218a7b9bcf0
  xmodel/landing-ledger-ll1-r2-hostile-review-grok46-20260829.md
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e
  cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json
```

The td7 route control and MFE type boundary are:

```text
dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90
  xmodel/sol-h5a.md
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14
  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5259d77766cc8179f3d1248ee0c1320daf411f04758487d2e94e216bb
  xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
```

No legacy enumerator was run or edited.  The checker reconstructs the td12
rows from closed formulas, reads the hash-pinned LL-1 JSON as frozen data, and
reweights only its emitted graph:

```text
6ca098b8145f091884d7f11ab1d6aac49dadaab91a6ba7ed18f7c022efce99b5
  cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py
```

Its canonical stdout SHA-256 is
`4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011`
under both ordinary Python and `python3 -O`.

## 2. Typed pricing rule

For one nonzero up direction of reduced multiplicity `m`, put

```text
delta = X/m - kbar > 0.
```

The legacy AF2 summand is `max(1,ceil(delta))` for one selected cv witness.
The audited arity theorem says something stronger but differently typed.  If
we take **all distinct actual cv flags below that direction**, their total
weight is at least

```text
L_safe(delta) = delta          if delta is a positive integer,
                ceil(2 delta)  if delta is nonintegral.
```

For separate nonzero direction-orbits, their full sets are disjoint by the
first-separation/no-remerging partition, so the local full-direction floors
may be summed.  Along a trunk, every such set is assigned to its first exit
vertex, so sets charged at different trunk vertices are also disjoint.  This
is the full-actual-set consumer used below.

The following objects must remain distinct.

| object | treatment in this sweep |
|---|---|
| full actual exit set below a nonzero up direction | apply `L_safe` |
| one MFE-selected witness for a direction | keep legacy raywise floor; safe-floor upgrade is `UNTYPED` |
| one arbitrary actual ray/flag | keep its individual corrected-9.3 floor |
| epsilon/zero direction | retain its separately derived P0 floor; not repriced here |
| pole or merge arrival | retain its independently reviewed price; never infer a nonzero exit |
| `L_safe` value | lower bound only; no attainment or equality claim |

This distinction is essential at `delta=2/3`: the full exit set costs at
least two, but two actual flags of weight one each are compatible with a
single selected witness of weight one.  Repricing a representative as two
would be invalid.

## 3. Exhaustive td12 thirteen-edge menu

For every dirty menu row, `l=2`, `lex=0`, `Sm=k`, and every nonzero root has
multiplicity one.  The closed formulas are

```text
dp = eps + nu(k+2),             dq = 1 + nu(k+1),
E  = 2dq-dp,                    kbar = 9dq/E,
X  = 9dp/E,                     delta_j = X-kbar.
```

The complete reconstruction is:

| eps | k | nu | E | kbar | X | each nonzero delta | old NE | safe NE | zero kept | total old -> safe |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 7  | 9  | 15 | 21 | 6 | 6 | 6 | 0 | 6 -> 6 |
| 0 | 1 | 25 | 27 | 17 | 25 | 8 | 8 | 8 | 0 | 8 -> 8 |
| 0 | 2 | 5  | 12 | 12 | 15 | 3 | 6 | 6 | 0 | 6 -> 6 |
| 0 | 2 | 17 | 36 | 13 | 17 | 4 | 8 | 8 | 0 | 8 -> 8 |
| 0 | 4 | 13 | 54 | 11 | 13 | 2 | 8 | 8 | 0 | 8 -> 8 |
| 0 | 8 | 11 | 90 | 10 | 11 | 1 | 8 | 8 | 0 | 8 -> 8 |
| 1 | 1 | 2  | 3  | 15 | 21 | 6 | 6 | 6 | 3 | 9 -> 9 |
| 1 | 1 | 8  | 9  | 17 | 25 | 8 | 8 | 8 | 1 | 9 -> 9 |
| 1 | 2 | 4  | 9  | 13 | 17 | 4 | 8 | 8 | 1 | 9 -> 9 |
| 1 | 4 | 2  | 9  | 11 | 13 | 2 | 8 | 8 | 1 | 9 -> 9 |

Thus there is no nonintegral nonzero defect in the dirty menu and no floor
increase.  The two clean-neutral rows have no charged nonzero exit; the
pure-epsilon row has only its zero-direction floor `9`.  They are `N/A`, not
untyped failures.  All ten dirty rows satisfy the recorded N1 and R1.0 gcd
filters, so there is no hidden filter-induced untyped row.

Downstream: the four P1-shaped rows remain

```text
(nu,k,charge,budget) = (25,1,8,9), (17,2,8,8),
                       (13,4,8,6), (11,8,8,2).
```

Exactly the first two fit, as before.  The later exact-charge results `8` for
the `nu=25` direction and `4+4=8` for the `nu=17` sibling are consistent with
this sweep but are not used to manufacture equality for the other rows.

## 4. LL-1: every changed nonintegral full-direction floor

The frozen LL-1 graph has 72 transition records and 16 unique dirty cells.
Exact replay finds precisely these four increases and no others:

| cell `(dp,dq)@nu` | eps | nonzero mult | delta | NE old -> safe | zero kept | cell total old -> safe | immediate effect |
|---|---:|---:|---:|---:|---:|---:|---|
| `(17,5)@2` | 3 | 3 | 2/3 | 1 -> 2 | 1 | 2 -> 3 | `M'=1`; remains MP2-dead |
| `(51,15)@7` | 2 | 3 | 2/3 | 1 -> 2 | 1 | 2 -> 3 | old charge-4 target was already DEAD; new charge 5 is pruned |
| `(85,25)@12` | 1 | 3 | 2/3 | 1 -> 2 | 1 | 2 -> 3 | removes fragile `(2/5,5,4)` row |
| `(119,35)@17` | 0 | 3 | 2/3 | 1 -> 2 | 0 | 1 -> 2 | former `(2/7,7,3)` slack row moves to equality charge 4 |

For the epsilon rows, the retained zero summands are, respectively,
`ceil(1/3)=1`, `ceil(1/2)=1`, and `ceil(1)=1`.  They are not folded into
`delta=2/3` and are not evidence of full-exit attainment.

### 4.1 Reweighted verdicts

Because every changed edge cost only increases, no newly affordable edge can
appear.  Pooling the frozen transition templates by reduced source `(w,M)`
is exact for the new in-budget graph: any edge affordable from a repriced
source was already emitted from the same source at an equal-or-lower legacy
charge.  Replaying to the global `psi>=1` cap `sum lambda<=4` gives 17 states
and these seven surviving terminal rows:

```text
ALIVE:          (2/3,3,2), (2/5,5,3)
ALIVE_FRAGILE:  (3/4,4,2), (2/7,7,4), (2/9,9,4),
                (3/10,10,4), (3/8,8,4).
```

The following six legacy alive rows disappear from the in-budget book:

```text
(2/7,7,3)   ALIVE
(1/2,2,4)   ALIVE_FRAGILE
(1/2,4,4)   ALIVE_FRAGILE
(2/5,5,4)   ALIVE_FRAGILE
(2/11,11,4) ALIVE_FRAGILE
(2/13,13,4) ALIVE_FRAGILE.
```

There are no new alive rows.  `(2/7,7,4)` was already present through the
other boundary route, so the base survives but loses the distinct slack-1
state and all formerly in-budget descendants of that slack.  This is a
verdict change at the frozen LL-1 reduced-superset scope; it is not a landing,
realizability, or JC2 statement.  Canonical LL-1 files should be quarantined
from numerical consumption until a reviewed replacement incorporates these
four floors.

## 5. Small td7 and MFE controls

The reviewed td7 discriminating route gives the following full-direction
checks:

| cell | nonzero delta | old -> safe nonzero floor | zero kept |
|---|---:|---:|---:|
| `(21,15)@nu7` | 2 | 2 -> 2 | 0 |
| `(35,15)@nu7` | 1/2 | 1 -> 1 | 0 |
| `(63,9)@nu4` | 1/3 | 1 -> 1 | 1 |

Hence its displayed budget equality remains `2+1+2=5`; this sampled td7
route has no verdict change.

For MFE, the selected-exit theorem assigns one witness `H(F,d)` to each
selected direction-orbit and proves only

```text
wt(H(F,d)) >= price(F,d).
```

It explicitly does not identify that representative set with every actual cv
flag farther down a direction.  Therefore a row carrying only
`price(F,d)=ceil(delta)` and a representative witness is **UNTYPED** for
replacement by `ceil(2delta)`.  The repair is not to change that row, but to
add a full-exit-set field and prove the corresponding actual flags are all
inserted, pairwise distinctly, in the global Corollary-7.1 budget.  The td12
and LL-1 calculations above use that explicit full-direction interpretation;
the generic MFE theorem remains unchanged.

## 6. Exclusions and review risks

1. A reviewer should check the full-set upgrade across successive LL-1 trunk
   vertices against the first-separation partition.  If a consumer retains
   only MFE representatives, the four increases must be withdrawn for that
   consumer and marked `UNTYPED`, not silently retained.
2. Zero directions, pure-epsilon rows, pole entries, and merge arrivals are
   deliberately outside the safe nonzero-direction rule.
3. `L_safe` is a lower floor.  No row is declared attained merely because its
   new floor equals its budget.
4. The LL-1 graph replay changes only the hash-pinned reduced residue book.
   It does not rerun the legacy generator, strengthen its completeness
   theorem, or assert source realization.
5. The exhaustive claims are limited to the mandated `td=12` thirteen-edge
   menu and the frozen LL-1 residue graph.  The td7 calculation is the stated
   verify-only route sample; it is not a reprice of all 17 td7 cells.

No canonical file, legacy engine, web resource, AWS resource, or heavy local
computation was used or changed.

*End of sealed report body.*

---

Report-body bytes: `12149` (the complete file before the separator above).  
Report-body SHA-256:
`2d873e680cfdc464fc0bc707aec5c072ba9310ee0600a98786643c0ca8c93ac5`.
