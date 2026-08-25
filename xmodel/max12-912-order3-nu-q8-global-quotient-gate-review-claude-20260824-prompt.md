# Hostile review — corrected Q8 global quotient gate

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`.  Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable.  Read in full:

- `xmodel/max12-912-order3-nu-q8-global-quotient-gate-20260824.md`;
- every file in
  `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/`;
- only the frozen parents pinned by that manifest.

Charged hashes:

```text
report          2102e5d730af7d9bd4a434a99ea9b7213cdf08016becd0e49061f5210ec0feaa
manifest        3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4
freeze          c34fff2b838ca4803872b709857ae7becb1751a7e1ce261c9fa8c7e6d8b46c97
replay          f0f52954bed71b65b9219fd497f7ea2bbe6652144c463ca06f03391b87957fdd
replay payload  d05eeb86d8c11b6463f25b18bff1a59b736a924bd3fcf619aaf23404f4e764a5
```

Run the manifest check and the full replay.  Inspect the replay rather than
trusting PASS, and independently attack:

1. The exact parity quotient: derive the involution, substitution
   `t=x0`, `q_c=t*c`, `x2=t*d2`, `x4=t*d4`, `w=t^2`; check that dividing the
   odd rows by `t` is reversible on the charged punctured branch and that the
   stated six equations and outputs `n=r6/p^9`, `q=r8/p^10` are source-honest.
2. The selected-component dimension claim.  Verify that it comes only from
   the reviewed rank-six formal IFT at each Q8 contact plus algebraization of
   that completed local branch.  Reject any inference of a characteristic-zero
   upper bound, reducedness, irreducibility, or whole-open dimension from the
   two 607-element modular bases.
3. The exact `w^5` Hensel calculation over `Q[v]/(Q8)`: check the coefficient
   field, invertibility at every step, substitution residuals, and agreement
   with the frozen terminal jet.  Look for a zero divisor or an illicit choice
   of one root instead of the full degree-eight algebra.
4. Every bounded nonrelation claim.  Check the Padé ranges and independently
   audit why full column rank at a good finite prime rules out a rational
   relation in each precisely stated box.  Confirm there is no claim outside
   those finite boxes.
5. The scale reconstruction and terminal descent:
   `pi=p^9=nu/n`, `S=r8^9=nu^10 q^9/n^10=nu^10 Z`, and
   `nu^10 h^3 (Z')^9=j^9 Z^8`.  Search specifically for a missing derivative
   factor, chosen ninth root, hidden vanishing denominator, or illicit import
   of the parity-only identity `r6=p^9 R6(v)`.
6. Scope and boundary accounting: distinguish a formal coefficient-fibre
   branch from a global trajectory; charge `w=0`, `x5=0`, `x3-2*x5=0`, `p=0`,
   projective endpoints, both Taylor families, and the still-missing global
   quotient equation/normalization/genus analysis.

State the smallest false identity or missing hypothesis if one exists.  Give
the exact promotable sentence and its strict scope.  Write exactly
`xmodel/max12-912-order3-nu-q8-global-quotient-gate-review-claude-20260824.md`.
Do not edit any other file.  End with exactly one verdict: `CONFIRMED`, `GAP`,
or `REFUTED`.
