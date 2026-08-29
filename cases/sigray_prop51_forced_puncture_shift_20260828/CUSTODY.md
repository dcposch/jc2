# Custody: Sigray Proposition 5.1 forced-puncture-shift repair

Date: 2026-08-28

Primary source:

```
refs/sigray_full.pdf
SHA256 9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
```

Page custody (printed page equals PDF page):

- p. 18: Proposition 4.1, condition (7), equation (8).
- pp. 20--21: Proposition 4.3 and Notation 4.2 (`g-b`, `m_{F,b}`).
- pp. 23--24: Proposition 5.1 and Notation 5.1.
- pp. 35--37: Proposition 7.2 and Proposition 7.3 (`b=q(c)=g(P)`).

Producer:

```
xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md
```

Exact arithmetic control:

```
cases/sigray_prop51_forced_puncture_shift_20260828/verify_threshold.py
```

The checker is standard-library only and does not construct an Eggers--Wall
tree.  It checks only the coefficient and piecewise-linear arithmetic exposed
in the producer.

No canonical ledger is modified by this artifact.
