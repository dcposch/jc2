# Hostile different-model review — SECANT-IDEMPOTENT

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer artifacts on top.

Read in full:

- `xmodel/fresh-connection-gate-20260824.md`
- every file under `cases/fresh_connection_20260824/`
- the avenue-32 collision-ideal entry and any locally cited secant/Bezoutian
  prior-art notes in `APPROACHES.md`, `AUDIT.md`, and `xmodel/`

Frozen producer hashes:

- report: `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`
- Python replay: `c55f9f1173aef8a16ecc13c2162ee2fd89bb6916cfaa95f4e9d57b7030105eef`
- Singular replay: `bd5469b4a28f4a84c8f6635f6c95b3dcc6295d94a195d6ad2e36f903edefc891`

Independently rerun both engines and attack exactly:

1. For an arbitrary polynomial `2x2` secant matrix `A` satisfying
   `A*(x-u,y-v)^T=(P(x,y)-P(u,v),Q(x,y)-Q(u,v))^T`, check the adjugate
   identities modulo the collision ideal.
2. Check that every such `A` restricts to `J_F` on the diagonal, even when
   it is not the telescoping choice. For constant Jacobian `c!=0`, verify
   that `e=c^-1 det A` obeys `e*J_delta=0`, `1-e in J_delta`, and `e^2=e`
   in the self-fiber-product ring.
3. Audit the uniqueness statement at its exact scope. State the precise
   properties under which the diagonal idempotent is unique; reject any
   stronger claim if arbitrary idempotents could exist.
4. Prove or refute scheme-theoretically
   `I:(x-u,y-v)^infinity = I+(det A)`. Check both containments, ideal
   saturation rather than element saturation, nilpotents/embedded diagonal
   structure, and the product decomposition. Verify `eC` really is the
   diagonal quotient.
5. Check convention independence: two polynomial secant matrices produce
   the same idempotent class modulo `I`, hence the same three-generator
   ideal.
6. Independently verify the characteristic-zero automorphism controls, the
   characteristic-3 Artin--Schreier collision, and the non-Keller rejection.
   Do not use producer verdict strings as evidence.
7. Scope and priority: the theorem removes saturation computationally but
   `I+(det A)=(1)` for every characteristic-zero Keller map is exactly the
   injectivity endpoint. It gives no finite degree/support bound and no JC2
   implication. Check whether the identity is standard Bezoutian/secant
   algebra; no literature novelty should be promoted absent a primary
   source.

Identify the smallest failing hypothesis or overclaim. Do not edit producer
or canonical files and do not start a generic collision search.

Write exactly one file:

`xmodel/secant-idempotent-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
replay/hashes, the exact saturation proof, priority caveats, scope exclusions,
and promotion advice for theorem versus software interface.
