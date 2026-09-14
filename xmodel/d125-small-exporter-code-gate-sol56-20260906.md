# Independent engineering gate: D125 small-source exporter

Status: **CONFIRMED as a provisional construction instrument at static-source and tiny-control scope; not independent full-stream certification.** One unqualified safety description is narrowly **REFUTED**: the artifact-byte budget does not meter the CLI's final stdout copy or stderr. The absence of an actual production JSONL/Singular import remains an explicit **GAP**. Review 2026-09-06, Sol56; producer remained TERMINAL/IDLE.

## Scope, custody, and verdicts

I read all 1,311 lines of the eight immutable files in `/tmp/jc2-lane.h7lTCN/inputs`, plus the 38-line producer runner without executing it. The frozen report hash is `eddaf82a9c793de1b4e5a223fef5d93ba3e214a0c61cf3775f95d023b99fb085`; the repository report and supplied artifact-manifest hash `1001c53ce55ae6043693922669799e848c234526e0d8f06e7109b776dc0ba33c` match. The exporter/baseline/tests are `9fd003e4…`, `ec2fa2d…`, `331e97c8…`; the preflight/receiver/lift gates and guardrail are `f1fdd20d…`, `cd69c238…`, `4295593a…`, `e47fd16c…`; repository copies match byte-for-byte. Runner `ef6c9f01…` matches its declared pin. I did not read the separate AWS pilot, production outputs, live lanes, other reviews, or protected-project material.

| area | CONFIRMED | REFUTED | GAP |
|---|---|---|---|
| formula / complete indices | all six literal maps, formulas, guards, 660+105 index rosters | none | no full-size row materialization or independent full-stream evaluation |
| stream | static record order, zero retention, canonical footer, strict EOF; independently tested on a toy stream | none | no actual production stream inspected; built-in replay uses the same formulas |
| field | exact Q and Q(rho) representation; one field-valued polynomial per golden row | none | no actual-output field audit |
| safety | fail-closed cooperative checks and artifact writes at their coded scope | total-process interpretation of `aggregate_output_bytes` | authentication/sandbox and pre-context process caps are external |
| adapter text | source emits import-only exact Singular text | none | no Singular parse/import or actual `.sing` comparison |

## Formula and completeness audit

I rebuilt each closed polygon by an area decomposition independent of `baseline.lattice`, and rebuilt face powers by separate coefficient convolution. All six case/branch maps match (`baseline.py:89-167`). Rational and golden outer forms are respectively

`H=pi^2(pi^3+gamma^3)` and
`H=pi^2(pi^3+(3-2rho)gamma*pi^2+(2-rho)gamma^2*pi+rho*gamma^3)`;

the code fixes their complete `H^3,H^5` faces, using zero for every absent face monomial. Unequal inner values are exactly `1,kappa^3` for A and `5/(9kappa),5kappa^2/3,kappa^5` for B. Common faces are `kappa^3 G_k^3,kappa^5 G_k^5`, with `G_3=gamma(gamma*pi-1)^2` or `G_4=gamma^3(pi-1)^2`. Both origins are fixed zero. Intersections agree and no face slot is silently freed.

| case (each branch) | raw A/B | fixed A/B | free A/B | variables with lambdas | rows |
|---|---:|---:|---:|---:|---:|
| unequal | 83/215 | 12/19 | 71/196 | 269 | 803 |
| common-3 | 94/241 | 17/27 | 77/214 | 295 | 816 |
| common-4 | 115/296 | 17/27 | 98/269 | 371 | 816 |

Free IDs follow increasing A exponent pairs, then B pairs; common clients then have `c,z`; all clients finally append unrestricted, zero-permitted `lambda2,lambda3` (`baseline.py:132-182`, `exporter.py:211-242`). There is no extra gauge, Hermite/graph substitution, B compression, saturation, or support deletion.

