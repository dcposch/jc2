# Frontier external-108 overlay implementation

Status: **COMPLETE / UNREVIEWED_PENDING_DIFFERENT_MODEL_GATE**.  The scoped
implementation and focused regression are complete.  The tool intentionally
continues to require the campaign's manual external check until a different
model reviews the new overlay.  No claim about openness, a counterexample, or
an internally replayed proof of the external theorem is made.

Receipt start was 2026-09-06T12:40:54Z; the completed pre-seal audit ended at
2026-09-06T12:57:16Z, 16 minutes 22 seconds later and within the 30-minute cap.

## Result

`ops/frontier_gate.py` now reports two independent theorem results without
changing the meaning of its legacy gcd fields.  The cited GGHV consequence is
implemented only in its robust form: for a characteristic-zero polynomial
counterexample candidate `P,Q in K[x,y]` with nonzero constant Jacobian, the
declared actual maximum total degree cannot be strictly below 108.

The legacy `theorem`, `source`, `verdict`, and `reason` remain exclusively the
`GGV-Heitmann-gcd16` result.  New separate fields are:

- `external_theorem`: theorem name, statement, v1 source URL, and frozen PDF
  SHA-256;
- `trust`: `CITED_EXTERNAL_THEOREM`, `AUDIT17(jjjjjjjjjjjj)`, and the explicit
  fact that the external chain was not internally replayed;
- `actual_degree_context`: polynomial/characteristic-zero/nonzero-constant-
  Jacobian context, whether an actual-total declaration exists, and an
  explicit `transformed_chart_degrees_supported=false`;
- `scope`: strict criterion, applicability, and either an attained fixed-pair
  maximum or a separately typed inclusive cap;
- `conclusion`: `EXCLUDED_BY_EXTERNAL_LT108`,
  `INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND`, or
  `OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED`;
- `overall_verdict`: the effective purpose-aware union of the gcd and external
  theorem results.

For `purpose=frontier`, either theorem's exclusion produces
`REFUSE_CLASSICALLY_CLOSED` and process status 3.  For an explicitly supplied
`purpose=method-control`, the same exclusion produces `METHOD_CONTROL_ONLY`
and status 0.  If neither theorem excludes the registered scope, the effective
result is only `NOT_CLOSED_BY_THIS_GATE`; it asserts neither openness nor
existence.

No sub-125 arbitrary-pair list or census filter was implemented.  The strict
external floor is not treated as attainment: fixed or capped level 108 remains
inconclusive.  Partial-y degrees with unbounded total degrees are outside both
actual-total theorem applications.  Laurent/transformed-chart degrees and
nonconstant-Jacobian `J=x^k` charts are explicitly unsupported, not classified
as polynomial Keller degrees.  The interface has no transformed-chart option;
unknown options are refused by argparse, while the accepted total-degree
options explicitly declare original-polynomial actual total degrees.  The gate
records that it cannot verify the truth of a caller's mathematical declaration.

## Frozen inputs and source trust

All five files in `/tmp/jc2-lane.jM6LSe/inputs` were read from that directory.
Their pins were mechanically checked against `charged-inputs.list`; all five
passed.  At initial verification their live charged counterparts also matched
byte for byte.  The source PDF, present beside the charged text, independently
matches the hash frozen in the round packet and `AUDIT17(jjjjjjjjjjjj)`.

| Input | SHA-256 |
|---|---|
| frozen `frontier_gate.py` | `d709794d7702103d6cf0c33cd9f903064c3fd602df884713f9c23fc115bba631` |
| frozen `COORDINATION.md` | `d6f75d19c0545c1bc27cbcdeb8e4ee92082b798da3791331d848283575bc9b99` |
| frozen synthesis | `e2aa98d754101057ffdd818f35ddd35808cc6e2c79eeb5eed475472b76770cf2` |
| frozen GGHV v1 text | `f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368` |
| frozen `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |
| source PDF | `ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd` |

The cited source is `https://arxiv.org/abs/2204.14178v1`.  Its full imported
reduction/classification chain remains externally trusted rather than
internally replayed.  The implementation consumes only the confirmed strict
actual-max-degree consequence, not Theorem 2.1's normalized sub-125 list.
There is no new exit-price assertion, so the FALLACY-v2 charge-basis rule is
not applicable.

An unrelated root-owned update changed live `COORDINATION.md` after the initial
pin check (12:42:46Z snapshot SHA
`85baaafc19e5a10087c3f946994dba149b67d4353fd3c7a928897dd9f948576e`).
This lane neither edited that file nor substituted its later bytes for the
frozen charged input.  All other non-gate charged counterparts remained equal
to their frozen copies at the final preservation check.

## Consumer compatibility

The repository was searched for every command invocation, import, and output
reader of `frontier_gate.py`, and every hit was inspected before selecting the
additive schema.

- `ops/test_frontier_gate.py` parses JSON and checks only the legacy `verdict`
  plus process status.  Its four tests pass unchanged; extra keys are accepted.
- The identical
  `box/full-j-solver-pilot-20260906/{harvest.py,evidence/harvest.py}` consumers
  call a frozen worker-local gate through `subprocess.check_output` and save
  stdout without parsing it.  Their frozen evidence is untouched.  If the new
  gate is deliberately copied into that workflow, its existing 99/66 frontier
  command now aborts on status 3 as the requested fail-closed behavior; a
  method/source-validation replay must explicitly switch to
  `--purpose method-control`.
- Current registration documents and historical reports contain archived
  commands/results but no machine reader or exact-key schema dependency.  They
  were not rewritten.
