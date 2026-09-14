#!/usr/bin/env bash
# Validate the closed full presentation and derive the exact-Q/second-prime inputs.
set -Eeuo pipefail

readonly BASE=/home/ubuntu/t2t3-full
readonly FULL=$BASE/presentations/full
readonly SUBSET=$BASE/presentations/d2-z55
readonly PREFIX=$BASE/presentations/sound-prefix500
readonly META=$FULL/99-delta2.build.json
readonly MS1=$FULL/99-delta2.ms
readonly SING_STD=$FULL/99-delta2.sing
readonly MS2=$FULL/99-delta2-p1073741783.ms
readonly SING_SLIM=$FULL/99-delta2-slimgb.sing

[[ $(< "$BASE/logs/full-build.rc") == 0 ]]
[[ ! -e $PREFIX && ! -e $MS2 && ! -e $SING_SLIM ]]

/usr/bin/python3 - "$META" <<'PY' > "$BASE/logs/full-presentation-validation.json"
import hashlib
import json
import pathlib
import sys

meta_path = pathlib.Path(sys.argv[1])
meta = json.loads(meta_path.read_text())
assert meta["schema"] == "T2T3_DIRECT_BUILD/v1"
assert meta["status"] == "EMITTED_EXACT_Q_AND_MODULAR_NOT_RUN"
assert meta["case"] == "99-delta2" and meta["field"] == "Q"
assert meta["input_sha256"] == "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea"
assert meta["semantic_variable_count"] == meta["solver_variable_count"] == 449
assert meta["semantic_variable_order_sha256"] == "ee778e93b4293b9399761911d80dd71dd63b5fa95d21055cf50cd0db51428a4b"
assert meta["order"]["matrix_flat_sha256"] == "547fabda8bf5874666699a9e296a06b796299774191b59583e156001d6e5cf00"
assert meta["modular_prime"] == 1073741827
assert meta["raw_row_count"] == 4470
assert meta["emitted_generator_count"] == 2754
assert sum(meta["identically_zero_after_substitution"].values()) == 1716
assert meta["emitted_nonzero_counts"] == {
    "T2_face": 17, "T2_strict": 1263, "T2_upper": 462,
    "T3_face": 46, "T3_recurrence": 1, "T3_strict": 962, "inverse": 3,
}
stream_sha = meta["canonical_primitive_generator_sequence_sha256"]
assert len(stream_sha) == 64 and all(c in "0123456789abcdef" for c in stream_sha)

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(16 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

root = meta_path.parent
checks = {
    meta["singular_file"]: meta["singular_file_sha256"],
    meta["msolve_file"]: meta["msolve_file_sha256"],
    meta["labels_file"]: meta["labels_file_sha256"],
    meta["variable_map_file"]: meta["variable_map_sha256"],
}
actual = {name: sha(root / name) for name in checks}
assert actual == checks
print(json.dumps({
    "schema": "T2T3_FULL_PRESENTATION_VALIDATION/v1",
    "valid": True,
    "metadata_sha256": sha(meta_path),
    "artifact_sha256_recomputed": actual,
    "canonical_primitive_generator_sequence_sha256": stream_sha,
    "raw_rows": 4470,
    "zero_rows": 1716,
    "emitted_generators": 2754,
    "variables": 449,
}, indent=2, sort_keys=True))
PY

/usr/bin/python3 "$BASE/drivers/verify_literal_subset.py" "$FULL" "$SUBSET" \
  > "$BASE/logs/subset-inclusion.json"

/usr/bin/python3 "$BASE/drivers/make_sound_prefix.py" \
  --case 99-delta2 --rows 500 --source-dir "$FULL" --output-dir "$PREFIX" \
  > "$BASE/logs/sound-prefix500.stdout" &
prefix_pid=$!

(
  [[ $(grep -Fxc 'ideal G=std(I);' "$SING_STD") == 1 ]]
  sed 's/^ideal G=std(I);$/ideal G=slimgb(I);/' "$SING_STD" > "$SING_SLIM"
  [[ $(grep -Fxc 'ideal G=slimgb(I);' "$SING_SLIM") == 1 ]]
  original_sha=$(sha256sum "$SING_STD" | cut -d' ' -f1)
  reverse_sha=$(sed 's/^ideal G=slimgb(I);$/ideal G=std(I);/' "$SING_SLIM" | sha256sum | cut -d' ' -f1)
  [[ $reverse_sha == "$original_sha" ]]
  sha256sum "$SING_SLIM" > "$BASE/logs/slimgb.sha256"
  printf 'source_sha256=%s\nreverse_transform_sha256=%s\nreplacement_count=1\n' \
    "$original_sha" "$reverse_sha" > "$BASE/logs/slimgb-derivation.txt"
) &
slim_pid=$!

(
  {
    IFS= read -r aliases
    IFS= read -r prime
    [[ $prime == 1073741827 ]]
    printf '%s\n1073741783\n' "$aliases"
    cat
  } < "$MS1" > "$MS2"
  [[ $(sed -n '2p' "$MS2") == 1073741783 ]]
  offset=$(head -n 2 "$MS1" | wc -c)
  [[ $offset == $(head -n 2 "$MS2" | wc -c) ]]
  cmp -s -i "$offset:$offset" "$MS1" "$MS2"
  sha256sum "$MS2" > "$BASE/logs/p1073741783.sha256"
  printf 'source_prime=1073741827\nderived_prime=1073741783\nbody_from_line3_byte_identical=true\nbyte_offset=%s\n' \
    "$offset" > "$BASE/logs/p1073741783-derivation.txt"
) &
prime_pid=$!

wait "$prefix_pid"
wait "$slim_pid"
wait "$prime_pid"

sha256sum "$BASE/logs/full-presentation-validation.json" \
  "$BASE/logs/subset-inclusion.json" "$PREFIX/prefix.json" \
  "$BASE/logs/slimgb-derivation.txt" "$BASE/logs/p1073741783-derivation.txt" \
  > "$BASE/logs/preparation-artifacts.sha256"
date -u +%Y-%m-%dT%H:%M:%SZ > "$BASE/logs/preparation-complete.utc"
