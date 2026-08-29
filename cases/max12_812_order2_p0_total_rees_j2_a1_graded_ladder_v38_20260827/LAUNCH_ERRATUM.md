# V38 launch-orchestration erratum

Date: 2026-08-27

The immutable `launch_host.sh` extracted its source bundle correctly but then
started each remote `run_aws.sh` from the SSH account's default directory
instead of the extracted source root.  The first two pilot starts therefore
failed immediately with `run_aws.sh: No such file or directory`, before any
freeze check, compiler, or mathematical computation ran.

No frozen mathematical program or manifest was changed.  The additive
`launch_host_v2.sh` changes only the remote invocation to `cd` into the
hash-addressed source root before starting `run_aws.sh`.  Its own hash is
recorded in `FREEZE_LAUNCH_V2.sha256`.  The two pilot jobs were restarted by
the same explicit `cd` invocation and passed their full frozen compiler,
validator, stdout-binding, and relocatable-evidence contracts.
