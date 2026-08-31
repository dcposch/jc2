# Systems lane: SEMANTIC-REPLAY/v1 — replay-integrity CI gate

You are a systems build lane implementing the round-1033 synthesis §4
systems trial. Do not edit any file outside your report; never inspect
`jc2-lean`.

charged_input=xmodel/ideation-20260831T1033Z-synthesis.md
charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
charged_input=xmodel/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
```

Spec (synthesis §4, verbatim contract): every finite-exhaustiveness
replay certificate must declare, per promoted claim, (a) the generator
whose output it consumes, (b) one accepted and one rejected witness
driven through the actual production path, and (c) one metamorphic
generator mutation that must change the claim digest; the gate FAILS
on invariance (mutation does not change the digest) or bypass (witness
not produced by the declared generator/path). Acceptance tests, both
mandatory: the quarantined 16-row reducible ledger (charged) must FAIL
the gate as-is; the reviewed conductor census (charged) must PASS
after you write its (compliant) certificate from data already present
in the artifact — if the census artifact does NOT contain enough to
write a compliant certificate, that is a finding: report exactly what
is missing instead of inventing it, and demonstrate the gate failing
for the right reason.

Deliverables in the report: (1) the declaration format, as a small
schema embedded in replay certificates (plain text or JSON, additive
to existing artifact conventions — nothing existing is renamed); (2)
`ops/replay_gate.py` — a checker with a CLI (`check <certificate>`,
exit 0 pass / 3 fail-invariance / 4 fail-bypass / 2 malformed) and
pure-stdlib implementation, presented as ONE fenced unified diff
adding the new file plus `ops/test_replay_gate.py` with tests
covering: compliant pass, invariance fail, bypass fail, malformed
certificate, and BOTH acceptance fixtures (small inline extracts of
the charged artifacts are fine as test data — cite the exact source
lines you extracted); (3) a worked walkthrough of both acceptance
runs with expected output. The coordinator applies the diff and runs
the suite; a diff that does not apply to a clean tree is a failed
lane. Keep it minimal: no CI-runner integration, no changes to
existing tools.

Desk-scale only; no CAS. Three hours hard budget.

Write one report and no other file:

```text
xmodel/systems-semantic-replay-v1-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your
very first action and append each completed section as you finish it.
End its body with a single standalone `<!-- BODY-END -->` line and
write absolutely nothing after that line. Do not include a
`charge_basis` declaration.
