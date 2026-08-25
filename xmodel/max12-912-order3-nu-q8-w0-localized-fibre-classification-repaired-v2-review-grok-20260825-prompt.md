Act as an independent hostile algebraic-geometry and computer-algebra referee.
The producer is GPT-family; you are the required different-model Grok
reviewer, and you also reviewed V1. Read in full:

- `xmodel/max12-912-order3-nu-q8-w0-localized-fibre-classification-repaired-v2-20260825.md`;
- V1 report and your V1 review named and hash-pinned there;
- `cases/max12_912_order3_nu_q8_w0_localized_fibre_classification_repaired_v2_aws_20260825/PREREGISTRATION.md`,
  `find_irreducible_prime.py`, both factor generators, the valid V2 factor
  runner, `replay.py`, the valid V2 replay runner, `MANIFEST.sha256`, and
  `FREEZE.sha256`;
- every accepted AWS input/output/source hash/run.meta named in that manifest;
- the failed Singular factor-parser V1 input/output as a negative control;
- the immutable V1 case manifest/freeze and exact parent sources named by the
  successor.

Audit the repaired successor from source rather than trusting PASS strings.
Charge each V1 repair separately:

1. verify that the prose now cites the actually computed loaded Q8-singular
   ideal containing `inu*e6-1`, and that deleting/adding this inverse is
   licensed only because the reviewed `e6`-unit statement already holds;
2. independently check the degree-eight Rabin criterion over F7, the
   primitive/good-reduction implication to irreducibility over Q, and the
   separate Singular factor-count/mutual-divisibility parser; make sure the
   failed `intvec` attempt is not consumed;
3. verify both missing characteristic-zero non-Q8 `V(e8)`/`D(e8)` ideals on
   both engine/order implementations, literal inverse equations, source-row
   reductions, and unit-ideal interpretation;
4. verify that shape-basis provenance is narrowed and not needed for the V1
   dimension/kernel scheme-isomorphism argument;
5. verify the explicit transitive order-three fibre/descent hashes in every
   applicable new lane, distinguishing the octic-only factor lane;
6. verify the corrected-octic sign/associate wording.

Also attack the manifest, fixed stdout hashes, wrapper negative controls, and
the final replay. Check that V2 makes no new horizontal-specialization
inference: it remains only the finite affine `p=1,k=mu=0,w=0,
x5*(x3-2*x5)!=0` scheme. Boundary incidence, horizontal closure,
relative-projective escape, terminal, both true-centre Taylor families,
`p=0`, other `(9,12)` leaves, maximum twelve, Keller, and JC2 must remain
charged.

List every mathematical, source-fidelity, custody, or scope defect, even if
repairable. Do not use Bash, CAS, network access, or write/edit any file;
disclose that limitation. Return a self-contained review on stdout, at most
2,500 words. End with exactly one verdict token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `BLOCKED`.
