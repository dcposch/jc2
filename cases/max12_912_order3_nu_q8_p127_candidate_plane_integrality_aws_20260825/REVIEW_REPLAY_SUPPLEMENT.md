# Independent review and AWS replay supplement

Date: 2026-08-25

The producer theorem for the pinned standalone polynomial `H(w,v)` received
an independent hostile different-model verdict of `CONFIRMED` in
`xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-review-claude-20260825.md`.
The reviewer independently checked the source semantics and mathematics but
had no shell or CAS.  The coordinator therefore also reran the exact frozen
case on AWS r6a host `ip-172-30-0-34`, tag
`q8_p127_candidate_plane_integrality_r6a_review_20260825T0855Z`.

The replay exited with `generator_rc=0`, `singular_rc=0`, `audit_rc=0`,
`rc=0`, and `endpoint=PASS`.  Its `input.sing`, `result.out`, `audit.json`,
`audit.out`, and three empty stderr files are byte-identical to the original
Box02 evidence.  The replay metadata additionally pins the candidate JSON of
SHA-256
`9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce`.

The reviewer found no required repair.  It supplied the compressed missing
edge case in the producer exposition: a repeated geometric component
`H=G^e`, `e>=2`, is excluded by the frozen squarefreeness certificate at
`w=25`.  Optional future hardenings are to assert that no support key exceeds
`190` and to include the cross-case candidate JSON in every successor
manifest.  Neither changes this frozen theorem.

Scope is unchanged: this supplement certifies only arithmetic irreducibility
over `F_127(w)` and geometric integrality over `F_127` of the explicit pinned
plane curve.  It does not establish selected-Q8 quotient membership,
coordinate reconstruction, contact membership, characteristic-zero lifting,
a trajectory exclusion, maximum-twelve, or JC2.
