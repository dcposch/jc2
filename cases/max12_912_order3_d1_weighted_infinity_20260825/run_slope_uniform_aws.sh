#!/usr/bin/env bash
set -euo pipefail

case_dir="cases/max12_912_order3_d1_weighted_infinity_20260825"
: "${JC2_AWS_TAG:?missing JC2_AWS_TAG}"
: "${D1_SLOPE_RUN_DIR:?missing D1_SLOPE_RUN_DIR}"
coordinates="${D1_SLOPE_COORDINATES:-normal}"
chart="${D1_SLOPE_CHART:-global}"
control_only="${D1_SLOPE_CONTROL_ONLY:-0}"
timeout_seconds="${D1_SLOPE_TIMEOUT_SECONDS:-14400}"
vm_kib="${D1_SLOPE_VM_KIB:-268435456}"

test "$(uname -s)" = Linux || { echo REFUSE_NON_LINUX >&2; exit 91; }
test -r /sys/class/dmi/id/sys_vendor || { echo REFUSE_NO_DMI >&2; exit 92; }
test "$(tr -d '\r\n' </sys/class/dmi/id/sys_vendor)" = "Amazon EC2" || {
  echo REFUSE_NON_AWS_EC2 >&2; exit 93;
}
case "$JC2_AWS_TAG" in
  max12_912_order3_d1_slope_uniform_*) ;;
  *) echo REFUSE_UNREGISTERED_AWS_TAG >&2; exit 94 ;;
esac
case "$D1_SLOPE_RUN_DIR" in
  /home/ubuntu/jobs/max12_912_order3_d1_slope_uniform_*) ;;
  *) echo REFUSE_BAD_RUN_DIR >&2; exit 95 ;;
esac
test ! -e "$D1_SLOPE_RUN_DIR" || { echo REFUSE_EXISTING_RUN_DIR >&2; exit 96; }
case "$coordinates" in normal|B) ;; *) echo REFUSE_COORDINATES >&2; exit 97;; esac
case "$chart" in global|p|c) ;; *) echo REFUSE_CHART >&2; exit 102;; esac
case "$control_only" in 0|1) ;; *) echo REFUSE_CONTROL_ONLY >&2; exit 103;; esac
control_arg=()
if test "$control_only" = 1; then control_arg=(--control-only); fi
case "$timeout_seconds" in *[!0-9]*|'') echo REFUSE_TIMEOUT >&2; exit 98;; esac
case "$vm_kib" in *[!0-9]*|'') echo REFUSE_VM_CAP >&2; exit 99;; esac

mkdir "$D1_SLOPE_RUN_DIR"
printf '%s\n' "$JC2_AWS_TAG" >"$D1_SLOPE_RUN_DIR/AWS_TAG"
hostname >"$D1_SLOPE_RUN_DIR/HOSTNAME"
date -u +%Y-%m-%dT%H:%M:%SZ >"$D1_SLOPE_RUN_DIR/START_UTC"
sha256sum -c "$case_dir/SOURCE_CLOSURE_SLOPE_UNIFORM.sha256" \
  >"$D1_SLOPE_RUN_DIR/source_closure.stdout" \
  2>"$D1_SLOPE_RUN_DIR/source_closure.stderr"

/usr/bin/time -v -o "$D1_SLOPE_RUN_DIR/payload.time" \
  python3 "$case_dir/compile_slope_uniform.py" --coordinates "$coordinates" \
    --chart "$chart" "${control_arg[@]}" \
  >"$D1_SLOPE_RUN_DIR/payload.json" \
  2>"$D1_SLOPE_RUN_DIR/payload.stderr"
grep -qx 'PASS-D1-SLOPE-UNIFORM-COMPILER' "$D1_SLOPE_RUN_DIR/payload.json"

/usr/bin/time -v -o "$D1_SLOPE_RUN_DIR/emit.time" \
  python3 "$case_dir/compile_slope_uniform.py" --singular \
    --coordinates "$coordinates" --chart "$chart" \
    "${control_arg[@]}" \
  >"$D1_SLOPE_RUN_DIR/slope_uniform.sing" \
  2>"$D1_SLOPE_RUN_DIR/emit.stderr"

set +e
/usr/bin/time -v -o "$D1_SLOPE_RUN_DIR/singular.time" \
  timeout "$timeout_seconds" bash -lc \
  "ulimit -v '$vm_kib'; exec Singular '$D1_SLOPE_RUN_DIR/slope_uniform.sing'" \
  >"$D1_SLOPE_RUN_DIR/singular.stdout" \
  2>"$D1_SLOPE_RUN_DIR/singular.stderr"
rc=$?
set -e
if test "$rc" -eq 0; then
  test ! -s "$D1_SLOPE_RUN_DIR/singular.stderr" || rc=104
fi
if test "$rc" -eq 0; then
  grep -qx 'PASS_D1_SLOPE_UNIFORM_SOURCE_AND_CONTROLS' \
    "$D1_SLOPE_RUN_DIR/singular.stdout" || rc=100
  grep -Eq '^SLOPE_UNIFORM_H_IS_UNIT=[01]$' \
    "$D1_SLOPE_RUN_DIR/singular.stdout" || rc=101
fi
printf '%s\n' "$rc" >"$D1_SLOPE_RUN_DIR/singular.rc"
date -u +%Y-%m-%dT%H:%M:%SZ >"$D1_SLOPE_RUN_DIR/END_UTC"
find "$D1_SLOPE_RUN_DIR" -maxdepth 1 -type f \
  ! -name OUTPUTS.sha256 -print0 \
  | sort -z | xargs -0 sha256sum >"$D1_SLOPE_RUN_DIR/OUTPUTS.sha256"
exit "$rc"
