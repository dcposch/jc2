# D5G: review-independent raw-global determinant and `H`-multiple custody

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2

## Verdict

**`PASS-D5G-REVIEW-INDEPENDENT-RAW-GLOBAL-DETERMINANT`.**

The literal generic raw coefficients `D0,...,D22` are now compiled directly
from D3's 400 positive-weight `2S/3S` rows.  No Morse chart, carrier branch,
source equation, or D4R1 theorem is used.  The endpoint artifact contains
exact replayable decompositions

```text
D22 = H*Q22 + R22,       deg_X R22 < 8,
D22 = M(Y22) + rM22,     deg_X rM22 < 7,
M(Y)=4H Y'+6H'Y.
```

This provides the missing direct custody of the global `H`-multiple.  It
does not provide a target verdict: the raw rows remain generic and
`D1,...,D21` are not assumed zero.

## 1. Literal determinant source

Work in

```text
C=Q[400 named positive-weight D3 raw slots],
S=C[X],
H=X^8-1,
F0=H^2,
G0=H^3.
```

For every `0<=n<=22`, the compiler expands exactly

```text
D_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j').
```

A sparse coefficient-ring monomial is a sorted tuple of zero, one, or two
raw slot names.  Each final term is serialized as

```text
[raw coefficient monomial, X degree, rational coefficient].
```

The direct artifact contains 32,135 final sparse terms arising from 58,572
pre-combination derivative contributions.  Every contribution at every
weight is serialized literally with its two source rows, derivative side,
source weights, `X` degree, and rational coefficient, and each weight has a
separate contribution digest.  The 1,374 weight-22 contributions are also
copied into the endpoint certificate.

The fixed leading square/cube rows give `D0=0` exactly: 17 derivative
contributions cancel, rather than being omitted by convention.

An independent implementation guard specializes all 400 raw slots to
deterministic nonzero rationals, constructs dense `Q[X,t]/(t^23)` series,
differentiates and multiplies the full expression

```text
12F_XG-8FG_X-t(F_XG_t-F_tG_X),
```

and compares every coefficient with the sparse compiler.  The independent
check passes; its `E0..E22` digest is

```text
db5ededadbefb2153dba1f1098bbd6b63881eeae7b65b2451e2448d45766ba3e.
```

## 2. Exact endpoint custody

The literal generic `D22` has 778 terms and `X` degree 17.  Because `H` is
monic, ordinary Euclidean division in `C[X]` requires no localization:

```text
Q22: 523 terms, X degree <=9,
R22: 778 terms, X degree <=7.
```

The certificate multiplies and adds these sparse objects back to the exact
778-term `D22`.  `R22` is the degree-`<8` object visible factorwise modulo
`H`; `Q22` is the exact, separately frozen global `H`-multiple.  Neither is
interpolated from carrier bits.

The confirmed `M` reduction independently gives

```text
Y22:  621 terms, X degree <=10,
rM22: 680 terms, X degree <=6.
```

Its seven coordinates contain respectively

```text
93, 90, 90, 97, 104, 103, 103
```

coefficient-ring terms.  The complete leading-term cancellation trace and
the identity `D22=M(Y22)+rM22` are frozen in the endpoint certificate.

## 3. Load-bearing mutations

The decisive custody mutation is exact:

```text
D22 -> D22+H.
```

The replay verifies

```text
R22_mutated = R22,
Q22_mutated = Q22+1,
rM22_mutated != rM22.
```

Thus all factor values remain unchanged while both the invisible quotient
and the seven-coordinate `M` obstruction detect the mutation.

Two source/compiler mutations also fail closed:

- deleting raw slot `f_0_1` changes the complete direct determinant digest;
- changing the recurrence coefficient `(i-8)` to `(i-7)` changes it.

## 4. Dependency lock and scope

D4R1's freeze is pinned only as a lifecycle hold.  Its result is not read or
used.  The local naturality square

```text
E(t,xi(t)) = q0(t)*C(t)
```

remains `LOCKED_PENDING_D4R1_FRESH_HOSTILE_REVIEW`.  In particular, D5G
does not infer `D0=...=D21=0`, `R22=1`, or `Q22=0`.

The exact replay is:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/compile_d5g.py --check \
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/DIRECT_DETERMINANT.json \
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/D22_CERTIFICATE.json \
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/RESULT.json
```

This is a raw-global compiler/custody result only.  It proves no Keller
specialization, target identity, local/global naturality theorem, `8_28`
face/family exclusion, `G2-PSC`, `G2-BD`, Keller pair, counterexample, or
JC2 result.
