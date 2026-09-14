# Resume round 2: independent mathematical and acceptance audit

Scope: read the three frozen charged mathematical reports and frozen FALLACY-v2, then inspect retained small implementation/proof/control artifacts. The parent mechanically verified the frozen-input hashes before this audit. No worker lifecycle action, heavy computation, worker-tree copy, ledger edit, jc2-lean edit, or ideation edit was performed. This note does not itself certify any production solver result.

## 1. Theorems A and B can be retained, with their existing scope

Theorem A may be restated verbatim from charged report lines 34–36:

> Over a characteristic-zero field, every realized datum satisfying Moh's monic Keller setup has, at each effective index, a specialized constant-coefficient target polynomial whose composition has actual y-degree D_i and nonzero scalar leader. Therefore its coefficient equations, exact upper-degree equations, scalar-leader equations, and a leader localizer are necessary equations on any coefficient chart intended to contain every such realization.

The source bridge is essential: Moh's coefficient specialization psi acts on formal target coefficients before composition, not on the physical source x after composition. Printed Proposition 2.2 supplies equality, with scalar-unit leader for M_i<e=n−1; terminal M_h=n−1 is excluded from the effective list. The report's separate p172 root-order argument supplies total degree in the already placed coordinates. Do not attribute that stronger assertion to Proposition 2.2 alone.

The effective degree sequences and relevant normalized depths are:

| Client | (n,m,D2) | all displayed effective degrees | full ambient Q bound | leader depth |
|---|---|---|---:|---:|
| (99,66) | (99,66,55) | 66,55,145 | 198 | 143 |
| D108 | (108,72,63) | 72,63,227 | 216 | 153 |

The existential full target family is Q=G³−F²+aG²+bFG+cF+dG+e0. All five lower scalar target variables are retained. The positive-degree rows do not determine e0; it is an unused free coordinate, not a missing equation. Family representatives are necessary enlargements, not independently certified canonical characteristic polynomials.

The complete physical degree/leader block has coefficients q_pq=0 for q>D2, q_p,D2=0 for p>0, q_0,D2−lambda=0, and Zlambda−1=0. The total-degree implementation additionally kills every coefficient with p+q>D2 and imposes the complete homogeneous target: lambda*y^15*(y−x)^40 for 99, lambda*y^14*(y−x)^49 for D108. These are exact characteristic rows adjoined to every finite stage, not consequences of shallow truncation.

Theorem B may likewise be retained: in the full source coefficient charts, actual D2 faces together with attained constant-target degree 55/63 exclude every point with J(F,G) identically zero. The proof is sound under its explicit hypotheses. Zero Jacobian in characteristic zero gives F=f(H),G=g(H). With deg H=deg_y H=k0, attainment yields k0|gcd(n,m,D2), namely 11 or 9. Unique factorization of the fixed F top then forces (k0,deg f)=(11,9) or (9,12). The actual physical D2 F valuations are −9 or −12, so the F faces would be ninth/twelfth powers. Actual root multiplicities 24/21 contradict that divisibility. The common-polynomial source is retained at its reported hash; this audit consumed the local supplied proof/source discussion and did not add a new external citation.

The actual faces are (pi³−1)^24,(pi³−1)^16 for 99 and (pi⁴−1)^21,(pi⁴−1)^14 for D108. They require the outer equality-face audit: offset-zero outer D1 moments kill all outer equality contributions, with exact-Q ranks 11,11,8,11 and 9,9,7,9. A floor alone would not prove those faces. Retain the actual source-map images and residual rows through every optimization.

The T2-only chart permits a nonconstant Jacobian of degree at most 20/25. The stronger all-effective-degree theorem, which additionally requires T3 and compatibility, cannot be applied to these runs. Neither Theorem A nor B alone decides any unrestricted branch ideal.

## 2. Exact verdict typing

A completed validated proper ideal should be labelled **PROPER — EXACT-Q-PROPER-AUGMENTED-IDEAL: existence over Qbar of a nondegenerate necessary-chart survivor**. The exact charged-text language to preserve is:

> Consequently, a verified proper complete augmented ideal over Q would, by extension of scalars and the weak Nullstellensatz, prove existence of a point over Qbar with J not identically zero. It would be an existential nondegenerate necessary-chart survivor, even if no coordinates were extracted. It would not be a Keller pair: its Jacobian may have degree up to 20/25. A timeout, a memory failure, or a partial coefficient construction proves no properness and supplies no such survivor.

This semantic statement actually occurs in charged §6; §7 gives the implementation and controls. Older retained driver labels NONUNIT_NOT_POINT or EXACT-Q-NONUNIT-NO-POINT predate/suppress this strengthened consequence and must not be reported as “no point exists.” Properness gives existence without exhibited coordinates. Restore inactive free variables via the declared injection; polynomial coefficient rings remain faithfully flat under extension to Qbar.

A unit after all acceptance checks and independent replay supports **DEAD ON THE AUGMENTED NECESSARY CHART — PROVED-HERE (gate)** for the precise coverage-valid branch. A unit in a necessary enlargement safely excludes its source locus. A unit confined to an unsupported slice excludes only that slice. Do not call the old Delta unit or a toy negative control a branch kill.

