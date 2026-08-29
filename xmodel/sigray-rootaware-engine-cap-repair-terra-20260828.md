# Sigray root-aware engine cap repair

Date: 2026-08-28 16:15:45Z  
Producer: GPT-5.6-terra / Codex  
Scope: follow-up engine repair after the hostile review
`xmodel/sigray-rootaware-engine-hostile-review-gpt55-20260828.md` at SHA-256
`e9245ec8d8b33d66a7f0c0365d891d15f8068894dc7e0e467d503556b4f3b255`.
The original patch map remains
`a7fb8f1dc83361fa4c4d2f4f4acc71eee4b9b05f16094423d42e55f268640519`.
The prior implementation report remains immutable at
`e8d823fe8f084bdbb58630cbaff532377c282517c2919f91b9c99c0cd7c3d896`.
No canonical prose was edited. `jc2-lean` was not entered, listed, searched,
read, built, modified, status-checked, or controlled.

## 1. Verdict

**HOSTILE-REVIEW BLOCKER PATCHED; lightweight deterministic gates pass.**

The common engine no longer performs a capped search for the zero-charge
`MU1` branch. It solves that branch exactly over every `l>=0` and `m>=m0`.
The hostile witness at `l=98` is therefore emitted even when a caller passes
the nominal value `KMAX=0`, and its child is classified
`TERMINAL_ROOT_M1`.

All other zero-charge caps in the five repaired consumers were audited. A
finite truncation now has one of four explicit dispositions: an exact
arithmetic solution, an `OPEN/NO_VERDICT` outcome, a recorded BFS frontier,
or an expressly non-exhaustive diagnostic rider. No new full census was run;
promotion still requires hostile re-review and AWS reruns.

## 2. Exact unbounded `MU1` solve

For `MU1`,

```text
dp = 1,  dq = l+2,  l>=0,
dp*(c*m+e) = dq*(a*m+b),
a = c.
```

Put `r=l+1` and `X=a*m+b`. On the admissible ray, `X>0`. The equation is
equivalent to

```text
r X = e-b.
```

If `a>0`, every solution comes from a positive divisor `X | (e-b)` with
`X congruent to b (mod a)`:

```text
m = (X-b)/a >= m0,
l = (e-b)/X - 1 >= 0.
```

Conversely, those formulas satisfy the original equation, so this is an
exact finite divisor enumeration with no `l` or `m` cap. If `e-b<=0`,
positivity of `X` proves there is no solution. If `a=c=0`, the equation is
independent of `m`; an integral `r=(e-b)/b>=1` gives the exact all-`m>=m0`
family. The engine reports that degenerate family `OPEN` instead of treating
it as a finite-search closure.

The nominal `KMAX`, `NUSWEEP`, and `MSWEEP` arguments are deliberately
ignored for `branch='MU1'`.

### Hostile witness

```text
Q = (rho=1/100, nu=101, M=1, kappa=100)
red = (a,b,c,e,m0) = (100,1,100,100,0)
e-b = 99
X = 1  =>  m=0, l=98
```

Observed locally:

```text
KMAX=0: points=[(98, 1, 0)] families=[] cert=EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b=99
KMAX=48: points=[(98, 1, 0)] families=[] cert=EXACT MU1 divisor solve: (l+1)(a*m+b)=e-b=99
child=Q[rho=1/100,nu=1,M=1,kap=1,pc=1] lambda=0 disposition=TERMINAL_ROOT_M1
```

## 3. Zero-charge cap audit

| Site | Finite mechanism | Repaired disposition |
|---|---|---|
| `sheet6_campaign.solve_pattern(...,'MU1')` | Former `l<=48` | Exact divisor solve for all `l,m`; nominal caps ignored. |
| `MU1`, `a=c=0` | Infinite all-`m` family | Exact degenerate family, consumed as mandatory `OPEN`. |
| `sheet6_campaign` `IIa_0` | `l<=48`, `nu<=1200`, `m<=1200` | Mandatory zero-charge `OPEN/NO_VERDICT` tail on every call. |
| Common zero-charge child realization | finite parameter samples and residue splits | Any unresolved `None`/`SKIP` realization is an explicit `OPEN/NO_VERDICT`; unresolved split periods were already `OPEN`. |
| Common parametric reduction | finite `s` fallback | Existing `s>=6` `OPEN` retained with zero lower charge for `MU1`/`IIa_0`. |
| Common chain traversal | depth cap | Existing `frontier` prevents an exclusion verdict. |
| `h3_check` chain/root scans | depth 7 and parametric `s<=40` | Depth is counted as `NO_VERDICT`; every unproved parametric `s>40` remainder carries `OPEN_s_tail`, propagated by HIII, TDU, and two-pole suffix consumers. |
| `twopole_check.mu1_children` | `nuF<=24`, `l<=4` | Mandatory `OPEN/NO_VERDICT` tail. |
| Two-pole parametric premerge | instances `s<=5` | Mandatory `OPEN/NO_VERDICT` tail; the finite merge join prints an additional rider. |
| Two-pole premerge/L1 traversal | depth 6 | Recorded `NO_VERDICT` frontier/tail. |
| Two-pole phase-2 merge enumeration | `S<=12`, `nu<=48`, `l<=4` | Always labeled a capped diagnostic with an explicit `NO_VERDICT` rider; no general closure claim. Positive `k` is budget-priced, but the rider covers the uncharged `k=0` tails. |
| L1 zero-chain menu | Former finite `l` menu | Uses the exact common `MU1` solver. |
| L1 merge display | `nu<=48`, `l<=8` | Programmatic `NO_VERDICT-L1-MERGE-CAPS`; premerge cap tails are also returned as `NO_VERDICT-L1-PREMERGE-TAILS`. |
| Two-pole phase-3 root menu | `k,l<=4` | Complete only for the conditional `td=6` budget screen: `ratio_kl=dq`, `psi=dq-1=k+l+1`, nonnegative lambda and `tot<=5-psi` force `k+l<=4`. Outside that screen the cap is explicitly diagnostic. |

