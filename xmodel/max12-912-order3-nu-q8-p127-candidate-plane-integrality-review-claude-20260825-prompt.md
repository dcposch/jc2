Act as an independent hostile algebraic-geometry and computational-algebra
referee. Read in full:

- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
- every file in
  `cases/max12_912_order3_nu_q8_p127_candidate_plane_integrality_aws_20260825/`
- the pinned candidate source needed by `generate.py`.

Audit, rather than merely restating, the exact claim that the explicit
`H(w,v)` is geometrically integral over `F_127`.

1. Verify the code really uses the pinned monic degree-190 candidate and
   emits the two advertised specializations without coefficient/order drift.
2. Check fail-closed parsing of Singular factorization, squarefreeness,
   retained degree, and the proper subset-sum sets `{2,188}` and
   `{1,3,4,186,187,189}`.
3. Prove or refute the specialization argument: monic factors over
   `F_127(w)[v]` descend to `F_127[w][v]`, and their `v`-degrees cannot drop
   after specializing `w`.
4. Prove or refute that arithmetic irreducibility plus the displayed smooth
   `F_127`-rational point implies geometric integrality; check constant-field,
   repeated-component, and perfect-field edge cases.
5. Enforce the exact standalone-plane scope and identify the smallest repair
   for any source, custody, or mathematical defect.

Do not use Bash, CAS, or network access; disclose that limitation. Write the
complete review, and no other file, to
`xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-review-claude-20260825.md`.
End with exactly one token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `BLOCKED`.
