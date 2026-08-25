#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then echo "usage: $0 REPO OUTROOT TAG WORKERS" >&2; exit 64; fi
repo=$1
outroot=$2
tag=$3
workers=$4
case_rel=cases/max12_912_order3_nu_q8_sparse_mixed_volume_affine_shard_aws_20260825
case_dir="$repo/$case_rel"
out="$outroot/$tag"
if [ -e "$out" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$out"
: > "$out/result.out"
: > "$out/stderr.log"
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "method=exact-Normaliz-origin-augmented-affine-mixed-volume-shard"
  echo "workers=$workers"
  echo "virtual_memory_limit_kib=33554432"
  echo "timeout_seconds=7200"
  normaliz --version | head -1 | sed 's/^/normaliz=/'
  sha256sum "$0" "$case_dir/affine_only.py" \
    "$repo/cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/mixed_volume.py" \
    "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
} > "$out/run.meta"
set +e
(
  ulimit -v 33554432
  timeout --signal=TERM --kill-after=120 7200 /usr/bin/time -v \
    python3 "$case_dir/affine_only.py" \
      --work "$out/work" --workers "$workers" --output "$out/result.json"
) > "$out/result.out" 2> "$out/stderr.log"
rc=$?
set -e
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
} >> "$out/run.meta"
if [ "$rc" -ne 0 ]; then echo "endpoint=FAIL" >> "$out/run.meta"; exit "$rc"; fi
for marker in Q8-SPARSE-MIXED-VOLUME-AFFINE-SHARD status=PASS; do
  count=$(grep -Fxc "$marker" "$out/result.out" || true)
  if [ "$count" -ne 1 ]; then echo "endpoint=FAIL marker=$marker count=$count" >> "$out/run.meta"; exit 66; fi
done
test -s "$out/result.json"
{
  echo "endpoint=PASS"
  sha256sum "$out/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$out/stderr.log" | sed 's/^/stderr_sha256=/'
  sha256sum "$out/result.json" | sed 's/^/result_sha256=/'
} >> "$out/run.meta"

