#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "refusing outside Linux" >&2
  exit 125
fi
if [[ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" != "Amazon EC2" ]]; then
  echo "refusing outside Amazon EC2" >&2
  exit 125
fi
if [[ $# -ne 2 ]]; then
  echo "usage: run_exact.sh RUN_DIR INPUT.sing" >&2
  exit 125
fi

run_dir=$1
input_name=$2
case "$input_name" in
  local_power.sing|global_minass.sing|global_power.sing) ;;
  *) echo "unregistered input: $input_name" >&2; exit 125 ;;
esac
cd "$run_dir"

test "$(sha256sum prelude_Q.sing | cut -d ' ' -f 1)" = "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a"
case "$input_name" in
  local_power.sing)
    test "$(sha256sum "$input_name" | cut -d ' ' -f 1)" = "83eb1ce7fee72e0356fae710ef440fe9cdf7b18b8b3cb6db81ba9ea484b2eafa"
    ;;
  global_minass.sing)
    test "$(sha256sum "$input_name" | cut -d ' ' -f 1)" = "8fd2faa1dcd7feaf149bdf027d7231e374a783039ea99d4d2ce81e0d6a66cdf0"
    ;;
  global_power.sing)
    test "$(sha256sum "$input_name" | cut -d ' ' -f 1)" = "bb95d104e6d5ddfb31a59c88a782a584c3a836134b041ad0d4a5ea6caede53ef"
    ;;
esac

Singular -v
exec Singular -q "$input_name"
