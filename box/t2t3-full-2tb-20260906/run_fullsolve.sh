#!/usr/bin/env bash
# Capped detached-run payload for the full (99,66), delta=2 direct ideal.
# This is the reviewed t2t3 long-solve runner with only the requested larger
# caps and msolve thread count changed.
set -Eeuo pipefail

readonly WALL_SECONDS=72000
readonly TERM_GRACE_SECONDS=60
readonly MSOLVE_AS_KIB=1677721600        # 1600 GiB = 1717986918400 bytes.
readonly SINGULAR_RSS_BYTES=1288490188800 # 1200 GiB sampled aggregate PGID RSS.

die() { printf 'run_fullsolve: %s\n' "$*" >&2; exit 64; }

if [[ ${1:-} == __msolve_exec ]]; then
  [[ $# -eq 5 ]] || die '__msolve_exec expects SOLVER INPUT BASIS LIMIT_RECORD'
  solver=$2 input=$3 basis=$4 limit_record=$5
  ulimit -v "$MSOLVE_AS_KIB"
  actual_limit=$(ulimit -v)
  [[ $actual_limit == "$MSOLVE_AS_KIB" ]] || die "RLIMIT_AS verification failed"
  {
    printf 'LIMIT_KIND=RLIMIT_AS LIMIT_KIB=%s\n' "$actual_limit"
    if [[ -r /proc/$$/limits ]]; then
      while IFS= read -r limit_line; do
        case $limit_line in 'Max address space'*) printf 'PROC_LIMIT=%s\n' "$limit_line" ;; esac
      done < "/proc/$$/limits"
    fi
  } > "$limit_record"
  exec "$solver" -g 2 -t 120 -v 2 --random-seed 0 -f "$input" -o "$basis"
fi

[[ $# -eq 3 ]] || die 'usage: run_fullsolve.sh {msolve|singular} FRESH_RUN_DIR INPUT'
mode=$1 run_arg=$2 input_arg=$3
[[ $mode == msolve || $mode == singular ]] || die 'mode must be msolve or singular'
job_tag=${T2T3_JOB_TAG:-}
[[ $job_tag =~ ^t2t3-full-(p1073741827|p1073741783|q-slimgb)$ ]] || \
  die 'T2T3_JOB_TAG is missing or unregistered'
aws_vendor=$(< /sys/devices/virtual/dmi/id/board_vendor)
[[ $aws_vendor == 'Amazon EC2' ]] || die 'heavy runner refuses to run off AWS EC2'

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
wrapper=$(realpath -e -- "${BASH_SOURCE[0]}")
caprun=${CAPRUN:-$script_dir/run_capped.py}
[[ -f $caprun ]] || die "CAPRUN is not a regular file: $caprun"
caprun=$(realpath -e -- "$caprun")
input=$(realpath -e -- "$input_arg")
[[ -f $input ]] || die "input is not a regular file: $input"
run_dir=$(realpath -m -- "$run_arg")
[[ ! -e $run_dir ]] || die "run directory must be fresh: $run_dir"
mkdir -p -- "$(dirname -- "$run_dir")"
mkdir -- "$run_dir"
mkdir -- "$run_dir/tmp"
run_dir=$(realpath -e -- "$run_dir")
export TMPDIR=$run_dir/tmp

stdout_file=$run_dir/solver.stdout
stderr_file=$run_dir/solver.stderr
telemetry_file=$run_dir/caprun.json
rc_file=$run_dir/runner.rc
custody_file=$run_dir/custody.txt
post_file=$run_dir/postflight.sha256
time_file=$run_dir/time.txt
limit_file=$run_dir/limit.txt

cap_args=(
  --wall-seconds "$WALL_SECONDS" --term-grace-seconds "$TERM_GRACE_SECONDS"
  --stdout-file "$stdout_file" --stderr-file "$stderr_file"
  --telemetry-file "$telemetry_file" --cwd "$run_dir"
)

if [[ $mode == msolve ]]; then
  solver=$(realpath -e -- "${MSOLVE_BIN:-/usr/local/bin/msolve}")
  [[ -x $solver ]] || die "msolve is not executable: $solver"
  command=(/usr/bin/time -v -o "$time_file" "$wrapper" __msolve_exec
           "$solver" "$input" "$run_dir/basis.ms" "$limit_file")
  limit_kind=RLIMIT_AS limit_value=$MSOLVE_AS_KIB limit_units=KiB
else
  solver=$(realpath -e -- "${SINGULAR_BIN:-/usr/bin/Singular}")
  [[ -x $solver ]] || die "Singular is not executable: $solver"
  cap_args+=(--rss-bytes "$SINGULAR_RSS_BYTES" --rss-sample-seconds 0.05)
  command=(/usr/bin/time -v -o "$time_file" "$solver" -q --no-rc --no-warn
           --no-shell --threads=1 --flint-threads=1 "$input")
  limit_kind=sampled_aggregate_PGID_RSS limit_value=$SINGULAR_RSS_BYTES limit_units=bytes
fi

caprun_pid='' wait_interrupted=0 pending_signal=''
forward_to_caprun() {
  pending_signal=$1; wait_interrupted=1
  [[ -z $caprun_pid ]] || kill -s "$1" "$caprun_pid" 2>/dev/null || true
}
trap 'forward_to_caprun HUP' HUP
trap 'forward_to_caprun INT' INT
trap 'forward_to_caprun TERM' TERM

{
  printf 'schema=T2T3_FULL_2TB_WORKER_RUN/v1\n'
  printf 'utc_preflight=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'job_tag=%s\nmode=%s\nhostname=%s\naws_vendor=%s\nnproc=%s\n' \
    "$job_tag" "$mode" "$(hostname)" "$aws_vendor" "$(nproc)"
  printf 'run_dir=%s\nTMPDIR=%s\ninput=%s\nsolver=%s\nwrapper=%s\ncaprun=%s\n' \
    "$run_dir" "$TMPDIR" "$input" "$solver" "$wrapper" "$caprun"
  printf 'wall_seconds=%s\nterm_grace_seconds=%s\n' "$WALL_SECONDS" "$TERM_GRACE_SECONDS"
  printf 'limit_kind=%s\nlimit_value=%s\nlimit_units=%s\n' "$limit_kind" "$limit_value" "$limit_units"
  printf 'input_sha256=%s\n' "$(sha256sum -- "$input" | cut -d' ' -f1)"
  printf 'solver_sha256=%s\n' "$(sha256sum -- "$solver" | cut -d' ' -f1)"
  printf 'wrapper_sha256=%s\n' "$(sha256sum -- "$wrapper" | cut -d' ' -f1)"
  printf 'caprun_sha256=%s\n' "$(sha256sum -- "$caprun" | cut -d' ' -f1)"
  printf 'argv_shellquoted='; printf ' %q' "${command[@]}"; printf '\n'
} > "$custody_file"

set +e
/usr/bin/python3 "$caprun" "${cap_args[@]}" -- "${command[@]}" &
caprun_pid=$!
[[ -z $pending_signal ]] || kill -s "$pending_signal" "$caprun_pid" 2>/dev/null || true
while true; do
  wait_interrupted=0
  wait "$caprun_pid"; wait_rc=$?
  (( wait_interrupted )) || { runner_rc=$wait_rc; break; }
done
set -e
trap - HUP INT TERM

{
  for artifact in "$input" "$custody_file" "$stdout_file" "$stderr_file" \
      "$telemetry_file" "$time_file" "$limit_file" "$run_dir/basis.ms"; do
    [[ ! -f $artifact ]] || sha256sum -- "$artifact"
  done
} > "$post_file.tmp"
mv -- "$post_file.tmp" "$post_file"
printf '%s\n' "$runner_rc" > "$rc_file.tmp"
mv -- "$rc_file.tmp" "$rc_file"
exit "$runner_rc"
