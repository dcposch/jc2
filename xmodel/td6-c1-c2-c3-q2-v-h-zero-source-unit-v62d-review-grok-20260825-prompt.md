# Hostile bounded review charge: TD6 V62D `V=H=0,D(U)` source unit

Act as an adversarial algebra/source/custody reviewer.  This is a bounded,
read-only audit.  Do not edit producer bytes, canonical ledgers, or any file
except the requested review report.  Do not run the substantive replay or any
local CAS/heavy computation.  Hashing, archive extraction to a private `/tmp`
directory, source reading, and short exact hand checks are allowed.

Read in full:

- `xmodel/td6-c1-c2-c3-q2-v-h-zero-source-unit-v62d-aws-20260825.md`;
- `cases/td6_c1_c2_c3_q2_v_h_zero_source_unit_v62d_aws_20260825/README.md`;
- that case's `MANIFEST.sha256`, `FREEZE.sha256`, `verify.py`, two AWS
  outputs, three proof artifacts per host, and portable source archive;
- the source archive's `SOURCE.sha256`, `V62D_SOURCE.sha256`,
  `V62D_RUNBOOK.md`, V62D producer, and the exact parent portions it consumes;
- the separately frozen direct U-zero report only as a scope/composition
  boundary, not as evidence internal to V62D.

Adversarially verify or refute, separately:

1. Source typing and ring: fixed `(c1,c2,c3)=(C,V,U)`, `H=C-3U^2`, raw
   `V=H=0` over the rational function field with arbitrary `beta`, direct
   `q_beta`/`q_beta'`, and no illicit specialization or normalization.
2. Exact ranks and dependencies: first `38/132`; previous/pole `37/94`;
   exactly the two nonzero dependencies `('X-1',11)` and `('X-1',13)`.
3. The Bezout/sign normalization really gives reduced target `1`; the
   combination is returned to raw previous equations before one original-
   first-pivot polynomial division; the resulting first+previous
   multipliers replay `1` from arbitrary-degree original rows.  Check that
   the serialized certificate corresponds to the asserted source identity,
   not only to echelon rows.
4. No current, N13, or P12 dependency is smuggled into this theorem.  Check
   the two omission controls are meaningful.
5. Denominator completeness: audit every source multiplier/coefficient and
   every normalized first/previous pivot/lead coefficient.  Decide whether
   the radical is really only `{U}`, including hidden constant-field,
   normalizer, Bezout, or serialization denominators.  Any omitted nonunit is
   a theorem blocker.
6. Independent custody: archive/source closure, 111/111 source check,
   rc=0 twice, exact proof-artifact byte agreement, and the claim that stdout
   differs only by three absolute artifact paths.
7. Scope: strongest allowed result is only emptiness on
   `V=H=0,D(U)` inside the fixed source-typed A3 q2-beta family.  V62D alone
   does not cover `U=0`, whole H, whole A3, TD6, SP-2, landing, or JC2.  The
   separate U-zero theorem may be named only as a later union leaf.

Try hard to flip the result through a sign error, beta-dependent pivot,
function-field-versus-localization gap, raw/echelon ancestry gap, omitted
denominator, incomplete source archive, vacuous omission control, or scope
overreach.  Distinguish load-bearing defects from expository/custody nits.

Write the review to
`xmodel/td6-c1-c2-c3-q2-v-h-zero-source-unit-v62d-review-grok-20260825.md`.
End with exactly one verdict token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `FAILED`.
