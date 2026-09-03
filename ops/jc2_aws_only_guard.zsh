#!/bin/zsh

# Stop JC2 campaign computations that are accidentally launched on this Mac.
# Coordination, SSH, hashing, editing, and text-only review remain untouched.

setopt NO_NOMATCH

readonly campaign_root="/Users/dc/code/math/jc2"
readonly guard_log="/tmp/jc2_aws_only_guard.log"

print -r -- "$(date -u +%Y-%m-%dT%H:%M:%SZ) guard started pid=$$" >> "$guard_log"

while true; do
  ps -axo pid=,comm= | while read -r pid executable; do
    [[ "$pid" == "$$" ]] && continue

    base_name="${executable:t}"
    case "$base_name" in
      Singular|singular|lean|lake|sage|msolve|M2|Macaulay2|magma|julia|gap|gp|wolframscript)
        ;;
      python|python3|python3.*|Python|Python3|Python3.*)
        # Python is stopped only when it is actually consuming substantial
        # local resources; lightweight campaign compilers remain permitted.
        cpu_rss="$(ps -p "$pid" -o %cpu=,rss= 2>/dev/null)"
        [[ -z "$cpu_rss" ]] && continue
        if ! print -r -- "$cpu_rss" | awk '{ exit !(($1 + 0) >= 25 || ($2 + 0) >= 524288) }'; then
          continue
        fi
        ;;
      *)
        continue
        ;;
    esac

    command_line="$(ps -p "$pid" -o command= 2>/dev/null)"
    process_cwd="$(lsof -a -p "$pid" -d cwd -Fn 2>/dev/null | sed -n 's/^n//p' | head -1)"
    if [[ "$command_line" == *"$campaign_root"* || "$process_cwd" == "$campaign_root"* ]]; then
      print -r -- "$(date -u +%Y-%m-%dT%H:%M:%SZ) TERM pid=$pid exe=$base_name cwd=$process_cwd cmd=$command_line" >> "$guard_log"
      kill -TERM "$pid" 2>/dev/null || true
    fi
  done
  sleep 5
done
