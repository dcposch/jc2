# guided_gb timeout-contract patch (2026-09-05)

Drivers for the `guided-gb-timeout-fix-grok46` lane.

- `guided_gb.py.diff` — full patch against frozen `box/lib/guided_gb.py`
- `unit-test-results.json` — 12/12 PASS
- `control-replay.json` — census-sweep five-control verdict identity
- `census-certs/` — replayed certificates only (no 12 MiB script copies)
- `repro.log` — unpatched TimeoutExpired / unstaged timeout vs patched typed stage

Large copies (`census-controls/`, `unit/`) are local-only.
