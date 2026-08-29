# Hostile re-review: Sigray root-aware engine cap repair

Date: 2026-08-28
Reviewer: GPT-5 / Codex
Scope: exact re-review of the cap repair after
`xmodel/sigray-rootaware-engine-hostile-review-gpt55-20260828.md` and
`xmodel/sigray-rootaware-engine-cap-repair-terra-20260828.md`.

## 0. Verdict

**PASS.**

The prior blocker is repaired. The zero-charge `MU1` branch is no longer a
finite `KMAX` search. It is solved exactly by divisor enumeration, and the
hostile `l=98` witness is emitted even when `KMAX=0`; the resulting child has
the root signature and is classified `TERMINAL_ROOT_M1`.

I did not find a remaining path where a zero-charge, depth, parameter, or
unbounded cap is silently promoted to absence. Within the repaired consumers,
uncertified tails are surfaced as `OPEN`, `NO_VERDICT`, `RESIDUE`, frontier
counts, or an explicit diagnostic rider. The two-pole `td=6` root-menu
`l<=4` completeness statement is correctly conditional on the repaired
singleton budget screen, not a general root-menu theorem.

No engine or canonical document was edited by this review. The only write was
this report and its SHA-256 sidecar. `jc2-lean` was excluded from traversal and
was not entered, listed, searched, read, built, modified, status-checked, or
controlled.

## 1. Custody

The repaired report hash was verified before review and matches the required
hash:

```text
93f98e4df5fd67536f3a5ab9c6f948a6bb06bbdbd10b825980596cc865c811d5  xmodel/sigray-rootaware-engine-cap-repair-terra-20260828.md
```

Both report sidecars verified:

```text
xmodel/sigray-rootaware-engine-hostile-review-gpt55-20260828.md: OK
xmodel/sigray-rootaware-engine-cap-repair-terra-20260828.md: OK
```

Original hostile-review hash:

```text
e9245ec8d8b33d66a7f0c0365d891d15f8068894dc7e0e467d503556b4f3b255  xmodel/sigray-rootaware-engine-hostile-review-gpt55-20260828.md
```

Controlling Section 7 and Section 8 inputs checked:

```text
758c022696da6dbafaf7c907af25d733162ece203cc6599a30a903de03c93840  xmodel/sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
f31f948747656102a529eeac54e66a6a66ba67bdbbc922c1fa3fbac1f75598de  xmodel/sigray-section7-kappa-variation-salvage-gpt55-20260828.md
fa25c8afe524a2bcecc305de50dc57831534a01e66614592a591acab393709f3  xmodel/sigray-section8-full-hostile-review-opus5-20260828.md
```

The controlling Section 7 state is the later actual-weight hostile review:
the amended one-point Lemma 3.2 route is `PASS`, proving the numerical
content of repaired Corollary 7.1 for prescribed fibres and distinct
critical-value flags, while explicitly not restoring printed equation `(22)`,
printed per-puncture `delta`, or fixed-weight `(22-cl)`. The older final
delta gate and kappa-variation reports remain relevant negative controls:
they explain why the fixed transport route failed.

The controlling Section 8 state is: Statement 8.4's direct gcd form is valid
including the root edge, but corrected Proposition 8.4 is a nonroot theorem
only. Every use of an `M=1` kill must therefore either have a certified
nonroot down vertex or first preserve/report the root signature. Pole entries
may use independent pole metadata as a nonroot certificate.

## 2. Reviewed File State

Current repaired file hashes match the cap-repair report:

```text
6905f95e6eeca8f3a8a8468b4c5f56fc131dd4206b2827050ac04ea1939ead8f  cases/sheet6_campaign.py
defcaee8367337d9d882e46fbba1b71bc2db0ce48aaffcf5e44a929d391f3e50  cases/h3_check.py
9a7a0fce73d08f243956d64ff8a85c82a15b9c81f0d07d7cacc0162212fcaf3a  cases/hiii_compose.py
b078c88424c566a8dd37c368e57e9e2aa8932f1bbde49d0c58580940eab806f3  cases/twopole_check.py
c37067fd9f923853ef3a7d5d23c255983e7273466c0df29acf44200c5f29426c  cases/monodromy_td.py
0baf1d54328f0f9829126672536673af277068d4b6dda0221fd94b3c0994d212  cases/sigray_rootaware_smoke.py
```

Tracked diff numstat:

```text
74      26      cases/h3_check.py
32      15      cases/hiii_compose.py
1       1       cases/monodromy_td.py
226     44      cases/sheet6_campaign.py
196     69      cases/twopole_check.py
```

`cases/sigray_rootaware_smoke.py` is a new 224-line smoke file; I inspected it
with a no-index diff and direct line-numbered reads.

## 3. Exact `MU1` Solver

For `MU1`, the common reduction gives

```text
dp = 1, dq = l + 2, l >= 0, nu_F = 1,
dp*(c*m+e) = dq*(a*m+b), and a = c.
```

So

```text
c*m + e = (l+2)(a*m+b)
a*m + e = (l+2)(a*m+b)
e - b = (l+1)(a*m+b).
```