For `J=A_gamma B_pi-A_pi B_gamma`, the row `(I,J)` forces `(k,l)=(I+1-i,J+1-j)` and adds `(i*l-j*k)a_(i,j)b_(k,l)` (`exporter.py:124-140`). Exactly the 660 pairs `0<=I<=23`, `0<=J`, `I+J<=38` are emitted; only `(2,0)` then subtracts c. Thus fixed `c=-5/(9kappa)` contributes `+5/(9kappa)`, while common clients subtract the one c variable. This target convention survived an actual sign corruption.

The apparently omitted 120 universal triangle positions are identities, not a truncation. The full degree triangle has 780 positions. Source supports have `i_A<=9`, `i_B<=15`, so every differentiated nonzero product has `I=i+k-1<=23`; total degrees at most 15 and 25 give `I+J<=38`. Negative I or J forces both corresponding exponents zero and hence determinant zero. Therefore the `I>=24` tail has `15+14+...+1=120` identically zero coefficients for every permitted assignment.

For the lift, finite expansion of
`gamma=v^-1`, `pi=v^4u-lambda2*v^2-lambda3*v-v^-1`
independently agrees with the loop at `exporter.py:143-169`. For source `(i,j)` and output `(t,e)`, it forces
`d=(e+i+j-5t-3b)/2`, rejects nonintegral/negative d or `z=j-t-b-d<0`, and contributes
`a_(i,j) j!/(t!b!d!z!) (-1)^(j-t) lambda2^b lambda3^d`.
The complete negative rosters are A: `t=0..2`, `5t-15<=e<0` (30), and B: `t=0..4`, `5t-25<=e<0` (75), including specialized zero rows. Six nonorigin fixed units produce metadata-bearing zero rows. Unequal c is already a fixed unit and its scalar-guard row is zero; common clients emit precisely `z*c-1`. No origin or lambda guard appears.

## Stream and coefficient field

`records()` regenerates and exactly compares the production specification before yielding anything. `payload()` orders header; displayed variables; every A/B coefficient-map record; every fixed-assignment residual (zero because the fixed value was substituted); all 660 J rows; all 105 lift rows; six fixed-unit rows; and the scalar guard (`exporter.py:181-281`). `row_record` retains empty polynomials. The footer independently records complete status, counts by kind, term and zero-row counts, all unused IDs, prefix-record count, and SHA-256 of every preceding canonical byte. `verify_stream` compares every expected canonical line and then requires true EOF (`exporter.py:284-290`). These mechanisms are **CONFIRMED**, but regeneration uses the production formulas themselves. No actual 803/816-row file was produced or inspected here, so independent full-stream certification remains **GAP**.

The pair arithmetic implements `rho^2=3rho-1` exactly: multiplication is `(ac-bd)+(ad+bc+3bd)rho`, inverse uses norm `a^2+3ab+b^2`, and wires contain two canonical rational pairs (`baseline.py:13-70,194-200`). Rational clients require zero rho component. In a golden row, each literal is one coefficient `a+b*rho` multiplying one monomial; the equation is never split into rational components. This preserves both formal embeddings and imposes no rational-point restriction.

## Cooperative production safety

Source inspection confirms duplicate-key-rejecting authority JSON; literal root GREEN/construction-only flags; nonempty job and 64-lowercase-hex registration fields; exact client, Linux/Amazon EC2 DMI board-asset-tag instance, and resolved cwd below `/home/ubuntu/`; exact pin dictionary and sibling-baseline hash; positive bounded caps; and a live timezone-aware deadline no farther away than the wall cap (`exporter.py:43-109`). Production APIs require a `ProductionContext`; unchecked arithmetic is toy-capped. The context installs CPU/AS limits and a real-time timer and repeatedly checks PID, PGID, cwd and monotonic deadline.

JSONL, optional Singular and manifest names are fixed from the validated client and opened with exclusive `xb`. One shared artifact budget charges before each write; failures retain partial files. Replay and a deadline check precede the exclusive manifest write. Source/AST inspection found no subprocess, shell, network, CAS or solver invocation (`exporter.py:293-383`).

These controls are cooperative safety checks, not authentication or a cryptographic sandbox. The registration hash is only shape-checked; no registry/signature is consulted. Dependency pins other than baseline are equality to compiled strings, not runtime reads. Imports, unbounded authority `read_bytes`/parse, DMI reads and initial hashing occur before the context limits. The three names are individually exclusive, not atomically reserved, and there are no uid, permission, fresh-directory, namespace or race controls. Those duties remain with the root runner.

