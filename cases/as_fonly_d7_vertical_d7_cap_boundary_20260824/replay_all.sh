#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$case_dir"

scratch=$(mktemp -d "${TMPDIR:-/tmp}/as-d7-cap-boundary.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM

if command -v Singular >/dev/null 2>&1; then
  singular_bin=$(command -v Singular)
elif command -v singular >/dev/null 2>&1; then
  singular_bin=$(command -v singular)
else
  printf '%s\n' 'Singular executable not found' >&2
  exit 69
fi

python3 audit_d7_source.py > "$scratch/source.out"
python3 audit_d7_joint.py > "$scratch/joint.out"
"$singular_bin" -q audit_boundary_containment.sing > "$scratch/boundary.out"
"$singular_bin" -q audit_hzero_minass.sing > "$scratch/hzero.out"
"$singular_bin" -q audit_hgeneric_minass.sing > "$scratch/hgeneric.out"

grep -q '^PASS-D7-INTEGER-SOURCE-AUDIT$' "$scratch/source.out"
grep -q '^PASS-D7-JOINT-CENSUS-CONTROLS$' "$scratch/joint.out"
grep -q '^PASS-D7-BOUNDARY-DIRECT$' "$scratch/boundary.out"
grep -q '^PASS-D7-HZERO$' "$scratch/hzero.out"
grep -q '^PASS-D7-HGENERIC-BASE-SL$' "$scratch/hgeneric.out"

(
  cd "$scratch"
  shasum -a 256 -c "$case_dir/EXPECTED_OUTPUT_SHA256.txt"
)
shasum -a 256 -c MANIFEST.sha256
shasum -a 256 "$scratch/source.out" "$scratch/joint.out" \
  "$scratch/boundary.out" "$scratch/hzero.out" "$scratch/hgeneric.out"
printf '%s\n' 'PASS-AS-FONLY-D7-CAP-BOUNDARY-ALL'
