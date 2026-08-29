# Cutoff-three modular r6d R2 preregistration

Date: 2026-08-28

Status: **HOLD — explicit coordinator clearance required**

## Exact scope and charge

This is one discovery-only modular `core` reconnaissance over all six
nonzero-`V` localization charts.  It is a fresh successor to the contained
R0 operational abort, not a continuation or replay of its run namespace.
No modular outcome is promotable; any chart used in a closure still needs
an exact-Q certificate and the complete six-chart exact cover.

Host: r6d, instance `i-07eeaf8ba6f0bc419`, public `100.26.198.153`.

Immutable source:
`/home/ubuntu/jobs/ggv_8_28_tail3_source_r1_20260828T050159Z`.

Fresh run root, currently absent:
`/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r2_20260828T050159Z`.

Archive SHA-256:
`be3a9915cea967e01b634b637f39d482204316f041dd6c57f6e64592a8cf6b87`.
The charged inner source, target, worker, PGID guard, regression, preflight,
runner, and stop hashes are listed in `CONTAINMENT_REPAIR_R1.md`.

The charge is six simultaneous 40-GiB address-space workers, six-GiB output
limit per worker, 21,600-second job and global wall limits, 240-GiB maximum
aggregate worker address space, 150-GiB live MemAvailable floor, 50-GiB live
free-disk floor, 390-GiB initial MemAvailable gate, 86-GiB initial free-disk
gate, zero configured/used swap, and 30-second telemetry.  Each sample sums
RSS over the namespace-validated recorded worker PGID.  Crossing a live
floor or seeing swap triggers TERM and bounded KILL through the validated
group helper.  Every transcript, rc, job hash, telemetry row, and terminal
marker is retained; nothing in an older namespace is removed.

## Process topology

The launcher is a new `setsid` session.  The runner starts each worker with
its own `setsid`, so worker PID = PGID = SID.  `job_worker.sh` invokes
`/usr/bin/time -v -> timeout --foreground -> prlimit -> Singular`; all of
those processes remain in that one recorded worker PGID/SID, and every
command line carries the immutable run-namespace job path.  The frozen
preflight regression demonstrated both actual-descendant RSS inclusion and
complete validated TERM cleanup.

## Mandatory immediate recheck and exact launch command

Immediately before executing this command, the coordinator must first
confirm that no authoritative terminal result has made the reconnaissance
stale.  The command then fails closed unless the launch root is absent, the
archive and charged source hashes match, the source tree remains read-only,
and a fresh full preflight repeats the host/Singular identity, source and
evidence replay, no-heavy-process census, memory/disk/swap gates, and live
dummy-descendant regression.  `run_aws.sh` repeats all those gates again in
its new inner namespace before Singular.

```bash
ssh -i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes \
  -o ConnectTimeout=10 ubuntu@100.26.198.153 '
set -euo pipefail
source_root=/home/ubuntu/jobs/ggv_8_28_tail3_source_r1_20260828T050159Z
case_dir=$source_root/cases/ggv_8_28_upper_endpoint_tail3_desk_20260828
launch_root=/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r2_20260828T050159Z
archive=$source_root/GGV_8_28_TAIL3_SOURCE_R1_20260828T050159Z.tar.gz
expected_archive=be3a9915cea967e01b634b637f39d482204316f041dd6c57f6e64592a8cf6b87
[[ ! -e "$launch_root" ]]
[[ "$(sha256sum "$archive" | awk "{print \$1}")" == "$expected_archive" ]]
[[ "$(sha256sum "$case_dir/SOURCE.sha256" | awk "{print \$1}")" == \
  07626ff48f5acbf78b14bc3b6e3832f311b962358d7c82b8684dcfdb44a3ea08 ]]
[[ "$(sha256sum "$case_dir/EVIDENCE.sha256" | awk "{print \$1}")" == \
  10667433866a1b1abe361ba8dd7efc56aa1325afcfb97a6c8c3fda2f179f0387 ]]
[[ "$(sha256sum "$case_dir/TARGETS/tail3_v_nonzero_d22_target.json" | awk "{print \$1}")" == \
  8443dcb605c15e1fafd281d669c1ea23ec5e875589914af5d6c4540e83fa9363 ]]
if find "$source_root/cases" -type f -perm -u=w -print | grep .; then
  echo "STOP: immutable source tree became writable" >&2
  exit 41
fi
install -d -m 700 "$launch_root"
bash "$case_dir/TARGETS/preflight_aws.sh" \
  390 86 mod core 0,1,2,3,4,5 \
  2>&1 | tee "$launch_root/PREFLIGHT_IMMEDIATE_R2.txt"
sha256sum "$archive" "$case_dir/SOURCE.sha256" \
  "$case_dir/EVIDENCE.sha256" \
  "$case_dir/TARGETS/tail3_v_nonzero_d22_target.json" \
  "$case_dir/TARGETS/job_worker.sh" \
  "$case_dir/TARGETS/process_group_guard.sh" \
  "$case_dir/TARGETS/regress_process_group_control.sh" \
  "$case_dir/TARGETS/preflight_aws.sh" \
  "$case_dir/TARGETS/run_aws.sh" \
  "$case_dir/TARGETS/stop_aws.sh" \
  | tee "$launch_root/START_HASHES.sha256"
nohup setsid env TAIL3_RUN_ROOT="$launch_root/runs" \
  bash "$case_dir/TARGETS/run_aws.sh" \
    mod core cutoff3_core_mod_r6d_r2 all \
  >"$launch_root/launcher.stdout" \
  2>"$launch_root/launcher.stderr" </dev/null &
launcher_pid=$!
printf "%s\n" "$launcher_pid" | tee "$launch_root/launcher.pid"
sleep 1
read -r observed_pid observed_sid observed_pgid observed_args \
  < <(ps -o pid=,sid=,pgid=,args= -p "$launcher_pid")
launcher_start=$(awk "{print \$22}" "/proc/$launcher_pid/stat")
[[ "$observed_pid" == "$launcher_pid" \
   && "$observed_sid" == "$launcher_pid" \
   && "$observed_pgid" == "$launcher_pid" \
   && "$launcher_start" =~ ^[0-9]+$ \
   && "$observed_args" == *"$case_dir/TARGETS/run_aws.sh"* ]]
printf "%s %s %s %s\n" "$observed_pid" "$launcher_start" \
  "$observed_sid" "$observed_pgid" \
  | tee "$launch_root/launcher.identity"
printf "%s\n" "$observed_args" | tee "$launch_root/launcher.args"
echo "LAUNCH_ROOT=$launch_root"
echo "LAUNCHER_PID=$launcher_pid"
'
```