- Canonical `COORDINATION.md` currently describes the legacy `verdict` to human
  consumers.  Because 99/66 must retain a gcd-inconclusive legacy verdict, that
  prose alone cannot consume the new closure.  Root's required manual external
  check therefore remains necessary until an independent review authorizes a
  canonical policy update to consult process status or `overall_verdict`.
- No Python import/API consumer and no parser of `registered_scope` or saved
  `frontier.json` was found.

Thus the JSON change is additive and the legacy theorem result remains
semantically stable.  The intentional compatibility boundary is the new
effective nonzero process status for externally closed frontier work.

## Controls and mutation evidence

The complete result matrix is
`box/frontier-external108-overlay-sol56-20260906/control-matrix.tsv`.

| Registration | Legacy gcd verdict | External conclusion | Effective result / status |
|---|---|---|---|
| actual 99/66 | `NOT_CLOSED_BY_THIS_GATE` | excluded `<108` | refuse / 3 |
| actual 108/72 | inconclusive | inconclusive at 108 | not closed by gate / 0 |
| actual 108/108 | inconclusive | inconclusive at 108 | not closed by gate / 0 |
| common inclusive cap 107 | inconclusive | excluded `<108` | refuse / 3 |
| common inclusive cap 108 | inconclusive | inconclusive | not closed by gate / 0 |
| partial-y 99/66, totals unbounded | inconclusive | out of scope | not closed by gate / 0 |
| actual 99/66, explicit method control | inconclusive | excluded `<108` | method control only / 0 |
| actual 108/107 | gcd closure | external inconclusive | refuse / 3 |
| old actual 9/12 and old cap 12 | gcd closure | also external closure | refuse / 3 |

Nonpositive fixed degrees, caps, and partial-y degrees retain argparse status 2,
empty stdout, and the existing `all degrees and caps must be positive integers`
diagnostic.

The focused suite creates two actual temporary source mutants and evaluates
them with a fixed behavioral oracle.  Replacing the strict comparison `<` by
`<=` is rejected by the cap-108 control; replacing the partial-y branch's
unknown actual maximum with `max(deg_y_P,deg_y_Q)` is rejected by the unbounded
partial-y control.  The production gate hash is checked before and after these
mutants.  The additional actual 108/107 control detects dropping the gcd side
of the effective `gcd_closed OR external_closed` rule.

Final capped command:

```text
/usr/bin/time -v timeout --signal=TERM 30s prlimit --as=536870912 -- python3 -m unittest -v ops.test_frontier_gate ops.test_frontier_external108
```

Result: **PASS, 14/14 tests**, exit 0, 0.78 seconds wall, 20,704 KiB maximum
RSS.  `python3 -m py_compile` and `git diff --check` also pass.  No AWS, heavy
CAS, regeneration, solve, adapter edit, external post, or stage commit ran.

## Output hashes

| Output | SHA-256 |
|---|---|
| `ops/frontier_gate.py` | `18367153f8b89126c57557edf8e5c53dddf8475bd617aed47848072c29516812` |
| `ops/test_frontier_external108.py` | `cd146c616a71034cf9c4d473abf922b2a1ec251aaff58e8f1aa4ae0e483ccf0a` |
| `input-pins.sha256` | `605ac3c8bfdbf83af48bdbccde638c76fb1471927b70ac0bee7f23ab40e601ab` |
| `control-matrix.tsv` | `b9250389406b87670499bf03c49fdd6faa96bae54f57c7f53e1a30e6938d5f66` |
| `test-results.txt` | `bd89c857de4d148efbdf2ce8a8dddbe165009375c4c8cb676fb3e3b1cea3437a` |

`box/frontier-external108-overlay-sol56-20260906/output-pins.sha256`
mechanically verifies all five rows above.  The focused test separately pins
the implementation plus the GGHV PDF and text inputs.

## Residual gaps and completion handshake

- The GGHV chain is cited external trust; it was not internally reconstructed
  or replayed here.
- The overlay implementation remains unreviewed until a different-model gate.
  Same-model read-only audits found no blocking defect but do not discharge
  that requirement.  Manual external checking remains required meanwhile.
- The focused immutable-source test depends on the campaign's local untracked
  GGHV PDF/text artifacts and is therefore workspace-specific rather than
  portable to a clean checkout lacking those charged sources.
- There is no typed transformed-chart CLI mode.  Such degrees are explicitly
  unsupported and must not be passed as actual totals; this declaration is not
  machine-provable from integers alone.
- At level 108 the implemented bound is inconclusive only.  It does not claim
  the 72/108 or 108/108 scopes are open, attainable, or otherwise viable.
- No census, arbitrary-pair sub-125 classifier, internal unit certificate,
  external theorem proof, D108 source-map result, or JC2 result was produced.

Completion handshake:

```text
tag=frontier-external108-overlay-sol56-20260906
status=COMPLETE
receipt_start_utc=2026-09-06T12:40:54Z
completed_preseal_utc=2026-09-06T12:57:16Z
elapsed_to_completed_preseal=00:16:22
implementation_review_status=UNREVIEWED_PENDING_DIFFERENT_MODEL_GATE
manual_external_check_required=true
owned_live_writers=0
charged_frozen_inputs_verified=5/5
source_pdf_hash_verified=true
output_manifest_verified=5/5
legacy_and_focused_tests=14/14_PASS
mutants_rejected=2/2
unrelated_dirty_files_preserved=true
canonical_docs_edited=false
stage_commit=false
ready_for_root_independent_gate=true
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11043`.
- Body SHA-256:
  `c72da23ee57c2165d1b7158f0dbc86206f95ca0f233b3d81ea7890dc0656244a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
