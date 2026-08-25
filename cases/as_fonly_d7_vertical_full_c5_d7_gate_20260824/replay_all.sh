#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$case_dir"
scratch=$(mktemp -d "${TMPDIR:-/tmp}/as-full-c5-d7.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM

python3 audit_full_c5_source.py > "$scratch/source.out"
python3 audit_lower_divergence.py > "$scratch/lower.out"
python3 compile_full_c5_gate.py > "$scratch/compiler.out"

grep -q '^PASS-FULL-C5-INTEGER-SOURCE$' "$scratch/source.out"
grep -q '^PASS-LOWER-ACCEPTED-DIVERGENCE$' "$scratch/lower.out"
grep -q '^PASS-DISCOVERY-FULL-C5-GATE$' "$scratch/compiler.out"
(
  cd "$scratch"
  shasum -a 256 -c "$case_dir/EXPECTED_OUTPUT_SHA256.txt"
)
shasum -a 256 -c MANIFEST.sha256
printf '%s\n' 'PASS-AS-FONLY-D7-FULL-C5-GATE-ALL'
