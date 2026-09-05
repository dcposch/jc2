# Hostile gate: does the promoted whole-tree screen close degree-wide `(99,66)` by citation?

Lane `n1-screen-gate-grok46-20260905`. Charged: Fable Q2 (17(eeeeee)(A)), the eight-skeleton
enumeration, batch-2 remainder, frozen Moh enumerator, Moh 1983 PDF, FALLACY-v2, and the
centre-gate screen (`rerun_screens.py` / `opus5_probe.Tree` / `moh_skeleton_full_frozen.py`).
No ledger, `jc2-lean`, or `ideation-*` file was edited. Batch-3 was receipt-only.

## Verdict first

**DEGREE-WIDE `(99,66)` CLOSED BY CITATION. NOTIFY-WORTHY.**

The desk claim reproduces on the charged driver, imports unmodified. Exactly eight
`(1)`–`(13)`-admissible skeletons at `(n,m)=(99,66)`. Seven die under the promoted
whole-tree screen; the eighth is the printed Moh row and is already dead by the banked
configuration trichotomy.

| id | first killing screen | exact condition | source | claim |
|---|---|---|---|---|
| S1 | `PARTITION` (`danger=False`) | forced major zero sibling `b=13` at `D_2` fails `(12)∨(13)` | Moh Thm p.200(4) + Prop. 5.5 / p.201(12)(13); 17(r) | **PASS** |
| S4 | `PARTITION` | forced major zero siblings `b=2` and `b=13` fail `(12)∨(13)` | same | **PASS** |
| S5 | `PARTITION` | forced major zero sibling `b=7` fails `(12)∨(13)` | same | **PASS** |
| S6 | `PARTITION` | forced major zero sibling `b=4` fails `(12)∨(13)` | same | **PASS** |
| S2 | `UNGATED` Prop. 5.6 (also `GATED`) | `p.200(4)` forces the major zero sibling `b=5`, which is S3’s selected chain; empty-free still-centred zero leaf at `D_1` | Prop. 5.6 p.188; Lemma 5.3 top-chart flag; 17(r)+17(hh) | **PASS** |
| S3 | `UNGATED` Prop. 5.6 (also `GATED`) | selected `V_2=5` is the `(11)`-branch zero factor; empty-free still-centred `D_1` leaf | Prop. 5.6 p.188; p.201 `(11)` remark; 17(r)+17(hh) | **PASS** |
| S7 | `UNGATED` Prop. 5.6 (also `GATED`) | selected `V_2=8` is the `(11)`-branch zero factor; empty-free still-centred `D_1` leaf | same | **PASS** |
| S8 | screen **SURVIVES**; dead by chart | unique row whose `D_2` zero factor is minor (`b=0 ≰ 3/2`) | 17(pppp) B `δ=2[2,1]`; 17(tttt) C `δ=5/2[1,1,1]`; 17(bbbbbb) A unsplit | **PASS** |

**Citation list (load-bearing):** 17(r) + 17(hh) + 17(pppp) + 17(tttt) + 17(bbbbbb).

17(ll) is a MEASURED re-base of the same operative screen (`C_FULL_TREE_POLYNOMIAL_ODE`,
“`s=3` EXACT at `n≤100` (Moh’s six)”), not a third necessary condition. It corroborates
the table (only S8 of the eight `s=3` rows can be among Moh’s six) and is not required
to close any of the seven.

**Scope, not a send-to-chart.** Prop. 5.6’s printed conclusion is
`k[f,g]=k[x,y]` **or** a simultaneous degree-reducing automorphism. The N1 theorem
that this citation closes is Moh’s search under the p.200-bottom condition (3)
(degrees not simultaneously reducible) — the published open case of the `≤100`
induction. It is **not** a proof that every simultaneously-reducible `(99,66)` pair
is impossible without the rest of `≤100`. Moh `≤100` itself is **not** closed: the
operative screen still leaves 14 excess `u_s=1` rows
`((90,60)×4,(96,64)×4,(96,72)×6)`, `OPEN[MOH-PROGRAM-ARTIFACT]` (17(hh)/17(ll)).

Batch-3 joint charts are a redundant instrument cross-check, not the critical path.
Receipt still `initial_status=RUNNING` with no `final_status`; its `.md` was not opened.

No new exit-price assertion; no `charge_basis` line.

## 0. Custody

