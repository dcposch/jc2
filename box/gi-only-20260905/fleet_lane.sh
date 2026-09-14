#!/usr/bin/env bash
# Reproducible operations for the four gi-only-20260905 workers only.
# All mutations require an ID/IP in the fixed allow-list below.  The generic
# fleet-wide destructive operation is intentionally not exposed.
set -euo pipefail

ROOT=/home/ubuntu/jc2
GI="$ROOT/box/gi-only-20260905"
FROZEN=/tmp/jc2-lane.ymMTCq/inputs
FLEET="$ROOT/ops/fleet/fleet.sh"
DISPATCH="$ROOT/ops/fleet/dispatch.sh"

declare -A ID_TO_IP=(
  [i-0889ee47ceb889561]=172.30.0.236
  [i-0d8bf8dd339a2e161]=172.30.0.238
  [i-0fe012c4207c7a220]=172.30.0.235
  [i-0a067499279342f0c]=172.30.0.75
)
declare -A IP_TO_ID=(
  [172.30.0.236]=i-0889ee47ceb889561
  [172.30.0.238]=i-0d8bf8dd339a2e161
  [172.30.0.235]=i-0fe012c4207c7a220
  [172.30.0.75]=i-0a067499279342f0c
)

CLASSES=(
  C_n24m16_Mm12_m2_5_ell1_s4
  C_n18m12_M2_9_ell2_s3
  C_n24m18_Mm15_14_ell1_s3
  C_n24m16_M12_17_ell1_s3
  C_n24m18_M9_20_ell1_s3
  C_n16m12_M6_13_ell3_s3
)

die() { echo "fleet_lane: $*" >&2; exit 2; }
allowed_ip() { [[ -n ${IP_TO_ID[${1:-}]:-} ]] || die "IP is not a lane worker: ${1:-}"; }
allowed_id() { [[ -n ${ID_TO_IP[${1:-}]:-} ]] || die "instance is not a lane worker: ${1:-}"; }
allowed_class() {
  local want=${1:-} item
  for item in "${CLASSES[@]}"; do [[ $item == "$want" ]] && return 0; done
  die "unknown class: $want"
}

local_preflight() {
  [[ $(sha256sum "$FLEET" | awk '{print $1}') == ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d ]] || die "fleet.sh hash mismatch"
  [[ $(sha256sum "$DISPATCH" | awk '{print $1}') == dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599 ]] || die "dispatch.sh hash mismatch"
  [[ $(sha256sum "$FROZEN/sprime3_compiler.py" | awk '{print $1}') == 7e6cfeedcee999a0163df9a23fd03fea695ca55a5de64e2e85b883a2fd4e1833 ]] || die "compiler hash mismatch"
  [[ $(sha256sum "$FROZEN/builder_fix.py" | awk '{print $1}') == d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b ]] || die "builder_fix hash mismatch"
  [[ $(sha256sum "$FROZEN/guided_gb.py" | awk '{print $1}') == 501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3 ]] || die "guided_gb hash mismatch"
}

sync_one() {
  local ip=$1
  allowed_ip "$ip"
  local_preflight
  "$FLEET" run "$ip" "mkdir -p $ROOT/box/gi-only-20260905 $ROOT/box/moh14-charts-20260905/hsupport-gate-20260905 $ROOT/box/orderbasis-20260903 $ROOT/box/lib"
  "$FLEET" push "$ip" "$GI/" "$ROOT/box/gi-only-20260905/"
  "$FLEET" push "$ip" "$FROZEN/sprime3_compiler.py" "$ROOT/box/moh14-charts-20260905/sprime3_compiler.py"
  "$FLEET" push "$ip" "$FROZEN/builder_fix.py" "$ROOT/box/moh14-charts-20260905/builder_fix.py"
  "$FLEET" push "$ip" "$FROZEN/guided_gb.py" "$ROOT/box/lib/guided_gb.py"
  "$FLEET" push "$ip" "$ROOT/box/moh14-charts-20260905/msolve_chart.py" "$ROOT/box/moh14-charts-20260905/msolve_chart.py"
  "$FLEET" push "$ip" "$ROOT/box/moh14-charts-20260905/hsupport-gate-20260905/verify_source_complete.py" "$ROOT/box/moh14-charts-20260905/hsupport-gate-20260905/verify_source_complete.py"
  "$FLEET" push "$ip" "$ROOT/box/orderbasis-20260903/order_basis_full.py" "$ROOT/box/orderbasis-20260903/order_basis_full.py"
  "$FLEET" push "$ip" "$ROOT/box/moh_skeleton_full.py" "$ROOT/box/moh_skeleton_full.py"
  "$FLEET" run "$ip" "chmod 755 $GI/solve_class.py $GI/time_singular.sh $GI/fleet_lane.sh $GI/classes/*/jobs/*_fleet.sh; sha256sum $ROOT/box/moh14-charts-20260905/sprime3_compiler.py $ROOT/box/moh14-charts-20260905/builder_fix.py $ROOT/box/lib/guided_gb.py; python3 -c 'import msolveio; print(\"msolveio=ok\")'; command -v Singular; command -v msolve"
}

