# box/psgrowth-drivers-20260903/ — PS-GROWTH lane drivers (Opus 5, 2026-09-03)

Report: `xmodel/ps-growth-opus5-20260903.md`.  Desk scale: whole directory
re-runs in < 12 min on one core, < 1 GB, except `starres2.py`'s (2,3,2) row.

| file | what it does | log |
|---|---|---|
| `psgrowth.py` | the PS-GROWTH checker: chi = Res_y(g-c,T-f), P_k by Newton, R_k by reduction, PS-0/PS-1'/PS-1/PS-1c/PS-2/PS-3/PS-3+, cmax and the whole `{-ord_t f(tau_i)}` multiset from chi's Newton polygon; positive controls n=2..6 + the degree-15 composition; non-Keller negatives; vacuity guard; OPEN[PS-VACUITY] sweep k<=20 | `psgrowth.log` (1495 checks, 0 failures) |
| `starres.py` | RESIDUE-LEAD via `sp.solve` — **SUPERSEDED**, its solution sets are incomplete (it reports no (2,3,2) star; one exists) | `starres.log` |
| `existence.py` | BOTTOM-ODE star existence for the 12 census-relevant (d,e,V), saturated Groebner, with controls | `existence.log` (14 checks, 0 failures) |
| `starres2.py` | RESIDUE-LEAD via saturated Groebner + ideal-membership vanishing test, with positive/negative controls on the test itself | `starres2.log` |
| `leadcheck.py` | end-to-end: PREDICT `{k : PS-3 attained}` from the bottom star, MEASURE it on the pair | `leadcheck.log` (10 checks, 0 failures) |
| `genfun.py` | control on the second proof of PS-1: (GF-P) `sum P_k T^{-k-1} = d/dT log chi` and (GF-R) `sum R_k T^{-k-1} = -(1/J) d/dx log chi` | `genfun.log` (108 checks, 0 failures) |
| `resdeg.py` | RES-DEGREE measured and corrected, with a refutation witness for the charged form | `resdeg.log` (32 checks, 0 failures) |
| `trio105.py` | the D=105 trio's (q, e, cmax) and forced-vanishing ranges; how the range grows with D over the census | `trio105.log` |

Run: `python3 psgrowth.py 20`, `python3 leadcheck.py`, `python3 resdeg.py`,
`python3 trio105.py`, `python3 existence.py`, `python3 genfun.py`,
`python3 starres2.py [d,e,V ...]`.
