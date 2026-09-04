# K=16 Square-Tail Hilbert-Guided Standard-Basis Run

Lane: `k16-square-tail-stdhilb-gpt55-20260903`.
Date: 2026-09-04.
Output directory: `box/k16stdhilb-20260903/`.

## 1. Input Custody

The frozen input directory is `/tmp/jc2-lane.YU5vA0/inputs`.  I generated
`box/k16stdhilb-20260903/input_manifest.sha256` mechanically from
`xmodel/k16-square-tail-stdhilb-gpt55-20260903.run.v2` by matching the indexed
`charged_input_<i>_basename=` and `charged_input_<i>_sha256=` fields, and then
ran `sha256sum -c` on that manifest.

Result: all 14 charged inputs verified `OK`.

## 2. Question

For fixed `t`, let

```text
S_t = A_t[b4,q2_0,...,q(t-1)_0,b3],
weights = (1,2,...,t-1,t+1),
J_t^tail = <T_{t,t},T_{t,t+1},...,T_{t,2t-1}>.
```

The tested statement is that `J_t^tail` is an hsop.  Since `S_t` is a
Cohen-Macaulay polynomial ring over the coefficient fibre, `dim S_t/J_t^tail =
0` makes the `t` tail rows a regular sequence and forces the complete-
intersection Hilbert series

```text
prod_{d=2t+2}^{3t+1}(1-s^d) /
((1-s) prod_{j=2}^{t-1}(1-s^j) (1-s^{t+1})).
```

The predicted fibre lengths are:

```text
t=3: 90
t=4: 572
t=5: 3640
t=6: 23256
t=7: 149226
t=8: 961400
```

## 3. Method

The long jobs wrap banked preexpanded cone sources containing `T0,...,T(2t-1)`
in the requested weighted residual ring.  The wrapper copies only the ring,
the `minpoly` statement if present, and the polynomial row declarations; it
does not rederive terminal rows.

Each guided run calls Singular as

```text
std(J, TARGET_HNUM, WTS)
```

where `TARGET_HNUM` is the predicted complete-intersection Hilbert numerator,
with Singular's required trailing Hilbert-vector bookkeeping zero.  The
target series is used only as a performance guide.  A run is accepted only
after the transcript independently prints:

```text
NF(T_{t,k},G)=0 for every selected row k
dim(G)
vdim(std(minbase(lead(G))))
the predicted length used for comparison
```

No guided standard basis is reported as evidence unless its normal-form and
lead-ideal length checks both pass.

Every Singular job is run in the foreground under `timeout 3000`, with Singular
thread options capped at four and a 24 GB virtual-memory ulimit.

## 4. Mandatory Controls

Controls required before reporting a `t=7` or `t=8` result:

```text
positive control: t=5, p=1009, both fibres, length 3640
positive control: t=6, p=1009, both fibres, length 23256
negative control: t=2, y=1/5 full cone, guided run must not return dim 0
perturbed-series control: a deliberately wrong target must fail NF or vdim
```

## 5. Driver Artifacts

All lane files were written under `box/k16stdhilb-20260903/`.  The driver
wrapper is `emit_square_tail_guided.py`; it imports the frozen banked parser
from `/tmp/jc2-lane.YU5vA0/inputs/emit_preexpanded_cone_job.py` and reuses the
preexpanded terminal-row sources.  The runner is `run_singular_job.sh`.

The runner command shape for each Singular file is:

```text
/usr/bin/time -f 'wall=%e maxrss_kb=%M exit=%x' \
  timeout 3000 bash -c 'ulimit -v 25165824; exec Singular --cpus=4 --threads=4 --flint-threads=4 -q "$1"'
```

This keeps every Singular process in the foreground with the requested 3000
second timeout, four-thread cap, and 24 GB virtual-memory cap.  The derived
artifact checksum file is `box/k16stdhilb-20260903/artifacts.sha256`; it
contains 91 file checksums and excludes itself.

No ledger files, `jc2-lean` files, or `ideation-*` files were edited.

## 6. Mandatory Controls

All accepted-control transcripts have empty stderr files and `runner_exit=0`.

Positive controls at `p=1009`:

| index | fibre | transcript | guided sec | NF all zero | dim | vdim(G) | lead dim | lead vdim | wall sec | RSS KB | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `t=5` | `b0` | `t5_p1009_b0_tail_guided.out` | 1 | 1 | 0 | 3640 | 0 | 3640 | 0.82 | 15752 | PASS |
| `t=5` | `b1` | `t5_p1009_b1_tail_guided.out` | 1 | 1 | 0 | 3640 | 0 | 3640 | 0.82 | 15836 | PASS |
| `t=6` | `b0` | `t6_p1009_b0_tail_guided.out` | 33 | 1 | 0 | 23256 | 0 | 23256 | 35.32 | 144192 | PASS |
| `t=6` | `b1` | `t6_p1009_b1_tail_guided.out` | 35 | 1 | 0 | 23256 | 0 | 23256 | 37.08 | 143980 | PASS |