dispatch_one() {
  local ip=$1 class_id=$2
  allowed_ip "$ip"; allowed_class "$class_id"
  local stem="${class_id}_G"
  # dispatch.sh is charged and rooted at moh14-charts; the explicit relative
  # class path resolves to this sibling output bundle.
  # The outer guard covers optional extraction (<=3600 for the largest chart),
  # modular emission/screen, guided emission, and the exact-Q run (<=600).
  # The exact production watchdog remains the requested 600 seconds.
  "$DISPATCH" run "$ip" "../../gi-only-20260905/classes/$class_id" "$stem" 5200
}

poll_one() {
  local ip=$1 class_id=$2
  allowed_ip "$ip"; allowed_class "$class_id"
  "$DISPATCH" poll "$ip" "${class_id}_G"
}

collect_one() {
  local ip=$1 class_id=$2
  allowed_ip "$ip"; allowed_class "$class_id"
  local id=${IP_TO_ID[$ip]} stem="${class_id}_G"
  local dest="$GI/fleet/$id/$class_id"
  # Preserve the complete named-class snapshot before a worker is reused or
  # terminated: solve custody alone omits worker-generated rows, metadata, the
  # guided exact-Q input, and updated fibre aliases.
  mkdir -p "$dest/class"
  "$FLEET" pull "$ip" "$GI/classes/$class_id/" "$dest/class/"
  "$FLEET" pull "$ip" "/home/ubuntu/${stem}.log" "$dest/${stem}.dispatch.log"
  # Install the same collected snapshot in the canonical local class path;
  # the per-instance copy above remains the immutable custody source.
  rsync -a "$dest/class/" "$GI/classes/$class_id/"
  sha256sum \
    "$dest/class/solve/solve-result.json" \
    "$dest/class/rows/${stem}_rows.tsv" \
    "$dest/class/meta/${stem}.json" \
    "$dest/class/jobs/${stem}_Q_guided.sing" \
    "$dest/${stem}.dispatch.log"
}

terminate_ids() {
  local id
  [[ $# -gt 0 ]] || die "terminate requires explicit lane instance IDs"
  for id in "$@"; do allowed_id "$id"; done
  "$FLEET" term "$@"
}

usage() {
  echo "usage: $0 sync IP | dispatch IP CLASS | poll IP CLASS | collect IP CLASS | terminate ID... | list"
}

cmd=${1:-}; shift || true
case "$cmd" in
  sync) [[ $# == 1 ]] || die "sync requires IP"; sync_one "$1" ;;
  dispatch) [[ $# == 2 ]] || die "dispatch requires IP CLASS"; dispatch_one "$1" "$2" ;;
  poll) [[ $# == 2 ]] || die "poll requires IP CLASS"; poll_one "$1" "$2" ;;
  collect) [[ $# == 2 ]] || die "collect requires IP CLASS"; collect_one "$1" "$2" ;;
  terminate) terminate_ids "$@" ;;
  list) for id in "${!ID_TO_IP[@]}"; do echo "$id ${ID_TO_IP[$id]}"; done | sort ;;
  *) usage; exit 2 ;;
esac
