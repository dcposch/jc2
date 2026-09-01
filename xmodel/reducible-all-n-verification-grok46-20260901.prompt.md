# Verification lane: REDUCIBLE-ALL-N — computation arm

Independent arm; computations only. Targets: (1) re-enumerate the
general-N budget profiles at N=6 and N=7 from scratch and diff
against the charged census; (2) verify the N=4/N=5 instance
recovery exactly matches the promoted cages (row for row); (3) the
NO-DEG-CAP witnesses (re-derive the family the report exhibits);
(4) spot-check three gate applications at N=6 (Zariski-Nagata,
eta/cover, per-component M-INF) numerically. HOLDS/BROKEN per
target.
charged_input=xmodel/reducible-all-n-opus5-20260901.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
7c63614eff87640789d4591c67d8f8ce7d48645310d3146e87c44ddfc0dddf89  {{LANE_INPUTS}}/reducible-all-n-opus5-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Desk-scale exact reasoning only; fetch/hash literature as needed; no
CAS. Do not edit canonical ledgers, any charged file, or inspect
`jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/reducible-all-n-verification-grok46-20260901.md
```

Skeleton first WITHOUT the BODY-END marker; bounded per-section
writes; seal only at completion; budget-short => type OPEN then
seal. Under 4,500 words. No charge_basis.