One wording-level claim is **REFUTED** if `aggregate_output_bytes` means total process output: `main()` prints a second manifest representation to stdout after the budgeted manifest write, and stderr is also unmetered (`exporter.py:368-383`). The implemented cap is sound only as an aggregate **artifact-file** budget. A non-UTC aware offset is also accepted despite the `deadline_utc` name, though conversion to an absolute timestamp preserves the deadline. An external tightly capped pilot can compensate; this gate neither observed nor controlled that pilot.

## Singular import text

Static generation is **CONFIRMED import-only**. It declares `ring R=0,(...),dp` or `ring R=(0,rho),(...),dp` followed by `minpoly=rho^2-3*rho+1`; renders exact rationals and one `a+b*rho` coefficient; and uses only internally generated safe identifiers `A_gN_pN`, `B_gN_pN`, `c`, `z`, `lambda2`, `lambda3`. It writes every row, including `0`, with a label comment, then only the fixed completion marker, `size(I)`, and `quit` (`exporter.py:303-349`). `size(I)` is diagnostic, not certification. No Singular process or production expansion ran. Runtime parser/import acceptance and independent checking of actual adapter output remain **GAP**.

## Bounded controls and evidence

All commands used only the standard library and fresh paths under `box/d125-small-exporter-code-gate-sol56-20260906/`; each had 30-second wall, 25-second CPU and 512-MiB AS caps. The checkers accept `--inputs`, so a deleted lane snapshot can be relocated without changing review code.

`contract_formula_controls.py` (`7004cd15…`) passed normally and under `-O` in 0.071/0.116 seconds. It pinned all eight frozen inputs, compared 2,088 independently rebuilt map records including all 238 fixed records, checked all six variable/row counts and the 660/120 proof, and made 324 repeated-power lift plus 24 independent derivative comparisons. Receipts are `result-contract-normal-v2.json` (`c30b5067…`) and `result-contract-optimized-v2.json` (`e4c15b08…`).

`independent_tiny_controls.py` (`b017f755…`) used the frozen emitter only to form a degree-6 four-slot-per-member stream. Its separate formal-derivative oracle matched all 49 J rows; finite Laurent powers matched all 14 lift rows; and it recomputed canonicality, record/kind/term/zero counts, used IDs, prefix hash, footer and EOF. The 71-row original had identical hash `805255af…` in both modes. Six actual mutations—required-row deletion, golden equation component split, target sign, fixed-zero face, scalar guard, and lambda-variable exponent—each carried a fully repaired footer, passed footer-only validation, and was rejected by both the independent semantics and frozen strict replay normally and under `-O`. Receipts `result-normal-v2.json` (`05962ab…`) and `result-optimized-v2.json` (`62094619…`) passed in 0.103/0.150 seconds; recorded rejections were expected `ControlFailure` semantic mismatches/count mismatches and `ValueError` strict-replay mismatches.

For corroboration, `relocated_producer_controls.py` ran the exact frozen test from virtual fresh paths, not `run_controls.py`: 53 checks passed in each mode, and its six repaired-footer mutations exited 1 at the intended strict-replay `ValueError` in each mode. All 14 children terminated; receipt `producer-replay-v1.json` is `1aa2634d…`. No CAS, SymPy, Singular, AWS/network access, solver subprocess, full J construction or full lift generation occurred.

## Gate boundary

The formulas, complete index obligations, literal stream design, field representation and import-only adapter source are fit for a separately owned, tightly externally capped construction pilot. This does not promote any observed production output, performance or cost: none was inspected. Full actual-output semantic comparison and a bounded Singular import remain required. Properness, an ideal point, a counterexample, and necessity beyond the exact incoming conditional chain are not claims of this engineering gate. A second exporter is unnecessary for this scope because the verifier uses independent derivative and finite-power semantics; same-formula replay alone would not suffice.

<!-- BODY-END -->
