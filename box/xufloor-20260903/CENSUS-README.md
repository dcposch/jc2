# Candidate principal-floor census

`xu_screen_candidate.py` is a copy of the frozen charged `xu_screen.py` with
the frozen-input path updated and two parallel result columns:

- `*_promoted`: the charged policy, with principal floor `0` for `u_s > 1`;
- `*_candidate`: the computational candidate `max(V_s/u_s - 1, 0)` for
  `u_s > 1` (unchanged from promoted when `u_s = 1`).

The candidate is deliberately not asserted as a theorem by these programs.

Run from `/home/ubuntu/jc2`:

```bash
set -o pipefail
python3 box/xufloor-20260903/xu_screen_candidate.py \
  2>&1 | tee box/xufloor-20260903/run.log
python3 box/xufloor-20260903/audit_results.py \
  | tee box/xufloor-20260903/audit_summary.json \
        box/xufloor-20260903/audit.log >/dev/null
```

The first command writes `results.json`.  The second is read-only except for
the shell's `tee` outputs and asserts the charged baseline, candidate delta,
all `u_s=1` non-regressions, the direct two-point list, the three named K=16
rows, Xu's three calibrations, and the `(99,66)` / `(108,72)` target bounds.

Measured totals:

```text
                         rows killed   groups killed   groups touched
promoted                   43 / 1420      29 / 686        37 / 686
candidate                  48 / 1420      33 / 686        42 / 686
candidate - promoted       +5             +4              +5
```

Within `u_s > 1` (310 rows / 177 groups), the corresponding promoted counts
are `9 / 7 / 8`, and candidate counts are `14 / 11 / 13`.

Code-model caveat: `IM_max` and `Im_min` remain the charged separate extrema
over the operative full-tree embeddings.  A kill is fail-closed if the
candidate floor is proved, but a survival is not attainment, and the program
does not exploit same-tree correlation.
