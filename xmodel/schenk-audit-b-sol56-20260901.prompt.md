# Hostile audit (AUDIT-B-SOL56): Schenk's claimed proof of JC2

You are a full hostile audit lane on an EXTERNAL claimed proof of
JC2: Schenk, "A valuation-theoretic proof of the Jacobian conjecture
in dimension two" (Zenodo 18622130, 2026-02-12, 569KB PDF, charged).
The claimed strategy (per the sweep): normalize the projective graph,
Stein-factor, kill horizontal boundary (U-HIT), analyze affine
dicriticals by Rees degeneration, force positivity of the Jacobian
two-form, contradict the Keller identity, then finite-etale
triviality over A^2 + ZMT.

Your stance: DEFAULT TO REFUTATION, with the seriousness the claim
deserves. The campaign has independently promoted theorems in exactly
this territory (integration #6 chain: the Y=Spec B construction, the
four boxes, e = 1 + v(dx∧dy), B0 at all degrees under H2, the
weighted budgets) — use them as a REFERENCE FRAME to locate where
Schenk's chain must do real work: a sound proof must, at minimum,
handle the configurations our promoted results show to be consistent
up to their gates (ramified dicriticals with mu>=2 EXIST in our
analysis; reducible A_F configurations survive our machinery at
N>=5). Any Schenk step that would prove impossible a configuration
our promoted numerics exhibit as consistent deserves maximal
scrutiny — but equally, do NOT assume our framework is complete:
audit his argument on its own terms, lemma by lemma.

Protocol: (1) reconstruct the full logical skeleton (every lemma,
its exact statement, what it consumes); (2) verify each lemma
independently — flag VERIFIED / GAP / FALSE with the exact location
and a countermodel or missing-step description; (3) pay special
attention to: the U-HIT boundary-killing step (compare our promoted
purity/branch-locus machinery), the Rees degeneration of affine
dicriticals (does the degeneration preserve the Keller condition and
the dicritical structure? — degenerations often break exactness),
the two-form positivity step (our Lemma 4.2 gives v_l(dx∧dy) =
mu_l - 1 >= 1 at ramified dicriticals — a ZERO of the form, not a
pole; positivity arguments must handle sign conventions and the
boundary divisors at infinity where v(dx∧dy) < 0 — the form has
POLES at L_inf: total degree -3 on P^2 — check whether his
positivity bookkeeping accounts for the polar part), and the final
etale-triviality step (standard, but check what feeds it);
(4) verdict: SOUND (state it plainly with the full verified chain
— this resolves JC2), REPAIRABLE-GAP (the exact gap + whether our
promoted machinery fills it), or FATALLY-FLAWED (the exact false
step with countermodel). Work alone; a parallel independent audit
runs on another model; do not hedge toward consensus.
charged_input=refs/schenk_jc2_zenodo18622130.pdf
charged_input=xmodel/web-sweep-20260901-grok46.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24  {{LANE_INPUTS}}/schenk_jc2_zenodo18622130.pdf
23fab48635178dd905d67be2b9d0eeb8574b641be0d097c82af4a55bf4fcc7d4  {{LANE_INPUTS}}/web-sweep-20260901-grok46.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Desk-scale exact reasoning only; you may fetch and hash additional
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/schenk-audit-b-sol56-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,500 words. Do not include a `charge_basis` declaration.
