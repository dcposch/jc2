#!/bin/sh
set -eu

[ "$(uname -s)" = Linux ] || {
  echo "AWS preflight refused non-Linux platform" >&2
  exit 97
}
[ -n "${TD6_REGISTERED_AWS_TAG:-}" ] || {
  echo "AWS preflight requires TD6_REGISTERED_AWS_TAG" >&2
  exit 98
}
case "$(hostname)" in ip-*) ;; *)
  echo "AWS preflight refused hostname $(hostname)" >&2
  exit 99
esac
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || {
  echo "AWS preflight refused non-EC2 DMI identity" >&2
  exit 96
}

root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
cd "$root"
sha256sum -c SOURCE.sha256
: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
mkdir -p "$TD6_OUTPUT_DIR"
echo "aws_platform=$(uname -s)"
echo "aws_hostname=$(hostname)"
echo "aws_run_tag=$TD6_REGISTERED_AWS_TAG"
python3 jc2/cases/td6_c1_c2_c3_all_q_vector_ad_repaired_20260825/replay.py p12
