#!/usr/bin/env bash
set -euo pipefail

# Navigation-only characteristic-32003 lane retaining s as the ninth variable.
# It probes the finite cover over the s-line at fixed (k,mu,nu)=(1,1,1).
# It is not a characteristic-zero section classifier.

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
: "${D1_GENERIC_SINGULAR:?set the frozen generic Singular source}"
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
[[ -f "$D1_GENERIC_SINGULAR" ]] || { echo MISSING_GENERIC_SOURCE >&2; exit 96; }
[[ "$(grep -c '^poly R[1-8]=' "$D1_GENERIC_SINGULAR")" == 8 ]] || {
  echo BAD_GENERIC_ROW_COUNT >&2
  exit 97
}

mkdir "$D1_RUN_DIR"
printf '%s\n' "$JC2_AWS_TAG" > "$D1_RUN_DIR/AWS_TAG"
hostname > "$D1_RUN_DIR/HOSTNAME"
date -u +%FT%TZ > "$D1_RUN_DIR/START_UTC"
cp "$D1_GENERIC_SINGULAR" "$D1_RUN_DIR/generic_source.sing"

{
  printf 'ring R=32003,(s,A0,A1,A2,A3,A4,A5,A6,A7),dp;\n'
  printf 'option(redSB);\n'
  grep '^poly R[1-8]=' "$D1_GENERIC_SINGULAR" | \
    sed -E 's/\<k\>/1/g; s/\<mu\>/1/g; s/\<nu\>/1/g'
} > "$D1_RUN_DIR/sretained_rows.sing"

cp "$D1_RUN_DIR/sretained_rows.sing" "$D1_RUN_DIR/sretained_emit.sing"
for row in {1..8}; do
  printf 'print(R%d);\n' "$row" >> "$D1_RUN_DIR/sretained_emit.sing"
done
/usr/bin/time -v -o "$D1_RUN_DIR/emit.time" \
  timeout 120 Singular -q "$D1_RUN_DIR/sretained_emit.sing" \
  > "$D1_RUN_DIR/sretained_polys.txt" 2> "$D1_RUN_DIR/emit.stderr"
emit_rc=$?
printf '%s\n' "$emit_rc" > "$D1_RUN_DIR/emit.rc"
[[ "$emit_rc" == 0 ]] || exit "$emit_rc"
[[ "$(wc -l < "$D1_RUN_DIR/sretained_polys.txt")" == 8 ]] || {
  echo BAD_EMITTED_ROW_COUNT >&2
  exit 98
}
{
  printf 's,A0,A1,A2,A3,A4,A5,A6,A7\n32003\n'
  awk '{ printf "%s%s\n", $0, (NR == 8 ? "" : ",") }' \
    "$D1_RUN_DIR/sretained_polys.txt"
} > "$D1_RUN_DIR/sretained.ms"

{
  cat "$D1_RUN_DIR/sretained_rows.sing"
  printf 'ideal I=R1,R2,R3,R4,R5,R6,R7,R8;\n'
  printf 'ideal G=slimgb(I);\n'
  printf 'print("PASS-D1-S-RETAINED-SLIMGB");\n'
  printf 'print("dimension="+string(dim(G)));\n'
  printf 'print("gb_size="+string(size(G)));\n'
  printf 'print("multiplicity="+string(mult(G)));\n'
} > "$D1_RUN_DIR/sretained_slimgb.sing"

sha256sum "$D1_RUN_DIR"/*.sing "$D1_RUN_DIR/sretained.ms" \
  > "$D1_RUN_DIR/INPUTS.sha256"

(
  set +e
  /usr/bin/time -v -o "$D1_RUN_DIR/msolve.time" \
    timeout 1800 msolve -v 2 -g 2 -t 16 \
    -f "$D1_RUN_DIR/sretained.ms" \
    -o "$D1_RUN_DIR/sretained_msolve.result" \
    > "$D1_RUN_DIR/msolve.stdout" 2> "$D1_RUN_DIR/msolve.stderr"
  rc=$?
  printf '%s\n' "$rc" > "$D1_RUN_DIR/msolve.rc"
) &
msolve_pid=$!
printf '%s\n' "$msolve_pid" > "$D1_RUN_DIR/msolve.pid"

(
  set +e
  /usr/bin/time -v -o "$D1_RUN_DIR/slimgb.time" \
    timeout 1800 Singular -q "$D1_RUN_DIR/sretained_slimgb.sing" \
    > "$D1_RUN_DIR/slimgb.stdout" 2> "$D1_RUN_DIR/slimgb.stderr"
  rc=$?
  printf '%s\n' "$rc" > "$D1_RUN_DIR/slimgb.rc"
) &
slimgb_pid=$!
printf '%s\n' "$slimgb_pid" > "$D1_RUN_DIR/slimgb.pid"

wait_rc=0
wait "$msolve_pid" || wait_rc=1
wait "$slimgb_pid" || wait_rc=1
for lane in msolve slimgb; do
  sha256sum "$D1_RUN_DIR/$lane.stdout" "$D1_RUN_DIR/$lane.stderr" \
    "$D1_RUN_DIR/$lane.time" > "$D1_RUN_DIR/$lane.OUTPUTS.sha256"
  [[ -f "$D1_RUN_DIR/sretained_msolve.result" ]] && \
    sha256sum "$D1_RUN_DIR/sretained_msolve.result" \
      > "$D1_RUN_DIR/msolve.RESULT.sha256"
done
date -u +%FT%TZ > "$D1_RUN_DIR/END_UTC"
printf '%s\n' "$wait_rc" > "$D1_RUN_DIR/RUNNER.rc"
exit "$wait_rc"
