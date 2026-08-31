# Research lane: NONMONOGENIC — empty the class (7.1), or bypass on four coefficients

You are a bounded primary research lane on the last algebraic gap of
the triple-cover route (charged TRIPLE-COVER-CLOSE §7): the class
(7.1) of non-monogenic Miranda resolvents compatible with the (6,4)
row, and the OPEN four-coefficient bypass (its §3). Either result
completes the monogenic no-go into a UNIFORM kill of the row.

charged_input=xmodel/pi1s4-64-triple-cover-close-sol56-20260831.md
charged_input=xmodel/pi1s4-64-triple-cover-r2-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  {{LANE_INPUTS}}/pi1s4-64-triple-cover-close-sol56-20260831.md
c99ffc7f64562ac08e81aa7e927dc04e8c0765182d99db9fdc9f10351772cf9f  {{LANE_INPUTS}}/pi1s4-64-triple-cover-r2-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Routes, in order:

1. **Four-coefficient bypass, properly.** The charged §3 explains why
   the naive bypass fails; engage its exact failure point. The
   Miranda datum is a binary cubic I(S,T) over C[x,y] with
   disc(I) = -27 kappa F; the row constraints are (a) the infinity
   germ of V(F): one place, mult 2, the (2,15) Puiseux type; (b)
   exactly three affine nodes. Derive the infinity-order analysis
   DIRECTLY for the four-coefficient discriminant
   D = b^2c^2 - 3a^2d^2 + 4a^3c + 4bd^3 - 6abcd (weighted orders of
   the four coefficients at the place at infinity; which order
   vectors give a (2,15) germ of D? — the charged depressed-form
   analysis got orders {2,3,4,6} vs required 5; run the same
   valuation bookkeeping in four variables, using that the binary
   cubic's GL_2-invariant structure constrains the achievable
   discriminant germs; if the full four-coefficient family still
   cannot achieve order 5, the bypass closes and monogenicity is
   unnecessary).
2. **Emptiness of (7.1) directly.** The obstruction to monogenicity
   is the unit-representation condition (charged §2: the binary
   cubic represents a unit iff the algebra has a power basis).
   For a cubic over C[x,y] with disc = -27 kappa F, F our sextic:
   determine whether I(S,T) = 1 must have a solution — this is a
   polynomial unit-representation problem over a polynomial ring
   (C[x,y] points, not field points); use the structure: at every
   point of C^2 - F=0 the fibre cubic is separable; the Tschirnhausen
   bundle is trivial; obstruction lives in... analyze the universal
   family or produce a countermodel (a binary cubic over C[x,y] with
   squarefree discriminant representing no unit) — a countermodel
   would keep (7.1) potentially nonempty and the route stays
   conditional; type honestly.
3. Assemble: uniform kill (theorem), or the exact surviving
   subclass with all constraints listed.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-nonmonogenic-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
