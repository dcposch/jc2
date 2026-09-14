# One PRE-SCIENCE dummy — disabled literal operator procedure

No command below is authorized while any `__PLACEHOLDER__` remains. Bind every
value from one fresh worker and a separately approved registration; never use
the closed attempt's host, boot, unit or clock values. `/usr/bin/jq` and every
listed executable must first be pinned, included in actual native closure and
qualified. This runs no science import.

Required bindings: `__INSTANCE__`, `__BOOT__`, `__HOST__`, `__PID_NS__`,
`__CGROUP_NS__`, `__UID__`, `__GID__`, `__UNIT__`, `__ABS_DEADLINE__`,
`__MOUNT__`, `__ADMIN__`, `__OUTPUT__`, `__PYTHON__`, `__SETPRIV__`,
`__CAPRUN__`, `__PROBE__`, and exact SHA-256 for the latter four plus jq.
The probe SHA must be
`16d723b7fbe6dc218351274e4078df1959add5c2914174079d707fdc14e17158`.

After ROOT authenticates EC2/instance/host/boot/namespaces, immutable source
ancestry, native/import closure and an absolute stop no later than25 seconds
after admission, prepare one fresh root-owned tmpfs and exact two children:

```sh
install -d -o root -g root -m 0755 __MOUNT__
mount -t tmpfs -o size=268435456,mode=0755,nodev,nosuid,noexec tmpfs __MOUNT__
install -d -o root -g root -m 0755 __ADMIN__
install -d -o __UID__ -g __GID__ -m 0700 __OUTPUT__
test "$(find __MOUNT__ -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)" = $'admin\noutput'
sha256sum __PYTHON__ __SETPRIV__ __CAPRUN__ __PROBE__
```

Arm the independent absolute exact-unit TERM/KILL before this one blocking
launch. The registration must prove `__ADMIN__` and `__OUTPUT__` are the two
siblings above and `__ABS_DEADLINE__` dominates RuntimeMaxSec/cleanup.

```sh
set +e
systemd-run --quiet --wait --unit=__UNIT__ --service-type=exec \
  -p User=root -p Group=root -p Restart=no -p KillMode=control-group \
  -p Delegate=no -p NoNewPrivileges=yes \
  -p 'CapabilityBoundingSet=CAP_KILL CAP_SETUID CAP_SETGID' -p AmbientCapabilities= \
  -p RestrictRealtime=yes -p RestrictNamespaces=yes -p ProtectControlGroups=yes \
  -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms \
  -p MemoryMax=34359738368 -p MemorySwapMax=0 -p TasksMax=64 \
  -p LimitCPU=4 -p LimitAS=34359738368 -p LimitFSIZE=268435456 \
  -p RuntimeMaxSec=20s -p TimeoutStopSec=5s \
  -p StandardOutput=file:__OUTPUT__/runner.stdout \
  -p StandardError=file:__OUTPUT__/runner.stderr \
  -E HOME=__OUTPUT__ -E TMPDIR=__OUTPUT__ -E TMP=__OUTPUT__ -E TEMP=__OUTPUT__ \
  -E XDG_CACHE_HOME=__OUTPUT__ -E PYTHONPYCACHEPREFIX=__OUTPUT__/pycache \
  __PYTHON__ -E -s -S -B __CAPRUN__ \
    --wall-seconds 5 --cpu-seconds 3 --rss-bytes 33554432 \
    --stdout-file __OUTPUT__/dummy.stdout --stderr-file __OUTPUT__/dummy.stderr \
    --telemetry-file __OUTPUT__/dummy.telemetry.json --cwd __OUTPUT__ -- \
    __SETPRIV__ --reuid=__UID__ --regid=__GID__ --clear-groups --no-new-privs \
    __PYTHON__ -E -s -S -B __PROBE__ --descendant-rss-term-kill
wait_rc=$?
set -e
printf '%s\n' "$wait_rc" >__ADMIN__/systemd-run.exit
systemctl show __UNIT__.service -p Id -p LoadState -p ActiveState -p SubState \
  -p Result -p ExecMainCode -p ExecMainStatus -p ControlGroup \
  >__ADMIN__/unit-terminal.properties
test "$wait_rc" -eq 125
test "$(systemctl show __UNIT__.service -P ExecMainStatus)" = 125
```

This blocking `--wait` is the only wait; no live poll/observer is used. Before
unloading the unit, ROOT reads all files WHOLE and requires: empty dummy stderr;
CAPRUN's one-line runner stdout; telemetry schema CAPRUN/v1, RESOURCE_CAP/rss,
runner_exit_code125, exact argv hash/count/executable/cwd/caps, leader PID=PGID,
proc-field22 start identity with `__BOOT__`, max group RSS>33554432, TERM and
KILL sent, leader reaped, cleanup_complete true, and empty live-before-reap.

Require dummy stdout to contain exactly two LF-terminated physical lines. Line1
is `DESCENDANT_READY`; line2 must parse with the exact v2 keysets and must equal
its `jq -cS` reserialization byte-for-byte. Require payload67108864, UID/GID
bindings, NNP1/zero CapEff, CPU limits3/4, AS32GiB pair, FSIZE256MiB pair,
cpu.max `80000 100000\n`, burst `0\n`, memory.max `34359738368\n`, swap
`0\n`, type `domain\n`, empty subtree, and the registered boot/PID/cgroup
namespaces. Child PID differs from telemetry leader; child PGID equals leader
PGID; child cgroup path equals the unit ControlGroup under `/sys/fs/cgroup`;
its recorded directory identity and exact control bytes agree with the bound
unit facts. Controllers are observational, not a completeness assertion.

Any missing/short/extra/malformed byte, wrong numeric exit, cap-before-marker,
identity mismatch or deadline failure is STOP with no retry. Finally require
the exact unit cgroup `cgroup.procs` empty and no descendants if it persists,
then stop/reset the exact unit and require its cgroup path absent; stop the
absolute timers only after that proof. Hash/freeze the exact stdout, stderr,
telemetry, runner streams, exit file, unit properties, source pins and tmpfs
census before durable transfer. Self-reported data plus CAPRUN sampling is not
a no-escape or true-peak theorem; ROOT retains physical mount/unit/no-writer
and retirement proof.
