#!/usr/bin/env bash
set -euo pipefail

case_dir="cases/max12_912_order3_d1_weighted_infinity_20260825"
: "${JC2_AWS_TAG:?missing JC2_AWS_TAG}"
: "${D1_INFINITY_RUN_DIR:?missing D1_INFINITY_RUN_DIR}"
characteristic="${D1_INFINITY_CHARACTERISTIC:-0}"
chart="${D1_INFINITY_CHART:-global}"

test "$(uname -s)" = Linux || { echo REFUSE_NON_LINUX >&2; exit 91; }
test -r /sys/class/dmi/id/sys_vendor || { echo REFUSE_NO_DMI >&2; exit 92; }
test "$(tr -d '\r\n' </sys/class/dmi/id/sys_vendor)" = "Amazon EC2" || {
  echo REFUSE_NON_AWS_EC2 >&2; exit 93;
}
case "$JC2_AWS_TAG" in
  max12_912_order3_d1_infty_exceptional_v2_*) ;;
  *) echo REFUSE_UNREGISTERED_AWS_TAG >&2; exit 94 ;;
esac
case "$D1_INFINITY_RUN_DIR" in
  /home/ubuntu/jobs/max12_912_order3_d1_infty_exceptional_v2_*) ;;
  *) echo REFUSE_BAD_RUN_DIR >&2; exit 95 ;;
esac
test ! -e "$D1_INFINITY_RUN_DIR" || { echo REFUSE_EXISTING_RUN_DIR >&2; exit 96; }
case "$characteristic" in
  0|32003) ;;
  *) echo REFUSE_UNREGISTERED_CHARACTERISTIC >&2; exit 97 ;;
esac
case "$chart" in
  global|0|1|2|3|4|5|6|7) ;;
  *) echo REFUSE_UNREGISTERED_CHART >&2; exit 98 ;;
esac

mkdir "$D1_INFINITY_RUN_DIR"
printf '%s\n' "$JC2_AWS_TAG" >"$D1_INFINITY_RUN_DIR/AWS_TAG"
hostname >"$D1_INFINITY_RUN_DIR/HOSTNAME"
date -u +%Y-%m-%dT%H:%M:%SZ >"$D1_INFINITY_RUN_DIR/START_UTC"
sha256sum -c "$case_dir/SOURCE_CLOSURE_V2.sha256" \
  >"$D1_INFINITY_RUN_DIR/source_closure_v2.stdout" \
  2>"$D1_INFINITY_RUN_DIR/source_closure_v2.stderr"
sha256sum -c "$case_dir/SOURCE_CLOSURE.sha256" \
  >"$D1_INFINITY_RUN_DIR/source_closure_v1.stdout" \
  2>"$D1_INFINITY_RUN_DIR/source_closure_v1.stderr"

/usr/bin/time -v -o "$D1_INFINITY_RUN_DIR/payload.time" \
  python3 "$case_dir/compile_exceptional_v2.py" --chart "$chart" \
  >"$D1_INFINITY_RUN_DIR/payload.json" \
  2>"$D1_INFINITY_RUN_DIR/payload.stderr"

/usr/bin/time -v -o "$D1_INFINITY_RUN_DIR/emit.time" \
  python3 "$case_dir/compile_exceptional_v2.py" --singular \
    --characteristic "$characteristic" --chart "$chart" \
  >"$D1_INFINITY_RUN_DIR/exceptional.sing" \
  2>"$D1_INFINITY_RUN_DIR/emit.stderr"

set +e
/usr/bin/time -v -o "$D1_INFINITY_RUN_DIR/singular.time" \
  timeout 7200 bash -lc \
  "ulimit -v 134217728; exec Singular '$D1_INFINITY_RUN_DIR/exceptional.sing'" \
  >"$D1_INFINITY_RUN_DIR/singular.stdout" \
  2>"$D1_INFINITY_RUN_DIR/singular.stderr"
rc=$?
set -e
printf '%s\n' "$rc" >"$D1_INFINITY_RUN_DIR/singular.rc"
date -u +%Y-%m-%dT%H:%M:%SZ >"$D1_INFINITY_RUN_DIR/END_UTC"
find "$D1_INFINITY_RUN_DIR" -maxdepth 1 -type f \
  ! -name OUTPUTS.sha256 -print0 \
  | sort -z | xargs -0 sha256sum >"$D1_INFINITY_RUN_DIR/OUTPUTS.sha256"
exit "$rc"
