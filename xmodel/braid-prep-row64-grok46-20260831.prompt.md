# Systems lane: BRAID-PREP — certified braid-monodromy job for the row family

You are a systems/preparation lane. The (6,4) row is now an explicit
one-parameter family (charged ZVK-U6 Theorem ROW-NF, PROVISIONAL):
x = r(t)^2, y = q(t), r = t^3+bt+c, q = t^4+(2b/3)t^2+(4c/3)t,
c != 0, modulus j = b^3/c^2. Deciding
OPEN[PI1S4-(6,4)-FACTORIZATION] needs the ACTUAL braid monodromy of
a row member: the conjugating words of the 5 tangency braids and 3
node braids over the 11 discriminant values, certified. Campaign
policy: heavy/uncertain computation is AWS-only. Produce the
complete job bundle.

charged_input=xmodel/pi1s4-64-zvk-u6-opus5-20260831.md
charged_input=xmodel/pi1s4-64-fixed-tuple-opus5-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  {{LANE_INPUTS}}/pi1s4-64-zvk-u6-opus5-20260831.md
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  {{LANE_INPUTS}}/pi1s4-64-fixed-tuple-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Deliverables in fenced blocks with exact filenames:

1. A SageMath script `braid_monodromy_row64.sage` using the SIROCCO
   certified-homotopy library (sage.schemes.curves via
   braid_monodromy(); confirm the exact API against current Sage
   docs — fetch and record the doc URL and version) to compute the
   braid monodromy factorization of the affine curve F(x,y)=0 for
   TWO rational parameter choices (pick (b,c) giving j generic, e.g.
   (0,1) — check c!=0, j=0 — and one with j=-27/4 excluded/included
   per the cross-locus correction: pick also (b,c)=(1,1), j=1),
   where F is the implicit equation: derive F symbolically in the
   script from the parametrization by resultant
   (Res_t(x - r(t)^2, y - q(t))), verify degree 6, irreducibility,
   and the three nodes (discriminant checks) before the monodromy
   call.
2. A postprocessing script `check_s4_tuples.py` (pure Python): given
   the braid factorization as words in B_6 (Sage generators), (a)
   verify the product equals the expected rho_inf up to conjugacy
   via exponent sum e=11 and permutation type; (b) enumerate ALL
   6-tuples of S_4 transpositions (46656) and test Hurwitz-
   fixedness under EVERY factor (the full monodromy group), plus
   the generation and node-disjointness conditions from the charged
   reports; output the surviving count and tuples. Include a
   negative control (a random braid word whose fixed set should
   differ) and the rho_inf-only positive control (must reproduce
   72 per the promoted count — cite it as the expected value).
3. `run_braid_job.sh` driver with caps and logs; installation notes
   for sage+sirocco on Ubuntu (apt/conda exact commands).
4. SHA-256 manifest of every file body.

M2/Sage dialect discipline (after today's failures): flag every API
call you could not verify against fetched documentation; prefer
long-form explicit code over clever idioms; no reserved-name
variables (pi, gamma, I, O); every assertion message self-describing.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/braid-prep-row64-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
7,000 words. Do not include a `charge_basis` declaration.
