#!/bin/sh
set -eu
if [ "$#" -ne 3 ]; then
  echo "usage: $0 <repo> <out-root> <tag>" >&2
  exit 2
fi
repo_root=$1
out_root=$2
tag=$3
case "$tag" in ''|*[!A-Za-z0-9._-]*) exit 2 ;; esac
case_dir=$repo_root/cases/max12_912_order3_nu_q8_p127_candidate_plane_integrality_aws_20260825
lane=$out_root/$tag
if [ -e "$lane" ]; then echo "duplicate lane refused" >&2; exit 3; fi
mkdir -p "$lane"
meta=$lane/run.meta
set +e
python3 "$case_dir/generate.py" > "$lane/input.sing" 2> "$lane/generator.stderr"
generator_rc=$?
set -e
{
  echo "tag=$tag"
  echo "host=$(hostname)"
  echo "start_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "generator_rc=$generator_rc"
  Singular --version | head -1 | sed 's/^/singular=/'
  sha256sum "$0" "$case_dir/generate.py" "$case_dir/audit.py" \
    "$repo_root/cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json" \
    | sed 's/^/source_sha256=/'
} > "$meta"
if [ "$generator_rc" -ne 0 ] || [ ! -s "$lane/input.sing" ] || [ -s "$lane/generator.stderr" ]; then
  echo "rc=90" >> "$meta"
  exit 90
fi
set +e
Singular -q < "$lane/input.sing" > "$lane/result.out" 2> "$lane/stderr.log"
singular_rc=$?
python3 "$case_dir/audit.py" "$lane/result.out" --output "$lane/audit.json" \
  > "$lane/audit.out" 2> "$lane/audit.stderr"
audit_rc=$?
set -e
rc=91
endpoint=FAIL
if [ "$singular_rc" -eq 0 ] && [ "$audit_rc" -eq 0 ] \
  && [ ! -s "$lane/stderr.log" ] && [ ! -s "$lane/audit.stderr" ] \
  && grep -qx 'status=PASS' "$lane/audit.out"; then
  rc=0
  endpoint=PASS
fi
{
  echo "end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "singular_rc=$singular_rc"
  echo "audit_rc=$audit_rc"
  echo "rc=$rc"
  echo "endpoint=$endpoint"
  sha256sum "$lane/result.out" "$lane/audit.json" "$lane/audit.out" \
    "$lane/stderr.log" "$lane/audit.stderr" | sed 's/^/output_sha256=/'
} >> "$meta"
exit "$rc"
