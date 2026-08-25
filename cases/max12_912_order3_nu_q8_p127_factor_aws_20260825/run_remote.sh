#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then echo "usage: $0 REPO OUTROOT TAG" >&2; exit 64; fi
repo=$1
outroot=$2
tag=$3
case_rel=cases/max12_912_order3_nu_q8_p127_factor_aws_20260825
case_dir="$repo/$case_rel"
out="$outroot/$tag"
if [ -e "$out" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$out"
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/factor_q8.sing" | sed 's/^/source_sha256=/'
} > "$out/run.meta"
set +e
timeout 300 Singular -q "$case_dir/factor_q8.sing" > "$out/result.out" 2> "$out/stderr.log"
rc=$?
set -e
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
} >> "$out/run.meta"
if [ "$rc" -ne 0 ]; then echo "endpoint=FAIL" >> "$out/run.meta"; exit "$rc"; fi
count=$(grep -Fxc Q8-P127-FACTORIZATION "$out/result.out" || true)
if [ "$count" -ne 1 ]; then echo "endpoint=FAIL marker_count=$count" >> "$out/run.meta"; exit 66; fi
if grep -Eq '^\s*\?|error occurred|failed' "$out/result.out" "$out/stderr.log"; then
  echo "endpoint=FAIL singular_diagnostic=1" >> "$out/run.meta"
  exit 67
fi
for marker in factorization_begin factorization_end; do
  count=$(grep -Fxc "$marker" "$out/result.out" || true)
  if [ "$count" -ne 1 ]; then echo "endpoint=FAIL marker=$marker count=$count" >> "$out/run.meta"; exit 68; fi
done
{
  echo "endpoint=PASS"
  sha256sum "$out/result.out" | sed 's/^/stdout_sha256=/'
  sha256sum "$out/stderr.log" | sed 's/^/stderr_sha256=/'
} >> "$out/run.meta"
