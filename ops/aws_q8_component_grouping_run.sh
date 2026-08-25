#!/usr/bin/env bash
set -uo pipefail

if [ "$#" -ne 3 ]; then
  printf 'usage: %s <prime> <saturation|grouping> <std|slimgb>\n' "$0" >&2
  exit 2
fi

Q8_PRIME=$1
Q8_MODE=$2
Q8_ENGINE=$3
case "$Q8_PRIME" in
  ''|*[!0-9]*) exit 2 ;;
esac
case "$Q8_MODE" in saturation|grouping) ;; *) exit 2 ;; esac
case "$Q8_ENGINE" in std|slimgb) ;; *) exit 2 ;; esac

Q8_ROOT=/home/ubuntu/q8_component_grouping_20260824/jc2
Q8_CASE=$Q8_ROOT/cases/max12_912_order3_nu_q8_component_grouping_aws_20260824
Q8_TAG=q8_group_${Q8_MODE}_p${Q8_PRIME}_${Q8_ENGINE}_$(date -u +%Y%m%dT%H%M%SZ)
Q8_RUN=$Q8_ROOT/runs/$Q8_TAG
mkdir -p "$Q8_RUN"
cd "$Q8_ROOT" || exit 125

{
  printf 'tag=%s\n' "$Q8_TAG"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'prime=%s\n' "$Q8_PRIME"
  printf 'mode=%s\n' "$Q8_MODE"
  printf 'engine=%s\n' "$Q8_ENGINE"
  printf 'generator_sha256=%s\n' '1165b270f3fe7ffe7796a9a1eca452a495daf858c67ae525a45af0e9bbd67ac5'
  printf 'compiler_sha256=%s\n' '22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545'
  printf 'parent_manifest_sha256=%s\n' '3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4'
  printf 'virtual_memory_limit_kib=%s\n' '268435456'
  printf 'timeout_seconds=%s\n' '43200'
  printf 'singular=%s\n' "$(/usr/bin/Singular --version | head -1)"
} > "$Q8_RUN/run.meta"

python3 "$Q8_CASE/generate.py" \
  --prime "$Q8_PRIME" --mode "$Q8_MODE" --engine "$Q8_ENGINE" \
  > "$Q8_RUN/input.sing" 2> "$Q8_RUN/generator.stderr" || exit 126
printf 'input_sha256=%s\n' "$(sha256sum "$Q8_RUN/input.sing" | cut -d ' ' -f 1)" \
  >> "$Q8_RUN/run.meta"

ulimit -v 268435456
set +e
timeout 43200 /usr/bin/time -v /usr/bin/Singular -q \
  < "$Q8_RUN/input.sing" \
  > "$Q8_RUN/result.out" \
  2> "$Q8_RUN/stderr.log"
Q8_RC=$?
set -e

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$Q8_RC"
  printf 'result_sha256=%s\n' "$(sha256sum "$Q8_RUN/result.out" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$Q8_RUN/stderr.log" | cut -d ' ' -f 1)"
} >> "$Q8_RUN/run.meta"
printf '%s mode=%s prime=%s rc=%s run=%s\n' \
  "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$Q8_MODE" "$Q8_PRIME" "$Q8_RC" "$Q8_RUN" \
  >> "$Q8_ROOT/lanes.log"
exit "$Q8_RC"
