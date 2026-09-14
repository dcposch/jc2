#!/bin/bash
# READ-ONLY metadata; no Python/module/CAS execution or package installation.
set -euo pipefail
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-08d2a40f272ee9fa2
test -f /usr/bin/python3.12
test -d /usr/lib/python3.12
test -x /usr/bin/setpriv
date -u '+NATIVE_START %Y-%m-%d %H:%M:%S.%N UTC'
hostname
readlink /proc/self/ns/pid
sed -n '1p' /proc/sys/kernel/random/boot_id
dpkg-query -W -f='${Package} ${Version}\n' python3.12 python3.12-minimal libpython3.12-stdlib util-linux procps
declare -A jc2_native
jc2_listing=$(
 printf '%s\n' /usr/bin/python3 /usr/bin/python3.12 /usr/bin/setpriv || exit 2
 # Match the unchanged CAPRUN's fixed ps preference, not shell PATH discovery.
 if test -f /bin/ps && test -x /bin/ps; then
  printf '%s\n' /bin/ps || exit 2
 elif test -f /usr/bin/ps && test -x /usr/bin/ps; then
  printf '%s\n' /usr/bin/ps || exit 2
 else
  exit 2
 fi
 if test -e /usr/lib/python312.zip || test -L /usr/lib/python312.zip; then
  test -f /usr/lib/python312.zip || exit 2
  printf '%s\n' /usr/lib/python312.zip || exit 2
 fi
 if command -v rg >/dev/null 2>&1; then
  rg --files --hidden --no-ignore /usr/lib/python3.12 |
   awk '/\.(py|pyc|so)$/ && !/\/(site-packages|dist-packages)\//' || exit 2
 else
  find /usr/lib/python3.12 \( -type f -o -type l \) \
   \( -name '*.py' -o -name '*.pyc' -o -name '*.so' \) \
   ! -path '*/site-packages/*' ! -path '*/dist-packages/*' || exit 2
 fi
)
test -n "$jc2_listing"
mapfile -t jc2_bases <<< "$jc2_listing"
if ! test -e /usr/lib/python312.zip && ! test -L /usr/lib/python312.zip; then
 printf 'ABSENT /usr/lib/python312.zip\n'
fi
for jc2_path in "${jc2_bases[@]}"; do
 jc2_real=$(readlink -f "$jc2_path")
 test -f "$jc2_real"
 jc2_native["$jc2_real"]=1
 printf 'ALIAS %s %s\n' "$jc2_path" "$jc2_real"
 jc2_file=$(file -Lb "$jc2_real")
 if [[ "$jc2_file" == ELF* ]]; then
  jc2_ldd=$(ldd "$jc2_real")
  if [[ "$jc2_ldd" == *'not found'* ]]; then
   printf 'MISSING_ELF_DEPENDENCY %s\n' "$jc2_real" >&2
   exit 2
  fi
  jc2_deps=$(printf '%s\n' "$jc2_ldd" |
   awk '/=> \/|^[[:space:]]*\// {for(i=1;i<=NF;i++) if(substr($i,1,1)=="/") print $i}')
  while IFS= read -r jc2_dep; do
   test -n "$jc2_dep" || continue
   jc2_resolved=$(readlink -f "$jc2_dep")
   test -f "$jc2_resolved"
   jc2_native["$jc2_resolved"]=1
   printf 'ALIAS %s %s\n' "$jc2_dep" "$jc2_resolved"
  done <<< "$jc2_deps"
 fi
done
# The canonical manifest can be large; a separately pinned file will carry it.
printf '%s\n' "${!jc2_native[@]}" | sort |
 while IFS= read -r jc2_path; do
  sha256sum "$jc2_path"
  stat --printf='FILE %s %u %g %a %n\n' "$jc2_path"
 done
date -u '+NATIVE_END %Y-%m-%d %H:%M:%S.%N UTC'
