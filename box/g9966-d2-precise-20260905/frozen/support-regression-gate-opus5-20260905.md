# Support-regression gate — do the h-support gate's two findings invalidate any banked kill?

Opus 5 · 2026-09-05 · lane `support-regression-gate-opus5-20260905`

**Disposition: three of the five banked kill families are hit. `17(dddddd)` (S5 /
corrected S6) is REGRESSED outright — it runs the exact routine the h-support
gate refuted, and at `d = -delta_s = 3/2` resp. `3` neither cap is recoverable.
`17(ddddd)` (D=108 delta=3) is REGRESSED with a MEASURED demonstration: removing
the D2 weight floor from the h3 inventory turns the stage-0 incidence ideal from
`[1]` into a non-unit. The `k=4`-ray kills `17(aaaaaa)/(bbbbbb)` are SOUND in the
h block (the total-degree cap is exactly the gate's own `G_1` at `d = 1`) but
carry a separate, independently-published load-bearing cap on the beta block.
`17(pppp)/(tttt)` are UNDECIDABLE-FROM-RECORD on their D2 block and SOUND on D1.
The K16 ray charts `17(zzz)/(cccc)/(jjjj)` are SOUND — they have no coefficient
inventory of the audited type. No ledger was edited; no big solve was run.**

## 0. Custody

The manifest was built mechanically from `xmodel/support-regression-gate-opus5-20260905.run.v2`
by joining its numbered `_basename` and `_sha256` fields with `awk` and
prefixing `lane_inputs_dir`; no digest was retyped. `sha256sum -c` returned `OK`
for all six frozen files in `/tmp/jc2-lane.HmtLeH/inputs`. Retained as
`box/support-regression-20260905/frozen-inputs.sha256` and `.check.log`. No
content mismatch. Repo files outside the frozen set were read read-only at basis
`1ec9c6cc`. Only `box/support-regression-20260905/` and this report were
written. No ledger, no `jc2-lean`, no `ideation-*`. No new exit-price assertion
is made, so no FALLACY-v2 `charge_basis=` line applies.

## 1. The two failure modes, stated as a decision procedure

The gate proved (`moh-hsupport-gate-astra-20260905.md`, sections 1 and 3):

* **(i) cap** — `b+a <= K` and `b <= K-V2` do not follow from a Theorem-1.2
  order lower bound. They are a total-degree cap and an x-width cap.
* **(ii) centering** — the raw support inequality `b <= floor(a*delta_1 - i*B)`
  is exact only for a CENTERED generic point `sigma = pi t^delta`. Moh
  Def 5.1(4) (printed p.179) writes `sigma_i = sum a_j t^j + pi t^{delta_i}`.
  The countercontrol `h = y(y-x^2)^3 + x^5` has a weight `-5` monomial below
  `B` yet `ord h(sigma_1) = B`.

The gate also supplied the **repair that discharges both at once** (its section
4): translate by the trace `eta = -[y^{N-1}]Q/N`, then with `d = -delta_s > 0`
and `x`-weight 1, `y`-weight `d`,

```text
  deg_x [y^a] F <= floor(d*(L-a)),      G_i = { (b,a) : a<K, b <= floor(d*(iK-a)) }.
```

This gives a **decision procedure for this audit**, which I apply row by row:

> A total-degree cap `b+a <= iK` on block `i` is a PROVED over-approximation
> exactly when `d = -delta_s <= 1`, because then `G_i` contains the capped set
> and the cap coincides with (or is implied by) the gate's own envelope. When
> `d > 1` the cap is strictly inside `G_i` and is load-bearing.

`delta_s = -(ell+1)/(n' - M_s' - 1)` (gate section 4; Moh's p.171 remark
extending Prop 4.6 to `J = x^ell`). All arithmetic below is in
`box/support-regression-20260905/envelope_compare.py`.

## 2. Kill-by-kill verdicts

### 2.1 `17(aaaaaa)` / `17(bbbbbb)` — k=4-ray rows K=7,8,9

**Routine.** `box/k4raypinned-20260903/pinned_chart.py:79-91` —

```python
def mons(dmax, ymax):  return [(i,j) for j in range(ymax+1) for i in range(dmax-j+1)]
def h_mons(K, drop_top=True):        out = mons(K-1, K-1); drop (0,K-1)
def lower_beta_mons(b, K):           return mons(b-1, K-1)
```

emitted at `:167-168` as `poly h = y^(K-1)*(y-x) + sum h_ij x^i y^j`, with `b`
hard-set to `K-2` at `:109`. The banked K=8/K=9 chart uses the same convention
(`box/k4rayk89-20260903/structure-note.md:47`,
`k4ray-K89-sol56-20260903.md:76`).

**Support enumerated.** h: pinned degree-K face `y^(K-1)(y-x)`, plus every
`(i,j)` with `i+j <= K-1`, minus `(0,K-1)`. Counts 27 / 35 / 44 at K=7/8/9.
beta: `deg beta <= K-2` with top band pinned to the single scalar
`mu*y^(K-3)(y-x)`; lower `(i,j)` with `i+j <= K-3`. Counts 15 / 21 / 28.

**Justification cited.** `lf(f)=H^2`, `lf(g)=H^3` from the vanishing of the
degree-`5K-2` Jacobian band (`k4ray-unsplit-lemma-opus5-20260903.md:125-134`);
LEVEL 4 `H^2 | beta_b^3`, `rho_{3b-2K} = beta_b^3/(3H^2)`, `deg rho = 3b-2K`
exactly (`k4ray-degree-tower-opus5-20260903.md:243-259`).

**VERDICT — h block: SOUND.** The ray is
`(n,m; M_2', V_2'; k) = (3K, 2K; 3K-6; K-1; 4)` with `(delta_2', delta_1') = (-1, 0)`
(`k4ray-unsplit-lemma-opus5-20260903.md:85`), and independently
`delta_s = -(4+1)/(3K - (3K-6) - 1) = -5/5 = -1` for **every** K. Hence `d = 1`
and the gate's own `G_1 = {b <= floor(1*(K-a))} = {b+a <= K}` is *exactly* the
chart's cap. This is the `d <= 1` branch of the section-1 procedure, so the cap
is a proved over-approximation, not an assumption.

Centering is discharged, and I demand the group element as FALLACY-v2 requires.
The outer-disc argument is center-free by construction (the center `eta` is the
translation, not an assumption). Three elements are composed to reach the
chart's gauge, and each preserves `ord(root) >= -1`, hence total degree `<= K`:
`y |-> y + eta(x)` (trace, det 1, `x` fixed, `J` unchanged); `y |-> a y + b x`
(x-fixing linear, moves the two distinct roots of `lf(h)` to `0` and `x`,
preserves total degree, scales `J` by `a` into `c`); `y |-> y + s` (constant,
kills `h_{0,K-1}`). `ord(x) = -1`, so the linear step cannot lower a root's
order below `-1`. Both dropped coordinate families are therefore accounted:
`x^2 y^{K-2} .. x^K` are removed by the leading-form pin (a separate necessity
obligation, already typed `17(zzzzz)`), and `(0,K-1)` by the constant gauge.

**VERDICT — beta block: REGRESSED (load-bearing cap; NOT caused by the gate).**
`deg beta <= K-2` is a total-degree cap on the `beta_2` block whose proved
envelope is `deg B <= 2K-1` (and the gate's `G_2` gives `b+a <= 2K`). The
producing lane says so in terms: `k4ray-unsplit-lemma-opus5-20260903.md:144-146`
raises `OPEN[K4RAY-BETA-DEG]`; `17(zzzzz)` publishes the residual stratum
`ceil(2(K-1)/3)+1 <= deg beta <= 2K-1` of width `~4K/3`, "GROWING linearly in K
(NOT bounded)"; `k4ray-pinned-chart-gpt55-20260903.md:306-308` states
"the report claims only the pinned bottom residual band `b=K-2`";
`k4ray-K89-sol56-20260903.md:143-147` states "the total-degree beta bound
[is a] residual obligation ... This lane does not manufacture those missing
implications."

The charted stratum is `b = b_min` only:

```text
K   b_min  b_max   charted   uncovered strata   beta coords at b_min / at b_max
7     5      13       5             8                  15  /  70
8     6      15       6             9                  21  /  92
9     7      17       7            10                  28  / 117
```

So `17(aaaaaa)`'s "the nonconstant arm is DEAD, so with the composite arm the
(21,14) row is DEAD" is not a cover: the composite arm kills `deg beta = 0`
only (`17(zzzzz)` CORRECTION), the `3b <= 2K` argument kills `b < b_min`
(`k4ray-degree-tower-opus5-20260903.md:97-107`), and the chart kills `b = b_min`.
`b_min < b <= b_max` is uncovered.

**Consequence.** `K=8 UNIT => D=108 no-split row DEAD` and
`K=9 UNIT => case (A) DEAD` drop to CONDITIONAL on `deg beta = b_min`.
**Repair.** Nine (K=8) / ten (K=9) further pinned charts, one per `b`; at
`b = b_max` the beta block alone is 92 / 117 coefficients versus 21 / 28 today,
and LEVEL 4 no longer pins the top band to one scalar (the "pinned shape count
= 1" result of `k4ray-degree-tower-opus5-20260903.md:368-378` is stated at
`b = b_min` only). Given K=8/K=9 already needed the exact lower-band
parametrization to fit in 36 variables, the upper strata are not a cheap
continuation of the same instrument.

### 2.2 `17(ddddd)` — D=108 delta=3 split branch — REGRESSED (MEASURED)

**Routine.** `box/g108gate-20260903/band_engine.py:291-311` `h3_template`,
consumed by `minor_incidence_rows` (`:322-352`) and `incidence_audit`
(`:420-...`).

```python
result = {(0,7):1, (0,8):2, (0,9):1}          # face  z^7 w^2
for r in range(1,10):
    vmin = max(0, ceil((cutoff - 4*r)/6))     # D2 weight floor 4r+6q >= 43
    cap  = 9 - r                              # total degree <= 9
```

**Support enumerated.** 7 free `h3` coordinates at `cutoff=43`
(`Hc_1_7, Hc_1_8, Hc_2_6, Hc_2_7, Hc_3_6, Hc_4_5, Hc_5_4`), 9 at the `cutoff=42`
control. The full lower box has 45 positions; 36 are strictly below the
weight-42 threshold and are set to zero (`band_engine.py:126-133`).

**Cap: SOUND.** `cap = 9-r` is "total degree = y-degree = 9" for `h3`, and
D=108 has `M = (-72,81,106)`, `n = 108`, `ell = 0`, so
`delta_s = -1/(108-106-1) = -1`, `d = 1` — matching the published major radii
`(3/8, 1/4, -1)` of `17(ssss)`. The `d <= 1` branch applies.

**Floor: mode (ii), and MEASURED LOAD-BEARING.** The weight `4r+6q` comes from
the D2 substitution `t = s^4, z = pi s^6` (`band_engine.py:222`) — a generic
point carrying only the D3-level center (`z = w-1`, i.e. `w = 1`) and **no**
Def 5.1(4) intermediate center. That is exactly the derivation the gate
refuted. I re-ran the pinned `qstar_reduce` with the floor removed and every
one of the 45 lower coordinates free
(`box/support-regression-20260905/d108_uncapped_incidence.py`, output
`.out`):

```text
baseline_cutoff43   h3_free_coords=  7  Qstar_pivots= 7  residual_rows=5  GB=[1]          UNIT=True
control_cutoff42    h3_free_coords=  9  Qstar_pivots= 9  residual_rows=2  GB=[1]          UNIT=True
UNCAPPED_no_floor   h3_free_coords= 45  Qstar_pivots=12  residual_rows=0  GB=[Zc*c - 1]   UNIT=False
```

With the floor removed the 12 nonzero incidence rows become 12 pivots and the
residual is **empty** — the block carries no information at all. `17(ddddd)`
states "the kill is independent of the outer accounting (the unit ideal is
generated by the incidence rows alone)", so the entire certificate rests on the
floor. The `7 -> 9` robustness control recorded in `17(ddddd)` enlarges only by
the two weight-42 *equality* directions; it does not touch the 36 sub-threshold
coordinates and so does not address mode (ii).

**VERDICT: REGRESSED.** `D108-DELTA3-DEAD` drops to CONDITIONAL on the D2
generic point being centered at `z=0`. Missing coordinates: the 36 positions
`{(r,q) : 1<=r<=9, 0<=q<=9-r, 4r+6q < 42}`.

**Repair estimate.** The cheap repair is *not* to add 36 free coordinates — that
is measured to destroy the certificate. It is to prove the intermediate center
vanishes. Structurally the only Def 5.1(4) center term below order 6 in `s` is
an integer-`t` term that is a **constant in `y`**, absorbable by the `y`
translation gauge; but that gauge's availability must be asserted explicitly,
and the sibling (99,66) engine already declares `"b0":"fixed_zero"`
(`box/g9966band-20260903/band_engine.py:278`), i.e. a translation gauge is
consumed on at least one branch there. Estimated cost: one page of source
argument plus a gauge-ledger check — cheap if it succeeds, fatal to this kill if
it does not.

### 2.3 `17(pppp)` / `17(tttt)` — (99,66) delta=2 and delta=5/2 — UNDECIDABLE-FROM-RECORD

**Routines.** `box/g9966band-20260903/band_engine.py:242-254` (`h3_template`:
face `z^8 w^3`, `cap = 11-r`, `vmin = ceil((33-3r)/4)`, 21 free coordinates of a
66-position box) and `:307-334` (`build_major_h2`:
`for r in range(1,34): for q in range(34-r)` — total degree `<= 33 = n/d_2` —
with `3r+4q >= 97` and the seven exact `h2` D1 rows).

**Caps: SOUND.** `M = (-66,72,97)`, `n = 99`, `ell = 0` gives
`delta_s = -1/(99-97-1) = -1`, `d = 1`. Both total-degree caps (11 for `h3`,
33 for `h2`) are "total degree = y-degree" and lie inside the gate's `G_i`.

**D1 block: SOUND on mode (ii).** `g9966-outer-bridge-grok46-20260903.md:145-153`
recentres explicitly: `t = e^9`, `w = 1 + e^{12} + Pi e^{13}`, "a remaining term
contributes `c_{r,q} e^{9r+12q}(1+Pi e)^q`", exact Q-Gaussian on the binomial
matrix, rank **176** of **225** raw slots, leftover rows reduce to zero. The
gate report types this "necessary order vanishing, not equality-face
attainment" (`g9966-branchB-kill-gate-gpt55-20260903.md:171-173`), and the `>=`
vs `=` distinction is clean throughout ("Theorem 1.2 is `>=`; the equality face
is allowed"). This is the correct center-aware treatment.

**D2 block: exposed to mode (ii).** `g9966-outer-bridge-grok46-20260903.md:137-141` uses `t = s^3`, `w = 1 + pi s^4`, so
`t^r (w-1)^q` has "exact weight `3r+4q`", and "strict vanishing ... is the unit
row `c_{r,q}=0` on every slot with `3r+4q < 189`" — 5598 unit coordinate rows on
thresholds `189,285,93,189`. That is the raw-weight rule with a generic point
carrying only the outer center `1`; the same rule sets `vmin` in `h3_template`,
dropping 45 of 66 `h3` coordinates.

**VERDICT: UNDECIDABLE-FROM-RECORD** (leaning REGRESSED on D2). Two things are
missing: **(a)** a statement that the D2 center is exhausted by `w = 1` (or that
the residual center is absorbed by the `y`-translation gauge, whose availability
is contested by `"b0":"fixed_zero"` at `band_engine.py:278`); **(b)** whether
the two kill rows — `stage4_J_d159_k35 = 6264` (delta=2) and
`stage8_G_local16_coord0 = 64` (delta=5/2) — survive an enlarged `h3`/`h2`
inventory. I did not re-run this: it is a multi-stage elimination (15 pivots
through stage 4; 66 cumulative rational pivots through stage 8) and is outside
this lane's small-check budget. Two facts argue *against* assuming the D=108
outcome transfers: the (99,66) kill consumes far more than the incidence block,
and its D1 half is already center-correct. Two facts argue *for* concern: the
`h3` drop is proportionally larger here (45 of 66) than at D=108 (36 of 45), and
the branch face determination (`h3_branch_map`, `:257-280`) assigns values to 18
of the 21 surviving coordinates, so the surviving free dimension is very thin.

**Repair estimate.** Re-emit `h3_template` and the `D2` preblock on
`S_i = D_i ∪ G_i` and replay stages 0-4 (delta=2) / 0-8 (delta=5/2). `h3` grows
21 -> up to 66 free coordinates before the branch map; the `D2` unit-row count
falls from 5598 by the number of slots a center admits. The engine is exact
sympy `qstar_reduce` with rational pivots only, so this is a re-run, not a new
instrument — but it is a several-hour job, not a small check.

### 2.4 `17(dddddd)` — S5 and corrected S6 — REGRESSED

**Routine.** The `order_basis_full` inventory, quoted verbatim in the charged
report at `g9966-n1-batch2-sol56-20260903.md:484-492` and in
`order-basis-full-gpt55-20260903.md:72-75`:

```text
h lower:                       s<K,  r+s<K,   0<=r<=u',  -r + delta1*s >= B
coefficient space at deficit j: s<K,  r+s<=j*K,           -r + delta1*s >= j*B
```

This is, term for term, the routine the h-support gate refuted. `r+s<K` is the
total-degree cap. `0<=r<=u'` with `u' = K - V_2'` **is** the flagged x-width cap
`b <= K-V2`. `-r + delta1*s >= B` is the raw centered-D1 weight floor. The
frozen "before" implementation is
`box/moh14-charts-20260905/hsupport-gate-20260905/before/sprime3_compiler.py:186-204`
(`for xpow in range(0, u+1)` / `if xpow+ypow > K: continue` /
`order_allowed(d1, B, xpow, ypow)`); the repaired successor at
`sprime3_compiler.py:189-200` documents in its own docstring that "No
total-degree or x-width bound follows from these hypotheses."

**Both caps are load-bearing here, and unlike every other row in this audit
neither is recoverable**, because the descended data have `d > 1`
(`box/support-regression-20260905/envelope-compare.out`):

```text
S5  (9,6; M'=(-6,2),  V2'=1, K=3, u'=2, ell=8)   delta1=3/2  delta_s=-3/2  B=-3/2  d=3/2
    chart h-support   5   [(0,0),(0,1),(0,2),(1,0),(1,1)]
    D_1              11 ;  G_1  11 ;  S_1 = D_1 u G_1  14
    MISSING           9   (1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2),(4,0),(4,2)

S6  (9,6; M'=(-6,5),  V2'=2, K=3, u'=1, ell=8)   delta_s = -9/3 = -3        d=3
    chart h-support   5 (report records 2 lower h monomials)
    D_1               9 ;  G_1  21 ;  S_1 = D_1 u G_1  21
    MISSING          16   up to (9,0)
```

At `d = 3/2` and `d = 3` the gate's `G_1` reaches `r <= floor(d*(K-s))`, far
outside `r+s < K`; the x-width cap `r <= u'` (2 resp. 1) is even tighter. So the
charts are strict subsets of the proved necessary envelope, and a UNIT on a
subset chart does not transfer.

Two aggravating details. First, the report states its own inventory rules and
adds "No support inferred from a lower bound was silently upgraded to an
equality" (`g9966-n1-batch2-sol56-20260903.md:494`) — true and irrelevant: the defect is not floor-vs-equality,
it is that the caps are not floors at all. Second, `S5`'s recorded death
"instead rests" on components after an explicit note that "the full 103
descended coefficient rows remain ... lower coefficient band was **not**
performed" (`g9966-n1-batch2-sol56-20260903.md:251-259`), so there is no wider system to fall back on.

**VERDICT: REGRESSED.** `S5 = DEAD[UNIT_IDEAL_CHAR0]` and the rebuilt
`S6 = DEAD` both drop to CONDITIONAL. The `17(dddddd)` tally "S5 + corrected S6
= 2 of the 7 non-S8 skeletons dead; with banked S8 = 3 DEAD / 5 OPEN" is not
sound as stated; the ERRATUM in that same delta (the `ell = v_s - u_s - 1 = 8`
correction) is independent of this finding and stands.

**Repair estimate — this is the cheapest of the four.** Re-emit both partitions
on `S_i = D_i ∪ G_i`. `h` grows 5 -> 14 (S5) and 5 -> 21 (S6); the alpha spaces
(dims 7, 14, 19 at deficits 1,2,3) and the beta space (dim 13 at deficit 2) grow
by the same `r+s <= jK` / `r <= u'` relaxation at `j = 1,2,3`. Current charts are
59 and 60 variables with 103 coefficient rows; the repaired charts are plausibly
110-160 variables. At `K = 3` this is small — a same-day re-solve, and the
correct next action for this family.

### 2.5 `17(zzz)` / `17(cccc)` / `17(jjjj)` — K16 ray charts `T_{t,k}` / `I_{t,+}` — SOUND

**Construction.** `T_{t,k} = -[X^k] sigma_t(R)`
(`k16-terminal-proof-sol56-20260903.md:62`) — coefficient extraction from a
PROVED closed coefficient-array recurrence on the spine variables
`(b_3, b_4, C_j, q_{j,0}, T(0), b_i)`. `I_{t,+} = <T_{t,1},...,T_{t,2t-1}>`.

**Why this family is not exposed.** There is no free-coefficient support
enumeration anywhere in it and no order-floor truncation of unknowns: the spine
is fully parametrized and the ideal is generated by *computed* polynomials, not
by rows against a truncated ansatz. The bounds that look like caps are outputs,
not inputs: `(2.15)` `deg_b4 <= W`, `deg_b3 <= floor(W/(t+1))`,
`deg_{u_i} <= floor(W/i)`, `total degree <= W` with `W = 4t+1-k`, together with
the generating function `(2.16)`, are *derived* properties of the `T_{t,k}`
already produced. The `(6.3)` weighted grading extended in `17(cccc)` is a
proved homogeneity, gate-CONFIRMED by `17(jjjj)` "as an indexed consequence of
the Sol recurrence (symbolic weight audit)". LEMMA CONE is a `G_m`-orbit
argument on that cone. None of this touches a `b+a <= K`, a `b <= K-V2`, or a
raw D1 weight.

**VERDICT: SOUND.** The pre-existing `17(jjjj)` `ONE GAP` (the `b_4`-direction /
`b_4 = 1`-chart statement, or `dim I_{t,+} = 0` outright) is unchanged by this
audit and is not a support defect.

**One boundary note, so this is not read too widely.** The K16 *order-chart*
controls at `box/orderchart-20260903/` — rows `(16,12;13;3;k=1)` and
`(28,20;25;3;k=1)`, both `[1]` — DO run `order_basis_full` and are therefore in
the same regressed class as S5/S6. They are not consumed by `17(zzz)/(cccc)/(jjjj)`,
and `order-basis-full-gpt55-20260903.md:263-267` already types them as
"one-direction" slice controls that "do not validate the multi-direction prefix
generalization". No promotion depends on them.

## 3. What the ledger's top-level claims become

Stated as consequences only; no ledger edit is made here.

| Ledger claim | Status after this audit |
|---|---|
| `17(bbbbbb)` **D=108 CLOSED at skeleton level** | CONDITIONAL on **both** arms: no-split covers `deg beta = b_min` only (2.1); split branch `17(ddddd)` is measured floor-dependent (2.2) |
| `17(bbbbbb)` **(99,66) SKELETON VERDICT COMPLETE, all three configurations** | CONDITIONAL on all three: (A) `deg beta = b_min` only; (B) `17(pppp)` and (C) `17(tttt)` undecidable-from-record on D2 |
| `17(tttt)` `NO-KELLER-PAIR-WITH-THE-(99,66)-SKELETON` PROMOTED | drops to CONDITIONAL — condition (i) of its own typing ("the necessity of the declared joint two-point chart") is exactly where the D2 centering sits |
| `17(dddddd)` `S5 + corrected S6 = 2 dead of 7` | both drop to CONDITIONAL; the `ell = v_s-u_s-1` ERRATUM is unaffected |
| `17(zzz)/(cccc)/(jjjj)` K16 ray, `(T)` at `t=1..7` | unchanged |

The `17(dddddd)` audit-scan note — "the `k=4` ray (`k = v_s-u_s-1 = 4`) and the
D=108 descent (`k=4`) used it CORRECTLY" — is confirmed by this lane: `ell = 4`
is what makes `delta_s = -1` on the ray, and that is precisely what makes the
`k=4`-ray h inventory sound.

## 4. Adversarial notes and negative controls

* **The pin is a normalization; I demanded the element.** For the `k=4` ray I
  wrote the composite `y |-> y+eta(x)`, `y |-> a y + b x`, `y |-> y + s` and
  checked each preserves `ord(root) >= delta_s = -1` and `J = c x^4`. That is
  what makes the cap sound there, and it is exactly the check that the D2
  blocks of 2.2 and 2.3 do not carry in the record.
* **A weaker ideal is safe; a smaller chart is not.** The `local_power <= 8`
  truncation in `minor_incidence_rows` drops ROWS — safe (a unit on a subideal
  is a unit). The `vmin` floor drops UNKNOWNS — unsafe. `17(ddddd)`'s
  `7 -> 9` control and `k4ray`'s `I_light ⊂ I_full` containment are both of the
  safe kind and neither addresses the unsafe kind.
* **Negative control on my own probe.** `d108_uncapped_incidence.py` reproduces
  the pinned engine's `cutoff=43` result (`[1]`, 7 pivots, 5 residual rows) and
  its `cutoff=42` control (`[1]`, 9 pivots, 2 residual rows) before reporting
  the uncapped case, and imports `qstar_reduce` from the frozen
  `box/g108gate-20260903/band_engine.py` unmodified. The three lines differ only
  in `vmin`.
* **What I did not do.** No large solve. I did not re-run the (99,66) staged
  elimination, and I say so rather than typing a verdict from the D=108 outcome.
  I did not re-derive Moh Def 5.1(4) from the PDF beyond the gate's citation.
* **Flag/place/series.** The `b`-stratum finding in 2.1 is a carrier/attainment
  defect (a charted stratum is not the whole stratum), not a support-inventory
  defect; I report it separately rather than folding it into the gate's
  mode (i) so the two are not conflated.

## 5. Artifacts

```text
box/support-regression-20260905/frozen-inputs.sha256          manifest built by awk from the receipt
box/support-regression-20260905/frozen-inputs.check.log       sha256sum -c, 6/6 OK
box/support-regression-20260905/d108_uncapped_incidence.py    D=108 floor-removal probe
box/support-regression-20260905/d108-uncapped-incidence.out   baseline / 42-control / uncapped
box/support-regression-20260905/envelope_compare.py           chart support vs S_1 = D_1 u G_1
box/support-regression-20260905/envelope-compare.out          S5, S6, k=4 ray, (99,66), D=108 radii
```

<!-- BODY-END -->
