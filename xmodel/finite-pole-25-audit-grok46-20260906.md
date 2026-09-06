# DATA: the 25 finite-pole rows — Grok 4.6 — 2026-09-06

```text
TYPE. DATA (a row needs its printed line; a convention is not a kill).
  25/25 removed by one clause: descend_own PROP6.3_FINITE_POLE
  (dropped n'-1 tail at source δ_{s-1}=0), then roster NONEMPTY filter.
  Class (a) on all 25: child Prop 6.3(1)(2) monicity, not (b) empty
  first-support and not (c) packet-depth closure.
  Prop 5.3: every above-average packet in the returned source-tree
  witness is carried. 0 reopen. 25 STANDS; 0 OPEN.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` joined by index with `awk`,
then `sha256sum -c` on `/tmp/jc2-lane.b5mnbI/inputs`: **9/9 OK**. Reads were
those frozen copies. No ledger, `jc2-lean`, `ideation-*`, or fleet. Driver:
`box/finite-pole-25-20260906/audit.py`. JSON ~99 KB. Report+JSON ≤ 1 MB.
Rows stay `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.

## 1. The removal clause (uniform on all 25)

Replay of charged `descend_own` on the 25 `actual_rows` with
`roster=null` (JSON `printed_closure_cross.finite_pole_25`):

- `us=1`, `dropped=True` (`raw_M[s-1]==n'-1`), source `δ_{s-1}=0`,
  `δ_s=-1`, `q_degree=V_s∈[3,7]`, `p_exponent=A∈[13,185]`.
- Outer first-support: 1 route, `first_nonzero=2`. Charged
  `own_v_routes.py:149-153` returns a whole-source witness
  (`full_source_routes=1`, `rejected_first_support=[]`). Lines 85–94
  already require a child for every `r>lo` factor.
- Then `descend_own.py:196-209` appends
  `licensed_obstructions[0].name=PROP6.3_FINITE_POLE` and **wipes**
  `choices`. `V_vectors=[]`. `route_state=EMPTY_PROP6.3_FINITE_POLE`
  (lines 262–265). `top_license=NO_CHILD_PROP6.3_FINITE_POLE` (256–258).
- Roster pipeline: `build_roster.py:195` keeps only nonempty `V_vectors`;
  `chart_counts.py:1492` keeps `route_state=="NONEMPTY"`. Charged
  `roster.jsonl` has 66 records, all `provenance.own_route_state=NONEMPTY`.
  The 25 are absent. Charged residual66 report lines 136–144: 90
  `EMPTY_PROP6.3_FINITE_POLE` among 1,420; 66 `NONEMPTY`.

`own_v_routes` did **not** remove them. The wipe is the dropped-tail
obstruction, not an empty first-support set.

**Printed line.** Moh Prop. 4.6 p.170: at this disc
`T_{s-1,initial}=p^A q` with `q` squarefree of degree
`V_s(n-M_{s-1})/d_s=V_s≥3` and `A=(-μ_{s-1}+M_{s-1}-n)/d_{s-1}≥13`.
After one constant normalization, a nonzero residue `C` remains. Prop. 6.3(1)(2)
p.197 requires `T_{s-1}(σ)∈k[γ][π]`, monic in `π`. A root cannot pole above
finite nonzero `γ`. Prop. 6.4 pp.198–199 licenses `u_s=1`. Code restates this
at `descend_own.py:196-201`. License field:
`Prop6.4; Prop4.6 p170; Prop6.3(1)(2)`.

**Class (a)** on all 25: own-`V'` that the outer/full routes would have
kept is contradicted by a printed child necessary condition (Prop. 6.3(1)(2)
monicity). Not (b): the own-route set is nonempty until the obstruction.
Not (c): this is not a packet-depth search termination; the `n'-1` drop is
the trigger for (a).

## 2. Prop 5.3 carry (the six-rows check)

Charged six-rows: an empty closure is valid only if **every** above-average
packet is carried by Prop. 5.3 p.180 to the prescribed next disc. For (a)
the check is not the removal's content; it was replayed anyway.

On every returned witness the unique major at `δ_{s-1}=0` is the selected
zero factor (`z=V_{s-1}>lo`); `zero_major_child` is present and the selected
path continues to `j=2` (nonzero, then bottom). Every `r>lo` packet at `j=2`
has `nonzero_major_children`. Unselected parts at `s-1` are all `≤lo` in the
returned pattern (eight rows have leftover p-degree `>lo`, but the witness
parts them below average). No above-average packet is treated as final at
`D_{s-1}`.

