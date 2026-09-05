# ROSTER: the all-degree residual is 66 necessary configurations

Lane `residual66-roster-sol56-20260905`, frozen basis
`a733bbc8087abb579f16a853350ad2a400b5dca8`. The requested repair, replay,
controls, receiver sizing, and split-window crosswalk are complete.

The finite result is:

> **1,420 operative rows = 1,354 empty necessary-data sets + 66 singleton
> necessary configurations.** Of the 66, **46 have `u_s=1`** and **20 have
> `u_s>1`**. The exact resonance repair adds exactly one singleton, the
> requested `(168,112)` configuration. There are **52 distinct G_i receiver
> charts**. The cheapest has **193 unknowns excluding `T`** (194 including
> `T`), so no chart meets the conditional `<=60` exact-Q demonstration gate.

This is deliberately a roster of configurations, not a list of degree pairs.
A nonempty necessary-data set is not an attained Keller pair. Likewise, a
chart's unknown count is its size, not a proof that the chart is easy or hard.

## 0. Custody, changes, and reproducibility

The eight charged inputs were taken only from
`/tmp/jc2-lane.fzVFfW/inputs`. The manifest was rebuilt mechanically with
`awk` from the receipt's paired `charged_input_<i>_basename=` and
`charged_input_<i>_sha256=` declarations, then passed to `sha256sum -c`:
**8/8 OK**. The exact manifest and checker output are
`box/residual66-20260905/inputs.sha256` and `inputs.check.log`; the reproducing
driver is `verify_inputs.sh`. No frozen input was edited.

The historical sweep driver contains the superseded literal lane path
`/tmp/jc2-lane.wwyG4k/inputs`. For this replay that path was a compatibility
symlink to `/tmp/jc2-lane.fzVFfW`, so the module actually loaded was the
hash-verified charged `moh_skeleton_full.py`; both paths resolved to the same
file and digest.

The only library edit is `box/lib/own_v_routes.py`. All other new drivers and
deliverables are under `box/residual66-20260905/`. There were no ledger,
`jc2-lean`, or `ideation-*` edits.

The principal artifacts are:

| artifact | role |
|---|---|
| `box/lib/own_v_routes.py` | corrected whole-pattern resonance predicate; legacy control flag |
| `box/child-own-v-20260905/summary.json` | fresh full-sweep counts |
| `box/residual66-20260905/verify_controls.py` / `controls.json` | patched/legacy differential and 18 positive/negative controls |
| `box/residual66-20260905/chart_counts.py` / `chart-counts.json` | exact G_i unknown and generator counts for 52 receiver classes |
| `box/residual66-20260905/build_roster.py` | joins own data, route typing, chart sizes, and split screens |
| `box/residual66-20260905/roster.jsonl` | 66 complete machine-readable roster records |
| `box/residual66-20260905/roster.md` | 66-row human table sorted by chart size |

## 1. Prop. 4.6(5): exact repair and differential control

The charged implementation rejected either a zero-root factor `z` or a
nonzero orbit multiplicity `r` whenever `P == Q*z` or `P == Q*r`. That treats
one factor of multiplicity `P/Q` as if the entire polynomial were a power of
`q`. Prop. 4.6(5), as fixed by the gate, excludes only the whole pattern
`p(pi)=q(pi)^w`.

For a completed candidate let

```text
w = P/Q,
multiplicities = ({z} when z>0) union the orbit multiplicities,
distinct roots of p = [z>0] + A * (# nonzero orbits).
```

The corrected search rejects precisely when `w` is integral, every present
multiplicity equals `w`, and the distinct-root count is `Q=deg q`. Equivalently
the accepted predicate is

```text
NOT(all multiplicities equal w AND #distinct roots = deg q).
```

The state `(distinct_roots, all_multiplicity_w)` is carried inside the cached
completion search and tested only after a whole factor pattern has been
assembled. This placement matters: a resonant first completion cannot suppress
a later nonresonant completion. Constructor keyword
`legacy_resonance_filter=True` restores both historical per-factor rejections
and disables the corrected final test, giving an exact control rather than a
second implementation. The production module also exports
`is_q_power_pattern`; `verify_controls.py` imports that function directly for
its mixed-multiplicity nonpower and genuine-power truth table. The controls do
not test a duplicate predicate.

