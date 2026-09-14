#!/usr/bin/env bash
# Run Singular with GNU time custody.  solve_class.py owns the 600 s process-
# group watchdog; this wrapper exists only so guided_gb stdout/stderr keep the
# solver's peak-RSS and wall-clock record beside its machine markers.
set -euo pipefail

singular_bin=${GI_SINGULAR_BIN:-Singular}
exec /usr/bin/time -v "$singular_bin" "$@"
