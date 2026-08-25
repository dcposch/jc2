# TD6 fixed-A3 q2-beta finite `B3` factors (V67)

Frozen status: **dual-AWS producer-exact source-DAG identities on `D(w)`;
hostile review pending.**

V67 rebuilds the two finite parameter factors left by the V66 birational
`B3=0` chart:

```text
2t-1=0,
t^2-4t+2=0.
```

With `w=V0/U0`, their exact raw-center parameterization is

```text
U0 = w^2 (t-2)^2/(16t),
V0 = w^3 (t-2)^2/(16t),
C0 = w^4 (t-2)^2(-5t^2+20t-4)/(256t^2).
```

The first factor is over `Q(w)` with `t=1/2`; the second is over
`Q(t)(w)` with `t^2-4t+2=0`.  The script checks the inverse formulas and
the raw `B3` identity exactly.  It retains polynomial beta,
`q_beta=t+beta*t^2+t^25`, direct
`q_beta'=1+2 beta t+25 t^24`, fixed `p=t^15`, and frozen F1/pole/
dead-stretch data, with no weighted source scaling.

Both components have ranks

```text
3470/3602 -> 38/132 -> 38/94 -> 25/56.
```

Current row 13 gives `N13=(k/25)beta`, traces through exactly previous row
`('X-1',14)` and original first rows, and is protected by current/previous
edge omission controls.  Previous row `('X-1',0)` is a separate quadratic
cache/control and is not an N13 edge.  Genuine P12 uses 28 original first
rows; its raw term count is 2,893 on `2t-1` and 2,885 on the quadratic
factor.  In both cases it composes with N13 to the unit `-k/50`.

Every source-DAG leaf denominator is a power of the univariate curve
parameter `w`.  The implementation's polynomial generator is printed as
`x` and some legacy markers call it `U_POLY`; it is not the raw center
coordinate `U0`.  Stage denominators are `w^11`; the complete charts are
`w^27` and `w^23`.  Therefore V67 licenses only the two factor opens
`D(w)`.  On either parameterized curve `w=0` is the raw origin, retained as
a separate composition leaf.  This package does not consume the origin
theorem and does not claim whole-factor closure.

## AWS custody

Source archive SHA256:
`13bdaa2a0033eef77088a3a1bc46c7288efde85398f0897107769c04ff404306`.

| factor | host | run directory | rc | stdout SHA256 | max RSS KiB |
|---|---|---|---:|---|---:|
| `2t-1` | Box03 | `/home/ubuntu/runs/td6_v67_b3half_main_box03_20260825T1525Z` | 0 | `f3c25f82457d35bf804b62e4f39f72bf7b65f6a0d1e8eea8f314f1bb3173a98b` | 3,002,732 |
| `2t-1` | Box02 | `/home/ubuntu/runs/td6_v67_b3half_box02_mirror_20260825T1539Z` | 0 | `148fd9ef72d3390f456e057c806e7c4630c568127390db45d0e3fe7029000f70` | 3,000,420 |
| quadratic | Box03 | `/home/ubuntu/runs/td6_v67_b3tq_main_box03_20260825T1525Z` | 0 | `1a65f2a2ee3db2250084adeb6eb2ef12a1ffbbb6db84c096212214b72358bfe6` | 3,438,400 |
| quadratic | Box02 | `/home/ubuntu/runs/td6_v67_b3tq_box02_mirror_20260825T1539Z` | 0 | `46a1608bd37f8f862b13df197c5ba8d60c4f428f4ac81b0342a984cf7c680d8d` | 3,437,592 |

After replacing only each absolute artifact directory, the paired stdout is
byte-identical at SHA256 `bf5b63f1...` (`2t-1`) and `538b70f5...`
(quadratic).  The proof DAG and denominator ledger are byte-identical at
`5fe6def1...` / `1d18859a...` and `d71cf73a...` / `795ca7bc...`.

Separate direct-q-prime omission runs on both factor types print
`direct_qprime_omission_changes_N13=true`, then end rc one in the expected
absent-N13 reporter lookup.  They are negative controls, not theorem
evidence.

Run `python3 verify.py` for a lightweight custody/marker/paired-stream audit.
It performs no substantive algebra.

Scope firewall: no whole factor in this package, no whole `B3=0`, no whole
A3, no other TD6 modulus, no TD6, no SP-2, no landing theorem, and no JC2
conclusion.
