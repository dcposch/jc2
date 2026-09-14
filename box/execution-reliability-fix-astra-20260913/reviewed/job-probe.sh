#!/usr/bin/env bash
# No CAS. AWS-only fixture invoked only by the guarded job service.
set -eu
case ${1:?fixture mode} in
  first)
    printf 'FIRST_STDOUT\n'
    printf 'FIRST_DIAGNOSTIC\n' >&2
    printf 'partial evidence\n' > partial.txt
    printf '%s\n' "${2:-no extra argument}" > literal-argument.txt
    ;;
  second)
    test "$(< partial.txt)" = 'partial evidence'
    printf 'SECOND_RAN\n' > second.txt
    ;;
  fail)
    printf 'PARTIAL_BEFORE_EXIT17\n' > partial.txt
    printf 'EXIT17_STDOUT\n'
    printf 'VISIBLE_EXPECTED_FAILURE_17\n' >&2
    exit 17
    ;;
  timeout)
    printf 'TIMEOUT_PARTIAL\n' > partial.txt
    /usr/bin/setsid /usr/bin/bash -c '
      trap "" TERM
      printf "%s\n" "$$" > stubborn.pid
      cat /proc/$$/cgroup /proc/$$/status > stubborn.identity
      printf "STUBBORN_READY\n" >&2
      while :; do sleep 1; done
    ' &
    wait
    ;;
  kill-controller)
    printf 'KILL_PARTIAL\n' > partial.txt
    printf 'ABOUT_TO_KILL_CONTROLLER\n' >&2
    sync -f partial.txt
    kill -KILL "$PPID"
    while :; do sleep 1; done
    ;;
  *) printf 'unknown fixture\n' >&2; exit 64 ;;
esac
