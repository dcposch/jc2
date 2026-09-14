# Operative-flag ablation (hostile gate, 2026-09-05)

`Tree(n,m,Ms, gate=?, ode=?, recenter=?, capacity=False, passport=False)` over the
23,720 core rows of `census(n<=200, Kmin=16, full=True)`, with the same
`d_s > V_s > d_s/2` top-window guard the operative driver applies.

| variant | rows | vs baseline (1,420) | wall |
|---|---:|---|---:|
| `gate=F ode=T rec=T`  (operative baseline) | 1,420 | — | 13.3 s |
| `gate=F ode=F rec=T`  (`ode` off)          | 1,691 | +271 / -0 | 13.7 s |
| `gate=F ode=T rec=F`  (`recenter` off)     | 2,824 | +1,404 / -0 | 15.9 s |
| `gate=T ode=T rec=T`  (`gate` on)          | 10,606 | +9,186 / -0 | 624.2 s |
| `gate=F ode=F rec=F`  (all off)            | 3,090 | +1,670 / -0 | 32.4 s |

Every variant is a strict superset of the baseline: each flag only removes rows.
`gate=False` (reject a still-dangerous path at the bottom regardless of free exponents)
is the largest single necessity in the screen.

Raw stdout for the last two variants: `ablation2.log`.
Reproduce: see the inline scripts quoted in the gate report's replay block, or rerun
`gate_replay.py` with the `evaluate(...)` kwargs varied.
