#!/usr/bin/env bash
set -u

if (( $# < 6 )); then
    echo "usage: $0 BINARY INPUT OUTPUT_PREFIX TIMEOUT_SECONDS THREADS VM_LIMIT_KIB [MSOLVE_OPTIONS ...]" >&2
    exit 64
fi

binary=$1
input=$2
prefix=$3
timeout_seconds=$4
threads=$5
vm_limit_kib=$6
shift 6

mkdir -p "$(dirname "$prefix")"

{
    printf 'started_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'hostname=%s\n' "$(hostname)"
    printf 'binary=%s\n' "$binary"
    printf 'binary_version=%s\n' "$($binary -V 2>&1 | head -n 1)"
    printf 'binary_sha256=%s\n' "$(sha256sum "$binary" | awk '{print $1}')"
    printf 'input=%s\n' "$input"
    printf 'input_sha256=%s\n' "$(sha256sum "$input" | awk '{print $1}')"
    printf 'timeout_seconds=%s\n' "$timeout_seconds"
    printf 'threads=%s\n' "$threads"
    printf 'vm_limit_kib=%s\n' "$vm_limit_kib"
    printf 'msolve_options='
    printf '%q ' "$@"
    printf '\n'
} >"${prefix}.meta"

ulimit -v "$vm_limit_kib"
set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s "${timeout_seconds}s" \
    nice -n 15 "$binary" -g 2 -t "$threads" -v 2 "$@" \
    -f "$input" -o "${prefix}.out" \
    >"${prefix}.stdout" 2>"${prefix}.stderr"
rc=$?
set -e

printf '%s\n' "$rc" >"${prefix}.rc"
{
    printf 'finished_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf 'return_code=%s\n' "$rc"
    if [[ -f ${prefix}.out ]]; then
        printf 'output_sha256=%s\n' "$(sha256sum "${prefix}.out" | awk '{print $1}')"
    fi
} >>"${prefix}.meta"

exit "$rc"
