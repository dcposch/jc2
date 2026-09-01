# Research lane: ROW-84 — kill the (8,4) survivor with its own geometry

You are the flagship lane on the (8,4) residual row. TORUS-CHECK's
non-transfer note is binding: the (6,4) kill does not transport; the
(8,4) row needs its own §1-style geometry. Its ROW-SWEEP data
(PROVISIONAL, reviewed): sole survivor Delta=(8,4,6,3),
characteristic (4;10,19), (delta_inf, delta_aff, M_inf)=(18,3,22),
three-node attained, degree 8.

charged_input=xmodel/pi1s4-64-torus-check-opus5-20260831.md
charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/pi1s4-64-triple-cover-close-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe  {{LANE_INPUTS}}/pi1s4-64-torus-check-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  {{LANE_INPUTS}}/pi1s4-64-triple-cover-close-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Build the kill chain, adapting the ROW-KILL template, fail closed:

1. **Row normal form.** Derive the (8,4) analogue of ROW-NF: the
   one-place degree-(8,4) parametrizations with delta-sequence
   (8,4,6,3)... careful: gcd tower 8,4 gives g=4 then the 6,3 —
   re-derive the characteristic data ((4;10,19) is charged); obtain
   the family in closed form with its modulus, delta_aff=3 by the
   direct method, and the implicit OCTIC's singularity ledger
   (three nodes + what at infinity? mult 4 germ, semigroup from
   (4;10,19)).
2. **The resolvent target.** A meridian-transposition S_4 rep gives
   the S_3 resolvent; INF-TRIVIAL analogue: derive gamma_inf in
   terms of the tangency generators via the (8,4) discriminant
   census (V = d-1 = 7 vertical tangencies; how many simultaneous?
   the fold structure x = s(t)^2 with deg s = 4 — is there one? —
   or x = u(t)^4? type the actual tower) and determine psi(gamma_inf).
3. **The projective classification input.** If psi descends: normal
   triple covers of P^2 with deg Delta_pi = 8 — Sh12 covers 6; what
   covers 8? Tokunaga T91 (Cardano) gives the general triple-cover
   framework: fetch/hash and extract the branch-divisor constraints
   for normal S_3 (non-cyclic) triple planes at branch degree 8
   (torus-type analogue: F = G_?^3 + G_?^2 shapes with
   deg constraints — derive what Delta_pi = 8 forces); alternatively
   Miranda's classification via the cubic-surface projection
   analogue. If the literature has no degree-8 rigidity, derive the
   constraint directly from the Miranda binary-cubic data with the
   (8,4) infinity germ (the TRIPLE-COVER-CLOSE §4 valuation
   bookkeeping — its infinity-order exhaustion was degree-6-specific;
   redo at degree 8).
4. Verdict: row KILLED (theorem + chain), or typed OPEN at the exact
   missing classification/lemma.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-84-row-kill-opus5-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
