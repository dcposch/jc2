# Corrected-Q10 to Q9 source-state gate

Status: **PRODUCER EXACT; PROVISIONAL PENDING INDEPENDENT SOURCE/RESULT
REVIEW.**

## Typed row

Write the determinant filtration in the frozen convention as

```text
A = U_x - x^2,                  L = A + V_y,
K = A V_y - U_y V_x,
E = L/3 + K + C_x + D_y,
M = A D_y + C_x V_y - U_y D_x - C_y V_x,
F = E/3 + M + W_x + Z_y,
N = {C,D},
T = A Z_y + W_x V_y - U_y Z_x - W_y V_x,
G = F/3 + N + T.
```

All divisions here are used only after the preceding accepted-digit rows
make them coefficientwise exact over the integers.  For the total-degree
nine row, the typed support gives `E_9=0` and `(W_x+Z_y)_9=0`; hence
`F_9=M_9`.  The corrected-Q10 predecessor makes `M_9/3` integral, and the
row imposed by this gate is therefore

```text
G_9 = M_9/3 + {C,D}_9 + T_9 = 0 mod 3.             (1)
```

The compiler reconstructs canonical integer representatives for every one
of the 33,225 corrected-Q10 states and asserts all required divisions.  It
then restores exactly the previously suppressed layers

```text
C2,D2:  6 coefficients; E_1 gives 2 rows,
C4,D4: 10 coefficients; E_3 gives 4 rows,
W7,Z7: 16 coefficients; F_6 gives 7 rows,
G_9:                         gives 10 rows.
```

Thus each predecessor is tested by a 23-row affine system in 32 variables
over `F3`.  The support calculation excludes products of two newly restored
variables from these rows.  The compiler also evaluates an all-ones point as
a nonlinear-term control, row-reduces the augmented matrix exactly, and
substitutes its canonical witness back into all 23 source rows.

The six current-digit degree-six Frobenius coefficients remain absent from
these four row bands.  They contribute a separate factor `3^6=729`; they are
not silently included in the displayed 32-variable fibre.

## Exact result

The 27 source-frozen AWS shards reproduce the complete predecessor chain:

```text
visible predecessor states             1,085,103
N12 survivors                             629,115
corrected-Q11 survivors                    260,847
corrected-Q10 survivors                     33,225
Q10 states with nonzero M9/3 mod 3           5,710
Q9-compatible predecessor states            11,881
Q9-incompatible predecessor states          21,344
```

The exact `(rank,augmented-rank)` census is

```text
(13,13):  6,615       (13,14):  4,320
(15,15):  2,106       (16,17):  5,288
(16,16):  3,160       (17,18): 11,736.             (2)
```

Consequently the relevant 32-variable fibre histogram is

```text
0^21344,
(3^16)^3160,
(3^17)^2106,
(3^19)^6615.                                      (3)
```

The total number of relevant completions is

```text
8,096,356,425,843,
```

and restoring the six independent current Frobenius spectators gives

```text
5,902,243,834,439,547.                            (4)
```

Exactly 79 of the 2,187 structural bases have a Q9-compatible state.  The
per-base compatible-state histogram is

```text
0^2108, 1^28, 3^18, 9^6, 27^12,
108^4, 243^6, 405^2, 2187^2, 4347^1.              (5)
```

The first emitted witness has a rank-13 fibre of size `3^19`; its exact
30-coordinate predecessor vector and 32-coordinate restored-layer vector
are retained in `aggregate.out` and are substituted back into the source
rows by the compiler.

The ordered 27-leaf output Merkle root is

```text
31b77bef882a784b43ee146d930f192385714efce730b9126c8c2df4038b7be7. (6)
```

## Execution and provenance

```text
host: Box02 / ip-172-30-0-186 / 34.203.207.55
tag: as_d7_q9_state_20260825T011049Z
UTC: 2026-08-25T01:12:19Z--01:16:10Z
overall/aggregate rc: 0/0
per-shard cap: one CPU, 8 GiB VM, 12 hours
observed peak RSS: 21,752 KiB
longest shard: 3:51.69; other shards: 11.77--16.71 seconds
```

The transported archive SHA-256 is
`7edde1b07a9ec0839d535bb20d1ab0779d0afa96afa281a1b115c1aee143546b`.
Box02 verified the runner manifest and the complete recursive source
closure before launch.  The compiler SHA-256 is
`54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2`;
the source freeze SHA-256 is
`1aa89a7bebf557494970f7a6ed045d031a5999f35516caced58f3937dd0ea589`.
The aggregate output SHA-256 is
`ab38fefa43d3b2065f839bfed2deccd58b75e0570fc36324cce67db805b5d3d0`.

`./verify_frozen_results.sh` is a bounded hash-and-aggregate check.  It does
not rerun the 33,225-state source compiler.

## Scope

This exact producer shows that the displayed source-honest Q9 extension
problem is nonempty, while eliminating 21,344 of its 33,225 predecessor
states.  It does not assert that every integer representative convention is
already independently audited, nor that the surviving states extend through
degree eight or any lower row.  The shards are partitions of one
implementation, not independent reviews.

No recurrence, all-depth lift/no-lift, characteristic-zero, counterexample,
or JC2 conclusion is licensed.

