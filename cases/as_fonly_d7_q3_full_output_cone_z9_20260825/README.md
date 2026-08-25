# Exact fixed-D7 `Z/9` output-cone gate at three pinned Q3 fibres

Status: **PRODUCER-EXACT / REVIEW PENDING**.

This case consumes the different-model-CONFIRMED Q3 affine fibres above the
three pinned Q5 predecessor points `0000`, `0270`, and `0513`.  At one literal
Q3 particular in each fibre it adjoins every polynomial output coefficient of
total degree at most seven at orders 27 and 81:

```text
P=P0+27U+81V,  Q=Q0+27W+81Z.
```

Combining the two fresh digits as `T=U+3V in Z/9` gives 72 variables.  Every
one of the 91 determinant coefficients in degrees 0 through 12 is imposed
modulo 243.  The exact AWS replay finds a solution at all three points.

## Exact results

| parent | mod-3 rank / kernel | Bockstein rank / kernel | solutions | result SHA-256 |
|---|---:|---:|---:|---|
| `0000` | `27 / 45` | `36 / 81` | `3^81` | `3e6a559c5b4906b489b9c43350b95259a191c1fbe529656f32b52fdc40bd4f0a` |
| `0270` | `27 / 45` | `43 / 74` | `3^74` | `eb6936b975de974f26e0f571a3e1839ee118d6ed96ea12bf769ecd2f6015d97e` |
| `0513` | `27 / 45` | `43 / 74` | `3^74` | `c8716a9828b42f3b97f89a41e646b5fa8b8744fe5945ebfe1b24a42141b9fd1e` |

For every reconstructed particular, literal integer expansion verifies
`det J(P,Q)-1` coefficientwise divisible by 243.  Both derivative-zero
constant columns are present and identically zero.  All `36*36=1296` fresh
`P/Q` pair controls have quadratic remainder divisible by 729.  Every
reviewed Q3-kernel direction is literally an order-81, D7-supported output
difference; all `72*kdim` mixed second differences with a fresh order-27
basis are coefficientwise divisible by `81*27=2187` (`1008`, `720`, and
`720` controls respectively).

The row-8 column audit explains why the earlier displayed degree-at-most-three
exclusions do not close these fibres.  The full cone has nonzero `Z/9`
columns at `P_1_1`, `P_3_1`, `Q_0_2`, and `Q_2_2`; in particular degree-four
digits are live.

## Replay and custody

AWS host: r6d, hostname `ip-172-30-0-45`.

Immutable job:

```text
/home/ubuntu/jobs/as_q3_full_output_cone_z9_20260825T145301Z
```

All three jobs returned rc 0 in about 11.8 seconds with peak RSS below 23 MiB.
The staged source/input archive is
`aws_run/SOURCE_CLOSURE.tar.gz`, SHA-256
`c3cb56df1c9ad751bd363a79300185245681ad5524ad5f347bf412e5499c702e`.
`aws_run/SOURCE_CLOSURE.sha256` and `aws_run/PINNED_INPUTS.sha256` record the
remote transitive closure and immediate inputs.  Per-point inputs, outputs,
resource logs, and hashes are under `aws_run/base_*`.

Portable replay (substantive execution must remain AWS-only):

```bash
JC2_ROOT=/path/to/jc2 \
OUTPUT_ROOT=/path/to/fresh/output \
bash cases/as_fonly_d7_q3_full_output_cone_z9_20260825/replay_all.sh
```

## Strict scope

This is a complete order-27/order-81 **output-digit cone modulo 243 over three
pinned Q3 fibres**.  It is not the whole Q5/global predecessor scheme.  It
does not impose the next terminal modulus 729 or order-243 digits, prove a
compatible deeper lift, produce a `Z_3` point, prove a collision, give a
characteristic-zero counterexample, or decide JC2.

