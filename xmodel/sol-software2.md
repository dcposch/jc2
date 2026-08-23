# Software acceleration second opinion

## Executive summary

- **Material-upside rank: 1 > 2 > 3 > 5; deployable-today rank: 2 > 1a > 3 > 5, because item 1b still lacks a correctly specified series-valued Jacobian object.**
- **Item 1 is the only branch-closing build:** implement point extraction and full D23 reconstruction now, but do not compute `e` from the scalar `.ms` Jacobian or promote `e <= 11` until the square function block and surplus-equation bridge are banked.
- **Item 2 is an immediate GO, not merely D25 preparation:** a read-only three-prime FLINT replay reduces the current 72v/54eq/48,621-term compatibility object to a candidate **29v/32eq/12,654-term** equivalent object.
- **Item 3 is useful scheduling instrumentation, not an algebraic acceleration; item 5 is correctness/availability insurance and must not delay items 1a or 2.**
- **Best missed one-day lever:** turn the Row_22 prototype into a cached previous-locus quotient/Schur compiler, with a content-addressed point and reconstruction manifest shared by every later depth.

## Ranking and execution order

The campaign-impact order is **1, 2, 3, 5**. The engineering order should be more nuanced:

1. Freeze the item-1 point/reconstruction manifest and the mathematical definition of the valuation object.
2. In parallel, ship and gate the item-2 22-pivot pre-elimination on the current D23 compatibility system.
3. Use the smaller artifact for point extraction; activate the `e` decision only after the series-object gate closes.
4. Add the telemetry parser, then the SG updater and tiered CI.

## Item 1 — valuation-`e` pipeline: rank 1, split GO/BLOCK

**Verdict.** Point extraction plus complete D23 reconstruction is a GO now. The final `e <= 11` classifier is **blocked from promotion**, not from prototyping, until its input is the original series-valued equation map required by `xmodel/sol-instrument4.md` §6. A scalar `.ms` Jacobian has entries in a finite field and no uniformizer: its minors have valuation only `0` or `infinity`. Worse, pivot definitions, radical equations, and Rabinowitsch rows contain unit derivatives and can manufacture a false `e = 0`.

This is still rank 1 because a valid point with `e <= 11` ends the D23 NONEMPTY branch immediately, whereas every other item merely makes another computation cheaper. Its honest output scope is a **mod-`p` formal germ on the named B-frozen/no-log/radical chart**, not a characteristic-zero germ or a counterexample.

### Build now: point certificate and reconstruction

1. Parse and hash the exact msolve artifact, variable order, monomial order, characteristic, radical factor, `W` branch, solver version, and command. A proper positive-dimensional basis needs reproducible slicing; failure to find an `F_p`-rational point is not emptiness, so the extractor must also admit finite extension fields.
2. Verify every extracted coordinate against the complete row22compat basis and all 54 emitted equations/saturations.
3. Reconstruct the object projected away by the Schur collapse. A row22compat point has no `x74,...,x83`: solve the four deep directions and choose the six-dimensional deep kernel. Verify the 72-row fiber system, the unspecialized 77-row hybrid, and the pristine source rows. Search over, or prove invariance across, the six kernel parameters because `e` may depend on that choice.
4. Emit a machine-readable point certificate containing chart data, all reconstructed coordinates, pivot and Schur choices, row hashes, and exact zero residuals. Current `/tmp`-dependent point scripts are discovery harnesses, not a reusable certificate path.

The 12 banked points are D21 points with 22 coordinates, not D23 points. Their required regression result is **`NOT_IN_DOMAIN` / Row_22 compatibility failure for all 12**. If the pipeline assigns any of them an `e`, it has certified the wrong object. They are strong negative controls but provide no positive test of the valuation arithmetic.

### Required valuation-object manifest

Before `e` can carry the DEPTH-STAB conclusion, freeze all of the following:

- the uniformizer, exactly `t = x^(-1/42)`, and the truncation convention `F(s) = 0 mod t^23`;
- the original equation vector in `F_p[[t]][eta]`, before coefficient extraction, and the actual unknown **series/function** coordinates;
- a square subsystem and its chosen function block, or the correct Jacobian/Fitting ideal, together with an exact proof that every surplus equation lies in its completed local ideal;
- every equation and variable shift used to pass from the raw chart to the emitted rows; and
- which transformations are unimodular over `F_p[[t]]` and which merely preserve the scalar variety.

The chart normalization is load-bearing. The global chart is `y = P(t) + eta*t^32`; ordinary `tf/tg` tails advance one `t`-level while the 21-ramified `tg01/tg02` series occupy only even global levels. Computing in `u = t^2` is allowed only with the explicit conversion `v_t = 2 v_u`. Multiplication by `W`, `A`, or a nonzero radical scalar is multiplication by a `t`-adic unit; multiplication or division by a power of `t` changes `e`. Also keep the uniformizer named `t` or `tau` distinct from the unrelated convention `t = eta^nu` elsewhere in the repository.

