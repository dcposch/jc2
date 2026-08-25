#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 5 ]]; then
  echo "usage: run_replay_remote.sh VM_KIB REPO OUT TAG PYTHON" >&2
  exit 64
fi
vm_kib=$1; repo=$2; outroot=$3; tag=$4; python_bin=$5
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825"
out="$outroot/$tag"
test ! -e "$out"
mkdir -p "$out"
ulimit -v "$vm_kib"
sha256sum "$case_dir/replay.py" "$case_dir/run_replay_remote.sh" \
  "$case_dir/REPLAY_INPUT.manifest.sha256" > "$out/source.sha256"
{
  echo "tag=$tag"; echo "host=$(hostname)"; echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  echo "virtual_memory_limit_kib=$vm_kib"; cat "$out/source.sha256";
} > "$out/run.meta"
set +e
/usr/bin/time -v timeout 300 "$python_bin" "$case_dir/replay.py" \
  > "$out/stdout" 2> "$out/stderr"
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/stdout" "$out/stderr";
} >> "$out/run.meta"
echo "$rc" > "$out/runner.rc"
test "$rc" = 0
test "$(grep -c '^Q8_W0_X5_CYLINDER_LOCAL_GERM_V3_REPLAY_PASS$' "$out/stdout" || true)" = 1
