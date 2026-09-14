set -euo pipefail
date -u '+NATIVE_START %Y-%m-%d %H:%M:%S.%N UTC'
declare -A jc2_native
mapfile -t jc2_bases < <(
 printf '%s\n' /usr/bin/python3 /usr/bin/python3.12
 find /usr/lib/python3.12/lib-dynload -maxdepth 1 -type f -name '*.so'
 find /usr/local/lib/python3.12/dist-packages/flint -type f ! -path '*/test/*' ! -path '*/tests/*'
 find /usr/local/lib/python3.12/dist-packages/python_flint.libs -maxdepth 1 -type f
 printf '%s\n' /usr/local/lib/python3.12/dist-packages/python_flint-0.9.0.dist-info/METADATA
)
for jc2_path in "${jc2_bases[@]}"; do
 jc2_native["$jc2_path"]=1
 jc2_real=$(readlink -f "$jc2_path"); jc2_native["$jc2_real"]=1
 if file -Lb "$jc2_path" | grep -q '^ELF'; then
  while IFS= read -r jc2_dep; do
   test -f "$jc2_dep" || continue
   jc2_native["$jc2_dep"]=1
   jc2_real=$(readlink -f "$jc2_dep"); jc2_native["$jc2_real"]=1
  done < <(ldd "$jc2_path" | awk '/=> \/|^[[:space:]]*\// {for(i=1;i<=NF;i++) if(substr($i,1,1)=="/") print $i}')
 fi
done
printf '%s\n' "${!jc2_native[@]}" | sort | xargs -d '\n' sha256sum
date -u '+NATIVE_END %Y-%m-%d %H:%M:%S.%N UTC'
for jc2_path in "${!jc2_native[@]}"; do
 printf 'REAL %s %s\n' "$jc2_path" "$(readlink -f "$jc2_path")"
done
