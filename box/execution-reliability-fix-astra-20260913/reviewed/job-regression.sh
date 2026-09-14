#!/usr/bin/env bash
# Run ONLY on an explicitly registered disposable AWS worker. No AWS API calls.
# Usage: sudo bash job-regression.sh INSTANCE UNIQUE_PREFIX JOB_SH PROBE_SH
set -Eeuo pipefail
export PATH=/usr/sbin:/usr/bin:/sbin:/bin
trap 'rc=$?; printf "REGRESSION_FAIL line=%s rc=%s command=%q\n" "$LINENO" "$rc" "$BASH_COMMAND" >&2; exit "$rc"' ERR
instance=${1:?}; prefix=${2:?}; job=${3:?}; probe=${4:?}
[[ $EUID == 0 && $instance =~ ^i-[0-9a-f]{17}$ && $instance != i-0252f535410c26ebc ]]
[[ $(< /sys/class/dmi/id/sys_vendor) == 'Amazon EC2' ]]
[[ $(< /sys/class/dmi/id/board_asset_tag) == "$instance" ]]
[[ $prefix =~ ^[a-z0-9][a-z0-9-]{0,29}$ ]]
base=/opt/jc2-job-regression-$prefix
[[ ! -e $base ]]
mkdir -m 0755 "$base"
exec > >(tee "$base/regression.stdout") 2> >(tee "$base/regression.stderr" >&2)
printf 'REGRESSION_START %s\n' "$(date -u +%FT%T.%NZ)"
bash -n "$job"
bash -n "$probe"
sha256sum "$job" "$probe" > "$base/sources.sha256"
getent group ubuntu
hash() { sha256sum "$1" | cut -d ' ' -f 1; }
bundle() {
  local suffix=$1 mode=$2 wall=${3:-30}
  tag=$prefix-$suffix
  stage=$base/$suffix
  mkdir "$stage"
  install -m 0444 "$probe" "$stage/probe.sh"
  jq -n --arg tag "$tag" --arg instance "$instance" --arg pin "$(hash "$probe")" \
    --arg mode "$mode" --argjson wall "$wall" '{
    schema:"JC2-JOB/v1",instance:$instance,tag:$tag,wall_seconds:$wall,
    memory_mib:256,cpu_percent:80,tasks_max:32,file_mib:8,
    files:{"probe.sh":$pin},phases:[
      {name:"first",argv:["/usr/bin/bash","@payload/probe.sh",$mode,"literal ; $not_expanded * with spaces"],expected_exit:0},
      {name:"second",argv:["/usr/bin/bash","@payload/probe.sh","second"],expected_exit:0}]
    }' > "$stage/job.json"
  out=/var/lib/jc2-jobs/$tag
  unit=jc2-job-$tag.service
}
launch() { bash "$job" start "$instance" "$tag" "$stage" "$(hash "$stage/job.json")"; }
terminal() {
  local i active
  for ((i=0;i<45;i++)); do
    active=$(systemctl show "$unit" -p ActiveState --value)
    if [[ ( $active == inactive || $active == failed ) && ! -e /sys/fs/cgroup/system.slice/$unit ]]; then return; fi
    sleep 1
  done
  printf 'TERMINAL_POLL_EXPIRED %s\n' "$unit" >&2
  return 1
}
collect_twice() {
  local before
  bash "$job" collect "$instance" "$tag"
  before=$(hash "$out/evidence.tar")
  bash "$job" collect "$instance" "$tag"
  [[ $(hash "$out/evidence.tar") == "$before" ]]
  runuser -u ubuntu -- test -r "$out/evidence.tar"
  runuser -u ubuntu -- bash "$job" status "$instance" "$tag"
}
refusal_count=0
refusal() {
  local rc
  refusal_count=$((refusal_count + 1))
  if "$@" > "$base/refusal-$refusal_count.stdout" 2> "$base/refusal-$refusal_count.stderr"; then
    printf 'EXPECTED_REFUSAL_WAS_ACCEPTED\n' >&2; return 1
  else rc=$?; fi
  [[ $rc -ne 0 ]]
  cat "$base/refusal-$refusal_count.stderr"
}

