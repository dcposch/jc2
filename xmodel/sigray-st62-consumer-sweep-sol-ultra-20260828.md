# Sigray Statement 6.2 consumer sweep

Date: 2026-08-28 UTC.  Role: coordinator source/consumer audit.  This is a
desk audit of the exact text on printed page 29 of
`refs/sigray_full.pdf` and every substantive campaign use found by a scoped
search of the promoted `ladder/*.md` sources.  It does not audit Proposition
6.7 or Proposition 6.8; it identifies them as the newly exposed dependencies.
No heavy computation and no `jc2-lean` access occurred.

## Verdict

**The printed Statement 6.2 has a genuine omitted hypothesis, but the omission
has caused no presently identified wrong mathematical conclusion in a
promoted campaign document.**  Every load-bearing alternative child used by
AF2, III, MULTIPOLE, A2P, or the Statements 9.6--9.11 template is separately
put in `V_a cap T_a^+` by Proposition 3.2 plus Proposition 6.7 before the
regularity consequence is consumed.  Several documents had left that
dependency implicit; the four affected canonical derivations have now been
made explicit.

This is a conditional safety result, not a discharge of the source perimeter:
Proposition 6.7 is now visibly load-bearing and lies beyond the completed
72-item audit.  Proposition 6.8 is then the same-branch pole constructor used
by MULTIPOLE.  Both must be audited next.

## Exact defect and clean repair

The source states, for `F,G in V_a cap T_a^+` with `F=G+c`,

```
F in T_a^down  iff
d_G < (1-pi(G))*mult(p_G,c).
```

Its displayed computation proves this equivalence exactly.  It then says that
if `H=G+c*`, `mult(p_G,c*) >= mult(p_G,c)`, and `F in T_a^down`, then
`H in T_a^down`.  The calculation only proves the corresponding strict
inequality for `H`.  Membership in `T_a^down` additionally requires
`H in T_a^+`, which is neither stated nor implied by the preceding hypotheses.
An `H` with nonpositive `d_H` is the abstract failure mode.

The clean repaired clause is therefore:

> If additionally `H in V_a cap T_a^+`, then
> `mult(p_G,c*) >= mult(p_G,c)` and `F in T_a^down` imply
> `H in T_a^down`.

Equivalently, without the added domain hypothesis, retain only the strict
inequality proved by the displayed calculation.  No change to the iff is
needed.

## Consumer census

1. **`SHEET6-AF2.md`, R1/R2 and the two-direction kill.  SAFE conditional on
   Proposition 6.7.**  The parent lies in `T_a^down`; whenever the reduced
   pattern has another root, `deg p>1`.  Proposition 3.2 gives the alternative
   vertex and Proposition 6.7 puts it in `T_a^+`.  Thus both members of the
   Statement 6.2 pair lie in `V_a cap T_a^+`.  The document now states this
   before R2.

2. **`SHEET6-A2P-REVIEW.md`, R1/R2.  SAFE and already explicit.**  The review
   already records that the standing `F,G in V_a cap T_a^+` hypothesis is met
   and cites Proposition 6.7 for the alternative child.  No edit was needed.

3. **`SHEET6-III.md`, S3 regularity step.  SAFE conditional on Proposition
   6.7.**  The case has a down parent and more than one root, hence
   `deg p>1`; Proposition 3.2/6.7 supplies a positive alternative vertex.
   This chain is now explicit.

4. **`SHEET6-MULTIPOLE.md`, D5(c)/D6(a).  SAFE conditional on Propositions
   6.7 and 6.8.**  At the pre-merge down vertex, a non-chain root implies
   `deg p>1`; Proposition 3.2/6.7 supplies the positive child.  Only then is
   the Statement 6.2 computation used, after which Proposition 6.8 constructs
   the same-branch pole.  The repaired domain and dependency chain are now
   explicit in D5 and in the cross-consistency note.

5. **`SHEET6-CAMPAIGN.md`, root-pattern template extracted from source
   Statements 9.6--9.11.  SAFE conditional on Proposition 6.7.**  Outside the
   separately handled axis/case-IV branch, the parent and chosen child are the
   `V_a cap T_a^down` pair of Proposition 9.3.  The proofs invoke the
   multiplicity comparison only after `p` is known to have more than one root.
   Every existing alternative direction is therefore a vertex by Proposition
   3.2 and belongs to `T_a^+` by Proposition 6.7.  Regularity then excludes it
   from `T_a^down`, yielding the required strict multiplicity inequality.
   The template now records this chain.

6. **`SHEET6-DEPTH-REVIEW.md` and `BOOK-OFFAXIS-REVIEW.md`.  NO POSITIVE
   CONSUMER.**  The former explicitly says the clause is unused; the latter is
   a critique of a proposed off-axis argument, not a theorem relying on the
   omitted hypothesis.

Occurrences of “section 6.2” in PILOT, III, TDUNIFORM, and REVIEW that denote
local document sections are not Statement 6.2 consumers.

## Consequences

- No promoted Q-row, AF2 kill, III restriction, or MULTIPOLE conclusion is
  rolled back by this defect on the present audit evidence.
- Statement 6.2 remains a source `GAP` until the corrected clause is formally
  banked/reviewed; its iff is verified.
- The earlier risk description “a deep child may evade regularity” is resolved
  at known consumers only because Proposition 6.7 supplies positivity.  It is
  not resolved globally.
- Next source order: audit Proposition 6.7 first, then Proposition 6.8 and its
  termination/same-branch assertions.  If Proposition 6.7 fails or needs an
  auxiliary-`h`/suitable-`kappa` rider, reopen every conditional-safe row above.

## Filing edits

The following canonical files received dependency-only clarifications; no
formula, survivor set, or theorem conclusion changed:

- `ladder/SHEET6-AF2.md`;
- `ladder/SHEET6-III.md`;
- `ladder/SHEET6-MULTIPOLE.md`;
- `ladder/SHEET6-CAMPAIGN.md`.

