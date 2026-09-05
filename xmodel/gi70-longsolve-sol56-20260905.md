# GI70 long solve: smallest proved Moh chart

**FINAL DISPOSITION: OPEN / COMPUTE-BOUND.  No class kill and no proved
necessary-chart survivor.**

## 1. Question and promotion boundary

This lane asks one deliberately narrow compute question for the class
`C_n24m16_Mm12_m2_5_ell1_s4`: does the full class-uniform (G_i)-only
coefficient chart have any point with (c\ne0)?  In the canonical P-first
orientation, put

\[
 I=(\operatorname{coeff}_{x,y,h}(J(P,Q)-cx))\subset
 \mathbb Q[z,c].
\]

The production unit test is (I+(Tc-1)=(1)).  An exact-ℚ UNIT, or an exact
rational identity checked in this original ring, kills this class by the
source-support theorem.  A finite-field UNIT is only a screen.  A completed
proper basis is a **necessary-chart survivor** only after dimension, degree,
and an exact sample point checked against all 66 rows and (Tc-1) are
recorded.  Anything weaker is typed `OPEN / COMPUTE-BOUND`.  These are the
frozen classifier rules in
`/tmp/jc2-lane.68h1yv/inputs/gi-only-charts-sol56-20260905.md:54-59,292-316`;
timeouts prove neither emptiness nor nonemptiness (`:419-424`).

No run produced a UNIT, a completed proper basis, or an identity.  Jobs (a),
(c), and (d) exhausted their 10,200-second watchdogs.  Job (b) stopped during
its first modular Hilbert computation after an erroneous 9,900-second internal
timeout, so no Hilbert vector, guided run, or CRT stage existed.  Consequently
there is no exact-Q certificate to consume, no c-section certificate to lift,
and no completed NONUNIT basis from which dimension, degree, or a sample point
could honestly be reported.

## 2. Frozen custody and mutation boundary

Before mathematical use, `verify_charged.sh` read
`xmodel/gi70-longsolve-sol56-20260905.run.v2` itself.  Its awk program joined
each numbered `charged_input_<i>_basename` and `_sha256` field to the receipt's
`lane_inputs_dir`, wrote `custody/charged-from-receipt.sha256`, and ran
`sha256sum -c`.  All six entries returned `OK`; no expected hash was typed into
the verifier and no mismatch was waived.

