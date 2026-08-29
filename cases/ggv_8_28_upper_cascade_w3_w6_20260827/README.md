# Exact upper-face cascade through D6

This case replays the branch-P/branch-Q cascade theorem in the companion
xmodel report.  It uses pure Python exact rational arithmetic; runtime is
about three seconds on a laptop.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_upper_cascade.py --check
```

The replay checks universal Laurent identities, three saturated raw-window
fixtures, determinant rows `D0..D6`, gate mutations, solution dimensions,
and the two q1-negative square controls.  It does not solve or sample the
endpoint equation `D22=1`.

