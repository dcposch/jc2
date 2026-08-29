# K00 V27 Singular raw-column semantics probe

Date: 2026-08-27T19:59:47Z

Lifecycle: **EXACT AWS TOOL-SEMANTICS PREFLIGHT / NOT A MATHEMATICAL
ENDPOINT**.

On audited idle AWS host `ip-172-30-0-34` (r6a), Singular 4.3.2 executed
`singular_raw_column_semantics_probe.sing` with SHA-256
`c0f20b096b63ead719f07e13ff667108a1f059348ff1c8230ebe80ee6275594d`.
The exact stdout was:

```text
A_NCOLS=3
A_SIZE=3
B_NCOLS=3
B_SIZE=3
C_NCOLS=5
C_SIZE=5
RAW_COLUMN_SEMANTICS=PASS
```

Thus assignment into an initially empty ideal preserves repeated nonzero
columns, and comma concatenation preserves repeated columns and concatenates
an ideal's columns on the frozen engine.  This clears only the source-storage
mechanism used by the repaired successor runners.  Their literal censuses,
hashes, computations, and mathematical endpoints remain independently
fail-closed.
