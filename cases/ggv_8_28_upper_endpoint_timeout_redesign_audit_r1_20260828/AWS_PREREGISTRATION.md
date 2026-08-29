# Preregistered AWS execution contract: proper-open resume

Status: `DESIGN_FROZEN_LAUNCH_NOT_AUTHORIZED`.

No instance or job may be launched from this document without a later explicit
GO and a frozen adapter source/archive hash plus hostile review.

## Frozen mathematical inputs

The only production inputs are the four terminal archives in
`FROZEN_INPUTS.sha256`. Per-branch scripts must pin the node-input, witness,
partial-transcript, pivot, residual, and `OPEN_SB` hashes recorded in
`DESIGN_AUDIT.md`. Original bytes remain immutable.

## Lane order and resources after a future GO

1. Pilot `TRIPLE02` first because its exact open basis has two generators and 169
   bytes. Fanout remains held until this pilot passes every adapter, reducer,
   semantic-plant, and full-kernel marker.
2. If the pilot is clean, run `Q1P02`, `C8P02`, and P as independent lanes; do not
   serialize them or combine their verdicts.

Each lane uses one pinned CPU on AWS Linux/Amazon EC2, preferably a 128-GiB
memory-optimized instance and never more than 1 TiB. Swap total/free must be zero
at preflight, every 10-second telemetry sample, and termination. The pilot hard
cap is 30 minutes; Q1P02/C8P02 are 45 minutes; P is 60 minutes. Per-process virtual
memory is capped at 96 GiB on 128-GiB hosts, file output at 32 GiB, and all child
processes must stay in one recorded PGID/SID. A swap event, orphan, host/IMDS/tag
mismatch, or cap event terminates only that lane with no verdict.

The source archive, preregistration, adapter, controls, original inputs, generated
scripts, stdout/stderr/time, exact outputs, telemetry, process identities, and
terminal manifest must be archived. Singular diagnostics are fatal regardless of
return code.

## Mandatory preflight controls

- Proper fixture: `I=(x*y)`, `Delta=x`; require saturated ideal `(y)`, nonunit,
  stable, `NF(Delta)!=0`, and `EMPTY_POWER_SEARCH_ENTERED=0`.
- Empty fixture: `I=(x^3)`, `Delta=x`; require unit saturation and an exact
  membership witness with exponent 3, with `EMPTY_POWER_SEARCH_ENTERED=1`.
- Mutations reversing the dichotomy, deleting the proper-skip marker, replacing a
  proper basis by `(1)`, or making the old 257-step loop reachable must be rejected.
- Reducer adversary: a displayed factor that belongs to a pinned ideal must reduce
  to zero before any factor/content interpretation.
- Endpoint semantics: an actual diagonal `e`, nonzero `NF(e+1)`, zero affine replay,
  and a bordered zero expression whose `+Delta` replay is nonzero and equals
  `NF(Delta)`.

## Required production markers

Before chart construction:

- `ARCHIVED_SATURATION_PREFIX_EXACT=1`
- `OPEN_STANDARD_BASIS_REPLAY_FAILURES=0`
- `NODE_IDEAL_INCLUSION_FAILURES=0`
- `SATURATION_STABILITY_FAILURES=0`
- `OPEN_UNIT_NF_NONZERO=1`
- `OPEN_DELTA_NF_NONZERO=1`
- `OPEN_DICHOTOMY=PROPER`
- `EMPTY_POWER_SEARCH_ENTERED=0`
- `PROPER_OPEN_RESUME_CERTIFICATE_COMPLETE=1`

Before a mathematical terminal marker:

- `NF_RATIONAL_UNIT_PIVOT_COUNT=95`
- `NF_PIVOT_INVARIANT_FAILURES=0`
- complete next-size-minor identity count with zero failures
- complete 106-row kernel replay count with zero failures
- complete endpoint diagonal/cross coefficient count
- `ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=1`
- `ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=1`
- `BORDERED_NONZERO_PLANT_EQUALS_DELTA=1`
- `NO_CLOSED_COMPLEMENT_OR_WHOLE_COMPONENT_INFERENCE=1`

## Exact terminal classifications

- all endpoint coefficients zero:
  `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY`;
- at least one endpoint coefficient has nonzero normal form:
  `RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_PENDING_NILPOTENCE_RADICAL`;
- banked-vs-replayed reducer/basis/stability disagreement:
  `REDUCER_DISAGREEMENT_NO_VERDICT`;
- source, parser, control, diagnostic, or marker failure:
  `ADAPTER_FAILURE_NO_VERDICT`;
- hard cap: `TIMEOUT_NO_VERDICT`;
- infrastructure/swap/containment failure:
  `INFRASTRUCTURE_FAILURE_NO_VERDICT`.

No terminal classification from one lane promotes another lane, the closed
complement, a whole component, or an ambient endpoint statement.
