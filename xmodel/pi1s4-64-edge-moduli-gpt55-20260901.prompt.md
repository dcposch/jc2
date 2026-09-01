# Research lane: EDGE-MODULI — the two excluded j values

Bounded lane on TORUS-CHECK residual R2: the row moduli
j in {-27/4, -81/16} are outside Theorem ROW-KILL (the three-
ordinary-node stratum). Determine the affine singularity type of the
row curve at each excluded j (from ROW-NF: j=-27/4 is the (2,1)
cross-locus / tacnode candidate per the reviewed correction; -81/16
per the torus-check §3.4), then: if the singularities remain nodes
+ possibly A_2/A_3-type double points of smooth branches, run the
NO-TORUS + INF-TRIVIAL + Shimada chain for those members (the
promoted N-A/PI1-S4 machinery covers tangential double points; an
inner-singularity reopening per Oka's calculus needs A_2/A_5 or
mult>=3 — check what actually occurs); if a genuinely inner-capable
singularity occurs, type the residual precisely. Deliver: the two
members KILLED (extending ROW-KILL to the whole row), or the exact
typed residual per j.
charged_input=xmodel/pi1s4-64-torus-check-opus5-20260831.md
charged_input=xmodel/pi1s4-64-zvk-u6-opus5-20260831.md
charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe  {{LANE_INPUTS}}/pi1s4-64-torus-check-opus5-20260831.md
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  {{LANE_INPUTS}}/pi1s4-64-zvk-u6-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-edge-moduli-gpt55-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
4,500 words. Do not include a `charge_basis` declaration.
