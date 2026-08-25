#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo REFUSE_NON_LINUX >&2
  exit 97
fi
if [[ ! -r /sys/class/dmi/id/sys_vendor ]] || \
   [[ "$(tr -d '\r\n' </sys/class/dmi/id/sys_vendor)" != "Amazon EC2" ]]; then
  echo REFUSE_NON_AWS_EC2 >&2
  exit 96
fi
if [[ "${JC2_AWS_TAG:-}" != max12_912_order3_d1_* ]]; then
  echo REFUSE_UNREGISTERED_AWS_TAG >&2
  exit 98
fi
if [[ ! -f cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/SOURCE_CLOSURE_V2.sha256 ]]; then
  echo REFUSE_MISSING_V2_CLOSURE >&2
  exit 99
fi

case_dir=cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825
run_dir=${D1_RUN_DIR:?D1_RUN_DIR is required}
case "$run_dir" in
  /home/ubuntu/jobs/max12_912_order3_d1_*) ;;
  *) echo REFUSE_UNREGISTERED_RUN_DIR >&2; exit 95 ;;
esac
if [[ -e "$run_dir" ]]; then
  echo REFUSE_DUPLICATE_RUN_DIR >&2
  exit 94
fi
mkdir -p "$run_dir"
hostname >"$run_dir/hostname.txt"
printf '%s\n' "$$" >"$run_dir/runner.pid"
printf '%s\n' "$JC2_AWS_TAG" >"$run_dir/aws_tag.txt"
cp "$case_dir/SOURCE_CLOSURE_V2.sha256" "$run_dir/"
sha256sum -c "$case_dir/SOURCE_CLOSURE_V2.sha256" \
  >"$run_dir/source_closure.stdout" 2>"$run_dir/source_closure.stderr"

ulimit -v 134217728
/usr/bin/time -v -o "$run_dir/independent.time" timeout 30m \
  python3 "$case_dir/independent_reconstruct.py" \
  >"$run_dir/independent.json" 2>"$run_dir/independent.stderr"
/usr/bin/time -v -o "$run_dir/source_rows.time" timeout 30m \
  python3 "$case_dir/compile_gate_v2.py" \
  >"$run_dir/source_rows.json" 2>"$run_dir/source_rows.stderr"
/usr/bin/time -v -o "$run_dir/stage_a_emit.time" timeout 30m \
  python3 "$case_dir/stage_a_interface.py" --generic-absolute --engine slimgb \
  >"$run_dir/stage_a_generic.sing" 2>"$run_dir/stage_a_emit.stderr"
if [[ "${D1_SOURCE_ONLY:-0}" == 1 ]]; then
  sha256sum "$run_dir"/* >"$run_dir/OUTPUTS.sha256"
  echo PASS-D1-V2-AWS-SOURCE-ONLY-RUNNER
  exit 0
fi
/usr/bin/time -v -o "$run_dir/stage_a_generic.time" timeout 2h \
  Singular "$run_dir/stage_a_generic.sing" \
  >"$run_dir/stage_a_generic.stdout" 2>"$run_dir/stage_a_generic.stderr"

sha256sum "$run_dir"/* >"$run_dir/OUTPUTS.sha256"
echo PASS-D1-V2-AWS-SOURCE-AND-GENERIC-RUNNER
