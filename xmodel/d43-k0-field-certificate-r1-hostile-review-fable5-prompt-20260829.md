# Hostile source review: D43 K0 field certificate R1

You are Fable 5 acting as a different-model adversarial mathematics and
certificate-source referee.  Work in `/Users/dc/code/math/jc2`.

Review the exact packet
`cases/d43_k0_field_certificate_r1_20260828/`.  Read its
`REVIEW_REQUEST.md` completely and execute every applicable attack.  Treat
the producer report as allegation, not evidence.

## Frozen charge

- Packet `SOURCE_SEAL.sha256` full-file SHA-256:
  `583db53e641adfee8dec8cc3f5f4fc2c413b2f2651362790bea9d08dea5cb611`.
- `SOURCE_ARCHIVE.tar` SHA-256:
  `e5d140db10194f1cab0812e3eaa003ca7aafd36a6e2b1fb11c153862975790b5`.
- `REVIEW_REQUEST.md` SHA-256:
  `d61e56aa890861ebbfcfe9a915a266822651d1b1e42557ff4eead319efbf6ce2`.
- Producer report
  `xmodel/d43-k0-field-certificate-r1-opus5-20260828.md`, SHA-256
  `2fac39ec75073fda92d3dff2ccd88ee37289bb36dd841a65a58b9ca2fdf81887`.
- Theorem report
  `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md`, SHA-256
  `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430`.
- Independent theorem review
  `xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md`, report-body
  seal
  `877e451f33b24b7714c712404401f11b35b6621e80400e791c4b54cfbe5078fd`.

## Required work

Replay the packet seal/archive determinism and bounded Python preflight.
Read every Python gate, every GP `chk`, the runner/supervisor/worker, mutation
battery, manifests, and authorization contract.  Attack every item A--F in
`REVIEW_REQUEST.md`, especially:

- whether the character specializations really prove Kummer rank two and
  where valuation/integral-closure input enters;
- whether monic freeness plus Kummer independence is gated end-to-end rather
  than asserted by literals;
- every gate's falsifier and every load-bearing literal not reachable through
  `Spec` mutations;
- named-gate behavior for all MUST_FAIL and the real reason both MUST_SURVIVE
  mutations survive; construct at least one new surviving mutation;
- GP 2.15.4 syntax/semantics risks and the exact consequence of never having
  executed the GP file;
- archive/terminal TOCTOU, single-writer, duplicate-run, regex-policy and
  provisional instance-type issues;
- strict separation of unconditional K0, conditional E-ratio, corroboration,
  and forbidden D43/JC2 claims.

No AWS launch or registration is authorized.  Do not run heavy CAS locally.
Do not inspect unrelated repository paths, run global status/inventory
commands, delegate, or access `jc2-lean` in any way.

## Output

Write only
`xmodel/d43-k0-field-certificate-r1-hostile-review-fable5-20260829.md`.

Return exactly one source verdict: `PASS_FOR_PINNED_GP_REHEARSAL`,
`REPAIR_REQUIRED`, or `FAIL`.  A PASS only licenses a separately authorized
one-core live PARI rehearsal; it does not itself certify a two-engine run.
List exact replay evidence, theorem/scope limits, all defects, and the minimal
next action.  End with a report-body self-hash.

No canonical-ledger edits, commit, push, web, or AWS action.