Put `r=l+1` and `X=a*m+b`. On every valid reduced ray, the code asserts
`a>=0` and `a*m0+b>0`, hence `X>0` for all `m>=m0`. Therefore:

- If `e-b<=0`, there is no positive `r*X` solution.
- If `a>0`, every solution corresponds exactly to a positive divisor
  `X | (e-b)` satisfying `X == b mod a`, with
  `m=(X-b)/a >= m0` and `l=(e-b)/X - 1 >= 0`.
- Conversely, every such divisor satisfies both
  `(l+1)(a*m+b)=e-b` and the original
  `c*m+e=(l+2)(a*m+b)`.
- If `a=c=0`, then `b>0` by positivity. The equation is independent of `m`;
  when `b | (e-b)` and `r=(e-b)/b>=1`, the exact solution is the all-`m>=m0`
  family at `l=r-1`. The engine returns this as an `OPEN` degenerate family,
  not a finite closure.

The implementation at `cases/sheet6_campaign.py:123-176` matches this
derivation. `solve_pattern(..., branch='MU1')` dispatches to it before the
finite `KMAX/NUSWEEP/MSWEEP` loops at lines 179-195.

Hostile witness reproduced:

```text
witness_red {'a': 100, 'b': 1, 'c': 100, 'e': 100, 'm0': 0, 'n0': (0, 1), 'style': 'II'}
cap 0 pts [(98, 1, 0)] fams [] cert EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b=99
cap 1 pts [(98, 1, 0)] fams [] cert EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b=99
cap 48 pts [(98, 1, 0)] fams [] cert EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b=99
cap 120 pts [(98, 1, 0)] fams [] cert EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b=99
root_outcomes [(0, (Fraction(1, 100), (0, 1), 1, (0, 1)), 'TERMINAL_ROOT_M1')]
bash_root_count 1 open_count 0 frontier_count 0
MU1_EXACT_BRUTE_PASS 10920
```

The brute check exhaustively compared the exact solver with direct equation
search for 10,920 valid small reduced cases, including negative `b` cases
with positive admissible ray, `e-b<=0`, ordinary divisor cases, and the
`a=c=0` all-`m` family.

## 4. Cap And Propagation Audit

`cases/sheet6_campaign.py`

- `MU1` is exact and ignores `KMAX`.
- `IIa_0` still uses a finite box, but `step_one_branch()` now appends a
  mandatory zero-charge `OPEN ... NO_VERDICT` tail before consuming results
  (`lines 412-420`).
- Zero-charge child realization failures, unresolved residue splits, and
  `SKIP` outcomes are converted to `OPEN ... NO_VERDICT`
  (`lines 428-455`).
- S-dependent fallback has lower charge zero for `MU1` and `IIa_0`
  (`lines 495-500`).
- `bash()` carries `OPEN`, depth frontier, and root terminals into the final
  verdict; it excludes only when all three are empty (`lines 520-547`).
- `tdu_bash()` propagates root hits, opens, `OPEN_s_tail`, and frontier counts
  (`lines 893-952`).

`cases/h3_check.py`

- Parametric IV checks append `OPEN_s_tail` at `SMAX+1` (`lines 65-69`).
- `run()` records opens and depth frontier before printing a `NO_VERDICT`
  summary (`lines 81-120`).
- IV rows with an `OPEN_s_tail` are not reported as psi-killed; the class
  priority is `SURVIVOR`, then `OPEN_s_tail`, then conditional psi kill
  (`lines 127-147`).
- Root-signature children are reported separately from IV survivors
  (`lines 189-209`).

`cases/hiii_compose.py`

- E5 case-III children are explicitly nonroot-scoped by `nuF>=2`; `MF<2`
  cannot hide a root terminal (`lines 74-83`).
- Unlocked parametric III nodes return `OPEN_E5U`; consumers may budget-kill
  them only through the exact `budget_kill_all_s` certificate (`lines 57-58`,
  `214-220`).
- `run_compose()` applies root-first disposition, preserves `OPEN`, carries
  `OPEN_s_tail`, and prints frontier counts (`lines 205-268`).
- The return value remains the legacy IV ledger; no current caller uses it as
  a closure certificate.

`cases/twopole_check.py`

- `mu1_children()` appends a mandatory zero-charge premerge
  `NO_VERDICT` tail for `nuF>24` or `l>4` (`lines 68-82`).
- Parametric premerge instances beyond `s>5` and depth frontier are recorded
  as `NO_VERDICT` (`lines 99-102`, `116-122`).
- `suffix_bash()` returns `RESIDUE` when there is any IV survivor, open tail,
  root signature, unresolved M1 scope, or frontier (`lines 209-269`).
- Phase 2 finite merge enumeration is explicitly printed as a capped
  diagnostic with an unenumerated-tail rider before it is consumed
  (`lines 543-546`). The raw `all_merges()` generator itself is not a
  theorem-grade closure API.
