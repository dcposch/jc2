#!/usr/bin/env bash
set -uo pipefail

AWS_ROOT=$1
AWS_RUN=$2
AWS_NAME=$3
shift 3
AWS_START=$(date -u +%Y-%m-%dT%H:%M:%SZ)

cd "$AWS_ROOT" || exit 125
{
  printf 'lane=%s\n' "$AWS_NAME"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$AWS_START"
  printf 'argv='
  printf '%q ' "$@"
  printf '\n'
} > "$AWS_RUN/$AWS_NAME.meta"

set +e
timeout 43200 /usr/bin/time -v "$@" \
  > "$AWS_RUN/$AWS_NAME.stdout" \
  2> "$AWS_RUN/$AWS_NAME.stderr"
AWS_RC=$?
set -e

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$AWS_RC"
  printf 'stdout_sha256=%s\n' "$(sha256sum "$AWS_RUN/$AWS_NAME.stdout" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$AWS_RUN/$AWS_NAME.stderr" | cut -d ' ' -f 1)"
} >> "$AWS_RUN/$AWS_NAME.meta"
printf '%s lane=%s rc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$AWS_NAME" "$AWS_RC" \
  >> "$AWS_RUN/lanes.log"
exit "$AWS_RC"
