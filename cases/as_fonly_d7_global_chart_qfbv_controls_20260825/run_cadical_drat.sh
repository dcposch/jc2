#!/usr/bin/env bash
set -euo pipefail
: "${INPUT_DIMACS:?}"
: "${OUTPUT_DRAT:?}"
: "${CADICAL_STDOUT:?}"
: "${CADICAL_STDERR:?}"
set +e
/usr/bin/time -v cadical --no-binary "$INPUT_DIMACS" "$OUTPUT_DRAT" \
  >"$CADICAL_STDOUT" 2>"$CADICAL_STDERR"
rc=$?
set -e
if [[ "$rc" -ne 20 ]]; then
  printf 'FAIL-CADICAL-RC-%s\n' "$rc" >&2
  exit 1
fi
grep -q '^s UNSATISFIABLE$' "$CADICAL_STDOUT"
printf 'PASS-AS-GLOBAL-CHART-CADICAL-DRAT\n'

