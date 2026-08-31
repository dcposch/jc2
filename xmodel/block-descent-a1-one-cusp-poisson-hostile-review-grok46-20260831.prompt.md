# Hostile review assignment: one-cusp Poisson locally-finite obstruction

Act as an independent hostile mathematical referee. Review exactly the
one-cusp Poisson/locally-finite packet named below. Its charged claims, on
`R = C[A,U,Z]/(U^2 - A - A^2 Z)`: the Hamiltonian field `X_H` is locally
finite iff it is locally nilpotent iff `H in C[A]`; hence a hypothetical
quartic Keller pair induces two non-locally-finite Hamiltonian flows; and
via cofinite image plus the exact degree-four fibre ledger, both generic
coordinate fibres are neither `A1` nor `C*`. It claims no horn exclusion.
Do not promote it, edit any charged file, edit canonical ledgers, or
inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md.artifact.json

Your charged inputs are frozen, read-only copies in `{{LANE_INPUTS}}`. Read
them there, not from the live repository. Before mathematical reading,
reproduce these SHA-256 hashes against the frozen copies:

```text
cd27b7f6687103fae0fc4e5fe19772e0f8e62939d73a655ebf04e57905ddba05  {{LANE_INPUTS}}/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
a255cf39d6b3fb07c5a4c4e494921b7fa795e7881c7b21c4dccdcd2692a87a94  {{LANE_INPUTS}}/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md.artifact.json
```

If any hash fails, stop and report the mismatch instead of reviewing.

Independently test:

1. the ring presentation `R = C[A,U,Z]/(U^2 - A - A^2 Z)` and every claimed
   geometric property of `Spec R` the packet uses (smoothness or its
   absence, normality, the ruling, units);
2. the Poisson/Hamiltonian construction itself: that the claimed bracket is
   a genuine Poisson bracket on `R` and `X_H` is the asserted derivation;
3. both directions of `X_H` locally finite iff locally nilpotent iff
   `H in C[A]` — hunt hardest for a locally finite but non-nilpotent
   semisimple case the equivalence might miss;
4. the transfer to a hypothetical quartic Keller pair: why exactly two flows
   are charged, why each is Hamiltonian for the packet's bracket, and why
   non-membership in `C[A]` follows;
5. the cofinite-image argument and the exact degree-four fibre ledger, and
   the step excluding `A1` and `C*` generic coordinate fibres;
6. the packet's negative controls (the claimed failures of Picard,
   ML/Derksen, and ruling-functorial shortcuts) — verify each control
   computation and that the packet's own argument does not secretly rely on
   the shortcut it disproves;
7. the declared scope limits: nothing proves arbitrary Hamiltonian slices
   locally finite, preserves the ruling under every etale selfmap, or
   closes the wild mixed/mixed hyperbolic horn — flag any wording that
   overreaches this.

Actively seek a wrong Jacobi identity, a localization or completion step
performed in the wrong ring, a semisimple locally-finite counterexample, a
fibre count valid only for special coefficients, or a hidden genericity
assumption in the ledger. State the weakest exact hypotheses, any
correction and blast radius, and one best next falsification test. Give a
per-claim verdict from `CONFIRMED`, `REFUTED`, `GAP`, with the attack
shown.

Computation rules: short exact desk arithmetic and exact symbolic checks by
hand only. Never run Singular, msolve, any CAS, or any computation of
uncertain duration or memory on this machine; if one seems necessary,
record exactly what is blocked and why instead of running it.

Write one report and no other file:

```text
xmodel/block-descent-a1-one-cusp-poisson-hostile-review-grok46-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 6,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Do not include a `charge_basis` declaration: this review
asserts no new exit price.
