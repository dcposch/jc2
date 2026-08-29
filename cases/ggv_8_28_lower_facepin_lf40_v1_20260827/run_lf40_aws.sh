#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only LF40 runner refused host" >&2
  exit 125
fi
if [[ $# -ne 10 ]]; then
  echo "usage: $0 SOURCE_ROOT JOB_ROOT TAG VMEM_KIB OUTER_TIMEOUT INNER_TIMEOUT FREEZE_REL EXPECTED_FREEZE_SHA SOURCE_ARCHIVE EXPECTED_ARCHIVE_SHA" >&2
  exit 125
fi

lf40_source_root=$1
lf40_job_root=$2
lf40_lane_tag=$3
lf40_cap_kib=$4
lf40_outer_timeout=$5
lf40_inner_timeout=$6
lf40_freeze_rel=$7
lf40_expected_freeze_sha=$8
lf40_source_archive=$9
lf40_expected_archive_sha=${10}
lf40_case_rel=cases/ggv_8_28_lower_facepin_lf40_v1_20260827

case "$lf40_lane_tag" in
  ggv_8_28_lf40_v1_*_r6b) ;;
  *) echo "malformed registered LF40 r6b lane" >&2; exit 125 ;;
esac
if [[ "$lf40_cap_kib" != "503316480" ]] || \
   [[ "$lf40_outer_timeout" != "43200" ]] || \
   [[ "$lf40_inner_timeout" != "42600" ]]; then
  echo "LF40 resource envelope differs from preregistration" >&2
  exit 125
fi
if [[ ! -d "$lf40_source_root" ]] || [[ ! -f "$lf40_source_archive" ]] || \
   [[ -e "$lf40_job_root" ]]; then
  echo "source/archive missing or job output target not fresh" >&2
  exit 125
fi
if find "$lf40_source_root" -type f -perm /222 -print -quit | grep -q .; then
  echo "immutable LF40 source tree contains writable file" >&2
  exit 125
fi

lf40_freeze="$lf40_source_root/$lf40_freeze_rel"
lf40_actual_freeze_sha=$(sha256sum "$lf40_freeze" | awk '{print $1}')
lf40_actual_archive_sha=$(sha256sum "$lf40_source_archive" | awk '{print $1}')
if [[ "$lf40_actual_freeze_sha" != "$lf40_expected_freeze_sha" ]] || \
   [[ "$lf40_actual_archive_sha" != "$lf40_expected_archive_sha" ]]; then
  echo "LF40 source freeze/archive digest mismatch" >&2
  exit 125
fi

mkdir -p "$lf40_job_root/run" "$lf40_job_root/replay"
{
  printf 'tag=%s\n' "$lf40_lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'dmi_vendor=%s\n' "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)"
  printf 'launcher_pid=%s\n' "$$"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=QQ_exact\n'
  printf 'engine=Singular_slimgb_sequential\n'
  printf 'workers=1\n'
  printf 'nice_level=5\n'
  printf 'virtual_memory_cap_kib=%s\n' "$lf40_cap_kib"
  printf 'outer_timeout_seconds=%s\n' "$lf40_outer_timeout"
  printf 'inner_timeout_seconds=%s\n' "$lf40_inner_timeout"
  printf 'source_freeze_sha256=%s\n' "$lf40_actual_freeze_sha"
  printf 'source_archive_sha256=%s\n' "$lf40_actual_archive_sha"
  printf 'representation=substituted_408_740_plus_rabinowitsch_409_741\n'
  printf 'saturator=exactly_a_times_b_times_rho_times_f_0_8_times_g_0_12\n'
  printf 'lifecycle=PRODUCER_UNREVIEWED_NOT_PROMOTED_EVIDENCE\n'
  printf 'placement=r6b_idle_at_live_preflight_20260827T184745Z\n'
  printf 'scope=actual_GGV_8_28_raw_prefinal_lower_necessary_system_only_no_JC2\n'
} > "$lf40_job_root/launch_registration.txt"

{
  date -u +snapshot_utc=%Y-%m-%dT%H:%M:%SZ
  free -b
  swapon --show
  df -h / /home/ubuntu
  /usr/bin/Singular --version | head -n 2
  ps -eo pid,ppid,stat,etimes,rss,pcpu,comm,args
  find /home/ubuntu/jobs -mindepth 1 -maxdepth 1 -printf '%TY-%Tm-%TdT%TH:%TM:%TSZ %y %f\n' | LC_ALL=C sort
} > "$lf40_job_root/protected_capacity_preflight.txt"