### 1.1 The single changed row

The patched-minus-legacy survivor set is exactly

```text
source (n,m) = (168,112)
M = (-112,140,160,166),  d = (168,56,28,4,2)
V = (3,21,3),            (u_s,v_s) = (1,3)
```

Its source-tree witness is:

| level | delta | A | P | Q | z | orbit multiplicities | selected mode |
|---:|---:|---:|---:|---:|---:|---|---|
| `j=3` | `1/5` | 5 | 21 | 6 | 21 | `()` | zero |
| `j=2` | `3/10` | 10 | 42 | 21 | 2 | `(3,1)` | nonzero |
| bottom | `delta_1=3/4` | `A_1=2` | — | — | — | `V_2=3`, centre lattice 10 | — |

At the critical `j=2` node, `w=P/Q=2` and the factor pattern has
`1+10*2=21=deg q` distinct roots, but its multiplicities are `{2,3,1}`.
Therefore `p` is not `q^2`; the printed condition is satisfied. The legacy
filter nevertheless rejects its `z=2` factor. The patched child singleton is

```text
(n',m') = (42,28)
M'      = (-28,35,40)
d'      = (42,14,7,1)
own V'  = (3,7)
s'=3, ell=1, delta'=(7/6,-1/3,-2), u_s=1.
```

Here and throughout the roster, `delta'` is in increasing index order
`(delta'_1,...,delta'_{s'})`. The legacy replay has 1,355 empty / 65 singleton;
the corrected replay has 1,354 / 66. The set assertions in `controls.json`
show no legacy survivor disappears and the row above is the sole addition.

`OPEN[RESONANCE-FILTER-EXACT-FORM]` is therefore closed at the implementation
level specified by the gate: the predicate is whole-pattern exact, the old
predicate remains callable, and the only census delta is identified.

## 2. Fresh sweep and regression controls

The requested `box/child-own-v-20260905/sweep.py` was rerun without
`--reuse-enumeration`. It freshly enumerated 24,063 census rows, recovered the
same 1,420 operative source rows, and rewrote `own-rows.jsonl` and
`summary.json`. Every built-in comparison passed: full-source row equality
against the gate and inventory, hard-row multiset equality, characteristic
labels, and the historical `U_2` arithmetic check.

The corrected route-state partition is:

| route state | rows |
|---|---:|
| `NONEMPTY` | **66** |
| `EMPTY_NECESSARY_FIRST_SUPPORT` | 1,051 |
| `EMPTY_NECESSARY_WHOLE_SOURCE_TREE` | 213 |
| `EMPTY_PROP6.3_FINITE_POLE` | 90 |
| **total** | **1,420** |

Thus all empty states sum to **1,354**. The downstream typed partition also
checks: 46 own candidates at `u_s=1`, 20 at `u_s>1`, 890 other empty
necessary-data rows at `u_s=1`, 284 at `u_s>1`, 90 finite-pole rows, 84
`U_NEG_US1`, and six conditional `U_NEG_US2` rows.

Both existing test suites pass: six source-route tests and eight own-descent
tests. `verify_controls.py` then independently replays all 1,420 enumerated
sources through the patched tool and through the legacy flag. It also checks
the exact non-power predicate on all 91 saved route roots, 199 internal node
occurrences, and 245 bottom occurrences.

### 2.1 Six positive controls

All five of Moh's printed p.207 rows and the `(99,66)` row remain singleton.
The vectors below use `M'=(M'_1,...,M'_{s'})`,
`d'=(d'_1,...,d'_{s'+1})`, `V'=(V'_2,...,V'_{s'})`, and increasing-index
`delta'`.

