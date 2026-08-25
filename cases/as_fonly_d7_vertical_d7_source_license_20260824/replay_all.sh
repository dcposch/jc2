#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$case_dir"

scratch=$(mktemp -d "${TMPDIR:-/tmp}/as-d7-source-license.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
python3 audit_full_e1_degree7.py > "$scratch/source.out"
grep -q '^PASS-D7-FULL-E1-DEGREE7-SOURCE-LICENSE$' "$scratch/source.out"
actual=$(shasum -a 256 "$scratch/source.out" | awk '{print $1}')
expected=$(awk '{print $1}' EXPECTED_OUTPUT_SHA256.txt)
if [ "$actual" != "$expected" ]; then
  printf 'output hash mismatch: expected %s got %s\n' "$expected" "$actual" >&2
  exit 1
fi
shasum -a 256 -c MANIFEST.sha256
printf 'source_output_sha256 %s\n' "$actual"
printf '%s\n' 'PASS-AS-FONLY-D7-SOURCE-LICENSE-ALL'
