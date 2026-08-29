# Hostile review: Sigray root-aware engine repair

Date: 2026-08-28T15:54:37Z
Reviewer: GPT-5.5 / Codex

## 0. Verdict

**FAIL AS FILED; patchable.**

The root/nonroot ordering repair is mostly correct: constructed children are
budget-filtered, tested for the root signature `(nu,kappa-bar)=(1,1)`, and
only then killed as certified nonroot `M=1`.  The consumers no longer contain
the old raw `child.M == 1` BFS shortcut.

The blocker is completeness accounting, not the root predicate itself.
`cases/sheet6_campaign.py` adds the zero-cost `mu=1` root menu as branch
`MU1`, but the solver still silently caps its `l` variable at `KMAX=48`.
Because this branch has no automatic positive lambda charge, absence of a
child below the cap is not a no-solution certificate.  The current engine can
therefore omit an actual `TERMINAL_ROOT_M1` child and return no `OPEN` or
`NO_VERDICT`.

No engine or canonical prose was edited by this review.  `jc2-lean` was not
entered, listed, searched, read, built, modified, status-checked, or
controlled.

## 1. Custody

Reviewed repair report hash, verified locally:

```text
e8d823fe8f084bdbb58630cbaff532377c282517c2919f91b9c99c0cd7c3d896  xmodel/sigray-rootaware-engine-repair-terra-20260828.md
```

Primary source map, verified locally:

```text
a7fb8f1dc83361fa4c4d2f4f4acc71eee4b9b05f16094423d42e55f268640519  xmodel/sigray-canonical-consumer-patch-map-terra-20260828.md
```

Current Section 7 status checked for budget interaction:

```text
758c022696da6dbafaf7c907af25d733162ece203cc6599a30a903de03c93840  xmodel/sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
f31f948747656102a529eeac54e66a6a66ba67bdbbc922c1fa3fbac1f75598de  xmodel/sigray-section7-kappa-variation-salvage-gpt55-20260828.md
```

Relevant mathematical notes checked:

```text
a0d71267314471e976dff11f6243f6a4e83b92579bdc9e246eafc891a5718384  ladder/SHEET6-H3.md
2cc7c194b9dceacb4e900626677930941ecd46103da259bb2159b4a0314e1bda  ladder/SHEET6-2POLE.md
79ba9ce24b3e977462f701b52961c7df8db0aaffc38b28417b58040b3b126fe6  ladder/SHEET6-L1.md
9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a  ladder/SHEET6-LROOT.md
```

No repository `AGENTS.md` was found under `jc2`, and the explicit parent
checks `/Users/dc/code/math/AGENTS.md` and `/Users/dc/code/math/jc2/AGENTS.md`
produced no instruction content.

## 2. Exact reviewed file state

Current hashes:

```text
35f641c22287ba474501cfa5309a750843967929d4322b7ca7c26427afe5018b  cases/sheet6_campaign.py
cfd39d98a2b6e8ce365197f18d00a2b9bb4c7cf364ba92224074c110d4ccb332  cases/h3_check.py
b3bbd69e7a17801347b17a556ef4d4853cd3b055378c00c3b8101e756d78bbcd  cases/hiii_compose.py
310ede4cbef4d89ca05af4739e05b15fee86a451f19233c410289896af11a4bf  cases/twopole_check.py
c37067fd9f923853ef3a7d5d23c255983e7273466c0df29acf44200c5f29426c  cases/monodromy_td.py
ed0d7c4e63689c85ec7f19e4e9cfc3b7c7a4970d3681d0075a78803aff920b91  cases/sigray_rootaware_smoke.py
```

Diff status of the six requested paths:

```text
M       cases/h3_check.py
M       cases/hiii_compose.py
M       cases/monodromy_td.py
M       cases/sheet6_campaign.py
M       cases/twopole_check.py
untracked cases/sigray_rootaware_smoke.py
```

Tracked numstat:

```text
42      15      cases/h3_check.py
25      12      cases/hiii_compose.py
1       1       cases/monodromy_td.py
127     37      cases/sheet6_campaign.py
126     51      cases/twopole_check.py
```

There was no staged diff for the six requested paths.

## 3. Blocking finding: capped `MU1` can hide a root terminal

Affected lines:

- `cases/sheet6_campaign.py:118-184`: `solve_pattern()` uses finite
  `KMAX=48` for all branches.
- `cases/sheet6_campaign.py:145-154`: the `MU1` branch explicitly disables
  the old ratio-vs-1 no-solution bound, but no replacement bound is proved.
- `cases/sheet6_campaign.py:342-352`: `step_one_branch()` consumes the capped
  result and emits no `OPEN` when the cap is the only obstruction.
- `cases/sheet6_campaign.py:375-415`: `step()` now adds `MU1` to every node.
- `cases/sheet6_campaign.py:456-460`: `bash()` may return no root/open/frontier
  residue after such a silent omission.

Exact local counterexample:

```python
from fractions import Fraction as Fr
import sheet6_campaign as sc

node = sc.Node(Fr(1, 100), 101, 1, 100, 1, tag="root-cap-witness")
red = sc.reduce_ratio(node.rho, node.nu, node.kap, 1, "II")

assert red == {
    "a": 100, "b": 1, "c": 100, "e": 100,
    "m0": 0, "n0": (0, 1), "style": "II",
}

assert sc.step_one_branch(node, 1, "MU1") == []

pts120, _, _ = sc.solve_pattern(red, 1, "MU1", KMAX=120)
assert (98, 1, 0) in pts120

res = sc.child_from(node, red, 1, "MU1", 98, (0, 1), (0, 0))
assert res[0] == "CONT"
assert res[1] == 0
assert sc.has_root_signature(res[2])
assert sc.dispose_constructed_child(res[2]) == sc.TERMINAL_ROOT_M1
```

Observed output from the same probe:

```text
default_step_outcomes []
pts48 []
contains_l98_m0 True
child_l98_lam_child 0 Q[rho=1/100,nu=1,M=1,kap=1,pc=1]
disposition TERMINAL_ROOT_M1
```

This is not a heavy census artifact.  It is a direct one-node arithmetic
witness that the root-aware repair can still lose a root `M=1` terminal.

Minimal line-level patch:

```diff
diff --git a/cases/sheet6_campaign.py b/cases/sheet6_campaign.py
@@
 def step_one_branch(node, mu, branch):
@@
-    pts, fams, cert = solve_pattern(red, mu, branch)
+    pts, fams, cert = solve_pattern(red, mu, branch)
+    if branch == 'MU1':
+        out.append(('OPEN',
+                    f"mu=1 MU1: l>KMAX=48 unenumerated; "
+                    f"no root-completeness bound at {node}",
+                    lam_min))
```

That patch is deliberately conservative.  A stronger repair is acceptable only
if it proves an analytic `l` bound for `MU1` before suppressing the `OPEN`.
The smoke suite should add the synthetic `l=98` witness and require either the
root child to be emitted under the chosen bound or an explicit `OPEN`/`NO_VERDICT`.

## 4. Root/nonroot disposition

The central disposition API is coherent for exact node shapes:

- `cases/sheet6_campaign.py:229-246` recognizes the root signature before an
  `M=1` nonroot kill.
- `cases/sheet6_campaign.py:249-259` treats a constructed child missing the
  unique root signature as certified nonroot.
- Pole and interior-merge callers that possess geometric metadata pass
  `certified_nonroot=True`.

I did not find a current standard first-step child where a parametric
`M=1` family contains an isolated hidden `(nu,kappa)=(1,1)` specialization
while `has_root_signature()` is false.  A first-step-only scan over
`entry_nodes(3..6)` checked 287 constructed continuations in 18.6 seconds and
found zero such records.  A deeper recursive scan was attempted, exceeded the
light-test envelope at 30 seconds, and was interrupted; it is not used as
evidence.

The API is still sharper than the source-map recommendation, which said the
safest engine should require an explicit nonroot assertion rather than infer
nonrootness from the missing root signature.  Given Statement 9.2's unique
root signature, the inference is mathematically defensible for exact
constructed node shapes.  It is not a substitute for the `MU1` cap fix above.

## 5. `mu=1` grammar and tuple indexing

The implemented `MU1` grammar is the right specialization:

```text
IIa_0: dp = mu*nu, dq = (l+1)*nu + 1
mu=1, nu_F=1: dp = 1, dq = l + 2, l >= 0
```

The code consistently uses the `kl` slot as `l` for `MU1`
(`cases/sheet6_campaign.py:123`, `135`, `139`, `155`, `279`, `347`).
The tuple layout introduced for `twopole_check.root_merges()` is internally
consistent at the visible consumers:

```text
(pa, pb, mu1, mu2, k, l, ratio_kl, Di, tot, psi, ok, ode)
```

The smoke test indexes `row[11]` for `ode` and the main display indexes
`h[10]` for `ok`, `h[11]` for `ode`; these match
`cases/twopole_check.py:322-323`, `538-552`.

## 6. Two-pole root menu and caps

`cases/twopole_check.py:257-274` implements the corrected root menu

```text
dp = mu1 + mu2 + k
dq = k + 2 + l
```

and separates the all-`mu=1`, `k=0` ODE tags:

```text
even l: ROOT_ODE_LOG_DEAD_EVEN
l=1:   ROOT_ODE_EXACT_SOLVABLE_L1
odd l>1: ROOT_ODE_NO_LOG_OBSTRUCTION_ODD
other cells: ROOT_ODE_UNCHECKED
```

The parent reach test `kappa_parent < nu_parent`
(`cases/twopole_check.py:277-279`) is exactly the required
Prop. 9.3(d) condition for a child with `(nu,kappa)=(1,1)`.

The default `L1MAX=4` is not a general root-menu completeness theorem.
For the displayed `td=6` phase-3 budget screen, however, the root formula
gives `ratio_kl = dq` and `psi = dq-1 = k+1+l`; with nonnegative lambda,
budget consistency forces `k+l <= 4`.  Thus `l<=4` is budget-complete for
`td=6` phase-3 root-merge candidates, conditional on the Section 7 budget
inequality being available.  The code should say this explicitly.

Suggested display/doc patch:

```diff
diff --git a/cases/twopole_check.py b/cases/twopole_check.py
@@
 def root_pattern_menu(mu1, mu2, *, kmax=KMAX, lmax=L1MAX):
@@
-    The old menu fixed l=0. The l>=1 family has
+    The old menu fixed l=0. The l>=1 family has
     ``dp=mu1+mu2+k, dq=k+2+l``. For the all-mu=1, k=0 family, even l is
     logarithmically obstructed while odd l has no such obstruction; l=1 is
     the exact locally solvable ``(dp,dq)=(2,3)`` cell.
+    For the td=6 phase-3 budget screen, ``psi=dq-1`` and nonnegative lambda
+    force ``k+l<=4`` for budget-consistent hits.  Outside that td=6 budget
+    screen, ``lmax`` is only a diagnostic cap.
@@
-    print(f"root-merge solutions after parent reach: {len(hits)}; "
+    print(f"root-merge solutions after parent reach within "
+          f"k<={KMAX}, l<={L1MAX}: {len(hits)}; "
```

The phase-4/L1 display remains capped diagnostics (`LMAX=8`), not a theorem.

## 7. Section 7 budget interaction

The current engine comments and output still use `St 9.4` language as if the
global budget is unconditionally promoted.  The current Section 7 chain is
not that strong:

- `sigray-section7-resolution-free-coordinator-final-delta-gate-terra` is
  `FAIL` on fixed `kappa` transport.
- `sigray-section7-kappa-variation-salvage-gpt55` says the strongest supported
  fixed-weight `(22-cl)` route is not promoted.
- `sigray-section7-weighted-euler-inequality-hostile-review-terra` passes an
  amended weighted-Euler inequality, but explicitly does not promote printed
  `(22)`, printed per-puncture `delta`, or the failed fixed-weight `(22-cl)`.

The repair report correctly says it does not promote Section 7, but the Python
surfaces should not print exclusion-grade text without the same condition.
At minimum, patch the user-facing verdict/comment strings at:

- `cases/sheet6_campaign.py:419-423`, `456-458`;
- `cases/h3_check.py:9-11`;
- `cases/hiii_compose.py:9-11`;
- `cases/twopole_check.py:7-9`, `319-321`.

Suggested wording: "conditional on the currently accepted Section 7 budget
inequality / first-separation exit ledger."  Do not cite `(22-cl)` as proved
unless the separate Section 7 gate changes.

## 8. Preservation of legacy logic

Static scan result:

```text
no raw child.M == 1 / ch.M == 1 / c2.M == 1 BFS pruning remains
```

The `hiii_compose.e5_iii_outcomes()` `MF<2` filter is scoped by
`nuF>=2` (`cases/hiii_compose.py:73-82`), so it is a certified nonroot kill.
Pinned pole-entry deaths in `hiii_compose.py:324-340` and
`sheet6_campaign.py:716-731` use explicit pole nonroot metadata and remain
valid.

The only stale legacy text I found is comment/docstring text, not behavior:

- `cases/sheet6_campaign.py:20-21` still says `M_F=1 KILL` for IIb/III
  without saying "certified nonroot".
- `cases/twopole_check.py:20` still says `mu=2 I/IIb/III` children are added
  in `step_twopole()`, but the repaired code inherits `I` from `sc.step()` and
  adds only IIb/III locally.

These should be cleaned after the blocker is fixed, but they are not the
reason for the failing verdict.

## 9. Smoke-test adequacy

Local gates run:

```text
python3 -m py_compile cases/sigray_rootaware_smoke.py cases/sheet6_campaign.py \
  cases/h3_check.py cases/hiii_compose.py cases/twopole_check.py \
  cases/monodromy_td.py
python3 cases/sigray_rootaware_smoke.py
git diff --check -- cases/sheet6_campaign.py cases/h3_check.py \
  cases/hiii_compose.py cases/twopole_check.py cases/monodromy_td.py \
  cases/sigray_rootaware_smoke.py
```

Results:

```text
py_compile: pass
git diff --check: pass
ROOT-AWARE SMOKE PASS: 7 checks
```

The smoke suite is adequate for the root-before-`M=1` ordering, the restored
`mu=1`/`mu=2 I` emissions below the default caps, the two-pole `l=1` root
menu, and static removal of raw BFS M1 shortcuts.  It is not adequate for
cap/no-verdict soundness.  Add the `root-cap-witness` from section 3.

## 10. Required disposition before promotion

Do not promote the repair as "implemented; no code-level blocker" until all
three are true:

1. `MU1` either has a proved analytic `l` bound or emits an explicit
   `OPEN`/`NO_VERDICT` tail whenever the finite cap is used.
2. Root-menu cap text distinguishes the td=6 budget-complete phase-3 screen
   from general capped diagnostics.
3. Exclusion-grade output is explicitly conditional on the currently accepted
   Section 7 budget inequality, not on the failed fixed-weight `(22-cl)` route.

After those patches, the root/nonroot repair itself should be re-reviewed as
`PASS WITH PATCHES`; without them, the exact `l=98` root terminal above is a
current counterexample to sound root-aware enumeration.