| source configuration | own child data | route status |
|---|---|---|
| `(64,48); M=(-48,52,62); V=(3,3)` | `(16,12); M'=(-12,13); d'=(16,4,1); V'=(3); s'=2; ell=1; delta'=(1/4,-1)` | D1, p.207 |
| `(75,50); M=(-50,55,73); V=(2,4)` | `(15,10); M'=(-10,11); d'=(15,5,1); V'=(2); s'=2; ell=2; delta'=(4/3,-1)` | D1, p.207 |
| `(75,50); M=(-50,55,73); V=(3,4)` | `(15,10); M'=(-10,11); d'=(15,5,1); V'=(3); s'=2; ell=2; delta'=(1/2,-1)` | D1, p.207 |
| `(84,56); M=(-56,64,82); V=(2,3)` | `(21,14); M'=(-14,16); d'=(21,7,1); V'=(2); s'=2; ell=1; delta'=(7/6,-1/2)` | D1, p.207 |
| `(84,56); M=(-56,72,82); V=(5,3)` | `(21,14); M'=(-14,18); d'=(21,7,1); V'=(5); s'=2; ell=1; delta'=(1/3,-1)` | D1, p.207 |
| `(99,66); M=(-66,77,97); V=(8,8)` | `(27,18); M'=(-18,21); d'=(27,9,3); V'=(8); s'=2; ell=4; delta'=(0,-1)` | conditional retained prefix |

The last row is a printed-data control, not a p.207 descendant. Its retained
gcd is `u_s=3`, so its child labels remain prefix-only.

### 2.2 Twelve Moh `n<=100` empty fibres

All twelve requested negative fibres remain empty. The empty stage is also
stable: nine fail first-support arithmetic and three fail the necessary whole
source tree.

| fibre | source `(n,m); M; V` | patched state |
|---|---|---|
| `6_13/V1_1` | `(96,72); M=(-72,36,78,94); V=(1,1,5)` | `EMPTY_NECESSARY_WHOLE_SOURCE_TREE` |
| `6_13/V1_3` | `(96,72); M=(-72,36,78,94); V=(1,3,5)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `6_13/V4_3` | `(96,72); M=(-72,36,78,94); V=(4,3,5)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `2_9/V1_8` | `(90,60); M=(-60,10,45,88); V=(1,8,4)` | `EMPTY_NECESSARY_WHOLE_SOURCE_TREE` |
| `2_9/V3_8` | `(90,60); M=(-60,10,45,88); V=(3,8,4)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `12_17/V1_2` | `(96,64); M=(-64,48,68,94); V=(1,2,3)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `12_17/V2_1` | `(96,64); M=(-64,48,68,94); V=(2,1,3)` | `EMPTY_NECESSARY_WHOLE_SOURCE_TREE` |
| `12_17/V3_2` | `(96,64); M=(-64,48,68,94); V=(3,2,3)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `m12_m2_5/V1_1_6` | `(96,64); M=(-64,-48,-8,20,94); V=(1,1,6,3)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `9_20/V1_9` | `(96,72); M=(-72,36,80,94); V=(1,9,3)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `9_20/V4_9` | `(96,72); M=(-72,36,80,94); V=(4,9,3)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |
| `m15_14/V1_9` | `(96,72); M=(-72,-60,56,94); V=(1,9,3)` | `EMPTY_NECESSARY_FIRST_SUPPORT` |

## 3. The 66-row roster and descent typing

`roster.jsonl` has exactly 66 JSON objects, deterministically sorted by
intrinsic chart unknowns, then generator count, then source configuration.
`roster.md` renders every object as one human-table row in the same order.
Every machine record contains:

- source `n,m,M,d,V,s,(u_s,v_s)`;
- own child `n',m',M',d',V',s',ell,delta'` and first nonzero source index;
- descent status, license, prefix flag, and typed dependencies;
- the full G_i support/count certificate and receiver key;
- the complete split-window orders, counts, and typed ES leaves when `u_s>1`;
- control tags and provenance back to the full sweep row.

The vector conventions are explicit in every record. Source `d` is
`(d_1,...,d_{s+1})`; source `V` is only `(V_2,...,V_s)`, excluding the
internal appended `V_{s+1}=d_{s+1}` convention. Child `d'` is
`(d'_1,...,d'_{s'+1})`; `V'` is `(V'_2,...,V'_{s'})`; `delta'` is
`(delta'_1,...,delta'_{s'})`.

For all **46 `u_s=1` rows**, Proposition 6.4 supplies the radius and
Proposition 6.3 supplies the polynomial monomial-Jacobian descent. These are
typed `D1 / LICENSED_AND_FORCED`; their effective child gcd chains close at
one.

For all **20 `u_s>1` rows**, the retained last gcd equals `u_s>1`. The source
numbers do not provide later nondivisible coefficients or prove that this last
retained label is the effective child terminal. Their nominal D2 receiver
route is therefore `CONDITIONAL_PROP6.3_RADIUS`, never an unconditional
descent, and every such row carries both

