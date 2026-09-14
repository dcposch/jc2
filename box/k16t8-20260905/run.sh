#!/bin/bash
# usage: run.sh <script.sing> <timeout_seconds>   (foreground, line-buffered, records wall time and exit code)
f="$1"; T="${2:-600}"; stem="${f%.sing}"
start=$(date +%s)
stdbuf -oL timeout "$T" Singular -q "$f" > "$stem.out" 2> "$stem.err"
rc=$?
end=$(date +%s)
echo "exit=$rc wall=$((end-start))s timeout=$T" > "$stem.time"
echo "$stem exit=$rc wall=$((end-start))s"