The required Sol lengths were reproduced:

```text
t=5: TAIL_LEAD_VDIM=3640
t=6: TAIL_LEAD_VDIM=23256
```

Negative control at `t=2`, `y=1/5`, full cone:

| transcript | selected rows | NF all zero | dim | lead dim | vdim | wall sec | RSS KB | verdict |
|---|---|---:|---:|---:|---|---:|---:|---|
| `t2_y1over5_full_negative_guided.out` | `1,2,3` | 1 | 1 | 1 | NONTERMINATING | 0.01 | 11284 | PASS |

The guided run did not return dimension zero:

```text
FULL_DIM=1
FULL_LEAD_DIM=1
NEGATIVE_CONTROL=PASS
```

Perturbed-series control:

| transcript | target | selected rows | NF all zero | dim | lead dim | lead vdim | wall sec | RSS KB | verdict |
|---|---|---|---:|---:|---:|---|---:|---:|---|
| `t8_p1009_b0_tail_desc_froberg_wrong_guided.out` | wrong Froberg numerator, no bookkeeping zero | `15,14,13,12,11,10,9,8` | 0 | 7 | 7 | NONTERMINATING | 0.24 | 12552 | PASS |

This deliberately wrong target was detected immediately:

```text
NF_TAIL_T15_ZERO=1
NF_TAIL_T14_ZERO=0
NF_TAIL_T13_ZERO=0
NF_TAIL_T12_ZERO=0
NF_TAIL_T11_ZERO=0
NF_TAIL_T10_ZERO=0
NF_TAIL_T9_ZERO=0
NF_TAIL_T8_ZERO=0
TAIL_LEAD_DIM=7
TAIL_VDIM_MATCH_PREDICTED=0
PERTURBED_CONTROL=PASS
```

Several smaller wrong-target attempts at `t=5` were not used as the mandatory
perturbation control, because Singular still computed the true zero-dimensional
basis and the transcripts printed `PERTURBED_CONTROL=FAIL`.  They are retained
only as discarded diagnostics.

## 7. Main t=7 Tail Run

The `t=7` square-tail target used:

```text
variables = b4,q2_0,q3_0,q4_0,q5_0,q6_0,b3
weights   = 1,2,3,4,5,6,8
rows      = T7,T8,T9,T10,T11,T12,T13
degrees   = 22,21,20,19,18,17,16
L_7       = 149226
prime     = 1009
```

Fibre `b0` completed and passed all required checks:

| transcript | source sha256 | guided sec | NF all zero | basis size | dim | vdim(G) | lead min | lead dim | lead vdim | wall sec | RSS KB | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `t7_p1009_b0_tail_guided_checkfirst.out` | `c4efb7ccd15ded336a9726062ecba3ccd603ea1199590f13a2a45ec2a1afd18b` | 1562 | 1 | 14493 | 0 | 149226 | 14493 | 0 | 149226 | 2993.34 | 3393180 | PASS |

The transcript prints the two mandatory acceptance checks:

```text
NF_TAIL_T7_ZERO=1
NF_TAIL_T8_ZERO=1
NF_TAIL_T9_ZERO=1
NF_TAIL_T10_ZERO=1
NF_TAIL_T11_ZERO=1
NF_TAIL_T12_ZERO=1
NF_TAIL_T13_ZERO=1
NF_TAIL_ALL_ZERO=1
TAIL_DIM=0
TAIL_VDIM=149226
TAIL_LEAD_DIM=0
TAIL_LEAD_VDIM=149226
TAIL_VDIM_MATCH_PREDICTED=1
ACCEPT_TAIL=PASS
JOB_DONE t=7 job=tail
```

This is a valid modular dimension-zero and length match for the `b0` fibre.
It is not, by itself, the lane-requested two-fibre completion at `t=7`.

Fibre `b1` did not complete to checks:

| transcript | source sha256 | state reached | exit | wall sec | RSS KB | verdict |
|---|---|---|---:|---:|---:|---|
| `t7_p1009_b1_tail_guided_checkfirst.out` | `eda79273de10f9065e8e9eaca17ffbda47a208db7b73e03d186e04676f5e64b3` | after `GUIDED_STD_START`, before `GUIDED_STD_SECONDS` | 1 | 474.81 | 697444 | INCOMPLETE |

The branch-1 stdout ends:

```text
SELECTED_ROWS=7,8,9,10,11,12,13
GUIDED_STD_START

halt 1
```

The branch-1 stderr file is empty.  Since no `G` was printed and no NF, dim,
or lead-vdim checks ran, this is treated as an engine abort/incomplete
foreground job, not as a mathematical refutation.

One earlier `b0` run, `t7_p1009_b0_tail_guided.out`, computed `G` and printed
`TAIL_DIM=0`, `TAIL_VDIM=149226`, and all tail normal forms zero, but then
timed out while emitting the Hilbert numerator before the lead-ideal check.
It is retained as a discarded partial transcript:

