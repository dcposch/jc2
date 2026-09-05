# k=4-ray β-strata brute force — five K=7 strata closed over Q; K=8/K=9 still open

Lane `k4ray-strata-solve-opus5-20260905`. Adapter Opus 5.
Drivers: `box/k4ray-strata-solve-20260905/`. No ledger, no `jc2-lean`, no `ideation-*`.

**VERDICT (headline).** All 27 residual strata (54 cover charts) were built,
verified against the charged `pinned_chart.py`, and dispatched to four fleet
workers with 150-minute watchdogs. The lane replaced the frozen lane's dead end
(Singular `std` over Q, *every* extra stratum `INCONCLUSIVE_TIMEOUT`) with a
working engine: msolve decides these ideals in 4–900 s over `F_32003` and, on
the smaller ones, **over Q**. Result: **`K=7` strata `b = 9,10,11,12,13` are
exact-Q units of `I_light` on both cover charts** — the first exact-Q closure of
any k=4-ray stratum above `b_min`, cutting the `K=7` residual band from
`6 ≤ b ≤ 13` to `6 ≤ b ≤ 8`. **`K=8` is 0 of 9 and `K=9` is 0 of 10**: the
`D = 108` no-split arm and `(99,66)` configuration (A) stay conditional on
`deg β = b_min`. Nothing above `b_min` at `K=8,9` was decided either way — every
open entry is a named memory or wall-clock limit, and **no chart anywhere
returned a NONUNIT**, so there is no survivor and no counterexample to report.
Modular units are screens only and are never promoted.

No new exit-price assertion is made, so no FALLACY-v2 `charge_basis=` line.

## 0. Custody

The manifest was built mechanically from `xmodel/k4ray-strata-solve-opus5-20260905.run.v2`
by joining its numbered `charged_input_<i>_sha256` / `_basename` lines with
`awk` and prefixing `lane_inputs_dir=/tmp/jc2-lane.U1OyDP/inputs`; no digest was
retyped. `sha256sum -c` returned **7/7 OK**. Retained as
`box/k4ray-strata-solve-20260905/frozen-inputs.sha256` and `.check.log`. No
content mismatch.

Repo reads outside the frozen set were read-only at basis `7840c7b4`. Writes:
`box/k4ray-strata-solve-20260905/` and this report. `box/lib/guided_gb.py` in
the repo hashes to the charged `501f3b1f…` byte-for-byte and was used unmodified
on every worker.

Fleet: four `r7i.8xlarge` (32 vCPU / 247 GiB) launched by this lane with
`Owner=k4ray-strata-solve-opus5-20260905`, listed in
`box/k4ray-strata-solve-20260905/workers.txt`. These four and no others are the
instances this lane may terminate.

## 1. Chart verification (task 1)

`box/k4ray-beta-strata-20260905/strata_chart.py` was copied to the driver
directory with exactly one line changed (`HERE`, the output root) — `diff` is one
hunk — so the charted ideal is byte-identical to the frozen lane's.

**Against `pinned_chart.py` (charged).** `mons`, `h_mons`, `lower_beta_mons`,
`var_h`, `var_b`, the `quoy` proc, `h`, `f=h^2+B`, `Al=quoy(B^2,h,K)`,
`Rh=B^2-Al*h`, the Jacobian `JJ`, the ρ-row loop and the `RR→SS imap` are the
same text. The only generalisation is the top band:

```text
pinned_chart:  Btop = 2*mu*y^s*(y-x)          Rh_forced_top = (4/3)*mu^3*y^{3s-2K+2}*(y-x)
strata_chart:  Btop = 2*y^smin*(y-x)*Q        Rh_forced_top = (4/3)*y^{3smin-2K+2}*(y-x)*Q^3
```

which specialises to `pinned_chart` at `Q=mu` (the `d=0`, i.e. `b=b_min`, case).

