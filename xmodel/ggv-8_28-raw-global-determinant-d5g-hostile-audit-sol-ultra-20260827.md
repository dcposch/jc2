# Hostile audit: D5G direct raw-global determinant and `H`-multiple custody

Date: 2026-08-27  
Reviewer lane: independent `d5g_hostile_audit` / Sol Ultra  
Target: `xmodel/ggv-8_28-raw-global-determinant-d5g-sol-20260827.md`
and `cases/ggv_8_28_raw_global_determinant_d5g_20260827/`.

## Overall verdict

**PASS-D5G-INDEPENDENT-HOSTILE-AUDIT.**

No wrong coefficient, omitted support row, provenance mismatch,
quotient/remainder error, `M`-reduction error, false mutation outcome, hash
mismatch, or dependency leak was found.  The producer's exact narrow claim
is confirmed:

```text
raw D3 support plus F0=H^2 and G0=H^3
  -> literal generic D0,...,D22
  -> D22=H*Q22+R22
  -> D22=M(Y22)+rM22.
```

The promotion boundary is load-bearing.  This is custody of the literal
*raw-coordinate* determinant.  It does not identify that object with a
local Morse endpoint, impose `D1=...=D21=0`, impose `D22=1`, or prove a
Keller specialization or an `8_28` exclusion.  D4R1's freeze is read only as
a lifecycle hash; no D4R1 result or local-naturalness statement enters the
computation.

The independent audit case is

```text
cases/ggv_8_28_raw_global_determinant_d5g_hostile_audit_20260827/
```

Its verifier does not import or execute the producer compiler.  It builds
the four differentiated products in a separate sparse `Q[raw][X,t]`
representation, reconstructs every provenance record, and uses closed-form
reductions for the endpoint checks.  The frozen producer replay was also run
separately and passed byte for byte.  All work was desk-scale exact rational
arithmetic; no CAS, AWS, probabilistic specialization, `jc2-lean`, or
canonical-ledger edit was used.

## Verdict table

| Charged item | Verdict |
|---|---|
| Chart Jacobian and coefficient recurrence | **CONFIRMED** |
| D3 `2S/3S` lattice support and 400 positive slots | **CONFIRMED** |
| Literal `D0,...,D22` structural coefficients | **CONFIRMED** |
| All contribution records and contribution digests | **CONFIRMED** |
| `D0=0` by cancellation, rather than omission | **CONFIRMED** |
| Monic division `D22=H Q22+R22` | **CONFIRMED** |
| `M` reduction, seven-vector, and 621-step trace | **CONFIRMED** |
| `D22 -> D22+H` custody mutation | **CONFIRMED, strengthened exactly** |
| Drop-slot and `(i-8)->(i-7)` mutations | **CONFIRMED structurally** |
| Producer and dependency hashes | **CONFIRMED** |
| D4R1 nonconsumption and no target verdict | **CONFIRMED** |

No item is `CORRECTION` or `FAIL`.

## 1. Independent derivation of the determinant formula

Use the D3 chart

```text
x=t^3 X,   y=t^-1,   F=t^8 f,   G=t^12 g.
```

The coordinate Jacobian is

```text
det d(x,y)/d(X,t) = -t.
```

Since `f=t^-8 F` and `g=t^-12 G`, direct differentiation gives

```text
det d(f,g)/d(X,t)
 = -t^-21 [12 F_X G - 8 F G_X - t(F_X G_t-F_t G_X)].
```

Dividing by the coordinate Jacobian therefore gives

```text
J_(x,y)(f,g)=t^-22 E,
E=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X).
```

Writing `F=sum_i t^i F_i` and `G=sum_j t^j G_j`, the coefficient of
`t^n` is consequently

```text
D_n=sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j').
```

Thus both signs and both shifted integers in D5G are correct.  In
particular, the `+i` term comes from `+t F_t G_X`; it is not `-i`.

## 2. Support and raw-slot audit