Receipt `xmodel/n1-screen-gate-grok46-20260905.run.v2` was parsed with `awk` pairing
each `charged_input_<i>_sha256=` with `charged_input_<i>_basename=`, pointed at
`/tmp/jc2-lane.cTUqgC/inputs`, and checked with `sha256sum -c`. **9/9 OK**. No digest
was retyped. Frozen basis `d7ff4ceaaeaa508deec3f1bd7a906a8364fbaba7`.

The three import targets used by the screen are byte-identical to the frozen inputs
(`cmp` and matching SHA-256):

```text
1150ec4416bb690a2fcf4ed3b0983f389d2c400e5fefe8cda4612b55e1cf9372  rerun_screens.py
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  opus5_probe.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full_frozen.py
```

Drivers and JSON under `box/n1gate-20260905/`; `artifacts.sha256` checks 4/4.

Foreground only, `taskset -c 0,1,2`, exact `Fraction` arithmetic, enumerator and
`Tree` imported unmodified. The `ok()` / window call is the same as
`rerun_screens.run_one`.

Moh printed page `p` is PDF page `p−139`. Prop. 5.6 was read from
`box/centre-gate-20260903/moh_p188.png` (statement), p.190 (affine removal),
p.200 (Theorem (4)–(7)), p.201 (`(8)`–`(13)` and the `(11)` remark).

## 1. Enumeration: eight skeletons, matched S1..S8

`moh_skeleton_full_frozen.census(99, Kmin=2, full=True)`, filter `m=66`, sort key
`(M_2,V_3,V_2)` as in 17(cccccc). Count **8**. Every row has `s=3`,
`M_1=−66`, `M_3=97=n−2`, `d=(99,33,11,1)`, `windows_ok=true`, `full_ok=true`.
Here `u_s=d_s−V_s=11−V_3` and `v_s=V_3` (not `Skel.u`).

| id | `M=(M_1,M_2,M_3)` | `d` | `V=(V_2,V_3)` | `(u_s,v_s)` | `δ=(δ_1,δ_2,δ_3)` | `A_1,A_2` | `(10)` | `(11)` | `any10` |
|---|---|---|---|---|---|---|---|---|---|
| S1 | `(−66,−22,97)` | `(99,33,11,1)` | `(1,9)` | `(2,9)` | `(2/7, 3/14, −1)` | `1,14` | T | F | T |
| S2 | `(−66,22,97)` | same | `(1,7)` | `(4,7)` | `(11/16, 9/16, −1)` | `1,16` | T | F | T |
| S3 | `(−66,22,97)` | same | `(5,7)` | `(4,7)` | `(7/12, 9/16, −1)` | `3,16` | F | T | F |
| S4 | `(−66,22,97)` | same | `(1,8)` | `(3,8)` | `(6/11, 4/11, −1)` | `1,11` | T | F | T |
| S5 | `(−66,22,97)` | same | `(1,10)` | `(1,10)` | `(8/23, 2/23, −1)` | `1,23` | T | F | T |
| S6 | `(−66,55,97)` | same | `(2,10)` | `(1,10)` | `(14/39, 1/13, −1)` | `3,13` | T | F | T |
| S7 | `(−66,77,97)` | same | `(8,7)` | `(4,7)` | `(8/13, 7/13, −1)` | `1,13` | F | T | F |
| S8 | `(−66,77,97)` | same | `(8,8)` | `(3,8)` | `(4/9, 1/3, −1)` | `3,3` | T | F | T |

This is the charged 17(cccccc) table, including S8 = Moh p.202 printed `(99,66)` row
`MOH_TABLE` entry `(99,66,[77,97],{3:8,2:8})`. S3 and S7 are the only `(11)`-only
rows (`any10=False`), i.e. the printed Prop. 5.6 remark’s numerical shadow
(`Skel.any10`).

## 2. Screen replay (charged `Tree.ok`, same flags as `rerun_screens.py`)

Window test (all eight): `d_s=11 > V_s > 11/2`, so `V_s∈{7,8,9,10}`. All pass.

