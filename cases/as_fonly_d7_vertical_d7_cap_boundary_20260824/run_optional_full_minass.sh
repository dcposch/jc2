#!/bin/sh
set -eu

case_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$case_dir"

variant=${1:-}
output=${2:-}
if [ -z "$variant" ] || [ -z "$output" ]; then
  printf '%s\n' "usage: $0 {subsystem|char-dp|char-xfirst} OUTPUT" >&2
  exit 64
fi

case "$variant" in
  subsystem) input=optional_full_minass_subsystem.sing ;;
  char-dp) input=optional_full_minass_char_dp.sing ;;
  char-xfirst) input=optional_full_minass_char_xfirst_lp.sing ;;
  *) printf '%s\n' "unknown variant: $variant" >&2; exit 64 ;;
esac

if command -v Singular >/dev/null 2>&1; then
  singular_bin=$(command -v Singular)
elif command -v singular >/dev/null 2>&1; then
  singular_bin=$(command -v singular)
else
  printf '%s\n' 'Singular executable not found' >&2
  exit 69
fi

if command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c MANIFEST.sha256
  input_hash=$(sha256sum "$input" | awk '{print $1}')
else
  shasum -a 256 -c MANIFEST.sha256
  input_hash=$(shasum -a 256 "$input" | awk '{print $1}')
fi

printf 'variant %s\ninput %s\ninput_sha256 %s\n' "$variant" "$input" "$input_hash"
"$singular_bin" --version | sed -n '1,3p'
"$singular_bin" -q "$input" > "$output"
if ! grep -q '^PASS-D7-JOINT-' "$output"; then
  printf '%s\n' "completed without registered PASS marker: $output" >&2
  exit 1
fi
printf 'output %s\n' "$output"
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$output"
else
  shasum -a 256 "$output"
fi
