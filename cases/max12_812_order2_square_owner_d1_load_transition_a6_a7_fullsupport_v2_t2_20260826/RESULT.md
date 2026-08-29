# Producer result: D1 first lower-load transition `a=6,7`

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; HOSTILE REVIEW REQUIRED BEFORE
PROMOTION.**

## Result

The exact-Q Box03 and `F_65521` r6d endpoints both returned engine `rc=0`
and

```text
validator=PASS_D1_LOAD_TRANSITION_A6_A7_V2_T2.
```

The compiler reconstructs all seven frozen source tails with independent
`k10`, `k60+sigma*k61`, `k2`, and all charged targets.  It verifies the
complete moving source-to-Laurent bridge and both denominator recurrences at

```text
a=6: grades 23,24;
a=7: grades 25,26.
```

The exact source support is:

```text
a=6: U0 ; U1+KRC+S0,
a=7: U0+S0 ; U1+KRC+S1,
```

where `S0,S1` are the leading/first-jet `k6*C/L` terms.  V1 supplied a
fail-closed negative control: its incorrect `t*C*Inv1` row alignment broke
the source bridge.  V2 changes exactly two generated tokens to
`t*t*C*Inv1`; all source rows then agree on both fields.  Independent
negative sentinels confirm that deleting the moving `T1` connection,
`k6*C`, or `k10*RC` changes the generic rows.

For `a=6`, the first grade allocates nonzero `A0,C0` to opposite roots of
squarefree `L`.  At the `A0` root, the new `S0` and `KRC` modules are simple
poles and vanish after clearing `L^2`; the next numerator retains
`(3/2)*lambda^2*cv^2`.

For `a=7`, the first numerator factors as `C0*(A0+k60)`.  The root maps use
the shifted linear factor `A0+k60`.  At that root, the moving-L terms from
`U1` and `S1` cancel because `A0=-k60`; all remaining `S1` and `KRC` pieces
are simple, and the exact next numerator again equals

```text
(3/2)*lambda^2*cv^2.
```

It is nonzero on the registered nonzero-contact chart.  Thus, subject to the
reviewed first-normal/half-weight/M=0 hypotheses, the normalized D1 contacts

```text
(ord A,ord C,ord R)=(6,7,>=6), (7,8,>=7)
```

are producer-side eliminated on `D(p*k10)` even with the complete first
lower-load transition retained.

## Custody and resources

```text
af2f73f2fb56f989073eb022403f5c51a295fa079e65e6adb2c80a1670a4aeef
  /tmp/jc2_d1_load_transition_a6_a7_v2_t2_20260826T123000Z.tar.gz
ef494de76514760830e4838e7d336cd8982f4a56cacbe8d8cf147c1f0946ab6d
  exact-Q compiled input
16ed9782ab3d2e02ccc79e026b3b598fede5ef7a54f3b318aaca264011ae6074
  F_65521 compiled input
5608226c57b3af5764d384a2698efb1c9d78d2ebc5520246df9985a8a81c2f4e
  stdout on both fields
6478937aabd200a2544a989d74173b98d6de6fcf3961c4c6b2ee4e8cac3ecd3a
  validation on both fields
```

Exact Q used 0.05 seconds and 16,368 KiB peak RSS; `F_65521` used 0.03
seconds and 13,360 KiB.  Both recorded zero swaps.  `EVIDENCE.sha256`
freezes all 32 retrieved evidence files, including the before/after compiled
inputs.

## Firewall and successor

This is producer-tier until hostile review.  It covers only the fixed
`a=6,7` D1 contacts on `D(p*k10)`.  It covers no `a>=8`, no positive-order
k10, no p=0/k10=0, no other face, no zero/infinity receiver, no scheme
structure, and no full square/order-two/`(8,12)`/maximum-twelve/JC2 claim.

At `a=8`, a unit `k6*C/L` precedes the old `AC` face, so the geometry changes
rather than merely adding a simple next-grade module.  The next client must
classify the shifted lower-load leading factor and retain load valuations.
The exact all-load Chebyshev/Pell solution remains an expected survivor and
must be a positive control, not a unit target.

