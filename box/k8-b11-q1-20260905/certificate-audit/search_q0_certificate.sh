#!/usr/bin/env bash
# Deterministic read-only search for a pre-existing K8, b=11, q0 certificate.
# The campaign-forbidden jc2-lean and ideation-* trees/files are pruned.
set -euo pipefail

cd "$(dirname "$0")/../../.."

case_pattern='K8_B11_Q0|K8 b=11 q0|K=8 b=11 q0'
source_sha='e9278b6b373970afc97b5819cfaa08a1a804638308a1ff50f1553fa0fd1c012d'
body_sha='33e7f3e96e37fc1bb66a02788bbdc7a4b56be649bcf33d92661eb777ef2b7d5a'
active_log='xmodel/k8-b11-q1-sol56-20260905.log'
audit_dir='./box/k8-b11-q1-20260905/certificate-audit'

printf 'SEARCH_ROOT %s\n' "$PWD"
printf 'PRUNED .git jc2-lean **/ideation-* %s %s\n' "$active_log" "$audit_dir"
printf 'PATTERNS %s | %s | %s\n' "$case_pattern" "$source_sha" "$body_sha"

printf '\nFILENAME_HITS_BEGIN\n'
find . \
  \( -path './.git' -o -path './jc2-lean' -o -path "$audit_dir" -o -name 'ideation-*' \) -prune -o \
  -type f \( -iname '*K8*B11*Q0*' -o -iname '*k8*b11*q0*' \) -print \
  | sort
printf 'FILENAME_HITS_END\n'

printf '\nCONTENT_HIT_FILES_BEGIN\n'
rg -l --hidden \
  -g '!.git/**' -g '!jc2-lean/**' -g '!**/ideation-*' -g '!ideation-*' \
  -g '!box/k8-b11-q1-20260905/certificate-audit/**' \
  -g "!${active_log}" -g '!*.ms' \
  -e "$case_pattern" -e "$source_sha" -e "$body_sha" . \
  | sort
printf 'CONTENT_HIT_FILES_END\n'

printf '\nCERTIFICATE_PATH_INVENTORY_COUNT '
find . \
  \( -path './.git' -o -path './jc2-lean' -o -path "$audit_dir" -o -name 'ideation-*' \) -prune -o \
  -type f \( -iname '*lift*' -o -iname '*cofactor*' -o \
                  -iname '*certificate*' -o -name '*.sing' \) -print0 \
  | python3 -c 'import sys; print(sys.stdin.buffer.read().count(b"\0"))'

printf 'CERTIFICATE_CONTENT_HITS_BEGIN\n'
certificate_hits="$(find . \
  \( -path './.git' -o -path './jc2-lean' -o -path "$audit_dir" -o -name 'ideation-*' \) -prune -o \
  -type f \( -iname '*lift*' -o -iname '*cofactor*' -o \
                  -iname '*certificate*' -o -name '*.sing' \) -print0 \
  | sort -z \
  | xargs -0 -r rg -l \
      -e "$case_pattern" -e "$source_sha" -e "$body_sha" \
  || true)"
if [[ -n "$certificate_hits" ]]; then
  printf '%s\n' "$certificate_hits"
fi
printf 'CERTIFICATE_CONTENT_HITS_END\n'

printf '\nMS_INPUT_INVENTORY '
find . \
  \( -path './.git' -o -path './jc2-lean' -o -path "$audit_dir" -o -name 'ideation-*' \) -prune -o \
  -type f -name '*.ms' -printf '%s\n' \
  | awk '{count+=1; bytes+=$1} END {printf "files=%d bytes=%.0f\n",count,bytes}'
printf 'Q0_SOURCE_SHA_FILE_HITS_BEGIN\n'
ms_source_hits="$(find . \
  \( -path './.git' -o -path './jc2-lean' -o -path "$audit_dir" -o -name 'ideation-*' \) -prune -o \
  -type f -name '*.ms' -print0 \
  | sort -z \
  | xargs -0 -r sha256sum \
  | awk -v wanted="$source_sha" '$1 == wanted {print}')"
if [[ -n "$ms_source_hits" ]]; then
  printf '%s\n' "$ms_source_hits"
fi
printf 'Q0_SOURCE_SHA_FILE_HITS_END\n'

printf '\nROUND2_Q0_RECORD_BEGIN\n'
jq '{stem,K,b,nvars,ngens,ms_p0_sha256,body_sha256,extras,exactq,modular}' \
  box/k4ray-strata-r2-20260905/pull/172.30.0.119/K8_B11_Q0.json
printf 'ROUND2_Q0_RECORD_END\n'

printf '\nEARLIER_SOLVE_RECORDS_BEGIN\n'
jq '{stem,char,verdict,form_timed_out,form_wall,ngens_dumped,ms_sha256,msolve_rc,msolve_wall}' \
  box/k4ray-strata-solve-20260905/fleet-pull/172.30.0.60/msolve/K8_B11_Q0_p0.json \
  box/k4ray-strata-solve-20260905/fleet-pull/172.30.0.60/msolve/K8_B11_Q0_p32003.json
sha256sum \
  box/k4ray-strata-solve-20260905/fleet-pull/172.30.0.60/msolve/K8_B11_Q0_p32003.retry.msout
tail -n 1 \
  box/k4ray-strata-solve-20260905/fleet-pull/172.30.0.60/msolve/K8_B11_Q0_p32003.retry.msout
printf 'EARLIER_SOLVE_RECORDS_END\n'

printf '\nF4_RECORD '
rg '^K8_B11_Q0_p0[[:space:]]|^K8_B11_Q0_p32003[[:space:]]' \
  box/k4ray-strata-r2-20260905/f4deg.tsv \
  | tr '\n' ';'
printf '\n'

if [[ -z "$certificate_hits" && -z "$ms_source_hits" ]]; then
  printf 'FINAL_DISPOSITION NO_PREEXISTING_Q0_RATIONAL_COFACTOR_FOUND\n'
else
  printf 'FINAL_DISPOSITION POTENTIAL_Q0_CERTIFICATE_HITS_REQUIRE_REVIEW\n'
fi
