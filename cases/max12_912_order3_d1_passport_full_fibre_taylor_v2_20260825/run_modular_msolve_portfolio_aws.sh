#!/usr/bin/env bash
set -euo pipefail

# Navigation-only finite-field engine race for the frozen D1 row system.
# The caller supplies the already emitted fixed-specialization Singular files.
# This runner never promotes a characteristic-zero or geometric claim.

if [[ "$(uname -s)" != Linux ]]; then
  echo REFUSE_NON_LINUX >&2
  exit 90
fi
if [[ ! -r /sys/class/dmi/id/sys_vendor ]] || \
   [[ "$(< /sys/class/dmi/id/sys_vendor)" != "Amazon EC2" ]]; then
  echo REFUSE_NON_AWS_EC2 >&2
  exit 91
fi
: "${JC2_AWS_TAG:?set a unique max12_912_order3_d1_* AWS tag}"
if [[ ! "$JC2_AWS_TAG" =~ ^max12_912_order3_d1_[A-Za-z0-9_.-]+$ ]]; then
  echo REFUSE_UNREGISTERED_AWS_TAG >&2
  exit 92
fi
: "${D1_SPEC_DIR:?set directory containing spec_LABEL.sing files}"
: "${D1_RUN_DIR:?set a fresh /home/ubuntu/jobs/max12_912_order3_d1_* run dir}"
if [[ "$D1_RUN_DIR" != /home/ubuntu/jobs/max12_912_order3_d1_* ]]; then
  echo REFUSE_RUN_DIR >&2
  exit 93
fi
if [[ -e "$D1_RUN_DIR" ]]; then
  echo REFUSE_PREEXISTING_RUN_DIR >&2
  exit 94
fi
for tool in Singular msolve sha256sum timeout; do
  command -v "$tool" >/dev/null || { echo "MISSING_TOOL=$tool" >&2; exit 95; }
done

labels=(g1 g2 mu0 nu0 both0)
mkdir "$D1_RUN_DIR"
printf '%s\n' "$JC2_AWS_TAG" > "$D1_RUN_DIR/AWS_TAG"
hostname > "$D1_RUN_DIR/HOSTNAME"
date -u +%FT%TZ > "$D1_RUN_DIR/START_UTC"

for label in "${labels[@]}"; do
  source_file="$D1_SPEC_DIR/spec_${label}.sing"
  [[ -f "$source_file" ]] || { echo "MISSING_SOURCE=$source_file" >&2; exit 96; }
  cp "$source_file" "$D1_RUN_DIR/spec_${label}.sing"
  sed '/^ideal I=/,$d' "$source_file" > "$D1_RUN_DIR/spec_${label}_emit.sing"
  for row in {1..8}; do
    printf 'print(R%d);\n' "$row" >> "$D1_RUN_DIR/spec_${label}_emit.sing"
  done
  /usr/bin/time -v -o "$D1_RUN_DIR/spec_${label}_emit.time" \
    timeout 120 Singular -q "$D1_RUN_DIR/spec_${label}_emit.sing" \
    > "$D1_RUN_DIR/spec_${label}_polys.txt" \
    2> "$D1_RUN_DIR/spec_${label}_emit.stderr"
  emit_rc=$?
  printf '%s\n' "$emit_rc" > "$D1_RUN_DIR/spec_${label}_emit.rc"
  [[ "$emit_rc" == 0 ]] || exit "$emit_rc"
  [[ "$(wc -l < "$D1_RUN_DIR/spec_${label}_polys.txt")" == 8 ]] || {
    echo "BAD_POLY_LINE_COUNT=$label" >&2
    exit 97
  }
  {
    printf 'A0,A1,A2,A3,A4,A5,A6,A7\n32003\n'
    awk '{ printf "%s%s\n", $0, (NR == 8 ? "" : ",") }' \
      "$D1_RUN_DIR/spec_${label}_polys.txt"
  } > "$D1_RUN_DIR/spec_${label}.ms"
done

sha256sum "$D1_RUN_DIR"/spec_*.sing "$D1_RUN_DIR"/spec_*.ms \
  > "$D1_RUN_DIR/INPUTS.sha256"

# Optional exact generation control against the earlier g1 input.
if [[ -n "${D1_G1_REFERENCE_MS:-}" ]]; then
  cmp "$D1_RUN_DIR/spec_g1.ms" "$D1_G1_REFERENCE_MS" || {
    echo FAIL_G1_GENERATION_REFERENCE >&2
    exit 98
  }
  sha256sum "$D1_G1_REFERENCE_MS" > "$D1_RUN_DIR/G1_REFERENCE.sha256"
fi

for label in g2 mu0 nu0 both0; do
  (
    set +e
    start="$(date -u +%FT%TZ)"
    /usr/bin/time -v -o "$D1_RUN_DIR/${label}.time" \
      timeout 1200 msolve -v 2 -g 2 -t 12 \
      -f "$D1_RUN_DIR/spec_${label}.ms" \
      -o "$D1_RUN_DIR/spec_${label}_msolve.result" \
      > "$D1_RUN_DIR/${label}.stdout" \
      2> "$D1_RUN_DIR/${label}.stderr"
    rc=$?
    end="$(date -u +%FT%TZ)"
    {
      printf 'label=%s\n' "$label"
      printf 'host=%s\n' "$(hostname)"
      printf 'start_utc=%s\n' "$start"
      printf 'end_utc=%s\n' "$end"
      printf 'rc=%s\n' "$rc"
      sha256sum "$D1_RUN_DIR/spec_${label}.ms" \
        "$D1_RUN_DIR/${label}.stdout" "$D1_RUN_DIR/${label}.stderr"
      [[ -f "$D1_RUN_DIR/spec_${label}_msolve.result" ]] && \
        sha256sum "$D1_RUN_DIR/spec_${label}_msolve.result"
    } > "$D1_RUN_DIR/${label}.meta"
    printf '%s\n' "$rc" > "$D1_RUN_DIR/${label}.rc"
    exit "$rc"
  ) &
  printf '%s\n' "$!" > "$D1_RUN_DIR/${label}.pid"
done

wait_rc=0
for label in g2 mu0 nu0 both0; do
  if ! wait "$(< "$D1_RUN_DIR/${label}.pid")"; then
    wait_rc=1
  fi
done
date -u +%FT%TZ > "$D1_RUN_DIR/END_UTC"
printf '%s\n' "$wait_rc" > "$D1_RUN_DIR/PORTFOLIO.rc"
exit "$wait_rc"
