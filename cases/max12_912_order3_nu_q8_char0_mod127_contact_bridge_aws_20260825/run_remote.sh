#!/bin/sh
set -eu

repo=${1:?repository root required}
out_root=${2:?output root required}
tag=${3:?tag required}
case_dir="$repo/cases/max12_912_order3_nu_q8_char0_mod127_contact_bridge_aws_20260825"
out="$out_root/$tag"
mkdir -p "$out"

printf 'host=%s\nstarted_utc=%s\ntag=%s\n' "$(hostname)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$tag" > "$out/run.meta"
sha256sum "$case_dir/producer.py" "$case_dir/independent_replay.py" "$case_dir/run_remote.sh" > "$out/source.sha256"

set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s 1800 \
  python3 "$case_dir/producer.py" > "$out/producer.json" 2> "$out/producer.stderr"
producer_rc=$?
set -e
printf '%s\n' "$producer_rc" > "$out/producer.rc"
if [ "$producer_rc" -ne 0 ]; then
  printf 'status=FAIL_PRODUCER\nfinished_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$out/run.meta"
  exit "$producer_rc"
fi

set +e
/usr/bin/time -v timeout --signal=TERM --kill-after=30s 600 \
  python3 "$case_dir/independent_replay.py" "$out/producer.json" \
  > "$out/replay.json" 2> "$out/replay.stderr"
replay_rc=$?
set -e
printf '%s\n' "$replay_rc" > "$out/replay.rc"
if [ "$replay_rc" -ne 0 ]; then
  printf 'status=FAIL_REPLAY\nfinished_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$out/run.meta"
  exit "$replay_rc"
fi

sha256sum "$out/producer.json" "$out/replay.json" "$out/producer.stderr" "$out/replay.stderr" > "$out/output.sha256"
printf 'status=PASS\nfinished_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$out/run.meta"
printf '0\n' > "$out/runner.rc"