bundle success first
launch; terminal
[[ $(< "$out/output/batch-exit") == 0 ]]
[[ $(< "$out/output/phases/first/exit") == 0 ]]
[[ $(< "$out/output/phases/second/exit") == 0 ]]
[[ $(< "$out/output/literal-argument.txt") == 'literal ; $not_expanded * with spaces' ]]
jq -e '.service_result == "success" and .exit_code == "exited" and .exit_status == "0"' "$out/terminal.json"
before=$(hash "$out/output/phases/first/start.utc")
refusal bash "$job" start "$instance" "$tag" "$stage" "$(hash "$stage/job.json")"
[[ $(hash "$out/output/phases/first/start.utc") == "$before" ]]
collect_twice
printf 'PASS success argv-identity duplicate-refusal repeat-collection\n'

bundle failure fail
launch; terminal
[[ $(< "$out/output/phases/first/exit") == 17 ]]
[[ ! -e $out/output/phases/second && ! -e $out/output/batch-exit ]]
[[ $(< "$out/output/partial.txt") == PARTIAL_BEFORE_EXIT17 ]]
grep -q VISIBLE_EXPECTED_FAILURE_17 "$out/controller.stderr"
runuser -u ubuntu -- test -r "$out/output/phases/first/stderr"
jq -e '.service_result == "exit-code" and .exit_status == "1"' "$out/terminal.json"
# Force a real failed collection with a small inherited per-file limit.
# All originals survive. The next normal collection must rebuild the partial.
if (ulimit -f 8; bash "$job" collect "$instance" "$tag") > "$base/capped-collect.stdout" 2> "$base/capped-collect.stderr"; then
  printf 'EXPECTED_COLLECTION_FAILURE_WAS_ACCEPTED\n' >&2; exit 1
fi
[[ ! -e $out/evidence.tar ]]
collect_twice
printf 'PASS exit17 partial-evidence visible-stderr failed-collection-recovery\n'

bundle missing first
jq '.phases[0].argv=["/usr/bin/jc2-deliberately-missing-executable"]' "$stage/job.json" > "$stage/job.next"
mv "$stage/job.next" "$stage/job.json"
launch; terminal
[[ $(< "$out/output/phases/first/exit") == 127 ]]
[[ ! -e $out/output/phases/second ]]
collect_twice
printf 'PASS first-exec-failure-no-empty-success\n'

bundle timeout timeout 8
launch; terminal
[[ -f $out/output/stubborn.pid && ! -e $out/output/batch-exit ]]
pid=$(< "$out/output/stubborn.pid")
[[ $pid =~ ^[0-9]+$ && ! -e /proc/$pid ]]
grep -q "/system.slice/$unit" "$out/output/stubborn.identity"
jq -e '.service_result == "timeout"' "$out/terminal.json"
collect_twice
printf 'PASS timeout new-session-descendant-cleanup\n'

bundle killed kill-controller
launch; terminal
[[ $(< "$out/output/partial.txt") == KILL_PARTIAL ]]
[[ ! -e $out/output/phases/first/exit && ! -e $out/output/batch-exit ]]
jq -e '.service_result == "signal" and .exit_code == "killed" and .exit_status == "KILL"' "$out/terminal.json"
collect_twice
printf 'PASS controller-SIGKILL partial-evidence missing-phase-exit\n'

bundle badpin first
printf 'changed payload\n' >> "$stage/probe.sh"
refusal bash "$job" start "$instance" "$tag" "$stage" "$(hash "$stage/job.json")"
[[ ! -e $out/terminal.json && ! -e $out/output/phases ]]
collect_twice
printf 'PASS pre-service-admission-failure-is-UNKNOWN-and-collectible\n'

bundle badpath first
jq '.phases[0].argv[1]="@payload/../../etc/passwd"' "$stage/job.json" > "$stage/job.next"
mv "$stage/job.next" "$stage/job.json"
refusal bash "$job" start "$instance" "$tag" "$stage" "$(hash "$stage/job.json")"
[[ ! -e $out ]]
refusal bash "$job" start i-00000000000000000 "$tag" "$stage" "$(hash "$stage/job.json")"
refusal bash "$job" start i-0252f535410c26ebc "$tag" "$stage" "$(hash "$stage/job.json")"
printf 'PASS path-escape wrong-instance HQ-refusal\n'

bundle symlink first
mv "$stage/probe.sh" "$stage/original.sh"
ln -s original.sh "$stage/probe.sh"
refusal bash "$job" start "$instance" "$tag" "$stage" "$(hash "$stage/job.json")"
[[ ! -e $out/terminal.json ]]
collect_twice
printf 'PASS source-symlink-refusal\n'

printf 'REGRESSION_PASS %s\n' "$(date -u +%FT%T.%NZ)"
sync -f "$base"
# No deletion, broad process census, worker termination, or volume operation.
