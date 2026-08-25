#!/usr/bin/env bash
set -euo pipefail

# Cross-prime fixed-load routing control.  This is modular navigation only.

if [[ "$(uname -s)" != Linux ]]; then echo REFUSE_NON_LINUX >&2; exit 90; fi
if [[ ! -r /sys/class/dmi/id/sys_vendor ]] || \
   [[ "$(< /sys/class/dmi/id/sys_vendor)" != "Amazon EC2" ]]; then
  echo REFUSE_NON_AWS_EC2 >&2; exit 91
fi
: "${JC2_AWS_TAG:?set a unique max12_912_order3_d1_* tag}"
[[ "$JC2_AWS_TAG" =~ ^max12_912_order3_d1_[A-Za-z0-9_.-]+$ ]] || {
  echo REFUSE_UNREGISTERED_AWS_TAG >&2; exit 92;
}
: "${D1_GENERIC_SINGULAR:?set frozen generic Singular source}"
: "${D1_RUN_DIR:?set fresh /home/ubuntu/jobs/max12_912_order3_d1_* dir}"
[[ "$D1_RUN_DIR" == /home/ubuntu/jobs/max12_912_order3_d1_* ]] || {
  echo REFUSE_RUN_DIR >&2; exit 93;
}
[[ ! -e "$D1_RUN_DIR" ]] || { echo REFUSE_PREEXISTING_RUN_DIR >&2; exit 94; }
prime="${D1_PRIME:-65521}"
[[ "$prime" =~ ^[0-9]+$ ]] || { echo BAD_PRIME >&2; exit 95; }
for tool in Singular msolve sha256sum timeout; do
  command -v "$tool" >/dev/null || { echo "MISSING_TOOL=$tool" >&2; exit 96; }
done
[[ "$(grep -c '^poly R[1-8]=' "$D1_GENERIC_SINGULAR")" == 8 ]] || {
  echo BAD_GENERIC_ROW_COUNT >&2; exit 97;
}

mkdir "$D1_RUN_DIR"
hostname > "$D1_RUN_DIR/HOSTNAME"
printf '%s\n' "$JC2_AWS_TAG" > "$D1_RUN_DIR/AWS_TAG"
printf '%s\n' "$prime" > "$D1_RUN_DIR/PRIME"
cp "$D1_GENERIC_SINGULAR" "$D1_RUN_DIR/generic_source.sing"
{
  printf 'ring R=%s,(A0,A1,A2,A3,A4,A5,A6,A7),dp;\n' "$prime"
  printf 'option(redSB);\n'
  grep '^poly R[1-8]=' "$D1_GENERIC_SINGULAR" | \
    sed -E 's/\<s\>/2/g; s/\<k\>/1/g; s/\<mu\>/1/g; s/\<nu\>/1/g'
  for row in {1..8}; do printf 'print(R%d);\n' "$row"; done
} > "$D1_RUN_DIR/fixed_emit.sing"

/usr/bin/time -v -o "$D1_RUN_DIR/emit.time" \
  timeout 120 Singular -q "$D1_RUN_DIR/fixed_emit.sing" \
  > "$D1_RUN_DIR/fixed_polys.txt" 2> "$D1_RUN_DIR/emit.stderr"
emit_rc=$?
printf '%s\n' "$emit_rc" > "$D1_RUN_DIR/emit.rc"
[[ "$emit_rc" == 0 ]] || exit "$emit_rc"
[[ "$(wc -l < "$D1_RUN_DIR/fixed_polys.txt")" == 8 ]] || {
  echo BAD_EMITTED_ROW_COUNT >&2; exit 98;
}
{
  printf 'A0,A1,A2,A3,A4,A5,A6,A7\n%s\n' "$prime"
  awk '{ printf "%s%s\n", $0, (NR == 8 ? "" : ",") }' \
    "$D1_RUN_DIR/fixed_polys.txt"
} > "$D1_RUN_DIR/fixed.ms"
sha256sum "$D1_RUN_DIR/generic_source.sing" "$D1_RUN_DIR/fixed_emit.sing" \
  "$D1_RUN_DIR/fixed.ms" > "$D1_RUN_DIR/INPUTS.sha256"

set +e
/usr/bin/time -v -o "$D1_RUN_DIR/msolve.time" \
  timeout 1200 msolve -v 2 -g 2 -t 16 \
  -f "$D1_RUN_DIR/fixed.ms" -o "$D1_RUN_DIR/fixed_msolve.result" \
  > "$D1_RUN_DIR/msolve.stdout" 2> "$D1_RUN_DIR/msolve.stderr"
rc=$?
set -e
printf '%s\n' "$rc" > "$D1_RUN_DIR/msolve.rc"
sha256sum "$D1_RUN_DIR/msolve.stdout" "$D1_RUN_DIR/msolve.stderr" \
  "$D1_RUN_DIR/msolve.time" > "$D1_RUN_DIR/OUTPUTS.sha256"
[[ -f "$D1_RUN_DIR/fixed_msolve.result" ]] && \
  sha256sum "$D1_RUN_DIR/fixed_msolve.result" > "$D1_RUN_DIR/RESULT.sha256"
exit "$rc"