The audit independently enumerated the source polygons rather than trusting
the serialized row counts.  For `F/2S`, it enumerated

```text
0<=i<=16,
max(0,4i-8)<=j<=3i+8,
n=8+3i-j,  0<=n<=22.
```

For `G/3S`, it used the analogous bounds

```text
0<=i<=24,
max(0,4i-12)<=j<=3i+12,
n=12+3i-j,  0<=n<=22.
```

Every tuple, slot name, raw monomial, chart image, and weight in D3's
`RAW_INPUT.json` matches this enumeration.  The exact census is

| source | all rows through 22 | weight-zero rows | positive rows used by D5G |
|---|---:|---:|---:|
| `F` | 141 | 17 | 124 |
| `G` | 301 | 25 | 276 |
| total | 442 | 42 | 400 |

D5G correctly replaces the normalized weight-zero raw rows by the fixed
polynomials

```text
F0=(X^8-1)^2,   G0=(X^8-1)^3,
```

and treats precisely the remaining 400 slots as algebraically independent.
No nonexistent `F15`, `G22`, or other out-of-support row is introduced.

## 3. Full independent structural replay

The audit constructed the truncated bivariate expression from the four
products

```text
12 F_X G,  -8 F G_X,  -t F_X G_t,  +t F_t G_X
```

without calling the producer recurrence.  Its structural polynomial equals
the complete producer `DIRECT_DETERMINANT.json` term for term.  Exact totals
are

```text
32,135 final nonzero sparse terms,
58,572 nonzero pre-combination contributions,
778 terms in D22,
1,374 contributions to D22.
```

The independent canonical digest of all structural coefficients is

```text
0b82d31ddccfe5415fbe5916dd7ec50966e61a0aa71b15ca6cb6025b560bbd6f.
```

For every weight, the audit separately regenerated the two source row
names, weights, derivative side, output degree, and rational coefficient.
Every contribution list and every per-weight contribution digest matches.
The digest of the 23 contribution digests is

```text
cbe21f966bc15d70336ce18176c5954600b32b7d5320dc9e67f8a79f6a5ace45.
```

The top-level and endpoint-certificate copies of the 1,374 weight-22
records also match exactly.  At weight zero there are 17 nonzero
pre-combination contributions, but their aggregate is zero:

```text
12 (H^2)' H^3 - 8 H^2 (H^3)' = 24 H^4 H' - 24 H^4 H' = 0.
```

So `D0=0` is a checked cancellation and not a hard-coded empty row.

## 4. Independent endpoint decompositions

### Division by `H`

For a monomial of degree `d=8q+r`, `0<=r<8`, the audit used the closed
identity

```text
X^d=(X^8-1) sum_(a=0)^(q-1) X^(r+8a) + X^r.
```

Applying this coefficientwise in the raw coefficient ring reproduces the
producer's exact `Q22` and `R22`:

| object | terms | maximum `X` degree | independent digest |
|---|---:|---:|---|
| `D22` | 778 | 17 | `2aed3fee594725ff942a71ebc75b9c13406bb29d8696280e64ee922813cc43d0` |
| `Q22` | 523 | 9 | `e8eb577b323cad48dbfce2515f0851126c84e6bfd2eb3450208ce043dfbdc4ca` |
| `R22` | 778 | 7 | `37023c755120bd7b5da7b6d0df1bb96982dcf8241ac1f16e155bf8419d93f5e7` |

The identity `D22=H Q22+R22` and `deg R22<8` are exact over the polynomial
coefficient ring; no localization or evaluation at roots occurs.

### Reduction by `M`

From

```text
M(X^k)=4(k+12)X^(k+7)-4kX^(k-1),
```

the independent remainder of a monomial `X^(8q+r)` is zero for `r=7`, and
for `0<=r<=6` is

```text
prod_(s=1)^q (r+8s-7)/(r+8s+5) * X^r.
```

