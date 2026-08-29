# Retrospective TRIPLE03 root-chart endpoint semantic-plant replay

Date: 2026-08-28

## Frozen inputs

- Original six-chart terminal archive SHA-256:
  `1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787`
- Original `output/triple03/chart.sing` SHA-256:
  `0141cffd951fde163341dfa1d835194fce6168f49a91abc3c7171e7342e166d9`
- Original TRIPLE03 chart-delta artifact SHA-256:
  `9e07a399764ace2008ad89af5c865326b0cdb65ceab1bcc83f5edcc63463144b`
- Original TRIPLE03 endpoint-coefficient artifact SHA-256:
  `a20a6af9de8f45a9b0486827cbc503111c554d6484fae3a59f150b0fbe8b7c28`
- Original TRIPLE03 bordered-identity artifact SHA-256:
  `ba2576ce6b4cd9b0344e3a0e1f1246f188d1a7182fb66a4eda186c1dd45ad5cd`
- Independently planted closed-complement R5 terminal archive SHA-256:
  `b31a9b145b3bb8af6b6eda1be45c0b8d1cdea3819509c7e86873eb0284c3a2e9`

The original terminal archive is immutable input. Its member bytes are copied, not
rewritten. The replay adapter may create a separately named patched script whose
only mathematical addition is the semantic-control block below.

## Exact replay contract

The patched script must reproduce the original root chart and all original exact
markers. Before accepting its endpoint-zero output it must also certify, in the
same quotient reducer and chart:

1. the first bordered residual expression is zero;
2. adding the chart minor `DELTA` to that expression gives a nonzero normal form
   equal to `NF(DELTA)`;
3. the first diagonal endpoint coefficient has zero normal form;
4. adding `1` to that endpoint coefficient gives a nonzero normal form; and
5. `NF(e+1)-NF(e)-1` reduces to zero.

All three regenerated original artifacts named above must have byte-identical
SHA-256 values. Any Singular diagnostic, missing marker, failed mutation control,
source drift, artifact drift, nonzero swap, timeout, or containment failure is
`ADAPTER_FAILURE_NO_VERDICT` or `TIMEOUT_NO_VERDICT`, never mathematics.

## Scope firewall

The only production object is the literal TRIPLE03 root open `D(DELTA)` from the
frozen root-chart archive. A successful replay proves endpoint death only on that
open. It may be combined with the independently certified R5 closed complement
only after exact agreement and only as a scoped geometric cover of the literal
TRIPLE03 component. It does not establish a scheme-theoretic ideal equality,
nilpotence/radical statement, another component, or an ambient endpoint theorem.

## Execution contract

- AWS Linux on Amazon EC2 only; exact instance and hostname pinned at launch.
- Fresh immutable job tag and source archive; one pinned CPU.
- Zero configured swap at preflight, during telemetry, and at termination.
- 30-minute hard supervisor cap; 15-minute Singular production cap.
- 96 GiB virtual-memory cap and 32 GiB output-file cap.
- Fail closed on every Singular stdout/stderr diagnostic regardless of return code.
- Full source, original bytes, patched bytes, outputs, telemetry, and manifests
  archived; no orphan process may remain.
