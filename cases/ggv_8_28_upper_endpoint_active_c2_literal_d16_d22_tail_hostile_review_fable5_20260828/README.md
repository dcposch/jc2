# Hostile review case: active-c2 literal D16--D22 tail (Fable5, 2026-08-28)

Verdict: **PASS** (six named non-verdict-impacting defects/notes; see report).

Report:
`xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-hostile-review-fable5-20260828.md`

Independent checker (standard library only, no producer imports):
`xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-hostile-review-fable5-20260828-check.py`

Replay:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-hostile-review-fable5-20260828-check.py
```

Expected terminal marker:

```text
PASS_HOSTILE_FABLE5_ACTIVE_C2_LITERAL_D16_D22_TAIL
```

Confirmed independently: prefix D0..D15 with forced `c14=-6139/2^34` and
`g12=4093/2^28`; mode ladder `e=(12-b)/8` complete and annihilating; raw
windows (no F15+ slot, no G22 receiver, G16..G21 windows as frozen);
uniquely solved `c16=0`, `c18=16369/2^47`, `c20=0`; `G16..G21=0`
identically; `D0..D21=0` and homogeneous `D22=0`;
`g22=(9207/2^57)A^-5`; receiver operator `L22(R)=-40A^3A'R-8A^4R'` with
exact kernel `Q*A^-5` and `-L22(g22)=0`; endpoint equation `D22=1` fails.
All eight requested mutation classes executed and caught.

`SOURCE.sha256` covers the five frozen load-bearing inputs plus the
review checker.  `EVIDENCE.sha256` covers the report, this README, and
`RESULT.json` (no self-reference).
