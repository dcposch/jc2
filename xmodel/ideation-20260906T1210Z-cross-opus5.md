# Cross-review 20260906T1210Z — Opus5

All 9 charged inputs SHA-256 verified against `charged-inputs.list`, zero
mismatches. No live cross report/log read. No AWS/heavy CAS/jc2-lean/ledger/
adapter edit/external post. Tiny exact desk checks only (support functionals).
Round EXPEDITED/DEGRADED; this report is late against the 12:31 backstop —
record cadence debt, not completion.

## 1. Endpoint disagreement — individual verdict: MISTAKEN ENDPOINT

**My own blind claim is wrong. Astra and Sol are right: Theorem 5.1 covers all
three Prop 4.2 cases.** This is decidable from the charged primary alone, with
no appeal to [1] and no majority.

Prop 4.2 (`txt:349-351`) case (1): `N(P)={(0,0),(1,1),(6,16),(6,18),(0,12)}`,
`N(Q)={(0,0),(1,0),(9,24),(9,27),(0,18)}`. Thm 5.1(2) (`txt:661`) requires
`en_{3,-1}(P)=st_{1,0}(P)=(6,16)` and `st_{-1,1}(P)=en_{1,0}(P)=(6,18)`.

The paper defines no `st`/`en`; it inherits them (`txt:86`). But Thm 5.1(2)
**pins the orientation internally**. The `(1,0)`-face of `N(P)` is `i=6`, i.e.
`{(6,16),(6,17),(6,18)}`; the theorem assigns `st=(6,16)`, `en=(6,18)`, so the
face is traversed in `+ (0,1)`, i.e. in direction `ρ^⊥=(-ρ2,ρ1)` for `ρ=(1,0)`
— counterclockwise, interior on the left. Corroboration: `ρ=(3,-1)` gives `ρ^⊥=(1,3)`, face `{(1,1),(6,16)}` traversed
`(1,1)→(6,16)`, so `en=(6,16)` ✓; and `txt:356` prints `en_{-1,3}(F)=(16,6)`,
its `x↔y` mirror. One convention fits all three printed data.

Apply it to `ρ=(-1,1)`, `ρ^⊥=(-1,-1)`. In case (1), `v_{-1,1}=-i+j` is `12` at
both `(6,18)` and `(0,12)` — the tie I flagged is real — so the face is the
segment `(6,18)→(0,12)`, traversed in `(-1,-1)`. Hence
`st_{-1,1}(P)=(6,18)`, `en_{-1,1}(P)=(0,12)`. Thm 5.1(2) is **satisfied**.
Same for `Q`: `-9+27=-0+18=18`, face `(9,27)→(0,18)`, `st_{-1,1}(Q)=(9,27)` ✓
Thm 5.1(3). Cases (2) (`(0,6)`: `6<12`) and (3) give the vertex `st=en=(6,18)` ✓. My blind took `st` as the lexicographically-earlier point of the tie set —
intuitive lexicography, not the paper's `ρ^⊥` order.

Consequence: **no missing reduction, no Cor 5.7 manoeuvre needed for 99, and no
gap-note to the authors.** My blind §2 conclusions (b) and Card A are
withdrawn; `OPEN[PROP-4.2-CASE-1]` is **closed as operator error**. Surviving
and not withdrawn: Prop 4.2 and Cor 5.7 are each cited exactly once in v1,
Cor 5.7's polygons are the `(9,27)`/108 shape, and (5.9) is reproduced by an
independent char-0 `eliminate` (three concordant replays, not repeated here).

## 2. Degree-99 status — no upgrade, no over-filtering

`APPLIES_AS_EXTERNAL_THEOREM` via the **robust** bound: no counterexample with
`max{deg P,deg Q} < 108` (`txt:64-67`). That alone closes actual 99/66, and is
normalization-safe since degree-reducing normalization cannot raise the max. Do **not** implement blanket filtering of
every non-listed pair under Theorem 2.1's `<125` list: target addition sends a
hypothetical `(72,108)` to `(108,108)`, so the list is a statement about
representatives. Fable's "read it as normalised representative" is the right
repair but is stated as if it licenses the `108–124` bin; that bin stays
conditional, as its own Card A bin name concedes. Trust boundary unchanged: [1],[2],[3],[5],[6],[12] unread.