This audit does not promote historical positive-charge finite boxes to
theorem-grade completeness. They remain subject to analytic certification or
AWS widening. The point of this repair is narrower: no uncharged tail can be
silently converted into a closed verdict.

## 4. Root/nonroot and Section 7 status retained

The prior root-aware implementation remains intact:

- root signature `(nu,kappa-bar)=(1,1)` is recognized before any `M=1`
  filter;
- `mu=1` single-orbit and `mu=2` case-I root-capable children are constructed;
- `mu=2` IIb/III `M=1` deaths remain explicitly certified nonroot;
- root `M=1` and root `M>1` are separate terminal dispositions;
- pinned pole entries pass explicit nonroot metadata;
- the two-pole root menu contains `l>=1` and distinguishes the exactly locally
  solvable `l=1`, even-`l` logarithmic death, odd-`l>1` no-log-obstruction,
  and otherwise unchecked root ODE cases.

Every exclusion-grade global-budget string is conditional on the currently
accepted Section 7 weighted inequality / first-separation ledger. The failed
fixed-weight `(22-cl)` route is not cited as proved.

## 5. Exact changed-file hashes

```text
6905f95e6eeca8f3a8a8468b4c5f56fc131dd4206b2827050ac04ea1939ead8f  cases/sheet6_campaign.py
defcaee8367337d9d882e46fbba1b71bc2db0ce48aaffcf5e44a929d391f3e50  cases/h3_check.py
9a7a0fce73d08f243956d64ff8a85c82a15b9c81f0d07d7cacc0162212fcaf3a  cases/hiii_compose.py
b078c88424c566a8dd37c368e57e9e2aa8932f1bbde49d0c58580940eab806f3  cases/twopole_check.py
c37067fd9f923853ef3a7d5d23c255983e7273466c0df29acf44200c5f29426c  cases/monodromy_td.py
0baf1d54328f0f9829126672536673af277068d4b6dda0221fd94b3c0994d212  cases/sigray_rootaware_smoke.py
```

## 6. Lightweight local verification

No command below exceeded ten seconds. No full census, Singular job, or
heavy algebra computation was run locally.

Syntax and root/cap smoke:

```text
python3 -m py_compile cases/sigray_rootaware_smoke.py cases/sheet6_campaign.py \
  cases/h3_check.py cases/hiii_compose.py cases/twopole_check.py \
  cases/monodromy_td.py
python3 cases/sigray_rootaware_smoke.py

PASS disposition root/NR/pole certificates
PASS sheet6_campaign.bash root-before-M filter
PASS mu=1 single-orbit and mu=2 case-I root emission
PASS unbounded MU1 l=98 and mandatory zero-charge cap residues
PASS twopole suffix root-before-M filter
PASS h3 and hiii BFS root-before-M filters
PASS twopole l>=1 menu, ODE parity, parent reach, and l=1 emission
PASS static no raw child.M==1 BFS shortcuts
ROOT-AWARE SMOKE PASS: 8 checks
```

The cap smoke checks the hostile `l=98` witness under nominal caps
`0,1,48,120`, requires identical exact point sets, rejects a box/KMAX
certificate, checks the exact `a=c=0` all-`m` family, requires mandatory
`IIa_0` and two-pole `OPEN/NO_VERDICT` tails, and requires H3's parametric
`OPEN_s_tail`.

Legacy arithmetic gates:

```text
GATE PASS: Prop 9.1 11/11; Stmt 9.6 pairs {(21,15),(20,16)} + erratum (75,51) reproduced; engine reproduces St 9.6 (iii),(iv),(v) with lambdas 2,2,0
TDU GATE PASS: tdu_rows == prop91 slices td=3..7; prime-td closed form verified for the 11 primes <= 40
COMPOSE GATE PASS: 4 tails3 witnesses reproduced by E5 closed forms
L1-CAP GATE PASS: shapes=26 no_verdict_records=26 distinct=26
```

`git diff --check` on the five requested engine files and the smoke file
passed with no output. The hostile-review and prior-report SHA sidecars both
verified `OK` before this report was written.

## 7. Remaining AWS reruns and no-verdict boundaries

After hostile re-review, run on AWS only:

1. common `bash`, `bash5`, `bash6`, `tduniform`, and selected `tdu_bash`
   jobs, retaining root, IV, `OPEN`, and frontier ledgers separately;
2. H3 SF1 and HIII ordinary/pinned/AF2 compositions, including the new
   `OPEN_s_tail` counts;
3. two-pole premerge, interior merge, root merge, and L1 phases with raised
   diagnostic `S`, `nu`, `l`, `s`, and depth caps;
4. before/after invariants for certified nonroot transitions and singleton-pole
   entry deaths;
5. an independent check that every reported closure uses either an exact
   arithmetic certificate or an explicitly accepted conditional budget bound.

The general two-pole merge and L1 displays remain capped diagnostics. Root
ODE classification is complete only for the stated all-`mu=1`, `k=0` parity
cases; larger odd `l` is not asserted globally solvable, and all other root
ODE cells remain unchecked. H3's parametric tail remains `NO_VERDICT` until
an all-`s` arithmetic classifier replaces the finite diagnostic. Global
budget conclusions remain conditional on Section 7.

There is no remaining implementation ambiguity in the exact `MU1` grammar.
The remaining work is hostile re-review, AWS recensus, and analytic closure of
the explicitly recorded no-verdict boundaries.
