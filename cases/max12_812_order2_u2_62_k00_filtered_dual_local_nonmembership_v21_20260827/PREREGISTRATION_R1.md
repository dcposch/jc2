# V21R1 source-replay control repair

Date: 2026-08-27

Status: **FROZEN AFTER R0 FAILED CLOSED, BEFORE R1 EXECUTION.**

R0 reached no matrix, dual, or corollary endpoint.  It may be repaired only
as follows:

- test mutual generation of the serialized and freshly computed syzygy
  modules by reducing every component vector and requiring every residual to
  be zero, rather than comparing a module containing zero columns to the
  literal zero module; and
- replace unsupported `exit(integer)` statements by `quit`, while retaining
  mandatory positive sentinels in the Python wrapper.

All exact inputs, hashes, polynomial parsing, syzygy/image/target formulas,
matrix re-emission, dual replay, pairings, lemma, endpoint, dependency
repair, and scope firewalls are unchanged from `PREREGISTRATION.md`.

