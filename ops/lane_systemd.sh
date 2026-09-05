#!/bin/sh
# Linux counterpart of ops/lane_detach.py: run the unchanged ops/lane.sh as a
# transient per-user systemd unit so the lane survives the coordinator's
# terminal or agent process. lane.sh keeps all custody; this only detaches.
#   ops/lane_systemd.sh launch ADAPTER TAG PROMPT
#   ops/lane_systemd.sh status TAG        # active|inactive|failed + exit status
#   ops/lane_systemd.sh list              # live jc2 lane units
#   ops/lane_systemd.sh stop TAG          # TERM the unit (lane.sh records CANCELLED)
set -u
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
cmd=${1:-}
unit_for() { printf 'jc2-lane-%s' "$1"; }
case "$cmd" in
  launch)
    # DISK GUARD (2026-09-05): a full root disk killed a lane mid-run; refuse to launch below 400 MB free.
    _free_kb=$(df -Pk / | awk 'NR==2{print $4}'); if [ "${_free_kb:-0}" -lt 409600 ]; then echo "lane_systemd: REFUSING launch — root filesystem has ${_free_kb} KB free (< 400 MB); free space first" >&2; exit 75; fi
    [ "$#" -eq 4 ] || { echo "usage: $0 launch ADAPTER TAG PROMPT" >&2; exit 2; }
    adapter=$2; tag=$3; prompt=$4
    case "$prompt" in /*) ;; *) prompt=$(pwd -P)/$prompt ;; esac
    unit=$(unit_for "$tag")
    # Adapters need the model CLIs: nvm node (codex, claude) and ~/.grok/bin.
    node_bin=$(ls -d "$HOME"/.nvm/versions/node/*/bin 2>/dev/null | sort -V | tail -1)
    lane_path="$HOME/.grok/bin:${node_bin:+$node_bin:}/usr/local/bin:/usr/bin:/bin"
    systemd-run --user --quiet --collect --unit "$unit" \
      --property WorkingDirectory="$repo_root" \
      --setenv PATH="$lane_path" --setenv HOME="$HOME" \
      --setenv TMPDIR="${TMPDIR:-/tmp}" \
      sh "$repo_root/ops/lane.sh" "$adapter" "$tag" "$prompt" || exit $?
    echo "launched $unit (adapter=$adapter tag=$tag)"
    ;;
  status)
    [ "$#" -eq 2 ] || { echo "usage: $0 status TAG" >&2; exit 2; }
    unit=$(unit_for "$2")
    systemctl --user show "$unit" -p ActiveState -p SubState -p ExecMainStatus -p ExecMainStartTimestamp 2>/dev/null
    ;;
  list)
    systemctl --user list-units --no-legend --all 'jc2-lane-*' 2>/dev/null
    ;;
  stop)
    [ "$#" -eq 2 ] || { echo "usage: $0 stop TAG" >&2; exit 2; }
    systemctl --user kill --signal=TERM "$(unit_for "$2")"
    ;;
  *)
    echo "usage: $0 launch ADAPTER TAG PROMPT | status TAG | list | stop TAG" >&2
    exit 2
    ;;
esac
