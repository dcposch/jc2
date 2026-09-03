# box/nextcoeff-drivers-20260903/

Hostile review + EXPERIMENT NEXT-COEFF for the PS-GROWTH flagship
(`xmodel/ps-growth-opus5-20260903.md`). Report:
`xmodel/next-coeff-psreview-grok46-20260903.md`.

Original PS-GROWTH drivers were re-run from the frozen copies (import path
patched to this directory). New experiment: `nextcoeff.py`.

| file | what | log |
|---|---|---|
| `psgrowth.py` | PS-GROWTH checker, K=20 | `psgrowth.log` **1495 / 0** |
| `leadcheck.py` | RESIDUE-LEAD predicted vs measured | `leadcheck.log` **10 / 0** |
| `resdeg.py` | RES-DEGREE + NP1 witness | `resdeg.log` **32 / 0** |
| `existence.py` | 12 census stars, saturated GB | `existence.log` **14 / 0** (print: 12/12 exist; the check only asserts “decided”) |
| `genfun.py` | (GF-P),(GF-R) on A1–A6 to T^{-9} | `genfun.log` **108 / 0** |
| `trio105.py` | D=105 ranges + census K0 | `trio105.log` |
| `nextcoeff.py` | NEXT-COEFF expansions, B6 gate, PS3-NEG, K-channels | `nextcoeff.log` (8.9 s, 59 MB). 22 `FAIL` lines are **experimental mismatches** of the strict deficit=level dictionary, not CAS errors. |

```text
python3 psgrowth.py 20
python3 leadcheck.py
python3 resdeg.py
python3 existence.py
python3 genfun.py
python3 trio105.py
python3 nextcoeff.py
```

sympy 1.12, python3, one core. No ledger edited. No network.
