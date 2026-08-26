#!/usr/bin/env bash
set -euo pipefail

test "$#" -eq 2
base=$1
host_label=$2
source_dir="$base/source/payload"
test "$(uname -s)" = Linux
test -x "$source_dir/run_v78c_shard.sh"

exponents=(2 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 21 22 23 24)
: > "$base/launch_ledger.tsv"
printf 'exponent\tpid\ttag\trun_dir\n' >> "$base/launch_ledger.tsv"
for exponent in "${exponents[@]}"; do
  run="$base/q${exponent}"
  tag="td6_v78c_${host_label}_q${exponent}_20260826T0030Z"
  mkdir -p "$run/output"
  nohup env \
    RUN_DIR="$run" \
    SOURCE_DIR="$source_dir" \
    RUN_TAG="$tag" \
    Q_EXPONENT="$exponent" \
    bash -lc '
      set -o pipefail
      ulimit -v 12582912
      cd "$SOURCE_DIR"
      export PATH=/home/ubuntu/venvs/td6/bin:$PATH
      export TD6_REGISTERED_AWS_TAG="$RUN_TAG"
      export TD6_Q_EXPONENT="$Q_EXPONENT"
      export TD6_OUTPUT_DIR="$RUN_DIR/output"
      {
        printf "tag=%s\n" "$RUN_TAG"
        printf "hostname=%s\n" "$(hostname)"
        printf "exponent=%s\n" "$Q_EXPONENT"
        printf "start_utc=%s\n" "$(date -u +%FT%TZ)"
        printf "source_archive_sha256=%s\n" \
          "b566a57ea50c3f4d24c091f006fe321aa9bb813368049773ee89b347d1284be4"
        printf "virtual_memory_cap_kib=12582912\n"
        printf "timeout_seconds=14400\n"
      } > "$RUN_DIR/launch.meta"
      /usr/bin/time -v timeout 14400 ./run_v78c_shard.sh \
        > "$RUN_DIR/stdout" 2> "$RUN_DIR/stderr"
      rc=$?
      printf "%s\n" "$rc" > "$RUN_DIR/rc"
      {
        printf "finish_utc=%s\n" "$(date -u +%FT%TZ)"
        printf "rc=%s\n" "$rc"
      } > "$RUN_DIR/finish.meta"
      exit "$rc"
    ' </dev/null > "$run/nohup.log" 2>&1 &
  pid=$!
  printf '%s\n' "$pid" > "$run/shell.pid"
  printf '%s\t%s\t%s\t%s\n' "$exponent" "$pid" "$tag" "$run" \
    >> "$base/launch_ledger.tsv"
done

cat "$base/launch_ledger.tsv"

