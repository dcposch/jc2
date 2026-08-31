# Research lane: SHEET-GATE — locate the fixed sheets, or park (M)

You are a bounded primary research lane. Your own model family produced
the Euler-inertia identity (M) in this round; two independent
cross-pollination attacks broke its conversion step, and this lane is
the repair-or-park gate. Do not edit canonical ledgers, any charged
file, or inspect `jc2-lean`.

charged_input=xmodel/ideation-20260831T1033Z-opus5.md
charged_input=xmodel/ideation-20260831T1033Z-crosspoll-sol56.md
charged_input=xmodel/ideation-20260831T1033Z-crosspoll-grok46.md
charged_input=xmodel/ideation-20260831T1033Z-synthesis.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
240adb4b4720cbc27caf879f95b9cdb1ac9dc62b7807183028f6b63a5d8b80ea  {{LANE_INPUTS}}/ideation-20260831T1033Z-opus5.md
426c7305fc215a3d55ef6a1d429f66c22071ac442384d6ca3d151b9d9029fad2  {{LANE_INPUTS}}/ideation-20260831T1033Z-crosspoll-sol56.md
8db5e5389e1aadf73447898748af8195a020e7150434a59d727a7758c6c2c10f  {{LANE_INPUTS}}/ideation-20260831T1033Z-crosspoll-grok46.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
```

The attacks you must answer exactly (see the two cross-pollination
reports, their sections on the strongest proposal): (i) a
monodromy-fixed sheet may close up on the boundary `Y-U` of the finite
normalization, so `#F^{-1}(p) = #Fix(H_p)` is unproved — countermodel
`q: Delta -> Delta` identity with `U = Delta^*`; (ii) the assembly
silently uses that `F^{-1}(D - Sing D) -> D - Sing D` is a finite
covering of degree `sigma`, a claim the packet parenthetically
discarded; (iii) ordinary `e` on singular curves needs a written
`chi_c` lemma; (iv) `s_p` must be computed from Puiseux local
monodromy, not from infinity colourings.

Task, in order: (1) build the four-box audit at the generic point of
the unique rank-four branch — sheet center in `U` versus `Y-U`, and
`e=1` versus `e>1` — and determine, with sourced or fully proved
statements only, which boxes are empty for a Keller source; (2) prove
or refute the covering lemma (ii) and the sheet-location theorem needed
for (i), using any promoted campaign input (the census fibre counts
`f(z)=2` at generic `B`, the companion floor, etale-ness) — note the
promoted quartic census DATA are consistent with `b=0`; the question is
whether a THEOREM forces it; (3) write the `chi_c` additivity lemma for
(E) or type it OPEN; (4) state the corrected identity that actually
holds — (M) if rescued, the weighted/inequality form with the `a`,`b`
bookkeeping if not — and exactly which corollaries survive at which
scope; (5) list what remains OPEN. A parked (M) with a clean weighted
inequality is a fully successful outcome; do not force the strong form.
Six hours hard budget.

Computation rules: desk-scale exact reasoning only; you may fetch and
hash primary literature (record exact sources). Never run Singular,
msolve, any CAS, or any computation of uncertain duration or memory on
this machine.

Write one report and no other file:

```text
xmodel/round1033-sheet-gate-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Include a `charge_basis` declaration only if you assert a genuinely new
exit price with a direct mathematical-source citation; otherwise omit
it entirely.
