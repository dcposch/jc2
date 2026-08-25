#!/usr/bin/env bash
set -uo pipefail

AS_ROOT=/home/ubuntu/as_fonly_d7_vertical_next_top_carry_20260824
AS_TAG=as_d7_next_top_$(date -u +%Y%m%dT%H%M%SZ)
AS_RUN=$AS_ROOT/runs/$AS_TAG
mkdir -p "$AS_RUN"
cd "$AS_ROOT" || exit 125
export JC2_ROOT=/home/ubuntu

sha256sum -c RUNNER_MANIFEST.sha256 \
  > "$AS_RUN/source_verify.stdout" \
  2> "$AS_RUN/source_verify.stderr" || exit 126
find \
  /home/ubuntu/cases/as_fonly_d7_degree10_pointwise_20260824 \
  /home/ubuntu/cases/as_fonly_d7_postd10_d98_f3_corrected_20260824 \
  /home/ubuntu/cases/as_fonly_d7_vertical_d7_source_license_20260824 \
  /home/ubuntu/cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824 \
  /home/ubuntu/cases/as_fonly_d7_vertical_next_cartier_20260824 \
  -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum \
  > "$AS_RUN/source_closure.sha256"
{
  printf 'tag=%s\n' "$AS_TAG"
  printf 'host=%s\n' "$(hostname)"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'python=%s\n' "$(python3 --version 2>&1)"
  printf 'compiler_sha256=%s\n' '1fc18eeb80ad3ae3b8c498fe5548e9adda423df1df60237077e0df6ef5e30d44'
  printf 'runner_manifest_sha256=%s\n' 'b5862a84741f47b21d77277421a23ed9baed32204b0cbee21ea686e4a7f097bb'
  printf 'virtual_memory_limit_kib=%s\n' '16777216'
  printf 'timeout_seconds=%s\n' '43200'
} > "$AS_RUN/run.meta"

ulimit -v 16777216
set +e
timeout 43200 /usr/bin/time -v python3 compile_next_top_carry.py \
  > "$AS_RUN/run.stdout" \
  2> "$AS_RUN/run.stderr"
AS_RC=$?
set -e

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$AS_RC"
  printf 'stdout_sha256=%s\n' "$(sha256sum "$AS_RUN/run.stdout" | cut -d ' ' -f 1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$AS_RUN/run.stderr" | cut -d ' ' -f 1)"
} >> "$AS_RUN/run.meta"
printf '%s rc=%s run=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$AS_RC" "$AS_RUN" >> "$AS_ROOT/lanes.log"
exit "$AS_RC"
