#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "REFUSE: Linux required" >&2
  exit 64
fi

dmi="$(cat /sys/devices/virtual/dmi/id/sys_vendor 2>/dev/null || true)"
if [[ "$dmi" != *Amazon* ]]; then
  echo "REFUSE: Amazon EC2 required" >&2
  exit 64
fi

: "${JC2_AWS_JOB_TAG:?REFUSE: registered tag required}"
: "${EXPECTED_SOURCE_SHA256:?REFUSE: source hash required}"

if [[ $# -ne 2 ]]; then
  echo "usage: run_aws.sh SOURCE.py OUT_DIR" >&2
  exit 64
fi

source_file=$1
out_dir=$2
mkdir -p "$out_dir"
exec > >(tee "$out_dir/stdout") 2> >(tee "$out_dir/stderr" >&2)

echo "started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "host=$(hostname)"
echo "dmi=$dmi"
echo "tag=$JC2_AWS_JOB_TAG"
echo "python=$(/usr/bin/python3 --version 2>&1)"
actual_source_sha="$(sha256sum "$source_file" | awk '{print $1}')"
echo "source_sha256=$actual_source_sha"
[[ "$actual_source_sha" == "$EXPECTED_SOURCE_SHA256" ]]

ulimit -v 8388608
timeout --signal=TERM --kill-after=30 600 \
  /usr/bin/python3 "$source_file" --out "$out_dir/classes.json"

echo "classes_sha256=$(sha256sum "$out_dir/classes.json" | awk '{print $1}')"
echo "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
