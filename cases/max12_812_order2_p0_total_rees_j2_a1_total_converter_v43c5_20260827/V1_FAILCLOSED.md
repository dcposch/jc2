# V43C5 V1 fail-closed AWS attempt

The frozen V1 AWS run on r6b ended with `rc=1` before constructing or
serializing any converter certificate.  It had already replayed the frozen
source chain, then stopped at the literal-row census assertion

`('literal total map', 59, 70)`.

The two integers have different meanings in the pinned V43 source:

- 59 is the number of nonzero literal total row records; and
- 70 is the number of named row-slot hashes (ten grades times seven rows),
  including 11 slots whose literal polynomial is zero.

Thus V1 has no mathematical verdict.  Its source, preregistration, and AWS
failure bytes remain immutable.  The additive V2 successor checks and records
both censuses and the exact zero-row complement without changing the converter
algebra.

Run metadata: r6b `ip-172-30-0-106`, 2026-08-27 13:27:07Z--13:31:11Z,
243.40 seconds wall time, 153,380 KiB maximum RSS, zero swap, one core.  The
stderr SHA-256 is
`7ee399df9a76105ac321aff599fa7109ef062f9f44dc0f62d0031ad10de88d85`;
the run-metadata SHA-256 is
`16c699e01d2febb17a7cb6a78eb85164484533af5455278db7ed8337c9247536`.