```text
runner_exit=124
wall=3000.14
maxrss_kb=3392724
```

The accepted `b0` check-first rerun above supersedes this partial transcript.

## 8. t=8 Status

The `t=8` proof jobs were emitted but not run:

```text
t8_p1009_b0_tail_guided.sing
t8_p1009_b1_tail_guided.sing
```

The card condition was "same at `t=8` if `t=7` completes within budget."  Since
the `t=7` second fibre did not complete to checks, no `t=8` square-tail result
is reported.  The only executed `t=8` job is the deliberately wrong
perturbed-series control in Section 6; it is not evidence for the true
`t=8` tail ideal.

## 9. Full-Cone Status and Implication

The full-cone `t=7` sources were emitted:

```text
t7_p1009_b0_full_from_tail_guided.sing
t7_p1009_b1_full_from_tail_guided.sing
```

They were not executed.  No full-cone Groebner-basis transcript is claimed in
this lane.

The logical implication requested by the card is:

```text
J_t^tail subset I_{t,+}
dim S_t/J_t^tail = 0
=> dim S_t/I_{t,+} = 0.
```

This implication is purely by containment: quotienting a zero-dimensional
algebra by more equations cannot raise Krull dimension.  Therefore an accepted
square-tail hsop result at an index would force the full cone to have
dimension zero at that index.  The full-cone computation is useful as a
separate check or for additional data, but it is not logically needed for
`(V0)` once the tail hsop is proved.

In this run, the implication applies only to the completed `t=7`, `b0`
modular fibre.  It is not promoted here to a full `t=7` two-fibre result, and
there is no `t=8` true-tail result.

## 10. Promotion Chain

The properness gate promotes only the dimension-zero statement:

```text
modular dim=0  =>  characteristic-zero dim=0.
```

It does not promote modular Hilbert functions or modular lengths by flatness.
For the square-tail test, once characteristic-zero dimension zero is promoted,
Cohen-Macaulayness and the row degrees force the characteristic-zero complete-
intersection Hilbert series separately.

At each fully proved index, the promoted chain would be:

```text
tail hsop
  => dim I_{t,+}=0 by containment
  => (V0)
  => terminal unit statement (8.1) through the banked CONE criterion
  => theorem (T) through the banked CONE chain.
```

Promotion was not completed at `t=7` or `t=8` in this lane, because the
lane-requested two-fibre `t=7` computation did not complete and the true `t=8`
jobs were not run.

## 11. Interpretation

The accepted controls remove the main guided-Hilbert hazards:

```text
t=5 and t=6 reproduce the known lengths in both p=1009 fibres.
t=2, y=1/5 does not falsely become dimension zero.
a deliberately wrong t=8 series is caught by NF and lead-dimension failure.
```

The completed `t=7`, `b0` run supports the predicted square-tail statement in
that modular fibre:

```text
dim=0
vdim(G)=149226
vdim(lead(G))=149226
all tail rows reduce to zero
```

However, the card asks for both fibres at the split modular specialization and
does not permit reporting a guided result without the normal-form and
lead-ideal length checks.  The `b1` run stopped before those checks.  Thus the
uniform `t=7` claim is not proved here.  There is also no true `t=8` run.

No accepted transcript has `dim>0` for the true `t=7` or `t=8` tail target, and
no mandatory control failed.  Therefore the outcome is not `REFUTED`.

## 12. FALLACY-v2

No exit-price assertion is made in this report, so no `charge_basis` line is
applicable.  The ring, coefficient field, variable order, row set, Hilbert
target, normal-form checks, and lead-ideal length checks are printed in each
accepted transcript.

The relevant variable/ring maps are printed in the `META` lines.  For the
accepted `t=7`, `b0` run:

```text
META t=7 job=tail target=tail-ci expected=success vars=b4,q2_0,q3_0,q4_0,q5_0,q6_0,b3 weights=1,2,3,4,5,6,8
ROW_GRADING_CHECK=PASS
SELECTED_ROWS=7,8,9,10,11,12,13
```

No representative/attainment, pole/interior, raw-remainder, prime-label, or
exit-set charge assertion is used.

## 13. Verdict

Verdict by index:

| index | verdict | reason |
|---|---|---|
| `t=7` | TIMEOUT / ENGINE-ABORT | `b0` passes, but `b1` exits with `halt 1` before NF/dim/vdim checks. |
| `t=8` | TIMEOUT / NOT RUN | Conditional `t=8` true-tail jobs were not run because `t=7` did not complete. |

Overall lane verdict: `TIMEOUT`.

This run proves the `t=7`, `b0` modular fibre only.  It does not prove
SQUARE-TAIL at `t=7` or `t=8` under the card's mandatory reporting rule, and it
does not refute `(V0)`.

<!-- BODY-END -->
