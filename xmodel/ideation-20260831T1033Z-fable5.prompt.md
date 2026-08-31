# Blind full-portfolio ideation — round 20260831T1033Z

You are one of four equal-standing blind researchers in a full
whole-portfolio ideation round. You see the sealed packet and frozen
canonical inputs only; you must not look for, read, or reference any
other researcher's submission or any file outside the frozen inputs and
the primary mathematical literature. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`.

charged_input=xmodel/ideation-20260831T1033Z-packet.md
charged_input=APPROACHES.md
charged_input=AUDIT.md
charged_input=xmodel/block-descent-a1-rank4-irreducibility-coordinator-integration-fable5-20260831.md
charged_input=xmodel/block-descent-a1-wave23-coordinator-integration-fable5-20260831.md
charged_input=xmodel/block-descent-a1-harvest-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`. Verify the
packet hash first and stop on mismatch:

```text
196e1700fbc46855c5ebd3dbb5d28997cfa1b56a0ba75c0a3049c03dfb55b476  {{LANE_INPUTS}}/ideation-20260831T1033Z-packet.md
```

Read the packet, then the whole of `{{LANE_INPUTS}}/APPROACHES.md`
(overlays newest-first plus the 46-row inventory), the current-state
entries at the top of `{{LANE_INPUTS}}/AUDIT.md` (roughly the first 250
lines; deeper is provenance), and the three integrations. Then submit,
in this exact structure:

1. **Disposition vector** over the 46-row avenue inventory: for each
   numbered avenue (S/G/F rows of the master union table), one of
   `unchanged`, `raise`, `lower`, `reopen`, with a reason for every
   change. Compact table form.
2. **Bottleneck reranking**: the principal proof bottlenecks and the
   principal disproof bottlenecks, each ranked, each with one sentence.
3. **At least one genuinely new avenue or mechanism** — not a
   restatement of a listed one.
4. **At least one new connection between existing avenues.**
5. **The strongest proof attack and the strongest counterexample/
   falsification attack** available this week, each with its cheapest
   decisive first computation.
6. **One software acceleration or decisive experiment.**
7. **A campaign-systems check**: either an `UPGRADE` card (smallest
   useful test or implementation) or `NO_CHANGE` with evidence.
8. **At most three detailed idea cards**, each with explicit
   dependencies, cheapest discriminator, interpretation of each
   outcome, stop condition, and expected information gain.
9. **`continue / redesign / stop`** for each current major lane named
   in the packet's state summary.

Ground every claim in the frozen inputs or named primary literature;
flag any packet statement you believe is wrong rather than silently
working around it. Do not propose work already recorded as promoted,
refuted, retired, or stopped in the frozen inputs.

Computation rules: desk-scale reasoning only; you may fetch primary
literature (record exact sources). Never run Singular, msolve, any CAS,
or any computation of uncertain duration or memory on this machine.

Write one report and no other file:

```text
xmodel/ideation-20260831T1033Z-fable5.md
```

Create the report file with a skeleton of section headers as your first
action and append each completed section as you finish it. Keep it
under roughly 7,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