```text
OPEN[PROP6.3-RADIUS-US>1]
OPEN[CHILD-TERMINAL-SUPPORT-US>1]
```

No prefix terminal was promoted by analogy. Correspondingly, the G_i chart on
such a row is an exact-size formal receiver conditional on that retained last
label becoming the actual effective terminal.

## 4. Exact G_i receiver sizes

The charged source-support theorem is used with all three hypotheses named:
H1 is a licensed Proposition 6.3 descendant with effective terminal data; H2
is the root-replacement normalization `Q=T_1^psi(P)`, equivalently
`M'_1=-m'`; H3 is the actual terminal radius
`d=-delta'_{s'}=(ell+1)/(n'-M'_{s'}-1)>0`. The 46 D1 rows meet these
hypotheses. For a `u_s>1` row, the same formulas give only an exact-size formal
receiver conditional on its two typed opens; no H1/H3 terminal coverage is
asserted.

Under those hypotheses, for a receiver degree pair set

```text
K=gcd(n',m'),  e=n'/K,  q=m'/K,
d=(ell+1)/(n'-M'_last-1),
G_i={(b,a): 0<=a<K, 0<=b<=floor(d*(iK-a))}.
```

The chart uses `G_1` for `h-y^K`, `G_i` for `alpha_i` (`1<=i<=e`), and
`G_i` for `beta_i` (`2<=i<=q`), with `beta_1=0`. The constant coordinates of
`alpha_e` and `beta_q` are removed by the licensed translation gauges. The
reported unknown count is all remaining coefficient coordinates plus `c`; it
excludes the structural variables `x,y` and the saturation inverse `T`.
`unknowns_with_T` adds one. Generator totals separately count the nonzero
h-adic coefficient rows of `J(P,Q)-c*x^ell`, then add `T*c-1`.

`chart_counts.py` sends every one of the 52 receiver classes through the actual
production path in memory: `gi_only_emit.supports`, the charged compiler's
`build_spec`, the production P/Q swap, `native_builder_text`, and the charged
`builder_fix`. The emitter, compiler, row generator, and builder fix are all
hash-pinned. Its count-only interpreter consumes the resulting fixed P-first
row program in the emitted phase order: setup, `HDIV`, H-level allocation,
formal pair updates, monic division and quotient propagation, target
subtraction, and row append. Nine mutation controls require rejection of an
extra H mutation, duplicate target, `h`/`alpha`/`beta`/`c` mutations, an
`HDIV` rewrite, an extra append, and moving the append phase before division.
The per-program digest is an integrity tripwire binding the interpreted bytes
to the in-memory producer output, not an independently predicted hash.

All **52 classes / 349 coefficient blocks** agree on every support set, gauge,
and unknown count (59,368 coefficient coordinates before the 52 copies of
`c`). The authoritative emitted-program interpretation counts 102,422 h-adic
coefficient generators over the 52 distinct charts. It derives a structural
upper coordinate set and evaluates the same emitted plan after assigning every
independent coefficient deterministically modulo `1,000,000,007`; on every
class every structural coordinate is nonzero. Each row is therefore a nonzero
integer/Q coefficient polynomial, so the count is exact rather than a
probabilistic genericity assertion. The former compact reconstruction agrees
on every coordinate but is retained only as a cross-check. The six classes
with materialized h-adic row files additionally match coordinate-for-coordinate,
not merely by totals.

As a strong control, all six pre-emitted classes in
`box/gi-only-20260905/` match coordinate-for-coordinate and count-for-count:

| canonical class | unknowns excluding `T` | coefficient generators |
|---|---:|---:|
| `(24,16; M'_last=5, ell=1)` | 70 | 66 |
| `(18,12; M'_last=9, ell=2)` | 109 | 150 |
| `(24,18; M'_last=14, ell=1)` | 127 | 173 |
| `(24,16; M'_last=17, ell=1)` | 171 | 247 |
| `(24,18; M'_last=20, ell=1)` | 341 | 560 |
| `(16,12; M'_last=13, ell=3)` | 455 | 756 |

### 4.1 Receiver-key correction