| id | PARTITION | PARTITION_ODE | GATED | UNGATED | UNGATED_ODE | POLY_ODE | PARTITION witness |
|---|---|---|---|---|---|---|---|
| S1 | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD | — |
| S2 | SURV | SURV | DEAD | DEAD | DEAD | DEAD | nonzero, `b=5`, orbits `[1]` |
| S3 | SURV | SURV | DEAD | DEAD | DEAD | DEAD | zero, `b=5`, orbits `[1]` |
| S4 | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD | — |
| S5 | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD | — |
| S6 | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD | — |
| S7 | SURV | SURV | DEAD | DEAD | DEAD | DEAD | zero, `b=8`, orbits `[1]` |
| S8 | SURV | SURV | SURV | SURV | SURV | SURV | nonzero, `b=0`, orbits `[8]` |

`CLAIM_MATCH True` against Fable’s five-column table. ODE, passport, recenter/`POLY`
are **not load-bearing**: every kill already fires on bare `PARTITION` or bare
`UNGATED`, and S8 survives the strongest listed column
(`POLY_ODE` = `C_FULL_TREE_POLYNOMIAL_ODE`).

Fable’s label `UNGATED_ODE = C_FULL_TREE_POLYNOMIAL_ODE` is a **misidentification**.
`rerun_screens.UNGATED_ODE` is `danger=True, gate=False, ode=True` with
`recenter=False` (`C_FULL_TREE_ODE`). POLY is `recenter=True` (17(gg), promoted
with 17(hh)). Harmless here: the two columns agree on all eight rows.

## 3. Exact kill, per skeleton

All eight have a unique tree node `j=2` (`s=3`). At that node
`P=V_3·d_2/d_3`, `Q=V_3·(n−M_2)/d_3`, `lo=d_2/(n−M_2)`, and the zero-factor
multiplicity runs `b ≡ P (mod A_2)`, `0≤b≤P`. p.200(4) requires every
**major** factor (`V>lo`) to extend, including the zero factor whether or not
the selected path uses it (`opus5_probe.py` comment at the `zmaj and child(b,True,None)`
test). `(12)∨(13)` is Prop. 5.5 at `r=2`, applied to every `D_1` leaf of that DP.

### 3.1 S1, S4, S5, S6 — gap-free (`PARTITION`), not Prop. 5.6

Each selected path satisfies `(1)`–`(13)` (enumerator). Each dies because the
**only** `b` that can host the selected `V_2` as a nonzero orbit has a **major
zero sibling** whose own `D_1` fails `(12)∨(13)`. Independent `Skel` replay
(same `M`, sibling `V_2=b`):

| id | `A_2,P,Q,lo` | hosting `b` | sibling `V_2=b` | sibling `A_1` | sibling `(12)∨(13)` | selected `(12)∨(13)` |
|---|---|---|---|---|---|---|
| S1 | `14,27,99,3/11` | `13` | `13` | `16` | **False** | True |
| S4 | `11,24,56,3/7` | `2` and `13` | `2`, `13` | `9`, `8` | **False**, **False** | True |
| S5 | `23,30,70,3/7` | `7` | `7` | `17` | **False** | True |
| S6 | `13,30,40,3/4` | `4` | `4` | `19` | **False** | True |

No other `b` hosts the selected `V_2`. So p.200(4) (“if the number of roots of
`g` in `E_i` is above threshold, the tower extends to `E_i`”) cannot be satisfied
for that `V`-assignment: the forced major zero packet has no legal `D_1`.
This is the gap-free whole-tree DP of 17(r) (`danger=False`; Prop. 5.6 off).
`Tree.why` is the generic `(j=2, "no admissible (b, orbit multiset)", A, P, Q, lo)`.

**Promoted? Necessary?** Yes. 17(r) PROMOTED the local whole-major-tree obligation
as PROVED-IN-SOURCE from Prop. 5.3 / p.200(4) (universal in the covering, not a
privileged factor) and `C_FULL_TREE` as a named derived necessary filter. The
`(12)∨(13)` test on a `D_1` leaf is printed Prop. 5.5 / p.201. These four kills
do not use Prop. 5.6, ODE, passport, recenter, Xu, or 17(hh). They are Jacobian-tower
conditions, not minimality conditions.

### 3.2 S3, S7 — selected `(11)`-zero chain, Prop. 5.6, empty free set

S3: `A_2=16, P=21, Q=49, lo=3/7`, selected `V_2=5=b`, `zmaj=True`,
`any10=False`, `(11)=True`. PARTITION witness: mode `zero`, `b=5`, leftover
orbit `[1]`. Free set of the selected chain: `∅`. Incoming `danger=True`
(Lemma 5.3: the selected tower begins as a zero factor). Ungated Prop. 5.6
kills the `D_1` zero leaf. Gated does too (`not free_exponents`).

