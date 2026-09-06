#!/usr/bin/env bash
# One-shot worker launcher for the t2t3 direct-presentation long solves.
#
# Public interface:
#   run_longsolve.sh msolve  FRESH_RUN_DIR INPUT.ms
#   run_longsolve.sh singular FRESH_RUN_DIR INPUT.sing
#
# CAPRUN defaults to run_capped.py beside this file, then to the repository
# copy.  On a worker, stage this script, run_capped.py, and (optionally)
# lane_eta.py together.  MSOLVE_BIN and SINGULAR_BIN may name exact alternate
# binaries; their resolved paths and hashes are recorded before execution.

set -Eeuo pipefail

readonly WALL_SECONDS=72000
readonly TERM_GRACE_SECONDS=60
readonly MSOLVE_AS_KIB=419430400       # 400 GiB RLIMIT_AS (ulimit -v is KiB).
readonly SINGULAR_RSS_BYTES=214748364800 # 200 GiB sampled aggregate PGID RSS.

die() {
  printf 'run_longsolve: %s\n' "$*" >&2
  exit 64
}

# Private child mode.  CAPRUN starts /usr/bin/time as the registered process-
# group leader; time forks this helper in the same PGID, and exec preserves the
# group when the helper becomes msolve.  Thus the shell-imposed RLIMIT_AS and
# CAPRUN's exact-PGID lifecycle cover every solver process.
if [[ ${1:-} == __msolve_exec ]]; then
  [[ $# -eq 5 ]] || die '__msolve_exec expects SOLVER INPUT BASIS LIMIT_RECORD'
  solver=$2
  input=$3
  basis=$4
  limit_record=$5
  ulimit -v "$MSOLVE_AS_KIB"
  actual_limit=$(ulimit -v)
  [[ $actual_limit == "$MSOLVE_AS_KIB" ]] || \
    die "RLIMIT_AS verification failed: requested=$MSOLVE_AS_KIB actual=$actual_limit KiB"
  {
    printf 'LIMIT_KIND=RLIMIT_AS LIMIT_KIB=%s\n' "$actual_limit"
    if [[ -r /proc/$$/limits ]]; then
      while IFS= read -r limit_line; do
        case $limit_line in
          'Max address space'*) printf 'PROC_LIMIT=%s\n' "$limit_line" ;;
        esac
      done < "/proc/$$/limits"
    fi
  } > "$limit_record"
  exec "$solver" -g 2 -t 64 -v 2 --random-seed 0 \
    -f "$input" -o "$basis"
fi

usage() {
  cat >&2 <<'EOF'
usage: run_longsolve.sh {msolve|singular} FRESH_RUN_DIR INPUT

The run directory must not already exist.  Completion is signaled by the
atomic appearance of runner.rc; CAPRUN details are in caprun.json.
EOF
  exit 64
}

[[ $# -eq 3 ]] || usage
mode=$1
run_arg=$2
input_arg=$3
[[ $mode == msolve || $mode == singular ]] || usage

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
wrapper=$(realpath -e -- "${BASH_SOURCE[0]}")
if [[ -n ${CAPRUN:-} ]]; then
  caprun=$CAPRUN
elif [[ -f $script_dir/run_capped.py ]]; then
  caprun=$script_dir/run_capped.py
else
  caprun=$script_dir/../../ops/run_capped.py
fi

[[ -f $caprun ]] || die "CAPRUN is not a regular file: $caprun"
caprun=$(realpath -e -- "$caprun")
input=$(realpath -e -- "$input_arg")
[[ -f $input ]] || die "input is not a regular file: $input"
run_dir=$(realpath -m -- "$run_arg")
[[ ! -e $run_dir ]] || die "run directory must be fresh: $run_dir"
mkdir -p -- "$(dirname -- "$run_dir")"
mkdir -- "$run_dir" || die "could not claim fresh run directory: $run_dir"
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
  --wall-seconds "$WALL_SECONDS"
  --term-grace-seconds "$TERM_GRACE_SECONDS"
  --stdout-file "$stdout_file"
  --stderr-file "$stderr_file"
  --telemetry-file "$telemetry_file"
  --cwd "$run_dir"
)

if [[ $mode == msolve ]]; then
  solver=${MSOLVE_BIN:-/usr/local/bin/msolve}
  solver=$(realpath -e -- "$solver")
  [[ -x $solver ]] || die "msolve is not executable: $solver"
  basis=$run_dir/basis.ms
  command=(
    /usr/bin/time -v -o "$time_file" "$wrapper"
    __msolve_exec "$solver" "$input" "$basis" "$limit_file"
  )
  limit_kind=RLIMIT_AS
  limit_value=$MSOLVE_AS_KIB
  limit_units=KiB
else
  solver=${SINGULAR_BIN:-/usr/bin/Singular}
  solver=$(realpath -e -- "$solver")
  [[ -x $solver ]] || die "Singular is not executable: $solver"
  cap_args+=(
    --rss-bytes "$SINGULAR_RSS_BYTES"
    --rss-sample-seconds 0.05
  )
  command=(
    /usr/bin/time -v -o "$time_file" "$solver" -q --no-rc --no-warn --no-shell
    --threads=1 --flint-threads=1 "$input"
  )
  limit_kind=sampled_aggregate_PGID_RSS
  limit_value=$SINGULAR_RSS_BYTES
  limit_units=bytes
fi

caprun_pid=''
wait_interrupted=0
pending_signal=''
forward_to_caprun() {
  pending_signal=$1
  wait_interrupted=1
  if [[ -n $caprun_pid ]]; then
    kill -s "$1" "$caprun_pid" 2>/dev/null || true
  fi
}
trap 'forward_to_caprun HUP' HUP
trap 'forward_to_caprun INT' INT
trap 'forward_to_caprun TERM' TERM

{
  printf 'schema=T2T3_WORKER_RUN/v1\n'
  printf 'utc_preflight=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'mode=%s\n' "$mode"
  printf 'hostname=%s\n' "$(hostname)"
  printf 'nproc=%s\n' "$(nproc)"
  printf 'run_dir=%s\n' "$run_dir"
  printf 'TMPDIR=%s\n' "$TMPDIR"
  printf 'input=%s\n' "$input"
  printf 'solver=%s\n' "$solver"
  printf 'wrapper=%s\n' "$wrapper"
  printf 'caprun=%s\n' "$caprun"
  printf 'wall_seconds=%s\n' "$WALL_SECONDS"
  printf 'term_grace_seconds=%s\n' "$TERM_GRACE_SECONDS"
  printf 'limit_kind=%s\n' "$limit_kind"
  printf 'limit_value=%s\n' "$limit_value"
  printf 'limit_units=%s\n' "$limit_units"
  printf 'input_sha256=%s\n' "$(sha256sum -- "$input" | cut -d' ' -f1)"
  printf 'solver_sha256=%s\n' "$(sha256sum -- "$solver" | cut -d' ' -f1)"
  printf 'wrapper_sha256=%s\n' "$(sha256sum -- "$wrapper" | cut -d' ' -f1)"
  printf 'caprun_sha256=%s\n' "$(sha256sum -- "$caprun" | cut -d' ' -f1)"
  printf 'argv_shellquoted='
  printf ' %q' "${command[@]}"
  printf '\n'
} > "$custody_file"

set +e
/usr/bin/python3 "$caprun" "${cap_args[@]}" -- "${command[@]}" &
caprun_pid=$!
if [[ -n $pending_signal ]]; then
  kill -s "$pending_signal" "$caprun_pid" 2>/dev/null || true
fi
while true; do
  wait_interrupted=0
  wait "$caprun_pid"
  wait_rc=$?
  if (( wait_interrupted )); then
    continue
  fi
  runner_rc=$wait_rc
  break
done
set -e
trap - HUP INT TERM

{
  for artifact in "$input" "$custody_file" "$stdout_file" "$stderr_file" \
      "$telemetry_file" "$time_file" "$limit_file" "$run_dir/basis.ms"; do
    if [[ -f $artifact ]]; then
      sha256sum -- "$artifact"
    fi
  done
} > "$post_file.tmp"
mv -- "$post_file.tmp" "$post_file"

if [[ $mode == msolve ]]; then
  if [[ -n ${LANE_ETA:-} ]]; then
    lane_eta=$LANE_ETA
  elif [[ -f $script_dir/lane_eta.py ]]; then
    lane_eta=$script_dir/lane_eta.py
  else
    lane_eta=$script_dir/../../ops/lane_eta.py
  fi
  if [[ -f $lane_eta ]]; then
    /usr/bin/python3 "$lane_eta" --status "$stderr_file" \
      > "$run_dir/f4-status.txt" 2> "$run_dir/f4-status.stderr" || true
  fi
fi

printf '%s\n' "$runner_rc" > "$rc_file.tmp"
mv -- "$rc_file.tmp" "$rc_file"
exit "$runner_rc"