The charged theorem says specifically that `d` and `|G_1|` are determined by
`(n',M'_last,ell)` inside its fixed degree context; it does not say that every
`G_i` block or the complete chart is three-field determined. A complete chart
key must be `(n',m',M'_last,ell)`: `m'` fixes `K`, the number `q` of beta
blocks, and hence the chart size. There are four three-field collisions in the
residual:

```text
(35,30,1): m'=14 -> 403 unknowns; m'=21 -> 471
(30,25,3): m'=20 -> 724;          m'=24 -> 818
(35,31,2): m'=20 -> 894;          m'=25 -> 1,014
(42,38,2): m'=12 -> 1,034;        m'=18 -> 1,133
```

The roster therefore stores the four-field key and states V-independence only
at fixed receiver degree pair. This preserves the valid content of
17(fffffff) without merging unequal charts.

### 4.2 Cheapest attacks

The first ten rows by exact chart size are:

| roster | source configuration | receiver `(n',m',M'_last,ell)` | unknowns excl./incl. `T` | generators coeff./total |
|---|---|---|---:|---:|
| R001 | `(84,56); M=(-56,64,82); V=(2,3)` | `(21,14,16,1)` | **193/194** | **289/290** |
| R002 | `(75,50); M=(-50,55,73); V=(2,4)` | `(15,10,11,2)` | 199/200 | 300/301 |
| R003 | `(75,50); M=(-50,55,73); V=(3,4)` | `(15,10,11,2)` | 199/200 | 300/301 |
| R004 | `(64,48); M=(-48,52,62); V=(3,3)` | `(16,12,13,1)` | 241/242 | 378/379 |
| R005 | `(135,90); M=(-90,100,133); V=(4,4)` | `(27,18,20,2)` | 307/308 | 484/485 |
| R006 | `(156,104); M=(-104,120,154); V=(3,3)` | `(39,26,30,1)` | 322/323 | 495/496 |
| R007 | `(84,56); M=(-56,72,82); V=(5,3)` | `(21,14,18,1)` | 370/371 | 595/596 |
| R008 | `(147,98); M=(-98,105,145); V=(6,6)` | `(21,14,15,4)` | 370/371 | 595/596 |
| R009 | `(192,128); M=(-128,148,190); V=(2,3)` | `(48,32,37,1)` | 388/389 | 600/601 |
| R010 | `(140,56); M=(-56,120,138); V=(3,3)` | `(35,14,30,1)` | 403/404 | 576/577 |

The unique cheapest configuration is R001. Since **193 > 60**, the task's
antecedent for a 600-second exact-Q `guided_gb` demonstration is false. No
solver was run and no kill is claimed. The largest roster receiver has 4,889
unknowns excluding `T`. These numbers rank chart size only; they do not rank
proof difficulty.

## 5. Split-window status of all 20 prefix rows

`build_roster.py` calls the charged `box/lib/split_window.py` afresh on every
`u_s>1` source. A leaf records a strict-window first-separation candidate
`rho` and root partition `lambda`, after the Galois and local-exponent screens.
It is a typed necessary ES leaf, not an attained exit and not a joint-chart
lift.

All 20 rows have at least one survivor. Consequently **zero are D2-forced**;
there are **36 typed ES leaves**, with per-row leaf-count histogram
`{1:13, 2:3, 3:1, 4:2, 6:1}`. The D2 branch remains as an alternative on each
row.

