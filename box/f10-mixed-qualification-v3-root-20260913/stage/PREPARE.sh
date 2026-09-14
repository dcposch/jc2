#!/bin/bash
# INERT one-client administrative preparation, not scientific launch authority.
# Mechanical physical/source binding only after a new ROOT registration.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
  printf '%s\n' 'DISABLED: unresolved preparation binding' >&2
  exit 2
fi
task_instance=i-05ceda98fbb668717
task_stop='2026-09-13 01:20:00 UTC'
task_term='2026-09-13 01:19:55 UTC'
task_stage=/home/ubuntu/jc2-mixed-v3-stage-20260913
task_base=/opt/jc2-mixed-20260912
task_prep="$task_base/prep"
task_dispatch_sha=079f9ad7b92e64af5c5fc6a5e17de14ffa5245627ee5c8a4ce0ef2a018a2fa5d
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = "$task_instance"
test "$(date -u +%s)" -lt "$(date -u -d "$task_stop" +%s)"
test ! -e "$task_base"
test -d /usr/lib/python3/dist-packages/sympy
test -d /usr/lib/python3/dist-packages/mpmath
test -x /usr/bin/jq
test "$(sha256sum "$task_stage/authority.py" | cut -d' ' -f1)" = ecdd37dfb900a13dca6dac03dcec3a608c7fd575d3ffccb1ec3976fd400b2097
test "$(sha256sum "$task_stage/produce.py" | cut -d' ' -f1)" = 8aee305b5fc32f0a20f2bb8ccfe01ac1c389c98594ea7724070e1badfae2abe0
test "$(sha256sum "$task_stage/check.py" | cut -d' ' -f1)" = 1ab7f3b3e08178eecabd1b2af86620554a9006fbfffe35378c92940c27a4a5a5
test "$(sha256sum "$task_stage/run_capped.py" | cut -d' ' -f1)" = 4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2
test "$(sha256sum "$task_stage/probe.py" | cut -d' ' -f1)" = 16d723b7fbe6dc218351274e4078df1959add5c2914174079d707fdc14e17158
test "$(sha256sum "$task_stage/dispatch.py" | cut -d' ' -f1)" = "$task_dispatch_sha"
test "$(sha256sum "$task_stage/native_records.py" | cut -d' ' -f1)" = 63178c8aeab6d2f81bfddf4cdcc732ee00204c73f68f43c5f04761a2dfe4be9a
test "$(sha256sum "$task_stage/native-metadata.actual.sh" | cut -d' ' -f1)" = 3976fdc39cbf8653b37943853afa426afeda9ab1b28bb184e52db2609a4e4191
test "$(sha256sum "$task_stage/inspect_native.py" | cut -d' ' -f1)" = f419027050b1de290407626955512c95b03747eb7279ed0abf65bf4268cbaa3d
test "$(sha256sum "$task_stage/inspect_imports.py" | cut -d' ' -f1)" = 31a911548dc37f22d80187ac406608427ad774e8942e4d5bb85238a3f4d054a1
install -d -o root -g root -m 0755 "$task_base" "$task_base/science" "$task_base/runtime" "$task_base/lib" "$task_base/meta" "$task_prep"
for task_name in authority.py produce.py check.py; do
  install -o root -g root -m 0444 "$task_stage/$task_name" "$task_base/science/$task_name"
done
for task_name in dispatch.py run_capped.py probe.py; do
  install -o root -g root -m 0444 "$task_stage/$task_name" "$task_base/runtime/$task_name"
done
cp -a /usr/lib/python3/dist-packages/sympy /usr/lib/python3/dist-packages/mpmath "$task_base/lib/"
for task_name in native-metadata.actual.sh native_records.py inspect_native.py inspect_imports.py; do
  install -o root -g root -m 0444 "$task_stage/$task_name" "$task_base/meta/$task_name"
