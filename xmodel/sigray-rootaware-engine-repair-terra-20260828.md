# Sigray root-aware engine repair

Date: 2026-08-28 15:43:44Z  
Producer: GPT-5.6-terra / Codex  
Scope: engine-only implementation of
`xmodel/sigray-canonical-consumer-patch-map-terra-20260828.md` at SHA-256
`a7fb8f1dc83361fa4c4d2f4f4acc71eee4b9b05f16094423d42e55f268640519`.
No canonical prose was edited. `jc2-lean` was not entered, listed, searched,
read, built, modified, status-checked, or controlled.

## 1. Verdict

**IMPLEMENTED; lightweight gates pass. Full census verdicts remain pending
root-aware AWS reruns and hostile review.**

The previous engines could discard `M=1` before learning that a child had the
root signature `(nu,kappa-bar)=(1,1)`. They also suppressed two root-capable
transition grammars before constructing a child. The repaired engines now use
one shared root/nonroot disposition API, recognize a root terminal before the
nonroot Proposition 8.4 filter, and keep root `M=1` as a candidate.

## 2. Implementation

### Shared disposition and transition grammar

`cases/sheet6_campaign.py` now exports:

- `has_root_signature(node)`;
- `dispose_m1(node, certified_nonroot=...)`, with the explicit dispositions
  `KEEP`, `KILL_NR_M1`, `TERMINAL_ROOT_M1`, `TERMINAL_ROOT_M_GT1`, and
  `UNRESOLVED_M1_SCOPE`;
- `dispose_constructed_child(node)`, which performs root recognition first
  and then supplies the transition grammar's nonroot certificate.

An explicit `certified_nonroot=True` overrides a numerical root-like fixture.
This is needed for a pinned pole entry: pole metadata proves nonrootness, so
its `M=1` remains dead.

The abstract `KILL_M1` outcomes were deleted. Two previously hidden branches
are now constructed:

1. `mu=1`, one residual root orbit. This is not an invented degree pattern:
   the proof of Sigray Statement 9.6 writes
   `p=eta^nu-c^nu`, `deg(q)=n nu+1`, `n>=1`. Specializing the existing
   `IIa_0` degree law to the possible root value `nu_F=1` gives
   `deg(p)=1`, `deg(q)=l+2`, `l>=0`, `M_F=1`, and zero exit charge.
2. `mu=2`, case I. Its `M_F=1` child is now constructed because `nu_F=1`
   can be the root. The `mu=2` IIb/III shortcuts remain absent from the
   common graph because their grammar forces `nu_F>=2`, so their `M_F=1`
   cells are certified `NR-M1`.

All common BFS paths now use the order

```text
budget -> root-terminal recognition -> certified NR-M1 kill -> enqueue.
```

`bash` and `tdu_bash` collect root hits separately. The legacy arithmetic
gate filters the certified-nonroot survivor graph, so adding terminal root
records does not corrupt its historical expected list. The `cong_survivors`
raw `M_F>=2` filter is explicitly scoped by `nu_F>=2`.

### Consumer engines

- `cases/h3_check.py`: records root terminals before `M=1`; the SF1 scan is
  terminal-aware and includes `M` in its deduplication key. Its grand count is
  now explicitly an IV-survivor count, with root terminals separate.
- `cases/hiii_compose.py`: records `TERMINAL_ROOT_M1` and root `M>1` before
  the nonroot filter. The E5 `M_F<2` site now carries an explicit
  `nu_F>=2` assertion. Pinned entry deaths call the central API with a pole
  certificate. Returned legacy counts remain IV-only and are labelled so.
- `cases/twopole_check.py`: `suffix_bash` requires an explicit
  `certified_nonroot` keyword; descendants use root-first disposition. The
  phase-3 root menu now includes `l>=1`, with
  `dp=mu_1+mu_2+k`, `dq=k+2+l`, before applying the parent
  `kappa-bar<nu` reach test. The all-`mu=1`, `k=0` ODE cases are separated:
  even `l` is tagged log-dead, `l=1` is tagged exactly locally solvable, and
  larger odd `l` is retained as having no log obstruction. Other root ODE
  cells are `ROOT_ODE_UNCHECKED`, never silently killed. The L1 stage likewise
  recognizes the root first, retains odd-root cells, and applies its old ODE
  death only to nonroot `nu=1` cells.