Resource limits, parser rejection, incomplete emission, missing result markers, stale metadata, process death, and a partial Groebner computation all remain **OPEN**, refined as compute-bound / memory-bound / CAS-error / construction-bound with stage, observed wall and observed peak RSS. A basis-size or dimension line printed before completed result markers proves no properness. Missing RSS is “not captured,” never zero. Mark parser-invalid attempts as quarantined, not successful stage results.

A validated proper stage is a survivor of that finite necessary stage; do not call it a stage-8 survivor unless the completed stage is 8. A validated unit at stage s excludes every stronger stage once audited cumulative inclusion is recorded; still itemize the requested stage schedule and any live/cancelled/incomplete attempts. A stage-8 proper result similarly implies properness of genuinely weaker included ideals, but inference is distinct from execution custody.

## 3. Gauge coverage and derived consequences

Beta=1 spends the residual simultaneous source dilation once: F_alpha=alpha^(−n)F(alpha*x,alpha*y), G_alpha=alpha^(−m)G(alpha*x,alpha*y). Beta transforms by alpha^(−4)/alpha^(−5); lambda by alpha^(−143)/alpha^(−153). Lambda, separation, and Jacobian scalar must remain free/nonzero where required. Selecting a root conjugate alone does not normalize beta.

For 99 the frozen complete diagonal-translation proof permits jet0=0 while retaining minor_a2/v and transporting all source coefficient images, finite rows, target scalars, and lambda. Rational graph pivots do not invert coefficient variables. Radical front consequences are algebraic-set consequences, not falsely certified linear ideal identities. The cutoffs are stage0 D≤29,C≤60; stages1–8 D≤30,C≤62. No stronger cutoff is justified by the retained proof; the next-band graph retains its scalar tau including tau=0.

The frozen D108 even-face/three-jet chart has a documented universal-coverage gap. Its mu=0 restriction is not justified by centering the abstract face while leaving the physical generic arc fixed. A unit there cannot alone prove DEAD for the full D108 branch. The supplementary repaired chart keeps minor_mean=mu with h3 face −((pi−mu)^2−c) and complete F/G target powers 12/8; c≠0. At mu=0 it recovers the frozen equations. Strong-front cutoffs remain stage0 D≤32,C≤66; stages1–8 D≤33,C≤68.

The later retained theorem d108-meanfree-translation-theorem.md permits a jet0=0 slice **after** the full-mean repair. It gives j0'=j0−q, u'=u, v'=v−qu, mu'=mu+q²u−2qv, c'=c; taking q=j0 retains every mean, including the u=v=0 boundary. Its inverse explicitly identifies full chart with slice times a free affine coordinate. Exact complete minor-prefix transport through local order12 and actual major/outer source maps are checked in d108-meanfree-translation-control.json. This supports meanfree_jet0_stage8_slimgb if its actual input binds to the retained maps and meanfree_stage_v2.py. It does not authorize jet0=0 in the frozen mu=0 chart.

The alternative D108 computational translation T_q of h and outer coordinates is an invertible algebraic presentation; it keeps the original minor variables/rows. Do not describe it as an unsupported source-gauge slice.

## 4. Leading-target subtraction, including the user's 17(rrrrrrrrr)/(nnnnnnnnn) check

Those literal numbered labels do not appear in the three frozen charged mathematical reports. The substantive required check is fully specified there: every leading pole tag is actual coefficient minus its derived complete target; strict-lower tags remain homogeneous zero rows. Do not invent a missing source citation to those literal labels.

| Source branch | F leading local power / target | G leading local power / target |
|---|---|---|
| 99 delta2 | 81 / (zeta²(zeta+3rho))^9 | 54 / (zeta²(zeta+3rho))^6 |
| 99 delta5/2 | 189 / (pi(pi²−c))^9 | 126 / (pi(pi²−c))^6 |
| D108 frozen delta3 | 96 / (pi²−c)^12 | 64 / (pi²−c)^8 |
| D108 repaired delta3 | 96 / ((pi−mu)²−c)^12 | 64 / ((pi−mu)²−c)^8 |

The gate shows that treating the top pole coefficient as coefficient=0 manufactures units, e.g. D108 constant coefficient c^12. Existing controls prove strict-lower identity and corrected Delta witness cancellation. The requested shallow stages do not reach these leading local powers, but the emitters must still define the correct convention.

In the complete characteristic circuit, the reduced ambient normalizer is 6k−2=196/214; its target depths 141/151 represent the same physical rows as original depths 143/153. The complete circuit leader targets are lambda*z^40*(1+z)^15 and lambda*z^49*(1+z)^14. Check all 16 or 15 binomial coefficients, exact sign, all target positions, and the leader localizer. Require no accidental leader term in source/graph rows, no lambda=1 pin, and no lost coefficient because a support table omitted an otherwise zero entry. Existing target-subtraction-audit.json covers ten scripts only; bind its script hashes or redo the lightweight check per emitted production stage.