| frozen input | verified SHA-256 |
|---|---|
| `gi-only-charts-sol56-20260905.md` | `0a273aba609bc695f49e1c0db2a1b4cd0a4bb593cbd6a69226891cd2f3dc1279` |
| `graded-moh-astra-r2-20260905.md` | `31b1a6a8a94a61968d88f4b92713b6a5eb15d6da1df041f37d055e933ba1deb6` |
| `guided_gb.py` | `501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3` |
| `fleet.sh` | `a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c` |
| `dispatch.sh` | `dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

The checked output is `box/gi70-longsolve-20260905/custody/charged-check.log`.
The live chart rows and metadata were separately bound as
`a5e22fbb9c7f16858a9ce342b9ee325b73f5ea2c60ad93ce7675424b3ecb702c`
and `02fb1692949695e52f6d178246e88c4053b8fbe30f54ce4d28c37ef1d4bdd82e`.
Every transmitted driver/input was rechecked on the worker from
`custody/payload.sha256`.  Work was confined to
`box/gi70-longsolve-20260905/` and this report.  No ledger, `jc2-lean`, or
`ideation-*` file was edited.

## 3. Exact chart audited

Here (K=8,e=3,q=2,d=1/9,\ell=1,D=n+m-1=39).  The proved support is

\[
G_i=\{(b,a):0\le a<K,\ 0\le b\le\lfloor d(iK-a)\rfloor\}.
\]

The coordinate inventory is 8 coefficients of (h), 8 of (A_1), 16 of
(A_2), 22 of (A_3), 15 of (B_2), and (c): 70 intrinsic unknowns,
or 71 after adjoining (T).  There are exactly 66 nonzero coefficient rows
and 67 generators after (Tc-1).  This agrees with the frozen target row and
totals at
`/tmp/jc2-lane.68h1yv/inputs/gi-only-charts-sol56-20260905.md:142-165`.
The rows contain 65,990 expanded terms.  The only occurrence of `c` is the
linear `-c` in source row 22.  `custody/chart.json` records the complete
variable order, both degree vectors, source paths and hashes, row count, and
the token-level (c\mapsto1) rule.

This is a class chart, not a representative-fibre guess: (G_i) depends only
on the class data and the frozen theorem gives a canonical per-class receiver
(`/tmp/jc2-lane.68h1yv/inputs/gi-only-charts-sol56-20260905.md:45-52`).
The target is literally P-first (J(P,Q)-cx), and only the two terminal
constant gauges are used (`:118-140`).

## 4. Bigrading, order, and the homogeneity boundary

For a coefficient (z=z_{i,b,a}), with (h) assigned block index (i=1),
the exact bidegree is

\[
 \deg z=(b,iK-a),\qquad \deg c=(2,39).
\]

The row extracted at ((j,b,a)) has degree
((b+1,39-a-8j)).  Monic triangular conversion between ordinary and
(h)-adic coefficients proves that the **66-row ideal (I), before adding
(Tc-1),** is ℕ²-homogeneous.  See
`/tmp/jc2-lane.68h1yv/inputs/graded-moh-astra-r2-20260905.md:13-35`.
Neither (I+(Tc-1)) nor the (c=1) dehomogenization is called homogeneous.

Job (a) scalarizes the honest bidegree by the positive functional
((b,w)\mapsto17b+w).  Its ring order is

```text
(dp(1), wp(17*x_charge + y_deficit))
```

with `T` alone in the first block and all 70 coefficient variables in the
weighted block.  Thus every coefficient generator remains homogeneous in the
weighted block while the inhomogeneous Rabinowitsch relation is explicit and
separate.  No Singular `homog` conversion was used.

Job (b) instead computes the genuinely homogeneous saturation
(S=(I:c^\infty)).  `sat(I,ideal(c))` is retained only through list component
`[1]`; its type is asserted to be `ideal`, the active ring has 70 variables,
and the controls

```text
sat((c),(c)) = (1),      sat((c*h_0_7),(c)) = (h_0_7)
```

are checked by normal forms.  This implements the `sat()`-wrapping guard in
`/tmp/jc2-lane.68h1yv/inputs/FALLACY-v2.md:16-17` rather than trusting a
printed object.

## 5. The four simultaneous 170-minute jobs

Exactly one on-demand `r7i.16xlarge` was launched: instance
`i-0b29f3356aaf6ef81`, private IP `172.30.0.111`, launch time
`2026-09-05T16:41:38Z`.  The worker exposed 64 vCPUs and 495 GiB RAM, with no
swap.  Singular was 4.3.2.  `msolve -V` returned exactly `0.10.1`, and
`/usr/local/bin/msolve` had the official SHA-256
`0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`.

All four wrappers were launched detached through the frozen `dispatch.sh`.
Each has an inner
`timeout --signal=TERM --kill-after=60s 10200s` and a slightly wider outer
dispatch guard.  They started within 64 seconds and ran concurrently:

| label | computation | field/order | start UTC | terminal status |
|---|---|---|---|---|
| (a) | `std(I+(Tc-1))` | exact ℚ; separate `T`/weighted blocks | `2026-09-05T17:00:52Z` | timeout 124 at `19:50:52Z` |
| (b) | modular Hilbert seed, then `guided_gb` | (S=(I:c^\infty)); wp | `2026-09-05T17:01:46Z` | driver error 1 at `19:46:49Z` |
| (c) | modular F4, `-g 2 -t 32 -v 2 -l 44 -m 2000` | (c=1), (p=1073741827) | `2026-09-05T17:01:51Z` | timeout 124 at `19:51:52Z` |
| (d) | `slimgb(I|_{c=1})` | exact ℚ; dp | `2026-09-05T17:01:56Z` | timeout 124 at `19:51:57Z` |

Job (b) first runs an ordinary modular `std(S)` at (p=32003), then computes
`hilb(HG,1,weights)`.  The full returned integer vector, including exactly
one trailing Singular bookkeeping zero, is the `HilbertHint` passed to the
frozen `guided_gb.py`.  Fresh fibres (p=32009,32027) then run
`std(S,HNUM,WTS)` in parallel.  The helper's CRT stage reconstructs only
`dimension`, leading-ideal dimension/vector-space dimension, and basis size;
it reconstructs neither basis coefficients nor an identity.  Its promotion
scope is deliberately `NONE`, `allow_modular_unit_promotion=false`, and the
inapplicable positive-dimensional perturbed-Hilbert heuristic is disabled.

Before (c) started, an independent parser recounted 69 variables, 66
generators and 65,990 expanded terms after token-level (c\mapsto1).  It
computed

\[
65{,}990\cdot69=4{,}553{,}310<2{,}147{,}483{,}647,
\]

a 471.6-fold signed-32-bit margin.  It also required a bijective source-to-
`v1,...,v69` map, exact comma termination, no denominators, and no parentheses.
The machine result is `results/c_c1_msolve/guard.json`; matching variable names
alone were not used as a ring map, as required by `FALLACY-v2.md:20-21`.

## 6. Results and resource record

| job | elapsed evidence | furthest trustworthy state | sampled peak RSS |
|---|---:|---|---:|
| (a) exact `std` | 10,200 s | controls passed; entered `std`; no return marker | 11,956,276 KiB |
| (b) Hilbert/guided | 9,900 s seed | saturation seed still in `std`; no `HNUM` marker | 91,863,060 KiB* |
| (c) msolve F4 | 10,200 s | incomplete F4; last preserved progress: degree 8, counter 269,752 | 41,736,680 KiB |
| (d) exact `slimgb` | 10,200 s | controls passed; entered `slimgb`; no return marker | 2,532,352 KiB |

`*` The (b) maximum is the original `/usr/bin/time -v` value captured before
a duplicate launch truncated that file; its last scheduled-process sample was
87,784,868 KiB at 9,000 seconds.  The original time record also gave user
9,831.45 s, system 83.70 s, elapsed 2:45:02, no swap, and exit 1.  The executed
driver contains `timeout=9_900`; this is an operational deviation from the
requested 170-minute watchdog, not a solver verdict.

Each wrapper sampled the full relevant process table and byte-valued memory
totals immediately and every 900 seconds in `rss-15min.log`; `/usr/bin/time -v`
records the final peak.  The controller also polled all four dispatch logs and
an explicit process/RSS table.  This matters because the stock dispatch poll
counts Singular globally and does not see msolve.  The per-job logs contain 12
scheduled samples for (a), 12 original samples plus one duplicate-start sample
for (b), 12 original samples plus one duplicate-start sample for (c), and 12
for (d).  The maximum controller-poll `used` memory was 150,911,524,864 bytes
(about 140.6 GiB), leaving over 350 GiB of the 495-GiB worker; no swap or OOM
event occurred.

No result is inferred from silence, process death, a return code alone, or a
modular leading ideal.  The positive/negative controls precede both exact
computations.  In particular, (c)'s live F4 progress is not a basis, and (b)
never completed even the Hilbert seed.  Therefore the promotion matrix is:
exact UNIT **absent**; modular UNIT **absent**; original-ring rational identity
**absent**; c^N lift **not applicable**; completed NONUNIT basis **absent**;
dimension/degree/sample point **not available**.  Calling either a kill or a
survivor here would violate the frozen rules.

## 7. Why the (c=1) section is licensed, and what a lift would mean

For ((\ell+1,D)=(2,39)), choose ((A,B)=(20,-1)), so
(20\cdot2-39=1).  With

\[
k(z)=20b-(iK-a),\qquad k(c)=1,
\]

the frozen cone lemma gives the explicit Laurent product

\[
(\mathbb Q[z,c]/I)[c^{-1}]
 \simeq (\mathbb Q[z]/I|_{c=1})[s,s^{-1}],
\]

and therefore

\[
I+(Tc-1)=(1)\quad\Longleftrightarrow\quad I|_{c=1}=(1).
\]

This needs no rational-point assumption or root extraction
(`/tmp/jc2-lane.68h1yv/inputs/graded-moh-astra-r2-20260905.md:37-58`).
Nevertheless a modular section UNIT is not promoted.  Given an **exact**
section identity (1=\sum h_i(z)f_i(z,1)), the required recorded lift expands
each cofactor into monomials (m), sets
(k_i=20u_i-v_i) for (deg f_i=(u_i,v_i)), chooses
(N\ge\max(1,k(m)+k_i)), and verifies in the original ring

\[
c^N=\sum_{i,m}\operatorname{coeff}_m(h_i)
c^{N-k(m)-k_i}m f_i(z,c).
\]

The exact formula and its nonnegative-exponent justification are frozen at
`:58-62`; conversion to a Rabinowitsch identity is at `:92`.  A lift is
reported only if the multiplication was actually checked, with declared row
order and ring maps.

## 8. Source-support consumption and FALLACY-v2 audit

The source-support theorem applies under (H1) licensed minimal descendant and
effective characteristic data, (H2) root replacement (Q=T_1^\psi(P)) with
the printed (M_1=-m') normalization, and (H3)
(d=-\delta_{s'}=(\ell+1)/(n'-M'_{s'}-1)>0).  These conditions and the
consumption statement are
`/tmp/jc2-lane.68h1yv/inputs/gi-only-charts-sol56-20260905.md:87-114`.
The theorem says that the full (G_i) chart receives every actual source in
the class.  It does not say that this necessary receiver is attained.

Accordingly:

- an exact-Q UNIT with complete controls is a class kill;
- a modular UNIT is a screen until an exact original-ring certificate exists;
- a NONUNIT basis is not an actual Moh source or counterexample;
- a lower bound, representative, or stopped computation is not attainment;
- no support coordinate, generator, or torus branch is silently omitted.

The full-envelope warning is frozen at `:392-410`, and the promotion boundary
at `:411-417`.  The `sat()` component and controls, explicit field/ring map,
and no-floor-to-attainment requirements were checked against
`/tmp/jc2-lane.68h1yv/inputs/FALLACY-v2.md:9-21`.  No new exit-price assertion
is made, so the `charge_basis` declaration rule at `FALLACY-v2.md:32-36` does
not apply.

## 9. Collection, termination, and reproducibility

Collection exposed a dispatch-controller defect.  A controller shell blocked
behind (a), then launched a duplicate (b) at `19:50:53Z`; after its exact
process groups were stopped about 162 seconds later, it advanced to a duplicate
(c) at `19:53:35Z`.  These launches truncated several top-level logs.  Neither
is admitted as mathematical evidence.  The original (b)/(c) return-code mtimes,
the append-only RSS samples, the controller polls, and the captured (b) time
record preserve the claims above.  `custody/b-driver-incident.md` enumerates
the affected files and PIDs; `custody/remote-final-processes.log` records the
57-second duplicate c process immediately before shutdown.

The failsafe observed the exact instance still running at `19:54:31Z`, made a
final collection at `19:54:33Z`, and requested termination only for
`i-0b29f3356aaf6ef81`.  `custody/instance-final.json`, written at `19:55:37Z`,
reports `State: terminated`, the requested `r7i.16xlarge` type, launch time,
and owner.  Thus the paid worker was terminated before this report was sealed.

The complete reproducible bundle is `box/gi70-longsolve-20260905/`:

- `build_payload.py`, `custody/chart.json`: independent chart/grading emission;
- `inputs/`: exact weighted, modular-Hilbert, c=1 msolve, and c=1 slimgb inputs;
- `jobs/`: the four detached 10,200-second wrappers and RSS sampler;
- `run_guided.py`: Hilbert seed plus two-prime guided/CRT orchestration;
- `guard_msolve.py`: independent 32-bit and map check;
- `dispatch-logs/`, `results/`, `logs/polls.log`: collected primary output;
- `custody/`: receipt manifest, payload checks, worker facts, and termination state.

The honest compute answer is therefore **OPEN / COMPUTE-BOUND**.  This run
neither kills `C_n24m16_Mm12_m2_5_ell1_s4` nor exhibits a necessary-chart
survivor.  It does establish that the three full-watchdog methods did not
finish at this scale, that the modular Hilbert seed alone reached about
87.6 GiB before its shorter driver timeout, and that msolve reached degree 8
without approaching the machine's memory ceiling.  All interpretations above
are bounded by the frozen source-support and FALLACY-v2 rules.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15160`.
- Body SHA-256:
  `f14dcb1b4fc7f0ffe4a5b304ad90f3af99369a1292df1152d6f172194448a56b`.
- Frozen basis: `da92fdf2ed051564475f74c2960d0f934c52990f`.