- `cases/monodromy_td.py`: comment-only clarification that the singleton
  `b=1` filter is corrected Proposition 8.4 at a nonroot pole entry.
- `cases/sigray_rootaware_smoke.py`: new deterministic seven-check gate.

## 3. Exact changed-file hashes

```text
35f641c22287ba474501cfa5309a750843967929d4322b7ca7c26427afe5018b  cases/sheet6_campaign.py
cfd39d98a2b6e8ce365197f18d00a2b9bb4c7cf364ba92224074c110d4ccb332  cases/h3_check.py
b3bbd69e7a17801347b17a556ef4d4853cd3b055378c00c3b8101e756d78bbcd  cases/hiii_compose.py
310ede4cbef4d89ca05af4739e05b15fee86a451f19233c410289896af11a4bf  cases/twopole_check.py
c37067fd9f923853ef3a7d5d23c255983e7273466c0df29acf44200c5f29426c  cases/monodromy_td.py
ed0d7c4e63689c85ec7f19e4e9cfc3b7c7a4970d3681d0075a78803aff920b91  cases/sigray_rootaware_smoke.py
```

## 4. Local tests (pure Python; no census)

Command:

```text
python3 -m py_compile cases/sigray_rootaware_smoke.py cases/sheet6_campaign.py \
  cases/h3_check.py cases/hiii_compose.py cases/twopole_check.py \
  cases/monodromy_td.py
python3 cases/sigray_rootaware_smoke.py
```

Output:

```text
PASS disposition root/NR/pole certificates
PASS sheet6_campaign.bash root-before-M filter
PASS mu=1 single-orbit and mu=2 case-I root emission
PASS twopole suffix root-before-M filter
PASS h3 and hiii BFS root-before-M filters
PASS twopole l>=1 menu, ODE parity, parent reach, and l=1 emission
PASS static no raw child.M==1 BFS shortcuts
ROOT-AWARE SMOKE PASS: 7 checks
```

Legacy lightweight gates:

```text
GATE PASS: Prop 9.1 11/11; Stmt 9.6 pairs {(21,15),(20,16)} + erratum (75,51) reproduced; engine reproduces St 9.6 (iii),(iv),(v) with lambdas 2,2,0
TDU GATE PASS: tdu_rows == prop91 slices td=3..7; prime-td closed form verified for the 11 primes <= 40
COMPOSE GATE PASS: 4 tails3 witnesses reproduced by E5 closed forms
```

`git diff --check` on the five requested engine files passed with no output.
All local commands completed in under ten seconds. No Singular, large CAS,
or full enumeration ran locally.

## 5. Remaining AWS reruns

After hostile review, rerun on AWS only:

1. `bash`, `bash5`, `bash6`, and the `tduniform`/`tdu_bash` jobs, recording
   root terminals separately from IV and nonroot continuation classes;
2. `h3_check` SF1 and `hiii_compose` ordinary/pinned/AF2 compositions;
3. both two-pole root phases, with raised `l`, depth, and instance caps, and
   an explicit report that the row-1 `td=6` family dies (if it still does)
   at the parent `kappa-bar<nu` reach test rather than at the old l-free or
   blanket-ODE filters;
4. a before/after invariant check that certified nonroot transition and
   singleton-pole entry counts are unchanged.

The old exhaustive root/SF1 and phase-3 counts must remain quarantined until
these reruns land.

## 6. Ambiguities and no-verdict boundaries

- The `mu=1` root degree grammar is source-derived as above, but the common
  solver's `l` search currently inherits its historical cap (`l<=48`). Root
  `l` carries no automatic positive charge, so this cap is not a completeness
  theorem. Raise it on AWS and/or prove an analytic bound before claiming an
  exhaustive root census.
- The two-pole phase-3 menu inherits `L1MAX=4`; the L1 display uses its
  historical default `LMAX=8`. These are finite diagnostic caps, not general
  `l` bounds.
- Only the all-`mu=1`, `k=0` parity obstruction is classified. Larger odd
  `l` is retained, not asserted solvable; all other root ODE patterns remain
  explicitly unchecked.
- This implementation does not promote the repaired Section 7 budget. Every
  census that uses global exit charges remains conditional on `(22-cl)` and
  first-separation ownership.

There is no code-level blocker. The remaining blockers are hostile review,
AWS recensus, and analytic/cap completeness for the uncharged root `l` menu.