cd "$lf40_source_root"
sha256sum -c "$lf40_freeze_rel" > "$lf40_job_root/freeze_check.stdout"
if [[ ! -s "$lf40_job_root/freeze_check.stdout" ]] || \
   grep -Fq ': FAILED' "$lf40_job_root/freeze_check.stdout"; then
  echo "LF40 source freeze replay failed" >&2
  exit 125
fi

python3 -B "$lf40_case_rel/facepin_custody_gate.py" \
  "$lf40_source_root" "$lf40_job_root/replay/desk_gate" \
  > "$lf40_job_root/run/desk_gate.stdout" 2> "$lf40_job_root/run/desk_gate.stderr"
cmp "$lf40_source_root/$lf40_case_rel/desk_gate/DESK_GATE_EVIDENCE.sha256" \
    "$lf40_job_root/replay/desk_gate/DESK_GATE_EVIDENCE.sha256"
(cd "$lf40_job_root/replay/desk_gate" && sha256sum -c DESK_GATE_EVIDENCE.sha256) \
  > "$lf40_job_root/run/desk_gate_hash_replay.stdout"

python3 -B "$lf40_case_rel/compile_lf40.py" \
  "$lf40_source_root" "$lf40_job_root/replay/compiled" \
  > "$lf40_job_root/run/compiler.stdout" 2> "$lf40_job_root/run/compiler.stderr"
cmp "$lf40_source_root/$lf40_case_rel/compiled/COMPILER_EVIDENCE.sha256" \
    "$lf40_job_root/replay/compiled/COMPILER_EVIDENCE.sha256"
(cd "$lf40_job_root/replay/compiled" && sha256sum -c COMPILER_EVIDENCE.sha256) \
  > "$lf40_job_root/run/compiler_hash_replay.stdout"

export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
ulimit -v "$lf40_cap_kib"

set +e
timeout --signal=TERM --kill-after=300 "$lf40_outer_timeout" \
  /usr/bin/time -v timeout --signal=TERM --kill-after=300 "$lf40_inner_timeout" \
  nice -n 5 /usr/bin/Singular -q \
  "$lf40_job_root/replay/compiled/lf40_sequential_QQ.sing" \
  > "$lf40_job_root/run/solver.stdout" \
  2> "$lf40_job_root/run/solver.stderr"
lf40_solver_rc=$?
set -e

set +e
python3 -B "$lf40_case_rel/validate_aws_output.py" \
  "$lf40_job_root/replay/compiled/compiler_result.json" \
  "$lf40_job_root/run/solver.stdout" "$lf40_solver_rc" \
  "$lf40_job_root/RESULT.json" \
  > "$lf40_job_root/run/validator.stdout" \
  2> "$lf40_job_root/run/validator.stderr"
lf40_validator_rc=$?
set -e

lf40_max_rss=$(sed -n 's/^[[:space:]]*Maximum resident set size (kbytes):[[:space:]]*//p' \
  "$lf40_job_root/run/solver.stderr" | tail -n 1)
lf40_swaps=$(sed -n 's/^[[:space:]]*Swaps:[[:space:]]*//p' \
  "$lf40_job_root/run/solver.stderr" | tail -n 1)
lf40_elapsed=$(sed -n 's/^[[:space:]]*Elapsed (wall clock) time (h:mm:ss or m:ss):[[:space:]]*//p' \
  "$lf40_job_root/run/solver.stderr" | tail -n 1)
{
  printf 'solver_rc=%s\n' "$lf40_solver_rc"
  printf 'validator_rc=%s\n' "$lf40_validator_rc"
  printf 'max_rss_kib=%s\n' "${lf40_max_rss:-MISSING}"
  printf 'swaps=%s\n' "${lf40_swaps:-MISSING}"
  printf 'elapsed_wall=%s\n' "${lf40_elapsed:-MISSING}"
} > "$lf40_job_root/run/FINAL.validation"
{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'solver_rc=%s\n' "$lf40_solver_rc"
  printf 'validator_rc=%s\n' "$lf40_validator_rc"
} >> "$lf40_job_root/launch_registration.txt"

(
  cd "$lf40_job_root"
  find . -type f ! -name EVIDENCE.sha256 ! -name EVIDENCE.sha256.tmp -print0 \
    | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256.tmp
  mv EVIDENCE.sha256.tmp EVIDENCE.sha256
)

if [[ "$lf40_validator_rc" -ne 0 ]]; then
  exit "$lf40_validator_rc"
fi
exit 0

