#!/usr/bin/env bash
set -euo pipefail

here=$(cd -- "$(dirname -- "$0")" && pwd)
replay_dir=$(mktemp -d "$here/.replay.XXXXXX")
trap 'rm -rf -- "$replay_dir"' EXIT

audit_tmp="$replay_dir/run_audit.tsv"
printf 'stem\texit\twall_ms\tstdout_match\tstderr_match\tstderr_empty\trecurrence_pass\tbrcr_done\tdriver_done\tbad_markers\tstd_calls\tsource_sha256\tstdout_sha256\tmetadata_sha256\n' > "$audit_tmp"

failed=0
for stem in \
  brcr_t2_split_b0 \
  brcr_t2_split_b1 \
  brcr_t3_exact \
  brcr_t4_exact \
  brcr_t5_exact \
  brcr_t6_exact
do
  source_file="$here/$stem.sing"
  stored_out="$here/$stem.out"
  stored_err="$here/$stem.err"
  metadata_file="$here/$stem.json"
  fresh_out="$replay_dir/$stem.out"
  fresh_err="$replay_dir/$stem.err"

  start_ns=$(date +%s%N)
  set +e
  timeout 1200 stdbuf -oL Singular -q "$source_file" > "$fresh_out" 2> "$fresh_err"
  exit_code=$?
  set -e
  end_ns=$(date +%s%N)
  wall_ms=$(( (end_ns - start_ns) / 1000000 ))

  stdout_match=false
  stderr_match=false
  stderr_empty=false
  cmp -s "$fresh_out" "$stored_out" && stdout_match=true
  cmp -s "$fresh_err" "$stored_err" && stderr_match=true
  test ! -s "$fresh_err" && stderr_empty=true
  recurrence_pass=$(grep -Ec '^RECURRENCE_PASS([[:space:]]|$)' "$fresh_out" || true)
  brcr_done=$(grep -xc 'BRCR_DONE' "$fresh_out" || true)
  driver_done=$(grep -xc 'DRIVER_DONE' "$fresh_out" || true)
  bad_markers=$(grep -Eic '(^|[[:space:]])FAIL([[:space:]]|$)|error occurred|div\. by 0' "$fresh_out" || true)
  std_calls=$(grep -Eic '(^|[^[:alnum:]_])(std|slimgb|groebner)[[:space:]]*\(' "$source_file" || true)
  source_hash=$(sha256sum "$source_file" | cut -d' ' -f1)
  stdout_hash=$(sha256sum "$fresh_out" | cut -d' ' -f1)
  metadata_hash=$(sha256sum "$metadata_file" | cut -d' ' -f1)

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$stem" "$exit_code" "$wall_ms" "$stdout_match" "$stderr_match" \
    "$stderr_empty" "$recurrence_pass" "$brcr_done" "$driver_done" \
    "$bad_markers" "$std_calls" "$source_hash" "$stdout_hash" "$metadata_hash" \
    >> "$audit_tmp"

  if test "$exit_code" -ne 0 \
    || test "$stdout_match" != true \
    || test "$stderr_match" != true \
    || test "$stderr_empty" != true \
    || test "$recurrence_pass" -ne 1 \
    || test "$brcr_done" -ne 1 \
    || test "$driver_done" -ne 1 \
    || test "$bad_markers" -ne 0 \
    || test "$std_calls" -ne 0
  then
    failed=1
  fi
done

mv -- "$audit_tmp" "$here/run_audit.tsv"
cat "$here/run_audit.tsv"
exit "$failed"
