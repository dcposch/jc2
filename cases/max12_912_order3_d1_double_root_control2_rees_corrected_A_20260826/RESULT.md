# Corrected direct-saturation certificate

## Verdict

Both registered AWS executions completed with compiler and Singular return
code zero, empty compiler/CAS stderr, separated timing telemetry, and their
unique PASS markers.  The corrected direct-`sat` encoding agrees, as an
ideal, with the frozen 35-generator special fibre emitted by the reviewed
expanded/inverse-variable B encoding.

The two orders give different reduced-basis orderings and contraction-basis
sizes, as expected, but the same special-fibre ideal:

| execution | order | contraction generators | special-fibre generators | wall / max RSS |
|---|---:|---:|---:|---:|
| Box03 `LPDP` | `(lp(1),dp(8))` | 403 | 35 | 1:19.21 / 102852 KiB |
| r6d `DP` | `dp` | 546 | 35 | 5:51.12 / 494288 KiB |

Each execution checked both directions of ideal membership against the 35
generators parsed from the pinned B certificate and printed

```text
PASS_A_B_SPECIAL_FIBRE_MUTUAL_REDUCTION
LA20_IN_FULL_SPECIAL_FIBRE=1
TORUS_IN_FULL_SPECIAL_FIBRE=1
TORUS_SATURATION_EXPONENT=1
TORUS_SPECIAL_FIBRE_IS_UNIT=1
RESIDUE_IDEAL_IS_UNIT=1
CONTROL2_REES_RESIDUE_SURVIVES=0
```

In the Box03 order the final two reduced-basis entries are `la^20,s`; in the
r6d global order they occur as `s` and `la^20` at positions 1 and 35.
Mutual reduction, rather than textual basis equality, is the order-invariant
certificate.  Since `la` is among the coordinates required to be nonzero,
`la^20` alone makes the torus localization empty; the additional direct
membership of the full torus product and the exponent-one saturation are
consistent redundant checks.

## Exact theorem scope

For the finite Rees ideal in the pinned expanded equations, with

```text
a=1, h=q2=k=nu=0, mu=2/3,
w(la,tau,rho,q1,q0,r2,r1,r0)=(4,1,1,22,22,30,30,30),
```

the full weighted initial ideal contains `la^20`, hence has empty
intersection with the eight-coordinate torus.  Therefore no arc with this
exact fixed axis, fixed loads, support mask, and weight vector has a leading
coefficient in that torus (in particular the displayed residue does not
lift).

This does **not** exclude moving-axis directions, nonzero `q2`, moving loads,
another support or weight, another cancellation wall, the whole double-root
fan, D1, or JC2.  The corrected A polynomials are byte-extracted from the
reviewed B source, so this is an independent contraction/order check, not a
second independent derivation of the eight charged equations.

## Source correction and trust boundary

The earlier factored A input is invalid: exact AWS comparison passed
`E1,...,E7` and failed `E8`, with

```text
A_E8-B_E8=-25134148616192/43046721.
```

The bad polynomial is emitted at line 12 of the frozen factored A source by
`source_a` (`compile_control2_rees_v2.py:297-306`) through
`compact_row_string` (`:269-275`).  The clean repair does not attempt another
hand refactor: the AWS-only compiler extracts `E1,...,E8,LT` byte-for-byte
from pinned B SHA-256
`c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b`
and changes only the contraction and term order.  The historical impact is
enumerated in `IMPACT_MATRIX.md`.

The B-only fixed-weight theorem and its hostile certificate review remain
valid.  Promotion of this dual-contraction package is pending the focused
hostile source/certificate review; the two AWS endpoints themselves agree.

## Custody

```text
Box03 tag  max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T013127Z_box03_LPDP
c9eb14ffd7a7ab786dbec953bfa3f276b56e84f2eabbfc923f99c92bea3db07a  aws_box03_LPDP/singular.stdout
0e92f2d1c418d1710ef20b5dd288912e8b820c8d8d66dd6faa678ebf99c42e02  aws_box03_LPDP/corrected_A_lpdp.sing

r6d tag  max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826T013127Z_r6d_DP
96bed25e5816183bb279c8f7f1ef08beb8966767ac913db9c748250215481b1b  aws_r6d_DP/singular.stdout
a15555873395ed2cfedfedef35ee954dcbe4ed390c29791d5c9bbfff72b92131  aws_r6d_DP/corrected_A_dp.sing

d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088  expected_B_certificate.stdout
```

