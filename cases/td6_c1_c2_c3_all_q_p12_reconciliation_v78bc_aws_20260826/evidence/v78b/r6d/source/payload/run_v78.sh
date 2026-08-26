#!/bin/sh
set -eu

mode=${1:?usage: run_v78.sh p12|staged}
case "$mode" in p12|staged) ;; *) exit 2 ;; esac

[ "$(uname -s)" = Linux ] || {
  echo "AWS preflight refused non-Linux platform" >&2
  exit 97
}
[ -n "${TD6_REGISTERED_AWS_TAG:-}" ] || {
  echo "AWS preflight requires TD6_REGISTERED_AWS_TAG" >&2
  exit 98
}
case "$(hostname)" in ip-*) ;; *)
  echo "AWS preflight refused unregistered hostname $(hostname)" >&2
  exit 99
esac

root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
cd "$root"
sha256sum -c SOURCE.sha256
mkdir -p "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
echo "aws_platform=$(uname -s)"
echo "aws_hostname=$(hostname)"
echo "aws_run_tag=$TD6_REGISTERED_AWS_TAG"
echo "mode=$mode"
python3 jc2/cases/td6_c1_c2_c3_all_q_vector_ad_20260825/replay.py "$mode"
