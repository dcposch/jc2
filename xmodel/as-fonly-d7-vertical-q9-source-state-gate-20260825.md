# AS F-only `D=7`: exact Q9 source-state gate

**Status: PRODUCER EXACT; PROVISIONAL PENDING INDEPENDENT SOURCE/RESULT
REVIEW.**

The source-corrected finite branch remains nonempty through the next typed
row.  Starting from the exact 33,225 corrected-Q10 states, the producer
restores `C2,D2`, `C4,D4`, and `W7,Z7`, then solves the 23 affine rows

```text
E_1=0, E_3=0, F_6=0,
G_9=M_9/3+{C,D}_9+T_9=0 mod 3,
T=A Z_y+W_x V_y-U_y Z_x-W_y V_x.                 (1)
```

The compiler reconstructs canonical integer representatives, proves every
division before reducing modulo three, rechecks the accepted degree
12/11/10 source rows, proves the six current degree-six Frobenius variables
are spectators here, and substitutes a canonical witness back into all 23
rows.

The exact 27-way AWS census is

```text
corrected-Q10 predecessor states                    33,225
Q9-compatible predecessor states                    11,881
Q9-incompatible predecessor states                  21,344
relevant restored-layer completions       8,096,356,425,843
including the 729 current spectators     5,902,243,834,439,547. (2)
```

Compatible matrix ranks are 13, 15, and 16, with fibre sizes `3^19`,
`3^17`, and `3^16`; the exact rank/augmented-rank and structural-base
histograms are frozen in the portable case.  Seventy-nine of 2,187
structural bases survive.  Thus Q9 is a strong shrink, not a branch death.

Execution was on Box02, tag `as_d7_q9_state_20260825T011049Z`, from
`2026-08-25T01:12:19Z` to `01:16:10Z`, with overall/aggregate return codes
zero.  The ordered output Merkle root is

```text
31b77bef882a784b43ee146d930f192385714efce730b9126c8c2df4038b7be7. (3)
```

The frozen case is
`cases/as_fonly_d7_vertical_q9_state_gate_20260825/`; its bounded portable
check is `./verify_frozen_results.sh`.  It verifies source, runner, and
result hashes and regenerates the aggregate, but intentionally does not
rerun the AWS enumeration.

This producer licenses only nonemptiness of the displayed Q9 affine
extension problem for the canonical accepted-digit state.  Degree eight and
all lower rows remain open, and independent source/result review is pending.
There is no recurrence, all-depth, characteristic-zero, lift/no-lift,
counterexample, or JC2 inference.
