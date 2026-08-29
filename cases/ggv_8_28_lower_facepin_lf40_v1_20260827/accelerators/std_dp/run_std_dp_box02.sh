#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]] || \
   [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)" != "Amazon EC2" ]]; then
  echo "AWS-only LF40 std/dp runner refused host" >&2
  exit 125
fi
if [[ $# -ne 10 ]]; then
  echo "usage: $0 SOURCE_ROOT JOB_ROOT TAG VMEM_KIB OUTER_TIMEOUT INNER_TIMEOUT FREEZE_REL EXPECTED_FREEZE_SHA SOURCE_ARCHIVE EXPECTED_ARCHIVE_SHA" >&2
  exit 125
fi

source_root=$1
job_root=$2
lane_tag=$3
cap_kib=$4
outer_timeout=$5
inner_timeout=$6
freeze_rel=$7
expected_freeze_sha=$8
source_archive=$9
expected_archive_sha=${10}
case_rel=cases/ggv_8_28_lower_facepin_lf40_v1_20260827
program_rel=$case_rel/accelerators/std_dp/lf40_sequential_QQ_std_dp.sing
program_sha=7256fcaddcdc2875ca6c31b2033f0e6950a598b8a22d3cc338c92069a89f21a5

case "$lane_tag" in
  ggv_8_28_lf40_targetfix_r1_std_dp_*_box02) ;;
  *) echo "malformed LF40 std/dp Box02 tag" >&2; exit 125 ;;
esac
if [[ "$cap_kib" != "943718400" ]] || [[ "$outer_timeout" != "21600" ]] || \
   [[ "$inner_timeout" != "21000" ]]; then
  echo "LF40 std/dp resource envelope differs from preregistration" >&2
  exit 125
fi
if [[ ! -d "$source_root" ]] || [[ ! -f "$source_archive" ]] || \
   [[ -e "$job_root" ]]; then
  echo "source/archive missing or output target not fresh" >&2
  exit 125
fi
if find "$source_root" -type f -perm /222 -print -quit | grep -q .; then
  echo "source tree contains writable file" >&2
  exit 125
fi
if swapon --noheadings | grep -q .; then
  echo "LF40 std/dp refuses a swap-enabled host" >&2
  exit 125
fi

freeze_path=$source_root/$freeze_rel
actual_freeze_sha=$(sha256sum "$freeze_path" | awk '{print $1}')
actual_archive_sha=$(sha256sum "$source_archive" | awk '{print $1}')
actual_program_sha=$(sha256sum "$source_root/$program_rel" | awk '{print $1}')
if [[ "$actual_freeze_sha" != "$expected_freeze_sha" ]] || \
   [[ "$actual_archive_sha" != "$expected_archive_sha" ]] || \
   [[ "$actual_program_sha" != "$program_sha" ]]; then
  echo "LF40 std/dp source or program digest mismatch" >&2
  exit 125
fi

mkdir -p "$job_root/run" "$job_root/replay"
{
  printf 'tag=%s\n' "$lane_tag"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'field=QQ_exact\nalgorithm=std\norder=dp\nworkers=1\nnice_level=5\n'
  printf 'virtual_memory_cap_kib=%s\nouter_timeout_seconds=%s\ninner_timeout_seconds=%s\n' \
    "$cap_kib" "$outer_timeout" "$inner_timeout"
  printf 'source_freeze_sha256=%s\nsource_archive_sha256=%s\nprogram_sha256=%s\n' \
    "$actual_freeze_sha" "$actual_archive_sha" "$actual_program_sha"
  printf 'lifecycle=PRODUCER_UNREVIEWED_EXACT_CROSSCHECK_NOT_PROMOTED\n'
  printf 'scope=corrected_LF40_R1_identical_ideal_engine_substitution_only_no_JC2\n'
} > "$job_root/launch_registration.txt"

{
  date -u +snapshot_utc=%Y-%m-%dT%H:%M:%SZ
  free -b
  swapon --show
  df -h / /home/ubuntu
  /usr/bin/Singular --version | head -n 2
  ps -eo pid,ppid,stat,etimes,rss,pcpu,comm,args
} > "$job_root/protected_capacity_preflight.txt"