Do not use arbitrary maximal minors of the 77-by-87 scalar coefficient Jacobian. Once the theorem's series block is named, compute the relevant determinantal divisor with truncated Smith/rank-profile elimination over `F_{p^d}[t]/(t^23)`, stopping once the valuation exceeds 11. This avoids enumerating minors and must retain one explicit row/column minor as a witness.

### Promotion gates

- All 12 D21 points reject before valuation.
- A genuine D23 constant-block-dropped formal point gives the expected `e = 0`; the existing D21 ctl0 is only an emitter control.
- The DEPTH-STAB toy gives `e = 1`, and small random matrices agree with brute-force minor enumeration.
- Global-`t` and 21-chart `u=t^2` encodings agree after valuation conversion.
- Unit row/column transformations preserve `e`; a deliberate `t`-shift changes it by the predicted amount.
- Tau transport, admissible `W`-root changes, and original-versus-stably-reduced presentations agree.
- A `+42` or chart-offset mutation is detected.
- Singular/all-minor-zero points fail closed. A sampled high `e` is not a locus-wide lower bound.

Only after these gates pass does `e <= 11`, equivalently `23 >= 2e+1`, become the conditional live certificate claimed by DEPTH-STAB. Until then, report `E_CANDIDATE`, not `LIVE`.

## Item 2 — FLINT pre-elimination of all 22 pivots: rank 2, immediate GO

**Verdict.** Apply this to the current D23 row22compat object before treating it as only a D25 optimization. The safe order is:

1. form the six Schur compatibility rows `c = Lb` from the ten pristine Row_22 rows;
2. pseudo-divide the 22 unit-linear pivot coordinates out of those six rows only;
3. lattice-reduce and strip common `W`-unit content after every pivot; and
4. retain the 24 CORE2 rows and the two `uW_i W_i - 1` rows.

A read-only replay during this review measured the following at **each of the three banked primes**, with identical support:

| stage | six compatibility terms |
|---|---:|
| W-symbolic before pivots | 26,256 |
| after three cheap low pivots | 16,458 |
| after the 16 high pivots | 10,794 |
| after all 22 pivots | **7,306** |

The six final rows have sizes `1218,1218,1218,1218,1218,1216`, degree 9, and use 25 `x` variables. Those 25 contain all 18 variables used by the 24-row CORE2. Adding `W1,W2,uW1,uW2`, the 5,344 CORE2 terms, and two saturation rows gives the unbanked prototype census:

> **29 variables / 32 equations / 12,654 terms**, at all three primes.

The fixed-`W` replay also reproduces the documented `25,554 -> 16,134 -> 10,500 -> 7,054` trajectory. Thus the proposed `~50v/32eq` target is conservative: 29 variables are reachable on the current artifact, subject to the gates below.

**CONJECTURE:** the solver gain will be much larger than the 3.8-fold term reduction because 43 variables disappear, but no speed factor should be quoted until a same-hash, same-version, same-host A/B trace completes.

### Risks and gates

- **Schur first is mandatory.** Substituting the pivots into all ten pristine rows recreates the rejected 4,971,007-term, degree-32 object.
- Pivot coefficients are units only on the stated `W1*W2 != 0` chart. Keep the `uW` equations, record every stripped monomial, and reconstruct it exactly.
- Freeze pivot variable names, source row labels, order, radical branch, and transformation DAG. A positional `xN` match is not provenance.
- Require cross-prime support equality; independent scalar replay; tau transport; `+42` mutation detection; removed-variable absence; unique pivot back-solve; and verification of every pristine/raw row.
- Bank both the 29v artifact and the 72v reconstruction control. A NONEMPTY point from the smaller system is accepted only after full back-substitution.
- D25 does not inherit the 29-variable count automatically. Row_24 may reactivate old directions or introduce new auxiliaries. Re-run **Schur/project -> pivot -> unit-strip -> census** at each depth and retain the hybrid if degree or term mass crosses the pre-registered cap.

## Item 3 — msolve `-v 2` telemetry parser: rank 3, build as a classifier

**Verdict.** Worth a focused implementation after items 1a/2. It will prevent wasted 12–48 hour extensions and make presentation A/B tests comparable, but it does not reduce the Groebner workload. The current extension trace already supports redesign, so its immediate value is lower than its campaign-wide value.

Implement a streaming parser that emits append-only JSONL. Preserve printed round order—degrees repeat, reset, and arrive out of numeric order. Per F4 round record sequence, degree, selected pairs, pair backlog, matrix rows/columns, the printed density **interval**, new basis elements, zero reductions, and real/CPU time; enforce `new + zero = selected`. Parse final-basis reduction and characteristic-zero multi-modular phases separately. Join the trace to `/proc` or GNU-time RSS/CPU samples because `-v 2` does not report RSS.

