# Custody-manifest erratum

The immutable `MANIFEST.postrun.sha256` at SHA-256
`4409325ec61c8b8f724f94e230d853c1b8ba4651e15ac735a59d43e696f2aac1`
contains 89 valid SHA-256 records, all of which verify, but it also contains
seven leading Perl locale-warning lines.  Those lines were captured from
merged diagnostic output while the manifest patch was assembled.  They are
not hash records, so strict `shasum -c` reports seven malformed lines.

No evidence or source byte is affected.  The old manifest and
`FREEZE.sha256` remain immutable negative custody controls.
`MANIFEST.postrun.v2.sha256` is regenerated after this erratum with `LC_ALL=C`
and contains only valid records.  It includes the old manifest, old freeze,
and this erratum.  `FREEZE.v2.sha256` is the active custody root.

