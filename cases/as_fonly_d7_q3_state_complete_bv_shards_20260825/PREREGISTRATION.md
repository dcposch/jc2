# 27-way first-carry shards for the state-complete BV gate

For each displayed parent, independently derive the exact eight-column
`/27` source cone and its 27 accepted assignments from V1 SHA
`cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd`.
Pin one assignment into the already emitted monolithic state-complete QF_BV
formula and solve all 27 disjoint shards.  The ordered union is exactly the
monolith because the eight named raw variables are explicit formula inputs.

SAT requires the same independent literal-integer replay as the monolith.
UNSAT remains diagnostic until certificate-checked.  Preserve formula,
assignment, pinned-formula, solver/model, replay, and ordered-coverage hashes.
Run on AWS only.