The complete physical-J source has actual `F99,G66` and genuine `ZjJ0-1`, so a
point is a counterexample **independently of source-to-chart necessity**; the
external theorem therefore empties that complete chart. Full-ideal unit
**does not** imply the 466-row subset is unit — the old classical99 Opus gate
prediction is rejected by all four blinds and by me. An independently checked
subset unit would remain a valid internal certificate at its own scope. Do not
apply the absolute polynomial-degree theorem to the `.73` K7 `J=x^k` charts:
different target, different ring. `24,063→90→64` stays an arithmetic survivor
population; "64 externally open cases" is unsupported.

## 3. Deduplicated cards

All four blinds proposed the same D108 card. One card, one dependency note.

**Card 1 — D108 → GGHV `(8,28)` interface. `KNOWN` ingredients, `NEW` proposed
composition; NO MAP PROVED.** Known: our literal source top `h=(X+W)^8W^28`,
`F_top=h^3`, `G_top=h^2`; GGHV's two 108 rows `(8,28),(m,n)=(3,2)` (open,
`[P,Q]=x^2`) and `(9,27),(2,3)` (killed by Cor 5.7); `d0·st_{1,0}(R)=(8,28)
=4(2,7)` at `txt:166`. New only as a composition. **Strongest attack (mine, on
my own card):** `(8,28)` is a corner of a polygon in `L^(1)` after
*non-polynomial* automorphisms `φ1,φ2,φ3` (`txt:650-652`), whereas ours is a
literal source top — matching integers across those categories is the
flag/place/series conflation FALLACY-v2 forbids; and `m/n` multiplicity match
proves nothing about normalization. **Cheapest concrete test:** write the ring
map `L^(1) → our chart` (field, generator order, `x`-invertibility) and check
one invariant — their `[P,Q]=x^2` against our Jacobian normalization — before
any support work. **Stop:** at the first unmapped hypothesis, or on
normalization mismatch; mismatch kills the port, not D108. No solve, no
99-code port by variable-name analogy.

**Card 2 — K16.** `NO_NEW_MECHANISM`. Any next attack must cover all `m` and
both coefficient factors including the `b=0` boundary; the norm model carries
the same differential condition and adds no equation. **Stop norm-only
rewrites.** `(T)` stays `t≤8`.

## 4. Model roles — by surviving work and correction cost

By output, not votes. Astra and Sol both got the endpoint question right and ran
their own exact replays; Astra also caught two printed slips ((5.2) denominator,
`x-D2/3`). My blind produced one new internal item (the (5.9) replay) and one
false alarm that consumed this round's adjudication budget — net negative; keep
me on bounded source extraction *with* a mandatory convention check before any
"gap" claim. Fable's mathematical body is criticizable but not promotable by receipt
(workflow QUARANTINED for an invalid `delta` value); it did not read the proof
bodies or the three gate bodies, and it overreaches on arbitrary-degree
filtering, "smaller 108 supports", campaign novelty, sweep-stopping and `.73`
classification — do not silently inherit any of those. Its conditional
normalization chain and Sol's literal-theorem reading both stay **scoped**, not
merged. Recorded: root skimmed Fable's terminal failure-log math summary ~12:18
after sealing its own blind; no peer saw it.

## 5. Route ranking (corrected) and systems

1. D108 interface **map**, desk-scale, Card 1 stop rules. 2. All-degree
realizability obstruction (boundary-tree/td backbone). 3. Census→frontier
reconciliation carrying per-row external coverage. 4. K16 at `t≤8` scope only.
Dropped from my blind ranking: the Prop 4.2 case (1) desk check (dead).

**Software (one bounded item):** a per-theorem coverage table storing
normalization (target, `K[x,y]` vs `L^(1)`, which degrees are actual), printed
case coverage and unread deps, answering "is `(n,m)` closed, by which
proposition". Seed with GGHV p.3's 10 rows. **Campaign systems: `NO_UPGRADE`** — do not add another
canonical ledger; the failure was pre-launch frontier reconciliation, not index
structure. No changes to protected worker custody; `.63/.73` caps and `.103`
partials retained.

## 6. Directions

**STOP:** new 99 frontier solves/expansions/witness campaigns permanently;
dense 99 expansions; norm-only K16 rewrites; repeat web sweeps this round.
**REDESIGN:** avenue 1 into the theorem/source interface; D108 around Card 1
before any port. **CONTINUE:** D108 as the live case, boundary-tree backbone,
K16 at `t≤8`, already-launched capped solves under existing custody.

`OPEN[D108-CHART-IDENTIFICATION]`, `OPEN[K16-UNIFORM-m]`,
`OPEN[DEPENDENCY-PRIMARY-UNREAD]` typed open. No JC2 proof, no counterexample,
no new exclusion, no exit-price assertion in this report.

<!-- BODY-END -->
