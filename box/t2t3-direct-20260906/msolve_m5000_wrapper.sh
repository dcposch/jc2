#!/usr/bin/env bash
# Narrow launch adapter for the worker-built msolve 0.10.1 parser repair.
# run_worker_capped.sh supplies the input, output, threads, seed, and verbosity;
# this adapter only bounds F4 pair selection per matrix.
set -Eeuo pipefail
exec /tmp/msolve-patched/bin/msolve -m 5000 "$@"
