# Tools

Run commands from the repository root. The campaign does not require a particular
model adapter or cloud provider. Start with the contribution tools; read a tool's
`--help` or module header before using it.

## Contribution and evidence tools

| Tool | Purpose |
| --- | --- |
| `open_collision.py` | Compare a report's raised open questions with banked research |
| `frontier_gate.py` | Check implemented classical degree exclusions |
| `artifact_finalize.py` | Optional transactional report publication |
| `seal.py` | Artifact integrity checks |
| `replay_gate.py` | Replay admission checks |
| `validate_charge_basis.py` | Validate declared exit-price metadata |

Read [the replay guide](../docs/REPLAY.md) for mathematical and artifact requirements.
Run focused tool tests with `python -m pytest ops/test_<tool>.py -q`.

## Mathematical replay scripts

The named `*_replay.py`, generators, and enumerators support particular reports.
Use the report's exact basis, inputs, scope, and replay command. A script's presence
is not a recommendation to rerun a retired experiment or proof of a mathematical claim.

## Optional orchestration

`lane.sh`, `lane_systemd.sh`, `lane_detach.py`, `adapters/`, `run_capped.py`, and
[fleet/](fleet/README.md) are reusable orchestration implementations with their own
assumptions. They are not the contributor bootstrap. Configure your swarm's environment
and authority separately. `status.sh` displays an explicitly supplied swarm state file.

Older `aws_*`, route-specific launch scripts, telemetry, and prompts remain for
reproducing earlier work. They may contain historical deployment settings. Use them
only with their original report and reviewed scope; current HQ operation is documented
in HQ's separate workspace. No credentials, private inventory, or live queue belongs
in this directory. Existing frozen logs/receipts remain evidence; new transient logs
are ignored and should be kept in the swarm workspace.
