#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
scratch=$(mktemp -d "${TMPDIR:-/tmp}/as-binary-top3.XXXXXX")
trap 'rm -rf "$scratch"' EXIT HUP INT TERM

python3 "$case_dir/replay.py" > "$scratch/replay.out"
cmp "$case_dir/EXPECTED_OUTPUT.txt" "$scratch/replay.out"
(
  cd "$case_dir"
  shasum -a 256 -c MANIFEST.sha256
)
printf '%s\n' 'PASS-AS-FONLY-BINARY-TOP3-ALL'
