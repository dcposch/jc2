#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: pipeline_worker.sh RUN_DIR" >&2
  exit 64
fi

run_dir=$(realpath "$1")
source_dir="$run_dir/source"
work_dir="$run_dir/work"
output_dir="$run_dir/output"
records_dir="$run_dir/records"
mkdir -p "$work_dir" "$output_dir" "$records_dir"

ore_commit=18680180c884fac869a064db99f29a221aad9dfe
export ORE_COMMIT=$ore_commit

cd "$work_dir"
/usr/bin/timeout --foreground --signal=TERM --kill-after=30 300 \
  git clone -q https://github.com/mkauers/ore_algebra.git ore_algebra_src
git -C ore_algebra_src checkout -q "$ore_commit"
[[ "$(git -C ore_algebra_src rev-parse HEAD)" == "$ore_commit" ]]
git -C ore_algebra_src apply "$source_dir/ore_disable_analytic_extensions.patch"
git -C ore_algebra_src apply "$source_dir/ore_generic_multivariate_fallback.patch"
git -C ore_algebra_src diff --check
git -C ore_algebra_src status --short > "$records_dir/ORE_STATUS.txt"
git -C ore_algebra_src diff -- setup.py src/ore_algebra/ore_algebra.py > "$records_dir/ORE_MUTATIONS.diff"
sha256sum \
  "$source_dir/ore_disable_analytic_extensions.patch" \
  "$source_dir/ore_generic_multivariate_fallback.patch" \
  ore_algebra_src/setup.py \
  ore_algebra_src/src/ore_algebra/ore_algebra.py \
  "$records_dir/ORE_MUTATIONS.diff" > "$records_dir/MUTATIONS.sha256"
printf '%s\n' "$ore_commit" > "$records_dir/ORE_COMMIT.txt"

python3 -m venv venv
set +e
/usr/bin/time -v /usr/bin/timeout --foreground --signal=TERM --kill-after=60 1800 \
  venv/bin/pip install -q './ore_algebra_src[passagemath]' \
  > "$records_dir/install.stdout" 2> "$records_dir/install.stderr"
install_rc=$?
set -e
printf '%s\n' "$install_rc" > "$records_dir/install.rc"
if [[ "$install_rc" -ne 0 ]]; then
  printf '%s\n' "FAIL_INSTALL" > "$output_dir/TERMINAL"
  exit "$install_rc"
fi
venv/bin/pip freeze | LC_ALL=C sort > "$records_dir/TOOLCHAIN_FREEZE.txt"
chmod -R a-w ore_algebra_src

set +e
/usr/bin/time -v /usr/bin/timeout --foreground --signal=TERM --kill-after=60 14400 \
  venv/bin/python "$source_dir/run_pipeline.py" --output-dir "$output_dir" \
  > "$records_dir/pipeline.stdout" 2> "$records_dir/pipeline.stderr"
pipeline_rc=$?
set -e
printf '%s\n' "$pipeline_rc" > "$records_dir/pipeline.rc"
if [[ "$pipeline_rc" -eq 124 ]]; then
  stage=$(tr -d '\n' < "$output_dir/CURRENT_STAGE" 2>/dev/null || true)
  if [[ "$stage" == UPSTREAM* || "$stage" == "BRIDGE_PROBE" ]]; then
    printf '%s\n' "TIMEOUT_UPSTREAM" > "$output_dir/TERMINAL"
  else
    printf '%s\n' "TIMEOUT_CONTROL" > "$output_dir/TERMINAL"
  fi
elif [[ "$pipeline_rc" -ne 0 && ! -s "$output_dir/TERMINAL" ]]; then
  printf '%s\n' "FAIL_PIPELINE_RC" > "$output_dir/TERMINAL"
fi

find "$source_dir" -type f -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > "$records_dir/FROZEN_SOURCE.sha256"
find "$output_dir" -type f -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > "$records_dir/OUTPUTS.sha256"
exit "$pipeline_rc"