**LEVEL 4 is parametrised exactly, not sliced.** `H=y^{K-1}(y-x)`, so
`H^2 = y^{2K-2}(y-x)^2`. Writing the homogeneous `P=β_b` of degree `b` as
`y^α (y-x)^γ R` with `R` coprime to `y` and `y-x`, `H^2 | P^3` is
`3α ≥ 2K-2` and `3γ ≥ 2`, i.e. `α ≥ ceil((2K-2)/3) = smin` and `γ ≥ 1`. Hence

```text
LEVEL-4 locus  ==  { P = y^smin (y-x) Q : Q homogeneous of degree d = b-smin-1 }
```

with the ambient cap `deg_y P ≤ K-1` becoming `deg_y Q ≤ K-2-smin = ymax_Q`. At
`K=7,8,9`, `smin = 4,5,6` and `ymax_Q = 1`, so `Q = q0 x^d + q1 x^{d-1} y`
carries the **whole** locus. Confirmed independently of the frozen report.

**No unknown is dropped.** `h` is the full box `i+j ≤ K-1` minus `(0,K-1)` (the
constant gauge), `K(K+1)/2 - 1` = 27 / 35 / 44 coefficients at `K=7/8/9`. The
lower β block is `mons(b-1,K-1)` — every monomial of total degree `≤ b-1` and
`y`-degree `≤ K-1`; the `y`-cap is the same normal-form cap that `h` carries and
it does bite (at `K=7,b=8` it removes `y^7`, 36→35). There is no D2-style weight
floor anywhere in the chart. What is dropped is the MASTER `E`-cutoff **rows**
(`theorem_cut=False`); dropping rows enlarges the variety, so a unit of
`I_light` kills the theorem-cut ideal. The converse is not used.

**Cover.** `{q0≠0} ∪ {q0=0, q1≠0}` covers `Q≠0`, i.e. `deg β = b` exactly.
Both charts of every stratum were run; a stratum is decided only when **both**
covers are.

**Weighted homogeneity, machine-checked.** Every prelude that reached the dump
printed `PRE__HOMOG_I 1`, `PRE__HOMOG_CST 1`, `PRE__CST_ZERO 0`,
`TARGET_FOUND 1`. At `K=7` `PRE__CST_WT 29 = 5K-6`, matching the charged
grading. `q_j` carries weight `2K-b`, the same weight for both `j`, which is
what keeps the two-scalar top band inside the single grading.

## 2. Sizes (task 1, recorded)

27 strata / 54 charts; `census.json` in the driver dir. `gb` = GB variables
(geometric + one Rabinowitsch localizer); `ng` = generators actually emitted.

```text
K=8 (b_min=6, smin=5): b = 7..15   gb(q0) = 66,74,82,90,98,106,114,122,130  (q1: one less)
K=9 (b_min=7, smin=6): b = 8..17   gb(q0) = 83,92,101,110,119,128,137,146,155,164
K=7 (b_min=5, smin=4): b = 6..13   gb(q0) = 51,58,65,72,79,86,93,100
h / lower-β coefficients: K=7 27/(b-1 box), K=8 35/…, K=9 44/…  (see §1)
```

## 3. Engine (task 2) — what was actually run, and the resource story

Four `r7i.8xlarge` were launched at 15:20Z and all 54 charts were dispatched
detached (`setsid`, per-worker batch launcher) at **15:33:57Z** with 150-minute
(9000 s) watchdogs, K=8 first, then K=9, then K=7, round-robin over the workers
(`box/k4ray-strata-solve-20260905/assignment.txt`). Each chart ran two branches
in parallel: `strata_chart.py run … --chars 0` (charged `guided_gb`,
`PromotionPolicy.exact_q`, plain Singular `std` over Q with `reduce(1,G)`) and a
modular `F_32003` msolve screen. Polling was every ~10 min.

**Two engine facts changed the outcome.**

1. *msolve, not Singular `std`, is the engine for these charts.* The frozen lane
   reported every extra stratum as `INCONCLUSIVE_TIMEOUT` under Singular `std`
   (1800 s, `r7i.8xlarge`). msolve's F4 decides the same ideals in **4–900 s**
   over `F_32003` and, decisively, **also over Q**: msolve's characteristic-0
   Gröbner run returns `[1]` on the banked `K=7 b=5` chart in **0.31 s** where
   the charged Singular `std` needs 7.78 s for the same `UNIT_IDEAL_CHAR0`.
   This is the promotion path used below.