S7: `A_2=13, P=21, Q=14, lo=3/2`, selected `V_2=8=b`, same pattern, free `∅`.

This is the printed p.201 sentence: “the situation indicated by the equation
`(11)` cannot always happen as established by Proposition 5.6.” Prop. 5.6
(p.188, image-read): if the unique `π`-root in `D_1` is `σ_1=π t^{δ_1}`, then
either `k[x,y]=k[T_1^ψ,g]=k[f,g]` or an automorphism reduces the degrees of
`f`, `g` and `T_1^ψ` simultaneously. Empty free set + p.190 (`y↦y−ax−b`
removes `t^{-1}` and `t^0`; the only integral centre exponents below `δ_1`
in this search) gives `σ_1=π t^{δ_1}` **without** LEMMA[ZERO-FACTOR-CENTRE].

### 3.3 S2 — forced-zero *sibling*, not an all-zero selected chain

**Fable’s prose is wrong for S2; the screen column is right.**

PARTITION witness: mode **`nonzero`**, `b=5`, orbits `[1]`, selected free `{5/8}`.
`(10)=True`, `(11)=False`, `any10=True`. The selected chain is a nonzero factor
and would *clear* danger. The kill is p.200(4) on the **sibling**: `b=5` is
major (`5>3/7`), and that zero child is an empty-free still-centred zero leaf
(`danger` still set from `D_s`). Ungated *and gated* Prop. 5.6 skip this `b`;
it is the only `b` that hosts `V_2=1`.

The sibling data `(M_2,V_3,V_2)=(22,7,5)` **is S3**. S2 dies because a
`(99,66)` pair with S2’s selected `V` would have to carry S3 as a major zero
packet at the same `D_2`, and S3 is Prop. 5.6-forbidden.

17(hh) explicitly includes “forced-zero siblings, any multiplicity `b`”.
`OPEN[NONZERO-PARENT-TWIST]` is not used (`C_r=0` on the killed child).

### 3.4 S8 — unique screen survivor

`A_2=3, P=24, Q=16, lo=3/2`. The residue `b=P mod A_2=0` is **not major**
(`0 ≰ 3/2`). No forced major zero sibling. Selected `V_2=8` is a single
nonzero orbit of size 8; incoming `danger=True` is cleared on that child.
Witness (every column): mode `nonzero`, `b=0`, orbits `[8]`. This is Moh’s
printed row. It is the unique `(99,66)` skeleton with `P≡0 (mod A_2)` and
that residue below the major threshold.

## 4. Hostile: is each cited screen promoted and necessary?

FALLACY-v2: a citation kill is valid only if the cited condition is promoted
**and** necessary **and** the skeleton actually violates it.

### 4.1 Gap-free p.200(4) (S1, S4, S5, S6)

| test | result |
|---|---|
| Promoted? | **Yes.** 17(r) PROMOTED, different-model gate. |
| Necessary on a Jacobian pair with this characteristic data? | **Yes.** Prop. 5.3’s hypothesis is a universal conditional on multiplicity; p.200(4) is universal in the covering `E_i`. `(12)∨(13)` is Prop. 5.5 at every tower that reaches `D_1`. |
| Skeleton actually violates it? | **Yes.** §3.1: the unique hosting `b` has a major zero sibling with `(12)∨(13)` false (`Skel.full_ok=False` on that sibling). |
| Provisional / convention / passport / ODE / POLY / Xu? | **No.** Bare `PARTITION`. |

**Closed by citation. Do not send to a joint chart.**

### 4.2 Ungated Prop. 5.6 / 17(hh) (S2, S3, S7)

**Is “ungated Prop. 5.6” a promoted necessary condition on a Keller pair, or does it still carry a gate?**

Split the question.

**(a) Promotion of the lemma.** 17(cc) was PROVISIONAL. 17(hh) is **PROMOTED**
(GPT-5.5 gate, proof correction: full ancestor Puiseux Galois, general `L`;
multiplicity `b` irrelevant). LEMMA[ZERO-FACTOR-CENTRE]: on a still-centred
all-zero major chain, every non-integer centre coefficient in `(δ_r,δ_{r−1})`
vanishes; after p.190, `σ_1=π t^{δ_1}`. 17(u)’s gap-free/gapped split
collapses; ungated `C_FULL_TREE` is the operative tree screen; the POLY column
is promoted with it.