done
mount -t tmpfs -o size=268435456,mode=0755,nodev,nosuid,noexec tmpfs "$task_prep"
date -u '+PREPARATION_START %Y-%m-%d %H:%M:%S.%N UTC'
hostname
readlink /proc/self/ns/pid
readlink /proc/self/ns/cgroup
sed -n '1p' /proc/sys/kernel/random/boot_id
uname -srmo
systemd --version
dpkg-query -W -f='${Package} ${Version}\n' python3.12 python3.12-minimal libpython3.12-stdlib util-linux procps
find "$task_base/science" "$task_base/runtime" "$task_base/meta" -type f -exec sha256sum '{}' +
systemd-run --quiet --unit=jc2-mixed-v3-qual-term-20260913 --on-calendar="$task_term" --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=TERM jc2-mixed-v3-native-20260913.service jc2-mixed-v3-assembly-20260913.service jc2-mixed-v3-inspect-20260913.service jc2-mixed-v3-imports-20260913.service
systemd-run --quiet --unit=jc2-mixed-v3-qual-kill-20260913 --on-calendar="$task_stop" --timer-property=AccuracySec=1us /usr/bin/systemctl kill --kill-whom=all --signal=KILL jc2-mixed-v3-native-20260913.service jc2-mixed-v3-assembly-20260913.service jc2-mixed-v3-inspect-20260913.service jc2-mixed-v3-imports-20260913.service
systemctl show jc2-mixed-v3-qual-term-20260913.timer jc2-mixed-v3-qual-kill-20260913.timer -p Id -p ActiveState -p NextElapseUSecRealtime > "$task_prep/qualification-caps.properties"
test "$(systemctl show jc2-mixed-v3-qual-term-20260913.timer -P ActiveState)" = active
test "$(systemctl show jc2-mixed-v3-qual-kill-20260913.timer -P ActiveState)" = active
test "$(date -u +%s)" -lt "$(date -u -d "$task_stop" +%s)"
set +e
systemd-run --quiet --wait --unit=jc2-mixed-v3-native-20260913 --service-type=exec -p Restart=no -p KillMode=control-group -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=1073741824 -p MemorySwapMax=0 -p TasksMax=64 -p LimitAS=1073741824 -p LimitFSIZE=4194304 -p RuntimeMaxSec=595s -p TimeoutStopSec=5s -p StandardOutput=file:"$task_prep/native.stdout" -p StandardError=file:"$task_prep/native.stderr" /usr/bin/bash "$task_base/meta/native-metadata.actual.sh"
task_rc=$?
set -e
printf '%s\n' "$task_rc" > "$task_prep/native.wait-exit"
systemctl show jc2-mixed-v3-native-20260913.service -p Id -p LoadState -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus > "$task_prep/native.terminal.properties"
test "$task_rc" -eq 0
test ! -s "$task_prep/native.stderr"
test "$(stat -c %s "$task_prep/native.stdout")" -le 4194304
test "$(date -u +%s)" -lt "$(date -u -d "$task_stop" +%s)"
# Actual facts are independently queried here, not copied from an old worker
# or inferred from the native stdout being checked by the assembler.
jq -cnS --arg boot "$(tr -d '\n' < /proc/sys/kernel/random/boot_id)" --arg host "$(hostname)" --arg pns "$(readlink /proc/self/ns/pid)" --arg collector "$(sha256sum "$task_base/meta/native-metadata.actual.sh" | cut -d' ' -f1)" --arg py "$(dpkg-query -W -f='${Version}' python3.12)" --arg pym "$(dpkg-query -W -f='${Version}' python3.12-minimal)" --arg lib "$(dpkg-query -W -f='${Version}' libpython3.12-stdlib)" --arg util "$(dpkg-query -W -f='${Version}' util-linux)" --arg proc "$(dpkg-query -W -f='${Version}' procps)" '{schema:"r3-native-expected-facts/v1",boot_id:$boot,hostname:$host,pid_namespace:$pns,collector_sha256:$collector,packages:{"python3.12":$py,"python3.12-minimal":$pym,"libpython3.12-stdlib":$lib,"util-linux":$util,"procps":$proc}}' > "$task_base/meta/facts.json"
chmod 0444 "$task_base/meta/facts.json"
task_raw_sha="$(sha256sum "$task_prep/native.stdout" | cut -d' ' -f1)"
task_facts_sha="$(sha256sum "$task_base/meta/facts.json" | cut -d' ' -f1)"
set +e
systemd-run --quiet --wait --unit=jc2-mixed-v3-assembly-20260913 --service-type=exec -p Restart=no -p KillMode=control-group -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=1073741824 -p MemorySwapMax=0 -p TasksMax=64 -p LimitAS=1073741824 -p LimitFSIZE=4194304 -p RuntimeMaxSec=115s -p TimeoutStopSec=5s -p StandardOutput=file:"$task_prep/assembly.stdout" -p StandardError=file:"$task_prep/assembly.stderr" /usr/bin/python3.12 -I -S -B "$task_base/meta/native_records.py" --raw "$task_prep/native.stdout" --raw-sha256 "$task_raw_sha" --facts "$task_base/meta/facts.json" --facts-sha256 "$task_facts_sha" --out "$task_prep/assembled"
task_rc=$?
set -e
printf '%s\n' "$task_rc" > "$task_prep/assembly.wait-exit"
systemctl show jc2-mixed-v3-assembly-20260913.service -p Id -p LoadState -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus > "$task_prep/assembly.terminal.properties"
test "$task_rc" -eq 0
test ! -s "$task_prep/assembly.stderr"
test "$(sha256sum "$task_prep/native.stdout" | cut -d' ' -f1)" = "$task_raw_sha"
test "$(sha256sum "$task_base/meta/facts.json" | cut -d' ' -f1)" = "$task_facts_sha"
test "$(date -u +%s)" -lt "$(date -u -d "$task_stop" +%s)"
set +e
systemd-run --quiet --wait --unit=jc2-mixed-v3-inspect-20260913 --service-type=exec -p Restart=no -p KillMode=control-group -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=1073741824 -p MemorySwapMax=0 -p TasksMax=64 -p LimitAS=1073741824 -p LimitFSIZE=4194304 -p RuntimeMaxSec=25s -p TimeoutStopSec=5s -p StandardOutput=file:"$task_prep/inspect.stdout" -p StandardError=file:"$task_prep/inspect.stderr" /usr/bin/python3.12 -I -S -B "$task_base/meta/inspect_native.py"
task_rc=$?
set -e
printf '%s\n' "$task_rc" > "$task_prep/inspect.wait-exit"
systemctl show jc2-mixed-v3-inspect-20260913.service -p Id -p LoadState -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus > "$task_prep/inspect.terminal.properties"
test "$task_rc" -eq 0
test ! -s "$task_prep/inspect.stderr"
jq -e '.status=="METADATA_PINS_PATHS_MODES_ACL_COPY_CHECKED_NOT_SCIENCE"' "$task_prep/inspect.stdout" >/dev/null
test "$(date -u +%s)" -lt "$(date -u -d "$task_stop" +%s)"
set +e
systemd-run --quiet --wait --unit=jc2-mixed-v3-imports-20260913 --service-type=exec -p Restart=no -p KillMode=control-group -p CPUQuota=80% -p CPUQuotaPeriodSec=100ms -p MemoryMax=1073741824 -p MemorySwapMax=0 -p TasksMax=64 -p LimitAS=1073741824 -p LimitFSIZE=4194304 -p RuntimeMaxSec=25s -p TimeoutStopSec=5s -p StandardOutput=file:"$task_prep/imports.stdout" -p StandardError=file:"$task_prep/imports.stderr" /usr/bin/python3.12 -E -s -S -B "$task_base/meta/inspect_imports.py"
task_rc=$?
set -e
printf '%s\n' "$task_rc" > "$task_prep/imports.wait-exit"
systemctl show jc2-mixed-v3-imports-20260913.service -p Id -p LoadState -p ActiveState -p SubState -p Result -p ExecMainCode -p ExecMainStatus > "$task_prep/imports.terminal.properties"
test "$task_rc" -eq 0
test ! -s "$task_prep/imports.stderr"
jq -e '.status=="IMPORT_PATHS_APIS_PINS_CHECKED_NOT_ALGEBRA"' "$task_prep/imports.stdout" >/dev/null
test "$(date -u +%s)" -lt "$(date -u -d "$task_stop" +%s)"
date -u '+PREPARATION_END %Y-%m-%d %H:%M:%S.%N UTC'
printf '%s\n' 'METADATA_STAGES_COMPLETE_NOT_ROOT_ACCEPTED_NO_DUMMY_NO_SCIENCE'
# ROOT still checks actual live units/cgroups and all receipts, then separately
# binds the accepted one-shot dummy. No automatic science or worker retention.
