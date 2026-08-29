# V26 compiler-scaffold implementation status

Date: 2026-08-27

Status: **SOURCE SCAFFOLD COMPLETE; STATIC CHECKS PASS; DEPENDENCY HELD; NO
ALGEBRA RUN.**

The source compiler is `compile_fitting_atlas_v26.py`.  Its construction path
is the frozen V20R2 `LITERAL_140_EQUATION_DAG.json` plus
`SOURCE_COLUMNS.json`.  V23's matrix/witness and V24's `b`, prior rows, and
two compatibility polynomials are coefficientwise comparison controls only;
they cannot substitute for reconstruction.

The compiler:

- checks the 169/164/5 source-column census and substitutes the five boundary
  zeros before extracting any row;
- expands only the exact dependency slice of the 56 roots through grade
  seven, with a fail-closed term cap;
- retains all literal zero/nonzero rows through grade six, adds `F10`, and
  extracts the seven affine grade-seven equations in exactly
  `(d0_6,...,d5_6,k10_3)`;
- constructs `A`, `b`, and `E=[A|-b]`, proves all newest-variable second
  derivatives zero, and requires every entry of `A` to depend only on
  `(d0_1,...,d5_1)`;
- builds all `I_j(A)` and `I_j(E)`, `1<=j<=6`, as hash-consed exact
  fraction-free compound-determinant DAGs, and separately expands every
  `A`-minor for exact zero/rank/chart selection;
- makes every distinct nonzero `r`-minor of `A` an independent chart for
  `X_r`.  Thus no chosen witness defines the rank-five locus.  A rank chart
  uses the exact Rabinowitsch equation `zinv*k10_0*m-1`, and the union over
  the minor charts is exactly `D(k10_0) intersect D(I_r(A))`;
- emits a six-variable `B+I_5(A)` prepass, every rank-chart job specification,
  and the exact `D(W)` agreement job; and
- embeds toy rank/compatibility cases, exact `b`-sign and ordering mutations,
  the restored nonzero `k6_0` column, forced-unit/known-proper controls, and
  second-process replay requirements.

`run_v26_exact_worker.py` can materialize and run one independently capped
prepass, agreement, or rank-minor-chart job.  It refuses to run unless the
compiled directory contains `RELEASE_V24R2_EXACT.json`, bound to a validated
exact-Q V24R2 endpoint and its artifact hashes.  Every worker result remains
explicitly unreviewed and non-promotable until a separate replay and atlas
aggregation.

The current V24R2 exact-Q endpoint is not part of this scaffold.  Therefore
no release file exists, no worker is runnable, and there is no prepass,
rank-stratum, compatibility, jet, arc, closure, order-two, maximum-twelve, or
JC2 conclusion.

Static checks run locally (no Singular and no polynomial reconstruction):

```text
python3 -m py_compile compile_fitting_atlas_v26.py run_v26_exact_worker.py
bash -n run_v26_compile_aws.sh run_v26_worker_aws.sh
python3 compile_fitting_atlas_v26.py --static-self-test
K00_V26_STATIC_SELF_TEST=PASS
python3 compile_fitting_atlas_v26.py --static-input-check
K00_V26_STATIC_INPUT_CHECK=PASS
git diff --check -- cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827
```

