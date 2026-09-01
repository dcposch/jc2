# Verification lane: THEOREM EXHAUST — computation arm

Second arm of the paired review; independent; computations only.

Targets: (1) the semigroup arithmetic: S_D = <6,4,3>? compute the
gaps of <Δ> for Δ=(6,4,3) and (8,4,6,3), verify #gaps matches the
claimed δ_aff=3 at both rows and δ_∞=7/18 via the cluster identity;
(2) the §4 dimension count: replicate it concretely — for a one-place
(6,4) curve with 3 ∈ S_D, construct the degree filtration and verify
the count forces an element of pole degree 3 whose square... (follow
the report's own steps at two explicit examples: one ROW-NF member,
and one SYNTHETIC one-place (6,4) parametrization NOT in obvious fold
form — apply the §4 algorithm to it and verify it lands in the family
after the constructed automorphism — this is the strongest possible
test); (3) the (8,4) direct landing: take one explicit (8,4) member,
run the §5 proof steps, confirm arrival at a D_{b,c}; (4) GM Thm
2.1: fetch, hash-match `637acfd1…`, verify the statement as quoted;
(5) the transport composition on an explicit T (write a nontrivial
triangular automorphism and push a hypothetical meridian-transposition
rep through it, checking meridian classes). Verdict per target:
HOLDS / BROKEN / UNTESTABLE.
charged_input=xmodel/row-nf-exhaustiveness-opus5-20260901.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
30eb230dca026da6d59cbc7dd733cdb4ca63af443d5069ee83f7713b83a357f3  {{LANE_INPUTS}}/row-nf-exhaustiveness-opus5-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/row-nf-exhaustiveness-verification-grok46-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
