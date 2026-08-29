# Hostile different-model review: actual-total all-row grade-15 export V22R1

You are Grok 4.6, acting as an independent hostile mathematical and software
reviewer. Work in `/Users/dc/code/math/jc2`. Do not edit any campaign file,
case file, canonical ledger, or `jc2-lean`. Your sole permitted write is the
final report:

`xmodel/max12-812-order2-p0-total-rees-allrows-g15-v22r1-hostile-review-grok-20260827.md`

The producer is not trusted. Read and audit the complete case

`cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/`

including both preregistrations, both freezes, the V1 serialization erratum,
the V1 and R1 exporters/validators/launchers, and the two harvested successful
R1 roots `aws_q_r1/` and `aws_p65521_r1/`. Also inspect every pinned upstream
file necessary to assess the historical V9/V20 bridges and the V21 named-
section bridge. Do not infer a claim from a PASS token or producer JSON.

Observed top-level hashes to check independently rather than trust:

```text
PREREGISTRATION.md                    0c114f5990834b3ccdaa693d00a6265fd22dc72be7f7e501710b807def44b83c
PREREGISTRATION_R1.md                 34a087abdfc57efd6d1f898a6503a9129a8b93847d941bf5621f964234106eaf
V22_V1_SERIALIZATION_BRIDGE_ERRATUM.md caf6261223c8b196d43806112d4d3534e05269c5911a60f92e74921095015d13
export_allrows_g15_v22.py             c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6
export_allrows_g15_v22r1.py           d9f23a279b39b45ca27717a00493a6e928d1042007bc2c3c183eb2d239882768
validate_export_v22r1.py              763f31fdc6d01e016e74e12eeac8be84ec79cd78e35c6fc589bef1c5ab848b7e
aws_q_r1/RESULT.json                  829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8
aws_p65521_r1/RESULT.json             04c777e97b9113da9848c2c47fcfb3d880cc7b11319b74a0030dcc92aa92c94c
aws_q_r1/EVIDENCE.sha256              f213026a454c8f3171c0ce3c8b6cdfb6fe1a22e663caec08d47d08666309def9
aws_p65521_r1/EVIDENCE.sha256         7e862a38d91ee12913ab35af62ab1ed229f3335a2a375604b03e5ab47dc64d40
aws_q_r1/compiled/result.json         ba9cb4f2e30bd570e4231a262fad0a616111f9602ecdd00d61cb19427496c4f0
aws_p65521_r1/compiled/result.json    8e6a66100af7fe5a6981fbd396eeff6d0548c57a368d5c78395fa1143e023ec6
```

Audit at minimum:

1. Rehash every freeze/evidence entry after correctly remapping the remote
   path prefix to the harvested local root. Check completeness, not just
   listed-file integrity, and trace the two distinct AWS executions.
2. Determine whether V1 failed only because it demanded byte-identical text
   for semantically equal polynomials. Audit the R1 monkey-patch carefully:
   can it suppress any failure other than the exact named serialization
   bridge, can a duplicate/missing bridge pass, and are all 35 semantic
   equalities actually guarded in ordinary Singular before PASS?
3. Re-derive that the grade-15 emitter is exactly the reviewed V20 emitter
   extended one source coefficient, with cutoff 15 before construction. Check
   all 569 tails, weights, truncation sufficiency, variable/index conventions,
   rational arithmetic, and absence of accidental import side effects.
4. Independently verify every one of the 35 historical grade-10--14
   polynomial equalities. Explicitly distinguish exact-Q computation from a
   genuinely independent characteristic-65521 computation; say exactly what
   the second lane does and does not corroborate.
5. Parse all fourteen grade-15 files (seven Q, seven F65521) independently.
   Compare support and every coefficient after reducing Q modulo 65521. Check
   hashes, nonzeroness, term counts `133,224,355,140,585,200,759`, variable
   supports, rho evenness, and literal sigma-weight 15. Look for zero
   coefficients serialized modulo 65521 and latent telemetry defects.
6. Independently evaluate all four named sections. The required exact-Q
   residuals are: CS0 and Z00 all zero; A00 only row 6 equals `-1/16`; A10
   row 3 equals `-1/16`, row 5 equals `-(3/32)rho^2`, row 7 equals
   `-(3/128)rho^4`. Verify these from the full polynomial bytes and compare
   to the separately reviewed all-depth V21 theorem. Check the evaluation is
   discriminating with at least one mutation or unrelated nonzero section.
7. Audit all seven source-sensitivity controls and whether they meaningfully
   exercise the historical bridge. Inspect generated Singular for unguarded
   echoes, circular validation, qring/random/execute hazards, parser/ring
   hazards, and whether PASS can appear after a failed mathematical guard.
8. Search aggressively for convention drift or a missing source/Rees term.
   State exactly what the export certifies and what it cannot certify about
   J2 charts, formal arcs, Rees equations, Gate T, order two, maximum twelve,
   or JC2.

Use bounded local read-only checking only; uncertain/heavy algebra belongs on
AWS and should be reported as a gap rather than run locally. You may use
temporary files under `/tmp`, but leave no repo writes other than the report.

Give a decisive verdict: `CONFIRMED`, `CONFIRMED WITH REPAIRS`, or `REFUTED`.
List every defect and its actual mathematical effect. End with the strongest
precisely scoped theorem justified by the evidence and full reproduction
commands/checks. If something cannot be independently established, do not
soften it: identify it as a gap.
