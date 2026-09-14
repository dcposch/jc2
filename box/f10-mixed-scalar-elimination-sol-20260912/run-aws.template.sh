#!/bin/sh
# DISABLED/UNBOUND. Binding and execution require separate review and ROOT registration.
set -eu
[ "$#" -eq 4 ] || { echo 'REFUSED: argv' >&2; exit 64; }
[ "$1" = '--registered-job' ] || { echo 'REFUSED: registration flag' >&2; exit 64; }
[ "$2" = '@REGISTERED_JOB_TAG@' ] || { echo 'REFUSED: job tag' >&2; exit 64; }
mode=$3
out=$4
[ "$(uname -s)" = Linux ] || { echo 'REFUSED: Linux only' >&2; exit 65; }
[ -r /sys/class/dmi/id/sys_vendor ] || { echo 'REFUSED: no DMI' >&2; exit 65; }
[ "$(sed -n '1p' /sys/class/dmi/id/sys_vendor)" = 'Amazon EC2' ] || {
  echo 'REFUSED: off AWS' >&2; exit 65;
}
[ "$(id -u)" = '@UNPRIVILEGED_UID@' ] || { echo 'REFUSED: uid' >&2; exit 65; }
[ -d "$out" ] && [ ! -L "$out" ] || { echo 'REFUSED: output directory' >&2; exit 66; }
[ "$(sha256sum '@SOURCE_DIR@/eliminate.sing' | awk '{print $1}')" = '@ELIMINATE_SHA256@' ] || exit 66
[ "$(sha256sum '@SOURCE_DIR@/check-certificate.sing' | awk '{print $1}')" = '@CHECKER_SHA256@' ] || exit 66
case "$mode" in
  generate) script='@SOURCE_DIR@/eliminate.sing' ;;
  check) [ -f "$out/certificate.sing" ] || exit 66; script='@SOURCE_DIR@/check-certificate.sing' ;;
  *) echo 'REFUSED: mode' >&2; exit 64 ;;
esac
cd "$out"
exec /usr/bin/Singular -q "$script"
