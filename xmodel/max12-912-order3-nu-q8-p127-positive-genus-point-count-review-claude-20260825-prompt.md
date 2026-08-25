Act as an independent hostile algebraic-geometry and exact-software referee.
Read in full:

- `xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-20260825.md`
- every file in
  `cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825/`
- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
- its CONFIRMED review
  `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-review-claude-20260825.md`.

Audit, rather than restating, the exact standalone claim that the smooth
projective normalization of the pinned geometrically integral `H(w,v)=0`
over `F_127` has positive genus.

1. Verify the candidate pin, the construction and enumeration of
   `F_(127^2)`, and that the displayed quadratic modulus is irreducible.
2. Prove or refute the fibre formula using
   `gcd(H(w,v),v^(127^2)-v)`, and the second gcd with both partials.  Attack
   squarefreeness, repeated roots, zero/constant gcd degree conventions,
   partial-derivative construction, singular versus smooth counting, and
   possible missed affine points.
3. Audit every interval/partition, per-shard reconciliation, both independent
   AWS aggregates, source/hash pins, the four direct-enumeration controls,
   and the separation of the failed indentation-sensitive V1 aggregate from
   the accepted V2 endpoints.  Check whether the two host runs are genuinely
   independent evidence or merely identical-source replay, and phrase that
   accurately.
4. Prove or refute the genus argument: smooth affine rational points inject
   into the smooth projective normalization; a geometrically integral
   genus-zero curve with the reviewed `F_127`-rational smooth point is `P1`
   over `F_127`; and `#P1(F_(127^2))=16130`.  Check that
   `16168>16130` is sufficient despite uncounted points at infinity and
   singular branches.
5. Enforce the standalone-plane scope.  This producer must not infer quotient
   membership, component specialization, trajectory exclusion, maximum
   twelve, or JC2.  Identify the smallest repair for any mathematical,
   source, custody, or wording defect.

Do not use Bash, CAS, or network access; disclose that limitation.  Write the
complete review, and no other file, to
`xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-review-claude-20260825.md`.
End with exactly one token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `BLOCKED`.
