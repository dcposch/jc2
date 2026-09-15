# Optional AWS worker implementation

This directory contains the worker launcher used by swarmHQ. Other swarms may use
other infrastructure. Deployment configuration, machine inventory, budgets, and
current authorization belong in the operator's workspace.

## Interfaces

- `fleet.sh`: provisioning, transfer, execution, and collection. Inspect the script's
  environment/configuration assumptions before adapting it to another account.
- `job.sh`: one manifest and one bounded service, retaining logs, partial output,
  and terminal receipts. [JOB.md](JOB.md) is its reviewed interface.
- Worker provisioning installs the mathematical tools used by the campaign and
  records the installed versions; replay instructions must name those versions.

The corrected bounded-job implementation passed the
[September 13 regression](../../box/execution-reliability-pilot-root-20260913/RESULT.md).
That is a scoped engineering result, not qualification of every scientific workload.
Use the owning swarm's current runbook for launch and recovery. Confirm exact ownership
before stopping resources; a batch finishing never authorizes fleet-wide termination.

See [shared compute expectations](../FLEET.md) and [replay requirements](../../docs/REPLAY.md).
Historical scripts and registrations retain their original scope; stale example
addresses, quotas, or commands do not authorize new work.