- `l1_premerge()` returns no-verdict tails when requested, and `l1_stage()`
  installs `NO_VERDICT-L1-MERGE-CAPS` and
  `NO_VERDICT-L1-PREMERGE-TAILS` (`lines 347-392`, `483-489`).
- The phase-3 root menu includes the `l>=1` family and records exact
  `l=1`, even-log-dead, and odd-no-log-obstruction ODE status
  (`lines 272-294`).

`cases/monodromy_td.py`

- The only change is wording: singleton `b=1` entry filtering is described as
  corrected nonroot Proposition 8.4 (`lines 514-521`). The multi-pole
  non-promotion boundary remains explicit.

`cases/sigray_rootaware_smoke.py`

- The smoke suite tests root/nonroot disposition, shared BFS ordering, restored
  `mu=1` and `mu=2 I` root branches, the hostile `l=98` witness under caps
  `0,1,48,120`, `a=c=0` degenerate family reporting, mandatory zero-charge
  tails, H3/HIII root-first consumers, two-pole root menu parity, parent reach,
  L1 `l=1` root emission, and static absence of raw BFS `child.M==1` filters.

Static scan result:

```text
No remaining raw BFS filters of the form child.M == 1, ch.M == 1, or c2.M == 1
were found in the repaired consumers.
```

## 5. Root Scope And Budget Wording

The implementation now matches the Section 8 boundary:

- root signature `(nu,kappa-bar)=(1,1)` is tested before any `M=1` filter;
- constructed nonroot-looking `M=1` children are killed only through the
  centralized root-first disposition;
- pole/pinned entries pass explicit `certified_nonroot=True`;
- root `M=1` and root `M>1` are separate terminal dispositions.

The implementation also matches the Section 7 wording boundary. Patched
strings refer to the accepted Section 7 weighted budget / first-separation
ledger. I found no use of fixed-weight `(22-cl)` as a proved engine budget.

For two-pole phase 3, the `td=6` root `l<=4` statement is correctly
conditional. In `root_merges()`, `ratio_kl == dq`, so `psi=dq-1=k+l+1`.
The conditional budget is `tot <= 5 - psi`, and `tot>=0`; hence any
budget-consistent hit has `k+l<=4`. Since the menu enumerates
`0<=k<=4` and `0<=l<=4`, it covers all budget-consistent `td=6` phase-3 root
hits under that repaired singleton budget. Outside that screen, the file
labels the caps diagnostic only.

## 6. Lightweight Verification

No command below exceeded 30 seconds. No full census, Singular job, or heavy
AWS-style run was executed.

```text
/usr/bin/time -p python3 -m py_compile cases/sigray_rootaware_smoke.py cases/sheet6_campaign.py cases/h3_check.py cases/hiii_compose.py cases/twopole_check.py cases/monodromy_td.py
real 0.07
user 0.03
sys 0.01
```

```text
/usr/bin/time -p python3 cases/sigray_rootaware_smoke.py
PASS disposition root/NR/pole certificates
PASS sheet6_campaign.bash root-before-M filter
PASS mu=1 single-orbit and mu=2 case-I root emission
PASS unbounded MU1 l=98 and mandatory zero-charge cap residues
PASS twopole suffix root-before-M filter
PASS h3 and hiii BFS root-before-M filters
PASS twopole l>=1 menu, ODE parity, parent reach, and l=1 emission
PASS static no raw child.M==1 BFS shortcuts
ROOT-AWARE SMOKE PASS: 8 checks
real 0.27
user 0.24
sys 0.01
```

```text
/usr/bin/time -p git diff --check -- cases/sheet6_campaign.py cases/h3_check.py cases/hiii_compose.py cases/twopole_check.py cases/monodromy_td.py cases/sigray_rootaware_smoke.py
real 0.01
user 0.00
sys 0.00
```

```text
/usr/bin/time -p python3 - <<'PY'
... exact MU1 hostile witness and small brute-force cross-check ...
PY
real 6.19
user 6.09
sys 0.09
```

```text
/usr/bin/time -p python3 - <<'PY'
import sys
sys.path.insert(0, 'cases')
import sheet6_campaign as sc
import hiii_compose as hiii
print(sc.gate())
print(sc.tdu_gate())
print(hiii.gate_compose())
PY
GATE PASS: Prop 9.1 11/11; Stmt 9.6 pairs {(21,15),(20,16)} + erratum (75,51) reproduced; engine reproduces St 9.6 (iii),(iv),(v) with lambdas 2,2,0
TDU GATE PASS: tdu_rows == prop91 slices td=3..7; prime-td closed form verified for the 11 primes <= 40
COMPOSE GATE PASS: 4 tails3 witnesses reproduced by E5 closed forms
real 8.98
user 8.85
sys 0.12
```

## 7. Promotion Boundary

This PASS is code-level and cap-repair specific. It does not promote any
historical full census, AWS result, root ODE theorem beyond the stated parity
cells, general two-pole merge closure, L1 merge closure, or fixed-weight
Section 7 route.

After this review, the remaining required work is still the external recensus
and analytic closure of the explicitly recorded no-verdict boundaries. The
specific hostile blocker from the previous review is gone.
