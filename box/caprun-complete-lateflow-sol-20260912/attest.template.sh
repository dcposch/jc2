#!/bin/bash
# SEPARATE ROOT-owned metadata decision. RECIPE.js never invokes this file.
set -euo pipefail
test "$#" = 4
test "$1" = ROOT_EXPLICITLY_ATTESTS_OBSERVED_LIVE_STATE_NOT_RELEASE
jc2_observation="$2"
jc2_prepared_pins="$3"
jc2_decision="$4"
test ! -e "$jc2_decision"
test ! -L "$jc2_decision"
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_HOLDER_CUTOFF_PLACEHOLDER' +%s)"
test "$(date -u +%s)" -lt "$(date -ud 'JC2_ORIGINAL_ADMISSION_STOP_PLACEHOLDER' +%s)"
jq -e '.schema=="caprun-late-observation/v1" and .context=="ROOT_ATTESTED_CANDIDATE" and (.leaves|length)==9' "$jc2_observation" >/dev/null
jq -e 'keys|sort==["AUTHORITIES.preholder.json","ROOT-EXECUTION-CARD.preholder.md","ROOT-REGISTRATION.preholder.json","final-install.preholder.sh"]' "$jc2_prepared_pins" >/dev/null
jc2_observation_sha=$(sha256sum "$jc2_observation" | cut -d ' ' -f 1)
umask 077
set -o noclobber
jq -n --argjson prepared_pins "$(<"$jc2_prepared_pins")" --arg observation_sha256 "$jc2_observation_sha" '{schema:"ROOT_METADATA_BINDING_ONLY_NOT_RELEASE",context:"ROOT_ATTESTED_CANDIDATE",prepared_pins:$prepared_pins,observation_sha256:$observation_sha256,enabled:true,exclusive_no_concurrent_writer:true,root_no_migration:true,freeze_token:"ROOT_FREEZE_EXACT_PREFLIGHT9_REGISTRATION_ONLY"}' > "$jc2_decision"
chmod 0400 "$jc2_decision"
sha256sum "$jc2_observation" "$jc2_prepared_pins" "$jc2_decision"
# Invocation is the ROOT decision. This script does not inspect or authorize release.
