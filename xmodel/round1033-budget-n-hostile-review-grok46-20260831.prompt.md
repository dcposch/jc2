# Hostile review: BUDGET-N report (GPT-5.5) — source-typing audit

Different-model review of a source-typing report. Caution on
independence: the rank-four D-typing packet in this area is your own
model family's product; it was explicitly NOT exported by the charged
report and must not be used by you as evidence either — audit the
charged report strictly against the primary sources.

charged_input=xmodel/round1033-budget-n-gpt55-20260831.md
charged_input=xmodel/ideation-20260831T1033Z-synthesis.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
583562cb7fc32831f5faee84b009cf4cb12dc11a6619199e9a7bc7a463707b03  {{LANE_INPUTS}}/round1033-budget-n-gpt55-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
```

Tasks: (1) Re-open the pinned primary sources yourself — the cached
`refs/jc86.pdf` (verify recorded hash
`f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`),
the cached Chau PDFs in `refs/`, and fresh arXiv streams where the
report cites them — re-verify every hash the report records, then
check every quoted statement: Orevkov's Lemma 4.2 budget identity
exactly as displayed (summands, nonnegativity, Cor 4.3), the local
normal form Lemma 3.1 `u=x', v=y'^k` and whether it is stated at
generic branch points with the scope the report uses, the meaning of
`N` (geometric multiplicity vs degree), and Chau 2011's dicritical
definition and component-union statement under finite fibres. Flag
any quote that is a paraphrase doing extra work. (2) Verify the
derivation chain `2m_nt + m_triv <= sum_owners mu_l <= sum_L mu_l <=
N-1`: the distinct-owner selection, why owners' mu sum bounds by the
full `L_F` sum, and whether `mu_l>=2` for nontrivial generic inertia
really follows from the normal form as claimed — is "genuine
nontrivial inertia means k>=2" a theorem or a definition here? Type
it. (3) Verify the `N=5` table rows and the claimed impossibility at
`m_nt>=3`. (4) Verify the report indeed never uses "nontrivial pi_1"
as an inertia proxy, and that nothing from the unexported rank-four
packet leaks into the general-`N` rows. (5) The trivial-inertia fork:
is the ABSENT verdict for `mu_l>=2` at trivial inertia correct — or
does any primary source (including Orevkov's correction terms
`corr_l` and his Cor 4.3 context, or any Chau statement) actually
force more? If a source closes it, that is the day's biggest finding
— work it in full. Verdict per matrix row: CONFIRMED / REFUTED /
RETYPED, then an overall promotion recommendation for the weighted
bound at all `N`.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/round1033-budget-n-hostile-review-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 4,500 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
