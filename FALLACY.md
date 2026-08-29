# FALLACY.md: campaign reasoning guardrail

Check these before promoting a claim.

- **Flag/place/series.** Anti-pattern: one cv flag means one place/series, or
  every series split creates a flag. Safe replacement: distinguish all three;
  separate strict-below from at-level parting, and record within-place
  shedding by denominator jump.
- **Per-ray/exit-set charge.** Anti-pattern: charge every displayed ray, sheet,
  or incoming edge. Safe replacement: form the typed first-separation exit set,
  prove its flags distinct, and count each flag once.
- **Pole/interior.** Anti-pattern: use a pole identity or purity law at an
  interior/terminal vertex. Safe replacement: state the vertex class and verify
  every source hypothesis.
- **Floor/attainment.** Anti-pattern: call a lower bound or model price exact.
  Safe replacement: label a floor; claim equality only by theorem or a witness
  satisfying every omitted term.
- **`sat()` wrapping.** Anti-pattern: treat a CAS saturation return as an ideal.
  Safe replacement: extract the ideal component, assert its ring, and test
  positive and negative controls.
- **Raw remainder degree.** Anti-pattern: read degree before reduction or a
  parameter-leader split. Safe replacement: normal-form in the declared
  quotient/localization, branch on vanished leaders, and handle zero.
- **Variable name/ring map.** Anti-pattern: same names in two rings mean the same
  element. Safe replacement: declare the map, generator order, coefficient field,
  and image checks.
- **Prime label/derivative.** Anti-pattern: read a prime mark as differentiation.
  Safe replacement: keep it as a label unless the source defines a derivative;
  rename ambiguous symbols.

If no safe replacement exists, return typed `OPEN`; do not fill the gap by cap
or analogy.

For an exit claim, add one machine line:
`charge_basis={"delta":"3/2","branch":"q>=2","flag_count":1,"citation":"path:line"}`;
branches: `q=1-exact`, `q>=2`, `multi-flag`.
This declares, never infers, a basis.
