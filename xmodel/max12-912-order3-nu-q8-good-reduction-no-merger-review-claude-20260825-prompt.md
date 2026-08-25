You are a hostile, independent algebraic-geometry referee.  Work read-only
except for the single output file named below.  You have no Bash and must not
use web or network tools.  Do not edit any charged source, case artifact, or
top-level ledger.

Primary charge: rigorously attack the abstract DVR lemma and the claimed
sufficiency of its selected-Q8 discharge checklist in
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`.
The desired conclusion is *not* presumed true.  Seek a counterexample before
trying to repair the proof.

Read in full at least:

- `xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-candidate-q8-boundary-20260825.md`
- every source/result/README/manifest/freeze file in
  `cases/max12_912_order3_nu_q8_p127_candidate_q8_boundary_aws_20260825/`
- `xmodel/max12-912-order3-nu-q8-p127-rational-etale-point-20260825.md`
- `xmodel/max12-912-order3-nu-q8-infinity-primitivity-review-claude-20260825.md`
- the directly cited infinity, primitivity, formal-branch, and local-descent
  producer reports needed to understand what the proposed bridge consumes.

Audit these points explicitly:

1. Is the implication "pi non-zero-divisor and A/pi A a domain implies A a
   domain" valid in the stated noetherian local setting?  Check every use of
   Krull intersection and whether `A/pi A` really is a field at `eta_C`.
2. Does a horizontal generic curve component whose closure contains `q_i`
   necessarily have a one-dimensional special-fibre germ through `q_i`?
   Check closure versus normalization, flatness/torsion-freeness, dimension,
   embedded points, nonproperness, and whether local uniqueness at `q_i`
   really forces containment of `eta_C`.
3. Do closures of distinct *geometric* generic components correspond to
   distinct minimal primes after localization at `eta_C`?  Check finite DVR
   base change, ramification, residue-field extension, geometric
   irreducibility, and the misleading phrase "integral closure inside X".
4. Is each hypothesis necessary, redundant, or insufficient?  Construct the
   smallest explicit merger counterexample if the statement is false.  If a
   standard multiplicity-one specialization theorem is the correct result,
   state and prove the exact replacement without citing it as a black box.
5. Does checklist item 2 really promote the graph of H plus seven coordinate
   functions to a one-dimensional irreducible component rather than a proper
   subcurve of a higher-dimensional component?  Does a single 8x8 Jacobian
   point repair this, and must it be a Jacobian of the full original ideal?
6. Do the two fibre partitions plus one smooth rational point suffice for
   arithmetic irreducibility and then geometric integrality?  List all
   specialization/degree/content/flatness hypotheses needed.
7. At each of the eight boundary contacts, what exact full-source Jacobian or
   completed-local-ring statement is required for reducedness and unique
   one-dimensional local component?  Distinguish `H_v != 0` from a statement
   about the full eight-row solution scheme.
8. Does the checklist actually connect the eight characteristic-zero formal
   branches to horizontal generic components and their reductions, or is a
   properness/valuative-extension/denominator hypothesis missing?
9. Independently inspect the boundary replay source/result for its narrow
   advertised projection claim.  Do not promote it to component membership.
10. Trace the final logic into the reviewed primitive all-eight/singleton
    dichotomy and infinity exclusion.  Identify any hidden mismatch between
    the components used by those results and the scheme/components in the DVR
    lemma.

For every issue, classify it as fatal, repairable missing hypothesis,
wording-only, custody-only, or favorable strengthening.  Give a precise
corrected lemma and proof if repair is possible, then a revised minimal Q8
checklist.  State exactly what current evidence establishes and what remains
computationally unproved.  End with exactly one verdict token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, `INCONCLUSIVE`, or `REFUTED`.

Write the complete review only to
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-review-claude-20260825.md`.
