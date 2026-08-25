# Readable source-custody supplement for the TD6 P3 gate

The immutable theorem package
`cases/td6_c1_c2_c3_p3_raw_curve_aws_20260825/` preserves its exact producer
inside the pinned V17 compressed archive.  A hostile reviewer with Bash and
all execution tools disabled cannot inspect source bytes inside that archive.

This separate supplement is a byte-for-byte readable extraction of the V17
payload.  It does not alter or extend the theorem package.  In particular:

- original archive SHA-256:
  `b207bbba13ee20d2719ef15504df632f66674d69072d97b83f4c9970d53e0e98`;
- extracted `payload/SOURCE.sha256` SHA-256:
  `7b00ab87e35ca9b2cff9d31d7e0e75cd5cd4fbf5fbe64d1ad68f300c39a2032f`;
- P3 producer SHA-256:
  `1b492ad26a2f1c0cdc3ae3983068639163118010ffba9e53c9e6d097d56c9a22`.

Every file listed by `payload/SOURCE.sha256` is present and hash-checked.
There are no bytecode/cache files.  This supplement is for read-only review;
the executable evidence and mathematical verdict remain those of the
separately frozen AWS package.