cd "$source_root"
sha256sum -c "$freeze_rel" > "$job_root/freeze_check.stdout"
python3 -B "$case_rel/facepin_custody_gate.py" "$source_root" \
  "$job_root/replay/desk_gate" > "$job_root/run/desk_gate.stdout" \
  2> "$job_root/run/desk_gate.stderr"
cmp "$source_root/$case_rel/desk_gate/DESK_GATE_EVIDENCE.sha256" \
  "$job_root/replay/desk_gate/DESK_GATE_EVIDENCE.sha256"
python3 -B "$case_rel/compile_lf40.py" "$source_root" \
  "$job_root/replay/compiled" > "$job_root/run/compiler.stdout" \
  2> "$job_root/run/compiler.stderr"
cmp "$source_root/$case_rel/compiled/COMPILER_EVIDENCE.sha256" \
  "$job_root/replay/compiled/COMPILER_EVIDENCE.sha256"
python3 -B "$case_rel/accelerators/std_dp/verify_std_dp.py" "$source_root" \
  > "$job_root/run/accelerator_verify.stdout" \
  2> "$job_root/run/accelerator_verify.stderr"
sed 's/slimgb(/std(/g' "$job_root/replay/compiled/lf40_sequential_QQ.sing" \
  > "$job_root/replay/lf40_sequential_QQ_std_dp.sing"
cmp "$source_root/$program_rel" "$job_root/replay/lf40_sequential_QQ_std_dp.sing"

export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
ulimit -v "$cap_kib"
set +e
timeout --signal=TERM --kill-after=300 "$outer_timeout" \
  /usr/bin/time -v timeout --signal=TERM --kill-after=300 "$inner_timeout" \
  nice -n 5 /usr/bin/Singular -q "$job_root/replay/lf40_sequential_QQ_std_dp.sing" \
  > "$job_root/run/solver.stdout" 2> "$job_root/run/solver.stderr"
solver_rc=$?
set -e

set +e
python3 -B "$case_rel/validate_aws_output.py" \
  "$job_root/replay/compiled/compiler_result.json" \
  "$job_root/run/solver.stdout" "$solver_rc" "$job_root/RESULT.json" \
  > "$job_root/run/validator.stdout" 2> "$job_root/run/validator.stderr"
validator_rc=$?
set -e

max_rss=$(sed -n 's/^[[:space:]]*Maximum resident set size (kbytes):[[:space:]]*//p' \
  "$job_root/run/solver.stderr" | tail -n 1)
swaps=$(sed -n 's/^[[:space:]]*Swaps:[[:space:]]*//p' \
  "$job_root/run/solver.stderr" | tail -n 1)
elapsed=$(sed -n 's/^[[:space:]]*Elapsed (wall clock) time (h:mm:ss or m:ss):[[:space:]]*//p' \
  "$job_root/run/solver.stderr" | tail -n 1)
{
  printf 'solver_rc=%s\nvalidator_rc=%s\n' "$solver_rc" "$validator_rc"
  printf 'max_rss_kib=%s\nswaps=%s\nelapsed_wall=%s\n' \
    "${max_rss:-MISSING}" "${swaps:-MISSING}" "${elapsed:-MISSING}"
} > "$job_root/run/FINAL.validation"
{
  printf 'end_utc=%s\nsolver_rc=%s\nvalidator_rc=%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$solver_rc" "$validator_rc"
} >> "$job_root/launch_registration.txt"

(
  cd "$job_root"
  find . -type f ! -name EVIDENCE.sha256 ! -name EVIDENCE.sha256.tmp -print0 \
    | LC_ALL=C sort -z | xargs -0 sha256sum > EVIDENCE.sha256.tmp
  mv EVIDENCE.sha256.tmp EVIDENCE.sha256
)
if [[ "$validator_rc" -ne 0 ]]; then
  exit "$validator_rc"
fi
exit 0
