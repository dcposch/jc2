# V20R2 evidence-manifest custody erratum

Date: 2026-08-27

The successful R2 wrapper constructed
`run/ENDPOINT_EVIDENCE.sha256.tmp` inside the directory being walked, so its
`find` command included that temporary file in the manifest and then renamed
it.  The preserved original manifest therefore has one necessarily broken
self-entry.  This is an additive custody defect; it changes no source,
calculation, result, or evidence byte.

All other 21 walked entries replayed after rebasing the registered remote
prefix to the harvested path.  The two registration/freeze records also
replayed independently.  The clean manifest
`HARVEST_EVIDENCE_R2.sha256` is stored outside its own walked set and covers
all 23 files.  The original defective manifest is preserved byte-for-byte at
SHA-256
`72277a97af9a72dabb7c491a860018357eed7133fba9b1ff6f9676a6645397e4`.

No algebra rerun was performed or needed.  This repair licenses custody of
the compiler-only producer packet, not a nonlinear stratum or jet verdict.

