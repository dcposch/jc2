#!/usr/bin/env bash
set -u

TAG=${AWS_RUN_TAG:-}
FROZEN_ROOT=${FROZEN_ROOT:-}
EXPECTED_SETUP_SHA=38da4b778c52ea2b20105e9f15661c4a09c9776e06971fbcd989163a549d2f7a
ORE_COMMIT=18680180c884fac869a064db99f29a221aad9dfe
export ORE_COMMIT
if [ -z "$TAG" ] || [ -z "$FROZEN_ROOT" ]; then
  echo "FAIL_NO_TAG_OR_ENV" > TERMINAL
  exit 2
fi
if [ "$(uname -s)" != "Linux" ] || \
   [ "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor 2>/dev/null)" != "Amazon EC2" ]; then
  echo "FAIL_WRONG_HOST" > TERMINAL
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

if [ ! -x "$FROZEN_ROOT/venv/bin/python" ] || \
   [ "$(git -C "$FROZEN_ROOT/ore_algebra_src" rev-parse HEAD 2>/dev/null)" != "$ORE_COMMIT" ] || \
   [ "$(sha256sum "$FROZEN_ROOT/ore_algebra_src/setup.py" | awk '{print $1}')" != "$EXPECTED_SETUP_SHA" ]; then
  echo "FAIL_FROZEN_ENV_CHECK" > TERMINAL
  exit 4
fi
"$FROZEN_ROOT/venv/bin/pip" freeze | LC_ALL=C sort > TOOLCHAIN_FREEZE.txt
sha256sum "$FROZEN_ROOT/ore_algebra_src/setup.py" > PATCHED_SETUP.sha256

ulimit -v 419430400
export CT_ITERATION_LIMIT=96
set +e
timeout 14400 /usr/bin/time -v "$FROZEN_ROOT/venv/bin/python" run_ore_ct.py \
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
  TOOLCHAIN_FREEZE.txt PATCHED_SETUP.sha256 ct.stdout ct.stderr ct.rc TERMINAL \
  > EVIDENCE.sha256
exit "$rc"
