# TD6 H19R1 raw P13 coordinate-12 audit result

Date: 2026-08-26

Status: dual-AWS producer diagnostic complete; **not promoted mathematics**.
Independent hostile review is required before this artifact can be imported.

## Question and repaired scope

H18 found the sole nonzero coordinate 12 in the normalized P13/FIRST output,
namely `(3500000000/9)*(U/V)`. H19R1 asks whether that same unit is already a
literal coordinate-12 row in the uneliminated total-family CURRENT equation at
degree 13, before FIRST row operations.

The original H19 package is quarantined with no verdict: it did not pin the
transitive H15/H12/H11/compiler closure, and its claimed omission check removed
a serialized output record rather than a source term. H19R1 repairs both
defects. It retains all 132 transport variables and all 22 q coordinates,
reconstructs the six compiler-loop families into 68 nonzero source addends,
and checks that their sum equals the frozen H15 degree-13 compiler output with
2,757 parameter terms.

## Exact result

Both AWS replicas returned rc 0 and the banner
`TD6-V89H19R1-RAW-P13-COORDINATE12-FIRST-CANCELLATION-REQUIRED PASS`.
Before and after exact `F=0`, raw coordinate 12 is q-free and has exactly two
records:

- parameter monomial `(27,)`: `500000000/(27*U)`;
- parameter monomial `(29,)`: `-1562500000/(27*U)`.

Thus raw specialized coordinate 12 is **not** H18's normalized unit. The H18
unit appears only after the frozen FIRST elimination, so an explicit
FIRST-membership/cancellation certificate remains necessary.

The frozen AWS-only source census found exactly four ordered raw addends with
nonzero specialized coordinate 12:

1. `f1_times_dg2:i=13:j=1`;
2. `2f2_times_dg1:i=12:j=2`;
3. `minus2_df1_times_g2:i=13:j=1`;
4. `minus_df2_times_g1:i=12:j=2`.

The genuine negative control removes the first addend before aggregation. It
leaves the `(27,)` record unchanged and changes the `(29,)` coefficient to
`-1625000000/(27*U)`. Hence the source-term omission is real and detected.

## Dual custody

- r6a: instance `i-02cb2b4a379ffcc64`, tag
  `td6_v89h19r1_raw_p13_c12_20260826T234747Z_r6a`, remote root
  `/home/ubuntu/jobs/td6_coordinate12_h19_20260826T234603Z_r6a`, rc 0,
  6:38.39 wall time, 297160 KiB peak RSS, zero swaps.
- r6b: instance `i-0f089e64c378f5da3`, tag
  `td6_v89h19r1_raw_p13_c12_20260826T234747Z_r6b`, remote root
  `/home/ubuntu/jobs/td6_coordinate12_h19_20260826T234603Z_r6b`, rc 0,
  6:31.81 wall time, 297176 KiB peak RSS, zero swaps.

Both used Python 3.12.3, python-flint 0.9.0, and the enforced extension hash
`1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138`.
Assertions were enabled (`sys.flags.optimize=0`). The timeout was 43,200
seconds, the virtual-memory cap was 450,000,000 KiB, and algebraic libraries
were restricted to one thread. The three mathematical outputs and stdout are
byte-identical across hosts.

## Narrow verdict

H19R1 rules out only the direct-raw-unit shortcut. It does not invalidate H18,
does not establish the required original-FIRST membership, does not lift a
unit to independent total `F`, does not kill TD6, and does not resolve JC2.