**(b) Remaining gate on the lemma.** 17(hh) keeps `OPEN[NONZERO-PARENT-TWIST]`:
a nonzero parent factor may carry a Galois-legal twist `λ C^2 W^2`. That gate
is **correctly separated** and **not used** on S2/S3/S7: every Prop. 5.6 fire
here is on a zero child.

**(c) Is ungating *load-bearing* on these three rows?** **No.** The relevant
zero chains already have empty free sets (S3 and S7 selected; S2’s zero
sibling). Gated Prop. 5.6 (Opus §7.4 repair: kill only when `free_exponents`
is empty) kills all three. For empty free sets, `σ_1=π t^{δ_1}` follows from
Def. 1.3 + p.190 without the lemma. 17(hh) is the promotion that made ungated
`C_FULL_TREE` the operative screen; on *these* three skeletons the weaker
gated reading already kills. That is a strengthening of the citation, not a
hole.

**(d) Necessity on a Keller pair.** Prop. 5.6 does **not** say “no pair of
these degrees exists”. It says: `σ_1=π t^{δ_1}` ⇒ automorphism **or**
simultaneous degree reduction. For a pair satisfying Moh’s p.200-bottom (3)
(the search for a smallest Jacobian counterexample) both alternatives are
forbidden, so the chain cannot occur. That is the N1 theorem (published open
case of `≤100`). For an *unrestricted* “no polynomial pair of degrees
`(99,66)` with these data, including reducible ones”, Prop. 5.6 is not a
degree-preserving obstruction; those three skeletons would then need charts
or the rest of the `≤100` induction. The campaign’s degree-wide `(99,66)`
statement is the former. Fable already typed the latter as the reason the
theorem to state for Moh’s bound is `≤100`, not `(99,66)` alone.

**(e) Fable over-cite.** Citing 17(ll) as a necessary condition is inaccurate
(MEASURED census). Citing 17(hh) for S3/S7 is the correct *promotion record*
of Prop. 5.6 as operative, even though the lemma’s extra content (vanishing
of nonempty free coefficients) is not used. Citing 17(hh) for S2 is accurate
as the forced-zero-sibling clause.

**Closed by citation under Moh (3). Do not send S2, S3, S7 to a joint chart
for N1.** Named charts if someone later demands an unrestricted
degree-preserving kill: S2/S3 the K′=12 joint/unsplit charts of 17(cccccc)
(`(36,24; M_2'=8, V_2'∈{1,5}; k=26)` in the old helper, `ℓ=2` source-correct);
S7 the K′=12 chart `(36,24; M_2'=28, V_2'=8; ℓ=2)`. Those are redundant with
the screen for the N1 statement.

### 4.3 Conditions that are *not* used, and must not be cited as the kill

- Passport `(3.8)`: 17(r) EXTERNAL, `OPEN[PASSPORT-SHARPNESS]`.
- ODE `(3.7)` / Prop. A.3: promoted as a local identity, not needed here.
- Recenter / POLY: 17(gg) PROMOTED-QUALIFIED, 17(hh) made POLY operative; S1–S7
  already die without it; `δ_2` is non-integral on all eight, so the p.190
  edgewise rule does not fire at `j=2`.
- Xu Cor. 5.3 (17(eee)): not cited, not used.
- Enumerator `(10)/(11)` alone: S3/S7 *satisfy* `(11)`; the death is Prop. 5.6
  applied to that branch, not a failure of `(1)`–`(13)`.

## 5. S8 joint-chart citation (17(bbbbbb)) — confirmed

17(bbbbbb) (2026-09-04T21:47Z, PROVED-HERE exact) states the chain:

- split B, `δ=2` partition `[2,1]`: 17(pppp) **PROMOTED**;
- split C, `δ=5/2` partition `[1,1,1]`: 17(tttt) **PROMOTED**
  (QUALIFICATION[17(tttt)] was only on the *unsplit* configuration);
- unsplit A, descended `(27,18; M_2'=21, V_2'=8; k=4)`, K′=9, internal splits
  A and B both `UNIT_IDEAL_CHAR0` exact-Q, 36 variables: 17(bbbbbb) itself.

