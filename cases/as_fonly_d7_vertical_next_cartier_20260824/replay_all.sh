#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$case_dir"
scratch=$(mktemp -d "${TMPDIR:-/tmp}/as-d7-next-cartier.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM

python3 audit_next_cartier_source.py > "$scratch/source.out"
python3 compile_next_cartier.py > "$scratch/compiler.out"
grep -q '^PASS-NEXT-CARTIER-INTEGER-SOURCE$' "$scratch/source.out"
grep -q '^PASS-NEXT-CARTIER-COMPILER$' "$scratch/compiler.out"
(
  cd "$scratch"
  shasum -a 256 -c "$case_dir/EXPECTED_OUTPUT_SHA256.txt"
)
shasum -a 256 -c MANIFEST.sha256
printf '%s\n' 'PASS-AS-FONLY-D7-NEXT-CARTIER-ALL'
