#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
scratch_dir=$(mktemp -d "${TMPDIR:-/tmp}/as-fonly-d98-corrected.XXXXXX")
trap 'rm -rf "$scratch_dir"' EXIT HUP INT TERM

cd "$case_dir"

python3 audit_corrected_frobenius_rows.py
python3 replay_next_carry_controls.py
python3 reconstruct_representatives.py

python3 generate_corrected.py > "$scratch_dir/vertical.sing"
singular -q audit_vertical_d9_section.sing
singular -q audit_vertical_core_rank.sing
singular -q "$scratch_dir/vertical.sing" > "$scratch_dir/vertical-singular.out"
grep 'PASS-VERTICAL-D98-CORE' "$scratch_dir/vertical-singular.out"

STRUCTURAL=1 python3 generate_corrected.py > "$scratch_dir/vertical-structural.out"
grep -A 9 '^STRUCTURAL-VERTICAL-D98$' "$scratch_dir/vertical-structural.out"

BRANCH=g STRUCTURAL=1 python3 generate_corrected.py > "$scratch_dir/g-structural.out"
grep -A 9 '^STRUCTURAL-G-ENDPOINT-D98$' "$scratch_dir/g-structural.out"

ENUMERATE=1 python3 generate_corrected.py > "$scratch_dir/vertical-enumeration.out"
grep -A 10 '^ENUM-VERTICAL-D98$' "$scratch_dir/vertical-enumeration.out"

BRANCH=g ENUMERATE=1 python3 generate_corrected.py > "$scratch_dir/g-enumeration.out"
grep -A 10 '^ENUM-G-ENDPOINT-D98$' "$scratch_dir/g-enumeration.out"

shasum -a 256 -c MANIFEST.sha256
printf '%s\n' 'PASS-CORRECTED-POST-D10-D98-ALL'
