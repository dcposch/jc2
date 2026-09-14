#!/usr/bin/env bash
# JC2-JOB/v1: opt-in, AWS-worker-only, durable one-service batch runner.
# INTERNAL / UNREVIEWED. See JOB.md. Never allocates or terminates EC2.
set -Eeuo pipefail
export PATH=/usr/sbin:/usr/bin:/sbin:/bin
umask 027
ROOT=/var/lib/jc2-jobs
HQ=i-0252f535410c26ebc

die() { printf 'JC2-JOB ERROR: %s\n' "$*" >&2; exit 70; }
trap 'rc=$?; printf "JC2-JOB ERROR rc=%s line=%s command=%q\n" "$rc" "$LINENO" "$BASH_COMMAND" >&2; exit "$rc"' ERR
usage() {
  printf '%s\n' \
    'job.sh start INSTANCE TAG BUNDLE MANIFEST_SHA256 RUNNER_SHA256' \
    'job.sh status|stop|collect INSTANCE TAG' \
    'Run on the exact AWS worker with sudo; BUNDLE/job.json is frozen input.'
}
guard() {
  [[ $(uname -s) == Linux ]] || die 'Linux required'
  [[ $(< /sys/class/dmi/id/sys_vendor) == 'Amazon EC2' ]] || die 'AWS EC2 required'
  [[ $instance =~ ^i-[0-9a-f]{17}$ && $instance != "$HQ" ]] || die 'invalid instance or forbidden HQ'
  [[ $(< /sys/class/dmi/id/board_asset_tag) == "$instance" ]] || die 'instance mismatch'
  [[ $tag =~ ^[a-z0-9][a-z0-9-]{0,59}$ ]] || die 'invalid tag'
  [[ -f /sys/fs/cgroup/cgroup.controllers ]] || die 'cgroup v2 required'
  dir=$ROOT/$tag
  unit=jc2-job-$tag.service
  cg=/sys/fs/cgroup/system.slice/$unit
}
require_root() { [[ $EUID == 0 ]] || die 'sudo/root required'; }
hash() { sha256sum -- "$1" | cut -d ' ' -f 1; }
utc() { date -u +%Y-%m-%dT%H:%M:%S.%NZ; }
immutable_source() {
  local source=$1 parent mode
  [[ $source == /* && -f $source && ! -L $source ]] || die "source must be a regular nonsymlink file: $source"
  [[ $(realpath -e -- "$source") == "$source" ]] || die "noncanonical source ancestry: $source"
  [[ $(stat -c '%u:%a' "$source") == 0:444 ]] || die "source must be root-owned0444: $source"
  parent=$(dirname -- "$source")
  while :; do
    [[ -d $parent && ! -L $parent && $(stat -c %u "$parent") == 0 ]] || die "unsafe source parent: $parent"
    mode=$(stat -c %a "$parent")
    (( (8#$mode & 0022) == 0 )) || die "writable source parent: $parent"
    [[ $parent != / ]] || break
    parent=$(dirname -- "$parent")
  done
}
atomic_text() {
  local target=$1; shift
  printf '%s\n' "$*" > "$target.partial"
  sync -f "$target.partial"
  mv -T -- "$target.partial" "$target"
  sync -f "$(dirname -- "$target")"
}
check_existing() {
  [[ -d $dir && ! -L $dir ]] || die 'unknown job'
  [[ $(< "$dir/instance") == "$instance" ]] || die 'saved instance mismatch'
  [[ $(stat -c '%u:%a:%G' "$dir") == 0:2755:ubuntu ]] || die 'job directory ownership/mode drift'
}
manager_state() {
  systemctl show "$unit" --no-pager \
    -p LoadState -p ActiveState -p SubState -p MainPID -p ControlGroup \
    -p InvocationID -p Result -p ExecMainCode -p ExecMainStatus \
    -p RuntimeMaxUSec -p TimeoutStopUSec -p KillMode -p MemoryMax \
    -p MemorySwapMax -p CPUQuotaPerSecUSec -p TasksMax -p LimitFSIZE -p User -p Group
}
is_terminal() {
  local active
  active=$(systemctl show "$unit" -p ActiveState --value)
  [[ $active == inactive || $active == failed ]] && [[ ! -e $cg ]]
}
start() {
  require_root
  [[ $# == 3 ]] || die 'start requires bundle, manifest SHA256 and runner SHA256'
  local bundle=$1 expected=$2 runner_expected=$3 manifest key value src dest wall mem cpu tasks fsize runner
  [[ $bundle == /* && -d $bundle && ! -L $bundle ]] || die 'absolute regular bundle directory required'
  [[ $(realpath -e -- "$bundle") == "$bundle" ]] || die 'canonical bundle path required'
  [[ $expected =~ ^[0-9a-f]{64}$ ]] || die 'invalid manifest SHA256'
  [[ $runner_expected =~ ^[0-9a-f]{64}$ ]] || die 'invalid runner SHA256'
  runner=$(realpath -e -- "$0")
  [[ $0 == "$runner" ]] || die 'canonical absolute runner path required'
  immutable_source "$runner"
  [[ $(hash "$runner") == "$runner_expected" ]] || die 'runner SHA256 mismatch'
  manifest=$bundle/job.json
  immutable_source "$manifest"
  [[ $(stat -c %s "$manifest") -le 65536 ]] || die 'manifest exceeds 64 KiB'
  [[ $(hash "$manifest") == "$expected" ]] || die 'manifest SHA256 mismatch'
  # JSON is data; never source/eval it. Every file and argv string is bounded.
  jq -e --arg tag "$tag" --arg instance "$instance" '
    def integer($lo;$hi): type == "number" and floor == . and . >= $lo and . <= $hi;
    def path: type == "string" and test("^[A-Za-z0-9_-]+([./][A-Za-z0-9_-]+)*$") and (split("/") | all(. != ".."));
    . as $job |
    keys == ["cpu_percent","file_mib","files","instance","memory_mib","phases","schema","tag","tasks_max","wall_seconds"]
    and .schema == "JC2-JOB/v1" and .instance == $instance and .tag == $tag
    and (.wall_seconds | integer(1;43200)) and (.memory_mib | integer(64;1048576))
    and (.cpu_percent | integer(1;12800)) and (.tasks_max | integer(4;4096))
    and (.file_mib | integer(1;1024))
    and (.files | type == "object" and length >= 1 and length <= 128)
    and (.files | to_entries | all((.key | path) and (.value | type == "string" and test("^[0-9a-f]{64}$"))))
    and (.phases | type == "array" and length >= 1 and length <= 32)
    and ((.phases | map(.name) | unique | length) == (.phases | length))
    and (.phases | all(keys == ["argv","expected_exit","name"]
      and (.name | type == "string" and test("^[a-z0-9][a-z0-9-]{0,39}$"))
      and (.expected_exit | integer(0;255))
      and (.argv | type == "array" and length >= 1 and length <= 64
        and all(type == "string" and length <= 4096 and (contains("\u0000") | not)))
      and (.argv[0] | test("^/(usr/)?bin/[A-Za-z0-9_.+-]+$"))
      and (.argv | all(if startswith("@payload/") then ($job.files[.[9:]] | type == "string") else true end))))
  ' "$manifest" >/dev/null || die 'manifest schema rejected'
  [[ ! -e $dir && ! -L $dir ]] || die 'tag already exists; status/collect it, never retry in place'
  [[ $(systemctl show "$unit" -p LoadState --value) == not-found ]] || die 'unit already exists'
  [[ ! -e $cg ]] || die 'cgroup already exists'
  if [[ -e $ROOT ]]; then
    [[ -d $ROOT && ! -L $ROOT && $(stat -c '%u:%a' "$ROOT") == 0:755 ]] || die 'unsafe jobs root'
  else
    install -d -m 0755 -o root -g root "$ROOT"
  fi
  mkdir -m 0755 -- "$dir"  # atomic no-overwrite admission, retained even on setup failure
  chgrp ubuntu "$dir"
  chmod 2755 "$dir"
  exec 8>> "$dir/lifecycle.lock"
  flock -n 8 || die 'admission or collection still live'
  printf '%s\n' "$instance" > "$dir/instance"
  chmod 0444 "$dir/instance"
  printf 'EVIDENCE %s; admission diagnostics are in admission.stdout/admission.stderr\n' "$dir"
  # Direct files: no untracked tee writer can outlive this locked admission.
  # FD8 is retained through the last write and closes when this process exits.
  exec >> "$dir/admission.stdout" 2>> "$dir/admission.stderr"
  printf 'ADMISSION %s instance=%s tag=%s host=%s\n' "$(utc)" "$instance" "$tag" "$(hostname)"
  install -d -m 0755 "$dir/payload"
  install -d -m 2750 -o nobody -g ubuntu "$dir/output"
  install -m 0444 "$manifest" "$dir/job.json"
  [[ $(hash "$dir/job.json") == "$expected" ]] || die 'manifest changed during copy'
  # Copy only the registered file list: no recursive baked-tree traversal.
  while IFS=$'\t' read -r key value; do
    src=$bundle/$key; dest=$dir/payload/$key
    immutable_source "$src"
    [[ $(realpath -e -- "$src") == "$bundle/"* ]] || die "unsafe bundle file: $key"
    [[ $(stat -c %s "$src") -le 16777216 ]] || die "bundle file exceeds 16 MiB: $key"
    install -d -m 0755 "$(dirname -- "$dest")"
    install -m 0444 "$src" "$dest"
    [[ $(hash "$dest") == "$value" ]] || die "payload SHA256 mismatch: $key"
  done < <(jq -r '.files | to_entries[] | [.key,.value] | @tsv' "$dir/job.json")
  install -m 0444 "$runner" "$dir/runner.sh"
  [[ $(hash "$dir/runner.sh") == "$runner_expected" ]] || die 'runner changed during copy'
  sha256sum "$dir/runner.sh" "$dir/job.json" > "$dir/admission.sha256"
  wall=$(jq -r .wall_seconds "$dir/job.json")
  mem=$(jq -r .memory_mib "$dir/job.json")
  cpu=$(jq -r .cpu_percent "$dir/job.json")
  tasks=$(jq -r .tasks_max "$dir/job.json")
  fsize=$(jq -r .file_mib "$dir/job.json")
  sync -f "$dir"
  install -m 0640 -o root -g ubuntu /dev/null "$dir/controller.stdout"
  install -m 0640 -o root -g ubuntu /dev/null "$dir/controller.stderr"
  # The manager owns lifetime/descendants; SSH and the coordinator own neither.
  # No --collect: keep failed unit state available for status and recovery.
  if systemd-run --unit "$unit" --service-type=exec \
      --property="Description=JC2 bounded job $tag" \
      --property=User=nobody --property=Group=nogroup \
      --property=UMask=0027 --property=Restart=no \
      --property="RuntimeMaxSec=$wall" --property=TimeoutStopSec=5s \
      --property=KillMode=control-group --property=SendSIGKILL=yes \
      --property="MemoryMax=${mem}M" --property=MemorySwapMax=0 \
      --property="CPUQuota=${cpu}%" --property=CPUQuotaPeriodSec=100ms \
      --property="TasksMax=$tasks" --property="LimitFSIZE=${fsize}M" \
      --property=NoNewPrivileges=yes --property=CapabilityBoundingSet= \
      --property=AmbientCapabilities= --property=RestrictNamespaces=yes \
      --property=ProtectControlGroups=yes --property=ProtectSystem=strict \
      --property=ProtectHome=yes --property=PrivateTmp=yes \
      --property=RestrictSUIDSGID=yes --property=PrivateNetwork=yes \
      --property="ReadWritePaths=$dir" \
      --property="StandardOutput=append:$dir/controller.stdout" \
      --property="StandardError=append:$dir/controller.stderr" \
      --property="ExecStopPost=+/usr/bin/bash $dir/runner.sh _finish $instance $tag" \
      /usr/bin/bash "$dir/runner.sh" _run "$instance" "$tag"; then
    atomic_text "$dir/start-return" 0
  else
    local rc=$?
    atomic_text "$dir/start-return" "$rc"
    manager_state > "$dir/start-failure.manager"
    journalctl -u "$unit" --no-pager -o short-iso > "$dir/start-failure.journal" 2>&1 || true
    die "systemd start failed rc=$rc; evidence retained at $dir"
  fi
  manager_state
  printf 'EVIDENCE %s\n' "$dir"
  sync -f "$dir"
}
run_batch() {
  [[ $EUID == 65534 ]] || die 'payload service must already be nobody'
  check_existing
  local n name expected rc arg pid mem cpu tasks fsize
  local -a argv members
  cd "$dir/output"
  export JC2_JOB_PAYLOAD=$dir/payload JC2_JOB_OUTPUT=$dir/output
  export PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
  {
    printf 'UTC=%s\nHOST=%s\nPID=%s\n' "$(utc)" "$(hostname)" "$$"
    cat /proc/self/cgroup /proc/$$/stat /proc/$$/status /proc/$$/limits
    for n in cpu.max memory.max memory.swap.max pids.max; do
      printf '%s=' "$n"; cat "$cg/$n"
    done
  } > live-controls.txt
  sync -f live-controls.txt
  # Before any payload, this exact controller is live inside the enforced cgroup.
  [[ $(< "$cg/memory.swap.max") == 0 ]] || die 'swap limit mismatch'
  [[ $(awk '/^CapEff:/ {print $2}' /proc/$$/status) == 0000000000000000 ]] || die 'nonzero capabilities'
  [[ $(awk '/^NoNewPrivs:/ {print $2}' /proc/$$/status) == 1 ]] || die 'NoNewPrivileges missing'
  [[ $(awk '/^Uid:/ {print $2,$3,$4,$5}' /proc/$$/status) == '65534 65534 65534 65534' ]] || die 'UID vector mismatch'
  [[ $(awk '/^Gid:/ {print $2,$3,$4,$5}' /proc/$$/status) == '65534 65534 65534 65534' ]] || die 'GID vector mismatch'
  [[ $(awk -F: '$1 == 0 {print $3}' /proc/$$/cgroup) == "/system.slice/$unit" ]] || die 'unexpected cgroup'
  mem=$(jq -r .memory_mib "$dir/job.json")
  cpu=$(jq -r .cpu_percent "$dir/job.json")
  tasks=$(jq -r .tasks_max "$dir/job.json")
  fsize=$(jq -r .file_mib "$dir/job.json")
  [[ $(awk '$1=="Max" && $2=="file" && $3=="size" {n++;v=$4" "$5" "$6} END {if(n==1) print v; else exit 1}' /proc/$$/limits) == "$((fsize * 1048576)) $((fsize * 1048576)) bytes" ]] || die 'FSIZE soft/hard mismatch'
  [[ $(< "$cg/memory.max") == "$((mem * 1048576))" ]] || die 'kernel memory cap mismatch'
  [[ $(< "$cg/cpu.max") == "$((cpu * 1000)) 100000" ]] || die 'kernel CPU cap mismatch'
  [[ $(< "$cg/pids.max") == "$tasks" ]] || die 'kernel task cap mismatch'
  mkdir phases
  for ((n=0; n<$(jq '.phases | length' "$dir/job.json"); n++)); do
    name=$(jq -r ".phases[$n].name" "$dir/job.json")
    expected=$(jq -r ".phases[$n].expected_exit" "$dir/job.json")
    mkdir "phases/$name"
    jq ".phases[$n]" "$dir/job.json" > "phases/$name/command.json"
    argv=()
    while IFS= read -r -d '' arg; do
      [[ $arg != @payload/* ]] || arg=$dir/payload/${arg#@payload/}
      argv+=("$arg")
    done < <(jq -j ".phases[$n].argv[] | ., \"\\u0000\"" "$dir/job.json")
    atomic_text current-phase "$name"
    atomic_text "phases/$name/start.utc" "$(utc)"
    printf 'PHASE_START %s %s\n' "$(utc)" "$name"
    # The child inherits the one service cgroup even if it calls setsid/forks.
    if "${argv[@]}" > "phases/$name/stdout" 2> "phases/$name/stderr"; then rc=0; else rc=$?; fi
    atomic_text "phases/$name/exit" "$rc"
    atomic_text "phases/$name/end.utc" "$(utc)"
    printf 'PHASE_END %s %s actual=%s expected=%s\n' "$(utc)" "$name" "$rc" "$expected"
    sync -f "$dir"
    if [[ $rc != "$expected" ]]; then
      printf 'Unexpected phase exit; stderr follows (last 80 lines):\n' >&2
      tail -n 80 "phases/$name/stderr" >&2
      exit 1
    fi
    mapfile -t members < "$cg/cgroup.procs"
    for pid in "${members[@]}"; do
      [[ $pid == "$$" ]] || die "phase $name left a background cgroup member $pid; stopping whole job"
    done
  done
  atomic_text batch-exit 0
}
finish() {
  require_root
  check_existing
  # systemd supplies these even when SIGKILL/OOM prevented a shell EXIT trap.
  # This hook running is NOT itself proof that the cgroup is finally absent.
  printf 'FINISH %s result=%s code=%s status=%s\n' "$(utc)" \
    "${SERVICE_RESULT:-unknown}" "${EXIT_CODE:-unknown}" "${EXIT_STATUS:-unknown}"
  jq -n --arg utc "$(utc)" --arg result "${SERVICE_RESULT:-unknown}" \
    --arg code "${EXIT_CODE:-unknown}" --arg status "${EXIT_STATUS:-unknown}" \
    '{schema:"JC2-JOB/terminal-v1",utc:$utc,service_result:$result,exit_code:$code,exit_status:$status}' \
    > "$dir/terminal.json.partial"
  sync -f "$dir/terminal.json.partial"
  mv -T "$dir/terminal.json.partial" "$dir/terminal.json"
  sync -f "$dir"
}
status_job() {
  check_existing
  manager_state
  printf 'evidence=%s\n' "$dir"
  if [[ -e $cg ]]; then printf 'cleanup=NOT_CONFIRMED\n'; else printf 'cgroup=ABSENT\n'; fi
  [[ ! -f $dir/output/current-phase ]] || printf 'last_phase=%s\n' "$(< "$dir/output/current-phase")"
  if [[ -f $dir/terminal.json ]]; then cat "$dir/terminal.json"; else printf 'terminal_receipt=MISSING\n'; fi
  if [[ -f $dir/controller.stderr ]]; then tail -n 30 "$dir/controller.stderr"; fi
  # A missing unit with no receipt is UNKNOWN, never a successful run.
}
collect() {
  require_root; check_existing
  # No cleanup/deletion; even a failed admission or missing hook is collectible.
  # Same nonblocking lock as admission, acquired BEFORE the terminal test.
  exec 8>> "$dir/lifecycle.lock"
  flock -n 8 || die 'admission or collection still live'
  is_terminal || die 'writers/unit/cgroup not terminal; status or exact-tag stop first'
  if [[ ! -f $dir/evidence.tar ]]; then
    manager_state > "$dir/collected.manager"
    journalctl -u "$unit" --no-pager -o short-iso > "$dir/collected.journal" 2>&1 || true
    atomic_text "$dir/collected.utc" "$(utc)"
    tar --exclude='./evidence.tar' --exclude='./evidence.tar.partial' \
      --exclude='./evidence.sha256' --exclude='./evidence.sha256.partial' --exclude='./lifecycle.lock' \
      -C "$dir" -cf "$dir/evidence.tar.partial" .
    sync -f "$dir/evidence.tar.partial"
    mv -T "$dir/evidence.tar.partial" "$dir/evidence.tar"
  fi
  # A crash after the atomic archive rename but before hashing is recoverable.
  if [[ ! -f $dir/evidence.sha256 ]]; then
    (cd "$dir" && sha256sum evidence.tar) > "$dir/evidence.sha256.partial"
    sync -f "$dir/evidence.sha256.partial"
    mv -T "$dir/evidence.sha256.partial" "$dir/evidence.sha256"
    sync -f "$dir"
  fi
  (cd "$dir" && sha256sum --check evidence.sha256)
  cat "$dir/evidence.sha256"
  printf 'ARCHIVE %s/evidence.tar\n' "$dir"
}

command=${1:-help}
if [[ $command == help || $command == --help ]]; then usage; exit 0; fi
[[ $# -ge 3 ]] || { usage >&2; exit 64; }
instance=$2; tag=$3; shift 3
guard
case $command in
  start) start "$@" ;;
  _run) [[ $# == 0 ]] || die 'extra arguments'; run_batch ;;
  _finish) [[ $# == 0 ]] || die 'extra arguments'; finish ;;
  status) [[ $# == 0 ]] || die 'extra arguments'; status_job ;;
  collect) [[ $# == 0 ]] || die 'extra arguments'; collect ;;
  stop)
    [[ $# == 0 ]] || die 'extra arguments'; require_root; check_existing
    if is_terminal; then status_job; else systemctl stop "$unit"; status_job; fi ;;
  *) usage >&2; exit 64 ;;
esac
