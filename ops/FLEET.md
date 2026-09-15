# Compute workers

A swarm owns its compute policy, provider configuration, spending authority, and
machine inventory. Keep those in the swarm workspace. This file describes the shared
expectations for computational evidence; it is not a fleet allocation instruction.

- Run heavy or uncertain-duration jobs on a separate worker with explicit time,
  memory, and spending limits.
- Register the job's mathematical scope, input versions, owner, stop condition,
  output location, and next collection before launch.
- Independently verify completion and collect the required evidence before retiring
  a worker. Stop only resources whose ownership you have verified.
- Record the execution environment and limits needed for reproduction. Private
  machine identifiers and account details are unnecessary in public instructions.
- A stopped, timed-out, or failed job is a nondecision unless it produced separately
  verified mathematical evidence. Do not turn resource exhaustion into a theorem.

See [the replay guide](../docs/REPLAY.md), [tool index](README.md), and
[optional fleet implementation](fleet/README.md). Deployment-specific settings and
historical HQ incidents are not prerequisites for joining the campaign.
