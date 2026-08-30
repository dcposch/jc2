#!/usr/bin/env bash
# Fail-closed AWS runner for the R4-00 base-decide packets.
#
# usage: run_r4_00_base_decide.sh PACKET_DIR RUN_DIR JOB
#   JOB in { r2 | r1p | r1m | msolve:<shardfile.ms> }
#
# Refuses to run off Linux/EC2 or without a registered lane tag.  Verifies
# the packet manifest, then records host identity (hostname, DMI vendor,
# product, EC2 asset tag = instance id), UTC start/end, tool versions, argv,
# input hashes, /usr/bin/time -v resource use, return code, and output
# hashes into RUN_DIR/<job>.meta.  Every Singular invocation closes stdin
# and the scripts terminate with explicit quit;.
set -uo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing: not Linux (host=$(hostname))" >&2; exit 125
fi
VENDOR=$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null || true)
if [[ "$VENDOR" != "Amazon EC2" ]]; then
  echo "refusing: DMI vendor '$VENDOR' is not Amazon EC2" >&2; exit 125
fi
if [[ -z "${JC2_REGISTERED_AWS_LANE:-}" ]]; then
  echo "refusing: JC2_REGISTERED_AWS_LANE is mandatory" >&2; exit 125
fi
if (( $# != 3 )); then
  echo "usage: $0 PACKET_DIR RUN_DIR JOB" >&2; exit 125
fi
PACKET=$(readlink -f "$1"); RUN=$(readlink -f "$2"); JOB=$3
mkdir -p "$RUN"
cd "$PACKET" || exit 125
if ! sha256sum --quiet -c MANIFEST.sha256; then
  echo "refusing: packet manifest verification FAILED" >&2; exit 125
fi

PRODUCT=$(tr -d '\n' < /sys/class/dmi/id/product_name 2>/dev/null || true)
ASSET=$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag 2>/dev/null || true)
SAFE_JOB=${JOB//[:\/]/_}
META="$RUN/$SAFE_JOB.meta"

case "$JOB" in
  r2)   SCRIPT="R4_00_R2_BASE_DECIDE.sing" ;;
  r1p)  SCRIPT="R4_00_R1_BASE_DECIDE_epsP.sing" ;;
  r1m)  SCRIPT="R4_00_R1_BASE_DECIDE_epsM.sing" ;;
  msolve:*) SCRIPT="${JOB#msolve:}" ;;
  *) echo "refusing: unknown job '$JOB'" >&2; exit 125 ;;
esac
if [[ ! -f "$PACKET/$SCRIPT" ]]; then
  echo "refusing: missing packet input $SCRIPT" >&2; exit 125
fi

if [[ "$JOB" == msolve:* ]]; then
  TOOL=$(command -v msolve || true)
  [[ -n "$TOOL" ]] || { echo "refusing: msolve missing" >&2; exit 125; }
  VERSION=$("$TOOL" -h 2>&1 | head -n 3 | tr '\n' ' ')
  OUTFILE="$RUN/${SAFE_JOB}.gb"
  CMD=("$TOOL" -g 2 -t 4 -f "$PACKET/$SCRIPT" -o "$OUTFILE")
else
  TOOL=$(command -v Singular || true)
  [[ -n "$TOOL" ]] || { echo "refusing: Singular missing" >&2; exit 125; }
  VERSION=$("$TOOL" --version 2>&1 | head -n 1)
  OUTFILE=""
  CMD=("$TOOL" -q "$PACKET/$SCRIPT")
fi

{
  printf 'lane=%s\n' "$JC2_REGISTERED_AWS_LANE"
  printf 'job=%s\n' "$JOB"
  printf 'host=%s\n' "$(hostname)"
  printf 'uname=%s\n' "$(uname -a)"
  printf 'dmi_sys_vendor=%s\n' "$VENDOR"
  printf 'dmi_product_name=%s\n' "$PRODUCT"
  printf 'dmi_board_asset_tag=%s\n' "$ASSET"
  printf 'start_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'tool=%s\n' "$TOOL"
  printf 'tool_version=%s\n' "$VERSION"
  printf 'script=%s\n' "$SCRIPT"
  printf 'script_sha256=%s\n' "$(sha256sum "$PACKET/$SCRIPT" | cut -d' ' -f1)"
  printf 'manifest_sha256=%s\n' "$(sha256sum "$PACKET/MANIFEST.sha256" | cut -d' ' -f1)"
  printf 'argv='; printf '%q ' "${CMD[@]}"; printf '\n'
} > "$META"

cd "$RUN" || exit 125
set +e
timeout 43200 /usr/bin/time -v "${CMD[@]}" \
  > "$RUN/$SAFE_JOB.stdout" 2> "$RUN/$SAFE_JOB.stderr" < /dev/null
RC=$?
set -e

{
  printf 'end_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'rc=%s\n' "$RC"
  printf 'stdout_sha256=%s\n' "$(sha256sum "$RUN/$SAFE_JOB.stdout" | cut -d' ' -f1)"
  printf 'stderr_sha256=%s\n' "$(sha256sum "$RUN/$SAFE_JOB.stderr" | cut -d' ' -f1)"
  for f in "$RUN"/R2_CERT_*.txt "$RUN"/R1_*_CERT_*.txt "$RUN"/R2_COMPONENTS.txt \
           "$RUN"/R1_*_COMPONENTS.txt ${OUTFILE:+"$OUTFILE"}; do
    [[ -f "$f" ]] && printf 'artifact %s %s\n' \
      "$(sha256sum "$f" | cut -d' ' -f1)" "$(basename "$f")"
  done
} >> "$META"
printf '%s job=%s rc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$JOB" "$RC" \
  >> "$RUN/lanes.log"
exit "$RC"