| roster | source; `M`; `V` | `(u_s,v_s)` | conditional child prefix | typed ES survivors `(rho:lambda)`; D2 |
|---|---|---:|---|---|
| R012 | `(108,72); (-72,81,106); (7,7)` | `(2,7)` | `(24,16); M'=(-16,18); V'=(7)` | `3:(1,1)`; D2 remains |
| R015 | `(99,66); (-66,77,97); (8,8)` | `(3,8)` | `(27,18); M'=(-18,21); V'=(8)` | `2:(2,1)`, `5/2:(1,1,1)`; D2 remains |
| R016 | `(168,112); (-112,133,166); (3,5)` | `(2,5)` | `(48,32); M'=(-32,38); V'=(3)` | `2:(1,1)`; D2 remains |
| R023 | `(165,110); (-110,121,163); (2,9)` | `(2,9)` | `(30,20); M'=(-20,22); V'=(2)` | `4:(1,1)`; D2 remains |
| R024 | `(165,110); (-110,121,163); (3,9)` | `(2,9)` | `(30,20); M'=(-20,22); V'=(3)` | `4:(1,1)`; D2 remains |
| R029 | `(168,112); (-112,144,166); (5,5)` | `(3,5)` | `(63,42); M'=(-42,54); V'=(5)` | `3/2:(1,1,1)`; D2 remains |
| R035 | `(144,108); (-108,117,142); (3,7)` | `(2,7)` | `(32,24); M'=(-24,26); V'=(3)` | `3:(1,1)`; D2 remains |
| R038 | `(135,90); (-90,105,133); (8,11)` | `(4,11)` | `(36,24); M'=(-24,28); V'=(8)` | `2:(3,1)`, `5/2:(2,2)`, `5/2:(2,1,1)`, `8/3:(1,1,1,1)`; D2 remains |
| R043 | `(168,112); (-112,126,166); (7,11)` | `(3,11)` | `(36,24); M'=(-24,27); V'=(7)` | `3:(2,1)`, `3:(1,1,1)`, `7/2:(1,1,1)`; D2 remains |
| R044 | `(147,42); (-42,133,145); (4,5)` | `(2,5)` | `(42,12); M'=(-12,38); V'=(4)` | `2:(1,1)`; D2 remains |
| R045 | `(147,63); (-63,133,145); (5,5)` | `(2,5)` | `(42,18); M'=(-18,38); V'=(5)` | `2:(1,1)`; D2 remains |
| R049 | `(189,126); (-126,162,187); (5,7)` | `(2,7)` | `(42,28); M'=(-28,36); V'=(5)` | `3:(1,1)`; D2 remains |
| R051 | `(180,144); (-144,153,178); (5,7)` | `(2,7)` | `(40,32); M'=(-32,34); V'=(5)` | `3:(1,1)`; D2 remains |
| R052 | `(165,99); (-99,143,163); (7,8)` | `(3,8)` | `(45,27); M'=(-27,39); V'=(7)` | `2:(2,1)`, `5/2:(1,1,1)`; D2 remains |
| R053 | `(200,150); (-150,170,198); (7,7)` | `(3,7)` | `(60,45); M'=(-45,51); V'=(7)` | `2:(2,1)`, `2:(1,1,1)`; D2 remains |
| R054 | `(175,70); (-70,161,173); (8,5)` | `(2,5)` | `(50,20); M'=(-20,46); V'=(8)` | `2:(1,1)`; D2 remains |
| R055 | `(171,114); (-114,133,169); (8,14)` | `(5,14)` | `(45,30); M'=(-30,35); V'=(8)` | `2:(4,1)`, `5/2:(3,1,1)`, `5/2:(2,2,1)`, `5/2:(1,1,1,1,1)`, `8/3:(2,1,1,1)`, `11/4:(1,1,1,1,1)`; D2 remains |
| R062 | `(180,135); (-135,150,178); (11,11)` | `(4,11)` | `(48,36); M'=(-36,40); V'=(11)` | `2:(3,1)`, `5/2:(2,2)`, `5/2:(2,1,1)`, `8/3:(1,1,1,1)`; D2 remains |
| R065 | `(180,120); (-120,168,178); (11,9)` | `(3,9)` | `(45,30); M'=(-30,42); V'=(11)` | `5/2:(1,1,1)`; D2 remains |
| R066 | `(162,108); (-108,126,153,160); (8,8,7)` | `(2,7)` | `(36,24); M'=(-24,28,34); V'=(8,3)` | `3:(1,1)`; D2 remains |

## 6. Degree split and final status

Exactly six roster configurations have `n<=100`: the five Moh p.207 rows and
the `(99,66)` row listed in §2.1. The other **60** all satisfy
`100<n<=200`; their actual range is `108<=n<=200`. This is a statement about
the 66 source configurations, not about six degree pairs.

The completed conclusions are:

1. **Resonance filter: CONFIRMED-WITH-FIX.** The working predicate is the
   exact whole-pattern negation, with the historical per-factor behavior
   preserved behind a flag. The only survivor delta is the requested
   `(168,112)` row.
2. **Own-data sweep: CONFIRMED.** Fresh enumeration gives 1,354 empty and 66
   singleton necessary sets, split 46/20 by `u_s=1`/`u_s>1`.
