#!/usr/bin/env bash
set -uo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing heavy lane outside AWS: host=$(hostname) os=$(uname -s)" >&2
  exit 125
fi

AWS_VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$AWS_VENDOR" != "Amazon EC2" ]]; then
  echo "refusing heavy lane outside AWS EC2: host=$(hostname) vendor=${AWS_VENDOR:-unknown}" >&2
  exit 125
fi

if (( $# < 4 )); then
  echo "usage: $0 AWS_ROOT AWS_RUN REGISTERED_LANE_TAG COMMAND [ARG ...]" >&2
  exit 125
fi

AWS_ROOT=$1
AWS_RUN=$2
AWS_NAME=$3
shift 3
if [[ -z "$AWS_ROOT" || -z "$AWS_RUN" || -z "$AWS_NAME" ]]; then
  echo "refusing unregistered heavy lane: root, run directory, and lane tag are required" >&2
  exit 125
fi
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