The source h3/F/G pole targets, characteristic whole target, and leader localizer are three different obligations. Passing one does not establish the others. The positive attained backend control is deliberately outside the actual D2 faces and is not a branch survivor; correct face yields proper, wrong target yields unit.

## 5. Production acceptance and table requirements

Before interpreting each result, bind client, branch, stage, source-chart variant, source coefficient map, ordered polynomial-ring generators, coefficient field Q, monomial order, localizers, input SHA-256, emitter/driver SHA-256, emitted script SHA-256, and exact output SHA-256. Include return code, elapsed wall, and observed peak RSS separately from time/memory caps. For large worker outputs, retain only their hashes and compact observations locally. If a file changed during a run, reject that run until a stable bound version is established.

Require full script emission plus ALL_ROWS_PARSED, the expected ideal-row counts including every high-remainder and inclusive characteristic target coefficient, completed BEGIN_GB/END_GB and BEGIN_RESULT/END_RESULT markers, return code 0, no parser/CAS errors, and completed BEGIN_CONTROLS/END_CONTROLS with exact values [0,1]. Match output to the same unchanged script hash. Standard result format is [reduce(1,SB),dim(SB),size(SB)] with exactly three parsed entries and reduce-one exactly 0 or 1. Inspect actual output independently of the status string.

The coefficient graph is acyclic and monic, hence projects isomorphically to the full remainder ideal; all high-z remainder rows are retained. Characteristic t cutoffs are exact because multiplication cannot decrease t order. Optional graph_h_expr needs its own input-map graph audit. All original source residuals must be transported after rational/front substitutions. The graph ring contains no physical t,z, so do not subtract two dimensions; older remainder rings include t,z. A translation gauge may require restoring one free dimension when comparing full source schemes.

The current audited circuit emitter hashes 17a825098e24dcbeb973d7fe6f254c6f5884f2aad9bed196e12166db0520ce35. Its support controls bind that hash. Retained v2 toy-control metadata instead records emitter 9fd1880a..., while the independent projection controls bind exact positive/negative scripts cb38e088... and c60ee2f9.... Therefore do not assert that all old toy controls were generated by the current emitter without checking the intervening change or regenerating/rerunning the tiny controls. The retained run_singular_case.py hashes d3189becd3407fb74bf0bdfbaf82e4dd18f8a88c223b19bb39fcaa8957bdf191 and rejects failed markers/parser errors, but does not itself explicitly require ALL_ROWS_PARSED; check that independently in the final acceptance reader.

Charged §8 is a pending paragraph, not an already populated table. Reissue a table listing all stages0–8 for 99 delta2, 99 delta5/2, and D108 delta3, explicitly distinguishing frozen/full-mean variants and selected optimized attempts. Suggested compact columns: client/branch/chart, stage, attempt, rc, wall, peak RSS, full-block+controls, raw solver completion, accepted verdict, custody record. Record unevaluated/incomplete stages rather than silently aggregating them as proper or unit. A summary per client/branch may follow that full stage table.

For any unit add independent exact-Q replay and bind its script/output hashes, plus the above gauge/derived-face/target checks. Preserve the difference between exact unit, replayed gate proof, and universal branch coverage. For any proper result print the strengthened existential nondegenerate consequence prominently and attempt coordinates only if feasible. If every production attempt is bounded, the safe final language is: “Theorems A/B remain established. The augmented finite decision is compute-bound OPEN for [branches]; no accepted branch unit or completed proper augmented ideal was obtained.”

Worker termination and its receipt must precede the report seal. The final report should retain the exact BODY-END seal, replace pending-closeout language, and state which assertions are proved and which remain OPEN. No new exit-price assertion arises here, so no FALLACY charge_basis line is appropriate.

## 6. Fresh bounded exact-Q reruns in this resume

The parent requested fresh reruns of the small independent controls. All four completed with return code 0. Their executed sources differ from the inherited source only by redirecting the output path into resume-r2; execution preserves each original __file__ for dependency/hash lookup and sets PYTHONDONTWRITEBYTECODE=1. Original source, executed source, precise replacement, elapsed wall, output and log hashes are recorded in fresh-math-controls.json and individual fresh.custody.json files. All four fresh JSON objects are exactly equal to their inherited JSON objects.

| Check | Wall seconds | Fresh output SHA-256 |
|---|---:|---|
| source degree arithmetic, Delta and depressed identity | 0.415 | 3180da44b188733fff5516c76dc5d4519e88429bd53066444602c55216a5177c |
| actual D2 equality ranks and common-generator obstruction | 0.365 | a79fff99d3214aa6e0c180b8dfc636e91bc2bca4ad0fb4186b3fa8e0282e19e4 |
| all64 exact-Q coefficient-circuit support tests | 0.365 | f2a33d1986fe192a5641d3880611ea0ae311376e0f1dc154a421e5807aceec13 |
| generic monic remainder identity and high-row recovery k=2,3,4 | 1.716 | e7dd0292edb4cbe7ebe727d53e3b3d3503204ef8e959837e15a801e6c0b39f9e |

These fresh tests substantiate theorem arithmetic and generic complete-block equivalence. They are independent exact controls, not a completed production chart ideal or replacement for per-stage script/input/output custody.