3. **Controls: CONFIRMED.** Six positives remain nonempty; all twelve named
   Moh fibres remain empty at their expected stage.
4. **Roster: DELIVERED.** Each of 66 rows has complete source data, own child
   data, route typing, exact conditional/unconditional receiver sizes, and
   split status.
5. **Cheapest attack: IDENTIFIED, NOT RUN.** The minimum is 193 unknowns, so
   the conditional `<=60` exact-Q instruction does not fire.
6. **Prefix scope: STILL TYPED OPEN.** The two `u_s>1` dependencies named in
   §3 remain. The 36 ES leaves are necessary-screen survivors only.

No exit-price assertion, attainment claim, or exact kill is made here, so no
exit-charge declaration is due.

## 7. Verification transcript and artifact hashes

The final replay sequence was:

```sh
bash box/residual66-20260905/verify_inputs.sh
test "$(readlink -f /tmp/jc2-lane.wwyG4k)" = /tmp/jc2-lane.fzVFfW
PYTHONDONTWRITEBYTECODE=1 python3 box/child-own-v-20260905/test_own_v_routes.py
PYTHONDONTWRITEBYTECODE=1 python3 box/child-own-v-20260905/test_descend_own.py
PYTHONDONTWRITEBYTECODE=1 python3 box/child-own-v-20260905/sweep.py
PYTHONDONTWRITEBYTECODE=1 python3 box/residual66-20260905/verify_controls.py
PYTHONDONTWRITEBYTECODE=1 python3 box/residual66-20260905/chart_counts.py
PYTHONDONTWRITEBYTECODE=1 python3 box/residual66-20260905/build_roster.py --check-only
```

Root-level deterministic replays of `verify_controls.py`, `chart_counts.py`,
and `build_roster.py` matched their recorded outputs byte-for-byte. Two
independent full emitter-path chart replays produced byte-identical JSON. The
canonical replay took 160.64 seconds at 154,092 KiB peak RSS; the independent
audit took 162.08 seconds at 153,904 KiB.

| artifact | SHA-256 |
|---|---|
| `box/lib/own_v_routes.py` | `f07dd9b0e38118132ed2ec2e5e7e972f98ba8f223213062fed356a30188b3bf3` |
| `box/child-own-v-20260905/summary.json` | `443be8af5c16870aede8fc8d0fc52dffc0336d29501bfdce40b7f620ae51d651` |
| `box/child-own-v-20260905/own-rows.jsonl` | `7599c6f1a4ab27c99dfa7bf3a04a44bb3de45ad5976873bfb5ef18cd9aff6ddb` |
| `box/residual66-20260905/controls.json` | `968e86bd5c40c0d5f325942653073b623b54e029c9465e29a4dd5570533befc3` |
| `box/residual66-20260905/chart_counts.py` | `732eccb4d7eea8de8b665f06ed1a5c47c201d0b8987173cd0af9713ec93ef773` |
| `box/residual66-20260905/chart-counts.json` | `4f9382b1c39e2a0b39e2dc14757607f0051969aefc331f3eb2efacd2c1a61d44` |
| `box/residual66-20260905/roster.jsonl` | `cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf` |
| `box/residual66-20260905/roster.md` | `c04fc625d72ccd84baf0cda4664aeb47e6d8933dd13f3e6382cf1de98a3e6bcc` |

## References consumed

- `own-data-gate-opus5-20260905.md`, especially §4.1 and its exact
  Prop. 4.6(5) predicate.
- `child-own-v-astra-20260905.md`, for own data, D1 licensing, and retained
  prefix scope.
- `source-support-closeout-opus5-20260905.md`, theorem 17(fffffff) and the
  G_i-only receiver.
- Frozen `descend_own.py`, `own_v_routes.py`, `split_window.py`, and
  `moh_skeleton_full.py`.
- `FALLACY-v2.md`: configuration/pair, floor/attainment, place/flag, and
  chart-size guardrails.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24281`.
- Body SHA-256:
  `e0e7a97a328e3e51e0843ac32f3987d3bd38069689abf4d5e4984a82f3e6758d`.
- Frozen basis: `a733bbc8087abb579f16a853350ad2a400b5dca8`.
