# V6 compiler fail-closed result

Date: 2026-08-26 19:29Z

Verdict: **COMPILER-ONLY FAILURE; NO SINGULAR ROW SHARD RAN AND NO
MATHEMATICAL RESULT.**

Both frozen good-prime lanes verified their V6 and V2 freeze manifests and
generated the complete frozen stream source.  The row splitter itself found
the seven intended blocks, but the final row-program census counted the
deliberate release assignment `TPhi=0;` as a second `TPhi` formula and raised

```text
RuntimeError: ('row shard TPhi census', 1)
```

before any row input was written or Singular started.  V7 changes only that
assertion to count one nonzero formula assignment and one release assignment.
The common source archive SHA-256 was
`ca505fd7a80bc92727805ea97dc990230db8b59b055bc784212b74f84594558c`.
Harvested records are frozen in `FAILCLOSED_EVIDENCE.sha256`.
