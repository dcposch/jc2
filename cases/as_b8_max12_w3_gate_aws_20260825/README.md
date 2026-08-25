# AS-source-transformed B8 fixed-D12 survivor through `Z/27`

Status: **producer-exact finite-depth survivor; dual-AWS replay**.

Put `u=x+y^4`.  The special fibre is

```text
G8=(y+u^2,u^3-u),
```

the determinant-one target reorder of the right-composition of
`(s-s^3,t)` with `B8=(u,y+u^2)`.  The exact V2 coordinate envelope contains
all total-degree-at-most-twelve monomials with `y`-degree at most eight in
the first coordinate and at most twelve in the second: `81+91=172` digit
variables.  All 276 determinant positions through total degree 22 are kept.

The exact first-Cartier operator has rank 104 and nullity 68.  Deterministic
RREF gives

```text
R2=2*x*y^5+x^2*y,                         S2=0,
R3=2*x*y^6+x^3*y^5+x^4*y,                S3=x*y^9.
```

Therefore

```text
P=y+u^2+3*(2*x*y^5+x^2*y)
        +9*(2*x*y^6+x^3*y^5+x^4*y),
Q=u^3-u+9*x*y^9
```

has exact total and partial `y`-degree pair `(8,12)`, reduces to `G8`, and
satisfies

```text
det J(P,Q)=1 mod 27.
```

The replay checks this coefficientwise in `Z[x,y]`, not via characteristic-
three Frobenius.  It also checks the special-fibre collision
`(0,0),(1,2)->(0,0)` and proves that omitting the full `9`-digit fails modulo
27.

## V1 negative control

The preregistered V1 solver allowed all 91 D12 slots in each coordinate.
Its deterministic W3 point passed the determinant congruence but raised the
first coordinate's actual `y`-degree above eight, then failed closed at the
degree assertion.  It is not a `(8,12)` result.  The V1 launcher also wrote
an empty `runner.rc` and `0` PID because of a shell-interpolation defect; the
preserved `/usr/bin/time` stderr records exit status one and the exact failed
assertion.  V1 is routing/custody evidence only and is excluded from every
positive theorem claim.

## AWS custody

The immutable V2 source ran on two independent hosts:

| host | remote path | UTC end | rc | max RSS | stdout SHA-256 |
|---|---|---|---:|---:|---|
| Box02 `34.203.207.55` | `/home/ubuntu/jc2q8-box02/out/as_b8_max12_w3_gate_v2_box02` | `2026-08-25T16:23:21Z` | 0 | 15,616 KiB | `68bb935820310f79d39f8cd342de2c428ff2cced1ee986795600a61af2a7c604` |
| Box03 `98.80.65.144` | `/home/ubuntu/jc2q8-generic/out/as_b8_max12_w3_gate_v2_box03` | `2026-08-25T16:23:25Z` | 0 | 15,784 KiB | `68bb935820310f79d39f8cd342de2c428ff2cced1ee986795600a61af2a7c604` |

Both source checks passed, both stdout files are byte-identical, both return
codes are zero, and both payloads have SHA-256
`5c9219e497e7cc14017a9fefc395aaaddcf420ccb8911b0db77c9b0b6985384f`.

## Replay

Substantive computation is AWS-only.  On an AWS host:

```sh
cd cases/as_b8_max12_w3_gate_aws_20260825
sha256sum -c SOURCE_V2.sha256
timeout 1800 /usr/bin/time -v python3 replay_v2.py
```

## Scope firewall

This is one explicit fixed-D12 map modulo 27 and one deterministic point of
the complete W2 affine fibre.  It does not classify the other 68 kernel
directions, produce a modulo-81 or all-depth branch, give a `Z_3` or
characteristic-zero map, prove nonautomorphy in characteristic zero, enter
selected Q8 or TD6, settle either maximum-twelve frontier, or prove or
disprove JC2.