2. *The wall is memory and formation, not the Gröbner step.* The first sweep
   capped each branch at `ulimit -v 24 GiB`; msolve peaked at 21.4 GiB on
   `K=8 b=7` and **twelve charts died with `MSOLVE_RC_-11` (SIGSEGV)**. Those are
   resource failures, **not** mathematical verdicts, and are recorded as such;
   every one was re-queued on its already-emitted `.ms` file with a 110–200 GiB
   ceiling. Separately, Singular's Jacobian coefficient extraction
   (`coef(JJ,x*y)`) dominates wall time at large `b` (0.6 s at `K=7,b=6`;
   2455 s at `K=7,b=13`), which is what bounds coverage at the top of each band.

**Resource preemption, declared.** At 16:35Z the `guided_gb` Singular branch was
preempted on 50 of the 54 charts and kept only on `K8_B7_Q0/Q1` and
`K9_B8_Q0/Q1`. Reason: the frozen lane had already *measured* that branch as
`INCONCLUSIVE_TIMEOUT` at 1800 s on the smallest chart with a whole worker to
itself, so 14 copies per worker could not do better, and they were holding the
memory the msolve engines needed. Four later `guided_gb` runs were started on
the charts msolve had already decided (`K7 b=10,11,12`) as a cross-engine check.
This is a deviation from "run guided_gb on every stratum" and is declared here,
not hidden: exact-Q below is carried by msolve char 0, positive-controlled
against the charged Singular instrument on the banked `K=7 b=5` chart.

## 4. Controls (FALLACY-v2)

```text
POSITIVE, real chart, exact Q   K=7 b=5 q0 (banked b_min UNIT)  msolve char 0 -> [1], 0.31 s
                                 agrees with charged guided_gb UNIT_IDEAL_CHAR0 (7.78 s)
POSITIVE, real chart, modular   K=7 b=5 q0                       msolve F_32003 -> [1], 0.16 s
POSITIVE, K=8 b_min             K=8 b=6 q0 (17(bbbbbb) row)      msolve F_32003 -> [1], 818 s
NEGATIVE, emitter+classifier    (v0^2-1, v1-3) over F_32003      -> NONUNIT, basis 2
NEGATIVE, length-1 non-unit     (v0*v1-v2^2)                     -> NONUNIT, basis 1   <-- keys on
                                                                    content, not basis length
POSITIVE, emitter+classifier    (v0-1, v0-2)                     -> UNIT, basis 1
SIDE RESULT, K=7 b=5            ROWS + localizer WITHOUT CSTP-1  -> [1] mod p, 68 s
```

The last line matters: at `b=b_min`, `K=7`, the weighted-homogeneous row block
together with `q0≠0` alone is already the unit ideal, i.e. `q0 ∈ √ROWS`. That is
*not* assumed anywhere below; the promoted charts all carry `CSTP-1`.

Ring map, declared: `RR = Q[x,y,params]` with `dp`; `SS = Q[params]` with
`wp(K-i-j | 2K-i-j | 2K-b | 1)`; `ROWS=imap(RR,I0)`, `CSTP=imap(RR,CST)`. For
msolve the parameters are aliased `h_i_j,B_i_j,q_j,q_j_inv → v0..v_{n-1}`
(msolve rejects underscores) by a single regex substitution over the declared
name list, longest-first; the alias map is recorded in every JSON payload, so an
msolve point pulls back to chart coordinates. Over Q each row is passed through
Singular `cleardenom` first (`cleardenom(g)=c·g`, `c ∈ Q^*`: same ideal).
`sat()` is not used anywhere.

## 5. Results — all 27 strata, both covers

