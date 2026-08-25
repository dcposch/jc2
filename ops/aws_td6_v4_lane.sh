#!/usr/bin/env bash
set -uo pipefail

TD6_ROOT=$1
TD6_RUN=$2
TD6_NAME=$3
shift 3

TD6_PYTHON=/home/ubuntu/venvs/td6/bin/python
TD6_START=$(date -u +%Y-%m-%dT%H:%M:%SZ)

cd "$TD6_ROOT" || exit 125
{
  printf 'lane=%s\n' "$TD6_NAME"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$TD6_START"
  printf 'python=%s\n' "$($TD6_PYTHON --version 2>&1)"
  printf 'argv='
  printf '%q ' "$TD6_PYTHON" "$@"
  printf '\n'
} > "$TD6_RUN/$TD6_NAME.meta"

set +e
timeout 43200 "$TD6_PYTHON" "$@" \
  > "$TD6_RUN/$TD6_NAME.stdout" \
  2> "$TD6_RUN/$TD6_NAME.stderr"
TD6_RC=$?
set -e

TD6_END=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  printf 'end_utc=%s\n' "$TD6_END"
  printf 'rc=%s\n' "$TD6_RC"
  printf 'stdout_sha256=%s\n' "$(sha256sum "$TD6_RUN/$TD6_NAME.stdout" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$TD6_RUN/$TD6_NAME.stderr" | cut -d ' ' -f 1)"
} >> "$TD6_RUN/$TD6_NAME.meta"
printf '%s lane=%s rc=%s\n' "$TD6_END" "$TD6_NAME" "$TD6_RC" >> "$TD6_RUN/lanes.log"
exit "$TD6_RC"
