# Hostile review: upper-endpoint origin odd-coupling (Fable5, 2026-08-28)

Compact independent hostile audit of the frozen report
`xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md`
(the exact coupling `D22[X0] = F11[X1]*G11[X0] - F7[X0]*G15[X1] = J(P,Q)(0)`
and the resulting emptiness of the raw all-odd-weight-zero section at the
`D22 = +1` endpoint).

**Verdict: PASS** — no defect found; one non-blocking style note (§7 of the
review). The producer checker was not imported or trusted; all claims were
rebuilt from the frozen `RAW_INPUT.json` by a fresh standalone
standard-library checker.

## Contents

- `../../xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828.md`
  — full review report.
- `../../xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828-check.py`
  — standalone deterministic checker (fresh parser, complete `D22[X0]`
  enumeration, neighbor/prefactor audit, exact Laurent-Jacobian sign
  derivation, parity theorem, byte-pinned firewall sentences, 7-mutation
  detection grid, start/end hash pins).
- `checker_output.txt` — captured full output of the audit run
  (`PYTHONDONTWRITEBYTECODE=1 python3 -B`, repo root; exit 0; marker
  `PASS_HOSTILE_AUDIT_UPPER_ENDPOINT_ORIGIN_ODD_COUPLING_FABLE5`).
- `RESULT.json` — machine-readable verdict and per-item findings.
- `SOURCE.sha256` — frozen audited inputs (report, producer checker, raw
  source), verified unchanged at audit start and end.
- `EVIDENCE.sha256` — final-byte hashes of the review deliverables.

## Replay

```sh
cd <repo-root>
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828-check.py
```
