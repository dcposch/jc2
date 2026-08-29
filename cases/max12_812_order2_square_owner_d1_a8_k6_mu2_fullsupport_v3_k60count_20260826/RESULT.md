# Producer result: D1 `a=8` complete `k6`/`mu2` transition

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; HOSTILE REVIEW REQUIRED BEFORE
PROMOTION.**

## Result

Exact Q on Box03 and `F_65521` on r6d both returned engine rc 0 and

```text
validator=PASS_D1_A8_K6_MU2_V3_K60COUNT
```

with identical mathematical stdout.  The compiler rebuilt all seven frozen
Faber/source tails with independent `k10,k6,k2`, all six lower loads/targets,
the moving Laurent-to-Faber connection, and both root orientations.  This is
not a Laurent-only target client: in particular, the nonzero `mu2` source row
is carried through the complete frozen source transform.

The fixed contact is

```text
ord(A)=8, ord(C)=9, ord(R)>=8
```

on `D(p*k10)`.  The two exhaustive sections are:

1. On `D(k60)`, grade 26 is the simple-pole module
   `[(3/4)k60*C0/L]_-`.  Its first two exact denominator coefficients are
   nonzero scalar multiples of `k60*c1,k60*c0`; seven-row vanishing forces
   `C0=0`, contradicting the registered contact.
2. On `V(k60)`, write
   `k6=sigma*k61+sigma^2*k62+...`, allowing `k61,k62` to specialize to zero.
   Grades 27/28 are exactly

   ```text
   U0+S0 ; U1+KRC+S1+target(mu2).
   ```

   The first cleared numerator is `C0*(A0+k61)`, so the two root maps
   allocate `C0` and the shifted factor `A0+k61` to opposite roots of
   squarefree `L`.  At the shifted-A root, the moving `U1/S1` connection
   cancels exactly.  The complete inverse-Faber image of the `mu2` row has

   ```text
   h2=-mu2, h4=(p/2)mu2, h6=-(p^2/4)mu2,
   ```

   whose cleared `L^2` numerator is `-mu2*L`; it vanishes at either root.
   The next numerator therefore retains the exact nonzero residue

   ```text
   (3/2)*lambda^2*cv^2.
   ```

Deletion controls independently verify that removing the moving `T1`
connection, `k6*C`, or the `mu2` target changes the extracted rows.  Hence,
subject to the already reviewed first-normal/half-weight/`M=0` hypotheses,
the fixed D1 `a=8` contact is producer-side eliminated in both exhaustive
`k6` sections.

## Software controls and custody

V1 remains a useful partial control: its `D(k60)` client passed over both
fields, but its positive-valuation source ring omitted the formal `k60`
symbol used by a support filter.  V2 inserted the six symbols correctly but
failed before CAS because an assertion counted six repaired strings while
forgetting the one pre-existing `D(k60)` string.  V3 changes only that
postcondition, requiring exact counts

```text
old_before=6, new_before=1, old_after=0, new_after=7.
```

V3 compiled-input SHA-256 values are

```text
58a4145216694293c7af91b6368330777a6f9f2a414380b5ff47d87c1eb5e941
  exact Q
3b0bdf6fc0f70777a265a9d32a577059266bbbb1386b02fc05da2b39a7ec1a22
  F_65521
```

Both mathematical stdout files have SHA-256
`4a1f5e8c4aac59e6ec2fa22f167ebc0c95b85395d772e17ee0f4c54658084186`;
both validation files have SHA-256
`ba8743200200fe476ee6a21f5fe69d65a7aaf2232a34a426989c6ed033c371ed`.
The source freeze manifest has SHA-256
`dcd6c3eb2d390375f1c56bc638215a4e447efe680a4c5f345c18011945514f7f`.
`EVIDENCE.sha256` freezes all 32 retrieved files, including the frozen-V1 and
repaired compiled inputs.

Exact Q used 0.05 seconds and 14,936 KiB peak RSS; `F_65521` used 0.03
seconds and 12,876 KiB.  Both recorded zero swaps.

## Firewall and successor

This is producer-tier pending hostile review.  It covers only fixed `a=8`
on `D(p*k10)` after the cited upstream gates.  It covers no `a>=9`, no
positive-order `k10`, no `p=0` or `k10=0`, no other valuation face, no
zero/infinity receiver, no scheme structure, and no full square,
order-two, `(8,12)`, maximum-twelve, or JC2 claim.

In particular, tied lower loads genuinely admit the exact nonsquare
Chebyshev/Pell control `Q=z^4-1`,
`16Q^2+20Q+5=U4(z^2)`, `A=T5(z^2)`.  This result is a finite D1 contact
elimination, not blanket square forcing.  The next client must continue the
full-support contact atlas at `a>=9` and retain every newly timed `k6,k2`
and target module.

