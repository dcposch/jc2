# Research lane: valuation/completion structure of the wild one-cusp flows

You are a bounded primary research lane, not a reviewer. Attack the
surviving wild one-cusp quartic horn through the valuation and completion
structure of its two non-locally-finite Hamiltonian flows. Do not edit
canonical ledgers, any charged file, or inspect `jc2-lean`.

Read your context from the repository at the recorded basis; start from:

- `xmodel/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md`
  (`PROVISIONAL`, under separate different-model review): on
  `R = C[A,U,Z]/(U^2 - A - A^2 Z)`, `X_H` is locally finite iff LND iff
  `H in C[A]`; a hypothetical quartic Keller pair carries two
  non-locally-finite Hamiltonian flows, and both generic coordinate fibres
  are hyperbolic (neither `A1` nor `C*`);
- the reviewed one-cusp function-pair integration (`2531a89d...`) and
  inverse-Kummer successor (`bcc5148...`) entries in the top of `AUDIT.md`,
  for `mu = d1`, the saturated Orevkov--Chau budget, the companion curve's
  immersive `A1` normalization, and the monogenic index locus
  `u^mu - v^mu = 0`;
- the newest `LIVE STATE` block in `notes.md` for lifecycle states. Label
  every dependence on a provisional parent `PROVISIONAL`.

Known dead shortcuts you must not resurrect: Picard, ML/Derksen, and
ruling-functorial arguments are refuted by the packet's own negative
controls; boundary Fox coloring alone is insufficient; the residual Kummer
class is the inverse class, not an independent one.

Task, in order:

1. Compute the completion of `R` along the cusp point and along the
   boundary divisor, and the induced structure of the two charged
   Hamiltonian derivations there: their valuation growth on a filtration
   you make exact, and what non-local-finiteness forces about their leading
   terms.
2. Extract an exact invariant of a non-locally-finite Hamiltonian flow with
   hyperbolic generic fibre — for instance a lower bound on the growth of
   iterated brackets, a constraint on the flow's Newton polygon at the
   cusp, or an eigenvalue/weight obstruction in the completed local ring —
   and prove it from the packet's hypotheses alone.
3. Test that invariant against the exact degree-four fibre ledger and the
   monogenic index locus: either derive a contradiction closing part of the
   wild mixed/mixed horn, or state exactly the surviving parameter region
   and the single cheapest discriminator for it.
4. If a contradiction closes only a sub-stratum, state the exact stratum
   in the packet's own coordinates, with no monotone or genericity
   extrapolation.

Stop conditions: this is desk-scale exact algebra; if any step needs CAS or
uncertain-duration computation, freeze its design for AWS registration
instead of running it. Never run Singular, msolve, or any CAS on this
machine. Six hours is your hard budget; bank partial exact lemmas rather
than overrunning.

Write one report and no other file:

```text
xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section — so a truncated run still leaves your
partial findings. Keep it under roughly 7,000 words. End its body with a
single standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Include a `charge_basis` declaration only if you assert a
genuinely new exit price with a direct mathematical-source citation;
otherwise omit it entirely.
