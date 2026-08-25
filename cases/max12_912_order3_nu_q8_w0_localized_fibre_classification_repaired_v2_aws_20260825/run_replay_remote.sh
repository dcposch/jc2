#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: run_replay_remote.sh REPO OUTDIR" >&2
  exit 64
fi
repo=$1; out=$2
case_dir="$repo/cases/max12_912_order3_nu_q8_w0_localized_fibre_classification_repaired_v2_aws_20260825"
test ! -e "$out"
mkdir -p "$out"
sha256sum "$case_dir/replay.py" "$case_dir/PREREGISTRATION.md" \
  "$case_dir/PREREGISTRATION.manifest.sha256" > "$out/source.sha256"
{
  echo "host=$(hostname)"; echo "start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)";
  cat "$out/source.sha256";
} > "$out/run.meta"
set +e
/usr/bin/time -v timeout 120 python3 "$case_dir/replay.py" > "$out/stdout" 2> "$out/stderr"
rc=$?
set -e
{
  echo "end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "rc=$rc";
  sha256sum "$out/stdout" "$out/stderr";
} >> "$out/run.meta"
echo "$rc" > "$out/runner.rc"
if [[ $rc -ne 0 ]]; then exit "$rc"; fi
test "$(rg -c '^Q8_W0_LOCALIZED_FIBRE_REPAIRED_V2_REPLAY_PASS$' "$out/stdout" || true)" = 1
