#!/bin/bash
# Final manifest of the lane directory (run after all producers have stopped).
cd "$(dirname "$0")"
rm -f SHA256SUMS.final
find . -type f ! -name SHA256SUMS.final -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.final
sha256sum -c SHA256SUMS.final --quiet && echo "MANIFEST_OK files=$(wc -l < SHA256SUMS.final) sha256=$(sha256sum SHA256SUMS.final | cut -d' ' -f1)"
