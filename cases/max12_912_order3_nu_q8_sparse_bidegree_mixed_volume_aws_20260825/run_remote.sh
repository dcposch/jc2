#!/bin/sh
set -eu
if [ "$#" -ne 6 ]; then
  echo "usage: $0 REPO OUTROOT TAG KIND WORKERS CONTROLS" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
kind=$4
workers=$5
controls=$6
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 64 ;; esac
case "$kind" in vertical|horizontal) ;; *) exit 64 ;; esac
case "$controls" in yes|no) ;; *) exit 64 ;; esac
case_dir=$repo/cases/max12_912_order3_nu_q8_sparse_bidegree_mixed_volume_aws_20260825
lane=$outroot/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$lane"
control_arg=
if [ "$controls" = yes ]; then control_arg=--controls; fi
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "kind=$kind"
  echo "workers=$workers"
  echo "method=exact-Normaliz-origin-augmented-affine-BKK"
  normaliz --version | head -1 | sed 's/^/normaliz=/'
  sha256sum "$0" "$case_dir/bidegree.py" \
    "$repo/cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/mixed_volume.py" \
    "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" \
    | sed 's/^/source_sha256=/'
} > "$lane/run.meta"
set +e
(
  ulimit -v 33554432
  timeout --signal=TERM --kill-after=120 7200 /usr/bin/time -v \
    python3 "$case_dir/bidegree.py" --kind "$kind" --work "$lane/work" \
      --workers "$workers" --output "$lane/result.json" $control_arg
) > "$lane/result.out" 2> "$lane/stderr.log"
rc=$?
set -e
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
} >> "$lane/run.meta"
if [ "$rc" -ne 0 ]; then echo "endpoint=FAIL" >> "$lane/run.meta"; exit "$rc"; fi
for marker in Q8-SPARSE-BIDEGREE-MIXED-VOLUME status=PASS "kind=$kind"; do
  count=$(grep -Fxc "$marker" "$lane/result.out" || true)
  if [ "$count" -ne 1 ]; then
    echo "endpoint=FAIL marker=$marker count=$count" >> "$lane/run.meta"
    exit 66
  fi
done
python3 - "$lane/result.json" "$kind" "$controls" <<'PY'
import json, sys
p=json.load(open(sys.argv[1]))
assert p["status"] == "PASS" and p["kind"] == sys.argv[2]
assert isinstance(p["mixed_volume_bound"], int) and p["mixed_volume_bound"] >= 0
if sys.argv[3] == "yes":
    assert p["controls"] == {"coordinate_segments": 1, "repeated_standard_simplex": 1}
else:
    assert p["controls"] == {}
PY
{
  echo "endpoint=PASS"
  sha256sum "$lane/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$lane/stderr.log" | sed 's/^/stderr_sha256=/'
  sha256sum "$lane/result.json" | sed 's/^/result_sha256=/'
} >> "$lane/run.meta"
