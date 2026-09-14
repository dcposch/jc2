#!/usr/bin/env bash
# Run a source-complete native builder (y-first builder_fix ring) and demand NATIVE_DONE.
# Usage: extract_native.sh CLASS_DIR BUILDER_SING TIMEOUT_S
set -u
CLASS_DIR=$1; BUILDER=$2; LIMIT=${3:-3600}
mkdir -p "$CLASS_DIR/rows" "$CLASS_DIR/extract"
cd "$CLASS_DIR"
echo "EXTRACT_START builder=$BUILDER cwd=$CLASS_DIR utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "builder_sha=$(sha256sum "$BUILDER")"
timeout --signal=TERM --kill-after=30s "${LIMIT}s" \
  /usr/bin/time -v Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc "$BUILDER" \
  > extract/builder.stdout 2> extract/builder.stderr
rc=$?
echo "$rc" > extract/builder.rc
echo "EXTRACT_RC=$rc utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
tail -20 extract/builder.stdout || true
rows=$(ls -1 rows/*_rows.tsv 2>/dev/null | head -1 || true)
if [[ -n "$rows" ]]; then
  echo "rows_file=$rows lines=$(wc -l < "$rows") bytes=$(stat -c %s "$rows") sha=$(sha256sum "$rows")"
fi
grep -E 'NATIVE_DONE|NATIVE_FAIL|NATIVE_GATE' extract/builder.stdout || true
exit $rc