Every record needs input, options, binary/version, host, seed, and artifact hashes. A missing footer, partial line, timeout, nonzero return, or zero-byte output is censored—not a verdict. Support the campaign's 0.10.1 and 0.6.5 grammars with frozen fixtures.

The decision output should be `{EXTEND, REDESIGN, INSUFFICIENT}`, not a fabricated completion ETA. Fit ranges for the next round's wall/RSS/matrix envelope only from the last 3–5 completed checkpoints inside one contiguous phase. Never fit across a degree reset. Extend when completed frontiers still move and the next envelope fits the resource/cap; redesign on a sustained matrix/pair cliff, a censored stalled round with flat frontier and low CPU, or a resource-envelope veto. Keep all thresholds in a versioned policy file and require human confirmation before killing a lane.

**CONJECTURE:** a calibrated parser will recover more wall time by preventing bad extensions than by choosing among already-small presentations; its accuracy for final completion time will remain poor because the terminal regularity degree is unobserved.

## Item 5 — SG updater plus gate-suite CI: rank 4, split the work

**Verdict.** Do the AWS security-group updater as a small hygiene task; build CI incrementally as correctness infrastructure. Neither belongs on the present algebraic critical path.

For SG updates, discover the current public egress address, authorize an exact managed `/32`, verify AWS state and SSH, then retire only prior rules carrying this tool's tag. Never broaden to `/24`, never revoke untagged/manual rules, and fail closed if address discovery or identity checks disagree. This removes a recurrent access/recovery failure without changing running jobs.

CI is not currently a YAML-only addition. There is no pinned environment or workflow, several direction-b scripts hard-code `/Users/dc/...` and transient `/tmp` inputs, and several flagship gates print `FAIL` yet still exit zero. The first CI milestone is therefore:

1. make gates fail closed with structured summaries;
2. make paths repository-relative and fixtures explicit;
3. pin Python/python-flint and bank small hashes/negative controls; and
4. split a fast offline suite from scheduled artifact replay.

The fast tier should run ordinary tests, parser fixtures, emission hygiene (expanded/no parentheses, coefficients in `[0,p)`, variable/row hashes), small FLINT/Schur replays, and deliberate mutations. A scheduled/manual tier can replay large enumerators and frozen algebra artifacts. Do not run msolve Groebner jobs in hosted CI, and do not let a green toy gate imply that the series-valued `e` bridge has been checked.

## Missed high-leverage builds

### A. Previous-locus quotient/Schur depth compiler — first choice for one focused day

Generalize the successful Row_22 path into a depth-delta compiler:

- ingest the previous locus's hashed Groebner basis with its exact variable and monomial order;
- build a fast FLINT leading-monomial index and cache normal forms by polynomial hash;
- detect affine new-tail blocks, certify their rank/unit columns, and form left-kernel compatibility rows before old-pivot substitution;
- reduce after every pivot in the previous coordinate ring; and
- emit a rank-complete system plus a reconstruction DAG, never merely a generic-rank chart.

Use the banked 397-element D21 basis as the regression fixture, then use the row22compat basis as the live D25 quotient once its solver output is banked. This directly operationalizes the reduction that exposed only `d1=x17-x32` and `d2=x25-x37` at sampled D21 points.

**CONJECTURE:** exact cached normal forms will recover that two-difference structure globally, or expose a similarly small D25 obstruction module, before another global F4 run. Sampling may suggest the block, but only exact quotient reduction and rank-boundary coverage can promote it.

### B. Content-addressed lane and certificate ledger

Give every run an ID

```text
SHA256(input bytes || solver binary/version || arguments || emitter/gate hashes)
```

and record host, PID, start/cap/end, input transfer hash, RSS series, return code, output hash, chart/prime, and certificate status in one append-only ledger. Refuse a duplicate active run with the same ID; use exact PIDs and file hashes rather than generic `ps | head` checks. Feed the completed box01 health log and item-3 JSONL into this ledger.

This is a one-day read/launch/status MVP with no automatic instance stop, process kill, or verdict promotion. It directly prevents stale-object launches, duplicate relaunches, ambiguous zero-byte outputs, and loss of provenance between a NONEMPTY basis and its reconstructed point.

## Bottom line

Start item 1's extractor/certificate layer and item 2's 29-variable emission together. Item 2 is the strongest shippable acceleration found in this review; item 1 remains the highest-upside campaign move but earns a final verdict only after the original series map, square minor block, normalization, and surplus-equation theorem are explicit. Build telemetry and reliability automation behind those two, and make the quotient/Schur compiler—not another raw D25 emitter—the reusable depth engine.
