# Quarantined producer attempts

Date: 2026-08-26

These attempts are evidence about the compiler workflow only.  None carries
a mathematical verdict.

## V1 and V2 delivery failures

V1 omitted a frozen ancestry file from its archive.  V2 pre-created the
compiler output directory, violating the compiler's fail-closed fresh-output
contract.  Neither reached Singular and neither is evidence for or against a
contact cell.

## V3 Singular parser failure — preserved

V3 compiled the complete exact-Q client, but Singular diagnosed

```text
`polyBucket` ^ `number` failed
```

when powered moving-`p` expressions were inserted inline.  Singular itself
returned process status zero despite the diagnostics, demonstrating why the
hardened validator scans stdout as well as stderr.  V3 was preflight-only and
was never accepted or dual-launched.

Preserved custody:

```text
086fe6b7de786d8fd452d4bc3cf8a00378f229cbf42d2f08d47f02ddff0866fd
  failed_preflight_v3/compiled/square_d1_unique_ac_d23_lowa6_local_row_q.sing
a0e3aa060117121944c7e4bb2a5f3f21d5a53b88694561be3fe9dd88b78da1a7
  failed_preflight_v3/singular.stdout
21a4caddc2eaf3c6989e8982173df204816dbed539905083a0bb3156c09e2444
  failed_preflight_v3/singular.stderr
```

## Later preflight repairs

V4 named the moving-`p` polynomial but exposed Singular's precedence rule
that parses `P^2/32` as `P^(2/32)`; it is no-verdict.  V5 parenthesized the
powered numerator and produced the first clean dual positive result.  V6
added the actual `E` correction, but compared one side before normal-form
reduction and correctly failed its new control.  V7 reduced both sides by
the same Hensel-root ideal and is the frozen producer.
