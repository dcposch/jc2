#!/bin/bash
# ROOT administrative helper inventory; no candidate execution.
set -euo pipefail
if grep -Eq 'JC2_[A-Z0-9_]+_PLACEHOLDER' "$0"; then
 printf '%s\n' 'DISABLED: unresolved ROOT release metadata' >&2
 exit 2
fi
test "$(uname -s)" = Linux
test "$(tr -d '\n' < /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2'
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = JC2_INSTANCE_PLACEHOLDER
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
  test "$jc2_native_file_count" -le 3000
  sha256sum "$jc2_real"
  stat --printf='FILE %s %u %g %a %n\n' "$jc2_real"
  jc2_file=$(file -Lb "$jc2_real")
  if [[ "$jc2_file" == ELF* && "$jc2_file" != *relocatable* ]]; then
   jc2_ldd=$(ldd "$jc2_real")
   [[ "$jc2_ldd" != *'not found'* ]]
   jc2_deps=$(printf '%s\n' "$jc2_ldd" | awk '/=> \/|^[[:space:]]*\// {for(i=1;i<=NF;i++) if(substr($i,1,1)=="/") print $i}')
   while IFS= read -r jc2_dep; do
    test -n "$jc2_dep" || continue
    # ldd on the actual executable already lists the transitive resolved closure.
    jc2_dep_real=$(readlink -e "$jc2_dep")
    if test "$jc2_dep" != "$jc2_dep_real" && test -z "${jc2_native_aliases[$jc2_dep]+yes}"; then
     jc2_native_aliases["$jc2_dep"]="$jc2_dep_real"
     printf 'ALIAS %s %s\n' "$jc2_dep" "$jc2_dep_real"
    fi
    if test -z "${jc2_native_files[$jc2_dep_real]+yes}"; then
     test -f "$jc2_dep_real"
     jc2_native_files["$jc2_dep_real"]=1
     jc2_native_file_count=$((jc2_native_file_count+1))
     test "$jc2_native_file_count" -le 3000
     sha256sum "$jc2_dep_real"
     stat --printf='FILE %s %u %g %a %n\n' "$jc2_dep_real"
    fi
   done <<< "$jc2_deps"
  fi
 fi
}
# Ordinary distribution helper paths and actual ELF loader dependencies.
for jc2_helper in jq bash env systemd-run systemctl timeout ps chrt setpriv test id uname tr hostname readlink date sed awk find sort stat file ldd dpkg-query sha256sum cut head grep install mount findmnt mkfifo sync cmp od basename dirname cat sleep mkdir; do
 jc2_path=$(command -v "$jc2_helper")
 if [[ "$jc2_path" != /* ]]; then jc2_path="/usr/bin/$jc2_helper"; fi
 printf 'HELPER %s %s %s\n' "$jc2_helper" "$jc2_path" "$(readlink -e "$jc2_path")"
 jc2_native_visit "$jc2_path"
done
jc2_native_visit /usr/lib/systemd/systemd
jc2_native_visit /usr/sbin/sshd
jc2_native_visit /etc/ld.so.cache
dpkg-query -W -f='ADMIN_PACKAGE ${Package} ${Version}\n' jq libjq1 bash coreutils systemd systemd-sysv util-linux procps libc6 findutils mawk grep sed file openssh-server
declare -A jc2_protected_ancestors
while IFS= read -r jc2_path; do
 test -n "$jc2_path" || continue
 jc2_protected_ancestors["$jc2_path"]=1
 jc2_real=$(readlink -e "$jc2_path")
 while true; do
  jc2_protected_ancestors["$jc2_real"]=1
  test "$jc2_real" != / || break
  jc2_real=$(dirname "$jc2_real")
 done
 jc2_parent=$(dirname "$jc2_path")
 while true; do
  jc2_protected_ancestors["$jc2_parent"]=1
  test "$jc2_parent" != / || break
  jc2_parent=$(dirname "$jc2_parent")
 done
done < <(printf '%s\n' "${!jc2_native_files[@]}" "${!jc2_native_aliases[@]}"; sed -n -E 's/^[a-f0-9]{64}  (\/.*)$/\1/p;s/^DIRECTORY [0-9]+ [0-9]+ [0-7]+ (\/.*)$/\1/p;s/^ALIAS (\/[^ ]+) .*$/\1/p' /home/ubuntu/jc2-closedchild-preflight9-20260911b/native.stdout)
for jc2_path in "${!jc2_protected_ancestors[@]}"; do
 jc2_real=$(readlink -e "$jc2_path")
 test "$(stat -Lc %u "$jc2_path")" = 0
 jc2_mode=$(stat -Lc %a "$jc2_path")
 test "$((8#$jc2_mode & 8#022))" = 0
 stat -L --printf='PROTECTED %u %g %a %n\n' "$jc2_path"
done
printf 'HELPER_COUNTS %s %s %s PROTECTED %s\n' "$jc2_native_file_count" "$jc2_native_dir_count" "${#jc2_native_aliases[@]}" "${#jc2_protected_ancestors[@]}"
date -u '+ADMIN_END %Y-%m-%d %H:%M:%S.%N UTC'
