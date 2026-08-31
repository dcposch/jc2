# Preflight lane: AS109-D12 seed-provenance reconciliation

You are a bounded reconciliation lane on the disproof side. Do not
edit canonical ledgers, any charged file, or inspect `jc2-lean`.
Desk-scale exact reasoning only; no CAS, no computation of uncertain
duration.

charged_input=xmodel/ideation-20260831T1033Z-sol56.md
charged_input=xmodel/ideation-20260831T1033Z-grok46.md
charged_input=xmodel/ideation-20260831T1033Z-crosspoll-sol56.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
7bf7502e43a6bdd344b1c177cf3c2e83afd9ca464b7aeab451b96e6db7528b46  {{LANE_INPUTS}}/ideation-20260831T1033Z-sol56.md
329182487ac3e771be9aa73ded7b9f21c6ea3fd8e13235caafb8e103c96007a3  {{LANE_INPUTS}}/ideation-20260831T1033Z-grok46.md
426c7305fc215a3d55ef6a1d429f66c22071ac442384d6ca3d151b9d9029fad2  {{LANE_INPUTS}}/ideation-20260831T1033Z-crosspoll-sol56.md
```

The collision (cross-poll §"provenance/ring collision"): Sol's round
submission names an `F_109`/`AS109` fixed-support seed at its lines
99-101 and 142-148, while Grok's submission at its lines 90-98
describes an all-Witt `F_3` Artin-Schreier tower AND a 109-sheet
`Z_109` Hensel lane as distinct objects. Matching "AS", "109",
"degree 12" labels prove no ring map. The campaign's historical AS109
artifacts are the tracked `xmodel/as109-*-20260824*.md` files plus any
`as109` mentions in later ideation rounds; read them in place
(read-only) and cite by filename and line.

Deliver, fail closed at every step: (1) the definitive seed registry —
for EVERY distinct object that any artifact calls "AS109" or
"degree-12 disproof seed": its exact base field or coefficient ring
(`F_3`, `F_109`, `W(F_3)`, `Z_109`, ...), defining equations or tower
data as literally written, `x` and `y` support, generator order and
gauge, and the artifact+line where each field is stated (UNSTATED is
an allowed and important value); (2) the ring-map audit — for each
pair of registry entries, either an explicit map written down in some
artifact (cite it) or the verdict NO MAP CLAIMED; flag any artifact
that silently treats two entries as one object; (3) the reconciliation
verdict: SINGLE SEED (all labels resolve to one object — exhibit the
identifications), DISTINCT SEEDS (name each and state which the
matrix programme should target, with the deciding criterion), or
IRRECONCILABLE-AS-WRITTEN (name the exact missing datum per seed); (4)
the minimal preflight the matrix lane must run before charging
anything. You reconcile provenance only — do NOT evaluate whether any
seed actually threatens JC2. Three hours hard budget.

Write one report and no other file:

```text
xmodel/as109-d12-seed-provenance-reconciliation-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