`--` = the chart never reached the Gröbner step (Singular `coef(JJ,x*y)` still
running at the watchdog); `SEGV*` = SIGSEGV under this lane's `ulimit -v`, a
**resource** failure and not a verdict; `TO` = engine wall-clock timeout.
A stratum is `DEAD over Q` only when **both** cover charts are exact-Q units.

```text
stratum     q0 modp   q0 Q      q1 modp   q1 Q       verdict
K=8 b=7     SEGV*     SEGV*     SEGV*     SEGV*      UNDECIDED (resource)
K=8 b=8     SEGV*     SEGV*     SEGV*     SEGV*      UNDECIDED (resource)
K=8 b=9     SEGV*     SEGV*     SEGV*     --         UNDECIDED (resource)
K=8 b=10    SEGV*     SEGV*     SEGV*     --         UNDECIDED (resource)
K=8 b=11    UNIT      --        SEGV*     --         partial (q0 modular only)
K=8 b=12..15  --      --        --        --         UNDECIDED (formation)

K=9 b=8     SEGV*     --        SEGV*     --         UNDECIDED (resource)
K=9 b=9     SEGV*     --        SEGV*     --         UNDECIDED (resource)
K=9 b=10    --        --        SEGV*     --         UNDECIDED (resource)
K=9 b=11..17  --      --        --        --         UNDECIDED (formation)

K=7 b=6     SEGV*     --        UNIT      --         partial (q1 modular only)
K=7 b=7     UNIT      UNIT      SEGV*     --         partial (q0 exact-Q)
K=7 b=8     SEGV*     UNIT      SEGV*     preempted  partial (q0 exact-Q)
K=7 b=9     UNIT      UNIT      UNIT      UNIT       DEAD over Q
K=7 b=10    UNIT      UNIT      UNIT      UNIT       DEAD over Q
K=7 b=11    UNIT      UNIT      UNIT      UNIT       DEAD over Q
K=7 b=12    UNIT      UNIT      UNIT      UNIT       DEAD over Q
K=7 b=13    UNIT      UNIT      UNIT      UNIT       DEAD over Q
```

**No chart anywhere returned a NONUNIT basis.** There is therefore no survivor
of a necessary chart to report, and no sample point to publish. Every negative
entry above is an engine or memory limit, and each is named.

Selected timings (`form` = Singular Jacobian/ρ-row formation; `ms` = Gröbner):

```text
chart        nv   ng    form (s)   modp ms (s)   char-0 ms (s)
K=7 b=5 q0   44   151      0.04        0.16          0.31     <-- banked control
K=7 b=9  q1  71   235     75.4       257.6         179.3
K=7 b=10 q0  79   261    206.8        21.8          19.3
K=7 b=11 q1  85   275    446.9        19.2          12.3
K=7 b=12 q0  93   301    773.2         4.9           4.9
K=7 b=13 q1  99   317   2455.5         6.4           (unit)
K=8 b=6  q0  58   211      0.33      818.1          --        <-- b_min control
K=8 b=7  q0  66   243      4.8      >3000 (TO)     >3365 SEGV*
K=9 b=8  q0  83   316    155.3      >3000 (TO)      --
```

**The band is hardest at the bottom.** msolve time falls by ~2.5 orders of
magnitude from `b=b_min+1` to `b=b_min+7` at `K=7` (258 s → 5 s) while the
Singular formation cost rises by ~30x (75 s → 2455 s). The two curves cross
around `b ≈ b_min+4`. That is the operative fact for any continuation: the
uncovered strata are *not* uniformly hard, and the expensive part at the top of
each band is polynomial arithmetic, not Gröbner.

## 6. Verdict (task 4)

```text
K=8 no-split row DEAD for ALL deg β?      NO. 0 of 9 strata closed.
                                          b=11 has one cover (q0) modular-UNIT only.
K=9 case (A) DEAD for all deg β?          NO. 0 of 10 strata closed.
K=7 row DEAD for all deg β?               NO, but 5 of 8 strata are now closed over Q
                                          (b=9,10,11,12,13); b=6,7,8 remain open.
D=108 no-split arm restored?              NO — still conditional on deg β = b_min = 6.
(99,66) configuration (A) restored?       NO — still conditional on deg β = b_min = 7.
```

