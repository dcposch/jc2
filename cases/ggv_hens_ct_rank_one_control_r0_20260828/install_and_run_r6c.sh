#!/usr/bin/env bash
set -u

TAG=${AWS_RUN_TAG:-}
if [ -z "$TAG" ]; then
  echo "FAIL_NO_TAG"
  exit 2
fi
if [ "$(uname -s)" != "Linux" ]; then
  echo "FAIL_NOT_LINUX"
  exit 2
fi
if [ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null)" != "Amazon EC2" ]; then
  echo "FAIL_NOT_EC2"
  exit 2
fi

date -u +START_UTC=%Y-%m-%dT%H:%M:%SZ
hostname
grep -E 'MemAvailable|SwapTotal|SwapFree' /proc/meminfo
ps -eo pid,rss,comm,args --sort=-rss | head -n 20

avail_kb=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
swap_total=$(awk '/SwapTotal:/ {print $2}' /proc/meminfo)
swap_free=$(awk '/SwapFree:/ {print $2}' /proc/meminfo)
if [ "$avail_kb" -lt 471859200 ] || [ "$swap_total" -ne "$swap_free" ]; then
  echo "RESOURCE_STOP" > TERMINAL
  exit 3
fi

ORE_COMMIT=18680180c884fac869a064db99f29a221aad9dfe
export ORE_COMMIT
python3 -m venv venv
if ! timeout 1800 venv/bin/pip install -q \
  "ore_algebra[passagemath] @ git+https://github.com/mkauers/ore_algebra.git@${ORE_COMMIT}"; then
  echo "FAIL_INSTALL" > TERMINAL
  exit 4
fi
venv/bin/pip freeze | LC_ALL=C sort > TOOLCHAIN_FREEZE.txt

ulimit -v 419430400
export CT_ITERATION_LIMIT=96
set +e
timeout 14400 /usr/bin/time -v venv/bin/python run_ore_ct.py \
  > ct.stdout 2> ct.stderr
rc=$?
set -e
printf '%s\n' "$rc" > ct.rc
if [ "$rc" -eq 124 ]; then
  echo "TIMEOUT" > TERMINAL
elif [ "$rc" -ne 0 ]; then
  if [ ! -s TERMINAL ]; then echo "FAIL_CT_RC" > TERMINAL; fi
fi
date -u +END_UTC=%Y-%m-%dT%H:%M:%SZ
sha256sum run_ore_ct.py replay_rank_one_controls.py PREREGISTRATION.md \
  TOOLCHAIN_FREEZE.txt ct.stdout ct.stderr ct.rc TERMINAL > EVIDENCE.sha256
exit "$rc"
