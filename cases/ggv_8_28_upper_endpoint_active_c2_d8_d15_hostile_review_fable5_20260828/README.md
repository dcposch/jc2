# Hostile review: active-c2 D8--D15 repair/extension (Fable 5)

Status: **REPAIR — DIFFERENT-MODEL HOSTILE REVIEW COMPLETE**

Independent, fully self-contained audit of the frozen deep active-`c2`
D8--D15 repair/extension.  The single authoritative checker lives in
xmodel (one checker, no copies):

```text
xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828-check.py
```

It reconstructs the fractional-power characteristic recurrence from
`F*ydot = e*Fdot*y` with all ten modes `c2,...,c20`, certifies it against
the determinant rows on a generic rational point, independently verifies
every charged D8--D11 identity, exhibits the exact surviving pole
`(N11+4*d1*B11r0)/(4194304A)` that refutes the charged `A|D` valuation
claim, confirms the exact `D=0` extension through D15, replays the
literal raw survivor (windows, forced `c14=-6139/2^34`, verified
q1-freeness), keeps the `c2=0` companion separate, and runs seven
sensitivity mutations.  Producer files are hash-pinned only; no producer
code is imported.

Replay (from the repository root):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828-check.py
```

Expected terminal marker:

```text
FABLE5_HOSTILE_ACTIVE_C2_D8_D15=REPAIR
```

On replay the checker re-verifies all seven frozen input hashes (start
and end) and asserts `RESULT.json` in this directory byte-exactly.
Report: `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828.md`.
Manifests: `SOURCE.sha256` (frozen inputs + authoritative checker),
`EVIDENCE.sha256` (report, this README, RESULT.json, checker).

Scope: characteristic-zero field/radical necessity plus one literal
rational fixture.  No scheme membership, endpoint emptiness, q1
exclusion, branch-P exclusion, Keller, or JC2 claim.
