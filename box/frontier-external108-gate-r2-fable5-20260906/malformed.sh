#!/bin/bash
# Malformed-input controls: every case must exit 2 with empty stdout.
G="$1"; fail=0
run() { out=$(python3 "$G" "$@" 2>/tmp/fable_r2_err); rc=$?; msg=$(head -c 120 /tmp/fable_r2_err | tr '\n' ' ' | sed 's/.*error: //'); printf '%s | rc=%s stdout_bytes=%s | %s\n' "$*" "$rc" "${#out}" "$msg"; if [ "$rc" != 2 ] || [ -n "$out" ]; then fail=1; fi; }
run --total-degrees 99 --tag t
run --total-degrees 99 66 --total-unbounded --tag t
run --partial-y-degrees 99 66 --tag t
run --total-cap 107 --total-degrees 99 66 --tag t
run --total-degrees abc 66 --tag t
run --total-degrees 99.5 66 --tag t
run --total-degrees 99 66
run --laurent-degrees 99 66 --tag t
run --total-cap 0 --tag t
run --total-degrees 0 66 --tag t
run --total-degrees 99 66 --purpose census --tag t
run --total-cap -108 --tag t
run
echo "malformed_all_rc2_empty_stdout=$([ $fail = 0 ] && echo yes || echo NO)"