After clearance and launch, wait for the runner's second preflight to finish,
then identify the sole child of `runs/`, verify six recorded PID/PGID pairs,
inspect every member's SID and namespace path, and capture the first
`TELEMETRY.tsv` row.  Clearance is invalid if any charged hash, host/resource
gate, terminal-result check, or absence check changes.

## Exact stop command

This command first resolves exactly one R2 namespace.  For every recorded
worker it checks PID = PGID, job containment, and every current PGID member's
SID = PGID plus immutable namespace path.  It similarly checks the runner's
recorded start time, SID/PGID, and source path before invoking the frozen
stop helper.  Any mismatch refuses the stop for manual fail-closed audit.

```bash
ssh -i /Users/dc/.ssh/claude-cli.pem -o BatchMode=yes \
  -o ConnectTimeout=10 ubuntu@100.26.198.153 '
set -euo pipefail
source_root=/home/ubuntu/jobs/ggv_8_28_tail3_source_r1_20260828T050159Z
case_dir=$source_root/cases/ggv_8_28_upper_endpoint_tail3_desk_20260828
launch_root=/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r2_20260828T050159Z
mapfile -t run_dirs < <(find "$launch_root/runs" -mindepth 1 -maxdepth 1 \
  -type d -name "tail3_*" -print 2>/dev/null || true)
[[ "${#run_dirs[@]}" -le 1 ]]
read -r launcher_pid launcher_start launcher_sid launcher_pgid \
  < "$launch_root/launcher.identity"
validate_launcher() {
  [[ "$launcher_pid" =~ ^[0-9]+$ && "$launcher_start" =~ ^[0-9]+$ \
     && "$launcher_sid" == "$launcher_pid" \
     && "$launcher_pgid" == "$launcher_pid" \
     && -r "/proc/$launcher_pid/stat" ]] || return 1
  observed_start=$(awk "{print \$22}" "/proc/$launcher_pid/stat")
  read -r _ observed_sid observed_pgid observed_args \
    < <(ps -o pid=,sid=,pgid=,args= -p "$launcher_pid")
  [[ "$observed_start" == "$launcher_start" \
     && "$observed_sid" == "$launcher_sid" \
     && "$observed_pgid" == "$launcher_pgid" \
     && "$observed_args" == *"$case_dir/TARGETS/run_aws.sh"* ]]
}
if [[ "${#run_dirs[@]}" == 0 \
      || ! -f "${run_dirs[0]}/runner.identity" ]]; then
  validate_launcher
  kill -TERM "$launcher_pid"
  echo "EARLY_PREFLIGHT_TERM_VALIDATED=$launcher_pid"
  exit 0
fi
run_dir=${run_dirs[0]}
while read -r pid pgid label job; do
  [[ "$pid" =~ ^[0-9]+$ && "$pid" == "$pgid" \
     && "$job" == "$run_dir/"* ]]
  found=0
  while read -r member member_pgid member_sid member_args; do
    [[ "$member_pgid" == "$pgid" ]] || continue
    found=1
    [[ "$member_sid" == "$pgid" && "$member_args" == *"$run_dir/"* ]]
  done < <(ps -eo pid=,pgid=,sid=,args=)
  [[ "$found" == 1 ]]
done < "$run_dir/children.pgids"
read -r runner_pid runner_start < "$run_dir/runner.identity"
read -r observed_start < <(awk "{print \$22}" "/proc/$runner_pid/stat")
read -r _ runner_sid runner_pgid runner_args \
  < <(ps -o pid=,sid=,pgid=,args= -p "$runner_pid")
[[ "$observed_start" == "$runner_start" \
   && "$runner_sid" == "$runner_pid" \
   && "$runner_pgid" == "$runner_pid" \
   && "$runner_args" == *"$case_dir/TARGETS/run_aws.sh"* ]]
[[ "$runner_pid" == "$launcher_pid" && "$runner_start" == "$launcher_start" ]]
bash "$case_dir/TARGETS/stop_aws.sh" "$run_dir"
'
```

The helper TERM-signals only namespace-validated recorded worker groups,
waits up to 60 seconds, KILL-signals only still-live validated groups, then
validates and TERM-signals the exact runner identity.  A post-stop census
and immutable custody harvest are mandatory before classification.
