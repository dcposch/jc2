#!/bin/sh
set -eu

if [ "$#" -ne 3 ]; then
  echo "usage: $0 REPO OUTROOT TAG" >&2
  exit 64
fi
repo=$1
outroot=$2
tag=$3
case_rel=cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825
case_dir="$repo/$case_rel"
out="$outroot/$tag"
if [ -e "$out" ]; then echo "duplicate lane refused" >&2; exit 65; fi
mkdir -p "$out"
: > "$out/result.json"
: > "$out/stderr.log"
{
  echo "tag=$tag"
  hostname | sed 's/^/host=/'
  date -u +start_utc=%Y-%m-%dT%H:%M:%SZ
  echo "method=exact-F127-Q8bar-full-source-contact-Jacobian"
  echo "virtual_memory_limit_kib=4194304"
  echo "timeout_seconds=1800"
  sha256sum "$0" "$case_dir/full_contact.py" "$repo/cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py" | sed 's/^/source_sha256=/'
} > "$out/run.meta"
set +e
(
  ulimit -v 4194304
  timeout --signal=TERM --kill-after=60 1800 /usr/bin/time -v \
    python3 "$case_dir/full_contact.py"
) > "$out/result.json" 2> "$out/stderr.log"
rc=$?
set -e
{
  date -u +end_utc=%Y-%m-%dT%H:%M:%SZ
  echo "rc=$rc"
} >> "$out/run.meta"
if [ "$rc" -ne 0 ]; then echo "endpoint=FAIL" >> "$out/run.meta"; exit "$rc"; fi
python3 - "$out/result.json" <<'PY'
import json, sys
payload=json.load(open(sys.argv[1]))
assert payload["status"] == "PASS"
assert payload["full_relative_jacobian"]["rank_at_every_geometric_q8_contact"] == 8
assert payload["full_relative_jacobian"]["gcd_determinant_q8"] == [1]
assert payload["full_relative_jacobian"]["determinant_norm_mod_127"] != 0
assert all(value == [0] for value in payload["row_residuals"].values())
assert any(value != [0] for value in payload["old_wrong_x1_residuals"].values())
PY
{
  echo "endpoint=PASS"
  sha256sum "$out/result.json" | sed 's/^/stdout_sha256=/'
  sha256sum "$out/stderr.log" | sed 's/^/stderr_sha256=/'
} >> "$out/run.meta"

