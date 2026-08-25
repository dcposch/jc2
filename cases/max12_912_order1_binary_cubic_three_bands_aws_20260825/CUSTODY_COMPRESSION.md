# Partial-case custody compression

This is a storage-only custody supplement for an incomplete case.  It does
not freeze or promote the three-band computation.

- Original path: `evidence/r6d/squarefree/singular.stdout`
- Original size: `97687924` bytes
- Original SHA-256:
  `72929ca3b7c8136bf381135fa7e19b15d54a0e067beba268541fe1e6e89cfe27`
- Replacement path: `evidence/r6d/squarefree/singular.stdout.gz`
- Compression: deterministic `gzip -n -9`
- Replacement size: `27040080` bytes
- Replacement SHA-256:
  `7224dd2b1b2ea70919854470d2acb1f6907fb9cf615a3174b8740057dde1e214`
- `gzip -dc` SHA-256:
  `72929ca3b7c8136bf381135fa7e19b15d54a0e067beba268541fe1e6e89cfe27`

The decompressed hash exactly matches the raw hash.  Only the exact raw file
named above was removed after that check; it is recoverable byte-for-byte from
the gzip member, and the remote AWS evidence remains unchanged.  No
incomplete-case manifest existed at the time of this supplement, so there was
no manifest to update.
