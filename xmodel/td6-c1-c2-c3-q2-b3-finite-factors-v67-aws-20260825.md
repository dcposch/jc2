# TD6 fixed-A3 q2-beta finite `B3` factor source-DAG gate (V67)

Status: **dual-AWS producer-exact on the two factor opens; hostile review
pending.**

V67 closes the source-DAG calculation on `D(w)` for both finite parameter
factors left by the V66 birational `B3=0` chart:

```text
2t-1=0,
t^2-4t+2=0,
w=V0/U0.
```

The exact source-checked center map is

```text
U0=w^2(t-2)^2/(16t),
V0=w^3(t-2)^2/(16t),
C0=w^4(t-2)^2(-5t^2+20t-4)/(256t^2).
```

On each exact function field the ranks are
`3470/3602 -> 38/132 -> 38/94 -> 25/56`.  Polynomial beta and direct
`q_beta'=1+2 beta t+25 t^24` are retained.  Current row 13 is exactly
`N13=(k/25)beta` and traces through previous row `('X-1',14)` plus original
first rows; row `('X-1',0)` is only an independently replayed quadratic
control/cache.  Genuine P12 uses 28 original first rows (2,893 raw terms on
`2t-1`, 2,885 on the quadratic factor) and composes with N13 to the unit
`-k/50`.

The complete emitted source-leaf and staged denominator support is only the
curve parameter `w`: stage `w^11`, final charts `w^27` and `w^23`.
The stdout's internal polynomial symbol `x`/legacy `U_POLY` denotes `w`, not
the raw center coordinate `U0`.  Consequently these are exact all-beta
incompatibility certificates only on `D(w)`.  Both parameterizations send
`w=0` to the raw origin; that endpoint remains a separate reviewed theorem
and is not consumed in this package.

Box02 and Box03 ran the same source archive
`13bdaa2a0033eef77088a3a1bc46c7288efde85398f0897107769c04ff404306`
under 12-GiB caps.  Paired proof DAGs and ledgers agree byte-for-byte.  After
normalizing only the absolute artifact path, the entire paired stdout agrees
at SHA256
`bf5b63f1371b6bee76975a5f273c71da83ac70f110ae90c92bf9a839c7a36004`
and
`538b70f522ad10f45dae9b842112799bcc4bc9e0e93c824a27b8eede6bd2b454`.
Separate direct-q-prime omission controls detect the loss of N13 before an
expected reporter `IndexError`; their rc-one streams are not theorem
evidence.

Frozen case:
`cases/td6_c1_c2_c3_q2_b3_finite_factors_v67_aws_20260825/`.

Exact scope: the two displayed factor opens `D(w)` in the fixed
source-typed A3 q2-beta section.  No whole factor or whole `B3=0` is claimed
here, and nothing implies whole A3, TD6, SP-2, landing, or JC2.
