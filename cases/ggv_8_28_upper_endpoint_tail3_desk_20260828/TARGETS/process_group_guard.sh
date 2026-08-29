#!/usr/bin/env bash
# Shared fail-closed validation for tail3 worker process groups.

tail3_validate_group() {
  local run_dir=$1
  local pgid=$2
  [[ "$run_dir" == /* && "$pgid" =~ ^[0-9]+$ ]] || return 2
  local found=0 pid observed args
  while read -r pid observed args; do
    [[ -n "$pid" ]] || continue
    if [[ "$observed" == "$pgid" ]]; then
      found=1
      if [[ "$args" != *"$run_dir/"* ]]; then
        echo "REFUSE: PGID $pgid member $pid lacks namespace path" >&2
        return 3
      fi
    fi
  done < <(ps -eo pid=,pgid=,args=)
  (( found == 1 ))
}

tail3_signal_group() {
  local run_dir=$1
  local pgid=$2
  local signal=$3
  if tail3_validate_group "$run_dir" "$pgid"; then
    kill -s "$signal" -- "-$pgid"
  else
    local rc=$?
    # An already-empty group is harmless; a live mismatched group is not.
    if ps -eo pgid= | awk -v wanted="$pgid" '$1==wanted {found=1} END {exit !found}'; then
      echo "REFUSE: live PGID $pgid failed namespace validation" >&2
      return "$rc"
    fi
  fi
}