Printed `N>0` on these 25 (charged census §2) is a **source-tower** Galois
product, not a child-polynomiality license. It does not reopen (a).

## 3. Per-row verdict

Clause = `PROP6.3_FINITE_POLE` as in §1. Class (a). Prop 5.3 = carried.
`q`=`q_degree`, `A`=`p_exponent`. Outer `V'` is recorded then wiped.

| id | (n,m) | s | q | A | outer V' | verdict |
|---|---|---:|---:|---:|---|---|
| E0022 | (108,72) | 4 | 3 | 13 | (8) | STANDS |
| E0053 | (120,80) | 4 | 4 | 25 | (7) | STANDS |
| E0097 | (135,90) | 4 | 4 | 13 | (8) | STANDS |
| E0120 | (144,96) | 4 | 5 | 25 | (7) | STANDS |
| E0127 | (144,96) | 4 | 3 | 13 | (8) | STANDS |
| E0301 | (160,120) | 4 | 4 | 89 | (3) | STANDS |
| E0344 | (162,108) | 4 | 5 | 13 | (8) | STANDS |
| E0354 | (168,48) | 4 | 3 | 49 | (4) | STANDS |
| E0355 | (168,72) | 4 | 3 | 103 | (5) | STANDS |
| E0383 | (168,112) | 4 | 6 | 25 | (7) | STANDS |
| E0415 | (180,108) | 4 | 3 | 67 | (7) | STANDS |
| E0452 | (180,120) | 4 | 3 | 29 | (11) | STANDS |
| E0467 | (180,120) | 4 | 5 | 41 | (2) | STANDS |
| E0468 | (180,120) | 4 | 5 | 41 | (3) | STANDS |
| E0475 | (180,120) | 4 | 4 | 25 | (7) | STANDS |
| E0483 | (180,120) | 4 | 3 | 13 | (8) | STANDS |
| E0489 | (180,120) | 4 | 4 | 13 | (8) | STANDS |
| E0608 | (180,120) | 5 | 4 | 53 | (8,3) | STANDS |
| E0724 | (189,126) | 4 | 6 | 13 | (8) | STANDS |
| E0771 | (192,144) | 4 | 5 | 89 | (3) | STANDS |
| E0773 | (192,144) | 4 | 3 | 49 | (11) | STANDS |
| E0939 | (192,128) | 4 | 3 | 99 | (3) | STANDS |
| E0946 | (192,128) | 4 | 7 | 25 | (7) | STANDS |
| E1263 | (200,80) | 4 | 3 | 83 | (8) | STANDS |
| E1279 | (200,160) | 4 | 4 | 185 | (5) | STANDS |

None rejoin the residual. None are `OPEN[PREMATURE-CLOSURE]` or `OPEN[other]`.

## 4. FALLACY-v2

*Pole/interior.* Vertex class is the infinity expansion of `D_s` (`δ_s=-1`)
at the subdisc `δ_{s-1}=0`; leftover `q`-roots are below-average at that
same disc. Prop. 6.3 hypotheses used: monic `g`, `δ_s=-1`, `u_s=1` via
Prop. 6.4. *Carrier/attainment.* No pair. *Floor/attainment.* No `I_M`
equality. *Flag/place/series.* Zero factor, `q`-constants, and `γ`-pole
kept distinct. *Target/arrival.* Source `δ_{s-1}` is not a child search
index. A missing actual-L embed is not this clause. No exit price.

## 5. Verdict

```text
DATA. 25/25: removal = descend_own PROP6.3_FINITE_POLE
  (lines 142-144, 196-209, 262-265) + roster NONEMPTY filter
  (build_roster.py:195; chart_counts.py:1492;
   roster.jsonl provenance.own_route_state).
  Class (a) Prop 6.3(1)(2) child monicity. Printed: Prop 4.6 p.170,
  Prop 6.3(1)(2) p.197, Prop 6.4 pp.198-199.
  STANDS on all 25. OPEN[PREMATURE-CLOSURE]=0. OPEN[other]=0.
DO NOT PROMOTE: the 25 as dead pairs; N>0 as a child license;
  any exit price; any residual rejoining.
```

Replay: `python3 box/finite-pole-25-20260906/audit.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6601`.
- Body SHA-256:
  `0714895067a0104e6dcceb1f59648382bd16f651289252f246353d58c33dce33`.
- Frozen basis: `87caec306a6c76b4d4f450c0f42c464b7ced4392`.
