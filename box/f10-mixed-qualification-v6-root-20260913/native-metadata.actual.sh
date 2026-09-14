#!/bin/bash
# ROOT read-only six-field native inventory. No Python/module/science execution.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0a59ae3233f3774a6
date -u '+NATIVE_START %Y-%m-%d %H:%M:%S.%N UTC'
hostname
readlink /proc/self/ns/pid
sed -n '1p' /proc/sys/kernel/random/boot_id
dpkg-query -W -f='${Package} ${Version}\n' python3.12 python3.12-minimal libpython3.12-stdlib util-linux procps
declare -A jc2_native_files jc2_native_dirs jc2_native_aliases
jc2_native_file_count=0
jc2_native_dir_count=0
jc2_native_visit() {
 local jc2_path="$1" jc2_real jc2_listing jc2_child jc2_file jc2_ldd jc2_deps jc2_dep
 [[ "$jc2_path" =~ ^/[A-Za-z0-9_./-]+$ ]]
 jc2_real=$(readlink -e "$jc2_path")
 test -n "$jc2_real"
 [[ "$jc2_real" =~ ^/[A-Za-z0-9_./-]+$ ]]
 if test "$jc2_path" != "$jc2_real"; then
  if test -z "${jc2_native_aliases[$jc2_path]+yes}"; then
   jc2_native_aliases["$jc2_path"]="$jc2_real"
   printf 'ALIAS %s %s\n' "$jc2_path" "$jc2_real"
  fi
 fi
 if test -d "$jc2_real"; then
  test -z "${jc2_native_dirs[$jc2_real]+yes}" || return 0
  jc2_native_dirs["$jc2_real"]=1
  jc2_native_dir_count=$((jc2_native_dir_count+1))
  test "$jc2_native_dir_count" -le 1000
  stat --printf='DIRECTORY %u %g %a %n\n' "$jc2_real"
  jc2_listing=$(find "$jc2_real" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C sort)
  while IFS= read -r jc2_child; do
   test -n "$jc2_child" || continue
   [[ "$jc2_child" =~ ^[A-Za-z0-9_.-]+$ ]]
   printf 'ENTRY %s %s\n' "$jc2_real" "$jc2_child"
   jc2_native_visit "$jc2_real/$jc2_child"
  done <<< "$jc2_listing"
 else
  test -f "$jc2_real"
  test -z "${jc2_native_files[$jc2_real]+yes}" || return 0
  jc2_native_files["$jc2_real"]=1
  jc2_native_file_count=$((jc2_native_file_count+1))
  test "$jc2_native_file_count" -le 8192
  sha256sum "$jc2_real"
  stat --printf='FILE %s %u %g %a %n\n' "$jc2_real"
  jc2_file=$(file -Lb "$jc2_real")
  if [[ "$jc2_file" == ELF* && "$jc2_file" != *relocatable* ]]; then
   jc2_ldd=$(ldd "$jc2_real")
   [[ "$jc2_ldd" != *'not found'* ]]
   jc2_deps=$(printf '%s\n' "$jc2_ldd" | awk '/=> \/|^[[:space:]]*\// {for(i=1;i<=NF;i++) if(substr($i,1,1)=="/") print $i}')
   while IFS= read -r jc2_dep; do
    test -n "$jc2_dep" || continue
    jc2_native_visit "$jc2_dep"
   done <<< "$jc2_deps"
  fi
 fi
}
# Declared base stdlib paths only; ROOT separately checks actual script paths and appended private lib.
printf 'PYTHON_PATH /usr/lib/python312.zip\n'
printf 'PYTHON_PATH /usr/lib/python3.12\n'
printf 'PYTHON_PATH /usr/lib/python3.12/lib-dynload\n'
for jc2_path in /usr/bin/python3 /usr/bin/python3.12 /usr/bin/setpriv /bin/ps /usr/bin/ps /usr/lib/python3.12 /etc/ld.so.cache /usr/bin/env /usr/bin/systemctl /opt/jc2-mixed-20260912/science /opt/jc2-mixed-20260912/runtime /opt/jc2-mixed-20260912/lib /usr/bin/bash /usr/bin/jq /usr/bin/head /usr/bin/cmp /usr/bin/od /usr/bin/tr /usr/bin/tail /usr/bin/wc /usr/bin/cut /usr/bin/find /usr/bin/sort /usr/bin/xargs /usr/bin/stat /usr/bin/sha256sum /usr/bin/install /usr/bin/mount /usr/bin/systemd-run /usr/bin/hostname /usr/bin/readlink /usr/bin/date /usr/bin/sed /usr/bin/cat; do
 jc2_native_visit "$jc2_path"
done
if test -e /usr/lib/python312.zip || test -L /usr/lib/python312.zip; then
 jc2_native_visit /usr/lib/python312.zip
else
 printf 'ABSENT /usr/lib/python312.zip\n'
fi
printf 'COUNTS %s %s %s\n' "$jc2_native_file_count" "$jc2_native_dir_count" "${#jc2_native_aliases[@]}"
date -u '+NATIVE_END %Y-%m-%d %H:%M:%S.%N UTC'
