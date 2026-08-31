# Systems lane: MSOLVE-PREP — job files for the six realization ideals

You are a systems/preparation lane. The charged NODAL-REALIZATION
report specs six finite CAS computations (msolve/Macaulay2 scale)
deciding the (8,6)/(9,6) nodal-realization types, each with a
positive control ((6,4,3): I_DP length 3 reduced) and a negative
control ((t^8,t^6): gcd-2). Campaign policy: heavy/uncertain CAS is
AWS-ONLY. Your job: produce, as your report, the complete
ready-to-run job bundle so the coordinator can launch it on an AWS
box verbatim.

charged_input=xmodel/nodal-realization-86-96-grok46-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08  {{LANE_INPUTS}}/nodal-realization-86-96-grok46-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Deliverables, all inside fenced blocks with exact filenames:

1. For EACH of the six types (§2-§7 of the charged report): the
   polynomial systems written out FULLY — expand the h_k / k_i
   coefficient polynomials from the parametrization ansatz exactly
   as the report defines them (do the symbolic expansion by hand,
   carefully; this is the error-prone step, show intermediate
   degree checks), in msolve input format (and a Macaulay2 .m2
   mirror for cross-checking), with the open conditions and
   saturations (gcd-loci, h_next != 0) encoded per the report's
   prescriptions (saturation via added inverse variables or
   colon-ideal steps in M2 — follow the report's §0 discipline:
   extract components, assert rings, no blind sat()).
2. The two control inputs, same formats.
3. A driver shell script `run_realization_suite.sh`: runs controls
   first (abort if controls fail), then the six systems, each with
   a wall-clock cap (suggest per-system caps from the report's size
   estimates), writing per-system logs and a summary table; plus
   the double-point-scheme post-check step for any solution point
   (the I_DP reduced-length test) as an M2 script.
4. A verification manifest: for each file, its SHA-256 (compute
   after writing the content in your report — the coordinator will
   re-hash after extraction), plus expected-output notes (what
   EMPTY vs nonempty means per type, from the report's verdict
   rules).

You may not run any of these. Desk-scale symbolic expansion only.
Flag any place where the charged report's spec is ambiguous instead
of guessing.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/msolve-prep-realization-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
7,000 words. Do not include a `charge_basis` declaration.
