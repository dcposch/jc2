# Task: hostile review of generic PCB as quotient-collision surplus

You are Claude Opus 5, acting as an independent adversarial mathematical
reviewer.  Work on repository basis commit
`31777ce90994a106aade85064c0d868e32863f94`.  Write exactly one deliverable:

`xmodel/pcb-generic-collision-surplus-hostile-review-opus5-20260829.md`

Write no other repository file, do not edit canonical ledgers, do not use git,
and do not enter, enumerate, search, read, build, status, modify, or control
`jc2-lean`.  Do not browse the web.  Temporary scratch outside the repository
is permitted.  Do not run Singular or any heavy/uncertain computation locally;
the permutation and integer checks requested below are desk-scale.

Review the sealed producer
`xmodel/pcb-generic-collision-surplus-sol56-20260829.md`, full SHA-256
`412091929a68e8539148d00c24ee71e1d0c45185571b48be55be19d3efe0813f`,
body SHA-256
`a2cf302ad66c01980e2e70c482ab0d9914b9b616525736d5735a9de7900a147f`.
Do not treat it as an oracle.  Reconstruct the argument from the exact
actual-weight packet
`xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md`
and its hostile review
`xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md`,
and check the Suzuki input against
`xmodel/dual-pencil-definition-gate-20260824.md` and
`xmodel/dual-pencil-review-grok-20260824.md`.

Attack, at minimum, and return a separate `CONFIRMED`, `REFUTED`, or `GAP`
verdict for each item:

1. The fixed-fibre Euler-Fubini identity
   `d-chi_a=sum_i sum_(P_i(z)=a) w_i(z)` and every finiteness or
   constructibility hypothesis it needs.
2. The generic identities `d-chi_gen=sum_i d_i b_i`,
   `n=sum_i d_i`, and
   `E_gen=sum_i b_i(d_i-1)+chi_gen-1` without identifying places, flags,
   series, or quotient points.
3. The exact collision formula
   `chi_a-chi_gen=sum_i b_i(d_i-q_i(a))-epsilon(a)`, including the sign,
   distinct-root convention, and nonnegativity of `epsilon(a)`.
4. The finite ramification sum `sum_a(d_i-q_i(a))=d_i-1`, the grouping
   `sum_a epsilon(a)=sum_i(I_i-b_i)`, and compatibility with Suzuki's total
   defect.
5. Equivalence of generic PCB to
   `sum_i b_i(d_i-1)>=2G+2s+n-2`, including all Euler-characteristic
   conventions and the claimed margin `Xi`.
6. The exact boundary germ in Section 4.1: the two-form, generic and collided
   local degrees, baseline five, and its non-polynomial scope.
7. Independently recompute the three permutations, product, transitivity,
   Riemann--Hurwitz genus, puncture counts, and the claimed admissible
   collision topology in Section 4.2.  Distinguish what follows from the
   permutation data from what would require an actual algebraic family.
8. Decide whether the matched local/Hurwitz controls really establish the
   stated dependency barrier, and identify any sentence that overclaims a
   refutation of `WEIGHT-AT-ATYPICAL`, PCB, or an actual polynomial theorem.
9. Audit the proposed `QCS-MARGIN/v1` source packet and say whether it is the
   cheapest honest next discriminator; list any missing required field.

State the maximum exact theorem safe to promote, all repairs, and the
cheapest decisive successor.  Formal boundary data are not a polynomial
map; a local germ and a Hurwitz passport are not one global source; a floor
is not attainment.  End the report with one standalone `<!-- BODY-END -->`
line and no seal block.