This closed formula reproduces all 680 terms of `rM22`.  Independently
applying `M` to the serialized `Y22` gives `D22-rM22`, and replaying all 621
listed leading cancellations reaches exactly the same `Y22` and remainder.
The seven-vector is the exact degree slicing of that remainder.

| object | terms | maximum `X` degree | independent digest |
|---|---:|---:|---|
| `Y22` | 621 | 10 | `ec210046166afb026e6a382ec6f5fce0a5a7ef43327e5e547c8ba9f6330bd2b9` |
| `rM22` | 680 | 6 | `49ab438543e717ddd4cf34ec36d2b32988cb9197ec1a2a10ce83f98bbdb4d289` |

## 5. Mutation audit

The decisive mutation is stronger than the producer's Boolean checks.
Since

```text
H=X^8-1=M(X/52)-12/13,
```

the artifact for `D22 -> D22+H` has exactly

```text
Q22_mutated-Q22       = 1,
R22_mutated-R22       = 0,
Y22_mutated-Y22       = X/52,
rM22_mutated-rM22     = -12/13.
```

All four equalities hold term for term.  This directly proves that
factorwise reduction modulo `H` loses the global quotient while the frozen
quotient and `M` vector detect it.

The two compiler/source mutations also change the independently constructed
structural polynomial, not merely producer metadata:

| mutation | independently changed coefficients |
|---|---:|
| delete `f_0_1` | 243 |
| replace `(i-8)` by `(i-7)` | 31,428 |

Their independent structural digests are frozen in the audit result.

## 6. Hash and dependency audit

All charged producer bytes match their claimed SHA-256 values:

```text
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
72e8ba988a0aaeccb86f473bf89b66847481c4e645998f5456e2ad0acb803541
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/PREREGISTRATION.md
059d9f32351f5bb5132e0a9cb10e68c35f78ac8504a8323732463f9126897b95
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/compile_d5g.py
069ab7a5fdb133aa2ffb0063e5f36c5664a070798de6ea00520698207e24838d
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/DIRECT_DETERMINANT.json
6346ab6afb307fea83516f742ca53b90e5eb8d42c2e1d5bef083920de23e434a
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/D22_CERTIFICATE.json
e20f4a67953eeab86d21bea5fbaf149dffe20b65b0af052354490b3bc04aa8da
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/RESULT.json
64f63865feeb1bd7e64ad6c8be1bc3abd28d3dc995a5a65ef8971a6954606870
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/README.md
838b1160f3ddf38fcbf360bd200ee2057e72da2b1b0ba8788d43b83720cdd043
  cases/ggv_8_28_raw_global_determinant_d5g_20260827/FREEZE.sha256
59e9bf2c6713b84ef848bae693a7e88f62c679ff56bad34fce4d3a28548663f3
  xmodel/ggv-8_28-raw-global-determinant-d5g-sol-20260827.md
```

Every dependency hash embedded in `RESULT.json` also matches live bytes.
Static inspection confirms that the only D4R1 file named by the producer is
its `FREEZE.sha256`; it is hashed in `build_result` but not passed to
`determinant`, `build_certificate`, the dense control, or either reduction.
No D4R1 result, cleanup DAG, Morse row, carrier value, source equation, or
branch choice is read.  The producer explicitly records
`local_naturality_dependency.consumed=false` and emits no target verdict.

Repository `HEAD` at audit time:

```text
418e413593120d19e15e6546eb50c985f4b1f038
```

## Scope firewall

The maximum licensed promotion is the D5G raw-global compiler/custody
result.  In particular, this audit proves none of:

- a local-to-global naturality square;
- the equations `D1=...=D21=0`, `R22=1`, or `Q22=0`;
- existence or nonexistence of a Keller specialization;
- an `8_28` face or family exclusion;
- `G2-PSC`, `G2-BD`, a counterexample, or JC2.

Within that boundary, the D5G result is exact and ready for narrow
promotion.
