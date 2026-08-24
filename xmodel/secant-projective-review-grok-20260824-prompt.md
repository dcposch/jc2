# Hostile different-model review — SECANT PROJECTIVE-CONNECTEDNESS

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer artifacts on top.

Read in full:

- `xmodel/secant-projective-connectedness-gate-20260824.md`
- every file under `cases/secant_projective_20260824/`
- the provisional parent `xmodel/fresh-connection-gate-20260824.md`
- the avenue-7, avenue-31, and avenue-32 entries in `APPROACHES.md`

Frozen producer hashes:

- report: `cabfa347` (verify and record the full SHA-256 independently)
- Python replay: `76f4ae48a2f7382a3b3fd0a11e9c99961f30b2e356dbd5617692fd08cfc82494`
- Singular replay: `ca5cd4ce255c84d9f046e70dbc1eefba4dbad70f43ad4c01e2f6513077bedefd`

Independently rerun both engines and attack exactly:

1. Verify the projective setup: the honest closure of the affine collision
   scheme is obtained by `Z`-saturation, and explain why connectedness of the
   naive two-equation complete intersection need not pass to that closure.
2. Recompute the identity and two-step tame automorphism controls. Check the
   two displayed homogeneous identities, both pure-infinity surfaces, the
   claimed saturation ideals and minimal/exhibited exponents, and the
   saturation of the secant-determinant off ideal.
3. Recompute the characteristic-three Artin--Schreier example. Check
   saturation, exact primary/intersection decomposition, the scheme-theoretic
   diagonal/off meeting `(X-U,Y-V,Z^2)`, and that the off component contains a
   marked affine collision.
4. Check the characteristic-zero rejection control and the precise scope of
   the statement that constant Jacobian removes affine diagonal/off contact
   but not boundary contact. Flag any hidden smoothness, reducedness, or
   projective-purity assumption.
5. Decide whether the producer's verdict
   `PROJECTIVE-CONNECTEDNESS=COSTUME / NEED-Z-SATURATED-INFINITY-DATUM` follows
   at the stated scope. In particular, distinguish a falsified general
   connectedness shortcut from any stronger claim about named Newton families
   or all possible compactifications.
6. Audit dependency hygiene: the parent SECANT-IDEMPOTENT theorem is still
   provisional while its separate review runs. Determine which projective
   calculations stand independently and ensure nothing here promotes the
   parent or implies JC2.

Identify the smallest failing hypothesis or overclaim. Do not edit producer
or canonical files and do not launch a generic projective search.

Write exactly one file:

`xmodel/secant-projective-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, replay outputs, exact algebra, scope exclusions, and promotion
advice for the negative gate and its missing infinity datum.
