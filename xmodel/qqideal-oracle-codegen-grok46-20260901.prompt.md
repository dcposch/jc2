# Research lane: QQIDEAL-ORACLE-CODEGEN — parallel-oracle window for the new stack

DC's software effort landed: `msolveio` 0.1.0 + `qqideal` 0.1.0
(pip, MIT) replace Macaulay2 as the GENERATION TARGET (msolve
stays the GB engine; Sage/SIROCCO stays for braids). Campaign
cutover policy: only after a parallel-oracle window — same jobs,
old stack vs qqideal; any disagreement is P0.

Your job: write the oracle window as Python against qqideal, for
the five corrected N=4 suite systems (audit §7.1, as encoded and
reviewed in the charged codegen + kill-review reports):
P1 (8,6,3), P2 (8,6,9), P3 (9,6,4) incl. the I_DP six-node
conditions, P4a (8,6,11), P4b (8,6,7).

qqideal API (coordinator-enumerated on the target box, v0.1.0):
  qqideal.ring(...), qqideal.ideal(...), qqideal.ideal_verdict,
  qqideal.double_point_ideal(p, q), qqideal.dimdeg,
  Verdict carries Kind + Certainty (MODULAR vs Q-exact); no
  boolean truth value.
msolveio API: emit_system(polynomials, variables,
  characteristic=0); run_groebner(source, gb=2, timeout,
  threads, binary, allow_unknown_version=False) -> RunResult
  (msolve_version, input_sha256, output_sha256);
  parse raises on solver-shaped bytes (EMPTY<->NONEMPTY inversion
  class closed at the library).
You cannot import these in your sandbox — write against the
signatures above; the coordinator executes on the box with
msolve 0.10.1 pinned via the binary parameter.

Deliverables:
(1) `box/qq_oracle_jobs.py` — one function per system building
    the corrected ideal EXACTLY as the reviewed derivation
    states (re-derive from the charged audit §7.1 + codegen
    derivation section; the kill-review's §2 re-derivation is
    the tightest statement — follow it), each returning the
    qqideal Verdict plus a custody dict (generator SHA-256 of
    the emitted system text via msolveio.emit_system, msolve
    version, wall time). Where the old jobs used Rabinowitsch
    opens and cover-colon loops, use qqideal's colon/saturate
    primitives; document the exact correspondence in comments.
    For P3's nodal conditions use qqideal.double_point_ideal —
    verify its contract against our I_DP definition (reduced,
    length delta_aff, immersive, distinct tangents) and state
    in a comment what it does and does not check.
(2) `box/qq_oracle_run.py` — runner: executes all five, prints
    a verdict table with certainty labels, and DIFFS against the
    recorded old-stack verdicts hard-coded from the charged
    reports: P1 EMPTY (two-engine, binding), P4a/P4b previously
    raw-NONEMPTY->vacated (expected: corrected systems decide
    fresh; record, do not assume), P2/P3 pending (record fresh).
    Any P1 disagreement prints ORACLE-P0 loudly and exits 2.
(3) Self-checks in the runner, reusing the reviewed three:
    (i) audit's charged A false-positive point must FAIL the
    corrected 8611 membership; (ii) the (9,6,2) exhibit curve
    must PASS its corrected membership; (iii) the HF-twin
    (9,6,4) point must PASS the corrected 964 locus (pre-nodal).
    Implement as pure-QQ substitutions (python-fractions or
    qqideal Poly evaluation), runnable WITHOUT msolve — run them
    in your sandbox NOW with plain Fraction arithmetic and print
    the transcripts verbatim in the report.
(4) Report with the derivation-correspondence table (old .ms/.m2
    encoding <-> qqideal calls, line-cited) and per-file SHA-256.

Report: `xmodel/qqideal-oracle-codegen-grok46-20260901.md`.
Seal-at-completion contract; target 15-25KB. PACE: write the
report sections as you go; do NOT leave the report to the end
(the bm-fact sibling died at the output cap doing exactly that).
charged_input=xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md
charged_input=xmodel/corrected-suite-codegen-grok46-20260901.md
charged_input=xmodel/corrected-863-kill-review-gpt55-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  {{LANE_INPUTS}}/encoding-faithfulness-audit-r2-sol56-20260901.md
d80c691861d362f1569b38c80a222c2df4992e62f13297adc2e5a996d99a0f18  {{LANE_INPUTS}}/corrected-suite-codegen-grok46-20260901.md
e9ddeaead333a544d2e896b4b5d827dd3bea867b5a04ea6bc15c7dd1a6c244bc  {{LANE_INPUTS}}/corrected-863-kill-review-gpt55-20260901.md
```
