#!/bin/sh
set -eu
if [ "$#" -ne 4 ]; then echo "usage: $0 REPO OUTROOT TAG WORKERS" >&2; exit 64; fi
repo=$1; outroot=$2; tag=$3; workers=$4
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_vertical_reduced_mixed_volume_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
{
  echo "tag=$tag"; hostname | sed 's/^/host=/'; date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "method=ratio-substituted-generic-vertical-origin-augmented-BKK"
  echo "workers=$workers"
  normaliz --version | head -1 | sed 's/^/normaliz=/'
  sha256sum "$0" "$case_dir/vertical_reduced.py" \
    "$repo/cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/mixed_volume.py" \
    "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
} > "$lane/run.meta"
set +e
(
  ulimit -v 33554432
  timeout --signal=TERM --kill-after=120 7200 /usr/bin/time -v \
    python3 "$case_dir/vertical_reduced.py" --work "$lane/work" \
      --workers "$workers" --output "$lane/result.json"
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
{ date -u +end_utc=%Y-%m-%dT%H:%M:%SZ; echo "rc=$rc"; } >> "$lane/run.meta"
if [ "$rc" -ne 0 ]; then echo "endpoint=FAIL" >> "$lane/run.meta"; exit "$rc"; fi
for marker in Q8-VERTICAL-REDUCED-MIXED-VOLUME status=PASS; do
  [ "$(grep -Fxc "$marker" "$lane/result.out" || true)" -eq 1 ] || { echo "endpoint=FAIL" >> "$lane/run.meta"; exit 66; }
done
python3 - "$lane/result.json" <<'PY'
import json,sys
p=json.load(open(sys.argv[1]))
assert p["status"]=="PASS"
assert p["controls"]=={"coordinate_segments":1,"repeated_standard_simplex":1}
assert p["vertical_degree_bound"]>=0
PY
{
  echo "endpoint=PASS"
  sha256sum "$lane/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$lane/stderr.log" | sed 's/^/stderr_sha256=/'
  sha256sum "$lane/result.json" | sed 's/^/result_sha256=/'
} >> "$lane/run.meta"