Together: “the `(99,66)` SKELETON VERDICT is COMPLETE for all three
configurations modulo N1”, on the tuple `M=(−66,77,97)`, `d=(99,33,11,1)`,
`V=(8,8)` — which is S8. ERRATUM[9966-TUPLE-IN-17tttt] confirms that gated
chart used this tuple. Citing “S8 dead by the joint chart, 17(bbbbbb)” is
correct as the *completing* delta; the split legs are 17(pppp) and 17(tttt)
and are named in 17(bbbbbb)’s chain. Not a screen kill.

## 6. Batch-3 lane (receipt only)

`xmodel/g9966-n1-batch3-opus5-20260903.run.v2`: `initial_status=RUNNING`,
`start_utc=2026-09-04T23:43:29Z`, `child_pid=2804816` still live at gate time,
**no `final_status` line**. Instruction: do not open its `.md` until
`final_status`. No independent joint-chart kill was consumed. Nothing in the
receipt contradicts the screen table. If that lane later reports unit ideals
on S1–S4,S7, they are a second instrument, not a promotion condition.

## 7. FALLACY-v2

- No flag/place/series identification. Detector orders of the eight rows are
  not used. The screen parameter is the `V`-assignment and the `D_2` partition.
- No `REPRESENTATIVE`/`FULL_ACTUAL_EXIT` confusion: these are skeleton
  non-existence claims (necessary filters), not exit prices. No
  `charge_basis` line.
- Pole identities not used.
- Floor/attainment not used.
- `sat()` / remainder degree / ring maps: not used (no Gröbner in this lane).
- Prime-as-derivative: not used.
- Merge-free / M-descent: not used (no Prop. 6.3 descent is cited for the
  seven screen kills; S8’s unsplit leg is consumed as a banked chart, not
  re-derived).
- Target/arrival index: `V_2` selected vs sibling `b` kept distinct (§3).
- Citation kills asserted only where promoted + necessary + violated (§4).
- Typed OPEN retained: `OPEN[NONZERO-PARENT-TWIST]` (not in play);
  `OPEN[MOH-PROGRAM-ARTIFACT]` (14 rows; Moh `≤100` not closed);
  batch-3 `RUNNING`.

## 8. Drivers

```text
box/n1gate-20260905/screen_eight.py       05efb84e4b5b2aafa2ac89dde02aed582f0adcace906210565478220c4a376b3
box/n1gate-20260905/diagnose_nodes.py     5503656b97e7c7e256be1b990eb6be1dcb93d7cfccffd84857cba75520d8d226
box/n1gate-20260905/screen_eight.json     6c65dd2a02861f87664815a31f1004203fbbe4ed44aa0228d29a729c0f9c486f
box/n1gate-20260905/diagnose_nodes.json   4beff2e9a955ace3ebff05b710d5ce6e85d48af97d8f239280a824aa6292e65b
```

`screen_eight.py` imports `moh_skeleton_full_frozen` and `opus5_probe.Tree` from
`box/centre-gate-20260903/` (unmodified) and calls `Tree.ok` exactly as
`rerun_screens.run_one`. `diagnose_nodes.py` enumerates every `b` at `j=2`.
Commands: `taskset -c 0,1,2 python3 -u box/n1gate-20260905/screen_eight.py`
and `diagnose_nodes.py`. Wall time `<1s`.

## 9. What this does and does not close

**Closes (NOTIFY-WORTHY).** No pair of degrees `(99,66)` satisfying Moh’s
p.200 search (1)–(3) (Jacobian, `M_s=n−2`, degrees not simultaneously
reducible) can carry any of the eight `(1)`–`(13)`-admissible skeletons:
S1,S4,S5,S6 violate p.200(4); S2,S3,S7 violate Prop. 5.6 on a still-centred
empty-free zero chain (selected or forced sibling); S8 is the printed row
and is dead in all three configurations. Completeness of `(1)`–`(13)` plus
the tree conditions is citable to printed theorems plus 17(r)/17(hh). That
is N1, and it is the degree-wide `(99,66)` headline.

**Does not close.** Moh’s `≤100` theorem (14 excess `u_s=1` rows).
Unrestricted reducible `(99,66)` pairs (Prop. 5.6’s second alternative)
without an induction on degree. K16, the `k=4` ray, `(H1)` census.

**Does not require.** Five joint-chart Gröbner kills of S1–S4,S7. Those
remain a legitimate independent-instrument cross-check (batch-3), not the
proof.

<!-- BODY-END -->
