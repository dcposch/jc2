# Bounded source-delta audit — `what-social-construct/jacobian-collision-geometry`

Work in `/Users/dc/code/math/jc2`.  A watched public repository formerly named
`what-social-construct/collision-ideals` was renamed/reframed as
`what-social-construct/jacobian-collision-geometry`; current public HEAD is
`9a3d6caa7fa4` (2026-08-24T09:35:06Z).  It added a standalone planar Paper II
and substantial boundary/conductor exposition.  This is a source audit, not a
request to prove JC2.

Clone the public repository at exactly that SHA into an untracked temporary
directory outside this repository.  Read its README, `paper/paper2.tex`,
`SEMANTIC-PARITY.md`, theorem inventory, and the Lean files supporting every
claim you discuss.  In this repository read:

- approach 32 and the current overlay in `APPROACHES.md`;
- `xmodel/secant-idempotent-review-grok-20260824.md`;
- `xmodel/websweep-2026-08-16.md` section A2;
- relevant collision/boundary entries in `AUDIT.md` and `PROGRESS.md`.

Answer precisely:

1. What unconditional mathematical and Lean-certified content is genuinely
   new since the watched Aug-14 state, rather than a rename, manuscript split,
   equivalent formulation, standard literature interface, or explicit
   hypothesis?
2. Does the current repository prove any universal implication that narrows
   unrestricted JC2?  Track `PlanarBoundaryCoherence`,
   `PlanarRamificationRigidity`, moving-sheet coverage, boundary separation,
   no-hidden-inertia, conductor landing, local-cohomology/DVR pole, and every
   bridge/interface.  Identify the first unproved arrow and say whether it is
   equivalent to all of JC2 or strictly weaker.
3. Crosswalk its secant/colon/collision decomposition with our reviewed result
   `I:Delta=I:Delta^infinity=I+(det A)`.  State exact duplication versus any
   stronger theorem, with hypotheses.
4. Audit the claimed finite Tate/conductor reduction and first-jet denominator
   ideal.  Is there a concrete, source-defined containment or computable
   invariant that can be tested on one of our named finite clients (maximum-12
   order-three fibre, TD6 center family, or AS branch) without assuming the
   missing universal theorem?  If yes, give the cheapest exact experiment and
   required data.  If no, identify the circular or absent landing map.
5. Check for theorem/README/manuscript semantic mismatch and for axioms,
   `sorry`, supplied structures, or proposition-valued interfaces that could
   make a conditional route look proved.

Do not edit either repository, canonical files, producer artifacts, prompts,
logs, or run records.  Do not launch AWS.  Write exactly:

`xmodel/websweep-20260824T2041Z-collision-geometry-delta-audit-codex.md`

Give an overall verdict from `NO_ACTIONABLE_DELTA`, `REUSABLE_SCOPED_DELTA`,
`ACTIONABLE_NEW_CLIENT`, or `UNSOUND_SCOPE`; include source SHA, exact file/
theorem references, the smallest missing implication, and one allocation
recommendation.  Do not claim independence or correctness merely from Lean
acceptance.