**Surviving / timed-out strata.**

```text
K=8 (9 open):   b = 7, 8, 9, 10, 11, 12, 13, 14, 15
K=9 (10 open):  b = 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
K=7 (3 open):   b = 6, 7, 8      (b = 9..13 CLOSED over Q, new this lane)
```

None of these is a measured non-unit; every one is a resource or wall-clock
limit with a named cause, listed per chart in §5 and per run in the JSON
payloads under `box/k4ray-strata-solve-20260905/`.

**What is new and promotable.** Five `K=7` strata strictly above `b_min`
(`b = 9,10,11,12,13`, both cover charts each, ten charts) are exact-Q units of
`I_light`. Since `I_light` drops MASTER cutoff **rows** (never unknowns), a unit
of `I_light` kills the theorem-cut ideal, so the `K=7` row's residual band is
reduced from `6 ≤ b ≤ 13` to `6 ≤ b ≤ 8`. This is the first exact-Q closure of
any k=4-ray stratum above `b_min`.

**Strength of the exact-Q claim, stated exactly.** The characteristic-zero
verdicts are msolve `-g 2` reduced Gröbner bases over Q equal to `[1]`, computed
from Singular-emitted, denominator-cleared integral generators. The engine was
positive-controlled against the charged `guided_gb` Singular `std` over Q on the
banked `K=7 b=5` chart (both `[1]`), and against a modular run of the same
chart. It is **one engine** on the ten new charts: the `guided_gb` Singular
`std` cross-checks started at 16:54Z on `K7 b=10,11,12` did not finish inside
the lane, and the four retained `guided_gb` runs returned no characteristic-zero
conclusion (`K8_B7_Q0`: `MODULAR_ONLY`, `accepted_run_count 0`, Singular rc 14
at 6189 s with peak RSS 25.1 GiB against a 24 GiB cap — a resource kill). A
second-engine confirmation of `K=7 b=9..13` is the obvious cheap continuation
and is not claimed here.

## 7. FALLACY-v2

