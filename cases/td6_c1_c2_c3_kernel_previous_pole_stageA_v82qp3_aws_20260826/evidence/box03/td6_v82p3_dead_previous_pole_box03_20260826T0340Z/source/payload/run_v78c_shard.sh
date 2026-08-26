#!/usr/bin/env bash
set -euo pipefail

test "$(uname -s)" = Linux || {
  echo "REFUSE: V78C shard requires registered AWS Linux" >&2
  exit 97
}
test -n "${TD6_REGISTERED_AWS_TAG:-}" || {
  echo "REFUSE: missing TD6_REGISTERED_AWS_TAG" >&2
  exit 98
}
test -n "${TD6_Q_EXPONENT:-}" || {
  echo "REFUSE: missing TD6_Q_EXPONENT" >&2
  exit 99
}
case ",2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24," in
  *",${TD6_Q_EXPONENT},"*) ;;
  *) echo "REFUSE: unlicensed q exponent ${TD6_Q_EXPONENT}" >&2; exit 100 ;;
esac

printf 'aws_platform=%s\n' "$(uname -s)"
printf 'aws_hostname=%s\n' "$(hostname)"
printf 'aws_run_tag=%s\n' "$TD6_REGISTERED_AWS_TAG"
python3 jc2/cases/td6_c1_c2_c3_all_q_vector_ad_repaired_20260825/replay_shard.py p12

