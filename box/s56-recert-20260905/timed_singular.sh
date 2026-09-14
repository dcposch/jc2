#!/bin/bash
set -u
if [[ -n "${S56_CPU:-}" ]]; then
  exec /usr/bin/time -v /usr/bin/taskset -c "$S56_CPU" /usr/bin/Singular "$@"
fi
exec /usr/bin/time -v /usr/bin/Singular "$@"
