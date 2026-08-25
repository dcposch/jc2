# Custody-manifest count correction

`CUSTODY_MANIFEST_ERRATUM.md` correctly identifies and quarantines the seven
non-hash locale-warning lines, but it incorrectly says that the immutable
`MANIFEST.postrun.sha256` contains 89 valid records.  The exact count is **96
valid SHA-256 records plus seven warning lines, for 103 physical lines**.

All 96 valid records verify.  `MANIFEST.postrun.v2.sha256` contains 99 valid
records and verifies strictly; the extra three records are the old manifest,
old freeze, and first erratum.  This correction changes only the stated count.
No source, evidence, result, or mathematical claim changes.

The prior manifests, freezes, and erratum remain immutable.  The active final
case manifest is `MANIFEST.postrun.v3.sha256`, with custody root
`FREEZE.v3.sha256`.

