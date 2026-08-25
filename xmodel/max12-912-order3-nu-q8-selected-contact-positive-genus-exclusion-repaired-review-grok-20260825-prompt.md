Act as an independent hostile algebraic-geometry referee.  The producer is
GPT-family; you are the required different-model reviewer.  Read in full:

- `xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-20260825.md`;
- its frozen case manifest and every parent report/review named by it;
- especially the now-CONFIRMED positive-genus review
  `xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-review-grok-20260825.md`.

This is a concise successor audit after a first diagnostic review returned
`CONFIRMED_WITH_REPAIRS`.  Verify that the repaired report actually closes
all seven items: finite DVR extension before identifying the generic curve
with `P1`; existence of a component dominating the special curve via a
proper-model/divisorial-valuation argument; geometric rather than ground-field
Luroth after finite constant extension; the full 8x8 unit Jacobian at the
winning contact as the uniformizer/separability certificate; Galois
propagation only among characteristic-zero components; semistable/arithmetic
genus only as a remark; and fibre-completion precision for `K[[w]]` and
`k[[w]]`.

Then attack the load-bearing chain once more: common whole-source `R[[w]]`,
zero closure ideal and unique special branch at the winning full contact,
identity with an `H`-dominating component, positive genus upstairs, ruled
residue/geometric-Luroth obstruction to a rational generic component, and
primitive all-eight/eight-singleton propagation.  Check that the separately
reviewed point count is now attached and that no inference escapes the
selected `k=mu=0,nu!=0` corrected-Q8 contact leaf.

List only defects that affect the repaired theorem.  End with exactly one
verdict token on its own line: `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or
`BLOCKED`.

Do not use Bash, CAS, network access, or write/edit any file; disclose that
limitation.  Return a self-contained review on stdout, at most 3,000 words.
