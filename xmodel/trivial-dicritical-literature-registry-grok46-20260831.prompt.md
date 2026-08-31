# Scout lane: the trivial-dicritical question in the literature

You are a bounded literature-registry lane on what is now the
campaign's single convergent open bit. Three independent lanes reduced
the rank-four master identity, the all-degree component budget, and
the sheet-location gap to one question:

> Can a Keller map `F:C^2->C^2` (Jacobian a nonzero constant, not
> invertible) have a TRIVIAL dicritical: a dicritical divisor `l` at
> infinity whose image closure is an affine curve (a component of the
> non-properness set `A_F`) and whose generic local degree is
> `mu_l = 1` — equivalently, by the day's Lemma 4.2, a divisorial
> valuation `v` at infinity with `v(dx∧dy)=0` that is dicritical for
> `F` with affine image?

charged_input=xmodel/ideation-20260831T1033Z-synthesis.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
```

Your job is a REGISTRY, not a proof. Sweep the primary literature on
dicritical divisors and non-properness sets of Keller maps: Orevkov
1987 (cached `refs/jc86.pdf`), the cached Chau papers in `refs/`
(1999 Ann. Polon. Math. 71; the 2003/2004 non-proper value set note;
2011 pencil paper), and fetch-and-hash beyond them: Abhyankar's
dicritical divisor series (with Luengo; Artal Bartolo), Cassou-Nogues
on dicriticals, Le Dung Trang & Weber on the Jacobian conjecture and
dicritical/rational fibrations, Gwozdziewicz, Jelonek's non-properness
papers, Cassou-Nogues--Daigle if relevant, and anything any of these
cite that bears directly on multiplicities/ramification of dicriticals
under the Jacobian condition (e.g. statements like "each dicritical of
a Keller map is ramified", "A_F is contained in the critical values of
the extension", asymptotic-value structure, Newton polygon
constraints at infinity on dicritical valuations).

For every statement found: exact source (title, venue, year,
theorem/lemma number, page, PDF SHA-256 of what you fetched), the
statement verbatim or a scope-faithful transcription, its hypotheses
(is `F` Keller or general polynomial? plane only? finite fibres?),
and what it yields for the boxed question: FORCES `mu>=2` (closes),
PARTIAL (closes under named extra hypotheses — type them), STRUCTURE
(relevant but not decisive), or NOTHING. If several sources combine
to close it, exhibit the combination as a typed chain with every link
cited — flag any link that is your own inference rather than a
source statement. End with: verdict SOURCED-CLOSED / SOURCED-PARTIAL
/ ABSENT; the three most promising attack routes if ABSENT; and the
exact acquisition list (papers to pin) for a successor proof lane.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/trivial-dicritical-literature-registry-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