- **Carrier/attainment.** `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. Ten charts
  decided at `K=7` do not decide `K=8` or `K=9`; the `b_min` charts do not decide
  the band; and five closed `K=7` strata do not close the `K=7` row. Each is
  reported at its own level and nothing is lifted by analogy.
- **Floor/attainment.** `3b ≥ 2K+1` remains a floor and LEVEL 4 remains a
  necessary shape. Neither is used as a kill; the kills are units of `I_light`.
- **Modular unit.** Not promoted. `1 ∈ I_p` does not give `1 ∈ I_Q` (`px-1` is a
  non-unit over Q whose reduction mod `p` is the unit ideal), so every
  `MODULAR_UNIT` in §5 is labelled a screen and only the char-0 column is used
  for the DEAD verdicts. Conversely no `MODULAR_NONUNIT` occurred, so the
  weaker converse direction is never invoked.
- **Resource failure vs mathematical verdict.** `MSOLVE_RC_-11` (SIGSEGV under
  `ulimit -v`), `RETRY_RC=137` (SIGKILL at the wall clock) and Singular rc 14
  are recorded as engine limits and are **not** counted as non-units, dimensions
  or survivors. `K=7 b=8 q1` is marked `preempted` because this lane killed it
  to relieve memory on `172.30.0.88`, not because it failed.
- **Dropping rows vs unknowns.** `I_light` omits MASTER `E`-cutoff rows (safe:
  more solutions), and the LEVEL-4 top band is the exact locus
  `y^smin(y-x) | β_b` re-derived in §1, not a slice. The lower β block carries no
  weight floor. Localizers are extra generators, never deleted coordinates.
- **Group element.** The Rabinowitsch generators `CSTP-1` and `q_j q_j_inv-1`
  are named and present in every promoted chart. No `G_m` slice (`q_j = 1`) was
  used for any promoted verdict; the possible cheaper `q_j=1` dehomogenisation is
  noted and not consumed.
- **Cover.** `{q0≠0} ∪ {q0=0,q1≠0}` is a cover of `deg β = b` exactly; a stratum
  is called DEAD only when both charts are units. `K=7 b=7` and `b=8` have one
  exact-Q cover each and are reported as `partial`, not as kills.
- **Variable/ring map.** Declared in §4. Every prelude that reached the dump
  printed `TARGET_FOUND 1`, `PRE__CST_ZERO 0`, `PRE__HOMOG_I 1`. The msolve
  alias map is stored per chart. No fake unit of the `CSTP≡0` kind occurred.
- **`sat()`.** Unused.
- **Report discipline.** No ledger edit, no `jc2-lean`, no `ideation-*`.

No exit-price assertion is made, so no `charge_basis=` line.

## 8. Artifacts

```text
box/k4ray-strata-solve-20260905/frozen-inputs.sha256     7/7 OK
box/k4ray-strata-solve-20260905/frozen-inputs.check.log
(all under box/k4ray-strata-solve-20260905/)
strata_chart.py        copy of the frozen chart (1-line diff)
msolve_export.py       self-contained msolve emitter (no msolveio version gate)
solve_stratum.sh       guided_gb + modular, one chart
exactq_msolve.sh eq_one.sh retry_msolve.sh      exact-Q / high-memory re-runs
dispatch_k4.sh dispatch_all.sh collect.sh final_collect.sh
census.json            27 strata / 54 charts, sizes
assignment.txt         chart -> worker;  workers.txt, fleet-ids.txt, terminate.log
emitter-controls.json  emitter/classifier controls
all-msjob.jsonl        every solver payload (custody)
all-retry.txt          raw msolve GB bodies for the retries
FINAL-TABLE.txt        the §5 table, machine-generated
status-01..13.tsv, poll.log, dispatch.log               polls and dispatch record
fleet-pull/<ip>/       per-worker JSON payloads and msout
```

Per-chart custody is in `all-msjob.jsonl`: each record carries `ms_sha256` of
the exact solver input, `nvars`, `ngens`, `weights`, the Singular `PRE__*`
markers, `msolve_rc`, `msolve_wall`, `form_wall`, and the verdict. Order is
`degrevlex` for msolve, `wp(tower weights)` for the Singular `SS` ring; the
coefficient field is stated per run (`0` or `32003`).

Reproduction of the new closures (one chart, ~4 min on 32 vCPU):

```bash
python3 -u box/k4ray-strata-solve-20260905/msolve_export.py 7 12 --pin-index 0 \
    --char 0 --run --threads 4          # -> EXACTQ_UNIT, msolve [1]
python3 -u box/k4ray-strata-solve-20260905/msolve_export.py 7 5 --pin-index 0 \
    --char 0 --run --threads 4          # banked control -> EXACTQ_UNIT in 0.31 s
```

Grep: `EXACTQ_UNIT`, `MODULAR_UNIT`, `MSOLVE_RC_-11`, `RETRY_RC=137`,
`TARGET_FOUND 1`, `PRE__HOMOG_I`, `DEAD over Q`.

## 9. Fleet termination

The four workers launched by this lane were terminated at 18:05Z and confirmed
`shutting-down` by an explicit `describe-instances` on their four IDs
(`box/k4ray-strata-solve-20260905/terminate.log`):

```text
i-0694335e26273c31b  172.30.0.60    r7i.8xlarge   shutting-down
i-02bd7df6effb9f09b  172.30.0.246   r7i.8xlarge   shutting-down
i-03a314c29582206ae  172.30.0.9     r7i.8xlarge   shutting-down
i-02aa55deef91520eb  172.30.0.88    r7i.8xlarge   shutting-down
```

`fleet.sh term` was called with those four IDs only; `term-all` was never used
and no other `jc2fleet` instance (several other lanes were running concurrently)
was touched. Wall clock: launch 15:20Z, dispatch 15:33Z, termination 18:05Z.

<!-- BODY-END -->
